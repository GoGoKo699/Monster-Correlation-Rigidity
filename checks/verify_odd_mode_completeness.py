#!/usr/bin/env python3
"""Exact certificates for complementary odd primary channels and their commutator.

No Monster matrix or character table. Small even-Heisenberg controls are c=3,
not holomorphic c=24. Completeness uses the analytic rank argument in Note19.
The previous polynomial-independence question remains unresolved.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import odd_mode_ward as ward

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []


def need(ok: bool, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def determinant(matrix):
    a = [list(map(F, r)) for r in matrix]
    ans = F(1)
    for i in range(len(a)):
        j = next((j for j in range(i, len(a)) if a[j][i]), None)
        if j is None:
            return F(0)
        if i != j:
            a[i], a[j] = a[j], a[i]
            ans = -ans
        p = a[i][i]
        ans *= p
        for j in range(i+1, len(a)):
            s = a[j][i]/p
            a[j] = [x-s*y for x, y in zip(a[j], a[i])]
    return ans


def pair_certificate(h: int):
    vac, pri = ward.Vir(24, 0), ward.Vir(24, 2)
    rows, total = [], F(0)
    for i in range(h+1):
        p, weight = i-1, 2*h-i
        basis = ward.parts(weight)
        matrix = [[vac.gram(a, b) for b in basis] for a in basis]
        rhs = []
        for lam in basis:
            value, index = F((-1)**h), p
            for m in lam:
                value *= (h-1)*(m+1)-index
                index += m
            rhs.append(value if index == 2*h-1 else F(0))
        projection = ward.solve(matrix, rhs)
        traces = [vac.mode(lam, weight-1, (2,)).get((2,), 0)
                  +196883*pri.mode(lam, weight-1, ()).get((), 0) for lam in basis]
        contribution = comb(h, i)*sum((x*y for x, y in zip(projection, traces)), F(0))
        total += contribution
        need(all(determinant([r[:k] for r in matrix[:k]]) > 0
                 for k in range(1, len(matrix)+1)), f'pair:h{h}_weight{weight}_positive_Gram')
        need([sum((a*x for a, x in zip(r, projection)), F(0)) for r in matrix] == rhs,
             f'pair:h{h}_weight{weight}_exact_projection')
        rows.append({'weight': weight, 'partitions': basis, 'gram': matrix, 'pairing': rhs,
                     'projection': projection, 'trace': traces, 'star_coefficient': comb(h, i),
                     'contribution': contribution})
    return total, rows


def certificates():
    results = {}
    for h, expected in ((3, -564), (5, -4)):
        total, rows = pair_certificate(h)
        need(total == expected, f'pair:h{h}_zero_mode_trace_coefficient')
        results[str(h)] = {'total': total, 'rows': rows}
    need([r['contribution'] for r in results['5']['rows']] ==
         [-613019, 2643600, -4519500, 3823700, -1598225, 263440],
         'pair:h5_all_six_contributions')
    total, rows = ward.reconstruct(3, 3, 5)
    for row in rows:
        matrix, x, rhs = row['gram'], row['projection'], row['pairing']
        need(all(determinant([r[:k] for r in matrix[:k]]) > 0
                 for k in range(1, len(matrix)+1)), f'triple:weight{row["weight"]}_positive_Gram')
        need([sum((a*b for a, b in zip(r, x)), F(0)) for r in matrix] == rhs,
             f'triple:weight{row["weight"]}_projection')
    need(total == -2, 'triple:335_coefficient_minus_two')
    need([r['contribution'] for r in rows] ==
         [131720, -958935, 2867775, -4519500, 3965400, -1839057, 352595],
         'triple:335_all_seven_contributions')
    need(ward.reconstruct(5, 3, 3)[0] == -2, 'triple:533_cyclic_convention_check')
    need(ward.reconstruct(3, 5, 3)[0] == -2, 'triple:353_cyclic_convention_check')
    need(ward.reconstruct(3, 3, 3)[0] == -36, 'regression:previous_333_coefficient')
    return {'pair': results, 'triple_335': {'total': total, 'rows': rows}}


def character_checks():
    order = 5
    def mul(a, b):
        return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(order+1)]
    def power(a, n):
        b = [1]+[0]*order
        for _ in range(n):
            b = mul(b, a)
        return b
    def inverse(a):
        b = [1]+[0]*order
        for i in range(1, order+1):
            b[i] = -sum(a[j]*b[i-j] for j in range(1, i+1))
        return b
    e4 = [1]+[240*sum(d**3 for d in range(1, k+1) if k % d == 0)
               for k in range(1, order+1)]
    delta = [1]+[0]*order
    for m in range(1, order+1):
        factor = [0]*(order+1)
        for j in range(order//m+1):
            factor[j*m] = (-1)**j*comb(24, j)
        delta = mul(delta, factor)
    chars = mul(power(e4, 3), inverse(delta))
    chars[1] -= 744
    need(chars == [1, 0, 196884, 21493760, 864299970, 20245856256],
         'character:J_through_weight_five_no_group_data')
    def partitions(n, top=None):
        if n == 0:
            return [()]
        top = n if top is None else top
        return [(k,)+rest for k in range(min(n, top), 0, -1)
                for rest in partitions(n-k, k)]
    counts = {0: 1, 1: 0}
    for n in range(2, 6):
        counts[n] = chars[n]-len(ward.parts(n))-sum(counts[h]*len(partitions(n-h))
                                                          for h in range(2, n))
    need([counts[h] for h in range(2, 6)] == [196883, 21296876, 842609326, 19360062527],
         'character:four_primary_multiplicities')
    # Check absence of relevant low-level null states by positive exact Grams.
    for h in range(2, 5):
        module = ward.Vir(24, h)
        for level in range(1, 6-h):
            bs = partitions(level)
            gram = [[module.gram(a, b) for b in bs] for a in bs]
            need(all(determinant([r[:k] for r in gram[:k]]) > 0
                     for k in range(1, len(bs)+1)), f'descendants:h{h}_level{level}_no_null')
    need(counts[3]+counts[5] == counts[2]*(counts[2]-1)//2,
         'completeness:odd_primary_dimensions_exhaust_skew_space')
    need(F(564, 2) == 282 and F(4, 2) == 2, 'completeness:half_Frobenius_isometry_scales')
    need(F(36, 282) == F(6, 47), 'commutator:three_channel_coefficient_six_over_47')
    need(F(2, 2) == 1, 'commutator:five_channel_coefficient_one')
    need(F(282, 2) == 141, 'commutator:mixed_five_three_projection_coefficient')
    need(F(47, 6)**2/F(141) == F(47, 108), 'Jacobi:exact_missing_channel_coefficient')
    return {'character': chars, 'primary_dimensions': counts,
            'skew_dimension': counts[2]*(counts[2]-1)//2}


def general_heisenberg_mode(field, index, state, n, cutoff):
    """Direct normal-ordered monomial fields; annihilators never act on new creators."""
    out = defaultdict(F)
    for mon, c1 in field.items():
        slots = tuple((p % n, p//n+1) for p, count in enumerate(mon) for _ in range(count))
        weight = sum(m for _, m in slots)
        target = index+1-weight
        for key, c2 in state.items():
            inputweight = sum((p//n+1)*v for p, v in enumerate(key))
            outputweight = inputweight-target
            if outputweight < 0:
                continue
            remaining, created = list(key), [0]*len(key)
            def rec(k, total, coefficient):
                if k == len(slots):
                    if total == target:
                        result = tuple(a+b for a, b in zip(remaining, created))
                        out[result] += c1*c2*coefficient
                    return
                species, m = slots[k]
                if k == len(slots)-1:
                    modes = [target-total]
                else:
                    modes = [r for r in range(1, min(inputweight, cutoff)+1)
                             if remaining[(r-1)*n+species]]+list(range(-outputweight, -m+1))
                for r in modes:
                    if not r or abs(r) > cutoff:
                        continue
                    derivative = (-1)**(m-1)*ward.bc(r+m-1, m-1)
                    if not derivative:
                        continue
                    p = (abs(r)-1)*n+species
                    if r > 0:
                        if not remaining[p]:
                            continue
                        factor = r*remaining[p]
                        remaining[p] -= 1
                        rec(k+1, total+r, coefficient*derivative*factor)
                        remaining[p] += 1
                    else:
                        created[p] += 1
                        rec(k+1, total+r, coefficient*derivative)
                        created[p] -= 1
            rec(0, 0, F(1))
    return {k: c for k, c in out.items() if c}


def fock_checks():
    path = Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(path.read_bytes()).hexdigest() ==
         '701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:unchanged_note13_oscillator_helper')
    spec = importlib.util.spec_from_file_location('_odd_fock', path)
    o = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(o)
    n, cutoff = 3, 16
    o.GRADE = cutoff
    I = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
    vac = {(0,)*(n*cutoff): F(1)}
    def vir(m, s):
        return o.quadratic_mode(I, m+1, s, n)
    def state(terms):
        out = {}
        for coefficient, slots in terms:
            key = [0]*(n*cutoff)
            for mode, species in slots:
                key[(mode-1)*n+species] += 1
            k = tuple(key)
            out[k] = out.get(k, F(0))+coefficient
        return {k: c for k, c in out.items() if c}
    # An explicit weight-five primary in the even Heisenberg algebra.
    w = state([(-F(4, 5), [(2, 2), (3, 1)]), (F(4, 5), [(2, 1), (3, 2)]),
               (F(2, 5), [(1, 2), (4, 1)]), (-F(1), [(1, 2)]*3+[(2, 1)]),
               (-F(2, 5), [(1, 1), (4, 2)]), (F(1), [(1, 1), (1, 2), (1, 2), (2, 2)]),
               (-F(1), [(1, 1), (1, 1), (1, 2), (2, 1)]), (F(1), [(1, 1)]*3+[(2, 2)])])
    need(all(not vir(m, w) for m in range(1, 6)), 'fock:explicit_weight_five_state_is_primary')
    norm = o.inner(w, w, n)
    need(norm == F(1024, 25), 'fock:positive_weight_five_norm')
    need(general_heisenberg_mode(w, -1, vac, n, cutoff) == w, 'fock:general_field_creation')
    need(o.inner(vac, general_heisenberg_mode(w, 9, w, n, cutoff), n) == -norm,
         'fock:odd_primary_highest_pole_sign')
    @lru_cache(None)
    def descend(lam):
        s = vac
        for m in reversed(lam):
            s = vir(-m, s)
        return s
    pair_count = 0
    for i in range(6):
        p, weight = i-1, 10-i
        actual = general_heisenberg_mode(w, p, w, n, cutoff)
        for lam in ward.parts(weight):
            coefficient, q = -F(1), p
            for m in lam:
                coefficient *= 4*(m+1)-q
                q += m
            expected = coefficient*norm if q == 9 else F(0)
            if o.inner(descend(lam), actual, n) != expected:
                raise RuntimeError('Weight-five pair Ward control failed')
            pair_count += 1
    need(pair_count == 37, 'fock:all_37_weight_five_pair_projections')
    skew = []
    for i, j in combinations(range(n), 2):
        A = [[0]*n for _ in range(n)]
        A[i][j], A[j][i] = 1, -1
        skew.append(tuple(map(tuple, A)))
    def w3(A):
        return state([(F(A[i][j], 2), [(2, i), (1, j)])
                      for i in range(n) for j in range(n) if A[i][j]])
    @lru_cache(None)
    def mode3_cached(A, index, source):
        s, out = dict(source), {}
        for i in range(n):
            for j in range(n):
                if not A[i][j]:
                    continue
                for r in range(-cutoff, cutoff+1):
                    q = index-2-r
                    if not r or not q or abs(q) > cutoff:
                        continue
                    value = s
                    for species, mode in reversed(sorted(((i, r), (j, q)), key=lambda x: x[1] >= 0)):
                        value = o.oscillator(value, species, mode, n)
                    out = o.add((1, out), (-F(r+1, 2)*A[i][j], value))
        return tuple(sorted(out.items()))
    def mode3(A, index, source):
        return dict(mode3_cached(A, index, tuple(sorted(source.items()))))
    a, b = w3(skew[0]), w3(skew[1])
    t = o.inner(a, mode3(skew[1], 4, w), n)
    need(t == -F(48, 5), 'fock:nonzero_335_coupling')
    need(t == o.inner(w, mode3(skew[0], 0, b), n), 'fock:335_first_slot_convention')
    for p in range(5, 11):
        actual = o.inner(vac, mode3(skew[0], p, mode3(skew[1], 9-p, w)), n)
        need(actual == ward.ward((), p, 9-p, 3, 3, 5)*t, f'fock:335_vacuum_word_p{p}')
    triple_count = 0
    for i in range(4):
        r = i-1
        for j in range(7-i):
            s, weight, actual = j-1, 11-i-j, {}
            for k in range(max(7-s, 7)+1):
                coefficient = (-1)**k*ward.bc(r, k)
                if k <= 7-s:
                    actual = o.add((1, actual), (coefficient, mode3(skew[0], r-k, mode3(skew[1], s+k, w))))
                if k <= 7:
                    actual = o.add((1, actual), (-coefficient*(-1 if r % 2 else 1),
                                                mode3(skew[1], r+s-k, mode3(skew[0], k, w))))
            for lam in ward.parts(weight):
                if o.inner(descend(lam), actual, n) != ward.composite(lam, r, s, 3, 3, 5)*t:
                    raise RuntimeError('335 composite Ward control failed')
                triple_count += 1
    need(triple_count == 130, 'fock:all_130_335_composite_pairings')
    cross_count = 0
    for i in range(4):
        actual, weight = mode3(skew[0], i-1, w), 8-i
        for lam in ward.parts(weight):
            if o.inner(descend(lam), actual, n):
                raise RuntimeError('Different-weight primary vacuum projection nonzero')
            cross_count += 1
    need(True, 'fock:cross_weight_three_five_vacuum_projection_zero')
    qstates, qmats = [], []
    for i in range(n):
        for j in range(i, n):
            A = [[0]*n for _ in range(n)]
            A[i][j] = A[j][i] = 1
            qmats.append(A)
            qstates.append(o.quadratic_mode(A, -1, vac, n))
    actions = [general_heisenberg_mode(w, 4, b, n, cutoff) for b in qstates]
    for i, a in enumerate(qstates):
        for j, b in enumerate(qstates):
            coefficient = o.inner(w, o.quadratic_mode(qmats[i], -2, b, n), n)
            if coefficient != o.inner(a, actions[j], n):
                raise RuntimeError('Pair generation/zero-mode adjoint mismatch')
    need(True, 'fock:all_36_weight_five_pair_zero_mode_adjoints')
    need(all(o.inner(a, actions[j], n) == -o.inner(actions[i], b, n)
             for i, a in enumerate(qstates) for j, b in enumerate(qstates)),
         'fock:weight_five_zero_mode_is_skew_adjoint')
    omega = vir(-2, vac)
    need(not general_heisenberg_mode(w, 4, omega, n, cutoff), 'fock:zero_mode_kills_stress_direction')
    return {'central_charge': n, 'pair_pairings': pair_count, 'composite_pairings_335': triple_count,
            'different_weight_pairings': cross_count, 'pair_zero_mode_adjoints': 36,
            'weight_five_norm': norm, 'coupling_335': t,
            'oscillator_cutoff': cutoff, 'highest_composite_weight': 11,
            'example_is_extremal_holomorphic': False}


def algebra_checks():
    n = 4
    def zero(): return [[F(0)]*n for _ in range(n)]
    def add(a, b): return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]
    def scale(a, c): return [[c*x for x in r] for r in a]
    def mul(a, b): return [[sum((a[i][k]*b[k][j] for k in range(n)), F(0))
                           for j in range(n)] for i in range(n)]
    def comm(a, b): return add(mul(a, b), scale(mul(b, a), -1))
    basis = []
    for i, j in combinations(range(n), 2):
        a = zero(); a[i][j] = 1; a[j][i] = -1; basis.append(a)
    def p5(a): return scale(basis[4], a[1][3])
    def p3(a): return add(a, scale(p5(a), -1))
    def total(xs):
        a = zero()
        for x in xs: a = add(a, x)
        return a
    def beta3(a, b): return scale(p3(comm(a, b)), F(47, 6))
    def beta5(a, b): return p5(comm(a, b))
    def mixed(z, c): return scale(p3(comm(z, c)), 141)
    x, y, z = basis[0], basis[3], basis[5]
    cyclic = [(x, y, z), (y, z, x), (z, x, y)]
    jac = total([beta3(beta3(a, b), c) for a, b, c in cyclic])
    excursion = total([mixed(beta5(a, b), c) for a, b, c in cyclic])
    need(jac != zero(), 'negative:truncated_bracket_can_have_nonzero_Jacobiator')
    need(add(jac, scale(excursion, F(47, 108))) == zero(), 'Jacobi:missing_channel_exactly_restores_matrix_identity')
    need(all(comm(a, b) == add(scale(beta3(a, b), F(6, 47)), beta5(a, b))
             for a, b in product(basis, repeat=2)), 'commutator:two_channel_decomposition_all_small_pairs')
    need(all(add(p3(a), p5(a)) == a for a in basis), 'completeness:complementary_projectors_recover_every_direction')
    return {'commutator_coefficients': ['6/47', '1'], 'mixed_53_to_3_coefficient': 141,
            'Jacobi_correction': '47/108', 'toy_decomposition_claimed_to_be_CFT': False}


def strings(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {k: strings(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [strings(v) for v in x]
    return x


def main():
    cert = certificates()
    counts = character_checks()
    fock = fock_checks()
    algebra = algebra_checks()
    report = {'status': 'PASS within exact Ward/Fock/scalar scopes', 'base_commit': BASE,
              'checks': len(LABELS), 'labels': LABELS, 'certificates': cert,
              'character_and_dimensions': counts, 'Fock_controls': fock, 'algebra': algebra,
              'largest_square_matrix_dimension': 14, 'arithmetic': 'integers and fractions only',
              'Monster_character_data_used': False, 'full_extremal_tensor_constructed': False,
              'Note18_polynomial_independence': 'UNRESOLVED', 'new_selection_axiom': False,
              'Monster_uniqueness_proved': False, 'independent_review_or_formal_verification': False}
    print(json.dumps(strings(report), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
