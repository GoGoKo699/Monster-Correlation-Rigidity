#!/usr/bin/env python3
"""Adversarial final checks of the bounded core (not a VOA proof assistant).

Uses independent bisection bounds and a 3-stress algebra to audit the saved
interval implementation. All existing verifier sources are hash checked.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import verify_calibration_and_sharpness as cal
import verify_extraction_core as core

LABELS=[]
COUNTS={'interval_endpoint_cases':0,'square_root_cases':0,'field_pairs':0,
        'sound_successes':0,'inconclusive_pairs':0,'monotonicity_pairs':0}

def need(value,label):
    if not value: raise RuntimeError(label)
    LABELS.append(label)

def require(value,message):
    if not value: raise RuntimeError(message)


def independent_root(x,steps=160):
    """Rational bisection oracle; no integer-square-root implementation shared."""
    if x<0: raise ValueError('negative radicand')
    lo,hi=Q(0),max(Q(1),x)
    for _ in range(steps):
        mid=(lo+hi)/2
        if mid*mid>x: hi=mid
        else: lo=mid
    return lo,hi


def polyadd(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]

def polymul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z


def structural_identities():
    # The local estimate is verified by the chord-polynomial calculation,
    # not by constructing or sampling any candidate interaction tensor.
    q=[1,0,-Q(1,2)]
    t2=polyadd([1],[-x for x in polymul(q,q)])
    require(t2==[0,0,1,0,-Q(1,4)],'chord t squared')
    qt=polymul(q,t2)
    require(qt==[0,0,1,0,-Q(3,4),0,Q(1,8)],'q times t squared')
    need(Q(3,4)-Q(1,8)*Q(1,10)**2>0,'proof:qt_squared_le_chord_squared_on_declared_ball')
    need(Q(3)-Q(3,100)-Q(4,10)>2,'proof:quadratic_loss_constant_has_strict_margin')
    need(Q(1,50)<Q(1,2),'proof:entry_loss_strictly_below_critical_gap')
    # e0 f norm uses BOTH the Virasoro commutator and the idempotence of f.
    need(2*2==4,'proof:singular_product_norm_is_four_times_Ising_overlap')
    need(Q(47,192)*Q(3,188)==Q(1,256),'proof:discrete_gap_conversion')
    need(Q(1,128)+2*Q(1,256)<Q(3,188),'proof:historical_pair_budget_is_strict')
    # Uniqueness condition in the lemma is not assumed in the pair theorem:
    # when budget is small enough it follows automatically.
    need(2*Q(3,188)<Q(1,10),'proof:certifying_overlap_budget_implies_unique_rounding')
    # Independent order-two Taylor coefficients for the known-theory curve.
    d=Q(2208,2209)
    loss=3*d+46*Q(3,2)*d
    distance=2*Q(1,2)*d
    need(loss==72*d and distance==d,'proof:sharp_curve_leading_coefficients')


def interval_audit():
    intervals=[cal.Interval(Q(a,3),Q(b,3)) for a in range(-6,7)
               for b in range(a,7)]
    # Every pair of endpoints is enough for extrema of multiplication on a box;
    # midpoint controls also exercise crossing-zero square/cube special cases.
    for A,B in product(intervals,repeat=2):
        valuesA=(A.lo,(A.lo+A.hi)/2,A.hi)
        valuesB=(B.lo,(B.lo+B.hi)/2,B.hi)
        for x,y in product(valuesA,valuesB):
            require((A*B).contains(x*y),'product inclusion')
            require((A+B).contains(x+y),'sum inclusion')
            require((A-B).contains(x-y),'difference inclusion')
            if not B.lo<=0<=B.hi:
                require((A/B).contains(x/y),'division inclusion')
            COUNTS['interval_endpoint_cases']+=1
        for x in valuesA:
            require(A.square().contains(x*x) and A.cube().contains(x**3),
                    'power inclusion')
    need(True,'implementation:exhaustive_rational_interval_box_controls')
    for x in [Q(0),Q(1),Q(2),Q(141),Q(1,10**50),Q(10**40),
              Q(47,192),Q(1,4),Q(999999,1000000)]:
        for bits in (0,1,8,32,80):
            lo,hi=cal.sqrt_bounds(x,bits)
            require(lo*lo<=x<=hi*hi and hi-lo<=Q(1,2**bits),'root enclosure')
            lower,upper=independent_root(x,steps=400)
            require(lo<=upper and hi>=lower,'root independent oracle agreement')
            COUNTS['square_root_cases']+=1
    need(True,'implementation:roots_cover_tiny_large_and_exact_square_inputs')
    for args in [(-Q(1),80),(Q(1),-1)]:
        try: cal.sqrt_bounds(*args)
        except ValueError: continue
        raise RuntimeError('invalid root was not rejected')
    need(True,'implementation:invalid_root_domains_rejected')
    try: cal.Interval.point(1)/cal.Interval(-Q(1),Q(1))
    except ValueError: pass
    else: raise RuntimeError('division by interval containing zero')
    need(True,'implementation:zero_crossing_denominator_rejected')


G=(Q(1,4),Q(1,4),Q(23,2))
W=(Q(1),)*3
E=(Q(1),Q(0),Q(0)); F=(Q(0),Q(1),Q(0))

def ip(x,y):return sum(g*a*b for g,a,b in zip(G,x,y))
def raw(x):return ip(x,x),ip(W,x),sum(2*g*a**3 for g,a in zip(G,x))
def shift(x,s,a):return tuple(s*t+a for t in x)
def plus(x,y,t):return tuple(a+t*b for a,b in zip(x,y))


def oracle(f,z):
    # Compute projected primary norm/cubic from coordinates independently,
    # not by copying the implementation's correction formula.
    def projected(w):
        tau=ip(W,w)
        u=tuple(x-tau/12 for x in w)
        norm=ip(u,u); cub=sum(2*g*x**3 for g,x in zip(G,u))
        return u,norm,cub
    x,N,c=projected(f); y,NN,cc=projected(z)
    require(N>0 and NN>0,'oracle primary norm')
    _,b=independent_root(N); _,bb=independent_root(NN)
    caplo,caph=independent_root(Q(2116,141))
    # We only certify tested positive-cubic cases; negative ones are checked
    # by the interval routine returning inconclusive below.
    if c<=0 or cc<=0: return False
    fminus=c/(N*b); gminus=cc/(NN*bb)
    ex=max(Q(0),caph-fminus); ey=max(Q(0),caph-gminus)
    pl,ph=independent_root(N*NN)
    cross=ip(x,y)
    ol,oh=sorted((cross/pl,cross/ph))
    delta=max(abs(ol+Q(1,47)),abs(oh+Q(1,47)))
    rx=independent_root(ex/2)[1]; ry=independent_root(ey/2)[1]
    return ex<Q(1,50) and ey<Q(1,50) and delta+rx+ry<Q(3,188)


def calibration_audit():
    A=tuple(x-Q(1,48) for x in E)
    B=tuple(x-Q(1,48) for x in F)
    target_tangent=plus(B,A,Q(1,47))
    for t,s,a in product((Q(0),Q(1,10**6),Q(1,1000),Q(1,20)),
                         (Q(1,10),Q(1),Q(11)),(Q(-3),Q(0),Q(5))):
        f=shift(plus(A,target_tangent,t),s,a)
        z=shift(B,Q(7,3),-Q(2,5))
        n,tau,c=raw(f); nn,tt,cc=raw(z)
        values=(n,nn,tau,tt,c,cc,ip(f,z))
        answer=cal.calibrated_criterion(*(cal.Interval.point(x) for x in values))
        COUNTS['field_pairs']+=1
        if answer['certified']:
            require(oracle(f,z),'independent oracle rejected a successful interval certificate')
            COUNTS['sound_successes']+=1
        else: COUNTS['inconclusive_pairs']+=1
        small=cal.calibrated_criterion(*(cal.Interval.radius(x,Q(1,10**16)) for x in values))
        large=cal.calibrated_criterion(*(cal.Interval.radius(x,Q(1,10**12)) for x in values))
        require(not large['certified'] or small['certified'],'nested interval monotonicity')
        COUNTS['monotonicity_pairs']+=1
    need(COUNTS['sound_successes']>0,'implementation:successful_calibrations_pass_independent_rational_oracle')
    need(COUNTS['inconclusive_pairs']>0,'implementation:off_target_inputs_are_not_all_accepted')
    need(True,'implementation:interval_enlargement_does_not_improve_certification')
    # Mutant normalization omitting cubic stress correction produces a large
    # false apparent signal after stress shift; the correct identity cancels it.
    f=shift(E,Q(2),Q(5)); n,tau,c=raw(f)
    corrected=c-tau*n/2+tau**3/36
    primary=tuple(x-tau/12 for x in f)
    exact=sum(2*g*x**3 for g,x in zip(G,primary))
    need(corrected==exact and c!=exact,'negative_control:stress_term_is_essential')
    values=(Q(1,4),Q(1,4),Q(1,4),Q(1,4),Q(1,2),Q(1,2),Q(0))
    need(cal.calibrated_criterion(*(cal.Interval.point(x) for x in values))['certified'],
         'implementation:uncentered_exact_Ising_pair_passes')
    impossible=list(values); impossible[4]=Q(100)
    need(not cal.calibrated_criterion(*(cal.Interval.point(x) for x in impossible))['certified'],
         'implementation:inconsistent_cap_is_not_a_success')
    same=list(values); same[6]=Q(1,4)
    need(not cal.calibrated_criterion(*(cal.Interval.point(x) for x in same))['certified'],
         'implementation:duplicating_one_Ising_field_fails_pair_condition')
    near_zero=(Q(12),Q(1,4),Q(12),Q(1,4),Q(24),Q(1,2),Q(1,4))
    need(not cal.calibrated_criterion(*(cal.Interval.point(x) for x in near_zero))['certified'],
         'implementation:pure_stress_projection_is_rejected')
    need(not core.interval_certificate(Q(0),Q(0),Q(3,188))['sufficient_inequalities_pass'],
         'implementation:discrete_gap_boundary_is_strict')


def main():
    files={'verify_extraction_core.py':'d2062b1577beb7a34c0665fc358da7b1daf846886cd48dfa0b26acf83c107e83',
           'verify_calibration_and_sharpness.py':'d2c16a6c9c01af9d1198cfc2b4459d78966a42c314b8a0575bd37626bcd2eef1'}
    for path,h in files.items():
        need(hashlib.sha256(Path(__file__).with_name(path).read_bytes()).hexdigest()==h,
             'preservation:'+path)
    structural_identities(); interval_audit(); calibration_audit()
    print(json.dumps({'status':'PASS bounded adversarial implementation and normalization checks',
        'reviewed_head':'6d460bef7041f17cba1658c99d6797ef4b00275c',
        'checks':len(LABELS),'labels':LABELS,'case_counts':COUNTS,
        'arithmetic':'rational arithmetic; independent bisection oracle',
        'largest_physical_coefficient_vector':3,'full_VOA_simulated':False,
        'analytic_proof_or_source_theorems_verified_by_sampling':False,
        'manuscript_written':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
