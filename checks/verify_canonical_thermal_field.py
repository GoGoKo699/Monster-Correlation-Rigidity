#!/usr/bin/env python3
"""Exact certificates for the canonical first nonzero primary thermal field.

No assumed Monster action, full CFT, large OPE tensor, or floating point.
The source conformal-design and modular theorems are explicit dependencies.
Small even-boson controls are not extremal holomorphic c24 theories.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import thermal_field_virasoro as v

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]
D=196883
KAPPA=F(13858,3)


def need(ok,label):
    if not bool(ok): raise RuntimeError(label)
    LABELS.append(label)


def ldl(M):
    n=len(M);L=[[F(i==j) for j in range(n)] for i in range(n)];diag=[]
    for i in range(n):
        val=M[i][i]-sum((L[i][k]**2*diag[k] for k in range(i)),F(0))
        if val<=0: raise RuntimeError('Nonpositive Gram pivot')
        diag.append(val)
        for j in range(i+1,n):
            L[j][i]=(M[j][i]-sum((L[j][k]*L[i][k]*diag[k] for k in range(i)),F(0)))/val
    return diag


@lru_cache(None)
def partitions(n,top=None):
    if n==0:return ((),)
    if n<0:return ()
    top=n if top is None else top
    return tuple((i,)+tail for i in range(min(top,n),0,-1) for tail in partitions(n-i,i))


@lru_cache(None)
def pairing(lam,p,h):
    if not lam:return F((-1)**h if p==2*h-1 else 0)
    m,rest=lam[0],lam[1:]
    return ((h-1)*(m+1)-p)*pairing(rest,p+m,h)


def projection(N,c=24,h=2):
    module=v.Vir(c,0);basis=v.parts(N)
    M=[[module.gram(a,b) for b in basis] for a in basis]
    pivots=ldl(M)
    rhs=[pairing(lam,2*h-N-1,h) for lam in basis]
    x=v.solve(M,rhs)
    value=sum((a*b for a,b in zip(rhs,x)),F(0))
    return {'weight':N,'partitions':basis,'gram':M,'positive_LDL_pivots':pivots,
            'pairing_per_unit_input':rhs,'projection_per_unit_input':x,
            'vacuum_norm_per_input_squared':value}


def raw_scalar(N,d=D,kappa=KAPPA,s2=F(1,3)):
    if N==0:return F(d)
    if N==1:return F(0)
    if N in (2,3):return s2*d
    return F(comb(N-1,3)+int(N==4))+(N-3)*(kappa+s2)+s2*d


def casimir_certificate():
    vac=v.Vir(24,0);states={0:{():F(D)},1:{}};rows=[]
    for N in range(2,13):
        row=projection(N);rhs=row['pairing_per_unit_input'];x=row['projection_per_unit_input'];M=row['gram']
        need([sum((a*b for a,b in zip(r,x)),F(0)) for r in M]==rhs,f'Casimir:w{N}_projection_equations')
        states[N]={lam:D*a for lam,a in zip(row['partitions'],x) if a}
        raw= D*raw_scalar(N);vn=D*D*row['vacuum_norm_per_input_squared'];residual=raw-vn
        row.update(raw_norm=raw,vacuum_projection_norm=vn,primary_residual_norm=residual)
        need(residual==0 if N<12 else residual>0,f'Casimir:w{N}_vanishing_then_positive_norm')
        rows.append(row)
    for m in range(1,13):
        lhs=vac.apply(m,states[12]);rhs={lam:(m+10)*a for lam,a in states[12-m].items()}
        need(lhs==rhs,f'Casimir:weight12_positive_Virasoro_recursion_L{m}')
    rho=rows[-1]['primary_residual_norm']/D;norm=D*rho
    need(rows[-1]['vacuum_norm_per_input_squared']==F(282875933416397,518707716131049),
         'normalization:weight12_vacuum_coefficient')
    need(raw_scalar(12)==F(322109,3),'normalization:raw_Casimir_scalar')
    need(rho==F(20620704,878199601),'normalization:zero_mode_scalar_on_P2')
    need(norm==F(68811289248,14884739),'normalization:canonical_field_norm')
    need(D*rho==norm,'normalization:Riesz_trace_equals_field_norm')
    need(rho*rho/(norm)==norm/(D*D),'normalization:unit_field_first_level_action')
    need(1/norm==F(14884739,68811289248),'normalization:Delta_normalized_field_norm')
    return norm,rho,rows


@lru_cache(None)
def block(h,N):
    if h==N:return F(1)
    basis=v.parts(N) if h==0 else partitions(N-h)
    if not basis:return F(0)
    module=v.Vir(24,h);M=[[module.gram(a,b) for b in basis] for a in basis];ldl(M)
    rhs=[]
    for lam in basis:
        p=3-N;coef=F(1)
        for m in lam:coef*=m+1-p;p+=m
        if p!=3-h:raise RuntimeError('Descendant degree')
        rhs.append(coef)
    x=v.solve(M,rhs)
    return sum((a*b for a,b in zip(rhs,x)),F(0))


def six_interface(norm):
    vac,pri=v.Vir(24,0),v.Vir(24,2);a6=F(0);certificate=[]
    for i in range(7):
        N=12-i;row=projection(N,h=6);x=[comb(6,i)*z for z in row['projection_per_unit_input']]
        ell=[vac.mode(lam,N-1,(2,)).get((2,),F(0))+D*pri.mode(lam,N-1,()).get((),F(0)) for lam in row['partitions']]
        contribution=sum((a*b for a,b in zip(x,ell)),F(0));a6+=contribution
        certificate.append({'weight':N,'star_index':i,'projection':x,'trace_vector':ell,'contribution':contribution})
    need(a6==F(3523416,14884739),'P6:independent_pair_vacuum_coefficient')
    # Recompute the finite channel through grade six, not just stored scalar values.
    ts=(1,1,1,1,-1,-1);fs=(KAPPA,F(899),F(155,3),-F(7,3),F(845,3),-F(1,3))
    qs=(0,KAPPA,0,0,0,0);js=(D,0,0,0,0,0);A={}
    expected=[[D,0,0,0,0,0],[0]*6,[0,KAPPA,0,0,0,0],[0,0,0,0,564,0],
              [0,0,54,0,0,0],[0,0,0,0,0,4],[0,0,0,4,0,0]]
    for N in range(7):
        raw=[]
        for t,f,q,j in zip(ts,fs,qs,js):
            if N==0:z=j
            elif N==1:z=0
            elif N==2:z=q+F(j,3)
            elif N==3:z=q+f-f*t+F(j+1-t,3)
            else:z=comb(N-1,3)+int(N==4)*t+(N-2)*(f+F(1,3))+q+F(j,3)-f*t-F(t,3)
            raw.append(F(z))
        for h in range(N):
            if h==1:continue
            raw=[z-block(h,N)*u for z,u in zip(raw,A[h])]
        A[N]=raw
        need(raw==list(map(F,expected[N])),f'P6:finite_channel_weight{N}')
    visible=18538750076;dim6=312092484374;invisible=dim6-visible
    need(invisible==293553734298,'P6:invisible_dimension')
    need(0<a6<4,'P6:both_signs_of_canonical_field_action')
    need((4-a6)*visible-a6*invisible==4*visible-a6*dim6,'P6:response_trace_identity')
    lower=a6*a6/norm;upper=(4-a6)**2/norm
    need(lower>0 and upper>lower,'P6:nonzero_OPE_component_norm_bounds')
    need((a6/norm)**2*norm==lower,'P6:projection_onto_canonical_field_normalization')
    return {'a6':a6,'pair_vacuum_certificate':certificate,'primary_dimension':dim6,
            'visible_dimension':visible,'invisible_dimension':invisible,
            'action_numerators':[4-a6,-a6],'unit_field_action_common_denominator_squared':norm,
            'invisible_pair_primary_norm_lower_bound':lower,'visible_pair_primary_norm_lower_bound':upper}



def torus_block(h,level,s=12,c=24):
    module=v.Vir(c,h);basis=partitions(level)
    @lru_cache(None)
    def matrix_element(lam,n,mu):
        if lam:
            m,rest=lam[0],lam[1:]
            z=sum((a*matrix_element(rest,n,w) for w,a in module.act(m,mu).items()),F(0))
            return z+((s-1)*(m+1)-n)*matrix_element(rest,n+m,mu)
        if mu:
            k,rest=mu[0],mu[1:]
            return (n+(s-1)*(k-1))*matrix_element((),n-k,rest)
        return F(n==s-1)
    M=[[module.gram(a,b) for b in basis] for a in basis];pivots=ldl(M)
    O=[[matrix_element(a,s-1,b) for b in basis] for a in basis]
    trace=F(0)
    for j in range(len(basis)):
        column=v.solve(M,[O[i][j] for i in range(len(basis))]);trace+=column[j]
    return {'primary_weight':h,'level':level,'inserted_weight':s,'central_charge':c,
            'partitions':basis,'gram':M,'positive_LDL_pivots':pivots,
            'inserted_mode_matrix_per_unit_primary_expectation':O,'trace_multiplier':trace}


def crossed_channel_normalization(norm,six):
    tau={2:1,3:-24,4:252,5:-1472,6:4830};primary={};cert=[]
    for n in range(2,7):
        pieces=[torus_block(h,n-h) for h in range(2,n)]
        primary[n]=F(tau[n])-sum((row['trace_multiplier']*primary[row['primary_weight']] for row in pieces),F(0))
        cert.append({'energy_level':n,'total_trace_multiplier':tau[n],
                     'descendant_certificates':pieces,'primary_trace_multiplier':primary[n]})
    expected=[F(1),-F(58),F(44022,41),-F(977155,94),F(947015938,15717)]
    for n,q in zip(range(2,7),expected):
        need(primary[n]==q,f'compatibility:thermal_primary_trace_weight{n}')
    total=4*six['visible_dimension']-six['a6']*six['primary_dimension']
    need(primary[6]*norm==total,'compatibility:genus_zero_norm_matches_weight6_thermal_trace')
    need(total/primary[6]==norm,'compatibility:independent_second_normalization_route')
    need(torus_block(2,1)['trace_multiplier']==34,'compatibility:descendant_trace_not_plain_multiplicity')
    need(F(tau[6])*norm!=total,'negative:ignoring_descendants_creates_false_incompatibility')
    return {'certificate':cert,'weight6_primary_trace_from_pair_action':total,
            'normalization_recovered_from_thermal_compatibility':total/primary[6]}

def fock_checks():
    path=Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(path.read_bytes()).hexdigest()=='701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:unchanged_oscillator_helper')
    spec=importlib.util.spec_from_file_location('_thermal_axis_fock',path);o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=12
    records=[]
    for n in (2,3):
        vac={(0,)*(n*o.GRADE):F(1)};I=[[int(i==j) for j in range(n)] for i in range(n)]
        def vir(m,state):return o.quadratic_mode(I,m+1,state,n)
        @lru_cache(None)
        def descendant(lam):
            state=vac
            for m in reversed(lam):state=vir(-m,state)
            return state
        basis=[]
        for j in range(1,n):
            M=[[0]*n for _ in range(n)]
            for i in range(j):M[i][i]=1
            M[j][j]=-j;basis.append(M)
        for i in range(n):
            for j in range(i+1,n):
                M=[[0]*n for _ in range(n)];M[i][j]=M[j][i]=1;basis.append(M)
        states=[o.quadratic_mode(M,-1,vac,n) for M in basis]
        norms=[o.inner(s,s,n) for s in states];dim=len(states)
        need(all(o.inner(a,b,n)==(norms[i] if i==j else 0) for i,a in enumerate(states) for j,b in enumerate(states)),f'fock:c{n}_orthogonal_primary_basis')
        need(all(not vir(m,s) for s in states for m in (1,2)),f'fock:c{n}_external_primarity')
        def casimir(N):
            return o.add(*[(1/g,o.quadratic_mode(M,3-N,s,n)) for M,s,g in zip(basis,states,norms)])
        def projected_vacuum(N):
            row=projection(N,c=n)
            return o.add(*[(dim*a,descendant(lam)) for lam,a in zip(row['partitions'],row['projection_per_unit_input'])])
        raw4=casimir(4);V4=projected_vacuum(4);R4=o.add((1,raw4),(-1,V4));Rnorm=o.inner(R4,R4,n)
        need(Rnorm>0,f'fock:c{n}_nonzero_primary_Casimir_at_weight4')
        need(all(not vir(m,R4) for m in range(1,5)),f'fock:c{n}_primary_projection_at_weight4')
        # Independently expand derivative-current fields on finite-grade inputs.
        # Normal ordering bounds each annihilated/created total by the input grade.
        def zero_mode(field,source):
            if not source:return {}
            grade=sum((i//n+1)*q for i,q in enumerate(next(iter(source))))
            mode_range=tuple(range(-grade,0))+tuple(range(1,grade+1))
            out={}
            for key,coefficient in field.items():
                factors=[(p%n,p//n+1) for p,count in enumerate(key) for _ in range(count)]
                if len(factors)>2*grade:continue
                for modes in product(mode_range,repeat=len(factors)):
                    if sum(modes) or sum(r for r in modes if r>0)>grade:continue
                    c=coefficient;ops=[]
                    for (species,m),r in zip(factors,modes):
                        c*=(-1)**(m-1)*v.bc(r+m-1,m-1);ops.append((species,r))
                    if not c:continue
                    ops.sort(key=lambda t:t[1]>=0);value=source
                    for species,r in reversed(ops):value=o.oscillator(value,species,r,n)
                    out=o.add((1,out),(c,value))
            return out
        actions=[zero_mode(R4,s) for s in states]
        trace=sum((o.inner(s,a,n)/g for s,a,g in zip(states,actions,norms)),F(0))
        need(trace==Rnorm,f'fock:c{n}_Riesz_identity_on_actual_nonzero_Casimir')
        need(all(a==o.add((Rnorm/dim,s)) for a,s in zip(actions,states)),f'fock:c{n}_scalar_first_level_action')
        # Every primary part of an initial pair checks the Riesz identity off-axis.
        omega=vir(-2,vac);p0=F(6,5*n+22);q0=F(44,n*(5*n+22));p2=F(22,5*n+44);q2=F(3*n,4*(5*n+44))
        count=0
        for i,j in combinations_with_replacement(range(dim),2):
            a,b=states[i],states[j];ab=o.quadratic_mode(basis[i],1,b,n);g=o.inner(a,b,n)
            mu=o.add((1,ab),(-F(4,n)*g,omega));B=o.add((1,o.quadratic_mode(basis[i],0,b,n)),(-F(1,2),o.deriv(ab,n)))
            S=o.add((1,o.quadratic_mode(basis[i],-1,b,n)),(-F(1,2),o.deriv(B,n)),
                    (-p2,vir(-2,mu)),(-q2,o.deriv(o.deriv(mu,n),n)),
                    (-g*p0,vir(-4,vac)),(-g*q0,vir(-2,omega)))
            if any(vir(m,S) for m in range(1,5)):raise RuntimeError('Primary control failed')
            tt=sum((o.inner(s,zero_mode(S,s),n)/gg for s,gg in zip(states,norms)),F(0))
            if tt!=o.inner(R4,S,n):raise RuntimeError('Off-axis Riesz identity')
            count+=1
        need(True,f'fock:c{n}_all_pair_primary_Riesz_identities')
        if n==2:
            need(Rnorm==F(3,2),'fock:c2_exact_primary_Casimir_norm')
            # Independent descendant-insertion matrices from actual oscillator fields.
            for level in (1,2):
                row=torus_block(2,level,s=4,c=2);desc=[]
                for lam in row['partitions']:
                    state=states[0]
                    for m in reversed(lam):state=vir(-m,state)
                    desc.append(state)
                actual=[[o.inner(a,zero_mode(R4,b),n) for b in desc] for a in desc]
                expected=[[Rnorm/dim*z for z in r] for r in row['inserted_mode_matrix_per_unit_primary_expectation']]
                need(actual==expected,f'fock:c2_weight4_primary_insertion_on_descendants_level{level}')
            raw12=casimir(12);vac12=projected_vacuum(12);rest=o.add((1,raw12),(-1,vac12))
            need(o.inner(raw12,raw12,n)==418,'fock:c2_independent_grade12_raw_norm')
            need(bool(vir(1,rest)),'negative:c2_without_11design_vacuum_subtraction_not_primary_at12')
            for lam in v.parts(12):
                if o.inner(descendant(lam),raw12,n)!=dim*pairing(lam,-9,2):raise RuntimeError('Grade12 Fock pairing')
            need(True,'fock:c2_all21_grade12_Casimir_pairings')
        records.append({'central_charge':n,'primary_basis_dimension':dim,'weight4_primary_Casimir_norm':Rnorm,'independent_Riesz_pair_controls':count})
    return records


def modular_checks(norm):
    # E4^3/Delta and Delta, generated as finite integer series, not group data.
    N=12
    def mul(a,b):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]
    delta=[1]+[0]*N
    for m in range(1,N+1):
        factor=[0]*(N+1)
        for j in range(min(24,N//m)+1):factor[j*m]=(-1)**j*comb(24,j)
        delta=mul(delta,factor)
    need(delta[:5]==[1,-24,252,-1472,4830],'modular:Delta_coefficients')
    need(norm>0,'modular:nonzero_rank_one_response_functional')
    # Rational Euclidean controls for the Riesz and maximization identities.
    r=[F(3),F(4),F(0)];vectors=[[F(1),0,0],[0,F(1),0],[0,0,F(1)],[F(3,5),F(4,5),0],[F(4,5),-F(3,5),0]]
    for k,x in enumerate(vectors):
        dot=sum(a*b for a,b in zip(r,x));xx=sum(a*a for a in x)
        need(dot*dot<=25*xx,f'Riesz:unit_field_bound_control{k}')
    need(sum(r[i]*vectors[3][i] for i in range(3))==5,'Riesz:positive_maximizer')
    need(sum(r[i]*vectors[4][i] for i in range(3))==0,'Riesz:orthogonal_primary_has_zero_one_point')
    return {'q_inverse_Delta_coefficients':delta[:6], 'squared_max_unit_primary_response_multiplier':norm}


def strings(obj):
    if isinstance(obj,F):return str(obj)
    if isinstance(obj,dict):return {str(k):strings(x) for k,x in obj.items()}
    if isinstance(obj,(tuple,list)):return [strings(x) for x in obj]
    return obj


def main():
    need(hashlib.sha256(Path(v.__file__).read_bytes()).hexdigest()=='cefc291c6be9de9518037d353dc9b25857735963fb8747aea579bce41cc24fdb','dependency:unchanged_exact_Virasoro_helper')
    norm,rho,cert=casimir_certificate();six=six_interface(norm);cross=crossed_channel_normalization(norm,six);fock=fock_checks();mod=modular_checks(norm)
    print(json.dumps(strings({'status':'PASS within declared exact Casimir/Fock scopes','base_commit':BASE,
        'checks':len(LABELS),'labels':LABELS,'casimir_certificate':cert,'canonical_norm_squared':norm,
        'canonical_zero_mode_on_P2':rho,'crossed_channel_normalization':cross,'weight_six_interface':six,'Fock_controls':fock,'modular':mod,
        'arithmetic':'integers and fractions only','largest_square_matrix_dimension':21,
        'largest_oscillator_grade':12,'Monster_data_used':False,'full_extremal_OPE_tensor_constructed':False,
        'new_independent_selection_condition_proved':False,'unique_invariant_primary_proved_for_unknown_CFT':False,
        'source_theorems_formally_verified':False}),sort_keys=True,indent=2))

if __name__=='__main__':main()
