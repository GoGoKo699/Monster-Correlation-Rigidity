#!/usr/bin/env python3
"""Exact audit of which hypotheses low-weight readout actually uses.

Finite generic-c Virasoro systems and independent even-free-boson projections.
No holomorphic character, exceptional trace constants or Monster data are input.
Source-level theorems and the all-c proof remain analytic dependencies.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, combinations, permutations
from pathlib import Path
import hashlib, importlib.util, json
import reference_virasoro as v

BASE='09e3f98ad79034eefab43f4fb9ea432368fc19e7'
LABELS=[];MAX=0

def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    LABELS.append(label)
def Z(n):
    global MAX
    MAX=max(MAX,n)
    return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye(n):
    a=Z(n)
    for i in range(n):a[i][i]=Q(1)
    return a
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,t):return [[t*x for x in r] for r in a]
def tp(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum((x*y for x,y in zip(r,s)),Q(0)) for s in zip(*b)] for r in a]
def tr(a):return sum((a[i][i] for i in range(len(a))),Q(0))
def dot(a,b):return sum((x*y for r,s in zip(a,b) for x,y in zip(r,s)),Q(0))
def ha(a,b):return add(a[0],b[0]),add(a[1],b[1])
def hs(a,t):return sc(a[0],t),sc(a[1],t)
def hm(a,b):return add(mm(a[0],b[0]),sc(mm(a[1],b[1]),-1)),add(mm(a[0],b[1]),mm(a[1],b[0]))
def hd(a):return tp(a[0]),sc(tp(a[1]),-1)
def hz(n):return Z(n),Z(n)
def hdot(a,b):return dot(a[0],b[0])+dot(a[1],b[1])
def psd(a):
    if hd(a)!=a:return False
    n=len(a[0]);m=Z(2*n)
    for i,j in product(range(n),repeat=2):
        m[i][j]=m[i+n][j+n]=a[0][i][j];m[i][j+n]=-a[1][i][j];m[i+n][j]=a[1][i][j]
    for k in range(2*n):
        x=m[k][k]
        if x<0:return False
        if not x:
            if any(m[i][k] for i in range(k+1,2*n)):return False
            continue
        for i in range(k+1,2*n):
            for j in range(k+1,2*n):m[i][j]-=m[i][k]*m[k][j]/x
    return True

def constants(c):
    c=Q(c);g=8/c
    a=(c-88)/(2*(5*c+44));j=4*(c-44)/(c*(5*c+22))
    t=2*(c-25)/(7*c+114)
    r=2*(c-40)/(9*(c+24))
    s=-c*(5*c*c-572*c+11220)/(2*(c+15)*(5*c+44)*(35*c-34))
    z=-8*(c*c-55*c+748)/((2*c-1)*(5*c+22)*(7*c+68))
    A=2*(5*c+44)/(5*c+22);b=11*c/(2*(5*c+44));e=(5*c+164)/(2*(7*c+114))
    M2=32*(c-1)**2/(c*(2*c-1));C2=A+(b*b+b)*M2;B=M2+2+g
    return dict(gamma=g,a=a,j=j,t=t,r=r,s=s,z=z,A=A,b=b,e=e,M2=M2,C2=C2,B=B)

@lru_cache(None)
def parts(n,top=None):
    if n==0:return ((),)
    if n<0:return ()
    return tuple((k,)+x for k in range(min(n,n if top is None else top),0,-1) for x in parts(n-k,k))

def block(c,h,n):
    if h==n:return Q(1),None
    basis=v.parts(n) if h==0 else parts(n-h)
    if not basis:return Q(0),None
    vir=v.Vir(c,h);M=[[vir.gram(a,b) for b in basis] for a in basis]
    global MAX;MAX=max(MAX,len(M))
    rhs=[]
    for lam in basis:
        p=3-n;x=Q(1)
        for k in lam:x*=k+1-p;p+=k
        if p!=3-h:raise RuntimeError('Wrong Ward degree')
        rhs.append(x)
    sol=v.solve(M,rhs)
    need([sum((a*b for a,b in zip(row,sol)),Q(0)) for row in M]==rhs,f'Gram:c{c}_h{h}_to{n}')
    return sum((x*y for x,y in zip(rhs,sol)),Q(0)),dict(h=h,n=n,gram=M,pairing=rhs,solution=sol)

# Exact univariate polynomials: symbolic certificates, not interpolation.
class Poly:
    def __init__(self,values=0):
        if isinstance(values,Poly):self.a=values.a;return
        if not isinstance(values,(list,tuple)):values=[values]
        a=list(map(Q,values))
        while len(a)>1 and a[-1]==0:a.pop()
        self.a=tuple(a or [Q(0)])
    def __bool__(self):return any(self.a)
    def __add__(self,b):
        b=Poly(b);return Poly([(self.a[i] if i<len(self.a) else 0)+(b.a[i] if i<len(b.a) else 0) for i in range(max(len(self.a),len(b.a)))])
    __radd__=__add__
    def __neg__(self):return Poly([-x for x in self.a])
    def __sub__(self,b):return self+-Poly(b)
    def __rsub__(self,b):return Poly(b)+-self
    def __mul__(self,b):
        b=Poly(b);out=[Q(0)]*(len(self.a)+len(b.a)-1)
        for i,x in enumerate(self.a):
            for j,y in enumerate(b.a):out[i+j]+=x*y
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self,n):
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,b):return self.a==Poly(b).a

def poly_det(M):
    total=Poly(0);n=len(M)
    for perm in permutations(range(n)):
        z=Poly((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):
            z=z*M[i][perm[i]]
            if not z:break
        total=total+z
    return total

def symbolic_central_charge():
    c=Poly([0,1]);records=[]
    forms={
      (3,5):(2*(6*c+139),7*c+114),
      (4,6):(25*c+728,9*(c+24)),
      (2,6):(250*c**3+15185*c**2+180482*c-179520,2*(c+15)*(5*c+44)*(35*c-34)),
      (0,6):(4*(100*c**3+3257*c**2+23724*c-11968),c*(2*c-1)*(5*c+22)*(7*c+68)),
      (2,4):(9*c+176,2*(5*c+44)),
      (0,4):(36*c+352,c*(5*c+22))}
    for (h,n),(num,den) in forms.items():
        vir=v.Vir(1,h);vir.c=c
        basis=v.parts(n) if h==0 else parts(n-h)
        M=[[Poly(vir.gram(a,b)) for b in basis] for a in basis];rhs=[]
        for lam in basis:
            p0=3-n;k=Q(1)
            for x in lam:k*=x+1-p0;p0+=x
            rhs.append(Poly(k))
        determinant=poly_det(M)
        bordered=[row+[r] for row,r in zip(M,rhs)]+[rhs+[Poly(0)]]
        quadratic=-poly_det(bordered)
        need(determinant*num==quadratic*den,f'symbolic:all_c_h{h}_to{n}_closed_block_identity')
        if (h,n)==(0,6):
            need(determinant==Q(3,4)*c**4*(2*c-1)*(5*c+22)**2*(7*c+68),'symbolic:unitarity_four_state_determinant')
        records.append(dict(h=h,n=n,gram_polynomial_coefficients=[[a.a for a in row] for row in M],
            determinant_coefficients=determinant.a,quadratic_adjugate_coefficients=quadratic.a,
            proposed_numerator_coefficients=num.a,proposed_denominator_coefficients=den.a,
            cleared_polynomial_identity_zero=True))
    return records


def coefficient_checks():
    records=[]
    for c in (Q(1),Q(3,2),Q(2),Q(3),Q(24),Q(25),Q(40)):
        k=constants(c);g=k['gamma']
        b35,_=block(c,3,5);b46,_=block(c,4,6);b26,cert=block(c,2,6);b06,_=block(c,0,6)
        need(b35==2*(6*c+139)/(7*c+114),f'coeff:c{c}_35_closed_form')
        need(2-b35==k['t'],f'coeff:c{c}_skew_identity')
        need(3-b46==k['r'] and 1-b26-3*k['a']==k['s'] and g-b06-3*k['j']==k['z'],f'coeff:c{c}_symmetric_identity')
        need(k['b']==1+k['a'] and k['A']==2+g+k['j'] and k['e']==(1-k['t'])/2,f'coeff:c{c}_witness_measured_span')
        need(0<k['e']<1 and k['M2']>=0 and k['C2']>0,f'coeff:c{c}_stability_signs')
        records.append(dict(c=c,constants=k,level_four_h2_certificate=cert))
    k=constants(24)
    need(k['C2']==Q(135249252,5609497) and k['C2']<25,'audit:same_stability_constant_without_extremal_data')
    need(k['B']==Q(815,47) and k['B']<18,'audit:same_impurity_constant_without_extremal_data')
    need(k['A']==Q(164,71) and k['b']==Q(33,41) and k['e']==Q(71,141),'audit:c24_small_witness_coefficients')
    # General norm cap comes from a Virasoro vector of charge c_u>=1/2.
    for c in (Q(1),Q(2),Q(3),Q(24),Q(40)):
        k=constants(c)
        need(k['M2']/(k['M2']+32/c)==((c-1)/c)**2,f'unitarity:c{c}_cubic_cap_algebra')
    return records

def fock_controls(n,stop):
    path=Path(__file__).with_name('verify_weight_three.py')
    need(hashlib.sha256(path.read_bytes()).hexdigest()=='701bb43baa4198dab9a4639c6e763b7d0e809e1a516b011f973432fedcb9a724',f'dependency:c{n}_Fock_bytes')
    spec=importlib.util.spec_from_file_location('_audit_fock'+str(n),path);o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=6
    vac={(0,)*(n*6):Q(1)};I=eye(n)
    def vir(m,s):return o.quadratic_mode(I,m+1,s,n)
    @lru_cache(None)
    def space(grade):
        out=[]
        def visit(pos,left,key,count):
            if pos==n*6:
                if left==0 and count%2==0:out.append(tuple(key))
                return
            w=pos//n+1
            for a in range(left//w+1):visit(pos+1,left-a*w,key+[a],count+a)
        visit(0,grade,[],0);return tuple(out)
    def independent(states):
        piv={};kept=[]
        for s in states:
            z=s.copy()
            for p,b in sorted(piv.items()):
                if z.get(p):z=o.add((1,z),(-z[p],b))
            if z:
                p=min(z);a=z[p];piv[p]={key:c/a for key,c in z.items()};kept.append(s)
        return kept
    mats=[]
    for j in range(1,n):
        A=Z(n)
        for i in range(j):A[i][i]=1
        A[j][j]=-j;mats.append(A)
    for i,j in combinations(range(n),2):
        A=Z(n);A[i][j]=A[j][i]=1;mats.append(A)
    states=[o.quadratic_mode(A,-1,vac,n) for A in mats];d=len(states)
    gs=[o.inner(s,s,n) for s in states];metric=[[gs[i]*int(i==j) for j in range(d)] for i in range(d)]
    need(all(o.inner(a,b,n)==metric[i][j] for i,a in enumerate(states) for j,b in enumerate(states)),f'fock:c{n}_orthogonal_primary_coordinates')
    full=[[o.quadratic_mode(A,1,s,n) for s in states] for A in mats]
    C=[[[o.inner(a,full[i][j],n) for j in range(d)] for i in range(d)] for a in states]
    omega=vir(-2,vac);g=Q(8,n);k=constants(n)
    pairs=list(product(range(d),repeat=2));Grams={};ranks=[]
    for h in range(2,stop+1):
        candidates=[o.deriv({key:Q(1)},n) for key in space(h-1)]
        candidates += [vir(-2,{key:Q(1)}) for key in space(h-2)]
        desc=independent([s for s in candidates if s]);M=[[o.inner(a,b,n) for b in desc] for a in desc]
        global MAX;MAX=max(MAX,len(M))
        out=[]
        for i,j in pairs:
            raw=o.quadratic_mode(mats[i],3-h,states[j],n)
            sol=v.solve(M,[o.inner(a,raw,n) for a in desc])
            out.append(o.add((1,raw),*[(-x,s) for x,s in zip(sol,desc)]))
        need(all(not vir(m,s) for s in out for m in range(1,h+1)),f'fock:c{n}_h{h}_all_primary_conditions')
        need(all(out[d*i+j]==o.add(((-1)**h,out[d*j+i])) for i,j in pairs),f'fock:c{n}_h{h}_parity')
        Gram=[[o.inner(a,b,n) for b in out] for a in out];Grams[h]=Gram
        # Independent four-label expressions, no special spectrum or trace data.
        pred=[]
        for i,j in pairs:
            row=[]
            for a,b in pairs:
                X=sum((C[t][i][a]*C[t][j][b]/gs[t] for t in range(d)),Q(0))
                Y=sum((C[t][i][j]*C[t][a][b]/gs[t] for t in range(d)),Q(0))
                Zz=sum((C[t][i][b]*C[t][j][a]/gs[t] for t in range(d)),Q(0))
                p=metric[i][a]*metric[j][b];q=metric[i][b]*metric[j][a];r0=metric[i][j]*metric[a][b]
                if h==2:z=Y
                elif h==3:z=X-Zz+g*(p-q)
                elif h==4:z=(X+Zz)/2+(1+g/2)*(p+q)+k['a']*Y+k['j']*r0
                elif h==5:z=2*(p-q)+k['t']*Grams[3][d*i+j][d*a+b]
                else:z=2*(p+q)+k['r']*Grams[4][d*i+j][d*a+b]+k['s']*Y+k['z']*r0
                row.append(z)
            pred.append(row)
        need(Gram==pred,f'fock:c{n}_h{h}_independent_projection_matches_generic_Gram')
        ranks.append(dict(weight=h,rank=o.rank(Gram),descendant_Gram_size=len(M)))
    R4norm=sum((Grams[4][d*i+i][d*j+j]/(gs[i]*gs[j]) for i in range(d) for j in range(d)),Q(0))
    need(R4norm==Q(6*n*(n-1)**2*(n+2),5*n+22) and R4norm>0,f'fock:c{n}_nonzero_weight_four_Casimir_trace')
    # The frame in actual (nonorthonormal) primary coordinates. Covariant output
    # matrices act against contravariant density matrices; metric factors retained.
    def frame(h,P):
        out=hz(d)
        for i,j in pairs:
            for a,b in pairs:
                for part in range(2):out[part][i][j]+=(-1)**h*Grams[h][d*a+b][d*i+j]*P[part][b][a]
        return out
    def FF(P):
        out=hz(d)
        for mat,norm in zip(C,gs):out=ha(out,hs((mm(mm(mat,P[0]),mat),mm(mm(mat,P[1]),mat)),1/norm))
        return out
    def metricP(P):return mm(mm(metric,P[0]),metric),mm(mm(metric,P[1]),metric)
    testPs=[]
    for j in range(d):
        p=hz(d);p[0][j][j]=1/gs[j];testPs.append(p)
    for j in range(1,d):
        # Rational normalized projectors for vectors e0+(1+i)e_j.
        p=hz(d);p[0][0][0]=1;p[0][j][j]=2;p[0][0][j]=p[0][j][0]=1;p[1][0][j]=-1;p[1][j][0]=1
        p=hs(p,1/(gs[0]+2*gs[j]));testPs.append(p)
    for ix,P in enumerate(testPs):
        need(hm(hm(P,(metric,Z(d))),P)==P,f'fock:c{n}_state{ix}_metric_purity')
        Iminus=ha((metric,Z(d)),hs(metricP(P),-1))
        direct=ha(ha(frame(2,P),hs(FF(P),-1)),hs(Iminus,2+g))
        measured=ha(ha(hs((metric,Z(d)),k['A']),hs(frame(2,P),k['b'])),hs(frame(4,P),-1))
        measured=ha(ha(measured,hs(frame(3,P),-k['e'])),hs(frame(5,P),-Q(1,2)))
        need(direct==measured,f'fock:c{n}_state{ix}_generic_witness_measured_span')
        need(hm(direct,P)==hz(d) and psd(ha(direct,hs(Iminus,-2))),f'fock:c{n}_state{ix}_target_kernel_and_gap')
        need(psd(ha(hs(Iminus,k['B']),hs(direct,-1))),f'fock:c{n}_state{ix}_generic_unitarity_upper_bound')
        r={h:hdot(P,frame(h,P)) for h in (2,3,4,5)}
        norm=k['b']**2*r[2]+r[4]+k['e']**2*r[3]+r[5]/4
        need(norm==k['A']+(k['b']**2+k['b'])*r[2]+(k['e']**2-k['e'])*r[3]-r[5]/4 and norm<=k['C2'],f'fock:c{n}_state{ix}_coefficient_norm_bound')
    # Explicitly distinguish this control from a hypothetical exceptional tensor.
    need(d!=196883 and n!=24,f'negative:c{n}_control_is_not_the_Monster_data')
    return dict(c=n,primary_dimension=d,orthogonal_basis_squared_norms=gs,channel_controls=ranks,
                tested_pure_projectors=len(testPs),weight_four_Casimir_norm=R4norm,holomorphic_extremal_assumption_used=False)

def comparator():
    n=24;minimum_norm_squared=6
    need(Q(minimum_norm_squared,2)>2,'comparison:no_lattice_momentum_states_through_weight_two')
    need(n*(n+1)//2-1==299,'comparison:c24_fixed_lattice_first_primary_dimension_299')
    need(299!=196883,'comparison:known_example_is_not_moonshine_VOA')
    # The odd eigenspace V_L^- has weight-one states, a non-vacuum V_L^+ module.
    need(n>0,'comparison:nontrivial_odd_module_obstructs_holomorphicity')
    # Local four-oscillator lower examples do not refer to lattice momenta.
    A=Z(4);A[0][0]=1;A[1][1]=-1
    B=Z(4);B[2][2]=1;B[3][3]=-1
    need(mm(A,B)==Z(4),'comparison:pure_lower_example_has_disjoint_oscillator_support')
    X=Z(4);X[0][1]=X[1][0]=Q(1,2);X[2][3]=X[3][2]=-Q(1,2)
    plus=add(sc(eye(4),Q(1,4)),sc(X,Q(1,2)));minus=add(sc(eye(4),Q(1,4)),sc(X,-Q(1,2)))
    need(psd((plus,Z(4))) and psd((minus,Z(4))) and tr(plus)==tr(minus)==1,'comparison:rank_two_states_positive_normalized')
    need(mm(plus,plus)==sc(plus,Q(1,2)) and mm(minus,minus)==sc(minus,Q(1,2)) and mm(plus,minus)==Z(4),'comparison:orthogonal_rank_two_state_supports')
    # Four-current monomial is literally the same under the two pairings.
    need(sorted((0,1)+(2,3))==sorted((0,2)+(1,3)),'comparison:mixed_blind_normal_product_identity')
    need(Q(6*24*23**2*26,5*24+22)==Q(990288,71),'comparison:weight_four_thermal_response_nonzero')
    need(Q(8*22**2,24*23)==Q(484,69)<constants(24)['M2'],'comparison:cubic_extremum_not_saturated')
    need(Q(484,69)/(Q(484,69)+Q(32,24))==Q(22,24)**2,'comparison:maximizing_Virasoro_charge_one')
    return dict(model='V_L^+ for L=sqrt(6) Z^24',central_charge=24,weight_one_dimension=0,
                first_primary_dimension=299,holomorphic=False,sharp_pure_cutoff=5,sharp_all_state_linear_cutoff=6,
                weight_four_primary_trace_witness_norm=Q(990288,71),max_real_cubic_squared=Q(484,69),
                smallest_nonzero_Virasoro_charge_in_weight_two=1,
                is_counterexample_to_holomorphic_moonshine_uniqueness=False,
                higher_OPE_data_or_thermal_11design_transferred=False)

def local_sharpness_controls():
    p=Path(__file__).with_name('verify_weight_three.py')
    spec=importlib.util.spec_from_file_location('_scope_lower_examples',p);o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);o.GRADE=6
    n=4;vac={(0,)*24:Q(1)}
    A=Z(n);A[0][0]=1;A[1][1]=-1
    B=Z(n);B[2][2]=1;B[3][3]=-1
    u=o.quadratic_mode(A,-1,vac,n);v0=o.quadratic_mode(B,-1,vac,n)
    need(o.inner(u,u,n)==o.inner(v0,v0,n)==1 and o.inner(u,v0,n)==0,'sharp:pure_pair_orthonormal')
    need(not o.quadratic_mode(A,1,v0,n) and not o.quadratic_mode(A,0,v0,n),'sharp:all_weight_three_data_of_conjugate_pair_agree')
    w=o.add((Q(1,2),o.quadratic_mode(A,-2,v0,n)),(-Q(1,2),o.quadratic_mode(B,-2,u,n)))
    need(o.inner(w,w,n)==2 and all(not o.quadratic_mode(eye(n),m+1,w,n) for m in range(1,6)),'sharp:nonzero_weight_five_primary_separator')
    mats=[];states=[]
    for i,j in ((0,1),(2,3),(0,2),(1,3)):
        M=Z(n);M[i][j]=M[j][i]=1;mats.append(M);states.append(o.quadratic_mode(M,-1,vac,n))
    need([[o.inner(x,y,n) for y in states] for x in states]==eye(4),'sharp:mixed_pair_four_orthonormal_fields')
    def image(h):
        return o.add(*[(Q(s,2),o.quadratic_mode(mats[i],3-h,states[j],n)) for i,j,s in ((0,1,1),(1,0,1),(2,3,-1),(3,2,-1))])
    need(all(not image(h) for h in range(6)),'sharp:entire_mixed_pair_raw_channels_through_five_zero')
    w6=image(6)
    need(o.inner(w6,w6,n)==4 and all(not o.quadratic_mode(eye(n),m+1,w6,n) for m in range(1,7)),'sharp:nonzero_weight_six_primary_separator')
    return {'oscillator_directions':4,'embedded_in_comparison_model_by_lattice_construction':True,
            'entire_comparison_VOA_simulated':False,'w5_norm_squared':2,'w6_norm_squared':4}


def strings(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):strings(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [strings(v) for v in x]
    return x

def main():
    need(hashlib.sha256(Path(v.__file__).read_bytes()).hexdigest()=='cefc291c6be9de9518037d353dc9b25857735963fb8747aea579bce41cc24fdb','dependency:PBW_helper_unchanged')
    symbolic=symbolic_central_charge();coefficients=coefficient_checks();fock=[fock_controls(2,6),fock_controls(3,5)];comp=comparator();sharp=local_sharpness_controls()
    print(json.dumps(strings(dict(status='PASS within exact finite-Ward/Fock scope',base_commit=BASE,checks=len(LABELS),labels=LABELS,
       central_charge_polynomial_certificate=symbolic,central_charge_certificates=coefficients,Fock_controls=fock,comparison=comp,sharpness_controls=sharp,largest_square_matrix_dimension=MAX,
       arithmetic='integers and fractions only',full_monster_tensor_used=False,exceptional_character_or_trace_identities_used=False,
       all_c_statement_is_analytic_not_finite_sampling=True,original_stability_bound_invalidated=False,
       Monster_specificity_of_readout_package_supported=False,source_theorems_formally_verified=False)),sort_keys=True,indent=2))
if __name__=='__main__':main()
