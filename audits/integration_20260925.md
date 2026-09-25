# Integration errata and evidence boundaries

25 September 2026. Main inspected at a450e022781c4109609ff8f274787942c513df1a; robustness report inspected at c48f2c7798f0c507d657cb43e9ce7c41d7d5b83d. This integration updates current summaries only. Notes01-05, prior audits, original data/results/checkers, provenance archives and LICENSE remain byte-identical.

## Mathematical corrections applied to current statements

1. **Zero endpoint (V13).** At U=I all errors vanish. Any rounded coefficient comparison multiplied by that error must be non-strict at zero. Use D_M^2<=(20842432/196883)W^2<=106W^2 in C12 and D_M<=c sqrt(epsilon)<=1.151 sqrt(epsilon) in C13. Strict numerical comparisons of constants remain correct; strict product comparisons require positive error. No constant or sufficient threshold changes.
2. **Normalizer domains (R09).** State 0<=q<1, 0<=beta<1, t>0, and L a positive integer, alongside all other hypotheses in note05. The A5 counterexample falsifies an unqualified intermediate walk step with beta=2; it does not falsify the Monster specialization or the corrected lemma conclusion.
3. **Source locator (R10).** The retained centralizer array is at lines2114-2130 of the pinned GAP source, not the incomplete historical locator. The character row is at2264-2270. All194 values of each array match; do not alter the data to correct its locator.
4. **External source norm (V12).** The complementary idempotent's squared norm in the HS form is47/32, not3/2. The audit explains the normalization and why the source uniqueness argument survives. This is an external-source erratum, not evidence of changed project constants.

The bounded VOA and eight-obligation audits reconstruct the specified chain after these repairs. They do not constitute independent human/expert review, exhaustive verification of all ancillary claims, or novelty clearance. The current README's historical statement that no audit had been completed is superseded.

## Access convention

In note06 section2, filtering a maximally mixed input to obtain sigma presupposes the **Lueders projective instrument** rho -> P rho P on the accepted outcome. An oracle for the effect P alone fixes the probability, not the postselected state. The coherent extension construction supplies the required instrument. This distinction is part of the access specification, not a generic consequence of knowing a POVM effect.

## New work and verification policy

Note06 and the priority matrix supply an access-model assessment and a limited primary-source comparison. They do not extend C13 to arbitrary noise or improve its sufficient threshold. Source-read depth is stated in those files.

A read-only GitHub workflow checks the fixed audit baseline and the candidate. Initial strict replay on the runner failed at the historical average toy report, even after specifying the recorded Python/NumPy versions. The unchanged root verifier correctly reports a byte mismatch. The original seed's twelve scientific replays reproduce exactly in the local Python3.13.5/NumPy2.3.5 environment.

To inspect rather than erase numerical portability differences, a separate checker runs every preserved scientific script, requires its original internal checks to succeed, and compares reports. Only floating leaves in the prior average-toy and pair-toy reports may differ, with atol=rtol=5e-12; every difference is printed. Six specific finite-difference fields in the pair-toy report instead require both recorded and observed values to satisfy the original 2e-6 analytic-target test, with the analytic targets themselves agreeing under the default tight tolerance. Their cross-platform difference is bounded by twice the original target tolerance plus the target-comparison allowance. This exception follows from the preserved script's finite-difference test (step 2e-4), not a tolerance inferred from a desired passing result. The initial uniform 5e-12 comparison rejected this amplified numerical difference; that failure is retained in the workflow history. Keys, sequence lengths, types, strings, booleans and integers are exact, as are all reports outside the allowlist. Nonfinite values or larger differences fail. This is a separate bounded numerical comparison, not byte-identical replay. The workflow retains a warning on strict failure and gates numerical agreement and new tests separately. Recorded reports and verify.py are not edited to suppress the failure.

The new access checker records44 tests, including arbitrary small isometry preparation, inverse measurement, Choi equality for a symmetric tensor, SWAP contraction, controlled reflection, calibration and a padded-subspace counterexample. Its largest matrix is81. It remains active under optimized Python. No full Monster simulation or efficient isometry construction is claimed.
