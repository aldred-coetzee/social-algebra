"""The fitted case: does first-year growth add out-of-time information about graduation beyond team size?

    cd sim
    ~/.local/bin/uv run python -m models.apache_fitted_case rule      # writes the rule (and nothing else) to results/apache_fitted_case.md
    ~/.local/bin/uv run python -m models.apache_fitted_case report    # refuses unless the rule is already in that file; then fits, freezes, scores once

Prior work.  models/00-v0.md section 1.1 (team activity: per-member contributions; the prospective first-year growth
g = ln((months 6-11 + 1)/(months 0-5 + 1)), cuts fixed in advance) and section 8 "Team" (the rule written first);
results/apache_activity_survival.md (the in-sample work, its Review, the conversation lead; ledger L4623-L4633,
file 117 section 4.3).  Loaders, the member rule, the activity measure, the landmark table, the logistic fit, the AUC
and the log-loss are the functions of models/apache_activity_survival.py, imported and not changed.

Privacy and terms.  Only counts of podlings, coefficients, AUCs and log-losses leave this module; no name, address or
text is read here.  The data are local-use-only and git-ignored (sim/data/README.md); nothing from them is committed.

Procedure fixed by RULE_TEXT below, which is copied verbatim into the results file before any number is computed.
`report` refuses to run unless that file already contains it.  Implementation decisions that the rule left open are
listed in IMPLEMENTATION and were taken before any fit.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from models import apache_activity_survival as A

SIM = A.SIM
RESULTS = SIM / "results" / "apache_fitted_case.md"
SEED = A.SEED

TRAIN_YEARS = (2003, 2012)
TEST_YEARS = (2013, 2021)
AUC_MARGIN = 0.02
BOOT = 2000
L2 = A.PRIMARY["l2"]
MIN_N = A.PRIMARY["min_n"]

MODELS = {"A": ("ln_n",), "B": ("ln_n", "growth"), "C": ("ln_n", "growth", "cal_year")}
NAMES = {
    "0": "baseline: the training-set base rate",
    "A": "A: size only, logistic on ln n",
    "B": "B: size + growth, logistic on ln n and g",
    "C": "C: size + growth + start year",
}

# Copied verbatim from the brief (items 1-5; the sentence "THE RULE, written here before any fit" is the brief's own lead-in).
RULE_TEXT = """\
1. Unit: a podling with a recorded outcome (graduated vs retired). Training set: podlings whose incubation STARTED 2003-01-01 to 2012-12-31. Test set: podlings started 2013-01-01 to 2021-12-31. No podling appears in both. Nothing from the test set is looked at until the models are frozen.
2. Features, all computable from the first 12 months of a podling's record only: n = number of regular members (as the existing module defines it, computed on months 0–11); g = prospective first-year growth as in §1.1; start year as a control. Models: (A) size only: logistic on n; (B) size + growth: logistic on n and g; (C) size + growth + start year. Baseline (0): predict the training-set base rate. Fit all on training only; freeze.
3. Score on the test set once: held-out AUC and log-loss for (0), (A), (B), (C); the pre-registered decision criterion is: B beats A on held-out AUC by more than 0.02 AND B's log-loss is lower than A's. Report bootstrap intervals (resample test podlings, 2,000 draws) for the AUC difference B − A; do not re-tune.
4. Secondary (reported, not decisive, clearly labelled): the conversation-concentration lead (development-list messages, automated senders removed, W = 12 months; Gini and top-3 share added to A) scored on the same held-out set with the same frozen protocol; and the same four models with a 6-month feature window.
5. Everything else is exploratory and must be labelled so."""

# Decisions the rule left open, taken before any fit (so that the file can say they were not outcome-driven).
IMPLEMENTATION = [
    "**Population.** The module's own landmark table: a resolved podling (graduated or retired by the data end, from the ASF's `podlings.xml`) still in the Incubator at month W (exit month >= W), so that no feature can contain the exit; at least 3 regular members (the module's `min_n`), so that ln n and the shape measures are defined. The podlings dropped by these two conditions are counted below, by set.",
    "**Features.** n = regular members, active (commits plus human-list messages from non-automated senders) in at least ceil(W/4) of the window's months, at least 2 (3 of 12 at W = 12; 2 of 6 at W = 6); the model takes ln n (the module's size feature). g = ln((events in the window's second half + 1)/(events in its first half + 1)), the halves being months 0-5 and 6-11 at W = 12 and months 0-2 and 3-5 at W = 6; g enters as a number, not as the growth/steady/collapse classes. Start year = the calendar year of the podling's `startdate`.",
    "**Fit.** The module's ridge logistic regression (`logit_fit`, penalty 1 on inputs standardised on the training set, intercept free), the module's default, not tuned. Frozen means: training mean, standard deviation and coefficients are stored and applied unchanged to the test set. Model C extrapolates the start year beyond the training range (2013-2021 against 2003-2012); that is what the rule asks for.",
    "**Scoring.** Held-out AUC (`auc_score`, Mann-Whitney, ties one half) and log-loss (`logloss`, probabilities clipped to [1e-6, 1-1e-6]) of the graduation probability, once, on the test set. The baseline's AUC is 0.5 by construction (a constant).",
    "**Bootstrap.** Resample the test podlings with replacement, 2,000 draws, seed 20261101, models frozen (predictions fixed); a draw with one class only is skipped and counted. 95% percentile intervals. Reported for B - A in AUC and in log-loss and for each model's AUC.",
    "**Conversation lead (secondary).** Development-list messages (module measure `dev_messages`: every message on a development list that is not commit mail, from a non-automated sender), W = 12; a regular member of THAT measure is active on a development list in at least 3 of the 12 months; Gini (rescaled by n/(n-1)) and top-3 share of the members' totals are added to A's ln n (A's n is the events-based n of the primary). They need at least 3 such members, so the secondary is scored on the podlings that have them, and A is re-fitted and re-scored on that same subset for the comparison; the podlings lost are counted.",
]


def rule_block() -> str:
    return (
        "## The rule, written before any fit\n\n"
        "Copied verbatim from the brief of 2026-11-01; written into this file before the first number was computed "
        "(`report` refuses to run unless this block is already here).\n\n" + RULE_TEXT + "\n"
    )


# ------------------------------------------------------------------ pure pieces (no data needed)

def split_masks(cal_year, train=TRAIN_YEARS, test=TEST_YEARS) -> tuple[np.ndarray, np.ndarray]:
    """Boolean masks of the training and the test set by calendar year of the podling's start.  Disjoint by construction;
    a podling started outside both ranges is in neither."""
    y = np.asarray(cal_year)
    return (y >= train[0]) & (y <= train[1]), (y >= test[0]) & (y <= test[1])


@dataclass
class Frozen:
    """A logistic model fitted on training rows only; every constant it needs for the test set is stored."""

    names: tuple
    mu: np.ndarray
    sd: np.ndarray
    beta: np.ndarray  # intercept first, on the standardised inputs

    @classmethod
    def fit(cls, X, y, names, l2: float = L2) -> "Frozen":
        X = np.asarray(X, float)
        mu, sd = X.mean(0), X.std(0)
        sd = np.where(sd > 1e-12, sd, 1.0)  # the module's own floor (apache_activity_survival._standardise)
        return cls(tuple(names), mu, sd, A.logit_fit((X - mu) / sd, np.asarray(y, float), l2))

    def predict(self, X) -> np.ndarray:
        return A.logit_predict(self.beta, (np.asarray(X, float) - self.mu) / self.sd)

    def raw(self) -> tuple[float, np.ndarray]:
        """Intercept and slopes on the original scale of the inputs."""
        slope = self.beta[1:] / self.sd
        return float(self.beta[0] - (slope * self.mu).sum()), slope


def criterion(auc_a: float, auc_b: float, ll_a: float, ll_b: float, margin: float = AUC_MARGIN) -> bool:
    """The pre-registered decision criterion: B beats A on held-out AUC by MORE than the margin AND B's log-loss is lower."""
    return bool(round(auc_b - auc_a, 12) > margin and ll_b < ll_a)  # rounded so that float noise cannot turn "exactly the margin" into "more"


def base_rate_scores(y_train, n_test: int) -> np.ndarray:
    return np.full(n_test, float(np.mean(y_train)))


def bootstrap(y, scores: dict[str, np.ndarray], *, draws: int = BOOT, seed: int = SEED) -> dict:
    """Resample test podlings (rows) with replacement; the predictions are fixed (frozen models).  For every draw with both
    classes: AUC and log-loss of each model.  Returns arrays and the number of draws skipped."""
    y = np.asarray(y)
    n = len(y)
    rng = np.random.default_rng(seed)
    auc = {k: [] for k in scores}
    ll = {k: [] for k in scores}
    skipped = 0
    for _ in range(draws):
        ix = rng.integers(0, n, n)
        yb = y[ix]
        if yb.min() == yb.max():
            skipped += 1
            continue
        for k, s in scores.items():
            sb = np.asarray(s)[ix]
            auc[k].append(A.auc_score(yb, sb))
            ll[k].append(A.logloss(yb, sb))
    return {"auc": {k: np.array(v) for k, v in auc.items()}, "ll": {k: np.array(v) for k, v in ll.items()}, "skipped": skipped}


def interval(x, level: float = 0.95) -> tuple[float, float]:
    a = (1 - level) / 2
    return float(np.quantile(x, a)), float(np.quantile(x, 1 - a))


# ------------------------------------------------------------------ the tables

def make_table(panel: A.Panel, W: int, *, conversation: bool = False) -> dict:
    """The module's landmark table (one row per resolved podling still incubating at month W), with the calendar start year,
    and (conversation=True) the Gini, top-3 share and member count of the development-list messages added from the module's
    `dev_messages` table, whose rows are the same podlings."""
    tab = A.landmark_table(panel, W=W)
    tab["cal_year"] = (panel.start_ym[tab["p"].astype(int)] // 12).astype(float)
    if conversation:
        d = A.landmark_table(panel, W=W, measure="dev_messages")
        assert np.array_equal(d["p"], tab["p"])
        tab["conv_n"], tab["conv_gini"], tab["conv_top3"] = d["n"], d["gini"], d["top3"]
    return tab


def counts_for(panel: A.Panel, W: int) -> dict:
    """Counts by set at every filter step, from the panel's labels and start dates (no feature is looked at)."""
    res = panel.resolved()
    cal = panel.start_ym[res] // 12
    out = {}
    for name, rng_ in (("train", TRAIN_YEARS), ("test", TEST_YEARS)):
        m = (cal >= rng_[0]) & (cal <= rng_[1])
        p = res[m]
        y = panel.label[p]
        stay = panel.exit_m[p] >= W
        out[name] = {"resolved": (int(y.sum()), int((1 - y).sum())), "incubating_at_W": (int(y[stay].sum()), int((1 - y[stay]).sum()))}
    out["outside"] = int(((cal < TRAIN_YEARS[0]) | ((cal > TRAIN_YEARS[1]) & (cal < TEST_YEARS[0])) | (cal > TEST_YEARS[1])).sum())
    return out


def run_case(tab: dict, models: dict[str, tuple], *, mask_extra=None, min_n: int = MIN_N, seed: int = SEED, draws: int = BOOT) -> dict:
    """Fit every model on the training rows, freeze, score the test rows once.  `tab` holds the columns the models name,
    `y`, `cal_year`, `n`; rows with n < min_n (and, if given, rows failing `mask_extra`) are dropped first.  Model names are
    free keys of `models`; the baseline is always '0'."""
    keep = tab["n"] >= min_n
    if mask_extra is not None:
        keep &= mask_extra
    tr_all, te_all = split_masks(tab["cal_year"])
    tr, te = keep & tr_all, keep & te_all
    ytr, yte = tab["y"][tr], tab["y"][te]
    R = {"n_train": int(tr.sum()), "n_test": int(te.sum()),
         "train_pos_neg": (int(ytr.sum()), int((1 - ytr).sum())), "test_pos_neg": (int(yte.sum()), int((1 - yte).sum())),
         "dropped": {"train": int((tr_all & ~keep).sum()), "test": int((te_all & ~keep).sum())},
         "models": {}, "scores": {}, "base_rate_train": float(ytr.mean()), "base_rate_test": float(yte.mean())}
    scores = {"0": base_rate_scores(ytr, int(te.sum()))}
    for name, cols in models.items():
        Xtr = np.column_stack([tab[c][tr] for c in cols])
        Xte = np.column_stack([tab[c][te] for c in cols])
        fz = Frozen.fit(Xtr, ytr, cols)
        scores[name] = fz.predict(Xte)
        b0, sl = fz.raw()
        R["models"][name] = {
            "features": cols, "beta_std": fz.beta.tolist(), "mu": fz.mu.tolist(), "sd": fz.sd.tolist(),
            "intercept_raw": b0, "slopes_raw": sl.tolist(),
            "train_auc": A.auc_score(ytr, fz.predict(Xtr)), "train_ll": A.logloss(ytr, fz.predict(Xtr)),
            "cv_auc_train": A.cv_auc(Xtr, ytr, folds=5, repeats=20, seed=seed, l2=L2),
        }
    R["scores"] = scores
    R["test"] = {
        k: {"auc": (0.5 if k == "0" else A.auc_score(yte, s)), "ll": A.logloss(yte, s), "mean_pred": float(np.mean(s))}
        for k, s in scores.items()
    }
    B = bootstrap(yte, scores, draws=draws, seed=seed)
    R["boot"] = B
    R["boot_ci"] = {"auc": {k: interval(v) for k, v in B["auc"].items()}, "ll": {k: interval(v) for k, v in B["ll"].items()}}
    if "A" in models and "B" in models:
        dauc = B["auc"]["B"] - B["auc"]["A"]
        dll = B["ll"]["B"] - B["ll"]["A"]
        R["diff"] = {
            "auc": R["test"]["B"]["auc"] - R["test"]["A"]["auc"], "auc_ci": interval(dauc), "auc_share_gt0": float((dauc > 0).mean()),
            "auc_share_gt_margin": float((dauc > AUC_MARGIN).mean()),
            "ll": R["test"]["B"]["ll"] - R["test"]["A"]["ll"], "ll_ci": interval(dll), "ll_share_lt0": float((dll < 0).mean()),
            "met": criterion(R["test"]["A"]["auc"], R["test"]["B"]["auc"], R["test"]["A"]["ll"], R["test"]["B"]["ll"]),
        }
    return R


def run_all(panel: A.Panel, log=print) -> dict:
    out: dict = {"counts12": counts_for(panel, 12), "counts6": counts_for(panel, 6)}
    log("primary (W = 12) ...")
    t12 = make_table(panel, 12, conversation=True)
    out["primary"] = run_case(t12, MODELS)
    log("secondary: conversation lead ...")
    ok = (t12["conv_n"] >= MIN_N) & np.isfinite(t12["conv_gini"])
    conv_models = {"A": ("ln_n",), "A+conv": ("ln_n", "conv_gini", "conv_top3")}
    out["conv"] = run_case(t12, conv_models, mask_extra=ok)
    cb = out["conv"]
    dauc = cb["boot"]["auc"]["A+conv"] - cb["boot"]["auc"]["A"]
    dll = cb["boot"]["ll"]["A+conv"] - cb["boot"]["ll"]["A"]
    cb["diff_conv"] = {"auc": cb["test"]["A+conv"]["auc"] - cb["test"]["A"]["auc"], "auc_ci": interval(dauc),
                       "ll": cb["test"]["A+conv"]["ll"] - cb["test"]["A"]["ll"], "ll_ci": interval(dll)}
    log("secondary: 6-month window ...")
    t6 = make_table(panel, 6)
    out["w6"] = run_case(t6, MODELS)
    log("exploratory ...")
    # (x1) include the podlings with fewer than 3 regular members, with ln(1 + n) in place of ln n
    t12x = dict(t12)
    t12x["ln1p_n"] = np.log1p(t12["n"])
    mods_x = {"A": ("ln1p_n",), "B": ("ln1p_n", "growth"), "C": ("ln1p_n", "growth", "cal_year")}
    tr_all, te_all = split_masks(t12["cal_year"])
    out["x_all_n"] = run_case(t12x, mods_x, min_n=0)
    out["x_all_n"]["note_n_included"] = int((t12["n"] < MIN_N)[tr_all | te_all].sum())
    return out


# ------------------------------------------------------------------ the report

def _f(x: float, d: int = 3) -> str:
    return f"{x:.{d}f}"


def _ci(ci, d: int = 3) -> str:
    return f"[{ci[0]:+.{d}f}, {ci[1]:+.{d}f}]"


def _ci_plain(ci, d: int = 3) -> str:
    return f"[{ci[0]:.{d}f}, {ci[1]:.{d}f}]"


def _counts_table(c: dict, W: int) -> str:
    rows = ["| set | resolved (graduated / retired) | still incubating at month %d (graduated / retired) |" % W, "|---|---|---|"]
    for name, label in (("train", "training: started 2003-2012"), ("test", "test: started 2013-2021")):
        r, s = c[name]["resolved"], c[name]["incubating_at_W"]
        rows.append(f"| {label} | {sum(r)} ({r[0]} / {r[1]}) | {sum(s)} ({s[0]} / {s[1]}) |")
    return "\n".join(rows)


def _score_table(R: dict, names: list[str], label) -> str:
    rows = ["| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | mean predicted | in-training AUC |", "|---|---|---|---|---|"]
    for k in names:
        t = R["test"][k]
        auc_ci = R["boot_ci"]["auc"][k]
        ll_ci = R["boot_ci"]["ll"][k]
        tr = R["models"].get(k, {}).get("train_auc")
        rows.append(f"| {label(k)} | {_f(t['auc'])} {_ci_plain(auc_ci)} | {_f(t['ll'])} {_ci_plain(ll_ci)} | {_f(t['mean_pred'])} | {'-' if tr is None else _f(tr)} |")
    return "\n".join(rows)


def _coef_table(R: dict, names: list[str], feat_label: dict) -> str:
    rows = ["| model | intercept (standardised) | coefficients on standardised inputs | raw intercept | raw slopes | training mean / sd of inputs | in-training 5-fold CV AUC |", "|---|---|---|---|---|---|---|"]
    for k in names:
        m = R["models"][k]
        cols = m["features"]
        std = ", ".join(f"{feat_label.get(c, c)} {b:+.3f}" for c, b in zip(cols, m["beta_std"][1:]))
        raw = ", ".join(f"{feat_label.get(c, c)} {b:+.4f}" for c, b in zip(cols, m["slopes_raw"]))
        ms = ", ".join(f"{feat_label.get(c, c)} {mu:.3f} / {sd:.3f}" for c, mu, sd in zip(cols, m["mu"], m["sd"]))
        rows.append(f"| {k} | {m['beta_std'][0]:+.3f} | {std} | {m['intercept_raw']:+.3f} | {raw} | {ms} | {_f(m['cv_auc_train'])} |")
    return "\n".join(rows)


def _decision_text(R: dict, tag: str) -> str:
    d = R["diff"]
    a, b = R["test"]["A"], R["test"]["B"]
    c1 = d["auc"] > AUC_MARGIN
    c2 = b["ll"] < a["ll"]
    verdict = "MET" if d["met"] else "NOT MET"
    return (
        f"**{tag}: the criterion is {verdict}.** B's held-out AUC {_f(b['auc'])} against A's {_f(a['auc'])}: difference {d['auc']:+.3f} "
        f"({'more' if c1 else 'not more'} than {AUC_MARGIN}). B's held-out log-loss {_f(b['ll'])} against A's {_f(a['ll'])}: difference {d['ll']:+.3f} "
        f"({'lower' if c2 else 'not lower'}). The criterion needs both; here {'both hold' if (c1 and c2) else ('only the AUC condition holds' if c1 else ('only the log-loss condition holds' if c2 else 'neither holds'))}."
    )


FEAT = {"ln_n": "ln n", "growth": "g", "cal_year": "start year", "conv_gini": "Gini (dev lists)", "conv_top3": "top-3 share (dev lists)", "ln1p_n": "ln(1+n)"}


def write_report(R: dict, panel: A.Panel, path: Path = RESULTS) -> str:
    P, C, W6, X = R["primary"], R["conv"], R["w6"], R["x_all_n"]
    L = []
    L.append("# Apache Incubator: the fitted case. Does first-year growth add out-of-time information about graduation beyond team size?\n")
    L.append(f"_Generated 2026-11-01 by `uv run python -m models.apache_fitted_case report` (seed {SEED}; {BOOT} bootstrap draws). Code: `sim/models/apache_fitted_case.py`; checks: `sim/tests/test_apache_fitted_case.py`. Built on `sim/models/apache_activity_survival.py` (loaders, member rule, landmark table, logistic fit, AUC and log-loss are imported, not changed). Data: the Apache Incubator sustainability dataset (CC BY 4.0, doi:10.5281/zenodo.5637530) and the ASF's `podlings.xml`; local-use-only, not in the repo; this file holds counts and statistics only, no name, address or message text._\n")
    L.append("**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). This is the single fitted case on which the team-scale half of that programme continues or stops: `models/00-v0.md` section 8 \"Team\".\n")
    L.append(rule_block())
    L.append("## Decisions the rule left open (taken before any fit)\n")
    for it in IMPLEMENTATION:
        L.append("- " + it)
    L.append("")
    L.append("**What had been seen before the rule was written (disclosure).** The in-sample work (`results/apache_activity_survival.md`) used all 207 podlings at risk at month 12, including the ones that are now the test set: size AUC 0.758, size + growth 0.768 (a paired edge of +0.010, 95% -0.012 to +0.033), the split by era with the shape results of each, and the conversation lead's era dependence (absent before 2013, present after). The rule, the criterion and the margin of 0.02 were fixed after seeing that, not before it. So the test set is out-of-time but not unseen: its in-sample aggregates were. No model is fitted on the 2013-2021 podlings here. The features of all podlings are built in one table (the module's landmark table), and the split is applied before any fit; no statistic that involves a test podling's outcome (AUC, log-loss, bootstrap) is computed until all models are frozen. The counts of the test set (labels and start dates only) are read first.\n")
    L.append("## Counts\n")
    c12 = R["counts12"]
    L.append(_counts_table(c12, 12))
    L.append(f"\n(Podlings started outside both ranges, resolved: {c12['outside']}; none is in either set. No podling is in both sets: the sets are disjoint by calendar year of the start.)\n")
    L.append("Used by the primary analysis (W = 12), after the module's condition of at least 3 regular members in months 0-11:\n")
    L.append("| set | podlings | graduated / retired | base rate of graduation | dropped for n < 3 |\n|---|---|---|---|---|")
    L.append(f"| training | {P['n_train']} | {P['train_pos_neg'][0]} / {P['train_pos_neg'][1]} | {_f(P['base_rate_train'])} | {P['dropped']['train']} |")
    L.append(f"| test | {P['n_test']} | {P['test_pos_neg'][0]} / {P['test_pos_neg'][1]} | {_f(P['base_rate_test'])} | {P['dropped']['test']} |\n")
    L.append("## Frozen coefficients (fitted on the training set only)\n")
    L.append("Inputs are standardised on the training set (mean and standard deviation in the last-but-one column); the coefficients act on the standardised inputs; the raw columns are the same model on the original scale (ln n, g in log-ratio units, calendar year). Logistic, ridge penalty 1 (the module's default, not tuned). Sign: positive goes with graduation.\n")
    L.append(_coef_table(P, ["A", "B", "C"], FEAT))
    L.append("")
    L.append("## Held-out result (test set, scored once)\n")
    L.append(f"Test set: {P['n_test']} podlings, {P['test_pos_neg'][0]} graduated and {P['test_pos_neg'][1]} retired. Intervals: bootstrap of the test podlings, {BOOT} draws ({P['boot']['skipped']} skipped for one class), models frozen.\n")
    L.append(_score_table(P, ["0", "A", "B", "C"], lambda k: NAMES[k]))
    d = P["diff"]
    L.append("")
    L.append("**B minus A (the decisive contrast).**\n")
    L.append("| quantity | point | 95% bootstrap interval | share of draws |\n|---|---|---|---|")
    L.append(f"| AUC, B - A | {d['auc']:+.3f} | {_ci(d['auc_ci'])} | above 0: {d['auc_share_gt0']:.3f}; above 0.02: {d['auc_share_gt_margin']:.3f} |")
    L.append(f"| log-loss, B - A | {d['ll']:+.3f} | {_ci(d['ll_ci'])} | below 0: {d['ll_share_lt0']:.3f} |\n")
    L.append("## Decision, exactly per the criterion\n")
    L.append("Criterion (rule item 3): B beats A on held-out AUC by more than 0.02 AND B's log-loss is lower than A's.\n")
    L.append(_decision_text(P, "Decision"))
    L.append("")
    for k in ("C",):
        L.append(f"For reference only (not part of the criterion): C against A, AUC {P['test']['C']['auc'] - P['test']['A']['auc']:+.3f}, log-loss {P['test']['C']['ll'] - P['test']['A']['ll']:+.3f}; C against B, AUC {P['test']['C']['auc'] - P['test']['B']['auc']:+.3f}, log-loss {P['test']['C']['ll'] - P['test']['B']['ll']:+.3f}.\n")
    L.append("## Secondary (reported, not decisive)\n")
    L.append("### S1. The conversation-concentration lead, same frozen protocol\n")
    L.append(f"Development-list messages, automated senders removed, W = 12; Gini and top-3 share of the development-list members' totals added to A's ln n. Needs at least 3 regular development-list members, so scored on a subset of the same held-out set: training {C['n_train']} podlings ({C['train_pos_neg'][0]} / {C['train_pos_neg'][1]}), test {C['n_test']} ({C['test_pos_neg'][0]} / {C['test_pos_neg'][1]}); lost to the extra condition (beyond n >= 3 in events): {C['dropped']['train']} training and {C['dropped']['test']} test. A is re-fitted and re-scored on this subset.\n")
    L.append(_coef_table(C, ["A", "A+conv"], FEAT))
    L.append("")
    L.append(_score_table(C, ["0", "A", "A+conv"], lambda k: {"0": NAMES["0"], "A": "A on this subset", "A+conv": "A + Gini + top-3 (development lists)"}[k]))
    dc = C["diff_conv"]
    L.append(f"\nA+conv minus A: AUC {dc['auc']:+.3f} {_ci(dc['auc_ci'])}; log-loss {dc['ll']:+.3f} {_ci(dc['ll_ci'])}. Read against the lead's own rule (gain above 0.02 AUC): {'above' if dc['auc'] > AUC_MARGIN else 'not above'} 0.02. This is the lead of `results/apache_activity_survival.md` 7.4 on podlings that were part of its in-sample data (the test era 2013-2021 is the era where the lead was present in-sample); it was found in a search of 42 variants and is NOT the confirmation on podlings after July 2021 that that file asks for. The lead's own rule also needs a one-sided permutation p, which is not computed here.\n")
    L.append("### S2. The same four models with a 6-month feature window\n")
    c6 = R["counts6"]
    L.append(f"W = 6: features from months 0-5 (n: active in at least 2 of the 6 months; g: months 3-5 against months 0-2). Population: still incubating at month 6 with at least 3 regular members. Training {W6['n_train']} ({W6['train_pos_neg'][0]} / {W6['train_pos_neg'][1]}), test {W6['n_test']} ({W6['test_pos_neg'][0]} / {W6['test_pos_neg'][1]}); dropped for n < 3: {W6['dropped']['train']} training, {W6['dropped']['test']} test. Resolved podlings still incubating at month 6: training {sum(c6['train']['incubating_at_W'])}, test {sum(c6['test']['incubating_at_W'])}.\n")
    L.append(_coef_table(W6, ["A", "B", "C"], FEAT))
    L.append("")
    L.append(_score_table(W6, ["0", "A", "B", "C"], lambda k: NAMES[k]))
    d6 = W6["diff"]
    L.append(f"\nB minus A: AUC {d6['auc']:+.3f} {_ci(d6['auc_ci'])}; log-loss {d6['ll']:+.3f} {_ci(d6['ll_ci'])}.\n")
    L.append(_decision_text(W6, "The criterion applied to the 6-month window (secondary, not decisive)"))
    L.append("")
    L.append("## Exploratory (nothing here was pre-specified)\n")
    L.append("- **Population sensitivity.** The primary drops podlings with fewer than 3 regular members (five of the six in-sample were retired). Re-running A, B, C with those podlings included and ln(1 + n) in place of ln n (the same frozen protocol):\n")
    xd = X["diff"]
    L.append(f"  training {X['n_train']} ({X['train_pos_neg'][0]} / {X['train_pos_neg'][1]}), test {X['n_test']} ({X['test_pos_neg'][0]} / {X['test_pos_neg'][1]}); held-out AUC A {_f(X['test']['A']['auc'])}, B {_f(X['test']['B']['auc'])}, C {_f(X['test']['C']['auc'])}; log-loss A {_f(X['test']['A']['ll'])}, B {_f(X['test']['B']['ll'])}, C {_f(X['test']['C']['ll'])}; B - A in AUC {xd['auc']:+.3f} {_ci(xd['auc_ci'])}. (The criterion read on this population: {'met' if xd['met'] else 'not met'}.)")
    L.append("- **Calibration across the eras.** Training base rate of graduation " + _f(P['base_rate_train']) + ", test " + _f(P['base_rate_test']) + " (the base rate itself barely moved); mean predicted probability on the test set: A " + _f(P['test']['A']['mean_pred']) + ", B " + _f(P['test']['B']['mean_pred']) + ", C " + _f(P['test']['C']['mean_pred']) + ". C's higher mean comes from extrapolating the start-year slope into 2013-2021.")
    L.append("- **Fit against transfer.** In-training AUC against held-out AUC: A " + _f(P['models']['A']['train_auc']) + " against " + _f(P['test']['A']['auc']) + ", B " + _f(P['models']['B']['train_auc']) + " against " + _f(P['test']['B']['auc']) + ", C " + _f(P['models']['C']['train_auc']) + " against " + _f(P['test']['C']['auc']) + " (in-training 5-fold CV AUC in the coefficient table). The size signal travelled to 2013-2021 about intact.\n")
    L.append("## Caveats\n")
    L.append("- **Size is close to a tautology.** The number of people active in the first year is part of what 'a project that thrives' means; a podling that has not drawn three regular members by month 12 is already, in most senses, failing. Size predicting graduation is the expected result and is no support for any mechanism of the algebra. What the criterion tests is narrower: whether the direction of the first-year trend adds anything out of time.")
    L.append("- **The outcome labels are an institution's.** Graduated is a vote of the Incubator; retired is mostly an administrative closing after a project has gone quiet (L4632: dissolution against success, not a split). Activity is both a symptom and a cause of the label, the exit month's mail is partly about the exit, and the dataset holds only podlings resolved by mid-2021, so the 2013-2021 test set is a closed cohort in which the slowest outcomes are missing.")
    L.append("- **Era drift.** The Incubator's practice, tooling and the places where work is recorded changed between the two periods (more of the discussion in trackers and pull requests); the base rate of graduation is nearly the same in the two periods (see above) but what produces it need not be, the commit file starts in 2005 (nine early podlings have no first-year commits, all in the training period), and model C extrapolates the start year beyond the range on which it was fitted.")
    L.append(f"- **The test set is small.** {P['n_test']} podlings, {P['test_pos_neg'][1]} of them retired. A difference of 0.02 in AUC is well inside the sampling noise of one AUC from a sample this size (the interval of B - A above shows how much); the decision is therefore made on a rule that cannot separate small true effects from nothing, and the interval, not the verdict word, is the information. The bootstrap resamples podlings with the models fixed, so it leaves out the variation from re-fitting on another training set.")
    L.append("- **The test era was not unseen** (disclosure above), and the margin 0.02 and the criterion were written knowing the in-sample edge was +0.010.")
    L.append("- **One pseudonym per address, activity not effort, 'regular member' a window choice**: as in `results/apache_activity_survival.md` section 8, unchanged here.")
    L.append("- **A refutation here is of the proxy only.** The dataset records no anchoring, no enemy weight and no tie signs; nothing in this file touches the certificate of `models/00-v0.md` 7.5. What the criterion decides is whether first-year growth, as the measurable of 1.1, carries out-of-time information about exit beyond size on this population.\n")
    L.append("## Reproduce\n")
    L.append("    cd sim\n    ~/.local/bin/uv run python -m models.apache_fitted_case rule      # once: writes the rule into this file, no number\n    ~/.local/bin/uv run python -m models.apache_fitted_case report    # fits, freezes, scores once; about a minute\n    ~/.local/bin/uv run pytest -q\n")
    text = "\n".join(L)
    path.write_text(text)
    return text


def write_rule_stub(path: Path = RESULTS) -> None:
    if path.exists() and RULE_TEXT in path.read_text():
        print(f"the rule is already in {path}")
        return
    path.write_text(
        "# Apache Incubator: the fitted case. Does first-year growth add out-of-time information about graduation beyond team size?\n\n"
        "_Stub written before any fit. No number has been computed. `report` replaces everything below the rule._\n\n" + rule_block()
    )
    print(f"wrote the rule to {path}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rule", help="write the rule (verbatim) to results/apache_fitted_case.md, before any fit")
    sub.add_parser("report", help="fit on the training set, freeze, score the test set once, write the results file")
    args = ap.parse_args(argv)
    if args.cmd == "rule":
        write_rule_stub()
    else:
        if not RESULTS.exists() or RULE_TEXT not in RESULTS.read_text():
            raise SystemExit("run `rule` first: the rule must be in results/apache_fitted_case.md before any number is computed")
        if not (A.DERIVED / "meta.json").exists():
            raise SystemExit("derived/ is absent: run the activity module's `fetch` and `build` first")
        panel = A.Panel()
        R = run_all(panel)
        write_report(R, panel)
        print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
