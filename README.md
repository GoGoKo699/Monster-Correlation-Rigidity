# Monster Correlation Rigidity

Ruge Lin's research project on exceptional finite symmetry as a property of quantum correlations, rather than only a representation fitting into a register.

**Current status:** a mathematical rigidity derivation with two bounded assistant audits, a complete tagged A0-sector circuit, and a theorem-level stability comparison with an explicit reducible counterexample. The full multiplication isometry is not compiled. No independent expert review, formal verification, established novelty, practical implementation or quantum advantage is claimed.

## Latest: what makes exact normalizer rounding possible?

[Note 10](research/10_normalizer_stability_comparison.md) compares repaired C11 with original Gowers-Hatami, De Chiffre-Ozawa-Thom, and Burger-Ozawa-Thom statements. C11's averaged-intertwiner equivalence step directly matches Gowers-Hatami Lemma 7.1. Qualitative stability at a fixed representation already follows from compactness. Neither is a new project stability paradigm.

The comparison yields a concrete obstruction. For the fixed group A5 x A5, faithful reducible representations of dimension D=16k+4 admit operations whose class-mean squared image error is 8/D, while their **exact squared distance from the full orthogonal normalizer is 24k/D**. The nonconstant class-walk norm stays 1/3 and group-matrix separation stays bounded below. Even uniform error over the entire group tends to zero. At k=10000 all other repaired C11 conditions hold, but deleting irreducibility would make its conclusion false by a factor 20000.

This does **not** falsify the actual C11 or the Monster certificate. A four-dimensional unmatched representation component obstructs the exact implementation of an automorphism that works on the much larger remaining space. The averaged intertwiner is nonzero but singular.

There is a precise conditional repair: once the recovered automorphism is orthogonally implementable in the given representation, projection onto the full intertwiner space and polar completion recover the same bound z^2/(1-q), even for reducible representations. Compatibility cannot be inferred from small normalized error alone. These are self-contained derivations using standard techniques; comprehensive priority remains unresolved.

The [96-check verifier](checks/verify_normalizer_priority.py) checks exact A5 data, small intertwiner/trace identities, a valid irreducible control, compatible reducible controls, and the large-family scalar witness. Largest dense matrix: 60 by 60. The dimension-160004 representation and the full continuous normalizer are not numerically enumerated; the exact minimum is proved analytically.

## The correlation certificate and its costs remain unchanged

Let d=196883, P=WW^dagger be the full rank-d multiplication projector, and sigma=P/d. Preparing sigma, applying the same fixed U to both registers and measuring P defines ideal rejection epsilon(U). With the audit repairs,

$$\epsilon(U)\le10^{-12}\quad\Longrightarrow\quad
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}\le1.151\sqrt{\epsilon(U)}.$$

The sufficient real-orthogonal threshold is 1e-10. These are normalized Frobenius statements, not worst-case channel bounds, optimal thresholds or an efficient extraction algorithm. Note 10 changes none of them.

[Note 06](research/06_probe_access.md) separates access, calibration and statistical costs. At zero calibration error, zero-rejection sampling to the present 1e-12 threshold at 95 percent confidence requires about 3e12 ideal independent trials. Two calls to U do not pay for the special probe preparation and measurement.

[Note 09](research/09_jordan_and_a0_sector.md) combines all three A0 output branches coherently, using the [QQA](research/07_seysen_qqa_block.md) and [XXA](research/08_leech_xxa_block.md) constructions. Its 135774249-instruction ideal-angle hierarchical circuit uses 105 wires, forty outputs and sixty-five clean work wires. Each output uses twenty tagged qubits, not a canonical eighteen-qubit packing. It covers only 299 of 196883 input dimensions and is not a standalone Monster test. All X/Q input sectors, full sigma/P circuits, finite-gate-set synthesis and certified precision remain open.

## Claims, evidence and priority

[STATUS_CURRENT.md](STATUS_CURRENT.md) is the active ledger; `STATUS.md` is the protected import-era record. Notes 01-09, earlier code/results and all archives remain unchanged. Read them with the [VOA audit](audits/voa_extrema_audit.md), [robustness audit](audits/robustness_proof_audit.md) and [integration errata](audits/integration_20260925.md). Note 10 refines, rather than silently rewrites, the historical [priority matrix](audits/priority_matrix.md).

```sh
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
OPENBLAS_NUM_THREADS=1 python checks/verify_normalizer_priority.py
```

Strict historical byte replay and the separate bounded-portability policy remain distinct. Neither archived evidence nor old tolerances are changed to hide a mismatch. The new report agrees locally under normal/-O/-OO. Read the actual baseline/candidate workflow outcomes. Small consistency tests are not formal verification or expert review.

The [current work order](work_orders/CURRENT.md) targets the quantitative correlation-to-symmetry contribution and its precursors, not another isolated circuit. Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, remains unchanged. No large cloud simulation, manuscript, release or outreach is authorized.
