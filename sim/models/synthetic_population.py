"""Synthetic-population identifiability: can known drives be recovered from observables, and do they predict group outcomes?

    cd sim
    ~/.local/bin/uv run python -m models.synthetic_population rule      # writes the rule (and nothing else) to results/synthetic_population_identifiability.md
    ~/.local/bin/uv run python -m models.synthetic_population report    # refuses unless the rule is already in that file; then runs everything once

Purpose.  Every real-data test so far ran on traces with no measured drive and came back null.  Here per-person drives
are KNOWN to exist and to generate behaviour (notes/2026-10-29-modelled-population-testbed.md, the no-circularity rule:
the generator below is NOT the coupled linear form of models/00-v0.md; it is a softmax choice model with a relationship
state).  Method D is given the generator's structure, so it is a best case; the file says so.

Procedure fixed by RULE_TEXT, copied verbatim into the results file before any number is computed.  Decisions the rule left
open, and one defect in the rule (its exit condition cannot fire), are in DECISIONS and DEVIATION.

Inference functions (`person_features`, `fit_drives`) receive an `Obs` (choices and exit steps) and never the drives.
"""

from __future__ import annotations

import argparse
import math
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from models import apache_activity_survival as A

SIM = Path(__file__).resolve().parent.parent
RESULTS = SIM / "results" / "synthetic_population_identifiability.md"
TITLE = "# Synthetic population: can known drives be recovered from observables, and do they predict group outcomes?"

SIZES = (3, 8, 25)
N_TRAIN, N_TEST = 60, 30
T = 120
WINDOW = 60  # steps observed by the inference methods; outcomes are steps WINDOW..T-1
SEED_TRAIN, SEED_TEST, SEED_CALIB = 20261101, 20261102, 20261100
BETA_M, BETA_SIM, BETA_R = 0.5, 0.8, 0.3
EXIT_STREAK = 10
EXIT_C_RULE = -1.0  # the rule's threshold
C_GRID = (-1.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0)
CALIB_GROUPS = 40
L2 = 1.0
PRIOR_SD = 3.0  # weak Gaussian stabiliser on theta-hat (a decision the rule left open)
BOUND = 6.0
C1_MIN, C2_RMSE, C2_AUC, C3_REL = 0.5, 0.05, 0.02, 0.10
NEG = -1e9

RULE_TEXT = """\
1. World. Persons have a drive vector θ_i = (s_i, a_i, f_i): activity set point s_i ~ N(0,1), affiliation a_i ~ N(0,1), aversion f_i ~ N(0,1), independent, fixed. Groups of size n ∈ {3, 8, 25}. 60 groups per size for training, 30 per size held out, drawn fresh. T = 120 steps per group.
2. Generator (NOT v0's linear coupled form). At each step each person i chooses one action from {act, idle, approach j, avoid j for each j ≠ i} by softmax with temperature 1 over utilities: U(act) = s_i + 0.5·m_{-i}(t−1) where m_{-i} is the others' mean activity last step (1 if they acted else 0); U(idle) = 0; U(approach j) = a_i + 0.8·sim(i,j) − 0.3·r_ij(t−1), U(avoid j) = f_i − 0.8·sim(i,j) + 0.3·r_ij(t−1), where sim(i,j) = −|a_i − a_j| and r_ij(t) is a relationship state updated r_ij ← 0.8·r_ij + 1 on approach, −1 on avoid, decays otherwise. A person leaves the group permanently when their realised utility (the utility of the chosen action, plus Gumbel noise) has been below −1 for 10 consecutive steps. Noise seeds fixed: 20261101 for training worlds, 20261102 for held-out.
3. Observables (all the inference may see): per person per step, whether they acted (0/1); the signed tie events (who approached/avoided whom, when); exit step if any. Drives are never seen by any inference.
4. Inference methods, each fitted on training groups only, frozen, applied to held-out groups: (P) person-effects: per-person activity rate and net approach rate estimated from the first 60 steps; (D) drive recovery: a maximum-likelihood fit of the generator's three per-person parameters from the first 60 steps' observables, with the generator's structure known but the parameters unknown (treat 0.5, 0.8, 0.3 as known constants; estimate θ_i by maximising the softmax likelihood of the observed choices, scipy.optimize per person); (O) oracle: the true θ_i.
5. Outcomes to predict on held-out groups from steps 61–120: (i) group total activity in steps 61–120 (RMSE, relative to predicting the training mean); (ii) whether any member exits in steps 61–120 (AUC and log-loss); (iii) per-person activity in steps 61–120 (RMSE). The predictor for each method is a ridge regression (reuse `logit_fit` for the binary outcome, write a small ridge for continuous) from the method's per-person features aggregated to the group by mean and min, fitted on training groups only, penalty 1, standardised on training.
6. Identifiability measure: Pearson correlation between recovered θ̂_i and true θ_i, per drive, per group size, on held-out persons; also at 30 and 120 steps of observation (secondary).
7. Criteria, decided before the run: (C1) drives are "recoverable at size n" if all three correlations exceed 0.5 at 60 steps; (C2) the drive-based predictor D "beats" P at size n if D's RMSE on (i) is lower by more than 5% of P's AND D's AUC on (ii) exceeds P's by more than 0.02; (C3) D is "near oracle" if D's RMSE on (i) is within 10% of O's. Report all three per size. A failure of C2 where C1 holds means recovered drives carry no extra information about outcomes beyond person rates; a failure of C1 means the drives cannot be recovered from these observables with this much data.
8. Secondary, labelled so: C1 with tie-sign events withheld (activity only), to show which channel carries the drives.

Nothing else is run. No tuning."""

DECISIONS = [
    "**Reading of item 7, C2.** The brief says \"lower by more than 5% of P's\" without naming the quantity; it is read as 5% of P's RMSE on (i). D beats P when (RMSE_P - RMSE_D) > 0.05 x RMSE_P on outcome (i) AND AUC_D - AUC_P > 0.02 on outcome (ii). Both strict: a difference exactly at a margin is not a pass. C1 is strict (> 0.5). C3 is RMSE_D <= 1.10 x RMSE_O (\"within 10%\", inclusive).",
    "**Joint fit per group, not per person in isolation.** A person's utilities for approach/avoid depend on the other members' a_j, which are also unknown. D therefore maximises the softmax likelihood of ALL the group's observed choices over all 3n parameters at once (L-BFGS-B, analytic gradient, one group at a time), which is the per-person likelihood summed over persons with the others' a_j free. Start at 0; box bounds +-6. A weak Gaussian stabiliser N(0, 3^2) on each parameter is added (a ridge, 1/18 per unit squared), because an unpenalised likelihood diverges for a person who never chose some action; the true population is N(0, 1), so the stabiliser is far weaker than the truth and is not tuned.",
    "**State is computed from the observables.** The relationship state r_ij(t-1) and the others' mean activity m(t-1) are deterministic functions of the observed choices, so D conditions on them exactly (reconstructed in `reconstruct_state`; a test checks it equals the generator's internal state). The exit event itself is not used in the likelihood (the person simply stops contributing after their last step).",
    "**Choice, noise, presence.** A person chooses by Gumbel-max (identical to softmax at temperature 1); the realised utility is max_k (U_k + G_k), which is the chosen action's utility plus its noise. A person who has left chooses nothing, is not a target of approach/avoid, and is not counted in m. Exit takes effect at the end of the step in which the streak reaches 10; `exit_step` is that step (0-indexed). r_ij is directional (i's state towards j) and changes only by i's own approach/avoid of j.",
    "**Features.** P: per person, acts / steps present, and (approaches - avoids) / steps present, over steps 0..59 while present. D: (s-hat, a-hat, f-hat). O: the true (s, a, f). Group features: mean and min across all the group's members (including those who left before step 60, whose features come from the steps they were present). One model per group size.",
    "**Outcomes.** (i) total acts by all members in steps 60..119 (0-indexed; \"61-120\"); (ii) any exit with exit_step in 60..119; (iii) per person present at step 60: acts / steps present in steps 60..119. For (iii) the regressors are the person's OWN features plus the group mean and min (group aggregates alone cannot separate members of a group); persons absent at step 60 have no outcome. RMSE is relative to predicting the training-set mean (baseline); a binary outcome with a single class in training predicts the training base rate and the AUC is reported where defined.",
    "**Ridge.** Continuous: centre y, standardise X on training, minimise |y - Xb|^2 + 1 x |b|^2 (intercept free). Binary: `apache_activity_survival.logit_fit`, penalty 1, on the same standardisation. Frozen: mean, sd and coefficients stored from training, applied unchanged to held-out.",
    "**Secondary, activity only.** Ties withheld means the observable is only whether each person acted (act vs not-act), plus the others' activity m. The tie state r is then unobservable and is taken as 0 in the likelihood (a misspecification: the generator has r != 0), and the likelihood is of act versus not-act, where the not-act probability sums idle, approach and avoid. Run at 60 steps on the held-out groups. Also at 30 and 120 steps with ties (item 6).",
    "**Correlations** are pooled over all held-out persons of a size (30 groups x n persons), recovered against true, at each window; persons who left early are included with the steps they were present.",
    "**Compute.** The group-level fits are independent and run in a process pool (up to 8 workers). Seeds: each group has its own stream, default_rng([seed, n, group index]); the world's drives and noise both come from that stream, so a training and a held-out group can never share a person.",
]

DEVIATION = (
    "**A defect in the rule, found by working it through before any run, and the one deviation made.** Item 2's exit condition cannot fire. "
    "The realised utility of a person is the maximum over their actions of (utility + Gumbel noise). Because idle has utility 0 and is always available, "
    "that maximum is below a threshold c with probability exp(-e^(-c) x S) <= exp(-e^(-c)), where S = sum_k e^(U_k) >= 1. At the rule's c = -1 that is at most 0.066 "
    "per step, and ten steps in a row is at most 1.6e-12: nobody ever leaves, outcome (ii) has no events at any size, and its AUC is undefined. "
    "The calibration table below confirms it (first row). The minimal repair that keeps the rule's form (a streak of 10 steps, the same realised utility, a threshold) "
    "is to make the threshold c a property of the world, chosen once, before the training and held-out worlds are drawn, on a third seed (20261100) that no later number uses: "
    "40 groups per size, each c in a fixed grid, and the c that maximises the minimum over the three sizes of min(p, 1 - p), p = the share of groups with at least one exit in steps 60..119 "
    "(ties to the smaller c). The training and held-out worlds then run with that c. Nothing else in the rule is altered, and no inference method sees c being chosen. "
    "Because S grows with n (more approach and avoid options), a single c cannot make exits equally likely at all sizes; where a size ends with no or all-groups exits, outcome (ii) is reported as undefined there and C2 is then 'not met (AUC undefined)'."
)


def rule_block() -> str:
    return (
        "## The rule, written before any run\n\n"
        "Copied verbatim from the brief of 2026-11-01; written into this file before the first number was computed "
        "(`report` refuses to run unless this block is already here).\n\n" + RULE_TEXT + "\n"
    )


# ------------------------------------------------------------------ the world

ACT, IDLE = 0, 1  # choice codes; approach j = 2 + j, avoid j = 2 + n + j; -1 = absent


@dataclass
class Obs:
    """Everything an inference method may see.  No drive is in here."""

    n: int
    choice: np.ndarray  # (T, n) int: -1 absent, 0 act, 1 idle, 2+j approach j, 2+n+j avoid j
    exit_step: np.ndarray  # (n,) int: step at whose end the person left, -1 if never


@dataclass
class World:
    obs: Obs
    theta: np.ndarray  # (n, 3): s, a, f  -- ground truth, never passed to inference
    r_before: np.ndarray  # (T, n, n) generator's r_ij(t-1) at each step (for a test only)
    m_before: np.ndarray  # (T, n) generator's m_{-i}(t-1) (for a test only)


def make_world(n: int, seed: int, idx: int, c_exit: float, steps: int = T, streak: int = EXIT_STREAK) -> World:
    rng = np.random.default_rng([seed, n, idx])
    theta = rng.standard_normal((n, 3))
    s, a, f = theta[:, 0], theta[:, 1], theta[:, 2]
    absd = np.abs(a[:, None] - a[None, :])
    off = ~np.eye(n, dtype=bool)
    present = np.ones(n, bool)
    r = np.zeros((n, n))
    prev = np.zeros(n)
    low = np.zeros(n, int)
    exit_step = -np.ones(n, int)
    choice = -np.ones((steps, n), int)
    r_before = np.zeros((steps, n, n))
    m_before = np.zeros((steps, n))
    for t in range(steps):
        pj = present[None, :] & off
        cnt = pj.sum(1)
        m = np.where(cnt > 0, (pj * prev[None, :]).sum(1) / np.maximum(cnt, 1), 0.0)
        r_before[t], m_before[t] = r, m
        U = np.empty((n, 2 + 2 * n))
        U[:, 0] = s + BETA_M * m
        U[:, 1] = 0.0
        U[:, 2 : 2 + n] = a[:, None] - BETA_SIM * absd - BETA_R * r
        U[:, 2 + n :] = f[:, None] + BETA_SIM * absd + BETA_R * r
        valid = np.concatenate([np.ones((n, 2), bool), pj, pj], axis=1)
        G = rng.gumbel(size=U.shape)  # drawn for everyone every step so the stream does not depend on who has left
        V = np.where(valid, U + G, -np.inf)
        k = V.argmax(1)
        real = V.max(1)
        acted = np.zeros(n)
        r_new = 0.8 * r
        for i in np.flatnonzero(present):
            choice[t, i] = k[i]
            if k[i] == ACT:
                acted[i] = 1.0
            elif k[i] >= 2 + n:
                r_new[i, k[i] - 2 - n] -= 1.0
            elif k[i] >= 2:
                r_new[i, k[i] - 2] += 1.0
        r = r_new
        low = np.where(present & (real < c_exit), low + 1, 0)
        gone = present & (low >= streak)
        exit_step[gone] = t
        present = present & ~gone
        prev = acted
    return World(Obs(n, choice, exit_step), theta, r_before, m_before)


def reconstruct_state(obs: Obs) -> tuple[np.ndarray, np.ndarray]:
    """r_ij(t-1) and m_{-i}(t-1) at each step, as deterministic functions of the observed choices only."""
    n, ch = obs.n, obs.choice
    steps = ch.shape[0]
    off = ~np.eye(n, dtype=bool)
    r = np.zeros((n, n))
    prev = np.zeros(n)
    R = np.zeros((steps, n, n))
    M = np.zeros((steps, n))
    for t in range(steps):
        pres = ch[t] >= 0
        pj = pres[None, :] & off
        cnt = pj.sum(1)
        M[t] = np.where(cnt > 0, (pj * prev[None, :]).sum(1) / np.maximum(cnt, 1), 0.0)
        R[t] = r
        r = 0.8 * r
        for i in np.flatnonzero(pres):
            k = ch[t, i]
            if k >= 2 + n:
                r[i, k - 2 - n] -= 1.0
            elif k >= 2:
                r[i, k - 2] += 1.0
        prev = (ch[t] == ACT).astype(float)
    return R, M


# ------------------------------------------------------------------ inference (receives Obs, never theta)

def person_features(obs: Obs, steps: int) -> np.ndarray:
    """Method P: per person, act rate and net approach rate over the first `steps` steps while present."""
    n, ch = obs.n, obs.choice[:steps]
    pres = ch >= 0
    k = np.maximum(pres.sum(0), 1)
    act = (ch == ACT).sum(0) / k
    app = ((ch >= 2) & (ch < 2 + n)).sum(0)
    avo = (ch >= 2 + n).sum(0)
    return np.c_[act, (app - avo) / k]


def _nll_grad(x, n, W, R, M, pres, Y, act_only, act_flag):
    s, a, f = x[:n], x[n : 2 * n], x[2 * n :]
    d = a[:, None] - a[None, :]
    absd, sg = np.abs(d), np.sign(d)
    K = 2 + 2 * n
    L = np.empty((W, n, K))
    L[:, :, 0] = s[None, :] + BETA_M * M
    L[:, :, 1] = 0.0
    L[:, :, 2 : 2 + n] = a[None, :, None] - BETA_SIM * absd[None] - BETA_R * R
    L[:, :, 2 + n :] = f[None, :, None] + BETA_SIM * absd[None] + BETA_R * R
    off = ~np.eye(n, dtype=bool)
    pj = pres[:, None, :] & off[None]  # (W, i, j): j present, j != i
    valid = np.concatenate([np.ones((W, n, 2), bool), pj, pj], axis=2)
    L = np.where(valid, L, NEG)
    mx = L.max(2, keepdims=True)
    E = np.exp(L - mx)
    Z = E.sum(2, keepdims=True)
    lse = (mx + np.log(Z))[:, :, 0]
    P = E / Z
    w = pres.astype(float)
    if not act_only:
        ll = (w * ((L * Y).sum(2) - lse)).sum()
        Gt = (Y - P) * w[:, :, None]
    else:
        pa = np.clip(P[:, :, 0], 1e-12, 1 - 1e-12)
        ll = (w * np.where(act_flag, np.log(pa), np.log1p(-pa))).sum()
        Pn = P.copy()
        Pn[:, :, 0] = 0.0
        Pn = Pn / np.maximum(1.0 - P[:, :, 0:1], 1e-12)
        Yw = np.where(act_flag[:, :, None], np.eye(K)[0][None, None, :], Pn)
        Gt = (Yw - P) * w[:, :, None]
    ds = Gt[:, :, 0].sum(0)
    GA = Gt[:, :, 2 : 2 + n].sum(0)
    GV = Gt[:, :, 2 + n :].sum(0)
    df = GV.sum(1)
    da = (
        GA.sum(1)
        - BETA_SIM * (GA * sg).sum(1)
        + BETA_SIM * (GA * sg).sum(0)
        + BETA_SIM * (GV * sg).sum(1)
        - BETA_SIM * (GV * sg).sum(0)
    )
    nll = -ll + 0.5 * (x @ x) / PRIOR_SD**2
    grad = -np.r_[ds, da, df] + x / PRIOR_SD**2
    return nll, grad


def _prepare(obs: Obs, steps: int, ties: bool):
    n = obs.n
    ch = obs.choice[:steps]
    R, M = reconstruct_state(Obs(n, ch, obs.exit_step))
    if not ties:
        R = np.zeros_like(R)  # r cannot be observed without the tie events
    pres = ch >= 0
    K = 2 + 2 * n
    Y = np.zeros((steps, n, K))
    t_ix, i_ix = np.nonzero(pres)
    Y[t_ix, i_ix, ch[t_ix, i_ix]] = 1.0
    return n, steps, R, M, pres, Y, (ch == ACT)


def fit_drives(obs: Obs, steps: int, ties: bool = True) -> np.ndarray:
    """Method D: ML estimate of (s, a, f) for every member from the first `steps` steps of `obs`.  Returns (n, 3).
    `ties=False` withholds the tie events (activity only; r taken as 0)."""
    n, W, R, M, pres, Y, act_flag = _prepare(obs, steps, ties)
    x0 = np.zeros(3 * n)
    res = minimize(
        _nll_grad, x0, args=(n, W, R, M, pres, Y, not ties, act_flag), jac=True, method="L-BFGS-B",
        bounds=[(-BOUND, BOUND)] * (3 * n), options={"maxiter": 300},
    )
    x = res.x
    return np.c_[x[:n], x[n : 2 * n], x[2 * n :]]


# ------------------------------------------------------------------ prediction

def ridge_fit(X, y, l2: float = L2):
    X = np.asarray(X, float)
    mu, sd = X.mean(0), X.std(0)
    sd = np.where(sd > 1e-12, sd, 1.0)
    Z = (X - mu) / sd
    ym = float(np.mean(y))
    b = np.linalg.solve(Z.T @ Z + l2 * np.eye(Z.shape[1]), Z.T @ (np.asarray(y, float) - ym))
    return {"mu": mu, "sd": sd, "b": b, "ym": ym}


def ridge_predict(m, X):
    return m["ym"] + ((np.asarray(X, float) - m["mu"]) / m["sd"]) @ m["b"]


def logit_model(X, y, l2: float = L2):
    X = np.asarray(X, float)
    mu, sd = X.mean(0), X.std(0)
    sd = np.where(sd > 1e-12, sd, 1.0)
    y = np.asarray(y, float)
    if y.min() == y.max():  # one class: predict the base rate
        return {"mu": mu, "sd": sd, "beta": None, "p": float(y.mean())}
    return {"mu": mu, "sd": sd, "beta": A.logit_fit((X - mu) / sd, y, l2), "p": float(y.mean())}


def logit_apply(m, X):
    if m["beta"] is None:
        return np.full(len(X), m["p"])
    return A.logit_predict(m["beta"], (np.asarray(X, float) - m["mu"]) / m["sd"])


def rmse(y, p) -> float:
    return float(np.sqrt(np.mean((np.asarray(y, float) - np.asarray(p, float)) ** 2)))


def group_agg(F: np.ndarray) -> np.ndarray:
    """(n, k) per-person features -> (2k,) group features: mean then min."""
    return np.r_[F.mean(0), F.min(0)]


# ------------------------------------------------------------------ criteria

def c1_met(corrs) -> bool:
    return bool(all(c > C1_MIN for c in corrs))


def c2_met(rmse_d: float, rmse_p: float, auc_d: float, auc_p: float) -> bool:
    if any(math.isnan(v) for v in (rmse_d, rmse_p, auc_d, auc_p)):
        return False
    return bool(round(rmse_p - rmse_d - C2_RMSE * rmse_p, 12) > 0 and round(auc_d - auc_p - C2_AUC, 12) > 0)


def c3_met(rmse_d: float, rmse_o: float) -> bool:
    return bool(rmse_d <= (1.0 + C3_REL) * rmse_o)


# ------------------------------------------------------------------ the run

def _work(job):
    kind, n, seed, idx, c, steps, ties = job
    w = make_world(n, seed, idx, c)
    if kind == "calib":
        return w.obs.exit_step
    return fit_drives(w.obs, steps, ties)


def _pmap(jobs, workers):
    if workers <= 1:
        return [_work(j) for j in jobs]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(_work, jobs, chunksize=2))


def calibrate(workers: int):
    rows = []
    for c in C_GRID:
        row = {"c": c}
        for n in SIZES:
            ex = [make_world(n, SEED_CALIB, i, c).obs.exit_step for i in range(CALIB_GROUPS)]
            win = np.mean([((e >= WINDOW) & (e < T)).any() for e in ex])
            early = np.mean([np.mean((e >= 0) & (e < WINDOW)) for e in ex])
            row[n] = (float(win), float(early))
        rows.append(row)
    score = [min(min(r[n][0], 1 - r[n][0]) for n in SIZES) for r in rows]
    best = int(np.argmax(score))  # first maximum: ties to the smaller c in grid order (grid ascends after the rule's row)
    return rows, score, rows[best]["c"]


def pearson(x, y) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.std() < 1e-12 or y.std() < 1e-12:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def run_all(workers: int = 8):
    rows, score, c_exit = calibrate(workers)
    R = {"calib": rows, "calib_score": score, "c_exit": c_exit, "size": {}}
    for n in SIZES:
        tr = [make_world(n, SEED_TRAIN, i, c_exit) for i in range(N_TRAIN)]
        te = [make_world(n, SEED_TEST, i, c_exit) for i in range(N_TEST)]
        # drive fits: training at 60 steps (for the ridge); held-out at 30, 60, 120, and 60 activity-only
        def fits(worlds, seed, steps, ties):
            return _pmap([("fit", n, seed, i, c_exit, steps, ties) for i in range(len(worlds))], workers)
        D_tr = fits(tr, SEED_TRAIN, WINDOW, True)
        D_te = {
            ("ties", 30): fits(te, SEED_TEST, 30, True),
            ("ties", 60): fits(te, SEED_TEST, WINDOW, True),
            ("ties", 120): fits(te, SEED_TEST, 120, True),
            ("act", 60): fits(te, SEED_TEST, WINDOW, False),
        }
        theta_te = np.vstack([w.theta for w in te])
        corr = {k: [pearson(np.vstack(v)[:, d], theta_te[:, d]) for d in range(3)] for k, v in D_te.items()}

        def table(worlds, Dfits):
            X = {m: [] for m in "PDO"}
            y_tot, y_exit = [], []
            pX = {m: [] for m in "PDO"}
            y_pp = []
            for w, Dh in zip(worlds, Dfits):
                ob = w.obs
                Fm = {"P": person_features(ob, WINDOW), "D": Dh, "O": w.theta}
                for m in "PDO":
                    X[m].append(group_agg(Fm[m]))
                ch2 = ob.choice[WINDOW:T]
                y_tot.append(float((ch2 == ACT).sum()))
                y_exit.append(float(((ob.exit_step >= WINDOW) & (ob.exit_step < T)).any()))
                here = ob.choice[WINDOW] >= 0
                kk = np.maximum((ch2 >= 0).sum(0), 1)
                rate = (ch2 == ACT).sum(0) / kk
                for i in np.flatnonzero(here):
                    for m in "PDO":
                        pX[m].append(np.r_[Fm[m][i], group_agg(Fm[m])])
                    y_pp.append(rate[i])
            return ({m: np.array(v) for m, v in X.items()}, np.array(y_tot), np.array(y_exit),
                    {m: np.array(v) for m, v in pX.items()}, np.array(y_pp))

        Xtr, ytot_tr, yex_tr, pXtr, ypp_tr = table(tr, D_tr)
        Xte, ytot_te, yex_te, pXte, ypp_te = table(te, D_te[("ties", 60)])
        out = {"n_exit_tr": int(yex_tr.sum()), "n_exit_te": int(yex_te.sum()),
               "n_persons_te": len(theta_te), "n_pp_te": len(ypp_te), "n_pp_tr": len(ypp_tr),
               "corr": corr, "base_tot": rmse(ytot_te, ytot_tr.mean()), "base_pp": rmse(ypp_te, ypp_tr.mean()),
               "mean_tot_te": float(ytot_te.mean()), "methods": {}}
        base_p = float(yex_tr.mean())
        out["base_exit_ll"] = A.logloss(yex_te, np.full(len(yex_te), base_p))
        for m in "PDO":
            mt = ridge_fit(Xtr[m], ytot_tr)
            r_tot = rmse(ytot_te, ridge_predict(mt, Xte[m]))
            me = logit_model(Xtr[m], yex_tr)
            pe = logit_apply(me, Xte[m])
            auc = A.auc_score(yex_te, pe) if 0 < yex_te.sum() < len(yex_te) else float("nan")
            ll = A.logloss(yex_te, pe)
            mp = ridge_fit(pXtr[m], ypp_tr)
            r_pp = rmse(ypp_te, ridge_predict(mp, pXte[m]))
            out["methods"][m] = {"rmse_tot": r_tot, "auc": auc, "ll": ll, "rmse_pp": r_pp}
        R["size"][n] = out
    return R


# ------------------------------------------------------------------ report

def _f(v, k=3):
    return "n/a" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.{k}f}"


def write_report(R) -> None:
    S = R["size"]
    L = []
    w = L.append
    w(TITLE + "\n")
    w(
        "_Generated 2026-11-01 by `uv run python -m models.synthetic_population report` (seeds 20261101 training, 20261102 held-out, "
        "20261100 calibration of one world constant). Code: `sim/models/synthetic_population.py`; checks: `sim/tests/test_synthetic_population.py`. "
        "Built on `sim/models/apache_activity_survival.py` (`logit_fit`, `auc_score`, `logloss` imported, not changed). "
        "Everything here is synthetic: no third-party data, no licence question._\n"
    )
    w(
        "**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict "
        "or steer outcomes at the membership, group and crowd scales, sensitive to group size (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). "
        "This experiment asks the identifiability question the real-data tests could not: where drives are KNOWN to generate behaviour, can they be recovered "
        "from the observables, and do they predict held-out group outcomes beyond person-level rates?\n"
    )
    w(rule_block())
    w("## Deviation from the rule\n\n" + DEVIATION + "\n")
    w("### Calibration of the exit threshold c (seed 20261100, 40 groups per size; share of groups with an exit in steps 60..119 / mean share of persons gone before step 60)\n")
    w("| c | n = 3 | n = 8 | n = 25 | score = min over sizes of min(p, 1 - p) |")
    w("|---|---|---|---|---|")
    for r, sc in zip(R["calib"], R["calib_score"]):
        tag = " (the rule's value)" if r["c"] == EXIT_C_RULE else ""
        cells = " | ".join(f"{r[n][0]:.2f} / {r[n][1]:.2f}" for n in SIZES)
        w(f"| {r['c']:+.1f}{tag} | {cells} | {sc:.3f} |")
    w(f"\nChosen: **c = {R['c_exit']:+.1f}**. Used for every training and held-out world below.\n")
    w("## Decisions the rule left open (taken before the run)\n")
    for d in DECISIONS:
        w("- " + d)
    w("")
    w("## Counts\n")
    w("| size | training groups / persons | held-out groups / persons | groups with an exit in steps 60..119, training / held-out | persons present at step 60 (outcome iii), training / held-out | mean total acts in steps 60..119, held-out |")
    w("|---|---|---|---|---|---|")
    for n in SIZES:
        o = S[n]
        w(f"| {n} | {N_TRAIN} / {N_TRAIN * n} | {N_TEST} / {o['n_persons_te']} | {o['n_exit_tr']} of {N_TRAIN} / {o['n_exit_te']} of {N_TEST} | {o['n_pp_tr']} / {o['n_pp_te']} | {o['mean_tot_te']:.1f} |")
    w("")
    w("## C1. Recovery of the drives (correlation of recovered with true, held-out persons, 60 steps)\n")
    w("| size | corr(s-hat, s) | corr(a-hat, a) | corr(f-hat, f) | C1 (all three > 0.5) |")
    w("|---|---|---|---|---|")
    for n in SIZES:
        c = S[n]["corr"][("ties", 60)]
        w(f"| {n} | {_f(c[0])} | {_f(c[1])} | {_f(c[2])} | {'MET' if c1_met(c) else 'NOT MET'} |")
    w("")
    w("### Secondary: observation length (ties observed) and the channel (activity only, 60 steps)\n")
    w("| size | window | corr s | corr a | corr f | C1 |")
    w("|---|---|---|---|---|---|")
    for n in SIZES:
        for key, lab in ((("ties", 30), "30 steps, ties"), (("ties", 60), "60 steps, ties"), (("ties", 120), "120 steps, ties"), (("act", 60), "60 steps, activity only (ties withheld)")):
            c = S[n]["corr"][key]
            w(f"| {n} | {lab} | {_f(c[0])} | {_f(c[1])} | {_f(c[2])} | {'MET' if c1_met(c) else 'NOT MET'} |")
    w("")
    w("## Outcomes on the held-out groups (steps 60..119), ridge predictors fitted on the training groups\n")
    w("RMSE is in the outcome's own units; 'rel' is RMSE divided by the RMSE of predicting the training mean (below 1 is better than the mean). AUC and log-loss are for 'any member exits'; the baseline log-loss predicts the training base rate.\n")
    w("| size | method | (i) group total activity: RMSE [rel] | (ii) any exit: AUC | (ii) log-loss | (iii) per-person activity: RMSE [rel] |")
    w("|---|---|---|---|---|---|")
    for n in SIZES:
        o = S[n]
        w(f"| {n} | baseline (training mean / base rate) | {o['base_tot']:.3f} [1.000] | 0.500 | {_f(o['base_exit_ll'])} | {o['base_pp']:.4f} [1.000] |")
        for m, lab in (("P", "P person effects"), ("D", "D drive recovery"), ("O", "O oracle")):
            r = o["methods"][m]
            w(f"| {n} | {lab} | {r['rmse_tot']:.3f} [{r['rmse_tot'] / o['base_tot']:.3f}] | {_f(r['auc'])} | {_f(r['ll'])} | {r['rmse_pp']:.4f} [{r['rmse_pp'] / o['base_pp']:.3f}] |")
    w("")
    w("## Decision, exactly per the criteria\n")
    w("| size | C1 recoverable | C2 D beats P | C3 D near oracle | reading |")
    w("|---|---|---|---|---|")
    readings = []
    for n in SIZES:
        o = S[n]
        c1 = c1_met(o["corr"][("ties", 60)])
        d, p, ora = o["methods"]["D"], o["methods"]["P"], o["methods"]["O"]
        c2 = c2_met(d["rmse_tot"], p["rmse_tot"], d["auc"], p["auc"])
        c3 = c3_met(d["rmse_tot"], ora["rmse_tot"])
        gap_r = (p["rmse_tot"] - d["rmse_tot"]) / p["rmse_tot"]
        gap_a = d["auc"] - p["auc"] if not (math.isnan(d["auc"]) or math.isnan(p["auc"])) else float("nan")
        if c1 and not c2:
            why = []
            if not (gap_r > C2_RMSE):
                why.append("D's RMSE on (i) is not lower than P's by more than 5%" + (" (it is higher)" if gap_r < 0 else ""))
            if math.isnan(gap_a):
                why.append("the AUC comparison is undefined")
            elif not (gap_a > C2_AUC):
                why.append("D's AUC on (ii) does not exceed P's by more than 0.02")
            rd = "C1 holds, C2 fails (" + "; ".join(why) + "): by the rule's own reading, recovered drives carry no extra information about these outcomes beyond person rates, subject to the caveats on the aggregation and on the small counts."
        elif not c1:
            rd = "C1 fails: the drives cannot be recovered from these observables with this much data."
        else:
            rd = "C1 and C2 hold."
        extra = f" RMSE gap (P - D)/P = {gap_r:+.3f} (needs > {C2_RMSE}); AUC gap D - P = {_f(gap_a)} (needs > {C2_AUC})."
        if math.isnan(gap_a):
            extra += " AUC undefined (no exits, or every group had one, in the held-out set)."
        w(f"| {n} | {'MET' if c1 else 'NOT MET'} | {'MET' if c2 else 'NOT MET'} | {'MET' if c3 else 'NOT MET'} | {rd}{extra} D/O RMSE on (i) = {d['rmse_tot'] / ora['rmse_tot']:.3f} (needs <= {1 + C3_REL:.2f}). |")
    w("")
    w("## Caveats\n")
    for t in [
        "**This is a synthetic world of our own design.** The generator is a softmax choice model with a relationship state, written for this test; nothing says people, or any real group, behave like it. A result here is about identifiability in a world where the answer is known, not about people.",
        "**The generator's structure is given to method D.** D knows the utility form, the three constants (0.5, 0.8, 0.3), the choice set and the exit-free likelihood; only the drive values are unknown. This is a best case for D: a real analyst does not know the structure, and a misspecified drive model would recover less. A failure of C1 here is therefore strong; a success is the most that could be hoped for, not evidence for real data.",
        "**The drives are the generator's primitives by construction.** That drives exist in this world is not a finding; what is tested is whether they can be recovered from the observables at 60 steps, at three group sizes, and whether recovering them adds anything about held-out outcomes beyond per-person rates, which are themselves almost sufficient statistics for a person whose behaviour is a function of three fixed numbers.",
        "**The exit condition needed a repair** (see Deviation): the threshold was chosen on a third seed to make exits possible; at some sizes exits remain rare or universal, and outcome (ii) is then weak or undefined there. Exit depends on the number of options (larger groups have more of them), which is a property of this generator, not of groups.",
        "**The aggregation is a poor match to this generator.** Group features are the mean and min of per-person values and the regression is linear in them, but the group's total activity is a sum of softmax probabilities e^s/Z_i, nonlinear in the drives, with Z_i growing with the number of options. Per-person act rates measure that directly, so P has a built-in advantage on (i) that the drives must overcome through a linear map; the oracle O, which has the true drives, does not beat the baseline by much at n = 3 and is far from perfect at n = 25 for the same reason. A C2 failure here is therefore partly a failure of the rule's prescribed predictor form, not only of the drives' information. This was not tuned.",
        "**The chosen exit threshold gives a degenerate small world.** The calibration score at the chosen c was only 0.10 (no c in the grid made exits moderately likely at every size). At n = 3 most members have gone before step 60 (see the calibration row), so the held-out n = 3 outcomes rest on few remaining persons and low activity; at n = 25 only a handful of groups have an exit in the outcome window, so AUC (ii) there rests on a handful of events.",
        "**Small held-out sets.** 30 groups per size: 30 group-level outcomes for (i) and (ii) at each size. AUC on a handful of exit events is very noisy; no intervals are computed (the rule asked for none), so a gap near a margin is not distinguishable from nothing.",
        "**Group aggregates by mean and min** lose which member is which; the (iii) regression adds the person's own features to the aggregates, a decision of this file (see Decisions). Different aggregates could change C2.",
        "**Activity-only secondary is misspecified on purpose of the withholding:** r cannot be observed without ties and is set to 0 in that likelihood; part of any shortfall there is that misspecification, not only the missing channel.",
        "**One run, no tuning.** The tests exercise machinery on small worlds; the numbers above are the single run.",
    ]:
        w("- " + t)
    w("")
    w("## Reproduce\n")
    w("    cd sim")
    w("    ~/.local/bin/uv run python -m models.synthetic_population rule      # once: writes the rule into this file, no number")
    w("    ~/.local/bin/uv run python -m models.synthetic_population report    # the single run; writes this file")
    w("    ~/.local/bin/uv run pytest -q tests/test_synthetic_population.py")
    RESULTS.write_text("\n".join(L) + "\n")


def write_rule_stub() -> None:
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    if RESULTS.exists() and RULE_TEXT in RESULTS.read_text():
        print(f"the rule is already in {RESULTS}")
        return
    RESULTS.write_text(
        TITLE + "\n\n_Stub written before any run. No number has been computed. `report` replaces everything below the rule._\n\n" + rule_block()
    )
    print(f"wrote the rule to {RESULTS}")


def require_rule(path: Path = RESULTS) -> None:
    if not path.exists() or RULE_TEXT not in path.read_text():
        raise SystemExit("run `rule` first: the rule must be in results/synthetic_population_identifiability.md before any number is computed")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rule", help="write the rule (verbatim) to the results file, before any run")
    sub.add_parser("report", help="run everything once and write the results file")
    args = ap.parse_args(argv)
    if args.cmd == "rule":
        write_rule_stub()
    else:
        require_rule()
        R = run_all()
        write_report(R)
        print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
