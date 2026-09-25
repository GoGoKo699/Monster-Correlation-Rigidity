#!/usr/bin/env python3
"""Exact, bounded verification of mixed-response closure.

The reduction itself is proved by index contraction in the accompanying note.
These controls use small symmetric cubics, NOT holomorphic c=24 CFTs.
No fourth/fifth trace table, Monster data, floating point, or network is used.
All tests use explicit exceptions and remain active under -O and -OO.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations, permutations
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []
MAX_SQUARE = 0


def need(ok: bool, label: str) -> None:
    if not bool(ok):
        raise RuntimeError('Check failed: '+label)
    LABELS.append(label)


def zeros(n: int):
    global MAX_SQUARE
    MAX_SQUARE = max(MAX_SQUARE, n)
    return [[0]*n for _ in range(n)]


def eye(n: int):
    out = zeros(n)
    for i in range(n):
        out[i][i] = 1
    return out


def scale(A, x):
    return [[x*a for a in row] for row in A]


def add(A, B):
    return [[a+b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def mm(A, B):
    n = len(A)
    out = zeros(n)
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j, b in enumerate(B[k]):
                    if b:
                        out[i][j] += a*b
    return out


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def word(*matrices):
    out = eye(len(matrices[0]))
    for matrix in matrices:
        out = mm(out, matrix)
    return out


def total(matrices, n: int):
    out = zeros(n)
    for matrix in matrices:
        out = add(out, matrix)
    return out


def wedge_operator(n: int, operation):
    """Unit e_i wedge e_j is Eij-Eji with half-Frobenius metric."""
    pairs = list(combinations(range(n), 2))
    out = zeros(len(pairs))
    for col, (i, j) in enumerate(pairs):
        X = zeros(n)
        X[i][j], X[j][i] = 1, -1
        Y = operation(X)
        for row, (a, b) in enumerate(pairs):
            out[row][col] = Y[a][b]
    return out


def tensor(n: int, kind: str, factor=1):
    C = [[[0]*n for _ in range(n)] for _ in range(n)]
    if kind == 'xyz':
        if n % 3:
            raise ValueError('xyz blocks require dimension divisible by three')
        for b in range(n//3):
            for i, j, k in permutations(range(3*b, 3*b+3)):
                C[i][j][k] = factor
    elif kind == 'harmonic2':
        if n % 2:
            raise ValueError('harmonic blocks require even dimension')
        for b in range(n//2):
            i, j = 2*b, 2*b+1
            C[i][i][i] = factor
            for a, b, c in set(permutations((i, j, j))):
                C[a][b][c] = -factor
    elif kind == 'arbitrary':
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j][k] = Q((i+j+k+i*j+j*k+i*k) % 7-3, 3)
    else:
        raise ValueError('Unknown tensor family')
    return C


def operators(L):
    n = len(L)
    def F(X):
        return total((word(A, X, A) for A in L), n)
    Fw = wedge_operator(n, F)
    Ds = [wedge_operator(n, lambda X, A=A: add(mm(A, X), mm(X, A))) for A in L]
    return F, Fw, Ds


def trace_controls(n: int, kind: str, factor, kappa, nu):
    C = tensor(n, kind, factor)
    L = C
    prefix = f'algebra:d{n}_{kind}_scale{factor}'
    need(all(C[i][j][k] == C[k][i][j] == C[j][i][k]
             for i in range(n) for j in range(n) for k in range(n)), prefix+':full_cubic_symmetry')
    need(all(tr(A) == 0 for A in L), prefix+':tracefree')
    need(all(tr(mm(A, B)) == kappa*int(i == j)
             for i, A in enumerate(L) for j, B in enumerate(L)), prefix+':quadratic_identity')
    need(all(tr(word(A, B, D)) == nu*C[i][j][k]
             for i, A in enumerate(L) for j, B in enumerate(L) for k, D in enumerate(L)),
         prefix+':cubic_trace_identity')
    F, Fw, Ds = operators(L)
    m = len(Fw)
    need(total((mm(A, A) for A in L), n) == scale(eye(n), kappa), prefix+':sum_L_squared')
    need(all(F(A) == scale(A, nu) for A in L), prefix+':F_on_multiplication_operators')
    for label, direct, expected in (
        ('U0', lambda De, Df: tr(mm(De, Df)), (n-2)*kappa),
        ('U1', lambda De, Df: tr(word(Fw, De, Df)), -kappa*nu),
        ('U2', lambda De, Df: tr(word(Fw, De, Fw, Df)), kappa*nu*(kappa-nu))):
        need(all(direct(De, Df) == expected*int(i == j)
                 for i, De in enumerate(Ds) for j, Df in enumerate(Ds)), prefix+':'+label+'_all_basis_pairs')
    # Verify both six-matrix swap traces separately, not merely their difference.
    for label, order in (
        ('Z1', lambda Mi, Mj, A, B: (Mi, A, Mj, B, Mi, Mj)),
        ('Z2', lambda Mi, Mj, A, B: (Mi, A, Mj, Mi, Mj, B))):
        need(all(sum(tr(word(*order(Mi, Mj, A, B))) for Mi in L for Mj in L)
                 == kappa*nu*nu*int(a == b)
                 for a, A in enumerate(L) for b, B in enumerate(L)), prefix+':'+label+'_all_basis_pairs')
    for gamma in (0, Q(1, 3), Q(1), Q(2)):
        G = add(Fw, scale(eye(m), gamma))
        coeff = kappa*(nu*(kappa-nu-2*gamma)+gamma*gamma*(n-2))
        need(all(tr(word(G, De, G, Df)) == coeff*int(i == j)
                 for i, De in enumerate(Ds) for j, Df in enumerate(Ds)), prefix+f':full_shifted_trace_gamma{gamma}')
    need(total((mm(D, D) for D in Ds), m) == add(scale(eye(m), 2*kappa), scale(Fw, 2)),
         prefix+':sum_D_squared_operator')
    need(total((word(D, Fw, D) for D in Ds), m) == scale(Fw, 2*nu),
         prefix+':sandwiched_F_operator')
    return {'dimension': n, 'family': kind, 'scale': str(factor),
            'kappa': str(kappa), 'nu': str(nu), 'exterior_dimension': m,
            'is_extremal_VOA': False}


def crossed_contraction_controls():
    for n in (2, 3, 4):
        C = tensor(n, 'arbitrary')
        L = C
        F, Fw, Ds = operators(L)
        R = wedge_operator(n, lambda X: total((word(A, B, X, A, B) for A in L for B in L), n))
        need(R == zeros(len(R)), f'crossing:d{n}_full_symmetry_kills_crossed_skew_operator')
        rhs = wedge_operator(n, lambda X: total(
            (add(word(F(A), X, A), word(A, X, F(A))) for A in L), n))
        need(total((word(D, Fw, D) for D in Ds), len(Fw)) == rhs,
             f'crossing:d{n}_operator_expansion_before_isotropy')
        # Direct index check for the triangle contraction used in the proof.
        need(all(sum(C[i][a][b]*C[i][e][f]*C[j][f][a]
                     for i in range(n) for a in range(n) for f in range(n))
                 == tr(word(L[b], L[e], L[j]))
                 for b in range(n) for e in range(n) for j in range(n)),
             f'crossing:d{n}_triangle_index_identity')
    # A list of symmetric matrices without full cubic symmetry is insufficient.
    L = [eye(2), eye(2)]
    R = wedge_operator(2, lambda X: total((word(A, B, X, A, B) for A in L for B in L), 2))
    need(R != zeros(1), 'negative:matrix_symmetry_alone_does_not_kill_crossed_term')


def projected_operator_controls():
    for n, kind, gamma, p, beta, denom, kappa, nu in (
        (6, 'xyz', Q(1), Q(1), Q(0), Q(1), Q(2), Q(1)),
        (4, 'harmonic2', Q(2), Q(2), Q(0), Q(3), Q(2), Q(0))):
        L = tensor(n, kind)
        F, Fw, Ds = operators(L)
        m = len(Fw)
        G = add(Fw, scale(eye(m), gamma))
        Pi = scale(G, 1/p)
        need(mm(Pi, Pi) == Pi, f'projected:d{n}_genuine_nontrivial_projector')
        need(0 < tr(Pi) < m, f'projected:d{n}_both_range_and_kernel_present')
        H = [scale(word(Pi, D, Pi), p/denom) for D in Ds]
        coeff = (2*p/(denom*denom))*((nu+gamma)*beta+gamma*kappa)
        need(total((mm(h, h) for h in H), m) == scale(Pi, coeff),
             f'projected:d{n}_operator_sum_of_squares_on_entire_range')
        K = kappa*(nu*(kappa-nu-2*gamma)+gamma*gamma*(n-2))/(denom*denom)
        need(all(tr(mm(x, y)) == K*int(i == j) for i, x in enumerate(H) for j, y in enumerate(H)),
             f'projected:d{n}_physical_normalization_trace_formula')
        need(n*K == coeff*tr(Pi), f'projected:d{n}_two_sides_total_strength_match')
        need(all(tr(h) == 0 for h in H), f'projected:d{n}_linear_trace_zero')
    # A harmonic tensor with a decoupled extra direction is not isotropic.
    C = [[[0]*3 for _ in range(3)] for _ in range(3)]
    h = tensor(2, 'harmonic2')
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j][k] = h[i][j][k]
    _, Fw, Ds = operators(C)
    G = add(Fw, eye(len(Fw)))
    norms = [tr(word(G, D, G, D)) for D in Ds]
    need(norms[2] == 0 and norms[0] != 0,
         'negative:arbitrary_harmonic_cubic_is_not_an_extremal_countermodel')


def extremal_scalars():
    d, kappa, nu, gamma = 196883, Q(13858, 3), Q(899), Q(1, 3)
    p, beta, denom, dim3 = Q(282), Q(845, 3), Q(104), 21296876
    U0 = (d-2)*kappa
    U1 = -kappa*nu
    U2 = kappa*nu*(kappa-nu)
    total_trace = U2+2*gamma*U1+gamma*gamma*U0
    need(U0 == 909458966, 'physical:U0')
    need(U1 == -Q(12458342, 3), 'physical:U1')
    need(U2 == Q(139047555062, 9), 'physical:U2')
    need(total_trace == 15548010816, 'physical:repeated_action_target_follows_from_degree_three')
    coeff_H = total_trace/(denom*denom)
    need(coeff_H == 1437501, 'physical:compressed_bilinear_trace_coefficient')
    # Independent value from Matsuo Theorem 5.1(2), followed by the already
    # established descendant subtraction; the general trace formula is input.
    central, dim2, dimV3 = 24, 196884, 21493760
    full_trace = -Q(2)*(20*central*central+40*central*dim2+(3*central-198)*dimV3)/(central*(5*central+22))
    need(full_trace == 1478400, 'physical:full_weight_three_trace_from_source_formula')
    need(full_trace-Q(9,4)*4620-Q(1,2)*61008 == coeff_H,
         'physical:independent_descendant_subtraction_agrees')
    coeff_operator = 2*p*((nu+gamma)*beta+gamma*kappa)/(denom*denom)
    need(coeff_operator == Q(53157, 4), 'physical:operator_sum_of_squares_coefficient')
    need(d*coeff_H == dim3*coeff_operator, 'physical:trace_of_operator_identity_matches_bilinear_trace')
    need(coeff_H/Q(dim3) == Q(1131, 16756), 'physical:microcanonical_primary_average')
    need(dim3 == 21493760-196884, 'physical:weight_three_primary_dimension')
    return {'d': d, 'kappa': str(kappa), 'nu': str(nu), 'shift': str(gamma),
            'U0': str(U0), 'U1': str(U1), 'U2': str(U2),
            'repeated_action_trace_coefficient': str(total_trace),
            'primary_action_bilinear_trace': str(coeff_H),
            'sum_primary_actions_squared': str(coeff_operator),
            'primary_three_dimension': dim3,
            'averaged_primary_bilinear_trace': '1131/16756',
            'fourth_or_fifth_trace_needed_for_scalar_reduction': False}


def main():
    examples = []
    for n, kind, factor, kappa, nu in (
        (2, 'harmonic2', Q(1), Q(2), Q(0)),
        (3, 'xyz', Q(1), Q(2), Q(1)),
        (4, 'harmonic2', Q(1), Q(2), Q(0)),
        (6, 'xyz', Q(1), Q(2), Q(1)),
        (3, 'xyz', -Q(3, 2), Q(9, 2), Q(9, 4))):
        examples.append(trace_controls(n, kind, factor, kappa, nu))
    crossed_contraction_controls()
    projected_operator_controls()
    scalars = extremal_scalars()
    print(json.dumps({'status': 'PASS within exact cubic-contraction scopes',
                      'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
                      'examples': examples, 'extremal_scalars': scalars,
                      'arithmetic': 'integers and fractions only',
                      'largest_square_matrix_dimension': MAX_SQUARE,
                      'Monster_data_used': False, 'full_extremal_tensor_constructed': False,
                      'small_algebras_claimed_to_be_CFTs': False,
                      'new_independent_selection_condition_found': False,
                      'moonshine_uniqueness_proved': False,
                      'formal_verification_or_independent_review': False},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
