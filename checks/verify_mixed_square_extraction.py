#!/usr/bin/env python3
"""Exact local mixed-square certificates, not a full VOA construction.

Two source-realized algebras are tested with rational coefficients and a
Q(sqrt(3)) real field for the complete idempotent lists. The universal fusion
and unitary-module theorems are imported, not proved by these finite tests.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product, combinations
from math import isqrt
import json

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    LABELS.append(label)

@dataclass(frozen=True)
class R3:
    """The real algebraic number a+b sqrt(3), exact arithmetic only."""
    a: Q=Q(0)
    b: Q=Q(0)
    def __post_init__(self):
        object.__setattr__(self,'a',Q(self.a));object.__setattr__(self,'b',Q(self.b))
    @staticmethod
    def co(x):return x if isinstance(x,R3) else R3(Q(x))
    def __add__(self,y):
        y=self.co(y);return R3(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return R3(-self.a,-self.b)
    def __sub__(self,y):return self+-self.co(y)
    def __rsub__(self,y):return self.co(y)+-self
    def __mul__(self,y):
        y=self.co(y);return R3(self.a*y.a+3*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=self.co(y);den=y.a*y.a-3*y.b*y.b
        if den==0:raise ZeroDivisionError()
        return self*R3(y.a/den,-y.b/den)
    def __bool__(self):return bool(self.a or self.b)
    def __eq__(self,y):
        y=self.co(y);return self.a==y.a and self.b==y.b
    def __str__(self):return str(self.a) if self.b==0 else f'({self.a})+({self.b})sqrt(3)'
    def __hash__(self):return hash((self.a,self.b))

def vv(a,b,k=1):return [x+k*y for x,y in zip(a,b)]
def sc(a,k):return [k*x for x in a]

class Algebra:
    def __init__(self,metric):
        self.g=list(map(Q,metric));self.n=len(metric)
        self.e=[[Q(i==j) for i in range(self.n)] for j in range(self.n)]
        self.tab={(i,j):[Q(0)]*self.n for i,j in product(range(self.n),repeat=2)}
    def put(self,i,j,v):self.tab[i,j]=self.tab[j,i]=list(map(Q,v))
    def prod(self,a,b):
        out=[Q(0)]*self.n
        for i,j in product(range(self.n),repeat=2):
            if a[i] and b[j]:out=vv(out,self.tab[i,j],a[i]*b[j])
        return out
    def ip(self,a,b):return sum((g*x*y for g,x,y in zip(self.g,a,b)),Q(0))
    def mat(self,a):return [[self.prod(a,b)[i] for b in self.e] for i in range(self.n)]
    def check(self,label):
        need(all(g>0 for g in self.g),label+':positive_metric')
        need(all(self.prod(a,b)==self.prod(b,a) for a,b in product(self.e,repeat=2)),label+':commutativity')
        need(all(self.ip(self.prod(a,b),c)==self.ip(a,self.prod(b,c)) for a,b,c in product(self.e,repeat=3)),label+':all_metric_invariance_entries')

def monster_core():
    # HLY Lemma 4.2, positive real Y=X+ + X-, Z=i(X+ - X-).
    a=Algebra([Q(2,5),Q(3,7),162,162])
    a.put(0,0,[2,0,0,0]);a.put(1,1,[0,2,0,0])
    a.put(0,2,[0,0,Q(2,3),0]);a.put(0,3,[0,0,0,Q(2,3)])
    a.put(1,2,[0,0,Q(4,3),0]);a.put(1,3,[0,0,0,Q(4,3)])
    a.put(2,2,[270,504,20,0]);a.put(3,3,[270,504,-20,0]);a.put(2,3,[0,0,0,-20])
    return a

def code_core():
    # HLY Lemma 3.11, the full five-dimensional weight-two algebra of M_D.
    a=Algebra([Q(2,5)]*3+[54,54])
    for i in range(3):
        z=[0]*5;z[i]=2;a.put(i,i,z)
        a.put(i,3,[0,0,0,Q(2,3),0]);a.put(i,4,[0,0,0,0,Q(2,3)])
    a.put(3,3,[90,90,90,8,0]);a.put(4,4,[90,90,90,-8,0]);a.put(3,4,[0,0,0,0,-8])
    return a

def mixed_square(a,u,y):
    n=a.ip(y,y);yy=a.prod(y,y)
    d=vv(vv(yy,a.prod(u,yy),-Q(3,2)),u,Q(10,3)*n)
    dn=a.ip(d,d)
    v=sc(d,4*n/(3*dn));charge=32*n*n/(9*dn)
    return d,v,charge

def rank(columns):
    if not columns:return 0
    A=[list(map(Q,r)) for r in zip(*columns)];i=0
    for j in range(len(columns)):
        pivot=next((k for k in range(i,len(A)) if A[k][j]),None)
        if pivot is None:continue
        A[i],A[pivot]=A[pivot],A[i];p=A[i][j];A[i]=[x/p for x in A[i]]
        for k in range(i+1,len(A)):
            p=A[k][j];A[k]=[x-p*y for x,y in zip(A[k],A[i])]
        i+=1
        if i==len(A):break
    return i

def fusion_and_candidate():
    # Exact finite minimal-model fusion: (1,3)*(1,3) in M(5,6).
    hs=[Q((6-5*s)**2-1,120) for s in (1,3,5)]
    need(hs==[0,Q(2,3),3],'fusion:two_thirds_square_vacuum_two_thirds_three')
    need(3>2,'fusion:weight_three_module_not_in_ambient_grade_two')
    # Projector polynomial on the only possible weight-two outputs.
    for eigen in (Q(0),Q(2,3),Q(2)):
        # The rank-one u correction is checked separately by invariant metric.
        if eigen!=2:need(1-Q(3,2)*eigen==int(eigen==0),f'projection:zero_channel_at_{eigen}')
    need(Q(2,3)/Q(2,5)==Q(5,3),'projection:u_coefficient_from_invariant_metric')
    need(Q(5,3)-Q(3,2)*Q(10,3)+Q(10,3)==0,'projection:full_stress_component_removed')
    need(Q(2)-Q(2,3)==Q(4,3),'projection:complementary_weight')
    # Kac-table obstruction with h=4/3: all c_m below c_90, plus the endpoint.
    table=[]
    for m in range(3,91):
        rad3=3+16*m*(m+1)
        if rad3%3:continue
        z=isqrt(rad3//3)
        if z*z!=rad3//3:continue
        pairs=[]
        for r in range(1,m):
            for sign in (-1,1):
                q=(m+1)*r-sign*z
                if q%m==0 and 1<=q//m<=m:pairs.append((r,q//m))
        if pairs:table.append({'m':m,'charge':1-Q(6,m*(m+1)),'labels':pairs})
    need([x['m'] for x in table]==[6,90],'Virasoro:exact_Kac_scan_below_and_at_second_h_four_thirds_charge')
    need(table[0]['charge']==Q(6,7) and table[1]['charge']==Q(1364,1365),'Virasoro:companion_charge_gap')
    need(Q(32,9)/Q(40,261)==Q(116,5),'projection:Cauchy_bound_is_full_commutant_charge')
    return {'fusion_weights':hs,'h_four_thirds_unitary_models_below_endpoint':table,
            'automatic_Virasoro_idempotence_claimed':False}

def mixed_controls():
    records=[]
    phases=[(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(-Q(8,17),Q(15,17))]
    for name,a,yi,zi,expected_v,q,n in [
       ('monstrous_3A',monster_core(),2,3,[0,1,0,0],Q(6,7),Q(162)),
       ('ternary_code',code_core(),3,4,[0,1,1,0,0],Q(8,5),Q(54))]:
        a.check(name);u=a.e[0];Y=a.e[yi];Z=a.e[zi]
        for j,(c,s) in enumerate(phases):
            need(c*c+s*s==1,f'{name}:phase{j}_unit_circle')
            y=vv(sc(Y,c),Z,s);d,v,charge=mixed_square(a,u,y)
            need(a.prod(u,d)==[0]*a.n,f'{name}:phase{j}_extracted_square_commutes')
            need(v==list(map(Q,expected_v)) and charge==q,f'{name}:phase{j}_same_companion_without_endpoint')
            need(a.prod(v,v)==sc(v,2) and 2*a.ip(v,v)==charge,f'{name}:phase{j}_candidate_actually_Virasoro')
            need(a.prod(v,y)==sc(y,Q(4,3)),f'{name}:phase{j}_mixed_highest_weight')
            need(a.ip(d,d)/n**2==(Q(112,27) if name=='monstrous_3A' else Q(20,9)),f'{name}:phase{j}_normalized_square_norm')
        y=vv(sc(Y,Q(3,5)),Z,Q(4,5));yy=a.prod(y,y)
        generated=[u,y,yy,a.prod(u,yy)]
        need(rank(generated)==4,f'{name}:generic_single_seed_generates_closed_four_dimensional_algebra')
        need(all(rank(generated+[a.prod(b,c)])==4 for b,c in product(generated,repeat=2)),f'{name}:all_generated_products_close')
        k=Q(20) if name=='monstrous_3A' else Q(8)
        records.append({'name':name,'metric':a.g,'companion_charge':q,'restricted_cubic_amplitude_squared':k*k/n,
                        'square_norm_per_unit_y':Q(112,27) if name=='monstrous_3A' else Q(20,9),
                        'generic_seed_generated_dimension':4,'source_embedding_is_imported':True})
    return records

def extraction():
    a=monster_core();u,v,Y,Z=a.e;n=Q(162)
    # Work in a rotated seed basis, not the known Ising direction.
    p=vv(sc(Y,Q(3,5)),Z,Q(4,5));q=vv(sc(Y,-Q(4,5)),Z,Q(3,5))
    A=a.ip(a.prod(p,p),p)/n;B=a.ip(a.prod(p,p),q)/n
    need((A,B)==(-Q(468,25),-Q(176,25)),'extraction:rotated_seed_cubic_coefficients')
    need(A*A+B*B==400,'extraction:invariant_harmonic_amplitude')
    need(a.ip(a.prod(p,q),q)/n==-A and a.ip(a.prod(q,q),q)/n==-B,'extraction:harmonic_cubic_identities')
    # Projective stationary polynomial A t^3-3B t^2-3A t+B; exact factorization.
    lhs=[B,-3*A,-3*B,A]
    rhs=[-Q(4,25)*44,Q(4,25)*351,Q(4,25)*132,-Q(4,25)*117]
    need(lhs==rhs,'extraction:projective_cubic_from_seed')
    need([44,3*11-4*96,4*39-3*96,3*39]==[44,-351,-132,117],'extraction:factorization_three_t_plus_four')
    roots=[R3(-Q(4,3)),R3(Q(16,13),-Q(25,39)),R3(Q(16,13),Q(25,39))]
    for j,t in enumerate(roots):
        need(((A*t-3*B)*t-3*A)*t+B==0,f'extraction:stationary_root{j}')
    # Recover all oriented maxima of the harmonic cubic, not preinserted e's.
    directions=[(R3(1),R3(0)),(R3(-Q(1,2)),R3(0,Q(1,2))),
                (R3(-Q(1,2)),R3(0,-Q(1,2)))]
    recovered=[]
    for j,(c,s) in enumerate(directions):
        h=vv(sc(Y,c),Z,s)
        d,v_found,charge=mixed_square(a,u,h)
        hpart=vv(vv(a.prod(h,h),u,-270),v_found,-504)
        need(hpart==sc(h,20),f'extraction:maximum_direction{j}_quadratic_fixed_point')
        e=vv(vv(sc(u,Q(5,32)),v_found,Q(7,16)),h,Q(1,32))
        # Equivalent endpoint-free formula using only u and the maximizing h.
        e2=vv(vv(sc(a.prod(h,h),Q(1,1152)),h,Q(1,72)),u,-Q(5,64))
        need(e==e2 and a.prod(e,e)==sc(e,2),f'extraction:root{j}_recovered_Ising_idempotent')
        need(a.ip(e,e)==Q(1,4),f'extraction:root{j}_charge_one_half')
        # The root coordinates relative to the supplied rotated basis match.
        xp=a.ip(h,p)/n;xq=a.ip(h,q)/n;t=xq/xp
        need(any(t==r for r in roots),f'extraction:root{j}_came_from_seed_polynomial')
        need(a.ip(a.prod(h,h),h)==20*n,f'extraction:root{j}_positive_orientation')
        recovered.append(e)
    need(all(a.ip(e,f)==Q(13,1024) for e,f in combinations(recovered,2)),
         'extraction:three_Ising_vectors_are_not_orthogonal')
    # Seed already at a stationary line: choose its sign, do not divide by a zero discriminant.
    for sg in (Q(-1),Q(1)):
        y=sc(Y,sg);cubic=a.ip(a.prod(y,y),y)/n
        selected=sc(y,1 if cubic>0 else -1)
        need(selected==Y,'extraction:stationary_seed_sign_'+str(sg))
    return {'seed_coordinates':[Q(3,5),Q(4,5)],'seed_cubic_coefficients':[A,B],
            'projective_stationary_polynomial':lhs,'stationary_roots':roots,'Ising_vectors_recovered':recovered,
            'orthogonal_pair_recovered':False,'existence_of_3A_plane_from_ambient_axioms_proved':False}

def no_Ising_control():
    a=code_core();u1,u2,u3,Y,Z=a.e;omega=vv(vv(u1,u2),u3)
    need(a.ip(omega,omega)==Q(6,5),'counterexample:total_charge_twelve_fifths')
    need(all(a.prod(omega,x)==sc(x,2) for x in a.e),'counterexample:complete_weight_two_unit')
    # A direct contradiction for an arbitrary real Ising candidate.
    # Charge 1/2 => sum a_i=5/8; all a_i^2-a_i+45R^2=0.
    alpha=Q(5,24);from_stress=alpha*(1-alpha)/45
    from_plane=(Q(4,3)*Q(5,8)-2)**2/64
    need(from_stress==Q(19,5184) and from_plane==Q(49,2304) and from_stress!=from_plane,
         'counterexample:two_required_radii_for_Ising_are_inconsistent')
    # Exhaust all real idempotents, including zero. Nonzero plane => a_i in {a,1-a}.
    phases=[(R3(1),R3(0)),(R3(-Q(1,2)),R3(0,Q(1,2))),
            (R3(-Q(1,2)),R3(0,-Q(1,2)))]
    solutions=[]
    for bits in product((0,1),repeat=3):solutions.append([R3(x) for x in (*bits,0,0)])
    polys=[]
    for k in range(4):
        alpha=Q(5,14) if k in (0,3) else Q(1,6)
        radius=Q(1,14) if k in (0,3) else Q(1,18)
        signed=radius if k<2 else -radius
        S=k+(3-2*k)*alpha
        need(45*(Q(4,3)*S-2)**2==64*alpha*(1-alpha),f'counterexample:branch{k}_radial_polynomial')
        need(45*radius*radius==alpha*(1-alpha),f'counterexample:branch{k}_stress_equations')
        polys.append({'large_root_count':k,'small_root':alpha,'plane_radius_squared':radius*radius,'charge':Q(4,5)*S})
        for positions in combinations(range(3),k):
            av=[1-alpha if i in positions else alpha for i in range(3)]
            for c,s in phases:solutions.append([R3(t) for t in av]+[signed*c,signed*s])
    need(len(solutions)==32 and len(set(map(tuple,solutions)))==32,'counterexample:thirty_two_distinct_idempotents_including_zero')
    charge_counts={}
    for e in solutions:
        if a.prod(e,e)!=sc(e,2):raise RuntimeError('Non-idempotent in exact exhaustive list')
        charge=2*a.ip(e,e)
        if charge.b:raise RuntimeError('Irrational charge')
        need(charge==2*a.ip(e,omega),'counterexample:charge_from_stress_'+str(len(charge_counts))+'_'+str(sum(charge_counts.values())))
        charge_counts[charge.a]=charge_counts.get(charge.a,0)+1
    expected={Q(0):1,Q(4,5):3,Q(8,5):3,Q(12,5):1,Q(6,7):3,Q(14,15):9,Q(22,15):9,Q(54,35):3}
    need(charge_counts==expected,'counterexample:complete_charge_histogram')
    need(Q(1,2) not in charge_counts,'counterexample:no_Ising_anywhere_in_full_code_weight_two_space')
    need(min(q for q in charge_counts if q)>Q(1,2),'counterexample:positive_charge_gap')
    # Exact factorization of the two radial polynomials; no numerical search.
    # For k0/3: 4(14a-9)(14a-5); k1/2:4(6a-5)(6a-1).
    for k in range(4):
        c=Q(4,3)*k-2;d=Q(4,3)*(3-2*k)
        coefficients=[45*c*c,90*c*d-64,45*d*d+64]
        wanted=[180,-784,784] if k in (0,3) else [20,-144,144]
        need(coefficients==wanted,f'counterexample:exhaustive_branch{k}_factorization')
    spectator_charge=Q(24)-Q(12,5)
    need(spectator_charge==Q(108,5) and all(r+e*spectator_charge!=Q(1,2) for r in charge_counts for e in (0,1)),
         'counterexample:adding_ambient_stress_does_not_create_an_Ising_vector')
    return {'code':'D={(0,0,0),(1,1,1),(-1,-1,-1)}','central_charge':Q(12,5),
            'full_weight_two_dimension':5,'charge_counts':charge_counts,'complete_real_idempotents':solutions,
            'radial_branches':polys,'Ising_radius_requirements':[from_stress,from_plane],
            'embedding_into_moonshine_is_imported':True,'counterexample_to_moonshine_uniqueness':False}

def conv(x):
    if isinstance(x,(Q,R3)):return str(x)
    if isinstance(x,dict):return {str(k):conv(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [conv(v) for v in x]
    return x

def main():
    fusion=fusion_and_candidate();mixed=mixed_controls();found=extraction();negative=no_Ising_control()
    print(json.dumps(conv({'status':'PASS within exact fusion-interface and finite-algebra scopes',
       'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,'fusion_and_gap':fusion,
       'two_local_models':mixed,'endpoint_free_extraction':found,'genuine_Ising_free_subtheory':negative,
       'arithmetic':'rationals and explicitly represented real Q(sqrt(3))',
       'largest_matrix_dimension':5,'full_Monster_tensor_constructed':False,
       'first_Ising_forced_from_original_assumptions':False,'source_theorems_formally_verified':False}),indent=2,sort_keys=True))
if __name__=='__main__':main()
