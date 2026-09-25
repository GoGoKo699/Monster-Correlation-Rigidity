# Monster Correlation Rigidity

Ruge Lin's research project on exceptional finite symmetry as a property of quantum correlations, rather than only a representation that fits into a register.

**Current status:** a mathematical rigidity derivation with two bounded assistant audits and explicit repairs, plus two separately constructed isometry branches. This is not independent expert review, formal verification, established novelty, a complete probe circuit, or a practical quantum-advantage claim.

## Latest result

[Note 08](research/08_leech_xxa_block.md) constructs the normalized Leech quadratic-form encoding

$$J_X|A\rangle=\frac1{\sqrt{5040}}\sum_r(\lambda_r^T A\lambda_r)|r,r\rangle$$

on the 299-dimensional space of complex symmetric traceless 24 by 24 matrices. A flat frame operator gives input-independent transfer probability 1/312. Known-angle dilution and 14 amplification rounds remove postselection without reflecting about the unknown input or retaining its label. This is a specialization of established block-encoding/amplification techniques, with the row loader explicitly priced.

The direct reference construction has **57,349,301 logical instructions on 63 wires**, including 1,298,668 arbitrary-angle rotations. It is a finite upper bound, not a practical cost claim. Its 36 output wires contain two native row labels; 27 work wires are clean in the ideal circuit. Physical routing, fault-tolerant synthesis, high-precision angle compilation and canonical full-representation packing are excluded.

The [generator](circuits/leech_xxa.py) specifies finite row/uniform-loader circuits and the full hierarchical amplification plan. The [51-check verifier](checks/verify_leech_xxa.py) tests frame arithmetic and component constructions; it does not simulate the full 63-wire amplified circuit. Its checks include all 98,280 length-24 Leech rows, which are not Monster axes. Largest dense operator: 32 by 32.

[Note 07](research/07_seysen_qqa_block.md) previously constructed the normalized spinor-vector branch using matrix vectorization and twelve Bell pairs. These are **two output branches on the same A_0 input sector**, not a completed 196883-dimensional isometry. Their squared Griess weights are 3780/6929 and 3072/6929 respectively. Neither isolated branch is a Monster membership test.

## Mathematical certificate and remaining cost

Let d=196883, P=WW^dagger be the rank-d multiplication projector and sigma=P/d. Prepare sigma, apply a fixed U to both registers, and measure P, giving ideal rejection epsilon(U). The assembled derivation, read with the audits, gives

$$\epsilon(U)\le10^{-12}\ \Longrightarrow\
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}\le1.151\sqrt{\epsilon(U)}.$$

No prior calibration promise is assumed. The sufficient real-orthogonal threshold is 1e-10. These are normalized Frobenius statements, not worst-case channel bounds, and the thresholds are not optimality claims. Notes 07-08 do not improve them.

[Note 06](research/06_probe_access.md) distinguishes coherent access, channel/copy access, calibration and sample costs. Two calls to U do not pay for preparing and measuring the special probe. At zero calibration error, zero-rejection sampling to the current 1e-12 threshold at 95 percent confidence requires about 3e12 ideal independent trials. The full W circuit, practical precision and comprehensive priority remain open.

## Read the record

[STATUS_CURRENT.md](STATUS_CURRENT.md) is the active claim ledger; `STATUS.md` is the unchanged import-era record. The [current work order](work_orders/CURRENT.md) gives the next bounded task. Notes [01](research/01_local_rigidity.md), [02](research/02_pair_correlations.md), [03](research/03_uniform_axis_rounding.md), [04](research/04_average_transport.md), and [05](research/05_normalizer_rounding.md) retain their original bytes and must be read with the [VOA audit](audits/voa_extrema_audit.md), [robustness audit](audits/robustness_proof_audit.md) and [integration errata](audits/integration_20260925.md). The [priority matrix](audits/priority_matrix.md) is partial.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
python checks/audit_parameter_domains.py
OPENBLAS_NUM_THREADS=1 python checks/verify_probe_access.py
OPENBLAS_NUM_THREADS=1 python checks/verify_seysen_block.py
OPENBLAS_NUM_THREADS=1 python checks/verify_leech_xxa.py
python circuits/leech_xxa.py --plan
```

The unchanged root verifier requires strict byte replay of historical reports. Some historical floating-point reports differ on GitHub runners. The separate, unchanged portability inspector reports only its previously specified bounded exceptions; it does not turn a strict replay failure into a strict pass or overwrite evidence. The new report agrees locally under normal Python, -O and -OO. Read the actual workflow outcome for each tested commit. Numerical checks at 1e-10 do not establish 1e-12 circuit accuracy.

Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). No large cloud simulation, manuscript, release or outreach is part of the present work order. The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and all provenance archives remain unchanged.
