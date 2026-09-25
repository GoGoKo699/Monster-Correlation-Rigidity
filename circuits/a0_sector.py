#!/usr/bin/env python3
"""Constructive tagged A0-sector composition with every control/routing cost.

The plan references the immutable QQA/XXA generators and the new AAA emitter.
This prices a hierarchical ideal-angle circuit, not a full 105-wire simulation
or the complete 196883-input W. Output encoding: 2 sector bits + 18 payload bits
per register, i.e. 20 physical qubits per logical Griess register, not 18.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import argparse
import json
import math
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import seysen_qqa as q
import leech_xxa as x
import jordan_aaa as a

SOURCE = list(range(10))
EXTRA_COORD = list(range(10, 20))
SPIN1 = list(range(20, 32))
SPIN2 = list(range(32, 44))
WORK = list(range(44, 61))
OUT1 = list(range(61, 79))
TAG1 = [79, 80]
OUT2 = list(range(81, 99))
TAG2 = [99, 100]
SELECTOR = [101, 102]
CONTROL, CONTROL_SCRATCH = 103, 104
WEIGHTS = (77, 3780, 3072)


def lift_gate(c: q.Circuit, g: q.Gate, control: int, scratch: int) -> None:
    """Exact controlled lift; controlled-H includes its correct relative phase."""
    if control in g.wires or scratch in g.wires or control == scratch:
        raise ValueError('Overlapping lift wires')
    if g.name == 'X':
        c.add('CX', control, *g.wires)
    elif g.name == 'CX':
        c.add('CCX', control, *g.wires)
    elif g.name == 'CCX':
        u, v, t = g.wires
        c.add('CCX', u, v, scratch)
        c.add('CCX', control, scratch, t)
        c.add('CCX', u, v, scratch)
    elif g.name == 'H':
        t = g.wires[0]
        c.add('H', t)
        c.add('CX', control, t)
        c.add('H', t)
        c.add('Ry', t, angle=math.pi/4)
        c.add('CX', control, t)
        c.add('Ry', t, angle=-math.pi/4)
        c.add('CX', control, t)
    elif g.name == 'Ry':
        t = g.wires[0]
        c.add('Ry', t, angle=g.angle/2)
        c.add('CX', control, t)
        c.add('Ry', t, angle=-g.angle/2)
        c.add('CX', control, t)
    else:
        raise ValueError('Unsupported lifted gate')


def lift_counts(counts: dict[str, int]) -> Counter:
    b = Counter(counts)
    return Counter({'CCX': 3*b['CCX']+b['CX'],
                    'CX': b['X']+3*b['H']+2*b['Ry'],
                    'H': 2*b['H'], 'Ry': 2*b['H']+2*b['Ry']})


def selector_preparation() -> q.Circuit:
    c = q.Circuit()
    c.add('Ry', SELECTOR[1], angle=2*math.asin(math.sqrt(3072/6929)))
    c.conditioned([(SELECTOR[1], 0)], SELECTOR[0], [], kind='Ry',
                  angle=2*math.asin(math.sqrt(3780/(77+3780))))
    return c


def branch_marker(tag: int) -> q.Circuit:
    if tag not in (0, 1, 2):
        raise ValueError('Invalid branch')
    c = q.Circuit()
    c.conditioned([(w, (tag >> j) & 1) for j, w in enumerate(SELECTOR)],
                  CONTROL, [], kind='X')
    return c


def routing_pairs(tag: int) -> list[tuple[int, int]]:
    if tag == 0:
        return list(zip(SOURCE, OUT1[:10]))+list(zip(EXTRA_COORD, OUT2[:10]))
    if tag == 1:
        return []  # XXA outputs already occupy the common native payloads.
    if tag == 2:
        return (list(zip(SPIN1, OUT1[:12]))+list(zip(SOURCE[:5], OUT1[12:17]))+
                list(zip(SPIN2, OUT2[:12]))+list(zip(SOURCE[5:], OUT2[12:17])))
    raise ValueError('Invalid branch')


def routing(tag: int) -> q.Circuit:
    c = q.Circuit()
    for u, v in routing_pairs(tag):
        a.cswap(c, CONTROL, [u], [v])
    for j in range(2):
        if (tag >> j) & 1:
            c.add('CX', CONTROL, TAG1[j])
            c.add('CX', CONTROL, TAG2[j])
    return c


def selector_erasure() -> q.Circuit:
    c = q.Circuit()
    for u, v in zip(TAG1, SELECTOR):
        c.add('CX', u, v)
    return c


def wire_maps() -> dict[str, dict[int, int]]:
    aaa = dict(zip(range(20), SOURCE+EXTRA_COORD))
    aaa.update(dict(zip(range(20, 33), WORK[:13])))
    qqa = dict(zip(range(10), SOURCE))
    qqa.update(dict(zip(range(10, 21), WORK[:11])))
    qqa.update(dict(zip(range(21, 45), SPIN1+SPIN2)))
    xxa = dict(zip(range(10), SOURCE))
    xxa.update(dict(zip(range(10, 27), WORK)))
    xxa.update(dict(zip(range(27, 45), OUT1)))
    xxa.update(dict(zip(range(45, 63), OUT2)))
    return {'AAA': aaa, 'XXA': xxa, 'QQA': qqa}


@lru_cache(None)
def branch_counts() -> dict[str, dict[str, int]]:
    return {'AAA': a.report()['total'], 'XXA': x.report()['total'],
            'QQA': q.resource_report()['gates']}


def report() -> dict:
    total = Counter(a.counts(selector_preparation()))
    control_overhead = Counter(total)
    for tag, name in enumerate(('AAA', 'XXA', 'QQA')):
        total += lift_counts(branch_counts()[name])
        overhead = Counter(a.counts(branch_marker(tag)))
        overhead.update(a.counts(branch_marker(tag)))
        overhead.update(a.counts(routing(tag)))
        total += overhead
        control_overhead += overhead
    total.update(a.counts(selector_erasure()))
    control_overhead.update(a.counts(selector_erasure()))
    return {
        'status': 'constructive tagged A0-sector ideal-angle budget; not full W',
        'source_base': 'c51e5ffaf06b90101c70df1d4f5347aa03b9cc14',
        'input_dimension': 299,
        'full_input_dimension': 196883,
        'sector_dimensions': {'A0': 299, 'X': 98280, 'Q': 98304},
        'branch_weights': ['77/6929', '3780/6929', '3072/6929'],
        'physical_qubits_per_output_register': 20,
        'total_wires': 105, 'output_wires': 40, 'clean_zero_workspace_wires': 65,
        'uncontrolled_branch_counts': branch_counts(),
        'controlled_branch_counts': {k: dict(sorted(lift_counts(v).items()))
                                     for k, v in branch_counts().items()},
        'selector_routing_tag_erasure_overhead': dict(sorted(control_overhead.items())),
        'total': dict(sorted(total.items())),
        'total_instructions': sum(total.values()),
        'controlled_H_relative_phase_retained': True,
        'all_A0_output_branches_combined': True,
        'full_W': False, 'full_circuit_simulated': False,
        'canonical_18_qubit_packing': False,
        'finite_gate_set_synthesis': False,
        'measurements_or_postselection': False,
    }


def plan() -> dict:
    branches = []
    for tag, name in enumerate(('AAA', 'XXA', 'QQA')):
        branches.append({'tag': tag, 'component': name,
            'chronological_operations': ['compute_selector_match_into_control',
                'apply_elementwise_controlled_mapped_component',
                'controlled_route_to_common_payloads_and_set_tags',
                'uncompute_selector_match'],
            'routing_pairs': routing_pairs(tag)})
    return {
        'chronological_operations': ['selector_preparation', branches, 'selector_erasure'],
        'component_definitions': {
            'AAA': 'jordan_aaa.build()',
            'QQA': 'seysen_qqa.build(bell_pairs=True)',
            'XXA': 'leech_xxa.plan(), with J=seysen_qqa.build(bell_pairs=False)'
        },
        'XXA_completion_details': {
            'L': 'emit_uniform; inverse emit_row on X; inverse emit_row on Y; '
                 'Ry on flag by 2*asin(sqrt(312)*sin(pi/58))',
            'inverse': 'reverse elementary order and negate every Ry angle',
            'phase_predicates': 'leech_xxa.emit_source_reflection and emit_good_reflection',
            'final': 'X on flag, then 18 label-copy CNOTs',
        },
        'wire_maps': wire_maps(),
        'control_lift': 'lift_gate for every mapped X,H,CX,CCX,Ry instruction',
        'control_wire': CONTROL, 'control_scratch': CONTROL_SCRATCH,
        'branch_relative_signs': [1, 1, 1],
        'native_output_encoding': {
            'tag0_A0': 'payload=(i+32*j) in low 10 bits; i<j<24 or 1<=i=j<24',
            'tag1_X': 'payload is the complete 18-bit leech_xxa native label',
            'tag2_Q': 'payload=s+4096*i with s<4096 and i<24; bit17=0',
            'tag3': 'invalid logical sector'
        },
        'initial_nonzero_register': SOURCE,
        'initial_other_wires': 'zero',
        'output_payloads': [OUT1, OUT2], 'output_tags': [TAG1, TAG2],
        'final_other_wires': 'zero on every valid coherent A0 input',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', action='store_true')
    args = parser.parse_args()
    print(json.dumps(plan() if args.plan else report(), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
