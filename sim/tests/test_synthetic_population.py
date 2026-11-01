"""Synthetic-population identifiability experiment: machinery tests on small worlds (fast, no data needed).

Covers: the generator is deterministic under its seed; training and held-out worlds use different seeds and share no
person; no inference function is given the drives; `report` refuses without the rule block; the criterion functions at
their edges; the likelihood gradient is right; the state D conditions on equals the generator's; D recovers drives in a
well-sampled toy world.  Results: sim/results/synthetic_population_identifiability.md.
"""
from __future__ import annotations

import inspect

import numpy as np
import pytest
from scipy.optimize import check_grad

from models import synthetic_population as S


def test_generator_is_deterministic_under_seed():
    a = S.make_world(5, S.SEED_TRAIN, 3, 2.0, steps=30)
    b = S.make_world(5, S.SEED_TRAIN, 3, 2.0, steps=30)
    assert np.array_equal(a.obs.choice, b.obs.choice) and np.array_equal(a.theta, b.theta)
    assert np.array_equal(a.obs.exit_step, b.obs.exit_step)
    c = S.make_world(5, S.SEED_TRAIN, 4, 2.0, steps=30)
    assert not np.array_equal(a.theta, c.theta)


def test_train_and_heldout_use_different_seeds_and_share_no_person():
    assert S.SEED_TRAIN == 20261101 and S.SEED_TEST == 20261102 and S.SEED_CALIB not in (S.SEED_TRAIN, S.SEED_TEST)
    tr = np.vstack([S.make_world(8, S.SEED_TRAIN, i, 2.0, steps=5).theta for i in range(10)])
    te = np.vstack([S.make_world(8, S.SEED_TEST, i, 2.0, steps=5).theta for i in range(10)])
    rows = {tuple(r) for r in tr}
    assert not any(tuple(r) in rows for r in te)
    assert len({tuple(r) for r in tr}) == len(tr)  # nobody repeated within a set either


def test_no_inference_function_receives_theta():
    for fn in (S.person_features, S.fit_drives, S.reconstruct_state):
        names = list(inspect.signature(fn).parameters)
        assert "theta" not in names and names[0] == "obs"
    w = S.make_world(4, 1, 0, 2.0, steps=20)
    assert not hasattr(w.obs, "theta") and set(vars(w.obs)) == {"n", "choice", "exit_step"}
    # fitting is a function of the observables only: a world whose drives are altered but whose choices are identical gives the same fit
    w2 = S.World(w.obs, w.theta + 5.0, w.r_before, w.m_before)
    assert np.allclose(S.fit_drives(w.obs, 20), S.fit_drives(w2.obs, 20))


def test_report_refuses_without_the_rule_block(tmp_path):
    p = tmp_path / "x.md"
    with pytest.raises(SystemExit):
        S.require_rule(p)
    p.write_text("# nothing here\n")
    with pytest.raises(SystemExit):
        S.require_rule(p)
    p.write_text(S.rule_block())
    S.require_rule(p)  # does not raise


def test_rule_block_is_verbatim_and_carries_the_numbers():
    b = S.rule_block()
    assert S.RULE_TEXT in b and "20261101" in b and "20261102" in b and "Nothing else is run. No tuning." in b
    assert "C1" in b and "more than 0.02" in b and "within 10%" in b


def test_criteria_at_the_edges():
    assert S.c1_met([0.51, 0.6, 0.9]) and not S.c1_met([0.5, 0.9, 0.9])  # equality is not a pass
    assert not S.c1_met([0.9, 0.9, float("nan")])
    # C2: both conditions, both strict
    assert S.c2_met(94.9, 100.0, 0.80, 0.77)
    assert not S.c2_met(95.0, 100.0, 0.80, 0.77)  # exactly 5%
    assert not S.c2_met(90.0, 100.0, 0.79, 0.77)  # exactly 0.02 (not more)
    assert not S.c2_met(90.0, 100.0, 0.70, 0.77)
    assert not S.c2_met(90.0, 100.0, float("nan"), 0.5)
    # C3: within 10% is inclusive
    assert S.c3_met(110.0, 100.0) and not S.c3_met(110.5, 100.0) and S.c3_met(90.0, 100.0)


def test_the_rules_exit_threshold_never_fires_and_a_higher_one_does():
    ex = [S.make_world(3, S.SEED_CALIB, i, S.EXIT_C_RULE).obs.exit_step for i in range(40)]
    assert all((e < 0).all() for e in ex)
    ex = [S.make_world(3, S.SEED_CALIB, i, 3.0).obs.exit_step for i in range(20)]
    assert any((e >= 0).any() for e in ex)


def test_reconstructed_state_equals_generators_state_and_absent_persons_stop():
    w = S.make_world(6, 7, 1, 3.0, steps=60)
    R, M = S.reconstruct_state(w.obs)
    assert np.allclose(R, w.r_before) and np.allclose(M, w.m_before)
    for i in np.flatnonzero(w.obs.exit_step >= 0):
        e = w.obs.exit_step[i]
        assert (w.obs.choice[: e + 1, i] >= 0).all() and (w.obs.choice[e + 1 :, i] == -1).all()


def test_choices_are_valid_actions():
    w = S.make_world(5, 3, 0, 3.0, steps=40)
    ch = w.obs.choice
    n = 5
    for t in range(40):
        for i in range(n):
            k = ch[t, i]
            assert k == -1 or 0 <= k < 2 + 2 * n
            if k >= 2:
                j = (k - 2) % n
                assert j != i and ch[t, j] >= 0  # target is present


@pytest.mark.parametrize("ties", [True, False])
def test_likelihood_gradient_matches_finite_differences(ties):
    w = S.make_world(4, 11, 2, 3.0, steps=25)
    n, W, R, M, pres, Y, act = S._prepare(w.obs, 25, ties)
    rng = np.random.default_rng(0)
    x = rng.normal(size=3 * n)
    f = lambda z: S._nll_grad(z, n, W, R, M, pres, Y, not ties, act)[0]
    g = lambda z: S._nll_grad(z, n, W, R, M, pres, Y, not ties, act)[1]
    assert check_grad(f, g, x, epsilon=1e-6) < 1e-4 * max(1.0, np.linalg.norm(g(x)))


def test_drive_fit_recovers_drives_in_a_long_toy_world():
    ws = [S.make_world(5, 5, i, -9.0, steps=400) for i in range(4)]
    est = np.vstack([S.fit_drives(w.obs, 400) for w in ws])
    tru = np.vstack([w.theta for w in ws])
    for d in range(3):
        assert S.pearson(est[:, d], tru[:, d]) > 0.5


def test_person_features_shape_and_ranges():
    w = S.make_world(5, 5, 0, -9.0, steps=60)
    F = S.person_features(w.obs, 60)
    assert F.shape == (5, 2) and (F[:, 0] >= 0).all() and (F[:, 0] <= 1).all()


def test_ridge_and_logit_models_are_frozen_on_training_rows():
    rng = np.random.default_rng(1)
    X, y = rng.normal(size=(50, 3)), rng.normal(size=50)
    m = S.ridge_fit(X, y)
    p1 = S.ridge_predict(m, X[:5])
    assert np.allclose(p1, S.ridge_predict(m, X[:5]))  # applying does not refit
    # closed form: zero penalty would be OLS; with a big penalty predictions shrink to the mean
    big = S.ridge_fit(X, y, l2=1e9)
    assert np.allclose(S.ridge_predict(big, X), y.mean(), atol=1e-3)
    yb = (y > 0).astype(float)
    lm = S.logit_model(X, yb)
    assert S.logit_apply(lm, X).shape == (50,)
    one = S.logit_model(X, np.zeros(50))
    assert np.allclose(S.logit_apply(one, X), 0.0)  # single class: base rate


def test_pearson_degenerate_is_nan():
    assert np.isnan(S.pearson([1, 1, 1], [1, 2, 3])) and S.pearson([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)
