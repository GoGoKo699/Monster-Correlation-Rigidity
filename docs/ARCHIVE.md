# Archive and pending-work index

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

## Pending branches are not released dependencies

The links below point to fixed commits, so they remain unambiguous even if a
branch later changes. They identify provenance or separate work, **not a review
or a merge of those proposals**.

| Record | Fixed destination | Relation to the current theorem |
|---|---|---|
| Earlier two-field bridge, PR23 | [Selection note](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/ac5acad7cad4a63f0d879e4ea716f5a27c3bcd61/research/two_field_selection.md) | Historical provenance. The active core states its own proof and does not require this unmerged file. |
| Extended-six-sevenths proposal, PR27 | [Existence proposal](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/576fd31b53862d0b7667a723330ae27c859cc774/research/extended_six_sevenths_forces_ising.md) | Separate proposed sufficient hypothesis; not a premise or certified part of the release scope. |
| General-readout scope audit, PR22 | [Readout comparison](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/blob/d2b85266d4273ae7c6ce32d87e0b6060a881b87e/audits/readout_scope_audit.md) | Separate readout question; not the Monster-specific identification claim selected here. |

Other pending pull requests remain separate as well. The release is not a
certification of the full research backlog. Manuscript writing remains on hold.

The import-era `STATUS.md` is protected by the original seed verifier and remains
byte-identical, including its dated headings. Use this index and the current
scientific-status page rather than interpreting its old “current” label as a
statement about the release candidate.
