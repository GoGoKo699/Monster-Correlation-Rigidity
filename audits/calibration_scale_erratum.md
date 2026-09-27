# Calibration implementation erratum: positive small denominators

Baseline: `ecd0623e9de41b49754b6ca16dc23752443143af`.
Affected code: `checks/verify_calibration_and_sharpness.py`.
The normalized-correlation theorem, calibration identities, and all physical
hypotheses and comparison tolerances are unchanged.

## Reproduced defect

For exact orthogonal Ising stress tensors $e,f$, let $w_1=s e$, $w_2=s f$ with
$s=2^{-39}$. The seven exact scalar inputs in the public function's order are

```math
(s^2/4,\ s^2/4,\ s/4,\ s/4,\ s^3/2,\ s^3/2,\ 0).
```

Each projected norm is $(47/192)s^2$. The positive cross denominator equals
$(47/48)2^{-80}$, but the old absolute $2^{-80}$ grid gives it a zero lower
endpoint. The subsequent interval division raises `ValueError`. This is an
implementation exception on valid scaled inputs, not a false-positive
certificate or a counterexample to the analytic theorem.

The [pinned audit report](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/62cba790ac69b8cf7ad339ad8d0aa21578366770/audits/release_sanity_20260927.md)
and its recorded runner logs preserve the original finding.

## Correction and evidence

`checks/scale_safe_roots.py` refines the dyadic grid using exact numerator and
denominator bit lengths. The [arithmetic proof](../docs/CALIBRATION_PRECISION.md)
shows that every positive accepted radicand receives a positive lower root bound
and an outward enclosure. The public calibration function returns an explicit
inconclusive result at the documented square-root work limit.

`checks/verify_calibration_scales.py` reproduces the old zero-lower-endpoint
calculation without restoring the old bug. It tests the corrected public path
on exact and finite-width independently scaled pairs, very small/large scales,
known stress shifts, near-zero norm boundaries, negative signs, duplicate fields,
impossible couplings, and the resource-limit case. Existing calibration controls
and the adversarial rational/bisection audit are also rerun on the repaired code.

The old 74-check stdout is not overwritten. The refined enclosures change that
output; [current report metadata](../results/current_reports.json) records the
new fingerprint separately. The earlier audit's source-hash expectation is
updated explicitly for the repaired source, while its mathematical and
implementation controls are retained. All historical source bytes remain
accessible at the baseline commit, and all pre-existing saved report files
remain unchanged.

No Monte Carlo or full VOA simulation is used. A false or inconclusive answer
does not establish that the theory differs from moonshine. The certificate
continues to assume the exact ambient class, weight, real structure, and known
stress tensor; it does not infer those premises from the seven numbers.
