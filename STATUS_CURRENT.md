# Current claim ledger — 25 September 2026

Latest continuation base: `5428fffc82ccd1ede8a4203b1e73acb6816de289`.
`STATUS.md` remains the unchanged import-era ledger. The active statements incorporate explicit audit errata.

**Overall:** exploratory mathematical certification, two bounded assistant proof audits, and two separate normalized branch constructions. No independent expert/formal review, comprehensive novelty clearance, full W compilation or practical implementation claim.

| ID | Statement | Current basis and boundary |
|---|---|---|
| C01 | Full Griess automorphism group is Monster | Imported classical theorem |
| C02 | Trace identities, Ising spectrum and axis correspondence | Classical inputs; conversions reconstructed in the audits, not all foundational proofs rederived |
| C03 | Local cubic sensitivity and pair-test local coefficient | Notes 01-02 and robustness audit |
| C04 | Pair/cubic collective stabilizer is phase times Monster | Note 02; fixed logical-space unitary model |
| C05 | Three-register unique parent ground state; gap 11161/13858 | Note 02; not a scalable frustration-free chain |
| C06 | Global state infidelity controlled by pair rejection | Note 02; not by itself a gate-distance theorem |
| C07 | Historical global gate certificate at loss <=1e-25 | Note 03 and VOA supplement; threshold superseded by C13, use non-strict rounded endpoint |
| C08 | All-error real/complex axis-ensemble transport | Note 04 and audited localization; matching is not automatically a group action |
| C09 | Independent-unitary agreement and product-unitary stabilizers | Note 04; not general channels, feedback or device independence |
| C10 | At most four conjugate 2A generators suffice | Imported DMPZ theorem crediting Zisser; original Zisser proof not obtained |
| C11 | Class mixing yields a nearby orthogonal normalizer | Note 05 plus R09: 0<=q<1, 0<=beta<1, t>0, positive integer L, and all remaining hypotheses. Priority unresolved |
| C12 | W(O)^2<=3e-9 implies D_M(O)^2<=(20842432/196883)W(O)^2<=106W(O)^2 | Note 05 plus audits; strictness only for positive error, not all-error constant-factor equivalence |
| C13 | Complex loss<=1e-12 (real<=1e-10) gives D_M<=sqrt(1681pi^2/12528)sqrt(loss)<=1.151sqrt(loss) | Eight obligations reconstructed with repairs; no calibration promise or practical implementation claim |
| C14 | Orthogonal normalizer is signed Monster | Unique invariant cubic plus full algebra theorem; not a general normalizer-to-group inference |
| C15 | Clean W access implements preparation/P measurement; sigma=J(E) | Note 06; full efficient W access not proved, padding/workspace checks required |
| C16 | Trusted prep/effect error a+b adds to an observed-loss confidence bound | Note 06; independent identical trials and C13's threshold still required |
| C17 | Ordinary independent SWAP outcomes have d-suppressed signal and quadratic-d precision cost | Note 06 restricted model; not a lower bound on general quantum protocols |
| C18 | Source kappa_S=27716/3, project kappa=13858/3; A_0 output weights 77/6929,3780/6929,3072/6929 | Note 07 from 24-coordinate and Leech moments; source conventions and invariant cubic identification remain dependencies |
| C19 | Normalized A_0 -> Q tensor Q clean 1746-instruction circuit | Note 07; 45 wires, 11 clean work wires, arbitrary-angle gate library, native encoding |
| C20 | Leech row-transfer block has K^dagger K=1/312 on all A_0; 14-round exact amplification removes postselection coherently | Note 08; standard block-encoding/amplification specialization. Trace mode is 1/24 and excluded; no unknown-input reflection |
| C21 | Normalized A_0 -> X tensor X finite clean circuit, 57,349,301 logical instructions on 63 wires | Note 08 and generator; 27 clean work wires, priced static row templates, arbitrary-angle library. No full circuit simulation, fault-tolerant synthesis, full-register packing or efficiency/optimality claim |

## Corrections and literature

The [integration errata](audits/integration_20260925.md) records zero-error inequalities, omitted C11 domains, an external complementary-norm typo and the corrected pinned-GAP source locator. Historical notes/data are not silently rewritten. The audits found no blocking gap after their stated repairs in the obligations examined, not exhaustive proof/priority clearance.

Note 07 fixes normalization by an independent contraction check, not identity norm alone. Note 08 depends on its Leech fourth moment and the explicit source shapes, and spells out the higher-rank source projection needed for coherent amplification. Block encoding, flat-frame algebra and known-success amplification are existing techniques. The original normalizer theorem's priority remains unresolved. BHMT printed pages 10-11 were visually checked in this continuation; Seysen screenshot attempts failed and its indicated parsed equations were read.

## Verification scope

The root verifier, provenance guard and bounded-portability policy remain unchanged. Strict historical byte replay can fail on GitHub floating reports; the separate portability result must be reported distinctly. Neither archive nor recorded old report is regenerated to obtain a pass.

Historical replay maximum matrix dimension is 256. The parameter-domain checker has 20 exact checks, access checker 44, and QQA checker 50. The new XXA checker has 51 labeled checks, all 98280 length-24 Leech rows, exact moment contractions, all 1059 unsigned row trees, 30 specialized signed elementary circuits/inverses, two phase predicates and a rank-three coherent amplification model. Leech rows are not Monster axes. Largest dense operator is 32 by 32; largest dense state vector has length 1024. No N by 299 encoding matrix or full 63-wire amplified circuit is simulated.

Normal/-O/-OO outputs agree locally for the new checks. This runtime cannot clone over the network; the mounted original seed's twelve replays were checked locally. Current baseline/candidate root-verifier outcomes are separately established by the read-only workflow, not inferred from seed replay. A numerical tolerance of 1e-10 is not a 1e-12 synthesis certificate. All notes 01-07, prior audits, old scripts/data/results, archives, import-era ledger, license and portability rules remain unchanged.

## Still open

Complete W and P circuits; the remaining A_0 output branch and all X/Q input sectors; relative phases, clean coherent combination and canonical representation indexing; certified rotation synthesis, practical costs and robust precision; theorem-level novelty and independent specialist review; efficient nearest-Monster extraction; worst-case channel, leakage or adversarial-use certification; untrusted probes and publication readiness.

C20-C21 do not improve C13 or its statistical trial count. The 1/312 transfer probability is not the 3780/6929 squared weight of this branch in W. Both compiled branches concern the same 299-dimensional input sector and are not standalone Monster tests.
