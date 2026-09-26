# Monster Correlation Rigidity

Quantitative identification of the moonshine vertex operator algebra from near-extremal low-energy correlation coefficients. Research by Ruge Lin.

**Manuscript writing is on hold.** This repository contains research proofs, source comparisons, scope controls and reproducible certificates, not a drafted paper. The [current scientific status](docs/RESEARCH_STATUS.md) records the reviewed scope and remaining boundaries.

## The selected result

Work in an **exact** simple unitary, rational, C2-cofinite, holomorphic vertex operator algebra of CFT type, with central charge 24 and no weight-one states. Let x and y be real unit weight-two primaries, and let f(x) be the normalized self-three-point coefficient. Put

$$M=\frac{46}{\sqrt{141}}.$$

If

$$f(x),f(y)\ge M-\frac1{32768},\qquad
\left|\langle x,y\rangle+\frac1{47}\right|\le\frac1{128},$$

then the underlying VOA is isomorphic to the moonshine VOA.

The proof extracts nearby exact Ising directions, uses Sakuma's discrete overlap gap to force an orthogonal pair, and then applies the **prior classification theorem of Abe–Lam–Yamada**. The quantitative criterion does not assume a Monster action, its multiplication table, or a preidentified nearby exact axis. It also does not prove uniqueness of the bare ambient class: actual fields satisfying the inequalities are additional input.

The general version allows unequal self-coupling deficits and an explicit overlap-error budget. The square-root field-distance exponent is sharp. For actual real fields of exact weight two, seven scalar intervals can be used to correct stress contamination and normalization before applying the criterion.

## Read the research

| Document | Purpose |
|---|---|
| [Self-contained core proof](research/uniform_extraction_core.md) | Exact hypotheses, uniform localization, pair rounding and attributed classification endpoint. |
| [Sharpness and calibration](research/sharpness_and_calibration.md) | Optimal extraction exponent and certified scalar preprocessing. |
| [Final bounded review](audits/final_quantitative_review.md) | Adversarial proof/source/implementation checks and their limits. |
| [Contribution comparison](audits/quantitative_contribution_verdict.md) | Closest inspected prior results, attribution and a scoped priority judgment. |
| [Background evidence](docs/background_claims.md) | Scientific support for eventual framing, without manuscript prose. |

Finite coefficient tolerances are not approximate VOA axioms or a device-independent experiment. Exact grading, real structure, the known stress tensor and the ambient class remain hypotheses. No practical field-finding algorithm, sample complexity, optimal numerical decision region, or explicit implemented isomorphism is claimed.

## Reproduce the selected certificates

```sh
python checks/verify_extraction_core.py
python checks/verify_calibration_and_sharpness.py
python checks/audit_quantitative_core.py
# Each script also runs unchanged with python -O and python -OO.
```

The preserved core reports have 63 and 74 labeled checks. The final review adds 23 labeled controls, including exact interval and independent rational-oracle cases. No full Monster tensor is simulated. Passing finite checks is not a proof-assistant verification of the source theorems or an independent human review.

The historical `verify.py` and `checks/replay_portability.py` are unchanged. Their strict replay and bounded-portability outcomes are reported separately; a green overall job is not a claim of byte-identical historical floating-point output.

## Earlier research and preservation

The earlier [physical-selection ledger](PHYSICS_STATUS.md), [claim ledger](STATUS.md), numbered research notes, immutable archives, code and recorded results remain available as historical research. Their older “current” labels do not supersede [the active work order](work_orders/CURRENT.md) or [the present status](docs/RESEARCH_STATUS.md). Unrelated pending branches are not merged merely to create this reader path.

Original code and documentation retain the owner's [MIT license](LICENSE). Imported mathematical results remain attributed to their authors. Research inquiries and corrections may be sent to Ruge Lin at gogoko699@gmail.com.
