#!/usr/bin/env python3
"""Exact A5 witness for the omitted parameter domains in note 05, section 5.

This demonstrates failure of the stated proof steps when beta=2, not a
counterexample to the normalizer lemma's conclusion: the witness has O=I.
The same group with beta=0 supplies a valid-domain control.  The regular walk
is certified using integer matrices and rational spectral-projector traces;
there are no floating-point calculations or external dependencies.

The standard A5 representation is the real sum-zero subspace of R^5.  Its
character is fixed_points(g)-1.  Character norm one establishes absolute
irreducibility by the usual finite-group character criterion.  Its orthogonal
matrix separation follows from that character, without choosing a basis.

Largest matrix: 60 by 60.  This is no Monster simulation, formal proof,
priority assessment, or independent expert review.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
import json


Permutation = tuple[int, ...]
Matrix = list[list[int]]
CHECKS: list[str] = []


def need(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError("Check failed: " + label)
    CHECKS.append(label)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(value: Permutation) -> Permutation:
    result = [0] * len(value)
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def is_even(value: Permutation) -> bool:
    return sum(
        value[i] > value[j]
        for i in range(len(value))
        for j in range(i + 1, len(value))
    ) % 2 == 0


def identity_matrix(size: int) -> Matrix:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    result = [[0] * size for _ in range(size)]
    for i, row in enumerate(left):
        for k, coefficient in enumerate(row):
            if coefficient:
                for j, entry in enumerate(right[k]):
                    result[i][j] += coefficient * entry
    return result


def shifted(matrix: Matrix, eigenvalue: int) -> Matrix:
    return [
        [entry - eigenvalue * int(i == j) for j, entry in enumerate(row)]
        for i, row in enumerate(matrix)
    ]


def trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def scalar_hypotheses(
    *, beta: Fraction, threshold: Fraction, length: int,
    q: Fraction, z_squared: Fraction, order: int, separation_squared: Fraction,
) -> tuple[Fraction, dict[str, bool]]:
    """Evaluate just the scalar inequalities printed in the historical note.

    Both witnesses have a positive accumulated error, so squaring the
    separation comparison preserves its strict inequality.
    """
    if beta == 1:
        raise ValueError("The historical formula is undefined at beta=1")
    conditional_bound = (q + beta) / (1 - beta)
    accumulated_error = length * threshold
    if accumulated_error <= 0:
        raise ValueError("These witnesses require positive accumulated error")
    return conditional_bound, {
        "z_squared_le_beta_t_squared": z_squared <= beta * threshold**2,
        "r_lt_one": conditional_bound < 1,
        "order_minus_one_times_r_to_L_lt_one":
            (order - 1) * conditional_bound**length < 1,
        "L_times_t_lt_one": accumulated_error < 1,
        "three_L_times_t_lt_s0":
            (3 * accumulated_error)**2 < separation_squared,
    }


def main() -> None:
    ident = tuple(range(5))
    group = [value for value in permutations(range(5)) if is_even(value)]
    group_set = set(group)
    index = {value: i for i, value in enumerate(group)}
    order = len(group)
    identity_index = index[ident]
    need(order == 60, "A5 has 60 enumerated even permutations")
    need(
        all(compose(g, h) in group_set for g in group for h in group)
        and all(inverse(g) in group_set for g in group),
        "The enumerated permutations are closed under products and inverses",
    )
    involutions = [
        value for value in group
        if value != ident and compose(value, value) == ident
    ]
    need(len(involutions) == 15, "There are 15 nonidentity involutions")
    need(
        {compose(compose(g, involutions[0]), inverse(g)) for g in group}
        == set(involutions),
        "The involutions form one conjugacy class",
    )

    degree = 4
    character = [sum(g[i] == i for i in range(5)) - 1 for g in group]
    need(
        character[identity_index] == degree
        and sum(character) == 0
        and sum(value**2 for value in character) == order,
        "The standard sum-zero character has degree four and squared norm one",
    )
    max_nonidentity_character = max(
        character[i] for i in range(order) if i != identity_index
    )
    need(
        max_nonidentity_character == 1 < degree,
        "Every nonidentity standard matrix has trace below four (faithfulness)",
    )
    separation_squared = 2 - 2 * Fraction(max_nonidentity_character, degree)
    need(
        separation_squared == Fraction(3, 2),
        "The standard orthogonal representation has s0 squared equal to 3/2",
    )

    # A[row][column] counts left multiplication by one class element.
    adjacency = [[0] * order for _ in range(order)]
    for c in involutions:
        for column, g in enumerate(group):
            adjacency[index[compose(c, g)]][column] += 1
    class_size = len(involutions)
    need(
        all(sum(row) == class_size for row in adjacency)
        and all(
            adjacency[i][j] == adjacency[j][i]
            for i in range(order) for j in range(order)
        ),
        "The integer class-walk adjacency is symmetric with row sum fifteen",
    )

    polynomial = adjacency
    for eigenvalue in (15, -5, 3):
        polynomial = multiply(polynomial, shifted(adjacency, eigenvalue))
    need(
        all(entry == 0 for row in polynomial for entry in row),
        "A(A-15I)(A+5I)(A-3I) vanishes exactly",
    )

    # A is real symmetric.  The distinct-root polynomial restricts its
    # spectrum to these roots, and each Lagrange polynomial is a projector.
    roots = (15, -5, 0, 3)
    multiplicities: dict[int, int] = {}
    for root in roots:
        numerator = identity_matrix(order)
        denominator = 1
        for other in roots:
            if other != root:
                numerator = multiply(numerator, shifted(adjacency, other))
                denominator *= root - other
        multiplicity = Fraction(trace(numerator), denominator)
        need(
            multiplicity.denominator == 1 and multiplicity > 0,
            "The exact projector trace at eigenvalue " + str(root)
            + " is a positive integer",
        )
        multiplicities[root] = multiplicity.numerator
    need(
        multiplicities == {15: 1, -5: 18, 0: 16, 3: 25},
        "The full adjacency spectrum has multiplicities 1,18,16,25",
    )
    q = max(Fraction(abs(root), class_size) for root in roots if root != 15)
    need(
        multiplicities[15] == 1 and sum(multiplicities.values()) == order
        and q == Fraction(1, 3),
        "The uniform class walk has unique constant mode and exact q=1/3",
    )

    # O=I and h_c=c make every assigned error zero, so all class elements
    # are good and the actual good-set walk is A/15 in both cases.
    threshold = Fraction(1, 100)
    z_squared = Fraction(0)
    invalid_beta = Fraction(2)
    invalid_length = 1
    invalid_r, invalid_conditions = scalar_hypotheses(
        beta=invalid_beta, threshold=threshold, length=invalid_length,
        q=q, z_squared=z_squared, order=order,
        separation_squared=separation_squared,
    )
    need(
        all(invalid_conditions.values()),
        "The beta=2 witness satisfies every displayed scalar hypothesis",
    )
    need(
        invalid_r == Fraction(-7, 3) and q > invalid_r,
        "The claimed conditioned-walk bound fails: actual 1/3 exceeds -7/3",
    )
    need(
        adjacency[identity_index][identity_index] == 0,
        "The claimed exact-one-step full support fails at the identity",
    )

    valid_beta = Fraction(0)
    valid_length = 5
    valid_r, valid_conditions = scalar_hypotheses(
        beta=valid_beta, threshold=threshold, length=valid_length,
        q=q, z_squared=z_squared, order=order,
        separation_squared=separation_squared,
    )
    need(
        0 <= valid_beta < 1 and threshold > 0 and valid_length >= 1
        and all(valid_conditions.values()),
        "The beta=0, L=5 control satisfies the intended domains and inequalities",
    )
    adjacency_squared = multiply(adjacency, adjacency)
    adjacency_fourth = multiply(adjacency_squared, adjacency_squared)
    adjacency_fifth = multiply(adjacency_fourth, adjacency)
    minimum_five_step_count = min(min(row) for row in adjacency_fifth)
    need(
        minimum_five_step_count > 0
        and all(sum(row) == class_size**valid_length for row in adjacency_fifth),
        "The valid control has positive exact-five-step counts for every pair",
    )

    report = {
        "status": "PASS: omitted-domain proof-step witness and valid-domain control",
        "scope": "Historical note 05 section 5 parameter domains only",
        "checks": CHECKS,
        "check_count": len(CHECKS),
        "group": "A5, with its standard real four-dimensional representation",
        "group_order": order,
        "class_size": class_size,
        "adjacency_eigenvalue_multiplicities": {
            str(root): multiplicities[root] for root in roots
        },
        "actual_walk_norm_on_nonconstant_functions": str(q),
        "standard_representation_separation_squared": str(separation_squared),
        "witness_common_assignment": "O=I and h_c=c; every assigned error is zero",
        "invalid_domain_witness": {
            "beta": str(invalid_beta),
            "t": str(threshold),
            "L": invalid_length,
            "z_squared": str(z_squared),
            "r": str(invalid_r),
            "displayed_scalar_hypotheses": invalid_conditions,
            "actual_bad_fraction": "0",
            "claimed_walk_norm_bound_is_false": q > invalid_r,
            "exact_one_step_identity_count": adjacency[identity_index][identity_index],
            "is_counterexample_to_lemma_conclusion": False,
            "reason": "O=I already normalizes G; the proof steps fail because beta>=1",
        },
        "valid_domain_control": {
            "beta": str(valid_beta),
            "t": str(threshold),
            "L": valid_length,
            "z_squared": str(z_squared),
            "r": str(valid_r),
            "displayed_scalar_hypotheses": valid_conditions,
            "mixing_expression": str((order - 1) * valid_r**valid_length),
            "minimum_exact_five_step_count": minimum_five_step_count,
            "transition_probability_denominator": class_size**valid_length,
        },
        "required_domain_repair": "0<=beta<1, t>0, L a positive integer, 0<=q<1",
        "arithmetic": "Exact integers and fractions; Python standard library only",
        "largest_matrix_dimension": order,
        "full_monster_simulation": False,
        "formal_proof": False,
        "independent_expert_review": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
