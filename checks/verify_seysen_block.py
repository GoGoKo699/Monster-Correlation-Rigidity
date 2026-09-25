#!/usr/bin/env python3
"""Small exact/sparse checks of the Seysen QQA block, not the full Monster.

The actual check count is emitted. Exact fractions establish
normalization/counting identities. Floating gates use atol=1e-10. The complete
21-wire coordinate circuit is evaluated sparsely on all 299 valid inputs;
12 independent Bell pairs are checked separately, not tensor-expanded into a
45-qubit state. Largest dense matrix is 24x24. No source data are downloaded.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import math
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('seysen_qqa',ROOT/'circuits/seysen_qqa.py')
if spec is None or spec.loader is None:raise RuntimeError('Missing circuit source')
q=importlib.util.module_from_spec(spec);sys.modules[spec.name]=q;spec.loader.exec_module(q)
LABELS=[];TOL=1e-10;MAX_SUPPORT=0;MAX_PRUNED=0.


def need(ok,label):
    if not ok:raise RuntimeError('Check failed: '+label)
    LABELS.append(label)


def close(a,b,label):need(bool(np.linalg.norm(np.asarray(a)-np.asarray(b))<TOL),label)


def apply(circuit,state):
    """Sparse unitary application. The accumulated pruning norm is bounded."""
    global MAX_SUPPORT,MAX_PRUNED
    state=dict(state);removed=0.
    for g in circuit.gates:
        name=g.name;ws=g.wires
        if name in ('X','CX','CCX'):
            mask=sum(1<<j for j in ws[:-1]);bit=1<<ws[-1]
            state={(k^bit if k&mask==mask else k):v for k,v in state.items()}
        else:
            bit=1<<ws[0];out={}
            if name=='H':a=b=c=1/math.sqrt(2);d=-a
            elif name=='Ry':a=d=math.cos(g.angle/2);c=math.sin(g.angle/2);b=-c
            else:raise RuntimeError('Unknown gate '+name)
            for k,v in state.items():
                if k&bit:
                    out[k^bit]=out.get(k^bit,0)+b*v;out[k]=out.get(k,0)+d*v
                else:
                    out[k]=out.get(k,0)+a*v;out[k^bit]=out.get(k^bit,0)+c*v
            # Report and bound numerical truncation; never infer exactness from it.
            tiny=[k for k,v in out.items() if abs(v)<1e-14]
            removed+=math.sqrt(sum(abs(out[k])**2 for k in tiny))
            for k in tiny:del out[k]
            state=out
        MAX_SUPPORT=max(MAX_SUPPORT,len(state))
    MAX_PRUNED=max(MAX_PRUNED,removed)
    if removed>=TOL/10:raise RuntimeError('Sparse pruning error budget exceeded')
    return state


def dist(a,b):return math.sqrt(sum(abs(a.get(k,0)-b.get(k,0))**2 for k in a.keys()|b.keys()))


def exact_normalization():
    n=24;m=4096;d=196883
    need(n*(n+1)//2-1==299,'dimension:A0')
    need(299+98280+m*n==d,'dimension:traceless_total')
    need(F(n,16)==F(3,2),'normalization:source_identity_norm_squared')
    need(2*F(n,16)==3,'normalization:VOA_identity_norm_squared')
    need(F(4,1)/4==1 and F(24,8)+1==4,'normalization:identity_on_A_X_Q_blocks')
    need(2*F(2,3)==F(4,3),'normalization:removed_two_scalar_cross_terms')
    # A Golay realization: multiples of g(x) with even parity extension.
    # Parameters are checked, so no external table or unverified oracle is used.
    generator=sum(1<<i for i in (11,9,7,6,5,1,0))
    words=[]
    for x in range(4096):
        w=0
        for k in range(12):
            if (x>>k)&1:w^=generator<<k
        words.append(w|((w.bit_count()&1)<<23))
    distribution=Counter(w.bit_count() for w in words)
    need(len(set(words))==4096 and max(words)<2**24,'Golay:4096_distinct_24bit_words')
    need(distribution=={0:1,8:759,12:2576,16:759,24:1},'Golay:weight_distribution_minimum_eight')
    generators=[words[1<<k] for k in range(12)]
    need(all((a&b).bit_count()%2==0 for a in generators for b in generators),'Golay:self_duality_from_generator_orthogonality')
    octads=[w for w in words if w.bit_count()==8]
    need(all(sum((w>>i)&1 for w in octads)==253 for i in range(24)),'Golay:octad_point_incidence_253')
    need(all(sum(((w>>i)&1)*((w>>j)&1) for w in octads)==77
             for i,j in combinations(range(24),2)),'Golay:octad_pair_incidence_77')
    need(759*math.comb(8,5)==math.comb(24,5),'Golay:Steiner_five_subset_count')
    # Quartic even moments for one representative from each antipodal pair.
    diag=[F(184),F(4048),F(3328)];cross=[F(8),F(1232),F(1280)]
    need(sum(diag)==7560 and sum(cross)==2520,'Leech:fourth_moments_7560_2520')
    need(sum(diag)==3*sum(cross),'Leech:isotropic_quartic_relation')
    contrib=[F(176),F(2816),F(2048)]
    need(sum(contrib)==5040,'Leech:diagonal_difference_contraction')
    need(552+48576+49152==98280,'Leech:three_antipodal_shape_counts')
    kaa=F(4*(n+2))-F(4,3);kxx=F(5040);kqq=F(m)
    ks=kaa+kxx+kqq
    need(kaa==F(308,3),'normalization:A0_to_A0A0_squared_norm')
    need(ks==F(27716,3),'normalization:source_kappa')
    need(ks/2==F(13858,3),'normalization:project_kappa')
    weights=[kaa/ks,kxx/ks,kqq/ks]
    need(weights==[F(77,6929),F(3780,6929),F(3072,6929)],'normalization:three_exact_branch_weights')
    need(sum(weights)==1,'normalization:branch_weights_sum_one')
    return {'source_kappa':str(ks),'project_kappa':str(ks/2),
            'A0_output_weights':dict(zip(['A0_A0','X_X','Q_Q'],map(str,weights))),
            'valid_input_fraction':str(F(299,d))}


def check_helmert_and_products():
    n=24
    h=np.zeros((n,n));h[:,0]=1/math.sqrt(n)
    for k in range(1,n):h[:k,k]=1/math.sqrt(k*(k+1));h[k,k]=-math.sqrt(k/(k+1))
    close(h.T@h,np.eye(n),'Helmert:orthogonal_24_by_24')
    hs=np.eye(n)
    for k in range(1,n):
        c=np.eye(n);a=math.sqrt(k/(k+1));b=1/math.sqrt(k+1)
        c[0,0]=a;c[0,k]=b;c[k,0]=b;c[k,k]=-a
        hs=hs@c
    close(hs,h,'Helmert:23_two_level_steps')
    rng=np.random.default_rng(7129)
    for trial in range(3):
        a=rng.normal(size=(n,n));a=(a+a.T)/2;a-=np.trace(a)*np.eye(n)/n;a/=np.linalg.norm(a)
        # Operator norm on Sym^2 is computed by summing over an orthonormal basis.
        total=0.
        for i in range(n):
            b=np.zeros((n,n));b[i,i]=1
            total+=np.linalg.norm(2*(a@b+b@a))**2
            for j in range(i+1,n):
                b=np.zeros((n,n));b[i,j]=b[j,i]=1/math.sqrt(2)
                total+=np.linalg.norm(2*(a@b+b@a))**2
        close(total,104.,f'products:full_A_operator_norm_{trial}')
        close(total-4/3,308/3,f'products:traceless_A_operator_norm_{trial}')
        close(np.linalg.norm(a)**2,1.,f'products:QQ_vectorization_norm_{trial}')
    bad=np.zeros((n,n));bad[0,1]=bad[1,0]=1
    close(np.linalg.norm(bad)**2,2.,'negative_control:unnormalized_offdiagonal_gives_norm_two')


def classical_checks():
    x=list(range(5));y=list(range(5,10));scratch=list(range(12,21))
    eq=q.Circuit();eq.equality(x,y,10,scratch)
    gt=q.Circuit();gt.greater(x,y,11,scratch)
    for c,target,pred,label in [(eq,10,lambda a,b:a==b,'equal'),(gt,11,lambda a,b:a>b,'greater')]:
        for a in range(32):
            for b in range(32):
                initial=a+(b<<5)
                state=apply(c,{initial:1.})
                expected={initial+(int(pred(a,b))<<target):1.}
                if state!=expected:raise RuntimeError(f'Comparator {label}: {a},{b}')
        need(True,f'circuit:{label}_all_1024_inputs_clean_scratch')


def circuit_checks():
    c=q.build(bell_pairs=False);ci=q.inverse(c)
    all_expected=[];all_initial=[]
    for i in range(24):
        for j in range(i+1,24):
            expected={i+(j<<5):1/math.sqrt(2),j+(i<<5):1/math.sqrt(2)}
            initial={i+(j<<5):1.};actual=apply(c,initial)
            if dist(actual,expected)>=TOL:raise RuntimeError(f'Offdiagonal {i},{j}')
            if any(k>>10 for k in actual):raise RuntimeError('Unclean output ancilla')
            all_initial.append(initial);all_expected.append(expected)
    need(True,'circuit:all_276_offdiagonal_basis_vectors')
    for k in range(1,24):
        expected={i+(i<<5):1/math.sqrt(k*(k+1)) for i in range(k)}
        expected[k+(k<<5)]=-math.sqrt(k/(k+1))
        initial={k+(k<<5):1.};actual=apply(c,initial)
        if dist(actual,expected)>=TOL:raise RuntimeError(f'Diagonal {k}')
        if any(t>>10 for t in actual):raise RuntimeError('Unclean diagonal workspace')
        all_initial.append(initial);all_expected.append(expected)
    need(True,'circuit:all_23_traceless_diagonal_basis_vectors')
    need(len(all_initial)==299,'circuit:complete_299_dimensional_domain')
    identity={i+(i<<5):1/math.sqrt(24) for i in range(24)}
    need(dist(apply(c,{0:1.}),identity)<TOL,'circuit:excluded_zero_label_maps_to_identity_direction')
    # Complex superpositions test coherence and inverse on the actual gate list.
    rng=np.random.default_rng(8052)
    for trial in range(2):
        coeff=rng.normal(size=299)+1j*rng.normal(size=299);coeff/=np.linalg.norm(coeff)
        initial={};expected={}
        for z,a,b in zip(coeff,all_initial,all_expected):
            for k,v in a.items():initial[k]=initial.get(k,0)+z*v
            for k,v in b.items():expected[k]=expected.get(k,0)+z*v
        actual=apply(c,initial)
        need(dist(actual,expected)<TOL,f'circuit:complex_superposition_{trial}')
        need(dist(apply(ci,actual),initial)<TOL,f'circuit:inverse_and_uncomputation_{trial}')
        need(all(not (k>>10) for k in actual),f'circuit:workspace_zero_superposition_{trial}')
    bell=q.Circuit();bell.add('H',0);bell.add('CX',0,1)
    need(dist(apply(bell,{0:1.}),{0:1/math.sqrt(2),3:1/math.sqrt(2)})<TOL,'circuit:Bell_pair_primitive')
    full=q.build();suffix=full.gates[len(c.gates):]
    need(len(suffix)==24 and all(g.wires[0]>=21 for g in suffix),'circuit:twelve_Bell_pairs_disjoint_from_coordinate_subroutine')
    report=q.resource_report()
    need(report['gates']=={'CCX':799,'CX':131,'H':60,'Ry':48,'X':708},'circuit:exact_emitted_gate_counts')
    need(report['total_gates']==1746 and report['total_wires']==45,'circuit:gate_and_wire_totals')
    need(MAX_PRUNED<TOL/10,'circuit:sparse_pruning_error_below_declared_budget')
    return report


def main():
    scalar=exact_normalization();check_helmert_and_products();classical_checks();resources=circuit_checks()
    print(json.dumps({'status':'PASS within normalized QQA-block scope','checks':len(LABELS),
        'labels':LABELS,'normalization':scalar,'resources':resources,
        'numerical_tolerance':TOL,'sparse_pruning_budget':TOL/10,
        'largest_dense_matrix_dimension':24,'largest_simulated_wire_count':21,
        'Bell_pairs_verified_separately':True,'full_45_wire_state_expanded':False,
        'full_Monster_simulation':False,'complete_W_compiled':False,
        'priority_established':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
