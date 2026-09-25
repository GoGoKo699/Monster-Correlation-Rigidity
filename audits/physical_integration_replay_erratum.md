# Correction: PR9 historical-replay outcome

Date:25 September2026. Recorded during the continuation from `514c11d54ac5d743767ec631f55d258665a5501b`.

The integration comment5828517436 on PR9 and the message of merge commit514c11d54ac5d743767ec631f55d258665a5501b incorrectly said that workflow36106639219 reproduced all historical reports byte-identically on both trees. The same error said `all_reports_byte_identical=true`.

The actual logs of job107980561128 show the following for BOTH the pinned baseline109e1cffd3c61f374635fec0a36f97e972d373e5 and its PR candidate:

- `RuntimeError: prior average toy differs from recorded report under None` in unchanged verify.py.
- `all_reports_byte_identical: false` in the separate replay_portability.py report.
- `PASS under explicitly bounded portability comparison` under the unchanged policy.

The comparison reports75 differing float leaves in the historical average toy (maximum absolute difference1.7763568394002505e-15), and23 in the historical pair toy (maximum6.938893903907228e-08, arising in the pre-existing finite-difference exception). These were not strict byte matches. The new37-check integer/fraction report reproduced, and the overall CI job completed successfully under its explicitly permitted portability fallback.

Corrected top-level PR9 comment5828944938 records this distinction. The merge was not based on a new scientific-check failure, but its outcome was incorrectly described. No change to source data, archived reports, tolerances, or theorem follows from correcting that reporting error. The immutable commit text and old evidence are left intact; this erratum supersedes the incorrect verification wording.

For subsequent integrations, an overall green workflow is not sufficient evidence of strict replay. The original strict output and the separate portability report must be inspected and reported individually.
