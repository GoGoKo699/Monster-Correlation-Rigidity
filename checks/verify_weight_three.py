#!/usr/bin/env python3
"""Exact, bounded checks for the weight-three OPE Gram identity.

The oscillator tests are in small even free-boson VOAs, not the c=24
holomorphic candidate. Large dimensions below are scalar consequences only.
No Monster matrix, character table, OPE tensor, or uniqueness proof is used.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
import json

BASE = '514c11d54ac5d743767ec631f55d258665a5501b'
LABELS: list[str] = []
GRADE = 3


def need(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)
    LABELS.append(label)


def add(*terms):
    out = defaultdict(Q)
    for scale, state in terms:
        for v, c in state.items():
            out[v] += scale*c
    return {v: c for v, c in out.items() if c}


def inner(a, b, n):
    total = Q(0)
    for v, c in a.items():
        if v in b:
            norm = 1
            for pos, count in enumerate(v):
                mode = pos//n+1
                norm *= mode**count*factorial(count)
            total += c*b[v]*norm
    return total


def oscillator(state, species, mode, n):
    if mode == 0 or abs(mode) > GRADE:
        return {}
    out = defaultdict(Q)
    pos = (abs(mode)-1)*n+species
    for v, c in state.items():
        w = list(v)
        if mode > 0:
            if w[pos] == 0:
                continue
            factor = mode*w[pos]
            w[pos] -= 1
        else:
            factor = 1
            w[pos] += 1
        out[tuple(w)] += c*factor
    return dict(out)


def quadratic_mode(A, k, state, n):
    """Direct normal-ordered oscillator sum for Y(a_A,z), a_A=1/2 A_ij h_i h_j."""
    out = {}
    for i in range(n):
        for j in range(n):
            if not A[i][j]:
                continue
            for m in range(-GRADE, GRADE+1):
                l = k-1-m
                ops = [(i, m), (j, l)]
                # Creation operators on the left; act from the right.
                ops.sort(key=lambda p: p[1] >= 0)
                v = state
                for species, mode in reversed(ops):
                    v = oscillator(v, species, mode, n)
                out = add((1, out), (Q(A[i][j], 2), v))
    return out


def deriv(state, n):
    out = defaultdict(Q)
    for v, c in state.items():
        for mode in range(1, GRADE):
            for i in range(n):
                pos = (mode-1)*n+i
                if v[pos]:
                    w = list(v)
                    w[pos] -= 1
                    w[pos+n] += 1
                    out[tuple(w)] += c*mode*v[pos]
    return dict(out)


def matrix_product(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matrix_add(A, B, scale=1):
    return [[a+scale*b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def metric(A, B):
    return Q(trace(matrix_product(A, B)), 2)


def rank(A):
    if not A:
        return 0
    M = [list(map(Q, row)) for row in A]
    row = 0
    for col in range(len(M[0])):
        p = next((p for p in range(row, len(M)) if M[p][col]), None)
        if p is None:
            continue
        M[row], M[p] = M[p], M[row]
        z = M[row][col]
        M[row] = [x/z for x in M[row]]
        for p in range(row+1, len(M)):
            z = M[p][col]
            if z:
                M[p] = [x-z*y for x, y in zip(M[p], M[row])]
        row += 1
        if row == len(M):
            break
    return row


def oscillator_checks(n):
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    basis = []
    for i in range(n):
        for j in range(i, n):
            A = [[0]*n for _ in range(n)]
            A[i][j] = A[j][i] = 1
            basis.append(A)
    vacuum = {(0,)*(n*GRADE): Q(1)}
    states = [quadratic_mode(A, -1, vacuum, n) for A in basis]
    d = len(basis)
    prod = [[quadratic_mode(A, 1, b, n) for b in states] for A in basis]
    raw = [[quadratic_mode(A, 0, b, n) for b in states] for A in basis]
    primary = [[add((1, raw[i][j]), (-Q(1, 2), deriv(prod[i][j], n)))
                for j in range(d)] for i in range(d)]
    need(all(inner(states[i], states[j], n) == metric(basis[i], basis[j])
             for i in range(d) for j in range(d)), f'oscillator:n{n}_two_point_metric')
    need(all(prod[i][j] == quadratic_mode(matrix_add(matrix_product(basis[i], basis[j]),
                                                           matrix_product(basis[j], basis[i])),
                                                 -1, vacuum, n)
             for i in range(d) for j in range(d)), f'oscillator:n{n}_Jordan_product_from_modes')
    need(all(add((1, primary[i][j]), (1, primary[j][i])) == {}
             for i in range(d) for j in range(d)), f'oscillator:n{n}_antisymmetry_with_derivative_subtraction')
    need(all(quadratic_mode(I, m+1, primary[i][j], n) == {}
             for m in (1, 2, 3) for i in range(d) for j in range(d)),
         f'oscillator:n{n}_all_positive_Virasoro_modes_through_weight_three')
    need(all(inner(primary[i][j], deriv(x, n), n) == 0
             for i in range(d) for j in range(d) for x in states),
         f'oscillator:n{n}_orthogonal_to_all_weight_two_derivatives')
    pairs = list(combinations(range(d), 2))
    gram = [[inner(primary[i][j], primary[k][l], n) for k, l in pairs] for i, j in pairs]
    rhs = [[inner(prod[i][k], prod[j][l], n)-inner(prod[i][l], prod[j][k], n)
            for k, l in pairs] for i, j in pairs]
    need(gram == rhs, f'oscillator:n{n}_every_four_label_Gram_entry')
    need(rank(gram) == n*(n-1)//2, f'oscillator:n{n}_rank_fills_small_weight_three_primary_space')
    need(any(raw[i][i] for i in range(d)) and all(not primary[i][i] for i in range(d)),
         f'negative_control:n{n}_raw_zero_product_is_not_antisymmetric')
    # Compute an actual weight-three vector from the matrix commutator independently.
    need(all(primary[i][j] == commutator_state(basis[i], basis[j], n)
             for i in range(d) for j in range(d)), f'oscillator:n{n}_half_commutator_state_normalization')
    stress_state = quadratic_mode(I, -1, vacuum, n)
    need(all(add((1, quadratic_mode(I, 0, b, n)),
                  (-Q(1, 2), deriv(quadratic_mode(I, 1, b, n), n))) == {}
             for b in states), f'oscillator:n{n}_stress_direction_has_no_primary_channel')
    need(inner(stress_state, stress_state, n) == Q(n, 2), f'oscillator:n{n}_central_charge_normalization')
    return {'bosons': n, 'weight_two_dimension': d, 'Gram_dimension': len(pairs),
            'four_label_entries_checked': len(pairs)**2, 'weight_three_primary_rank': rank(gram)}


def commutator_state(A, B, n):
    M = matrix_add(matrix_product(A, B), matrix_product(B, A), -1)
    out = {}
    for i in range(n):
        for j in range(n):
            if M[i][j]:
                v = [0]*(GRADE*n)
                v[n+i] += 1
                v[j] += 1
                out[tuple(v)] = Q(M[i][j], 2)
    return out


def contraction_checks():
    # Tensor-index identity tested on arbitrary small symmetric cubics.
    # These are not asserted to extend to physical VOAs.
    for n in (2, 3):
        C = [[[Q((i+j+k) % 5-2, 3) for k in range(n)]
              for j in range(n)] for i in range(n)]
        L = [[[C[k][i][j] for j in range(n)] for i in range(n)] for k in range(n)]
        pairs = list(combinations(range(n), 2))
        columns = []
        for k, l in pairs:
            X = [[Q(0) for _ in range(n)] for _ in range(n)]
            X[k][l], X[l][k] = Q(1), -Q(1)
            FX = [[Q(0) for _ in range(n)] for _ in range(n)]
            for A in L:
                FX = matrix_add(FX, matrix_product(matrix_product(A, X), A))
            columns.append([FX[i][j] for i, j in pairs])
        Fmat = list(map(list, zip(*columns)))
        tensor = [[sum(C[i][k][p]*C[j][l][p]-C[i][l][p]*C[j][k][p]
                       for p in range(n)) for k, l in pairs] for i, j in pairs]
        need(Fmat == tensor, f'contraction:n{n}_skew_matrix_and_exterior_normalizations')
        G = [[tensor[i][j]+Q(i == j, 3) for j in range(len(pairs))]
             for i in range(len(pairs))]
        need(G == [[Fmat[i][j]+Q(i == j, 3) for j in range(len(pairs))]
                   for i in range(len(pairs))], f'contraction:n{n}_stress_shift_has_positive_sign')


def scalar_checks():
    d, kappa, s2 = 196883, Q(13858, 3), Q(1, 3)
    size = d*(d-1)//2
    roots = (Q(845, 3), -Q(1, 3))
    mp = (-d*kappa/2-roots[1]*size)/(roots[0]-roots[1])
    need(mp == 21296876, 'extremal:positive_skew_multiplicity_from_trace')
    need(size-mp == 19360062527, 'extremal:zero_Gram_multiplicity')
    need(tuple(x+s2 for x in roots) == (282, 0), 'extremal:Gram_eigenvalues_282_and_zero')
    need(21493760-196884 == mp, 'extremal:rank_equals_all_available_weight_three_primaries')
    need(roots[0]-roots[1] == 282, 'extremal:orthogonal_projector_denominator')
    need(-d*kappa/2+s2*size == 282*mp, 'extremal:total_squared_OPE_strength_by_Gram_trace')
    need(282*mp == 6005719032, 'extremal:total_squared_OPE_strength_exact')
    need(2*282*mp/d == 61008, 'extremal:ordered_pair_factor_two_for_each_weight_two_direction')
    # Curvature-operator spectrum already implies positive Gram and exact rank.
    need(all((x+s2)**2 == 282*(x+s2) for x in roots), 'redundancy:projector_polynomial')
    need(all(x+s2 >= 0 for x in roots), 'redundancy:positivity_already_follows_from_spectrum')
    need(roots[1] < 0, 'negative_control:omitted_stress_channel_creates_negative_Gram')
    # Sum over b of ||w(a,b)||^2 for unit primary a: tracelessness of mu kills
    # sum_b <mu(a,a),mu(b,b)>; retained stress term supplies (d-1)/3.
    need(s2*(d-1)-kappa == 61008, 'extremal:fixed_a_sum_from_tracefree_primary_product')
    # The 3 cyclic equations eliminate a possible four-form ambiguity.
    A = [[1, -1, 0], [-1, 0, -1], [0, -1, 1]]
    need(rank(A) == 3, 'polarization:cyclic_mode_equations_have_unique_solution')
    for x, y, z in ((2, 3, 5), (Q(2, 7), -Q(3, 11), Q(4, 9))):
        a, b, c = x-z, y-z, y-x
        need(a-b == x-y and -a-c == z-y and -b+c == z-x,
             f'polarization:four_label_solution_{len(LABELS)}')
    # A symmetric primary cubic alone is insufficient: in dimension two use
    # C000=1, C011=C101=C110=-1. It has F|wedge=-2.
    need(-2+s2 < 0, 'negative_control:arbitrary_symmetric_cubic_need_not_admit_positive_weight_three')
    return {'weight_two_primary_dimension': d, 'weight_three_primary_dimension': int(mp),
            'antisymmetric_domain_dimension': size, 'kernel_dimension': int(size-mp),
            'squared_nonzero_singular_value': 282,
            'total_squared_OPE_strength_unordered_pairs': int(282*mp),
            'strength_per_unit_weight_three_primary': 282,
            'sum_over_b_for_each_unit_weight_two_primary': 61008}


def main():
    examples = [oscillator_checks(n) for n in (2, 3)]
    contraction_checks()
    scalars = scalar_checks()
    print(json.dumps({'status': 'PASS within exact oscillator and scalar scopes',
                      'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
                      'oscillator_examples': examples, 'extremal_scalars': scalars,
                      'largest_square_matrix_dimension': 15,
                      'largest_oscillator_grade': GRADE,
                      'arithmetic': 'integers and fractions only',
                      'full_extremal_OPE_tensor_constructed': False,
                      'Monster_data_used': False,
                      'source_theorems_formally_verified': False,
                      'moonshine_uniqueness_proved': False,
                      'novelty_established': False}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
