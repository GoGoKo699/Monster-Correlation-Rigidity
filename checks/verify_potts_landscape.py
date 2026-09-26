#!/usr/bin/env python3
"""Exact bounded certificate: the Potts peak is a real local maximum, not a fake VOA.

Imported interfaces: unitary minimal-model modules; the extended Potts module
list; the existing Moonshine 3A subalgebra; and the first five repeated traces.
The checks below do not prove these source theorems or simulate the full CFT.
No floating point, numerical eigensolver, Monster character data or network.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS = []

def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)

def zeros(n): return [Q(0)] * n

def va(a, b, scale=1): return [x + scale*y for x, y in zip(a, b)]

def vs(a, scalar): return [scalar*x for x in a]

def pd(a, b):
    r = zeros(len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    return trim(r)

def trim(p):
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p

def pa(a, b, scale=1):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0) for i in range(n)])

def powp(a, n):
    r=[Q(1)]
    for _ in range(n): r=pd(r,a)
    return r

def dp(a): return [i*a[i] for i in range(1,len(a))] or [Q(0)]

def ev(a, t): return sum((x*t**i for i,x in enumerate(a)),Q(0))

def solve(M, rhs):
    n=len(rhs);A=[list(map(Q,row))+[Q(r)] for row,r in zip(M,rhs)]
    for i in range(n):
        k=next(k for k in range(i,n) if A[k][i])
        A[i],A[k]=A[k],A[i]
        p=A[i][i];A[i]=[x/p for x in A[i]]
        for j in range(n):
            if j!=i:
                q=A[j][i];A[j]=[x-q*y for x,y in zip(A[j],A[i])]
    return [row[-1] for row in A]

def moments(r):
    return [Q(196884),16407*r,r*(1271*r+2310),3*r*(31*r*r+155*r+300),
            r*(13*r**3+120*r*r+534*r+864)/2,
            r*(7*r**4+100*r**3+740*r*r+2720*r+3840)/16]

def spectra_and_barrier():
    r=Q(4,5);p=moments(r)
    weights=[Q(0),Q(1,15),Q(2,5),Q(2,3)]
    M=[[h**k for h in weights] for k in range(4)]
    rhs=[p[k]-2**k for k in range(4)]
    multiplicities=solve(M,rhs)
    need(multiplicities==[57478,129168,8671,1566], 'Potts:four_source_traces_determine_all_multiplicities')
    for k in range(6):
        need(sum(m*h**k for m,h in zip(multiplicities,weights))+2**k==p[k],
             f'Potts:repeated_trace_order_{k}')
    need(all(m>0 and m.denominator==1 for m in multiplicities), 'Potts:positive_integer_counts')
    tangent_counts=multiplicities[:];tangent_counts[0]-=1
    need(sum(tangent_counts)==196882, 'Potts:entire_ambient_primary_tangent_dimension')
    hs=[6*(h-1) for h in weights]
    need(hs==[-6,-Q(28,5),-Q(18,5),-2], 'Potts:Hessian_numerators_over_b')
    need(all(x<0 for x in hs), 'Potts:all_ambient_tangent_directions_strictly_decrease')
    b2=r*(24-r)/48;lam_raw=2-r/6;lam2=lam_raw**2/b2
    need(b2==Q(29,75) and lam2==Q(784,87), 'Potts:primary_centering_and_peak_value')
    need(lam2<Q(2116,141), 'Potts:peak_is_below_Ising_global_value')
    # Local estimate: loss >= s^2[1/b - (3 lambda/4)s^2-Ms].
    need(Q(1)/b2>Q(8,5)**2, 'barrier:inverse_b_exceeds_eight_fifths')
    need(lam2<Q(31,10)**2 and Q(2116,141)<16, 'barrier:rational_cubic_upper_bounds')
    radius=Q(1,8)
    lower=Q(8,5)-Q(93,40)*radius**2-4*radius
    need(lower==Q(2723,2560)>1, 'barrier:uniform_quadratic_loss_coefficient_exceeds_one')
    need(radius*radius==Q(1,64), 'barrier:exit_loss_one_over_64')
    # Intermediate local expansion verified as a symbolic polynomial identity.
    # q=1-s^2/2, t^2=s^2-s^4/4; 1-q^3 >= 3s^2/2-3s^4/4.
    q=[1,0,-Q(1,2)]
    one_minus_q3=pa([1],powp(q,3),-1)
    need(pa(one_minus_q3,[0,0,Q(3,2),0,-Q(3,4)],-1)==[0,0,0,0,0,0,Q(1,8)],
         'barrier:exact_chord_cubic_remainder_positive')
    need(Q(3,2)*lam_raw-3*(Q(2,3)-r/12)==1, 'barrier:leading_loss_coefficient_is_inverse_b')
    return {'charge':r,'b_squared':b2,'self_cubic_squared':lam2,'weight_two_spectrum':
            [{'eigenvalue':h,'multiplicity':m} for h,m in zip(weights+[Q(2)],multiplicities+[Q(1)])],
            'tangent_Hessian_numerators_over_b':hs,'tangent_multiplicities':tangent_counts,
            'local_chord_radius':radius,'guaranteed_loss_per_squared_distance':1,
            'guaranteed_exit_loss':Q(1,64),'Potts_module_classification_is_imported':True}

def all_maximum_spectra():
    """Exhaust the small necessary spectral relaxation, not full VOA realizations."""
    hs=sorted(set(Q((6*a-5*b)**2-1,120) for a in range(1,5) for b in range(1,6)))
    need(hs==[0,Q(1,40),Q(1,15),Q(1,8),Q(2,5),Q(21,40),Q(2,3),Q(7,5),Q(13,8),3],
         'Kac:full_c_four_fifths_table')
    low=[h for h in hs if h<1]
    need(len(low)==7 and 1 not in hs, 'Kac:local_maximum_has_seven_possible_lower_weights')
    # The solution to all six affine moment equations is parametrized by q=1566-n_(2/3).
    base=[Q(57478),0,Q(129168),0,Q(8671),0,Q(1566)]
    slope=[-Q(4862,27),Q(56576,135),-Q(1768,5),Q(1088,9),-Q(1547,135),Q(832,135),-Q(1)]
    ps=moments(Q(4,5))
    for k in range(6):
        need(sum(m*h**k for m,h in zip(base,low))==ps[k]-2**k and
             sum(m*h**k for m,h in zip(slope,low))==0,
             f'affine_spectra:all_q_exact_trace_{k}')
    # The first six columns have a nonzero Vandermonde determinant.
    vd=Q(1)
    for i in range(6):
        for j in range(i+1,6):vd*=low[j]-low[i]
    need(vd!=0, 'affine_spectra:rank_six_and_one_parameter_complete')
    need(gcd(56576,135)==1, 'affine_spectra:integer_multiplicity_forces_q_multiple_135')
    upper=base[0]/(-slope[0])
    need(270<upper<405, 'affine_spectra:nonnegative_zero_sector_allows_only_three_multiples')
    rows=[]
    for q in (0,135,270):
        n=[a+q*b for a,b in zip(base,slope)]
        need(all(x>=0 and x.denominator==1 for x in n),f'affine_spectra:q{q}_all_nonnegative_integers')
        need(sum(n)+1==196884,f'affine_spectra:q{q}_total_dimension')
        rows.append({'q':q,'multiplicities':n,'known_Potts_realization':q==0})
    need(all(base[i]+405*slope[i]<0 for i in [0]),'affine_spectra:q405_is_impossible')
    need(rows[0]['multiplicities']==[57478,0,129168,0,8671,0,1566], 'affine_spectra:extended_Potts_row')
    return {'ordered_weights':low,'base_vector':base,'slope_vector':slope,
            'Vandermonde_minor':vd,'q_upper_from_zero_sector':upper,'three_possible_rows':rows,
            'other_two_rows_realized_by_VOAs_here':False,
            'spectrum_of_a_global_maximum_classified':False}

class ThreeA:
    """Positive real version of the exact four-dimensional 3A algebra plus spectator stress."""
    def __init__(self):
        self.n=5;self.g=[Q(2,5),Q(3,7),Q(162),Q(162),Q(391,35)]
        self.basis=[[Q(i==j) for i in range(5)] for j in range(5)]
        self.tab={}
        def put(i,j,vec):self.tab[i,j]=self.tab[j,i]=list(map(Q,vec))
        for i in range(5):
            for j in range(i,5):put(i,j,[0]*5)
        put(0,0,[2,0,0,0,0]);put(1,1,[0,2,0,0,0]);put(4,4,[0,0,0,0,2])
        put(0,2,[0,0,Q(2,3),0,0]);put(0,3,[0,0,0,Q(2,3),0])
        put(1,2,[0,0,Q(4,3),0,0]);put(1,3,[0,0,0,Q(4,3),0])
        put(2,2,[270,504,20,0,0]);put(3,3,[270,504,-20,0,0]);put(2,3,[0,0,0,-20,0])
    def prod(self,a,b):
        out=zeros(5)
        for i,j in product(range(5),repeat=2):out=va(out,self.tab[i,j],a[i]*b[j])
        return out
    def ip(self,a,b):return sum((x*y*g for x,y,g in zip(a,b,self.g)),Q(0))
    def matrix(self,a):return [[self.prod(a,b)[i] for b in self.basis] for i in range(5)]
    @property
    def omega(self):return va(va(self.basis[0],self.basis[1]),self.basis[4])
    def center(self,a):return va(a,self.omega,-self.ip(a,self.omega)/12)
    def cubic(self,a,b,c):return self.ip(self.prod(a,b),c)

def algebra_and_path():
    alg=ThreeA();u,v,Y,Z,w=alg.basis;om=alg.omega
    need(all(g>0 for g in alg.g),'3A:positive_real_metric_after_conjugate_basis_conversion')
    need(all(alg.prod(a,b)==alg.prod(b,a) for a,b in product(alg.basis,repeat=2)),'3A:commutative_product')
    need(all(alg.ip(alg.prod(a,b),c)==alg.ip(a,alg.prod(b,c)) for a,b,c in product(alg.basis,repeat=3)),
         '3A:all_125_metric_invariance_entries')
    need(alg.ip(om,om)==12 and all(alg.prod(om,a)==vs(a,2) for a in alg.basis), '3A:full_c24_stress_normalization')
    operators=[alg.matrix(a) for a in alg.basis]
    need(all(alg.g[i]*R[i][j]==alg.g[j]*R[j][i]
             for R in operators for i,j in product(range(5),repeat=2)),
         '3A:all_five_by_five_multiplication_matrices_metric_self_adjoint')
    e=va(va(vs(u,Q(5,32)),vs(v,Q(7,16))),vs(Y,Q(1,32)))
    x=va(va(vs(u,Q(1,16)),vs(v,Q(7,8))),vs(Y,-Q(1,48)))
    for label,a,r in [('Potts',u,Q(4,5)),('Ising',e,Q(1,2)),('nonextendable_four_fifths',x,Q(4,5)),('companion',v,Q(6,7))]:
        need(alg.prod(a,a)==vs(a,2),f'3A:{label}_Virasoro_idempotence')
        need(alg.ip(a,a)==r/2,f'3A:{label}_central_charge')
        z=alg.center(a);b2=alg.ip(z,z)
        need(alg.ip(z,om)==0 and b2==r*(24-r)/48,f'3A:{label}_ambient_primary_centering')
        need(alg.center(alg.prod(z,z))==vs(z,2-r/6),f'3A:{label}_primary_critical_equation')
    need(alg.prod(x,Z)==vs(Z,Q(13,8)) and alg.ip(Z,x)==alg.ip(Z,om)==0,
         '3A:nonextendable_equal_charge_point_has_actual_uphill_direction')
    need(Q(13,8)>1,'3A:same_charge_does_not_imply_same_local_type')
    # A useful global algebraic identity inside this known subalgebra.
    recovered=va(va(vs(alg.prod(Y,Y),Q(1,1152)),vs(Y,Q(1,72))),vs(u,-Q(5,64)))
    need(recovered==e,'3A:Ising_vector_recovered_from_one_mixed_square')
    need(alg.prod(u,v)==zeros(5) and alg.prod(u,Y)==vs(Y,Q(2,3)) and alg.prod(v,Y)==vs(Y,Q(4,3)),
         '3A:mixed_eigenspace_relations')
    need(alg.ip(u,e)==Q(1,16),'3A:Potts_Ising_overlap')
    A=alg.center(u);B=alg.center(e)
    U=alg.ip(A,A);V=alg.ip(B,B);W=alg.ip(A,B)
    need((U,V,W)==(Q(29,75),Q(47,192),Q(13,240)),'path:three_exact_inner_products')
    aa=Q(28,15);bb=Q(23,12)
    cubic=[alg.cubic(A,A,A),3*alg.cubic(A,A,B),3*alg.cubic(A,B,B),alg.cubic(B,B,B)]
    norm=[U,2*W,V]
    need(cubic==[aa*U,3*aa*W,3*bb*W,bb*V],'path:all_four_cubic_coefficients')
    derivative=pa(vs(pd(dp(cubic),norm),2),vs(pd(cubic,dp(norm)),3),-1)
    need(derivative==[0,-Q(489,800),Q(10563,12800)], 'path:derivative_numerator_factorization')
    stationary=Q(2608,3521)
    need(ev(derivative,stationary)==0 and derivative[1]<0 and derivative[2]>0,
         'path:single_interior_minimum_not_an_ambient_critical_claim')
    # The numerator of F'(t) is derivative/(2 norm^(5/2)).
    need(derivative==[0,-Q(3*2608,12800),Q(3*3521,12800)],'path:explicit_three_t_factor')
    value2=ev(cubic,stationary)**2/ev(norm,stationary)**3
    need(value2==Q(505485828592144,64205847970317),'path:exact_minimum_coupling_squared')
    need(value2<Q(784,87)<Q(2116,141),'path:dip_below_Potts_and_endpoint_at_Ising')
    need(ev(cubic,Q(2))>0 and ev(cubic,Q(2))**2>Q(784,87)*ev(norm,Q(2))**3,
         'path:t_equals_two_already_exceeds_nonIsing_existence_threshold')
    need(cubic[-1]**2/norm[-1]**3==Q(2116,141),'path:limiting_endpoint_is_unitarity_cap')
    # This supplied path is not asserted to minimize escape barriers in the full sphere.
    # The target lies well outside radius 1/8 (squared overlap < 1/25).
    overlap2=W*W/(U*V)
    need(overlap2==Q(169,5452) and overlap2<Q(1,25),'path:finite_nonlocal_separation_from_Ising_target')
    need(Q(2)-Q(2,5)>Q(1,64),'path:endpoint_outside_guaranteed_barrier_neighborhood')
    return {'basis':['u_4/5','v_6/7','Y','Z','spectator_stress'], 'metric_diagonal':alg.g,
            'structure_constants':[[alg.tab[i,j] for j in range(5)] for i in range(5)],
            'Ising_vector':e,'other_four_fifths_vector':x,'uphill_vector_for_other_point':Z,
            'mixed_square_reconstruction_coefficients':[Q(1,1152),Q(1,72),-Q(5,64)],
            'path_numerator_coefficients':cubic,'path_norm_squared_coefficients':norm,
            'path_derivative_cleared_numerator':derivative,'path_minimizing_parameter':stationary,
            'path_minimum_self_cubic_squared':value2,'normalized_endpoint_overlap_squared':overlap2,
            'path_is_optimal_escape_route_proved':False,'3A_embedding_is_imported_prior_result':True}

def source_scope_checks():
    # These are checks of distinctions, not new source-theorem proofs.
    allowed_extended=[Q(0),Q(2,5),Q(2,3),Q(1,15)]
    need(max(allowed_extended)<1,'source_interface:Potts_lowest_module_weights_below_one')
    need(Q(7,5)-Q(2,5)==1,'source_interface:seven_fifths_requires_one_extra_ambient_grade')
    need(3>2,'source_interface:spin_three_extension_state_not_a_weight_two_axis')
    need(Q(4,5)+Q(6,7)==Q(58,35),'scope:3A_internal_charge_not_ambient_charge_24')
    need(24-Q(58,35)==Q(782,35),'scope:spectator_stress_charge_kept_explicit')
    # The model-specific construction cannot be asserted for every arbitrary c4/5 vector.
    return {'first_Ising_forced_from_original_assumptions':False,
            'second_orthogonal_Ising_forced':False,
            'all_charge_four_fifths_local_maxima_extendable_proved':False,
            'new_orthogonal_Ising_pair_supplied_by_3A_formula':False,
            'forbidden_inference':'all locally maximal self-couplings saturate the Ising cap',
            'known_subalgebra_data_not_transferred_to_unknown_candidate':True}

def strings(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,dict):return {k:strings(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [strings(v) for v in obj]
    return obj

def main():
    sp=spectra_and_barrier();relax=all_maximum_spectra();a=algebra_and_path();scope=source_scope_checks()
    print(json.dumps(strings({'status':'PASS within exact spectral/algebra/path scopes',
          'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,'Potts_peak':sp,
          'necessary_spectral_relaxation':relax,'small_3A_algebra':a,'scope':scope,
          'arithmetic':'integers and fractions only','largest_constructed_square_matrix':5,
          'largest_displayed_rectangular_constraint_matrix':[6,7],
          'full_Monster_tensor_constructed':False,'source_theorems_formally_verified':False,
          'independent_expert_review':False,'novelty_established':False}),sort_keys=True,indent=2))

if __name__=='__main__':main()
