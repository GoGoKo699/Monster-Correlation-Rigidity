# The next primary level has a determined cubic interaction

**Date:** 25 September 2026. **Live base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/primary-three-bracket`. PRs12–15 were inspected and remain separate. No pending branch is silently merged or rewritten.

## 1. Result and scope

This continues the physical-selection question, not engineered gate recognition. In the declared class of Note12 (unitary strongly rational bosonic holomorphic chiral theories, no weight-one currents, minimum positive central charge), let a,b,c be real PCT-fixed Virasoro primaries of weight three. Then

\[
\boxed{\operatorname{Tr}_{V_2}(a_{(2)}b_{(2)}c_{(2)})
=-36\langle a,b_{(2)}c\rangle.}\tag{1}
\]

This is reconstructed from the conformal-design trace rule through weight nine and explicit Virasoro vacuum projection. It does not use the disputed fifth-trace coefficient, a Monster representation, or an assumed Griess multiplication table. The calculation is formal in the three-point coefficient, so it includes cases where that coefficient is zero.

Combined with the already derived onto pair map B from weight-two to weight-three primaries, equation (1) determines the entire primary 3,3,3 coupling once the original 2,2,2 tensor is specified. The result is a projected matrix-commutator law, not only a summed response. It supplies an explicit uncontracted consistency equation relating two routes to a mixed action.

**The independence of that equation from the earlier full cubic identities is not established in this continuation.** No countermodel satisfying all those identities has been supplied, and no complete algebraic reduction of the new equation to them has been proved. A new necessary equation is not automatically a new selection principle. The original interaction tensor remains unclassified, and Monster uniqueness is not claimed.

The underlying physical restrictions remain substantial assumptions, not a universal law or demonstrated dynamical selection process. Known moonshine data are used only for a separate consistency witness below, not to identify an unknown candidate.

## 2. Reality, adjoints and the primary product

Write Y(a,z)=sum_n a_(n) z^(-n-1), and normalize the positive Hermitian form by ||1||=1. Work first on the PCT-fixed real space and extend sesquilinearly. For a primary of weight h,

\[
a_{(n)}^\dagger=(-1)^h a_{(2h-2-n)},\qquad L_m^\dagger=L_{-m}.
\]

In particular a_(2) is skew adjoint at weight three. It is not legitimate to use the even-weight adjoint rule for these modes. The convention is fixed by [DL, Definition2.2].

Let pi3 be orthogonal projection onto the weight-three primary space, and define

\[
\beta(a,b)=\pi_3(a_{(2)}b).
\]

Virasoro invariance makes positive-level descendants orthogonal to primaries. Skew symmetry and the adjoint formula imply that the three-form

\[
\varphi(a,b,c)=\langle a,b_{(2)}c\rangle
\]

is totally alternating on real primaries. Raw a_(2)b need not itself be primary. Thus beta is an alternating product with invariant positive metric, but is not presumed to satisfy the Jacobi identity or define conserved weight-one currents.

All claims below concern primary OPE data and zero-mode matrix elements. They are not rates, experimentally available controls, an RG flow, or a proof of an emergent continuous Lie symmetry.

## 3. Reduce the trace to weights at most nine

The inherited extremal conformal-design theorem [H, Theorem3.1] supplies

\[
\operatorname{Tr}_{V_2}o(u)=\operatorname{Tr}_{V_2}o(\pi_{\rm vac}u)
\]

for every homogeneous u through weight eleven, where o(u)=u_(wt(u)-1). Only weights three through nine are used here. This is an imported theorem, not a consequence of the numerical checker.

For homogeneous x of weight h define the finite state sum

\[
x\star y=\sum_{i=0}^h\binom hi x_{(i-1)}y.
\]

Summing the Borcherds iterate [M, equation(1.1)] yields

\[
\begin{aligned}
o(x\star y)={}&o(x)o(y)
+\sum_{j\ge1}x_{(h-1-j)}y_{(k-1+j)}\\
&+\sum_{j\ge0}y_{(k-2-j)}x_{(h+j)},
\end{aligned}\tag{2}
\]

with k=wt(y), applied componentwise when the state sum is inhomogeneous. This is not an assertion about Zhu multiplication on a lowest-weight module: V2 is not assumed to be such a module.

On V2, the extra terms first pass through V1 or the vacuum. The V1 terms vanish because V1=0. If y is a weight-three primary, the possible vacuum terms vanish as well: y_(4)V2=0 by its adjoint and y_(0)1=0, and the return term contains y_(0)1. Hence o(x star y)=o(x)o(y) on V2 for arbitrary homogeneous x with this right-hand y.

Apply the identity twice. For weight-three primaries a,b,c,

\[
\operatorname{Tr}_{V_2}a_{(2)}b_{(2)}c_{(2)}
=\operatorname{Tr}_{V_2}o(\Xi),
\]

\[
\Xi=(a\star b)\star c
=\sum_{i=0}^3\sum_{j=0}^{6-i}
\binom3i\binom{6-i}j(a_{(i-1)}b)_{(j-1)}c.\tag{3}
\]

Each summand has ordinary conformal weight N=9-i-j, between three and nine. The design trace rule therefore determines its trace from the vacuum Virasoro component.

## 4. Complete finite certificate for the coefficient -36

Set t=phi(a,b,c) as a formal scalar. Use the vacuum basis u_lambda=L_-lambda1 ... L_-lambdal 1, with nonincreasing parts at least two. At each N let M_N be its Gram matrix, b_N the pairing vector of Xi_N (coefficient of t), and ell_N the zero-mode trace vector on V2. Its trace contribution is ell_N^T M_N^(-1)b_N times t.

The complete rational matrices, pairings, projections and traces are emitted in `results/primary_three_bracket.json`. The largest Gram matrix is 8 by 8. The separate contributions are

| Weight N | Vacuum basis size | Coefficient of t |
|---|---:|---:|
| 3 | 1 | 98442 |
| 4 | 2 | -1120995 |
| 5 | 2 | 4538070 |
| 6 | 4 | -8975643 |
| 7 | 4 | 9432675 |
| 8 | 7 | -5076594 |
| 9 | 8 | 1104009 |
| **Sum** | | **-36** |

These are not coefficients fit to a known CFT. The reduction (2)–(3) determines the exhaustive finite calculation. The omega-state contributions cancel to zero; the contribution per weight-two primary sums to -36/196883.

For explicit reproduction of every pairing, the initial coefficients are

\[
\langle1,a_{(p)}b_{(q)}c\rangle
=-\binom{p-3}{2}t
\quad(p\ge5,\ p+q=7),
\]

and zero otherwise. Exchanging a and b reverses this coefficient. Positive Virasoro operators act through

\[
[L_m,a_{(p)}]=(2(m+1)-p)a_{(m+p)}.
\]

For the composite in (3) use

\[
(a_{(r)}b)_{(s)}c
=\sum_{k\ge0}(-1)^k\binom rk
\left[a_{(r-k)}b_{(s+k)}c-(-1)^r b_{(r+s-k)}a_{(k)}c\right].
\]

The two parts truncate at k<=5-s and k<=5 respectively. Negative r uses the generalized integer binomial coefficient. All arithmetic is rational. No division by t occurs.

The trace vector ell_N is calculated by acting with vacuum descendant zero modes on omega and on one weight-two Virasoro highest-weight vector, repeating the latter contribution196883 times. The PBW/normal-order algorithm is adapted from pending PR14's helper, with generalized primary weights and a new coefficient convention. An independent oscillator calculation tests its pairings and descendant actions. The 2,3,3 regression reproduces PR14 after converting the first-slot Hermitian convention; no sign is inferred from equal absolute values.

## 5. Recover individual weight-three cubic couplings from the first level

On P2 define the primary cubic multiplication matrices L_e, the contraction F(X)=sum_i L_i X L_i, and

\[
G=F_-+I/3=p\Pi,\qquad p=282,
\quad B:\wedge^2P_2\longrightarrow P_3,\quad B^\dagger B=G.
\]

B is onto and BB^dagger=pI, as in Note13. Use the exterior metric for which e_i wedge e_j has norm one. We identify a wedge b with X=ab^T-ba^T, endowed with half the Frobenius metric. For skew X,Y,

\[
\langle X,Y\rangle_-=-\tfrac12\operatorname{tr}(XY).
\]

The exact mode commutator [a_(1),b_(1)]=B(a,b)_(2) implies that (Bx)_(2) on P2 is represented by the skew matrix Gx. It kills the stress direction in V2. This is the primary cubic contraction including the I/3 stress contribution, not an assumed Monster representation.

Let K_w=pi3 w_(2) pi3. Equation(1), with (a,b,c)=(Bx,Bz,By), gives

\[
-36\langle Bx,K_{Bz}By\rangle
=\operatorname{tr}\big((Gx)(Gz)(Gy)\big).
\]

For skew matrices the right-hand side equals -<Gx,[Gz,Gy]>_-. Therefore

\[
\boxed{B^\dagger K_{Bz}B=\tfrac1{36}G\,\operatorname{ad}_{Gz}\,G.}\tag{4}
\]

This is valid for every z, including ker G. With the isometry J_B=B/sqrt(p) from im Pi onto P3,

\[
\boxed{J_B^\dagger K_{Bz}J_B=\tfrac{p}{36}\Pi\operatorname{ad}_{Gz}\Pi.}\tag{5}
\]

Thus the primary 3,3,3 interaction is fixed, up to the already chosen output basis, once the primary weight-two tensor is specified. It is not an independent new set of freely chosen coupling constants.

An equivalent field-space description is useful. Set M_w=w_(2)|P2 and iota(w)=M_w/sqrt(p); this is an isometric embedding of P3 into the skew matrices. Its image is im Pi, and

\[
\boxed{\iota(\beta(w,v))
=\frac{p^{3/2}}{36}\Pi[\iota(w),\iota(v)].}\tag{6}
\]

The projection is essential. A projected matrix commutator need not obey Jacobi. For example in so(4), project onto the five elementary skew matrices other than E_24-E_42. The projected Jacobiator on the edges12,23,34 is the nonzero edge14. This abstract example is only a guard against an incorrect general inference; it is not a candidate extremal CFT. Requiring Jacobi of a primary-truncated OPE would add an unjustified assumption. Formula(6) does not prove a Lie symmetry or a Monster action.

## 6. The requested uncontracted compatibility equation

The corrected mixed action from the supplied repair/PR14 is

\[
H_a=\pi_3a_{(1)}\pi_3\simeq\frac p{104}\Pi\mathcal D_a\Pi,
\quad\mathcal D_a(Y)=L_aY+YL_a.
\]

Its physical use retains that derivation as a separate dependency. The new coefficient -36 did not require the mixed-action formula or the disputed fifth trace.

Use the normalized descendant identification L_-1/2 from V2 to L_-1(V2). Put b_a(v)=B(a,v), with b_a(omega)=0. The full weight-three action is

\[
E_a=a_{(1)}|V_3=
\begin{pmatrix}(3/2)R_a&(1/2)b_a^\dagger\\(1/2)b_a&H_a\end{pmatrix}.
\]

Consequently the primary block of [E_a,E_b] is

\[
\boxed{K_{B(a,b)}=[H_a,H_b]
+\tfrac14(b_ab_b^\dagger-b_bb_a^\dagger).}\tag{7}
\]

This is the descendant excursion that cannot be discarded when taking a compressed commutator. In exterior coordinates, b_ab_b^dagger-b_bb_a^dagger=p Pi ad_(a wedge b) Pi. Combining (5) and (7) produces a completely explicit equation in the original cubic.

For x=sum_(a<b) x_ab e_a wedge e_b, define

\[
\mathcal Q_x=\sum_{a<b}x_{ab}
(\mathcal D_aG\mathcal D_b-\mathcal D_bG\mathcal D_a).
\]

Then every admissible candidate satisfies

\[
\boxed{\Pi\left(9\mathcal Q_x+24336\operatorname{ad}_x
-2704\operatorname{ad}_{Gx}\right)\Pi=0\quad\text{for all }x.}\tag{8}
\]

Replacing both external Pi by G gives an equivalent polynomial identity, with no division or rank choice. For x in ker G it reduces to the requested zero-state factorization test. For general x it fixes the nonzero-state action as well. Coefficients in (8) follow from p=282, the mixed normalization104, and the newly derived36; they are checked separately.

This is a necessary uncontracted condition involving six independent weight-two labels, not merely a trace after summing output states. However, the attempted reduction to existing lower cubic contraction identities was not completed. No exact countermodel meeting the full physical antecedent system was found or claimed. It remains **UNRESOLVED whether (8) is an independent restriction or a consequence of that system**. The new universal VOA derivation proves necessity, not polynomial independence.

A meaningful next step is an algebraic certificate for (8) from the precise earlier joint identities, or an exact countermodel satisfying all of them and the corrected lower formulas. Small cubics that only match some traces do not establish independence. Continuing to compute scalar moments without deciding this implication would not answer the selection question.

## 7. Independent controls, limits and source depth

The checker has **52 exact checks** and emits the entire rational certificate, not only -36. Independent c3 even-Heisenberg calculations verify70 composite pairings,154 Virasoro Gram entries,56 descendant zero-mode actions,54 star-identity inputs on the full quadratic space, and27 compressed-commutator inputs. A nonzero descendant excursion provides a negative control for discarding that term. The private oscillator cutoff is14; the largest composite weight is9 and largest square matrix8x8. These small examples are not holomorphic c24 theories.

There is also a known-example check inside the moonshine theory. For a skew matrix A on three oscillator directions, w_A=(1/2)sum A_ij h_i(-2)h_j(-1)1 has norm from half the Frobenius metric. Direct modes give

\[
\langle w_A,(w_B)_{(2)}w_C\rangle=-\tfrac52\operatorname{tr}(ABC).
\]

In the complete weight-two representation the oscillator symmetric-square block contributes26 tr(ABC), the diagonal Leech block contributes zero, and the twisted block contributes64 tr(ABC). Thus the full trace is90 tr(ABC), agreeing with -36 times the direct coefficient. The Sym^2 index n+2 follows by expanding tensor factors and inserting (I+swap)/2; the twisted contribution is4096/4^3. These use the inherited explicit block conventions [S]. They are a consistency witness, not the proof of the universal coefficient. No 196884-dimensional matrix is built.

The distinction between (1), the physical compressed action, and the unresolved algebraic implication (8) is maintained throughout. No independent specialist review, formal verification, full OPE reconstruction, comprehensive priority clearance, physical implementation, or moonshine uniqueness is claimed.

All previously recorded main files and unmerged branches are preserved. Runtime network Git access failed; new local checks are not described as a current-main historical replay. The additive PR has its own manifest and read-only workflow. Actual strict and bounded-portability outcomes must be read separately; the previous reporting erratum remains in force. No manuscript, release or outreach is performed.

### Primary sources and inspected passages

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1, Theorem3.1 and the end-of-section2 trace-rule discussion. The relevant parsed statements were read; printed page12 was visually inspected. The theorem supplies trace reduction to vacuum data, not a Monster-action assumption. https://arxiv.org/abs/math/0701626

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1, Definition2.2, the Heisenberg construction and the moonshine unitarity discussion. Printed page3 was visually inspected. We retain the odd-primary adjoint sign rather than extrapolating an even-weight rule. https://arxiv.org/abs/1308.2361

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1, section1 iterate/Virasoro and vacuum conventions. These were reread in parsed text; the disputed fifth-order numerical coefficient is not a premise. https://arxiv.org/abs/math/0007169

[S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, sections7.4 and10.1. The block decomposition and source product conventions support the separate known-example control. The full source-to-VOA scale is inherited from the explicit normalization audit; it is not newly proved by the8x8 certificate. https://arxiv.org/abs/2002.10921

Pending PR14, head e608dec00a26c714a68ec33b9463faadacdce573, provides the previous2,3,3 reconstruction and the PBW algorithm adapted here. PR15/Note17 supplies the preceding response-closure result. Reading them and reproducing the supplied Note17 package is not a comprehensive audit or merger of those branches. No downloaded papers or fonts are bundled.
