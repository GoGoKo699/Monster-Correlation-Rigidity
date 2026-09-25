# Prescribed-image normalizer rounding: precursors and a reducible obstruction

**Date:** 25 September 2026. **Base:** `5aa28ca60c33a1dcd0d271277b4467803fbea05d`.
**Branch:** `research/normalizer-priority`. Live main and branches were checked; no open PR was present.

This is a bounded theorem-level comparison for repaired claim C11, not a comprehensive novelty audit. It identifies a directly matching prior lemma, separates three different stability questions, and derives an explicit obstruction to removing irreducibility. A conditional reducible extension explains the obstruction's exact location. Neither result falsifies the actual C11 or changes any Monster rejection threshold.

## 1. Findings

1. The nonzero averaged-intertwiner step of C11 is the real orthogonal specialization of the argument in Gowers-Hatami Lemma 7.1 [GH]. It should not be presented as a new representation-stability mechanism.
2. Approximate multiplicativity, approximate equality of two representations, and approximate preservation of a prescribed finite matrix image are different inputs. Applying an approximate-representation theorem directly to `g -> O rho(g) O^T` repairs nothing: this map is already exactly multiplicative.
3. For the fixed group G=A5 x A5, there is a faithful **reducible** real orthogonal family of dimension D=16k+4 with fixed nonconstant class-walk norm q=1/3, separation squared 24k/D, and class-mean image error squared 8/D, but exact normalizer distance squared **24k/D**. The approximation is even uniform on the entire group, with squared error 10/D. The distance stays bounded away from zero as the error tends to zero.
4. If the discrete rounded automorphism is known to be implementable in the given representation, the C11 average bound survives without irreducibility. Projection onto all intertwiners and polar completion replace the one-dimensional Schur argument. This is a conditional specialization of standard averaging/polar techniques, not a claimed new general stability theory.

The outstanding project-specific comparison is the quantitative route from *class-averaged assignments* to a compatible automorphism of the *prescribed finite image*, followed by the correlation-loss specialization. The sources checked here do not eliminate that route without additional arguments. This statement is not evidence that the route is novel or publication-significant.

## 2. The exact C11 under comparison

Use ||B||_{2,d}=||B||_F/sqrt(d). Let G be finite, rho:G -> O(d) faithful and absolutely irreducible over the reals, and C an involution conjugacy class. Uniform C averaging has absolute operator norm at most q on every nontrivial complex irreducible representation. Let

$$s_0=\min_{g\ne h}\|\rho(g)-\rho(h)\|_{2,d}>0.$$

For O in O(d), arbitrary assignments h_c in G satisfy

$$\mathbb E_{c\in C}\|O\rho(c)O^T-\rho(h_c)\|_{2,d}^2\le z^2.$$

The repaired parameter domains and conditions are

$$0\le q<1,\quad0\le\beta<1,\quad t>0,\quad L\in\mathbb Z_{\ge1},$$

$$z^2\le\beta t^2,\quad r=\frac{q+\beta}{1-\beta}<1,\quad
(|G|-1)r^L<1,\quad Lt<1,\quad3Lt<s_0.$$

Then an orthogonal normalizer R exists with

$$\min_{s=\pm1}\|O-sR\|_{2,d}^2\le\frac{z^2}{1-q}.$$

The sign can be absorbed into the normalizer. This is an existential certificate, not an efficient extraction algorithm. It does not imply proximity to G itself; the Monster specialization separately identifies its orthogonal normalizer using its unique invariant cubic and the full algebra automorphism theorem.

The precise statement and repaired proof are note 05 section 5 and the robustness audit section 5. All historical files remain unchanged. Absolute irreducibility means that the complexification is irreducible, not merely that there are no real invariant subspaces.

## 3. Primary-source comparison

Here eta denotes a precursor's defect, never the project's quantum rejection probability. Supremum, class average and full-group averages are not interchanged.

| Checked statement | Input and norm | Output / dimension / target |
|---|---|---|
| GH Definition 6.2, Theorem 6.9, p=2 | Finite G; affine multiplicative defect <=eta for every admissible quadruple; normalized Hilbert-Schmidt norm; 0<eta<=1/4 | Uniform error <=(7+3sqrt(2))eta to a partial affine representation; m in [(1-eta^2)d,d/(1-eta^2)]; no prescribed finite image |
| GH Lemma 7.1 | Two irreducible representations, uniformly less than one apart in normalized Schatten norm | Equivalence by nonzero averaging and Schur; this directly matches C11's equivalence step |
| GH Theorem 7.3, p=2 | Two exact representations uniformly eta-close in normalized Hilbert-Schmidt norm | Partial intertwiner within 3eta of identity; common component dimension >=(1-4eta^2)d; not full equivalence |
| De Chiffre-Ozawa-Thom Definition 5.1, Theorem 5.2 [DCT] | Amenable G; for every g, mean over h of multiplicative defect <eta; invariant lower-semicontinuous operator-algebra seminorm | Uniform error <71eta after compression from an amplified corner; corner defects <40eta and <30eta; no fixed image |
| Burger-Ozawa-Thom Theorem 3.2 [BOT], Gamma=Lambda=G, C=1 | Amenable G; normalized-at-identity unitary map with uniform multiplicative defect eta<1/10 in **operator norm** | Same-Hilbert-space representation at uniform distance <=eta+120eta^2; no prescribed finite image |

These are existence statements with constructions in their proofs, not complexity guarantees in the repository's encoded-input/oracle model. A finite sum over all group elements is a mathematical construction, not automatically efficient access to the Monster.

GH's printed Theorem 6.12 says “finite Abelian group” in both the retrieved arXiv and published text. This comparison uses the explicitly finite-group Theorem 6.9 and Lemma 7.1, not an unannounced correction of Theorem 6.12. The earlier approximate-representation priority row is superseded at this finer level by the present comparison.

Original Grove-Karcher-Ruh [GKR] was located bibliographically, but its full theorem/proof was not obtained. The same-dimension result transmitted in GH's introduction has a normalized-Hilbert-Schmidt smallness scale proportional to d^(-1/2); it is recorded only as a secondary transmission, not a checked original theorem. Original Kazhdan [K] likewise remains unread. BOT supplies an actual alternative proof for the operator-norm comparison above, not evidence that the original paper was inspected.

DCT also proves genuinely averaged inverse/stability statements, including Theorem 3.1's two averaged four-factor defects. Therefore neither the word “average” nor a move from scalar to matrix-valued data is by itself a novelty distinction. Its mean-representation hypothesis is not C11's average of distances on one conjugacy class.

## 4. Explicit attempted reductions

### 4.1 Applying multiplicativity stability to the conjugate representation is vacuous

Set f(g)=O rho(g) O^T. For every O,

$$f(g)f(h)=f(gh).$$

The input defect is identically zero, including when O is far from the normalizer. A theorem concluding that f is close to some representation may simply return f. It has learned nothing about the requirement f(G)=rho(G), or about a conjugating matrix close to O.

The checker provides an exact rational example in the standard A5 module. In R^5 take a=(1,-1,0,0,0)^T, b=(0,0,1,-1,0)^T and

$$N=5I-aa^T-bb^T+2(ba^T-ab^T),\qquad O=N/5.$$

N^T N=25I and O fixes the all-ones vector, so it restricts to the four-dimensional sum-zero space. Every conjugated multiplication defect is zero. Nevertheless

$$\mathbb E_{c\in C}\min_{h\in A_5}
\|O\rho(c)O^T-\rho(h)\|_{2,4}^2=96/125.$$

This last finite minimum is checked exactly over 15 by 60 choices. It is a counterexample to the *proposed direct inference from multiplicativity defect alone*, not to any precursor theorem or to C11's small-error hypothesis.

### 4.2 Rounding to the finite image first already repairs multiplication

C11 first discards assignments with error >t and obtains all-group coverage by words of exactly L good steps. This gives a target element within delta=Lt of every f(g). Separation 2delta<s_0 makes the nearest assignment phi(g) unique. Its multiplication defect satisfies

$$\|\rho(\phi(gh))-\rho(\phi(g)\phi(h))\|_{2,d}\le3\delta<s_0,$$

so it is **zero**, not merely small. Injectivity follows from 2delta<s_0; finiteness makes phi an automorphism. The nearest assignments on the original class are at least as accurate as the supplied assignments, including the discarded ones.

Thus applying GH/BOT/DCT to rho composed with phi *after* this step is redundant: it is again an exact representation, this time inside the desired image. A route that instead repairs a partially defined or approximate map must still prove same-dimension realizability, preservation of the desired finite image, and compatibility of the recovered automorphism. The checked theorems do not provide those properties solely from their own input defects.

### 4.3 A precise part is already in GH

Compare alpha(g)=O rho(g) O^T and sigma(g)=rho(phi(g)). Their uniform distance is <=delta<1. Both are irreducible. GH Lemma 7.1 applies directly after complexification. Its proof averages alpha(g)sigma(g)^* and shows it is nonzero, then invokes Schur.

In the real convention used by C11, this is

$$A=\mathbb E_g\rho(\phi(g))^T O\rho(g),\qquad
A\rho(h)=\rho(\phi(h))A.$$

The distance ||A-O||_{2,d}<1 implies A is nonzero; absolute irreducibility gives A^T A=a^2I, a>0. R=A/a is an orthogonal implementer. This is an explicit real specialization of the prior averaging argument. The subsequent class-gap estimate is an elementary Poincare estimate in the conjugation representation, not an additional approximate-multiplicativity theorem.

### 4.4 Why norm and dimension cannot be silently changed

The general bound ||B||_op <=sqrt(d)||B||_{2,d} loses sqrt(d). It does not turn a dimension-independent Hilbert-Schmidt hypothesis into a dimension-independent operator-norm hypothesis.

Even GH Theorem 6.9's p=2 dimension interval forces the integer m to equal d only when, for example, eta^2<1/(d+1). Indeed then d-1<(1-eta^2)d<=m<=d/(1-eta^2)<d+1. This is a sufficient integer-forcing observation, not a necessary threshold. It still does not force the representation's image to be rho(G).

Conversely, C11 is not a general proof of approximate-representation stability: it assumes an exact representation, an exact conjugating O, and approximate assignment into a fixed finite image. No construction of these data from an arbitrary approximate representation is supplied. These obstructions to naive reductions do not establish logical independence from every combination of classical results.

### 4.5 Qualitative fixed-representation normalizer stability is not a novelty claim

For a fixed faithful rho and a generating class C, define the continuous function

$$F(O)=\mathbb E_c\min_{h\in G}\|O\rho(c)O^T-\rho(h)\|_{2,d}^2.$$

Its zero set is precisely the normalizer: inclusion of all conjugated generators in rho(G) gives inclusion of the full conjugated finite group, and equal orders give equality. Since O(d) is compact, for every a>0 the minimum of F over matrices at normalizer distance at least a is positive whenever that set is nonempty. Thus F(O_j)->0 implies distance(O_j,N)->0 at fixed representation, without irreducibility. This elementary argument supplies no explicit modulus or the C11 constant/threshold.

There is also a classical subgroup-neighborhood route. Csikos-Katay-Kocsis-Palfy [CKKP, Theorem 2.15] transmits Montgomery-Zippin's theorem that a subgroup sufficiently near a fixed compact subgroup of a fixed Lie group can be conjugated into it by an element in any specified identity neighborhood. For K=rho(G), H=OKO^T, equal finite orders make containment equality, so a small conjugator a gives aO in N(K). This is a qualitative prescribed-image result, not a theorem with C11's explicit normalized-error radius. The original 1942 source was located but its retrieval failed; only the stated transmission is used here. Neither route is contradicted by Proposition 1, which changes representation dimension.

## 5. A fixed-group obstruction without irreducibility

### Proposition 1

Let H=A5 and let sigma:H -> O(4) be its standard action on the sum-zero part of R^5. Let C be its class of 15 double transpositions. For k>=1 put

$$G=H\times H,\quad \mathcal C=C\times C,\quad D_k=16k+4,$$

$$\rho_k(g,h)=(\sigma(g)\otimes\sigma(h))^{\oplus k}\oplus\sigma(g).$$

Let F be the tensor-factor swap on R^4 tensor R^4, define O_k=F^(direct sum k) direct sum I_4, and assign every (g,h) to phi(g,h)=(h,g). Then rho_k is faithful real orthogonal, phi is an exact automorphism, and

$$\mathbb E_{(c,d)\in\mathcal C}
\|O_k\rho_k(c,d)O_k^T-\rho_k(d,c)\|_{2,D_k}^2=\frac8{D_k},\tag{1}$$

$$\max_{g,h\in H}
\|O_k\rho_k(g,h)O_k^T-\rho_k(h,g)\|_{2,D_k}^2=\frac{10}{D_k},\tag{2}$$

$$s_{0,k}^2=\frac{24k}{D_k},\qquad
\min_{R\in N_{O(D_k)}(\rho_k(G))}\|O_k-R\|_{2,D_k}^2=\frac{24k}{D_k}.\tag{3}$$

The absolute class-walk bound is q=1/3 for every k. Consequently both class-averaged and uniform errors tend to zero, while the normalizer distance tends to sqrt(3/2). The group and class are fixed and separation is bounded below; this is not a failure caused by coalescing group matrices or vanishing class gap.

### Proof: group and error calculations

The standard character is chi(g)=number of fixed points of g minus one. Its values are 4 at identity, 0 on double transpositions, 1 on 3-cycles, and -1 on 5-cycles. Its squared character norm is one, so its complexification is irreducible; it is faithful. The exact A5 class-walk spectrum is

$$1^{(1)},\quad(-1/3)^{(18)},\quad0^{(16)},\quad(1/5)^{(25)}.$$

The checker reconstructs this from a 60 by 60 integer adjacency matrix, not an imported character table. The product walk has tensor-product eigenvalues and therefore the same absolute nonconstant bound 1/3. In particular the product class generates G and has no periodicity obstruction.

Since F(A tensor B)F^T=B tensor A, the large blocks of O_k rho_k(g,h) O_k^T and rho_k(h,g) agree exactly. Their only difference is sigma(g)-sigma(h) on the final four-dimensional summand. Its unnormalized squared norm is

$$\|\sigma(g)-\sigma(h)\|_F^2=8-2\chi(g^{-1}h).$$

The maximum is ten. Uniform C averaging of sigma(c) is zero, so the mean over independent c,d is eight. This proves (1)-(2). The operator-norm residual, in contrast, has supremum two; it does not tend to zero.

The character of rho_k is k chi(g)chi(h)+chi(g). The largest nonidentity value is 4k+4, achieved at g=e and h a 3-cycle. Hence rho_k is faithful and

$$s_{0,k}^2=2-2\frac{4k+4}{16k+4}=\frac{24k}{16k+4}.$$

### Proof: exact distance to the entire normalizer

The two direct factors of H x H are its two minimal nontrivial normal subgroups. Every automorphism either preserves them or exchanges them. This follows from nonabelian simplicity of H; no classification of Aut(A5) is needed.

Write S=sigma tensor sigma (dimension 16), tau_1=sigma tensor 1 (dimension 4), and tau_2=1 tensor sigma. These are irreducible and pairwise inequivalent. Rho_k contains S with multiplicity k and tau_1 once, but contains no tau_2. An automorphism exchanging the factors would send the four-dimensional constituent to one with the opposite kernel. Therefore it cannot be implemented by any normalizer of rho_k(G).

Every actual normalizer induces a factor-preserving automorphism (alpha,beta). Its large-isotypic-block intertwiner has the form

$$M\otimes(U\otimes V),\qquad M\in O(k),\quad U,V\in O(4),$$

and its remaining block is some B in O(4). To justify this form, equivalence of external tensor products requires equivalence in each factor; choose orthogonal factor intertwiners U,V. Absolute irreducibility then makes the remaining freedom exactly an orthogonal multiplicity-space matrix M. If either factor twist is not equivalent, there is no such normalizer, which only restricts the set further.

The swap trace identity is

$$\operatorname{Tr}[F(U\otimes V)]=\operatorname{Tr}(UV).$$

It gives, for every normalizer R,

$$\operatorname{Tr}(O_k^T R)\le |\operatorname{Tr}M|\,|\operatorname{Tr}(UV)|
+|\operatorname{Tr}B|\le4k+4.$$

Thus the squared distance is at least 2-2(4k+4)/D_k. The identity is itself a normalizer and attains the bound, because Tr F=4. This proves the equality in (3). The proof covers the full continuous orthogonal normalizer, not merely a finite sample or inner automorphisms. The minus sign adds no alternative since -R is also a normalizer.

### The averaged intertwiner exposes the failure

For the assigned factor-swap automorphism,

$$A_k=\mathbb E_{g,h}\rho_k(h,g)^T O_k\rho_k(g,h)
=F^{\oplus k}\oplus0_4.$$

It is nonzero and ||A_k-O_k||_{2,D_k}^2=4/D_k, but it has rank D_k-4. Nonzero does not imply invertible in a reducible representation. Here the small unmatched constituent is precisely the obstruction to any orthogonal implementation of phi.

After comparing the two already conjugated representations, the corresponding partial intertwiner is I_(16k) direct sum 0_4. They have a common component of codimension four. This is consistent with GH's partial-intertwiner conclusion, rather than a contradiction to it. The commutant also has dimension k^2+1, so the final scalar-only Poincare step of irreducible C11 cannot be reused unchanged.

## 6. A numerical-size witness with exact scalar inequalities

Take k=10000, D=160004, and

$$q=1/3,\quad\beta=1/16,\quad L=10,\quad
z^2=\frac{2}{40001},\quad t^2=\frac{32}{40001},\quad r=19/45.$$

Then

$$z^2=\beta t^2,\qquad
3599r^{10}=\frac{22065707461825799}{34050628916015625}<1,$$

$$L^2t^2<1,\qquad9L^2t^2<\frac{60000}{40001}=s_0^2.$$

In fact every assigned error is below t, even before discarding. Thus all repaired scalar conditions and all group/class/faithfulness requirements hold. **The missing hypothesis is irreducibility.** An irreducibility-free version of C11 would incorrectly assert

$$\operatorname{dist}(O_k,N)^2\le\frac{z^2}{1-q}=\frac3{40001},$$

whereas the actual answer is 60000/40001, larger by a factor 20000. The huge representation is never materialized; these are exact rational consequences of the proved block formulas.

This is a family of counterexamples to a proposed extension, not to C11 itself, nor to a fixed-dimension compactness statement. Dimension grows while the group remains fixed. Neither the family nor its constants have received comprehensive priority clearance.

## 7. The exact missing hypothesis: representation compatibility

### Proposition 2: compatible reducible rounding

Let rho:G -> O(d) be any real orthogonal representation of a finite group. Let C and q have the same class-gap property as above. Suppose an automorphism phi is **orthogonally implementable** in rho: there exists R_0 with

$$\rho(\phi(g))=R_0\rho(g)R_0^T.$$

For any O in O(d), define

$$z_\phi^2=\mathbb E_c\|O\rho(c)O^T-\rho(\phi(c))\|_{2,d}^2.$$

Then some orthogonal R implementing this same phi satisfies

$$\|O-R\|_{2,d}^2\le\frac{z_\phi^2}{1-q}.\tag{4}$$

There is no smallness restriction for this *conditional* estimate. The implementability hypothesis is indispensable: Proposition 1 supplies arbitrarily small z_phi for a nonimplementable phi.

### Proof

Set sigma=rho composed with phi and

$$A=\mathbb E_g\sigma(g)^T O\rho(g).$$

This is the orthogonal projection of O onto the space of intertwiners. Apply the class gap to the orthogonal action B -> sigma(g)B rho(g)^T on matrices. There may now be many invariant directions, so project onto the *whole* invariant space, not just scalar matrices:

$$z_\phi^2\ge2(1-q)\|O-A\|_{2,d}^2
=2(1-q)(1-\|A\|_{2,d}^2).$$

Write Q=R_0^T O and A=R_0 B. The matrix B lies in the real commutant of rho and has operator norm at most one, since it is an average of orthogonal matrices. Its polar partial isometry extends to an orthogonal V in that commutant. For completeness: its initial and final support representations are equivalent through the polar map; cancellation in the completely reducible finite-group representation then makes its two kernel representations equivalent as well. An orthogonal intertwiner on the kernels completes the polar map. This is where compatibility, not merely nonzero A, is used.

For R=R_0 V, averaging is an orthogonal projection and V is in the commutant, so

$$\langle O,R\rangle_{2,d}=\langle B,V\rangle_{2,d}
=\operatorname{Tr}|B|/d.$$

Every singular value of B lies in [0,1]. Therefore

$$\|O-R\|_{2,d}^2=2-2\operatorname{Tr}|B|/d
\le2(1-\|B\|_{2,d}^2)\le z_\phi^2/(1-q).$$

This proves (4), including singular B. The same argument gives the exact distance to the set of implementers of this fixed phi as 2-2 Tr|A|/d; the trace inequality for orthogonal matrices supplies the matching lower bound. This does not by itself minimize over different automorphisms.

Consequently steps 1-2 of C11 work for arbitrary faithful rho, and its conclusion continues to hold **provided the resulting nearest automorphism is representation-compatible**. The nearest-assignment property ensures z_phi<=z. Absolute irreducibility plus delta<1 was one sufficient way to obtain that compatibility. Real irreducibility alone also suffices here: a nonzero real intertwiner between irreducible real representations is invertible, and the full-intertwiner estimate handles a non-scalar commutant. This observation does not rewrite the stronger historical C11 hypothesis. Another a priori sufficient condition is that every automorphism of G preserve the representation's equivalence class; the real regular representation has this property by permutation of its group-labelled basis. No efficient compatibility test or Monster extraction algorithm is claimed.

Conversely, if a nearest assignment phi has uniform error <=delta and R is a normalizer implementing psi, then

$$\|\rho(\phi(g))-\rho(\psi(g))\|_{2,d}
\le\delta+2\|O-R\|_{2,d}.$$

If this is less than s_0, discreteness forces phi=psi. A noncompatible phi therefore excludes every normalizer closer than (s_0-delta)/2 when delta<s_0. This is a general lower bound, separate from Proposition 1's sharper exact answer.

## 8. Classification after this comparison

| Component | Outcome |
|---|---|
| Averaging an intertwiner, nonzero test, Schur equivalence | Direct prior match to GH Lemma 7.1; not a project novelty claim |
| Partial equivalence of nearby reducible representations | Explicit prior GH theorem; does not imply equivalence on every constituent |
| Good-set conditioning, mixing-to-word coverage, separated nearest-image multiplication | Elementary reconstructed estimates; no checked source here replaces their joint class-to-image implication |
| Class-gap bound after compatibility is known | Poincare plus polar rounding; standard techniques, with Proposition 2 a self-contained conditional formulation |
| Irreducibility-free exact-normalizer extension | Falsified by Proposition 1 even at fixed group, fixed gap and positive separation |
| Qualitative normalizer stability at fixed representation | Direct compactness consequence; classical subgroup-neighborhood context also exists |
| Repaired C11 and assembled Monster correlation certificate | Not subsumed by a single checked precursor without the stated additional steps; priority and significance remain unresolved |

A theorem assembled from these estimates may still be a useful quantitative corollary or specialization. Whether it is a publishable contribution cannot be inferred from the Monster's exceptional name, from a large representation dimension, or from the absence of search hits. No claim of logical independence from all classical machinery is made.

## 9. Verification and source depth

`checks/verify_normalizer_priority.py` has **96 labeled checks**, identical locally under normal Python, -O and -OO. It enumerates A5, proves simplicity from its exact conjugacy-class sizes, checks its real standard matrices and all 3600 products, and reconstructs the regular class spectrum with exact integer spectral polynomials. It checks product-group characters, all 3600 flip identities, the k=1 averaged intertwiner, and the large-k scalar inequalities. It includes the exact zero-defect/wrong-image example, a valid irreducible C11 control, and compatible reducible polar-rounding controls, including a singular average.

The exact normalizer minimum is proved by constituent analysis and the trace inequality; it is **not** numerically optimized over all normalizers. Largest dense matrix: 60 by 60; largest explicitly formed reducible representation: 20 by 20. No dimension-160004 representation, full Monster matrix, Monster tensor or circuit is simulated. Numerical checks use tolerance 1e-10; all displayed witness inequalities use integers and rational arithmetic. No practical precision, independent expert review or formal verification is claimed.

The unchanged root verifier and existing bounded-portability inspector remain separate. Runtime network checkout/download failed, so a local seed replay is not claimed to verify live main. The read-only workflow checks the pinned current baseline and candidate. Its actual strict replay and bounded-portability outcomes must be read before integration. Old reports and tolerances are not altered.

Read depth: GH's indicated statements and the averaged-intertwiner proof were read in parsed arXiv text and cross-checked against the published PDF's parsed text. BOT's Theorem 3.2 and its averaging iteration, and DCT's Definition 5.1, Theorem 5.2 and its displayed reduction to Theorem 3.1 were read. Browser screenshot requests returned service errors for the relevant PDF pages; no successful visual inspection is claimed. GKR and Kazhdan original proofs were not obtained. CKKP Theorem 2.15 and its source locator were read in parsed text; the original Montgomery-Zippin article could not be retrieved, and its proof was not read. This is a scoped mathematical comparison, not exhaustive source review.

## Primary-source register

[GH] W. T. Gowers and O. Hatami, *Inverse and stability theorems for approximate representations of finite groups*, arXiv:1510.04085v2; Sbornik: Mathematics 208(12) (2017), 1784-1817, DOI 10.1070/SM8872. Definition 6.2, Theorem 6.9, Lemma 7.1 and Theorem 7.3. ArXiv printed pp.27,32,34-35; published Lemma 7.1 and Theorem 7.3 on pp.1809-1810.
https://arxiv.org/abs/1510.04085
https://www.mathnet.ru/eng/sm8872

[DCT] M. De Chiffre, N. Ozawa and A. Thom, *Operator algebraic approach to inverse and stability theorems for amenable groups*, arXiv:1706.04544v2. Definition 5.1 and Theorem 5.2, printed pp.18-19; Theorem 3.1, printed p.11.
https://arxiv.org/abs/1706.04544

[BOT] M. Burger, N. Ozawa and A. Thom, *On Ulam stability*, arXiv:1010.0565v1. Theorem 3.2 and proof, printed pp.7-8. Its ambient metric is operator norm, not normalized Frobenius distance.
https://arxiv.org/abs/1010.0565

[GKR] K. Grove, H. Karcher and E. A. Ruh, *Group actions and curvature*, Inventiones Mathematicae 23 (1974), 31-48, DOI 10.1007/BF01405201. Bibliographic record obtained; original theorem/proof not read here.
https://doi.org/10.1007/BF01405201

[K] D. Kazhdan, *On epsilon-representations*, Israel Journal of Mathematics 43 (1982), 315-323. Original proof not read; do not substitute BOT's alternative proof while claiming original-source access.

[CKKP] B. Csikos, T. Katay, A. Kocsis and M. Palfy, *Compact Lie groups isolated up to conjugacy*, arXiv:2209.15389v1, Theorem 2.15, printed p.8. It attributes the theorem and near-identity refinement to D. Montgomery and L. Zippin, *A theorem on Lie groups*, Bulletin of the American Mathematical Society 48 (1942), 448-452, Theorem 1 and p.451 corollary. The latter original was not obtained.
https://arxiv.org/abs/2209.15389

All earlier research notes 01-09, audits, circuits, checkers, data/results, provenance, import-era STATUS.md, root verifier, portability policy and original MIT license are preserved. Only this new note/check/report and intentional current-summary/workflow/manifest updates form the patch. No downloaded papers are bundled; no manuscript, release or outreach is performed.
