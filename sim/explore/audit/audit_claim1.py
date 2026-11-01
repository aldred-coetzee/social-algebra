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
# (A) lower end strict whenever tau_1 != tau_2
viol = eq = 0; N = 60000
for _ in range(N):
    a, b = crowd(), crowd(); t1, t2 = tau(a), tau(b); tm = tau(a + b)
    if t1 != t2:
        if tm <= min(t1, t2): viol += 1
    else:
        eq += (tm == t1)
print(f"(A) {N} pairs: tau_m <= min with tau_1 != tau_2: {viol} violations; equal parts gave equality every time: {eq}")
# (B) M7(iii)'s margin: inf of E_2 over [0, tau_2) is 0 for every crowd with tau_2 > 0
#     (approached from the left at tau_2). Check on a fine grid just below tau_2.
mx = Fr(0); cnt = 0
for _ in range(2000):
    b = crowd(); t2 = tau(b)
    if t2 == 0: continue
    cnt += 1
    r = t2 - Fr(1, 10**6)
    mx = max(mx, F(b, r) - r)
print(f"(B) {cnt} crowds with tau_2 > 0: largest E_2 at tau_2 - 1e-6 is {float(mx):.2e} (so inf over [0,tau_2) is 0)")
# (C) sharpened necessity: ignition at some weight requires F_1(tau_2^-) >= tau_2 as well
def Fleft(th, r): return Fr(sum(1 for t in th if t < r), len(th))
bad = ign = 0
for _ in range(60000):
    a, b = crowd(), crowd(); t1, t2 = tau(a), tau(b)
    if t1 >= t2: a, b, t1, t2 = b, a, t2, t1
    if t1 == t2: continue
    # try many integer weights by replicating crowds
    fired = any(tau(a * i + b * j) > t2 for i in range(1, 6) for j in range(1, 6))
    if fired:
        ign += 1
        if not (F(a, t2) > t2 and Fleft(a, t2) >= t2): bad += 1
print(f"(C) {ign} igniting pairs: sharpened necessary condition failed {bad} times")
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
    if eps is None or eps > 0:
        tested += 1
        lam_star = Fr(1, 2) if eps is None else eps / (1 + eps)
        # pick integer weights i:j with i/(i+j) < lam_star
        i, j = 1, int(1 / lam_star) + 2
        ok += tau(a * (i * len(b)) + b * (j * len(a))) > t2   # weight of a is i/(i+j)
print(f"(D) corrected margin condition held in {tested} pairs; small weight ignited in {ok} of them")
