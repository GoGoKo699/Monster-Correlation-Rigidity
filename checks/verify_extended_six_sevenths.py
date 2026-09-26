#!/usr/bin/env python3
"""Exact bounded certificate for the extended-6/7 sufficient Ising criterion.

Imported hypotheses: the extremal repeated trace identities, unitary Kac
classification, and the W(6/7) ordinary-module theorem. Finite arithmetic is
not a proof of those results or a full VOA construction. No floating point,
optimization package, network, or Monster character table is used here.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
import json

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]


def need(ok,label):
    if not bool(ok): raise RuntimeError(label)
    LABELS.append(label)


def solve(M,b):
    n=len(b);a=[list(map(Q,row))+[Q(t)] for row,t in zip(M,b)]
    for i in range(n):
        j=next(j for j in range(i,n) if a[j][i])
        a[i],a[j]=a[j],a[i];v=a[i][i];a[i]=[x/v for x in a[i]]
        for j in range(n):
            if j!=i:
                v=a[j][i];a[j]=[x-v*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]


def padd(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]


def pmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def pscale(a,x):return [x*y for y in a]
def ppower(a,n):
    out=[Q(1)]
    for _ in range(n):out=pmul(out,a)
    return out

def peval(a,x):return sum((t*x**i for i,t in enumerate(a)),Q(0))


def moments(r):
    return [Q(196884),16407*r,r*(1271*r+2310),3*r*(31*r*r+155*r+300),
            r*(13*r**3+120*r*r+534*r+864)/2,
            r*(7*r**4+100*r**3+740*r*r+2720*r+3840)/16]


def kac(m):
    return sorted(set(Q(((m+1)*a-m*b)**2-1,4*m*(m+1))
                      for a in range(1,m) for b in range(1,m+1)))


def spectral_certificate():
    h=list(map(Q,['0','1/21','1/7','10/21','5/7','4/3']))
    p=moments(Q(6,7));rhs=[a-2**k for k,a in enumerate(p)]
    M=[[x**k for x in h] for k in range(6)]
    n=solve(M,rhs)
    need(n==[35973,123556,29394,7176,782,2],'extension:unique_six_eigenvalue_multiplicities')
    for k in range(6):
        need(sum(x**k*z for x,z in zip(h,n))+2**k==p[k],f'extension:repeated_trace_{k}')
    need(all(x>0 and x.denominator==1 for x in n),'extension:positive_integral_dimensions')
    determinant=Q(1)
    for i in range(6):
        for j in range(i+1,6):determinant*=h[j]-h[i]
    need(determinant!=0,'extension:Vandermonde_is_nonsingular')
    poly=[Q(1)]
    for x in h[:-1]:poly=pmul(poly,[-x,1])
    denominator=peval(poly,h[-1]);poly=pscale(poly,1/denominator)
    need(denominator==Q(2600,2401),'extension:projector_normalization')
    need(poly==[0,Q(1,468),-Q(7,104),Q(12397,23400),-Q(9947,7800),Q(2401,2600)],
         'extension:degree_five_projector_coefficients')
    need([peval(poly,x) for x in h]==[0,0,0,0,0,1],'extension:exact_spectral_projector_values')
    need(sum(a*b for a,b in zip(poly,rhs))==2,'extension:projector_trace_two')
    need(Q(12,7)-Q(5,7)==1,'extension:excluded_companion_needs_ambient_weight_one')
    need(Q(22,7)>2 and 5>2,'extension:other_companions_above_weight_two')
    need(3+2*3==9,'extension:nine_modules_but_six_distinct_lowest_weights')
    tang=n[:];tang[0]-=1
    need(sum(tang)==196882 and sum(tang[:-1])==196880 and tang[-1]==2,
         'extension:two_positive_and_remaining_negative_tangent_directions')
    return {'weights':h,'multiplicities':n,'trace_inputs':p,'Vandermonde':M,
            'Vandermonde_determinant':determinant,'projector_coefficients':poly,
            'projector_trace':2,'module_classification_is_imported':True}


def threshold_certificate():
    h=list(map(Q,['0','3/80','1/10','7/16','3/5','3/2']))
    p=moments(Q(7,10));M=[[x**k for x in h] for k in range(6)]
    n=solve(M,[z-2**k for k,z in enumerate(p)])
    need(n==[51054,91392,47634,4864,1938,1],'threshold:tricritical_multiplicities')
    for k in range(6):need(sum(x**k*y for x,y in zip(h,n))+2**k==p[k],f'threshold:trace_{k}')
    need(n[-1]==1 and h[-1]>1,'threshold:compulsory_uphill_tricritical_direction')
    need(all(x<1 for x in h[:-1]),'threshold:all_other_tricritical_directions_decrease')
    need(kac(4)==h,'threshold:Kac_weights_match_tricritical_list')
    charges=[1-Q(6,m*(m+1)) for m in range(3,8)]
    need(charges[:3]==[Q(1,2),Q(7,10),Q(4,5)],'threshold:first_three_unitary_charges')
    r=Q(4,5);b2=r*(24-r)/48
    need((2-r/6)**2/b2==Q(784,87),'threshold:no_Ising_cap_squared')
    # Derivative numerator of lambda(r)=(2-r/6)/sqrt(r(24-r)/48).
    b=[Q(0),Q(1,2),-Q(1,48)];N=[Q(2),-Q(1,6)];db=[Q(1,2),-Q(1,24)]
    numerator=padd(pscale(b,-Q(1,6)),pscale(pmul(N,db),-Q(1,2)))
    need(numerator==[-Q(1,2),0,0],'threshold:critical_value_strictly_decreasing')
    return {'tricritical_weights':h,'multiplicities':n,'Vandermonde':M,
            'unitary_charge_sample':charges,'non_Ising_global_bound_squared':Q(784,87),
            'global_maximum_existence_and_unitary_classification_are_analytic_inputs':True}


def trial_certificate():
    r=Q(6,7);b=Q(9,14);a=Q(26,9);beta=Q(53,27)
    need(b*b==r*(24-r)/48,'trial:ambient_normalization_is_rational')
    need((2-r/6)/b==a,'trial:centered_self_coupling')
    need((Q(4,3)-r/12)/b==beta,'trial:mixed_coupling_from_response_eigenvalue')
    q,t=Q(4,5),Q(3,5)
    need(q*q+t*t==1,'trial:both_signs_are_unit_primaries')
    constant=a*q**3+3*beta*q*t*t;odd=t**3
    need(constant==Q(3572,1125) and odd==Q(27,125),'trial:exact_two_sign_coefficients')
    plus=[constant,odd];minus=[constant,-odd]
    need(pscale(padd(plus,minus),Q(1,2))==[constant,0],'trial:unknown_self_cubic_cancels_symbolically')
    need(constant>Q(31,10) and Q(31,10)**2>Q(784,87),'trial:strict_no_Ising_bound_violation')
    need(constant**2-Q(784,87)==Q(39266336,36703125),'trial:exact_squared_margin')
    for k in [Q(0),Q(1),-Q(1),Q(7,3),-Q(11,5)]:
        need(max(peval(plus,k),peval(minus,k))>=constant,f'trial:sign_control_k{k}')
    # The numerical maximum in the plane is not used as an algorithm or premise.
    q2=beta/(3*beta-a)
    need(q2==Q(53,81) and 0<q2<1,'trial:optional_average_optimum_is_interior')
    need(4*beta**3/(3*beta-a)>constant**2,'trial:simple_four_three_choice_is_sufficient_not_optimal')
    return {'a_self_cubic':a,'a_y_y_coupling':beta,'mixing_coefficients':[q,t],
            'self_couplings_formal_in_k':[plus,minus],'average':constant,
            'squared_margin':constant**2-Q(784,87),'Ising_trial_field_itself_claimed':False}


def polarized_traces(r,s):
    S={j:[r/2]+[Q(0)]*(j-1)+[s/2] for j in range(1,6)}
    def term(c,*factors):
        p=[Q(c)]
        for f in factors:p=pmul(p,f)
        return p
    T={0:[Q(196884)],1:term(32814,S[1]),
       2:padd(term(4620,S[2]),term(5084,S[1],S[1])),
       3:padd(padd(term(1800,S[3]),term(1860,S[2],S[1])),term(744,S[1],S[1],S[1]))}
    for degree,terms in [(4,[(864,[4]),(912,[3,1]),(156,[2,2]),(480,[2,1,1]),(104,[1,1,1,1])]),
                         (5,[(480,[5]),(520,[4,1]),(160,[3,2]),(280,[3,1,1]),(90,[2,2,1]),(100,[2,1,1,1]),(14,[1,1,1,1,1])])]:
        T[degree]=[Q(0)]
        for c,ks in terms:T[degree]=padd(T[degree],term(c,*[S[j] for j in ks]))
    return T,{(n-b,b):a/Q(comb(n,b)) for n,p in T.items() for b,a in enumerate(p)}


def missing_shared_sector_control():
    r,s=Q(4,5),Q(6,7);T,mixed=polarized_traces(r,s)
    hs=list(map(Q,['0','1/15','2/5','2/3']))
    ks=list(map(Q,['0','1/21','1/7','10/21','5/7','4/3']))
    table=[[9019,38200,7554,2460,242,2],[25200,78192,20700,4536,540,0],
           [1303,6300,888,180,0,0],[450,864,252,0,0,0]]
    for (a,b),value in mixed.items():
        z=sum(Q(table[i][j])*h**a*k**b for i,h in enumerate(hs) for j,k in enumerate(ks))
        z+=2**a*int(b==0)+2**b*int(a==0)
        need(z==value,f'shared_relaxation:exact_mixed_moment_{a}_{b}')
    need(table[-1][-1]==0,'shared_relaxation:desired_shared_sector_absent')
    need(sum(row[-1] for row in table)==2,'shared_relaxation:forced_four_thirds_space_still_present')
    need(all(n>=0 and isinstance(n,int) for row in table for n in row),'shared_relaxation:all_counts_nonnegative_integers')
    need(sum(map(sum,table))+2==196884,'shared_relaxation:full_weight_two_dimension')
    for i in range(6):
        need(mixed[(i,0)]==moments(r)[i] and mixed[(0,i)]==moments(s)[i],f'shared_relaxation:both_marginals_{i}')
    return {'row_weights':hs,'column_weights':ks,'multiplicities':table,
            'extra_stress_directions':[[2,0,1],[0,2,1]],
            'polarized_trace_polynomial_coefficients':T,
            'mixed_moments':{f'{a},{b}':z for (a,b),z in mixed.items()},
            'this_table_constructs_a_VOA':False,'this_table_excludes_all_Ising_vectors':False}


def scope_controls():
    hs=list(map(Q,['0','1/56','1/21','5/56','1/7','3/8','10/21','33/56','5/7']))
    ns=[8153,62974,68688,26908,21287,2244,5670,34,925]
    for k,p in enumerate(moments(Q(6,7))):
        need(sum(h**k*n for h,n in zip(hs,ns))+2**k==p,f'bare_control:moment_{k}')
    need(all(h in kac(6) and h<1 for h in hs),'bare_control:allowed_unitary_weights_below_one')
    need(all(n>0 for n in ns) and sum(ns)+1==196884,'bare_control:integral_full_dimension')
    need(Q(4,3) not in hs,'bare_control:extension_cannot_be_omitted_from_proof')
    # An actual outside-class tensor product, checked only on its weight-two algebra.
    count=28;r=Q(6,7);charges=[r]*count
    need(sum(charges)==24,'tensor_control:total_central_charge_twenty_four')
    need(count!=196884,'tensor_control:extremal_character_not_satisfied')
    need(Q(1,2)/r not in list(range(29)),'tensor_control:no_sum_of_factor_charges_is_Ising')
    omega=[Q(1)]*count;e=[Q(1)]+[Q(0)]*(count-1)
    def ip(a,b):return sum(r*x*y/2 for x,y in zip(a,b))
    def prod(a,b):return [2*x*y for x,y in zip(a,b)]
    need(prod(e,e)==[2*x for x in e] and ip(e,e)==r/2,'tensor_control:extendable_factor_charge')
    need(ip(omega,omega)==12,'tensor_control:ambient_stress_norm')
    a=[x-r*z/24 for x,z in zip(e,omega)];norm=ip(a,a)
    need(ip(a,omega)==0 and norm==Q(81,196),'tensor_control:primary_centering')
    need(ip(prod(a,a),a)**2/norm**3==Q(676,81),'tensor_control:same_charge_critical_cubic')
    need(2!=moments(r)[1],'tensor_control:ambient_trace_hypothesis_fails')
    return {'bare_Virasoro_relaxation':{'weights':hs,'multiplicities':ns,'extra_eigenvalue_two':1,'VOA_realization_proved':False},
            'outside_class_model':'W(6/7) tensor power 28','holomorphic':False,
            'weight_two_dimension':28,'full_tensor_product_constructed':False}


def small_model_controls():
    # Prior 3A table, used only as a normalization control, never to prove necessity.
    g=list(map(Q,['2/5','3/7','162','162','391/35']))
    basis=[[Q(i==j) for i in range(5)] for j in range(5)]
    table={}
    def put(i,j,z):table[i,j]=table[j,i]=list(map(Q,z))
    for i in range(5):
        for j in range(i,5):put(i,j,[0]*5)
    put(0,0,[2,0,0,0,0]);put(1,1,[0,2,0,0,0]);put(4,4,[0,0,0,0,2])
    put(0,2,[0,0,Q(2,3),0,0]);put(0,3,[0,0,0,Q(2,3),0])
    put(1,2,[0,0,Q(4,3),0,0]);put(1,3,[0,0,0,Q(4,3),0])
    put(2,2,[270,504,20,0,0]);put(3,3,[270,504,-20,0,0]);put(2,3,[0,0,0,-20,0])
    def mul(a,b):return [sum(a[i]*b[j]*table[i,j][k] for i,j in product(range(5),repeat=2)) for k in range(5)]
    def ip(a,b):return sum(x*y*z for x,y,z in zip(a,b,g))
    def add(a,b,t=1):return [x+t*y for x,y in zip(a,b)]
    def scale(a,t):return [t*x for x in a]
    u,v,Y,Z,w=basis;omega=add(add(u,v),w);a=scale(add(v,omega,-Q(1,28)),Q(14,9))
    need(all(ip(mul(x,y),z)==ip(x,mul(y,z)) for x,y,z in product(basis,repeat=3)),
         'known_control:all_small_metric_invariance_entries')
    need(ip(a,a)==1 and ip(a,omega)==0 and ip(mul(a,a),a)==Q(26,9),'known_control:normalized_companion_primary')
    for label,y in [('Y',Y),('mixed',scale(add(scale(Y,3),scale(Z,4)),Q(1,5)))]:
        need(mul(v,y)==scale(y,Q(4,3)) and ip(y,a)==ip(y,omega)==0,f'known_control:{label}_ambient_primary_response')
        need(ip(mul(a,y),y)/ip(y,y)==Q(53,27) and ip(mul(a,a),y)==0,
             f'known_control:{label}_normalized_even_cubic_data')
    return {'small_real_algebra_dimension':5,'full_extremal_algebra_constructed':False,
            'known_table_is_premise_of_main_proof':False}


def strings(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,dict):return {str(k):strings(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [strings(v) for v in obj]
    return obj


def main():
    spectrum=spectral_certificate();threshold=threshold_certificate();trial=trial_certificate()
    joint=missing_shared_sector_control();controls=scope_controls();model=small_model_controls()
    print(json.dumps(strings({'status':'PASS within exact spectrum/trial/relaxation scopes','base_commit':BASE,
       'checks':len(LABELS),'labels':LABELS,'extended_sector':spectrum,'no_Ising_threshold':threshold,
       'two_sign_trial':trial,'joint_spectral_relaxation':joint,'scope_controls':controls,'known_small_control':model,
       'arithmetic':'integers and fractions only','largest_square_matrix_dimension':6,
       'largest_coefficient_vector_dimension':28,'full_Monster_tensor_constructed':False,
       'bare_assumptions_force_extended_six_sevenths_proved':False,'orthogonal_Ising_partner_proved':False,
       'source_classification_theorems_formally_verified':False,'novelty_established':False}),sort_keys=True,indent=2))


if __name__=='__main__':main()
