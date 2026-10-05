# Archive and research dispositions

[Overview](../README.md) · [Current scientific status](RESEARCH_STATUS.md) · [Reproduction](REPRODUCIBILITY.md)

## The active path

The released-science scope, when a release is tagged, is the
[quantitative correlation criterion](../research/uniform_extraction_core.md)
and [sharpness/calibration](../research/sharpness_and_calibration.md).
Start learning with [Gaberdiel and the physics lessons](learn/README.md), using
Yamauchi only as the secondary algebraic supplement.

**Only [Current scientific status](RESEARCH_STATUS.md) is authoritative for the
present project.** The older ledgers below describe earlier research directions.
They are preserved as records, not silently reinterpreted as current claims.

## Historical research on main

| Records | What they contain |
|---|---|
| [Import-era ledger](../STATUS.md), [gate-testing ledger](../STATUS_CURRENT.md), [physical-selection ledger](../PHYSICS_STATUS.md) | Dated scope and claim decisions from before selection of the current core. |
| [Notes 01](../research/01_local_rigidity.md), [02](../research/02_pair_correlations.md), [03](../research/03_uniform_axis_rounding.md), [04](../research/04_average_transport.md), [05](../research/05_normalizer_rounding.md) | Protected original local/global gate-rigidity and transport derivations. |
| [Notes 06](../research/06_probe_access.md), [07](../research/07_seysen_qqa_block.md), [08](../research/08_leech_xxa_block.md), [09](../research/09_jordan_and_a0_sector.md) | Access assumptions and bounded circuit constructions, not a complete practical Monster test. |
| [Notes 10](../research/10_normalizer_stability_comparison.md), [11](../research/11_pair_test_prior_art_and_conditioning.md) | Earlier normalizer and support-test comparisons and their limitations. |
| [Notes 12](../research/12_physical_selection_from_extremality.md), [13](../research/13_weight_three_ope_channel.md), [14](../research/14_weight_four_and_four_point_closure.md) | Physical-selection and higher-weight/OPE investigations that are not dependencies of the current core. |
| [VOA audit](../audits/voa_extrema_audit.md), [robustness audit](../audits/robustness_proof_audit.md) | Earlier corrections and their source-interface depth. Consult these before relying on an uncorrected historical statement. |
| [Replay erratum](../audits/physical_integration_replay_erratum.md), [integration dossier](BOUNDED_CORE_STATUS.md) | Recorded verification and integration stages, not current release announcements. |

**Legacy rendering:** all fourteen numbered notes and the two older mathematical
audits retain their original notation. Some macros can fail in GitHub viewers.
Use the source view for those records. The protected notes and provenance ZIPs
have not been rewritten to conceal either display defects or scientific errata.
The active learning/proof path uses the approved native-math display style.

The [license/source notice](../COPYING.md) describes retained archives and
external attribution. Frozen manifests must be checked against their own
recorded versions; do not overwrite them to match a later layout change.

## Disposition of earlier pull requests

The 28 September 2026 review compared PRs #12–27 with the selected core at
`7b9b14dc5d2a693b8607332089407f11a08f84a9`. The table records their dispositions
and fixes each research record to its inspected head. Branches and commits are
retained. Closing a proposal does not erase its files or discussion; a separate
research result can be revisited through a new, focused integration.

**Archived** means outside the selected quantitative criterion. It is neither
a rejection of the mathematics nor a fresh proof or reproducibility audit of
every archived result. No new theorem or scientific checker from these branches
is needed by the current core.

| PR | Disposition | Fixed record | Reason |
|---|---|---|---|
| [#12](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/12) | Rejected as written | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/b0d7224bbc20d0d8aeb217e1caf4014fd3c298d1/research/15_mixed_action_and_null_relations.md) | The proposed mixed-action formula and necessary null relation fail on the explicit zero-state counterexample in PR13. |
| [#13](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/13) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/30279b1b0e030f5ab23f4e35e3cb85a01fa9c996/research/15_mixed_action_normalization_audit.md) | Counterexample to PR12; preserved as corrective evidence. Its old integration edits would restore superseded status and work-order text. |
| [#14](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/14) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/e608dec00a26c714a68ec33b9463faadacdce573/research/16_mixed_trace_reconstruction.md) | Separate reconstruction of the corrected mixed coupling and alternating fifth trace; not a dependency of the current core. |
| [#15](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/15) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/5ab0ade8e5c99580a675c196c7c8342095146548/research/17_mixed_response_closure.md) | Separate scalar-response redundancy and operator-isotropy result in the earlier higher-OPE programme. |
| [#16](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/16) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/9254b954ed7e3d1fb2033175e66552fdf0092823/research/18_primary_three_bracket.md) | Separate primary-three interactions and compatibility analysis; its later independence question is addressed in PR21. |
| [#17](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/17) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/fde92a04964def3a12c5a8cc75362c4fced96c73/research/19_odd_mode_completeness.md) | Separate odd-operator completeness result; used by later exploratory branches, not by the selected theorem. |
| [#18](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/18) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/0b3a13d4ab64a0b5e106796530126e9d43f8cb47/research/20_forced_weight_five_channel.md) | Separate forced weight-five interaction result; its physical channel identification uses PR17. |
| [#19](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/19) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/b1beb68f18bd64e31b6efc21d17bea3b21c8e644/research/21_canonical_thermal_field.md) | Separate canonical weight-twelve thermal field and response calculation. |
| [#20](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/20) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/a6badedc1046d05c8c3a7bb5c78d1982d296a234/research/22_thermal_silence_complete_readout.md) | Separate complete-readout and thermal-silence result; its odd completeness uses PR17. |
| [#21](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/21) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/71f09cedc8e0d846409ca4ea3614e46bbf9f833a/research/24_operator_factorization_closure.md) | Separate positive-norm redundancy certificate for an earlier operator equation; the current proof does not need fifth-order trace inputs. |
| [#22](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/22) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/d2b85266d4273ae7c6ce32d87e0b6060a881b87e/audits/readout_scope_audit.md) | Separate general-readout scope correction; current main already excludes a Monster-specific readout claim. |
| [#23](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/23) | Superseded | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/ac5acad7cad4a63f0d879e4ea716f5a27c3bcd61/research/two_field_selection.md) | The quantitative two-field argument is consolidated and extended in the current core and its sharpness/calibration companion. |
| [#24](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/24) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/367eb4cff1bb6ebc3f5e99182cd10391d5106b5d/research/ising_partner_landscape.md) | Separate Ising-partner landscape obstruction to local ascent; the current theorem does not propose such a search algorithm. |
| [#25](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/25) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/0a2dbada7b739396934d5042da7a37880e15816a/research/potts_local_maximum.md) | Separate extended-Potts local-maximum realization and supplied escape curve; consistent with the selected criterion. |
| [#26](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/26) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/18c383925498f349dd395fb2fbd2b445abcf58b0/research/mixed_square_extraction.md) | Separate conditional mixed-square construction and Ising-free subtheory control; preserve the latest root-based checker correction at this head. |
| [#27](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/27) | Archived separate research | [Record](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/576fd31b53862d0b7667a723330ae27c859cc774/research/extended_six_sevenths_forces_ising.md) | Alternative sufficient hypothesis using an actual extended six-sevenths subalgebra; forces one Ising vector, not the orthogonal pair required at the endpoint. |

**Normalization warning:** PR12's proposed condition is rejected as written,
not merely deferred. PR13 supplies a zero-state counterexample in the known
moonshine algebra. PR14 separately reconstructs the corrected mixed coupling
and alternating fifth-trace component; it does not reconstruct every term of
the full fifth trace. The selected core uses none of these disputed fifth-trace
inputs. The lower-order results in historical Notes 12–14 are not rejected by
this counterexample.

PR26's fixed record uses its actual latest head `18c3839`, including the
root-based checker correction. Its original PR description names an earlier
head; the fixed link above is authoritative for this archival disposition.
The import-era `STATUS.md` is protected by the original seed verifier and remains
byte-identical, including its dated headings. Use this index and the current
scientific-status page rather than interpreting its old “current” label as a
statement about the release candidate.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
