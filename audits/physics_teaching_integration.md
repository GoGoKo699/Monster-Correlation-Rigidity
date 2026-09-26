# Physics-first teaching integration

Read and preservation baseline: `a7ccd55cc729bb1643c668ec6d2085363b17096b`.

## Reader path

The primary teaching anchor is Matthias R. Gaberdiel, *An Introduction to Conformal Field Theory*, hep-th/9910156v2. Hiroshi Yamauchi, *3-transposition groups arising in VOA theory*, 2201.06887v1, is the secondary, selectively used Section 4 anchor. The audience is physicists with quantum-state, inner-product, linear-algebra and elementary-calculus background, not prior VOA expertise.

[The reading map](../docs/learn/README.md) interleaves source selections with five local lessons. Each lesson has two self-checks and explained answers. The sequence covers correlation coefficients; weight-two projection and the mode-index dictionary; internal Ising stress tensors; value-to-vector localization and discrete overlap rounding; and a passing and inconclusive certificate. Seven-scalar calibration and exponent sharpness follow the main criterion. The companion assumptions page separates exact premises, tutorial references, imported proof inputs, and project estimates.

The local explanations are original teaching material, not copied tutorial passages. The relevant official arXiv HTML sections, headings, mode/inner-product conventions, unitary-series discussion and Ising-pair table were inspected for the reading map. No full reconstruction of either review or of the imported classification proofs is claimed. Exact proof interfaces remain those attributed in the unchanged core. No downloaded papers are bundled.

## Preservation

Only three existing files change: README.md gains a reading-path section without changing its prior text; snapshot_manifest.json changes only its README fingerprint and scope description; the quantitative review workflow adds the teaching-layer audit. All other files from the baseline remain byte-identical, including both selected proofs, all scientific checkers/reports, historical integration manifests, archives, license, root verifier and portability policy. The new [manifest](../results/physics_teaching_manifest.json) declares before/after hashes and additions, excluding itself.

The existing historical integration audit is not reinterpreted against new documentation. It is replayed between its original baseline `98d4fe9fdab36d0b10176e0105b1283889c9b227` and the frozen reviewed commit above. A separate teaching audit compares that reviewed commit to the candidate, verifies the exact changed-file allowlist and every other tracked byte, and confirms that removing the new README section recovers the original README. Old reports are neither rewritten nor relaxed to accommodate reader changes.

## Validation and its limits

`checks/verify_teaching.py` checks the worked rational arithmetic, learning-path order, ten self-checks, local links, elementary Markdown/math syntax, and declared source fingerprints. With `--baseline` it also verifies the full tracked-file delta. It is run in normal, -O and -OO modes, with byte comparisons. These checks do not certify browser rendering, teaching effectiveness, or imported VOA theorems.

The workflow separately runs unchanged strict historical replay and unchanged bounded portability on the historical baseline, reviewed baseline and candidate. It also compares the unchanged 63-, 74- and 23-check core reports in all three Python modes. Actual outcomes belong to the job logs: a green aggregate status is not by itself a strict-replay result.

Local work used connector-read sources and hash-verified reconstructions of the three modified baseline files. Network checkout was unavailable in the local container. Local syntax/arithmetic and documentation checks must therefore not be described as a complete local repository replay; the full baseline/candidate comparison runs in GitHub Actions. The PR records its actual job results after execution.

This is teaching and reader maintenance, not new research, a fresh scientific audit, manuscript drafting, a release, or a claim of independent expert review. Manuscript writing remains on hold.
