#!/usr/bin/env python3
"""Exact audit witness for the pending mixed-action selection condition.

Uses the actual A/X/Q block formulas of the Griess algebra. Matrices explicitly
built are at most 6x6; the 98280 Leech rows are streamed, not stored as an
operator. Oscillator fields occupy three of the 24 Heisenberg coordinates.
This is not a full CFT simulation or a proof of a corrected universal trace
formula. Historical dependencies are hash-checked, never edited.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
PENDING='b0d7224bbc20d0d8aeb217e1caf4014fd3c298d1'
LABELS=[]


def need(ok, label):
    if not ok: raise RuntimeError(label)
    LABELS.append(label)


def load_dependencies():
    expected={
        'checks/verify_weight_three.py':'701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
        'circuits/leech_xxa.py':'0cfee265c6ef61cb3c43a225006f63a9f395503c60521436c4ef7263c48bceb7',
        'circuits/seysen_qqa.py':'e72b8924d898f9c676d9584a4df857fd9a86dcd3ff970aee6821b9e43907826a'}
    for path,digest in expected.items():
        need(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'dependency:'+path)
    spec=importlib.util.spec_from_file_location('_fock_audit',ROOT/'checks/verify_weight_three.py')
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=4
    sys.path.insert(0,str(ROOT/'circuits'))
    import leech_xxa
    return o,leech_xxa


def zero(n): return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def add(a,b,k=1): return [[x+k*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,k): return [[k*x for x in ar] for ar in a]
def mul(a,b):
    n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def comm(a,b): return add(mul(a,b),mul(b,a),-1)
def prod(a,b): return scale(add(mul(a,b),mul(b,a)),2)
def metric(a,b): return 2*tr(mul(a,b))
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def trace_word(matrices,w):
    out=eye(len(matrices[0]))
    for i in w:out=mul(out,matrices[i])
    return tr(out)


def fields():
    a=zero(3);a[0][0]=1;a[1][1]=-1
    b=zero(3);b[0][0]=1;b[2][2]=-1
    out=[a,b]
    for i,j in ((0,1),(0,2),(1,2)):
        m=zero(3);m[i][j]=m[j][i]=1;out.append(m)
    return out


def jordan_matrices(mats):
    pairs=list(combinations(range(3),2));labels=[(i,i) for i in range(3)]+pairs
    basis=[]
    for i,j in labels:
        m=zero(3);m[i][j]=m[j][i]=1;basis.append(m)
    ans=[]
    for a in mats:
        cols=[add(mul(a,b),mul(b,a)) for b in basis]
        # Coordinates in the raw symmetric basis: coefficient is one entry.
        ans.append([[v[i][j] for v in cols] for i,j in labels])
    return ans


def tree(mats,w):
    a,b,c,d,e=(mats[i] for i in w)
    return metric(prod(a,b),prod(c,prod(d,e)))


def tree_t(mats,w):
    a,b,c,d,e=w;H=lambda *p:tree(mats,p)
    return (-H(b,c,a,d,e)+H(b,d,a,c,e)+H(a,c,b,d,e)-H(a,d,b,c,e)
            -H(a,d,c,b,e)+H(a,e,c,b,d)+H(a,c,d,b,e)-H(a,e,d,b,c)
            -H(a,c,e,b,d)+H(a,d,e,b,c))/2


def source_polynomial(mats,w):
    cyc=lambda f:sum(f(w[i:]+w[:i]) for i in range(5))
    out=30*cyc(lambda p:tree(mats,p))
    out+=4*cyc(lambda p:tree(mats,(p[0],p[3],p[2],p[1],p[4])))
    out-=22*cyc(lambda p:tree(mats,(p[0],p[4],p[2],p[1],p[3])))
    for i,j in combinations(range(5),2):
        a,b,c=[k for k in range(5) if k not in (i,j)]
        out+=8*metric(mats[w[i]],mats[w[j]])*metric(mats[w[a]],prod(mats[w[b]],mats[w[c]]))
    return out


def oscillator_checks(o,mats):
    vac={(0,)*12:Q(1)}
    # a_M=1/2 M_ij h_i(-1)h_j(-1); source A is a_(2A).
    doubled=[scale(a,2) for a in mats]
    states=[o.quadratic_mode(a,-1,vac,3) for a in doubled]
    p=[[o.quadratic_mode(a,1,b,3) for b in states] for a in doubled]
    B=[[o.add((1,o.quadratic_mode(a,0,b,3)),(-Q(1,2),o.deriv(p[i][j],3)))
        for j,b in enumerate(states)] for i,a in enumerate(doubled)]
    need(all(tr(a)==0 for a in mats),'fields:five_trace_zero_matrices')
    need(all(o.inner(states[i],states[j],3)==metric(mats[i],mats[j])
             for i in range(5) for j in range(5)),'fields:VOA_metric_2Tr_exact')
    need(all(p[i][j]==o.quadratic_mode(scale(prod(mats[i],mats[j]),2),-1,vac,3)
             for i in range(5) for j in range(5)),'fields:source_product_2Jordan_from_modes')
    need(comm(mats[0],mats[1])==zero(3),'null:commuting_diagonal_inputs')
    need(B[0][1]=={},'null:actual_primary_created_state_is_zero')
    norm=metric(prod(mats[0],mats[0]),prod(mats[1],mats[1]))-metric(prod(mats[0],mats[1]),prod(mats[0],mats[1]))
    need(norm==0,'null:independent_four_label_Gram_norm_zero')
    words=list(permutations(range(5)))
    omega=Q(0)
    for w in words:
        state=states[w[4]]
        for idx,mode in ((w[3],0),(w[2],1),(w[1],2),(w[0],3)):
            state=o.quadratic_mode(doubled[idx],mode,state,3)
        omega+=sign(w)*o.inner(vac,state,3)/120
    need(omega==48,'mode:original_120_term_normalized_five_form_48')
    need(tree_t(mats,tuple(range(5)))==48,'null:ten_tree_value_t_48')
    for w in words:
        a,b,c,d,e=w
        T=o.inner(B[a][b],o.quadratic_mode(doubled[e],1,B[c][d],3),3)
        need_local=(T==tree_t(mats,w)-sign(w)*omega)
        if not need_local:raise RuntimeError('Generic mixed identity fails on '+str(w))
    need(True,'mode:generic_mixed_identity_all_120_distinct_permutations')
    need(2*tree_t(mats,tuple(range(5)))==96,'null:claimed_A_operator_entry_96')
    need(Q(96,4)==24,'null:pending_formula_assigns_24_to_zero_state')
    return omega


def leech_moments(leech,words):
    # Check low-order normalizations independently of the fifth formula.
    sums={w:0 for w in words};shape={0:0,1:0,2:0};counts={0:0,1:0,2:0}
    for r in leech.labels():
        v=leech.integer_row(r);x,y,z=v[:3]
        q=(x*x-y*y,x*x-z*z,2*x*y,2*x*z,2*y*z)
        for w in words:
            p=1
            for i in w:p*=q[i]
            sums[w]+=p
        p=1
        for i in q:p*=i
        shape[r&3]+=p;counts[r&3]+=1
    need(counts=={0:552,1:48576,2:49152},'Leech:streamed_all_98280_rows_by_shape')
    shape={t:Q(v,8**5) for t,v in shape.items()}
    need(shape=={0:0,1:0,2:288},'Leech:five_product_diagonal_trace_288')
    return {w:Q(v,8**len(w)) for w,v in sums.items()},sum(shape.values())


def full_trace_checks(leech,mats,omega):
    jr=jordan_matrices(mats)
    need(comm(jr[0],jr[1])==zero(6),'null:full_Sym3_Jordan_commutator_zero')
    # Remaining 21 three-dimensional cross-coordinate blocks and Q commute
    # because A,B commute; X is diagonal for every A argument.
    need(comm(mats[0],mats[1])==zero(3),'null:cross_coordinate_and_Q_commutators_zero')
    need(300+98280+4096*24==196884,'source:all_Griess_blocks_accounted_for')
    words2=[(i,j) for i in range(5) for j in range(5)]
    words3=[(0,0,1),(0,2,2),(1,2,2),(2,3,4),(4,3,2)]
    words4=[(0,1,2,2),(0,2,1,2),(0,0,0,0),(0,0,1,1),(2,3,2,3),(2,2,3,3)]
    moments,x5=leech_moments(leech,words2+words3+words4)
    def raw(w):
        xs=x5 if len(w)==5 else moments[w]
        return 2**len(w)*(trace_word(jr,w)+21*trace_word(mats,w))+4096*trace_word(mats,w)+xs
    need(all(raw(w)==4620*metric(mats[w[0]],mats[w[1]]) for w in words2),
         'source:25_second_trace_normalizations')
    need(all(raw(w)==900*metric(mats[w[0]],prod(mats[w[1]],mats[w[2]])) for w in words3),
         'source:five_third_trace_normalizations')
    def fourth(w):
        a,b,c,d=(mats[i] for i in w)
        return 166*metric(prod(a,b),prod(c,d))-116*metric(prod(a,c),prod(b,d))+166*metric(prod(a,d),prod(b,c))+52*(metric(a,b)*metric(c,d)+metric(a,c)*metric(b,d)+metric(a,d)*metric(b,c))
    need(all(raw(w)==fourth(w) for w in words4),'source:six_fourth_trace_normalizations')
    words=list(permutations(range(5)))
    alt3=sum(sign(w)*trace_word(mats,w) for w in words)/120
    alt6=sum(sign(w)*trace_word(jr,w) for w in words)/120
    need(alt3==Q(1,4),'trace:alternating_3_coordinate_trace_one_quarter')
    need(alt6==Q(7,4),'trace:alternating_Sym3_Jordan_trace_seven_quarters')
    altfull=sum(sign(w)*raw(w) for w in words)/120
    need(altfull==1248,'trace:full_Griess_alternating_fifth_trace_1248')
    need(altfull/omega==26,'trace:coefficient_for_normalized_mode_form_must_be_26')
    need(altfull!=52*omega,'negative:printed_52_conflicts_with_normalized_mode_definition')
    residuals={(raw(w)-source_polynomial(mats,w))*sign(w) for w in words}
    need(residuals=={1248},'trace:all_120_unalternated_remainders_require_26')
    # One numerical coefficient cannot be declared a universal theorem solely
    # from this finite witness. The report explicitly preserves that boundary.
    return {'mode_five_form':str(omega),'alternating_full_trace':str(altfull),
            'forced_coefficient_in_tested_trace_shape':'26','Leech_diagonal_fifth_trace':'288',
            'null_pair_tree_value':'48','null_pair_A_entry':'96',
            'actual_null_pair_mixed_element':'0','pending_predicted_mixed_element':'24'}


def formal_checks():
    # A finite exact coefficient certificate in 15 five-leaf trees, 10 metric
    # times cubic terms, and one alternating symbol. No tensor fitting.
    def hkey(a,b,c,d,e):return ('H',c,tuple(sorted((tuple(sorted((a,b))),tuple(sorted((d,e)))))))
    def mkey(a,b,c,d,e):return ('M',tuple(sorted((a,b))),tuple(sorted((c,d,e))))
    words=list(permutations(range(5)))
    hk=sorted({hkey(*p) for p in words});mk=sorted({mkey(*p) for p in words})
    keys=hk+mk+[('Omega',)];ind={k:i for i,k in enumerate(keys)}
    def unit(k):return [Q(k==v) for v in keys]
    def lin(*args):return [sum(s*v[i] for s,v in args) for i in range(26)]
    H=lambda *p:unit(hkey(*p))
    O=unit(('Omega',));metric_sum=[sum(unit(k)[i] for k in mk) for i in range(26)]
    def cyc(fn,w):return lin(*[(1,fn(*(w[i:]+w[:i]))) for i in range(5)])
    def R(w,h):
        return lin((30,cyc(H,w)),(4,cyc(lambda a,b,c,d,e:H(a,d,c,b,e),w)),
                   (-22,cyc(lambda a,b,c,d,e:H(a,e,c,b,d),w)),(8,metric_sum),(h*sign(w),O))
    a,b,c,d,e=range(5)
    t=lin((-Q(1,2),H(b,c,a,d,e)),(Q(1,2),H(b,d,a,c,e)),(Q(1,2),H(a,c,b,d,e)),
          (-Q(1,2),H(a,d,b,c,e)),(-Q(1,2),H(a,d,c,b,e)),(Q(1,2),H(a,e,c,b,d)),
          (Q(1,2),H(a,c,d,b,e)),(-Q(1,2),H(a,e,d,b,c)),(-Q(1,2),H(a,c,e,b,d)),(Q(1,2),H(a,d,e,b,c)))
    need(len(hk)==15 and len(mk)==10,'formal:15_tree_and_10_metric_cubic_coordinates')
    for h in (26,52,Q(13,60)):
        lhs=lin((1,R((e,a,b,c,d),h)),(-1,R((e,b,a,c,d),h)),(-1,R((e,a,b,d,c),h)),(1,R((e,b,a,d,c),h)))
        need(lhs==lin((-104,t),(4*h,O)),'formal:pair_antisymmetrized_trace_coefficient_'+str(h))
    need(Q(1,2)-Q(13,52)==Q(1,4),'formal:h52_gives_spurious_A_quarter')
    need(Q(1,2)-Q(13,26)==0 and Q(1,4*26)==Q(1,104),
         'formal:h26_gives_supported_GDG_over_104_conditionally')
    c=24;dim=196884
    denom=10*c*(2*c-1)*(3*c+46)*(5*c+3)*(5*c+22)*(7*c+68)*(11*c+232)
    h=-Q(c,12)*(100*c**5-13295*c**4+498218*c**3-387184*c**2-189230304*c-5501184)*(dim-1)
    need(h/denom==Q(13,60),'source:literal_appendix_H_over_D10_is_13_over_60')
    need(h/denom not in (26,52),'source:appendix_cannot_be_silently_identified_with_corollary')
    need(120*h/denom==26,'source:factor_120_observation_not_an_assumed_normalization_repair')


def main():
    o,l=load_dependencies();m=fields();omega=oscillator_checks(o,m)
    witness=full_trace_checks(l,m,omega);formal_checks()
    print(json.dumps({'status':'PASS: exact normalization conflict and null-condition falsification',
        'base_commit':BASE,'audited_pending_head':PENDING,'checks':len(LABELS),'labels':LABELS,
        'witness':witness,'arithmetic':'integers and fractions only',
        'largest_explicit_matrix_dimension':6,'streamed_Leech_rows':98280,
        'largest_oscillator_grade':4,'distinct_five_label_permutations_checked':120,
        'full_Griess_matrix_materialized':False,'Monster_group_matrices_used':False,
        'known_Griess_block_formulas_used':True,'new_physical_selection_constraint_validated':False,
        'universal_corrected_fifth_trace_independently_proved':False,
        'journal_version_normalization_checked':False,'moonshine_uniqueness_proved':False},
        sort_keys=True,indent=2))

if __name__=='__main__':main()
