# Claim ledger — 23 September 2026

**Overall status:** exploratory mathematical research with written proofs and computational consistency checks. No independent proof review, comprehensive novelty clearance, or efficient implementation claim.

## Current claims

| ID | Statement | Basis | Status / boundary |
|---|---|---|---|
| C01 | Monster is the full automorphism group of the Griess algebra | Classical literature | Imported theorem; not project novelty |
| C02 | Trace identities, Ising spectrum, axis correspondence | Matsuo/Norton; axial/VOA literature | Imported inputs with explicit normalization conversions |
| C03 | Exact local cubic sensitivity and pair-test local coefficient | Notes 01–02 | Written derivations; scalar and contraction checks, not independent review |
| C04 | Pair probe and cubic ray have collective stabilizer phase times Monster | Note 02 | Written derivation; fixed logical-space unitary model |
| C05 | Three-site parent unique ground state, gap 11161/13858 | Note 02 | Written derivation; not a scalable frustration-free chain |
| C06 | Global state fidelity controlled by pair-test rejection | Note 02 | Written derivation; does not by itself bound gate distance |
| C07 | Uniform-axis global gate result at rejection <=1e-25 | Note 03 | Retained valid checkpoint claim; sufficient threshold superseded by C13 |
| C08 | All-error real and complex ensemble-transport bounds | Note 04 | Written derivation; arbitrary ensemble matching, not automatically group action |
| C09 | Independent-unitary synchronization and product-unitary stabilizers | Note 04 | Written derivation; not arbitrary noise or feedback control |
| C10 | Four conjugate 2A involutions suffice to generate Monster | Di Martino–Pellegrini–Zalesski, Theorem 3.1 | Imported published upper bound, credited there to Zisser |
| C11 | Good-class mixing gives robust rounding to an orthogonal normalizer | Note 05, general lemma | New written project derivation; priority not established |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<106 W(O)^2 | Note 05 | Written average-to-single-symmetry derivation; sufficient small-error range |
| C13 | Rejection<=1e-12 for complex U (1e-10 for real O) implies D_M<=1.151 sqrt(rejection) | Note 05 | Written derivation without calibration promise; no practical sample claim |
| C14 | Normalizer equals signed Monster in the chosen representation | Note 05; unique invariant cubic + full algebra automorphism theorem | Essential additional argument; false for general finite representations |

## Computational evidence

The recorded new exact checker has 35 scalar/character checks. The new small-example checker has 40 tests on A5 and small tensors. All remain active under optimized Python. Root verification also replays six earlier scientific reports. These are consistency tests of arithmetic, normalization, and general finite-dimensional identities. They do **not** test the full Monster tensor or prove imported classifications.

The source character excerpt has 194 columns and only the degree-196883 row plus class centralizers. No complete Monster character table was obtained in this checkpoint. The all-representation class-gap bound is deduced from conjugate generation instead.

## Not established

- Novelty of the assembled theorem, quantitative constants, or general normalizer lemma relative to all prior literature.
- Independent correctness review of the analytic proofs, especially VOA-to-extremum and global-to-local transitions.
- Efficient preparation of the probes, measurement of P, group-word finding, or nearest-element extraction.
- Useful experimental precision, fault-tolerant implementation, or quantum advantage.
- Operator/diamond-norm global certification at comparable constants.
- General channels, leakage, adversarially correlated gate uses, or untrusted preparation/measurement.
- A manuscript submission target or publication-readiness judgment.

## Supersession rules

Do not edit old archives to make historical status text look current. C13 improves a sufficient threshold, not a lower bound or an experimentally observed limit. C12 resolves the earlier small-error matching-to-one-element gap, not an all-error constant-factor equivalence over the entire unitary group.

Every proposed change must identify affected claim IDs, add a proof or counterexample, and state what the tests can and cannot detect.
