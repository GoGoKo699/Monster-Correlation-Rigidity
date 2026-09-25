#!/usr/bin/env python3
"""Small access-model checks; no Monster tensor and no efficiency certification.

Emits deterministic pass/fail data, not platform-sensitive floating residuals.
All conditions remain active under -O and -OO. Numerical tolerance is 1e-10.
"""
from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
from itertools import permutations
import json
import math
import numpy as np

LABELS: list[str] = []
TOL = 1e-10


def need(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)
    LABELS.append(label)


def close(a, b, label: str) -> None:
    need(bool(np.linalg.norm(np.asarray(a)-np.asarray(b)) <= TOL), label)


def unitary(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q


def check_isometry_model(d: int) -> None:
    n = d*d
    extension = unitary(n, 600+d)
    inds = [a*d for a in range(d)]
    w = extension[:, inds]
    pin = np.zeros((n,n), complex)
    pin[inds, inds] = 1
    p = w @ w.conj().T
    sigma = p/d
    close(w.conj().T @ w, np.eye(d), f'd{d}:isometry')
    close(extension @ (pin/d) @ extension.conj().T, sigma, f'd{d}:mixed_preparation')
    close(extension @ pin @ extension.conj().T, p, f'd{d}:inverse_measurement_effect')
    close(p @ p, p, f'd{d}:projection')
    close(np.trace(p), d, f'd{d}:rank_trace')
    prob = np.trace(p)/n
    close(prob, 1/d, f'd{d}:maximally_mixed_filter_probability')
    close((p/n)/prob, sigma, f'd{d}:conditional_filtered_state')
    u = unitary(d, 40+d)
    uu = np.kron(u,u)
    out = uu @ sigma @ uu.conj().T
    eps = 1-np.trace(p @ out).real
    close(np.trace(pin @ extension.conj().T @ out @ extension), 1-eps,
          f'd{d}:operational_acceptance')
    close(np.trace(sigma @ out), (1-eps)/d, f'd{d}:swap_signal')
    swap = np.zeros((n*n,n*n))
    for i in range(n):
        for j in range(n):
            swap[i*n+j,j*n+i] = 1
    close(np.trace(swap @ np.kron(sigma,out)), (1-eps)/d, f'd{d}:swap_contraction')
    vals, vecs = np.linalg.eigh(sigma)
    refl = (vecs*np.exp(-1j*math.pi*d*vals)) @ vecs.conj().T
    close(refl, np.eye(n)-2*p, f'd{d}:density_reflection')
    # A flagged program specifies a controlled reflection, not just its channel.
    flag = np.diag([0.,1.])
    prog = np.kron(flag,sigma)
    vals, vecs = np.linalg.eigh(prog)
    ctrl = (vecs*np.exp(-1j*math.pi*d*vals)) @ vecs.conj().T
    ideal_ctrl = np.kron(np.diag([1.,0.]),np.eye(n))+np.kron(flag,np.eye(n)-2*p)
    close(ctrl, ideal_ctrl, f'd{d}:flagged_controlled_reflection')
    tau0 = np.zeros((n,n)); tau0[0,0] = 1
    a = .07; b = .04
    noisy_prep = (1-a)*sigma+a*tau0
    effect = (1-b)*p+b*np.eye(n)/2
    noisy_out = uu @ noisy_prep @ uu.conj().T
    prep_error = np.linalg.svd(noisy_prep-sigma,compute_uv=False).sum()/2
    meas_error = np.linalg.norm(effect-p,2)
    actual_error = abs(np.trace(effect @ noisy_out).real-(1-eps))
    need(actual_error <= prep_error+meas_error+TOL, f'd{d}:calibration_triangle_bound')
    need(prep_error <= a+TOL and meas_error <= b+TOL, f'd{d}:error_budget')


def check_symmetric_tensor() -> None:
    d=3
    t=np.zeros((d,d,d))
    for ijk in permutations(range(d)):
        t[ijk]=1
    kappa=2
    w=t.reshape(d,d*d).T/math.sqrt(kappa)
    p=w@w.T
    kraus=[t[k]/math.sqrt(kappa) for k in range(d)]
    j=np.zeros((d*d,d*d))
    for a in range(d):
        for b in range(d):
            e=np.zeros((d,d)); e[a,b]=1
            image=sum(k@e@k.T for k in kraus)
            j[a*d:(a+1)*d,b*d:(b+1)*d]=image/d
    close(w.T@w,np.eye(d),'tensor:isometry')
    close(j,p/d,'tensor:normalized_Choi_equals_pair_probe')
    close(sum(k.T@k for k in kraus),np.eye(d),'tensor:trace_preserving_channel')
    close(np.trace(j.reshape(d,d,d,d),axis1=1,axis2=3),np.eye(d)/d,'tensor:Choi_input_marginal')
    # Qubit padding: an ancilla-zero test alone includes an unwanted input.
    D=4
    correct=np.zeros((D*D,D*D)); naive=correct.copy()
    for a in range(D):
        naive[a*D,a*D]=1
        if a<d: correct[a*D,a*D]=1
    pad=np.zeros(D*D);pad[d*D]=1
    close(pad@naive@pad,1,'padding:naive_test_accepts_unused_basis_vector')
    close(pad@correct@pad,0,'padding:logical_membership_rejects_unused_basis_vector')


def scalar_checks() -> dict:
    d=196883
    need(d*d == 38762915689,'scalar:dimension_squared')
    need(F(d,d*d)==F(1,d),'scalar:filter_probability')
    need(F(1,2)+F(1,2*d) < F(3,4),'scalar:swap_probability_range')
    # KL <= 4 delta^2/(3d^2), Pinsker TV>=1/3 gives N>=d^2/(6 delta^2).
    need(F(16,3)*F(1,4)==F(4,3),'scalar:Bernoulli_KL_constant')
    need(F(2,9)/F(4,3)==F(1,6),'scalar:restricted_SWAP_lower_constant')
    with localcontext() as ctx:
        ctx.prec=80
        alpha=Decimal('0.05'); threshold=Decimal('1e-12')
        counts=[]
        for eta in (Decimal(0),threshold/2):
            budget=threshold-eta
            n=int((alpha.ln()/(1-budget).ln()).to_integral_value(rounding=ROUND_CEILING))
            need(Decimal(n)*(1-budget).ln() <= alpha.ln(),'confidence:zero_rejection_sufficient_'+str(eta))
            need(Decimal(n-1)*(1-budget).ln() > alpha.ln(),'confidence:zero_rejection_minimal_'+str(eta))
            counts.append(n)
        need(threshold-threshold==0,'confidence:budget_at_threshold_uninformative')
    return {'logical_dimension':d,'logical_dimension_squared':d*d,
            'uniform_filter_expected_trials':d,
            'zero_rejection_95pct_trials_ideal':counts[0],
            'zero_rejection_95pct_trials_half_budget':counts[1]}


def main() -> None:
    for d in (2,3):
        check_isometry_model(d)
    check_symmetric_tensor()
    scalars=scalar_checks()
    print(json.dumps({'status':'PASS within declared access-model scope',
                      'checks':len(LABELS),'labels':LABELS,'scalars':scalars,
                      'largest_matrix_dimension':81,'numerical_tolerance':TOL,
                      'full_Monster_simulation':False,'efficient_W_constructed':False,
                      'novelty_established':False},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
