# Monster Correlation Rigidity — physical selection

Ruge Lin's project asks whether independently meaningful physical requirements select the Monster, rather than recognizing a symmetry inserted into a chosen tensor. [PHYSICS_STATUS.md](PHYSICS_STATUS.md) is active; the old certification and import ledgers remain unchanged.

## Latest: mixed interactions and null relations

[Note 15](research/15_mixed_action_and_null_relations.md) computes how a weight-two primary field acts between the weight-three primaries produced by pairs. The mixed form is T_e(x,y)=<Bx,e_(1)By>, with primary compression implicit. In the declared extremal class,

$$T_e=\tfrac14\mathcal A_e+\tfrac1{208}G\mathcal D_eG,\qquad G=B^\dagger B=282\Pi.$$

All operators are explicitly constructed from the still-unknown primary weight-two multiplication. The alternating five-field term is **not independently adjustable**: the prior fifth-trace theorem fixes it as (1/52)Alt Tr(R_aR_bR_cR_dR_e). Matsuo's Remark4.3 already states applicability of the trace formulae without an assumed Monster action; this source attribution is now explicit.

If a superposition of pairs creates the zero state, it must remain invisible to every mixed probe. The resulting tensor-only necessary condition is

$$G\mathcal A_e=282\mathcal A_e=\mathcal A_eG.$$

This is a quintic polynomial condition, including lower-degree terms. **Its independence from the preceding fourth- and fifth-trace identities is unresolved.** It is not yet a new selection theorem. Projecting an inconsistent proposed action onto Pi would change the mode-derived answer, not prove consistency.

Small actual CFT controls show that the generic five-form can be nonzero and is essential to null-relation cancellation. They do not obey the extremal fifth-trace constants, so they are not counterexamples to the physical class. The next task is an explicit polynomial implication calculation, not another coefficient of the already closed first-field four-point function.

## Physical scope

The class consists of nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs, no weight-one currents, minimizing positive central charge. These restrictions yield c=24, J and universal contraction identities by prior modular/design/trace results. They are not universal necessities or a demonstrated RG mechanism.

Notes [12](research/12_physical_selection_from_extremality.md), [13](research/13_weight_three_ope_channel.md) and [14](research/14_weight_four_and_four_point_closure.md) establish the current spectral, production-channel and conditional four-point constraints. None reconstructs the complete initial multiplication or proves its automorphism group must be the Monster. No alternative complete CFT is constructed either.

## Evidence

The [62-check verifier](checks/verify_mixed_action.py) uses only integers and fractions. It evaluates 3157 five-label mixed entries, equally many descendant corrections, independent quinary/trace controls and symbolic tree coefficients. Largest square matrix10x10; symbolic system121x15; oscillator cutoff4. The c2/c3 free-boson examples are not extremal c24 theories. No Monster data or full cubic is constructed.

```sh
python checks/verify_mixed_action.py
python -O checks/verify_mixed_action.py
python -OO checks/verify_mixed_action.py
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
```

PR11 was integrated after its actual logs showed strict historical replay failures on both trees and PASS under the unchanged bounded-portability policy. Its65-check exact report passed. A green workflow is not a strict replay claim. The prior [PR9 erratum](audits/physical_integration_replay_erratum.md), archived evidence, old tolerances, notes01-14 and MIT license remain intact. No expert/formal review, comprehensive priority clearance, full physical realization, manuscript, release or outreach is claimed.
