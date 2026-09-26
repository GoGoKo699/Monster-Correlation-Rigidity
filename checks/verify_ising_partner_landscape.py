#!/usr/bin/env python3
"""Exact small certificates for an Ising-commutant search and a tricritical trap.

Sources, not proved by this script: conformal designs, Ising/2A representations,
unitary Virasoro classification, existence of the 2A subalgebra in moonshine,
and Abe-Lam-Yamada's two-Ising theorem. No fifth trace or group character data.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []


def need(ok: bool, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def solve(matrix, rhs):
    n = len(rhs)
    a = [[Q(x) for x in row] + [Q(b)] for row, b in zip(matrix, rhs)]
    determinant = Q(1)
    for i in range(n):
        p = next((k for k in range(i, n) if a[k][i]), None)
        if p is None:
            raise ValueError('Singular system')
        if p != i:
            a[i], a[p] = a[p], a[i]
            determinant = -determinant
        d = a[i][i]
        determinant *= d
        a[i] = [x/d for x in a[i]]
        for k in range(n):
            if k != i:
                d = a[k][i]
                a[k] = [x-d*y for x, y in zip(a[k], a[i])]
    return [row[-1] for row in a], determinant


def trace_coefficients(c, dimension):
    """Matsuo Theorem 2.1 through order three, applied via design hypotheses."""
    c, d = Q(c), Q(dimension)
    den = c*(2*c-1)*(5*c+22)*(7*c+68)
    return [4*d/c,
            -2*(5*c*c-88*d+2*c*d)/(c*(5*c+22)),
            4*(5*c+22*d)/(c*(5*c+22)),
            (-3*c*c*(70*c*c+769*c-340)
             +2*d*(4*c**3-445*c*c+12236*c-5984))/den,
            (4*c*(70*c*c+1017*c-340)
             -8*d*(32*c*c-1419*c+748))/den,
            5952*c*(d-1)/den]


def virasoro_moments(c, dimension, r):
    q = Q(r, 2)
    a1, a2, b2, a3, b3, c3 = trace_coefficients(c, dimension)
    # u*u=2u, <u,u>=<u,eta>=r/2.
    return [Q(dimension), a1*q, a2*q+b2*q*q,
            2*a3*q+3*b3*q*q+c3*q**3]


def ising_commutant():
    coeff = trace_coefficients(24, 196884)
    need(coeff == [32814, 4620, 5084, 900, 620, 744],
         'source_conversion:ambient_first_three_trace_coefficients')
    eigenvalues = [Q(0), Q(1, 16), Q(1, 2), Q(2)]
    moments = virasoro_moments(24, 196884, Q(1, 2))
    vandermonde = [[x**k for x in eigenvalues] for k in range(4)]
    multiplicities, det = solve(vandermonde, moments)
    need(det != 0, 'Ising:moment_system_is_invertible')
    need(multiplicities == [96256, 96256, 4371, 1],
         'Ising:eigenspace_dimensions_without_group_characters')
    for k in range(4):
        need(sum(n*x**k for n, x in zip(multiplicities, eigenvalues)) == moments[k],
             f'Ising:moment_order_{k}')
    def q0(x):
        return (1-16*x)*(1-2*x)*(1-x/2)
    need([q0(x) for x in eigenvalues] == [1, 0, 0, 0],
         'Ising:commutant_projector_polynomial')
    C = Q(47, 2)
    need(24-Q(1, 2) == C, 'commutant:central_charge')
    need(96256-1 == 96255, 'commutant:primary_dimension')
    need(11+2-2*3 == 7, 'commutant:derived_design_strength_is_seven_not_eleven')
    need(Q(2, 1)/C == Q(4, 47), 'commutant:stress_direction_projector_normalization')
    cc = trace_coefficients(C, 96256)
    need(cc == [16384, 2406, 2584, 479, 328, 384],
         'source_conversion:commutant_first_three_trace_coefficients')
    return {'charge': C, 'weight_two_dimension': 96256,
            'primary_dimension': 96255, 'Ising_eigenvalues': eigenvalues,
            'Ising_multiplicities': multiplicities, 'moment_matrix': vandermonde,
            'moment_rhs': moments, 'moment_determinant': det,
            'commutant_trace_coefficients': cc, 'inherited_design_strength': 7}


def two_a_control():
    # The exact three-Ising Griess algebra. It is not being claimed to be a
    # standalone c24 theory. A fourth vector z is the complementary stress.
    n = 4
    unit = [[Q(i == j) for i in range(n)] for j in range(n)]
    e, f, g, z = unit
    metric = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(3):
        for j in range(3):
            metric[i][j] = Q(1, 4) if i == j else Q(1, 32)
    metric[3][3] = Q(57, 5)
    def add(a, b, s=1):
        return [x+s*y for x, y in zip(a, b)]
    def scale(a, s):
        return [s*x for x in a]
    def inner(a, b):
        return sum(a[i]*metric[i][j]*b[j] for i, j in product(range(n), repeat=2))
    def mul(a, b):
        out = [Q(0)]*n
        for i, j in product(range(n), repeat=2):
            c = a[i]*b[j]
            if i == j:
                out[i] += 2*c
            elif i < 3 and j < 3:
                k = 3-i-j
                out[i] += c/4
                out[j] += c/4
                out[k] -= c/4
        return out
    for i, a in enumerate(unit[:3]):
        need(mul(a, a) == scale(a, 2) and inner(a, a) == Q(1, 4),
             f'2A:axis_{i}_Ising_idempotence_and_norm')
    need(all(inner(mul(a, b), c) == inner(a, mul(b, c))
             for a, b, c in product(unit, repeat=3)), '2A:metric_invariance_all_basis_labels')
    Omega = scale(add(add(e, f), g), Q(4, 5))
    u = add(Omega, e, -1)
    omega = add(Omega, z)
    eta = add(omega, e, -1)
    need(mul(Omega, Omega) == scale(Omega, 2), '2A:subalgebra_conformal_vector')
    need(2*inner(Omega, Omega) == Q(6, 5), '2A:subalgebra_charge_six_fifths')
    need(mul(u, u) == scale(u, 2) and mul(e, u) == [0]*n,
         '2A:tricritical_vector_commutes_with_first_Ising')
    need(2*inner(u, u) == Q(7, 10), '2A:tricritical_charge')
    need(inner(omega, omega) == 12 and inner(eta, eta) == Q(47, 4),
         '2A:ambient_and_commutant_stress_norms')
    v = add(f, g, -1)
    need(inner(v, v) == Q(7, 16), '2A:explicit_nonzero_escape_direction')
    need(mul(e, v) == scale(v, Q(1, 2)), '2A:escape_is_not_in_commutant')
    need(mul(u, v) == scale(v, Q(3, 2)), '2A:escape_has_tricritical_eigenvalue_three_halves')
    need(inner(v, omega) == inner(v, u) == 0, '2A:escape_is_ambient_sphere_tangent')
    neg = add(e, z, -Q(5, 228))
    need(inner(neg, omega) == inner(neg, u) == 0 and inner(neg, neg) > 0,
         '2A:ambient_negative_tangent_exists')
    need(mul(u, neg) == [0]*n, '2A:ambient_negative_tangent_eigenvalue_zero')
    for C, stress, label in [(Q(24), omega, 'ambient'), (Q(47, 2), eta, 'commutant')]:
        r = Q(7, 10)
        x = add(u, stress, -r/C)
        B2 = r*(C-r)/(2*C)
        need(inner(x, stress) == 0 and inner(x, x) == B2,
             f'2A:{label}_centered_primary_norm')
        projected = add(mul(x, x), stress, -4*B2/C)
        need(projected == scale(x, 2-4*r/C), f'2A:{label}_cubic_critical_equation')
    need(6*(Q(3, 2)-1) == 3 and 6*(0-1) == -6,
         '2A:ambient_Hessian_has_both_signs')
    need(inner(mul(x, x), v) == 0 and
         inner(mul(x, v), v)/inner(v, v) == Q(3, 2)*(1-r/C),
         '2A:unconstrained_escape_curve_through_commutant_centered_point')
    need(6*Q(3, 2)*(1-r/C)-3*(2-4*r/C) == 3*(1+r/C) > 0,
         '2A:unconstrained_escape_curve_positive_second_derivative')
    return {'metric': metric, 'Omega': Omega, 'derived_tricritical': u,
            'complementary_stress': z, 'escape_vector': v,
            'negative_ambient_direction': neg,
            'existence_of_full_moonshine_embedding_is_a_source_input': True}


def tricritical_spectrum():
    C, r, dimension = Q(47, 2), Q(7, 10), 96256
    # sigma-type is an imported representation-theoretic condition of a
    # derived 2A vector; do not assume it for all c=7/10 Virasoro vectors.
    possible = [Q(0), Q(1, 10), Q(3, 5), Q(3, 2)]
    moments = virasoro_moments(C, dimension, r)
    rhs = [x-2**k for k, x in enumerate(moments)]  # the single u direction
    matrix = [[h**k for h in possible] for k in range(4)]
    multiplicities, det = solve(matrix, rhs)
    need(det != 0, 'tricritical:four_by_four_moment_system_invertible')
    need(multiplicities == [48621, 45696, 1938, 0],
         'tricritical:full_commutant_spectrum_reconstructed')
    need(all(x >= 0 and x.denominator == 1 for x in multiplicities),
         'tricritical:multiplicities_nonnegative_integers')
    need(sum(multiplicities)+1 == dimension, 'tricritical:spectrum_exhausts_commutant')
    for k in range(4):
        need(sum(m*h**k for m, h in zip(multiplicities, possible)) == rhs[k],
             f'tricritical:moment_order_{k}')
    B2 = r*(C-r)/(2*C)
    lambda2 = (2-4*r/C)**2/B2
    cap2 = 8*(C-1)**2/(C*Q(1, 2)*(C-Q(1, 2)))
    need(B2 == Q(399, 1175), 'landscape:tricritical_primary_norm_squared')
    need(lambda2 == Q(195364, 18753), 'landscape:false_peak_cubic_squared')
    need(cap2 == Q(16200, 1081), 'landscape:Ising_global_cap_squared')
    need(lambda2 < Q(13, 4)**2 < cap2, 'selection:coarse_threshold_thirteen_quarters')
    need(Q(19, 5)**2 < cap2 < 16, 'landscape:cap_between_nineteen_fifths_and_four')
    hess = [6*(h-1) for h in possible[:3]]
    mult = [int(multiplicities[0])-1, int(multiplicities[1]), int(multiplicities[2])]
    need(hess == [-6, -Q(27, 5), -Q(12, 5)], 'landscape:Hessian_numerators')
    need(all(h < 0 for h in hess), 'landscape:strict_local_maximum_in_every_tangent_direction')
    need(sum(mult) == 96254, 'landscape:tangent_dimension')
    need(multiplicities[-1] == 0, 'landscape:all_three_halves_escape_directions_absent')
    need(B2 < Q(9, 25), 'basin:leading_quadratic_loss_exceeds_two')
    rad = Q(1, 10)
    need(2-3*rad**2-4*rad == Q(157, 100) > Q(3, 2),
         'basin:uniform_lower_loss_coefficient')
    need(Q(3, 2)*rad**2 == Q(3, 200), 'basin:required_boundary_drop')
    # The exact Ising curve obeys a different charge. It cannot lie in the
    # radius-one-tenth basin since its cubic is strictly larger.
    need(cap2 > lambda2, 'basin:higher_peak_cannot_be_reached_monotonically_through_boundary')
    return {'possible_sigma_type_weights': possible, 'moment_matrix': matrix,
            'moment_rhs_after_removing_u': rhs, 'matrix_determinant': det,
            'multiplicities': multiplicities, 'primary_norm_squared': B2,
            'false_peak_cubic_squared': lambda2, 'Ising_cap_squared': cap2,
            'Hessian_values_times_primary_norm': hess, 'Hessian_multiplicities': mult,
            'certified_radius': rad, 'loss_coefficient': Q(3, 2),
            'boundary_drop': Q(3, 200),
            'source_sigma_type_condition_not_proved_by_matrix_check': True}


def normalization_and_limits():
    # General charge/cubic conversions at rational r; universal identities
    # are written and proved in the note, not inferred from this sample.
    C = Q(47, 2)
    for r in [Q(1, 2), Q(7, 10), Q(4, 5), Q(1), Q(7), C/2]:
        b2 = r*(C-r)/(2*C)
        num = 2-4*r/C
        derivative_num = -4*b2/C-num*(C-2*r)/(4*C)
        need(derivative_num == -Q(1, 2), f'normalization:monotonicity_numerator_at_charge_{r}')
        need(2*(r/C)**2+4*b2/C == 2*r/C,
             f'normalization:idempotence_stress_component_at_charge_{r}')
    # Kac-table derivation of allowed unitary Virasoro lowest weights.
    for m, expected in [(3, {Q(0), Q(1, 16), Q(1, 2)}),
                        (4, {Q(0), Q(3, 80), Q(1, 10), Q(7, 16), Q(3, 5), Q(3, 2)})]:
        weights = {Q(((m+1)*a-m*b)**2-1, 4*m*(m+1))
                   for a in range(1, m) for b in range(1, m+1)}
        need(weights == expected, f'Kac:unitary_model_m{m}_weights')
    # Normalizing the same residual field with the *ambient* stress gives
    # different cubic numbers; the two central charges must not be conflated.
    C0, r = Q(24), Q(7, 10)
    ambient2 = 8*(C0-2*r)**2/(C0*r*(C0-r))
    need(ambient2 == Q(51076, 4893), 'negative:ambient_tricritical_cubic_uses_charge_twenty_four')
    need(ambient2 != Q(195364, 18753), 'negative:ambient_and_commutant_normalizations_differ')
    return {'first_Ising_forced_from_bare_assumptions': False,
            'second_Ising_forced_from_first_alone': False,
            'local_ascent_is_a_complete_partner_search': False,
            'global_witness_above_thirteen_quarters_implies_partner': True,
            'known_commutant_identified_with_all_unknown_commutants': False,
            'new_classification_or_independence_theorem_claimed': False}


def stringify(x):
    if isinstance(x, Q): return str(x)
    if isinstance(x, dict): return {str(k): stringify(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [stringify(v) for v in x]
    return x


def main():
    arena = ising_commutant()
    control = two_a_control()
    spectrum = tricritical_spectrum()
    limits = normalization_and_limits()
    report = {'status': 'PASS: exact low-dimensional algebra and moment certificates',
              'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
              'commutant': arena, 'two_A_control': control,
              'tricritical_spectrum_and_landscape': spectrum, 'scope': limits,
              'arithmetic': 'integers and fractions only',
              'largest_square_matrix_dimension': 4,
              'largest_state_coefficient_vector_length': 4,
              'group_character_data_used': False,
              'full_Monster_operator_or_CFT_constructed': False,
              'source_theorems_formally_verified': False,
              'finite_samples_prove_continuum_landscape': False,
              'independent_expert_review_or_novelty_clearance': False}
    print(json.dumps(stringify(report), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
