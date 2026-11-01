"""Run the wiki-RfA conversion test and the Bitcoin formation check end to end and write
sim/results/wikirfa_conversion.md.

    cd sim
    ~/.local/bin/uv run python -m models.wikirfa_report fetch     # three SNAP files, local use only, git-ignored
    ~/.local/bin/uv run python -m models.wikirfa_report report    # about 5 minutes on 8 cores; writes results/wikirfa_conversion.md

Everything computed lives in models/wikirfa.py (ledger ids L4547-L4668, L4854, L4855 are cited there); this module
only organises the runs and formats the tables.  Seeded: the same command reproduces the numbers.  Only computed
statistics are written out (counts, rates, p-values), never votes, names or comments, which are not ours to
redistribute (sim/data/README.md).
"""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

import numpy as np

from models import wikirfa as wr

RESULTS = Path(__file__).resolve().parents[1] / "results" / "wikirfa_conversion.md"

# the nulls of the main tables, in the order shown
MAIN_NULLS = ("voter_uncond", "ctx_voter", "ctx_voter_res", "ctx_candidacy", "ev_cur_old", "ev_pair_old",
              "ev_voter_old", "ev_cur_old_deg", "ev_cur_old_pos")
NULL_TITLE = {
    "voter_uncond": "the brief: signs shuffled within voter, conversions re-determined",
    "ctx_voter": "conversions held; context signs shuffled within voter",
    "ctx_voter_res": "conversions held; context signs shuffled within voter and candidacy outcome",
    "ctx_candidacy": "conversions held; context signs shuffled within candidacy",
    "ev_cur_old": "contexts held; who converts permuted within the same new candidacy and old sign",
    "ev_pair_old": "contexts held; permuted within the same old and new candidacy and old sign",
    "ev_voter_old": "contexts held; permuted within the same voter and old sign",
    "ev_cur_old_deg": "as ev_cur_old, and within terciles of the number of triples",
    "ev_cur_old_pos": "as ev_cur_old, and within terciles of the voter's share of positive votes",
}
PRIMARY_EVENT_NULLS = ("ev_cur_old", "ev_voter_old")
STATS = ("share_w", "share_s", "share_w_up", "share_w_down", "r0", "r1", "r2", "r3", "r1_minus_r3", "r_bal", "r1_minus_rbal",
         "n0", "n1", "n2", "n3")
FIRST_TIE_KEYS = (
    "repair_DLL", "repair_LDL", "repair_LLD", "repair_LLDLDL", "repair_DLL_minus_LDL", "repair_DLL_minus_others",
    "join_DLL", "join_LDL", "join_LLD", "join_LLDLDL", "join_DLL_minus_LDL", "join_DLL_minus_others",
    "join_inc", "join_notinc", "join_inc_minus_notinc",
    "comp_DLL", "comp_LDL", "comp_LLD")
ERA_SPLIT = float(datetime.date(2007, 1, 1).toordinal())


def _all_stats(net: wr.Network, obs: dict, null: dict) -> dict:
    """compare() for every statistic the report quotes, for one network against one null run."""
    D = wr.derived(null["cells"])
    out = {k: wr.compare(obs["d_" + k], D[k]) for k in STATS}
    out["event_share"] = wr.compare(obs["event_share"], null["event_share"])
    oi, ni = wr.interaction_stats(obs["cells"]), wr.interaction_stats(null["cells"])
    for k in ("I", "I_FF", "I_FB", "I_BF", "I_BB"):
        out[k] = wr.compare(oi[k], ni[k])
    of, nf = wr.first_tie_stats(obs["cells"]), wr.first_tie_stats(null["cells"])
    for k in FIRST_TIE_KEYS:
        out["ft_" + k] = wr.compare(of[k], nf[k])
    for typ in wr.DK_UNBALANCED:
        for o in (0, 1, 2):
            k = f"rate_{typ}_{wr.ORIENT[o]}"
            out["ft_" + k] = wr.compare(of[k], nf[k])
    out["conv_mean"] = null["conv"].mean(0).tolist()
    return out


def variants(raw: wr.RawVotes, cands: wr.Candidacies, base: wr.Network) -> dict[str, wr.Network]:
    """The secondary cuts.  Each is the same votes and transitions with fewer instances, or a rebuilt network."""
    ctx, vt, tr = base.ctx, base.vt, base.trans
    out: dict[str, wr.Network] = {}
    out["context cut-off at the vote, not the candidacy start"] = wr.build_network(raw, cands, cutoff="vote")
    covoter = (ctx.o % 2 == 0) & (vt.cy[ctx.e2] == vt.cy[tr.prev[ctx.tr]])      # w voted on v at the old candidacy too
    out["no co-voters of the old candidacy (w -> v tie not from the old candidacy)"] = base.restrict(~covoter)
    age = np.maximum(tr.cutoff[ctx.tr] - vt.t[ctx.e1], tr.cutoff[ctx.tr] - vt.t[ctx.e2])
    out["contexts at most two years old"] = base.restrict(age <= 730.0)
    for o in range(4):
        out[f"orientation {wr.ORIENT[o]} only"] = base.restrict(ctx.o == o)
    out["new candidacy before 2007"] = base.restrict(tr.cutoff[ctx.tr] < ERA_SPLIT)
    out["new candidacy in 2007 or later"] = base.restrict(tr.cutoff[ctx.tr] >= ERA_SPLIT)
    raw_nd = wr.RawVotes(raw.voter, raw.cand, np.where(np.isnan(raw.t), 0, raw.vote).astype(np.int8), raw.res, raw.yea, raw.t,
                         raw.n_users, raw.notes)
    out["undated votes dropped"] = wr.build_network(raw_nd, cands)
    return out


def run(n_draws: int = wr.N_DRAWS, seed: int = wr.SEED, workers: int | None = None, bitcoin: bool = True,
        progress=print) -> dict:
    """Compute everything the report needs.  Returns plain dicts and arrays."""
    raw = wr.load_wikirfa()
    cands = wr.assign_candidacies(raw)
    net = wr.build_network(raw, cands)
    out: dict = {"n_draws": n_draws, "seed": seed, "raw_notes": raw.notes, "vt_notes": net.vt.notes,
                 "resign117": wr.resign_counts_117(raw), "char": wr.characterise(net), "types": wr.type_table(net)}
    obs = wr.observed(net)
    out["obs"] = obs
    out["obs_first_tie"] = wr.first_tie_stats(obs["cells"])
    out["ft_counts"] = wr.dk_table(obs["cells"])
    out["obs_interaction"] = wr.interaction_stats(obs["cells"])
    out["main"] = {}
    for name in MAIN_NULLS:
        progress(f"null {name}")
        nul = wr.run_null(net, name, n_draws, seed, workers)
        out["main"][name] = _all_stats(net, obs, nul)
        if name == "ev_cur_old":
            out["ev_cur_old_cells_mean"] = nul["cells"].mean(0)
    out["variants"] = {}
    for vname, vnet in variants(raw, cands, net).items():
        vobs = wr.observed(vnet)
        out["variants"][vname] = {"n_inst": int(vobs["d_n_inst"]), "n_chg": int(vobs["d_n_chg"]), "obs": {
            "share_w": float(vobs["d_share_w"]), "event_share": vobs["event_share"]}, "nulls": {}}
        for nname in PRIMARY_EVENT_NULLS:
            progress(f"variant {vname} / {nname}")
            nul = wr.run_null(vnet, nname, n_draws, seed, workers)
            out["variants"][vname]["nulls"][nname] = _all_stats(vnet, vobs, nul)
    if bitcoin:
        out["bitcoin"] = run_bitcoin(n_draws, seed, progress)
    return out


def run_bitcoin(n_draws: int, seed: int, progress=print) -> dict:
    res = {}
    for src in (wr.OTC, wr.ALPHA):
        progress(f"bitcoin {src.key}")
        d = wr.load_bitcoin(src)
        proj = wr.bitcoin_projection(d)
        r = {
            "ratings": len(d["src"]), "positive": int((d["rating"] > 0).sum()), "negative": int((d["rating"] < 0).sum()),
            "nodes": proj.n_nodes, "repeat_ordered_pairs": len(d["src"]) - len(np.unique(d["src"] * 1_000_000 + d["dst"])),
            "pairs": len(proj.sign), "both_signs": proj.n_both_signs, "triangles": len(proj.tri), "tied": int(proj.tied.sum()),
            "all": wr.bitcoin_stats(proj.sign, proj.tri), "ordered": wr.bitcoin_stats(proj.sign, proj.tri, ~proj.tied),
        }
        for nm, within in (("null_global", None), ("null_rater", "rater"), ("null_ratee", "ratee")):
            r[nm] = {"all": wr.bitcoin_null(proj, d, n_draws, seed, within=within),
                     "ordered": wr.bitcoin_null(proj, d, n_draws, seed, within=within, subset=~proj.tied)}
        res[src.key] = r
    return res


# ------------------------------------------------------------------ formatting

def pc(x: float, d: int = 1) -> str:
    return f"{100 * x:.{d}f}%"


def pp(x: float, d: int = 1) -> str:
    return f"{100 * x:+.{d}f}"


def fp(p: float, B: int) -> str:
    lim = 1.0 / (B + 1)
    if p <= lim * 1.0001:
        return f"<{lim:.0e}".replace("e-0", "e-")
    return f"{p:.3f}" if p >= 0.001 else f"{p:.1e}".replace("e-0", "e-")


def zs(c: dict) -> str:
    return f"{c['z']:+.1f}"


def ex_cell(c: dict, scale: float = 100.0, d: int = 1) -> str:
    """'null mean | excess | z' pieces for a table row."""
    return f"{c['mean'] * scale:.{d}f} | {(c['obs'] - c['mean']) * scale:+.{d}f} | {zs(c)}"


def table(header: list[str], rows: list[list[str]], align: str | None = None) -> list[str]:
    align = align or ("l" + "r" * (len(header) - 1))
    sep = " | ".join(":---" if a == "l" else "---:" for a in align)
    lines = ["| " + " | ".join(header) + " |", "| " + sep + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return lines


# ------------------------------------------------------------------ the report

def _keep_review(text, path):
    """`text` with a hand-written '## Review (' section at the end of the existing file at `path` kept, so
    regenerating the numbers does not delete a review of them."""
    p = Path(path)
    if p.exists():
        old = p.read_text(encoding="utf-8")
        i = old.find("\n## Review (")
        if i >= 0:
            return text.rstrip("\n") + "\n" + old[i:]
    return text


def build_report(out: dict) -> str:
    B, seed = out["n_draws"], out["seed"]
    M, V, C, O = out["main"], out["variants"], out["char"], out["obs"]
    raw_n, vn = out["raw_notes"], out["vt_notes"]
    r117 = out["resign117"]
    L: list[str] = []
    add = L.append

    def X(null: str, key: str) -> dict:
        return M[null][key]

    def excess(null: str, key: str) -> float:
        c = M[null][key]
        return c["obs"] - c["mean"]

    # --- guards: the verdict text below states these; a re-run that breaks one must be re-read, not published
    assert X("voter_uncond", "share_w")["p_ge"] <= 2.0 / (B + 1) and excess("voter_uncond", "share_w") > 0.05
    assert abs(X("voter_uncond", "share_w")["mean"] - 0.5) < 0.01
    assert X("ctx_candidacy", "share_w")["p_ge"] > 0.05 and excess("ctx_candidacy", "share_w") < 0.01
    assert all(excess(n, "share_w") > 0.005 and X(n, "share_w")["p_ge"] < 0.01 for n in ("ev_cur_old", "ev_pair_old", "ev_voter_old", "ev_cur_old_deg", "ev_cur_old_pos"))
    assert 0.02 < excess("ev_cur_old", "share_w") < 0.04 and 0.008 < excess("ev_voter_old", "share_w") < 0.025
    assert all(X(n, "I_FB")["z"] > 3 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos")) and all(abs(X(n, "I_FF")["z"]) < 2 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"))
    assert all(X(n, "I")["z"] > 3 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"))
    assert all(X(n, "r1")["z"] > 3 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos")) and all(abs(X(n, "r3")["z"]) < 2.5 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"))
    assert X("ev_cur_old", "r1_minus_r3")["z"] > 3 and abs(X("ev_voter_old", "r1_minus_r3")["z"]) < 2 and abs(X("ev_cur_old_pos", "r1_minus_r3")["z"]) < 2
    assert all(X(n, "ft_join_DLL_minus_LDL")["z"] > 1.5 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"))
    assert all(abs(X(n, "ft_join_LDL")["z"]) < 2 for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"))
    assert abs(X("ev_cur_old_pos", "ft_repair_DLL_minus_LDL")["z"]) < 1.5

    add("# Wiki-RfA and Bitcoin: the tie-conversion half of the v0.1 n = 3 test, on explicit-sign data")
    add("")
    add(f"_Generated {datetime.date.today().isoformat()} by `uv run python -m models.wikirfa_report report` (seed {seed}, {B:,} null draws). "
        "Code: `sim/models/wikirfa.py`, `sim/models/wikirfa_report.py`; checks: `sim/tests/test_wikirfa_conversion.py`. Ledger ids are the lines of "
        "`docs/ledger.jsonl` with source \"117 §\" (L4547-L4668, L4854, L4855). Results are computed statistics only: the SNAP files are local-use-only "
        "and are not redistributed (`sim/data/README.md`), and no vote text, comment or user name is read into a result._")
    add("")
    add("**What was tested (v0.1 §7, n = 3; v0's hypothesis, not a source's).** In longitudinal signed triads the one-negative triangle must convert to a "
        "balanced triangle faster than the all-negative one, and \"if conversion runs at the null rate, (4.2b)/(5.1) is refuted\". The Newcomb run "
        "(`results/newcomb_n3.md`) left the conversion half undecided: 15 and 33 events, ranks recoded to signs, 17 men. Wikipedia's requests for adminship "
        f"are the first explicit-sign file in which the same ordered pair is signed twice: a voter rates a candidate at a candidacy and again at a later "
        f"candidacy of the same candidate, sometimes with the opposite sign [L4564]. Each third party in a triple is a user tied to both, and the triple is judged "
        "before and after the re-vote; the 16 directed triad types are those of Leskovec, Huttenlocher & Kleinberg (106 §1.2).")
    add("")

    # ------------------------------------------------------------ verdict
    pw = lambda n: X(n, "share_w")  # noqa: E731
    ev = lambda n: X(n, "event_share")  # noqa: E731
    r1 = lambda n: X(n, "r1")  # noqa: E731
    add("## Verdict")
    add("")
    add(f"**In short.** Against the brief's own null (signs shuffled within voter, {B:,} draws) conversion moves triples toward weak balance {pp(excess('voter_uncond', 'share_w'))[1:]} points more than chance, p {fp(pw('voter_uncond')['p_ge'], B)}; "
        f"but {pp(min(excess('voter_uncond', 'share_w') - excess(n, 'share_w') for n in ('ctx_voter', 'ctx_voter_res', 'ctx_candidacy')))[1:]} to {pp(max(excess('voter_uncond', 'share_w') - excess(n, 'share_w') for n in ('ctx_voter', 'ctx_voter_res', 'ctx_candidacy')))[1:]} of that is the {pc(C['n_up'] / C['n_conv'], 0)} oppose-to-support direction mix. "
        f"Holding the network and permuting who converts leaves {pp(excess('ev_voter_old', 'share_w'))[1:]} to {pp(excess('ev_cur_old', 'share_w'))[1:]} points (z {zs(pw('ev_voter_old'))} to {zs(pw('ev_cur_old'))}); the part that only balance could produce is confined to triples where u and v rated the same third party, and the friend-of-a-friend chain shows none. "
        "The first-tie asymmetry is a property of the voter, not the triple. Bitcoin's closure figure reproduces and shrinks under reputation-preserving baselines. For v0.2 that is a weak, setting-specific agreement term, not a law.")
    add("")
    j = lambda n, k: X(n, "ft_" + k)  # noqa: E731
    fi = lambda n, k: X(n, "ft_" + k)["obs"] - X(n, "ft_" + k)["mean"]  # noqa: E731
    bt = out.get("bitcoin")
    add(f"- **Data and terms.** SNAP wiki-RfA (198,275 votes, 2003 to May 2013; West, Paskov, Leskovec & Potts 2014) and the Bitcoin OTC and Alpha rating files, fetched on 2026-11-01 from `snap.stanford.edu` into git-ignored `sim/data/`, sha256 recorded "
        "in `sim/data/README.md`. The pages state no terms and ask for citations; the wiki-RfA \"License\" link is the SNAP software BSD licence, and the comments are Wikipedia text (CC BY-SA), which the parser streams past and stores none of. "
        "Nothing stated forbids local research use of a public download, so the run went ahead; nothing is committed or redistributed.")
    add(f"- **Counts.** {raw_n['n_records']:,} records leave {vn['n_usable']:,} non-neutral votes with a named voter, a placeable candidacy and another user as candidate (neutral {vn['n_neutral']:,}, empty voter {vn['n_empty_voter']:,}, self {vn['n_self']}, unplaceable undated {vn['n_unplaced']} dropped; the groups overlap), "
        f"and {vn['n_rows']:,} (voter, candidate, candidacy) votes after collapsing {vn['n_collapsed_within_candidacy']:,} repeats inside a candidacy: {vn['cands_n_candidacies']:,} candidacies of {vn['cands_n_candidates']:,} candidates. **{C['n_trans']:,} re-votes** (consecutive votes of one voter on one candidate at different candidacies, {C['n_voters_revote']:,} voters); "
        f"**{C['n_conv']:,} conversions**: {C['n_up']} oppose-to-support, {C['n_down']} support-to-oppose, in {C['n_pairs_with_conv']:,} pairs, by {C['n_voters_conv']} voters, on {C['n_cands_conv']} candidates. 117's 677 reproduces exactly under its own rule "
        f"({r117['cells'][(-1, 1)]} + {r117['cells'][(1, -1)]}: first vote per year, first against last) and is a lower bound. {C['n_conv_with_ctx']:,} conversions sit in at least one triple: {C['n_inst']:,} instances (re-vote, third party, orientation).")
    add(f"- **What a conversion is here.** {pc(C['rate_conv_old_neg'])} of re-votes after an oppose flip to support, {pc(C['rate_conv_old_pos'])} after a support flip to oppose; {C['res_cross']['up'][(-1, 1)]} of the {C['n_up']} oppose-to-support conversions are a failed candidacy followed by a passed one. "
        "Most conversions are a candidate judged better the second time, not a tie settling after tension.")
    add(f"- **Against the brief's null, conversion moves triples toward weak balance far more than chance: {pc(O['d_share_w'])} of the weak-balance changes are repairs against {pc(pw('voter_uncond')['mean'])}, {pp(excess('voter_uncond', 'share_w'))} points, p {fp(pw('voter_uncond')['p_ge'], B)} "
        f"({B:,} draws, signs shuffled within voter).** But that null makes as many support-to-oppose as oppose-to-support conversions ({X('voter_uncond', 'conv_mean')[2]:.0f} against {X('voter_uncond', 'conv_mean')[1]:.0f}; observed {C['n_down']} against {C['n_up']}), and in a mostly positive context the direction alone moves the share: "
        f"holding the observed conversions and shuffling only context signs gives {pc(pw('ctx_voter')['mean'])} (within voter), {pc(pw('ctx_voter_res')['mean'])} (within voter and candidacy outcome), {pc(pw('ctx_candidacy')['mean'])} (within candidacy: {pp(excess('ctx_candidacy', 'share_w'))} points, p {fp(pw('ctx_candidacy')['p_ge'], B)}). "
        f"**{pp(min(excess('voter_uncond', 'share_w') - excess(n, 'share_w') for n in ('ctx_voter', 'ctx_voter_res', 'ctx_candidacy')))[1:]} to {pp(max(excess('voter_uncond', 'share_w') - excess(n, 'share_w') for n in ('ctx_voter', 'ctx_voter_res', 'ctx_candidacy')))[1:]} of the {excess('voter_uncond', 'share_w') * 100:.1f} points are the direction mix (the observed old and new signs).**")
    add(f"- **Holding the network and permuting who converts (Newcomb's conditional design, the dynamic test) leaves a small excess that halves under voter controls.** Repair share {pc(O['d_share_w'])} against {pc(pw('ev_cur_old')['mean'])} for re-votes with the same new candidacy and old sign "
        f"({pp(excess('ev_cur_old', 'share_w'))} points, z {zs(pw('ev_cur_old'))}, p {fp(pw('ev_cur_old')['p_ge'], B)}), {pc(pw('ev_voter_old')['mean'])} within the same voter and old sign ({pp(excess('ev_voter_old', 'share_w'))}, z {zs(pw('ev_voter_old'))}, p {fp(pw('ev_voter_old')['p_ge'], B)}), "
        f"{pc(pw('ev_cur_old_pos')['mean'])} also within terciles of the voter's generosity ({pp(excess('ev_cur_old_pos', 'share_w'))}, z {zs(pw('ev_cur_old_pos'))}). Counting each conversion once: {pp(excess('ev_cur_old', 'event_share'))}, {pp(excess('ev_voter_old', 'event_share'))}, {pp(excess('ev_cur_old_pos', 'event_share'))} points "
        f"(z {zs(ev('ev_cur_old'))}, {zs(ev('ev_voter_old'))}, {zs(ev('ev_cur_old_pos'))}). A re-vote inside a one-negative triple flips at {pc(O['d_r1'])} against {pc(r1('ev_cur_old')['mean'])} / {pc(r1('ev_voter_old')['mean'])} / {pc(r1('ev_cur_old_pos')['mean'])} "
        f"({pp(excess('ev_cur_old', 'r1'))} / {pp(excess('ev_voter_old', 'r1'))} / {pp(excess('ev_cur_old_pos', 'r1'))} points); inside a weakly balanced one it flips at its null ({pc(O['d_r_bal'])}).")
    add(f"- **The excess is agreement on a third party, not a friend of a friend.** A double-difference contrast in which the voter's generosity and the candidate's reception cancel (a planted 20-point lift in the strictly unbalanced cells scores 0.4, an additive effect 0) is at its null in the chain u -> w -> v "
        f"(FF: {excess('ev_cur_old', 'I_FF'):+.3f}, z {zs(X('ev_cur_old', 'I_FF'))}) and above it where u and v both rated the third party (FB: {excess('ev_cur_old', 'I_FB'):+.3f}, z {zs(X('ev_cur_old', 'I_FB'))}; within voter {excess('ev_voter_old', 'I_FB'):+.3f}, z {zs(X('ev_voter_old', 'I_FB'))}), "
        f"less where the third party rated both (BF: {excess('ev_cur_old', 'I_BF'):+.3f}, z {zs(X('ev_cur_old', 'I_BF'))}; within voter z {zs(X('ev_voter_old', 'I_BF'))}). The FF repair-share excess "
        f"({pp(V['orientation FF only']['nulls']['ev_cur_old']['share_w']['obs'] - V['orientation FF only']['nulls']['ev_cur_old']['share_w']['mean'])} points) is the voter's own generosity: it vanishes within voter ({pp(V['orientation FF only']['nulls']['ev_voter_old']['share_w']['obs'] - V['orientation FF only']['nulls']['ev_voter_old']['share_w']['mean'])}).")
    add(f"- **v0's contrast, one-negative faster than all-negative, is not a robust finding.** The one-negative class flips above its null in every event-permutation null; the all-negative class does not ({pc(O['d_r3'])} against {pc(X('ev_cur_old', 'r3')['mean'])}, z {zs(X('ev_cur_old', 'r3'))}). "
        f"The difference r1 - r3 exceeds its null by {pp(excess('ev_cur_old', 'r1_minus_r3'))} points (z {zs(X('ev_cur_old', 'r1_minus_r3'))}) with candidacy held, by {pp(excess('ev_voter_old', 'r1_minus_r3'))} (z {zs(X('ev_voter_old', 'r1_minus_r3'))}) within voter and {pp(excess('ev_cur_old_pos', 'r1_minus_r3'))} (z {zs(X('ev_cur_old_pos', 'r1_minus_r3'))}) with generosity held.")
    add(f"- **First-tie asymmetry (Q2): which tie is negative does predict the conversion, but as a property of the voter, not of the triple.** Where a positive tie turns negative (a join), the converting voter joins above null exactly when the lone negative tie touches him "
        f"(DLL-FF, DLL-BF, LLD-FB: {pc(j('ev_cur_old', 'join_inc')['obs'])} against {pc(j('ev_cur_old', 'join_inc')['mean'])}, z {zs(j('ev_cur_old', 'join_inc'))}) and not when it is the third party's tie to the candidate (LDL-FF, LDL-FB, LLD-BF: {pc(j('ev_cur_old', 'join_notinc')['obs'])} against {pc(j('ev_cur_old', 'join_notinc')['mean'])}, z {zs(j('ev_cur_old', 'join_notinc'))}); "
        f"contrast {pp(fi('ev_cur_old', 'join_inc_minus_notinc'))} points over null (z {zs(j('ev_cur_old', 'join_inc_minus_notinc'))}) with the candidacy held, but {pp(fi('ev_voter_old', 'join_inc_minus_notinc'))} (z {zs(j('ev_voter_old', 'join_inc_minus_notinc'))}) with the voter held and {pp(fi('ev_cur_old_pos', 'join_inc_minus_notinc'))} (z {zs(j('ev_cur_old_pos', 'join_inc_minus_notinc'))}) within generosity terciles: a voter with a negative tie to someone is a voter who turns against candidates, whatever the triple. "
        f"In D&K's terms the first-tie-negative form DLL joins at {pc(j('ev_cur_old', 'join_DLL')['obs'])} against {pc(j('ev_cur_old', 'join_DLL')['mean'])} and the second-tie-negative form LDL at its null ({pc(j('ev_cur_old', 'join_LDL')['obs'])} against {pc(j('ev_cur_old', 'join_LDL')['mean'])}). "
        "Repairs (the converting tie is the lone negative one) are above null for all three forms, most for DLL, but the DLL - LDL gap is explained by voter generosity. The reactive first-tie form is the reverse of Newcomb's, where DLL was the stable one [L4508, L4511].")
    if bt:
        o, a = bt["otc"], bt["alpha"]
        shr = lambda r, nn, sub: r[nn][sub]["balanced"] / r[nn][sub]["n"]  # noqa: E731
        add(f"- **Bitcoin OTC and Alpha (formation only; no pair is rated twice).** 117's figure reproduces exactly: OTC {o['all']['balanced']:,} of {o['all']['n']:,} triangles balanced ({pc(o['all']['balanced'] / o['all']['n'])}) against {pc(shr(o, 'null_global', 'all').mean())} under the global sign shuffle; "
            f"Alpha {a['ordered']['balanced']:,} of {a['ordered']['n']:,} strictly ordered ({pc(a['ordered']['balanced'] / a['ordered']['n'])}; {pc(a['all']['balanced'] / a['all']['n'])} of all {a['all']['n']:,}) against {pc(shr(a, 'null_global', 'ordered').mean())}. "
            f"But the excess shrinks with a stricter baseline: within rater {pc(shr(o, 'null_rater', 'all').mean())} (OTC) and {pc(shr(a, 'null_rater', 'ordered').mean())} (Alpha); within ratee, i.e. holding each trader's reputation, {pc(shr(o, 'null_ratee', 'all').mean())} (OTC, still below the data) and {pc(shr(a, 'null_ratee', 'ordered').mean())} (Alpha, strictly ordered, where it reaches the data: p {fp(wr.compare(a['ordered']['balanced'] / a['ordered']['n'], shr(a, 'null_ratee', 'ordered'))['p_ge'], B)}). "
            "Whether the all-negative triangle is enriched (117) or depleted also depends on the baseline (section 8).")
    add("- **For v0.2.** Tie conversion toward weak balance exceeds the null on wiki-RfA, but little: "
        f"{pp(excess('ev_voter_old', 'share_w'))} to {pp(excess('ev_cur_old', 'share_w'))} points of repair share and {pp(excess('ev_voter_old', 'r1'))} to {pp(excess('ev_cur_old', 'r1'))} points of flip rate in one-negative triples once the network, the candidacy and the direction are held, against {pp(excess('voter_uncond', 'share_w'))} under the brief's null, most of which is the {pc(C['n_up'] / C['n_conv'], 0)} oppose-to-support mix. "
        "The part that only balance could produce (the interaction) is local to triples where u and v rated the same third party, so v0.2 can carry it as a weak, setting-specific agreement term with a fitted coefficient, not as a law, and the chain form of (4.2b) (friend of a friend) has no support from conversion. "
        f"Caveats: **votes are not friendships** (a tie in a triple is a vote at some other candidacy); **a vote is a one-shot evaluation** of a candidacy, and most conversions are the candidate improving; **timing is by candidacy** (about a week), not by tie; "
        f"**selection into re-voting** is severe ({pc(C['n_trans'] / C['n_pairs_total'])} of pairs re-vote, almost all after a failed candidacy, {C['n_voters_conv']} voters supply the conversions). Section 9.")
    add("")

    # ------------------------------------------------------------ 1 data
    add("## 1. Data, terms, cleaning")
    add("")
    add(f"- **Source and terms [L4561, L4567].** `snap.stanford.edu/data/wiki-RfA.txt.gz` (14,936,383 bytes, sha256 `{wr.WIKIRFA.sha256}`) and the two Bitcoin files (397,258 and 149,480 bytes); plain public downloads, no login or access control; "
        "`robots.txt` disallows only course-video directories. Neither page states terms; both ask for citations (West et al. 2014, TACL 2: 297-310; Kumar et al. 2016 and 2018). The wiki-RfA comments are Wikipedia text under CC BY-SA 4.0 / GFDL (117 §3.3), skipped unread at parse time and never stored; "
        "user names are replaced by integers on load and written nowhere. Absence of a stated licence is not a grant, so the files are used for local runs only (git-ignored, never committed) and only statistics are published.")
    add(f"- **The file reproduces 117's counts [L4562, L4563].** {raw_n['n_records']:,} records: 144,451 support, 41,176 oppose, 12,648 neutral; the per-year totals; {raw_n['n_users']:,} named users and {raw_n['n_empty_voter']:,} records with an empty voter. Found here: "
        f"{raw_n['dat_empty']:,} records have no time, one has an impossible one (hour 31), three month names carry slips (`Mya`, `Julu`, `Janry`, read as May, July, January).")
    add(f"- **A finding in the file: 18 elections carry both outcome labels, 15 of them as a complete copy.** Grouping a candidate's votes by (candidate, result) as 117's 3,926 elections do would make the copy a second candidacy and its votes 618 re-votes with a zero-day gap. "
        f"Candidacies here are a candidate's dated votes split at gaps of more than 14 days (the median span is 6.3 days); in {vn['cands_n_clusters_with_both_labels']} clusters both labels occur ({vn['cands_n_clusters_label_tie']} exact ties, equal numbers of votes under each label and the outcome unknown; in the rest a few votes carry the other label), and "
        f"{vn['cands_n_stray_clusters']} late or mis-dated stray signatures ({vn['cands_n_stray_votes']} votes) are folded into the nearest big candidacy. Undated votes join their candidacy by year; {vn['cands_n_unplaced_undated']} cannot be placed and are dropped.")
    add(f"- **117's 677 [L4564, L4855].** Under its rule (ordered pairs with a named voter, the first vote of the pair in each file year, the first and last non-neutral of those): {r117['multi_year_pairs']:,} pairs vote in more than one year, {r117['pairs_gt1_vote']:,} pairs carry more than one vote "
        f"({r117['votes_in_those']:,} votes), and {r117['cells'][(-1, 1)]} oppose-to-support plus {r117['cells'][(1, -1)]} support-to-oppose changes = **{r117['changes']}**, exactly. Its two non-changing cells do not reproduce: {r117['cells'][(1, 1)]:,} support-to-support and {r117['cells'][(-1, -1)]} oppose-to-oppose here, against 1,946 and 647 "
        f"in 117 (not resolved; they do not enter this analysis). Counting every sign change between consecutive candidacies gives **{C['n_conv']:,}**.")
    add("")

    # ------------------------------------------------------------ 2 conversions
    add("## 2. The conversions: direction, timing, selection, and the 16 types")
    add("")
    g = C["gap_days"]
    rc = C["res_cross"]
    rows = [
        ["after an oppose (old sign -)", f"{C['trans_old_neg']:,}", f"{C['n_up']}", pc(C["rate_conv_old_neg"]), f"{g['up'][2]:.0f}"],
        ["after a support (old sign +)", f"{C['trans_old_pos']:,}", f"{C['n_down']}", pc(C["rate_conv_old_pos"]), f"{g['down'][2]:.0f}"],
        ["all re-votes", f"{C['n_trans']:,}", f"{C['n_conv']:,}", pc(C["n_conv"] / C["n_trans"]), f"{g['conv'][2]:.0f}"],
    ]
    L += table(["re-votes", "n", "converted", "rate", "median days between the two votes, conversions"], rows)
    add("")
    add(f"Median gap for re-votes that did not convert: {g['nonconv'][2]:.0f} days; {pc(C['share_within_a_year'], 0)} of conversions fall within a year of the earlier vote; the clock is minutes in the file but a candidacy lasts about a week, so \"before\" means before the candidacy began. "
        f"Outcomes of the two candidacies, (earlier, later) = (failed, passed) / (failed, failed) / (passed, failed) / (passed, passed): all re-votes {rc['all'][(-1, 1)]:,} / {rc['all'][(-1, -1)]:,} / {rc['all'][(1, -1)]} / {rc['all'][(1, 1)]}; "
        f"oppose-to-support conversions {rc['up'][(-1, 1)]} / {rc['up'][(-1, -1)]} / {rc['up'][(1, -1)]} / {rc['up'][(1, 1)]}; support-to-oppose {rc['down'][(-1, 1)]} / {rc['down'][(-1, -1)]} / {rc['down'][(1, -1)]} / {rc['down'][(1, 1)]} "
        f"({C['n_trans'] - sum(rc['all'].values())} re-votes involve one of the {vn['cands_n_clusters_label_tie']} candidacies of unknown outcome). "
        f"Re-votes are {pc(C['n_trans'] / C['n_pairs_total'], 0)} of the {C['n_pairs_total']:,} voter-candidate pairs and come mostly from candidates who failed (a re-run after a pass is rare): **selection into re-voting is the selection of failed-then-re-run candidates and of the voters who turn up twice**. "
        f"The conversions are concentrated but not dominated: {C['n_voters_conv']} converting voters (at most {C['max_conv_per_voter']} conversions each; the ten largest hold {pc(C['top10_voter_share_conv'], 0)}), {C['n_cands_conv']} candidates. "
        "Conversions / re-votes by year of the later vote: " + ", ".join(f"{y}: {c}/{n}" for y, (c, n) in sorted(C["by_year"].items())) + ". "
        f"Candidacy of the converting vote, second / third / fourth / fifth of its candidate: {C['nth_candidacy'][2]} / {C['nth_candidacy'][3]} / {C['nth_candidacy'][4]} / {C['nth_candidacy'][5]} conversions out of {C['nth_candidacy_trans'][2]:,} / {C['nth_candidacy_trans'][3]:,} / {C['nth_candidacy_trans'][4]:,} / {C['nth_candidacy_trans'][5]:,} re-votes.")
    add("")
    add("**The 16 directed triad types [106 §1.2] over all instances.** F = the u-w tie runs u to w (first letter) or the w-v tie runs w to v (second letter), B = the reverse; p / m = the sign of the u-w tie then the w-v tie. "
        "\"Expected\" is the mean of the 10,000 draws of the Newcomb-style null (conversions permuted within the same new candidacy and old sign). Balance predicts the converting tie's sign on all 16 types, status on 8 [106 §1.2].")
    add("")
    cm = out["ev_cur_old_cells_mean"]
    rows = []
    for r in out["types"]:
        o = wr.ORIENT.index(r["type"][:2])
        a, b = (1 if r["type"][2] == "p" else -1), (1 if r["type"][3] == "p" else -1)
        m = (wr.CELL_O == o) & (wr.CELL_S1 == a) & (wr.CELL_S2 == b) & wr.CELL_CHG
        e_up, e_dn = float(cm[m & (wr.CELL_OLD < 0)].sum()), float(cm[m & (wr.CELL_OLD > 0)].sum())
        sym = lambda v: {1: "+", -1: "-", 0: "none"}[v]  # noqa: E731
        rows.append([r["type"], f"{r['n']:,}", f"{r['n_old_neg']:,}", f"{r['up']:,} ({e_up:,.0f})", pc(r["up"] / max(r["n_old_neg"], 1), 0),
                     f"{r['n_old_pos']:,}", f"{r['down']:,} ({e_dn:,.0f})", pc(r["down"] / max(r["n_old_pos"], 1), 0), sym(r["balance"]), sym(r["status"])])
    L += table(["type", "instances", "from -", "-> + (expected)", "rate", "from +", "+ -> - (expected)", "rate", "balance", "status"], rows, "lrrrrrrrrr")
    add("")
    T = {r["type"]: r for r in out["types"]}
    rate_up = lambda t: pc(T[t]["up"] / T[t]["n_old_neg"], 0)  # noqa: E731
    add(f"Reading. The rate of oppose-to-support conversion follows the sign of the u-w tie whatever the w-v tie is (FF: {rate_up('FFpp')} and {rate_up('FFpm')} when u -> w is positive, {rate_up('FFmp')} and {rate_up('FFmm')} when it is negative): "
        f"the voter's own generosity, which is not balance. The product structure that balance needs shows only where u and v rated the same third party (FB): from an oppose, conversion is {rate_up('FBpp')} when both ratings are positive, {rate_up('FBmm')} when both are negative, "
        f"{rate_up('FBpm')} and {rate_up('FBmp')} when they disagree.")
    add("")

    # ------------------------------------------------------------ 3 headline
    add("## 3. Do conversions move triples toward weak balance more than the null? (H1)")
    add("")
    add(f"**Statistic.** Over converting instances, FIX = a one-negative triple becomes balanced, BREAK = a weakly balanced one becomes one-negative; the share FIX / (FIX + BREAK) is {pc(O['d_share_w'], 2)} ({O['d_fix_w']:,} against {O['d_brk_w']:,}); strict balance {pc(O['d_share_s'], 2)}; "
        f"the event-level mean (each of {O['n_events']:,} conversions weighs one) {pc(O['event_share'], 2)}. Flipping any tie of a one-negative triple makes it balanced, so FIX is exactly \"the triple was one-negative\". "
        "Instances share ties, so the permutation nulls, not a binomial, carry the inference; p = (1 + #{null >= obs}) / (B + 1), one-sided.")
    add("")
    add("**What the nulls hold.** (1) *The brief:* every voter's non-neutral signs shuffled over his votes, targets and times kept, conversions re-determined. (2) *Context shuffles (conversions held):* the observed old and new sign of every re-vote is kept and only the signs of the "
        "context ties are shuffled, within voter, within voter and candidacy outcome, or within candidacy. They compare the converters' triples with random triples, so they are blind to the static depletion of one-negative triples (the (a) half of the test; table below). "
        "(3) *Event permutations (network held, Newcomb's conditional design):* contexts and old signs stay as observed and the conversion indicator is permuted among the re-votes of a stratum, so every pre-state class size is fixed and only *who converts* is random: "
        "same new candidacy and old sign (candidate-level consensus and direction held); same old and new candidacy; same voter and old sign (voter propensity held); and the first with terciles of the number of triples or of the voter's share of positive votes added. "
        "Group (3) is the dynamic test (it holds the pre-state, as Newcomb's conditional null held the start wave); group (2) compares the converters' triples with random ones. **(3) was added after (2)'s rows disagreed with each other and the brief's; that is post hoc and is why both are shown.**")
    add("")
    rows = []
    for n in MAIN_NULLS:
        a, e = X(n, "share_w"), X(n, "event_share")
        rows.append([n, NULL_TITLE[n], pc(a["mean"]), f"{(a['obs'] - a['mean']) * 100:+.1f}", zs(a), fp(a["p_ge"], B), pc(e["mean"]), f"{(e['obs'] - e['mean']) * 100:+.1f}", zs(e), fp(e["p_ge"], B)])
    L += table(["null", "what it holds", "share null", "excess (pp)", "z", "p", "event-level null", "excess (pp)", "z", "p"], rows, "llrrrrrrrr")
    add("")
    add(f"Observed pooled share {pc(O['d_share_w'], 1)}, event-level {pc(O['event_share'], 1)}. Excess in percentage points; p one-sided upper tail. "
        f"Number of conversions per draw in the brief's null: {X('voter_uncond', 'conv_mean')[0]:.0f} ({X('voter_uncond', 'conv_mean')[1]:.0f} oppose-to-support, {X('voter_uncond', 'conv_mean')[2]:.0f} support-to-oppose); in every other null {C['n_conv']:,} ({C['n_up']} and {C['n_down']}).")
    add("")
    add("**By direction** (share FIX / (FIX + BREAK) among oppose-to-support and among support-to-oppose conversions; the null mean, the excess in points and z):")
    add("")
    rows = []
    for n in ("ctx_voter_res", "ctx_candidacy", "ev_cur_old", "ev_voter_old", "ev_cur_old_pos"):
        u, d = X(n, "share_w_up"), X(n, "share_w_down")
        rows.append([n, f"{pc(u['obs'])} vs {pc(u['mean'])}", f"{(u['obs'] - u['mean']) * 100:+.1f}", zs(u), f"{pc(d['obs'])} vs {pc(d['mean'])}", f"{(d['obs'] - d['mean']) * 100:+.1f}", zs(d)])
    L += table(["null", "oppose -> support: obs vs null", "excess", "z", "support -> oppose: obs vs null", "excess", "z"], rows)
    add("")
    add("The two directions part under the context shuffles (support-to-oppose conversions sit in *less* tension-resolving contexts than random ones) and agree under the event permutations (both above null). "
        "That is the signature of the static depletion: the real network has fewer one-negative triples than a shuffled one, so a random context is more often a repair than a real one, and a converter's real context can be below the random baseline and above its non-converting neighbours at once.")
    add("")
    add("**Static depletion, for reference (the (a) half; instances by pre-state class, observed against the context shuffles).**")
    add("")
    rows = []
    for k, nm in ((0, "no negative"), (1, "one-negative"), (2, "two-negative"), (3, "all-negative")):
        rows.append([nm, f"{O['d_n' + str(k)]:,}"] + [f"{X(n, 'n' + str(k))['mean']:,.0f} ({pp((O['d_n' + str(k)] - X(n, 'n' + str(k))['mean']) / X(n, 'n' + str(k))['mean'], 0)}%)" for n in ("ctx_voter", "ctx_voter_res", "ctx_candidacy")])
    L += table(["pre-state class", "observed", "ctx_voter", "ctx_voter_res", "ctx_candidacy"], rows)
    add("")

    # ------------------------------------------------------------ 4 hazard
    add("## 4. Hazard by pre-state class (H2): v0's \"one-negative faster than all-negative\"")
    add("")
    add(f"The class is the number of negative ties among (u-w, w-v, old u-v): 0, 1, 2, 3. Class sizes (instances) {O['d_n0']:,} / {O['d_n1']:,} / {O['d_n2']:,} / {O['d_n3']:,}; they are fixed under the event permutations, so the rate of conversion in a class is comparable with its null "
        "(under the brief's null the sizes move and the rates are not comparable; not shown). Cells show observed vs null (excess in points, z, upper-tail p). A re-vote flips more easily from an oppose than from a support, so class 3 (which needs an old oppose) converts more than class 0 in every null; the question is the excess over the null.")
    add("")
    rows = []
    for n in ("ev_cur_old", "ev_pair_old", "ev_voter_old", "ev_cur_old_deg", "ev_cur_old_pos"):
        cells = [n]
        for k in ("r1", "r_bal", "r3", "r1_minus_rbal", "r1_minus_r3"):
            c = X(n, k)
            cells.append(f"{pc(c['obs'])} vs {pc(c['mean'])} ({(c['obs'] - c['mean']) * 100:+.1f}, z {zs(c)}, p {fp(c['p_ge'], B)})")
        rows.append(cells)
    L += table(["null", "one-negative (r1)", "weakly balanced (0, 2, 3)", "all-negative (r3)", "r1 - balanced", "r1 - r3"], rows, "lrrrrr")
    add("")
    add("One-negative triples flip above their null in every row; weakly balanced triples are at theirs (the largest departure is -0.5 points); the all-negative class never flips significantly faster than its null (excess between -3.2 and +1.4 points). "
        "v0's contrast holds against the null difference only where the voter is not held fixed. The prediction that conversion is *at the null rate* if balance does not operate is not what is seen: the one-negative rate is above it.")
    add("")

    # ------------------------------------------------------------ 5 interaction
    add("## 5. Where the excess sits: the balance-specific interaction")
    add("")
    add("The repair share mixes balance with two additive effects that are not balance: the voter's generosity (u's tie to w is positive, so u is positive toward v too) and the candidate's reception (w supports v, so u is drawn to). "
        "Strict balance predicts a *product*: the effect of the w-v sign should reverse with the u-w sign. Within each orientation and old sign the conversion rate of the four context cells (pp, pm, mp, mm) gives "
        "D = sgn(old)(r_pp + r_mm - r_pm - r_mp), which cancels both additive effects and is positive when conversion is higher exactly where the product of the three signs is negative (a planted full balance rule gives D = 0.4, a planted additive effect 0, `test_interaction_contrast_...`). "
        "I is the precision-weighted mean of the eight blocks. The nulls centre above zero because strata with higher conversion rates hold a different mix of context cells; the comparison is the excess over the null.")
    add("")
    rows = []
    for n in ("voter_uncond", "ctx_candidacy", "ev_cur_old", "ev_voter_old", "ev_cur_old_pos"):
        cells = [n]
        for k in ("I", "I_FF", "I_FB", "I_BF", "I_BB"):
            c = X(n, k)
            cells.append(f"{c['obs']:+.3f} vs {c['mean']:+.3f} (z {zs(c)})")
        rows.append(cells)
    L += table(["null", "I (all)", "FF: u->w->v", "FB: u->w<-v", "BF: u<-w->v", "BB: cycle"], rows, "lrrrrr")
    add("")
    add("FF is at its null in every row: no transitivity (friend of a friend) in the conversions. FB (u and v both rated w) carries it, BF (w rated both) a smaller part, BB (a directed cycle, few instances) nothing. "
        f"On the contrast's scale an excess of {excess('ev_cur_old', 'I'):.3f} means conversion is about {excess('ev_cur_old', 'I') * 50:.1f} points higher in the two strictly unbalanced context cells than in the two balanced ones, beyond the additive baseline (FB: {excess('ev_cur_old', 'I_FB') * 50:.1f}; within voter, all orientations {excess('ev_voter_old', 'I') * 50:.1f} and FB {excess('ev_voter_old', 'I_FB') * 50:.1f}). "
        "That is also what homophily of judgement predicts (u and v voted alike on w), and the data cannot separate the two: the sign law's similarity-as-attraction generator and balance coincide on this triple.")
    add("")

    # ------------------------------------------------------------ 6 first tie
    add("## 6. The first-tie asymmetry (Q2)")
    add("")
    add("D&K's types name the signs of an ordered triple i->j, j->k, i->k (L = +, D = -). With u -> v the converting tie, the orientation fixes where it sits: FF is (u->w, w->v, u->v), so the converting tie is **third**; FB is (u->v, v->w, u->w), **first**; BF is (w->u, u->v, w->v), **second**; BB is a cycle and has no D&K type. "
        "For a one-negative triple the lone negative tie is first (DLL), second (LDL) or third (LLD). Either the converting tie is that negative tie (a **repair**: oppose to support; the diagonal cells FF-LLD, FB-DLL, BF-LDL) or a positive tie turns negative (a **join**: the other six). "
        "Cells give the conversion rate (conversions / re-vote instances) against the null mean of the same-new-candidacy event permutation, with z.")
    add("")
    rows = []
    for typ in wr.DK_UNBALANCED:
        row = [f"**{typ}** ({'first' if typ == 'DLL' else 'second' if typ == 'LDL' else 'third'} tie negative)"]
        for o in (0, 1, 2):
            c = j("ev_cur_old", f"rate_{typ}_{wr.ORIENT[o]}")
            n_k = out["ft_counts"][(typ, o)]
            tag = " (repair)" if (typ, o) in (("LLD", 0), ("DLL", 1), ("LDL", 2)) else ""
            row.append(f"{n_k[1]:,}/{n_k[0]:,} = {pc(c['obs'])}{tag}; null {pc(c['mean'])}, z {zs(c)}")
        rows.append(row)
    L += table(["type", "FF (converting tie third)", "FB (first)", "BF (second)"], rows, "lrrr")
    add("")
    add("Contrasts, by kind of conversion. The repair rate of a type is its diagonal cell; the join rate pools its two off-diagonal cells.")
    add("")
    rows = []
    for lab, k in (("repair, DLL", "repair_DLL"), ("repair, LDL", "repair_LDL"), ("repair, LLD", "repair_LLD"), ("**repair: DLL - LDL**", "repair_DLL_minus_LDL"), ("repair: DLL - (LLD, LDL)", "repair_DLL_minus_others"),
                   ("join, DLL (first tie negative)", "join_DLL"), ("join, LDL (second)", "join_LDL"), ("join, LLD (third)", "join_LLD"), ("**join: DLL - LDL**", "join_DLL_minus_LDL"), ("join: DLL - (LLD, LDL)", "join_DLL_minus_others"),
                   ("join, negative tie touches the voter (DLL-FF, DLL-BF, LLD-FB)", "join_inc"), ("join, negative tie is w-v (LDL-FF, LDL-FB, LLD-BF)", "join_notinc"), ("**join: touches the voter - not**", "join_inc_minus_notinc"),
                   ("share of unbalanced conversions that are DLL", "comp_DLL"), ("... LDL", "comp_LDL"), ("... LLD", "comp_LLD")):
        cells = [lab, pc(j("ev_cur_old", k)["obs"])]
        for n in ("ev_cur_old", "ev_voter_old", "ev_cur_old_pos"):
            c = j(n, k)
            cells.append(f"{pc(c['mean'])} ({(c['obs'] - c['mean']) * 100:+.1f}, z {zs(c)}, p {fp(c['p_ge'], B)})")
        rows.append(cells)
    L += table(["", "observed", "null: same new candidacy", "null: same voter", "null: + voter generosity"], rows)
    add("")
    add("Reading. **Joins.** Each of the three join cells whose lone negative tie touches the converting voter (DLL-FF: u -> w negative; DLL-BF: w -> u negative; LLD-FB: u -> w negative) is above its null, and the three whose negative tie is the third party's tie to the candidate "
        f"(LDL-FF, LDL-FB: w -> v and v -> w; LLD-BF: w -> v) are at it: pooled {pc(j('ev_cur_old', 'join_inc')['obs'])} against {pc(j('ev_cur_old', 'join_inc')['mean'])} and {pc(j('ev_cur_old', 'join_notinc')['obs'])} against {pc(j('ev_cur_old', 'join_notinc')['mean'])}. "
        "D&K's \"first tie\" (position one) is a proxy for that incidence in the join cells, because the first tie of the ordered triple is one of u's ties whenever the converting tie is not the first. "
        f"With the voter held fixed the incidence contrast is {pp(fi('ev_voter_old', 'join_inc_minus_notinc'))} points (z {zs(j('ev_voter_old', 'join_inc_minus_notinc'))}) and within generosity terciles {pp(fi('ev_cur_old_pos', 'join_inc_minus_notinc'))} (z {zs(j('ev_cur_old_pos', 'join_inc_minus_notinc'))}): "
        "so the asymmetry is the voter's own negativity (a voter who has a negative tie to a third party is a voter who turns against candidates), not a feature of the triple and not shown to be rivalry for the third party [L4511]. "
        f"DLL minus LDL on its own is above its null in all three nulls (z {zs(j('ev_cur_old', 'join_DLL_minus_LDL'))}, {zs(j('ev_voter_old', 'join_DLL_minus_LDL'))}, {zs(j('ev_cur_old_pos', 'join_DLL_minus_LDL'))}) but is largely the incidence contrast under another name. "
        "**Repairs.** Repair rates are above null for all three forms and highest for DLL, but the DLL - LDL gap disappears once the voter's generosity is held. "
        "**Against Newcomb.** D&K found balance supported when the first tie is positive and contradicted when it is negative [L4508], and DLL over-represented and persistent; here the first-tie-negative form is the *more* reactive, "
        "in the direction balance asks for (the voter turns against a candidate whom a person the voter dislikes supports). The analyses do not measure the same thing: Newcomb's triple changes through any of three ties, mostly by losing one, and here only the voter's tie to the candidate is re-observed, so this neither confirms nor contradicts D&K.")
    add("")

    # ------------------------------------------------------------ sensitivities
    add("## 7. Sensitivities (secondary; none replaces the headline)")
    add("")
    add("Pooled repair share, event-level share, flip-rate excess in one-negative triples over weakly balanced ones, and the interaction contrast, each as observed / null mean (excess, z), under two event-permutation nulls: **A** same new candidacy and old sign, **B** same voter and old sign.")
    add("")
    rows = []
    for vname, d in [("main analysis", None)] + list(V.items()):
        cells = [vname, f"{C['n_inst']:,}" if d is None else f"{d['n_inst']:,}"]
        for nn in PRIMARY_EVENT_NULLS:
            for k in ("share_w", "event_share", "r1_minus_rbal", "I"):
                c = M[nn][k] if d is None else d["nulls"][nn][k]
                if k == "I":
                    cells.append(f"{c['obs']:.3f} / {c['mean']:.3f} ({c['obs'] - c['mean']:+.3f}, {zs(c)})")
                else:
                    cells.append(f"{c['obs']:.3f} / {c['mean']:.3f} ({(c['obs'] - c['mean']) * 100:+.1f}, {zs(c)})")
        rows.append(cells)
    L += table(["cut", "instances", "A share", "A event", "A r1-bal", "A I", "B share", "B event", "B r1-bal", "B I"], rows, "lrrrrrrrrr")
    add("")
    add("Cut-off at the vote's own time keeps the in-candidacy votes of others that came earlier (herding is possible there) and raises the observed share; excluding w -> v ties from the old candidacy (co-voters of the old vote) leaves the excess; contexts at most two years old leave it; "
        "FF shows an excess under A that vanishes under B and has no interaction; FB carries the interaction; BB is empty. The era split shows it in both halves, thinly before 2007. Dropping every undated vote changes nothing.")
    add("")

    # ------------------------------------------------------------ bitcoin
    add("## 8. Bitcoin OTC and Alpha: formation, not conversion [L4567-L4580]")
    add("")
    if bt:
        o, a = bt["otc"], bt["alpha"]
        NN = ("null_global", "null_rater", "null_ratee")
        NT = {"null_global": "global", "null_rater": "rater", "null_ratee": "ratee"}
        shr = lambda r, nn, sub: r[nn][sub]["balanced"] / r[nn][sub]["n"]  # noqa: E731
        clo = lambda r, nn, sub, t: r[nn][sub]["close_pos_" + t] / r[nn][sub]["first_" + t]  # noqa: E731
        cmp_bal = lambda r, nn, sub: wr.compare(r[sub]["balanced"] / r[sub]["n"], shr(r, nn, sub))  # noqa: E731
        cmp_neg = lambda r, nn, sub, k: wr.compare(float(r[sub]["neg_counts"][k]), r[nn][sub]["neg_counts"][:, k].astype(float))  # noqa: E731
        # guards: the sentences below say these
        lim = 2.0 / (B + 1)
        assert all(cmp_bal(o, nn, "all")["p_ge"] <= lim for nn in NN) and all(cmp_bal(a, nn, sub)["p_ge"] <= lim for nn in NN[:2] for sub in ("all", "ordered"))
        assert cmp_bal(a, "null_ratee", "ordered")["p_ge"] > 0.05 and 0.001 < cmp_bal(a, "null_ratee", "all")["p_ge"] < 0.01
        assert all(cmp_neg(o, nn, "all", 1)["p_le"] <= lim for nn in NN) and all(cmp_neg(a, nn, "all", 1)["p_le"] <= lim for nn in NN[:2])
        assert 0.001 < cmp_neg(a, "null_ratee", "all", 1)["p_le"] < 0.02 and cmp_neg(a, "null_ratee", "ordered", 1)["p_le"] > 0.05
        assert cmp_neg(o, "null_global", "all", 3)["p_ge"] <= lim and all(cmp_neg(o, nn, "all", 3)["p_le"] <= lim for nn in NN[1:])
        add(f"No ordered pair is rated twice in either file ({o['repeat_ordered_pairs']} and {a['repeat_ordered_pairs']} repeats): a tie is signed once, so only the closing of a triangle by a new tie can be looked at [L4571, L4580]. "
            f"Undirected projection, each pair signed and timed by its earliest rating (the rule that reproduces 117's counts): OTC {o['pairs']:,} pairs ({o['both_signs']} rated with opposite signs in the two directions) and {o['triangles']:,} triangles; "
            f"Alpha {a['pairs']:,} pairs ({a['both_signs']}) and {a['triangles']:,} triangles, of which {a['triangles'] - a['tied']:,} have strictly ordered edge times ({a['tied']:,} have a tie in the times, broken by pair number) [L4572]. "
            "The third edge's sign equals the product of the first two exactly when the triangle has an even number of negative ties, so the \"closing-edge balance\" is the share of strictly balanced triangles.")
        add("")
        add("Three sign-shuffled nulls, each re-signing the pairs from the shuffled ratings: **global** (all pair signs permuted: 117's null, here 10,000 draws instead of 20), **rater** (each rater's ratings shuffled among his own: a negative-prone rater stays negative-prone) "
            "and **ratee** (shuffled among those received by the same trader: a widely distrusted trader stays distrusted, which is reputation or status in the sense of Leskovec et al.).")
        add("")
        rows = []
        for key, nm, sub in (("otc", "OTC", "all"), ("alpha", "Alpha, strictly ordered", "ordered"), ("alpha", "Alpha, all triangles", "all")):
            r = bt[key]
            st = r[sub]
            cells = [nm, f"{st['n']:,}", f"{st['balanced']:,} ({pc(st['balanced'] / st['n'])})"]
            for nn in NN:
                sh = shr(r, nn, sub)
                c = cmp_bal(r, nn, sub)
                cells.append(f"{pc(sh.mean())} [{pc(np.percentile(sh, 2.5))}, {pc(np.percentile(sh, 97.5))}], p {fp(c['p_ge'], B)}")
            rows.append(cells)
        L += table(["", "triangles", "balanced (third edge = product of the first two)", "global null [95%], p", "rater null", "ratee null"], rows)
        add("")
        add(f"**117's OTC figure reproduces exactly**: 29,900 of 33,493 (89.3%) against 69.3% (117: 67.9-70.7 over 20 shuffles; here {pc(np.percentile(shr(o, 'null_global', 'all'), 2.5))}-{pc(np.percentile(shr(o, 'null_global', 'all'), 97.5))} at 95%). Alpha, which 117 gives for the strictly ordered triangles only "
            f"(17,567 of 20,016, 87.8%, null 78.8%), reproduces too, and with all 22,153 triangles is {pc(a['all']['balanced'] / a['all']['n'])} against {pc(shr(a, 'null_global', 'all').mean())}. "
            f"**The excess does not survive every baseline.** Keeping each rater's negativity trims OTC's null to {pc(shr(o, 'null_rater', 'all').mean())}; keeping each ratee's reputation lifts it to {pc(shr(o, 'null_ratee', 'all').mean())} (the data stay above every draw), and in Alpha the ratee null reaches the strictly ordered data "
            f"({pc(shr(a, 'null_ratee', 'ordered').mean())} against {pc(a['ordered']['balanced'] / a['ordered']['n'])}, p {fp(cmp_bal(a, 'null_ratee', 'ordered')['p_ge'], B)}; with the {a['tied']:,} tied-time triangles added the data are {pp(a['all']['balanced'] / a['all']['n'] - shr(a, 'null_ratee', 'all').mean())} points above it, p {fp(cmp_bal(a, 'null_ratee', 'all')['p_ge'], B)}): "
            "in Alpha the balance of the triangles adds almost nothing to who is widely distrusted.")
        add("")
        add("Triangles by number of negative ties, the weak-balance reading (a one-negative triangle is the forbidden one; an all-negative one is balanced only weakly): observed, then each null's mean and the tail p in the direction of the departure.")
        add("")
        rows = []
        for key, nm in (("otc", "OTC"), ("alpha", "Alpha (all)")):
            r = bt[key]
            for k, lab in ((1, "one-negative"), (3, "all-negative")):
                cells = [nm, lab, f"{r['all']['neg_counts'][k]:,}"]
                for nn in NN:
                    c = cmp_neg(r, nn, "all", k)
                    below = c["obs"] < c["mean"]
                    cells.append(f"{c['mean']:,.0f} ({'below' if below else 'above'}, p {fp(c['p_le'] if below else c['p_ge'], B)})")
                rows.append(cells)
        L += table(["", "class", "observed", "global null", "rater null", "ratee null"], rows)
        add("")
        add("The one-negative triangle is depleted against every baseline in OTC and against the global and rater baselines in Alpha; against the ratee baseline Alpha's depletion is mild with all triangles "
            f"(p {fp(cmp_neg(a, 'null_ratee', 'all', 1)['p_le'], B)}) and absent among the strictly ordered ones (p {fp(cmp_neg(a, 'null_ratee', 'ordered', 1)['p_le'], B)}). "
            "**The all-negative triangle is commoner than the global null (OTC 239 against 84; Alpha 96 against 13) but rarer than the rater and ratee nulls in OTC (against about 1,000).** "
            "117's reading, that strict balance fails because the all-negative triangle is commoner than null, holds only against the global shuffle; once raters' negativity or targets' reputation is kept, OTC is depleted in both the one- and the all-negative triangle, "
            "which is what strict balance predicts. The formation figures support the weak form under the global baseline and the strict form under the others, so they do not settle strict against weak.")
        add("")
        add("Closing sign by the first two edges (the two earliest edges by time; the share of closings that are positive):")
        add("")
        rows = []
        for key, nm, sub in (("otc", "OTC", "all"), ("alpha", "Alpha (all)", "all"), ("alpha", "Alpha (ordered)", "ordered")):
            r = bt[key]
            st = r[sub]
            for t, lab in (("pp", "(+,+)"), ("pm", "(+,-)"), ("mm", "(-,-)")):
                cells = [nm, lab, f"{st['first_' + t]:,}", pc(st["close_pos_" + t] / st["first_" + t])]
                for nn in NN:
                    cells.append(pc(clo(r, nn, sub, t).mean()))
                rows.append(cells)
        L += table(["", "first two", "triangles", "closes positive", "global null", "rater null", "ratee null"], rows, "llrrrrr")
        add("")
        ot = o["all"]
        add(f"A mixed start (+,-) closes *negative* {pc(1 - ot['close_pos_pm'] / ot['first_pm'], 0)} of the time in OTC against {pc(1 - clo(o, 'null_global', 'all', 'pm').mean(), 0)} under the global null, {pc(1 - clo(o, 'null_rater', 'all', 'pm').mean(), 0)} within rater and {pc(1 - clo(o, 'null_ratee', 'all', 'pm').mean(), 0)} within ratee: the friend-of-my-enemy half of balance, robust. "
            f"A (-,-) start closes positive {pc(ot['close_pos_mm'] / ot['first_mm'])} against {pc(clo(o, 'null_global', 'all', 'mm').mean())} globally (enemy of my enemy fails), {pc(clo(o, 'null_rater', 'all', 'mm').mean())} within rater and {pc(clo(o, 'null_ratee', 'all', 'mm').mean())} within ratee (it works): "
            "the verdict on that half depends on the baseline, as the all-negative count does. A (+,+) start closes positive at the global null rate in Alpha and below the ratee null in both files. "
            "Formation follows balance more strongly than conversion does (a new tie has to take some sign; a re-vote already has one), and none of this is a conversion result.")
    add("")

    # ------------------------------------------------------------ caveats
    add("## 9. What this cannot say, and what was decided when")
    add("")
    add("- **Votes are not friendships.** The ties in a triple are public evaluations of candidacies by voters: u -> w is u's vote at w's adminship election, w -> v is w's vote at an earlier candidacy of v. Agreement on a third party is agreement of judgement about a wiki role; "
        "it is balance in form and similarity-as-attraction or faction in content, and the FB-carried interaction cannot tell them apart.")
    add("- **A vote is a one-shot evaluation of a candidacy.** Oppose-to-support conversions are 79% of the total and 70% of those are a failed candidacy followed by a passed one: the candidate changed, or the voter judged the same record differently the second time. "
        "The nulls hold the new candidacy fixed but cannot hold *why* a given voter changed.")
    add("- **Timing granularity.** The unit of \"before\" is the candidacy (about a week; times are minutes, but 9,367 votes have none and are placed at their candidacy's median). Contexts are votes dated before the new candidacy began. "
        f"Votes inside a candidacy are visible to later voters (the cut-off-at-the-vote cut raises the observed repair share by {pp(V['context cut-off at the vote, not the candidacy start']['obs']['share_w'] - O['d_share_w'])} points, consistent with herding), so the primary cut excludes them.")
    add(f"- **Selection into re-voting.** {C['n_trans']:,} re-votes by {C['n_voters_revote']:,} voters (of 11,380 users) among {C['n_pairs_total']:,} voter-candidate pairs; almost all follow a failed candidacy; {C['n_voters_conv']} voters and {C['n_cands_conv']} candidates supply the conversions, and a voter can supply 25. "
        "A candidacy cannot be re-voted unless the candidate failed, so the ties that can convert are the ties of a particular kind of candidate; the voter-matched nulls use only voters who re-vote at least twice with the same old sign.")
    add("- **One tie only.** A one-negative triple can be resolved through any of its three ties; here only the voter's tie to the candidate is re-observed, so tension resolved by changing u's tie to w or w's to v is invisible. The conversion rates are lower bounds on resolution.")
    add("- **Overlap and multiplicity.** Triples share ties, the same third party recurs across re-votes, and a voter appears many times: the permutation nulls respect that structure within their strata, the pooled counts do not. "
        f"{len(MAIN_NULLS)} nulls, several statistics and {len(V)} cuts are shown without correction; read p of about 0.001-0.05 as suggestive. **Fixed before any null was computed:** the candidacy rule, the context cut-off, weak balance as the primary reading, the pooled repair share under the brief's null as the headline test, 10,000 draws. "
        "**Post hoc:** the conditional context shuffles (added on seeing the 79% direction mix), the event-permutation family (added when the context shuffles disagreed), the interaction contrast and orientation split (added on seeing that the FF cell rates carry no product structure), and the voter-generosity and number-of-triples terciles. "
        "The first-tie contrasts were defined after the cell rates were seen and before any null was run on them. Nothing was dropped for disagreeing.")
    add("- **Not tested.** The v0 §7 criterion as written (\"conversion at the null rate\") has no unique null; the nulls here are three different ones, and the answer depends on which is taken, which is the finding. The directed first-tie asymmetry in *formation* (Bitcoin ratings are directed and timed) is untested; the counts above are undirected.")
    add("")
    add("## Reproduce")
    add("")
    add("    cd sim")
    add("    ~/.local/bin/uv run python -m models.wikirfa_report fetch    # once; checks sha256, writes to git-ignored data/wiki-rfa/ and data/bitcoin/")
    add("    ~/.local/bin/uv run python -m models.wikirfa_report report   # about 5 minutes on 8 cores; rewrites this file")
    add("    ~/.local/bin/uv run pytest tests/test_wikirfa_conversion.py")
    add("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="download the wiki-RfA and Bitcoin files for local use (git-ignored); verifies sha256")
    sub.add_parser("check", help="verify the local files' checksums and parse them")
    rp = sub.add_parser("report", help="run everything and write results/wikirfa_conversion.md")
    rp.add_argument("--draws", type=int, default=wr.N_DRAWS)
    rp.add_argument("--seed", type=int, default=wr.SEED)
    rp.add_argument("--out", type=Path, default=RESULTS)
    rp.add_argument("--dump", type=Path, default=None, help="also dump the raw results as JSON (for inspection)")
    args = ap.parse_args(argv)
    if args.cmd == "fetch":
        for src in wr.SOURCES.values():
            print(f"wrote {wr.fetch(src)}")
    elif args.cmd == "check":
        raw = wr.load_wikirfa()
        print(f"ok: wiki-RfA {raw.notes['n_records']} records, sha256 {wr.sha256_of(wr.WIKIRFA.path)}")
        for src in (wr.OTC, wr.ALPHA):
            d = wr.load_bitcoin(src)
            print(f"ok: {src.key} {len(d['src'])} ratings, sha256 {wr.sha256_of(src.path)}")
    else:
        out = run(args.draws, args.seed)
        if args.dump:
            args.dump.write_text(json.dumps(out, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o)))
        text = build_report(out)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        text = _keep_review(text, args.out)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
