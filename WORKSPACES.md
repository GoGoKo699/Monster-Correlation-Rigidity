# Workspace coordination

Canonical repository: https://github.com/GoGoKo699/Monster-Correlation-Rigidity

## Roles

The main conversation is the integration workspace. It maintains the current claim ledger, checks compatibility of corrections, and integrates reviewed changes. The repository is the shared source of truth; conversation summaries are not a substitute for reading the current branch.

The first additional workspace is a proof auditor. Its assignment is [INDEPENDENT_AUDIT.md](work_orders/INDEPENDENT_AUDIT.md). This means a fresh reconstruction of the argument, not a claim of independent human, expert, or formal review. No additional workspace is assumed to be running merely because this file exists.

## Branch and file ownership

Start the audit on `audit/voa-extrema` from the latest main. Check existing branches and pull requests before creating it; never reset someone else's branch. Record the exact base commit in the audit report. Put new findings in `audits/` and small new checks in `checks/audit_*`. Keep patches to shared front-door files separate for integration.

Do not change LICENSE, the five research notes, original check scripts/data/results, or provenance ZIPs. Correct historical statements through a separately named erratum and update affected claims explicitly. Do not force-push. Use a small pull request to main rather than direct simultaneous edits of main.

## Evidence rules

A passing arithmetic or toy test is not a proof audit. Each audit outcome must identify the exact statement, source or proof, missing assumption or correction, and affected claim IDs. Use PASS, ERROR, or UNRESOLVED with that evidence; do not use PASS merely because a script ran.

Before proposing integration, run `python verify.py`; hash changes must be intentional and documented. New checks should emit their report to stdout and remain effective under `-O` and `-OO`. Do not overwrite recorded reports to hide a mismatch. Include the largest tested dimension and whether full Monster data were used (the existing work uses no full Monster simulation).

Manuscript writing, release creation, DOI registration, researcher outreach, claims of established novelty, and claims of practical implementation are outside this work order.
