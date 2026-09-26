#!/usr/bin/env python3
"""Exact trace certificate, Fock controls and bracket-normalization checks.

The largest Virasoro Gram is 8x8. Small Fock controls are c=3, not extremal
holomorphic theories. A separate known-example trace uses proved block
multiplicities; no full Monster operator or character data is constructed.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import primary_three_ward as v

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]

def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)

def det(matrix):
    rows=[list(map(F,row)) for row in matrix];answer=F(1)
    for i in range(len(rows)):
        k=next((j for j in range(i,len(rows)) if rows[j][i]),None)
        if k is None:return F(0)
        if k!=i:rows[i],rows[k]=rows[k],rows[i];answer=-answer
        pivot=rows[i][i];answer*=pivot
        for j in range(i+1,len(rows)):
            scale=rows[j][i]/pivot
            rows[j]=[a-scale*b for a,b in zip(rows[j],rows[i])]
    return answer

def matrix(n,entries=()):
    a=[[F(0)]*n for _ in range(n)]
    for i,j,value in entries:a[i][j]=F(value)
    return tuple(map(tuple,a))
def eye(n):return matrix(n,[(i,i,1) for i in range(n)])
def add(a,b,k=1):return tuple(tuple(x+k*y for x,y in zip(ar,br)) for ar,br in zip(a,b))
def scale(a,k):return tuple(tuple(k*x for x in r) for r in a)
def mm(a,b):return tuple(tuple(sum((x*y for x,y in zip(ar,bc)),F(0)) for bc in zip(*b)) for ar in a)
def tr(a):return sum((a[i][i] for i in range(len(a))),F(0))
def comm(a,b):return add(mm(a,b),mm(b,a),-1)
def skew_basis(n):return tuple(matrix(n,[(i,j,1),(j,i,-1)]) for i,j in combinations(range(n),2))
def half(a,b):return -tr(mm(a,b))/2

def certificate_checks():
    total, rows=v.reconstruct()
    expected=[98442,-1120995,4538070,-8975643,9432675,-5076594,1104009]
    for row,e in zip(rows,expected):
        n=row['weight'];M=row['gram'];b=row['pairing'];x=row['projection']
        need(all(det([r[:k] for r in M[:k]])>0 for k in range(1,len(M)+1)),f'certificate:w{n}_positive_Gram_minors')
        need([sum((a*y for a,y in zip(r,x)),F(0)) for r in M]==b,f'certificate:w{n}_projection_system')
        need(row['contribution']==e,f'certificate:w{n}_exact_contribution')
    need(total==-36,'certificate:universal_triple_coefficient_minus_36')
    need(sum(r['vacuum_contribution'] for r in rows)==0,'certificate:stress_state_trace_cancels')
    need(sum(r['per_primary_contribution'] for r in rows)==-F(36,196883),'certificate:per_primary_coefficient')
    reg,regrows=v.reconstruct(2,3,3)
    need(reg==104,'regression:233_coefficient_in_first_slot_Hermitian_convention')
    need([r['contribution'] for r in regrows]==[-164070,1521466,-4859280,7135443,-4958560,1325105],
         'regression:all_six_233_contributions_match_after_sign_conversion')
    need(v.ward((),5,2,3,3,3)==-1 and v.ward((),5,2,3,3,3,True)==1,'sign:swapping_first_two_odd_primaries')
    need(v.bc(-1,5)==-1 and v.bc(-2,3)==-4,'modes:negative_binomial_coefficients')
    need(max(map(lambda r:len(r['gram']),rows))==8,'scope:largest_vacuum_Gram_eight')
    return rows

def fock_controls():
    path=Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(path.read_bytes()).hexdigest()=='701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:unchanged_note13_Fock_helper')
    spec=importlib.util.spec_from_file_location('_bracket_fock',path)
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=14
    n=3;vac={(0,)*(n*o.GRADE):F(1)};I=eye(n);basis=skew_basis(n)
    def state(A):
        out={}
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    key=[0]*(n*o.GRADE);key[n+i]+=1;key[j]+=1
                    out[tuple(key)]=out.get(tuple(key),F(0))+A[i][j]/2
        return {k:x for k,x in out.items() if x}
    def freeze(s):return tuple(sorted(s.items()))
    @lru_cache(None)
    def mode_cached(A,k,s):
        source=dict(s);out={}
        for i in range(n):
            for j in range(n):
                if not A[i][j]:continue
                for r in range(-o.GRADE,o.GRADE+1):
                    q=k-2-r
                    if not r or not q or abs(q)>o.GRADE:continue
                    ops=sorted(((i,r),(j,q)),key=lambda z:z[1]>=0)
                    z=source
                    for a,m in reversed(ops):z=o.oscillator(z,a,m,n)
                    out=o.add((1,out),(-F(r+1,2)*A[i][j],z))
        return freeze(out)
    def mode(A,k,s):return dict(mode_cached(A,k,freeze(s)))
    def vir(m,s):return o.quadratic_mode(I,m+1,s,n)
    def descend(lam):
        s=vac
        for m in reversed(lam):s=vir(-m,s)
        return s
    states=[state(A) for A in basis]
    need(all(mode(A,-1,vac)==s for A,s in zip(basis,states)),'fock:state_field_creation_convention')
    need(all(not vir(m,s) for m in (1,2,3) for s in states),'fock:weight_three_fields_are_primaries')
    need([[o.inner(a,b,n) for b in states] for a in states]==[[F(i==j) for j in range(3)] for i in range(3)],'fock:skew_half_Frobenius_metric')
    t=o.inner(states[0],mode(basis[1],2,states[2]),n)
    need(t!=0,'fock:nonzero_triple_control')
    need(t==-F(5,2)*tr(mm(mm(basis[0],basis[1]),basis[2])),'fock:direct_333_coefficient')
    for label,order in [('abc',(0,1,2)),('bac',(1,0,2))]:
        ia,ib,ic=order
        for p in range(3,9):
            q=7-p
            z=mode(basis[ia],p,mode(basis[ib],q,states[ic]))
            expected=v.ward((),p,q,3,3,3,swap=(label=='bac'))*t
            if o.inner(vac,z,n)!=expected:raise RuntimeError('Vacuum Ward coefficient')
        need(True,'fock:vacuum_Ward_words_'+label)
    # Test every composite pairing entering the universal certificate directly.
    count=0
    for i in range(4):
        r=i-1
        for j in range(7-i):
            s=j-1;N=9-i-j;actual={}
            for k in range(max(5-s,5)+1):
                c=(-1)**k*v.bc(r,k)
                if k<=5-s:actual=o.add((1,actual),(c,mode(basis[0],r-k,mode(basis[1],s+k,states[2]))))
                if k<=5:actual=o.add((1,actual),(-c*(-1 if r%2 else 1),mode(basis[1],r+s-k,mode(basis[0],k,states[2]))))
            for lam in v.parts(N):
                if o.inner(descend(lam),actual,n)!=v.composite(lam,r,s,3,3,3)*t:
                    raise RuntimeError('Composite pairing '+str((i,j,lam)))
                count+=1
    need(True,'fock:all_star_composite_pairings_match_Ward_reduction')
    # Check PBW Gram matrices and vacuum descendant zero modes independently at c=3.
    small=v.Vir(3,0);gram_count=0;trace_count=0
    a=matrix(3,[(0,0,1),(1,1,-1)])
    primary=o.quadratic_mode(a,-1,vac,n)
    def normal_mode(lam,index,source):
        if not lam:return source if index==-1 else {}
        m,rest=lam[0],lam[1:];level=sum((p//n+1)*c for p,c in enumerate(next(iter(source)))) if source else 0
        out={};k=m-2;wt=sum(rest)
        for j in range(max(0,level+wt-index)):
            out=o.add((1,out),(v.bc(j+k,k),vir(-j-m,normal_mode(rest,index+j,source))))
        for j in range(k,level+m):
            out=o.add((1,out),((-1)**k*v.bc(j,k),normal_mode(rest,index-1-j,vir(j-m+1,source))))
        return out
    for N in range(3,10):
        parts=v.parts(N);ss=[descend(l) for l in parts]
        for a1,l1 in zip(ss,parts):
            for a2,l2 in zip(ss,parts):
                if o.inner(a1,a2,n)!=small.gram(l1,l2):raise RuntimeError('Fock Gram')
                gram_count+=1
        for lam in parts:
            for source,module,word in [(descend((2,)),small,(2,)),(primary,v.Vir(3,2),())]:
                actual=normal_mode(lam,N-1,source)
                coeff=module.mode(lam,N-1,word).get(word,F(0))
                if actual!=o.add((coeff,source)):raise RuntimeError('Descendant zero mode')
                trace_count+=1
    need(True,'fock:all_vacuum_Gram_entries_through_nine')
    need(True,'fock:descendant_zero_modes_on_vacuum_and_h2_modules')
    # Direct finite star identity on the weight-two space, not a lowest-module assumption.
    quadratic_states=[]
    for i in range(n):
        for j in range(i,n):
            A=matrix(n,[(i,i,1)] if i==j else [(i,j,1),(j,i,1)])
            quadratic_states.append(o.quadratic_mode(A,-1,vac,n))
    star_count=0
    for A,B in product(basis,repeat=2):
        for source in quadratic_states:
            actual={}
            for i in range(4):
                r,s=i-1,5-i
                for k in range(max(4-s,4)+1):
                    c=v.bc(3,i)*(-1)**k*v.bc(r,k)
                    if k<=4-s:
                        actual=o.add((1,actual),(c,mode(A,r-k,mode(B,s+k,source))))
                    if k<=4:
                        actual=o.add((1,actual),(-c*(-1 if r%2 else 1),mode(B,r+s-k,mode(A,k,source))))
            if actual!=mode(A,2,mode(B,2,source)):raise RuntimeError('Star zero modes on V2')
            star_count+=1
    need(True,'fock:star_identity_on_all_six_quadratic_states')
    # Explicit compressed commutator versus full mode action in the small unitary VOA.
    syms=[matrix(3,[(0,0,1),(1,1,-1)]),matrix(3,[(0,1,1),(1,0,1)]),matrix(3,[(1,2,1),(2,1,1)])]
    def project3(z):return o.add((1,z),(-F(1,4),o.deriv(vir(1,z),n)))
    def H(A,z):return project3(o.quadratic_mode(A,1,z,n))
    def down(A,z):return o.deriv(vir(1,o.quadratic_mode(A,1,z,n)),n)
    comm_count=0;nonzero_excursion=False
    for A,B in product(syms,repeat=2):
        C=comm(A,B)
        for z in states:
            compressed=o.add((1,H(A,H(B,z))),(-1,H(B,H(A,z))))
            # P E_A (I-P) E_B P - reverse. Here (I-P)=D L1/4.
            leakage=o.add((F(1,4),H(A,down(B,z))),(-F(1,4),H(B,down(A,z))))
            expected=project3(mode(C,2,z))
            if o.add((1,compressed),(1,leakage))!=expected:raise RuntimeError('Compressed commutator')
            if leakage:nonzero_excursion=True
            comm_count+=1
    need(True,'fock:compressed_commutator_with_descendant_excursions')
    need(nonzero_excursion,'negative:omitting_descendant_excursions_changes_bracket')
    # Full known-example trace from exact block multiplicities, not a giant matrix.
    # Three commuting root-block actions have commutator zero; S^2 action has index n+2;
    # twisted commutators act as C/4 with multiplicity4096.
    fundamental=tr(mm(mm(basis[0],basis[1]),basis[2]))
    full=(24+2)*fundamental+F(4096,4**3)*fundamental
    need(full==-36*t,'known_example:full_V2_block_trace_matches_universal_coefficient')
    # Independent explicit Sym^2 action in small n, verifying the index formula.
    pairs=list(combinations(range(n),2))+[(i,i) for i in range(n)]
    acts=[]
    for A in basis:
        cols=[]
        for i,j in pairs:
            U=matrix(n,[(i,j,1)] if i==j else [(i,j,1),(j,i,1)])
            Y=comm(A,U);cols.append([Y[k][l] for k,l in pairs])
        acts.append(tuple(zip(*cols)))
    need(tr(mm(mm(acts[0],acts[1]),acts[2]))==(n+2)*fundamental,'known_example:small_explicit_Sym2_index_control')
    return {'composite_pairings':count,'Gram_entries':gram_count,'descendant_zero_mode_actions':trace_count,
            'star_identity_inputs':star_count,'compressed_commutator_inputs':comm_count,'example_triple_coefficient':str(t),
            'complete_known_V2_trace':str(full),'full_known_matrix_constructed':False}

def algebra_checks():
    n=4;bb=skew_basis(n);A,B,C=bb[0],bb[1],bb[3]
    for A,B,C in product(bb,repeat=3):
        need_value=half(A,comm(B,C))==-tr(mm(mm(A,B),C))
        if not need_value:raise RuntimeError('Skew trace conversion')
    need(True,'algebra:all_skew_trace_to_commutator_factors')
    p,m=F(282),F(104)
    need(p/m==F(141,52),'algebra:inherited_mixed_compression')
    need(p/F(36)==F(47,6),'algebra:generated_333_operator_prefactor')
    need(m*m/4==2704 and m*m/36==F(2704,9),'algebra:uncontracted_polynomial_coefficients')
    need(9*m*m/4==24336,'algebra:integer_cleared_operator_identity')
    # Projected commutators are not automatically Lie brackets.
    B4=skew_basis(4);keep=[0,1,2,3,5] # all edges except (1,3)
    def project(X):return sum_mats([scale(B4[i],half(B4[i],X)) for i in keep],4)
    def bracket(X,Y):return project(comm(X,Y))
    x,y,z=B4[0],B4[3],B4[5] # edges 01,12,23
    jac=add(add(bracket(bracket(x,y),z),bracket(bracket(y,z),x)),bracket(bracket(z,x),y))
    need(jac==B4[2],'negative:projected_skew_bracket_need_not_obey_Jacobi')
    return {'triple_trace_coefficient':-36,'mixed_normalization':104,'pair_Gram_eigenvalue':282,
            'operator_residual_coefficients':[9,24336,-2704],
            'independence_from_prior_cubic_identities':'UNRESOLVED',
            'Jacobi_imposed_on_primary_projection':False}

def sum_mats(items,n):
    result=matrix(n)
    for item in items:result=add(result,item)
    return result

def strings(obj):
    if isinstance(obj,F):return str(obj)
    if isinstance(obj,dict):return {k:strings(x) for k,x in obj.items()}
    if isinstance(obj,(tuple,list)):return [strings(x) for x in obj]
    return obj

def main():
    certificate=certificate_checks();fock=fock_controls();algebra=algebra_checks()
    def no_float(x):
        if isinstance(x,float):return False
        if isinstance(x,dict):return all(no_float(v) for v in x.values())
        if isinstance(x,(list,tuple)):return all(no_float(v) for v in x)
        return True
    need(no_float(certificate),'arithmetic:certificate_has_no_floating_point_coefficients')
    print(json.dumps(strings({'status':'PASS within declared exact Ward/Fock/algebra scopes','base_commit':BASE,
          'checks':len(LABELS),'labels':LABELS,'certificate':certificate,'Fock_controls':fock,'algebra':algebra,
          'arithmetic':'integers and fractions only','largest_square_matrix_dimension':8,
          'largest_physical_state_grade':9,'private_oscillator_cutoff':14,
          'complete_extremal_OPE_constructed':False,'source_theorem_formally_verified':False,
          'new_independent_selection_condition_proved':False,'Monster_uniqueness_proved':False}),sort_keys=True,indent=2))
if __name__=='__main__':main()
