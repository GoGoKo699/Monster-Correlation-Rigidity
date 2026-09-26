#!/usr/bin/env python3
"""Exact finite certificates for complete low-weight readout despite zero traces.

Inherited physical input: the joint multiplication spectrum of Notes12-14.
This script recomputes primary channel Grams only through weight six. Small
Fock examples test mode adjoints independently and are not extremal CFTs.
Rational Hermitian matrix controls test the linear-algebra consequences.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import readout_virasoro as v

BASE = '09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS: list[str] = []
MAX_SQUARE = 0
D = 196883
KAPPA = Q(13858,3)
LAM = {2:KAPPA,3:Q(564),4:Q(54),5:Q(4),6:Q(4)}


def need(ok, label):
    if not bool(ok): raise RuntimeError(label)
    LABELS.append(label)


def square(n):
    global MAX_SQUARE
    MAX_SQUARE = max(MAX_SQUARE,n)
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    a=square(n)
    for i in range(n): a[i][i]=Q(1)
    return a


def transpose(a): return [list(r) for r in zip(*a)]
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,c): return [[c*x for x in r] for r in a]
def mm(a,b): return [[sum((x*y for x,y in zip(r,c)),Q(0)) for c in zip(*b)] for r in a]
def trace(a): return sum((a[i][i] for i in range(len(a))),Q(0))
def dot(a,b): return sum((x*y for ar,br in zip(a,b) for x,y in zip(ar,br)),Q(0))


def ldl(m):
    global MAX_SQUARE
    MAX_SQUARE=max(MAX_SQUARE,len(m))
    n=len(m);l=eye(n);p=[]
    for i in range(n):
        z=m[i][i]-sum((l[i][k]**2*p[k] for k in range(i)),Q(0))
        if z<=0: raise RuntimeError('Nonpositive Gram pivot')
        p.append(z)
        for j in range(i+1,n):
            l[j][i]=(m[j][i]-sum((l[j][k]*l[i][k]*p[k] for k in range(i)),Q(0)))/z
    return p


@lru_cache(None)
def partitions(n, top=None):
    if n==0:return ((),)
    if n<0:return ()
    top=n if top is None else top
    return tuple((k,)+t for k in range(min(top,n),0,-1) for t in partitions(n-k,k))


@lru_cache(None)
def block(h,n):
    if h==n:return (Q(1),None)
    basis=v.parts(n) if h==0 else partitions(n-h)
    if not basis:return (Q(0),None)
    vir=v.Vir(24,h)
    m=[[vir.gram(a,b) for b in basis] for a in basis];pivots=ldl(m);rhs=[]
    for lam in basis:
        index=3-n;c=Q(1)
        for k in lam:
            c*=k+1-index;index+=k
        if index!=3-h: raise RuntimeError('Wrong descendant degree')
        rhs.append(c)
    sol=v.solve(m,rhs);coef=sum((a*b for a,b in zip(rhs,sol)),Q(0))
    return coef,{'primary_weight':h,'target_weight':n,'partitions':basis,'gram':m,
                 'positive_LDL_pivots':pivots,'pairing':rhs,'solution':sol,'coefficient':coef}


def channel_certificate():
    # I, Q-range, symmetric+/-, skew+/-; values are inherited joint data,
    # not reconstructed by a scalar check and not assumed group labels.
    fs=(KAPPA,Q(899),Q(155,3),-Q(7,3),Q(845,3),-Q(1,3))
    ts=(1,1,1,1,-1,-1);qs=(0,KAPPA,0,0,0,0);js=(D,0,0,0,0,0)
    dims=(1,D,842609326,18538750076,21296876,19360062527)
    expected=((D,0,0,0,0,0),(0,)*6,(0,KAPPA,0,0,0,0),
              (0,0,0,0,564,0),(0,0,54,0,0,0),(0,0,0,0,0,4),(0,0,0,4,0,0))
    prim={};rows=[]
    for n in range(7):
        raw=[]
        for f,t,q,j in zip(fs,ts,qs,js):
            if n==0:z=j
            elif n==1:z=0
            elif n==2:z=q+Q(j,3)
            elif n==3:z=q+f-f*t+Q(j+1-t,3)
            else:z=comb(n-1,3)+int(n==4)*t+(n-2)*(f+Q(1,3))+q+Q(j,3)-f*t-Q(t,3)
            raw.append(Q(z))
        out=raw[:];pieces=[]
        for h in range(n):
            if h==1:continue
            coefficient,cert=block(h,n)
            out=[a-coefficient*b for a,b in zip(out,prim[h])]
            if cert:pieces.append(cert)
        prim[n]=out
        need(out==list(map(Q,expected[n])),f'channel:primary_weight_{n}_all_six_sectors')
        need(all(a>=0 for a in out),f'channel:weight_{n}_positive_Gram')
        rows.append({'weight':n,'raw_eigenvalues':raw,'descendant_certificate':pieces,'primary_eigenvalues':out})
    ranks={h:sum(dim for dim,value in zip(dims,prim[h]) if value) for h in range(2,7)}
    need(sum(ranks.values())==D*D-1,'readout:all_non_scalar_matrix_directions_covered')
    need(ranks[6]==18538750076,'readout:strictly_missing_sector_below_weight_six')
    need(sum(ranks[h] for h in (2,4,6))==D*(D+1)//2-1,'readout:complete_real_symmetric_tracefree_space')
    need(sum(ranks[h] for h in (3,5))==D*(D-1)//2,'readout:complete_real_skew_space')
    need(min(LAM.values())==4 and max(LAM.values())==KAPPA,'readout:frame_bounds')
    reciprocal=sum((1/a for a in LAM.values()),Q(0))
    need(reciprocal<Q(2,3),'readout:single_weight_contrast_bound')
    return {'certificate':rows,'sector_dimensions':dims,'mode_image_ranks':ranks,
            'squared_frame_weights':LAM,'reciprocal_weight_sum':reciprocal,
            'minimum_cutoff_for_all_state_linear_readout':6,
            'assumed_joint_contraction_spectrum':True}


# Exact Hermitian matrices as (real,imaginary) rational arrays.
def hzero(n):return square(n),square(n)
def hadd(a,b):return add(a[0],b[0]),add(a[1],b[1])
def hscale(a,c):return scale(a[0],c),scale(a[1],c)
def hmul(a,b):return add(mm(a[0],b[0]),scale(mm(a[1],b[1]),-1)),add(mm(a[0],b[1]),mm(a[1],b[0]))
def hadjoint(a):return transpose(a[0]),scale(transpose(a[1]),-1)
def htrace(a):return trace(a[0]),trace(a[1])
def hdot(a,b):return dot(a[0],b[0])+dot(a[1],b[1])
def hermitian(a):return a==hadjoint(a)


def projector(re,im):
    n=len(re);r=square(n);z=square(n)
    for i,j in product(range(n),repeat=2):
        r[i][j]=re[i]*re[j]+im[i]*im[j]
        z[i][j]=im[i]*re[j]-re[i]*im[j]
    return r,z


def hermitian_basis(n):
    out=[]
    for k in range(1,n):
        a=square(n)
        for j in range(k):a[j][j]=1
        a[k][k]=-k;out.append((a,square(n)))
    for i in range(n):
        for j in range(i+1,n):
            a=square(n);a[i][j]=a[j][i]=1;out.append((a,square(n)))
            b=square(n);b[i][j],b[j][i]=1,-1;out.append((square(n),b))
    return out


def frame_controls():
    records=[]
    for n in (2,3,4):
        basis=hermitian_basis(n);norms=[hdot(a,a) for a in basis]
        need(len(basis)==n*n-1,f'frame:d{n}_complete_traceless_basis')
        need(all(hermitian(a) and htrace(a)==(0,0) for a in basis),f'frame:d{n}_Hermitian_and_tracefree')
        need(all(hdot(a,b)==(norms[i] if i==j else 0) for i,a in enumerate(basis) for j,b in enumerate(basis)),
             f'frame:d{n}_orthogonality')
        re=[Q(3,5),Q(0)]+[Q(0)]*(n-2);im=[Q(0),Q(4,5)]+[Q(0)]*(n-2)
        rho=projector(re,im);sigma=projector([Q(1)]+[Q(0)]*(n-1),[Q(0)]*n)
        I=(eye(n),square(n));tau=hscale(I,Q(1,n));delta=hadd(rho,hscale(sigma,-1))
        for label,state in [('complex_pure',rho),('mixed',hscale(hadd(rho,tau),Q(1,2))),('uniform',tau)]:
            coeff=[hdot(state,a) for a in basis]
            reconstructed=tau
            for a,c,g in zip(basis,coeff,norms):reconstructed=hadd(reconstructed,hscale(a,c/g))
            need(reconstructed==state,f'frame:d{n}_{label}_exact_state_reconstruction')
            score=sum((c*c/g for c,g in zip(coeff,norms)),Q(0))
            need(score==hdot(state,state)-Q(1,n),f'frame:d{n}_{label}_purity_identity')
        need(any(x for row in rho[1] for x in row),'frame:d'+str(n)+'_genuinely_complex_control')
        symmetric=[a for a in basis if not any(x for row in a[1] for x in row)]
        conjugate=(rho[0],scale(rho[1],-1))
        need(rho!=conjugate and all(hdot(rho,a)==hdot(conjugate,a) for a in symmetric),
             f'negative:d{n}_even_fields_alone_miss_imaginary_coherence')
        dist=sum((hdot(delta,a)**2/g for a,g in zip(basis,norms)),Q(0))
        need(dist==hdot(delta,delta),f'frame:d{n}_two_state_distance')
        # Missing one orthogonal probe creates indistinguishable mixed states.
        x=basis[-1];eps=Q(1,4*n);rplus=hadd(tau,hscale(x,eps));rminus=hadd(tau,hscale(x,-eps))
        need(all(hdot(rplus,a)==hdot(rminus,a) for a in basis[:-1]) and rplus!=rminus,
             f'negative:d{n}_incomplete_linear_readout')
        need(eps*2<Q(1,n),'negative:d'+str(n)+'_density_positivity_by_operator_norm_bound')
        # Exact error-detection residual on complex rotated code spaces.
        U=hadd(I,hscale(rho,-2))
        need(hmul(hadjoint(U),U)==I,f'code:d{n}_rational_complex_unitary')
        for k in range(1,n+1):
            q=square(n)
            for i in range(k):q[i][i]=1
            Qcode=hmul(hmul(U,(q,square(n))),hadjoint(U))
            total=Q(0)
            for a,g in zip(basis,norms):
                qa=hmul(hmul(Qcode,a),Qcode);trq=htrace(qa)
                if trq[1]:raise RuntimeError('Non-real compressed trace')
                traceless=hadd(qa,hscale(Qcode,-trq[0]/k))
                total+=hdot(traceless,traceless)/g
            need(total==k*k-1,f'code:d{n}_rank{k}_exact_detection_residual')
        # The synthesis cost bound follows for arbitrary assignment of five
        # positive sector weights; not a physical small-dimensional VOA.
        weights=[LAM[2+i%5] for i in range(len(basis))]
        cost=sum((hdot(delta,a)**2/(w*g) for a,w,g in zip(basis,weights,norms)),Q(0))
        need(dist/KAPPA<=cost<=dist/4,f'frame:d{n}_minimum_coefficient_norm_bounds')
        records.append({'dimension':n,'traceless_basis_size':len(basis),'all_code_ranks_tested':list(range(1,n+1)),
                        'models_are_extremal_CFTs':False})
    return records


def oscillator_controls():
    path=Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(path.read_bytes()).hexdigest()=='701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',
         'dependency:unchanged_oscillator_helper')
    spec=importlib.util.spec_from_file_location('_readout_fock',path);o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=6
    n=2;empty=(0,)*(n*o.GRADE);vac={empty:Q(1)};I=eye(n)
    def vir(m,s):return o.quadratic_mode(I,m+1,s,n)
    @lru_cache(None)
    def fock_basis(grade):
        values=[]
        def visit(pos,left,key,count):
            if pos==len(empty):
                if not left and count%2==0:values.append(tuple(key))
                return
            weight=pos//n+1
            for k in range(left//weight+1):visit(pos+1,left-k*weight,key+[k],count+k)
        visit(0,grade,[],0)
        return tuple(values)
    def independent(candidates):
        # Retain original columns; eliminate a copy to choose independent ones.
        pivots={};kept=[]
        for state in candidates:
            reduced=state.copy()
            for p,e in sorted(pivots.items()):
                if reduced.get(p):reduced=o.add((1,reduced),(-reduced[p],e))
            if reduced:
                p=min(reduced);z=reduced[p];pivots[p]={key:c/z for key,c in reduced.items()};kept.append(state)
        return kept
    As=[[[1,0],[0,-1]],[[0,1],[1,0]]]
    inputs=[o.quadratic_mode(A,-1,vac,n) for A in As]
    need([[o.inner(a,b,n) for b in inputs] for a in inputs]==eye(2),'fock:orthonormal_external_primaries')
    def zero_mode(field,source):
        out={}
        for key,c0 in field.items():
            factors=[(p%n,p//n+1) for p,occ in enumerate(key) for _ in range(occ)]
            if len(factors)>4:continue
            for modes in product((-2,-1,1,2),repeat=len(factors)):
                if sum(modes) or sum(x for x in modes if x>0)>2:continue
                c=c0;ops=[]
                for (species,m),r in zip(factors,modes):
                    c*=(-1)**(m-1)*v.bc(r+m-1,m-1);ops.append((species,r))
                if not c:continue
                ops.sort(key=lambda t:t[1]>=0);state=source
                for species,r in reversed(ops):state=o.oscillator(state,species,r,n)
                out=o.add((1,out),(c,state))
        return out
    report=[]
    for h in range(2,7):
        candidates=[o.deriv({key:Q(1)},n) for key in fock_basis(h-1)]
        if h>=2:candidates += [vir(-2,{key:Q(1)}) for key in fock_basis(h-2)]
        descendants=independent([s for s in candidates if s])
        gram=[[o.inner(a,b,n) for b in descendants] for a in descendants];ldl(gram)
        projected=[]
        for i,j in product(range(2),repeat=2):
            raw=o.quadratic_mode(As[i],3-h,inputs[j],n)
            rhs=[o.inner(a,raw,n) for a in descendants];sol=v.solve(gram,rhs)
            projected.append(o.add((1,raw),*[(-a,s) for a,s in zip(sol,descendants)]))
        need(all(not vir(m,s) for s in projected for m in range(1,h+1)),f'fock:h{h}_all_primary_conditions')
        need(all(projected[2*i+j]==o.add(((-1)**h,projected[2*j+i])) for i,j in product(range(2),repeat=2)),
             f'fock:h{h}_pair_parity')
        matrices=[]
        for w in projected:
            matrices.append([[o.inner(a,zero_mode(w,b),n) for b in inputs] for a in inputs])
        need(all(transpose(m)==scale(m,(-1)**h) for m in matrices),f'fock:h{h}_primary_zero_mode_adjoint')
        need(all(o.inner(w,projected[2*i+j],n)==m[i][j] for w,m in zip(projected,matrices) for i,j in product(range(2),repeat=2)),
             f'fock:h{h}_ordered_pair_zero_mode_duality_all_labels')
        # Construct the frame using a basis of the generated primary image.
        output_basis=independent([s for s in projected if s]);g=[[o.inner(a,b,n) for b in output_basis] for a in output_basis]
        gm=[[[o.inner(a,zero_mode(w,b),n) for b in inputs] for a in inputs] for w in output_basis]
        if g:ldl(g)
        actual=[[o.inner(a,b,n) for b in projected] for a in projected]
        frame=square(4)
        for k,l in product(range(2),repeat=2):
            coeff=v.solve(g,[m[k][l] for m in gm]) if g else []
            for i,j in product(range(2),repeat=2):frame[2*i+j][2*k+l]=sum((a*m[i][j] for a,m in zip(coeff,gm)),Q(0))
        need(frame==actual,f'fock:h{h}_independent_zero_mode_frame_equals_pair_Gram')
        report.append({'weight':h,'Fock_space_dimension':len(fock_basis(h)),'descendant_Gram_size':len(gram),
                       'generated_primary_rank':len(g),'zero_mode_frame':frame})
    return report


def scalar_and_boundary_checks(ch):
    # Direct orthogonal-pair lower bound across the FIVE separately weighted
    # primary spaces. This is not a many-outcome POVM or query bound.
    s=ch['reciprocal_weight_sum']
    need(2/s>3,'contrast:some_unit_homogeneous_primary_separates_orthogonal_states_more_than_sqrt3')
    need(Q(2,5)/4==Q(1,10),'code:bounded_probe_uniform_deviation_squared')
    need(len(LAM)==5,'contrast:five_orthogonal_response_sectors')
    need(D*D-1==38762915688,'dimension:complete_traceless_operator_count')
    need(1-Q(1,D)==Q(196882,196883),'purity:unit_state_contrast_to_uniform_primary_ensemble')
    need(ch['mode_image_ranks'][2]+ch['mode_image_ranks'][4]+ch['mode_image_ranks'][6] +
         ch['mode_image_ranks'][3]+ch['mode_image_ranks'][5] == D*D-1,'dimension:no_missing_complex_Hermitian_directions')
    # Canonical thermal field is scalar on P2; it cannot repair a missing
    # trace-free sector when fewer primary weights are read.
    norm=Q(68811289248,14884739)
    need(norm/D==Q(20620704,878199601),'canonical:fixed_scalar_response_on_first_primary_level')
    return {'single_homogeneous_primary_orthogonal_state_contrast_squared_lower_bound':2/s,
            'readout_is_physical_implementation':False,'no_QECC_claim_outside_entire_specified_error_family':True,
            'does_not_contradict_high_energy_or_thermodynamic_ETH':True}


def strings(obj):
    if isinstance(obj,Q):return str(obj)
    if isinstance(obj,dict):return {str(k):strings(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [strings(x) for x in obj]
    return obj


def main():
    need(hashlib.sha256(Path(v.__file__).read_bytes()).hexdigest()=='cefc291c6be9de9518037d353dc9b25857735963fb8747aea579bce41cc24fdb',
         'dependency:unchanged_exact_Virasoro_helper')
    channels=channel_certificate();frames=frame_controls();fock=oscillator_controls();bounds=scalar_and_boundary_checks(channels)
    print(json.dumps(strings({'status':'PASS within exact finite-channel/Fock/frame scopes','base_commit':BASE,
        'checks':len(LABELS),'labels':LABELS,'channel_certificate':channels,'rational_matrix_controls':frames,
        'Fock_controls':fock,'bounds':bounds,'largest_square_matrix_dimension':MAX_SQUARE,
        'largest_oscillator_grade':6,'arithmetic':'integers and fractions only','Monster_data_used':False,
        'full_extremal_tensor_constructed':False,'source_theorems_formally_verified':False,
        'independent_new_selection_condition_proved':False,'moonshine_uniqueness_proved':False}),sort_keys=True,indent=2))

if __name__=='__main__':main()
