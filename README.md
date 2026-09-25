# Monster Correlation Rigidity

Ruge Lin's research project on exceptional finite symmetry as a property of quantum correlations, rather than only a representation fitting into a register.

**Current status:** a source-dependent quantitative rigidity derivation with bounded assistant audits, an ideal-angle circuit for the A0 input sector only, and two rounds of theorem-level precursor comparison. No independent expert review, formal verification, comprehensive novelty clearance, full probe compiler, practical implementation or quantum advantage is claimed.

## Latest: the test is standard; the quantitative conditioning is the question

[Note 11](research/11_pair_test_prior_art_and_conditioning.md) gives an exact reduction of the pair experiment to a C2 Bose-support test: the auxiliary reflection is S=2P-I. Its acceptance/fidelity interpretation is a direct specialization of LaBorde–Rethinasamy–Wilde and earlier generalized phase estimation. Ordinary state invariance is a different property.

Wang's 2011 finite-unitary-set method already implies a query-level membership tester for the represented Monster. An explicit Gram-matrix specialization gives sufficient forward-U budgets 12561, 1259151 and 125918152 for promised phase-normalized Frobenius distances 0.1, 0.01 and 0.001, respectively, at false acceptance at most 1/3 and perfect completeness. Its collective Choi measurement is not compiled or claimed efficient. Two U calls per pair trial must not be presented as a complete two-query property test or a query advantage. The comparison is between sufficient bounds, not lower bounds or practical performance.

For any one fixed projector with finite collective stabilizer modulo phase, a square-root loss-to-distance law with some finite constant follows from local tangent conditioning and compactness. The exponent alone is not a novelty claim. Note 11 supplies two small analytic examples showing what the unspecified constants conceal: one pair projector family loses tangent sensitivity, while a real cubic family keeps uniformly positive tangent sensitivity but develops a distant almost-symmetry. Their exact finite stabilizers are unchanged for all positive parameters. They do not satisfy all Griess hypotheses or contradict the Monster theorem.

The remaining candidate contribution is the specific low-order Griess correlation realization, its full complex stabilizer identification, and explicit local/global conditioning estimates. Whether that quantitative package is new and significant remains unresolved. [Note 10](research/10_normalizer_stability_comparison.md) previously matched the averaged-intertwiner step to prior work and isolated the reducible representation-compatibility obstruction.

## The existing quantitative certificate

Let d=196883, P=WW^dagger be the full multiplication projector, and sigma=P/d. Preparing sigma, applying the same fixed U to both registers and measuring P defines ideal rejection epsilon(U). Read with the audit repairs,

$$\epsilon(U)\le10^{-12}\quad\Longrightarrow\quad
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}\le1.151\sqrt{\epsilon(U)}.$$

The real-orthogonal sufficient threshold is 1e-10. These are normalized Frobenius statements, not worst-case channel bounds, optimal thresholds or efficient nearest-element extraction. Note 11 improves no threshold. Trusted access and the fixed logical-space unitary promise are essential.

[Note 06](research/06_probe_access.md) accounts for access, calibration and sampling. At zero calibration error, zero-rejection sampling to the current 1e-12 threshold at 95 percent confidence takes about 3e12 independent ideal trials. Full W/P access is not supplied by the [complete tagged A0-sector construction](research/09_jordan_and_a0_sector.md): it covers 299 input dimensions only, with a 135774249-instruction hierarchical ideal-angle budget. All X/Q input sectors, complete probe preparation/measurement, packed-register integration and certified synthesis remain open.

## Evidence and coordination

[STATUS_CURRENT.md](STATUS_CURRENT.md) is the active claim ledger; STATUS.md is the protected import-era record. Read historical notes with the [VOA audit](audits/voa_extrema_audit.md), [robustness audit](audits/robustness_proof_audit.md), [integration errata](audits/integration_20260925.md), and newer comparisons. Neither a script pass nor an unmatched search establishes novelty or proof correctness.

The new [105-check verifier](checks/verify_pair_prior_art.py) checks small support/Choi reductions, finite-set Gram identities, conditioning examples and scalar budgets. Largest square matrix: 81 by 81; largest state vector: length 256. It does not construct a Monster-sized operator or numerically establish the analytic stabilizer-completeness/global-orbit proofs. Reports agree locally under normal/-O/-OO.

```sh
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
OPENBLAS_NUM_THREADS=1 python checks/verify_pair_prior_art.py
```

The original root verifier and the separate bounded-portability policy are unchanged. Recognized historical floating-report byte mismatches remain strict failures, not strict passes. No archived report or tolerance is altered. Read the workflow's actual baseline/candidate outcomes.

The [next work order](work_orders/CURRENT.md) targets a structurally stronger coarse soundness estimate, rather than another circuit block or an existence claim already supplied by generic testing. Use [AGENTS.md](AGENTS.md) and [WORKSPACES.md](WORKSPACES.md). The original [MIT license](LICENSE), Copyright (c) 2026 Ruge Lin, and all earlier scientific evidence remain unchanged. No manuscript, release, outreach or large cloud simulation is authorized.
