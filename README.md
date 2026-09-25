# Monster Correlation Rigidity — physical selection

Ruge Lin's research project asks whether independently meaningful physical requirements select the Monster, rather than merely whether an engineered object can have Monster symmetry.

**The owner has redirected the main research line.** Gate recognition, circuit compilation and rejection-threshold optimization are now subsidiary records, not the selection principle. The active ledger is [PHYSICS_STATUS.md](PHYSICS_STATUS.md). The unchanged [STATUS_CURRENT.md](STATUS_CURRENT.md) records the earlier certification track; [STATUS.md](STATUS.md) is the original import-era record.

## Current physical question

Among nontrivial, simple, unitary, strongly rational bosonic holomorphic chiral CFTs with no weight-one currents, minimize the positive central charge. This criterion is stated without a Monster action or Griess multiplication. Holomorphicity is a substantial restriction on the class of theories, not a universal law of physics. Minimizing central charge is not an asserted dynamical RG mechanism.

[Note 12](research/12_physical_selection_from_extremality.md) establishes the following chain using prior modular, conformal-design and trace theorems:

**minimal current-free holomorphic theory -> c=24 and the J spectrum -> conformal 11-design constraints -> fixed low-energy OPE contraction identities.**

At c=8 and c=16, modular characters force 248 and 496 currents respectively. At c=24 the current-free condition fixes J=q^(-1)+196884q+..., leaving 196883 weight-two primaries besides the stress tensor. The known moonshine theory attains the minimum; uniqueness is not assumed or proved.

For any candidate minimizer, all primary torus one-point functions of positive weight at most eleven vanish. This is Hoehn's prior theorem, derived from extremality and modularity, not an assumed finite symmetry. Hoehn explicitly permits replacing Matsuo's large-automorphism assumptions by these design conditions. Consequently the normalized primary three-point coefficients obey

$$\sum_{b,c}C_{abc}C_{a'bc}=\frac{13858}{3}\delta_{aa'}.$$

The same argument forces the six eigenvalues and multiplicities of the OPE contraction operator used earlier in the project. This is an explicit **corollary of established results**, not a new trace formula, a reconstructed full OPE tensor, or a proof that the Monster group has been selected. No Monster character table or irreducible decomposition is used in this derivation.

In the diagonal nonchiral completion, the scalar gap is four, excluding nontrivial relevant and marginal Lorentz-scalar deformations. This is a conformal-perturbation statement, not proof of a microscopic realization or attraction basin.

## The missing interaction problem

A spectrum and summed coupling constraints do not identify the full multiplication. We have not proved that every minimizer's weight-two algebra is the Conway–Griess algebra. The conditional Dong–Griess–Lam uniqueness theorem still requires precisely that hypothesis. Current 2026 primary literature also distinguishes partition-function equality from full VOA reconstruction; the moonshine uniqueness problem remains open there.

The [next bounded assignment](work_orders/CURRENT.md) is an uncontracted weight-two four-point/OPE consistency calculation, beginning with the weight-three primary channel and its positive Gram form. Do not insert a Monster representation, axis classification, or known multiplication table to close the argument. Failure to find an alternative tensor is not a uniqueness proof; an algebraic tensor without a complete CFT realization is not an alternative physical theory.

## Evidence and historical record

The [new checker](checks/verify_physical_selection.py) has 37 exact scalar checks of characters, modular-form dimensions, trace normalization, spectral roots and multiplicities. It uses integer/fraction arithmetic and constructs no dense matrix, Monster data or full OPE tensor. Its report reproduces under normal Python, -O and -OO. The source theorems and existence/uniqueness questions are not proved by those checks.

```sh
python checks/verify_physical_selection.py
python -O checks/verify_physical_selection.py
python -OO checks/verify_physical_selection.py
# Historical evidence replay, unchanged:
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
```

All notes 01–11, old code/data/results/audits, original status ledgers, provenance archives and license remain unchanged. The old rigidity theorem is a conditional recognition statement for a specified tensor, not evidence that physics selects that tensor. The prior complete A0-sector circuit is not a full probe compiler. Source depth, numerical portability distinctions and prior-review limits remain recorded.

Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). No independent expert review, formal verification, comprehensive novelty clearance, practical implementation, manuscript, release or outreach is claimed. The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, is preserved.
