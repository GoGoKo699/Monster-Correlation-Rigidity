# Current work order — 25 September 2026, after the first isometry block

Read AGENTS.md, WORKSPACES.md, STATUS_CURRENT.md, the integration errata and research/07_seysen_qqa_block.md. Keep proof validity, priority, and access feasibility separate. Preserve protected historical material; no manuscript, release or outreach is authorized.

## Completed bounded access deliverable

Note 07 converts Seysen's source metric and identity convention, independently reproduces kappa=13858/3, and gives the three exact output weights on A_0 inputs. The normalized A_0 -> Q tensor Q branch has a clean emitted circuit with 1746 instructions in the explicitly stated logical gate library. Its matrix-vectorization subroutine is checked on every valid input basis vector. This is not the complete W, a circuit-synthesis result at 1e-12 accuracy, or a standalone Monster test.

## Next bounded deliverable: A_0 -> X tensor X

Construct or falsify a resource-counted clean implementation of the normalized map

J_X|A> = (1/sqrt(5040)) sum_r (lambda_r A lambda_r^T) |r,r>, for A in A_0,

using one representative of each antipodal Leech short-vector pair. Note 07 proves J_X is an isometry using exact fourth moments. Do not retain a copy of the input A label. Distinguish an isometry implemented on arbitrary coherent input from preparation of each column separately with un-erased labels.

Specify a coherent label convention for all three Leech shapes, including the octad and sign routines. Establish amplitude normalization, workspace erasure, success probability of any postselection, and amplification costs. Use small Golay/coordinate calculations, not a dense Monster tensor. Reusing the source's known Golay/Leech formulas is prior art; the resource-counted quantum construction is the proposed deliverable. It is acceptable to prove an obstruction for one particular loading route, but not to relabel that obstruction as a lower bound for every implementation.

The remaining A_0 -> A_0 tensor A_0 branch, X/Q input sectors and their coherent combination remain open. Do not claim full preparation or measurement from one branch. Keep the optional native-to-full-register encoding cost explicit.

## Priority remains separate

Continue theorem-level comparison of the repaired C11 with fixed-target normalizer and approximate-representation stability literature. Record norms, average versus uniform assumptions, representation dimension and prescribed target image. Original Norton/Zisser proof-depth work remains open; a bibliographic reference or negative search does not complete the comparison.

## Acceptance and verification

Deliver a clean primitive and resource proof, a demonstrated correction/counterexample, or a precise precursor-theorem comparison. Work on an unused branch, record its exact base, and submit a small PR. Do not force-push or overwrite other workspaces.

Run unchanged python verify.py and report its strict outcome. Use the unchanged separately bounded portability inspector for recognized historical floating-report mismatches; never overwrite old results to make them pass. New checks must remain active under normal Python, -O and -OO. State the largest dense matrix, sparse simulation scope and whether the complete Monster is represented.
