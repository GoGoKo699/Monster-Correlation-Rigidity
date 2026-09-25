# Two complementary channels, rather than a truncated commutator

**Date:** 25 September 2026. **Live base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/odd-mode-completeness`. The primary-three checkpoint is pinned at `9254b954ed7e3d1fb2033175e66552fdf0092823` (PR16). This note does not merge that or any other pending branch.

## 1. A short structural statement

The owner asked for a simple physical explanation, not an indefinitely growing catalogue of identities. The preceding primary-three product was a projected matrix commutator. Here the first omitted sector is identified exactly.

Let P_h denote the real, PCT-fixed Virasoro primaries of weight h in the declared extremal class from Note12. For a,b in P2 set

B3(a wedge b)=pi3(a_(0)b),

B5(a wedge b)=pi5(a_(-2)b).

With unit exterior normalization, the result is

$$\boxed{\frac1{282}B3^\dagger B3+\frac12 B5^\dagger B5=I_{\wedge^2P2},\qquad B3\,B5^\dagger=0.}$$

Moreover each map is onto its entire primary space. Thus

$$x\longmapsto\left(B3x/\sqrt{282},\ B5x/\sqrt2\right)$$

is an orthogonal isomorphism from the antisymmetric pair space onto P3 direct sum P5. Combinations invisible in the weight-three primary coefficient are exactly the combinations carried by the weight-five primary coefficient. A null combination for one OPE coefficient is not a statement that all coefficients of the original field pairs vanish.

The zero-mode version is equally short. Define M_w=o(w)|P2, where o(w)=w_(h-1) for w in P_h. Then

$$\boxed{\mathfrak{so}(P2)=M(P3)\mathbin{\perp}M(P5).}$$

Here so(P2) means the **vector space of all real skew endomorphisms** of the first primary level. Its matrices have their ordinary commutator, but they are not all physical symmetry generators. In particular this does not identify the symmetry group with an orthogonal group, introduce weight-one currents, or construct the unrelated infinite-dimensional Monster Lie algebra.

For u,v in P3 define

beta3(u,v)=pi3(u_(2)v),

gamma5(u,v)=pi5(u_(0)v).

The omitted commutator component has an exact interpretation:

$$\boxed{[M_u,M_v]=\frac6{47}M_{\mathrm{beta3}(u,v)}+M_{\mathrm{gamma5}(u,v)}.}$$

A particular pair can have zero weight-five component. No claim that P3 pairs span all of P5 is made: surjectivity above concerns B5 on P2 pairs. The statement is that these two sectors exhaust every possible skew matrix component, and the displayed physical OPEs supply the two components of this commutator.

These are consequences of the declared physical assumptions and previous source theorems, not a new independent selection axiom or a classification of the starting cubic. Note18's separate uncontracted polynomial-independence question remains unresolved.

## 2. Inputs, metric and scope

The admissible theories remain nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs, with V1=0, minimizing positive central charge. The imported modular/design results give c=24, character J, and the trace-to-vacuum rule on V2 through field weight eleven [H]. This is a restricted selection problem, not a universal law or an RG dynamics. No Monster action, character decomposition, multiplication table or axis orbit is assumed here.

Write Y(w,z)=sum_n w_(n) z^(-n-1), and use the positive Hermitian form, real on PCT-fixed vectors. For a primary of weight h, [DL] gives

w_(n)^dagger=(-1)^h w_(2h-2-n).

For h=3 or5, M_w is skew adjoint. It kills the stress direction: commuting w_(h-1) through L_-2 1 gives a multiple of w_(h-3)1=0. Consequently its full V2 trace equals its trace on P2, and its image lies in so(P2).

Skew matrices have inner product <X,Y>_-=-tr(XY)/2. Identify the unit wedge a wedge b with ab^T-ba^T under this half-Frobenius metric. This fixes all factors of two. Complexification gives the corresponding Hermitian statements. For physical odd-spin Hermitian fields a factor i may instead be incorporated in the field convention; mixing those conventions without converting signs is not allowed.

At c24 the character calculation gives

| h | dim V_h | dim P_h |
|---|---:|---:|
| 2 | 196884 | 196883 |
| 3 | 21493760 | 21296876 |
| 4 | 864299970 | 842609326 |
| 5 | 20245856256 | 19360062527 |

For weight five specifically,

$$\dim P5=20245856256-2-3(196883)-2(21296876)-842609326.$$

The two vacuum descendants and the indicated low-level descendant multiplicities are retained. The relevant Virasoro Gram matrices are nondegenerate at c24; the certificate checks their positive leading principal minors. These are state counts, not assigned Monster representation dimensions.

## 3. The trace identities that make the dimension match meaningful

For u,v in P_h with h=3 or5,

$$\boxed{\operatorname{Tr}_{V2}(o(u)o(v))=t_h\langle u,v\rangle,\qquad t_3=-564,\quad t_5=-4.}$$

For u in P3 and v in P5,

$$\boxed{\operatorname{Tr}_{V2}(o(u)o(v))=0.}$$

These are statements on all inputs, not only orthogonal basis vectors. The h3 coefficient agrees with the inherited B3 normalization. The h5 coefficient and the cross-weight vanishing are obtained without using the joint multiplication spectrum or the disputed fifth-order trace table.

### Exact finite reconstruction

For homogeneous x of weight h define x star y=sum_(i=0)^h binom(h,i)x_(i-1)y. The mode iterate from [M, equation1.1], as explicitly summed in Note18, shows o(x star y)=o(x)o(y) on V2 when y is a primary of weight at least three. The correction terms first enter V1 or the vacuum; V1=0 and the primary creation/adjoint rules kill the vacuum terms. V2 is not being treated as a lowest-weight Zhu module.

For two equal weight-h primaries, x star y has components at ordinary weights 2h-i. At h5 these lie between five and ten, inside the conformal11-design range. At each weight, form the vacuum descendant Gram matrix in the basis L_-lambda 1 with all parts at least two. Its pairing against u_(p)v is a formal multiple of <u,v>. Starting with the coefficient (-1)^h at p=2h-1, successive Virasoro commutations give

$$\langle L_{-\lambda}1,u_{(p)}v\rangle
=(-1)^h\prod_{m\in\lambda}\big((h-1)(m+1)-p_{\rm current}\big)\langle u,v\rangle,$$

where p_current increases by m at each step, and the expression is zero unless the final index is 2h-1. Solve the exact Gram system and evaluate descendant zero modes on the stress state and on 196883 weight-two primary modules.

For h5 the weighted trace contributions are

| Composite weight | Vacuum Gram size | Contribution |
|---|---:|---:|
| 10 | 12 | -613019 |
| 9 | 8 | 2643600 |
| 8 | 7 | -4519500 |
| 7 | 4 | 3823700 |
| 6 | 4 | -1598225 |
| 5 | 2 | 263440 |
| **Total** | | **-4** |

No division by a possibly zero norm/correlation is used: the pairing coefficient is formal. The complete certificate, including every matrix and projection vector, is emitted by the checker. The h3 calculation reproduces -564.

For primaries of different weights, all pairings with vacuum Virasoro descendants vanish: commuting the Virasoro operators to the fields reduces the pairing to an inner product of one primary with a descendant of the other. They are orthogonal. Their star product has weights at most eight, so the design rule gives the cross trace zero. This is an analytic orthogonality argument, not a conclusion from a numerical dimension match.

## 4. Completeness proof in three steps

First, positivity and skew adjointness turn the trace identities into

$$\langle M_u,M_v\rangle_-=282\langle u,v\rangle\quad(u,v\in P3),$$

$$\langle M_u,M_v\rangle_-=2\langle u,v\rangle\quad(u,v\in P5).$$

Thus both zero-mode maps are injective, and their images are orthogonal. Second,

$$21296876+19360062527=\frac{196883\cdot196882}{2}.$$

Their dimensions therefore fill the entire skew-matrix space. The rank statement is secured by the nonzero norm identities before using this count. This proves the zero-mode decomposition.

Third, relate those zero modes to the pair coefficients. For a,b in P2 and w in P_h, h=3,5, adjoint invariance and skew symmetry give

$$\langle w,\pi_h(a_{(3-h)}b)\rangle=\langle a,M_wb\rangle
=\langle a\wedge b,M_w\rangle_-.$$

Derivative terms disappear against the primary w. Hence B_h^dagger w=M_w. Each B_h B_h^dagger is p_h I with p_3=282,p_5=2. If Pi_h is the projector onto M(P_h), then

$$B3^\dagger B3=282\Pi_3,\quad B5^\dagger B5=2\Pi_5,\quad\Pi_3+\Pi_5=I.$$

This proves the opening completeness relation and both surjectivity statements. In terms of the earlier contraction G, Pi_3=G/282 and Pi_5=I-G/282. The missing weight-five map is therefore canonically the complementary projection, up to a choice of orthonormal basis in P5.

There is a useful limitation. The weight-five Gram relation by itself could also be recovered as another coefficient of the already determined four-point kernel. It is not claimed as a new independent constraint. The organizing result is the identification of the **whole** skew operator space and the interpretation of the omitted commutator component below. Nothing here selects the initial cubic up to single-field basis change.

## 5. The weight-five term of a weight-three commutator

A second finite Ward calculation gives, for w in P5 and u,v in P3,

$$\boxed{\operatorname{Tr}_{V2}(M_wM_uM_v)=-2\langle w,u_{(0)}v\rangle.}$$

Here the star sum has top weight eleven, still within the inherited design rule. It uses no weight-twelve primary one-point data. The independent coefficient convention <u,v_(4)w> agrees with <w,u_(0)v>; both are checked in an explicit unitary free-boson example. Cyclic permutations of the weights (3,3,5), (5,3,3) and (3,5,3) all give -2 in their corresponding first-slot Hermitian convention.

For ordering (3,3,5), the contributions at weights5,...,11 are

131720, -958935, 2867775, -4519500, 3965400, -1839057, 352595,

which sum to -2. The largest Gram matrix is14x14. The full rational certificate is included. This extends the verified primary Ward engine from PR16; it is not an independent reimplementation of every PBW routine. The new pairings are checked separately by direct oscillator modes.

For skew matrices A,B,C,

$$\langle A,[B,C]\rangle_-=-\operatorname{tr}(ABC).$$

The -2 trace identity and the norm2 of M(P5) consequently imply

$$\Pi_5[M_u,M_v]=M_{\gamma5(u,v)},\qquad \gamma5(u,v)=\pi_5(u_{(0)}v).$$

The preceding -36 identity and norm282 on M(P3) imply

$$\Pi_3[M_u,M_v]=\frac{36}{282}M_{\beta3(u,v)}=\frac6{47}M_{\beta3(u,v)}.$$

Since the two images fill so(P2), these two projections give the full commutator, with no unidentified skew component. This establishes the formula in section1.

The field product itself is not asserted to close on P3 direct sum P5 at every mode. The equation identifies zero-mode matrix actions on P2 and the specified primary OPE components. Higher fields and descendants remain part of the full CFT.

## 6. The projected Jacobi defect is a specific omitted interaction

The same mixed trace, viewed with external weights (3,5,3), gives

$$M_{\delta3(w,u)}=141\Pi_3[M_w,M_u],\qquad
\delta3(w,u)=\pi_3(w_{(4)}u),\quad w\in P5,\ u\in P3.$$

Apply ordinary matrix Jacobi and project onto M(P3). In terms of the physical primary products,

$$\boxed{\sum_{\rm cyc}\beta3(\beta3(u,v),z)
=-\frac{47}{108}\sum_{\rm cyc}\delta3(\gamma5(u,v),z).}$$

The constant is (47/6)^2/141=47/108. The identity follows for every admissible candidate; it does not require the projected beta3 product itself to obey Jacobi. It quantifies the difference between retaining one sector and retaining both components of the matrix action.

This is the simple interpretation of the earlier projection warning: a failure of Jacobi after removing P5 need not be a failure of the underlying theory. The missing term is an actual, normalized OPE channel, not an arbitrary correction. The identity does not establish an L-infinity structure, prove Jacobi for every primary truncation, or introduce a new continuous symmetry. No existence of a nonzero Jacobi defect for every candidate is assumed; both sides can vanish for special inputs.

The checker uses a small split of so(4) only to verify this algebraic correction and show why discarding the complement can change an answer. It is not asserted to be a physical CFT or a countermodel to the full cubic equations.

## 7. What remains unresolved

The earlier operator condition from Note18,

Pi[9 Q_x+24336 ad_x-2704 ad_(Gx)]Pi=0,

still has no completed implication/independence certificate against the full antecedent cubic system. A bounded attempt at substitutions using lower trace contractions did not establish either outcome. This note must not be cited as deciding that question.

The new completeness relation reorganizes the problem: the odd zero-mode actions through weight five fill a familiar matrix space, and a previously projected-away commutator term is identified. It does not prove that all possible decompositions of that matrix space and all starting cubics are equivalent. The two sectors still depend on the unknown interactions. A matrix-space isometry is not necessarily induced by a change of basis of P2, and an arbitrary change of low-energy basis need not preserve all OPEs.

In particular, exponentiating an arbitrary skew matrix from the complete space does not give a symmetry of the CFT. Energy-level degeneracy allows such matrices as operators; actual internal symmetry must preserve every product and the vacuum/conformal structure. The Monster's simplicity is not being assumed as a selection condition.

The next sharp question is whether the compatibility of this two-channel decomposition with the symmetric primary multiplication is already forced by the earlier identities. The explicit Note18 residual is one formulation of that question. The present result provides a simpler description of the missing sector rather than an additional unexplained scalar condition. No new uniqueness theorem, alternative complete CFT, or universal physical selection law is claimed.

## 8. Evidence and primary-source scope

`checks/verify_odd_mode_completeness.py` emits **79 exact checks** and all pair/triple certificates. Every coefficient uses integer/fraction arithmetic. It regenerates the character through weight five from E4^3/Delta, subtracts Virasoro descendants with positive low-level Gram checks, and verifies all rank/scaling arithmetic. No Monster character table or group representation is used.

Independent c3 even-Heisenberg controls include an explicit eight-monomial weight-five primary with norm1024/25; all five positive Virasoro modes annihilate it. Direct normal-ordered fields verify37 weight-five pair projections,130 mixed composite pairings through weight11,17 cross-weight vacuum pairings, and36 pair-to-zero-mode adjoint identities. A nonzero 3,3,5 coefficient is -48/5 in that control. These are not holomorphic c24 theories. The test of the universal coefficient uses the exact conformal-design/Virasoro certificate, not an assertion that the free-boson control satisfies the design rule.

The largest square matrix in the delivered checker is14x14; private oscillator cutoff16. No full extremal OPE tensor, 196883-dimensional matrix, or large cloud simulation is constructed. The finite arithmetic is not a proof of the imported design theorem or formal verification of the whole VOA argument. No independent specialist review or comprehensive priority clearance is claimed. The group-theoretic decompositions for the known moonshine example are not being advertised as new observations.

The unchanged primary Ward engine from PR16 is copied under the additive name `odd_mode_ward.py`, with its provenance recorded. The old oscillator helper remains byte-identical. Normal/-O/-OO reports reproduce locally. Runtime Git DNS failed; local checks do not constitute a current-main root replay. A dedicated read-only workflow checks actual baseline/candidate preservation, unchanged historical verification and its separate portability policy, and the exact new report. Actual outcomes must be inspected before claiming them. All old main files and pending research branches are preserved. No manuscript, release or researcher outreach is performed.

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1, Theorem3.1 and the trace replacement at the end of section2. The relevant parsed text was read; printed page12 was visually inspected in this continuation. The imported result supplies the trace-to-vacuum rule, not a Monster action.
https://arxiv.org/abs/math/0701626

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1, section1 mode iterate and Virasoro conventions. These were read in parsed text; printed page16 was visually inspected for the existing lower-order context. The disputed fifth-order coefficient is not an input to either new certificate.
https://arxiv.org/abs/math/0007169

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1, Definition2.2 and the Heisenberg unitary construction. These are the inherited adjoint/PCT and positive-metric assumptions; the indicated passages were checked, not the whole paper.
https://arxiv.org/abs/1308.2361

[PR16] Pinned `9254b954ed7e3d1fb2033175e66552fdf0092823`, Note18 and `checks/primary_three_ward.py`, supplied in `Monster_Primary_Three_Bracket_Checkpoint.zip`. Its certificate was re-executed in this continuation. This is pending research evidence, not an external expert review. No downloaded papers or font files are bundled.
