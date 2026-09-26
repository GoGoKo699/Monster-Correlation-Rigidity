# A canonical field for the first nonzero thermal response

**Date:** 26 September 2026. **Base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Proposed additive branch:** `research/canonical-thermal-field`.

This follows the supplied local Note20/checkpoint on the necessary weight-twelve response. The live main branch and open PRs were read, including the newer odd-channel-nonclosure PR18. This work is separate from that branch, pending PR12-18, and the unresolved uncontracted polynomial of Note18. No pending result is silently integrated.

## 1. Result and its selection boundary

In the declared extremal class, the first nonzero primary thermal response has a canonical representing field R of weight twelve. Its definition uses only the first primary level, the invariant metric, and removal of vacuum descendants:

\[
 R=\pi_{12}\sum_{i=1}^{d} e_i{}_{(-9)}e_i,\qquad d=196883.
\]

No Monster action or multiplication table is needed. The sum is independent of the orthonormal primary basis. For every weight-twelve primary w,

\[
\operatorname{Tr}_{V_2}o(w)=\langle R,w\rangle,\qquad
F_w(\tau)=\langle R,w\rangle\Delta(\tau).
\tag{1}
\]

In the real PCT convention the form is real; complexification gives the usual sesquilinear formulation, with the representing vector in the first slot. The new exact normalization is

\[
\boxed{\|R\|^2=\mathcal N=\frac{68811289248}{14884739}>0.}\tag{2}
\]

Consequently the unit primary \(\widehat R=R/\sqrt{\mathcal N}\) has

\[
F_{\widehat R}(\tau)=\sqrt{\mathcal N}\,\Delta(\tau),\qquad
\max_{\|w\|=1}|F_w(\tau)|=\sqrt{\mathcal N}\,|\Delta(\tau)|.
\tag{3}
\]

Equality occurs only on this complex ray. At physical real q in (0,1), the unique real unit maximizer of the positive one-point function is +R-hat. Normalized thermal expectations divide by J(q). These are dimensionless chiral trace conventions, not a proposed experimental Hamiltonian deformation.

The first failure of cancellation is therefore one-dimensional as a **response functional**, with a fixed norm. This does not mean P12 is one-dimensional, or that it has only one symmetry-invariant primary. Orthogonal fields have vanishing one-point functions, but their higher correlators and individual zero modes need not vanish. A field selected inside every candidate is not a uniquely selected CFT.

This canonical construction and invariant-primary phenomena have substantial precedents: Matsuo's basis-independent Casimir states and Dong-Mason's higher-weight moonshine. In the known moonshine theory, Dong-Mason explicitly record the unique Monster-invariant weight-twelve primary with one-point function Delta. The result here is a normalized, group-free corollary for an arbitrary admissible candidate, not a claim to have discovered that known field or to have proved moonshine uniqueness.

## 2. Physical assumptions and mathematical dependencies

Admissible theories are nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs/VOAs of CFT type, with V1=0 and minimal positive central charge. Note12's modular argument selects c=24 and Z=J. Holomorphicity and this minimization are declared restrictions, not universal physical necessities or an established RG mechanism.

Let P_h be the Virasoro primary space at weight h. Unitarity supplies a positive Hermitian form, PCT-real coordinates and an orthogonal Virasoro decomposition. The relevant inherited inputs are:

* the conformal 11-design property from [H, Theorem3.1];
* dim P2=d=196883, with real symmetric primary multiplication mu;
* Tr L_a=0 and Tr(L_a L_b)=kappa<a,b>, kappa=13858/3, obtained through [H]'s explicit design replacement of [M]'s symmetry assumption;
* the ordinary mode, adjoint and Virasoro identities.

The main construction and norm use only these lower identities, not the complete six-sector spectrum, the disputed fifth trace, or the conditional all-weight closure statement of Note14. The later weight-six spectral interpretation additionally uses the finite channel identity B6^dagger B6=4Pi_s-; the checker recomputes that finite primary subtraction through weight six. The scalar compatibility proof is not a new proof of the imported modular/design theorems.

No alternative full CFT is constructed. No lowest-weight CFT uniqueness, independent specialist review, formal verification, comprehensive priority clearance, or physical implementation is claimed.

## 3. Why the Casimir remainder is primary and represents the trace

Put

\[
C_n=\sum_i e_i{}_{(3-n)}e_i,\quad C_0=d1,\quad C_1=0.
\]

This is the primary-only version of Matsuo's Casimir construction. His full V2 sum also includes the stress direction; that difference lies in the vacuum Virasoro module, so it does not change the primary remainder under consideration. The positive-mode relation for our primary-only sum is particularly simple:

\[
L_m C_n=(m+n-2)C_{n-m}\qquad(m>0).
\tag{4}
\]

Through weight eleven, the conformal-design trace condition places C_n in the vacuum Virasoro module. One can either use the usual Casimir/trace duality, or pair C_n with each nonvacuum Virasoro module: it reduces to lower-primary one-point traces and their descendant recursions, all zero by [H,DM]. This does not require a finite automorphism group.

Let V12 be the orthogonal projection of C12 to the vacuum module and set R=C12-V12. For every positive m, (4) puts L_m R in the vacuum module. Adjoint invariance also makes it orthogonal to that module. It therefore vanishes. Thus R is primary, not a remainder still containing nonvacuum descendants.

For primary w of weight twelve, the weight-two adjoint gives

\[
\langle w,e_i{}_{(-9)}e_i\rangle
=\langle e_i{}_{(11)}w,e_i\rangle
=\langle e_i,w_{(11)}e_i\rangle
\]

in real coordinates. In the second equality skew symmetry leaves only its zeroth derivative term after pairing with the primary e_i. All other terms are descendants. Also w_(11)omega=22w_(9)1=0, so trace on V2 equals trace on P2. Summing proves (1).

C12 is basis independent, and orthogonal vacuum projection commutes with every unitary VOA automorphism. Therefore R is fixed by every such physical internal symmetry. This does not establish uniqueness of the whole invariant subspace: invariant vectors in ker ell12 have not been ruled out for an unknown candidate.

## 4. Exact norm from first-level pairs

Use the full weight-two product a*b=mu(a,b)+(1/sqrt(3))<a,b>t, where t=omega/sqrt(12). A direct mode commutator gives

\[
\langle a_{(-9)}a,b_{(-9)}b\rangle
=165\langle a,b\rangle^2+9\|a*b\|^2+\langle a*a,b*b\rangle.
\tag{5}
\]

For clarity, [a_(11),b_(-9)] is B(a,b)_(2)+10(a*b)_(1)+165<a,b>I. The weight-three Gram identity gives the remaining B matrix element as <a*a,b*b>-||a*b||^2. This proves (5) without assuming the full first-field rational kernel at all weights.

Since sum_i mu(e_i,e_i)=0 and sum_ij||mu(e_i,e_j)||^2=d*kappa, summing (5) gives

\[
\|C_{12}\|^2
=d\left[165+9(\kappa+1/3)+d/3\right]
=d\frac{322109}{3}.
\tag{6}
\]

The vacuum projection is an exact 21-dimensional linear-algebra problem. In the basis L_-lambda1 ... L_-lambdar 1 indexed by partitions of twelve with all parts at least two, write M for the positive Virasoro Gram matrix and b for the pairing with a_(-9)b for unit <a,b>. Positive-mode commutation determines every entry of b. The complete matrices and positive LDL pivots are emitted by the checker. They give

\[
 b^T M^{-1}b=\frac{282875933416397}{518707716131049}.
\]

The projection of the summed C12 has pairing vector d b, so

\[
\|R\|^2=d\frac{322109}{3}
-d^2\frac{282875933416397}{518707716131049}
=\frac{68811289248}{14884739}.
\tag{7}
\]

All arithmetic is exact. The calculation never imposes a 12-design or sets the unknown primary response to zero. The same calculation through weights two to eleven yields zero primary remainder, providing lower-weight checks of the projection convention. The explicit L_m relations in (4) are checked separately through m=12 on the vacuum-projected vectors.

With rho=mathcal N/d, the same uncontracted pair calculation gives

\[
\boxed{o(R)|_{P_2}=\rho I,\qquad
\rho=\frac{20620704}{878199601}.}\tag{8}
\]

Indeed C12 paired against a_(-9)b is a scalar multiple of <a,b>; subtraction of the vacuum projection changes it by d b^T M^-1 b. This proves scalarity without assuming irreducibility under any group. For the unit field, the scalar is sqrt(mathcal N)/d. The stress state itself is annihilated, as required for a primary insertion.

The field with one-point function exactly Delta is R/mathcal N and has squared norm 1/mathcal N. It is not the unit-normalized field in (3).

## 5. The first thermal response has one distinguished direction

For any w in P12, modularity and the absence of a vacuum pole or weight-one constant term give

\[
F_w(\tau)=\ell_{12}(w)\Delta(\tau),\quad
\ell_{12}(w)=\langle R,w\rangle.
\]

The coefficient equals the trace on V2 because Delta starts with q. Equations (2)-(3) now follow by Cauchy-Schwarz. More precisely

\[
P_{12}=\mathbb R R\oplus\ker\ell_{12}
\]

orthogonally on the real space, with an analogous complex decomposition. At every temperature the same line is selected; changing tau changes only the common function Delta. This is a rank-one one-point-function statement, not a rank-one interacting theory. Primary fields in the orthogonal complement may still interact strongly.

For any orthonormal basis {w_A} of P12,

\[
\sum_A|\operatorname{Tr}_{V_2}o(w_A)|^2=\mathcal N.
\]

For the energy space V_(m+1), the corresponding representing vector is tau(m)R. No nonvanishing statement about every Ramanujan coefficient is required. At real thermal q in (0,1), Delta and J are positive, so the positive maximum has a fixed sign. On the general upper half-plane the absolute-value form of (3) applies.

## 6. The same field measures the two weight-six sectors

Let N_u=u_(5)|P2 for primary weight-six u. The finite channel calculation gives

\[
N^\dagger N=4\Pi_{\rm vis},\qquad
\dim P_6=312092484374,\quad \operatorname{rank}\Pi_{\rm vis}=18538750076.
\]

The primary part of u_(-1)v is Phi(u,v). The pair star identity and vacuum projection, with all lower-primary descendant traces zero, give the previous checkpoint's exact interface

\[
\operatorname{Tr}(N_uN_v)=a_6\langle u,v\rangle+
\langle R,\Phi(u,v)\rangle,\qquad a_6=\frac{3523416}{14884739}.
\tag{9}
\]

The new checker independently recomputes the finite vacuum projection yielding a6, rather than importing an unchecked decimal. The coefficient of the weight-twelve primary in this star sum is exactly one.

Pairing primary u,v against the R insertion and discarding descendant terms by orthogonality now gives

\[
\boxed{\pi_6o(R)\pi_6=4\Pi_{\rm vis}-a_6I.}\tag{10}
\]

Thus the unit field has the two primary-compressed eigenvalues

\[
\frac{4-a_6}{\sqrt{\mathcal N}},\qquad
-\frac{a_6}{\sqrt{\mathcal N}},
\]

with multiplicities 18538750076 and 293553734298. These are not asserted to be eigenvalues of the entire o(R)|V6: the full operator can mix primaries and descendants.

This closes the normalization gap in the earlier construction from an invisible unit u. Its coupling to a unit-normalized, canonically chosen weight-twelve field is now fixed:

\[
\langle\widehat R,\Phi(u,u)\rangle=-\frac{a_6}{\sqrt{\mathcal N}}
\quad (u\in\ker N,\ \|u\|=1).
\]

Consequently

\[
\|\Phi(u,u)\|^2\ge\frac{a_6^2}{\mathcal N}
=\frac{765191094}{63131045408653}>0.
\tag{11}
\]

This is a lower bound, not a claim that Phi lies entirely along R or that the bound is saturated. Its orthogonal component is not determined. Negative insertion values are not negative norms; adding a6I to (10) gives the positive semidefinite N^dagger N.

The two ways of forming weight twelve have the following fixed projections onto the same line:

\[
\pi_R\pi_{12}(a_{(-9)}b)=\frac{\langle a,b\rangle}{d}R,
\quad
\pi_R\Phi(u,v)=\frac{\langle u,(4\Pi_{\rm vis}-a_6I)v\rangle}{\mathcal N}R.
\]

They fix one component of two coupling tensors, not their full tensors or the overlap of all their orthogonal images.

## 7. Independent genus-one compatibility gives the same norm

A useful test is to compute Tr_P6 o(R) a second way from the modular one-point function. It is not correct to replace the primary trace by the whole-level coefficient of Delta.

For a Virasoro primary module of weight h and a primary insertion of weight s=12, the descendant contribution at level l is t_(h,l) times its primary expectation. It is computed as tr(M^-1 E), where M is the descendant Gram matrix and E its inserted-mode matrix. Moving positive Virasoro modes past the insertion, and then negative modes to the left vacuum, determines E completely. The checker emits the finite systems through level four and checks their oscillator counterpart independently.

If Tr_Ph o(R)=q_h mathcal N, triangular subtraction from F_R=mathcal N Delta gives

| h | q_h |
|---|---:|
| 2 | 1 |
| 3 | -58 |
| 4 | 44022/41 |
| 5 | -977155/94 |
| 6 | 947015938/15717 |

For example t_(2,1)=34, so the primary weight-three trace is (-24-34)mathcal N, not -24mathcal N. Omitting this distinction would manufacture a false inconsistency.

Equation (10) independently requires

\[
q_6\mathcal N=4(18538750076)-a_6(312092484374).
\tag{12}
\]

Solving (12) gives precisely the norm in (2), calculated earlier without the weight-six rank. Thus the first-level Casimir and the forced sixth-level response agree exactly after descendant subtraction.

This is a completed compatibility check, not an independent additional condition: all its scalar ingredients are already fixed by the stated lower data, modularity and the finite channel. Its agreement does not identify the original cubic. The six-label operator polynomial and the compatibility of the thermally silent components of higher OPEs remain outside this result.

## 8. Prior work and what remains undetermined

[M] introduces the Casimir sums, their invariance, and their Virasoro recursion. [DM] establishes primary one-point modularity, descendant trace relations and, for the known moonshine theory, the unique invariant primary with normalized Delta response. Our R/mathcal N agrees with that known field there. We do not assume or prove the corresponding uniqueness of invariant primaries for every candidate.

The new work is an explicit normalization and cross-channel interpretation under the group's absence from the premises. The norm and compressed actions are presented with a reproducible finite certificate. Exact-number searches and the scoped sources checked here do not establish priority; equivalent constants may be implicit in older Casimir or genus-two calculations. No new general Casimir theorem is claimed.

The useful physical statement is narrower: within each admissible theory there is a uniquely maximally responding weight-twelve primary ray, canonically constructed from the first level, and its normalized strength and two compressed actions are fixed. It neither selects a theory among all candidates nor identifies its symmetry group. Additional invariant fields with zero primary one-point function, higher-point functions and the original interaction algebra remain undetermined.

The next selection question must keep track of the common higher-state realization and components perpendicular to R, or settle the earlier uncontracted operator implication. Another scalar measuring only the norm of this same functional will not classify the theory. No physical implementation, RG selection mechanism, full OPE reconstruction, manuscript, release or outreach is supplied.

## 9. Evidence and source depth

The new checker has **94 exact integer/fraction checks**. It emits all vacuum Gram systems through twelve, including the 21x21 norm certificate, all positive Virasoro recursion checks, the independent a6 certificate, finite channel recursion, and descendant-insertion matrices for the second normalization route. No floating-point error tolerance is used. The largest square matrix is 21x21.

Independent even-free-boson controls at c=2 and3 construct nonzero weight-four primary Casimir remainders, verify the Riesz identities on 18 pair-primary controls, and compute the zero modes using derivative-current normal ordering rather than the PBW insertion recursion. Two additional descendant matrices test that recursion. At c=2 the exact norm is 3/2. A weight-twelve control verifies all 21 Casimir pairings and the raw norm418; its vacuum-subtracted remainder is NOT primary, confirming the necessity of the extremal design assumption. These examples are not holomorphic c24 candidates.

The supplied preceding checkpoint's nine hashes and its 78-check report were verified unchanged. The new 94-check report agrees under normal/-O/-OO. These checks are finite consistency evidence, not proof-assistant verification or an independent review of the imported theorems. No full Monster matrix, character table, huge P6/P12 operator or full extremal OPE tensor is built.

The live main is pinned above. Runtime Git access failed at DNS resolution. Local checks are not claimed as a live-main historical replay. An additive PR may use the available connector writes, preserving all existing files and pending branches; its read-only workflow must report actual strict and bounded-portability outcomes separately. No outcome is presumed from a green overall check. The PR9 reporting erratum remains in force.

### Primary sources actually inspected

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Section2.2, especially equations(2.5)-(2.7), Lemmas2.3-2.4 and the normalization of the Casimir states. Printed page9 was visually inspected. His full V2 sum and our primary-only sum are explicitly distinguished. No disputed fifth coefficient is an input. https://arxiv.org/abs/math/0007169

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. Theorem3.1, design/trace interpretation and the explicit replacement paragraph at the end of section2. Printed page12 was visually inspected. The imported theorem, not an assumed Monster action, supplies lower trace cancellation. https://arxiv.org/abs/math/0701626

[DM] C. Dong and G. Mason, *Monstrous Moonshine of Higher Weight*, arXiv:math/9803116v2. Proposition2, its descendant-trace proof, and the introduction's discussion of invariant primaries at weights12,16,20 (printed page4). These parsed passages were read. Repeated screenshot requests for page4 failed; no visual inspection of it is claimed. The unique invariant primary assertion there uses known-moonshine representation information and is not transferred to unknown candidates. https://arxiv.org/abs/math/9803116

The exact Virasoro helper is a byte-preserved copy from the supplied Note20 checkpoint/earlier PR16. The oscillator helper is the unchanged Note13 file. The unitary adjoint conventions remain those of Dong-Lin arXiv:1308.2361; this is an inherited interface, not a new full paper audit. No downloaded paper or font file is bundled.
