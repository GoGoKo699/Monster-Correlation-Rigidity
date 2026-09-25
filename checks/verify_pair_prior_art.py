#!/usr/bin/env python3
"""Scoped checks for Note 11: projector reductions, finite-set testing and conditioning.

No Monster-sized operator is constructed. The analytic orbit/stabilizer proofs
are not established by these tests. Maximum square matrix dimension: 81;
maximum state-vector length: 256. Large finite-set budgets use Decimal scalars.
"""
from __future__ import annotations
from decimal import Decimal as D, localcontext, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import numpy as np

BASE = '85215c45005a3241485b99b57b2dc9de63b85702'
ROOT = Path(__file__).resolve().parents[1]
LABELS: list[str] = []
TOL = 1e-10


def need(ok, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def close(x, y, label: str) -> None:
    need(np.linalg.norm(np.asarray(x)-np.asarray(y)) <= TOL, label)


def unitary(n: int, rng) -> np.ndarray:
    a = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    phases = np.diag(r)/abs(np.diag(r))
    return q @ np.diag(phases)


def rot(theta: float) -> np.ndarray:
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])


def loss(p, u, rank: int) -> float:
    v = np.kron(u, u)
    return float(np.linalg.norm((np.eye(len(p))-p) @ v @ p)**2/rank)


def projector_reductions() -> None:
    rng = np.random.default_rng(2291)
    for d, r in ((2, 1), (2, 2), (3, 3)):
        n = d*d
        basis = unitary(n, rng)[:, :r]
        p = basis @ basis.conj().T
        s = 2*p-np.eye(n)
        u = unitary(d, rng); v = np.kron(u, u)
        omega = v @ p @ v.conj().T/r
        eps = loss(p, u, r)
        close(p@p, p, f'projector:d{d}r{r}_idempotent')
        close(s@s, np.eye(n), f'Z2:d{d}r{r}_reflection_representation')
        close((np.eye(n)+s)/2, p, f'Z2:d{d}r{r}_Bose_projector_is_P')
        close(np.trace(p@omega), 1-eps, f'Z2:d{d}r{r}_same_pair_acceptance')
        close(np.linalg.norm(p-v@p@v.conj().T)**2/(2*r), eps,
              f'orbit:d{d}r{r}_squared_chord_identity')
        close(np.linalg.norm(p@v-v@p)**2/(2*r), eps,
              f'orbit:d{d}r{r}_commutator_identity')
        # Canonical channel-Choi commutation test on V=U tensor U.
        choi = v.reshape(-1)/math.sqrt(n)
        q = (np.eye(n*n)+np.kron(s, s.conj()))/2
        close(q@q, q, f'Choi:d{d}r{r}_commutation_projector')
        close(1-np.vdot(choi, q@choi), (2*r/n)*eps,
              f'Choi:d{d}r{r}_exact_signal_dilution')
    # General-state fidelity maximization: normalized projection attains Tr(P rho).
    a = rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4))
    rho = a@a.conj().T; rho /= np.trace(rho)
    values, vectors = np.linalg.eigh(rho)
    root = (vectors*np.sqrt(values))@vectors.conj().T
    basis = unitary(4, rng)[:, :2]; p = basis@basis.conj().T
    prob = np.trace(p@rho).real
    tau = p@rho@p/prob
    # Rank is exactly 2. Omit only the two structural zero eigenvalues.
    eig = np.linalg.eigvalsh(root@tau@root)[-2:]
    close(np.sqrt(np.maximum(eig, 0)).sum()**2, prob,
          'fidelity:normalized_projection_attains_support_probability')
    max_seen = 0.
    for _ in range(12):
        a = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
        t = a@a.conj().T; t /= np.trace(t)
        eig = np.linalg.eigvalsh(root@basis@t@basis.conj().T@root)[-2:]
        max_seen = max(max_seen, float(np.sqrt(np.maximum(eig, 0)).sum()**2))
    need(max_seen <= prob+TOL, 'fidelity:sample_supported_states_obey_analytic_upper_bound')
    p = np.diag([1., 0.]); omega = np.diag([0., 1.]); s = 2*p-np.eye(2)
    close(s@omega@s, omega, 'negative_control:ordinary_Z2_invariance_accepts_wrong_block')
    close(np.trace(p@omega), 0, 'negative_control:Bose_support_test_rejects_wrong_block')


def finite_set_gram_checks() -> None:
    # D3: six distinct projective rays, but their one-copy Choi span has dimension 4.
    reflection = np.diag([1., -1.])
    targets = [rot(2*math.pi*j/3)@s for s in (np.eye(2), reflection) for j in range(3)]
    states = [g.reshape(-1)/math.sqrt(2) for g in targets]
    mat = np.column_stack(states); gram = mat.conj().T@mat
    close(np.max(abs(gram-np.eye(6))), .5, 'finite_set:D3_max_offdiagonal_overlap_one_half')
    need(np.linalg.matrix_rank(mat, tol=TOL) == 4,
         'negative_control:distinct_one_copy_rays_need_not_be_linearly_independent')
    k = 4
    tensor_states = []
    for state in states:
        v = state
        for _ in range(k-1):
            v = np.kron(v, state)
        tensor_states.append(v)
    b = np.column_stack(tensor_states); gk = b.conj().T@b
    close(gk, gram**k, 'finite_set:tensor_power_Gram_entrywise_power')
    eigen = np.linalg.eigvalsh(gk)
    need(min(eigen) >= 1-5*(.5**k)-TOL, 'finite_set:Gershgorin_lower_bound')
    need(np.linalg.matrix_rank(b, tol=TOL) == 6, 'finite_set:powered_rays_are_independent')
    for j in range(6):
        overlaps = b.conj().T@tensor_states[j]
        close(np.vdot(overlaps, np.linalg.solve(gk, overlaps)), 1,
              f'finite_set:perfect_completeness_target{j}')
    rng = np.random.default_rng(2292)
    for j in range(3):
        u = unitary(2, rng); state = u.reshape(-1)/math.sqrt(2)
        query = state
        for _ in range(k-1):
            query = np.kron(query, state)
        overlaps = b.conj().T@query
        accept = np.vdot(overlaps, np.linalg.solve(gk, overlaps)).real
        a = max(abs(np.vdot(v, state)) for v in states)
        bound = 6*a**(2*k)/(1-5*.5**k)
        need(accept <= bound+TOL, f'finite_set:Gram_inverse_acceptance_bound{j}')
        d2 = min(2-abs(np.trace(g.conj().T@u)) for g in targets)
        close(d2, 2*(1-a), f'finite_set:phase_Frobenius_metric_conversion{j}')


def conditioning_checks() -> None:
    swap = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], float)
    sym = (np.eye(4)+swap)/2
    paulis = [np.array([[0,1],[1,0]], complex),
              np.array([[0,-1j],[1j,0]]), np.diag([1.,-1.])]
    u = rot(math.pi/4)
    for t in (F(1,2), F(1,10), F(1,100)):
        x = float(t)
        psi = np.array([1+x,0,0,1-x])/math.sqrt(2*(1+x*x))
        p = sym-np.outer(psi, psi)
        rank = 2
        close(np.trace(p), rank, f'conditioning:pair_rank_d_t{t}')
        close(p@p, p, f'conditioning:pair_projector_t{t}')
        exact_loss = (1-1/(1+t*t)**2)/2
        close(loss(p,u,rank), float(exact_loss), f'conditioning:pair_fixed_rotation_loss_t{t}')
        qdiag = []
        comms = []
        for h in paulis:
            kh = np.kron(h,np.eye(2))+np.kron(np.eye(2),h)
            comms.append(kh@p-p@kh)
        for comm in comms:
            qdiag.append(np.linalg.norm(comm)**2/(2*rank))
        expected = [2/(1+x*x),2*x*x/(1+x*x),2*(1-x*x)**2/(1+x*x)**2]
        close(qdiag,expected,f'conditioning:pair_exact_tangent_eigenvalues_t{t}')
        cross = np.array([[np.vdot(a,b).real/(2*rank) for a in comms] for b in comms])
        close(cross,np.diag(expected),f'conditioning:pair_tangent_offdiagonals_zero_t{t}')
        # Both group representatives stabilize P for all phases. Completeness
        # of the stabilizer is proved by the nondegenerate Takagi spectrum.
        for g in (np.eye(2),np.diag([1.,-1.])):
            close(loss(p,g,rank),0,f'conditioning:pair_exact_symmetry_{int(g[1,1])}_t{t}')
        dist2 = min(2-abs(np.trace(g.T@u)) for g in (np.eye(2),np.diag([1.,-1.])))
        close(dist2,2-math.sqrt(2),f'conditioning:pair_distance_independent_of_t{t}')
    # Cubic example: finite exact REAL ray stabilizer stays constant for t>0,
    # with a uniformly positive tangent coefficient but a distant near symmetry.
    v3 = np.zeros(8);v3[[0,3,5,6]]=[.5,-.5,-.5,-.5]
    v1 = np.zeros(8);v1[0]=math.sqrt(3)/2;v1[[3,5,6]]=1/(2*math.sqrt(3))
    close(np.vdot(v3,v1),0,'conditioning:cubic_harmonic_sectors_orthogonal')
    close([np.linalg.norm(v3),np.linalg.norm(v1)],[1,1],'conditioning:cubic_sectors_normalized')
    j = np.array([[0.,-1.],[1.,0.]])
    gen = np.kron(np.kron(j,np.eye(2)),np.eye(2))+np.kron(np.kron(np.eye(2),j),np.eye(2))+np.kron(np.eye(4),j)
    theta=2*math.pi/3;r=rot(theta);r3=np.kron(np.kron(r,r),r)
    for t in (F(1,2),F(1,10),F(1,100)):
        x=float(t);v=(v3+x*v1)/math.sqrt(1+x*x)
        overlap=np.vdot(v,r3@v)
        close(overlap,(1-x*x/2)/(1+x*x),f'conditioning:cubic_distant_overlap_t{t}')
        exact=3*t*t*(1+t*t/4)/(1+t*t)**2
        close(1-abs(overlap)**2,float(exact),f'conditioning:cubic_distant_loss_t{t}')
        curvature=(9+t*t)/(1+t*t)
        close(np.linalg.norm(gen@v)**2,float(curvature),f'conditioning:cubic_local_curvature_t{t}')
        need(curvature>=5,f'conditioning:cubic_uniformly_positive_local_bound_t{t}')
        g=[np.eye(2),-np.eye(2),np.diag([1.,-1.]),np.diag([-1.,1.])]
        close(min(np.linalg.norm(r-h)**2/2 for h in g),1,
              f'conditioning:cubic_distant_normalized_distance_one_t{t}')
        need(max(1-abs(np.vdot(v,np.kron(np.kron(h,h),h)@v))**2 for h in g)<TOL,
             f'conditioning:cubic_exact_real_ray_group_t{t}')
    close(abs(np.vdot(v3,r3@v3)),1,'conditioning:cubic_limit_has_extra_discrete_symmetry')


def budgets() -> dict:
    path=ROOT/'data/monster_character_excerpt.json'
    raw=path.read_bytes()
    need(hashlib.sha256(raw).hexdigest()=='70218f4f87e67896a64c8577b7a86fb0c46cebe3c71678397a7654b8ef0596e0',
         'source:pinned_character_excerpt_unchanged')
    data=json.loads(raw);chars=data['character'];m=data['centralizers'][0];d=chars[0]
    need(max(map(abs,chars[1:]))==4371,'Monster:maximum_ABSOLUTE_nonidentity_character_4371')
    need(F(4371,d)<1,'Monster:target_rays_are_projectively_distinct')
    need(m>d*d,'Monster:one_copy_target_Choi_rays_cannot_be_independent')
    out=[]
    with localcontext() as ctx:
        ctx.prec=90
        a=D(4371)/D(d)
        first=(D(2*(m-1)).ln()/(-a.ln()))
        ksep=int(first.to_integral_value(rounding=ROUND_CEILING))
        need(ksep==33,'Monster:33_copies_suffice_for_Gram_separation_bound')
        n=int(((D(1)/3).ln()/(1-D('1e-12')).ln()).to_integral_value(rounding=ROUND_CEILING))
        need(n==1098612288668,'comparison:current_threshold_gives_1098612288668_pair_trials')
        for eta,k_expected in (('0.1',12561),('0.01',1259151),('0.001',125918152)):
            b=1-D(eta)**2/2
            second=D(6*m).ln()/(-2*b.ln())
            k=max(ksep,int(second.to_integral_value(rounding=ROUND_CEILING)))
            need(k==k_expected,f'comparison:Wang_Gram_sufficient_calls_eta{eta}')
            need(D(k)*a.ln()+D(2*(m-1)).ln()<=0,f'comparison:Gram_condition_eta{eta}')
            need(2*D(k)*b.ln()+D(6*m).ln()<=0,f'comparison:one_third_soundness_eta{eta}')
            out.append({'phase_normalized_Frobenius_distance':eta,'sufficient_forward_calls':k,
                        'uncompiled_collective_Choi_measurement':True})
    return {'group_order':str(m),'dimension':d,'max_target_overlap':'4371/196883',
            'Wang_Gram_separation_copies':ksep,'finite_set_budgets':out,
            'pair_trials_from_current_threshold_for_failure_one_third':n,
            'pair_forward_calls_from_current_threshold':2*n,
            'comparison_is_between_sufficient_upper_bounds_not_lower_bounds':True,
            'quantum_advantage_or_practical_compiler_claim':False}


def main() -> None:
    projector_reductions();finite_set_gram_checks();conditioning_checks();table=budgets()
    print(json.dumps({'status':'PASS within stated prior-art and conditioning scopes',
        'base_commit':BASE,'checks':len(LABELS),'labels':LABELS,'budgets':table,
        'largest_square_matrix_dimension':81,'largest_state_vector_length':256,
        'large_Monster_Gram_matrix_constructed':False,
        'global_orbit_theorem_formally_verified':False,
        'stabilizer_completeness_proved_by_numerical_search':False,
        'new_C13_threshold':False,'full_W_compiled':False,'novelty_established':False,
        'numerical_tolerance':TOL,'Decimal_precision_for_scalar_budgets':90},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
