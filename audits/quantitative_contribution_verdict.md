# Correlation criterion and prior theorems

This comparison concerns the quantitative identification criterion in the [core proof](../research/uniform_extraction_core.md). Among the primary-source statements listed below, no result was identified with both the same finite-coefficient input and the same exact structural output. This conclusion is limited to the inspected statements and is revisable if a closer source is supplied.

## 1. The criterion and its inputs

Fix an exact simple unitary rational C2-cofinite holomorphic VOA of CFT type with c=24 and V1=0. Given two real normalized weight-two primaries, their two self-three-point coefficients and one cross-two-point coefficient satisfy explicit sufficient inequalities. These force nearby exact Ising directions, then an exact orthogonal pair, and finally the ambient VOA isomorphism type by the prior theorem of Abe–Lam–Yamada.

Uniformity means the constants do not depend on unknown multiplication coordinates or on an already supplied nearby exact axis. The exact ambient class is a hypothesis. Failure of the sufficient inequalities is inconclusive.

The quantitative step replaces an exact orthogonal-pair premise by sufficient coefficient bounds. The exact classification endpoint, critical-point-to-idempotent mechanism, and general variational geometry come from prior work.

## 2. Direct comparison

| Primary source / inspected statement | Its input and output | Relationship to the criterion |
|---|---|---|
| Tkachev, Proposition 2.1, *On an extremal property of Jordan algebras of Clifford type* | A positive metrized commutative algebra; extremizing a cubic on a unit sphere gives an idempotent with a tangent spectral inequality. | Supplies the general critical-point-to-idempotent and second-variation mechanism. The unitary Virasoro charge gap, exact Ising interpretation, and ambient classification require further inputs. |
| Tkachev, Proposition 2.7 | A unital positive metrized algebra; complementary nonzero idempotents exist. | A complementary stress component can have large charge. These idempotents therefore do not automatically supply two charge-1/2 Virasoro vectors. |
| Sakuma, Theorem 4.4 | Two exact Ising vectors in a positive-real current-free VOA; discrete pair possibilities and overlaps. | Supplies overlap quantization after the finite self-coupling deficits have been used to extract exact vectors. |
| Hall–Rehren–Shpectorov, Theorems 1.1–1.2 | Exact primitive semisimple idempotents obeying specified fusion rules; a universal axial construction and the nine two-generated Norton–Sakuma types. | Provides an algebraic exact-pair classification. Its axis/product normalization differs from that in the core proof and requires conversion before comparing numerical values. |
| Khasraw–McInroy–Shpectorov, introductory stability definition and structural theorems | Exact generating axes; stability means invariance under replacing a set of axes by another set with the same group closure. | “Stable” here concerns equivalent generating sets. It is a different property from metric robustness under coefficient errors. |
| Lam–Yamauchi, Theorem 1.1, framed characterization | A holomorphic c24 VOA with V1=0 and an exact Virasoro frame; moonshine identification. | An exact structural route requiring a complete frame. The correlation criterion instead takes two arbitrary fields satisfying finite-error bounds. |
| Abe–Lam–Yamada, Theorem A.1 | Exact orthogonal Ising pair, rationality, C2-cofiniteness, holomorphicity, CFT type, c24 and V1=0; ambient moonshine identification. | Supplies the full exact endpoint. The correlation criterion replaces its pair premise by sufficient coefficient inequalities. |
| Jiao–Zheng, introduction/main pair-generation result | Exact Ising pair with fixed overlap and appropriate exact involution data; identification of the generated subVOA, notably the 6A case. | The exact-pair input and generated-subVOA endpoint differ from extraction from arbitrary supplied fields and identification of the ambient VOA. |
| Loi–Phien, Lemma 2.11 and Theorem 3.1 | Local nondegenerate matrix data or a smooth function with derivative control and permission to perturb it; quantitative normal forms and Morse properties. | Quantitative geometry is prior work. Their permitted perturbation of a function changes the comparison: the core proof must work with the fixed exact VOA cubic. |
| Carpi–Codogni, Conjecture 1.3, Theorem 1.4 and section 14 | Genus-dependent partition data and reconstruction structure; a distinction between reconstructing the partition-function subalgebra/module and the full VOA. | Gives context for the distinction between spectral and product data. The correlation criterion assumes actual fields satisfying coefficient bounds, whereas full reconstruction and bare moonshine uniqueness are stronger questions. |

Exact pair, exact idempotent, and exact fusion-law assumptions are substantive premises. Comparing theorems requires preserving those distinctions, together with whether the conclusion identifies a generated subalgebra or the entire ambient VOA.

## 3. Sharpness and calibrated inputs

[Sharpness and calibration](../research/sharpness_and_calibration.md) supplies two precision results:

* The exponent 1/2 in value-to-nearest-axis distance is optimal, using an explicit curve inside the actual moonshine theory. It realizes the quadratic-loss phenomenon in the relevant class.
* Seven scalar coefficients for two exact real weight-two fields determine their primary-projected normalized inputs. Certified interval arithmetic propagates uncertainty in these coefficients while retaining the exact ambient axioms and grade/reality assumptions.

The exponent result concerns field-distance extraction. The numerical thresholds remain sufficient constants, and the optimality statement does not determine an optimal decision region for identifying a VOA.

## 4. Mathematical interfaces

The core argument uses a positive-energy cyclic Virasoro module, the distinction between exact Ising highest weights and their ambient descendants, uniform local growth without Monster multiplicities, global entry without compactness of a moduli space, singular-product orthogonality, and the exact ambient hypotheses of Abe–Lam–Yamada.

Calibration handles stress contamination within exact grade two and PCT reality. The sharpness curve is embedded in the known moonshine theory; its three-dimensional algebra describes that family within the ambient VOA. Orthogonality means commuting Virasoro subalgebras and vanishing singular OPE, while regular products can be nonzero.

The representation and classification theorems are imported through the source interfaces listed below. The finite certificates check the accompanying arithmetic and explicit examples.

## 5. Source statements and versions

* **Tkachev [T]**, arXiv:1801.05724, *On an extremal property of Jordan algebras of Clifford type*: Proposition 2.1 and its variational proof; Proposition 2.7; introduction and relevant references. Published DOI: 10.1080/00927872.2018.1499924. The comparison concerns the variational statements, rather than the full Jordan-algebra classification.
* **Hall–Rehren–Shpectorov [HRS]**, arXiv:1311.0217: introduction, Theorems 1.1–1.2, definitions of axes and normalization. The comparison uses the exact-axis hypotheses and pair-classification statements. The apparent c>=1 rationality statement in the preliminary text is not an input to the criterion.
* **Khasraw–McInroy–Shpectorov [KMS]**, arXiv:1809.10132v2: introduction and definition of stability under equivalent generating axes.
* **Sakuma [S]**, arXiv:math/0608709: exact hypotheses, Ising modules, Theorem 4.4 and reference trail. The pair classification supplies the discrete overlap possibilities.
* **Abe–Lam–Yamada [ALY]**, arXiv:1705.09022v4: Theorem A.1 and the Appendix endpoint, printed page 10. Its orbifold and simple-current-extension machinery supplies the exact ambient classification.
* **Lam–Yamauchi [LY]**, arXiv:math/0609718: Theorem 1.1 and introduction. The exact-frame characterization is a comparison theorem, rather than an additional premise of the correlation criterion.
* **Jiao–Zheng [JZ]**, arXiv:2201.11359: introduction and main exact-pair generation result. The comparison concerns the input and generated-subVOA conclusion.
* **Loi–Phien [LP]**, arXiv:1305.3352: Lemma 2.11 and Theorem 3.1, including the permitted perturbation. This is a quantitative-geometry comparison; the core proof states and proves its own elementary localization lemma.
* **Carpi–Codogni [CC]**, arXiv:2605.26972v1: introduction, Conjecture 1.3, Theorem 1.4 and section 14. These supply background on reconstruction distinctions.
* **Dong–Lin [DL]**, arXiv:1308.2361: Definitions 2.1–2.2, printed page 3, for positive Hermitian/PCT conventions.
* **Wassermann [W]**, arXiv:1012.6003: pp. 1–2 on the positive-energy unitary series, with attribution to the original FQS classification. The representation-theoretic interface uses this account of the series.
* **Lam–Shimakura [LS]**, arXiv:0810.5395: Theorem 3.1 and the moonshine lattice inclusion, printed page 6. The proof uses commuting Virasoro subalgebras and vanishing singular OPE, rather than the literal all-mode vanishing phrase preceding the source theorem.

### Primary source locations

[T] https://arxiv.org/abs/1801.05724

[HRS] https://arxiv.org/abs/1311.0217

[KMS] https://arxiv.org/abs/1809.10132

[S] https://arxiv.org/abs/math/0608709

[ALY] https://arxiv.org/abs/1705.09022

[LY] https://arxiv.org/abs/math/0609718

[JZ] https://arxiv.org/abs/2201.11359

[LP] https://arxiv.org/abs/1305.3352

[CC] https://arxiv.org/abs/2605.26972

[DL] https://arxiv.org/abs/1308.2361

[W] https://arxiv.org/abs/1012.6003

[LS] https://arxiv.org/abs/0810.5395
