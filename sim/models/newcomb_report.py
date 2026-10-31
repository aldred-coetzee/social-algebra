"""Run the Newcomb n = 3 test end to end and write sim/results/newcomb_n3.md.

    cd sim
    ~/.local/bin/uv run python -m models.newcomb_report fetch     # local-use-only download, git-ignored
    ~/.local/bin/uv run python -m models.newcomb_report report    # ~2 minutes; writes results/newcomb_n3.md

Everything computed lives in models/newcomb.py (ledger ids L4471-L4546 are cited there); this module
only organises the runs and formats the tables.  Seeded: the numbers in the results file are
reproduced exactly by the same command.  Only computed statistics are written out (counts,
rates, p-values), never the rank or signed matrices, which are not ours to redistribute [L4544].
"""
from __future__ import annotations

import argparse
import datetime
from pathlib import Path

import numpy as np
from scipy.stats import fisher_exact

from models import newcomb as nc

SEED = 20261031
N_DRAWS = 10_000
RESULTS = Path(__file__).resolve().parents[1] / "results" / "newcomb_n3.md"
CELLS = {
    "triple": (nc.TRIPLE_LEVEL, None),
    "sum": (nc.TRIANGLE_LEVEL, "sum"),
    "agree": (nc.TRIANGLE_LEVEL, "agree"),
}
CELL_TITLE = {
    "triple": "directed D&K triples",
    "sum": "triangles, 'sum' rule",
    "agree": "triangles, 'agree' rule",
}
WINDOWS = ("all", "early", "late", "nogap")
WINDOW_TITLE = {
    "all": "all 14 transitions",
    "early": "first 5 (waves 1-6)",
    "late": "last 9 (waves 6-15)",
    "nogap": "all but the two-week gap (9->10)",
}


# ------------------------------------------------------------------ the runs

def run(n_draws: int = N_DRAWS, seed: int = SEED, recodes: dict | None = None) -> dict:
    """Compute everything the report needs.  Returns plain dicts and arrays."""
    ranks = nc.load_ranks()
    out: dict = {"n_draws": n_draws, "seed": seed, "recodes": {}}
    for k, (name, (npos, nneg)) in enumerate((recodes or nc.RECODES).items()):
        rng = np.random.default_rng([seed, k])
        S = nc.recode(ranks, npos, nneg)
        obs = nc.observed_counts(S)
        null = nc.static_null(rng, n_draws, npos, nneg)
        res: dict = {"cut": (npos, nneg), "obs": obs, "null": null, "cells": {}}
        res["cmp"] = {key: nc.compare_to_null(obs[key], null[key]) for key in ("triple", "agree", "sum")}
        one, allneg = nc.TRIPLE_LEVEL.one_neg, nc.TRIPLE_LEVEL.all_neg
        pools = {
            "one_neg": nc.pool(obs["triple"], one), "strict_imb": nc.pool(obs["triple"], one + allneg),
            "complete": obs["triple"].sum(-1),
        }
        npools = {
            "one_neg": nc.pool(null["triple"], one), "strict_imb": nc.pool(null["triple"], one + allneg),
            "complete": null["triple"].sum(-1),
        }
        res["pooled"] = {key: nc.compare_to_null(pools[key][:, None], npools[key][:, None]) for key in pools}
        res["pooled_obs"], res["pooled_null_mean"] = pools, {key: v.mean() for key, v in npools.items()}
        for cell, (level, rule) in CELLS.items():
            Tobs = nc.observed_transitions(S, level, rule)
            Tc = nc.null_transitions(S, level, rule, "cond", n_draws, rng, (npos, nneg))
            c = {"Tobs": Tobs, "stats": {w: nc.conversion_stats(Tobs, Tc, level, nc.window_transitions(w)) for w in WINDOWS}}
            if name == nc.PRIMARY_RECODE:
                c["per_transition"] = [nc.conversion_stats(Tobs, Tc, level, [t]) for t in range(nc.N_TRANSITIONS)]
                pooled = Tc.sum(0).astype(np.float64)
                sd = pooled.std(0, ddof=1)
                with np.errstate(invalid="ignore", divide="ignore"):
                    c["z_matrix"] = np.where(sd > 0, (Tobs.sum(0) - pooled.mean(0)) / np.where(sd > 0, sd, 1), np.nan)
                if cell != "agree":  # the literal 'shuffled waves' null; too sparse to mean anything under 'agree'
                    Ti = nc.null_transitions(S, level, rule, "indep", n_draws, rng, (npos, nneg))
                    c["indep"] = {w: nc.conversion_stats(Tobs, Ti, level, nc.window_transitions(w)) for w in ("all", "early")}
            res["cells"][cell] = c
        out["recodes"][name] = res
    return out


# ------------------------------------------------------------------ formatting helpers

def table(headers: list[str], rows: list[list], align: str | None = None) -> list[str]:
    align = align or ("l" + "r" * (len(headers) - 1))
    sep = ["---:" if a == "r" else ":---" for a in align]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep) + " |"]
    lines += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return lines


def f3(x: float) -> str:
    return "n/a" if x is None or np.isnan(x) else f"{x:.3f}"


def pct(x: float, nd: int = 2) -> str:
    return "n/a" if x is None or np.isnan(x) else f"{100 * x:.{nd}f}%"


def zf(x: float) -> str:
    return "-" if np.isnan(x) else f"{x:+.1f}"


def ratio(a: float, b: float) -> str:
    return "n/a" if (np.isnan(a) or np.isnan(b) or b == 0) else f"{a / b:.2f}"


def pv(p: float) -> str:
    return "n/a" if np.isnan(p) else ("<0.001" if p < 0.001 else f"{p:.3f}")


def peq(p: float) -> str:
    """For running prose: 'p = 0.099' or 'p < 0.001'."""
    return "p n/a" if np.isnan(p) else ("p < 0.001" if p < 0.001 else f"p = {p:.3f}")


MIN_AT_RISK = 10  # below this a class is shown but no p-value is offered


def pvr(p: float, at_risk: int) -> str:
    return f"n/a (<{MIN_AT_RISK} at risk)" if at_risk < MIN_AT_RISK else pv(p)


def waves_flag(flags, kind: str) -> str:
    return f"{int((np.asarray(flags) == kind).sum())}/15"


# ------------------------------------------------------------------ the report

def build_report(out: dict) -> str:
    P = out["recodes"][nc.PRIMARY_RECODE]
    B = out["n_draws"]
    L: list[str] = []
    add = L.append
    today = datetime.date.today().isoformat()

    add("# Newcomb fraternity: the n = 3 refutation test of v0.1 section 7, run on the data")
    add("")
    add(f"_Generated {today} by `uv run python -m models.newcomb_report report` (seed {out['seed']}, {B:,} null draws). "
        "Code: `sim/models/newcomb.py`, `sim/models/newcomb_report.py`; checks: `sim/tests/test_newcomb_triads.py`. "
        "Ledger ids are the lines with source \"104 §\" (L4471-L4546). Results are computed statistics only; the rank "
        "file is local-use-only and is not redistributed (`sim/data/README.md`)._")
    add("")
    add("**What was tested (v0.1 §7, n = 3; v0's hypothesis, not a source's):** in longitudinal signed triads the "
        "one-negative triangle must be (a) under-represented against a sign-shuffled null and (b) convert to a balanced "
        "triangle faster than the all-negative one; if conversion runs at the null rate, (4.2b)/(5.1) is refuted. "
        "Half (a) is Doreian & Krackhardt's (2001) static count; half (b) is new: neither D&K nor the 1996 paper prints a "
        "type-to-type transition table [L4527].")
    add("")
    L += verdict_section(out)
    L += data_section(out)
    L += static_section(out)
    L += dynamics_section(out)
    L += sensitivity_section(out)
    L += caveats_section()
    add("## Reproduce")
    add("")
    add("    cd sim")
    add("    ~/.local/bin/uv run python -m models.newcomb_report fetch    # once; checks sha256, writes to git-ignored data/newcomb/")
    add("    ~/.local/bin/uv run python -m models.newcomb_report report   # rewrites this file")
    add("    ~/.local/bin/uv run pytest tests/test_newcomb_triads.py")
    add("")
    return "\n".join(L) + "\n"


# ---- data section

def data_section(out: dict) -> list[str]:
    P = out["recodes"][nc.PRIMARY_RECODE]
    S = nc.recode(nc.load_ranks())
    turn = [float((S[t] != S[t + 1])[~np.eye(nc.N, dtype=bool)].mean()) for t in range(nc.N_TRANSITIONS)]
    rec = P["obs"]["recip"]
    L = ["## 1. Data, terms, recode", ""]
    L.append("- **Source.** `newfrat.dat`, the UCINET dataset \"Newcomb Fraternity Networks\" (fifteen 17 x 17 rank matrices "
             "NEWC0-NEWC15 without NEWC9 [L4538]), fetched from the Internet Archive's public snapshot of "
             "`vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat` (the original host timed out from the box on "
             "2026-10-31). Two snapshots (2021-04-21, 2024-10-04) are byte-identical, 13,702 bytes, "
             f"sha256 `{nc.SHA256}`.")
    L.append("- **Independent cross-check.** The R package `networkdata` (`schochastics/networkdata`, `data/fraternity.rda`, "
             "list of 15 igraph objects, edge attribute `rank`) holds exactly the same 15 x 17 x 17 ranks (compared "
             "cell by cell once, with a throwaway reader; that file was not kept). "
             "Each row of each wave is a permutation of 1-16 (checked on every load).")
    L.append("- **Terms [L4539-L4544].** The Pajek/UCINET listing states none; absence of a stated licence is not a grant. "
             "The UCI mirror's R documentation says CC BY-NC-ND 2.5 \"if the source does not specify otherwise\". "
             "The `networkdata` MIT licence covers the package, not the data. Treated as not licensed for redistribution: "
             "fetched for local use into git-ignored `sim/data/newcomb/`, never committed, results only here. Credit: "
             "Newcomb (1961), *The Acquaintance Process*; Nordlie (1958), thesis; the UCINET distribution "
             "(Borgatti, Everett, Freeman), via Batagelj & Mrvar's Pajek datasets.")
    L.append("- **Waves.** 15 observation indices (D&K's \"weeks\" 1-15; wave 9 is NEWC8, wave 10 is NEWC10), so 14 transitions, "
             "of which 9->10 spans two calendar weeks, which the authors ignored [L4472, L4545]; windows below include a "
             "\"without the gap\" check.")
    L.append("- **The sign is a modelling choice, not data [L4476, L4479].** Ranks 1-4 -> +, 14-16 -> -, 5-13 -> 0 (D&K's top-4 / "
             "bottom-3), so every man sends exactly 4 + / 3 - / 9 0 ties in every wave (68 + and 51 - ties per wave, "
             "[L4480]; verified). D&K themselves call this \"a major data problem\" [L4479]: the files cannot say whether "
             "a man ranking 16 others dislikes the bottom three or merely likes them least. Null ties are a third state; "
             "absence is not coded negative. Section 4 reruns everything with top-3/bottom-3, top-5/bottom-4 and D&K's "
             "own top-3/bottom-2 [L4478].")
    L.append("- **Does the recode reproduce what the 1996 paper measured on the same ranks?** Reciprocated positive ties per wave: "
             f"{', '.join(str(int(x)) for x in rec)} (1996 text: 30-35 of 68, plot reaching 36 in weeks 3-5 and 10 "
             f"[L4520]; here 36 in waves 3, 4, 5 and 10; null median about 17 [L4521], here "
             f"{int(np.median(P['null']['recip']))}, mean {P['null']['recip'].mean():.1f}, closed form 17). "
             f"Share of ordered pairs changing state at the first transition: {pct(turn[0], 1)} (1996: \"slightly above 30%\" "
             f"[L4527]); at transitions 2-5: {', '.join(pct(x, 1) for x in turn[1:5])}. That is consistent with the file, the wave "
             "order and the recode being the ones the authors used.")
    L.append("- **Correction to the brief.** It asked for \"the 16 D&K types\". D&K have **eight** signed ordered-triple types "
             "(LLL ... DDD) [L4481]; sixteen is Leskovec et al.'s count of directed triad types with edge direction (084 §4). "
             "The eight are computed, plus the undirected triangle types.")
    L.append("")
    return L


# ---- static section

def static_section(out: dict) -> list[str]:
    P = out["recodes"][nc.PRIMARY_RECODE]
    B = out["n_draws"]
    cm = P["cmp"]["triple"]
    obs = P["obs"]["triple"]
    L = ["## 2. Static counts against the row-wise sign-shuffle null", ""]
    L.append(f"Null: D&K's [L4485], {B:,} draws; every man keeps his 4 L and 3 D out-ties, received ties are free. Its "
             "distribution is the same for every wave (every row of every wave is a permutation of 1-16), so one sample "
             "serves all waves. Null mean counts (closed form in brackets, from the row structure alone): "
             + ", ".join(f"{t} {m:.1f} [{e:.1f}]" for t, m, e in zip(nc.TRIPLE_TYPES, P["null"]["triple"].mean(0), nc.expected_triple_counts()))
             + ".")
    L.append("")
    L.append("### 2.1 D&K's eight directed types: p(obs > random) by wave (top-4 / bottom-3)")
    L.append("")
    L.append("Above 0.95 = significantly more than the null, below 0.05 = significantly fewer [L4486]. "
             "Types are named (i->j)(j->k)(i->k), L = +, D = -. Heider-balanced: LLL LDD DLD DDL [L4482]; one-negative: LLD LDL DLL; all-negative: DDD.")
    L.append("")
    rows = [[w + 1] + [f3(x) for x in cm["p_gt"][w]] for w in range(nc.N_WAVES)]
    L += table(["wave"] + list(nc.TRIPLE_TYPES), rows)
    L.append("")
    L.append("z-scores of the same counts against the null (observed - null mean) / null sd:")
    L.append("")
    rows = [[w + 1] + [zf(x) for x in cm["z"][w]] for w in range(nc.N_WAVES)]
    L += table(["wave"] + list(nc.TRIPLE_TYPES), rows)
    L.append("")
    L.append("Observed counts of ordered triples (null mean in the last row):")
    L.append("")
    rows = [[w + 1] + [int(x) for x in obs[w]] for w in range(nc.N_WAVES)]
    rows.append(["null mean"] + [f"{x:.1f}" for x in P["null"]["triple"].mean(0)])
    L += table(["wave"] + list(nc.TRIPLE_TYPES), rows)
    L.append("")
    L.append("**D&K's reported pattern, checked claim by claim (text-stated claims only, L4490-L4498), for each recode:**")
    L.append("")
    recs = list(out["recodes"])
    pats = {r: nc.dk_pattern(out["recodes"][r]["cmp"]["triple"]["p_gt"]) for r in recs}
    rows = [[claim] + ["yes" if pats[r][claim] else "**no**" for r in recs] for claim in pats[recs[0]]]
    L += table(["claim"] + [f"{r}" for r in recs], rows, "l" + "c" * len(recs))
    L.append("")

    # 2.2 the one-negative triangle, yes/no per wave
    L.append("### 2.2 Is the one-negative triangle under-represented? Yes/no per wave (top-4 / bottom-3)")
    L.append("")
    L.append("\"under\" / \"over\" = observed count below / above the null mean with a one-sided exact Monte-Carlo "
             "p <= 0.05 that counts ties against the observation (so a zero against a null that is mostly zero is not \"under\"); "
             "\"-\" = no difference detected. Columns: the three directed one-negative forms and their pool; "
             "the undirected one-negative triangle (++-) under the two symmetrisation rules.")
    L.append("")
    cols = {}
    for i, t in enumerate(nc.TRIPLE_TYPES):
        if t in nc.TRIPLE_ONE_NEG:
            cols[t] = nc.side(obs[:, i], cm["mean"][:, i], cm["p_up"][:, i], cm["p_dn"][:, i])
    pc = P["pooled"]["one_neg"]
    cols["LLD+LDL+DLL"] = nc.side(P["pooled_obs"]["one_neg"], pc["mean"][:, 0], pc["p_up"][:, 0], pc["p_dn"][:, 0])
    for rule in ("sum", "agree"):
        c = P["cmp"][rule]
        cols[f"++- ({rule})"] = nc.side(P["obs"][rule][:, 1], c["mean"][:, 1], c["p_up"][:, 1], c["p_dn"][:, 1])
    rows = [[w + 1] + [cols[k][w] for k in cols] for w in range(nc.N_WAVES)]
    rows.append(["**waves under**"] + [waves_flag(cols[k], "under") for k in cols])
    rows.append(["**waves over**"] + [waves_flag(cols[k], "over") for k in cols])
    L += table(["wave"] + list(cols), rows)
    L.append("")
    sh = P["pooled_obs"]["one_neg"] / P["pooled_obs"]["complete"]
    nsh = P["pooled_null_mean"]["one_neg"] / P["pooled_null_mean"]["complete"]
    L.append(f"The pool is depleted but the one-negative form is nowhere near forbidden: it is {pct(sh[0], 0)} of complete directed "
             f"triples at wave 1 and {pct(sh[-1], 0)} at wave 15, against {pct(nsh, 0)} under the null. "
             f"Pooled z-scores run from {zf(pc['z'][:, 0].min())} to {zf(pc['z'][:, 0].max())}.")
    L.append("")
    a = P["obs"]["agree"]
    ca = P["cmp"]["agree"]
    L.append("**Under the 'agree' rule the test cannot be run.** Only mutual ties of one sign survive, and "
             f"the null expects {ca['mean'][0, 1]:.2f} one-negative triangles per wave (P(count = 0) = "
             f"{(P['null']['agree'][:, 1] == 0).mean():.2f}). Observed one-negative triangles per wave: "
             f"{', '.join(str(int(x)) for x in a[:, 1])} (a single one in 15 waves). All-negative: "
             f"{', '.join(str(int(x)) for x in a[:, 3])} against a null mean of {ca['mean'][0, 3]:.3f}; all-positive "
             f"{', '.join(str(int(x)) for x in a[:, 0])} against {ca['mean'][0, 0]:.3f}.")
    L.append("")
    L.append("All four 'agree' triangle counts per wave (null mean in the last row), for completeness:")
    L.append("")
    rows = [[w + 1] + [int(x) for x in a[w]] for w in range(nc.N_WAVES)]
    rows.append(["null mean"] + [f"{x:.3f}" for x in P["null"]["agree"].mean(0)])
    L += table(["wave", "+++", "++-", "+--", "---"], rows)
    L.append("")
    s_ = P["obs"]["sum"]
    cs = P["cmp"]["sum"]
    L.append("Undirected triangle counts under the 'sum' rule (a pair is + / - if either direction is, a conflict is 0), "
             "types by number of negative edges; null mean in the last row:")
    L.append("")
    rows = [[w + 1] + [int(x) for x in s_[w]] + [int(s_[w].sum())] for w in range(nc.N_WAVES)]
    rows.append(["null mean"] + [f"{x:.1f}" for x in P["null"]["sum"].mean(0)] + [f"{P['null']['sum'].sum(1).mean():.1f}"])
    L += table(["wave", "+++", "++-", "+--", "---", "complete"], rows)
    L.append("")
    L.append("z-scores of the 'sum' triangle counts against the null:")
    L.append("")
    rows = [[w + 1] + [zf(x) for x in cs["z"][w]] for w in range(nc.N_WAVES)]
    L += table(["wave", "+++", "++-", "+--", "---"], rows)
    L.append("")

    # 2.3 weak vs strict, static
    L.append("### 2.3 Weak (Davis) vs strict (Heider) balance, static")
    L.append("")
    L.append("Strict balance forbids the one-negative AND the all-negative triple; weak balance forbids only the "
             "one-negative [L4482, L4483]. Share of complete directed triples that are strictly imbalanced "
             "(LLD LDL DLL DDD) and weakly imbalanced (LLD LDL DLL), observed vs null mean:")
    L.append("")
    comp, nco = P["pooled_obs"]["complete"], P["pooled_null_mean"]["complete"]
    rows = []
    for w in range(nc.N_WAVES):
        rows.append([w + 1, int(comp[w]), pct(P["pooled_obs"]["strict_imb"][w] / comp[w], 1),
                     pct(P["pooled_null_mean"]["strict_imb"] / nco, 1), pct(P["pooled_obs"]["one_neg"][w] / comp[w], 1),
                     pct(P["pooled_null_mean"]["one_neg"] / nco, 1), zf(P["cmp"]["triple"]["z"][w, 7])])
    L += table(["wave", "complete", "strict-imbal", "(null)", "weak-imbal", "(null)", "z of DDD"], rows)
    L.append("")
    pg = P["cmp"]["triple"]["p_gt"][:, 7]
    d_over = int((pg > 0.95).sum())
    first_always = next(w + 1 for w in range(nc.N_WAVES) if (pg[w:] > 0.95).all())
    ov = {rule: nc.side(P["obs"][rule][:, 3], P["cmp"][rule]["mean"][:, 3], P["cmp"][rule]["p_up"][:, 3], P["cmp"][rule]["p_dn"][:, 3])
          for rule in ("sum", "agree")}
    L.append(f"DDD, which strict balance forbids, is above its null in {d_over} of 15 waves by D&K's rule, and in every wave from "
             f"{first_always} on; the all-negative triangle is over-represented in {waves_flag(ov['sum'], 'over')} waves ('sum') and "
             f"{waves_flag(ov['agree'], 'over')} ('agree', on 1-2 triangles a wave against an expected 0.01). "
             "Strict balance fails as a total descriptive rule here, as in the large online networks (084 §4); the weak form "
             "is the one that survives, and only as a depletion, not a prohibition.")
    L.append("")
    return L


# ---- dynamics section

CLASS_TITLE = {
    "triple": ("one-negative (LLD, LDL, DLL)", "all-negative (DDD)"),
    "sum": ("one-negative (++-)", "all-negative (---)"),
    "agree": ("one-negative (++-)", "all-negative (---)"),
}


def naive_fisher(st: dict, target: str = "strict") -> float:
    o, a = st["classes"]["one_neg"], st["classes"]["all_neg"]
    if not o["start_obs"] or not a["start_obs"]:
        return float("nan")
    tab = [[o[target]["num_obs"], o["start_obs"] - o[target]["num_obs"]], [a[target]["num_obs"], a["start_obs"] - a[target]["num_obs"]]]
    return float(fisher_exact(tab, alternative="greater")[1])


def dynamics_section(out: dict) -> list[str]:
    P = out["recodes"][nc.PRIMARY_RECODE]
    B = out["n_draws"]
    L = ["## 3. Conversion: the new computation", ""]
    L.append("**Definitions.** A triple of the start class at wave w is followed to its type at wave w+1; counts are pooled over "
             "transitions (a triple at risk at several waves is counted at each, so they are not independent events). "
             "*Strict conversion* = it is a complete balanced type at w+1: LLL LDD DLD DDL (triples), +++ or +-- (triangles) [L4482]. "
             "*Incomplete* = a tie fell to 0, which v0 §4.2 calls vacuously balanced. *Relief* = strict conversion or incomplete, "
             "i.e. v0's own convention taken literally (added after the first transition matrices were seen; see section 5). "
             "*Stays weakly balanced* (all-negative class) = still a complete weak-balanced type, in practice still all-negative [L4483].")
    L.append("")
    L.append("**The null that matters is 'cond'.** The start wave is kept and the next wave's ties are re-placed at random "
             "within strata of start sign, keeping every man's own start-to-end transition table (directed triples) or the "
             "whole dyad transition table (triangles). Persistence, turnover and the 4/3/9 counts are held; only *which* ties "
             f"change is random ({B:,} draws per transition, independent across transitions; p = (1 + #{{null >= obs}})/(B + 1), one-sided "
             "in the direction v0 predicts unless marked). An excess over it means changes are aimed at tension; it cannot separate "
             "balance from reciprocity, popularity or rivalry (D&K's other mechanisms, L4511, L4512). The literal \"independently "
             "shuffled waves\" null is in 3.7: it ignores persistence, so every observed rate falls far below it.")
    L.append("")

    L.append("### 3.1 Strict conversion into a complete balanced type (all 14 transitions pooled, top-4 / bottom-3)")
    L.append("")
    rows = []
    for cell in CELLS:
        st = P["cells"][cell]["stats"]["all"]
        for cname, title in zip(("one_neg", "all_neg"), CLASS_TITLE[cell]):
            c = st["classes"][cname]
            s_ = c["strict"]
            rows.append([CELL_TITLE[cell], title, c["start_obs"], s_["num_obs"], pct(s_["rate_obs"]), pct(s_["rate_null_mean"]),
                         ratio(s_["rate_obs"], s_["rate_null_mean"]), pvr(s_["p_up"], c["start_obs"])])
    L += table(["cell", "start class", "at risk", "-> strict bal.", "rate", "null rate", "ratio", "p (>= obs)"], rows, "llrrrrrr")
    L.append("")
    L.append("v0 §7 asks whether the one-negative class converts *faster than the all-negative* one. The statistic is the "
             "difference of the two rates, compared with the same difference under the null, which is not zero (the one-negative "
             "triple has more routes to a balanced one than DDD has, so the null already favours it):")
    L.append("")
    rows = []
    for cell in CELLS:
        st = P["cells"][cell]["stats"]["all"]
        d = st["diff"]["strict"]
        small = min(st["classes"]["one_neg"]["start_obs"], st["classes"]["all_neg"]["start_obs"]) < MIN_AT_RISK
        rows.append([CELL_TITLE[cell], pct(d["obs"]), pct(d["null_mean"]), "n/a" if small else pv(d["p_up"]), "n/a" if small else pv(naive_fisher(st))])
    L += table(["cell", "r(1-neg) - r(all-neg)", "null mean of it", "p (>= obs), vs null", "naive Fisher p"], rows)
    L.append("")
    L.append("(\"naive Fisher p\": one-sided exact test on the raw counts, which ignores that triples share ties and that the null "
             "already favours the one-negative class; shown because it is the first thing a reader would compute.)")
    L.append("")

    L.append("### 3.2 Relief: balanced by a sign change OR by losing a tie (post hoc, v0's own convention)")
    L.append("")
    rows = []
    for cell in ("triple", "sum"):
        st = P["cells"][cell]["stats"]["all"]
        for cname, title in zip(("one_neg", "all_neg"), CLASS_TITLE[cell]):
            c = st["classes"][cname]
            r_ = c["relief"]
            rows.append([CELL_TITLE[cell], title, c["start_obs"], f"{r_['num_obs']} ({pct(r_['rate_obs'], 1)})", pct(r_["rate_null_mean"], 1),
                         pv(r_["p_up"]), pv(r_["p_dn"]), pct(c["inc"]["rate_obs"], 1), pct(c["inc"]["rate_null_mean"], 1)])
    L += table(["cell", "start class", "at risk", "relief (rate)", "null", "p (>= obs)", "p (<= obs)", "of it, tie lost", "null"], rows, "llrrrrrrr")
    L.append("")
    rows = []
    for cell in ("triple", "sum"):
        st = P["cells"][cell]["stats"]["all"]
        d = st["diff"]["relief"]
        rows.append([CELL_TITLE[cell], pct(d["obs"], 1), pct(d["null_mean"], 1), pv(d["p_up"]), pv(naive_fisher(st, "relief"))])
    L += table(["cell", "relief(1-neg) - relief(all-neg)", "null mean of it", "p (>= obs), vs null", "naive Fisher p"], rows)
    L.append("")

    L.append("### 3.3 Type-to-type transition counts (pooled over the 14 transitions)")
    L.append("")
    L.append("Rows = type at wave w, columns = type at wave w+1; \"inc\" = incomplete (some tie 0). These are the tables neither "
             "paper prints [L4527]. The second table gives the z-score of each cell against the 'cond' null (cells whose null "
             "never varies are \"-\").")
    L.append("")
    tz, sz = P["cells"]["triple"]["z_matrix"], P["cells"]["sum"]["z_matrix"]
    ti = nc.TRIPLE_TYPES.index
    d = {t: tz[ti(t), ti(t)] for t in nc.TRIPLE_TYPES}
    if not (d["LLL"] > 0 and d["LDD"] > 0 and d["LLD"] < 0 and d["LDL"] < 0 and d["DLL"] > 0 and d["DDD"] > 0 and d["DDL"] < 0
            and abs(d["DLD"]) < 2 and sz[0, 0] > 0 and sz[2, 2] > 0 and sz[1, 1] < 0 and sz[3, 3] > 0):
        raise AssertionError("the diagonal reading in 3.3 is stale, rewrite it")
    L.append("Read the diagonal (z of persistence against the null; a post hoc reading). Among directed types the first tie decides, as in D&K [L4508]: "
             f"with a positive first tie balanced types persist more than chance (LLL {zf(d['LLL'])}, LDD {zf(d['LDD'])}) and unbalanced ones less "
             f"(LLD {zf(d['LLD'])}, LDL {zf(d['LDL'])}); with a negative first tie the balanced DDL persists *less* ({zf(d['DDL'])}), DLD at chance "
             f"({zf(d['DLD'])}), and the unbalanced DLL and DDD *more* ({zf(d['DLL'])}, {zf(d['DDD'])}). Triangles: +++ {zf(sz[0, 0])}, +-- {zf(sz[2, 2])} "
             f"and --- {zf(sz[3, 3])} persist more, ++- {zf(sz[1, 1])} less.")
    L.append("")
    for cell in ("triple", "sum"):
        level = CELLS[cell][0]
        O = P["cells"][cell]["Tobs"].sum(0)
        Z = P["cells"][cell]["z_matrix"]
        L.append(f"**{CELL_TITLE[cell]}: observed counts**")
        L.append("")
        L += table(["from \\ to"] + list(level.labels), [[level.labels[a]] + [int(x) for x in O[a]] for a in range(level.k)])
        L.append("")
        L.append(f"**{CELL_TITLE[cell]}: z against the cond null**")
        L.append("")
        L += table(["from \\ to"] + list(level.labels), [[level.labels[a]] + [zf(x) for x in Z[a]] for a in range(level.k)])
        L.append("")
    O = P["cells"]["agree"]["Tobs"].sum(0)
    lab = nc.TRIANGLE_LEVEL.labels
    L.append("**triangles, 'agree' rule: observed counts** (the whole of the evidence under the rule the brief named)")
    L.append("")
    L += table(["from \\ to"] + list(lab), [[lab[a]] + [int(x) for x in O[a]] for a in range(len(lab))])
    L.append("")

    L.append("### 3.4 Windows")
    L.append("")
    L.append("D&K find the dynamics essentially over by waves 5-6 [L4498], so the informative window is the first transitions, when "
             "about 30% of ties change [L4527]. Strict conversion of the one-negative class vs its null, and the difference test:")
    L.append("")
    rows = []
    for cell in ("triple", "sum"):
        for w in WINDOWS:
            st = P["cells"][cell]["stats"][w]
            o, a = st["classes"]["one_neg"], st["classes"]["all_neg"]
            rows.append([CELL_TITLE[cell], WINDOW_TITLE[w], o["start_obs"], f"{o['strict']['num_obs']} ({pct(o['strict']['rate_obs'])})",
                         pct(o["strict"]["rate_null_mean"]), pv(o["strict"]["p_up"]), a["start_obs"],
                         f"{a['strict']['num_obs']} ({pct(a['strict']['rate_obs'])})", pv(st["diff"]["strict"]["p_up"])])
    L += table(["cell", "window", "1-neg at risk", "-> bal.", "null", "p", "all-neg at risk", "-> bal.", "p of difference"], rows, "llrrrrrrr")
    L.append("")
    L.append("Relief, same windows:")
    L.append("")
    rows = []
    for cell in ("triple", "sum"):
        for w in WINDOWS:
            st = P["cells"][cell]["stats"][w]
            o, a = st["classes"]["one_neg"]["relief"], st["classes"]["all_neg"]["relief"]
            rows.append([CELL_TITLE[cell], WINDOW_TITLE[w], pct(o["rate_obs"], 1), pct(o["rate_null_mean"], 1), pv(o["p_up"]),
                         pct(a["rate_obs"], 1), pct(a["rate_null_mean"], 1), pv(a["p_dn"]), pv(st["diff"]["relief"]["p_up"])])
    L += table(["cell", "window", "1-neg relief", "null", "p (>=)", "all-neg relief", "null", "p (<=)", "p of difference"], rows, "llrrrrrrr")
    L.append("")

    L.append("### 3.5 Per transition (directed triples; top-4 / bottom-3)")
    L.append("")
    rows = []
    for t, st in enumerate(P["cells"]["triple"]["per_transition"]):
        o, a = st["classes"]["one_neg"], st["classes"]["all_neg"]
        rows.append([f"{t + 1}->{t + 2}" + (" (gap)" if t + 1 == nc.GAP_TRANSITION else ""), o["start_obs"], o["strict"]["num_obs"],
                     pct(o["inc"]["rate_obs"], 0), a["start_obs"], a["strict"]["num_obs"], pct(a["weak"]["rate_obs"], 0)])
    L += table(["transition", "1-neg at risk", "-> bal.", "tie lost", "DDD at risk", "-> bal.", "DDD stays complete"], rows)
    L.append("")
    pt = P["cells"]["triple"]["per_transition"]
    conv = [st["classes"]["one_neg"]["strict"]["num_obs"] for st in pt]
    wk = [(st["classes"]["all_neg"]["weak"]["num_obs"], st["classes"]["all_neg"]["start_obs"]) for st in pt]
    early3 = sum(a for a, _ in wk[:3]) / sum(b for _, b in wk[:3])
    rest = sum(a for a, _ in wk[3:]) / sum(b for _, b in wk[3:])
    L.append(f"{sum(conv[:5])} of the {sum(conv)} directed strict conversions fall in the first five transitions, and DDD stays complete in "
             f"{pct(early3, 0)} of cases over transitions 1-3 against {pct(rest, 0)} over transitions 4-14: the all-negative stability is a "
             "late, consolidating pattern (D&K's macro-structure story, L4516), not present from the start.")
    L.append("")

    L.append("### 3.6 Weak vs strict, dynamic")
    L.append("")
    tr, su = P["cells"]["triple"]["stats"]["all"]["classes"]["all_neg"], P["cells"]["sum"]["stats"]["all"]["classes"]["all_neg"]
    L.append(f"Strict balance says the all-negative triple is as tense as the one-negative and should be repaired. It is not repaired: its "
             f"strict conversion is {tr['strict']['num_obs']} of {tr['start_obs']} (directed) and {su['strict']['num_obs']} of {su['start_obs']} (sum), "
             f"and it stays a complete weakly-balanced triple at {pct(tr['weak']['rate_obs'], 1)} (directed) and {pct(su['weak']['rate_obs'], 1)} "
             f"(sum) against null rates of {pct(tr['weak']['rate_null_mean'], 1)} and {pct(su['weak']['rate_null_mean'], 1)} "
             f"({'both p < 0.001' if max(tr['weak']['p_up'], su['weak']['p_up']) < 0.001 else peq(tr['weak']['p_up']) + ' and ' + peq(su['weak']['p_up'])}). It persists *more* than random tie change would, which is what weak "
             "balance (nothing to repair) predicts and strict balance does not. The cause may be macro-structure rather than a drive: "
             "the consensus-disliked men [L4516-L4518] keep their negative in-ties, and the null does not preserve received ties [L4485 note].")
    L.append("")

    L.append("### 3.7 The literal 'independently shuffled waves' null (why it is not the test)")
    L.append("")
    L.append("Both waves of a transition are re-drawn independently from the row-wise shuffle, so the null rate is the marginal share of "
             "balanced triples at the next wave whatever the start. Ties persist (70-90% per transition [L4528]), so observed "
             "conversion is far below it for every class and the comparison says nothing about balance:")
    L.append("")
    rows = []
    for cell in ("triple", "sum"):
        st = P["cells"][cell]["indep"]["all"]
        for cname, title in zip(("one_neg", "all_neg"), CLASS_TITLE[cell]):
            c = st["classes"][cname]
            rows.append([CELL_TITLE[cell], title, pct(c["strict"]["rate_obs"]), pct(c["strict"]["rate_null_mean"]), pv(c["strict"]["p_dn"]),
                         pct(c["inc"]["rate_obs"], 1), pct(c["inc"]["rate_null_mean"], 1)])
    L += table(["cell", "class", "strict conv.", "indep null", "p (<= obs)", "tie lost", "indep null"], rows, "llrrrrr")
    L.append("")
    return L


# ---- sensitivity section

def sensitivity_section(out: dict) -> list[str]:
    L = ["## 4. What the recode assumption does", ""]
    L.append("The cut changes which ties count as signed: top-3/bottom-3 and top-3/bottom-2 sign fewer ties (3+3 = 6 and 3+2 = 5 of 16), "
             "top-5/bottom-4 more (9 of 16); the null is rebuilt with the matching row composition each time. "
             "Static questions, each recode (counts of waves out of 15; D&K's rule for the directed types, exact Monte-Carlo for the triangles):")
    L.append("")
    rows = []
    i = nc.TRIPLE_TYPES.index
    for r, res in out["recodes"].items():
        cm = res["cmp"]["triple"]
        pc = res["pooled"]["one_neg"]
        sh = nc.side(res["pooled_obs"]["one_neg"], pc["mean"][:, 0], pc["p_up"][:, 0], pc["p_dn"][:, 0])
        cs = res["cmp"]["sum"]
        ssum = nc.side(res["obs"]["sum"][:, 1], cs["mean"][:, 1], cs["p_up"][:, 1], cs["p_dn"][:, 1])
        ca = res["cmp"]["agree"]
        sagr3 = nc.side(res["obs"]["agree"][:, 3], ca["mean"][:, 3], ca["p_up"][:, 3], ca["p_dn"][:, 3])
        npat = sum(nc.dk_pattern(cm["p_gt"]).values())
        rows.append([r, f"{int((cm['p_gt'][:, i('LLD')] < .05).sum())}", f"{int((cm['p_gt'][:, i('LDL')] < .05).sum())}",
                     f"{int((cm['p_gt'][5:, i('DLL')] > .95).sum())}/10", f"{int((cm['p_gt'][4:, i('DDD')] > .95).sum())}/11",
                     waves_flag(sh, "under").split("/")[0], waves_flag(ssum, "under").split("/")[0],
                     waves_flag(sagr3, "over").split("/")[0], f"{npat}/10",
                     int(res["obs"]["agree"][:, 1].sum())])
    L += table(["recode", "LLD under", "LDL under", "DLL over (w6-15)", "DDD over (w5-15)", "1-neg pool under", "++- (sum) under",
                "--- (agree) over", "D&K claims held", "++- (agree) seen"], rows)
    L.append("")
    L.append("The contrasts that matter (LLD and LDL depleted, DLL and DDD enriched, the one-negative pool depleted) survive every cut; "
             "D&K's claim that the qualitative results hold for top-3/bottom-3 and top-3/bottom-2 [L4478] is confirmed in that sense, "
             "but the wave-by-wave significance details (section 2.1) are not stable: fewer signed ties means smaller counts and "
             "a noisier early study. Dynamic questions, all 14 transitions pooled, strict conversion:")
    L.append("")
    rows = []
    for r, res in out["recodes"].items():
        for cell in ("triple", "sum", "agree"):
            st = res["cells"][cell]["stats"]["all"]
            o, a, d = st["classes"]["one_neg"], st["classes"]["all_neg"], st["diff"]["strict"]
            rows.append([r, CELL_TITLE[cell], o["start_obs"], f"{o['strict']['num_obs']} ({pct(o['strict']['rate_obs'])})", pct(o["strict"]["rate_null_mean"]),
                         pv(o["strict"]["p_up"]), a["start_obs"], f"{a['strict']['num_obs']} ({pct(a['strict']['rate_obs'])})", pv(d["p_up"])])
    L += table(["recode", "cell", "1-neg at risk", "-> bal. (rate)", "null", "p", "all-neg at risk", "-> bal. (rate)", "p of difference"], rows, "llrrrrrrr")
    L.append("")
    L.append("And relief (balanced or tie lost), where the one-negative class is compared with its null and with the all-negative class:")
    L.append("")
    rows = []
    for r, res in out["recodes"].items():
        for cell in ("triple", "sum"):
            st = res["cells"][cell]["stats"]["all"]
            o, a, d = st["classes"]["one_neg"]["relief"], st["classes"]["all_neg"]["relief"], st["diff"]["relief"]
            rows.append([r, CELL_TITLE[cell], pct(o["rate_obs"], 1), pct(o["rate_null_mean"], 1), pv(o["p_up"]), pct(a["rate_obs"], 1),
                         pct(a["rate_null_mean"], 1), pv(a["p_dn"]), pv(d["p_up"])])
    L += table(["recode", "cell", "1-neg relief", "null", "p (>=)", "all-neg relief", "null", "p (<=)", "p of difference"], rows, "llrrrrrrr")
    L.append("")
    return L


def caveats_section() -> list[str]:
    L = ["## 5. What this test cannot say, and what was decided when", ""]
    L += [
        "- **One group, 17 men, one semester, strangers meeting for the first time** [L4471]: an acquaintance process, not a mature group, and a triangle "
        "inside a group of 17 is not an isolated n = 3 triad (each of its edges is also an edge of 14 other triangles).",
        "- **Signs are a cut of ranks with fixed counts** [L4476, L4479, L4480]: neither the share of negative ties nor the share of balanced triples "
        "can vary, and a \"conversion\" can be a rank crossing the cut-off. Nothing here measures a sign the men reported.",
        "- **The nulls hold rows, not columns.** D&K's shuffle, and the conditional one built from it, leave popularity free. Consensus-disliked men "
        "(J, P, C, O: [L4517, L4518]) make negative triples persist, which looks like stability of the all-negative triangle without any drive "
        "[L4512]. Competition for a third party [L4511] and reciprocity [L4513] are the other rivals, and actor attributes are lost [L4473], "
        "so a pattern here cannot be assigned to balance rather than to those.",
        "- **Triples and triangles at risk overlap** and recur across waves; the permutation nulls respect the overlap, a naive count test does not "
        "(the Fisher p-values shown are for comparison only). The per-wave yes/no columns are 15 correlated tests, not 15 replications, and "
        "p-values across four recodes, three cells and four windows are not corrected for multiplicity: read p of about 0.02-0.05 as suggestive.",
        "- **What was fixed in advance.** Before any result was computed: the 4/3 recode, 10,000 draws, the cells (directed triples; undirected "
        "triangles under 'agree'), the strict-conversion statistic and its difference test, the three sensitivity recodes, and the 'sum' rule and "
        "the windows as secondaries. **Post hoc:** the 'relief' target and the reading of the z-matrices for where tension goes, both after "
        "the first transition matrices showed that almost every exit from a tense triple is a tie dropping to 0 rather than a sign change; "
        "relief is nonetheless v0's own convention (§4.2: an absent tie is vacuously balanced). Nothing was dropped for disagreeing.",
        "- **Absolute strict-conversion rates are tiny.** A conversion into a complete balanced type needs a + / - flip, which on a rank scale "
        "is a jump across nine neutral ranks. With 15 (directed) and 33 (sum) events the power to see a modest excess is low.",
    ]
    L.append("")
    return L


# ---- verdict (numbers are pulled from the run; assertions fail loudly if the prose would no longer be true)

def verdict_section(out: dict) -> list[str]:
    P = out["recodes"][nc.PRIMARY_RECODE]
    cm = P["cmp"]["triple"]
    i = nc.TRIPLE_TYPES.index
    pats = nc.dk_pattern(cm["p_gt"])
    tri, sm, ag = (P["cells"][c]["stats"]["all"] for c in ("triple", "sum", "agree"))
    tz, sz = P["cells"]["triple"]["z_matrix"], P["cells"]["sum"]["z_matrix"]
    pc = P["pooled"]["one_neg"]
    pool_side = nc.side(P["pooled_obs"]["one_neg"], pc["mean"][:, 0], pc["p_up"][:, 0], pc["p_dn"][:, 0])
    cs = P["cmp"]["sum"]
    sum_side = nc.side(P["obs"]["sum"][:, 1], cs["mean"][:, 1], cs["p_up"][:, 1], cs["p_dn"][:, 1])
    under_waves = [w + 1 for w in range(nc.N_WAVES) if sum_side[w] == "under"]
    sh = P["pooled_obs"]["one_neg"] / P["pooled_obs"]["complete"]
    nsh = P["pooled_null_mean"]["one_neg"] / P["pooled_null_mean"]["complete"]
    one = {k: tri["classes"]["one_neg"][k] for k in ("strict", "relief", "inc")}
    alln = {k: tri["classes"]["all_neg"][k] for k in ("strict", "relief", "weak")}
    sone = {k: sm["classes"]["one_neg"][k] for k in ("strict", "relief", "inc")}
    salln = {k: sm["classes"]["all_neg"][k] for k in ("strict", "relief", "weak")}

    # ranges over recodes and the two testable cells, used in the prose
    def cells_all():
        for r_, res_ in out["recodes"].items():
            for c_ in ("triple", "sum"):
                yield r_, c_, res_["cells"][c_]["stats"]["all"]
    ratios = [st["classes"]["one_neg"]["strict"]["rate_obs"] / st["classes"]["one_neg"]["strict"]["rate_null_mean"] for _, _, st in cells_all()]
    p_one = [st["classes"]["one_neg"]["strict"]["p_up"] for _, _, st in cells_all()]
    p_diff = [st["diff"]["strict"]["p_up"] for _, _, st in cells_all()]
    agree_seen = max(int(res_["obs"]["agree"][:, 1].sum()) for res_ in out["recodes"].values())
    held = {r_: sum(nc.dk_pattern(res_["cmp"]["triple"]["p_gt"]).values()) for r_, res_ in out["recodes"].items()}
    at_risk = {r_: res_["cells"]["triple"]["stats"]["all"]["classes"]["one_neg"]["start_obs"] for r_, res_ in out["recodes"].items()}
    ratio_p = (one["strict"]["rate_obs"] / one["strict"]["rate_null_mean"], sone["strict"]["rate_obs"] / sone["strict"]["rate_null_mean"])
    relief_sig = [st["diff"]["relief"]["p_up"] < 0.05 for _, _, st in cells_all()]
    n_relief = sum(relief_sig)

    # guards: the prose below is only true while these hold
    guards = {
        "all ten D&K claims reproduce at 4/3": all(pats.values()),
        "pooled one-negative below the null in all 15 waves": int((pool_side == "under").sum()) == 15,
        "DLL above the null in every wave from 6 on": bool((cm["p_gt"][5:, i("DLL")] > 0.95).all()),
        "agree rule has <= 1 one-negative triangle": int(P["obs"]["agree"][:, 1].sum()) <= 1,
        "directed one-neg strict conversion not significant": one["strict"]["p_up"] > 0.05,
        "directed strict difference not significant": tri["diff"]["strict"]["p_up"] > 0.05,
        "sum strict difference not significant": sm["diff"]["strict"]["p_up"] > 0.05,
        "sum one-neg strict conversion nominally significant": sone["strict"]["p_up"] < 0.05,
        "all-neg conversion not above the null": alln["strict"]["p_up"] > 0.05 and salln["strict"]["p_up"] > 0.05,
        "all-neg stays above the null": alln["weak"]["p_up"] < 0.01 and salln["weak"]["p_up"] < 0.01,
        "relief difference significant both ways": tri["diff"]["relief"]["p_up"] < 0.01 and sm["diff"]["relief"]["p_up"] < 0.01,
        "all-neg relief below the null both ways": alln["relief"]["p_dn"] < 0.01 and salln["relief"]["p_dn"] < 0.01,
        "directed one-neg relief at the null": one["relief"]["p_up"] > 0.05,
        "sum one-neg relief above the null": sone["relief"]["p_up"] < 0.01,
        "tension goes through lost ties (LLD, LDL, ++-) but not DLL": tz[1, 8] > 2 and tz[2, 8] > 2 and sz[1, 4] > 2 and tz[4, 8] < -2,
        "primary strict ratios are 1.3-1.6": all(1.3 < x < 1.6 for x in ratio_p),
        "recode ratios stay within 0.9-2.0": all(0.9 < x < 2.0 for x in ratios),
        "agree one-negative triangles never exceed 8": agree_seen <= 8,
        "relief difference significant in most recode-by-cell combinations": n_relief >= len(relief_sig) - 2,
    }
    bad = [k for k, v in guards.items() if not v]
    if bad:
        raise AssertionError("verdict prose is stale, rewrite it: " + "; ".join(bad))

    L = ["## Verdict", ""]
    ratio_txt = ("about " + format(min(ratio_p), ".1f")) if round(min(ratio_p), 1) == round(max(ratio_p), 1) else f"{min(ratio_p):.1f}-{max(ratio_p):.1f}"
    L.append("**In short.**")
    L.append("")
    L.append(f"- *The pre-specified undirected cell cannot be run.* Under the 'agree' symmetrisation (only mutual same-sign ties; the reading faithful to "
             f"v0's symmetric a_ij) the data hold **{int(P['obs']['agree'][:, 1].sum())}** one-negative triangle in 15 waves against an expected "
             f"{P['cmp']['agree']['mean'][0, 1]:.2f} per wave, and conversion has {ag['classes']['one_neg']['start_obs']} and "
             f"{ag['classes']['all_neg']['start_obs']} triangles at risk. Two proxies carry enough events: D&K's directed triples, and undirected "
             "triangles in which either direction signs a pair ('sum').")
    L.append("- *(a) Static: supported in aggregate, refuted for one of the three directed forms.* The one-negative class is below the sign-shuffled "
             "null in every wave as a pool, and LLD and LDL in every wave; DLL, also one-negative, is above it from wave 6 on (D&K's pattern, "
             "reproduced). All-negative DDD is enriched, which strict balance forbids.")
    L.append(f"- *(b) Conversion: not decided.* A one-negative triple becoming a complete balanced one is rare ({one['strict']['num_obs']} and "
             f"{sone['strict']['num_obs']} events) and runs at {ratio_txt} times the null rate ({peq(one['strict']['p_up'])} directed, "
             f"{peq(sone['strict']['p_up'])} 'sum'); it is not shown to be faster than the all-negative class ({peq(tri['diff']['strict']['p_up'])}, "
             f"{peq(sm['diff']['strict']['p_up'])}). So v0's criterion, \"conversion at the null rate\", is not established either way. If a lost tie also "
             f"counts as balanced (v0 §4.2; post hoc), one-negative triples do resolve faster than all-negative ones (in {n_relief} of {len(relief_sig)} "
             "recode-by-cell combinations), but because all-negative triples are unusually stable, which weak balance predicts and a consensus-disliked "
             "cluster also produces.")
    L.append("- *Net.* As an empirical rule, (4.2b)/(5.1) is **refuted in two forms by this data (symmetric in the three ties; strict and total), "
             "its weak form is supported as a depletion, and its dynamical claim is undecided.**")
    L.append("")
    L.append("**(a) Is the one-negative triangle under-represented against the sign-shuffled null?**")
    L.append("")
    L.append(f"- *Directed (D&K's eight types, top-4/bottom-3):* yes for two forms, no for the third. All ten text-stated claims of D&K's "
             f"Figure 1 reproduce on these files (section 2.1). LLD and LDL are below the null in 15/15 waves; DLL, also one-negative, is "
             f"*above* it in every wave from 6 on (p(obs > random) {cm['p_gt'][5:, i('DLL')].min():.3f} to {cm['p_gt'][5:, i('DLL')].max():.3f}, "
             f"z up to {cm['z'][:, i('DLL')].max():+.1f}); D&K's reading is rivalry for the third man, with the first tie negative [L4508, L4511]. "
             f"The pool of the three is below the null in 15/15 waves (z {pc['z'][:, 0].min():+.1f} to {pc['z'][:, 0].max():+.1f}) but is "
             f"{pct(sh[0], 0)} of complete triples at wave 1 and {pct(sh[-1], 0)} at wave 15 against {pct(nsh, 0)} under the null: depleted by up to half, not forbidden.")
    L.append(f"- *Undirected, 'sum' rule:* under-represented in {len(under_waves)} of 15 waves ({', '.join(str(w) for w in under_waves)}), not detectably in the rest.")
    L.append("- *Undirected, 'agree' rule:* untestable, see above.")
    L.append("- *Consequence for v0:* a rule symmetric in the three ties cannot tell LLD, LDL and DLL apart, and the data do: an unbalanced triple "
             "whose first tie is negative is over-represented, not depleted. D&K's first-tie asymmetry [L4508] is reproduced and 104 §9's conclusion "
             "stands: (4.2b)/(5.1) is refuted as stated for directed ties.")
    L.append("")
    L.append("**(b) Does it convert to balance faster than the all-negative one?**")
    L.append("")
    L.append(f"- *Literal reading (a complete balanced type at the next wave), top-4/bottom-3, 14 transitions pooled:* directed one-negative "
             f"{one['strict']['num_obs']} of {tri['classes']['one_neg']['start_obs']} ({pct(one['strict']['rate_obs'])}) against a null rate of "
             f"{pct(one['strict']['rate_null_mean'])} (ratio {ratio(one['strict']['rate_obs'], one['strict']['rate_null_mean'])}, {peq(one['strict']['p_up'])}); "
             f"DDD {alln['strict']['num_obs']} of {tri['classes']['all_neg']['start_obs']} ({pct(alln['strict']['rate_obs'])}, null {pct(alln['strict']['rate_null_mean'])}). "
             f"'Sum' triangles: {sone['strict']['num_obs']} of {sm['classes']['one_neg']['start_obs']} ({pct(sone['strict']['rate_obs'])}) against "
             f"{pct(sone['strict']['rate_null_mean'])} (ratio {ratio(sone['strict']['rate_obs'], sone['strict']['rate_null_mean'])}, {peq(sone['strict']['p_up'])}); "
             f"all-negative {salln['strict']['num_obs']} of {sm['classes']['all_neg']['start_obs']}, at its null rate. "
             f"**Faster than all-negative: {peq(tri['diff']['strict']['p_up'])} (directed) and {peq(sm['diff']['strict']['p_up'])} ('sum')** "
             f"(difference {pct(tri['diff']['strict']['obs'])} vs {pct(tri['diff']['strict']['null_mean'])} expected under the null; {pct(sm['diff']['strict']['obs'])} vs "
             f"{pct(sm['diff']['strict']['null_mean'])}). A modest excess in the predicted direction, from 15 and 33 events, no more. "
             f"It is not stable across the cuts (section 4: over four recodes and the two cells the ratio runs {min(ratios):.1f}-{max(ratios):.1f}, the p of the "
             f"one-negative rate {min(p_one):.2f}-{max(p_one):.2f}, the p of the difference {min(p_diff):.2f}-{max(p_diff):.2f}). Against v0's criterion: conversion "
             "cannot be told from the null rate at 5% in the better-powered directed analysis, and is nominally above it in one of the two.")
    L.append(f"- *Where tension goes (post hoc).* What leaves a one-negative class leaves almost entirely by a tie dropping to 0, not by a sign flip: triples that lose a tie "
             f"outnumber those that become complete balanced {one['inc']['num_obs']} to {one['strict']['num_obs']} (directed) and {sone['inc']['num_obs']} to "
             f"{sone['strict']['num_obs']} ('sum'), i.e. {pct(one['inc']['rate_obs'], 0)} and {pct(sone['inc']['rate_obs'], 0)} of those at risk "
             f"(null {pct(one['inc']['rate_null_mean'], 0)} and {pct(sone['inc']['rate_null_mean'], 0)}). Against the cond null the first-tie-positive "
             f"unbalanced forms lose ties more and persist less (LLD to incomplete z = {tz[1, 8]:+.1f}, LDL {tz[2, 8]:+.1f}, ++- {sz[1, 4]:+.1f}), whereas DLL, whose first tie is "
             f"negative, does the opposite (z = {tz[4, 8]:+.1f}): the first-tie rule again, now in the dynamics.")
    L.append(f"- *Relief reading (a complete balanced type OR a lost tie; v0 §4.2 calls an absent tie vacuously balanced; post hoc):* one-negative "
             f"{pct(one['relief']['rate_obs'], 1)} vs all-negative {pct(alln['relief']['rate_obs'], 1)} (directed), "
             f"{pct(sone['relief']['rate_obs'], 1)} vs {pct(salln['relief']['rate_obs'], 1)} ('sum'); the difference exceeds the null difference "
             f"({peq(tri['diff']['relief']['p_up'])} directed, {peq(sm['diff']['relief']['p_up'])} 'sum'; significant at 5% in {n_relief} of {len(relief_sig)} "
             "recode-by-cell combinations, section 4). Taken at face value that is the prediction. But the one-negative class "
             f"itself is at its null ({pct(one['relief']['rate_null_mean'], 1)}, {peq(one['relief']['p_up'])}) in the directed data and above it "
             f"({pct(sone['relief']['rate_null_mean'], 1)} null, {peq(sone['relief']['p_up'])}) in the 'sum' triangles, while the all-negative class resists relief "
             f"({pct(alln['relief']['rate_null_mean'], 1)} null, below it with {peq(alln['relief']['p_dn'])}). The asymmetry is carried by the stability of all-negative "
             "triples, which is a late pattern (section 3.5).")
    L.append("")
    L.append("**Weak (Davis) vs strict (Heider) balance.** Weak fits better than strict on every count. DDD is enriched from wave 5 on (z up to "
             f"{cm['z'][:, i('DDD')].max():+.1f}), the all-negative triangle is enriched under both symmetrisations, all-negative triples neither convert "
             f"({alln['strict']['num_obs']} of {tri['classes']['all_neg']['start_obs']}) nor dissolve at the null rate ({pct(alln['weak']['rate_obs'], 0)} stay complete against "
             f"{pct(alln['weak']['rate_null_mean'], 0)}), and the one-negative form is depleted but still common. Strict balance as a total rule is refuted "
             "on this group, as on the online networks (084 §4); the weak form survives as a depletion, not a prohibition.")
    L.append("")
    L.append("**What the recode does.** It sets how many ties are signed, hence how many triples are at risk (directed one-negative at risk: "
             + ", ".join(f"{r} {res['cells']['triple']['stats']['all']['classes']['one_neg']['start_obs']}" for r, res in out['recodes'].items())
             + ") and so the power; and it is a choice the files do not constrain [L4479]. The static contrasts (LLD, LDL depleted; DLL, DDD enriched; pool depleted) "
             "hold under all four cuts (section 4); D&K's ten wave-by-wave claims hold for "
             + ", ".join(f"{v}/10 at {r}" for r, v in held.items())
             + ", so [L4478]'s \"qualitative results also hold\" is true of the contrasts, not of the details. The conversion results move with the cut: "
             f"the strict ratio for the one-negative class runs {min(ratios):.1f}-{max(ratios):.1f} and its p {min(p_one):.2f}-{max(p_one):.2f}, and the 'agree' "
             f"rule never reaches a usable count (at most {agree_seen} one-negative triangles seen over all waves and cuts). The recode assumption therefore decides how "
             "powerful the test is and whether a marginal result survives; it does not decide the static verdicts.")
    L.append("")
    L.append("**Status of v0.1 §7, n = 3.**")
    L.append("")
    L.append("- *Refuted:* the symmetric triangle rule as a description of directed ties (DLL); strict balance as a total empirical rule (DDD enriched and stable).")
    L.append(f"- *Supported:* a depletion of the one-negative class in aggregate (directed pool 15/15 waves, 'sum' {len(under_waves)}/15), the weak form of balance, and the "
             "relief asymmetry between one-negative and all-negative triples, each with the caveats above (one group, ranks recoded to signs, popularity free in the null).")
    L.append(f"- *Not decided:* whether one-negative triples convert to balance faster than a no-pressure null does: {peq(one['strict']['p_up'])} directed, "
             f"{peq(sone['strict']['p_up'])} 'sum', difference from all-negative not significant, and the pre-specified 'agree' reading has no data. A decisive run "
             "needs a longer signed panel with explicit negatives, which D&K ask for [L4479] and which the ledger still lacks (v0 §7).")
    L.append("")
    return L


# ------------------------------------------------------------------ cli

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="download newfrat.dat for local use (git-ignored); verifies sha256")
    sub.add_parser("check", help="load the local file and run every integrity check")
    rp = sub.add_parser("report", help="run everything and write results/newcomb_n3.md")
    rp.add_argument("--draws", type=int, default=N_DRAWS)
    rp.add_argument("--seed", type=int, default=SEED)
    rp.add_argument("--out", type=Path, default=RESULTS)
    args = ap.parse_args(argv)
    if args.cmd == "fetch":
        print(f"wrote {nc.fetch()}")
    elif args.cmd == "check":
        r = nc.load_ranks()
        print(f"ok: {r.shape} ranks, sha256 {nc.sha256_of(nc.DATA_FILE)}")
    else:
        out = run(args.draws, args.seed)
        text = build_report(out)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
