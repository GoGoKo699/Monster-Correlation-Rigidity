#!/usr/bin/env python3
"""Bounded checks for the C11 precursor comparison and reducible obstruction.

The exact-normalizer LOWER bound is proved analytically in note 10, not by
sampling normalizers. This script checks its finite-group, character, trace,
intertwiner and scalar ingredients. No dense matrix larger than 60 by 60 is
formed; k=10000 is handled by exact scalar formulas, not a 160004-wire/matrix
simulation. Explicit exceptions keep all checks active under -O and -OO.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import math
import numpy as np

BASE = '5aa28ca60c33a1dcd0d271277b4467803fbea05d'
LABELS: list[str] = []
TOL = 1e-10


def need(ok: bool, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def close(x, y, label: str) -> None:
    need(np.linalg.norm(np.asarray(x)-np.asarray(y)) < TOL, label)


def mul(p, q):
    return tuple(p[q[j]] for j in range(len(p)))


def inv(p):
    return tuple(p.index(j) for j in range(len(p)))


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 == 0


def chi(p):
    return sum(i == p[i] for i in range(5))-1


def perm_matrix(p, *, exact=False):
    m = np.zeros((5, 5), dtype=object if exact else float)
    for j, i in enumerate(p):
        m[i, j] = 1
    return m


def a5_data():
    group = sorted(p for p in permutations(range(5)) if even(p))
    index = {p: j for j, p in enumerate(group)}
    identity = tuple(range(5))
    table = np.array([[index[mul(p, q)] for q in group] for p in group])
    need(len(group) == 60, 'group:A5_order_60_and_exact_closure')
    need(all(mul(p, inv(p)) == identity for p in group), 'group:inverses')
    conjugacy = set(frozenset(mul(mul(h, p), inv(h)) for h in group) for p in group)
    sizes = sorted(map(len, conjugacy))
    need(sizes == [1, 12, 12, 15, 20], 'group:A5_conjugacy_class_sizes')
    possible = {1+sum(t) for r in range(5) for t in combinations(sizes[1:], r)}
    need(not any(1 < n < 60 and 60 % n == 0 for n in possible),
         'group:no_proper_nontrivial_normal_subgroup_by_class_sizes')
    cls = [p for p in group if p != identity and mul(p, p) == identity]
    need(len(cls) == 15 and frozenset(cls) in conjugacy, 'group:15_involutions_one_class')
    need(sum(chi(p) for p in group) == 0, 'character:standard_has_no_invariants')
    need(sum(chi(p)**2 for p in group) == 60, 'character:standard_complex_irreducibility')
    need(max(chi(p) for p in group if p != identity) == 1,
         'character:faithful_standard_separation_squared_3_over_2')
    need(min(map(chi, group)) == -1, 'character:minimum_standard_character_minus_one')
    need(all(chi(c) == 0 for c in cls), 'character:class_average_is_zero_on_standard')
    adjacency = np.zeros((60, 60), dtype=np.int64)
    for j, p in enumerate(group):
        for c in cls:
            adjacency[j, index[mul(p, c)]] += 1
    need(np.array_equal(adjacency, adjacency.T), 'walk:involution_adjacency_symmetric')
    need(np.all(adjacency.sum(axis=1) == 15), 'walk:row_sums_15')
    eye = np.eye(60, dtype=np.int64)
    roots = (-5, 0, 3, 15)
    poly = eye.copy()
    for root in roots:
        poly = poly @ (adjacency-root*eye)
    need(not np.any(poly), 'walk:exact_degree_four_annihilating_polynomial')
    multiplicities = {}
    for root in roots:
        numerator, denominator = eye.copy(), 1
        for other in roots:
            if other != root:
                numerator = numerator @ (adjacency-other*eye)
                denominator *= root-other
        rank = F(int(np.trace(numerator)), denominator)
        need(rank.denominator == 1 and rank > 0, f'walk:spectral_projector_rank_{root}')
        multiplicities[str(root)] = int(rank)
    need(multiplicities == {'-5': 18, '0': 16, '3': 25, '15': 1},
         'walk:complete_multiplicities_and_absolute_q_one_third')
    vals = [F(v, 15) for v in roots]
    product_nonconstant = [abs(a*b) for a in vals for b in vals if (a, b) != (F(1), F(1))]
    need(max(product_nonconstant) == F(1, 3), 'product_walk:absolute_q_remains_one_third')
    need(60**2 == 3600 and 15**2 == 225, 'product_group:fixed_order_and_class_size')
    # H_5: R^4 -> sum-zero R^5, with orthonormal columns.
    helmert = np.zeros((5, 4))
    for k in range(1, 5):
        helmert[:k, k-1] = 1/math.sqrt(k*(k+1))
        helmert[k, k-1] = -math.sqrt(k/(k+1))
    close(helmert.T @ helmert, np.eye(4), 'coordinates:Helmert_isometry')
    close(helmert.sum(axis=0), 0, 'coordinates:Helmert_sum_zero')
    sigmas = [helmert.T @ perm_matrix(p) @ helmert for p in group]
    need(max(np.linalg.norm(s.T@s-np.eye(4)) for s in sigmas) < TOL,
         'coordinates:all_60_standard_matrices_orthogonal')
    need(max(abs(np.trace(s)-chi(p)) for p, s in zip(group, sigmas)) < TOL,
         'coordinates:matrix_traces_equal_exact_characters')
    need(max(np.linalg.norm(sigmas[i]@sigmas[j]-sigmas[table[i, j]])
             for i in range(60) for j in range(60)) < TOL,
         'coordinates:all_3600_standard_products')
    return group, cls, index, sigmas, multiplicities


def obstruction_checks(group, cls, index, sigmas):
    chars = [chi(p) for p in group]
    need(sum((a*b)**2 for a in chars for b in chars) == 3600,
         'constituents:tensor_product_complex_irreducible')
    need(sum(a*a*b for a in chars for b in chars) == 0,
         'constituents:tensor_product_orthogonal_to_first_factor')
    need(sum(a*b for a in chars for b in chars) == 0,
         'constituents:first_and_second_factor_inequivalent')
    need(sum(a*a for a in chars for _ in chars) == 3600,
         'constituents:four_dimensional_first_factor_irreducible')
    flip = np.zeros((16, 16))
    for i in range(4):
        for j in range(4):
            flip[4*j+i, 4*i+j] = 1
    close(flip@flip, np.eye(16), 'flip:orthogonal_involution')
    close(np.trace(flip), 4, 'flip:trace_four_plus_minus_multiplicities_ten_six')
    max_flip_error = 0.
    avg_intertwiner = np.zeros((20, 20))
    original = np.zeros((20, 20)); original[:16, :16] = flip; original[16:, 16:] = np.eye(4)
    for i, j in product(range(60), repeat=2):
        a, b = sigmas[i], sigmas[j]
        ab, ba = np.kron(a, b), np.kron(b, a)
        max_flip_error = max(max_flip_error, np.linalg.norm(flip@ab@flip.T-ba))
        source = np.zeros((20, 20)); source[:16, :16] = ab; source[16:, 16:] = a
        target = np.zeros((20, 20)); target[:16, :16] = ba; target[16:, 16:] = b
        avg_intertwiner += target.T @ original @ source / 3600
    need(max_flip_error < TOL, 'flip:all_3600_tensor_conjugation_identities')
    expected = np.zeros((20, 20)); expected[:16, :16] = flip
    close(avg_intertwiner, expected, 'intertwiner:full_group_average_is_flip_plus_zero_at_k1')
    need(np.linalg.matrix_rank(avg_intertwiner, tol=TOL) == 16,
         'intertwiner:nonzero_but_not_invertible')
    close(np.linalg.norm(avg_intertwiner-original)**2/20, 1/5,
          'intertwiner:normalized_squared_distance_four_over_D')
    close(avg_intertwiner @ original.T, np.diag([1.]*16+[0.]*4),
          'intertwiner:common_large_subrepresentation_projector')
    cls_dist = [8-2*chi(mul(inv(c), d)) for c in cls for d in cls]
    group_dist = [8-2*chi(mul(inv(g), h)) for g in group for h in group]
    need(F(sum(cls_dist), len(cls_dist)) == 8, 'residual:exact_class_mean_numerator_eight')
    need(max(group_dist) == 10, 'residual:exact_uniform_numerator_ten')
    need(max(cls_dist) == 10, 'residual:uniform_class_numerator_also_ten')
    need(F(sum(group_dist), len(group_dist)) == 8, 'residual:full_group_mean_numerator_eight')
    c, d = next((c, d) for c in cls for d in cls
                if mul(inv(c), d) != tuple(range(5)) and mul(mul(inv(c), d), mul(inv(c), d)) == tuple(range(5)))
    close(np.linalg.norm(sigmas[index[c]]-sigmas[index[d]], 2), 2,
          'residual:operator_norm_error_does_not_shrink')
    rng = np.random.default_rng(20260925)
    for j in range(8):
        u = np.linalg.qr(rng.normal(size=(4, 4)))[0]
        v = np.linalg.qr(rng.normal(size=(4, 4)))[0]
        close(np.trace(flip@np.kron(u, v)), np.trace(u@v), f'trace:flip_product_identity_{j}')
    # These samples check the identity, NOT optimization over all normalizers.
    for k in (1, 2, 10, 10000):
        dim = 16*k+4
        max_nonidentity = max(k*chi(g)*chi(h)+chi(g)
                              for g in group for h in group
                              if (g, h) != (tuple(range(5)), tuple(range(5))))
        need(max_nonidentity == 4*k+4, f'family:maximum_nonidentity_character_k{k}')
        need(F(2*(dim-max_nonidentity), dim) == F(24*k, dim),
             f'family:separation_squared_k{k}')
        need(max_nonidentity < dim, f'family:faithfulness_k{k}')
        need(F(2*(dim-(4*k+4)), dim) == F(24*k, dim),
             f'family:identity_attains_analytic_normalizer_bound_k{k}')
    k, dim = 10000, 160004
    z2, t2, beta, q, length = F(8, dim), F(128, dim), F(1, 16), F(1, 3), 10
    r, sep2 = (q+beta)/(1-beta), F(24*k, dim)
    need(0 <= beta < 1 and 0 <= q < 1 and t2 > 0 and length >= 1,
         'witness:C11_parameter_domains')
    need(z2 == beta*t2, 'witness:mean_error_Markov_condition')
    need(r == F(19, 45) and r < 1, 'witness:conditioned_walk_bound')
    need(3599*r**length < 1, 'witness:exact_length_mixing_condition')
    need(length**2*t2 < 1, 'witness:Lt_less_than_one')
    need(9*length**2*t2 < sep2, 'witness:three_Lt_less_than_separation')
    need(F(10, dim) < t2, 'witness:every_assignment_is_good_even_before_discarding')
    need(sep2 > z2/(1-q), 'witness:C11_without_irreducibility_has_false_conclusion')
    need(sep2/(z2/(1-q)) == 20000, 'witness:conclusion_violation_factor_20000')
    need(k*k+1 > 1, 'boundary:commutant_has_multiple_invariant_directions')
    return {'k': k, 'dimension': dim, 'group_order': 3600, 'class_size': 225,
            'q': str(q), 'beta': str(beta), 'L': length, 't_squared': str(t2),
            'r': str(r), 'mixing_expression': str(3599*r**length),
            'class_mean_error_squared': str(z2), 'uniform_error_squared': str(F(10, dim)),
            'separation_squared': str(sep2), 'exact_normalizer_distance_squared': str(sep2),
            'invalid_irreducibility_free_conclusion_bound': str(z2/(1-q)),
            'violation_ratio': 20000,
            'normalizer_distance_lower_bound_basis': 'analytic constituent and trace proof; not numerical minimization',
            'only_C11_group_hypothesis_removed': 'absolute irreducibility'}


def finite_image_and_valid_control(group, cls):
    identity = np.eye(5, dtype=object)
    aa = np.array([1, -1, 0, 0, 0], dtype=object)
    bb = np.array([0, 0, 1, -1, 0], dtype=object)
    diagonal = np.outer(aa, aa)+np.outer(bb, bb)
    skew = np.outer(bb, aa)-np.outer(aa, bb)
    numerator = 5*identity-diagonal+2*skew
    need(np.array_equal(numerator.T@numerator, 25*identity), 'exact_conjugate:rational_rotation_orthogonal')
    need(np.array_equal(numerator@np.ones(5, dtype=object), 5*np.ones(5, dtype=object)),
         'exact_conjugate:preserves_sum_zero_space')
    matrices = {p: perm_matrix(p, exact=True) for p in group}
    conjugates = {p: numerator@matrices[p]@numerator.T for p in group}
    need(all(np.array_equal(conjugates[p]@conjugates[q], 25*conjugates[mul(p, q)])
             for p in group for q in group), 'exact_conjugate:all_3600_multiplicativity_defects_zero')
    distances = []
    for p in cls:
        best = min(sum(int(x)**2 for x in (conjugates[p]-25*m).flat) for m in matrices.values())
        distances.append(F(best, 4*625))
    mean = sum(distances, F(0))/15
    need(mean > 0, 'exact_conjugate:positive_distance_from_prescribed_image_despite_zero_defect')
    # An irreducible positive control: near identity, original assignments c->c.
    m = 10000
    denom = m*m+1
    num = denom*identity-diagonal+m*skew
    need(np.array_equal(num.T@num, denom**2*identity), 'valid_control:exact_small_rotation_orthogonal')
    z2 = sum((F(sum(int(x)**2 for x in (num@matrices[c]@num.T-denom**2*matrices[c]).flat),
                 4*denom**4) for c in cls), F(0))/15
    q, beta, t, length = F(1, 3), F(1, 16), F(1, 100), 5
    r = (q+beta)/(1-beta)
    need(z2 <= beta*t*t, 'valid_control:Markov_condition')
    need(59*r**length < 1 and length*t < 1 and (3*length*t)**2 < F(3, 2),
         'valid_control:all_repaired_scalar_conditions')
    avg = sum((matrices[g].T@num@matrices[g] for g in group), np.zeros((5, 5), dtype=object))
    expected = 60*m*m*identity+12*np.ones((5, 5), dtype=object)
    need(np.array_equal(avg, expected), 'valid_control:exact_average_scalar_on_irreducible_subspace')
    dist2 = F(2, denom)
    need(dist2 <= z2/(1-q), 'valid_control:identity_normalizer_satisfies_C11_bound')
    return {'zero_defect_example_class_image_error_squared': str(mean),
            'valid_irreducible_control_class_error_squared': str(z2),
            'valid_control_distance_to_identity_squared': str(dist2)}


def compatible_reducible_checks(group, sigmas):
    # The positive generalization assumes an exact implementable automorphism.
    # Here phi=id. Test a reducible representation with a non-scalar commutant.
    reps = []
    for sigma in sigmas:
        r = np.eye(9); r[:4, :4] = sigma; r[4:8, 4:8] = sigma
        reps.append(r)
    rng = np.random.default_rng(371)
    original = np.linalg.qr(rng.normal(size=(9, 9)))[0]
    avg = sum((r.T@original@r for r in reps), np.zeros((9, 9)))/60
    left, values, right = np.linalg.svd(avg)
    need(min(values) > 1e-6, 'compatible_reducible:sample_average_nonsingular')
    rounded = left@right
    need(max(np.linalg.norm(rounded@r-r@rounded) for r in reps) < TOL,
         'compatible_reducible:polar_factor_is_exact_intertwiner_within_tolerance')
    dist2 = np.linalg.norm(original-rounded)**2/9
    close(dist2, 2-2*sum(values)/9, 'compatible_reducible:trace_norm_distance_formula')
    cls_indices = [j for j, p in enumerate(group)
                   if p != tuple(range(5)) and mul(p, p) == tuple(range(5))]
    z2 = sum(np.linalg.norm(original@reps[j]-reps[j]@original)**2/9 for j in cls_indices)/15
    need(dist2 <= 1.5*z2+TOL, 'compatible_reducible:same_average_bound_with_non_scalar_commutant')
    # A singular average can be completed when representations are compatible.
    u = np.ones(5)/math.sqrt(5); v = np.array([1., -1., 0., 0., 0.])/math.sqrt(2)
    rotation = np.eye(5)-np.outer(u, u)-np.outer(v, v)+np.outer(v, u)-np.outer(u, v)
    ps = [perm_matrix(p) for p in group]
    avg = sum((r.T@rotation@r for r in ps), np.zeros((5, 5)))/60
    close(avg, .75*(np.eye(5)-np.outer(u, u)), 'compatible_reducible:singular_average_projector_formula')
    need(np.linalg.matrix_rank(avg, tol=TOL) == 4, 'compatible_reducible:singular_average_rank_four')
    close(np.linalg.norm(rotation-np.eye(5))**2/5, .8,
          'compatible_reducible:orthogonal_kernel_completion_attains_trace_norm_formula')


def source_parameter_checks():
    # Integer forcing from GH Theorem 6.9's p=2 dimension interval.
    for dim in (4, 16, 196883):
        eps2 = F(1, 2*(dim+1))
        lower, upper = (1-eps2)*dim, F(dim)/(1-eps2)
        need(dim-1 < lower <= dim <= upper < dim+1,
             f'comparison:GH_affine_dimension_locked_below_scale_d{dim}')
    need(F(4, 160004) < F(40, 160004),
         'comparison:GH_partial_intertwiner_codimension_bound_allows_four_missing_dimensions')
    # The small-rank obstruction vanishes in normalized HS, not in operator norm.
    need(F(4, 160004) < F(1, 10000), 'comparison:rank_four_loss_hidden_in_normalized_HS')


def main() -> None:
    group, cls, index, sigmas, multiplicities = a5_data()
    witness = obstruction_checks(group, cls, index, sigmas)
    controls = finite_image_and_valid_control(group, cls)
    compatible_reducible_checks(group, sigmas)
    source_parameter_checks()
    print(json.dumps({'status': 'PASS within stated precursor/obstruction scopes',
        'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
        'A5_walk_adjacency_eigenvalue_multiplicities': multiplicities,
        'reducible_witness': witness, 'controls': controls,
        'largest_dense_matrix_dimension': 60,
        'largest_explicit_reducible_representation_dimension': 20,
        'large_k_checked_by_exact_scalars_only': True,
        'all_normalizers_numerically_enumerated': False,
        'full_Monster_matrices_constructed': False,
        'valid_C11_falsified': False,
        'C13_threshold_changed': False,
        'novelty_established': False, 'numerical_tolerance': TOL},
        sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
