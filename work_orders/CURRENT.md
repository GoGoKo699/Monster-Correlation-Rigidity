# Current work order: audit the complete robustness argument

The repository is now needed for proof dependencies, source priority, and parallel review. Do not start by adding another application.

## First deliverable: a falsification-oriented proof audit

Read research/05_normalizer_rounding.md in full and trace every imported result through notes 01–04. Check especially:

1. Every real sphere critical point used in the earlier extrema argument really produces the stated positive-energy unitary Virasoro representation; zero central charge and the identity branch are excluded correctly.
2. The projected multiplication's spectral normalization and every factor of d in the averaged matrix/tensor residual agree.
3. The finite-radius localization and matching-completion inequalities are valid globally on their claimed domains.
4. Four conjugate generators really imply the absolute 1/2 class ratio for every nontrivial irreducible representation; the minus-eigenspace argument is included.
5. Conditioning a class walk on the good subset keeps the stated spectral norm despite loss of conjugacy invariance.
6. Word replacement, nearest-point uniqueness, exact multiplication, injectivity, and the nonzero averaged intertwiner are separate justified steps.
7. The orthogonal normalizer is reduced to signed Monster using the unique invariant cubic, not an unsupported general inference.
8. The operator-norm bootstrap uses the actual preliminary Frobenius error and includes centering the logarithm.

Give each item PASS, ERROR with a correction/counterexample, or UNRESOLVED with the exact missing justification. Do not claim independent review when the same assistant merely repeats a proof.

## Second deliverable: priority matrix

Compare the main statements against Norton's original Griess chapter (not yet obtained), Matsuo's trace work, axial-algebra automorphism algorithms, Gowers–Hatami and related stability work, stability of finite subgroups/normalizers, and quantum symmetry testing. Distinguish an old input, a straightforward corollary, a potentially new quantitative statement, and an unresolved priority question. Negative web-search results do not establish novelty.

## Third deliverable: probe-access feasibility

Specify what preparation of sigma and measurement of P would require under a credible gate/access model. Do not infer efficiency from the 18-qubit register size or a constant query count. An honest conclusion that the result is presently a mathematical certification theorem rather than an implementation proposal is acceptable.

## Acceptance

A useful next checkpoint must contain either an actual correction, a sharper independently traceable argument, or a sourced novelty/resource assessment. A longer list of speculative connections is not a substitute.

## Parallel-workspace assignment

The first additional workspace should start with [the bounded VOA/extremum audit](INDEPENDENT_AUDIT.md), under [WORKSPACES.md](../WORKSPACES.md). The integration workspace remains responsible for combining corrections and maintaining STATUS.md. No second-workspace review is yet claimed.
