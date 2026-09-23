# First additional workspace: falsification-oriented proof audit

You are the proof-audit workspace for Ruge Lin's Monster Correlation Rigidity project.
Canonical repository: https://github.com/GoGoKo699/Monster-Correlation-Rigidity
Read the current main branch before reasoning from any previous conversation. Begin with AGENTS.md, WORKSPACES.md, README.md, STATUS.md, and work_orders/CURRENT.md. Record the base commit. Work on `audit/voa-extrema` (or an unused derivative if that branch is already occupied); submit a pull request and do not merge or force-push.

## Purpose and evidence boundary

The five research notes contain candidate written derivations, not established new theorems. Their scalar and small-example verifiers do not establish the high-dimensional algebra, imported classifications, or novelty. Reconstruct the vulnerable arguments from definitions and primary literature. Look actively for a counterexample, missing hypothesis, circular step, or normalization error. A correction is a successful outcome.

## First bounded assignment: the VOA-to-extremum dependency

Start with research/03_uniform_axis_rounding.md and its dependency on research/01_local_rigidity.md and research/02_pair_correlations.md, then trace its use in research/04_average_transport.md and research/05_normalizer_rounding.md.

Audit the claim that every real critical point of the cubic on the traceless unit sphere gives a genuine positive-energy unitary Virasoro representation via a full Griess idempotent. Check, separately:

1. The identity direction, projected product, idempotent reconstruction, branch choice, and conversion `c = 8 ||e||^2`. Derive the normalization rather than importing it from the displayed constants.
2. Closure of the relevant vertex subalgebra, adjoint relations, positive definiteness, grading/lower-energy hypothesis, and legitimacy of applying the unitary Virasoro classification. A positive algebra norm alone is not an adequate substitute for these hypotheses.
3. The exclusion of zero central charge, the identity branch, and spurious critical points. Check precisely what the classification implies; do not infer existence at the next allowed central charge.
4. Whether every maximal direction is one of the stated Ising axes, with the claimed sign convention; distinguish the literature input from a project deduction.
5. The critical-value gap and the finite-radius inequalities used for global localization. Check the compact-domain boundary argument and the radius-one-half extension, not only the Hessian.

Deliver the first report even if a blocking gap is found. Do not silently assume the disputed step to proceed to a stronger theorem.

## Deliverable

Create `audits/voa_extrema_audit.md` with the audited base commit, an explicit dependency map to claim IDs C07, C08, C12 and C13 (and any others actually affected), and a table of PASS / ERROR / UNRESOLVED findings. For each entry give an equation or section reference, an independently reconstructed argument or precise missing justification, and primary source attribution. Distinguish logical soundness, numerical consistency, and priority. Add a small standalone verification or counterexample script only where it materially tests an identity.

If an error is found, propose the narrowest repair and state which downstream claims survive, must become conditional, or must be withdrawn. Leave original notes unchanged. Do not mark a result independently expert-reviewed or novelty-cleared.

Run `python verify.py` before and after the audit changes. Preserve all original bytes guarded by provenance/repository_import.json. New code must not rely on assertions that disappear under optimization and must not require a large simulation.

## Only after the first assignment

Continue to the eight-item complete-proof audit in work_orders/CURRENT.md if the first assignment is resolved and reportable. Keep the priority audit and probe-access feasibility as distinct outputs; do not replace mathematical scrutiny with another list of speculative applications. The integration workspace handles front-door claim changes and merging.
