# Current claim ledger — 25 September 2026

Latest continuation base: `5aa28ca60c33a1dcd0d271277b4467803fbea05d`.
`STATUS.md` remains the unchanged import-era ledger. Active statements include explicit audit errata.

**Overall:** exploratory mathematical certification, two bounded assistant proof audits, a complete tagged A0-sector circuit, and a bounded C11 precursor comparison. Full W remains uncompiled. Independent expert/formal review, comprehensive priority clearance and practical implementation are not established.

| ID | Statement | Current basis and boundary |
|---|---|---|
| C01 | Full Griess automorphism group is Monster | Imported classical theorem |
| C02 | Trace identities, Ising spectrum and axis correspondence | Classical inputs; audited conversions, not all foundational proofs rederived |
| C03 | Local cubic sensitivity and pair-test local coefficient | Notes 01-02 and robustness audit |
| C04 | Pair/cubic collective stabilizer is phase times Monster | Note 02; fixed logical-space unitary model |
| C05 | Three-register unique parent ground state; gap 11161/13858 | Note 02; not a scalable frustration-free chain |
| C06 | Global state infidelity controlled by pair rejection | Note 02; not by itself a gate-distance theorem |
| C07 | Historical global gate certificate at loss <=1e-25 | Note 03 and VOA supplement; superseded threshold, non-strict rounded endpoint |
| C08 | All-error real/complex axis-ensemble transport | Note 04 and audited localization; matching is not automatically a group action |
| C09 | Independent-unitary agreement and product-unitary stabilizers | Note 04; not general channels, feedback or device independence |
| C10 | At most four conjugate 2A generators suffice | Imported DMPZ theorem crediting Zisser; original Zisser proof not obtained |
| C11 | Class mixing yields a nearby orthogonal normalizer | Note 05 plus R09, including all domain/irreducibility hypotheses. Note 10 matches the equivalence step to GH Lemma 7.1; full quantitative priority unresolved |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<=(20842432/196883)W(O)^2<=106W(O)^2 | Note 05 plus audits; strictness only for positive error, not all-error constant-factor equivalence |
| C13 | Complex loss<=1e-12 (real<=1e-10) gives D_M<=sqrt(1681pi^2/12528)sqrt(loss)<=1.151sqrt(loss) | Eight obligations reconstructed with repairs; no calibration promise or practical implementation claim |
| C14 | Orthogonal normalizer is signed Monster | Unique invariant cubic plus full algebra theorem; not a general normalizer-to-group inference |
| C15 | Clean W access implements preparation/P measurement; sigma=J(E) | Note 06; full efficient W access not proved; padding/workspace checks required |
| C16 | Trusted prep/effect error a+b adds to observed-loss confidence bound | Note 06; independent identical trials and C13 threshold still required |
| C17 | Ordinary independent SWAP outcomes have d-suppressed signal and quadratic-d precision cost | Note 06 restricted model; not a lower bound on general quantum protocols |
| C18 | Source kappa_S=27716/3, project kappa=13858/3; A0 output weights 77/6929,3780/6929,3072/6929 | Note 07; source conventions and invariant-cubic identification remain dependencies |
| C19 | Normalized A0 -> Q tensor Q clean 1746-instruction circuit | Note 07; 45 wires, eleven clean work wires, arbitrary-angle gate library, native encoding |
| C20 | Leech row transfer has squared singular value 1/312 on A0; fourteen-round exact coherent amplification | Note 08; standard methods specialized; different trace mode excluded; no unknown-input reflection |
| C21 | Normalized A0 -> X tensor X clean 57349301-instruction circuit | Note 08; 63 wires, 27 clean work wires; hierarchical finite upper bound, not full simulation or practical efficiency |
| C22 | Normalized A0 -> A0 tensor A0 clean 16957-instruction circuit, one amplification round | Note 09; squared transfer singular value 77/288, flag dilution probability 72/77; both output identities removed. 33 wires, thirteen clean work wires |
| C23 | Complete A0-sector isometry coherently combines all three branches with fixed relative phases | Note 09; 135774249-instruction hierarchical bound on 105 wires. 20-qubit tagged outputs, sixty-five clean work wires. Covers 299 input dimensions only, not full W |
| C24 | Dropping irreducibility from C11 is false even with fixed group/gap and positive separation | Note 10 Proposition 1: A5 x A5 family, D=16k+4, mean error squared 8/D, exact normalizer distance squared 24k/D. Analytic lower bound, not numerical optimization; valid C11 unaffected |
| C25 | A representation-compatible automorphism permits the same z_phi^2/(1-q) rounding bound for reducible representations | Note 10 Proposition 2, averaging and polar completion. Compatibility is an extra condition, not inferred from small error; standard techniques, priority not established |

## Precursor comparison and assumption boundary

C11's averaged-intertwiner equivalence argument directly matches Gowers-Hatami Lemma 7.1. The inspected GH/DCT/BOT approximate-representation statements do not by themselves convert a class assignment into a prescribed-image normalizer. Applying them to the conjugated representation is vacuous because its multiplicative defect is already zero. The discrete mixing/separation argument remains a separately identified step, not an established novelty claim.

For a fixed representation, qualitative convergence to its normalizer follows from compactness and the exact zero set. The new counterexample changes dimension, and the unmatched four-dimensional constituent prevents implementation of a factor-swap automorphism despite vanishing normalized average error. Its averaged intertwiner is nonzero but singular. At k=10000 all repaired C11 scalar conditions hold, but the conclusion with irreducibility deleted fails by a factor 20000. This does not contradict the actual C11, GH's partial-intertwiner theorem, or operator-norm stability.

Original GKR/Kazhdan and Montgomery-Zippin proofs were not obtained; transmitted statements and alternative proofs are labelled as such. Relevant parsed GH/DCT/BOT statements were read, including the direct averaged-intertwiner proof. Browser PDF screenshots failed; no successful visual inspection is claimed. The historical priority matrix is preserved, with note 10 as its more precise successor for C11. The counterexample and compatible extension have not received independent review or comprehensive priority clearance.

## Preserved repairs and access boundaries

The [integration errata](audits/integration_20260925.md) retains zero-error inequality repairs, C11 parameter domains, the external complementary-norm typo and corrected pinned-GAP source locator. Historical text and data are not silently rewritten. The bounded audits did not establish exhaustive proof/priority clearance.

The original vectorization remains valid on its stated input domain. Note 09 separately supplies an all-input-clean basis extension, an explicit Jordan phase correction, and coherent selector erasure. The tagged A0 encoding is not an unpriced conversion to a canonical packed Monster representation. All earlier normalization dependencies and circuit simulation/precision limits remain in force. C24-C25 change no C01-C23 threshold, circuit cost or statistical count.

## Verification scope

The new checker has 96 labeled checks with byte-identical local normal/-O/-OO outputs. A5 is enumerated exactly, including its class spectrum; the k=1 reducible representation and averaged intertwiner are checked in dimension twenty. All large-k witness inequalities are exact rational scalars. Largest dense matrix: sixty by sixty. The full continuous normalizer is handled by an analytic proof, not numerically searched. No dimension-160004 or full Monster matrix is constructed.

Prior verification remains unchanged: parameter-domain 20, probe-access 44, QQA 50, XXA 51, A0-sector 81. The full combined A0 circuit was not simulated; its largest dense coefficient matrix was 299 by 299 and largest coordinate tensor 24^4. Neither its tolerance 1e-10 nor the new small tests establish 1e-12 synthesis precision.

Root verifier, provenance guard and bounded-portability inspector remain unchanged. Strict historical floating-report byte mismatches must be reported separately from bounded numerical agreement; no old report or tolerance is changed. Runtime network checkout failed, so live baseline/candidate verification is established by the read-only GitHub workflow, not inferred from a mounted seed. Read its actual outcome before integration.

Earlier notes 01-09, all previous circuits/checkers/data/results, audit records, provenance, import-era ledger and license remain unchanged.

## Remaining obligations

The next bounded assignment compares the full quantitative pair-correlation certificate with symmetry-testing and tensor/algebra-stability precursors. Qualitative rigidity and the standard averaging step are not sufficient novelty claims. Original Norton/Zisser source-depth work, independent specialist review, and fresh scrutiny of note 10 remain unresolved.

Full W on X/Q input sectors, full sigma/P preparation and measurement, packed-register integration, certified rotation synthesis, practical resources, nearest-Monster extraction, worst-case channel/leakage/adversarial-use certification and untrusted probes remain open. A0 covers only 299/196883 of the full dimension and is not a standalone Monster test. No manuscript, release or outreach is authorized.
