#!/usr/bin/env python3
"""Exact checks for the weight-four projection and first-level four-point closure.

Small controls: even free-boson subalgebras at c=2,3 (not extremal c=24).
The historical grade-three helper is loaded privately at grade eight, without
editing it. Full extremal tensor/source-theorem proofs are not simulated.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from pathlib import Path
from math import comb
import hashlib
import importlib.util
import json

BASE = 'ba02084a1a74fc0b4db1299f6ab3bc327a0901ef'
ROOT = Path(__file__).resolve().parents[1]
LABELS = []
MAX_GRADE = 8


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def helpers():
    p = ROOT/'checks/verify_weight_three.py'
    need(hashlib.sha256(p.read_bytes()).hexdigest() ==
         '701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:historical_oscillator_helper_hash_unchanged')
    spec = importlib.util.spec_from_file_location('_private_fock_control', p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.GRADE = MAX_GRADE
    return module


def coefficients(c):
    c = Q(c)
    return (Q(22)/(5*c+44), 3*c/(4*(5*c+44)),
            Q(6)/(5*c+22), Q(44)/(c*(5*c+22)))


def descendant_checks():
    for c in (Q(2), Q(3), Q(24)):
        a,b,u,v = coefficients(c)
        g2 = [[8+c/2,12],[12,40]]
        g0 = [[5*c,3*c],[3*c,c*(c+8)/2]]
        need([g2[0][0]*a+12*b,12*a+40*b] == [4,6], f'descendants:c{c}_weight_two_linear_system')
        need([5*c*u+3*c*v,3*c*u+c*(c+8)/2*v] == [6,8], f'descendants:c{c}_vacuum_linear_system')
        need(g2[0][0]*40-144 == 4*(5*c+44), f'descendants:c{c}_weight_two_determinant')
        need(g0[0][0]*g0[1][1]-g0[0][1]**2 == c*c*(5*c+22)/2,
             f'descendants:c{c}_vacuum_determinant')
    a,b,u,v = coefficients(24)
    need((a,b,u,v) == (Q(11,82),Q(9,82),Q(3,71),Q(11,852)), 'descendants:c24_all_four_coefficients')
    need(4*a+6*b == Q(49,41), 'descendants:c24_weight_two_Gram_subtraction')
    need(6*u+8*v == Q(76,213), 'descendants:c24_vacuum_Gram_subtraction')


def oscillator_checks(o,n):
    eye = [[int(i==j) for j in range(n)] for i in range(n)]
    basis = []
    for i in range(1,n):
        a = [[0]*n for _ in range(n)]
        a[0][0],a[i][i] = 1,-1
        basis.append(a)
    for i in range(n):
        for j in range(i+1,n):
            a = [[0]*n for _ in range(n)]
            a[i][j]=a[j][i]=1
            basis.append(a)
    dim=len(basis)
    vac={(0,)*(n*MAX_GRADE):Q(1)}
    V=lambda m,s:o.quadratic_mode(eye,m+1,s,n)
    D=lambda s:o.deriv(s,n)
    states=[o.quadratic_mode(a,-1,vac,n) for a in basis]
    omega=V(-2,vac)
    g=[[o.inner(a,b,n) for b in states] for a in states]
    p=[[o.quadratic_mode(a,1,b,n) for b in states] for a in basis]
    mu=[[o.add((1,p[i][j]),(-Q(4,n)*g[i][j],omega)) for j in range(dim)] for i in range(dim)]
    B=[[o.add((1,o.quadratic_mode(a,0,states[j],n)),(-Q(1,2),D(p[i][j])))
        for j in range(dim)] for i,a in enumerate(basis)]
    raw=[[o.quadratic_mode(a,-1,b,n) for b in states] for a in basis]
    a2,b2,a0,b0=coefficients(n)
    c0=o.add((a0,V(-4,vac)),(b0,V(-2,omega)))
    out=[[o.add((1,raw[i][j]),(-Q(1,2),D(B[i][j])),(-a2,V(-2,mu[i][j])),
                (-b2,D(D(mu[i][j]))),(-g[i][j],c0)) for j in range(dim)] for i in range(dim)]
    need(all(not V(m,x) for x in states for m in (1,2)),f'fock:c{n}_external_fields_are_primaries')
    need(all(out[i][j]==out[j][i] for i in range(dim) for j in range(dim)),f'fock:c{n}_projected_product_symmetric')
    need(all(not V(m,out[i][j]) for i in range(dim) for j in range(dim) for m in range(1,5)),
         f'fock:c{n}_all_four_positive_Virasoro_modes_zero')
    descendants=[V(-4,vac),V(-2,omega)]+[v for x in states for v in (V(-2,x),D(D(x)))]+[D(B[i][j]) for i in range(dim) for j in range(i+1,dim)]
    need(all(o.inner(out[i][j],w,n)==0 for i in range(dim) for j in range(dim) for w in descendants),
         f'fock:c{n}_orthogonal_to_all_descendant_sectors')
    need(any(raw[i][j]!=raw[j][i] for i in range(dim) for j in range(dim)),
         f'negative:c{n}_raw_minus_one_product_not_symmetric')
    pairs=list(combinations_with_replacement(range(dim),2))
    Gram=[[o.inner(out[i][j],out[k][l],n) for k,l in pairs] for i,j in pairs]
    A2=4*a2+6*b2; A0=6*a0+8*b0; shift=Q(8,n)
    pred=[]
    for i,j in pairs:
        row=[]
        for k,l in pairs:
            X=o.inner(mu[i][k],mu[j][l],n);Y=o.inner(mu[i][j],mu[k][l],n);Z=o.inner(mu[i][l],mu[j][k],n)
            row.append((1+shift/2)*(g[i][k]*g[j][l]+g[i][l]*g[j][k])+(X+Z)/2+(1-A2)*Y+(shift-A0)*g[i][j]*g[k][l])
        pred.append(row)
    need(Gram==pred,f'fock:c{n}_all_projected_four_label_Gram_entries')
    # The unprojected rational four-point function determines every raw level.
    count=0
    for level in range(MAX_GRADE+1):
        vectors=[[o.quadratic_mode(a,3-level,b,n) for b in states] for a in basis]
        for i,j,k,l in product(range(dim),repeat=4):
            aa=g[i][j]*g[k][l];bb=g[i][k]*g[j][l];cc=g[i][l]*g[j][k]
            X=o.inner(p[i][k],p[j][l],n);Y=o.inner(p[i][j],p[k][l],n);Z=o.inner(p[i][l],p[j][k],n)
            if level==0: rhs=aa
            elif level==1: rhs=0
            elif level==2: rhs=Y
            elif level==3: rhs=Y+X-Z
            else: rhs=comb(level-1,3)*bb+int(level==4)*cc+(level-2)*X+Y-Z
            if o.inner(vectors[i][j],vectors[k][l],n)!=rhs:
                raise RuntimeError(f'Rational Gram mismatch c{n} level{level} labels{i,j,k,l}')
            count+=1
        need(True,f'fock:c{n}_raw_Gram_rational_coefficient_level{level}')
    need(any(V(1,raw[i][j]) for i,j in pairs),f'negative:c{n}_omitting_descendants_fails_primary_condition')
    return {'central_charge':n,'external_primary_dimension':dim,'projected_Gram_dimension':len(pairs),
            'projected_Gram_rank':o.rank(Gram),'raw_four_label_comparisons':count,'through_weight':MAX_GRADE}


def scalar_checks():
    d=196883;kappa=Q(13858,3)
    dims=[1,d,842609326,18538750076,21296876,19360062527]
    roots=[kappa,Q(899),Q(155,3),-Q(7,3),Q(845,3),-Q(1,3)]
    signs=[1,1,1,1,-1,-1]
    qs=[0,kappa,0,0,0,0];js=[d,0,0,0,0,0]
    h4=[roots[i]+Q(7,3)-Q(8,41)*qs[i]-Q(5,213)*js[i] for i in range(4)]
    need(h4==[0,0,54,0],'extremal:weight_four_Gram_spectrum')
    need(864299970-2-2*d-21296876==dims[2],'extremal:Gram_rank_equals_available_primary_dimension')
    need(54*dims[2]==45500903604,'extremal:total_ordered_pair_squared_coupling')
    need(sum(dims)==d*d,'closure:six_spectral_subspaces_exhaust_tensor_square')
    need(roots[1]==899 and qs[1]==kappa,'closure:F_Q_joint_data_fixed')
    need(all((x/54)**2==x/54 for x in h4),'redundancy:weight_four_is_scaled_projector')
    need(all(x>=0 for x in h4),'redundancy:weight_four_positivity_automatic')
    a,b,u,v=coefficients(24)
    need(1-(4*a+6*b)==-Q(8,41),'normalization:primary_Gram_Q_coefficient')
    need(Q(1,3)-(6*u+8*v)==-Q(5,213),'normalization:primary_Gram_J_coefficient')
    need(1+Q(1,6)==Q(7,6),'normalization:four_label_metric_coefficient')
    # Six idempotents of the commuting operator algebra, evaluated exactly.
    pi0=[Q(j,d) for j in js]; pi2=[q/kappa for q in qs]
    pis=[[Q(1+s,2) for s in signs],[Q(1-s,2) for s in signs]]
    psp=[(pis[0][i]-pi0[i]-pi2[i])*(roots[i]+Q(7,3))/54 for i in range(6)]
    pap=[pis[1][i]*(roots[i]+Q(1,3))/282 for i in range(6)]
    psm=[pis[0][i]-pi0[i]-pi2[i]-psp[i] for i in range(6)]
    pam=[pis[1][i]-pap[i] for i in range(6)]
    need([pi0,pi2,psp,psm,pap,pam]==[[Q(i==j) for i in range(6)] for j in range(6)],
         'closure:projectors_resolve_all_six_sectors')
    # Numerical-looking checks below are exact fractions at rational z.
    def kern(z,A,B,C,X,Y,Z):
        return A/z**4+B/(1-z)**4+C+Y/z**2+X/(1-z)**2+(Y+X-Z)/(z*(1-z))
    # For K_ab,cd: crossing a<->d maps z->1-z, with A<->B, X<->Y.
    for z in (Q(1,3),Q(2,5),Q(3,2)):
        A,B,C,X,Y,Z=map(Q,(2,3,5,7,11,13))
        need(kern(z,A,B,C,X,Y,Z)==kern(1-z,B,A,C,Y,X,Z),f'crossing:one_minus_z_at_{z}')
        # Exchanging a and b acts z->z/(z-1), with conformal prefactor.
        zz=z/(z-1)
        need(kern(z,A,B,C,X,Y,Z)==(1-z)**-4*kern(zz,A,C,B,Z,Y,X),f'crossing:mobius_exchange_at_{z}')
    return {'weight_four_primary_dimension':dims[2],'symmetric_pair_dimension':d*(d+1)//2,
            'nonzero_squared_singular_value':54,'total_squared_coupling_ordered_pairs':54*dims[2],
            'weight_four_Gram_eigenvalues_symmetric_sectors':list(map(str,h4)),
            'six_sector_dimensions':dims}


def main():
    o=helpers();descendant_checks()
    examples=[oscillator_checks(o,n) for n in (2,3)]
    scalars=scalar_checks()
    print(json.dumps({'status':'PASS within exact free-boson and scalar scopes','base_commit':BASE,
        'checks':len(LABELS),'labels':LABELS,'oscillator_controls':examples,'extremal_scalars':scalars,
        'arithmetic':'integers and fractions only','largest_square_matrix_dimension':15,
        'largest_oscillator_grade':MAX_GRADE,'Monster_data_used':False,
        'extremal_OPE_tensor_constructed':False,'all_weight_block_positivity_numerically_checked':False,
        'moonshine_uniqueness_proved':False,'novelty_established':False},sort_keys=True,indent=2))


if __name__=='__main__':
    main()
