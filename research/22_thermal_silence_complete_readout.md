# Thermal silence is compatible with complete low-energy readout

**Date:** 26 September 2026. **Base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Additive branch:** `research/thermal-silence-readout`.

## 1. The distinction that resolves the apparent paradox

The canonical field in Note21 is the unique direction of maximal *thermal one-point* response. It acts as a scalar on the first primary level P2. The present result concerns the many fields that have identically zero thermal one-point functions. Their zero modes are not invisible on individual states: **primaries of weights two through six span every traceless Hermitian operator on P2**. Weight six is the minimal cutoff for this complete linear, single-insertion readout on arbitrary density matrices.

Consequently, with an explicit weighting of the probe coefficients,

\[
\boxed{\sum_{h=2}^{6}\frac1{\lambda_h}\sum_\alpha
\big(\operatorname{Tr}(\rho A_{h\alpha})\big)^2
=\operatorname{Tr}\rho^2-\frac1d,\qquad d=196883.}\tag{1}
\]

Every pure state in P2 has a nonzero signal of exactly 1-1/d in this normalization, although every participating field has zero canonical thermal one-point function. An arbitrary state on this primary space is determined by these expectation values. This does not supply an efficient measurement scheme, a bounded observable on the entire CFT, or an identification of the CFT from its thermal data.

The result is a corollary reorganizing the earlier channel identities. It introduces no additional selection axiom. The odd-mode completeness part is already in pending PR17; Note20/21 supply the weight-six pair channel. What is added here is the complete complex-Hermitian reconstruction, its exact minimal linear cutoff, the purity identity, and quantitative limits on hiding states from the specified entire probe family. Standard linear algebra, rather than another high-order trace calculation, proves the implications.

The original interaction tensor remains unclassified. The unresolved uncontracted operator equation from Note18 is not settled. A spectrum of possible readout operators and their norms need not identify how those operators are embedded relative to the multiplication tensor.

## 2. Physical class and probe conventions

Retain the declared problem: nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs/VOAs, with V1=0, minimizing positive central charge. The prior modular/design argument yields c=24, character J and a real primary space V=P2 of dimension d=196883. These are restrictions on the admissible theories, not a universal law, RG mechanism, or asserted microscopic model. No Monster action, character table, multiplication table or axis classification is assumed.

All matrix statements concern the complexification of P2, not all V2 or the full Hilbert space. In particular V2 also contains the stress state. Write pi2 for the primary projection. For a PCT-fixed real primary w of weight h, define

\[
M_h(w)=\pi_2 w_{(h-1)}\pi_2.
\]

The positive-unitary adjoint convention [DL, Definition2.2] gives M_h(w)^T=(-1)^h M_h(w). Hence define the Hermitian compressed observable

\[
A_h(w)=\begin{cases}M_h(w),&h\text{ even},\\ iM_h(w),&h\text{ odd}.\end{cases}\tag{2}
\]

The factor i is a phase convention making odd zero modes self-adjoint; it is not an extra state, copy, or symmetry assumption. It is also essential for access to imaginary coherences of a complex density matrix. Even fields alone give only real symmetric matrices.

Each P_h carries its state inner product from the normalized two-point function. Let {w_(h,alpha)} be any real orthonormal primary basis, including possible zero-mode kernel vectors, and abbreviate A_(h,alpha)=A_h(w_(h,alpha)). All matrix Hilbert-Schmidt norms and traces are **unnormalized** in this note. This differs from the earlier normalized-Frobenius gate convention.

The conformal 11-design theorem [H, Theorem3.1] implies

\[
\operatorname{Tr}_{V_n}o(w)=0\quad\text{for every }n\text{ and }2\le h\le6.
\tag{3}
\]

Thus every such primary has identically vanishing thermal one-point function. The trace on P2 is also zero: the stress diagonal matrix element vanishes. For h>=3 the zero mode kills the stress vector; for h=2 it may mix stress and primaries, but its stress diagonal entry is zero. Compression to P2 must not be replaced by an assertion of invariant-subspace dynamics for h=2.

These dimensionless statements use the fixed plane/zero-mode normalization. On a physical cylinder, field insertions acquire their weight-dependent size factors. No thermodynamic limit or implementable set of bounded microscopic noise operators has been assumed.

## 3. The finite channel input: five orthogonal matrix spaces

For every h define the ordered-pair primary map

\[
B_h(a\otimes b)=\pi_h(a_{(3-h)}b),\qquad a,b\in P2.
\]

It is symmetric for even h and antisymmetric for odd h after primary projection. It uses the ordered tensor-product metric: a unit antisymmetric tensor is (a tensor b-b tensor a)/sqrt(2). In particular B3 has squared nonzero singular value **564**, twice the value282 in the unit-wedge convention of Note13. Likewise B5 has value4 rather than2. These factors must not be mixed.

Adjoint invariance and skew symmetry give, in real orthonormal coordinates,

\[
(B_h^\dagger w)_{ij}=\langle w,B_h(e_i,e_j)\rangle=(M_h(w))_{ij}.\tag{4}
\]

To verify the sign, move e_i's (3-h)-mode to its (h-1)-adjoint, then use skew symmetry. Positive derivatives disappear when paired with the primary e_j; the remaining (-1)^h is cancelled by transposing the parity-(-1)^h matrix M_h(w). Thus no extra minus sign remains in (4).

Let L_a be the primary multiplication matrix, F(X)=sum_i L_i X L_i, Q=m^dagger m and J(X)=Tr(X)I. Notes12-14 give their joint operator decomposition. Only the finite channel coefficients through h=6 are needed here; no all-weight four-point-closure assertion, fifth trace, or weight-twelve norm is used to prove completeness.

| h | Range in matrix space | Rank | B_h^dagger B_h on that range: lambda_h |
|---|---|---:|---:|
| 2 | multiplication operators, symmetric | 196883 | 13858/3 |
| 3 | F_-=845/3, antisymmetric | 21296876 | 564 |
| 4 | F_+=155/3, symmetric | 842609326 | 54 |
| 5 | F_-=-1/3, antisymmetric | 19360062527 | 4 |
| 6 | F_+=-7/3, symmetric | 18538750076 | 4 |

These are subspaces defined by the unknown cubic, not assigned irreducible representations of a known group. In particular P6 is larger than its displayed image and has a large zero-mode kernel. Zero columns in a primary basis do not invalidate the frame identities below.

### Finite reconstruction rather than an assumed dimension match

For independent external labels a,b,c,d set A=<a,b><c,d>, B=<a,c><b,d>, C=<a,d><b,c> and X=<a*c,b*d>, Y=<a*b,c*d>, Z=<a*d,b*c>, where * is the full product including stress. The raw pair Gram at levels0,1,2,3 is A,0,Y,Y+X-Z. For 4<=n<=6 it is

\[
\binom{n-1}{3}B+\delta_{n4}C+(n-2)X+Y-Z.\tag{5}
\]

This follows from the ordinary mode commutator; it is the finite range of Note14's kernel derivation. Projecting off all Virasoro descendants is triangular in n. For a primary of weight h, the descendant contribution at level n is determined by its Gram matrix and the pair-primary Ward coefficients. The checker emits all these rational systems through six (largest5x5), including the vacuum module, and obtains exactly the five nonzero eigenvalues in the table. Small Fock examples separately test the pair-to-zero-mode adjoint (4) and raw primary projection.

The joint spectral identities giving the six pair sectors remain inherited source-dependent premises. The finite arithmetic certificate checks their consequences; it does not independently prove the VOA trace theorem or turn arbitrary scalar multiplicities into a physical tensor.

## 4. Completeness and the exact reconstruction formula

After multiplying antisymmetric ranges by i as in (2), the five ranges are orthogonal real subspaces of Herm_0(P2). Denote their orthogonal projectors by P_h. Their ranks sum to

\[
196883+21296876+842609326+19360062527+18538750076
=d^2-1=38762915688.
\]

Their sum is therefore the traceless Hermitian projector. Equation(4) and the table give the frame operator of each primary weight:

\[
\sum_\alpha A_{h\alpha}\operatorname{Tr}(A_{h\alpha}X)
=\lambda_h P_hX.
\]

Adding the five orthogonal resolutions proves, for every Hermitian X,

\[
\boxed{X-\frac{\operatorname{Tr}X}{d}I
=\sum_{h=2}^{6}\frac1{\lambda_h}\sum_\alpha
\operatorname{Tr}(A_{h\alpha}X)A_{h\alpha}.}\tag{6}
\]

This is an explicit inverse at the level of known operator families. It is not an algorithm for recovering their unknown matrix entries from the partition function. An actual state-readout experiment would still need calibrated access to those fields and their coefficients.

Taking a Hilbert-Schmidt inner product of (6) with X yields Parseval:

\[
\sum_{h,\alpha}\frac{|\operatorname{Tr}(A_{h\alpha}X)|^2}{\lambda_h}
=\operatorname{Tr}X^2-\frac{(\operatorname{Tr}X)^2}{d}.\tag{7}
\]

For a density matrix rho this is (1), and (6) reconstructs rho after adding I/d. For two states rho,sigma it gives the exact squared Hilbert-Schmidt distance. Thus I/d is the only state on P2 with all these primary-mode expectation values zero. I/d is the uniform state on the **primary portion** of the first energy level, not the complete finite-temperature Gibbs state of the theory.

There is no paradox with (3). A vanishing trace is a cancellation over a whole energy space, not a bound on the operator or on every state. Every one of these fields can have a zero thermal one-point function while the collection resolves the whole first-level density matrix.

### Minimality of the linear cutoff

At h<=5, the symmetric F=-7/3 sector is missing. For any nonzero real Hermitian X in that sector, the two states rho_+=I/d+epsilon X and rho_-=I/d-epsilon X are distinct and positive for 0<epsilon<1/(d||X||_op), yet have identical expectation values for all primary modes through weight five. Weight six removes this entire missing sector.

This proves minimality for **linear single-primary-mode readout of arbitrary states**. It is not a lower bound for nonlinear sequences, products of lower fields, pure-state-only reconstruction, arbitrary measurements, or querying already known matrix entries. Virasoro descendants of a fixed primary have proportional matrix elements between two equal-weight primary external states by the three-point Ward identities, but that observation is not used to claim a resource lower bound for general composite experiments.

## 5. A bounded-probe distinction and a code-space consequence

For unit w in P_h, the table gives ||A_h(w)||_F<=sqrt(lambda_h). Hence the normalized compressed operator

\[
E_h(w)=A_h(w)/\sqrt{\lambda_h}
\]

has operator norm at most one **on P2**. For Delta=rho-sigma, optimizing w separately in each primary space gives

\[
\sup_{\|w\|=1}|\operatorname{Tr}(\Delta E_h(w))|=\|P_h\Delta\|_F.
\]

Since the five squared norms sum to ||Delta||_F^2, at least one homogeneous primary of weight h<=6 satisfies

\[
|\operatorname{Tr}(\Delta E_h(w))|\ge\|\Delta\|_F/\sqrt5.\tag{8}
\]

For orthogonal pure states the contrast is at least sqrt(2/5). The chosen field may depend on both states and on the unknown theory; this is an existence bound, not a state-independent small list of practical probes. Its normalization on P2 is not a uniform norm bound on the whole CFT. No zero-mode measurement circuit or fault-tolerant resource bound is supplied.

An exact error-detection consequence is also immediate. Let Q_C project onto a k-dimensional subspace C of P2, and define

\[
D_{h\alpha}=Q_C A_{h\alpha}Q_C
-\frac{\operatorname{Tr}(Q_C A_{h\alpha})}{k}Q_C.
\]

The map X -> Q_C X Q_C-Tr(Q_C X)Q_C/k is the Hilbert-Schmidt projection onto traceless Hermitian matrices supported on C. Its rank is k^2-1. Applying the Parseval frame to this projection gives

\[
\boxed{\sum_{h,\alpha}\frac{\|D_{h\alpha}\|_F^2}{\lambda_h}=k^2-1.}\tag{9}
\]

Therefore no k>=2 subspace detects every member of this entire probe/error family exactly. Equivalently it cannot satisfy the Knill-Laflamme conditions for an error family containing the identity and all these compressed operators [KL, Theorem3.2]. The KL theorem is prior work; (9) is its elementary frame specialization.

There is a normalized uniform obstruction as well. For any k>=2 choose two orthogonal unit vectors in C and use (8). For some normalized E_h(w),

\[
\inf_{a\in\mathbb R}\|Q_C E_h(w)Q_C-aQ_C\|_{\rm op}\ge1/\sqrt{10}.\tag{10}
\]

This is a necessary-condition failure for the **whole norm-calibrated compressed family**, not a recovery-fidelity theorem. It does not exclude approximate error correction against a specified small noise set, spatial erasure, volume-suppressed local insertions, or in other energy sectors. The asymptotic ETH/AQECC settings in [BC] concern different operator families and limits. We do not refute ETH, holographic coding or CFT codes by observing a finite low-energy degenerate level.

## 6. Relation to the canonical thermal field and to symmetry

The pending Note21 construction gives o(R)|P2=(||R||^2/d)I. Thus the canonical field with the strongest thermal one-point function distinguishes **none** of the states within P2 through its zero mode. In contrast, the low-weight fields whose thermal one-point functions all vanish collectively distinguish **every** such state.

This contrast is exact and useful: the thermal functional captures the scalar average and does not reconstruct the operator information. It must not be identified with a complete physical description. A unique thermal-response ray cannot by itself identify a theory's interactions or its internal symmetry group.

Full matrix-space access is also not full symmetry. A matrix realized as the zero mode of a field need not preserve the multiplication or any higher OPE. Exponentiating arbitrary skew actions does not create continuous internal symmetries. The potential Monster group is the group compatible with all the interaction data, not the set of all available matrices on one degenerate level.

This result is therefore a constraint on how we interpret the physical structure, not another independent polynomial selection condition. The original cubic and the embeddings of the five orthogonal sectors remain to be determined. The next truly selective question must concern their compatibility with shared operator products, rather than further scalar thermal averages. Note18's uncontracted implication/independence problem remains open in the project; no claim of a countermodel or a new classification is made here.

## 7. Evidence, provenance and priority boundaries

`checks/verify_thermal_silence_readout.py` has **112 exact integer/fraction checks**. It reconstructs the finite primary Gram table, verifies full real/imaginary state reconstruction and code-space residuals on rational complex matrices of dimensions2,3,4, and independently computes even-free-boson modes through weight six at c=2. The latter test constructs the full35-dimensional even Fock space at grade six, with a largest descendant Gram28x28. It checks all primary conditions, parity, the ordered-pair/zero-mode duality and the frame operator against direct derivative-current normal ordering. The boson theory is not an extremal holomorphic c24 example. The small rational frames are linear-algebra controls, not CFTs.

The primary Gram coefficient certificate has largest size5x5. The overall largest square matrix is28x28. No Monster character table, group matrix, full extremal tensor or large P2 operator is constructed. Passing these checks is not a source-theorem proof, formal verification, independent specialist review, or novelty clearance.

The supplied Note21 checkpoint's thirteen hashes were verified, and its94-check report was reproduced in normal mode without changing source bytes. The new proof of completeness does not depend on its weight-twelve norm; that note is used only for the contrast in section6. The copied Virasoro helper is byte-identical to the supplied one, and the existing Note13 oscillator helper is read without modification. Pending PR17's odd completeness is explicitly credited; its entire79-check suite was not independently rerun in this continuation.

All live-main files and pending PR branches are preserved. Runtime Git networking failed at DNS resolution, so local new-check execution is not described as a live-main historical replay. An additive workflow separately checks pinned baseline/candidate preservation, unchanged strict replay and bounded portability, and the new report in normal/-O/-OO modes. Actual outcomes must be read individually. No report is regenerated to conceal an old mismatch. No manuscript, release, outreach or practical implementation is performed.

The inverse/frame and error-detection arguments are standard linear algebra once the five-range resolution is known. This is an explicit derived consequence, not a claim of a new general tomography, design, or coding theorem. A scoped search did not provide a primary theorem with exactly this weight-six cutoff and normalization, but an unmatched search is not evidence of novelty.

## Sources and inspected scope

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. Definition and Theorem2.3; Theorem3.1 and its modular proof context. The definition and trace interpretation were read in parsed text; printed page13 was visually inspected. The earlier design-to-trace replacement and resulting joint multiplication identities remain inherited inputs from Note12.
https://arxiv.org/abs/math/0701626

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1, Definition2.2. The positive Hermitian/PCT convention was reread and printed page3 visually inspected. This is not a full audit of their unitarity proof.
https://arxiv.org/abs/1308.2361

[KL] E. Knill and R. Laflamme, *A Theory of Quantum Error-Correcting Codes*, arXiv:quant-ph/9604034v1, Theorem3.2, printed page13. The two displayed matrix-element conditions and their immediate context were read and visually inspected. We use the identity-error case as a necessary condition; no new general recovery theorem is claimed.
https://arxiv.org/abs/quant-ph/9604034

[BC] N. Bao and N. Cheng, *Eigenstate Thermalization Hypothesis and Approximate Quantum Error Correction*, arXiv:1906.03669. Section2's operator-family and thermodynamic-limit assumptions were read in parsed text. The screenshot request failed. It is cited to delimit, not transfer, the ETH/AQECC conclusions; its recovery analysis is not a premise here.
https://arxiv.org/abs/1906.03669

Project inputs: main Notes12-14; PR17 `research/19_odd_mode_completeness.md` at `fde92a04964def3a12c5a8cc75362c4fced96c73`; supplied Note20/21. No downloaded papers or font files are bundled.
