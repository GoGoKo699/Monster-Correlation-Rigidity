# Monster Correlation Rigidity

Research project for Ruge Lin: exceptional finite symmetry as an operational property of quantum correlations, not merely a finite-group representation fitting in a small register.

**Current scope:** mathematical certification with explicit access assumptions. Two bounded assistant proof audits have reconstructed the listed proof dependencies and recorded narrow repairs. This is not independent human/expert review, formal verification, comprehensive novelty clearance, or a practical implementation claim.

## Start here

`STATUS.md` is the immutable import-era ledger. Its current successor is `STATUS_CURRENT.md`; read the latter for integrated claims and corrections.

Read [STATUS_CURRENT.md](STATUS_CURRENT.md), the [audit integration errata](audits/integration_20260925.md), and [the current work order](work_orders/CURRENT.md). The newest work is [a normalized circuit for one Griess-isometry block](research/07_seysen_qqa_block.md), following [probe access and calibration](research/06_probe_access.md). The [priority matrix](audits/priority_matrix.md) remains a first source-based pass, not a completed novelty audit.

## Current mathematical statement

Let d=196883, let P be the rank-d projector defined by the traceless Griess multiplication isometry, and let sigma=P/d. Preparing sigma, applying the same fixed unitary U to both registers, and measuring P defines the ideal rejection probability epsilon(U).

The assembled derivation, read with both audit supplements, gives

$$\epsilon(U)\le10^{-12}\quad\Longrightarrow\quad
D_{\mathbb M}(U):=\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}
\le1.151\sqrt{\epsilon(U)}.$$

It does not assume prior calibration. For real orthogonal U the sufficient threshold is 10^-10. These are normalized Frobenius bounds, not worst-case channel bounds, and the thresholds are not claimed optimal. Non-strict comparisons include the zero-error case.

The central mechanism is correlations -> cubic extrema -> axes -> involutions -> approximate conjugation -> one rounded Monster operation. The underlying Griess/VOA inputs are classical. The complete quantitative theorem's priority remains unresolved.

## Access is a separate problem

A clean coherent extension A of W provides both probe preparation and the P measurement through A and its inverse. Thus two uses of U per trial do **not** mean two elementary gates, nor free probe access. No efficient circuit for the complete A is supplied.

Note 06 establishes explicit access reductions and limitations:

- The probe is the normalized Choi state of the multiplication channel. Channel access prepares it but does not specify an inverse dilation or P measurement.
- An ordinary repeated SWAP comparison sees Tr(sigma omega)=(1-epsilon)/d. Its restricted binary-observation complexity scales quadratically with d for fixed precision; this is not a lower bound for all quantum measurements.
- If trusted preparation trace error is at most a and effect operator error at most b, ideal loss is at most a+b plus a statistical upper confidence bound on observed rejection. The C13 threshold still has to be met after adding this budget.

At zero calibration error, reaching 10^-12 with no observed rejections at 95% confidence takes about 3 x 10^12 independent ideal trials. Neither this nor the generic copy-based alternatives is presently a practical proposal.

### First compiled block, not a complete probe

[Note 07](research/07_seysen_qqa_block.md) independently converts Seysen's normalization and compiles the normalized A_0 -> Q tensor Q branch. For a traceless symmetric 24 by 24 matrix A, this branch is twelve Bell pairs times matrix vectorization. Its squared weight in W is 3072/6929 for inputs in the 299-dimensional A_0 sector. This is not 44 percent of the entire isometry.

The [circuit generator](circuits/seysen_qqa.py) emits 1746 instructions on 45 wires: 799 Toffoli, 131 CNOT, 60 Hadamard, 708 X, and 48 Ry gates. Eleven work wires are clean on the specified input subspace. The gate library includes arbitrary-angle rotations; their finite-gate-set synthesis, physical routing, canonical 18-qubit sector packing and all other blocks are excluded. There is no postselection or amplification in this normalized subroutine. It does not by itself certify Monster membership or alter the loss thresholds.

## Research record

| Note | Role |
|---|---|
| [01](research/01_local_rigidity.md) | Local cubic sensitivity |
| [02](research/02_pair_correlations.md) | Pair projector, channel spectrum, exact stabilizers, parent-state gap |
| [03](research/03_uniform_axis_rounding.md) | Historical uniform-axis proof, threshold 10^-25 |
| [04](research/04_average_transport.md) | Average axis transport and independent-unitary agreement |
| [05](research/05_normalizer_rounding.md) | Single-symmetry rounding and improved sufficient thresholds |
| [06](research/06_probe_access.md) | Coherent versus copy access, calibration and resource accounting |
| [07](research/07_seysen_qqa_block.md) | Source metric/identity conversion, contraction weights, clean QQA block circuit |

Notes 01-06 remain unchanged. Read the historical claims with [the VOA audit](audits/voa_extrema_audit.md) and [the eight-obligation robustness audit](audits/robustness_proof_audit.md). The original C12 strict inequality at zero and general-lemma parameter domains require the explicit recorded corrections.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py
python checks/audit_parameter_domains.py
OPENBLAS_NUM_THREADS=1 python checks/verify_probe_access.py
OPENBLAS_NUM_THREADS=1 python checks/verify_seysen_block.py
python circuits/seysen_qqa.py --emit
# Separate, explicitly tolerant portability inspection; does not change evidence:
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
```

The unchanged root verifier requires byte-identical historical reports. The original recorded environment is Python3.13.5/NumPy2.3.5. A GitHub runner produced differing floating leaves in a historical toy report, so exact output portability must not be assumed even with matching package versions. The separate portability inspector permits finite floating-leaf differences only in two named historical numerical reports, with absolute/relative tolerance 5e-12, except the six pair-test finite-difference fields, for which both reports must remain within the original 2e-6 analytic-target tolerance. Structure and nonfloating values remain exact. It prints every difference and does not overwrite evidence. Strict failure remains distinguishable from bounded numerical agreement.

The access checker has 44 checks and largest matrix 81 by 81. The new block checker has 50 checks, evaluates the 21-wire coordinate subroutine sparsely on all 299 valid basis inputs and complex superpositions, and verifies the twelve Bell pairs separately. Its largest dense matrix is 24 by 24; it does not expand the 45-wire state. Historical toy replays reach 256 by 256. No full Monster tensor/matrix or axis list is generated. These tests do not establish 1e-12 circuit accuracy, imported classifications, or novelty.

## Coordination and provenance

Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). Keep work on separate branches, preserve the license and historical evidence, and identify the claim dependencies of each change. No manuscript, release, outreach, or quantum-advantage claim is authorized by the current work order.

The original MIT [LICENSE](LICENSE), Copyright (c)2026 Ruge Lin, and the [archived seed](provenance/Repository_Seed_2026-09-23.zip) are preserved. See [COPYING.md](COPYING.md) and [the import record](provenance/repository_import.json).
