> Integration note (26 September 2026): PR28 is now merged. The dated text below records its pre-integration stage. See [current scientific status](RESEARCH_STATUS.md) and [the final bounded review](../audits/final_quantitative_review.md) for the active disposition.

# Quantitative correlation criterion: research entry

Manuscript writing remains on hold. This page is an entry to the completed proof records and their stated review boundaries, not manuscript prose.

The selected claim is a sufficient, uniform criterion in an **exact** unitary rational C2-cofinite holomorphic VOA of CFT type with c=24 and no weight-one states. Near-maximal self-three-point coefficients of two actual real unit primary fields, together with a near-orthogonal-Ising overlap, force exact orthogonal Ising subalgebras and then the ambient moonshine VOA by a prior theorem.

Read the [self-contained theorem and proof](../research/uniform_extraction_core.md) first. The [sharpness and calibration note](../research/sharpness_and_calibration.md) proves the optimal field-distance exponent and gives exact stress/norm correction for seven scalar inputs. The [direct contribution comparison](../audits/quantitative_contribution_verdict.md) credits the older variational and classification results and states the bounded priority verdict. The [background claim ledger](background_claims.md) separates evidence for eventual framing from draft prose. The [status map](BOUNDED_CORE_STATUS.md) records remaining review and integration work.

The theorem does not prove that every theory in the bare class is moonshine, infer exact axioms from experimental data, find the relevant fields efficiently, or establish optimal numerical tolerances. Its square-root extraction exponent is sharp; the new calibration result retains exact grade-two, real-field, and known-stress assumptions. All source classification theorems remain attributed.

## Reproduction

```sh
python checks/verify_extraction_core.py
python -O checks/verify_extraction_core.py
python -OO checks/verify_extraction_core.py
python checks/verify_calibration_and_sharpness.py
python -O checks/verify_calibration_and_sharpness.py
python -OO checks/verify_calibration_and_sharpness.py
```

The first report has63 labelled checks; the second has74. Compare the exact stdout hashes with `results/quantitative_core_reports.json`. These are rational/polynomial controls, not a full Monster simulation or formal verification of the source theorems. The standalone checkpoint also includes the complete emitted JSON reports and a file-hash verifier.

The additive candidate preserves every pre-existing main file, including historical notes, data, root verification, portability policy and the original MIT license. No unrelated pending branch is integrated by this reader path. Refer to the actual integration record and workflow logs for strict historical byte replay versus bounded portability; a green job alone is not evidence of strict byte identity.
