#!/usr/bin/env python3
"""Small non-Monster checks of the general normalizer argument.

Uses the four-dimensional standard representation of A5. An odd permutation
normalizes A5 but is not in phase*A5: a negative control showing why identifying
the normalizer with the target group is a separate, essential input.
No matrix here is larger than 60 by 60. NumPy is the sole non-stdlib dependency.
"""
from __future__ import annotations
import itertools
import json
import numpy as np

CHECKS: list[str]=[]

def need(ok: bool, label: str) -> None:
    if not ok: raise RuntimeError('Check failed: '+label)
    CHECKS.append(label)

def compose(p: tuple[int,...],q: tuple[int,...]) -> tuple[int,...]:
    return tuple(p[q[i]] for i in range(len(p)))

def even(p: tuple[int,...]) -> bool:
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0

def distance2(a: np.ndarray,b: np.ndarray) -> float:
    return float(np.linalg.norm(a-b,'fro')**2/a.shape[0])

def main() -> None:
    rng=np.random.default_rng(20260923)
    group=[p for p in itertools.permutations(range(5)) if even(p)]
    index={p:i for i,p in enumerate(group)}; ident=tuple(range(5)); ei=index[ident]
    need(len(group)==60,'A5 enumerated as 60 even permutations')
    multiplication=np.array([[index[compose(g,h)] for h in group] for g in group])
    c=[i for i,p in enumerate(group) if p!=ident and compose(p,p)==ident]
    need(len(c)==15,'Double-transposition class has 15 involutions')
    basis=np.vstack([np.eye(4),-np.ones((1,4))])
    basis=np.linalg.qr(basis)[0]
    reps=np.array([basis.T@np.eye(5)[:,list(p)]@basis for p in group])
    need(np.allclose(basis.T@basis,np.eye(4),atol=1e-12),'Standard-module basis is orthonormal')
    need(np.allclose(np.ones(5)@basis,0,atol=1e-12),'Standard-module basis is traceless')
    need(all(np.allclose(reps[i]@reps[j],reps[multiplication[i,j]],atol=1e-12)
             for i in range(60) for j in range(60)),'All 3600 representation products agree')

    walk=np.zeros((60,60))
    for a in c:
        walk[multiplication[a,:],np.arange(60)]+=1/len(c)
    vals=np.linalg.eigvalsh(walk)
    q=float(np.max(np.abs(vals[:-1])))
    need(abs(vals[-1]-1)<1e-12 and abs(q-1/3)<1e-12,
         'Full-class walk has unique constant mode and nontrivial norm 1/3')
    deleted=walk.copy()
    deleted[multiplication[c[0],:],np.arange(60)]-=1/15
    deleted/=14/15
    qdel=float(np.max(np.abs(np.linalg.eigvalsh(deleted)[:-1])))
    need(qdel<=(q+1/15)/(1-1/15)+1e-12,'Deleting one class element obeys conditioning bound')
    need(float(np.min(np.linalg.matrix_power(deleted,10)))>0,
         'Ten-step deleted-class walk has full support')
    twirl=sum(np.kron(reps[a],reps[a]) for a in c)/len(c)
    tv=np.linalg.eigvalsh(twirl)
    need(abs(tv[-1]-1)<1e-12 and np.max(np.abs(tv[:-1]))<=1/3+1e-12,
         'Conjugation twirl satisfies the same spectral bound')

    # A completely independent tensor/tight-frame contraction check.
    T=np.einsum('ai,aj,ak->ijk',basis,basis,basis)
    frames=basis/np.sqrt(4/5)
    need(np.allclose(frames.T@frames/5,np.eye(4)/4,atol=1e-12),
         'Five simplex vectors form a tight frame')
    gram=np.einsum('aij,bij->ab',T,T); kappa=np.trace(gram)/4
    need(np.allclose(gram,kappa*np.eye(4),atol=1e-12),'Toy cubic contraction is isotropic')
    O=np.linalg.qr(rng.normal(size=(4,4)))[0]
    Tp=np.einsum('ai,bj,ck,ijk->abc',O,O,O,T)
    residuals=[]
    for a in frames:
        La=np.einsum('i,ijk->jk',a,T)
        LOa=np.einsum('i,ijk->jk',O@a,T)
        residuals.append(np.linalg.norm(O@La@O.T-LOa,'fro')**2/4)
    left=float(np.mean(residuals)); right=float(np.linalg.norm(Tp-T)**2/16)
    need(abs(left-right)<1e-12,'Averaged multiplication residual equals tensor residual divided by d^2')

    # Exact-spectrum projector comparison in small matrices, including distant frames.
    levels=np.array([-1,.5,11,46])/np.sqrt(141)
    J0=np.diag([1.,-1.,1.,1.]); A0=np.diag(levels)
    for j in range(12):
        Q=np.linalg.qr(rng.normal(size=(4,4)))[0]
        lhs=np.linalg.norm(Q@J0@Q.T-J0,'fro')**2
        rhs=(752/3)*np.linalg.norm(Q@A0@Q.T-A0,'fro')**2
        need(lhs<=rhs+1e-11,f'Spectral-projector global inequality trial {j+1}')

    odd=(1,0,2,3,4)
    oddR=basis.T@np.eye(5)[:,list(odd)]@basis
    min_phase_distance2=min(2-2*abs(float(np.trace(R.T@oddR)))/4 for R in reps)
    need(min_phase_distance2>0.9,'Odd permutation is outside phase*A5 in this representation')
    oddimages=[]
    for R in reps:
        candidates=[distance2(oddR@R@oddR.T,S) for S in reps]
        oddimages.append(int(np.argmin(candidates)))
    need(max(distance2(oddR@reps[g]@oddR.T,reps[oddimages[g]]) for g in range(60))<1e-20,
         'The outsider odd permutation nevertheless normalizes A5 exactly')

    diagnostics=[]
    for case,X in [('inner',reps[17]),('outer_normalizer',oddR)]:
        A=rng.normal(size=(4,4)); A=(A-A.T)*.003
        perturb=np.linalg.solve(np.eye(4)-A/2,np.eye(4)+A/2)
        O=perturb@X
        phi=[]; allerrors=[]
        for R in reps:
            cs=[distance2(O@R@O.T,S) for S in reps]
            phi.append(int(np.argmin(cs))); allerrors.append(min(cs))
        need(len(set(phi))==60,f'{case}: nearest map is bijective')
        need(all(phi[multiplication[i,j]]==multiplication[phi[i],phi[j]]
                 for i in range(60) for j in range(60)),f'{case}: all 3600 multiplication tests pass')
        average=sum(reps[phi[g]].T@O@reps[g] for g in range(60))/60
        need(np.linalg.norm(average,'fro')>1,f'{case}: averaged intertwiner is nonzero')
        need(all(np.allclose(average@reps[g],reps[phi[g]]@average,atol=1e-11)
                 for g in range(60)),f'{case}: exact intertwining equations hold numerically')
        scalar=float(np.trace(average.T@average)/4)
        need(np.allclose(average.T@average,scalar*np.eye(4),atol=1e-11),
             f'{case}: Schur normalization is scalar')
        R=average/np.sqrt(scalar)
        need(np.allclose(R.T@R,np.eye(4),atol=1e-11),f'{case}: normalized intertwiner is orthogonal')
        z2=float(np.mean([allerrors[a] for a in c]))
        DN2=min(distance2(O,R),distance2(O,-R))
        need(DN2<=z2/(1-q)+1e-11,f'{case}: class Poincare bound controls distance to normalizer')
        diagnostics.append({'case':case,'average_class_error_squared':f'{z2:.10f}',
                            'normalizer_distance_squared':f'{DN2:.10f}'})
    print(json.dumps({'status':'PASS within small-example scope',
                      'checks':CHECKS,'check_count':len(CHECKS),
                      'largest_matrix_dimension':60,
                      'toy_group':'A5 in its four-dimensional standard representation',
                      'normalizer_is_not_target_group_negative_control':True,
                      'normalizer_diagnostics':diagnostics,
                      'full_monster_simulation':False,
                      'independent_proof_review':False},indent=2,sort_keys=True))

if __name__=='__main__': main()
