"""The crowd gate on wiki-RfA: tests of models/crowd_gate_wikirfa.py and of what the data say.

Prior work: models/00-v0.md section 4.4 (the crowd law r(t+1) = F[r(t)], the two-sided gate, the sign operand
sigma), section 6 Theorem 6.3, section 7 "Crowd"; models/02-our-claims.md Claim 1 (excess function);
docs/prior-work/112 section 6.5 (the sign-law registry's five tests); docs/prior-work/117 section 3.3.
Ledger ids (docs/ledger.jsonl): Granovetter's map and its first crossing L1831, monotone convergence L1201,
cascade operator L1235, non-identifiability L1225, thresholds as net costs and benefits L3959, Kuran's
utility and threshold function L3965 and L3967, thresholds falling with the share L4395, the Hong Kong march
(first stage L4353, reduced form L4354, two-stage L4355, scope: the sign may flip with turnout L4363), the two
upper-gate mechanisms L4347 and L4348, the wiki-RfA file and its counts L4561-L4564.  Results and verdict:
sim/results/crowd_gate_wikirfa.md, produced by `models.crowd_gate_wikirfa report` from the same functions.

Two groups.  (1) MACHINERY, no data needed: the parser and the election builder on toy files, the strict-prior
bookkeeping against a brute-force loop, the estimators against independent implementations, and the whole
pipeline on SYNTHETIC elections with a planted truth: complements, substitutes, forward influence, time-
symmetric clustering, a planted participation gate, each detected (or not) by the within-election shuffle
null, and the null itself calibrated on data with no order dependence.  A method that cannot find a planted
effect, or that finds one in noise, would make the data result meaningless.  (2) DATA tests, skipped with a
reason when the git-ignored file is absent (sim/data/README.md): the counts the survey (117) published, the
cleaning, and the findings the results file reports.  A finding that moved would fail loudly; none was tuned
to pass.  Seeds are fixed; Monte Carlo assertions have wide margins.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):    # one BLAS thread per forked worker
    os.environ.setdefault(_v, "1")

import dataclasses

import numpy as np
import pytest
from scipy.optimize import minimize

from models import crowd_gate_wikirfa as cg

needs_data = pytest.mark.skipif(
    not cg.DATA_FILE.exists(),
    reason=f"sim/data/wiki-rfa/wiki-RfA.txt.gz is absent (local-use-only, git-ignored): {cg.FETCH_HINT}",
)


# ------------------------------------------------------------------ synthetic elections with a planted truth

def _sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def synth_votes(rng, n_el=60, n_per=60, kind="none", strength=0.0, n_pool=400, year=2008):
    """Elections of n_per signed votes at increasing minutes.  Each election has a candidate effect (its
    support composition) and each voter a propensity.  `kind` plants one order dependence on top:
      'none'       the sign ignores the votes before it
      'cumulative' logit += strength * (running share before - 0.5)           (+: complements, -: substitutes)
      'forward'    logit += strength * (mean of the previous 5 signs - 0.5)   (earlier votes -> later votes)
      'cluster'    logit += strength * z_k, z an AR(1) process shared by neighbours in time (no direction)
    Returns a cg.Votes (voters and candidates share one numbering, candidates first)."""
    theta = rng.normal(0, 0.8, n_pool)
    voter, cand, vote, res, yr, minute = [], [], [], [], [], []
    for e in range(n_el):
        base = rng.normal(1.0, 1.0)
        z = 0.0
        t = float(rng.integers(0, 10**6))
        signs = []
        vs = rng.choice(n_pool, n_per, replace=False)
        for k in range(n_per):
            t += rng.exponential(120.0)
            lg = base + theta[vs[k]]
            if kind == "cumulative" and k >= 1:
                lg += strength * (np.mean(signs) - 0.5)
            elif kind == "forward" and k >= 1:
                lg += strength * (np.mean(signs[-5:]) - 0.5)
            elif kind == "cluster":
                z = 0.85 * z + np.sqrt(1 - 0.85 ** 2) * rng.normal()
                lg += strength * z
            y = int(rng.random() < _sigmoid(lg))
            signs.append(y)
            voter.append(n_el + vs[k])
            cand.append(e)
            vote.append(1 if y else -1)
            minute.append(np.floor(t))
        res.extend([1 if np.mean(signs) > 0.75 else -1] * n_per)
        yr.extend([year] * n_per)
    return cg.Votes(np.array(voter, np.int32), np.array(cand, np.int32), np.array(vote, np.int8),
                    np.array(res, np.int8), np.array(yr, np.int16), np.array(minute, np.float64), n_el + n_pool)


def synth_sign_data(seed, **kw):
    v = synth_votes(np.random.default_rng(seed), **kw)
    E = cg.build_elections(v)
    return v, E, cg.build_sign_data(v, E)


def _null_of(SD, stat_keys, B=80, seed=1, windows=(), extras=False):
    cells = {"all": np.ones(SD.n_elections, bool)}
    obs = cg.sign_stats(SD, None, cells, windows=windows, extras=extras)
    keys, null = cg.sign_null(SD, cells, B=B, seed=seed, n_jobs=1, windows=windows, extras=extras)
    return {k: cg.compare_to_null(obs[k], null[:, keys.index(k)]) for k in stat_keys}


# ------------------------------------------------------------------ (1) machinery: parsing and elections

def test_parse_minute_handles_the_variants_in_the_file():
    """The DAT field of wiki-RfA [L4561]: abbreviated months occur ('Jun', 'Sept'), three slips ('Julu',
    'Janry', 'Mya'), 9,367 empty fields and one impossible hour; minutes since 2000-01-01."""
    base = cg.parse_minute("00:00, 1 January 2000")
    assert base == 0.0
    assert cg.parse_minute("01:30, 2 January 2000") == 1440 + 90
    assert cg.parse_minute("12:00, 5 Jun 2007") == cg.parse_minute("12:00, 5 June 2007")
    assert cg.parse_minute("12:00, 5 Sept 2007") == cg.parse_minute("12:00, 5 September 2007")
    assert cg.parse_minute("12:00, 5 Mya 2007") == cg.parse_minute("12:00, 5 May 2007")
    assert cg.parse_minute("12:00, 5 Julu 2007") == cg.parse_minute("12:00, 5 July 2007")
    assert np.isnan(cg.parse_minute(""))
    assert np.isnan(cg.parse_minute("31:29, 24 May 2008"))           # the one impossible hour
    assert np.isnan(cg.parse_minute("12:00, 31 February 2008"))
    assert np.isnan(cg.parse_minute("not a date"))


def test_parse_lines_skips_text_numbers_names_and_flags_empty_voters():
    text = (
        "SRC:Alice\nTGT:Bob\nVOT:1\nRES:1\nYEA:2008\nDAT:10:00, 3 May 2008\nTXT:'''Support''' per: nom\n\n"
        "SRC:Bob\nTGT:Bob\nVOT:-1\nRES:1\nYEA:2008\nDAT:10:05, 3 May 2008\nTXT:self\n\n"
        "SRC:\nTGT:Bob\nVOT:0\nRES:1\nYEA:2008\nDAT:\nTXT:\n\n"
    ).splitlines(keepends=True)
    v = cg.parse_lines(text)
    assert v.n == 3 and v.vote.tolist() == [1, -1, 0] and v.res.tolist() == [1, 1, 1]
    assert v.voter[2] == -1                                           # empty voter field
    assert v.voter[1] == v.cand[1]                                    # one numbering: a self-vote is visible
    assert v.voter[0] != v.cand[0]
    assert np.isnan(v.minute[2]) and not np.isnan(v.minute[0])


def _toy(rows):
    """rows: (voter, cand, vote, res, year, minute) with integer names."""
    a = np.array(rows, dtype=float)
    return cg.Votes(a[:, 0].astype(np.int32), a[:, 1].astype(np.int32), a[:, 2].astype(np.int8),
                    a[:, 3].astype(np.int8), a[:, 4].astype(np.int16), a[:, 5], int(max(a[:, 0].max(), a[:, 1].max()) + 1))


def test_build_elections_splits_candidacies_drops_strays_dupes_and_selfvotes():
    day = 1440.0
    rows = []
    # candidate 0: two candidacies in one (result, year), 60 days apart; 12 votes each
    for i in range(12):
        rows.append((10 + i, 0, 1, -1, 2008, 1000 + i * 60))
    for i in range(12):
        rows.append((30 + i, 0, -1, -1, 2008, 1000 + 60 * day + i * 60))
    rows.append((50, 0, 1, -1, 2008, 1000 + 30 * day))                # a lone stray vote between them
    rows.append((10, 0, -1, -1, 2008, 1000 + 20 * 60))                # voter 10 votes again in candidacy 1: last wins
    rows.append((0, 0, 1, -1, 2008, 1000 + 30))                       # self-vote
    rows.append((60, 0, 1, -1, 2008, np.nan))                         # undated
    rows.append((-1, 0, 1, -1, 2008, 1000 + 40))                      # empty voter
    v = _toy(rows)
    E = cg.build_elections(v, gap_days=10.0)
    assert E.n_elections == 2
    assert E.dropped == {"undated": 1, "empty_voter": 1, "self_vote": 1, "stray": 1, "duplicate": 1}
    assert E.size.tolist() == [12, 12]                                # 12 each: the repeat vote replaced, not added
    first = E.cl == 0
    assert int(E.vote[first & (E.voter == 10)][0]) == -1              # voter 10's LAST vote stands
    assert np.all(np.diff(E.minute[first]) >= 0)
    assert E.hours()[E.start[0]] == 0.0


def test_propensity_leaves_out_the_vote_the_history_counted():
    """The voter's propensity at an election leaves out the vote the history counted for that (voter, candidate,
    result, year) group.  Voter 10 changes his vote at candidate 0 and the file lists the later support FIRST and the
    earlier oppose second, so the election keeps the support (last in time) while the history counts the oppose (last
    in file order); his only other vote is a support at candidate 1.  Leaving the group out gives (1 + kappa*pi)/(1 +
    kappa); the first version subtracted the kept vote's own sign, giving (0 + kappa*pi)/(1 + kappa) -- a support taken
    out that was never counted, which is what 182 votes of the real file had (review of 2026-11-01)."""
    rows = [(10, 0, 1, -1, 2008, 2000.0), (10, 0, -1, -1, 2008, 1000.0)]
    rows += [(20 + i, 0, 1 if i % 2 else -1, -1, 2008, 1100.0 + i) for i in range(6)]
    rows += [(10, 1, 1, 1, 2008, 9000.0)] + [(40 + i, 1, 1, 1, 2008, 9100.0 + i) for i in range(6)]
    v = _toy(rows)
    E = cg.build_elections(v)
    SD = cg.build_sign_data(v, E, n_min=2)
    nv, ns = cg.voter_history(v)
    pi = ns.sum() / nv.sum()
    cand_of_vote = E.cand[SD.ekey][SD.cl]
    j = np.nonzero((SD.voter == 10) & (cand_of_vote == 0))[0]
    assert len(j) == 1 and SD.y[j[0]] == 1.0                          # the election keeps the later support
    assert SD.p[j[0]] == pytest.approx((1 + cg.KAPPA * pi) / (1 + cg.KAPPA))
    # and in general the other-vote counts behind p are never negative and never exceed the other votes
    other_n = nv[SD.voter] - 1.0
    other_s = SD.p * (other_n + cg.KAPPA) - cg.KAPPA * pi
    assert np.all(other_s > -1e-9) and np.all(other_s <= other_n + 1e-9)


# ------------------------------------------------------------------ (1) machinery: bookkeeping and estimators

def _brute_prior_post(SD):
    n = SD.n
    out = np.zeros((n, 4))
    for j in range(n):
        lo, hi = SD.c0[j], SD.c0[j] + SD.esz[j]
        before = [i for i in range(lo, hi) if SD.minute[i] < SD.minute[j]]
        after = [i for i in range(lo, hi) if SD.minute[i] > SD.minute[j]]
        out[j] = (len(before), SD.y[before].sum() if before else 0, len(after), SD.y[after].sum() if after else 0)
    return out


def test_strict_prior_and_post_counts_match_a_loop_even_with_tied_minutes():
    """Votes in the same minute do not see each other: 'before' is strictly earlier, 'after' strictly later."""
    rng = np.random.default_rng(3)
    v = synth_votes(rng, n_el=5, n_per=40)
    # force many ties: coarsen the clock to 6-hour blocks inside each election
    v = dataclasses.replace(v, minute=np.floor(v.minute / 360.0) * 360.0)
    E = cg.build_elections(v)
    SD = cg.build_sign_data(v, E, n_min=20)
    A = cg.arrange(SD)
    brute = _brute_prior_post(SD)
    assert np.array_equal(A.n_prior, brute[:, 0]) and np.allclose(A.S_prior, brute[:, 1])
    assert np.array_equal(A.n_post, brute[:, 2]) and np.allclose(A.S_post, brute[:, 3])
    assert (SD.tie_end - SD.tie_first).max() > 1                      # ties really occur here


def test_leave_one_out_share_and_window_features():
    v, E, SD = synth_sign_data(5, n_el=6, n_per=45)
    A = cg.arrange(SD)
    for e in range(SD.n_elections):
        sl = slice(SD.estart[e], SD.estart[e] + SD.esize[e])
        K = SD.y[sl].sum()
        assert np.allclose(A.f_loo[sl], (K - SD.y[sl]) / (SD.esize[e] - 1))
    L = 5
    wp, wq = cg._window_pair(SD, A, L)
    for j in (0, 7, 30, 44, 100, 200):
        lo, hi = SD.c0[j], SD.c0[j] + SD.esz[j]
        before = [i for i in range(lo, hi) if SD.minute[i] < SD.minute[j]][-L:]
        after = [i for i in range(lo, hi) if SD.minute[i] > SD.minute[j]][:L]
        assert np.isclose(wp[j], SD.y[before].mean() if before else 0.0)
        assert np.isclose(wq[j], SD.y[after].mean() if after else 0.0)


def test_within_shuffle_keeps_composition_and_slots_and_is_seeded():
    v, E, SD = synth_sign_data(2, n_el=8, n_per=50)
    src = cg.within_shuffle(np.random.default_rng(0), SD)
    assert np.array_equal(np.sort(src), np.arange(SD.n))
    assert np.array_equal(SD.cl[src], SD.cl)                          # a vote stays in its own election
    assert np.array_equal(cg.within_shuffle(np.random.default_rng(0), SD), src)
    A0, A1 = cg.arrange(SD), cg.arrange(SD, src)
    assert np.allclose(np.bincount(SD.cl, weights=A0.y), np.bincount(SD.cl, weights=A1.y))
    assert np.array_equal(A0.n_prior, A1.n_prior)                     # slot-attached counts do not move
    assert not np.allclose(A0.S_prior, A1.S_prior)                    # the share path does
    # voter-attached data travel with the vote
    assert np.array_equal(A1.voter, SD.voter[src]) and np.allclose(A1.p, SD.p[src])


def test_logit_irls_matches_a_generic_optimiser_and_the_sandwich_se():
    rng = np.random.default_rng(1)
    n, k = 4000, 4
    X = np.column_stack([np.ones(n), rng.normal(size=(n, k - 1))])
    g = rng.integers(0, 80, n)
    eff = rng.normal(0, 0.5, 80)[g]
    y = (rng.random(n) < _sigmoid(X @ np.array([-0.3, 0.8, -0.5, 0.2]) + eff)).astype(float)
    f = cg.logit_irls(X, y, groups=g)
    nll = lambda b: -np.sum(y * (X @ b) - np.log1p(np.exp(X @ b)))
    ref = minimize(nll, np.zeros(k), method="BFGS", options={"gtol": 1e-9}).x
    assert np.allclose(f.beta, ref, atol=1e-5)
    mu = _sigmoid(X @ f.beta)
    bread = np.linalg.inv((X.T * (mu * (1 - mu))) @ X)
    meat = sum(np.outer(X[g == c].T @ (y - mu)[g == c], X[g == c].T @ (y - mu)[g == c]) for c in np.unique(g))
    ng = len(np.unique(g))
    se = np.sqrt(np.diag(bread @ meat @ bread) * ng / (ng - 1))
    assert np.allclose(f.se, se, rtol=1e-4)


def test_logit_weights_reproduce_replication():
    rng = np.random.default_rng(4)
    X = np.column_stack([np.ones(300), rng.normal(size=(300, 2))])
    y = (rng.random(300) < 0.4).astype(float)
    w = rng.integers(1, 4, 300).astype(float)
    a = cg.logit_irls(X, y, weights=w, robust=False).beta
    rep = np.repeat(np.arange(300), w.astype(int))
    b = cg.logit_irls(X[rep], y[rep], robust=False).beta
    assert np.allclose(a, b, atol=1e-6)


def test_lpm_fe_equals_the_dummy_variable_regression_and_detrend_equals_polyfit():
    rng = np.random.default_rng(6)
    G, per = 12, 30
    g = np.repeat(np.arange(G), per)
    X = rng.normal(size=(G * per, 2)) + rng.normal(size=G)[g][:, None]
    y = 0.4 * X[:, 0] - 0.2 * X[:, 1] + rng.normal(size=G)[g] + rng.normal(size=G * per)
    f = cg.lpm_fe(X, y, g)
    D = np.column_stack([X, (g[:, None] == np.arange(G)[None, :]).astype(float)])
    ref = np.linalg.lstsq(D, y, rcond=None)[0][:2]
    assert np.allclose(f.beta, ref, atol=1e-8)
    pos = np.tile(np.linspace(0, 1, per), G)
    r = cg._detrend(y, g, pos, G, deg=2)
    for c in range(G):
        m = g == c
        co = np.polyfit(pos[m], y[m], 2)
        assert np.allclose(r[m], y[m] - np.polyval(co, pos[m]), atol=1e-7)


def test_compare_to_null_arithmetic():
    null = np.arange(100.0)
    c = cg.compare_to_null(150.0, null)
    assert c["p_up"] == pytest.approx(1 / 101) and c["p_down"] == 1.0 and c["B"] == 100
    assert c["null_mean"] == pytest.approx(49.5) and c["z"] > 3
    d = cg.compare_to_null(49.5, null)
    assert d["p_two"] == 1.0
    assert cg.compare_to_null(1.0, np.array([np.nan, 0.0, 2.0]))["B"] == 2


def test_regenerating_the_report_keeps_a_review_section():
    new = "# Title\n\n## Verdict\n\nnew numbers\n"
    old = "# Title\n\n## Verdict\n\nold numbers\n\n## Review (2026-11-01)\n\nwhat changed\n\n## Review (2026-12-01)\n\nmore\n"
    out = cg.keep_reviews(new, old)
    assert out.startswith(new.rstrip("\n")) and "old numbers" not in out
    assert out.endswith("## Review (2026-11-01)\n\nwhat changed\n\n## Review (2026-12-01)\n\nmore\n")
    assert cg.keep_reviews(new, None) == new and cg.keep_reviews(new, "# Title\n\nno review\n") == new


def test_wilson_interval_known_values():
    p, lo, hi = cg.wilson(0, 10)
    assert p == 0 and lo == pytest.approx(0.0, abs=1e-12) and hi == pytest.approx(0.2775, abs=2e-3)
    p, lo, hi = cg.wilson(50, 100)
    assert (lo, hi) == pytest.approx((0.4038, 0.5962), abs=2e-3)


# ------------------------------------------------------------------ (1) the pipeline on planted truths

def test_null_is_calibrated_when_signs_ignore_order():
    """No order dependence: the shuffle p-values of the running-share coefficient must not reject more often
    than chance (here: at the 10% level in at most 5 of 20 datasets; chance would give 2 and the binomial tail
    of 6 or more is 1%)."""
    rej = {"all:logit_s": 0, "all:fe_s": 0}
    for seed in range(20):
        _, _, SD = synth_sign_data(100 + seed, n_el=40, n_per=50, kind="none")
        for k, c in _null_of(SD, list(rej), B=60, seed=seed).items():
            rej[k] += c["p_two"] <= 0.10
    assert max(rej.values()) <= 5


def test_planted_complements_are_detected_as_complements():
    """The election-fixed-effect statistic finds a planted pull toward the running share (z > 4) and the primary
    logit points the same way.  The logit is the less powerful of the two for complements, by construction:
    herding makes the election's final composition an OUTCOME of the early votes, and the logit conditions on
    it (the results file says so); it is the more cautious test of complements and loses nothing against
    substitutes (next test)."""
    _, _, SD = synth_sign_data(11, n_el=200, n_per=60, kind="cumulative", strength=4.0)
    c = _null_of(SD, ["all:fe_s", "all:logit_s"], B=100)
    assert c["all:fe_s"]["p_up"] <= 0.02 and c["all:fe_s"]["z"] > 4
    assert c["all:logit_s"]["obs"] > 0.3 and c["all:logit_s"]["z"] > 2


def test_planted_substitutes_are_detected_as_substitutes():
    _, _, SD = synth_sign_data(12, n_el=200, n_per=60, kind="cumulative", strength=-4.0)
    c = _null_of(SD, ["all:logit_s", "all:fe_s"], B=100)
    for k in ("all:logit_s", "all:fe_s"):
        assert c[k]["p_down"] <= 0.02 and c[k]["z"] < -3


def test_agreement_with_the_running_majority_is_a_weak_statistic():
    """Recorded, because the literal reading of the task ('does a later vote follow the running majority?') is
    this statistic.  Under a planted pull toward the running share it does NOT rise above the shuffle null
    (the early majority can lock in the wrong side of the final composition, which the shuffle puts first), and
    under a planted push away from it it does not fall.  It is reported as a description, never as a test."""
    _, _, pos = synth_sign_data(11, n_el=200, n_per=60, kind="cumulative", strength=4.0)
    c = _null_of(pos, ["all:agree"], B=60)["all:agree"]
    assert c["z"] < 1.0


def test_window_forms_beat_cumulative_share_once_the_null_gain_is_subtracted():
    """Out-of-sample comparison of forms (election-level folds).  With forward influence from the last five
    votes the 5-vote window must out-predict the cumulative share by more than the same comparison gives on
    shuffled data, where any gain is mechanical."""
    forms = {k: cg.SIGN_FORMS[k] for k in ("controls only (no running state)",
                                           "cumulative share, linear (Kuran: threshold falls with the share)",
                                           "share of the last 5 votes")}
    v = synth_votes(np.random.default_rng(31), n_el=120, n_per=70, kind="forward", strength=5.0)
    SD = cg.build_sign_data(v, cg.build_elections(v), n_min=20)
    obs = {r["form"]: r["cv_gain_per_1000"] for r in cg.compare_sign_forms(SD, forms=forms)}
    shuffled = [cg.compare_sign_forms(SD, forms=forms, src=cg.within_shuffle(np.random.default_rng(s), SD)) for s in range(3)]
    null5 = np.mean([[r["cv_gain_per_1000"] for r in sh if r["form"] == "share of the last 5 votes"][0] for sh in shuffled])
    assert obs["share of the last 5 votes"] - null5 > 5.0
    assert obs["share of the last 5 votes"] > obs["cumulative share, linear (Kuran: threshold falls with the share)"]
    assert abs(null5) < 1.0


def synth_gap_votes(rng, kind, strength, n_el=150, n_per=60, mean_gap=6.0, year=2008):
    """Votes minutes apart, so that same-minute pairs are common.
      'visible' each vote leans toward the (up to five) most recent votes saved in a STRICTLY earlier minute
                and within the last 30 minutes -- influence that needs the earlier vote to be on the page
      'shock'   a latent mood z(t), an Ornstein-Uhlenbeck process in continuous time (correlation time 20 min),
                shifts every vote cast near the same moment -- a common shock, which needs no reading"""
    voter, cand, vote, res, yr, minute = [], [], [], [], [], []
    vid = n_el
    for e in range(n_el):
        base = rng.normal(1.0, 1.0)
        t, z, last_t = float(rng.integers(0, 10**6)), 0.0, None
        times, signs = [], []
        for k in range(n_per):
            dt = rng.exponential(mean_gap)
            t += dt
            tm = np.floor(t)
            if kind == "shock":
                a = np.exp(-(0.0 if last_t is None else tm - last_t) / 20.0)
                z = a * z + np.sqrt(1 - a * a) * rng.normal()
                lg = base + strength * z
            else:
                vis = [signs[i] for i in range(len(signs)) if times[i] < tm and tm - times[i] <= 30.0][-5:]
                lg = base + (strength * (np.mean(vis) - 0.5) if vis else 0.0)
            y = int(rng.random() < _sigmoid(lg))
            times.append(tm)
            signs.append(y)
            last_t = tm
            voter.append(vid)
            vid += 1
            cand.append(e)
            vote.append(1 if y else -1)
            minute.append(tm)
        res.extend([1 if np.mean(signs) > 0.75 else -1] * n_per)
        yr.extend([year] * n_per)
    return cg.Votes(np.array(voter, np.int32), np.array(cand, np.int32), np.array(vote, np.int8), np.array(res, np.int8),
                    np.array(yr, np.int16), np.array(minute, np.float64), vid + 1)


def test_time_reversal_placebo_cannot_tell_influence_from_shared_shocks_so_it_is_not_used_as_a_test():
    """A LIMIT recorded as a test.  The obvious placebo -- the share of the next L votes should not matter if
    earlier votes cause later ones -- fails: a stationary chain with planted FORWARD influence gives the
    previous-5 and next-5 windows almost equal coefficients (a reversible process looks the same run
    backwards), exactly as a shared shock does.  So 'the dependence is as strong backward as forward' is
    reported as time-symmetry, never as evidence against influence."""
    _, _, fwd = synth_sign_data(21, n_el=300, n_per=60, kind="forward", strength=5.0)
    obs = cg.sign_stats(fwd, None, {"all": np.ones(fwd.n_elections, bool)}, windows=(5,), extras=False)
    prior, post = obs["placebo:L5:logit_prior"], obs["placebo:L5:logit_post"]
    assert prior > 2.0 and post > 2.0                                # both windows carry the dependence
    assert abs(prior - post) < 0.35 * prior                          # forward-only influence is not visible as asymmetry


def test_gap_profile_recovers_a_planted_time_scale_and_neither_planted_world_has_a_same_minute_deficit():
    """Two planted worlds with votes minutes apart: visible influence (a vote leans toward the recent votes saved
    in earlier minutes) and a continuous-time common shock.  In both, consecutive votes agree more than chance
    and the excess fades with the gap (here over the half hour the shock lasts), and -- the point of the
    second half -- votes saved in the SAME minute agree MORE than chance too, because they share a history or a
    shock.  So the real file's same-minute deficit (the results file) is produced by neither model; and the
    same-minute bin cannot be used to tell reading from a shared shock, which an earlier draft of this
    module assumed."""
    out = {}
    for kind, strength in (("visible", 4.0), ("shock", 1.5)):
        v = synth_gap_votes(np.random.default_rng(51), kind, strength)
        SD = cg.build_sign_data(v, cg.build_elections(v), n_min=20)
        assert cg.gap_counts(SD)["same_minute"] > 150
        out[kind] = cg.compute_gap(SD, B=60, seed=3, n_jobs=1)["cmp"]
        assert out[kind]["gap2-5"]["z"] > 4 and out[kind]["same_minute"]["z"] > 2
    shock = out["shock"]
    assert shock["gap2-5"]["obs"] - shock["gap2-5"]["null_mean"] > shock["gap21-60"]["obs"] - shock["gap21-60"]["null_mean"]


def test_same_minute_agreement_is_order_free():
    """Within a minute the file order is the page's section order, so the same-minute bin must not depend on the
    order of slots: permuting slots inside every tie run leaves it unchanged."""
    v = synth_gap_votes(np.random.default_rng(52), "visible", 2.0, n_el=20)
    SD = cg.build_sign_data(v, cg.build_elections(v), n_min=20)
    ref = cg.gap_profile(SD)["same_minute"]
    rng = np.random.default_rng(0)
    src = np.arange(SD.n)
    starts = np.nonzero(np.arange(SD.n) == SD.tie_first)[0]
    for a in starts:
        b = SD.tie_end[a]
        src[a:b] = rng.permutation(np.arange(a, b))
    assert cg.gap_profile(SD, src)["same_minute"] == pytest.approx(ref)


# ------------------------------------------------------------------ (1) machinery: participation

def synth_hazard_votes(rng, n_el=70, penalty=1.0, year=2008):
    """Hourly arrivals over a week, rate = profile * scale_e * (penalty if the running support share is below
    one half, once five votes are in); signs are independent of timing (composition q_e only)."""
    voter, cand, vote, res, yr, minute = [], [], [], [], [], []
    vid = 10_000
    for e in range(n_el):
        q = rng.beta(4, 2)
        scale = rng.lognormal(0.0, 0.5)
        S = O = 0
        t0 = float(rng.integers(0, 10**6))
        for h in range(0, 168):
            prof = 4.0 * np.exp(-h / 18.0) + 0.35
            share = S / (S + O) if S + O >= 5 else 0.75
            m = penalty if share < 0.5 else 1.0
            for _ in range(rng.poisson(prof * scale * m)):
                s = 1 if rng.random() < q else -1
                S += s == 1
                O += s == -1
                voter.append(vid)
                vid += 1
                cand.append(e)
                vote.append(s)
                minute.append(t0 + h * 60 + float(rng.integers(0, 60)))
                res.append(1 if q > 0.7 else -1)
                yr.append(year)
    return cg.Votes(np.array(voter, np.int32), np.array(cand, np.int32), np.array(vote, np.int8), np.array(res, np.int8),
                    np.array(yr, np.int16), np.array(minute, np.float64), vid + 1)


def _hazard_of(rng_seed, **kw):
    v = synth_hazard_votes(np.random.default_rng(rng_seed), **kw)
    E = cg.build_elections(v)
    return cg.build_hazard_data(E, n_min=20)


def test_poisson_irls_matches_a_generic_optimiser():
    rng = np.random.default_rng(8)
    n = 3000
    X = np.column_stack([np.ones(n), rng.normal(size=(n, 2))])
    off = np.log(rng.uniform(0.5, 3.0, n))
    y = rng.poisson(np.exp(X @ np.array([0.2, 0.5, -0.3]) + off)).astype(float)
    f = cg.poisson_irls(X, y, off, groups=rng.integers(0, 50, n))
    nll = lambda b: -np.sum(y * (X @ b + off) - np.exp(X @ b + off))
    ref = minimize(nll, np.zeros(3), method="BFGS", options={"gtol": 1e-9}).x
    assert np.allclose(f.beta, ref, atol=2e-4)                        # the 1e-6 ridge moves it slightly


def test_hazard_bins_account_for_every_vote_and_states_are_strictly_before():
    HD = _hazard_of(41, n_el=15)
    hrs = np.concatenate([[0.0], cg.BIN_EDGES])
    for e in range(HD.n_elections):
        h = HD.hours[HD.estart[e]:HD.estart[e] + HD.esize[e]]
        assert HD.n1[e] == np.sum(h < 1.0)
        for b in range(len(cg.BIN_EDGES) - 1):
            assert HD.count[e, b] == np.sum((h >= cg.BIN_EDGES[b]) & (h < cg.BIN_EDGES[b + 1]))
    st = cg.hazard_states(HD, HD.sign)
    e, b = 3, 9
    h = HD.hours[HD.estart[e]:HD.estart[e] + HD.esize[e]]
    sg = HD.sign[HD.estart[e]:HD.estart[e] + HD.esize[e]]
    before = h < cg.BIN_EDGES[b]
    assert st["n"][e, b] == before.sum() and st["S"][e, b] == np.sum(sg[before] == 1) and st["O"][e, b] == np.sum(sg[before] == -1)


def test_shuffle_signs_keeps_neutral_slots_timing_and_composition():
    HD = _hazard_of(42, n_el=12)
    sg = cg.shuffle_signs(np.random.default_rng(0), HD)
    assert np.array_equal(sg == 0, HD.sign == 0)
    for e in range(HD.n_elections):
        sl = slice(HD.estart[e], HD.estart[e] + HD.esize[e])
        assert sorted(sg[sl]) == sorted(HD.sign[sl])
    assert not np.array_equal(sg, HD.sign)


def test_planted_participation_gate_is_found_by_the_share_shuffle_and_noise_is_not():
    """Arrivals are throttled while the running support share is below one half.  The sign-shuffle null (timing
    untouched, share path randomised) must put the low-share band's coefficient far below its null; with no
    throttle it must sit inside it."""
    win = cg.HAZARD_WINDOWS["1-168 h"]
    gated = _hazard_of(43, penalty=0.35)
    free = _hazard_of(44, penalty=1.0)
    g = cg.hazard_null(gated, "turn+rate+bands", win, B=40, seed=5, keys=("band0",))["band0"]
    f = cg.hazard_null(free, "turn+rate+bands", win, B=40, seed=5, keys=("band0",))["band0"]
    assert g["p_down"] <= 0.03 and g["z"] < -3
    assert abs(f["z"]) < 3


def _orbit_stage_counts(F, n_rounds, n=1000, rounds_per_stage=(2, 6, 5, 1)):
    """Granovetter's orbit r(t+1) = F(r(t)) [L1831], rounds laid on the clock in the four stages; the votes of
    a round are the increment of the orbit."""
    r = [F(0.0)]
    for _ in range(n_rounds - 1):
        r.append(F(r[-1]))
    inc = np.diff([0.0] + r)
    cuts = np.cumsum(rounds_per_stage)
    return np.array([[n * inc[a:b].sum() for a, b in zip(np.concatenate([[0], cuts[:-1]]), cuts)]])


def test_shape_classes_mean_what_the_crowd_law_says_about_the_orbit():
    """Under a monotone F the cumulative curve is the orbit [Theorem 6.3, L1201, L1235].  F with slope below one
    (a stall: first crossing from above, L1831) gives increments that shrink: 'decelerating'.  F with slope
    above one below a plateau (ignition) gives growing increments until it saturates: the classifier must call
    the second 'mid-phase faster than day 1'."""
    decel = _orbit_stage_counts(lambda r: min(1.0, 0.10 + 0.6 * r), 14)
    ignite = _orbit_stage_counts(lambda r: min(0.9, 0.02 + 1.35 * r), 14)
    assert cg.shape_class(decel)[0] in (0, 1)
    assert cg.shape_class(ignite)[0] == 2
    assert cg.SHAPE_LABELS[2].startswith("mid-phase")


def test_shape_class_arithmetic():
    # A=1-24h (23 h), B=24-96h (72 h), C=96-156h (60 h), D=156-168h (12 h)
    assert cg.shape_class(np.array([[230, 144, 60, 6]]))[0] == 0      # rates 10, 2, 1, .5
    assert cg.shape_class(np.array([[230, 144, 60, 24]]))[0] == 1     # an end bump (rate 2 > 1)
    assert cg.shape_class(np.array([[23, 144, 60, 6]]))[0] == 2       # B faster than A
    assert cg.shape_class(np.array([[230, 36, 120, 6]]))[0] == 3      # B < C


# =================================================================== (2) data tests (skipped without the file)

YEAR_VOTES_L4563 = {2003: 203, 2004: 6541, 2005: 20239, 2006: 45325, 2007: 41541, 2008: 30479, 2009: 21375,
                    2010: 13970, 2011: 8556, 2012: 6474, 2013: 3572}


@pytest.fixture(scope="module")
def V():
    return cg.load_votes()


@pytest.fixture(scope="module")
def E(V):
    return cg.build_elections(V)


@pytest.fixture(scope="module")
def SD(V, E):
    return cg.build_sign_data(V, E)


@pytest.fixture(scope="module")
def HD(E):
    return cg.build_hazard_data(E)


@pytest.fixture(scope="module")
def cells(SD):
    return cg.cells_of(SD)


_MEMO: dict = {}


def memo(key, fn):
    if key not in _MEMO:
        _MEMO[key] = fn()
    return _MEMO[key]


@needs_data
def test_file_matches_recorded_size_and_checksum():
    assert cg.DATA_FILE.stat().st_size == cg.SIZE_BYTES == 14_936_383
    assert cg.sha256_of(cg.DATA_FILE) == cg.SHA256


@needs_data
def test_counts_reproduce_the_survey(V):
    """117 section 3.3 [L4562, L4563]: 198,275 votes (144,451 support, 41,176 oppose, 12,648 neutral), 3,926
    distinct (candidate, year, result) groups, the votes per year, and 11,380 named users -- voters AND
    candidates, which is what the survey and the SNAP page count; the voters alone are 10,416 (an earlier draft
    of this test compared 11,380 with the voters and failed: a finding about the test, not the data)."""
    assert V.n == 198_275
    assert int((V.vote == 1).sum()) == 144_451 and int((V.vote == -1).sum()) == 41_176 and int((V.vote == 0).sum()) == 12_648
    for y, n in YEAR_VOTES_L4563.items():
        assert int((V.year == y).sum()) == n
    key = (V.cand.astype(np.int64) * 3 + (V.res + 1)) * 4096 + (V.year - 2000)
    assert len(np.unique(key)) == 3_926
    assert V.n_names == 11_380
    assert len(np.unique(V.voter[V.voter >= 0])) == 10_416
    assert len(np.unique(np.concatenate([V.voter[V.voter >= 0], V.cand]))) == 11_380
    assert int((V.voter < 0).sum()) == 1_661


@needs_data
def test_cleaning_counts_and_election_structure(V, E):
    assert int(np.isnan(V.minute).sum()) == 9_368 == E.dropped["undated"]       # 9,367 empty fields and one impossible hour
    assert E.dropped == {"undated": 9_368, "empty_voter": 1_661, "self_vote": 88, "stray": 30, "duplicate": 396}
    assert E.n_elections == 4_062 and len(E.vote) == 188_393
    assert np.all(np.diff(E.cl) >= 0) and np.all(np.diff(E.minute)[np.diff(E.cl) == 0] >= 0)
    key = E.cl.astype(np.int64) * (V.n_names + 1) + E.voter
    assert len(np.unique(key)) == len(key)                                   # one vote per voter per election
    big = E.size >= 40
    span = np.array([E.minute[E.start[e] + E.size[e] - 1] - E.minute[E.start[e]] for e in np.nonzero(big)[0]]) / 1440.0
    assert 6.0 < np.median(span) < 7.2                                       # a week


@needs_data
def test_sample_sizes(SD, HD, cells):
    assert SD.n_elections == 2_493 and SD.n == 162_733
    A = cg.arrange(SD)
    assert len(cg.target_rows(SD, A)) == 150_218
    assert HD.n_elections == 2_595 and HD.sign.size == 174_705
    assert sum(1 for c in cells if c.startswith("y")) == 10 and sum(1 for c in cells if c.startswith("n")) == 4


@needs_data
def test_primary_coefficient_is_positive_against_the_shuffle_and_in_every_year_and_size(SD, cells):
    """sigma, first reading (v0.1 section 4.4; L4355, L4363): the controlled coefficient on the running share is
    positive overall, in every year and in every size class; against the within-election shuffle it is far
    outside the null overall.  (Fitted values are asserted to the precision the results file prints.)"""
    fit = cg.sign_fit_table(SD, cells)
    assert fit["all"]["logit_s"] == pytest.approx(0.848, abs=0.01) and fit["all"]["logit_se"] == pytest.approx(0.099, abs=0.01)
    assert fit["all"]["ame10"] * 100 == pytest.approx(0.76, abs=0.05)
    assert all(fit[c]["logit_s"] > 0 for c in fit)
    obs = cg.sign_stats(SD, None, {"all": cells["all"]}, windows=(), extras=False)
    keys, null = cg.sign_null(SD, {"all": cells["all"]}, B=40, seed=11, n_jobs=1, windows=(), extras=False)
    c = cg.compare_to_null(obs["all:logit_s"], null[:, keys.index("all:logit_s")])
    assert abs(c["null_mean"]) < 0.15 and c["z"] > 4 and c["p_up"] <= 0.05
    f = cg.compare_to_null(obs["all:fe_s"], null[:, keys.index("all:fe_s")])
    assert f["null_mean"] < -0.5 and f["z"] > 10                       # the fixed-effect null is strongly negative, mechanically


@needs_data
def test_candidates_outcome_is_the_confounder_and_the_shuffle_reproduces_the_raw_association(SD):
    """The raw coefficient (clock and turnout only) is about 6 and the shuffle alone gives nearly all of it; the
    candidate's outcome removes it, the voter's propensity does not."""
    lad = cg.ladder_stats(SD, None)
    nul = [cg.ladder_stats(SD, cg.within_shuffle(np.random.default_rng(s), SD)) for s in range(8)]
    m = {k: np.mean([d[k] for d in nul]) for k in lad}
    assert lad["clock"] == pytest.approx(6.01, abs=0.05) and m["clock"] > 0.93 * lad["clock"]
    assert lad["propensity"] > 0.95 * lad["clock"]                      # propensity moves almost nothing
    assert lad["outcome"] < 0.2 * lad["clock"] and lad["both"] == pytest.approx(0.848, abs=0.01)
    assert abs(m["both"]) < 0.3


@needs_data
def test_local_dependence_is_positive_symmetric_in_time_and_in_every_year_and_size(SD, cells):
    """The share of the previous 10 and of the next 10 votes, entered together: both far above the null, nearly
    equal (time-symmetry: the limit of the placebo is tested above), in every year from 2005 and every size class
    (the drift test of the sign-law registry, 112 section 6.5 test 3, applied by analogy: 112 states it for the
    16-type tie-sign model; here the sign is stable while the magnitude moves)."""
    st = cg.sign_stats(SD, None, {}, windows=(10,), extras=False)
    nul = [cg.sign_stats(SD, cg.within_shuffle(np.random.default_rng(s), SD), {}, windows=(10,), extras=False) for s in range(20)]
    for k in ("placebo:L10:logit_prior", "placebo:L10:logit_post", "placebo:L10:fe_prior", "placebo:L10:fe_post"):
        n = np.array([d[k] for d in nul])
        assert cg.compare_to_null(st[k], n)["z"] > 8
    assert st["placebo:L10:logit_prior"] == pytest.approx(1.44, abs=0.03) and st["placebo:L10:logit_post"] == pytest.approx(1.63, abs=0.03)
    assert abs(st["placebo:L10:logit_prior"] - st["placebo:L10:logit_post"]) < 0.4
    loc = cg.local_stats(SD, None, cells, robust=True)
    for c in cells:
        if c in ("y2004",):
            continue
        assert loc[f"{c}:prior"] > 1.0 and loc[f"{c}:prior"] / loc[f"{c}:prior_se"] > 2.0, c


@needs_data
def test_local_dependence_is_positive_after_both_kinds_of_run_and_larger_after_supportive_ones(SD):
    """Added at the review of 2026-11-01.  The first version read 'no asymmetry' off two excesses of similar size
    without testing their difference.  Both slopes (previous-10 share below and above one half) sit far above their
    shuffle nulls, and the difference (the hinge coefficient) sits above its own null too (z +3.5 at 200 draws): an
    asymmetry of degree, not the correction of opposing runs that the comparator (L1130, `sa`) reports."""
    c = cg.compute_asym(SD, B=20, seed=8, n_jobs=1)
    assert c["below"]["obs"] > c["below"]["null_mean"] and c["below"]["z"] > 5
    assert c["above"]["obs"] > c["above"]["null_mean"] and c["above"]["z"] > 5
    assert c["diff"]["z"] > 2.0


@needs_data
def test_recent_majority_is_followed_and_the_cumulative_majority_is_not(SD, cells):
    """The literal question: does a vote have the sign of the running majority?  Of the last 5 to 10 votes yes
    (more than random order, most of all when votes arrive within minutes); of all earlier votes it has it less
    often than random order."""
    c = {"all": cells["all"]}
    obs = cg.majority_stats(SD, None, c)
    nul = [cg.majority_stats(SD, cg.within_shuffle(np.random.default_rng(s), SD), c) for s in range(25)]
    cmp_ = {k: cg.compare_to_null(obs[k], np.array([d[k] for d in nul])) for k in obs}
    ex = lambda k: cmp_[k]["obs"] - cmp_[k]["null_mean"]
    assert ex("all:w5") > 0.008 and cmp_["all:w5"]["z"] > 8
    assert ex("all:w10") > 0.004 and cmp_["all:w10"]["z"] > 8
    assert ex("all:cum") < -0.002 and cmp_["all:cum"]["z"] < -8
    assert ex("all:w5_fast") > 0.025 and ex("all:w5_fast") > 5 * abs(ex("all:w5_slow"))


@needs_data
def test_gap_profile_peaks_within_minutes_and_same_minute_votes_disagree(SD):
    """Consecutive votes agree more than chance at gaps of 1 to 60 minutes (peak 2-5), nothing after four hours; votes
    saved in the same minute agree LESS than chance (the unexplained anomaly the results file records)."""
    out = cg.compute_gap(SD, B=60, seed=4, n_jobs=1)
    c = out["cmp"]
    exc = lambda k: c[k]["obs"] - c[k]["null_mean"]
    assert exc("gap2-5") > 0.045 and c["gap2-5"]["z"] > 8
    assert exc("gap2-5") > exc("gap21-60") > exc("gap61-240") > -0.002
    assert abs(exc("gap>1000")) < 0.02 and exc("gap241-1000") < 0.005
    assert exc("same_minute") < -0.05 and c["same_minute"]["z"] < -3.5
    assert out["counts"]["same_minute"] == 927


@needs_data
def test_cumulative_coefficient_changes_sign_with_turnout_in_the_logit_and_not_when_detrended(SD):
    """L4363 (the sign may flip with turnout): in the primary logit the running-share coefficient is positive below
    20 earlier votes and negative from 40; with an election-specific quadratic trend removed it stays above its
    null in every turnout bin.  The two disagree at high turnout, which the results file calls undecided."""
    st = cg.sign_stats(SD, None, {}, windows=(), extras=True)
    logit = {b: st[f"turnout{b[0]}-{b[1]}:logit_s"] for b in cg.TURNOUT_BINS}
    assert logit[(5, 10)] > 1.0 and logit[(10, 20)] > 1.0 and logit[(40, 80)] < -0.5 and logit[(80, 10**9)] < -2.0
    nul = [cg.sign_stats(SD, cg.within_shuffle(np.random.default_rng(s), SD), {}, windows=(), extras=True) for s in range(8)]
    for b in cg.TURNOUT_BINS:
        k = f"turnout{b[0]}-{b[1]}:fe_q"
        assert st[k] > np.mean([d[k] for d in nul]) + 2 * np.std([d[k] for d in nul], ddof=1)       # z is 2.8 to 5.5 against 400 draws


@needs_data
def test_cumulative_share_has_no_out_of_sample_gain_but_the_last_ten_votes_do(SD):
    """Part 3: forms compared out of sample (election folds), the mechanical gain subtracted (same form fitted to
    shuffled elections).  The recency window carries the signal; Kuran's cumulative-share form does not."""
    forms = {k: cg.SIGN_FORMS[k] for k in ("controls only (no running state)",
                                           "cumulative share, linear (Kuran: threshold falls with the share)",
                                           "share of the last 10 votes")}
    obs = {r["form"]: r["cv_gain_per_1000"] for r in cg.compare_sign_forms(SD, forms=forms)}
    sh = [{r["form"]: r["cv_gain_per_1000"] for r in cg.compare_sign_forms(SD, forms=forms, src=cg.within_shuffle(np.random.default_rng(s), SD))}
          for s in range(3)]
    ex = {k: obs[k] - np.mean([d[k] for d in sh]) for k in obs}
    assert ex["share of the last 10 votes"] > 2.0
    assert abs(ex["cumulative share, linear (Kuran: threshold falls with the share)"]) < 0.3


# ------------------------------------------------------------------ participation on the data

@needs_data
def test_curves_are_monotone_front_loaded_and_failing_elections_finish_first(HD):
    cur = cg.curve_table(HD, {"all": np.ones(HD.n_elections, bool), "fail": HD.fclass == 0, "pass": HD.fclass == 4})
    for v in cur.values():
        assert all(b >= a for a, b in zip(v["pooled"], v["pooled"][1:])) and all(b >= a for a, b in zip(v["median"], v["median"][1:]))
    i24, i168 = cg.CHECK_HOURS.index(24), cg.CHECK_HOURS.index(168)
    assert 0.44 < cur["all"]["pooled"][i24] < 0.50 and cur["all"]["pooled"][i168] > 0.95
    assert cur["fail"]["pooled"][i24] > cur["pass"]["pooled"][i24] + 0.2


@needs_data
def test_shape_is_one_the_clock_also_makes_but_elections_are_far_more_diverse_than_the_clock(HD):
    sh = cg.shape_table(HD, B=60, seed=2)
    assert sh["n_elections"] == 1_285
    assert 0.84 < sh["obs_freq"][0] + sh["obs_freq"][1] < 0.90
    assert sh["null_mean"][0] + sh["null_mean"][1] > 0.96
    assert abs(sh["obs_freq"][0] - sh["null_mean"][0]) < 0.03               # the dominant shape matches the clock's
    assert sh["var_f24_obs"] > 4 * sh["var_f24_null"]
    assert sh["obs_freq"][2] > 10 * sh["null_mean"][2] and sh["obs_freq"][3] > 3 * sh["null_mean"][3]


@needs_data
def test_stall_attaches_to_failure_and_falls_with_final_support(HD):
    """Renamed at the review of 2026-11-01 from '..._to_decisive_failure_only': a third of the elections ending at
    40-60% support also stall, so the stall is graded in final support, not confined to decisive failure; what is
    confined is the outcome (almost no stalled election was promoted)."""
    st = cg.stall_table(HD)
    fail72, pass72 = st[72][0], st[72][4]
    assert fail72[2] > 0.6 and fail72[3] > 0.6                              # lower Wilson bound
    assert pass72[2] < 0.01 and pass72[4] < 0.015
    assert [r[2] for r in st[72]] == sorted([r[2] for r in st[72]], reverse=True)       # monotone in final support
    assert st[72][1][2] > 0.25                                              # 40-60%: not only decisive failure
    stalled, promoted = sum(r[0] for r in st[72]), sum(r[5] for r in st[72])
    assert stalled == 402 and promoted == 5                                 # 397 of 402 silent after 72 h failed


@needs_data
def test_late_acceleration_is_not_triggered_by_the_state(HD):
    """Ignition would show as a late rise larger in contested states than composition predicts.  The end-window
    ratio exceeds one in the passing bands (a deadline bump) but the contested-minus-decisive contrast is
    SMALLER than under the path-randomising shuffle.  Recorded at the review of 2026-11-01: the late rise is not
    purely clock and composition either -- the comfortably passing band (85-95% at hour 120) rises more than the
    shuffle gives, which is not where ignition would show."""
    obs = cg.late_accel_stat(HD, HD.sign)
    nul = [cg.late_accel_stat(HD, cg.shuffle_signs(np.random.default_rng(s), HD)) for s in range(60)]
    c = cg.compare_to_null(obs["contrast"], np.array([d["contrast"] for d in nul]))
    assert obs[".70-.85"] > 1.2 and obs["<.50"] < 0.9
    assert c["z"] < 1.0 and c["p_up"] > 0.5
    b = cg.compare_to_null(obs[".85-.95"], np.array([d[".85-.95"] for d in nul]))
    assert b["z"] > 3.0


@needs_data
def test_participation_falls_when_the_tally_runs_against_and_not_when_support_is_decisive(HD):
    r = cg.hazard_null(HD, "turn+rate+bands", cg.HAZARD_WINDOWS["1-168 h"], B=30, seed=6, keys=("band0", "band1", "band3", "band4"))
    assert r["band0"]["z"] < -6 and r["band1"]["z"] < -6
    assert r["band0"]["obs"] < r["band1"]["obs"] < 0
    assert abs(r["band3"]["z"]) < 3 and abs(r["band4"]["z"]) < 3              # no upper gate: the decisive-pass bands sit at their null


@needs_data
def test_share_curvature_in_the_hazard_is_negative_in_every_window_never_convex(HD):
    """The raw curvature is negative in every window, but the sign shuffle gives a negative curvature too (the
    mechanical shape), so the claim 'never convex' is tested on the EXCESS over that null (added at the review of
    2026-11-01; the first version tested the raw coefficient only): no window shows a convex excess."""
    for w, win in cg.HAZARD_WINDOWS.items():
        X, y, off, g, names = cg._hazard_columns(HD, HD.sign, "turn+rate+s+s2", *win)
        f = cg.poisson_irls(X, y, off, g, names)
        b = dict(zip(names, f.beta))
        assert b["s2"] < 0 and b["s"] > 0, w
        c = cg.hazard_null(HD, "turn+rate+s+s2", win, B=30, seed=6, keys=("s2",))["s2"]
        assert c["null_mean"] < 0 and c["z"] < 1.0, w           # the 24-168 h excess is z -0.2 at 150 draws: sign not asserted


@needs_data
def test_hazard_state_terms_beat_clock_plus_persistence_out_of_sample(HD):
    forms = {k: v for k, v in cg.HAZARD_FORMS.items() if v in ("", "turn+rate", "turn+rate+s+s2")}
    out = cg.compare_hazard_forms(HD, cg.HAZARD_WINDOWS["1-168 h"], forms=forms)
    by = {r["spec"]: r for r in out}
    assert by["turn+rate"]["cv_gain"] > 5_000                               # persistence and turnout over the bare clock
    sh = cg.compare_hazard_forms(HD, cg.HAZARD_WINDOWS["1-168 h"], forms=forms, sign=cg.shuffle_signs(np.random.default_rng(1), HD))
    shy = {r["spec"]: r for r in sh}
    assert by["turn+rate+s+s2"]["cv_gain"] - shy["turn+rate+s+s2"]["cv_gain"] > 100


@needs_data
def test_report_builds_end_to_end_and_names_its_verdict():
    one = {k: v for k, v in list(cg.ROBUST_VARIANTS.items())[:1]}
    R = cg.compute_all(B=8, B_rob=4, B_forms=2, B_haz=6, B_hforms=2, n_jobs=4, B_ladder=4, B_shape=8, B_late=8,
                       B_boot=20, k_folds=2, variants=one)
    text = cg.format_report(R)
    for head in ("## Verdict", "## 1. Data, terms, cleaning", "## 2. Part 1", "## 3. Part 2", "## 4. Part 3", "## 5. The sign operand sigma",
                 "## 6. Caveats", "## Reproduce"):
        assert head in text
    assert "wiki-RfA" in text and "sigma" in text
