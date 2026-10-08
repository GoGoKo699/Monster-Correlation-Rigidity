# Results and assumptions

The repository develops a quantitative criterion identifying the moonshine VOA
from near-extremal weight-two correlation coefficients.

## Result map

| Result | Statement | Proof |
|---|---|---|
| Correlation criterion | Two sufficiently near-extremal self-couplings and a controlled overlap force an orthogonal Ising pair and identify the ambient VOA as moonshine. | [Core, Q0–Q4](../research/uniform_extraction_core.md) |
| Sharp exponent | The square-root rate from coupling deficit to field distance is optimal, already in the moonshine VOA. | [Sharpness, section 3](../research/sharpness_and_calibration.md) |
| Calibration | Seven certified scalar intervals remove stress contamination and normalize two real weight-two fields before applying the criterion. | [Calibration, section 2](../research/sharpness_and_calibration.md) |

The classification endpoint is Abe–Lam–Yamada's Theorem A.1. The quantitative
step extracts exact Ising directions and uses Sakuma's discrete overlap gap.
The [source comparison](../audits/quantitative_contribution_verdict.md) identifies
the roles of prior variational methods and classification results.

## Input requirements

The ambient object is an exact simple unitary, rational, C2-cofinite,
holomorphic VOA of CFT type, with central charge 24 and no weight-one states.
The inputs are actual real weight-two fields. The core uses normalized
primaries; calibration also accepts stress-contaminated and unnormalized
fields when the stress tensor is known and projected norms are certified
positive.

Identification is conditional on fields satisfying the coefficient bounds.
The numerical tolerances are sufficient bounds; an inconclusive certificate
leaves the isomorphism type undecided. The sharpness result concerns the
field-distance exponent.

## Verification and learning

The [reproduction guide](REPRODUCIBILITY.md) describes exact finite certificates
and implementation checks. The [calibration input contract](CALIBRATION_PRECISION.md)
specifies interval inputs and the precision limit. The
[proof and source review](../audits/final_quantitative_review.md) records the
assistant's reconstruction and its source depth.

For a guided introduction, use the [physics learning path](learn/README.md).
