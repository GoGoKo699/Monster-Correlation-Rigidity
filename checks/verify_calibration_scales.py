#!/usr/bin/env python3
"""Regression tests for the audited small-scale calibration exception.

Exact scalar families only; no full VOA construction or theorem simulation.
"""
from fractions import Fraction as Q
from math import isqrt
import json
from verify_calibration_and_sharpness import Interval as I, calibrated_criterion
from scale_safe_roots import sqrt_bounds, SquareRootPrecisionLimit, MAX_ROOT_BITS

LABELS = []


def need(ok, label):
    if not ok:
        raise RuntimeError(label)
    LABELS.append(label)


def pair(k, ell, radius=Q(0), shift1=Q(0), shift2=Q(0)):
    s, t = Q(2)**(-k), Q(2)**(-ell)
    # w1 = s e + shift1*omega; w2 = t f + shift2*omega.
    def raw(scale, shift):
        n = scale**2/4 + scale*shift/2 + 12*shift**2
        tau = scale/4 + 12*shift
        cubic = scale**3/2 + Q(3,2)*scale**2*shift + Q(3,2)*scale*shift**2 + 24*shift**3
        return n, tau, cubic
    n1, a1, c1 = raw(s, shift1)
    n2, a2, c2 = raw(t, shift2)
    mutual = s*shift2/4 + t*shift1/4 + 12*shift1*shift2
    values = (n1, n2, a1, a2, c1, c2, mutual)
    weights = (s*s, t*t, s, t, s**3, t**3, s*t)
    return [I.radius(v, radius*w) for v, w in zip(values, weights)]


def root_tests():
    # An exact squared inequality checks containment without another sqrt call.
    for bits in (0, 1, 8, 80):
        for p in range(1, 20):
            for q in range(1, 20):
                x = Q(p, q)
                lo, hi = sqrt_bounds(x, bits)
                need(0 < lo <= hi and lo*lo <= x <= hi*hi,
                     f'root:{bits}:{p}:{q}')
                need(hi-lo <= max(Q(1), hi)/2**bits,
                     f'root_resolution:{bits}:{p}:{q}')
    for k in (-4096, -512, -100, 0, 39, 100, 512, 4096):
        x = Q(47, 192) * Q(2)**(2*k)
        lo, hi = sqrt_bounds(x)
        need(0 < lo and lo*lo <= x <= hi*hi, f'root_extreme:{k}')
    need(sqrt_bounds(Q(0)) == (0, 0), 'root:zero')
    for x, bits in ((Q(-1), 80), (Q(1), -1), (Q(1), 1.5)):
        try:
            sqrt_bounds(x, bits)
        except (ValueError, TypeError):
            need(True, f'root:invalid:{x}:{bits}')
        else:
            raise RuntimeError('invalid square-root argument accepted')
    # Reproduce the old absolute-grid failure without altering the new function.
    N = Q(47, 192) * Q(2)**(-78)
    old_k = isqrt((N*N).numerator * 2**160 // (N*N).denominator)
    need(old_k == 0 and N > 0, 'old_absolute_grid:zero_lower_bound_reproduced')
    need(sqrt_bounds(N*N)[0] > 0, 'adaptive_grid:positive_lower_bound')
    try:
        sqrt_bounds(Q(2)**(-2*(MAX_ROOT_BITS+1)))
    except SquareRootPrecisionLimit:
        need(True, 'root:typed_budget_limit')
    else:
        raise RuntimeError('precision limit not enforced')


def calibration_tests():
    powers = (-512, -100, 0, 10, 38, 39, 40, 60, 100, 512, 4096)
    cases = [(k, k) for k in powers] + [(k, -k) for k in powers]
    cases += [(39, 40), (40, 100), (100, 512)]
    cases = list(dict.fromkeys(cases))
    for k, ell in cases:
        result = calibrated_criterion(*pair(k, ell))
        need(result['certified'], f'pair_exact:{k}:{ell}')
        for index, f in enumerate(result['self_coupling_intervals']):
            need(f.lo > 0 and f.lo*f.lo <= Q(2116,141) <= f.hi*f.hi,
                 f'cap_inclusion:{k}:{ell}:{index}')
        need(result['primary_overlap_interval'].contains(-Q(1,47)),
             f'overlap_inclusion:{k}:{ell}')
        need(result['budget_upper'] < Q(3,188), f'budget:{k}:{ell}')
        noisy = calibrated_criterion(*pair(k, ell, Q(1,10**12)))
        need(noisy['certified'], f'pair_intervals:{k}:{ell}')
        wider = calibrated_criterion(*pair(k, ell, Q(1,10)))
        need(not wider['certified'], f'wide_intervals_inconclusive:{k}:{ell}')
    for k, ell in ((0,0), (39,40), (100,512), (-100,60)):
        answer = calibrated_criterion(*pair(k, ell, shift1=Q(1), shift2=-Q(2)))
        need(answer['certified'], f'exact_stress_shift:{k}:{ell}')
    args = pair(0,0)
    args[0] = I(Q(0), args[0].hi)
    need(not calibrated_criterion(*args)['certified'], 'norm_interval_reaches_zero')
    args = [I.point(v) for v in (12,Q(1,4),12,Q(1,4),24,Q(1,2),Q(1,4))]
    need(not calibrated_criterion(*args)['certified'], 'pure_stress_not_normalized')
    args = pair(0,0)
    args[2], args[4] = -args[2], -args[4]
    need(not calibrated_criterion(*args)['certified'], 'negative_sign_not_changed')
    args = pair(0,0)
    args[-1] = I.point(Q(1,4))
    need(not calibrated_criterion(*args)['certified'], 'duplicate_pair_rejected')
    args = pair(0,0)
    args[4] = I.point(100)
    need(not calibrated_criterion(*args)['certified'], 'impossible_coupling_rejected')
    answer = calibrated_criterion(*pair(20000,20000))
    need(not answer['certified'] and 'precision budget' in answer['reason'],
         'resource_limit_is_explicit_inconclusive')
    return len(cases)


def main():
    root_tests()
    pairs = calibration_tests()
    need(len(LABELS) == len(set(LABELS)), 'unique_regression_labels')
    print(json.dumps({'status':'PASS scale-aware calibration regression',
                      'checks':len(LABELS),'labels':LABELS,
                      'scale_pairs':pairs,'largest_field_scale_power':4096,
                      'resource_limit_probe_power':20000,
                      'largest_physical_coefficient_vector':3,
                      'full_VOA_simulated':False}, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
