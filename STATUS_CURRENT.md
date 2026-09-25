# Current claim ledger — 25 September 2026

Latest continuation base: `85215c45005a3241485b99b57b2dc9de63b85702`.
`STATUS.md` remains the unchanged import-era ledger. Active statements incorporate explicit audit errata.

**Overall:** exploratory mathematical certification, bounded assistant proof audits, a complete tagged A0-sector circuit only, and scoped normalizer/pair-test precursor comparisons. Full W remains uncompiled. Independent expert/formal review, comprehensive priority clearance and practical implementation are not established.

| ID | Statement | Current basis and boundary |
|---|---|---|
| C01 | Full Griess automorphism group is Monster | Imported classical theorem |
| C02 | Trace identities, Ising spectrum and axis correspondence | Classical inputs; audited conversions, not all foundational proofs rederived |
| C03 | Local cubic sensitivity and pair-test local coefficient | Notes 01-02 and robustness audit |
| C04 | Pair/cubic collective stabilizer is phase times Monster | Note 02; fixed logical-space unitary model; low-order identification priority remains unresolved |
| C05 | Three-register unique parent ground state; gap 11161/13858 | Note 02; not a scalable frustration-free chain |
| C06 | Global state infidelity controlled by pair rejection | Note 02; not by itself a gate-distance theorem |
| C07 | Historical global gate certificate at loss <=1e-25 | Note 03 and VOA supplement; superseded threshold, non-strict rounded endpoint |
| C08 | All-error real/complex axis-ensemble transport | Note 04 and audited localization; matching is not automatically a group action |
| C09 | Independent-unitary agreement and product-unitary stabilizers | Note 04; not general channels, feedback or device independence |
| C10 | At most four conjugate 2A generators suffice | Imported DMPZ theorem crediting Zisser; original Zisser proof not obtained |
| C11 | Class mixing yields a nearby orthogonal normalizer | Note 05 plus R09, all domain/irreducibility hypotheses. Note 10 matches the equivalence step to GH Lemma 7.1; quantitative priority unresolved |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<=(20842432/196883)W(O)^2<=106W(O)^2 | Note 05 plus audits; strictness only for positive error, not all-error constant-factor equivalence |
| C13 | Complex loss<=1e-12 (real<=1e-10) gives D_M<=sqrt(1681pi^2/12528)sqrt(loss)<=1.151sqrt(loss) | Eight obligations reconstructed with repairs; no calibration promise or practical implementation claim. Note 11 changes no threshold |
| C14 | Orthogonal normalizer is signed Monster | Unique invariant cubic plus full algebra theorem; not a general normalizer-to-group inference |
| C15 | Clean W access implements preparation/P measurement; sigma=J(E) | Note 06; full efficient W access not proved; padding/workspace checks required |
| C16 | Trusted prep/effect error a+b adds to observed-loss confidence bound | Note 06; independent identical trials and C13 threshold still required |
| C17 | Ordinary independent SWAP outcomes have d-suppressed signal and quadratic-d precision cost | Note 06 restricted model; not a lower bound on general quantum protocols |
| C18 | Source kappa_S=27716/3, project kappa=13858/3; A0 output weights 77/6929,3780/6929,3072/6929 | Note 07; source conventions and invariant-cubic identification remain dependencies |
| C19 | Normalized A0 -> Q tensor Q clean 1746-instruction circuit | Note 07; 45 wires, eleven clean work wires, arbitrary-angle gate library, native encoding |
| C20 | Leech row transfer has squared singular value 1/312 on A0; fourteen-round exact coherent amplification | Note 08; standard methods specialized; different trace mode excluded; no unknown-input reflection |
| C21 | Normalized A0 -> X tensor X clean 57349301-instruction circuit | Note 08; 63 wires, 27 clean work wires; hierarchical finite upper bound, not full simulation or practical efficiency |
| C22 | Normalized A0 -> A0 tensor A0 clean 16957-instruction circuit, one amplification round | Note 09; squared transfer singular value 77/288, flag dilution probability 72/77; both output identities removed. 33 wires, thirteen clean work wires |
| C23 | Complete A0-sector isometry coherently combines all three branches with fixed relative phases | Note 09; 135774249-instruction hierarchical bound on 105 wires. Twenty-qubit tagged outputs, sixty-five clean work wires. Covers 299 input dimensions only |
| C24 | Dropping irreducibility from C11 is false at fixed group/gap and positive separation | Note 10: A5 x A5, D=16k+4, mean error squared 8/D, exact normalizer distance squared 24k/D. Analytic minimum, valid C11 unaffected |
| C25 | A compatible automorphism permits the z_phi^2/(1-q) bound for reducible representations | Note 10, averaging and polar completion. Implementability is an extra condition; standard methods, priority unresolved |
| C26 | Pair acceptance is exactly a C2 Bose-support test; its unweighted Choi commutation loss is (2r/d^2)epsilon_P | Note 11, direct specialization/normalization of known support-testing methods. Reflection/probe access remains charged |
| C27 | A known finite-unitary-set tester supplies Monster query upper bounds | Wang Theorem 9 method and Note 11 Gram specialization. Arbitrary collective Choi measurement; no efficient compiler, optimality or practical advantage |
| C28 | A fixed P with finite projective collective stabilizer has some global square-root distance bound | Note 11 Proposition 1, elementary local derivative plus compactness; unknown constant/barrier, not a new stability paradigm |
| C29 | Exact group data alone do not control tangent or global conditioning | Note 11 Propositions 2-3: rank-two complex pair example and separate real binary-cubic example. Not Griess counterexamples; local and global controls distinguished |

## Priority and operational consequences

The pair acceptance/fidelity meaning is a direct specialization of LRW Theorem 3.1. Wang's 2011 finite-set theorem already establishes query-level membership testing for the Monster matrix set. Fixed-order inverse-free correlation testing is also an existing strategy, exemplified by GNW's Clifford test. Existence of such a test, the use of two forward calls per trial, or a square-root exponent without controlled constants is not enough for a novelty claim.

Note 11's conservative Gram benchmark uses max absolute character 4371 and target overlap 4371/196883. At promised distances 0.1,0.01,0.001 its sufficient forward-call counts are 12561,1259151,125918152, with false acceptance <=1/3. The current pair threshold alone gives a sufficient 1098612288668 independent trials, or twice as many U calls, at these distances. These are two upper bounds with different uncompiled measurements, NOT an actual-performance or lower-bound comparison. No query advantage has been established.

For fixed P, finite projective stabilizer gives positive local curvature and a compactness barrier away from that group, hence an unspecified global square-root law. The local prefactor in the Monster proof uses an actual spectral calculation; its explicit global entry threshold still needs the separate global argument. The conditioning examples do not impose the balanced-marginal/isometric-cubic Griess identities. They refute only broader proposed deductions from exact finite symmetry or positive local curvature alone.

The remaining candidate is the specific low-order Griess projector's complex collective stabilizer identification and explicit quantitative conditioning, not a general invention of quantum symmetry testing. Its priority and significance remain unresolved. Notes 10 and 11 refine the protected historical priority matrix rather than overwriting it. A fresh proof audit of their new conditional/obstruction arguments remains appropriate before publication use.

## Preserved repairs and scope

All integration errata remain in force: non-strict zero-error endpoints, C11 parameter domains, the external complementary-norm typo and the corrected pinned-GAP locator. Normalizer and group membership remain different until the invariant-cubic step. Note 10's incompatible reducible family does not falsify valid C11; its positive extension assumes implementability.

Notes 07-09 retain their valid-domain, workspace, relative-phase and native-encoding boundaries. Complete A0 is not complete W, does not prepare full sigma or measure full P, and is not a standalone Monster test. All normalization and primary algebraic dependencies remain. C26-C29 change no C01-C25 constant, threshold or circuit cost.

## Verification and sources

The new checker has 105 labeled checks, identical locally under normal/-O/-OO. Largest square matrix is 81 by 81; largest vector has length 256; a small rectangular Choi matrix is 256 by 6. The Monster Gram matrix and full operators are not constructed. Stabilizer completeness and the compact-orbit arguments are analytic, not numerically searched or formally verified. Numerical tolerance 1e-10 and 90-digit Decimal scalar budgets do not constitute circuit-synthesis or certified interval guarantees.

Previous checker scopes remain unchanged: domain20, access44, QQA50, XXA51, A0-sector81, normalizer-priority96. The largest earlier dense coefficient matrix remains 299 by 299. No combined 105-wire circuit simulation or Monster-tensor simulation is added.

LRW's support theorem/proof, Harrow's generalized-phase-estimation dependency, Wang's finite-set theorem/proof, GNW's relevant theorem/Clifford remark, and PSS's tensor-conditioning statement/proof were read in their stated scope. LRW printed page6, Harrow158 and GNW20 were visually inspected. Wang/PSS screenshot requests failed. Earlier original Norton/Zisser, GKR/Kazhdan and Montgomery-Zippin source-depth gaps remain unclosed.

The unchanged original seed's twelve scientific replays passed locally; network cloning failed, so this is NOT local live-main verification. Actual baseline/candidate replay is supplied separately by the read-only workflow. Strict historical floating-report byte mismatches and the unchanged bounded-portability policy remain distinct; no old evidence or tolerance is altered. Notes01-10, prior code/data/results/audits, provenance, STATUS.md, root verifier, portability inspector and original license remain unchanged.

## Remaining obligations

The next bounded assignment attempts structurally stronger coarse soundness for the Griess pair test, or identifies a precise obstruction to an attempted strengthening. A small numerical retuning of the current threshold is not the target. Full W/P circuits, practical resources and precision, nearest-Monster extraction, worst-case channel/leakage/adversarial-use certification, untrusted probes, comprehensive priority and independent specialist review remain open. No manuscript, release or outreach is authorized.
