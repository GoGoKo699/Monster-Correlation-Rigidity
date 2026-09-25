#!/usr/bin/env python3
"""Exact label/frame arithmetic, small gate checks and high-rank amplification.

Not a simulation of the full 63-wire circuit or of the full Monster tensor.
All 98280 length-24 Leech rows are checked in bounded memory. No N x 299
encoding matrix is formed. Largest dense operator is 32 x 32; a 1024-entry
state vector checks uniform-rank preparation. Reports omit unstable residuals.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'circuits'))
import leech_xxa as l
import seysen_qqa as q
LABELS=[];TOL=1e-10


def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    LABELS.append(label)

def close(a,b,label,tol=TOL):need(np.linalg.norm(np.asarray(a)-np.asarray(b))<tol,label)

def state_distance(a,b):return math.sqrt(sum(abs(a.get(k,0)-b.get(k,0))**2 for k in a.keys()|b.keys()))

def simulate(c,initial):
    state=dict(initial);pruned=0.
    for g in c.gates:
        if g.name in ('X','CX','CCX'):
            cs=sum(1<<w for w in g.wires[:-1]);t=1<<g.wires[-1]
            state={(k^t if k&cs==cs else k):v for k,v in state.items()}
        else:
            bit=1<<g.wires[0];out={}
            if g.name=='H':a=b=cc=1/math.sqrt(2);d=-a
            elif g.name=='Ry':a=d=math.cos(g.angle/2);cc=math.sin(g.angle/2);b=-cc
            else:raise RuntimeError('Unknown instruction')
            for k,v in state.items():
                if k&bit:out[k^bit]=out.get(k^bit,0)+b*v;out[k]=out.get(k,0)+d*v
                else:out[k]=out.get(k,0)+a*v;out[k^bit]=out.get(k^bit,0)+cc*v
            small=[k for k,v in out.items() if abs(v)<1e-14]
            pruned+=math.sqrt(sum(abs(out[k])**2 for k in small))
            for k in small:del out[k]
            state=out
    if pruned>1e-11:raise RuntimeError('Pruning budget exceeded')
    return state


def rows_and_moments():
    labels=list(l.labels());need(len(set(labels))==l.N,'labels:98280_distinct_valid_labels')
    need(all(l.label(*l.decode(r))==r for r in labels),'labels:encode_decode_roundtrip_all')
    code={l.codeword(j) for j in range(4096)}
    need(len(code)==4096 and Counter(x.bit_count() for x in code)=={0:1,8:759,12:2576,16:759,24:1},'Golay:full_weight_distribution')
    representatives={l.codeword(j<<1) for j in range(2048)}
    full=(1<<24)-1
    need(len(representatives)==2048 and all(not w&1 for w in representatives),'Golay:c0_zero_transversal')
    need(representatives|{w^full for w in representatives}==code,'Golay:transversal_and_complement_cover')
    seen=set();shapes=Counter();hasher=hashlib.sha256();xx=np.zeros((24,24),dtype=np.int64)
    dd=np.zeros(24,dtype=np.int64);cc=np.zeros((24,24),dtype=np.int64)
    # Exact contracted moments on six rational test matrices are formed as
    # sums of (a^T A a) aa^T. The largest accumulator is 24 x 24.
    matrices=[]
    h=np.zeros((24,24),dtype=np.int64);h[0,0]=1;h[1,1]=-1;matrices.append(h)
    f=np.zeros_like(h);f[2,5]=f[5,2]=1;matrices.append(f)
    matrices.append(np.eye(24,dtype=np.int64))
    rng=np.random.default_rng(871)
    for _ in range(2):
        a=rng.integers(-2,3,size=(24,24),dtype=np.int64);a=a+a.T
        a[0,0]-=np.trace(a);matrices.append(a)
    totals=[np.zeros_like(h) for _ in matrices]
    lattice_ok=norm_ok=True
    for start in range(0,l.N,1024):
        rr=labels[start:start+1024]
        block=[]
        for r in rr:
            a=l.integer_row(r);tag,_,_=l.decode(r);shapes[tag]+=1
            norm_ok &= sum(x*x for x in a)==32
            canonical=a if next(x for x in a if x)>0 else tuple(-x for x in a)
            seen.add(canonical);hasher.update(r.to_bytes(3,'little')+bytes(x+4 for x in a))
            lattice_ok &= all((sum(a)-4*x)%8==0 for x in a)
            # Source's Golay congruence description of the lattice.
            for residue in range(4):
                word=sum(1<<j for j,x in enumerate(a) if x%4==residue)
                lattice_ok &= word in code
            block.append(a)
        a=np.array(block,dtype=np.int64);sq=a*a
        xx+=a.T@a;dd+=np.sum(sq*sq,axis=0);cc+=sq.T@sq
        for matrix,total in zip(matrices,totals):
            quadratic=np.einsum('bi,ij,bj->b',a,matrix,a,optimize=True)
            total+=a.T@(quadratic[:,None]*a)
    need(norm_ok,'Leech:all_integer_squared_norms_32')
    need(lattice_ok,'Leech:all_lattice_congruences_and_Golay_residue_words')
    need(len(seen)==l.N,'Leech:unique_up_to_antipode_all_rows')
    need(shapes==dict(enumerate(l.COUNTS)),'Leech:three_shape_counts')
    need(np.array_equal(xx,np.eye(24,dtype=np.int64)*131040),'moments:second_exact')
    need(np.all(dd==7560*64),'moments:diagonal_fourth_exact')
    target=np.full((24,24),2520*64,dtype=np.int64);np.fill_diagonal(target,7560*64)
    need(np.array_equal(cc,target),'moments:mixed_even_fourth_exact')
    for j,(matrix,total) in enumerate(zip(matrices,totals)):
        expected=64*2520*(2*matrix+np.trace(matrix)*np.eye(24,dtype=np.int64))
        need(np.array_equal(total,expected),f'moments:contracted_fourth_matrix_{j}')
    # Proof of all odd-degree sign cancellations is structural, from minimum
    # dual distance and the parity sign subgroup, not these finitely many matrices.
    need(F(5040,16*l.N)==F(1,312),'frame:undiluted_singular_value_squared')
    need(F(2,24*26)==F(1,312),'frame:real_fourth_moment_general_formula')
    need(F(1,24)==13*F(1,312),'frame:trace_mode_is_different')
    need(299*F(1,312)+F(1,24)==1,'frame:spectrum_trace_one')
    for tag,ni,ns in ((0,276,2),(1,759,64),(2,24,2048)):
        need(F(l.COUNTS[tag],l.N)*F(1,ni)*F(1,ns)==F(1,l.N),f'uniform:exact_shape_probability_{tag}')
    return hasher.hexdigest()


def tree_state(weights):
    out=np.zeros(len(weights));out[0]=1.
    for prefix,t,angle in l.prep_nodes(tuple(weights)):
        c=math.cos(angle/2);s=math.sin(angle/2)
        for i in range(len(weights)):
            if i>>t&1 or any((i>>j&1)!=v for j,v in prefix):continue
            k=i^(1<<t);x,y=out[i],out[k];out[i]=c*x-s*y;out[k]=s*x+c*y
    return out


def gate_checks():
    need(len(tuple(l.row_description()))==1059+276+759*12+24+sum(g.bit_count() for g in l.golay_basis()[1:]),'compiler:unsigned_templates_and_linear_phase_terms')
    prep_specs=[data for kind,_,data in l.row_description() if kind=='prepare']
    maximum=0.
    for weights in prep_specs:
        v=tree_state(weights);expected=np.sqrt(np.array(weights)/sum(weights))
        maximum=max(maximum,float(np.linalg.norm(v-expected)))
    need(maximum<TOL,'loader:all_1059_unsigned_row_preparation_trees')
    for bits,n in ((9,276),(10,759),(5,24)):
        out=tree_state([1]*n+[0]*(2**bits-n))
        expected=np.zeros(2**bits);expected[:n]=1/math.sqrt(n)
        close(out,expected,f'loader:uniform_rank_{n}')
    close(tree_state(l.COUNTS+(0,)),np.sqrt(np.array(l.COUNTS+(0,))/l.N),'loader:shape_amplitudes')
    selections=[l.label(0,i,s) for i in (0,111,275) for s in (0,1)]
    selections += [l.label(1,i,s) for i in (0,379,758) for s in (0,1,37,63)]
    selections += [l.label(2,i,s) for i in (0,7,23) for s in (0,1,1019,2047)]
    for r in selections:
        c=l.Sink(store=True);l.emit_row(c,specialize_label=r)
        expected={i:x/math.sqrt(32) for i,x in enumerate(l.integer_row(r)) if x}
        actual=simulate(c,{0:1.})
        if state_distance(actual,expected)>=TOL:raise RuntimeError('Specialized row '+str(r))
        if state_distance(simulate(q.inverse(c),actual),{0:1.})>=TOL:raise RuntimeError('Row inverse')
        if any(k>>5 for k in actual):raise RuntimeError('Dirty row workspace')
    need(True,'loader:30_signed_specialized_elementary_circuits_and_inverses')
    for r in (l.label(0,21,1),l.label(1,153,37),l.label(2,7,1019)):
        c=l.Sink(store=True);l.emit_row(c,l.COORD_X,specialize_label=r);l.emit_row(c,l.COORD_Y,specialize_label=r)
        v=l.integer_row(r);expected={i+(j<<5):x*y/32 for i,x in enumerate(v) for j,y in enumerate(v) if x*y}
        actual=simulate(c,{0:1.})
        if state_distance(actual,expected)>=TOL:raise RuntimeError('Tensor-square row')
        if state_distance(simulate(q.inverse(c),actual),{0:1.})>=TOL:raise RuntimeError('Tensor-square inverse')
    need(True,'loader:three_tensor_square_circuits_and_clean_inverses')
    # A large conjunction is tested both on and off its marked subspace,
    # with a coherent control superposition. It uses at most four amplitudes.
    controls=list(range(27,44));target=0;yes=sum(1<<w for w in controls);no=yes^(1<<controls[3])
    c=l.Sink(store=True);c.conditioned([(w,1) for w in controls],target,l.SCRATCH,kind='Ry',angle=.71)
    actual=simulate(c,{yes:1/math.sqrt(2),no:1/math.sqrt(2)})
    expected={yes:math.cos(.71/2)/math.sqrt(2),yes|1:math.sin(.71/2)/math.sqrt(2),no:1/math.sqrt(2)}
    need(state_distance(actual,expected)<TOL,'loader:17_control_rotation_and_coherent_scratch_erasure')
    for emitter,marked,unmarked,name in ((l.emit_source_reflection,0,1<<l.LABEL[0],'source'),
        (l.emit_good_reflection,1<<l.FLAG,(1<<l.FLAG)|1,'good')):
        c=l.Sink(store=True);emitter(c)
        actual=simulate(c,{marked:1/math.sqrt(2),unmarked:1/math.sqrt(2)})
        need(state_distance(actual,{marked:-1/math.sqrt(2),unmarked:1/math.sqrt(2)})<TOL,f'reflection:{name}_elementary_phase_and_scratch')


def amplification_checks():
    beta=math.pi/58;dilution=math.sqrt(312)*math.sin(beta)
    need(0<dilution<1,'amplification:dilution_is_valid_rotation')
    need(math.ceil(math.pi/(4*math.asin(1/math.sqrt(312)))-.5)==14,'amplification:14_round_selection')
    close(29*beta,math.pi/2,'amplification:exact_target_angle')
    # Rank-three source/target, with independent complex basis changes and
    # complementary modes. This checks the higher-rank, not rank-one, formula.
    rng=np.random.default_rng(452)
    v,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
    w,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
    s=math.sin(beta);c=math.cos(beta);zero=np.zeros((3,3));eye=np.eye(3)
    rotation=np.block([[s*eye,-c*eye],[c*eye,s*eye]])
    b=np.block([[v,zero],[zero,w]])@rotation
    p=np.diag([1.]*3+[0.]*3);sf=np.eye(6)-2*p
    transformed=b@p
    for _ in range(14):transformed=b@sf@b.conj().T@sf@transformed
    close(transformed,np.block([[v,zero],[zero,zero]]),'amplification:rank_three_unknown_input_map')
    close(transformed.conj().T@transformed,p,'amplification:coherence_and_isometry')
    close(np.linalg.matrix_power(b@sf@b.conj().T@sf,14)@b@p,transformed,'amplification:time_order_and_even_global_phase')
    source=rng.normal(size=3)+1j*rng.normal(size=3);source/=np.linalg.norm(source)
    close(transformed@np.r_[source,np.zeros(3)],np.r_[v@source,np.zeros(3)],'amplification:complex_superposition')
    # A nonflat column has a different rotation angle and is not corrected.
    trace_prob=math.sin(29*math.asin(dilution/math.sqrt(24)))**2
    need(abs(trace_prob-1)>.1,'negative_control:trace_direction_not_compiled_as_A0')
    # Retaining which-column information turns a coherent sum into a mixture.
    desired=np.array([1,1])/math.sqrt(2)
    rho_wrong=np.diag([.5,.5])
    close(desired@rho_wrong@desired,.5,'negative_control:retained_input_label_destroys_coherence')


def resources():
    r=l.report();plan=l.plan()['time_order']
    need(plan.count('L')==15 and plan.count('L_inverse')==14,'resources:29_full_transfer_calls')
    need(plan.count('S_source')==plan.count('S_good')==14,'resources:28_reflections')
    need(r['total']=={'CCX':33936255,'CX':1298699,'H':1102684,'Ry':1298668,'X':19712995},'resources:reference_instruction_counts')
    need(r['total_instructions']==57349301,'resources:57349301_total')
    need(r['output_wires']+r['clean_zero_workspace_wires']==r['total_wires']==63,'resources:63_wire_interface')
    need(F(3780,6929)+F(3072,6929)+F(77,6929)==1,'resources:branch_weight_not_success_probability')
    need((ROOT/'results/leech_xxa_resources.json').read_text()==json.dumps(r,sort_keys=True,indent=2)+'\n','resources:recorded_report_exact')
    return r


def main():
    digest=rows_and_moments();gate_checks();amplification_checks();r=resources()
    print(json.dumps({'status':'PASS within stated frame/primitive scopes','checks':len(LABELS),'labels':LABELS,
      'all_Leech_rows_checked':98280,'rows_are_Monster_axes':False,'label_row_sha256':digest,
      'largest_dense_operator_dimension':32,'largest_dense_state_vector_length':1024,
      'largest_row_batch_shape':[1024,24],'reference_circuit_instructions':r['total_instructions'],
      'full_63_wire_circuit_simulated':False,'full_Monster_tensor_constructed':False,
      'specialized_row_circuits_tested':30,'floating_tolerance':TOL,'precision_certified_at_1e_12':False,
      'novelty_established':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
