# Audit record

Start with [current scientific status](../docs/RESEARCH_STATUS.md). These are
assistant reconstructions and finite checks, not independent human review or
formal verification of the imported theorems.

## Selected quantitative result

| Report | Scope |
|---|---|
| [Final bounded review](final_quantitative_review.md) | Theorem chain, source interfaces, calibration identities and sharpness; dated implementation findings. |
| [Contribution comparison](quantitative_contribution_verdict.md) | Closest inspected prior results and attributed classification endpoint; bounded priority assessment. |
| [Calibration erratum](calibration_scale_erratum.md) | Subsequent small-scale implementation repair, precision limit and preserved historical evidence. |

Use [current reproduction](../docs/REPRODUCIBILITY.md) for commands and report
fingerprints. The [maintenance work order](../work_orders/CURRENT.md) governs
new work on this selected result.

## Earlier gate-rigidity audits

| Report | Audited base | Findings |
|---|---|---|
| [VOA-to-extremum audit](voa_extrema_audit.md) | `0376cbf` | Reconstructs the critical-point dependency; records a source typo and zero-error endpoint corrections. |
| [Robustness audit](robustness_proof_audit.md) | `a450e02` | Records general-lemma parameter restrictions and a character-source correction; retains the Monster specialization with those repairs. |

The [parameter-domain checker](../checks/audit_parameter_domains.py) accompanies
the latter audit. The [archive index](../docs/ARCHIVE.md) separates these older
gate-testing investigations and pending branches from the selected release scope.
