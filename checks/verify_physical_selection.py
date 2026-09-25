#!/usr/bin/env python3
"""Exact scalar checks for spectral selection, with no assumed Monster data.

No CFT is constructed and no OPE tensor or Monster representation is loaded.
The source theorems and uniqueness questions are not verified by this script.
Uses only Python's standard library and is unchanged by -O / -OO.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
from math import comb

LABELS: list[str] = []
ORDER = 16
BASE = '109e1cffd3c61f374635fec0a36f97e972d373e5'


def need(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)
    LABELS.append(label)


def mul(a: list[int], b: list[int]) -> list[int]:
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(ORDER+1)]


def power(a: list[int], n: int) -> list[int]:
    ans = [1]+[0]*ORDER
    for _ in range(n):
        ans = mul(ans, a)
    return ans


def inverse(a: list[int]) -> list[int]:
    if a[0] != 1:
        raise ValueError('This exact inversion requires unit constant term')
    out = [1]+[0]*ORDER
    for i in range(1, ORDER+1):
        out[i] = -sum(a[j]*out[i-j] for j in range(1, i+1))
    return out


def e4() -> list[int]:
    return [1]+[240*sum(d**3 for d in range(1, n+1) if n % d == 0)
                for n in range(1, ORDER+1)]


def eta_product(exponent: int) -> list[int]:
    """prod_(m>=1) (1-q^m)^exponent, to ORDER; no leading fractional q."""
    out = [1]+[0]*ORDER
    for m in range(1, ORDER+1):
        factor = [0]*(ORDER+1)
        for j in range(min(exponent, ORDER//m)+1):
            factor[j*m] = (-1)**j*comb(exponent, j)
        out = mul(out, factor)
    return out


def m_dimension(weight: int) -> int:
    """Dimension using C[E4,E6]; a source input, not a proof of the ring theorem."""
    if weight < 0:
        return 0
    return sum(4*a+6*b == weight for a in range(weight//4+1)
               for b in range(weight//6+1))


def modular_checks() -> dict:
    E4 = e4()
    chars = {}
    for c in (8, 16, 24):
        chars[c] = mul(power(E4, c//8), inverse(eta_product(c)))
        need(mul(chars[c], eta_product(c)) == power(E4, c//8),
             f'series:inverse_identity_c{c}')
    need(m_dimension(4) == m_dimension(8) == 1, 'modular:weight4_and_weight8_dimensions_one')
    need(m_dimension(12) == 2, 'modular:weight12_dimension_two')
    need(chars[8][1] == 248, 'minimality:c8_has_248_weight_one_states')
    need(chars[16][1] == 496, 'minimality:c16_has_496_weight_one_states')
    need(chars[24][1] == 744, 'series:j_constant_744')
    J = chars[24].copy()
    J[1] -= 744  # This list is q*(j-744), i.e. degree equals conformal weight.
    need(J[:5] == [1, 0, 196884, 21493760, 864299970], 'series:J_first_five_weight_degeneracies')
    need(J[2]-1 == 196883, 'spectrum:weight_two_primaries_after_stress_removal')
    need(J[3]-J[2] == 21296876, 'spectrum:weight_three_primary_count')
    need(all(m_dimension(k-12) == 0 for k in range(1, 12)), 'thermal:no_cusp_form_for_weights_one_through_eleven')
    need(m_dimension(0) == 1, 'thermal:first_allowed_cusp_space_weight_twelve_dimension_one')
    need(all(m_dimension(k-12) == 0 for k in (13, 14, 15)), 'thermal:higher_weight_vanishing_is_not_monotone')
    Delta_over_q = eta_product(24)
    need(Delta_over_q[:4] == [1, -24, 252, -1472], 'thermal:weight12_Delta_coefficients')
    # Independent finite combinatorial check of the scalar-gap deduction from
    # integer left/right weights, not a proof of an RG attraction theorem.
    allowed = [0]+list(range(2, 8))
    scalars = [h+hb for h in allowed for hb in allowed if h == hb and h+hb > 0]
    need(min(scalars) == 4, 'physics:diagonal_completion_scalar_gap_four')
    return {'c8_weight_one_count': chars[8][1], 'c16_weight_one_count': chars[16][1],
            'q_times_J_first_five_coefficients': J[:5],
            'first_modularly_allowed_primary_one_point_weight': 12}


def algebra_checks() -> dict:
    c, dimB = 24, 196884
    d = dimB-1
    # Matsuo Theorem 2.1 coefficients, applicable via Hoehn's design replacement.
    second = F(-2*(5*c*c-88*dimB+2*c*dimB), c*(5*c+22))
    third = F(-3*c*c*(70*c*c+769*c-340)
              +2*dimB*(4*c**3-445*c*c+12236*c-5984),
              c*(2*c-1)*(5*c+22)*(7*c+68))
    need(second == 4620, 'trace:second_coefficient_from_general_c_dimension_formula')
    need(third == 900, 'trace:third_coefficient_from_general_c_dimension_formula')
    s2 = F(4, c//2)
    need(s2 == F(1, 3), 'normalization:unit_stress_direction_multiplication_squared')
    kappa = second-2*s2
    cubic_trace = third-3*s2
    need(kappa == F(13858, 3), 'OPE:primary_contraction_kappa_after_two_scalar_cross_terms')
    need(cubic_trace == 899, 'OPE:primary_triple_trace_after_three_scalar_cross_terms')
    need(F(2*2, c) == F(1, 6), 'OPE:physical_stress_tensor_coefficient')
    need(d*kappa == F(2728404614, 3), 'OPE:total_squared_three_point_strength')
    alpha, beta = F(166)-2*s2, F(-116)
    u, v = F(166)*s2+52-s2*s2, F(-116)*s2+52
    need((alpha, beta, u, v) == (F(496, 3), F(-116), F(965, 9), F(40, 3)),
         'trace:fourth_order_projection_coefficients')
    sym_roots, skew_roots = (F(155, 3), F(-7, 3)), (F(845, 3), F(-1, 3))
    need(all(x*x == (alpha+beta)*x+u+v for x in sym_roots), 'contraction:symmetric_complement_roots')
    need(all(x*x == (alpha-beta)*x+u-v for x in skew_roots), 'contraction:antisymmetric_roots')
    need(cubic_trace**2 == (alpha+beta)*cubic_trace+alpha*kappa+u+v,
         'contraction:multiplication_subspace_root')
    need(kappa**2 == (alpha+beta)*kappa+u+v+u*d,
         'contraction:scalar_subspace_root')
    ns, na = d*(d+1)//2-1-d, d*(d-1)//2
    msp = (d*kappa/2-kappa-d*cubic_trace-sym_roots[1]*ns)/(sym_roots[0]-sym_roots[1])
    map_ = (-d*kappa/2-skew_roots[1]*na)/(skew_roots[0]-skew_roots[1])
    dims = [F(1), F(d), msp, ns-msp, map_, na-map_]
    roots = [kappa, cubic_trace, *sym_roots, *skew_roots]
    need(all(x.denominator == 1 and x > 0 for x in dims), 'contraction:all_multiplicities_positive_integers')
    dims = list(map(int, dims))
    need(dims == [1, 196883, 842609326, 18538750076, 21296876, 19360062527],
         'contraction:multiplicities_without_group_characters')
    need(sum(dims) == d*d, 'contraction:dimensions_cover_End_primary_space')
    need(sum(n*x for n, x in zip(dims, roots)) == 0, 'contraction:full_superoperator_trace_zero')
    need(sum(n*x for n, x in zip(dims[:4], roots[:4])) == d*kappa/2,
         'contraction:symmetric_supertrace')
    need(sum(n*x for n, x in zip(dims[4:], roots[4:])) == -d*kappa/2,
         'contraction:antisymmetric_supertrace')
    need(max(abs(x/kappa) for x in roots[1:]) == F(2697, 13858), 'contraction:nontrivial_norm')
    need(1-F(2697, 13858) == F(11161, 13858), 'contraction:inherited_three_register_gap_arithmetic')
    need(second != kappa and third != cubic_trace, 'negative_control:unprojected_trace_constants_are_not_primary_constants')
    # Crucial logic guard: at order three the identity still contains the
    # UNKNOWN C_abc on its right. These scalar checks do not reconstruct it.
    return {'primary_dimension': d, 'kappa': str(kappa),
            'triple_trace_coefficient': str(cubic_trace),
            'total_squared_primary_three_point_strength': str(d*kappa),
            'contraction_spectrum': [{'eigenvalue': str(x/kappa), 'multiplicity': n}
                                     for x, n in zip(roots, dims)],
            'stabilizer_identified_from_these_checks': False}


def main() -> None:
    modular = modular_checks()
    algebra = algebra_checks()
    print(json.dumps({'status': 'PASS: exact modular/OPE scalar implications only',
                      'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
                      'modular': modular, 'algebra': algebra,
                      'series_truncation_order': ORDER,
                      'arithmetic': 'integers and fractions only',
                      'dense_matrices_constructed': False,
                      'Monster_character_data_used': False,
                      'VOA_or_full_OPE_tensor_constructed': False,
                      'moonshine_uniqueness_proved': False,
                      'new_physical_selection_theorem_claimed': False},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
