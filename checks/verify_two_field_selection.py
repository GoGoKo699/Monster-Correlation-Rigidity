#!/usr/bin/env python3
"""Exact arithmetic supporting the two-near-extremal-field criterion.

Imported mathematics, not verified here: unitary Virasoro classification,
Ising representation theory, Sakuma's overlap theorem, ALY uniqueness.
The continuum localization proof is in the accompanying note. Small tensor
products are genuine outside-holomorphic-class controls, not large CFT sims.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import permutations
import hashlib
import json
import selection_virasoro as v

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]


def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


class Poly:
    """Exact univariate polynomials, sufficient for the small Gram identity."""
    def __init__(self,coefficients=0):
        if isinstance(coefficients,Poly):
            self.a=coefficients.a
            return
        if not isinstance(coefficients,(list,tuple)):
            coefficients=[coefficients]
        a=list(map(Q,coefficients))
        while len(a)>1 and a[-1]==0:
            a.pop()
        self.a=tuple(a or [Q(0)])
    def __bool__(self):return any(self.a)
    def __add__(self,other):
        b=Poly(other)
        return Poly([(self.a[i] if i<len(self.a) else 0)+(b.a[i] if i<len(b.a) else 0)
                     for i in range(max(len(self.a),len(b.a)))])
    __radd__=__add__
    def __neg__(self):return Poly([-a for a in self.a])
    def __sub__(self,b):return self+-Poly(b)
    def __rsub__(self,b):return Poly(b)+-self
    def __mul__(self,other):
        b=Poly(other);result=[Q(0)]*(len(self.a)+len(b.a)-1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b.a):result[i+j]+=x*y
        return Poly(result)
    __rmul__=__mul__
    def __pow__(self,n):
        result=Poly(1)
        for _ in range(n):result=result*self
        return result
    def __eq__(self,b):return self.a==Poly(b).a
    def at(self,x):return sum((a*x**i for i,a in enumerate(self.a)),Q(0))


def determinant(matrix):
    n=len(matrix);ans=Poly(0)
    for p in permutations(range(n)):
        term=Poly((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):term=term*matrix[i][p[i]]
        ans=ans+term
    return ans


def charge_and_gram_checks():
    r=Poly([0,1]);b2=r*(24-r)*Q(1,48);num=2-r*Q(1,6)
    need(-b2*Q(1,6)-num*(12-r)*Q(1,48)==-Q(1,2),
         'critical:exact_derivative_numerator_is_minus_one_half')
    need(2*(r*Q(1,24))**2+b2*Q(1,6)==r*Q(1,12),
         'critical:Virasoro_idempotence_omega_component')
    need(r*Q(1,6)+num==2,'critical:Virasoro_idempotence_primary_component')
    need(12*(r*Q(1,24))**2+b2==r*Q(1,2),'critical:Virasoro_norm_and_charge')
    need(b2.at(Q(1,2))==Q(141,576),'critical:Ising_primary_component_norm')
    need(num.at(Q(1,2))==Q(23,12),'critical:Ising_numerator')
    M2=Q(2116,141);next2=Q(51076,4893)
    need(num.at(Q(1,2))**2/b2.at(Q(1,2))==M2,'critical:Ising_cubic_cap_squared')
    need(num.at(Q(7,10))**2/b2.at(Q(7,10))==next2,'critical:next_allowed_charge_value_squared')
    need(Q(19,5)**2<M2<16,'critical:rational_bounds_on_cap')
    need(next2<Q(33,10)**2,'critical:rational_upper_bound_nonIsing_critical')
    need(Q(19,5)-Q(33,10)==Q(1,2),'critical:strict_gap_exceeds_one_half')
    # Source classification is an input. Check its first parameters, not its proof.
    series=[1-Q(6,m*(m+1)) for m in range(2,10)]
    need(series[:4]==[0,Q(1,2),Q(7,10),Q(4,5)],'source_interface:first_unitary_series_charges')
    need(all(a<b for a,b in zip(series,series[1:])),'source_interface:sample_series_monotonicity')
    c=Poly([0,1]);vir=v.Vir(1,0);vir.c=c
    words=((6,),(4,2),(3,3),(2,2,2))
    gram=[[Poly(vir.gram(a,b)) for b in words] for a in words]
    det=determinant(gram)
    expected=Q(3,4)*c**4*(2*c-1)*(5*c+22)**2*(7*c+68)
    need(det==expected,'Virasoro:four_state_Gram_symbolic_determinant')
    for val in (Q(1,8),Q(1,4),Q(3,8)):
        need(det.at(val)<0,f'Virasoro:negative_determinant_below_half_at_{val}')
    need(det.at(Q(1,2))==0,'Virasoro:determinant_vanishes_at_Ising_charge')
    return {'unitary_series_sample':series,'cap_squared':M2,'nonIsing_critical_upper_squared':next2,
            'Gram_words':words,'Gram_polynomial_coefficients':[[z.a for z in row] for row in gram],
            'determinant_polynomial_coefficients':det.a,
            'classification_of_all_unitary_modules_is_imported':True}


def localization_checks():
    # The three allowed tangent values follow from the Ising module statement,
    # no multiplicities or Monster character data are used.
    spectrum=[Q(0),Q(1,16),Q(1,2)]
    tangent_scaled=[24*h-1 for h in spectrum]
    hessian_scaled=[6*z-3*46 for z in tangent_scaled]
    need(tangent_scaled==[-1,Q(1,2),11],'local:tangent_spectrum_numerators')
    need(hessian_scaled==[-144,-135,-72],'local:strictly_negative_Hessian_numerators')
    need(Q(36)**2>9*141,'local:36_over_sqrt141_exceeds_three')
    radius=Q(1,10)
    lower=3-3*radius**2-4*radius
    need(lower==Q(257,100)>2,'local:uniform_loss_coefficient_exceeds_two')
    need(2*radius**2==Q(1,50),'local:boundary_loss_for_global_entry')
    need(Q(19,5)-Q(1,50)>Q(33,10),'local:outside_critical_values_below_boundary')
    eps=Q(1,32768);rho=Q(1,256)
    need(eps<Q(1,50),'rounding:chosen_loss_inside_global_entry_range')
    need(2*rho*rho==eps,'rounding:chosen_chord_distance_one_over_256')
    need(2*rho<radius,'rounding:unique_nearby_maximum_at_chosen_tolerance')
    # A countercontrol against turning mere stationarity into saturation.
    r=Q(4,5);b2=r*(24-r)/48;num=2-r/6
    need(num*num/b2<Q(2116,141),'negative:charge_four_fifths_not_saturation')
    need(6*(0-1)<0,'negative:product_model_unsaturated_maximum_has_negative_Hessian')
    return {'local_radius':radius,'guaranteed_loss_coefficient':2,
            'global_entry_loss_strict_upper':Q(1,50),'chosen_self_coupling_loss':eps,
            'rounding_distance':rho,'tangent_Hessian_numerators_over_sqrt141':hessian_scaled,
            'continuum_compactness_argument_proved_in_note_not_by_tests':True}


def overlap_checks():
    # Normalization: e=omega/48+(sqrt141/24)*a.
    const=Q(12,48**2);scale=Q(141,24**2)
    need(const==Q(1,192) and scale==Q(47,192),'overlap:full_stress_and_primary_coefficients')
    need(const+scale==Q(1,4),'overlap:Ising_norm_one_quarter')
    need(const+scale*(-Q(1,47))==0,'overlap:orthogonal_Ising_pair_primary_overlap')
    allowed=sorted(set([Q(0),Q(1,256),Q(5,1024),Q(3,512),Q(1,128),Q(13,1024),Q(1,32),Q(1,4)]))
    need(min(q for q in allowed if q)>0 and min(q for q in allowed if q)==Q(1,256),
         'source_interface:minimum_positive_Sakuma_overlap')
    primary=[(h-const)/scale for h in allowed]
    need(primary[0]==-Q(1,47) and primary[-1]==1,'overlap:normalized_extreme_values')
    need(primary[1]-primary[0]==Q(3,188),'overlap:normalized_discrete_gap')
    delta=Q(1,128);rho=Q(1,256)
    propagated=delta+2*rho
    need(propagated==Q(1,64)<Q(3,188),'robust:primary_overlap_margin')
    upper=scale*propagated
    need(upper==Q(47,12288),'robust:Ising_overlap_upper_bound')
    need(Q(1,256)-upper==Q(1,12288)>0,'robust:strict_rounding_margin')
    need([q for q in allowed if abs(q)<=upper]==[0],'robust:zero_is_unique_allowed_overlap')
    # The same vector never passes the target overlap test.
    need(abs(1+Q(1,47))>delta,'negative:duplicate_saturated_field_fails_pair_condition')
    # Check several exact error allocations satisfying the general inequality.
    allocations=[]
    for distance,error in [(Q(1,512),Q(1,128)),(Q(1,1024),Q(1,100)),(Q(1,2048),Q(1,80))]:
        loss=2*distance**2
        need(loss<Q(1,50) and error+2*distance<Q(3,188),
             f'robust:general_error_allocation_distance_{distance}')
        allocations.append({'loss':loss,'two_point_error':error,'distance':distance})
    return {'Sakuma_overlap_values':allowed,'corresponding_primary_overlaps':primary,
            'chosen_two_point_error':delta,'rounded_Ising_overlap_bound':upper,
            'strict_overlap_margin':Q(1,12288),'other_sufficient_exact_allocations':allocations,
            'Sakuma_theorem_proved_by_table_check':False}


def add(a,b,k=1):return [x+k*y for x,y in zip(a,b)]
def mul(a,b):return [2*x*y for x,y in zip(a,b)]
def inner(a,b,charges):return sum((r*x*y/2 for x,y,r in zip(a,b,charges)),Q(0))
def centered(a,charges):
    omega=[Q(1)]*len(a)
    return add(a,omega,-inner(a,omega,charges)/12)


def tensor_product_control(n,r):
    charges=[Q(r)]*n;omega=[Q(1)]*n
    need(sum(charges)==24,f'control:{n}_factors_total_charge_24')
    need(inner(omega,omega,charges)==12,f'control:{n}_stress_norm')
    a=[Q(0)]*n;b=[Q(0)]*n;a[0]=1;b[1]=1
    need(mul(a,a)==[2*x for x in a] and mul(a,b)==[0]*n,
         f'control:{n}_orthogonal_factor_Virasoro_products')
    x=centered(a,charges);y=centered(b,charges)
    g=inner(x,x,charges);cubic=inner(mul(x,x),x,charges)
    need(inner(x,omega,charges)==0 and g>0,f'control:{n}_nonzero_primary_direction')
    need(centered(mul(x,x),charges)==[(2-r/6)*z for z in x],f'control:{n}_cubic_critical_equation')
    expected=4*(12-r)**2/(3*r*(24-r))
    need(cubic>0 and cubic*cubic/g**3==expected,f'control:{n}_normalized_cubic_value')
    # Centered overlap need not be -1/47 unless factors have the Ising charge.
    overlap=inner(x,y,charges)/g
    need(overlap==-Q(1,n-1),f'control:{n}_centered_factor_overlap')
    if r==Q(1,2):
        need(expected==Q(2116,141) and overlap==-Q(1,47),
             'negative:nonholomorphic_product_passes_exact_three_number_condition')
        need(n==48 and n-1==47 and n!=196884,
             'negative:Ising_product_weight_two_dimension_excludes_moonshine')
    else:
        need(expected<Q(2116,141),'negative:unitary_product_strictly_below_cap')
        need(r==Q(4,5)>Q(1,2),'negative:unsaturated_product_smallest_component_charge')
    return {'number_of_factors':n,'factor_charge':r,'weight_two_dimension':n,
            'primary_dimension':n-1,'normalized_self_coupling_squared':expected,
            'normalized_pair_overlap':overlap,'holomorphic':False,
            'full_tensor_product_VOA_simulated':False}


def known_pair_checks():
    # Weight-two algebra of one norm-four lattice direction. Basis A,E as in note.
    def prod(x,y):
        return [16*x[0]*y[0]+x[1]*y[1],16*(x[0]*y[1]+x[1]*y[0])]
    def form(x,y):return 32*x[0]*y[0]+2*x[1]*y[1]
    plus=[Q(1,16),Q(1,4)];minus=[Q(1,16),-Q(1,4)]
    need(prod(plus,plus)==[2*a for a in plus],'known_pair:positive_sign_Virasoro_product')
    need(prod(minus,minus)==[2*a for a in minus],'known_pair:negative_sign_Virasoro_product')
    need(prod(plus,minus)==[0,0] and form(plus,minus)==0,'known_pair:orthogonal_weight_two_pair')
    need(form(plus,plus)==form(minus,minus)==Q(1,4),'known_pair:both_charges_one_half')
    return {'basis_norms':[32,2],'Ising_plus':plus,'Ising_minus':minus,
            'full_lattice_or_moonshine_VOA_simulated':False}


def conclude_checks():
    # These statements are bookkeeping, not independent classification proofs.
    eps=Q(1,32768)
    need(Q(19,5)-eps>Q(33,10),'selection:score_threshold_excludes_nonIsing_critical_values')
    need(eps>0,'selection:positive_sufficient_separation_from_any_other_candidate')
    return {'conditional_identification_target':'underlying VOA is V^natural',
            'source_classification_theorem':'Abe-Lam-Yamada Theorem A.1 (2017)',
            'source_overlap_theorem':'Sakuma Theorems 4.3-4.4',
            'bare_holomorphic_spectral_assumptions_force_pair_established':False,
            'new_classification_theorem_claimed':False,
            'robust_corollary_priority_established':False,
            'errors_apply_to_approximate_VOA_axioms':False}


def stringify(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:stringify(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [stringify(z) for z in x]
    return x


def main():
    need(hashlib.sha256(Path(v.__file__).read_bytes()).hexdigest()==
         'cefc291c6be9de9518037d353dc9b25857735963fb8747aea579bce41cc24fdb',
         'dependency:preserved_exact_Virasoro_helper')
    charge=charge_and_gram_checks();local=localization_checks();overlap=overlap_checks()
    controls=[tensor_product_control(48,Q(1,2)),tensor_product_control(30,Q(4,5))]
    known=known_pair_checks();conclusion=conclude_checks()
    report={'status':'PASS within exact normalization/rounding/scope-control checks',
            'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,
            'charge_and_Gram_certificate':charge,'localization_bounds':local,
            'overlap_certificate':overlap,'tensor_product_controls':controls,
            'known_lattice_pair_control':known,'conclusions':conclusion,
            'largest_square_matrix_dimension':4,'largest_coefficient_vector_dimension':48,
            'arithmetic':'integers and fractions only','full_Monster_tensor_constructed':False,
            'source_theorems_formally_verified':False,'independent_specialist_review':False}
    print(json.dumps(stringify(report),sort_keys=True,indent=2))


if __name__=='__main__':main()
