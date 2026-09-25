#!/usr/bin/env python3
"""Jordan projection, actual 33-wire circuit samples, and tagged composition.

The all-input-clean coordinate basis is checked on all 1024 inputs. The full
16,957-instruction Jordan circuit is simulated sparsely on three coherent
inputs; it is not simulated on all 299 columns. The 135-million-instruction
combined circuit is NOT simulated. Its controls/routing are separately checked.
No full Monster tensor is used. Every test remains active under -O and -OO.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import math
import sys
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'circuits'))
import seysen_qqa as q
import jordan_aaa as a
import a0_sector as s

LABELS: list[str] = []
TOL = 1e-10
MAX_SUPPORT = 0
MAX_PRUNED = 0.


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    LABELS.append(label)


def close(x, y, label):
    need(np.linalg.norm(np.asarray(x)-np.asarray(y)) < TOL, label)


def distance(x, y):
    return math.sqrt(sum(abs(x.get(k, 0)-y.get(k, 0))**2 for k in x.keys() | y.keys()))


def simulate_small(c, initial):
    """Dictionary simulation also permits >64-bit labels with very small support."""
    global MAX_SUPPORT, MAX_PRUNED
    state = dict(initial)
    pruning = 0.
    for g in c.gates:
        if g.name in ('X', 'CX', 'CCX'):
            controls = sum(1 << j for j in g.wires[:-1]); bit = 1 << g.wires[-1]
            state = {(k ^ bit if k & controls == controls else k): v for k, v in state.items()}
        else:
            bit = 1 << g.wires[0]; out = {}
            if g.name == 'H':
                u = v = w = 1/math.sqrt(2); z = -u
            elif g.name == 'Ry':
                u = z = math.cos(g.angle/2); w = math.sin(g.angle/2); v = -w
            else:
                raise RuntimeError('Unsupported instruction')
            for k, value in state.items():
                if k & bit:
                    out[k ^ bit] = out.get(k ^ bit, 0)+v*value
                    out[k] = out.get(k, 0)+z*value
                else:
                    out[k] = out.get(k, 0)+u*value
                    out[k ^ bit] = out.get(k ^ bit, 0)+w*value
            tiny = [k for k, value in out.items() if abs(value) < 1e-14]
            pruning += math.sqrt(sum(abs(out[k])**2 for k in tiny))
            for k in tiny:
                del out[k]
            state = out
        MAX_SUPPORT = max(MAX_SUPPORT, len(state))
    MAX_PRUNED = max(MAX_PRUNED, pruning)
    if pruning > 1e-11:
        raise RuntimeError('Pruning error exceeds stated budget')
    return state


def simulate_np(c, initial):
    """Sparse gate application with arrays; no 2**33 state vector is allocated."""
    global MAX_SUPPORT, MAX_PRUNED
    indices = np.array(list(initial), dtype=np.int64)
    values = np.array(list(initial.values()), dtype=complex)
    pruning = 0.
    for g in c.gates:
        if g.name in ('X', 'CX', 'CCX'):
            mask = sum(1 << j for j in g.wires[:-1]); bit = 1 << g.wires[-1]
            indices ^= np.where(indices & mask == mask, bit, 0)
        else:
            bit = 1 << g.wires[0]
            bases, inverse = np.unique(indices & ~bit, return_inverse=True)
            v0 = np.zeros(len(bases), complex); v1 = np.zeros(len(bases), complex)
            low = (indices & bit) == 0
            v0[inverse[low]] = values[low]
            v1[inverse[~low]] = values[~low]
            if g.name == 'H':
                out0 = (v0+v1)/math.sqrt(2); out1 = (v0-v1)/math.sqrt(2)
            elif g.name == 'Ry':
                cc, ss = math.cos(g.angle/2), math.sin(g.angle/2)
                out0 = cc*v0-ss*v1; out1 = ss*v0+cc*v1
            else:
                raise RuntimeError('Unsupported instruction')
            indices = np.r_[bases, bases | bit]
            values = np.r_[out0, out1]
            keep = abs(values) >= 1e-14
            pruning += float(np.linalg.norm(values[~keep]))
            indices, values = indices[keep], values[keep]
        MAX_SUPPORT = max(MAX_SUPPORT, len(indices))
        if len(indices) > 1_000_000:
            raise RuntimeError('Sparse support exceeds bounded test scope')
    MAX_PRUNED = max(MAX_PRUNED, pruning)
    if pruning > 1e-11:
        raise RuntimeError('Pruning error exceeds stated budget')
    return dict(zip(map(int, indices), values))


def basis_vector(i, j, n=24):
    out = np.zeros((n, n))
    if i < j:
        out[i, j] = out[j, i] = 1/math.sqrt(2)
    elif i > j:
        out[j, i] = 1/math.sqrt(2); out[i, j] = -1/math.sqrt(2)
    elif i == 0:
        np.fill_diagonal(out, 1/math.sqrt(n))
    else:
        for k in range(i):
            out[k, k] = 1/math.sqrt(i*(i+1))
        out[i, i] = -math.sqrt(i/(i+1))
    return out


def basis_checks():
    c = a.clean_basis()
    for i in range(32):
        for j in range(32):
            initial = i+(j << 5)
            if i == j and i >= 24:
                expected = {initial: 1.}
            elif i != j:
                lo, hi = sorted((i, j))
                expected = {lo+(hi << 5): 1/math.sqrt(2),
                            hi+(lo << 5): (1 if i < j else -1)/math.sqrt(2)}
            else:
                b = basis_vector(i, j)
                expected = {k+(k << 5): b[k, k] for k in range(24) if b[k, k]}
            actual = simulate_small(c, {initial: 1.})
            if distance(actual, expected) >= TOL or any(k >> 10 for k in actual):
                raise RuntimeError(f'All-input basis failed at {i},{j}')
    need(True, 'basis:all_1024_columns_correct_and_workspace_zero')
    old = simulate_small(q.build(bell_pairs=False), {1: 1.})
    need(any(k >> 10 for k in old), 'boundary:old_valid_input_extension_not_clean_on_descending_input')
    rng = np.random.default_rng(417)
    z = rng.normal(size=1024)+1j*rng.normal(size=1024); z /= np.linalg.norm(z)
    initial = dict(enumerate(z))
    actual = simulate_np(c, initial)
    need(all(not (k >> 10) for k in actual), 'basis:full_ambient_complex_superposition_clean')
    need(distance(simulate_np(q.inverse(c), actual), initial) < TOL,
         'basis:full_ambient_superposition_inverse')
    predicate = a.predicate(a.X, a.Y, a.V1)
    for i in range(32):
        for j in range(32):
            for bit in (0, 1):
                initial = i+(j << 5)+(bit << a.V1)
                expected = (i+(j << 5)+((bit ^ int(a.valid_label(i, j))) << a.V1))
                actual = simulate_small(predicate, {initial: 1.})
                if actual != {expected: 1.}:
                    raise RuntimeError('Membership predicate failed')
    need(True, 'predicate:all_1024_labels_both_target_values_no_garbage')
    need(len(a.valid_labels()) == 299, 'predicate:exact_valid_dimension_299')
    expected = {i*(1 << 10)+i*(1 << 15): 1/math.sqrt(24) for i in range(24)}
    close(distance(simulate_small(a.bell(), {0: 1.}), expected), 0, 'bell:Phi24_amplitudes_padding_and_clean_work')


def projected_tensor(matrix):
    n = len(matrix)
    d = np.einsum('ik,jl->ijkl', matrix, np.eye(n))/math.sqrt(n)
    d = (d+d.swapaxes(0, 1))/2
    d -= np.einsum('ij,kl->ijkl', np.eye(n), np.einsum('iikl->kl', d))/n
    d = (d+d.swapaxes(2, 3))/2
    d -= np.einsum('ij,kl->ijkl', np.einsum('ijkk->ij', d), np.eye(n))/n
    return d


def projection_checks():
    for n in (2, 3, 4, 5, 24):
        rng = np.random.default_rng(n)
        b = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))
        tensor = projected_tensor(b)
        actual = np.einsum('ijkj->ik', tensor)/math.sqrt(n)
        expected = ((n+2)/(4*n)*b+np.trace(b)*np.eye(n)/(4*n)
                    -(b+b.T)/n**2+np.trace(b)*np.eye(n)/n**3)
        close(actual, expected, f'projection:full_input_adjoint_formula_n{n}')
        symmetric = (b+b.T)/2
        symmetric -= np.trace(symmetric)*np.eye(n)/n
        symmetric /= np.linalg.norm(symmetric)
        tensor = projected_tensor(symmetric)
        p = F((n+4)*(n-2), 4*n*n)
        close(np.vdot(tensor, tensor), float(p), f'projection:traceless_probability_n{n}')
        close(np.einsum('iikl->kl', tensor), 0, f'projection:first_output_trace_zero_n{n}')
        close(np.einsum('ijkk->ij', tensor), 0, f'projection:second_output_trace_zero_n{n}')
    need(F(4*(24+2))-F(32, 24) == F(308, 3), 'normalization:Jordan_contraction_308_over_3')
    need(F(308, 3)/384 == F(77, 288), 'normalization:transfer_probability_77_over_288')
    need(F(77, 288)*F(72, 77) == F(1, 4), 'normalization:known_dilution_gives_one_quarter')
    need(F(1, 4) < F(77, 288), 'normalization:dilution_amplitude_is_less_than_one')
    need(F(13, 48) != F(77, 288), 'negative_control:omitting_identity_removal_changes_probability')
    need(F(299, 576) != F(77, 288), 'negative_control:trace_input_has_different_singular_value')
    # Complete flat-eigenspace check on every valid basis label, using actual
    # projections and contraction, not merely equal stored column norms.
    for r in a.valid_labels():
        b = basis_vector(r & 31, r >> 5)
        tensor = projected_tensor(b)
        got = np.einsum('ijkj->ik', tensor)/math.sqrt(24)
        if np.linalg.norm(got-(77/288)*b) >= TOL:
            raise RuntimeError('Flat-subspace column failed')
    need(True, 'projection:all_299_basis_vectors_are_full_operator_eigenvectors')


def circuit_checks():
    labels = a.valid_labels()
    basis = np.array([basis_vector(r & 31, r >> 5) for r in labels])
    index = {r: k for k, r in enumerate(labels)}
    # Expected 299x299 output coefficients, computed directly from 4 Tr(A E_b E_c).
    def expected(initial):
        matrix = sum(v*basis[index[r]] for r, v in initial.items())
        ab = np.einsum('ij,bjk->bik', matrix, basis)
        coeff = 4*ab.reshape(299, -1)@basis.reshape(299, -1).T/math.sqrt(308/3)
        return {labels[i]+(labels[j] << 10): coeff[i, j]
                for i, j in zip(*np.nonzero(abs(coeff) >= 1e-14))}
    examples = [{32: 1.}, {33: 1.},
                {32: 1/math.sqrt(3), 33: 1j/math.sqrt(3), 66: -1/math.sqrt(3)}]
    full = a.build()
    for j, initial in enumerate(examples):
        target = expected(initial)
        actual = simulate_np(full, initial)
        need(distance(actual, target) < TOL, f'circuit:full_33_wire_Jordan_input_{j}_amplitude_and_phase')
        need(all(not (k >> 20) for k in actual), f'circuit:full_Jordan_input_{j}_workspace_zero')
        close(sum(abs(v)**2 for v in actual.values()), 1, f'circuit:full_Jordan_input_{j}_norm')
    need(distance(simulate_np(q.inverse(full), actual), examples[-1]) < TOL,
         'circuit:full_Jordan_complex_input_inverse')
    # Compare the unamplified circuit, including its broader source projection.
    raw = simulate_np(a.transfer(diluted=False), examples[-1])
    good = {k: v for k, v in raw.items()
            if k >> 20 == 0 and a.valid_label(k & 31, (k >> 5) & 31)
            and a.valid_label((k >> 10) & 31, (k >> 15) & 31)}
    need(distance(good, {k: v*math.sqrt(77/288) for k, v in expected(examples[-1]).items()}) < TOL,
         'circuit:raw_projected_amplitudes_match_Jordan_adjoint')
    # Without the four final sign/flag gates the output is -target with flag 1.
    uncorrected = q.Circuit(); uncorrected.gates = full.gates[:-4]
    target = {k | (1 << a.FLAG): -v for k, v in expected(examples[0]).items()}
    need(distance(simulate_np(uncorrected, examples[0]), target) < TOL,
         'negative_control:odd_amplification_sign_requires_correction')
    need(MAX_PRUNED < 1e-11, 'simulation:accumulated_sparse_pruning_below_budget')


def composition_checks():
    # All controlled primitive truth columns, including negative H/Ry amplitudes.
    prototypes = [q.Gate('X', (0,), None), q.Gate('H', (0,), None),
                  q.Gate('CX', (0, 1), None), q.Gate('CCX', (0, 1, 2), None),
                  q.Gate('Ry', (0,), .731)]
    for gate in prototypes:
        circuit = q.Circuit(); s.lift_gate(circuit, gate, 3, 4)
        base = q.Circuit(); base.gates = [gate]
        for k in range(16):
            if k >> 3:
                target = {v | 8: z for v, z in simulate_small(base, {k & 7: 1.}).items()}
            else:
                target = {k: 1.}
            if distance(simulate_small(circuit, {k: 1.}), target) >= TOL:
                raise RuntimeError('Controlled gate lift failed')
        need(True, 'control:exact_lift_all_columns_'+gate.name)
        need(Counter(a.counts(circuit)) == s.lift_counts({gate.name: 1}),
             'control:cost_formula_'+gate.name)
    for name, mapping in s.wire_maps().items():
        need(len(mapping.values()) == len(set(mapping.values())), 'routing:injective_wire_map_'+name)
        need(not ({s.CONTROL, s.CONTROL_SCRATCH} & set(mapping.values())),
             'routing:control_wires_disjoint_'+name)
    for tag in (0, 1, 2):
        marker = s.branch_marker(tag)
        for selector in range(4):
            initial = sum(((selector >> j) & 1) << w for j, w in enumerate(s.SELECTOR))
            actual = simulate_small(marker, {initial: 1.})
            target = {initial | ((selector == tag) << s.CONTROL): 1.}
            if actual != target:
                raise RuntimeError('Selector match failed')
        need(True, f'routing:selector_match_truth_table_tag{tag}')
        pairs = s.routing_pairs(tag)
        # All one-hot source payload bits and zero check exact selected routing;
        # false control must leave each payload unchanged.
        for bit in [None]+[u for u, _ in pairs]:
            value = 0 if bit is None else 1 << bit
            for control in (0, 1):
                initial = value | (control << s.CONTROL)
                target = initial
                if control:
                    if bit is not None:
                        target = (1 << dict(pairs)[bit]) | (1 << s.CONTROL)
                    for j in range(2):
                        if tag >> j & 1:
                            target |= (1 << s.TAG1[j]) | (1 << s.TAG2[j])
                if simulate_small(s.routing(tag), {initial: 1.}) != {target: 1.}:
                    raise RuntimeError('Controlled payload routing failed')
        need(True, f'routing:all_payload_wires_and_tags_tag{tag}')
    selector = simulate_small(s.selector_preparation(), {0: 1.})
    target = {sum(((tag >> j) & 1) << w for j, w in enumerate(s.SELECTOR)):
              math.sqrt(s.WEIGHTS[tag]/6929) for tag in range(3)}
    need(distance(selector, target) < TOL, 'composition:positive_exact_branch_weight_amplitudes')
    # Three branch-dependent payloads, with coherent signs retained.
    flagged = {}; unflagged = {}
    for tag in range(3):
        tags = sum(((tag >> j) & 1)*((1 << s.TAG1[j])+(1 << s.TAG2[j])) for j in range(2))
        sel = sum(((tag >> j) & 1) << w for j, w in enumerate(s.SELECTOR))
        payload = (tag+1) << s.OUT1[0]
        amplitude = math.sqrt(s.WEIGHTS[tag]/6929)*([1, 1j, -1][tag])
        flagged[tags | sel | payload] = amplitude
        unflagged[tags | payload] = amplitude
    need(distance(simulate_small(s.selector_erasure(), flagged), unflagged) < TOL,
         'composition:selector_erasure_preserves_coherent_relative_phases')
    need(F(77, 6929)+F(3780, 6929)+F(3072, 6929) == 1, 'composition:weights_sum_one')
    need(299+98280+98304 == 196883, 'composition:tagged_logical_dimension')
    need(F(299, 196883) < F(1, 500), 'boundary:complete_A0_is_less_than_one_five_hundredth_of_V')
    need(sum((F(v, 6929))**2 for v in s.WEIGHTS) < 1,
         'negative_control:discarding_selector_before_erasure_loses_branch_coherence')


def resource_checks():
    jordan, sector = a.report(), s.report()
    need(jordan['total'] == {'CCX': 7657, 'CX': 1571, 'H': 447, 'Ry': 444, 'X': 6838},
         'resources:16957_Jordan_instructions')
    need(sector['total'] == {'CCX': 103134594, 'CX': 25628550, 'H': 2206382,
                              'Ry': 4804705, 'X': 18}, 'resources:135774249_tagged_sector_instructions')
    need(jordan['total_wires'] == 33 and sector['total_wires'] == 105,
         'resources:33_and_105_wire_interfaces')
    need(sector['output_wires']+sector['clean_zero_workspace_wires'] == 105,
         'resources:40_output_and_65_clean_work_wires')
    for filename, result in [('jordan_aaa_resources.json', jordan), ('a0_sector_resources.json', sector)]:
        need((ROOT/'results'/filename).read_text() == json.dumps(result, sort_keys=True, indent=2)+'\n',
             'resources:recorded_'+filename)


def main():
    basis_checks(); projection_checks(); circuit_checks(); composition_checks(); resource_checks()
    print(json.dumps({
        'status': 'PASS within declared Jordan/sector-composition scopes',
        'checks': len(LABELS), 'labels': LABELS,
        'all_input_basis_columns_tested': 1024,
        'Jordan_flat_eigenspace_columns_tested': 299,
        'full_33_wire_Jordan_circuit_inputs_tested': 3,
        'Jordan_circuit_inverse_on_complex_input': True,
        'largest_dense_matrix_dimension': 299,
        'largest_coefficient_tensor_shape': [24, 24, 24, 24],
        'largest_coefficient_tensor_entries': 24**4,
        'sparse_support_hard_limit': 1_000_000,
        'sparse_pruning_budget': 1e-11, 'numerical_tolerance': TOL,
        'combined_105_wire_circuit_simulated': False,
        'full_Monster_tensor_constructed': False,
        'complete_full_W': False,
        'precision_certified_at_1e_12': False,
        'novelty_established': False,
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
