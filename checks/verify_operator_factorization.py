#!/usr/bin/env python3
"""Exact six-label factorization certificate plus independent small controls.

The symbolic proof uses the declared cubic trace equations, not numerical
Monster data. Controls evaluate unrestricted small real cubics directly and
must NOT be presented as extremal CFTs or as satisfying the physical inputs.
NumPy object arrays perform integer/Fraction contractions without roundoff.
"""
from __future__ import annotations
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import combinations, permutations
from functools import lru_cache
import json
import random
import numpy as np
import operator_factorization_graphs as g

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[]
LARGEST_ARRAY_ENTRIES=0
LARGEST_MATRIX_DIMENSION=0

def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    LABELS.append(label)

def keep_size(a):
    global LARGEST_ARRAY_ENTRIES,LARGEST_MATRIX_DIMENSION
    LARGEST_ARRAY_ENTRIES=max(LARGEST_ARRAY_ENTRIES,int(a.size))
    if a.ndim==2 and a.shape[0]==a.shape[1]:
        LARGEST_MATRIX_DIMENSION=max(LARGEST_MATRIX_DIMENSION,a.shape[0])
    return a

def symmetric_cubic(d,seed):
    rng=random.Random(seed);C=np.zeros((d,d,d),dtype=object)
    for i in range(d):
        for j in range(i,d):
            for k in range(j,d):
                value=rng.randint(-2,3)
                for p in set(permutations((i,j,k))):C[p]=value
    return keep_size(C)

class ClosedGraphEvaluator:
    """Independent dense contraction, with its own greedy contraction ordering."""
    def __init__(self,C):self.C=C;self.cache={}
    def value(self,graph):
        if graph in self.cache:return self.cache[graph]
        vertices,edges=graph
        if any(a<0 or b<0 for a,b in edges):raise ValueError('Only closed graphs here')
        incident=[[] for _ in range(vertices)]
        for idx,(a,b) in enumerate(edges):incident[a].append(idx);incident[b].append(idx)
        arrays=[]
        for labels in incident:
            if len(labels)!=3:raise ValueError('Nontrivalent input')
            A=self.C.copy();labels=list(labels)
            while len(set(labels))<len(labels):
                repeated=next(x for x in labels if labels.count(x)>1)
                i,j=[k for k,x in enumerate(labels) if x==repeated]
                A=np.trace(A,axis1=i,axis2=j);labels=[x for k,x in enumerate(labels) if k not in (i,j)]
            arrays.append((keep_size(np.asarray(A,dtype=object)),labels))
        scalar=F(1)
        while arrays:
            scalars=[i for i,(a,labels) in enumerate(arrays) if not labels]
            if scalars:
                for i in reversed(scalars):scalar*=arrays.pop(i)[0].item()
                continue
            if len(arrays)==1:raise ValueError('Uncontracted edge')
            options=[]
            for i,(a,la) in enumerate(arrays):
                for j in range(i+1,len(arrays)):
                    b,lb=arrays[j];shared=set(la)&set(lb)
                    if shared:
                        rank=len(la)+len(lb)-2*len(shared)
                        options.append((rank,-len(shared),i,j))
            if not options:raise ValueError('Disconnected non-scalar remainder')
            _,_,i,j=min(options);a,la=arrays[i];b,lb=arrays[j]
            shared=sorted(set(la)&set(lb));axesA=[la.index(x) for x in shared];axesB=[lb.index(x) for x in shared]
            c=keep_size(np.tensordot(a,b,axes=(axesA,axesB)))
            labels=[x for x in la if x not in shared]+[x for x in lb if x not in shared]
            arrays.pop(j);arrays.pop(i);arrays.append((c,labels))
        self.cache[graph]=scalar
        return scalar
    def polynomial(self,poly):return sum((a*self.value(k) for k,a in poly.items()),F(0))

def explicit_tensor_gram(C):
    """Direct matrices: no tensor graph generator, trace rules, or source coefficients."""
    d=len(C);L=[keep_size(C[i].copy()) for i in range(d)]
    pairs=list(combinations(range(d),2));wedges=[]
    for a,b in pairs:
        X=np.zeros((d,d),dtype=object);X[a,b]=1;X[b,a]=-1;wedges.append(keep_size(X))
    def field(X):return sum((A@X@A for A in L),np.zeros((d,d),dtype=object))
    def G(X):return field(X)+F(1,3)*X
    def D(a,X):return L[a]@X+X@L[a]
    def ad(A,X):return A@X-X@A
    values=[]
    for (a,b),X in zip(pairs,wedges):
        for Y in wedges:
            GY=G(Y)
            QY=D(a,G(D(b,GY)))-D(b,G(D(a,GY)))
            ops=(QY,ad(X,GY),ad(G(X),GY))
            for Z in wedges:
                GZ=G(Z)
                values.append([-F(1,2)*np.trace(GZ@op) for op in ops])
    # Tensor coefficients are defined for six ORDERED field indices. Each unit
    # exterior triple occurs 2^3 times; no normalized-Frobenius factor is used.
    M=[[8*sum((v[i]*v[j] for v in values),F(0)) for j in range(3)] for i in range(3)]
    return M,len(values)

def expand_boundary(poly):
    out=defaultdict(F)
    for graph,c in poly.items():
        n,edges=graph
        for perm,sign in g.GROUP:
            h=g.canon_edges(n,[(perm.get(a,a),perm.get(b,b)) for a,b in edges])
            out[h]+=c*F(sign,16)
    return {k:v for k,v in out.items() if v}

def graph_controls(certificate):
    # Prove that the signed boundary averaging changes none of the three
    # actual component tensors, not merely that their projected norms vanish.
    for kind in ('Q','x','Gx'):
        raw=g.component(kind)
        need(expand_boundary(raw)==raw,f'boundary:{kind}_exact_pair_antisymmetries')
        need(expand_boundary(g.project(raw))==raw,f'boundary:{kind}_canonical_orbits_reconstruct_original')
    need(len(g.GROUP)==16,'boundary:16_signed_permutations')
    need(len(g.PERMS)==12,'fifth:12_dihedral_trace_representatives')
    # Isomorphic relabelling is only dummy-index renaming.
    examples=list(certificate['raw_gram'][0][0])[:12]+list(g.SCALAR_GRAPHS[1:])
    rng=random.Random(240026)
    for i,graph in enumerate(examples):
        n,edges=graph;perm=list(range(n));rng.shuffle(perm)
        relabelled=[(perm[a] if a>=0 else a,perm[b] if b>=0 else b) for a,b in edges]
        need(g.canon_edges(n,relabelled)==graph,f'graph:dummy_relabelling_{i}')
    records=[]
    for d,seed in ((2,17),(3,28)):
        C=symmetric_cubic(d,seed);evaluator=ClosedGraphEvaluator(C)
        direct,count=explicit_tensor_gram(C)
        for i in range(3):
            for j in range(i,3):
                raw=g.norm_polynomial(certificate['components'][i],certificate['components'][j],loop_dimension=d)
                result=evaluator.polynomial(raw)
                need(result==direct[i][j],f'direct:d{d}_component_Gram_{i}{j}')
        kernel=(F(9),F(24336),F(-2704))
        residual=sum((kernel[i]*direct[i][j]*kernel[j] for i in range(3) for j in range(3)),F(0))
        if d==2:
            need(residual==0,'control:d2_one_dimensional_exterior_has_zero_skew_action')
        else:
            need(residual>0,f'negative:d{d}_arbitrary_cubic_does_not_satisfy_factorization')
        records.append({'dimension':d,'exterior_triples_tested':count,
                        'exact_direct_Gram':direct,'residual_norm_squared':residual,
                        'closed_graphs_independently_evaluated':len(evaluator.cache),
                        'satisfies_physical_trace_inputs':False})
    return records

def fifth_projection_controls():
    """Check the full-versus-primary subtraction independently with block matrices."""
    C=symmetric_cubic(5,515);d=len(C);eye=np.eye(d,dtype=object)
    L=[C[i] for i in range(d)]
    def traceword(mats):
        X=np.eye(len(mats[0]),dtype=object)
        for A in mats:X=X@A
        return np.trace(X)
    def features(labels,multiplication,metric_vectors):
        # Every vector space here is positive with an explicit invariant product.
        def product(a,b):return multiplication(a)@b
        def H(a,b,c,d,e):return product(a,b)@product(c,product(d,e))
        T=[F(0),F(0),F(0)];Ma=F(0);Mn=F(0)
        vectors=[metric_vectors[i] for i in labels]
        for k in range(5):
            a,b,c,dd,e=vectors[k:]+vectors[:k]
            T[0]+=H(a,b,c,dd,e);T[1]+=H(a,dd,c,b,e);T[2]+=H(a,e,c,b,dd)
            Ma+=(a@b)*(c@product(dd,e));Mn+=(a@c)*(b@product(dd,e))
        return T,Ma,Mn
    def primary_matrix(a):return sum((a[i]*L[i] for i in range(d)),np.zeros((d,d),dtype=object))
    primary_vectors=[eye[:,i] for i in range(d)]
    tuples=[tuple(range(5)),(0,0,1,2,4),(4,3,2,3,1),(1,1,1,1,2)]
    for s in (F(1),F(1,2),F(1,3)):
        gamma=s*s
        R=[]
        for i in range(d):
            A=np.zeros((d+1,d+1),dtype=object);A[0,i+1]=s;A[i+1,0]=s;A[1:,1:]=L[i]
            R.append(keep_size(A))
        Rt=s*np.eye(d+1,dtype=object)
        def full_matrix(a):return a[0]*Rt+sum((a[i+1]*R[i] for i in range(d)),np.zeros((d+1,d+1),dtype=object))
        fv=[np.concatenate((np.asarray([0],dtype=object),e)) for e in primary_vectors]
        for idx,labels in enumerate(tuples):
            T,Ma,Mn=features(labels,primary_matrix,primary_vectors)
            U,fa,fn=features(labels,full_matrix,fv)
            need(U==[T[0]+2*gamma*Ma,T[1]+2*gamma*Mn,T[2]+gamma*(Ma+Mn)],
                 f'projection:s{s}_tree_scalar_terms_{idx}')
            difference=traceword([R[i] for i in labels])-traceword([L[i] for i in labels])
            need(difference==gamma*T[0]+gamma*gamma*Ma,f'projection:s{s}_cyclic_block_trace_{idx}')
            full=30*U[0]+4*U[1]-22*U[2]+8*fa+8*fn
            projected=(30-gamma)*T[0]+4*T[1]-22*T[2]+(8+38*gamma-gamma*gamma)*Ma+(8-14*gamma)*Mn
            need(full-projected==difference,f'projection:s{s}_all_primary_fifth_coefficients_{idx}')
    need((30-F(1,3),8+38*F(1,3)-F(1,9),8-14*F(1,3))==(F(89,3),F(185,9),F(10,3)),
         'projection:physical_fifth_coefficients')
    # The entire tree-and-metric RHS has zero total alternating part. This test
    # has five independent external basis labels, not an automatic d<5 zero.
    alt=F(0)
    for labels in permutations(range(5)):
        T,Ma,Mn=features(labels,primary_matrix,primary_vectors)
        alt+=g.sgn(labels)*(F(89,3)*T[0]+4*T[1]-22*T[2]+F(185,9)*Ma+F(10,3)*Mn)
    need(alt==0,'fifth:all120_permutations_cancel_non_alternating_RHS')
    return {'block_matrix_dimension':6,'scalar_couplings_tested':['1','1/2','1/3'],
            'tuple_count_per_coupling':len(tuples),'alternation_terms':120,
            'tested_fifth_trace_identity_on_unknown_physical_cubic':False}

def certificate_checks(c):
    expected=[[17069,221,17290],[221,349,570],[17290,570,17860]]
    need(c['small_gram']==expected,'certificate:exact_small_Gram')
    need(c['relation_determinant']==F(11,18),'certificate:three_scalar_relations_nonsingular')
    expected_values=[-F(78155392232087354080,81),F(370415245037399715987080,243),-F(833649013146827440152746,243)]
    for i,(graph,want) in enumerate(zip(g.SCALAR_GRAPHS[1:],expected_values)):
        need(c['values'][graph]==want,f'certificate:closed_invariant_{i}')
        need(sum((a*c['values'][h] for h,a in c['relations'][i].items()),F(0))==0,
             f'certificate:scalar_relation_{i}_substituted')
    need(c['common_factor']>0,'certificate:positive_Gram_scale')
    K=c['small_gram'];z=[1,1,-1]
    need([sum(a*b for a,b in zip(row,z)) for row in K]==[0,0,0],'certificate:zero_residual_vector')
    need(K[0][0]*K[1][1]-K[0][1]**2==5908240,'certificate:positive_two_by_two_minor')
    need(K[2]==[a+b for a,b in zip(K[0],K[1])],'certificate:third_tensor_equals_sum_in_positive_space')
    need((F(2704,9)*9,9*2704)==(2704,24336),'normalization:restore_original_operator_coefficients')
    coeff=(F(9),F(24336),F(-2704));M=c['unscaled_gram']
    need(sum(coeff[i]*M[i][j]*coeff[j] for i in range(3) for j in range(3))==0,
         'certificate:unscaled_operator_residual_norm_zero')
    # The short-cycle identities alone leave unreduced invariants: no claim
    # that merely stopping a rewrite proves independence from those identities.
    residual=defaultdict(F)
    for i in range(3):
        for j in range(3):
            for h,a in c['reduced_gram'][i][j].items():residual[h]+=coeff[i]*coeff[j]*a
    residual={h:a for h,a in residual.items() if a}
    need(len(residual)==4,'scope:three_unresolved_invariants_before_fifth_relations')
    need(sum(a*c['values'][h] for h,a in residual.items())==0,'certificate:all_four_remaining_terms_cancel')
    need(max(n for n,edges in g.REDUCTION_DAG)<=16,'scope:no_graph_above_sixteen_cubic_vertices')
    for n in (2,3,4):
        need(g.REDUCTION_COUNTS[n]>0,f'certificate:trace_order_{n}_used')
    return residual

def serialized_certificate(c,residual):
    dag=[{'input':g.encode_graph(graph),'cycle':list(cycle),'replacement':g.encode_poly(step)}
         for graph,(cycle,step) in sorted(g.REDUCTION_DAG.items())]
    return {'source_constants':{'d':g.D,'kappa':str(g.KAPPA),'nu':str(g.NU),
                                'fourth':[str(x) for x in (g.ALPHA,g.BETA,g.U,g.V)],
                                'projected_non_alternating_fifth':['89/3','4','-22','185/9','10/3']},
            'component_order':['Q_x','ad_x','ad_Gx'],
            'six_index_components':[g.encode_poly(p) for p in c['components']],
            'rescaling':[str(x) for x in c['rescaling']],
            'raw_Gram_polynomials':[[g.encode_poly(p) for p in row] for row in c['raw_gram']],
            'short_cycle_Gram_reductions':[[g.encode_poly(p) for p in row] for row in c['reduced_gram']],
            'scalar_graphs':[g.encode_graph(h) for h in g.SCALAR_GRAPHS],
            'pentagon':list(g.PENTAGON),
            'three_fifth_relations':[g.encode_poly(row) for row in c['relations']],
            'scalar_relation_matrix':c['relation_matrix'],'scalar_relation_rhs':c['relation_rhs'],
            'scalar_relation_determinant':c['relation_determinant'],
            'scalar_graph_values':[str(c['values'][h]) for h in g.SCALAR_GRAPHS],
            'unscaled_Gram':c['unscaled_gram'],'positive_common_scale':c['common_factor'],
            'small_Gram':c['small_gram'],'kernel_vector':[1,1,-1],
            'original_residual_coefficients':[9,24336,-2704],
            'residual_before_fifth':g.encode_poly(residual),
            'all_short_cycle_steps':dag}

def strings(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):strings(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [strings(v) for v in o]
    if isinstance(o,np.integer):return int(o)
    return o

def main():
    certificate=g.build_certificate()
    residual=certificate_checks(certificate)
    graph=graph_controls(certificate)
    projection=fifth_projection_controls()
    report={'status':'PASS: exact positive-norm implication certificate and scoped controls',
            'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,
            'certificate':serialized_certificate(certificate,residual),
            'direct_small_cubic_controls':graph,'fifth_normalization_controls':projection,
            'largest_explicit_matrix_dimension':LARGEST_MATRIX_DIMENSION,
            'largest_numeric_tensor_entries':LARGEST_ARRAY_ENTRIES,
            'largest_symbolic_graph_vertices':max(h[0] for row in certificate['raw_gram'] for poly in row for h in poly),
            'short_cycle_reduction_steps':len(g.REDUCTION_DAG),
            'arithmetic':'integers and fractions; no floating tolerances',
            'full_Monster_tensor_constructed':False,'Monster_character_data_used':False,
            'six_label_operator_condition_independent':'NO: implied by stated traces and positive metric',
            'uses_disputed_alternating_five_form_coefficient':False,
            'real_positive_metric_required_for_zero_norm_implication':True,
            'source_theorems_formally_verified':False,'independent_expert_review':False,
            'full_physical_selection_or_novelty_claim':False}
    print(json.dumps(strings(report),indent=2,sort_keys=True))

if __name__=='__main__':main()
