# Proof-review protocol

Record the reviewed commit and the exact statement under review. Reconstruct
the argument from its hypotheses and cited primary sources, checking
normalizations, dependencies, circularity, and counterexamples.

For each finding, record PASS, ERROR, or UNRESOLVED with the supporting proof,
source passage, or counterexample and the affected claim. Identify the source
version and inspection depth. Finite arithmetic checks support the review;
analytic and imported classification arguments require their own evidence.

Use a separate branch and focused pull request. Follow [AGENTS.md](../AGENTS.md)
and [the maintainer workflow](../WORKSPACES.md), preserve existing evidence, and
run the checks in [the reproduction guide](../docs/REPRODUCIBILITY.md). Describe
assistant review accurately as assistant review.
