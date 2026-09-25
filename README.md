# Monster Correlation Rigidity — physical selection

Ruge Lin's project asks whether independently meaningful physical conditions
select the Monster, rather than merely recognizing symmetry in an engineered
tensor. [PHYSICS_STATUS.md](PHYSICS_STATUS.md) is the active ledger. The former
certification and import ledgers remain unchanged.

## Latest: an apparent selection condition fails a physical sanity check

[The mixed-action normalization audit](research/15_mixed_action_normalization_audit.md)
finds a blocking error in the unmerged PR12. Its proposed additional null-state
condition fails in an explicit sector of the actual Griess algebra: a pair that
creates the zero state is assigned a nonzero matrix element. The correct
matrix element is zero. This is not a new physical restriction excluding the
known Monster theory; it invalidates that proposed restriction.

The audit localizes a five-form normalization conflict in the retrieved
Matsuo arXiv v1. Direct mode evaluation gives48 for a normalized alternating
five-form, while the full Griess-block trace gives1248: ratio26, not52.
All120 distinct permutations agree with26 in the tested trace-polynomial shape.
The source really prints52 and a normalized1/120 definition; its appendix is
also inconsistent when literally specialized. The journal version has not
been checked. A corrected universal trace theorem is not claimed solely from
this finite witness.

With a reconciled coefficient26, the same formal derivation would give

$$T_e=G\mathcal D_eG/104,$$

which respects zero-state relations automatically. This conditional repair
removes the purported extra selection test. The exact known-algebra
counterexample is established; the all-input trace repair remains a separate
proof/source obligation. PR12 stays unmerged, with its branch and evidence
preserved and a blocking audit comment.

## What remains established on the physical track

[Note12](research/12_physical_selection_from_extremality.md) studies the declared
class of nontrivial unitary strongly rational bosonic holomorphic current-free
chiral CFTs of minimum positive central charge. This is a restricted criterion,
not a universal physical law or an established RG mechanism. Prior modular and
trace results give c=24, J and normalized low-energy OPE constraints without
assuming a Monster action. The complete unknown multiplication has not been
identified with the Conway–Griess algebra.

[Note13](research/13_weight_three_ope_channel.md) and
[Note14](research/14_weight_four_and_four_point_closure.md) derive generated
weight-three/four channels and conditional closure of the external-weight-two
four-point tests. Those results do not establish uniqueness. The new audit
changes none of their statements, the earlier certification constants, or
circuit costs; it prevents an unmerged five-field normalization error from
being added as a physical-selection premise.

## Evidence and next step

The [37-check exact audit](checks/verify_mixed_normalization.py) uses at most
6x6 matrices and streams98280 length-24 Leech rows. The mode calculation uses
three active Heisenberg coordinates; the trace accounts for all A/X/Q blocks
of the actual196884-dimensional algebra. No full multiplication matrix or
Monster group matrices are built. Integer/fraction reports agree locally under
normal Python,-O,-OO. Small calculations do not replace source-theorem review.

```sh
python checks/verify_mixed_normalization.py
python -O checks/verify_mixed_normalization.py
python -OO checks/verify_mixed_normalization.py
# Unchanged historical replay:
OPENBLAS_NUM_THREADS=1 python verify.py
OPENBLAS_NUM_THREADS=1 python checks/replay_portability.py
```

[CURRENT](work_orders/CURRENT.md) requires reconciliation of the universal
normalized fifth trace before using the candidate mixed formula or searching
for independent higher constraints. The goal remains physical selection, not
an endless series of coefficient matches. Earlier research, audits, code,
results, status records, archives, the root verifier, portability policy and
original MIT license are preserved. No independent specialist/formal review,
comprehensive novelty clearance, full probe compiler, manuscript, release or
outreach is claimed. Read each workflow's strict and bounded outcomes
separately; the PR9 reporting erratum remains in force.
