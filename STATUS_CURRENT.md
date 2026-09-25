# Current claim ledger — 25 September 2026

Latest continuation base: `c51e5ffaf06b90101c70df1d4f5347aa03b9cc14`.
`STATUS.md` remains the unchanged import-era ledger. Active statements include explicit audit errata.

**Overall:** exploratory mathematical certification with two bounded assistant proof audits, and a constructive complete A0-sector circuit in a tagged ideal-angle model. Full W remains uncompiled. Independent expert/formal review, comprehensive priority clearance and practical implementation are not established.

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
| C11 | Class mixing yields a nearby orthogonal normalizer | Note 05 plus R09: 0<=q<1, 0<=beta<1, t>0, positive integer L, and all remaining hypotheses. Priority unresolved |
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

## Repairs and domain distinctions

The [integration errata](audits/integration_20260925.md) retains zero-error inequality repairs, C11 domains, the external complementary-norm typo and corrected pinned-GAP source locator. Neither historical text nor data are silently rewritten. The audits found no blocking gap after their repairs in their stated obligations, not exhaustive proof/priority clearance.

The original vectorization is clean on valid inputs, not all ambient coordinate states. Note 09 supplies a separately named all-input-clean extension for its projection circuit; it does not reclassify the prior valid-domain use as erroneous. The Jordan one-round amplification has a minus sign that is corrected explicitly before coherent combination. Dropping identity projections or tracing out the selector gives a different map.

The tagged output encoding is fully specified for the restricted A0 sector. It is not an unpriced conversion to a canonical packed Monster representation; the other cubic blocks and generator encodings remain open. Source formulas, invariant-cubic identification and the earlier XXA/QQA constructions remain dependencies.

## Verification and source scope

The new checker has 81 labeled checks, identical under local normal/-O/-OO. Every one of the 1024 ambient basis-change inputs and all 299 flat-eigenspace columns are checked. The complete 33-wire Jordan gate list is sparsely simulated on three inputs and its inverse on a complex superposition. Largest dense matrix is 299 by 299; largest coefficient tensor is 24^4 entries. The full 105-wire combined circuit and full Monster tensor are not simulated. Numerical tolerance 1e-10 and pruning budget 1e-11 do not establish 1e-12 synthesis accuracy.

All prior checks retain their scope: parameter-domain 20, probe-access 44, QQA 50, XXA 51. The mounted XXA checkpoint replays locally with hashes matching the pinned dependency records. Network cloning failed; current-baseline/candidate root-verifier outcomes are obtained separately through the read-only GitHub workflow, not inferred from a seed replay.

Root verifier, provenance guard and bounded-portability inspector are unchanged. Strict historical floating-report byte mismatches must be reported separately from bounded numerical agreement; no old report or tolerance is changed to obtain a pass. Earlier notes 01-08, circuits, checks, results, audits, archives, import-era ledger and license remain unchanged.

The indicated Seysen parsed equations and BHMT theorem were read again; BHMT printed page 11 was visually checked. Seysen screenshots failed. The note records that limitation rather than claiming complete primary-proof or visual verification.

## Remaining obligations

Theorem-level priority of the repaired C11 and assembled rigidity result is the next bounded assignment. Original Norton/Zisser proof-depth work and specialist correctness review remain unresolved. Completing an access subroutine does not establish novelty or publication significance.

Full W on X/Q input sectors, full sigma/P preparation and measurement, packed-register integration, certified rotation synthesis, practical resources, nearest-Monster extraction, worst-case channel/leakage/adversarial-use certification and untrusted probes remain open. C22-C23 do not improve C13 or its statistical trial count. A0 is only 299/196883 of the full dimension and is not a standalone Monster test. No manuscript, release or outreach is authorized.
