# Monster Correlation Rigidity

Quantitative identification of the moonshine vertex operator algebra from near-extremal low-energy correlation coefficients under exact structural assumptions. Research by Ruge Lin.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

This repository contains research proofs, source comparisons, scope controls and reproducible certificates, not a drafted paper. The [current scientific status](docs/RESEARCH_STATUS.md) records the reviewed scope and remaining boundaries.

## Start here: a physicist's reading path

Can nearly extremal interaction coefficients identify an exact chiral theory within a specified class? Begin with [the five-lesson learning path](docs/learn/README.md): correlation functions, weight-two geometry, internal Ising structure, quantitative rounding, and a worked certificate. No prior VOA or Monster-group expertise is assumed.

The primary anchor is **Gaberdiel, _An Introduction to Conformal Field Theory_**. Selected parts of **Yamauchi, _3-transposition groups arising in VOA theory_**, provide the secondary algebraic anchor. The [reading map](docs/learn/README.md) interleaves short source selections with local explanations, calculations, and self-checks; it does not require two complete courses. [Assumptions and source roles](docs/learn/assumptions_and_sources.md) separates the physical language, exact premises, imported theorems, and project estimates.

For direct proof checking, start with the selected result below and the research documents that follow. The teaching path does not enlarge the theorem's scope.

## The selected result

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

The current exact checks and documentation checks use Python's standard library:

```sh
python verify_current.py
```

The command runs the selected checks in normal, `-O`, and `-OO` modes and
compares current fingerprints. The [reproduction guide](docs/REPRODUCIBILITY.md)
provides the complete inventory, pinned environment, and `--all` command.
It reports historical strict byte replay and bounded portability separately:
a floating-point mismatch remains a strict failure even if the bounded check passes.
See [calibration precision](docs/CALIBRATION_PRECISION.md) for the current
implementation and its explicit precision limit.

No full Monster tensor is simulated. Finite checks do not verify the imported
classification theorems or constitute independent human review.

## Earlier research and preservation

Use [the archive and research index](docs/ARCHIVE.md) for older gate-testing,
circuit, and readout records. It identifies the dated ledgers, including the
unchanged import-era `STATUS.md`. Their older “current” labels do not supersede
[the current scientific status](docs/RESEARCH_STATUS.md). Protected source notes,
provenance archives, and saved evidence remain available unchanged; legacy
mathematics may not render correctly in every GitHub viewer.

[Release scope](docs/RELEASE.md), [the changelog](CHANGELOG.md), and
[citation metadata](CITATION.cff) describe the current research package without
claiming a manuscript, publication, DOI, or tagged release. For LLM-assisted
research, [the source map](llms.txt) points questions to the theorem, its exact
assumptions, teaching anchors, verification, and historical boundaries.

Original code and documentation retain the owner's [MIT license](LICENSE).
Imported mathematical results remain attributed to their authors.
