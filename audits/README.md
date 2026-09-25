# Audit record

Two assistant proof-audit reports are available. They reconstruct arguments and check named primary-source inputs; they are not independent human/expert review or formal verification. Automated reports certify only their declared arithmetic and toy scopes.

| Report | Audited base | Outcome and scope |
|---|---|---|
| [VOA-to-extremum audit](voa_extrema_audit.md) | `0376cbfb8e8640d1b278b5c55c4815d83f5b6ca1` | Bounded assignment: no blocking gap found in the reconstructed dependency; external complement-norm typo and strict zero-error endpoint errors recorded. |
| [Robustness proof audit](robustness_proof_audit.md) | `a450e022781c4109609ff8f274787942c513df1a` | Completes the eight specified obligations in CURRENT.md; missing general-lemma parameter domains and inaccurate character-source locator recorded. Monster specialization passes with the explicit repairs. |

The [parameter-domain checker](../checks/audit_parameter_domains.py) supplies an exact small-group witness for an unrestricted proof step and a valid-domain control. Run it with normal Python, `-O`, and `-OO`; it is separate from the preserved root verifier. Its largest matrix is 60 by 60, and it uses no full Monster simulation.

The original [bounded assignment](../work_orders/INDEPENDENT_AUDIT.md) and [complete work order](../work_orders/CURRENT.md) remain the scope authorities. Priority and probe-access feasibility remain unresolved. Reports name their base commit, distinguish source inputs from project deductions, and use PASS, ERROR, or UNRESOLVED with supporting reasoning. Historical research notes are not edited retroactively; corrections and downstream claim IDs are recorded in the reports.
