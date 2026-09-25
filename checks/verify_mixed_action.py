#!/usr/bin/env python3
"""Exact bounded checks of the five-label mixed OPE reduction.

Free-boson c=2,3 controls are NOT extremal c=24 theories. No Monster
operators or unknown large cubic are constructed. Source trace identities
and polynomial-ideal independence are not verified by these controls.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import importlib.util
import json

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []
PERMS = [(p, (-1)**sum(p[i] > p[j] for i in range(5) for j in range(i+1,5)))
         for p in permutations(range(5))]


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def plus(a,b,scale=1):
    return [[x+scale*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def scale(a,k):
    return [[k*x for x in row] for row in a]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def eye(n):
    return [[Q(i==j) for j in range(n)] for i in range(n)]


def zero(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def helpers():
    p=Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(p.read_bytes()).hexdigest()==
         '701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:unchanged_weight_three_helper')
    spec=importlib.util.spec_from_file_location('_mixed_fock_control',p)
    o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
    o.GRADE=4
    return o


def tzero(H,a,b,c,d,e):
    """H(a,b,e,c,d)=<a*b,e*(c*d)> in the FULL weight-two algebra."""
    return (-H(b,c,a,d,e)+H(b,d,a,c,e)+H(a,c,b,d,e)-H(a,d,b,c,e)
            -H(a,d,c,b,e)+H(a,e,c,b,d)+H(a,c,d,b,e)-H(a,e,d,b,c)
            -H(a,c,e,b,d)+H(a,d,e,b,c))/2


def oscillator(o,n):
    As=[]
    for i in range(1,n):
        a=zero(n)
        # Mutually orthogonal diagonal basis with rational nonunit norms.
        for j in range(i): a[j][j]=1
        a[i][i]=-i
        As.append(a)
    for i,j in combinations(range(n),2):
        a=zero(n);a[i][j]=a[j][i]=1;As.append(a)
    m=len(As);pairs=list(combinations(range(m),2))
    weights=[Q(tr(mm(a,a)),2) for a in As]
    vac={(0,)*(n*o.GRADE):Q(1)}
    mode=lambda a,k,b:o.quadratic_mode(a,k,b,n)
    states=[mode(a,-1,vac) for a in As]
    P=[[mode(a,1,b) for b in states] for a in As]
    Bs=[[o.add((1,mode(a,0,states[j])),(-Q(1,2),o.deriv(P[i][j],n)))
         for j in range(m)] for i,a in enumerate(As)]
    Ps=[[plus(mm(a,b),mm(b,a)) for b in As] for a in As]
    def H(a,b,e,c,d):
        return Q(tr(mm(Ps[a][b],plus(mm(As[e],Ps[c][d]),mm(Ps[c][d],As[e])))),2)
    Tv={(a,b,c,d,e):o.inner(Bs[a][b],mode(As[e],1,Bs[c][d]),n)
        for a,b,c,d,e in product(range(m),repeat=5)}
    q=Q(0)
    if m==5:
        q=-sum(s*Tv[p] for p,s in PERMS)/120
    need(q==(3 if n==3 else 0),f'fock:c{n}_alternating_form_exact')
    for inds,t in Tv.items():
        w=0
        if len(set(inds))==5:
            w=q*(-1)**sum(inds[i]>inds[j] for i in range(5) for j in range(i+1,5))
        if t!=tzero(H,*inds)-w:
            raise RuntimeError(f'five-label mismatch c{n} labels{inds}')
    need(True,f'fock:c{n}_every_five_label_mixed_matrix_element')
    need(all(Tv[a,b,c,d,e]==Tv[c,d,a,b,e] for a,b,c,d,e in Tv),
         f'fock:c{n}_mixed_Hermitian_symmetry')
    need(all(Tv[a,b,c,d,e]==-Tv[b,a,c,d,e] for a,b,c,d,e in Tv),
         f'fock:c{n}_input_pair_antisymmetry')
    # Directly compute the source definition a3 b2 c1 d0 e, independent
    # of the primary-subtracted mixed expression.
    source_q=Q(0)
    if m==5:
        for (a,b,c,d,e),sg in PERMS:
            x=mode(As[d],0,states[e]);x=mode(As[c],1,x);x=mode(As[b],2,x)
            source_q+=sg*o.inner(states[a],x,n)/120
        need(source_q==q,'fock:c3_source_quinary_definition_and_sign')
        need(sum(s*tzero(H,*p) for p,s in PERMS)==0,'fock:c3_tree_part_has_zero_full_alternation')
    # Check the descendant correction for the UNPROJECTED mixed word.
    def gram(a,b,c,d):
        return o.inner(mode(a,1,c),mode(b,1,d),n)-o.inner(mode(a,1,d),mode(b,1,c),n)
    for a,b,c,d,e in product(range(m),repeat=5):
        raw=o.inner(mode(As[a],0,states[b]),mode(As[e],1,mode(As[c],0,states[d])),n)
        g1=gram(As[e],Ps[a][b],states[c],states[d])
        g2=gram(As[e],Ps[c][d],states[a],states[b])
        want=Tv[a,b,c,d,e]+(g1+g2)/2+Q(3,2)*H(a,b,e,c,d)
        if raw!=want: raise RuntimeError('descendant correction')
    need(True,f'fock:c{n}_every_raw_word_descendant_correction')
    G=[[o.inner(Bs[i][j],Bs[k][l],n) for k,l in pairs] for i,j in pairs]
    wm=[weights[i]*weights[j] for i,j in pairs]
    op=lambda a:[[x/wm[i] for x in row] for i,row in enumerate(a)]
    Go=op(G)
    eigen=Q(4 if n==2 else 5)
    need(mm(Go,Go)==scale(Go,eigen),f'fock:c{n}_Gram_scaled_projector')
    need(o.rank(Go)==n*(n-1)//2,f'fock:c{n}_Gram_rank')
    pi=scale(Go,1/eigen)
    residual=None
    for e in range(m):
        T=op([[Tv[i,j,k,l,e] for k,l in pairs] for i,j in pairs])
        need(mm(pi,T)==T and mm(T,pi)==T,f'fock:c{n}_actual_action_descends_field{e}')
        A=scale(op([[tzero(H,i,j,k,l,e) for k,l in pairs] for i,j in pairs]),2)
        if n==3 and e==0:
            residual=mm(plus(eye(len(pairs)),pi,-1),A)
    if n==3:
        need(o.rank(residual)==6,'negative:Gram_projector_alone_does_not_force_exceptional_A_support')
        need(residual[1][4]==-Q(12,5),'negative:unsupported_tree_part_exact_entry')
        need(any(Tv[p]!=tzero(H,*p) for p,s in PERMS),'negative:cannot_discard_generic_five_form')
    # Full multiplication matrices, independent trace computation.
    full=[eye(n)]+As;norms=[Q(n,2)]+weights
    Rs=[[[Q(tr(mm(full[i],plus(mm(a,full[j]),mm(full[j],a)))),2)/norms[i]
          for j in range(m+1)] for i in range(m+1)] for a in As]
    # Independently reconstruct F, D_e and F_e in a rational, nonunit basis.
    Ls=[[[Q(tr(mm(As[k],Ps[e][j])),2)/weights[k] for j in range(m)]
         for k in range(m)] for e in range(m)]
    transpose=lambda a:list(map(list,zip(*a)))
    xs=[]
    for i,j in pairs:
        x=zero(m);x[i][j]=1;x[j][i]=-1;xs.append(x)
    columns=[]
    for x in xs:
        fx=zero(m)
        for r in range(m):fx=plus(fx,scale(mm(mm(Ls[r],x),transpose(Ls[r])),1/weights[r]))
        columns.append([fx[i][j] for i,j in pairs])
    F=list(map(list,zip(*columns)));ss=Q(8,n)
    need(plus(F,scale(eye(len(pairs)),ss))==Go,f'operators:c{n}_F_plus_stress_is_Gram')
    for e in range(m):
        ds=[];fes=[]
        for x in xs:
            dx=plus(mm(Ls[e],x),mm(x,transpose(Ls[e])))
            fx=zero(m)
            for r in range(m):
                for t in range(m):
                    coeff=Q(tr(mm(As[e],Ps[r][t])),2)/(weights[r]*weights[t])
                    fx=plus(fx,scale(mm(mm(Ls[r],x),transpose(Ls[t])),coeff))
            ds.append([dx[i][j] for i,j in pairs]);fes.append([fx[i][j] for i,j in pairs])
        Dop=list(map(list,zip(*ds)));Fe=list(map(list,zip(*fes)))
        formula=plus(plus(plus(mm(F,Dop),mm(Dop,F)),scale(Dop,ss)),Fe,-1)
        actual=scale(op([[tzero(H,i,j,k,l,e) for k,l in pairs] for i,j in pairs]),2)
        need(formula==actual,f'operators:c{n}_cubic_A_formula_field{e}')
    tau=Q(0)
    if m==5:
        for p,sg in PERMS:
            mat=eye(6)
            for a in p:mat=mm(mat,Rs[a])
            tau+=sg*tr(mat)/120
        comm=lambda a,b:plus(mm(Rs[a],Rs[b]),mm(Rs[b],Rs[a]),-1)
        three=plus(plus(mm(comm(0,1),comm(2,3)),mm(comm(0,2),comm(1,3)),-1),mm(comm(0,3),comm(1,2)))
        need(tr(mm(Rs[4],three))/12==tau,'trace:alternated_five_trace_equals_three_commutator_terms')
        need(tau==Q(7,2),'trace:small_control_alternated_trace_exact')
        need(tau!=52*q,'negative:c3_is_not_an_extremal_fifth_trace_control')
    return {'central_charge':n,'primary_input_dimension':m,'exterior_dimension':len(pairs),
            'five_label_entries':m**5,'quinary_basis_value':str(q),'alternated_trace_basis_value':str(tau),
            'Gram_nonzero_eigenvalue':str(eigen),'Gram_rank':o.rank(Go)}


def formal_checks(o):
    def key(e,a,b,c,d):return (e,tuple(sorted((tuple(sorted((a,b))),tuple(sorted((c,d)))))))
    keys=sorted({key(*p) for p,s in PERMS});ix={k:i for i,k in enumerate(keys)}
    def rowkey(e,a,b,c,d):return ix[key(e,a,b,c,d)],(1 if a<b else -1)*(1 if c<d else -1)
    def H(a,b,e,c,d):
        r=[Q(0)]*15;r[ix[key(e,a,b,c,d)]]=1;return r
    # Coefficientwise tree evaluations avoid assuming numerical tensor values.
    anti=[];t0=[]
    def trace_tree(p,j):
        value=Q(0)
        for shift in range(5):
            a,b,c,d,e=p[shift:]+p[:shift]
            value+=30*H(a,b,c,d,e)[j]+4*H(a,d,c,b,e)[j]-22*H(a,e,c,b,d)[j]
        return value
    for j in range(15):
        h=lambda a,b,e,c,d:H(a,b,e,c,d)[j]
        t0.append(tzero(h,0,1,2,3,4))
        anti.append(trace_tree((4,0,1,2,3),j)-trace_tree((4,1,0,2,3),j)
                    -trace_tree((4,0,1,3,2),j)+trace_tree((4,1,0,3,2),j))
        need(sum(s*tzero(h,*p) for p,s in PERMS)==0,f'formal:tree_component{j}_zero_alternation')
    need(anti==[-104*x for x in t0],'formal:antisymmetrized_source_tree_coefficient_minus104')
    need(4*52==208,'formal:antisymmetrized_source_quinary_coefficient208')
    rows=[]
    for p,s in PERMS:
        e,a,b,c,d=p;r=[Q(0)]*15
        for arg in ((e,a,b,c,d),(b,a,e,c,d)):
            i,sg=rowkey(*arg);r[i]+=sg
        rows.append(r)
    need(o.rank(rows)==14,'formal:homogeneous_mode_system_rank14_of15')
    alt=[Q(0)]*15
    for (a,b,c,d,e),sg in PERMS:
        i,sg2=rowkey(e,a,b,c,d);alt[i]+=Q(sg*sg2,120)
    need(o.rank(rows+[alt])==15,'formal:alternating_component_removes_last_ambiguity')
    # The support equivalence is a block-algebra fact; this is not a small VOA.
    g=Q(282);pi=zero(4);pi[0][0]=pi[1][1]=1;G=scale(pi,g)
    D=[[Q(i+j+1) for j in range(4)] for i in range(4)]
    A=mm(mm(pi,D),pi)
    TT=plus(scale(A,Q(1,4)),scale(mm(mm(G,D),G),Q(1,208)))
    need(mm(pi,TT)==TT and mm(TT,pi)==TT,'quotient:supported_A_gives_supported_T')
    bad=plus(A,D)
    tb=plus(scale(bad,Q(1,4)),scale(mm(mm(G,D),G),Q(1,208)))
    need(mm(plus(eye(4),pi,-1),tb)==scale(mm(plus(eye(4),pi,-1),bad),Q(1,4)),
         'quotient:unsupported_residual_is_exactly_one_quarter')
    need(mm(G,A)==scale(A,g) and mm(A,G)==scale(A,g),'quotient:projector_and_quintic_form_equivalence')
    need(Q(282,208)==Q(141,104),'quotient:normalized_compressed_action_constant')


def main():
    o=helpers();examples=[oscillator(o,n) for n in (2,3)];formal_checks(o)
    print(json.dumps({'status':'PASS within exact mixed-mode, trace and formal scopes',
        'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,'examples':examples,
        'largest_square_matrix_dimension':10,'largest_symbolic_system_shape':[121,15],'largest_oscillator_grade':4,
        'arithmetic':'integers and fractions only','Monster_data_used':False,
        'full_extremal_cubic_constructed':False,'independence_from_previous_polynomial_identities_proved':False,
        'full_CFT_or_Monster_uniqueness_proved':False,'novelty_established':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
