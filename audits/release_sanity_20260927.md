# Pre-release sanity audit

Audited main: `ecd0623e9de41b49754b6ca16dc23752443143af`.
Tree: `20c5252c0bd5e83d6a908ee226e5799e947280fc`.
This report and its diagnostics live on the separate `audit/release-sanity-20260927` branch. Main, scientific sources, recorded results, tolerances, license, and archives were not changed. No release or manuscript was created.

## Verdict

A short reliability and documentation pass is recommended before tagging a polished release. The selected conditional analytic theorem has no newly identified blocking error at the source-interface depth reviewed here. A new implementation edge case does need correction: valid sufficiently small rescalings of an exact Ising pair cause an unhandled exception in the seven-scalar calibration routine. This does not falsify the theorem or exhibit a false-positive certificate.

The audit covers the complete tracked-file inventory, all existing Python checker entry points, the active scientific chain, source interfaces, navigation, and release packaging. It is not a fresh proof audit of every historical research note or pending branch, a comprehensive novelty search, independent human review, or proof-assistant verification.

## Execution and preservation

The [full audit run](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/actions/runs/36268793488), job `108478640211`, executed an isolated harness against a separate clean checkout of the pinned main. The job logs were inspected. Environment: Python 3.13.5, NumPy 2.3.5, one BLAS thread. Local network checkout was unavailable; these are actual GitHub-runner results, not a claimed local full checkout.

| Check | Actual result |
|---|---|
| Tracked-file inventory | 110 files; clean checkout before and after; every tracked file hash preserved |
| Python and JSON syntax | 24 Python files and 28 JSON files parsed without errors |
| Provenance ZIPs | All five passed CRC checks; retained fingerprints unchanged |
| Relative Markdown navigation | 103 links scanned; no missing targets or candidate broken anchors |
| Merge-conflict markers | None found |
| Existing checker entry points | Root verifier plus all 19 Python files under checks, each in normal/-O/-OO: 60 top-level executions |
| Checker outcomes | All 19 checks scripts returned zero in every mode; the root verifier returned nonzero in every mode |
| Current math and teaching | 445 expressions: 80 display and 365 inline; 10 pages; 21 malformed-input controls, eight valid-input controls, and 82 teaching checks passed |
| TeX parser | All 445 exported expressions parsed with MathJax 3.2.1 |

The three selected scientific reports match their saved fingerprints in all three modes:

| Script | Labeled checks | SHA256 of emitted report |
|---|---:|---|
| verify_extraction_core.py | 63 | `1dc55b7cdb8a614af4aaece9099f9bb4282e3583a0032a9050914e5f3873e06d` |
| verify_calibration_and_sharpness.py | 74 | `13a5cc28750faa5c5916f4d9e2717ccdc4cc3957c4911fb98b434dcc522d6ca3` |
| audit_quantitative_core.py | 23 | `2b863f6f9edbc17abed7eaf4bb6bc832cf0f356d44280467a5fcc51ac6b495e2` |

The root strict replay failed with `RuntimeError: prior average toy differs from recorded report under None`. The separate unchanged bounded-portability comparison passed, reporting 98 differing floating-point leaves and no byte identity. The harness deliberately records test failures rather than stopping early: its successful job completion must not be read as all scientific replays passing.

The root snapshot's 76 entries and the current Hopf-style manifest's 12 entries match. Earlier integration manifests describe their frozen historical versions and therefore need not match the current formatted files. This is not evidence corruption and must not be repaired by overwriting those old records.

## R01. Correct the calibration routine's small-scale exception

**Priority: fix before releasing the calibration code as a reusable implementation.**

Location: [checks/verify_calibration_and_sharpness.py](../checks/verify_calibration_and_sharpness.py), `sqrt_bounds`, `Interval.sqrt`, and `calibrated_criterion`.

The fixed dyadic square-root enclosure uses absolute resolution 2^(-80). A strictly positive number can therefore receive a lower square-root bound of zero. Checking that each projected norm is positive does not guarantee that subsequent denominator enclosures exclude zero.

Take two exact orthogonal Ising stress tensors e and f and set w1=s e, w2=s f, with positive s=2^(-k). The seven exact inputs, in the routine's argument order, are

```math
(n_1,n_2,\tau_1,\tau_2,q_1,q_2,m)
=(s^2/4,s^2/4,s/4,s/4,s^3/2,s^3/2,0).
```

These represent the same normalized primary directions for every positive s. Their exact projected norms are N1=N2=(47/192)s^2. At k=39, the cross denominator is

```math
\sqrt{N_1N_2}=\frac{47}{48}\,2^{-80}>0,
```

but its computed lower enclosure is zero. Division then raises `ValueError: denominator interval contains zero`.

The [separate scale audit](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/actions/runs/36269056141), job `108479379862`, ran the unchanged imported module on actual pinned main:

| k in s=2^(-k) | Original routine | Adaptive-precision in-memory control |
|---|---|---|
| -100, 0, 10, 38 | Certified | Certified |
| 39, 40, 60, 100 | Unhandled ValueError | Certified |

The tested source SHA256 remained `d2c16a6c9c01af9d1198cfc2b4459d78966a42c314b8a0575bd37626bcd2eef1` before and after. The adaptive control changed only the imported function in memory; it is not a committed or fully audited repair.

Minimal reproduction from the repository root:

```python
from fractions import Fraction as Q
import sys
sys.path.insert(0, 'checks')
from verify_calibration_and_sharpness import Interval, calibrated_criterion
s = Q(1, 2**39)
values = (s*s/4, s*s/4, s/4, s/4, s**3/2, s**3/2, Q(0))
calibrated_criterion(*(Interval.point(x) for x in values))
```

Recommended repair: adaptive exact square-root precision or rigorously tracked power-of-two input rescaling, plus regression tests for tiny/large scales, independently scaled fields, nonzero-width intervals, and norm intervals approaching zero. A resource limit should return an explicit inconclusive result, not an unexplained exception. Preserve rational outward containment and do not silently change comparison tolerances. Re-run the old controls and record any deliberately revised implementation/report fingerprints separately from historical evidence.

## R02. Provide a clear current verification entry point and environment

**Priority: pre-release usability.**

The root `verify.py` is a seed-era historical replay. It does not execute the selected extraction, calibration, or final core audit. The README lists those scripts separately, but a new reader can reasonably mistake the root command for the complete current verification suite.

Add a current verification wrapper and a short reproduction guide that distinguish current exact checks, documentation checks, historical byte replay, and bounded portability. Keep the historical verifier and its nonzero outcomes honest; do not turn the known mismatch into a strict pass. The published installation path should match the tested environment: `requirements.txt` currently says only `numpy`, while CI pins NumPy 2.3.5 and Python 3.13.5. A dedicated pinned requirements/constraints file is sufficient; pinning NumPy alone does not guarantee cross-platform floating-point byte identity.

## R03. Separate active, archived, and pending material

**Priority: pre-release clarity and source access.**

`docs/RESEARCH_STATUS.md` describes the selected correlation criterion, while `STATUS_CURRENT.md` still calls the earlier gate-testing line the remaining current candidate. The README warns about old ledgers, but direct entry into those files remains confusing. Use one authoritative current status entry and clearly label or index the historical records without erasing them.

Three references need explicit destinations or scope labels:

| Current reference | Problem | Appropriate correction |
|---|---|---|
| `research/two_field_selection.md` in the core's provenance paragraph | Not present on main; associated with pending PR23 | Link the exact historical branch/commit or PR and identify it as provenance, not an omitted core prerequisite |
| `research/extended_six_sevenths_forces_ising.md` in background A05 | Not present on main; pending PR27 | Move to a separate pending-work section or provide a pinned link and retain its unaudited/separate status |
| `audits/readout_scope_audit.md` in background B08 | Not present on main; pending PR22 | Provide an explicit pinned destination and distinguish it from released evidence |

The 103 checked relative links themselves resolve. These are missing inline path references, not broken Markdown hyperlinks. The self-contained core does not require the two ancillary results, and the backlog should not be merged merely to make a file reference resolve.

## R04. State the actual rendering coverage

**Priority: release presentation.**

The ten-page active path passes the current parser. A fresh local check of the supplied preview HTML at 1060- and 430-pixel widths found no page overflow, math error nodes, or collapsed tall displays in 20 page/viewport cases. That is not live GitHub browser validation.

The wider scan still finds the previously rejected macros in all 14 numbered historical research notes and two older audit documents. Thus the active path is checked; the whole repository is not display-clean. Keep the protected original notes and archives byte-identical. Supply clearly identified readable mirrors or an archive index, and label legacy rendering limitations instead of implying that the recent formatting pass covered all research history. Retain the Gaberdiel-first, Yamauchi-secondary physics teaching path and the approved native-math presentation.

## R05. Complete lightweight release metadata

**Priority: useful finishing work, not a mathematical blocker.**

The repository is already public, has no GitHub releases, and currently has an empty description and topic list. `CITATION.cff`, `llms.txt`, and a changelog are absent. Add citation metadata, a concise scope-accurate description/topics, and a versioned release note identifying the selected result, its exact assumptions, and archived work. An LLM/source map can point readers to the active theorem rather than older status files. No DOI, manuscript, new license, or elaborate website is necessary for this cleanup.

## Scientific reconstruction and its limits

The review reconstructed the critical-point-to-Virasoro conversion, charge monotonicity/gap, multiplicity-free tangent estimate, local-to-global compactness step, pair error propagation, calibration identities, and sharpness curve. A separately written local symbolic/rational check verified 21 identities without importing the repository's checker logic. Its largest physical coefficient vector has dimension three. Neither it nor the repository tests proves the imported classifications.

Primary interfaces rechecked: Abe–Lam–Yamada, arXiv:1705.09022, Theorem A.1 (printed page 10 visually inspected); Sakuma, math/0608709, the real-positive setting and Ising overlap data (printed page 2 visually inspected and Theorem 4.4 read in parsed text); Wassermann, 1012.6003, pages 1–2, the FQS unitary-series necessity statement read in parsed text. Requested screenshots of Wassermann page 2 and Sakuma page 14 were unavailable; no successful inspection of those images is claimed. Original classification proofs, comprehensive literature priority, all archived theorems, and all pending branches were not independently re-proved or certified.

The new calibration exception is an implementation limitation, not a reason to enlarge the theorem. No new missing analytic lemma was identified for the selected conditional result. Recommended next work is the bounded R01–R04 repair and R05 packaging, followed by verification of the exact release candidate. Manuscript writing remains on hold.
