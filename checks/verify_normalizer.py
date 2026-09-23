#!/usr/bin/env python3
"""Exact scalar/character checks for the normalizer-rounding research note.

Standard library only; assertions are not used. Literature theorems and all
Monster-sized matrix identities are mathematical inputs, not simulated here.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal, localcontext
import json

CHECKS: list[str] = []

def need(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError('Check failed: ' + label)
    CHECKS.append(label)

def dec(x: F | int) -> Decimal:
    x=F(x)
    return Decimal(x.numerator)/Decimal(x.denominator)

def main() -> None:
    root=Path(__file__).resolve().parents[1]
    tab=json.loads((root/'data'/'monster_character_excerpt.json').read_text())
    centralizers=tab['centralizers']
    # The input excerpt is a declared transcription, not an original GAP file.
    chi=tab.get('character',tab.get('chi'))
    if chi is None:
        other=[(k,len(v)) for k,v in tab.items() if isinstance(v,list)]
        raise RuntimeError('Find the declared character field: '+repr(other))
    d=196883; kappa=F(13858,3); gap=F(11161,13858)
    order=808017424794512875886459904961710757005754368000000000
    KR=F(48011041,787532); m2=F(2116,141)
    need(len(chi)==len(centralizers)==194,'Character excerpt has 194 classes')
    need(chi[0]==d and centralizers[0]==order,'Degree and group order')
    moments=[sum((F(c**k,z) for c,z in zip(chi,centralizers)),F(0)) for k in range(5)]
    need(moments==list(map(F,[1,0,1,1,6])),'Exact character moments 0 through 4')
    need(max(chi[1:])==4371,'Maximum nonidentity character equals 4371')
    need(max(map(abs,chi[1:]))==4371,'Maximum absolute nonidentity character equals 4371')
    sep2=2-2*F(4371,d)
    need(sep2>F(5,4)**2,'Distinct group matrices are separated by more than 5/4')

    scaled_spectrum=[F(46),F(-1),F(11),F(1,2)]
    spectral_gap=min(abs(F(1,2)-s) for s in scaled_spectrum if s!=F(1,2))
    need(spectral_gap==F(3,2),'Scaled Miyamoto eigenspace gap equals 3/2')
    g2=spectral_gap**2/F(141)
    lipschitz2=4/g2
    need(lipschitz2==F(752,3),'Squared spectral-projector Lipschitz coefficient')
    scale=lipschitz2*kappa/d
    need(scale==F(10421216,1771947),'Normalized tensor-to-involution scale')

    # Rigorous rational envelopes for B and B0; displayed decimals are diagnostic.
    root2upper=F(1415,1000); sqrtmupper=F(1969,1000)
    need(F(2)<root2upper**2,'sqrt(2) below 1.415')
    need(m2<sqrtmupper**4,'sqrt(M) below 1.969')
    Bupper=scale*(root2upper+4*sqrtmupper)**2
    need(Bupper<508,'B below 508 by exact rational arithmetic')
    sqrtKRupper=F(781,100); twoinvrootgap=F(2229,1000)
    need(KR<sqrtKRupper**2,'sqrt(K_R) below 7.81')
    need(4/gap<twoinvrootgap**2,'2/sqrt(Delta) below 2.229')
    B0upper=(3*sqrtKRupper+twoinvrootgap)**2/2
    need(B0upper<330,'B0 below 330 by exact rational arithmetic')
    need(2*F(508)/gap<1300,'Real rejection-to-conjugation coefficient below 1300')
    need(F(508)*330<170000,'Complex rejection-to-conjugation coefficient below 170000')

    beta=F(1,16); q=F(1,2); conditional=(q+beta)/(1-beta)
    need(conditional==F(3,5),'Deletion of at most 1/16 gives walk norm at most 3/5')
    length=250; threshold=F(1,600); delta=length*threshold
    need((order-1)*conditional**length<1,'The 250-step good-class walk has full support')
    need(delta==F(5,12),'Accumulated group-word error is 5/12')
    need(3*delta==F(5,4) and (3*delta)**2<sep2,'Multiplication rounds exactly by group separation')
    need(2*delta<3*delta,'Injectivity and nearest-point uniqueness also hold')
    need(delta<1,'Averaged intertwiner is nonzero')
    eta=beta*threshold**2
    need(eta==F(1,5760000),'Allowed average squared involution error')
    need(F(1300,10**10)<eta,'Real error 1e-10 meets normalizer-rounding condition')
    need(F(170000,10**12)<eta,'Complex error 1e-12 meets normalizer-rounding condition')
    need(F(2600)<52**2,'Real preliminary distance coefficient below 52')
    need(KR<8**2 and F(340000)<584**2 and 8+584<600,
         'Complex preliminary distance coefficient below 600')
    need(F(d*52**2,10**10)<F(1,9),'Real bootstrap ordinary operator distance below 1/3')
    need(F(d*600**2,10**12)<F(1,9),'Complex bootstrap ordinary operator distance below 1/3')
    need(F(256)<9*35,'4 asin(1/6) <= 4/sqrt(35) < pi/4 using pi > 3')
    # pi < 355/113 gives a rational certification of the displayed coefficient.
    need(F(1681)*F(355,113)**2/12528<F(1151,1000)**2,
         'Sharp local prefactor is below 1.151 using pi < 355/113')

    AW=9*scale
    need(AW==F(10421216,d),'Transport-to-involution squared coefficient A_W')
    need(AW*F(3,10**9)<eta,'Transport threshold W^2 <= 3e-9 is sufficient')
    need(2*AW<106<F(103,10)**2,'One-Monster distance squared below 106 W^2')
    with localcontext() as ctx:
        ctx.prec=50
        m=dec(m2).sqrt(); B=dec(scale)*(dec(2).sqrt()+4*m.sqrt())**2
        B0=(3*dec(KR).sqrt()+2/dec(gap).sqrt())**2/2
        diagnostics={
            'B':str(B),'B0':str(B0),
            'real_coefficient':str(2*B/dec(gap)),
            'complex_coefficient':str(B*B0),
            'minimum_group_separation':str(dec(sep2).sqrt()),
            'mixing_support_margin':str(dec((order-1)*conditional**length)),
            'transport_coefficient_A_W':str(dec(AW)),
            'normalizer_threshold_z_squared':str(dec(eta))}
    print(json.dumps({'status':'PASS within stated computational scope',
                      'checks':CHECKS,'check_count':len(CHECKS),
                      'diagnostic_decimal_values':diagnostics,
                      'literature_inputs_proved_by_this_script':False,
                      'full_monster_simulation':False,
                      'independent_proof_review':False},indent=2,sort_keys=True))

if __name__=='__main__': main()
