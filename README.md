# Monster Correlation Rigidity

Quantitative identification of the moonshine vertex operator algebra from near-extremal low-energy correlation coefficients under exact structural assumptions. Research by Ruge Lin.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## Start here: a physicist's reading path

Can nearly extremal interaction coefficients identify an exact chiral theory within a specified class? Begin with [the five-lesson learning path](docs/learn/README.md): correlation functions, weight-two geometry, internal Ising structure, quantitative rounding, and a worked certificate. No prior VOA or Monster-group expertise is assumed.

The primary anchor is **Gaberdiel, _An Introduction to Conformal Field Theory_**. Selected parts of **Yamauchi, _3-transposition groups arising in VOA theory_**, provide the secondary algebraic anchor. The [reading map](docs/learn/README.md) interleaves short source selections with local explanations, calculations, and self-checks; it does not require two complete courses. [Assumptions and source roles](docs/learn/assumptions_and_sources.md) separates the physical language, exact premises, imported theorems, and project estimates.

## The result

Work in an **exact** simple unitary, rational, $C_2$-cofinite, holomorphic vertex operator algebra of CFT type, with central charge 24 and no weight-one states. Let $x$ and $y$ be real unit weight-two primaries, and let $f(x)$ be the normalized self-three-point coefficient. Put

```math
M=\frac{46}{\sqrt{141}}.
```

If

```math
f(x),f(y)\ge M-\frac1{32768},\qquad
\left|\langle x,y\rangle+\frac1{47}\right|\le\frac1{128},
```

then the underlying VOA is isomorphic to the moonshine VOA.

The proof extracts nearby exact Ising directions, uses Sakuma's discrete overlap gap to force an orthogonal pair, and then applies the **prior classification theorem of Abe–Lam–Yamada**. The inputs are the specified fields and their coefficients; a Monster action or a preidentified nearby exact axis is unnecessary. The criterion is sufficient: fields satisfying its inequalities identify the VOA within the stated exact class.

The general version allows unequal self-coupling deficits and an explicit overlap-error budget. The square-root field-distance exponent is sharp. For actual real fields of exact weight two, seven scalar intervals can be used to correct stress contamination and normalization before applying the criterion.

## Read the research

| Document | Purpose |
|---|---|
| [Self-contained core proof](research/uniform_extraction_core.md) | Exact hypotheses, uniform localization, pair rounding and attributed classification endpoint. |
| [Sharpness and calibration](research/sharpness_and_calibration.md) | Optimal extraction exponent and certified scalar preprocessing. |
| [Contribution comparison](audits/quantitative_contribution_verdict.md) | Closest inspected prior results, attribution and a scoped priority judgment. |
| [Scientific context and sources](docs/background_claims.md) | Physical interpretation and primary-source roles. |
| [Results and assumptions](docs/RESEARCH_STATUS.md) | Result map and input requirements. |

Coefficient errors are allowed within the stated bounds; the ambient axioms, field grades, and real structure are exact premises. Calibration additionally uses a known stress tensor. The numerical tolerances are sufficient bounds, while the field-distance exponent is sharp.

## Reproduce the certificates

The exact certificates and documentation checks use Python's standard library:

```sh
python verify_current.py
```

The command runs the exact certificates, implementation checks, and documentation
checks in normal, `-O`, and `-OO` modes. The [reproduction guide](docs/REPRODUCIBILITY.md)
contains the full suite, pinned environment, and interpretation of the results.
See [calibration precision](docs/CALIBRATION_PRECISION.md) for the input contract
and precision limit.

## Reference

[Package contents](docs/RELEASE.md) · [Additional research and archive](docs/ARCHIVE.md) ·
[Citation metadata](CITATION.cff) · [AI source guide](llms.txt)

Original code and documentation retain the owner's [MIT license](LICENSE).
Imported mathematical results remain attributed to their authors.
