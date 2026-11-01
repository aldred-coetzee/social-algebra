# Audit scripts by the next-pattern session (2026-11-01), exact Fractions; checks corrections 1-3 and the corrected sufficiency of models/02 Claim 1. Slow by design.
from fractions import Fraction as Fr
import random
random.seed(7)
def F(th, r):            # empirical CDF at r
    return Fr(sum(1 for t in th if t <= r), len(th))
def tau(th):             # orbit from 0, exact
    r = Fr(0)
    while True:
        s = F(th, r)
        if s == r: return r
        r = s
def crowd():
    n = random.randint(1, 7); D = random.choice([6, 12, 20])
    return [Fr(random.randint(0, D), D) for _ in range(n)]
# (D) corrected sufficiency: B = {r <= tau_2 : E_1(r) <= 0}, eps = inf_B E_2 > 0 => small weights ignite
ok = tested = 0
import itertools
for _ in range(20000):
    a, b = crowd(), crowd(); t1, t2 = tau(a), tau(b)
    if t1 >= t2: a, b, t1, t2 = b, a, t2, t1
    if t1 == t2: continue
    # evaluate on all breakpoints: thresholds, tau_2, and points just left of them
    pts = sorted(set([Fr(0), t2] + [t for t in a + b if t < t2]))
    probe = []
    for p in pts:
        probe.append(p)
        if p > 0: probe.append(p - Fr(1, 10**6))
    Bset = [r for r in probe if F(a, r) - r <= 0]
    if not Bset: eps = None
    else: eps = min(F(b, r) - r for r in Bset)
    if eps is not None and eps <= Fr(2, 10**6): eps = Fr(0)   # a touch point of E_2 inside B: no margin
    if eps is None or eps > 0:
        lam_star = Fr(1, 2) if eps is None else eps / (1 + eps)
        i, j = 1, int(1 / lam_star) + 2
        if j > 40: continue
        tested += 1
        ok += tau(a * (i * len(b)) + b * (j * len(a))) > t2   # weight of a is i/(i+j)
print(f"(D) corrected margin condition held in {tested} pairs; small weight ignited in {ok} of them")
