# Workspace instructions

Read README.md, STATUS.md, and work_orders/CURRENT.md before extending the project.

## Fixed boundaries

- The project belongs to Ruge Lin and develops the Monster-related idea behind arXiv:2209.15025. It is a new research direction, not a defense of the old embedding observation.
- Preserve the owner's LICENSE. The MIT LICENSE from initial commit 40cbbbe04247c1f816cc2c7f8106264ecff2b253 must remain byte-identical.
- Preserve all files under provenance/*.zip and the historical research notes 01–05 byte-for-byte. New work may correct them through an explicit erratum, never through a silent archival rewrite.
- Never present scalar or toy verification as a full Monster simulation, proof assistant verification, novelty audit, or independent expert review.
- Keep state fidelity, axis-ensemble transport, normalized Frobenius gate distance, and worst-case channel distance distinct.
- Keep local promises and sufficient global thresholds explicit. Large constants and resource assumptions belong in public-facing theorem statements.
- Use primary sources. Treat inputs from the existing notes as derivations to audit, not unquestionable facts. Do not invent an external review or cite an unseen source as read.
- Do not conflate normalizing a finite group with belonging to it. Note 05 includes the necessary Monster-specific invariant-cubic step.
- No large cloud/network simulations are needed or authorized by this research plan.

## Workflow

Work on one claim or audit obligation at a time. Record the mathematical change and its dependencies. Run python verify.py after changes. Update snapshot_manifest.json only after an intentional, described source change; never rewrite recorded evidence merely to suppress a failure.

External references and mathematical data retain their source attribution. Do not bundle downloaded papers or font files. Do not publish a manuscript or contact researchers without the user's instruction.

If another workspace is active, use separate branches and small commits. Do not force-push or overwrite another workspace's unmerged work. The canonical remote is https://github.com/GoGoKo699/Monster-Correlation-Rigidity. Read WORKSPACES.md and use work_orders/INDEPENDENT_AUDIT.md for the first second-workspace assignment. A second assistant workspace is not independent human or expert review.
