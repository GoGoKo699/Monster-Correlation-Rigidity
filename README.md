# Monster Correlation Rigidity

Ruge Lin's research project on exceptional finite symmetry as a property of quantum correlations, rather than only a representation fitting into a register.

**Current status:** a mathematical rigidity derivation with two bounded assistant audits and explicit repairs, plus a constructive ideal-angle circuit for the complete 299-dimensional A0 input sector. The full 196883-dimensional multiplication isometry is **not** compiled. No independent expert review, formal verification, established novelty, practical implementation or quantum advantage is claimed.

## Latest result: all three A0 branches coherently combined

[Note 09](research/09_jordan_and_a0_sector.md) completes the normalized projected symmetric-matrix branch and combines it with the [QQA](research/07_seysen_qqa_block.md) and [Leech XXA](research/08_leech_xxa_block.md) constructions:

$$W_{A0}=\sqrt{77/6929}\,J_A+\sqrt{3780/6929}\,J_X+\sqrt{3072/6929}\,V_Q.$$

The three terms occupy orthogonal AA, XX and QQ output sectors. Controlled circuits, relative phases, output routing and coherent selector erasure are specified; discarding the selector is not substituted for uncomputation.

The new Jordan branch uses Bell insertion and projection onto two traceless symmetric matrix spaces. Its input-independent transfer probability is 77/288. Dilution to 1/4 permits one exact ideal-angle amplification round. The [emitted circuit](circuits/jordan_aaa.py) has **16957 logical instructions on 33 wires**, with thirteen clean work wires. A new basis extension is clean on every ambient coordinate input, not just the valid matrix-label subspace.

The [complete A0 composition](circuits/a0_sector.py) is a hierarchical circuit with **135774249 logical instructions on 105 wires**, including controlling the explicit Leech loader. It has forty output wires and sixty-five clean work wires. Each output uses a **20-qubit tagged encoding**, not a canonical 18-qubit packing. Arbitrary-angle Ry gates, Toffolis and unrestricted connectivity are the stated logical gate model; physical routing, fault-tolerant synthesis and high-precision angle compilation are excluded.

The new [81-check verifier](checks/verify_a0_sector.py) checks all 1024 ambient basis-change inputs and all 299 flat-eigenspace columns. It sparsely simulates the complete Jordan circuit on three inputs, including a complex superposition, and its inverse. It does **not** simulate the full 105-wire combined circuit or full Monster tensor. Largest dense matrix: 299 by 299; largest coefficient tensor: 24^4 entries.

This completes one input sector, **299/196883 of the logical dimension**, not the full W or the full probe. The X and Q input sectors remain uncompiled. No isolated branch or restricted sector is a standalone Monster membership test.

## Mathematical certificate and operational limits

Let d=196883, P=WW^dagger be the full rank-d multiplication projector, and sigma=P/d. Preparing sigma, applying the same fixed U to both registers and measuring P defines ideal rejection epsilon(U). Read with the audit repairs, the assembled derivation gives

$$\epsilon(U)\le10^{-12}\quad\Longrightarrow\quad
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}\le1.151\sqrt{\epsilon(U)}.$$

No prior calibration promise is assumed. The sufficient real-orthogonal threshold is 1e-10. These are normalized Frobenius statements, not worst-case channel bounds or optimal thresholds. Notes 07-09 do not improve them.

[Note 06](research/06_probe_access.md) separates coherent access, copy/channel access, calibration and statistical costs. Two U calls do not pay for the full probe preparation and measurement. At zero calibration error, zero-rejection sampling to the present 1e-12 threshold at 95 percent confidence requires about 3e12 ideal independent trials. Completing A0 does not supply the full sigma or P experiment.

## Claims, priority and verification

[STATUS_CURRENT.md](STATUS_CURRENT.md) is the active ledger; `STATUS.md` is the protected import-era record. Historical notes 01-08 remain unchanged. Read them with the [VOA audit](audits/voa_extrema_audit.md), [robustness audit](audits/robustness_proof_audit.md) and [integration errata](audits/integration_20260925.md). The [priority matrix](audits/priority_matrix.md) is partial. The [next bounded task](work_orders/CURRENT.md) prioritizes a theorem-level precursor comparison for C11, rather than assuming that more circuit components establish publication novelty.

```sh
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
OPENBLAS_NUM_THREADS=1 python checks/verify_a0_sector.py
python circuits/jordan_aaa.py --emit
python circuits/a0_sector.py --plan
```

The unchanged root verifier requires strict byte replay. Recognized historical floating-report mismatches remain strict failures; the separate unchanged portability inspector checks only its previously documented bounded exceptions. New outputs agree locally under normal/-O/-OO. Read the workflow for its actual baseline/candidate outcomes. Numerical tolerance 1e-10 does not certify 1e-12 circuit synthesis.

Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and all historical evidence are preserved. No large cloud simulation, manuscript, release or outreach is part of this work order.
