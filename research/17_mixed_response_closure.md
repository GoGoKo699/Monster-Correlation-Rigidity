# The repeated mixed response is already fixed by the cubic trace identities

**Date:** 25 September 2026. **Live base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/mixed-response-closure`.

The owner is investigating physical selection of the Monster, not recognition of an imposed symmetry. This continuation answers the precise independence question in the supplied fifth-trace reconstruction checkpoint. It does not import PR12's false null-state condition. PR13 is the pending normalization audit; PR14, at `e608dec00a26c714a68ec33b9463faadacdce573`, independently derives the corrected mixed coupling from conformal-design and Virasoro identities. Those branches are preserved. The local reconstruction note and PR14 use different derivations and do not have identical scopes.

## 1. Result: the proposed two-insertion test is redundant

The preceding checkpoint proposed checking

\[
\operatorname{Tr}_{\wedge^2 P_2}(G\mathcal D_eG\mathcal D_f)
=15548010816\langle e,f\rangle.
\tag{1}
\]

**Equation (1) follows from the first, second and third primary multiplication trace identities alone.** The fourth and corrected fifth multiplication traces are not needed for this algebraic reduction. In particular, this scalar cannot be an additional condition selecting the weight-two algebra among tensors satisfying those earlier identities.

Together with the corrected mixed-action law, it recovers

\[
\operatorname{Tr}_{P_3}(H_eH_f)=1437501\langle e,f\rangle.
\tag{2}
\]

There is also an operator-level consequence, stronger than the summed trace:

\[
\boxed{\sum_{i=1}^{196883} H_{e_i}^{\,2}=\frac{53157}{4}I_{P_3}.}
\tag{3}
\]

Here the e_i form any real orthonormal basis of weight-two primaries and H_e is the action e_(1) compressed to weight-three primaries. Thus every unit vector v in P3 obeys

\[
\sum_i\|H_{e_i}v\|^2=53157/4.
\]

This fixes the total squared response in either direction: for a fixed input field e, summed over all primary matrix elements, and for a fixed primary state v, summed over all first-level fields. It does not make the individual matrix elements equal, identify the cubic, or prove a Monster action. These are dimensionless OPE/zero-mode strengths, not transition rates, an experimental susceptibility, a Lorentz-invariant perturbation protocol, or eigenstate thermalization.

The algebraic proof is short enough to give without a Casimir calculation or a large example. Small exact checks below test all factors, including the exterior normalization and the crossed contraction.

## 2. Assumptions and conventions

Let V be a d-dimensional real Euclidean space and C a fully symmetric real cubic tensor. Define symmetric multiplication matrices by

\[
(L_a)_{ij}=C(a,e_i,e_j).
\]

Assume, for all a,b,c in V,

\[
\operatorname{tr}L_a=0,\qquad
\operatorname{tr}(L_aL_b)=\kappa\langle a,b\rangle,\qquad
\operatorname{tr}(L_aL_bL_c)=\nu C(a,b,c),\quad\kappa>0.
\tag{4}
\]

Lowercase tr is the matrix trace on V; capital Tr below denotes trace on an exterior space. The physical values from Note12 are

\[
d=196883,\quad \kappa=13858/3,\quad\nu=899.
\]

The source of these values is the lower-order Matsuo trace identities after separating the stress direction, with Hoehn's explicitly stated conformal-design replacement for a large-automorphism hypothesis. No Monster matrix, character decomposition, or known multiplication table is assumed in the theorem. It applies to any cubic satisfying (4), whether or not that cubic is known to extend to a CFT.

Identify a wedge b with the skew matrix ab^T-ba^T, with inner product one half of the Frobenius product. Equivalently divide the matrix by sqrt(2) and use the full Frobenius product. Then e_i wedge e_j, i<j, is orthonormal. Define

\[
F(X)=\sum_iL_iXL_i,\qquad
\mathcal D_a(X)=L_aX+XL_a,
\]

and use F_- for its restriction to skew matrices. In this note

\[
G=F_-+\gamma I
\]

with an arbitrary real gamma until specializing to gamma=1/3. Tensor products on the ordered square act in the usual vectorization convention. All traces are unchanged by the equivalent two exterior normalizations.

Full symmetry of C and (4) imply

\[
\sum_iL_i^2=\kappa I,\qquad F(L_a)=\nu L_a.
\tag{5}
\]

For example, the mn entry of F(L_a) is a three-matrix trace with labels m,a,n, by permuting the three indices of C. These identities are not fourth-order inputs.

## 3. Three exterior trace calculations

For symmetric matrices A=L_e and B=L_f, define

\[
U_0=\operatorname{Tr}_{\wedge^2V}(\mathcal D_e\mathcal D_f),\quad
U_1=\operatorname{Tr}_{\wedge^2V}(F_-\mathcal D_e\mathcal D_f),\quad
U_2=\operatorname{Tr}_{\wedge^2V}(F_-\mathcal D_eF_-\mathcal D_f).
\]

The identities are

\[
\boxed{\begin{aligned}
U_0&=(d-2)\kappa\langle e,f\rangle,\\
U_1&=-\kappa\nu\langle e,f\rangle,\\
U_2&=\kappa\nu(\kappa-\nu)\langle e,f\rangle.
\end{aligned}}
\tag{6}
\]

They hold for all e,f, not merely for basis inputs.

### Exterior trace rule

If an operator preserves the exterior subspace, its restricted trace is the full trace after multiplication by (I-S)/2, where S swaps tensor factors. In each product expansion, use

\[
\operatorname{tr}_{V\otimes V}(A\otimes B)=\operatorname{tr}A\operatorname{tr}B,
\qquad
\operatorname{tr}_{V\otimes V}\big(S(A\otimes B)\big)=\operatorname{tr}(AB).
\tag{7}
\]

On the ordered square, D_e=A tensor I+I tensor A and F=sum_i L_i tensor L_i. Expanding (7) immediately gives U0, including the d-2 rather than d factor.

For U1, tracelessness of the L_i leaves

\[
U_1=\sum_i\operatorname{tr}(L_iA)\operatorname{tr}(L_iB)
-\operatorname{tr}\big((\sum_iL_i^2)AB\big)
-\operatorname{tr}(F(A)B).
\]

The first two terms are both kappa squared times the inner product and cancel. The remaining term is -kappa nu times the inner product.

### The apparently sixth-order contraction in U2

The ordinary tensor-square trace contributes, after the factor one half,

\[
\sum_{i,j}\operatorname{tr}(L_iAL_jB)\operatorname{tr}(L_iL_j)
+\sum_{i,j}\operatorname{tr}(L_iAL_j)\operatorname{tr}(L_iL_jB)
=(\kappa^2\nu+\kappa\nu^2)\langle e,f\rangle.
\]

The swap trace contributes two sums,

\[
Z_1=\sum_{i,j}\operatorname{tr}(L_iAL_jBL_iL_j),\qquad
Z_2=\sum_{i,j}\operatorname{tr}(L_iAL_jL_iL_jB).
\]

Both equal kappa nu squared times the inner product. For Z2, use F(L_i)=nu L_i and then F(A)=nu A. For Z1, write its entries explicitly. The only nontrivial contraction is

\[
\sum_{i,a,s} C_{iab}C_{irs}C_{jsa}
=\operatorname{tr}(L_bL_rL_j)=\nu C_{brj}.
\tag{8}
\]

Hence

\[
Z_1=\nu\sum_j\operatorname{tr}(AL_jBL_j)
=\nu\operatorname{tr}(AF(B))
=\kappa\nu^2\langle e,f\rangle.
\]

Subtracting Z1+Z2 proves U2. Equation (8) uses full tensor symmetry; a collection of arbitrary symmetric matrices is not a substitute for a symmetric cubic. No fifth- or sixth-order trace theorem is invoked.

## 4. The redundancy certificate and physical response

Expanding G on both sides and using cyclicity gives

\[
\boxed{\operatorname{Tr}(G\mathcal D_eG\mathcal D_f)
=\kappa\big[\nu(\kappa-\nu-2\gamma)+\gamma^2(d-2)\big]\langle e,f\rangle.}
\tag{9}
\]

For the physical values and gamma=1/3, the three contributions before combining are

| Term | Coefficient of the inner product |
|---|---:|
| U0 | 909458966 |
| U1 | -12458342/3 |
| U2 | 139047555062/9 |

Their combination U2+(2/3)U1+U0/9 is exactly **15548010816**. This is a proof of implication from the earlier equations, not failure to find a countermodel or merely a check in the known moonshine example.

The identification of (9) as a physical P3 response additionally uses

\[
G=282\Pi,\qquad
H_e\simeq\frac{282}{104}\Pi\mathcal D_e\Pi.
\tag{10}
\]

The first is the inherited weight-three Gram identity. The corrected mixed-action law in the supplied checkpoint and PR14 gives the second. The new algebraic proof of (9) does not depend on either derivation of the disputed fifth trace; applying it to physical H_e does depend on (10). Since G squared is 282G, cyclicity yields

\[
\operatorname{Tr}_{P_3}(H_eH_f)=\frac{\operatorname{Tr}(G\mathcal D_eG\mathcal D_f)}{104^2}
=1437501\langle e,f\rangle.
\]

This agrees with the independent whole-level trace calculation. Matsuo Theorem5.1(2), with its symmetry hypothesis replaced by the established design trace condition, gives 1478400 on V3. The block decomposition through D(V2) and P3 subtracts (9/4)*4620 and (1/2)*61008, leaving 1437501. This equality is a valuable normalization check, but is not a new polynomial restriction once (4) and (10) hold. Dropping descendant transitions would produce a different, incorrect coefficient.

## 5. Operator-level isotropy in the opposite direction

In addition to scalar traces, (4) gives the exact operator identities on the exterior space

\[
\sum_i\mathcal D_i^2=2\kappa I+2F_-,\qquad
\sum_i\mathcal D_iF_-\mathcal D_i=2\nu F_-.
\tag{11}
\]

The first is a direct expansion. For the second, the two direct terms reduce to 2nu F_- by (5). The two crossed terms vanish on skew tensors. To see this, set

\[
R=\sum_{i,j}L_iL_j\otimes L_jL_i.
\]

Its entries are

\[
R_{ab,cd}=\operatorname{tr}(L_aL_cL_bL_d).
\]

Transposition and cyclicity show these entries are symmetric in c,d; therefore R annihilates the antisymmetric input subspace. This uses only full cubic symmetry and ordinary matrix trace properties, not the fourth-trace numerical formula. It is checked separately on arbitrary small cubics, even ones not satisfying (4).

It follows that

\[
\sum_i\mathcal D_iG\mathcal D_i
=2(\nu+\gamma)F_-+2\gamma\kappa I.
\tag{12}
\]

More generally suppose G=pPi with p>0, and define H_i=(p/c_m)Pi D_i Pi for a nonzero normalization c_m. On the range of Pi, F_- has eigenvalue beta=p-gamma. Thus

\[
\boxed{\sum_i H_i^2
=\frac{2p}{c_m^2}\big[(\nu+\gamma)\beta+\gamma\kappa\big]I_{\operatorname{im}\Pi}.}
\tag{13}
\]

In the physical application p=282, beta=845/3 and c_m=104, giving equation (3). As a consistency check,

\[
196883\,(1437501)=21296876\,(53157/4).
\]

Taking a trace of (3) recovers the total of (2), but the operator statement itself applies to each vector, including complex superpositions. It does not assert that H_e H_f is proportional to the identity for each pair of fields. Nor does equality of total strengths specify their commutators, joint spectra, or individual transition amplitudes.

## 6. Where the physical-selection question goes next

This result removes the proposed repeated-action scalar from the list of possible new constraints: even a weaker subset of the preceding algebraic identities already forces it. The operator sum of squares is likewise a consequence, not an extra axiom to impose on unknown candidates. A selected aggregate response is not a selected interaction tensor or symmetry group.

An uncontracted next compatibility condition can be stated with its descendant correction intact. On V3 write

\[
E_a=a_{(1)}=\begin{pmatrix}(3/2)R_a&(1/2)b_a^\dagger\\(1/2)b_a&H_a\end{pmatrix},
\quad b_a(v)=B(a,v).
\]

Since [a_(1),b_(1)]=B(a,b)_(2), its primary block is

\[
\pi_3 B(a,b)_{(2)}\pi_3
=[H_a,H_b]+\tfrac14(b_a b_b^\dagger-b_b b_a^\dagger).
\tag{14}
\]

Any linear combination of pairs with sum B(a,b)=0 must also make the right side vanish. This is a statement about the action on each generated state, not its trace after summing all states. Equation (14) is a necessary exact mode identity, not a proven independent restriction on the earlier tensor system. It must be reduced algebraically or checked against a countermodel satisfying the complete antecedents before being called new. Discarding the last two terms is not permitted: primary compression does not commute with taking commutators.

PR14 identifies a different, compatible boundary: four weight-three zero-mode insertions have a top composite of weight twelve. The 11-design trace rule does not specify the nonvacuum trace of that component. The generic weight-twelve primary one-point function is allowed to be a multiple of Delta. This does not prove that its coefficient is free, nonzero or independent, or that all the vacuum-projection terms of a new mixed calculation are already determined by the cubic. Neither route should be described as a completed physical principle selecting the Monster.

The immediate follow-up should distinguish operator-level factorization from scalar contractions before computing more numerical trace coefficients. The existing algebraic system itself could be rigid, but that classification has not been established. No alternative complete CFT has been constructed here. The owner's physical-selection objective remains central; no circuit or gate-testing work is added.

## 7. Evidence, scope and integration

The new checker has **119 labelled checks**, using only integers and fractions. It tests the complete lower trace assumptions on five small cubic examples (dimensions2,3,4,6 and a rescaled case), every exterior trace on all basis pairs, both six-matrix contractions, and the shifted result at four values of gamma. It checks crossed-operator cancellation on three arbitrary symmetric cubics, and the full projected sum-of-squares law on two examples with both nonzero range and kernel. These are algebraic controls, not c24 CFTs. Negative controls distinguish full cubic symmetry from a list of symmetric matrices and exclude a decoupled harmonic cubic from the isotropic assumptions.

Largest square matrix:15 by15. No Monster data, dense extremal tensor, giant representation or CFT is constructed. The implication proof is the explicit contraction above, not the finite list of tests. The physical lower-trace inputs, source theorems and corrected-action derivations retain their separate review obligations. No formal verification, independent specialist review, comprehensive priority clearance or moonshine uniqueness is claimed.

The supplied fifth-trace ZIP was inspected and extracted without changing its bytes. Runtime public git checkout failed due DNS resolution; a local test is not claimed to be a live-main replay. Unlike the preceding turn, write actions are available in the connector in this continuation. A fresh additive branch/PR records this result without rewriting or merging PR12, PR13 or PR14. All current-main files, including its snapshot manifest, remain byte-identical in the proposed additive tree. A supplemental manifest and read-only workflow check the new files and unchanged baseline/candidate root verification, with strict and bounded-portability outcomes kept separate. Actual outcomes are reported only after reading the logs.

The primary four-point closure statement from Note14 has not received a new comprehensive audit in this turn, and the present trace reduction does not require its all-weight claim. No manuscript, release, outreach or large simulation is performed.

## Sources and inspected interfaces

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Corollary4.1's traces through order three and Theorem5.1(2)'s V3 two-zero-mode trace were reread. Printed page16 was visually inspected in this continuation; the higher-level trace passage was read in parsed text. The fifth-order disputed coefficient is not a premise of the new algebraic proof.
https://arxiv.org/abs/math/0007169

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. The explicit design-for-symmetry replacement at the end of section2 and Theorem3.1 were checked; printed page12 was visually inspected. This is the inherited reason lower-order trace values apply without assuming a Monster action, not a newly proved modular theorem.
https://arxiv.org/abs/math/0701626

[R] The supplied `Monster_Fifth_Trace_Reconstruction_Checkpoint.zip`, research/16_fifth_trace_reconstruction.md, especially sections6-7; and the separately inspected PR14 note at pinned head `e608dec00a26c714a68ec33b9463faadacdce573`, research/16_mixed_trace_reconstruction.md. The former reconstructs the primary coefficient vector using a source structural span; the latter gives a separate Ward/design derivation of -104 and the mixed action. Reading this derivation is not an independent execution/audit of its entire65-check certificate. Both are pending research evidence, not external expert reviews.

No downloaded papers or fonts are bundled. The new general contraction identities are presented as elementary deductions, not a priority-cleared new representation-theoretic theorem.
