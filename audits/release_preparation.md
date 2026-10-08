# Release-preparation integration

Base commit: `ecd0623e9de41b49754b6ca16dc23752443143af`.
Base tree: `20c5252c0bd5e83d6a908ee226e5799e947280fc`.
The repository owner authorized the bounded repairs from the pre-release audit
and modifications to the GitHub-facing documentation. No release, manuscript,
DOI, outreach, or unrelated research-branch merge is included.

## Source and preservation

A read-only GitHub Actions artifact supplied the exact baseline source archive.
Its 110 extracted files reproduced the baseline Git tree above. Local tests
therefore use the actual complete source bytes, not a hand-reconstructed subset.
Network Git cloning in the local container was unavailable.

The release manifest declares every source change and addition and fingerprints
all other baseline files. Protected numbered research notes, provenance files,
original license, historical root verifier, bounded-portability policy, and all
pre-existing saved result files remain byte-identical. The gate-testing and
physical-selection ledgers retain their bodies below new historical banners.
The seed-protected `STATUS.md` remains wholly unchanged; the archive index
identifies it as historical. Canonical proof mathematics is
compared expression by expression; only provenance and implementation pointers
were added to those proofs.

## Calibration correction

The small-scale exception is fixed by scale-aware exact square-root enclosures.
The public function catches a typed precision-work-limit condition and returns
an explicit inconclusive result. The seven-scalar identities, physical premises,
and numerical comparison tolerances are unchanged. The original calibration
controls and independent bisection audit run on the corrected implementation.
The new scale checker covers exact and finite-width independently scaled fields,
stress shifts, tiny and large scales, sign/cap/duplicate controls, and the
resource-limit case. See [the erratum](calibration_scale_erratum.md).

Current exact outputs are recorded separately in
[current report metadata](../results/current_reports.json). Old 74-check and
23-check report fingerprints remain as historical evidence, not falsely
relabelled as the current implementation's output. The extraction output is
unchanged. Normal, `-O`, and `-OO` outputs agree in the local exact-check replay.

## Reader and reproduction repair

The current wrapper separates selected exact checks, documentation checks,
historical strict replay, and bounded portability. A pinned reproduction file,
archive/pending-work index, citation metadata, source map, changelog, and release
scope accompany it. The old integration workflow still executes its complete
chain on the frozen pre-release tree; an additional job checks the real candidate
against that tree and runs the complete current suite. This is not a replacement
of the archived science by a formatting-only check.

The desired About-sidebar description/topics are stored in
[repository metadata](../.github/repository_metadata.json). File creation does
not itself alter GitHub repository settings; no settings-write result is implied.

## Verification boundaries

The exact candidate's CI stdout/stderr is retained as a workflow artifact.
The pull-request validation record contains the actual final runner results,
including strict-versus-portability outcomes; an aggregate green workflow is not
a claim of strict byte identity. Local rendering uses Chromium/MathJax previews,
not GitHub's live browser. The active page inventory is explicit in the release
manifest; legacy rendering limitations remain documented in the archive index.

These are implementation, preservation, and release-readiness checks, not a new
scientific campaign, independent human review, complete audit of the research
backlog, or proof-assistant verification.

## Integration regression caught before merge

The first candidate added a historical banner to the seed-protected `STATUS.md`.
The complete CI suite correctly rejected that edit through the unchanged
provenance verifier. The banner was removed and the exact original file restored;
`STATUS.md` is now also explicitly protected by the current integrity check.
No historical checker, source hash, or numerical tolerance was weakened to
accept the edit. Current readers are directed through the archive index instead.
