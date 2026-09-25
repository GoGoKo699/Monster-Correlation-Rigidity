# Claim ledger — 25 September 2026

Initial live main inspected: `a450e022781c4109609ff8f274787942c513df1a`.
Continuation mathematical baseline: `c48f2c7798f0c507d657cb43e9ce7c41d7d5b83d` (PR #2).

**Overall:** exploratory mathematical certification. The bounded VOA audit and eight-obligation robustness audit are assistant reconstructions with explicit errata, not independent human/expert review or formal verification. The [priority matrix](audits/priority_matrix.md) is partial. Note06 specifies access models and costs but constructs no efficient Monster circuit.

## Current claims

| ID | Statement | Basis and present boundary |
|---|---|---|
| C01 | Full Griess automorphism group is Monster | Imported classical theorem, not project novelty |
| C02 | Trace identities, Ising spectrum and axis correspondence | Classical inputs with conversions reconstructed in the audits; foundational literature not all independently reproved |
| C03 | Local cubic sensitivity and pair-test local coefficient | Notes01-02; relevant spectral/local calculations reconstructed in robustness audit |
| C04 | Pair probe/cubic collective stabilizer is phase times Monster | Note02; fixed logical-space unitary model |
| C05 | Three-register unique parent ground state, gap11161/13858 | Note02; reconstructed spectral argument, not scalable frustration-free chain |
| C06 | Global state infidelity controlled by pair rejection | Note02; does not alone bound gate distance |
| C07 | Historical global gate certificate at rejection<=1e-25 | Note03 plus VOA supplement; sufficient threshold superseded by C13; use non-strict rounded endpoint |
| C08 | All-error real/complex ensemble transport | Note04 plus audit localization; matching not automatically a group action |
| C09 | Independent-unitary agreement and product-unitary stabilizers | Note04; not arbitrary channels, feedback, or device independence |
| C10 | At most four conjugate2A generators suffice | Imported DMPZ theorem crediting Zisser; original Zisser proof not obtained |
| C11 | Class mixing yields a nearby orthogonal normalizer | Note05 plus R09: 0<=q<1, 0<=beta<1, t>0, positive integer L, and all remaining printed scalar/group hypotheses. General lemma priority unresolved |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<=(20842432/196883)W(O)^2<=106W(O)^2 | Note05 plus audits; strictness only for positive error. No all-error constant-factor gate equivalence |
| C13 | Complex rejection<=1e-12 (real<=1e-10) implies D_M<=c sqrt(rejection), c=sqrt(1681pi^2/12528)<=1.151 | Eight listed dependencies reconstructed with repairs; no calibration promise, no practical implementation claim |
| C14 | Orthogonal normalizer equals signed Monster | Unique invariant cubic plus full algebra theorem, not a general normalizer-to-group inference |
| C15 | Clean coherent W access implements preparation and P measurement; sigma=J(E) | Note06 elementary reductions; efficient W access not proved; padding/workspace checks required |
| C16 | Trusted prep/effect budget a+b converts observed loss bounds into ideal-loss bounds | Note06; classical binomial coverage under independent identical trials; C13 threshold still required |
| C17 | Ordinary repeated binary SWAP outcomes have d-suppressed signal and quadratic d precision cost | Note06 restricted observation model; not a lower bound for general copy-access protocols or the fixed P |

## Required errata

[Integration summary](audits/integration_20260925.md) records the zero-error inequalities, omitted C11 parameter domains, the source complementary-norm typo, and the centralizer locator (2114-2130 at the pinned GAP commit). No original scientific value, note, data array, or archive is rewritten.

The audits found no blocking gap in the specified Monster proof obligations after these repairs. They did not exhaustively audit every ancillary claim or establish priority.

## Computational scope

The original root verifier executes eight scientific scripts across twelve modes/replays and insists on byte-identical recorded reports. A floating-report mismatch appeared on the GitHub runner; it is not reclassified as a strict pass. `checks/replay_portability.py` reports finite-leaf differences under explicit 5e-12 tolerances for only the two named historical numerical reports. The six pair finite-difference fields are separately checked against their analytic targets with the original 2e-6 tolerance; their cross-platform difference can be up to twice that tolerance. Exact leaves and all other reports remain exact. Original evidence is unchanged.

The parameter-domain witness adds20 exact checks; the access checker adds44 checks, largest matrix81. Historical maximum256 remains the largest replayed matrix. The scripts neither build the Monster nor independently prove its classifications. Consult workflow output for the tested commit, strict replay outcome, and bounded-portability outcome rather than assuming universal byte reproducibility.

## Still not established

Comprehensive novelty/priority; independent specialist correctness review; efficient clean W synthesis, P measurement, group-word finding or nearest-element extraction; practical precision or quantum advantage; comparable worst-case channel certification; general unknown channels, leakage or adversarially correlated uses; untrusted probe preparation/measurement; publication readiness.

The DME and SWAP resource estimates in note06 describe particular access routes and must not be converted into a universal impossibility claim. C15-C17 do not improve C13's thresholds.
