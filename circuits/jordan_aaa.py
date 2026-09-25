#!/usr/bin/env python3
"""Clean A0 -> A0 tensor A0 Jordan-adjoint circuit; not the full Monster W.

Native labels: (i,j), i<j<24, and (k,k), 1<=k<24, in two 5-bit words.
One exact ideal-angle amplification round implements the normalized map.
Uses a NEW all-input-clean basis extension. The historical seysen_qqa circuit
is preserved and must not be substituted for this extension off its domain.
Gate library X,H,CX,CCX,Ry; floating reference angles are not certified synthesis.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import json
import math
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import seysen_qqa as q

X = list(range(5))
Y = list(range(5, 10))
Z = list(range(10, 15))
T = list(range(15, 20))
FLAG, GT, V1, V2 = 20, 21, 22, 23
SCRATCH = list(range(24, 33))
N = 24


def append(c: q.Circuit, other: q.Circuit) -> None:
    c.gates.extend(other.gates)


def remap(c: q.Circuit, mapping: dict[int, int]) -> q.Circuit:
    out = q.Circuit()
    for g in c.gates:
        out.add(g.name, *(mapping[w] for w in g.wires), angle=g.angle)
    return out


def cswap(c: q.Circuit, control: int, x: list[int], y: list[int]) -> None:
    for a, b in zip(x, y):
        c.add('CX', a, b)
        c.add('CCX', control, b, a)
        c.add('CX', a, b)


def clean_basis() -> q.Circuit:
    """All 1024 coordinate inputs preserve zero workspace, not just 299 labels.

    Ascending inputs become symmetric pairs, descending inputs antisymmetric
    pairs. Diagonal inputs use the 24-level Helmert matrix, identity on 24..31.
    On valid labels this agrees in phase with the historical vectorization.
    """
    c = q.Circuit()
    x, y, diag, coin, scratch = X, Y, 10, 11, list(range(12, 21))
    c.equality(x, y, diag, scratch)
    c.greater(x, y, coin, scratch)
    cswap(c, coin, x, y)  # sort while preserving the orientation in coin
    c.conditioned([(diag, 0)], coin, scratch, kind='Z')
    c.conditioned([(diag, 0)], coin, scratch, kind='Ry', angle=math.pi/2)
    cswap(c, coin, x, y)  # unsort into the desired symmetric/antisymmetric state
    c.greater(x, y, coin, scratch)
    for a, b in zip(x, y):
        c.add('CCX', diag, a, b)
    for k in range(23, 0, -1):
        c.helmert_step(x, k, diag, scratch)
    for a, b in zip(x, y):
        c.add('CCX', diag, a, b)
    c.equality(x, y, diag, scratch)
    return c


def basis_on(x: list[int], y: list[int]) -> q.Circuit:
    mapping = dict(zip(range(21), x+y+[GT, V1]+SCRATCH))
    return remap(clean_basis(), mapping)


def valid_label(a: int, b: int) -> bool:
    return 0 <= a <= b < 24 and (a, b) != (0, 0)


def valid_labels() -> list[int]:
    return [a+(b << 5) for a in range(24) for b in range(a, 24)
            if valid_label(a, b)]


def predicate(x: list[int], y: list[int], target: int) -> q.Circuit:
    """Xor [x<=y<24 and (x,y)!=0] into target; every other wire is restored."""
    c = q.Circuit()
    c.greater(x, y, GT, SCRATCH)
    c.conditioned([(GT, 0)], target, SCRATCH, kind='X')
    c.conditioned([(GT, 0), (y[4], 1), (y[3], 1)], target, SCRATCH, kind='X')
    c.conditioned([(w, 0) for w in x+y], target, SCRATCH, kind='X')
    c.greater(x, y, GT, SCRATCH)
    return c


def mark(c: q.Circuit, controls: list[tuple[int, int]]) -> None:
    """Minus sign exactly on a computational subspace; no hidden global phase."""
    target, value = controls[-1]
    if value == 0:
        c.add('X', target)
    c.conditioned(controls[:-1], target, SCRATCH, kind='Z')
    if value == 0:
        c.add('X', target)


def bell() -> q.Circuit:
    """Prepare |Phi_24> on Z,T. Lower three bits are uniform; upper two avoid 11."""
    c = q.Circuit()
    for w in Z[:3]:
        c.add('H', w)
    c.add('Ry', Z[4], angle=2*math.asin(1/math.sqrt(3)))
    c.conditioned([(Z[4], 0)], Z[3], SCRATCH, kind='Ry', angle=math.pi/2)
    for a, b in zip(Z, T):
        c.add('CX', a, b)
    return c


def transfer(*, diluted: bool = True) -> q.Circuit:
    c = q.Circuit()
    append(c, basis_on(X, Y))
    append(c, bell())
    for a, b in zip(Y, Z):
        c.add('CX', a, b)
        c.add('CX', b, a)
        c.add('CX', a, b)
    append(c, q.inverse(basis_on(X, Y)))
    append(c, q.inverse(basis_on(Z, T)))
    if diluted:
        c.add('Ry', FLAG, angle=2*math.asin(math.sqrt(72/77)))
    return c


def source_reflection() -> q.Circuit:
    c = q.Circuit()
    mark(c, [(w, 0) for w in Z+T+[FLAG]])
    return c


def good_reflection() -> q.Circuit:
    c = q.Circuit()
    p1, p2 = predicate(X, Y, V1), predicate(Z, T, V2)
    append(c, p1)
    append(c, p2)
    mark(c, [(V1, 1), (V2, 1), (FLAG, 1)])
    append(c, q.inverse(p2))
    append(c, q.inverse(p1))
    return c


def build() -> q.Circuit:
    l = transfer()
    c = q.Circuit()
    for component in (l, good_reflection(), q.inverse(l), source_reflection(), l):
        append(c, component)
    # The implemented single Grover iterate is minus the standard one.
    # On the successful flag=1 subspace Z corrects that sign, then X clears it.
    c.add('H', FLAG)
    c.add('X', FLAG)
    c.add('H', FLAG)
    c.add('X', FLAG)
    return c


def counts(c: q.Circuit) -> dict[str, int]:
    return dict(sorted(Counter(g.name for g in c.gates).items()))


def report() -> dict:
    c = build()
    return {
        'source_base': 'c51e5ffaf06b90101c70df1d4f5347aa03b9cc14',
        'status': 'constructive ideal-angle Jordan branch; not full W',
        'input_dimension': len(valid_labels()),
        'source_contraction': str(Fraction(308, 3)),
        'undiluted_success_probability': str(Fraction(77, 288)),
        'dilution_probability': str(Fraction(72, 77)),
        'diluted_success_probability': '1/4',
        'amplification_rounds': 1,
        'transfer_calls': 3,
        'total_wires': 33,
        'output_wires': 20,
        'clean_zero_workspace_wires': 13,
        'branch_weight_in_W': '77/6929',
        'all_input_clean_basis': counts(clean_basis()),
        'bell_preparation': counts(bell()),
        'transfer': counts(transfer()),
        'source_reflection': counts(source_reflection()),
        'good_reflection': counts(good_reflection()),
        'total': counts(c),
        'total_instructions': len(c.gates),
        'measurements_or_postselection': False,
        'full_W': False,
        'finite_gate_set_synthesis': False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emit', action='store_true')
    args = parser.parse_args()
    result = report()
    if args.emit:
        result['circuit'] = [g._asdict() for g in build().gates]
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
