# Final bounded review of the quantitative core

26 September 2026. Reviewed head: `6d460bef7041f17cba1658c99d6797ef4b00275c` (PR28). Integration base: `98d4fe9fdab36d0b10176e0105b1283889c9b227`. This is a falsification-oriented reconstruction by the research assistant, not independent human review or proof-assistant verification. Manuscript drafting remains on hold.

## 1. Verdict

No blocking error was found in the selected theorem chain, its calibration formulas, or its sharpness claim at the source-interface depth recorded below. The original two proof files and both original checker sources remain byte-identical. No change to the theorem or its constants was required by this pass.

The bounded result is a sufficient quantitative identification theorem in an EXACT simple unitary rational C2-cofinite holomorphic VOA of CFT type with c=24 and V1=0. The three normalized coefficient inequalities imply an exact orthogonal Ising pair and hence the underlying moonshine VOA by the prior theorem of Abe–Lam–Yamada. Seven calibrated scalar intervals may replace preprocessed primary normalization. The square-root FIELD-DISTANCE exponent is sharp. None of this proves bare-class uniqueness, an optimal decision region, approximate-VOA stability, efficient experiments, or a constructed isomorphism.

For this chosen scope, no additional essential theorem has been identified as missing. The proof, precision boundaries, and evidence supporting eventual background and conclusions are assembled. The directed priority verdict is a reasoned comparison with recorded sources, not a guarantee of firstness or significance. The scientific record remains correctable if a new counterargument or prior theorem is found. The historical research backlog is not certified as a whole by this review.

## 2. Adversarial proof reconstruction

| Obligation | Check and disposition |
|---|---|
| Real cubic and metric | The Dong–Lin PCT convention makes the degree-two product metric-invariant and real on the fixed space. V1=0 and orthogonality to omega give exact primarity. PASS with those premises. |
| Critical point to Virasoro vector | Substituting mu(a,a)=lambda a yields e*e=2e and positive charge r. The internal vacuum grading equals ambient degree on Virasoro monomials. A lowest-degree vector in a proper submodule is orthogonal to all vacuum descendants, so positive definiteness excludes it. PASS; the FQS classification of the resulting irreducible representation is imported. |
| Uniform critical gap | The inverse lambda(r) is strictly decreasing; the positive unitary charges start at 1/2 then 7/10. This supplies a uniform critical-value gap, not an assumption that a maximum already belongs to a known Monster orbit. PASS. |
| Ising tangent spectrum | Sakuma's real-positive framework gives V2=Re plus eigenspaces of eigenvalues 0,1/2,1/16. The core does not assume sigma-type or omit the 1/16 sector. Its tangent bound is independent of multiplicities. PASS. |
| Global entry | A complement of fixed-radius neighborhoods is compact in EACH primary sphere. A boundary maximum has the local loss; an interior maximum is a nontop critical point. No compact moduli space of VOAs and no prescribed nearby exact axis are needed. PASS. |
| Pair rounding | The overlap error is bounded by the SUM of the two chord errors. The strict threshold 3/188 converts exactly to 1/256. A coincident pair cannot pass. PASS. |
| Orthogonality | Positivity gives e_(1)f=0 when the Ising overlap is zero; then ||e_(0)f||^2=2<f,e_(1)f>=0. General normalization is ||e_(0)f||^2=4<e,f>. Only singular OPE terms vanish, not regular products. PASS. |
| Ambient endpoint | ALY Theorem A.1 assumes precisely simplicity, rationality, C2-cofiniteness, holomorphicity, CFT type, c24 and V1=0, in addition to the exact orthogonal pair. Its conclusion is an underlying VOA isomorphism. No generation-by-pair or full-frame assumption is inserted. PASS by application of an imported theorem. |
| Calibration | The identities N=n-tau^2/12 and q_primary=q-tau*n/2+tau^3/36 follow independently from a three-stress algebra and from metric invariance. Positive primary norm is required before division. PASS. |
| Sharpness | In the supplied known-theory curve, loss has positive t^2 coefficient while distance has positive absolute-t coefficient. Separation of exact maxima makes the chosen axis the unique nearest one for small t. The conclusion concerns exponent 1/2, not optimal numerical constants. PASS. |

The proofs use correctly applied source statements; this is not a claim to re-prove FQS, Sakuma, or ALY. In particular the argument is not a proof that all positive commutative metrized algebras are VOAs.

## 3. Implementation audit

The saved 63-check and 74-check reports reproduce in normal Python, -O and -OO with unchanged source bytes. The new `checks/audit_quantitative_core.py` does not replace them. It adds 23 labeled tests including:

- 74,529 rational interval cases, covering sums, differences, products, division away from zero, and powers across zero;
- 45 exact square-root enclosures including zero, exact squares, very small and very large rationals;
- a separately written rational BISECTION oracle, rather than reuse of the implementation's integer-square-root method;
- 36 exact field-pair cases with stress shifts, scale changes and tangent perturbations. All 27 successful certificates also satisfy the independent conservative oracle; nine off-target cases remain inconclusive;
- 36 nested-interval tests: widening the input uncertainty never improves the certification result;
- negative controls for a duplicated field, pure stress, omitted cubic stress correction, a false coupling above the cap, and equality at a strict overlap boundary.

No failing case or required correction was found in these domains. This is not exhaustive testing of arbitrary rational input sizes. Soundness of the operations follows from their outward-enclosure definitions; the cases are implementation controls. The finite tests do not prove the continuum localization lemma or the source classification theorems. The largest physical coefficient vector has dimension three, and no full VOA is simulated.

## 4. Background and claim scope

The existing background ledger supports the eventual abstract, introduction and conclusion at claim level, without drafting those sections. The final read retained the distinction between partition data and product reconstruction, exact structural classification and quantitative input conditions, and theory identification versus measured-state tomography.

The 2026 Carpi–Codogni background source still treats the relevant unrestricted reconstruction/uniqueness issues with explicit conjectural qualifications. It is not used as a new proof premise. A bounded search for corrections to the ALY endpoint and related current uniqueness claims did not yield a directly conflicting primary result; this is not a global absence certificate.

Generic variational idempotent construction, compactness/quadratic growth, Ising overlap quantization, and the exact ambient classification are credited as prior work in `audits/quantitative_contribution_verdict.md`. The calibration formulas and sharp exponent are support for the quantitative statement, not independently exaggerated novelty claims. No submission strategy is recorded here.

## 5. Source interface recheck in this pass

- Dong–Lin, arXiv:1308.2361v1, Definitions2.1–2.2 and Remark2.3: parsed and visually inspected on printed page3. Positive Hermitian/PCT and vacuum normalization checked.
- Wassermann, arXiv:1012.6003v1, printed pages1–2: explicit positive-energy unitary-series statement and its FQS attribution re-read. The requested page2 screenshot failed; no visual inspection is claimed. The original FQS proof is an imported theorem, not independently audited here.
- Sakuma, arXiv:math/0608709v1, real-positive hypotheses and degree-two eigenspace statement on printed page2 visually inspected. Theorem4.4 overlap values re-read in parsed text. The classification proof remains imported.
- Abe–Lam–Yamada, arXiv:1705.09022v4, TheoremA.1 and the tensor-product interpretation of orthogonal Ising subalgebras: printed page10 visually inspected. The orbifold and extension-uniqueness proof remains imported.
- Lam–Shimakura, arXiv:0810.5395, source location for the real orthogonal pair re-opened. The explicit pair is already recorded in the preserved sharpness note; the ambient moonshine construction is not re-proved.
- Carpi–Codogni, arXiv:2605.26972v1, current HTML source and framing consulted. No claim about a full nonchiral CFT or a conformal-net equivalence is inferred.

No downloaded papers or fonts are bundled.

## 6. Integration and preservation

PR28 is merged at the integration base above after the proof review and both prior workflows were checked. The next patch updates only reader/status/work-order text and verification metadata; all mathematical proof/checker files from PR28 and every historical scientific payload remain unchanged. The original PR28 addition manifest is copied to provenance before its current workflow fingerprint is updated. The root snapshot changes only the README and CURRENT records, with all other entries preserved.

The old root verifier and portability policy remain byte-identical. A strict historical floating-report mismatch is still a strict failure even when the unchanged portability comparison passes. Exact new report checks and actual CI outcomes are reported separately in the integration record. No local live-main replay is claimed: runtime Git DNS access failed; source bytes were read through the connection and the supplied archive was replayed locally.
