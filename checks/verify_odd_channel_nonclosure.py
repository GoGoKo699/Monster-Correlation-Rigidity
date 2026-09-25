#!/usr/bin/env python3
"""Exact controls and complete dimension-elimination certificate for Note 20.

Cartan classification is an external theorem, not proved by this checker.
The hypothetical symmetric Lie algebra is checked on small sphere/product
controls. The extremal algebra and any full Monster operator are never built.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations, product
from math import isqrt
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
ODD_HEAD = 'fde92a04964def3a12c5a8cc75362c4fced96c73'
LABELS: list[str] = []
MAX_SQUARE = 0


def need(condition, label):
    if not bool(condition):
        raise RuntimeError(label)
    LABELS.append(label)


def zero(n):
    global MAX_SQUARE
    MAX_SQUARE = max(MAX_SQUARE, n)
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = Q(1)
    return out


def add(A, B, factor=1):
    return [[a+factor*b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def scale(A, factor):
    return [[factor*a for a in row] for row in A]


def mul(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def transpose(A):
    return list(map(list, zip(*A)))


def comm(A, B):
    return add(mul(A, B), mul(B, A), -1)


def trace(A):
    return sum((A[i][i] for i in range(len(A))), Q(0))


def half(A, B):
    return -trace(mul(A, B))/2


def apply(A, v):
    return [sum((a*b for a, b in zip(row, v)), Q(0)) for row in A]


def wedge(u, v):
    return [[a*b-c*d for b, d in zip(v, u)] for a, c in zip(u, v)]


def skew_basis(n):
    I = eye(n)
    return [wedge(I[i], I[j]) for i, j in combinations(range(n), 2)]


def sum_matrices(items, n):
    out = zero(n)
    for A in items:
        out = add(out, A)
    return out


def curvature_operator(n, operation):
    basis = skew_basis(n)
    columns = [operation(X) for X in basis]
    out = zero(len(basis))
    for i, A in enumerate(basis):
        for j, B in enumerate(columns):
            out[i][j] = half(A, B)
    return out


def bianchi(n, operation):
    basis = eye(n)
    for u, v, w in product(basis, repeat=3):
        terms = [apply(operation(wedge(u, v)), w),
                 apply(operation(wedge(v, w)), u),
                 apply(operation(wedge(w, u)), v)]
        if any(sum(entries) for entries in zip(*terms)):
            return False
    return True


def ricci(n, operation):
    basis = eye(n)
    return [[sum((half(operation(wedge(a, c)), wedge(b, c)) for c in basis), Q(0))
             for b in basis] for a in basis]


def cubic_controls():
    for n in (2, 3, 4):
        # Fully symmetric, otherwise arbitrary rational cubic. It need not be
        # trace-free, extremal, or realizable as a VOA.
        C = [[[Q((i+j+k+i*j+j*k+k*i) % 7-3, 3) for k in range(n)]
              for j in range(n)] for i in range(n)]
        L = C
        gamma = Q(2, 5)
        def F(X):
            return sum_matrices((mul(mul(A, X), A) for A in L), n)
        def R(X):
            return add(F(X), scale(X, gamma))
        basis = eye(n)
        need(all(F(wedge(a, b)) == comm(L[i], L[j])
                 for i, a in enumerate(basis) for j, b in enumerate(basis)),
             f'cubic:n{n}_commutator_curvature_identification')
        op = curvature_operator(n, R)
        need(op == transpose(op), f'cubic:n{n}_curvature_pair_symmetry')
        need(bianchi(n, R), f'cubic:n{n}_first_Bianchi_all_triples')
        # Ric_F(a,b)=<mu(a,b),sum_i mu(e_i,e_i)>-tr(L_a L_b).
        tau = [sum(C[k][i][i] for i in range(n)) for k in range(n)]
        expected = [[sum(C[i][j][k]*tau[k] for k in range(n))
                     - trace(mul(L[i], L[j])) + gamma*(n-1)*int(i == j)
                     for j in range(n)] for i in range(n)]
        need(ricci(n, R) == expected, f'cubic:n{n}_full_Ricci_formula')
        need(trace(op)*2 == trace(expected), f'cubic:n{n}_scalar_curvature_twice_operator_trace')
    # Trace-free harmonic binary cubic gives the simpler Ricci reduction.
    C = [[[Q(0)]*2 for _ in range(2)] for _ in range(2)]
    C[0][0][0] = 1
    C[0][1][1] = C[1][0][1] = C[1][1][0] = -1
    R = lambda X: add(sum_matrices((mul(mul(A, X), A) for A in C), 2), scale(X, 3))
    need(all(trace(A) == 0 for A in C), 'cubic:harmonic_tracefree')
    need(ricci(2, R) == eye(2), 'cubic:tracefree_Ricci_is_gamma_n_minus_one_minus_kappa')


def symmetric_pair_control(block_sizes):
    n = sum(block_sizes)
    units = eye(n)
    groups = []
    offset = 0
    for size in block_sizes:
        groups.append(set(range(offset, offset+size)))
        offset += size
    edges = [(i, j) for i, j in combinations(range(n), 2)
             if any(i in block and j in block for block in groups)]
    h = [wedge(units[i], units[j]) for i, j in edges]
    p = Q(2)
    def project(X):
        return sum_matrices((scale(A, half(A, X)) for A in h), n)
    def R(X):
        return scale(project(X), p)
    tag = 'x'.join(map(str, block_sizes))
    need(bianchi(n, R), f'symmetric_pair:{tag}_Bianchi')
    need(all(project(comm(A, B)) == comm(A, B) for A in h for B in h),
         f'symmetric_pair:{tag}_image_closed')
    need(all(comm(A, R(X)) == R(comm(A, X)) for A in h for X in skew_basis(n)),
         f'symmetric_pair:{tag}_equivariance_from_projection')
    op = curvature_operator(n, R)
    need(mul(op, op) == scale(op, p), f'symmetric_pair:{tag}_flat_positive_spectrum')
    hs = len(h)
    dimension = hs+n
    def bracket(x, y):
        A = sum_matrices((scale(a, t) for a, t in zip(h, x[:hs])), n)
        B = sum_matrices((scale(b, t) for b, t in zip(h, y[:hs])), n)
        u, v = x[hs:], y[hs:]
        first = add(comm(A, B), R(wedge(u, v)), -1)
        last = [a-b for a, b in zip(apply(A, v), apply(B, u))]
        return [half(a, first) for a in h]+last
    basis = [[Q(i == j) for j in range(dimension)] for i in range(dimension)]
    table = [[bracket(a, b) for b in basis] for a in basis]
    def bracket_basis_vector(i, v):
        return [sum((v[j]*table[i][j][k] for j in range(dimension)), Q(0))
                for k in range(dimension)]
    for i, j, k in product(range(dimension), repeat=3):
        terms = [bracket_basis_vector(i, table[j][k]),
                 bracket_basis_vector(j, table[k][i]),
                 bracket_basis_vector(k, table[i][j])]
        if any(sum(e) for e in zip(*terms)):
            raise RuntimeError('Symmetric-pair Jacobi '+tag)
    need(True, f'symmetric_pair:{tag}_every_Jacobi_basis_triple')
    weights = [1/p]*hs+[Q(1)]*n
    need(all(weights[k]*table[i][j][k] == weights[i]*table[j][k][i]
             for i, j, k in product(range(dimension), repeat=3)),
         f'symmetric_pair:{tag}_positive_invariant_metric_sign')
    Rric = ricci(n, R)
    need(trace(Rric) == 2*p*hs, f'symmetric_pair:{tag}_isotropy_dimension_trace')
    if len(set(block_sizes)) == 1:
        lam = p*(block_sizes[0]-1)
        need(Rric == scale(eye(n), lam), f'symmetric_pair:{tag}_common_Ricci_on_factors')
        need(all(Q(m*(m-1)//2, m) == lam/(2*p) for m in block_sizes),
             f'symmetric_pair:{tag}_factorwise_dimension_ratio')
    return {'tangent_dimension': n, 'isotropy_dimension': hs,
            'Lie_algebra_dimension': dimension, 'blocks': block_sizes,
            'Jacobi_basis_triples': dimension**3}


def negative_control():
    n = 4
    units = eye(n)
    # Four coordinate planes in a cycle: an Einstein algebraic curvature
    # projector that is not a Lie image. Bianchi alone does not imply closure.
    edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
    basis = [wedge(units[i], units[j]) for i, j in edges]
    def R(X):
        return sum_matrices((scale(A, half(A, X)) for A in basis), n)
    need(bianchi(n, R), 'negative:cycle_projector_is_Bianchi')
    need(ricci(n, R) == scale(eye(n), 2), 'negative:cycle_projector_is_Einstein')
    op = curvature_operator(n, R)
    need(mul(op, op) == op, 'negative:cycle_projector_has_flat_positive_spectrum')
    c = comm(basis[0], basis[1])
    need(c != R(c), 'negative:Bianchi_Einstein_projector_need_not_have_Lie_image')


def classification_certificate():
    d = 196883
    lam, p = Q(61008), Q(282)
    ratio = lam/(2*p)
    need(ratio == Q(5084, 47), 'extremal:required_isotropy_to_tangent_ratio')
    need(Q(21296876, d) == ratio, 'extremal:independent_rank_ratio_matches')
    need(ratio > 108, 'classification:large_ratio_threshold')
    # The non-Grassmann classical families and group type have ratio <=2.
    # Store the exact rational formula names; inequalities follow at n>=2.
    simple = {'AI': 'n/(n+2)<1', 'AII': 'n/(n-1)<=2 for n>=2',
              'CI': 'n/(n+1)<1', 'DIII': 'n/(n-1)<=2 for n>=2',
              'group_type': '1'}
    need(Q(2) < ratio, 'classification:all_single_parameter_and_group_types_excluded')
    dims_g = {'G2': 14, 'F4': 52, 'E6': 78, 'E7': 133, 'E8': 248}
    exceptionals = [('G', 'G2', 6), ('FI', 'F4', 24), ('FII', 'F4', 36),
                    ('EI', 'E6', 36), ('EII', 'E6', 38), ('EIII', 'E6', 46), ('EIV', 'E6', 52),
                    ('EV', 'E7', 63), ('EVI', 'E7', 69), ('EVII', 'E7', 79),
                    ('EVIII', 'E8', 120), ('EIX', 'E8', 136)]
    exc = []
    for name, group, h in exceptionals:
        m = dims_g[group]-h
        r = Q(h, m)
        need(r <= Q(9, 4) < ratio, f'classification:exceptional_{name}_excluded')
        exc.append({'family': name, 'tangent_dimension': m, 'isotropy_dimension': h,
                    'ratio': str(r)})
    # For p<=q, ratio>108 implies q/p>215 in BDI/AIII,
    # and q/p>214 in CII. The dimension bound then bounds p.
    # 196883 > c*p^2 is strict. Bounds below exhaust every possibility.
    bounds = [('BDI', 215, 30), ('AIII', 430, 21), ('CII', 856, 15)]
    entries = []
    for family, divisor, bound in bounds:
        need(divisor*bound**2 < d <= divisor*(bound+1)**2,
             f'classification:{family}_rank_bound_{bound}')
        for r in range(1, bound+1):
            if family == 'BDI':
                a, b, c = 47, -(47+10168*r), 47*r*(r-1)
                mfun = lambda q: r*q
                hfun = lambda q: (r*(r-1)+q*(q-1))//2
            elif family == 'AIII':
                a, b, c = 47, -10168*r, 47*(r*r-1)
                mfun = lambda q: 2*r*q
                hfun = lambda q: r*r+q*q-1  # effective S(U(r)U(q)), NOT U(r)U(q)
            else:
                a, b, c = 94, 47-20336*r, 47*(2*r*r+r)
                mfun = lambda q: 4*r*q
                hfun = lambda q: r*(2*r+1)+q*(2*q+1)
            disc = b*b-4*a*c
            root = isqrt(disc)
            rational_roots = []
            if root*root == disc:
                rational_roots = sorted(set([Q(-b-root, 2*a), Q(-b+root, 2*a)]))
            admitted = [int(q) for q in rational_roots
                        if q.denominator == 1 and q >= r and mfun(int(q)) <= d]
            need(not admitted, f'classification:{family}_p{r}_no_admissible_root')
            # An independent substitution confirms that the quadratic is the
            # cleared dimension-ratio equation, on sample integer arguments.
            multiplier = 2 if family == 'BDI' else 1
            if any(a*q*q+b*q+c != multiplier*(47*hfun(q)-5084*mfun(q))
                   for q in (r, r+1, 217*r)):
                raise RuntimeError('Wrong classification quadratic '+family)
            entries.append({'family': family, 'p': r, 'quadratic': [a, b, c],
                            'discriminant': disc, 'floor_sqrt': root,
                            'is_square': root*root == disc,
                            'rational_roots_when_square': list(map(str, rational_roots)),
                            'admissible_integer_roots': admitted})
    need(len(entries) == 66, 'classification:all_66_remaining_quadratics_excluded')
    need(sum(e['is_square'] for e in entries) == 2, 'classification:only_two_square_discriminants_both_excluded')
    return {'max_factor_tangent_dimension': d, 'required_ratio': str(ratio),
            'single_parameter_bounds': simple, 'exceptional_dimension_table': exc,
            'rank_bounds': [{'family': f, 'p_max': b, 'dimension_lower_bound_coefficient': c}
                           for f, c, b in bounds],
            'quadratic_certificate': entries, 'Cartan_classification_proved_by_checker': False}


def known_example():
    # Orthogonal oscillator pair, with [A,B] of unit half-Frobenius norm.
    units = eye(3)
    A, B = wedge(units[0], units[1]), wedge(units[1], units[2])
    C = comm(A, B)
    need(half(A, A) == half(B, B) == half(C, C) == 1, 'witness:three_unit_skew_matrices')
    # Check the Sym^2 representation trace index at n=3 explicitly.
    sym = []
    for i in range(3):
        X = zero(3); X[i][i] = 1; sym.append(X)
    for i, j in combinations(range(3), 2):
        X = zero(3); X[i][j] = X[j][i] = 1; sym.append(X)
    positions = [(i, i) for i in range(3)]+list(combinations(range(3), 2))
    columns = [comm(C, X) for X in sym]
    action = [[Y[i][j] for Y in columns] for i, j in positions]
    need(trace(mul(action, action)) == (3+2)*trace(mul(C, C)),
         'witness:explicit_small_symmetric_square_index')
    # Full n=24 trace is symbolic. The identity direction is killed.
    total = Q(24+2)+Q(4096, 16**2)
    projected = Q(15, 47)**2*(Q(24+2)+Q(4096, 4**2))
    missing = total-projected
    need(total == 42, 'witness:full_commutator_squared_norm')
    need(projected == Q(1350, 47), 'witness:weight_three_projection_squared_norm')
    need(missing == Q(624, 47), 'witness:weight_five_zero_mode_squared_norm_positive')
    need(missing/2 == Q(312, 47), 'witness:weight_five_primary_coupling_squared_norm')
    # Independent difference of the two explicit block actions.
    blockdiff = (24+2)*(1-Q(15,47))**2+4096*(Q(1,16)-Q(15,47*4))**2
    need(blockdiff == missing, 'witness:direct_complement_block_difference_agrees')
    return {'example_only_not_universal_lower_bound': True,
            'full_commutator_squared_norm': str(total),
            'weight_three_component_squared_norm': str(projected),
            'weight_five_component_squared_norm': str(missing),
            'physical_weight_five_primary_squared_norm': str(missing/2)}


def main():
    cubic_controls()
    small = [symmetric_pair_control(s) for s in ([3], [3, 3])]
    negative_control()
    need(Q(1,3)*(196883-1)-Q(13858,3) == 61008, 'extremal:Ricci_coefficient')
    need(2*282*21296876 == 61008*196883, 'extremal:curvature_trace_rank_consistency')
    classification = classification_certificate()
    witness = known_example()
    print(json.dumps({'status': 'PASS within exact curvature and classification-arithmetic scopes',
                      'base_commit': BASE, 'odd_mode_dependency_head': ODD_HEAD,
                      'checks': len(LABELS), 'labels': LABELS,
                      'small_symmetric_pair_controls': small,
                      'classification_certificate': classification,
                      'known_moonshine_example': witness,
                      'arithmetic': 'integers and fractions only',
                      'largest_square_matrix_dimension': MAX_SQUARE,
                      'full_extremal_tensor_constructed': False,
                      'Cartan_classification_independently_proved': False,
                      'pending_PR17_derivation_fully_audited': False,
                      'every_primary_pair_has_nonzero_weight_five_component': False,
                      'primary_three_bracket_Jacobi_failure_proved': False,
                      'new_independent_selection_axiom': False,
                      'prior_operator_identity_independence_settled': False,
                      'Monster_uniqueness_proved': False}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
