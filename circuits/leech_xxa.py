#!/usr/bin/env python3
"""A clean Leech quadratic-form encoding by a frame block and exact amplification.

Native label: two tag bits followed by 16 payload bits, little endian.
Tags 0/1/2 select pair/octad/Golay shapes. No QRAM or arbitrary-matrix oracle.
This is NOT a complete Griess W circuit. See research/08_leech_xxa_block.md.
Default: exact instruction counts for the finite reference compiler.
--emit-row: stream the full controlled single-row loader's elementary gates.
--plan: emit the hierarchical complete circuit (components remain reusable).
Angles use floats for reference only, not certified finite-gate-set synthesis.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from itertools import combinations
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import seysen_qqa as q

N=98280
COUNTS=(552,48576,49152)
COORD_X=list(range(5)); COORD_Y=list(range(5,10))
FLAG=10; SCRATCH=list(range(11,27)); LABEL=list(range(27,45)); OUT2=list(range(45,63))
TAG=LABEL[:2]; DATA=LABEL[2:]
PAIRS=tuple(combinations(range(24),2))
GENERATOR=sum(1<<i for i in (11,9,7,6,5,1,0))

@lru_cache(None)
def golay_basis() -> tuple[int,...]:
    out=[]
    for j in range(12):
        w=GENERATOR<<j
        out.append(w|((w.bit_count()&1)<<23))
    return tuple(out)

def codeword(message: int) -> int:
    if not 0<=message<4096: raise ValueError('Golay message must fit 12 bits')
    w=0
    for j,g in enumerate(golay_basis()):
        if message>>j&1:w^=g
    return w

@lru_cache(None)
def octads() -> tuple[int,...]:
    return tuple(sorted(codeword(j) for j in range(4096) if codeword(j).bit_count()==8))

@lru_cache(None)
def supports() -> tuple[tuple[int,...],...]:
    return tuple(tuple(i for i in range(24) if w>>i&1) for w in octads())

def label(tag:int,index:int,sign:int=0) -> int:
    if tag==0:
        if not (0<=index<276 and 0<=sign<2): raise ValueError('Pair label')
        payload=index|(sign<<9)
    elif tag==1:
        if not (0<=index<759 and 0<=sign<64): raise ValueError('Octad label')
        payload=index|(sign<<10)
    elif tag==2:
        if not (0<=index<24 and 0<=sign<2048): raise ValueError('Golay label')
        payload=index|(sign<<5)
    else:raise ValueError('Invalid tag')
    return tag|(payload<<2)

def decode(r:int) -> tuple[int,int,int]:
    if not 0<=r<2**18:raise ValueError('Label must fit 18 bits')
    tag=r&3;p=r>>2
    if tag==0:
        i=p&511;s=(p>>9)&1
        if p>>10 or i>=276:raise ValueError('Invalid pair payload')
    elif tag==1:
        i=p&1023;s=p>>10
        if i>=759:raise ValueError('Invalid octad payload')
    elif tag==2:
        i=p&31;s=p>>5
        if i>=24:raise ValueError('Invalid Golay payload')
    else:raise ValueError('Invalid tag')
    return tag,i,s

def labels():
    for tag,ni,ns in ((0,276,2),(1,759,64),(2,24,2048)):
        for i in range(ni):
            for s in range(ns):yield label(tag,i,s)

def integer_row(r:int) -> tuple[int,...]:
    """The physical Leech vector is this row divided by sqrt(8)."""
    tag,k,s=decode(r);v=[0]*24
    if tag==0:
        i,j=PAIRS[k];v[i]=4;v[j]=4*(-1 if s else 1)
    elif tag==1:
        supp=supports()[k];signs=[0]+[(s>>j)&1 for j in range(6)]+[s.bit_count()&1]
        for i,b in zip(supp,signs):v[i]=-2 if b else 2
    else:
        # The eleven generator rows j>=1 have bit 0 zero. This selects
        # exactly one representative of each codeword/complement pair.
        w=codeword(s<<1)
        v=[(-3 if i==k else 1)*(-1 if w>>i&1 else 1) for i in range(24)]
    return tuple(v)

def pattern(wires:list[int],value:int):return [(w,(value>>j)&1) for j,w in enumerate(wires)]

def prep_nodes(weights:tuple[int,...]):
    """Yield (prefix pattern in bit positions,target,angle) for |sqrt(w/sum w)>.

    At each binary prefix rotate its next zero input bit. Zero prefixes are
    skipped. Angles are exact mathematical 2 atan2(sqrt(right),sqrt(left)).
    """
    size=len(weights)
    if size==0 or size&(size-1) or any(x<0 for x in weights) or not sum(weights):
        raise ValueError('Nonnegative power-of-two weight array required')
    n=size.bit_length()-1
    def walk(lo:int,hi:int,prefix:list[tuple[int,int]]):
        if hi-lo==1:return
        mid=(lo+hi)//2;left=sum(weights[lo:mid]);right=sum(weights[mid:hi]);target=(hi-lo).bit_length()-2
        if not left and not right:return
        if right:yield prefix,target,2*math.atan2(math.sqrt(right),math.sqrt(left))
        yield from walk(lo,mid,prefix+[(target,0)])
        yield from walk(mid,hi,prefix+[(target,1)])
    yield from walk(0,size,[])

class Sink(q.Circuit):
    """Use the prior explicit elementary decompositions without storing millions of gates."""
    def __init__(self,*,store=False,stream=False):
        super().__init__();self.counts=Counter();self.store=store;self.stream=stream
    def add(self,name,*wires,angle=None):
        if len(set(wires))!=len(wires):raise ValueError('Repeated wire')
        if any(w<0 or w>=63 for w in wires):raise ValueError('Wire outside interface')
        if name=='Ry' and (angle is None or not math.isfinite(angle)):raise ValueError('Bad angle')
        g=q.Gate(name,tuple(wires),angle);self.counts[name]+=1
        if self.store:self.gates.append(g)
        if self.stream:print(json.dumps(g._asdict(),separators=(',',':')))

def controlled_prep(c:Sink,register:list[int],weights,controls):
    for prefix,t,angle in prep_nodes(tuple(weights)):
        cs=controls+[(register[j],b) for j,b in prefix]
        c.conditioned(cs,register[t],SCRATCH,kind='Ry',angle=angle)

def mark(c:Sink,controls):
    """Multiply the matching computational subspace by -1."""
    if not controls:raise ValueError('Nonempty phase condition required')
    target,b=controls[-1]
    if b==0:c.add('X',target)
    c.conditioned(controls[:-1],target,SCRATCH,kind='Z')
    if b==0:c.add('X',target)

def row_description():
    """Static unsigned rows, followed by linear sign phases; no 98280-row ROM."""
    for k,(i,j) in enumerate(PAIRS):
        w=[0]*32;w[i]=w[j]=16
        yield ('prepare',pattern(TAG,0)+pattern(DATA[:9],k),tuple(w))
    for k,supp in enumerate(supports()):
        w=[0]*32
        for i in supp:w[i]=4
        yield ('prepare',pattern(TAG,1)+pattern(DATA[:10],k),tuple(w))
    for k in range(24):
        w=[1]*24+[0]*8;w[k]=9
        yield ('prepare',pattern(TAG,2)+pattern(DATA[:5],k),tuple(w))
    for k,(_,j) in enumerate(PAIRS):
        yield ('phase',pattern(TAG,0)+pattern(DATA[:9],k)+[(DATA[9],1)],j)
    for k,supp in enumerate(supports()):
        for j in range(6):
            cs=pattern(TAG,1)+pattern(DATA[:10],k)+[(DATA[10+j],1)]
            yield ('phase',cs,supp[j+1]);yield ('phase',cs,supp[7])
    for k in range(24):yield ('phase',pattern(TAG,2)+pattern(DATA[:5],k),k)
    for j,g in enumerate(golay_basis()[1:]):
        for i in range(24):
            if g>>i&1:yield ('phase',pattern(TAG,2)+[(DATA[5+j],1)],i)

def emit_row(c:Sink,register=COORD_X,*,specialize_label:int|None=None):
    values={w:(specialize_label>>j)&1 for j,w in enumerate(LABEL)} if specialize_label is not None else None
    for kind,controls,data in row_description():
        if values is not None:
            if any(values[w]!=v for w,v in controls):continue
            controls=[]  # exact specialization of constant label controls
        if kind=='prepare':controlled_prep(c,register,data,controls)
        else:mark(c,controls+pattern(register,data))

def emit_uniform(c:Sink):
    controlled_prep(c,TAG,COUNTS+(0,),[])
    for tag,rankbits,limit,free in ((0,9,276,[9]),(1,10,759,list(range(10,16))),(2,5,24,list(range(5,16)))):
        cs=pattern(TAG,tag)
        controlled_prep(c,DATA[:rankbits],[1]*limit+[0]*(2**rankbits-limit),cs)
        for j in free:
            # H=Ry(pi/2) Z, so time order is Z followed by Ry.
            c.conditioned(cs,DATA[j],SCRATCH,kind='Z')
            c.conditioned(cs,DATA[j],SCRATCH,kind='Ry',angle=math.pi/2)

def emit_source_reflection(c:Sink):mark(c,pattern(LABEL,0)+[(FLAG,0)])
def emit_good_reflection(c:Sink):mark(c,pattern(COORD_X+COORD_Y,0)+[(FLAG,1)])

def scale(c,n):return Counter({k:v*n for k,v in c.items()})

def report():
    row=Sink();emit_row(row)
    uniform=Sink();emit_uniform(uniform)
    source=Sink();emit_source_reflection(source)
    good=Sink();emit_good_reflection(good)
    j=q.build(bell_pairs=False);jc=Counter(g.name for g in j.gates)
    lc=scale(row.counts,2)+uniform.counts+Counter({'Ry':1})
    total=jc+scale(lc,29)+scale(source.counts,14)+scale(good.counts,14)+Counter({'CX':18,'X':1})
    return {'status':'constructive ideal-angle circuit budget, not full W',
      'source_base':'5428fffc82ccd1ede8a4203b1e73acb6816de289',
      'label_bits':18,'valid_label_count':N,'input_dimension':299,
      'total_wires':63,'output_wires':36,'clean_zero_workspace_wires':27,
      'undiluted_success_probability':'1/312','amplification_rounds':14,
      'L_forward_calls':15,'L_inverse_calls':14,'controlled_row_loader_calls':58,
      'dilution_amplitude_expression':'sqrt(312)*sin(pi/58)',
      'normalized_branch_weight_in_W':'3780/6929',
      'row_loader':dict(sorted(row.counts.items())),
      'uniform_loader':dict(sorted(uniform.counts.items())),
      'source_reflection':dict(sorted(source.counts.items())),
      'good_reflection':dict(sorted(good.counts.items())),
      'vectorization':dict(sorted(jc.items())),
      'L':dict(sorted(lc.items())),
      'total':dict(sorted(total.items())), 'total_instructions':sum(total.values()),
      'oracle_calls_to_unknown_U':0,'QRAM':False,'measurements_or_postselection':False,
      'full_W':False,'finite_gate_set_synthesis':False,'canonical_sector_packing':False}

def plan():
    # Lists chronological operations; inverse components reverse gates/angles.
    ops=['J','L']
    for _ in range(14):ops+=['S_good','L_inverse','S_source','L']
    return {'time_order':ops+['X_on_flag','copy_label_18_CNOT'],
      'L_time_order':['uniform_label','row_loader_X_inverse','row_loader_Y_inverse','Ry_flag_dilution'],
      'row_source':'emit_row', 'uniform_source':'emit_uniform',
      'inverse_rule':'reverse order; negate Ry angles; other gates are self-inverse',
      'reflection_sign':'implemented iterate differs by minus sign from standard Grover; 14 rounds cancel it',
      'J_source':'seysen_qqa.build(bell_pairs=False)',
      'all_wires_defined':{'x':COORD_X,'y':COORD_Y,'flag':FLAG,'scratch':SCRATCH,'label':LABEL,'second_label':OUT2}}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--emit-row',action='store_true');p.add_argument('--plan',action='store_true')
    args=p.parse_args()
    if args.emit_row:emit_row(Sink(stream=True))
    else:print(json.dumps(plan() if args.plan else report(),sort_keys=True,indent=2))

if __name__=='__main__':main()
