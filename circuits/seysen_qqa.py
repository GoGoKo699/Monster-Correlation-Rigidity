#!/usr/bin/env python3
"""Clean A_0 -> Q tensor Q block isometry, not the complete Monster W.

Gate library: X, H, CNOT, Toffoli, Ry(angle). Angles are in radians.
Coordinates are little-endian five-bit words x[0:5], y[5:10].
Flags 10,11 and scratch 12:21 start and end at zero on valid inputs.
Twelve Bell pairs occupy wires (21+k,33+k), k=0,...,11.
The valid input labels are (i,j), i<j<24, and (k,k), 1<=k<24.
Outputs represent |Phi_4096> tensor vec(A), regrouped as (spinor,coordinate)
registers. No sector-packing circuit into a canonical 18-qubit layout is
included. No measurement, postselection, amplitude amplification or QRAM.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
import math
from typing import NamedTuple

class Gate(NamedTuple):
    name: str
    wires: tuple[int, ...]
    angle: float | None = None

class Circuit:
    def __init__(self) -> None:
        self.gates: list[Gate] = []

    def add(self, name: str, *wires: int, angle: float | None = None) -> None:
        if len(set(wires)) != len(wires):
            raise ValueError('Gate wires must be distinct')
        self.gates.append(Gate(name, tuple(wires), angle))

    def mcx(self, controls: list[int], target: int, scratch: list[int]) -> None:
        """Clean k-controlled X; 2k-3 Toffolis for k>=2."""
        k=len(controls)
        if k==0: self.add('X',target); return
        if k==1: self.add('CX',controls[0],target); return
        if k==2: self.add('CCX',*controls,target); return
        if len(scratch)<k-2: raise ValueError('Insufficient MCX scratch')
        chain=[(controls[0],controls[1],scratch[0])]
        chain += [(scratch[j-2],controls[j],scratch[j-1]) for j in range(2,k-1)]
        for g in chain: self.add('CCX',*g)
        self.add('CCX',scratch[k-3],controls[-1],target)
        for g in reversed(chain): self.add('CCX',*g)

    def conditioned(self, controls: list[tuple[int,int]], target: int,
                    scratch: list[int], *, kind: str, angle: float=0.) -> None:
        """X/Z/Ry with positive or negative controls, explicitly decomposed."""
        cs=[q for q,_ in controls]
        if len(set(cs+[target]))!=len(cs)+1 or set(cs+[target])&set(scratch):
            raise ValueError('Overlapping controlled-gate registers')
        neg=[q for q,v in controls if v==0]
        if any(v not in (0,1) for _,v in controls): raise ValueError('Bad control value')
        for q in neg:self.add('X',q)
        if kind in ('X','Z'):
            if kind=='Z':self.add('H',target)
            self.mcx(cs,target,scratch)
            if kind=='Z':self.add('H',target)
        elif kind=='Ry':
            if not cs:self.add('Ry',target,angle=angle)
            else:
                chain=[]
                if len(cs)>1:
                    if len(scratch)<len(cs)-1:raise ValueError('Insufficient Ry scratch')
                    chain=[(cs[0],cs[1],scratch[0])]
                    chain += [(scratch[j-2],cs[j],scratch[j-1]) for j in range(2,len(cs))]
                    for g in chain:self.add('CCX',*g)
                    control=scratch[len(cs)-2]
                else:control=cs[0]
                self.add('Ry',target,angle=angle/2)
                self.add('CX',control,target)
                self.add('Ry',target,angle=-angle/2)
                self.add('CX',control,target)
                for g in reversed(chain):self.add('CCX',*g)
        else:raise ValueError('Unsupported controlled gate')
        for q in reversed(neg):self.add('X',q)

    def equality(self, x: list[int], y: list[int], target: int,
                 scratch: list[int]) -> None:
        b=scratch[:len(x)];anc=scratch[len(x):]
        for a,c,t in zip(x,y,b):self.add('CX',a,t);self.add('CX',c,t)
        self.conditioned([(q,0) for q in b],target,anc,kind='X')
        for a,c,t in reversed(list(zip(x,y,b))):self.add('CX',c,t);self.add('CX',a,t)

    def greater(self, x: list[int], y: list[int], target: int,
                scratch: list[int]) -> None:
        """Xor x>y into target and restore all scratch (five-bit words)."""
        if len(x)!=5 or len(y)!=5 or len(scratch)<9:raise ValueError('Expected five-bit words')
        b=scratch[:5];p=scratch[5:8];aux=scratch[8:]
        for a,c,t in zip(x,y,b):
            self.add('CX',a,t);self.add('CX',c,t);self.add('X',t)
        chain=[(b[4],b[3],p[0]),(p[0],b[2],p[1]),(p[1],b[1],p[2])]
        for g in chain:self.add('CCX',*g)
        prefix={3:b[4],2:p[0],1:p[1],0:p[2]}
        for j in range(4,-1,-1):
            controls=([(prefix[j],1)] if j<4 else [])+[(x[j],1),(y[j],0)]
            self.conditioned(controls,target,aux,kind='X')
        for g in reversed(chain):self.add('CCX',*g)
        for a,c,t in reversed(list(zip(x,y,b))):
            self.add('X',t);self.add('CX',c,t);self.add('CX',a,t)

    def helmert_step(self, register: list[int], k: int, control: int,
                     scratch: list[int]) -> None:
        """On levels 0,k apply [[sqrt(k/(k+1)),1/sqrt(k+1)],
        [1/sqrt(k+1),-sqrt(k/(k+1))]], conditioned on control=1.
        Gray conjugations map k to a one-bit word while leaving zero fixed.
        """
        if not 0<k<2**len(register):raise ValueError('Bad Helmert level')
        pivot=(k&-k).bit_length()-1
        current=k;path=[]
        for j in range(len(register)):
            if j!=pivot and (current>>j)&1:
                controls=[(control,1)]+[(register[l],(current>>l)&1)
                                                    for l in range(len(register)) if l!=j]
                self.conditioned(controls,register[j],scratch,kind='X')
                path.append((controls,register[j]));current^=1<<j
        controls=[(control,1)]+[(register[j],0) for j in range(len(register)) if j!=pivot]
        self.conditioned(controls,register[pivot],scratch,kind='Z')
        self.conditioned(controls,register[pivot],scratch,kind='Ry',
                         angle=2*math.asin(1/math.sqrt(k+1)))
        for controls,target in reversed(path):self.conditioned(controls,target,scratch,kind='X')


def build(*, bell_pairs: bool=True) -> Circuit:
    c=Circuit();x=list(range(5));y=list(range(5,10));diag=10;coin=11;scratch=list(range(12,21))
    c.equality(x,y,diag,scratch)
    # Controlled H = controlled Ry(pi/2) after controlled Z.
    c.conditioned([(diag,0)],coin,scratch,kind='Z')
    c.conditioned([(diag,0)],coin,scratch,kind='Ry',angle=math.pi/2)
    for a,b in zip(x,y):
        c.add('CX',a,b);c.add('CCX',coin,b,a);c.add('CX',a,b)
    c.greater(x,y,coin,scratch)  # erase which-order information coherently
    for a,b in zip(x,y):c.add('CCX',diag,a,b)
    # H_24=C_1 ... C_23 as a matrix, hence C_23 is applied first.
    for k in range(23,0,-1):c.helmert_step(x,k,diag,scratch)
    for a,b in zip(x,y):c.add('CCX',diag,a,b)
    c.equality(x,y,diag,scratch)
    if bell_pairs:
        for j in range(12):c.add('H',21+j);c.add('CX',21+j,33+j)
    return c


def inverse(c: Circuit) -> Circuit:
    out=Circuit()
    for g in reversed(c.gates):out.gates.append(g._replace(angle=-g.angle) if g.name=='Ry' else g)
    return out


def resource_report() -> dict:
    c=build()
    return {'gates':dict(sorted(Counter(g.name for g in c.gates).items())),
            'total_gates':len(c.gates),'total_wires':45,'output_wires':34,
            'clean_workspace_wires':11,'bell_pairs':12,'input_subspace_dimension':299,
            'basis_encoding':'(i,j), 0<=i<j<24; (k,k), 1<=k<24',
            'exact_angle_gate_library':['X','H','CX','CCX','Ry'],
            'amplitude_amplification_rounds':0,'postselection':False,
            'canonical_18_qubit_sector_packing_included':False,
            'full_Monster_isometry':False}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emit',action='store_true',help='Emit the full elementary-gate list as JSON')
    args=parser.parse_args()
    report=resource_report()
    if args.emit:report['circuit']=[g._asdict() for g in build().gates]
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':main()
