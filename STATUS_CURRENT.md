# Current claim ledger — 25 September 2026

Latest continuation base: `ef7824945e92c12acc3652af21c5b617ce9ca8e8`.
`STATUS.md` remains the unchanged import-era ledger. Current statements use the explicit audit errata.

**Overall:** exploratory mathematical certification. The bounded VOA audit and eight-obligation robustness audit are assistant reconstructions, not independent human/expert review or formal verification. Priority is unresolved. Note 07 compiles one normalized isometry block; it does not implement the full probe.

## Current claims

| ID | Statement | Basis and present boundary |
|---|---|---|
| C01 | Full Griess automorphism group is Monster | Imported classical theorem, not project novelty |
| C02 | Trace identities, Ising spectrum and axis correspondence | Classical inputs with conversions reconstructed in the audits; foundational literature not all independently reproved |
| C03 | Local cubic sensitivity and pair-test local coefficient | Notes 01-02; relevant spectral/local calculations reconstructed in robustness audit |
| C04 | Pair probe/cubic collective stabilizer is phase times Monster | Note 02; fixed logical-space unitary model |
| C05 | Three-register unique parent ground state, gap 11161/13858 | Note 02; reconstructed spectral argument, not a scalable frustration-free chain |
| C06 | Global state infidelity controlled by pair rejection | Note 02; does not alone bound gate distance |
| C07 | Historical global gate certificate at rejection <=1e-25 | Note 03 plus VOA supplement; sufficient threshold superseded by C13; use non-strict rounded endpoint |
| C08 | All-error real/complex ensemble transport | Note 04 plus audit localization; matching not automatically a group action |
| C09 | Independent-unitary agreement and product-unitary stabilizers | Note 04; not arbitrary channels, feedback, or device independence |
| C10 | At most four conjugate 2A generators suffice | Imported DMPZ theorem crediting Zisser; original Zisser proof not obtained |
| C11 | Class mixing yields a nearby orthogonal normalizer | Note 05 plus R09: 0<=q<1, 0<=beta<1, t>0, positive integer L, and all remaining scalar/group hypotheses. Priority unresolved |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<=(20842432/196883)W(O)^2<=106W(O)^2 | Note 05 plus audits; strictness only for positive error. No all-error constant-factor gate equivalence |
| C13 | Complex rejection<=1e-12 (real<=1e-10) implies D_M<=c sqrt(rejection), c=sqrt(1681pi^2/12528)<=1.151 | Eight listed dependencies reconstructed with repairs; no calibration promise or practical implementation claim |
| C14 | Orthogonal normalizer equals signed Monster | Unique invariant cubic plus full algebra theorem, not a general normalizer-to-group inference |
| C15 | Clean coherent W access implements preparation and P measurement; sigma=J(E) | Note 06 reductions; full efficient W access not proved; padding/workspace checks required |
| C16 | Trusted prep/effect budget a+b converts observed loss bounds into ideal-loss bounds | Note 06; binomial coverage under independent identical trials; C13 threshold still required |
| C17 | Repeated binary SWAP outcomes have d-suppressed signal and quadratic d precision cost | Note 06 restricted model; not a lower bound for general copy-access protocols or the fixed P |
| C18 | Source kappa_S=27716/3 and quantum kappa=kappa_S/2; A_0 output weights 77/6929,3780/6929,3072/6929 | Note 07 derives these from 24-coordinate multiplication and Leech fourth moments. Depends on source formulas and base irreducible/cubic identification; not new classical algebra data |
| C19 | The normalized A_0 -> Q tensor Q branch has a clean deterministic 1746-instruction circuit | Note 07 and circuits/seysen_qqa.py; 45 wires, 11 clean work wires, stated basis encoding and arbitrary-angle gate library. No full W, packing, routing or fault-tolerant synthesis included |

## Corrections and source boundaries

The [integration errata](audits/integration_20260925.md) records zero-error inequalities, missing C11 parameter domains, an external-source complementary-norm typo, and the centralizer locator 2114-2130 at the pinned GAP commit. None is silently repaired in historical notes or data. The two audits found no blocking gap in their specified Monster obligations after these repairs, not an exhaustive proof/priority clearance.

Note 07 independently checks the factor-of-two source metric through contraction norms; identity normalization alone would be insufficient to identify the traceless cubic. Its source identification uses the previously audited unique invariant cubic line. PDF screenshot attempts failed; parsed source equations were read, with this limitation stated in the note.

## Computational scope

The unchanged root verifier executes eight historical scientific scripts across twelve replays and requires byte-identical reports. GitHub floating-report differences remain explicit strict failures, not reclassified strict passes. The unchanged portability inspector permits only the two named toy reports under its declared tight tolerance and six finite-difference analytic-target exceptions. It prints differences and leaves evidence unchanged.

The parameter-domain checker has 20 exact checks; note 06's access checker has 44 checks, largest matrix 81. The new note 07 checker has 50 checks, including sparse evaluation of the 21-wire coordinate circuit on all 299 basis inputs, complex superpositions, inverse/uncomputation, and both comparators on all 1024 inputs. Its largest dense matrix is 24 by 24. Twelve Bell pairs are verified separately; the 45-wire state is not expanded. Numerical tolerance 1e-10 and pruning budget 1e-11 are not a certificate of 1e-12 circuit accuracy. Historical maximum matrix dimension remains 256.

All new test outputs agree under normal/-O/-OO in local testing. GitHub workflow output records the actual tested commit and strict-versus-portability outcomes. The current continuation preserves notes 01-06, prior audits, original scripts/data/results, archives, provenance records, original STATUS.md, root verifier, portability policy and MIT LICENSE.

## Still not established

Comprehensive novelty/priority; independent specialist correctness review; full clean W synthesis or P measurement; resource-counted compilation of remaining blocks and their coherent combination; practical precision, fault-tolerant costs or quantum advantage; efficient group-word or nearest-element extraction; comparable worst-case channel certification; general unknown channels/leakage/adversarially correlated uses; untrusted preparation/measurement; publication readiness.

C18-C19 do not change C13's thresholds. The 3072/6929 weight is conditional on a 299-dimensional input sector, not a percentage of the complete isometry. The standalone block is not a Monster membership test.
