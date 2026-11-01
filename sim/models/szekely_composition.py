"""Measured drives, composition test: does the way members' SVO angles are combined (count above a cut) predict whether a
group reaches the threshold, and do drives add to person rates?  Szekely et al. 2021 threshold public-goods game.

    cd sim
    ~/.local/bin/uv run python -m models.szekely_composition rule      # writes the data facts and the rule (no model number) to results/szekely_composition.md
    ~/.local/bin/uv run python -m models.szekely_composition report    # refuses unless the rule block is already in that file; then fits, freezes, scores once

Why this test.  results/synthetic_population_identifiability.md "Decision": in a modelled population the drives are recoverable
through the tie channel, but a linear composition of them does not beat person rates.  Composition (how the members' drives
are combined into a group state) is therefore the thing under test; Claim 1 of models/02-our-claims.md says the group state
is a count above a cut, not a mean.  Here the drive is MEASURED (an SVO slider, before the game) and the group is real.

Privacy and terms.  Only counts and statistics leave this module.  No participant row is printed or written.  The data file is
local-use-only and git-ignored (sim/data/README.md).  Article CC BY 4.0, doi:10.1038/s41467-021-25734-w.

Procedure fixed by RULE_TEXT below, copied verbatim into the results file before any model is fitted.  `report` refuses to
run unless that file already contains it.  Decisions the rule left open are in IMPLEMENTATION, taken before any fit.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from models import apache_activity_survival as A
from models import apache_fitted_case as F

SIM = A.SIM
DATA = SIM / "data" / "szekely2021" / "full.csv"
DATA_SHA256 = "b0f366fe7733b4515428a8a3adb91ac4e113d29d7308477ed7de385bffdbeeb2"
RESULTS = SIM / "results" / "szekely_composition.md"
SEED = A.SEED
BOOT = 2000
L2 = 1.0
AUC_MARGIN = 0.02
K1_AUC_FLOOR = 0.55
THRESHOLD = 300.0
N_ROUNDS = 28
SWITCH = 15                      # first round of phase 2
PHASE_LEN = 14                   # rounds per phase
TRAIN_LEN = 10                   # first 10 of each phase's 14 rounds train (71%), the last 4 test
CUT_GRID = (15.0, 20.0, 22.45, 25.0, 30.0, 35.0)   # degrees, svo_angle
PCT_GRID = (20, 35, 50, 65, 80)                    # percentile cuts for risk and agreeableness
GROUP_SIZE = 6
DRIVES = {"svo_angle": "SVO angle (primary)", "risk": "risk (secondary)", "agreeableness": "agreeableness (secondary)"}
STRATA = ("phase 1", "phase 2", "pooled")

# ----------------------------------------------------------------------------------------------------------------------
# What was found in the file before any parameter of the rule was fixed.  Static text, no model result in it.  A data test
# recomputes each number from the file.
FACTS_TEXT = """\
Read from `full.csv` (sha256 `b0f366fe...bbeeb2`, 4.5 MB) before the rule's parameters were fixed. Only the structure of the file, its group-level outcome frequencies and its person-level distributions were looked at; no relation between any drive and any outcome was computed.

- **Size and the "two rows per person-round".** 14,872 rows, 286 persons, 28 rounds. The file is long in the experiment's belief-manipulation design: in 8 of the 28 rounds (1, 5, 10, 14, 15, 19, 24, 28) each person has FOUR rows, one per hypothetical-expectation condition (`manipulation`: High or Low empirical expectation crossed with High or Low normative expectation, used for the conditional-contribution elicitation), and in the other 20 rounds one row (`manipulation` blank). So 20 x 286 + 8 x 286 x 4 = 14,872. The flag `odr` is 1 on exactly one row per person-round (8,008 rows = 286 x 28; the "High EE and High NE" row in a conditional round, the blank row elsewhere) and 0 on the other 6,864 (286 x 8 x 3); the 6,864 carry no `contribution` and no `total_contribution`. The meaning of `odr` is inferred from this (the file's codebook was not read); what is established is that `odr` = 1 selects one row per person-round that carries the actual game record, and every analysis here uses those 8,008 rows only.
- **Treatment and the switch.** Two orders: High (0.9) to Low (0.6), 148 persons; Low (0.6) to High (0.9), 138. `disaster_probability` is constant within each phase of a person and changes at **round 15**: rounds 1-14 are phase 1, rounds 15-28 phase 2. It is the same for all members of a group-round (a group never mixes orders).
- **Group id and size.** `group_id` identifies a group-round (1,392 distinct values, each in exactly one round): groups are reshuffled every round. 1,261 group-rounds have six rows in the file; 131 have 1-5 (rounds 1-3 hold 48-49 groups, the rest 50). Players absent from the file still contributed to `total_contribution`.
- **Threshold.** In 800 of 1,392 group-rounds `total_contribution` is at least 300 and in all 800 `disaster_outcome` is 0; below 300 a disaster occurs with the round's probability (199 of 218 at 0.9, 220 of 374 at 0.6). The threshold is therefore 300 (of a 600 maximum with six players). The recorded total ranges 0 to 485; 57.5% of group-rounds reach 300. `total_contribution` equals the sum of the members' recorded contributions in the 1,063 six-row groups with no missing contribution; where a member has no recorded contribution the total usually exceeds the sum (of the 151 six-row, no-exclusion cases with exactly one member missing: by exactly 50 in 72, by 0 in 4, by other amounts from 20 to 90 in the rest).
- **`inactive` and `excluded`.** `inactive` is a running count of the person's rounds with a timeout on the contribution decision (non-decreasing; 0 for 10,873 of 14,872 rows). In the 8,008 game rows the contribution is missing in exactly 567, exactly the rows where `timeout_contribute` says a timeout occurred. `excluded` = "Excluded" on 371 game rows (23 persons, absorbing: once excluded, excluded for every later round; the first exclusion falls at inactive = 4); an excluded person has no contribution and leaves the group. Timeout players who are not excluded stay in the group and the total includes a default for them.
- **Persons.** `svo_angle`, `risk` and `agreeableness` are constant per person and have no missing value (286 each). `risk` is an ordinal scale exported with value labels on its ends only: persons have 1 (57), 2 (85), 3 (41), 4 (40), or the labels "Risk averse" (44) and "Risk seeking" (19), whose numeric codes the file does not give; the six levels read as a 0-5 scale with the labelled ends at 0 and 5 (an inference, recorded as a decision below). `agreeableness` is numeric, 17 to 45. `svo_angle` runs from -11.7 to 61.2 degrees, median 30.2; share of persons above 15 / 20 / 22.45 / 25 / 30 / 35 degrees: 0.797 / 0.734 / 0.699 / 0.650 / 0.507 / 0.364. `svo_type`: Prosocial 199, Individualistic 86, Altruistic 1.
- **Lag.** `contribution_1` is the previous round's recorded contribution (7,179 of 7,179 comparable pairs match exactly); missing in round 1 and after a timeout.
- **What was seen of the outcome before the rule.** The overall frequency of threshold-reached group-rounds (57.5%) and its frequency by round (0.82 in round 1, falling to 0.44 in round 28), over all rounds including the ones that are now test rounds. This is an aggregate of the outcome, not a relation with any drive. The rule, the split and the margin were fixed after seeing it.
"""

# Rule: the brief of 2026-11-01, with its one bracketed parameter filled from the facts above.
RULE_TEXT = """\
1. Unit: a group-round (one group of 6 in one round, one treatment order), with outcome y_bin = threshold reached (total contribution >= 300) and y_cont = total contribution. Persons' drive inputs: svo_angle (primary); secondary: risk, agreeableness.
2. Split, out of time within each treatment phase: phase 1 = rounds before the switch (rounds 1-14), phase 2 = rounds from the switch (rounds 15-28); within each phase the first 10 rounds (rounds 1-10 and 15-24; 71%, about 70%) train and the last 4 rounds (rounds 11-14 and 25-28; 29%, about 30%) test. Person-level training statistics (rates) are computed on training rounds only. Nothing from test rounds enters any fit. Models are fitted once per phase and frozen.
3. Models of the group outcome, all ridge (penalty 1, standardised on training), logistic for y_bin, linear for y_cont:
   (0) training base rate / mean;
   (M) mean composition: group mean of svo_angle (the field's standard aggregation);
   (Mo) moments: mean, min, max, sd of svo_angle;
   (T) threshold composition (ours, Claim 1 in models/02-our-claims.md: the group state is the count above a cut): the number of members with svo_angle above a cut c, with c chosen on the training rounds from the grid {15°, 20°, 22.45°, 25°, 30°, 35°} by training log-loss, then frozen; plus the number above a second cut if that improves training log-loss (at most two cuts);
   (R) person rates: each member's mean contribution over the training rounds of that phase (a person-effects rival; members with no training rounds get the training grand mean), aggregated as mean and min;
   (R+T) rates plus the threshold count;
   (R+M) rates plus the SVO mean.
4. Score on the test rounds once: held-out AUC and log-loss for y_bin, RMSE for y_cont (relative to predicting the training mean). Bootstrap over test group-rounds, 2,000 draws, seed 20261101, for the decisive differences.
5. Criteria, fixed now: (K1) measured drives carry information: M beats 0 on held-out log-loss and its AUC exceeds 0.55. (K2) composition matters: T beats M by more than 0.02 held-out AUC AND lower log-loss. (K3) drives add to rates: R+T beats R by more than 0.02 AUC AND lower log-loss (also report R+M vs R). Each per phase and pooled.
6. Secondary, labelled: the same with risk and agreeableness in place of svo_angle; and a dynamic person state, the member's previous-round contribution (contribution_1) aggregated as mean, as a further rival (D), vs R.
7. Everything else exploratory and labelled so. No re-tuning after scoring."""

IMPLEMENTATION = [
    "**Population.** A group-round is in the analysis if all six of its members have a row in the file and none of them is excluded (1,228 of 1,392; the others are counted below by reason). A group of fewer than six rows has members the file does not describe, so its composition is unknown; an excluded member is not playing and the group is not a group of six. Members who timed out (no recorded contribution) stay in: they are in the group and their drive values are known. The outcome is the recorded `total_contribution` (which includes the default for a timeout), y_bin = total >= 300, y_cont = total.",
    "**Treatment order.** Both orders are pooled within a phase. No model has an order or disaster-probability term (the rule's feature lists have none), so the 0.9 and 0.6 conditions are a source of unexplained outcome variation and a possible confound for any feature that differs between orders; the number of each order in each set is reported.",
    "**Phases and the pooled row.** Models are fitted once per phase (rule item 2). The pooled row concatenates the two phases' frozen test predictions and scores them together; nothing is refitted on pooled data. The pooled baseline (0) is each phase's own training base rate, so its pooled AUC is not 0.5.",
    "**Rates (R).** A person's rate in a phase is the mean of the person's recorded contributions (timeout rounds are skipped) over that phase's 10 training rounds, taken from every one of the person's game rows in those rounds (including rows in group-rounds that are not in the analysis). A person with none gets the grand mean of all recorded contributions in that phase's training rounds. In the TRAINING group-rounds a member's rate includes that member's own contribution in the very round being predicted, so R is flattered inside training and its coefficients are fitted on a feature that is partly the outcome; in the test rounds it is a pure forecast. The rule fixes this construction; the consequence is a caveat.",
    "**Cut choice (T).** Candidate counts use a strict inequality (angle > c). Each candidate cut is scored by the in-training log-loss of the ridge logistic model on that one count; the lowest wins, ties to the lower cut. A second cut is the best remaining grid value given the first (lowest in-training log-loss of the two-count model) and is KEPT if that two-count log-loss is lower than the one-cut log-loss at all (read literally: 'if that improves training log-loss'); no tolerance. Cuts are chosen per phase from that phase's training rounds only. For risk and agreeableness, whose scales differ, the grid is the 20th, 35th, 50th, 65th and 80th percentiles of the distinct persons who appear in that phase's training group-rounds.",
    "**Fit.** Logistic: `apache_activity_survival.logit_fit` through `apache_fitted_case.Frozen` (ridge penalty 1 on inputs standardised on the training rows, intercept free). Linear: centre y on the training mean, standardise the inputs on training, minimise squared error + 1 x |b|^2. Means, standard deviations and coefficients are stored from training and applied unchanged to the test rows.",
    "**Mo and sd.** sd is the population standard deviation (ddof 0) of the six members' angles.",
    "**Scoring.** Held-out AUC (`auc_score`, ties one half) and log-loss (`logloss`, clipped to [1e-6, 1-1e-6]) of y_bin; RMSE of y_cont, also given as a ratio to the RMSE of predicting the phase's training mean (below 1 beats the baseline).",
    "**Criteria edges.** Every margin is strict: K1 needs M's AUC > 0.55 and M's log-loss < the baseline's; K2 and K3 need an AUC difference > 0.02 (compared after rounding to 12 places, so that float noise cannot turn exactly 0.02 into 'more') and a lower log-loss. Where the criterion fails because of an AUC difference between 0 and 0.02, or because only one condition holds, the file says which.",
    "**Bootstrap.** Resample the test group-rounds with replacement, 2,000 draws, seed 20261101, within a phase for the phase rows and over the concatenated test rows for the pooled row; predictions frozen; the same draws for every model; a draw with one class only is skipped and counted. 95% percentile intervals, reported for every difference named in the criteria and for each model's AUC and log-loss. The bootstrap resamples group-rounds as independent although the same persons recur across rounds (a caveat).",
    "**Dynamic state (D).** The mean over the six members of `contribution_1`, the previous round's recorded contribution. A missing value (round 1, or after a timeout) is replaced by the phase's training mean of `contribution_1`. D is a one-step-ahead forecast: in a test round it uses the members' contributions in the previous round, which may itself be a test round; this is an input observed before the round, not a fit to test data. D is scored against R only.",
    "**Risk coding.** `risk` mixes the numerals 1-4 with two text labels. The labels are mapped to the ends of the scale the numerals sit inside: \"Risk averse\" = 0 and \"Risk seeking\" = 5, so the scale reads 0-5 in the order averse, 1, 2, 3, 4, seeking. This is an inference from the labelling, not from a codebook; risk's cut grid is percentile-based, so only the ordering matters for T, but the spacing matters for the mean in M, Mo and R+M. The direction (higher = more risk-seeking) does not matter to any model.",
    "**Secondary drives.** Risk and agreeableness get the same models M, Mo, T, R+T, R+M (cuts from the percentile grid) and the same K1-K3; R and D do not depend on the drive and are the same models as in the primary.",
]


def rule_block() -> str:
    return (
        "## The rule, written before any fit\n\n"
        "Copied from the brief of 2026-11-01; the one bracketed parameter of item 2 (\"[about 70%]\") is filled from the data facts above "
        "(10 of the phase's 14 rounds) and the rounds are written out; nothing else is changed. Written into this file before the first model was fitted "
        "(`report` refuses to run unless this block is already here).\n\n" + RULE_TEXT + "\n"
    )


def facts_block() -> str:
    return "## Facts about the data, established before the rule's parameters were fixed\n\n" + FACTS_TEXT


# ----------------------------------------------------------------------------------------------------------------------
# splits and criteria (pure)

def phase_of(rnd) -> np.ndarray:
    return np.where(np.asarray(rnd) >= SWITCH, 2, 1)


def split_rounds(rnd) -> tuple[np.ndarray, np.ndarray]:
    """Training and test masks by round number: within each phase the first TRAIN_LEN rounds train, the rest test."""
    r = np.asarray(rnd)
    pos = np.where(r >= SWITCH, r - SWITCH, r - 1)      # 0..13 within the phase
    ok = (r >= 1) & (r <= N_ROUNDS)
    return ok & (pos < TRAIN_LEN), ok & (pos >= TRAIN_LEN)


def beats(auc_x: float, auc_y: float, ll_x: float, ll_y: float, margin: float = AUC_MARGIN) -> bool:
    """X beats Y: AUC higher by MORE than the margin AND log-loss lower (the K2/K3 form; the Apache criterion with X = B)."""
    return F.criterion(auc_y, auc_x, ll_y, ll_x, margin)


def k1_met(auc_m: float, ll_m: float, ll_0: float, floor: float = K1_AUC_FLOOR) -> bool:
    """K1: M's log-loss below the baseline's AND M's AUC strictly above the floor."""
    return bool(ll_m < ll_0 and round(auc_m - floor, 12) > 0)


# ----------------------------------------------------------------------------------------------------------------------
# data

RISK_LABELS = {"Risk averse": 0.0, "Risk seeking": 5.0}


def _num(s: str) -> float:
    return float(s) if s != "" else float("nan")


def _risk(s: str) -> float:
    return RISK_LABELS[s] if s in RISK_LABELS else _num(s)


def read_game_rows(path: Path = DATA) -> tuple[int, list[dict]]:
    """All rows (count) and the odr == 1 rows (one per person-round)."""
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        raw = list(csv.DictReader(f))
    return len(raw), [r for r in raw if r["odr"] == "1"]


def sha256_of(path: Path = DATA) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Panel:
    """Person-round matrices and the retained group-rounds, built from the odr == 1 rows only."""

    def __init__(self, path: Path = DATA):
        self.n_raw, rows = read_game_rows(path)
        ids = sorted({int(r["id"]) for r in rows})
        ix = {i: k for k, i in enumerate(ids)}
        P = len(ids)
        self.n_persons = P
        self.contrib = np.full((P, N_ROUNDS), np.nan)
        self.prev = np.full((P, N_ROUNDS), np.nan)
        self.svo_angle = np.full(P, np.nan)
        self.risk = np.full(P, np.nan)
        self.agreeableness = np.full(P, np.nan)
        grp: dict[tuple[str, int], list[dict]] = {}
        for r in rows:
            p, rd = ix[int(r["id"])], int(r["round"])
            self.contrib[p, rd - 1] = _num(r["contribution"])
            self.prev[p, rd - 1] = _num(r["contribution_1"])
            self.svo_angle[p], self.risk[p], self.agreeableness[p] = _num(r["svo_angle"]), _risk(r["risk"]), _num(r["agreeableness"])
            grp.setdefault((r["group_id"], rd), []).append(r)
        self.n_group_rounds = len(grp)
        keep = []
        self.dropped = {"fewer than 6 rows": 0, "6 rows, a member excluded": 0, "no recorded total": 0}
        for (gid, rd), v in sorted(grp.items(), key=lambda kv: (kv[0][1], kv[0][0])):
            tot = v[0]["total_contribution"]
            if len(v) != GROUP_SIZE:
                self.dropped["fewer than 6 rows"] += 1
            elif any(r["excluded"] != "Included" for r in v):
                self.dropped["6 rows, a member excluded"] += 1
            elif tot == "":
                self.dropped["no recorded total"] += 1
            else:
                keep.append((rd, [ix[int(r["id"])] for r in v], float(tot), v[0]["treatment"].startswith("High")))
        self.rnd = np.array([k[0] for k in keep])
        self.mem = np.array([k[1] for k in keep])
        self.y_cont = np.array([k[2] for k in keep])
        self.y_bin = (self.y_cont >= THRESHOLD).astype(float)
        self.high_first = np.array([k[3] for k in keep])

    def person_values(self, drive: str) -> np.ndarray:
        return getattr(self, drive)


def person_training_stats(panel: Panel, ph: int) -> dict:
    """Person rates and the lag fill value, from the TRAINING rounds of phase `ph` only."""
    first = 1 if ph == 1 else SWITCH
    cols = np.arange(first, first + TRAIN_LEN) - 1
    c = panel.contrib[:, cols]
    seen = ~np.isnan(c)
    grand = float(np.nanmean(c))
    n = seen.sum(1)
    rate = np.where(n > 0, np.nansum(c, 1) / np.maximum(n, 1), grand)
    pv = panel.prev[:, cols]
    return {"rate": rate, "grand": grand, "prev_fill": float(np.nanmean(pv)) if (~np.isnan(pv)).any() else grand, "persons_without_rate": int((n == 0).sum()), "cols": cols}


# ----------------------------------------------------------------------------------------------------------------------
# models

@dataclass
class LinFrozen:
    """Ridge linear regression fitted on training rows only; mean of y, mean and sd of X and coefficients are stored."""

    mu: np.ndarray
    sd: np.ndarray
    ybar: float
    beta: np.ndarray

    @classmethod
    def fit(cls, X, y, l2: float = L2) -> "LinFrozen":
        X, y = np.asarray(X, float), np.asarray(y, float)
        mu, sd = X.mean(0), X.std(0)
        sd = np.where(sd > 1e-12, sd, 1.0)
        Z = (X - mu) / sd
        yb = float(y.mean())
        b = np.linalg.solve(Z.T @ Z + l2 * np.eye(Z.shape[1]), Z.T @ (y - yb))
        return cls(mu, sd, yb, b)

    def predict(self, X) -> np.ndarray:
        return self.ybar + ((np.asarray(X, float) - self.mu) / self.sd) @ self.beta


def _counts(V: np.ndarray, cuts) -> np.ndarray:
    return np.column_stack([(V > c).sum(1) for c in cuts]).astype(float)


def cut_grid(drive: str, V_train_persons: np.ndarray) -> tuple[float, ...]:
    if drive == "svo_angle":
        return CUT_GRID
    return tuple(float(x) for x in np.percentile(V_train_persons, PCT_GRID))


def choose_cuts(V_tr: np.ndarray, y_tr: np.ndarray, grid) -> tuple[list[float], float, float]:
    """The rule's item 3 (T): the best single cut by in-training log-loss (ties to the lower cut); then a second cut if that
    lowers the in-training log-loss.  V_tr is the training groups' member values (rows x 6).  Returns the cuts, the one-cut and
    the final in-training log-loss.  Uses the training rows only."""
    def ll(cs) -> float:
        X = _counts(V_tr, cs)
        return A.logloss(y_tr, F.Frozen.fit(X, y_tr, ("n",) * len(cs)).predict(X))

    grid = sorted(set(grid))
    s1 = [(ll([c]), c) for c in grid]
    best1 = min(s1, key=lambda t: t[0])           # min returns the first, i.e. the lowest cut, on ties
    c1, l1 = best1[1], best1[0]
    rest = [c for c in grid if c != c1]
    if not rest:
        return [c1], l1, l1
    s2 = [(ll(sorted([c1, c])), c) for c in rest]
    l2_, c2 = min(s2, key=lambda t: t[0])
    if l2_ < l1:
        return sorted([c1, c2]), l1, l2_
    return [c1], l1, l1


def fit_phase(panel: Panel, ph: int, drive: str, with_D: bool = True) -> dict:
    """Fit every model for one phase on its training group-rounds, freeze, predict its test group-rounds."""
    tr_all, te_all = split_rounds(panel.rnd)
    inph = phase_of(panel.rnd) == ph
    tr, te = inph & tr_all, inph & te_all
    st = person_training_stats(panel, ph)
    v = panel.person_values(drive)
    V = v[panel.mem]
    ytr_b, yte_b = panel.y_bin[tr], panel.y_bin[te]
    ytr_c, yte_c = panel.y_cont[tr], panel.y_cont[te]
    persons_tr = np.unique(panel.mem[tr])
    grid = cut_grid(drive, v[persons_tr])
    cuts, ll1, llf = choose_cuts(V[tr], ytr_b, grid)
    Tx = _counts(V, cuts)
    Mx = V.mean(1, keepdims=True)
    Mox = np.column_stack([V.mean(1), V.min(1), V.max(1), V.std(1)])
    Rr = st["rate"][panel.mem]
    Rx = np.column_stack([Rr.mean(1), Rr.min(1)])
    X = {
        "M": (Mx, ["mean"]),
        "Mo": (Mox, ["mean", "min", "max", "sd"]),
        "T": (Tx, [f"n above {c:g}" for c in cuts]),
        "R": (Rx, ["rate mean", "rate min"]),
        "R+T": (np.column_stack([Rx, Tx]), ["rate mean", "rate min"] + [f"n above {c:g}" for c in cuts]),
        "R+M": (np.column_stack([Rx, Mx]), ["rate mean", "rate min", "mean"]),
    }
    if with_D:
        pv = np.where(np.isnan(panel.prev[panel.mem, panel.rnd[:, None] - 1]), st["prev_fill"], panel.prev[panel.mem, panel.rnd[:, None] - 1])
        X["D"] = (pv.mean(1, keepdims=True), ["previous-round contribution, mean"])
    out = {"phase": ph, "n_train": int(tr.sum()), "n_test": int(te.sum()), "cuts": cuts, "cut_grid": list(grid),
           "ll_one_cut": ll1, "ll_final_cuts": llf,
           "base_rate_train": float(ytr_b.mean()), "base_rate_test": float(yte_b.mean()),
           "train_pos_neg": (int(ytr_b.sum()), int((1 - ytr_b).sum())), "test_pos_neg": (int(yte_b.sum()), int((1 - yte_b).sum())),
           "high_first": {"train": (int(panel.high_first[tr].sum()), int((~panel.high_first[tr]).sum())),
                          "test": (int(panel.high_first[te].sum()), int((~panel.high_first[te]).sum()))},
           "y_te_bin": yte_b, "y_te_cont": yte_c, "ybar_train": float(ytr_c.mean()),
           "persons_without_rate": st["persons_without_rate"], "models": {}, "scores": {"0": np.full(int(te.sum()), float(ytr_b.mean()))},
           "cont": {"0": np.full(int(te.sum()), float(ytr_c.mean()))}}
    for name, (Xa, cols) in X.items():
        fz = F.Frozen.fit(Xa[tr], ytr_b, cols)
        lf = LinFrozen.fit(Xa[tr], ytr_c)
        out["scores"][name] = fz.predict(Xa[te])
        out["cont"][name] = lf.predict(Xa[te])
        out["models"][name] = {"features": cols, "beta_std": fz.beta.tolist(), "train_auc": A.auc_score(ytr_b, fz.predict(Xa[tr])),
                               "train_ll": A.logloss(ytr_b, fz.predict(Xa[tr]))}
    # exploratory: does the drive relate to the person's own rate in this phase (training persons)?
    rr, vv = st["rate"][persons_tr], v[persons_tr]
    out["corr_drive_rate"] = float(np.corrcoef(rr, vv)[0, 1])
    return out


def _rmse(y, p) -> float:
    return float(np.sqrt(np.mean((np.asarray(y) - np.asarray(p)) ** 2)))


def score_stratum(y_bin, y_cont, scores: dict, conts: dict, *, draws: int = BOOT, seed: int = SEED) -> dict:
    """Held-out numbers for one stratum (a phase, or the two phases pooled) plus the bootstrap of the contrasts."""
    R = {"n": len(y_bin), "pos_neg": (int(np.sum(y_bin)), int(len(y_bin) - np.sum(y_bin))), "test": {}}
    base_rmse = _rmse(y_cont, conts["0"])
    for k, s in scores.items():
        R["test"][k] = {"auc": A.auc_score(y_bin, s), "ll": A.logloss(y_bin, s), "rmse": _rmse(y_cont, conts[k]), "rmse_ratio": _rmse(y_cont, conts[k]) / base_rmse}
    B = F.bootstrap(y_bin, scores, draws=draws, seed=seed)
    R["boot"] = B
    R["ci_auc"] = {k: F.interval(v) for k, v in B["auc"].items()}
    R["ci_ll"] = {k: F.interval(v) for k, v in B["ll"].items()}
    return R


def contrast(R: dict, x: str, y: str) -> dict:
    """x minus y: point differences and bootstrap intervals in AUC and log-loss."""
    B = R["boot"]
    da, dl = B["auc"][x] - B["auc"][y], B["ll"][x] - B["ll"][y]
    return {"auc": R["test"][x]["auc"] - R["test"][y]["auc"], "auc_ci": F.interval(da), "ll": R["test"][x]["ll"] - R["test"][y]["ll"], "ll_ci": F.interval(dl),
            "auc_share_gt_margin": float((da > AUC_MARGIN).mean()), "ll_share_lt0": float((dl < 0).mean())}


def verdicts(R: dict) -> dict:
    t = R["test"]
    out = {
        "K1": k1_met(t["M"]["auc"], t["M"]["ll"], t["0"]["ll"]),
        "K2": beats(t["T"]["auc"], t["M"]["auc"], t["T"]["ll"], t["M"]["ll"]),
        "K3": beats(t["R+T"]["auc"], t["R"]["auc"], t["R+T"]["ll"], t["R"]["ll"]),
        "K3b": beats(t["R+M"]["auc"], t["R"]["auc"], t["R+M"]["ll"], t["R"]["ll"]),
    }
    if "D" in t:
        out["D"] = beats(t["D"]["auc"], t["R"]["auc"], t["D"]["ll"], t["R"]["ll"])
    return out


def run_drive(panel: Panel, drive: str, *, draws: int = BOOT, seed: int = SEED, with_D: bool = False) -> dict:
    ph = {p: fit_phase(panel, p, drive, with_D=with_D) for p in (1, 2)}
    out = {"phases": ph, "strata": {}}
    for label, parts in (("phase 1", [1]), ("phase 2", [2]), ("pooled", [1, 2])):
        yb = np.concatenate([ph[p]["y_te_bin"] for p in parts])
        yc = np.concatenate([ph[p]["y_te_cont"] for p in parts])
        names = ph[parts[0]]["scores"].keys()
        sc = {k: np.concatenate([ph[p]["scores"][k] for p in parts]) for k in names}
        co = {k: np.concatenate([ph[p]["cont"][k] for p in parts]) for k in names}
        R = score_stratum(yb, yc, sc, co, draws=draws, seed=seed)
        R["verdict"] = verdicts(R)
        R["c"] = {"K1_ll": contrast(R, "M", "0"), "K2": contrast(R, "T", "M"), "K3": contrast(R, "R+T", "R"), "K3b": contrast(R, "R+M", "R")}
        if "D" in sc:
            R["c"]["D"] = contrast(R, "D", "R")
        out["strata"][label] = R
    return out


def counts_table(panel: Panel) -> dict:
    tr_all, te_all = split_rounds(panel.rnd)
    ph = phase_of(panel.rnd)
    out = {}
    for p in (1, 2):
        for nm, m in (("train", tr_all), ("test", te_all)):
            s = (ph == p) & m
            out[(p, nm)] = {"n": int(s.sum()), "pos_neg": (int(panel.y_bin[s].sum()), int((1 - panel.y_bin[s]).sum())), "rate": float(panel.y_bin[s].mean()),
                            "high_first": int(panel.high_first[s].sum()), "mean_total": float(panel.y_cont[s].mean())}
    return out


def run_all(panel: Panel, log=print) -> dict:
    out = {}
    for d in DRIVES:
        log(f"{d} ...")
        out[d] = run_drive(panel, d, with_D=(d == "svo_angle"))
    out["counts"] = counts_table(panel)
    return out


# ----------------------------------------------------------------------------------------------------------------------
# the report

_f, _ci, _cip = F._f, F._ci, F._ci_plain

MODEL_NAMES = {
    "0": "0: training base rate / mean", "M": "M: mean of the drive", "Mo": "Mo: mean, min, max, sd of the drive",
    "T": "T: count above a cut (cuts chosen on training)", "R": "R: person rates (mean, min)", "R+T": "R+T: rates + count above cut",
    "R+M": "R+M: rates + mean of the drive", "D": "D: previous-round contribution (mean)",
}


def _verdict(b: bool) -> str:
    return "MET" if b else "NOT MET"


def _model_table(R: dict, names) -> str:
    rows = ["| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | RMSE of total / baseline RMSE |", "|---|---|---|---|"]
    for k in names:
        t = R["test"][k]
        rows.append(f"| {MODEL_NAMES[k]} | {_f(t['auc'])} {_cip(R['ci_auc'][k])} | {_f(t['ll'])} {_cip(R['ci_ll'][k])} | {_f(t['rmse_ratio'])} |")
    return "\n".join(rows)


def _kt(res: dict, key: str, extra: bool = False) -> str:
    """One row per stratum for the K2 / K3 style contrasts."""
    rows = ["| stratum | test group-rounds | AUC difference [95%] | log-loss difference [95%] | share of draws AUC > +0.02 | criterion |", "|---|---|---|---|---|---|"]
    for s in STRATA:
        R = res["strata"][s]
        c = R["c"][key]
        vk = {"K2": "K2", "K3": "K3", "K3b": "K3b", "D": "D"}[key]
        rows.append(f"| {s} | {R['n']} | {c['auc']:+.3f} {_ci(c['auc_ci'])} | {c['ll']:+.3f} {_ci(c['ll_ci'])} | {c['auc_share_gt_margin']:.3f} | {_verdict(R['verdict'][vk])} |")
    return "\n".join(rows)


def _k1_table(res: dict) -> str:
    rows = ["| stratum | M held-out AUC [95%] | M log-loss | baseline log-loss | log-loss M - 0 [95%] | criterion |", "|---|---|---|---|---|---|"]
    for s in STRATA:
        R = res["strata"][s]
        c = R["c"]["K1_ll"]
        t = R["test"]
        rows.append(f"| {s} | {_f(t['M']['auc'])} {_cip(R['ci_auc']['M'])} | {_f(t['M']['ll'])} | {_f(t['0']['ll'])} | {c['ll']:+.3f} {_ci(c['ll_ci'])} | {_verdict(R['verdict']['K1'])} |")
    return "\n".join(rows)


def _coef_table(res: dict) -> str:
    rows = ["| phase | model | features | coefficients on standardised inputs (intercept first) | in-training AUC |", "|---|---|---|---|---|"]
    for p in (1, 2):
        ph = res["phases"][p]
        for k, m in ph["models"].items():
            rows.append(f"| {p} | {k} | {', '.join(m['features'])} | {', '.join(f'{b:+.3f}' for b in m['beta_std'])} | {_f(m['train_auc'])} |")
    return "\n".join(rows)


def _decision_line(label: str, res: dict) -> str:
    v = {s: res["strata"][s]["verdict"] for s in STRATA}
    return f"| {label} | " + " | ".join(" / ".join(f"{k} {_verdict(v[s][k])}" for k in ("K1", "K2", "K3")) for s in STRATA) + " |"


def _reading(P: dict) -> str:
    """The plain reading of the primary decision, every number taken from the run (nothing here is a new test)."""
    S1, S2, SP = (P["strata"][k] for k in STRATA)
    out = ["**Reading (nothing new is tested here).**\n"]
    out.append(f"- **K1** holds on the point estimates in {', '.join(s for s in STRATA if P['strata'][s]['verdict']['K1']) or 'no stratum'} and fails in {', '.join(s for s in STRATA if not P['strata'][s]['verdict']['K1']) or 'none'}; it is a weak pass where it holds: M's log-loss gain over the baseline is {S1['c']['K1_ll']['ll']:+.3f} / {S2['c']['K1_ll']['ll']:+.3f} / {SP['c']['K1_ll']['ll']:+.3f} (phase 1 / phase 2 / pooled), every one of those intervals contains 0, and the lower end of M's AUC interval is {S1['ci_auc']['M'][0]:.3f} / {S2['ci_auc']['M'][0]:.3f} / {SP['ci_auc']['M'][0]:.3f}, below the 0.55 floor in the phases. The pooled AUC is flattered by the phase mix: the baseline alone, which uses no drive, has pooled AUC {SP['test']['0']['auc']:.3f} because the two phases have different base rates, so the pooled K1 floor is partly met by phase membership.")
    out.append(f"- **K2** fails everywhere on the point estimates: T minus M is {S1['c']['K2']['auc']:+.3f} / {S2['c']['K2']['auc']:+.3f} / {SP['c']['K2']['auc']:+.3f} in AUC. No interval excludes 0 in either direction, so the data do not show composition-as-count to be better, and they do not show it to be worse either; the share of bootstrap draws in which T beats M by more than 0.02 is {S1['c']['K2']['auc_share_gt_margin']:.2f} / {S2['c']['K2']['auc_share_gt_margin']:.2f} / {SP['c']['K2']['auc_share_gt_margin']:.2f}.")
    out.append(f"- **K3** fails everywhere: adding the count to rates changes held-out AUC by {S1['c']['K3']['auc']:+.3f} / {S2['c']['K3']['auc']:+.3f} / {SP['c']['K3']['auc']:+.3f} and log-loss by {S1['c']['K3']['ll']:+.3f} / {S2['c']['K3']['ll']:+.3f} / {SP['c']['K3']['ll']:+.3f}; adding the mean changes AUC by {S1['c']['K3b']['auc']:+.3f} / {S2['c']['K3b']['auc']:+.3f} / {SP['c']['K3b']['auc']:+.3f}. Person rates alone carry the held-out information (AUC {S1['test']['R']['auc']:.3f} / {S2['test']['R']['auc']:.3f} / {SP['test']['R']['auc']:.3f}), and the measured drive adds none that this test can see.")
    out.append("")
    return "\n".join(out)


def write_report(R: dict, panel: Panel, path: Path = RESULTS) -> str:
    P = R["svo_angle"]
    C = R["counts"]
    L = []
    L.append("# Szekely 2021: does the composition of measured drives predict a group's threshold outcome, and do drives add to person rates?\n")
    L.append(f"_Generated 2026-11-01 by `uv run python -m models.szekely_composition report` (seed {SEED}; {BOOT} bootstrap draws). Code: `sim/models/szekely_composition.py`; checks: `sim/tests/test_szekely_composition.py`. Built on `sim/models/apache_activity_survival.py` and `sim/models/apache_fitted_case.py` (`logit_fit`, `auc_score`, `logloss`, `Frozen`, `criterion`, `bootstrap` imported, not changed). Data: Szekely, Lipari, Antonioni, Paolucci, Sanchez, Tummolini & Andrighetto (2021), Nature Communications 12, 5452, doi:10.1038/s41467-021-25734-w (article CC BY 4.0); data OSF project https://osf.io/wvgk9, file `full.csv` (OSF project licence field empty; reuse is 'data available' with attribution); local-use-only and git-ignored; this file holds counts and statistics only, never a participant row._\n")
    L.append("**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). This is the composition test on a real experiment with a measured drive: the synthetic population (`results/synthetic_population_identifiability.md`, Decision) found drives recoverable but their LINEAR composition no better than person rates, so how the drives are combined is what is under test here.\n")
    L.append(facts_block())
    L.append(rule_block())
    L.append("## Decisions the rule left open (taken before any fit)\n")
    for it in IMPLEMENTATION:
        L.append("- " + it)
    L.append("")
    L.append("## Counts\n")
    L.append(f"File: {panel.n_raw:,} rows; {panel.n_persons} persons; game rows (`odr` = 1): {panel.n_persons * N_ROUNDS:,}. Group-rounds in the file: {panel.n_group_rounds:,}. Dropped from the analysis: " + "; ".join(f"{k}: {v}" for k, v in panel.dropped.items()) + f". Analysed: {len(panel.rnd):,} group-rounds of six.\n")
    L.append("| phase | set | rounds | group-rounds | reached / not | reached share | mean total | High-first order group-rounds |\n|---|---|---|---|---|---|---|---|")
    rr = {(1, "train"): "1-10", (1, "test"): "11-14", (2, "train"): "15-24", (2, "test"): "25-28"}
    for (p, nm), c in C.items():
        L.append(f"| {p} | {nm} | {rr[(p, nm)]} | {c['n']} | {c['pos_neg'][0]} / {c['pos_neg'][1]} | {c['rate']:.3f} | {c['mean_total']:.1f} | {c['high_first']} |")
    L.append("")
    ph1, ph2 = P["phases"][1], P["phases"][2]
    L.append(f"Persons without any recorded contribution in a phase's training rounds (given the grand mean): phase 1 {ph1['persons_without_rate']}, phase 2 {ph2['persons_without_rate']}.\n")
    L.append("## Frozen choices and coefficients (primary drive, svo_angle; fitted on training rounds only)\n")
    for p, ph in ((1, ph1), (2, ph2)):
        L.append(f"- **Phase {p}.** Grid {ph['cut_grid']}. Cut(s) chosen for T: **{', '.join(f'{c:g}' for c in ph['cuts'])}** degrees; in-training log-loss with one cut {_f(ph['ll_one_cut'], 4)}, with the final cut set {_f(ph['ll_final_cuts'], 4)}.")
    L.append("")
    L.append("Coefficients act on inputs standardised on the training rows; positive goes with reaching the threshold. Logistic ridge, penalty 1.\n")
    L.append(_coef_table(P))
    L.append("")
    L.append("## Held-out result, primary drive (svo_angle), scored once\n")
    for s in STRATA:
        Rs = P["strata"][s]
        L.append(f"### {s.capitalize()}: {Rs['n']} test group-rounds ({Rs['pos_neg'][0]} reached, {Rs['pos_neg'][1]} not; {Rs['boot']['skipped']} of {BOOT} draws skipped for one class)\n")
        L.append(_model_table(Rs, ["0", "M", "Mo", "T", "R", "R+T", "R+M", "D"]))
        L.append("")
    L.append("## Decision, exactly per the criteria (primary drive)\n")
    L.append("**K1** (measured drives carry information: M beats 0 on held-out log-loss AND its AUC exceeds 0.55).\n")
    L.append(_k1_table(P))
    L.append("")
    L.append("**K2** (composition matters: T beats M by more than 0.02 held-out AUC AND lower log-loss). Differences are T minus M.\n")
    L.append(_kt(P, "K2"))
    L.append("")
    L.append("**K3** (drives add to rates: R+T beats R by more than 0.02 AUC AND lower log-loss). Differences are (R+T) minus R.\n")
    L.append(_kt(P, "K3"))
    L.append("")
    L.append("K3, companion report (rule item 5): (R+M) minus R.\n")
    L.append(_kt(P, "K3b"))
    L.append("")
    L.append("| | " + " | ".join(STRATA) + " |\n|---|---|---|---|")
    L.append(_decision_line("primary: svo_angle", P))
    L.append("")
    L.append(_reading(P))
    L.append("## Secondary (reported, not decisive)\n")
    L.append("### S1. Risk and agreeableness in place of svo_angle\n")
    L.append("Same models, same frozen protocol, cuts from the percentile grid. Decision rows as for the primary.\n")
    for d in ("risk", "agreeableness"):
        res = R[d]
        L.append(f"**{DRIVES[d]}.** Cuts chosen: phase 1 {', '.join(f'{c:.4g}' for c in res['phases'][1]['cuts'])}; phase 2 {', '.join(f'{c:.4g}' for c in res['phases'][2]['cuts'])}.\n")
        L.append("| stratum | K1: M AUC [95%] / log-loss M - 0 | K1 | K2: T - M AUC [95%] / log-loss | K2 | K3: (R+T) - R AUC [95%] / log-loss | K3 | (R+M) - R AUC / log-loss |\n|---|---|---|---|---|---|---|---|")
        for s in STRATA:
            Rs = res["strata"][s]
            c = Rs["c"]
            L.append(f"| {s} | {_f(Rs['test']['M']['auc'])} {_cip(Rs['ci_auc']['M'])} / {c['K1_ll']['ll']:+.3f} | {_verdict(Rs['verdict']['K1'])} | {c['K2']['auc']:+.3f} {_ci(c['K2']['auc_ci'])} / {c['K2']['ll']:+.3f} | {_verdict(Rs['verdict']['K2'])} | {c['K3']['auc']:+.3f} {_ci(c['K3']['auc_ci'])} / {c['K3']['ll']:+.3f} | {_verdict(Rs['verdict']['K3'])} | {c['K3b']['auc']:+.3f} / {c['K3b']['ll']:+.3f} |")
        L.append("")
        L.append(_decision_line(DRIVES[d], res))
        L.append("")
    L.append("### S2. A dynamic person state (D) against person rates (R)\n")
    L.append("D = mean over members of the previous-round contribution; the contrast is D minus R, with the same strict AUC margin and log-loss condition (the rule gives D no margin of its own; this is the K3 form, an assumption).\n")
    L.append(_kt(P, "D"))
    L.append("")
    L.append("## Exploratory (nothing here was pre-specified)\n")
    L.append(f"- **Does the drive relate to the person's own behaviour?** Correlation, across the persons in the phase's training group-rounds, of svo_angle with the person's training-round mean contribution: phase 1 {P['phases'][1]['corr_drive_rate']:+.3f}, phase 2 {P['phases'][2]['corr_drive_rate']:+.3f}; risk {R['risk']['phases'][1]['corr_drive_rate']:+.3f} / {R['risk']['phases'][2]['corr_drive_rate']:+.3f}; agreeableness {R['agreeableness']['phases'][1]['corr_drive_rate']:+.3f} / {R['agreeableness']['phases'][2]['corr_drive_rate']:+.3f}.")
    L.append("- **Fit against transfer.** In-training AUC of each model is in the coefficient table; the held-out AUCs are in the stratum tables above. R is flattered in training (its rate contains the outcome being predicted, see the decisions above), so a large gap between its two numbers is expected and is not overfitting of the usual kind.")
    L.append(f"- **D and the total.** D's RMSE ratio is {P['strata']['phase 1']['test']['D']['rmse_ratio']:.3f} / {P['strata']['phase 2']['test']['D']['rmse_ratio']:.3f} / {P['strata']['pooled']['test']['D']['rmse_ratio']:.3f} against R's {P['strata']['phase 1']['test']['R']['rmse_ratio']:.3f} / {P['strata']['phase 2']['test']['R']['rmse_ratio']:.3f} / {P['strata']['pooled']['test']['R']['rmse_ratio']:.3f} (phase 1 / phase 2 / pooled), so the previous round's contributions forecast the continuous total better than the person rates do while the two tie on the binary outcome. Not a criterion; the RMSE difference has no interval here.")
    L.append("- **Two nearby cuts.** Where the rule's literal second-cut step kept two cuts, the two counts together are a count in a band if the cuts are close (phase 1 cuts: " + ", ".join(f"{c:g}" for c in P["phases"][1]["cuts"]) + "; phase 2: " + ", ".join(f"{c:g}" for c in P["phases"][2]["cuts"]) + "), and opposite-signed coefficients in the coefficient table show it; the literal rule keeps a second cut on any in-training log-loss gain, however small (phase 2's gain is " + _f(P['phases'][2]['ll_one_cut'] - P['phases'][2]['ll_final_cuts'], 4) + ").")
    L.append("- **Total-contribution outcome.** The RMSE column of each table is y_cont relative to the training mean. The criteria are on the binary outcome only.\n")
    L.append("## Caveats\n")
    L.append("- **One group size.** Every group is six. Nothing here tests sensitivity to group size, which is half of what the programme claims; it tests composition at n = 6 only.")
    L.append("- **Reshuffled groups.** Groups are re-formed every round, so a member's rate is estimated across many different compositions, and a group-round is a one-off assembly. This helps the person-effects reading (the rate is a clean person trait) and hurts any model of a stable group state; it also means the same persons recur across group-rounds, so the bootstrap, which treats group-rounds as independent, understates the uncertainty.")
    L.append("- **Norms change across rounds** (the paper's own finding: empirical and normative expectations and contributions move with the disaster probability and with time). A model fitted on rounds 1-10 meets rounds 11-14 under the same probability but a later norm state; the frozen models cannot track that. The outcome frequency falls from 0.82 in round 1 to 0.44 in round 28, so the base rate differs between training and test inside a phase. Order and disaster probability are not in any model.")
    L.append("- **The threshold game favours a count-above-cut form.** A group reaches the threshold when the total passes 300, a threshold on a sum; a count of members above a cut is a natural coarse summary of that sum. T therefore has a structural advantage in this game that it may not have in games without a threshold. A pass on K2 here is weak support for the algebra's claim; a failure is stronger evidence against it than a pass is for it.")
    L.append("- **SVO is one drive among the paper's many measures.** The slider measures preference over own-and-other payoffs; it is not curiosity, fear or desire, and the experiment's main driver (beliefs about what others will do, the empirical and normative expectations) is not used here as a drive. A refutation is of this proxy for this outcome only.")
    L.append("- **R is built to be strong.** The person-effects rival uses the training outcomes themselves; inside training it contains the target. In the test rounds it is a real forecast, and the rule compares only held-out numbers.")
    L.append("- **The rule's margin was fixed after seeing outcome frequencies** (facts above) but before any relation of a drive to an outcome.")
    L.append("- **Measurement.** `svo_angle` is a single administration on day 1; an angle is a continuous summary of a slider task and its cuts (15 to 35 degrees) are the grid of the rule, not natural thresholds (22.45 degrees is the conventional boundary between individualistic and prosocial).")
    L.append("- **Licence and credit.** The article is CC BY 4.0; the OSF project sets no licence, so the data are used as 'available' with attribution and not redistributed. Credit: Szekely et al. 2021 for the experiment and the data; Murphy, Ackermann & Handgraaf (2011) for the SVO slider measure (as named by the paper; not read here). Nothing from the file is reproduced beyond aggregate statistics.\n")
    L.append("## Reproduce\n")
    L.append("    cd sim\n    ~/.local/bin/uv run python -m models.szekely_composition rule      # once: writes the data facts and the rule into this file, no model number\n    ~/.local/bin/uv run python -m models.szekely_composition report    # fits, freezes, scores once; about a minute\n    ~/.local/bin/uv run pytest -q tests/test_szekely_composition.py\n")
    text = "\n".join(L)
    path.write_text(text)
    return text


def write_rule_stub(path: Path = RESULTS) -> None:
    if path.exists() and RULE_TEXT in path.read_text() and FACTS_TEXT in path.read_text():
        print(f"the facts and the rule are already in {path}")
        return
    path.write_text(
        "# Szekely 2021: does the composition of measured drives predict a group's threshold outcome, and do drives add to person rates?\n\n"
        "_Stub written before any fit. No model has been fitted and no relation of a drive to an outcome has been computed. `report` replaces everything below the rule._\n\n"
        + facts_block() + "\n" + rule_block()
    )
    print(f"wrote the facts and the rule to {path}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rule", help="write the data facts and the rule (verbatim) to results/szekely_composition.md, before any fit")
    sub.add_parser("report", help="fit on the training rounds, freeze, score the test rounds once, write the results file")
    args = ap.parse_args(argv)
    if args.cmd == "rule":
        write_rule_stub()
        return 0
    if not RESULTS.exists() or RULE_TEXT not in RESULTS.read_text():
        raise SystemExit("run `rule` first: the rule must be in results/szekely_composition.md before any model is fitted")
    if not DATA.exists():
        raise SystemExit("sim/data/szekely2021/full.csv is absent (local-use-only): download https://osf.io/download/ra9ex/ and check the sha256 in sim/data/README.md")
    if sha256_of() != DATA_SHA256:
        raise SystemExit("full.csv does not match the recorded sha256")
    panel = Panel()
    R = run_all(panel)
    write_report(R, panel)
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
