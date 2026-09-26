#!/usr/bin/env python3
"""Exact arithmetic controls for the uniform extraction research record.

Source unitary/Ising/VOA classification theorems are explicit inputs, not
verified here. Continuum localization is proved in the note, not by testing
points. No floating point, external package, network, or Monster tensor.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []


def need(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    LABELS.append(label)


def padd(a: list[Q], b: list[Q]) -> list[Q]:
    return [(a[i] if i < len(a) else Q(0)) +
            (b[i] if i < len(b) else Q(0))
            for i in range(max(len(a), len(b)))]


def pscale(a: list[Q], c: Q) -> list[Q]:
    return [c*x for x in a]


def pmul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def peval(a: list[Q], x: Q) -> Q:
    return sum((c*x**i for i, c in enumerate(a)), Q(0))


def sqrt_upper(x: Q, bits: int = 48) -> Q:
    """Certified dyadic upper bound for sqrt(x), with no float conversion."""
    if x < 0 or bits < 0:
        raise ValueError('Nonnegative radicand and bit count required')
    den = 1 << bits
    num = isqrt((x.numerator*den*den)//x.denominator)
    if num*num*x.denominator < x.numerator*den*den:
        num += 1
    return Q(num, den)


def interval_certificate(ex: Q, ey: Q, delta: Q, bits: int = 48) -> dict:
    """A sufficient arithmetic test only; ambient VOA premises are NOT tested.

    A failure means this certificate did not establish the conclusion, not
    that the theory is non-moonshine. Negative deficits indicate inconsistent
    input bounds and are never silently clipped to zero.
    """
    if ex < 0 or ey < 0 or delta < 0:
        raise ValueError('Negative deficit/radius: check premises and normalization')
    rx = sqrt_upper(ex/2, bits)
    ry = sqrt_upper(ey/2, bits)
    budget = delta+rx+ry
    valid = ex < Q(1, 50) and ey < Q(1, 50) and budget < Q(3, 188)
    return {'sufficient_inequalities_pass': valid,
            'distance_upper_bounds': [rx, ry],
            'overlap_budget_upper': budget,
            'allowed_strict_budget': Q(3, 188),
            'requires_exact_ambient_VOA_and_normalized_real_primaries': True,
            'certificate_failure_refutes_moonshine': False}


def critical_checks() -> dict:
    # Polynomials in the component charge r.
    r = [Q(0), Q(1)]
    b2 = [Q(0), Q(1, 2), -Q(1, 48)]
    n = [Q(2), -Q(1, 6)]
    alpha = pscale(r, Q(1, 24))
    omega = padd(pscale(pmul(alpha, alpha), Q(2)), pscale(b2, Q(1, 6)))
    need(omega == pscale(alpha, Q(2))+[Q(0)], 'critical:omega_idempotence_polynomial')
    norm = padd(pscale(pmul(alpha, alpha), Q(12)), b2)
    need(norm == [Q(0), Q(1, 2), Q(0)], 'critical:positive_form_norm_is_r_over_two')
    need(padd(pscale(alpha, Q(4)), n) == [Q(2), Q(0)], 'critical:primary_idempotence_coefficient')
    deriv = padd(pscale(b2, -Q(1, 6)), pscale(pmul(n, [Q(1, 2), -Q(1, 24)]), -Q(1, 2)))
    need(deriv == [-Q(1, 2), Q(0), Q(0)], 'critical:strictly_decreasing_charge_conversion')
    cap2 = Q(2116, 141)
    next2 = Q(51076, 4893)
    need(peval(n, Q(1, 2))**2/peval(b2, Q(1, 2)) == cap2, 'critical:Ising_cap_squared')
    need(peval(n, Q(7, 10))**2/peval(b2, Q(7, 10)) == next2, 'critical:next_unitary_value_squared')
    need(Q(19, 5)**2 < cap2 < Q(4)**2, 'critical:rational_bounds_on_maximum')
    need(next2 < Q(33, 10)**2, 'critical:rational_bound_on_other_critical_values')
    need(Q(19, 5)-Q(33, 10) == Q(1, 2), 'critical:gap_greater_than_one_half')
    charges = [1-Q(6, m*(m+1)) for m in range(3, 7)]
    need(charges[:2] == [Q(1, 2), Q(7, 10)], 'source_interface:first_two_unitary_charges')
    return {'cap_squared': cap2, 'next_critical_upper_squared': next2,
            'first_unitary_charges': charges,
            'all_charge_classification_is_imported_not_proved_by_samples': True}


def localization_checks() -> dict:
    tangent = [24*h-1 for h in [Q(0), Q(1, 16), Q(1, 2)]]
    need(tangent == [-1, Q(1, 2), 11], 'local:Ising_tangent_numerators')
    need([6*z-138 for z in tangent] == [-144, -135, -72], 'local:strict_tangent_Hessian')
    s2 = [Q(0), Q(0), Q(1)]
    q = [Q(1), Q(0), -Q(1, 2)]
    one_minus_q3 = padd([Q(1)], pscale(pmul(pmul(q, q), q), -Q(1)))
    leading = [Q(0), Q(0), Q(3, 2), Q(0), -Q(3, 4)]
    residual = padd(one_minus_q3, pscale(leading, -Q(1)))
    need(residual == [0, 0, 0, 0, 0, 0, Q(1, 8)], 'local:exact_nonnegative_chord_remainder')
    need(36**2 > 9*141, 'local:36_over_sqrt141_greater_than_three')
    R, kappa = Q(1, 10), Q(2)
    lower = 3-3*R**2-4*R
    need(lower == Q(257, 100) > kappa, 'local:uniform_quadratic_growth_coefficient')
    need(kappa*R**2 == Q(1, 50) < Q(1, 2), 'global:entry_threshold_below_critical_gap')
    # A direct finite family control: f(x,y)=x^3. This checks an algebraic
    # instance, NOT the continuum compactness lemma by sampling.
    controls = []
    for t in [Q(0), Q(1, 200), Q(1, 100), Q(1, 80)]:
        x, y = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        dist2 = (x-1)**2+y*y
        loss = 1-x**3
        need(x*x+y*y == 1, f'circle:t{t}_unit_rational_point')
        need(loss >= dist2 and dist2 <= loss, f'circle:t{t}_positive_growth_and_localization')
        controls.append({'t': t, 'distance_squared': dist2, 'loss': loss})
    return {'local_radius': R, 'quadratic_growth': kappa,
            'global_entry_strict_threshold': Q(1, 50),
            'continuum_localization_proved_in_note_not_sampled': True,
            'simple_circle_controls': controls}


def rounding_checks() -> dict:
    values = [Q(0), Q(1, 256), Q(5, 1024), Q(3, 512), Q(1, 128), Q(13, 1024), Q(1, 32), Q(1, 4)]
    need(min(x for x in values if x > 0) == Q(1, 256), 'source_interface:least_positive_Ising_overlap')
    const, scale = Q(1, 192), Q(47, 192)
    need(const+scale*(-Q(1, 47)) == 0, 'overlap:orthogonal_pair_primary_overlap')
    need(scale*Q(3, 188) == Q(1, 256), 'overlap:strict_primary_threshold')
    historical = interval_certificate(Q(1, 32768), Q(1, 32768), Q(1, 128))
    need(historical['distance_upper_bounds'] == [Q(1, 256)]*2, 'rounding:historical_exact_distance')
    need(historical['sufficient_inequalities_pass'], 'rounding:historical_tolerances_pass')
    need(historical['overlap_budget_upper'] == Q(1, 64), 'rounding:historical_overlap_budget')
    need(Q(3, 188)-Q(1, 64) == Q(1, 3008), 'rounding:primary_margin')
    need(Q(1, 256)-scale*Q(1, 64) == Q(1, 12288), 'rounding:full_Ising_margin')
    need(2*Q(1, 256) < Q(1, 10), 'rounding:uniqueness_from_maximum_separation')
    asymmetric = []
    for ex, ey, delta in [(Q(0), Q(1, 32768), Q(1, 128)),
                          (Q(1, 131072), Q(1, 32768), Q(1, 128)),
                          (Q(1, 100000), Q(1, 50000), Q(1, 100)),
                          (Q(1, 1000000), Q(1, 900000), Q(1, 80))]:
        answer = interval_certificate(ex, ey, delta)
        need(answer['sufficient_inequalities_pass'], f'asymmetric:{ex}_{ey}_{delta}_passes')
        for value, bound in zip([ex/2, ey/2], answer['distance_upper_bounds']):
            need(bound*bound >= value, f'asymmetric:{ex}_{ey}_certified_square_root_{value}')
        asymmetric.append({'deficits': [ex, ey], 'overlap_radius': delta, 'certificate': answer})
    need(not interval_certificate(Q(0), Q(0), Q(3, 188))['sufficient_inequalities_pass'],
         'negative:discrete_boundary_equality_is_not_strict_certificate')
    need(not interval_certificate(Q(1, 50), Q(0), Q(0))['sufficient_inequalities_pass'],
         'negative:entry_boundary_equality_is_not_admitted')
    need(not interval_certificate(Q(1, 100), Q(1, 100), Q(0))['sufficient_inequalities_pass'],
         'negative:large_rounding_radii_do_not_certify_pair')
    for args in [(-Q(1, 1000), Q(0), Q(0)), (Q(0), Q(0), -Q(1, 1000))]:
        rejected = False
        try:
            interval_certificate(*args)
        except ValueError:
            rejected = True
        need(rejected, 'negative:inconsistent_bounds_rejected_'+str(args))
    need(not historical['certificate_failure_refutes_moonshine'], 'logic:certificate_failure_not_a_nonexistence_result')
    return {'source_overlap_values': values, 'historical_certificate': historical,
            'asymmetric_certificates': asymmetric,
            'classification_and_overlap_theorems_are_imported': True}


def countercontrols() -> dict:
    # f_t(cos theta,sin theta)=cos(2 theta)+t cos theta.
    # Endpoint values differ by 2t; angular Hessians are -4-t and -4+t.
    examples = []
    for t in [Q(1, 10), Q(1, 100), Q(1, 1000)]:
        need(-4+t < -3 and -4-t < -3, f'negative:t{t}_uniform_local_curvature')
        need((1+t)-(1-t) == 2*t, f'negative:t{t}_other_peak_approaches_top')
        examples.append({'t': t, 'critical_value_gap': 2*t, 'squared_distance_between_peaks': 4})
    # f=1-(1-x)^2 on the unit circle has loss exactly chord_distance^4/4.
    for t in [Q(1, 10), Q(1, 100)]:
        x, y = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        s2 = (x-1)**2+y*y
        need((1-x)**2 == s2*s2/4, f'negative:t{t}_quartic_loss_without_quadratic_growth')
    # A genuine source-defined outside-holomorphic-class example, checked only
    # on its factorwise stress algebra: 48 independent charge-1/2 factors.
    n, c = 48, Q(1, 2)
    omega = [Q(1)]*n
    e = [Q(1)]+[Q(0)]*(n-1)
    f = [Q(0), Q(1)]+[Q(0)]*(n-2)
    def ip(a: list[Q], b: list[Q]) -> Q:
        return sum((c*x*y/2 for x, y in zip(a, b)), Q(0))
    def prod(a: list[Q], b: list[Q]) -> list[Q]:
        return [2*x*y for x, y in zip(a, b)]
    a = [x-z/48 for x, z in zip(e, omega)]
    b = [x-z/48 for x, z in zip(f, omega)]
    norm = ip(a, a)
    cubic = ip(prod(a, a), a)
    need(n*c == 24 and norm == Q(47, 192), 'scope:Ising_tensor_product_centering')
    need(cubic*cubic/norm**3 == Q(2116, 141), 'scope:outside_holomorphic_class_has_same_cubic')
    need(ip(a, b)/norm == -Q(1, 47), 'scope:outside_holomorphic_class_has_same_overlap')
    need(n != 196884, 'scope:local_correlations_alone_do_not_classify_without_ambient_premises')
    return {'gap_counterexamples': examples, 'quartic_counterexample_exact': True,
            'tensor_product_factors': 48, 'outside_example_holomorphic': False,
            'full_tensor_product_VOA_constructed': False}


def strings(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): strings(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [strings(v) for v in x]
    return x


def main() -> None:
    critical = critical_checks()
    local = localization_checks()
    rounding = rounding_checks()
    controls = countercontrols()
    report = {'status': 'PASS within exact polynomial/interval/scope controls',
              'base_commit': BASE, 'checks': len(LABELS), 'labels': LABELS,
              'critical_value_certificate': critical, 'localization_controls': local,
              'overlap_certificate': rounding, 'countercontrols': controls,
              'arithmetic': 'integers and fractions only',
              'largest_constructed_square_matrix_dimension': 0,
              'largest_coefficient_vector_dimension': 48,
              'full_Monster_tensor_constructed': False,
              'source_theorems_formally_verified': False,
              'priority_or_significance_settled': False,
              'manuscript_written': False}
    print(json.dumps(strings(report), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
