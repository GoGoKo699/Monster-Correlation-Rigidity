# Ising partner search: a strict tricritical local maximum

**Date:** 26 September 2026. **Baseline:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Proposed additive branch:** `research/ising-partner-landscape`.

## 1. The question tested, and the result

The previous selection bridge uses the prior Abe–Lam–Yamada theorem: an exact simple rational C2-cofinite holomorphic CFT-type VOA with c=24 and V1=0 is moonshine if it contains two orthogonal Ising vectors. The owner asks whether the Monster is singled out by physics, not just whether a chosen tensor has Monster symmetry. This continuation tests the smaller missing implication: after locating one Ising component, can a second be forced in its commuting sector?

We obtain a precise conditional search space and a necessary caution about optimization:

* Given a real Ising vector e, its commutant has central charge 47/2 and a 96255-dimensional weight-two primary space. The inherited conformal-design guarantee is seven, not eleven.
* A real unit primary in that commutant with self-three-point coefficient greater than 13/4 already guarantees an orthogonal Ising partner, hence the full moonshine identification under the ambient hypotheses. No near-saturation tolerance or independently tuned pair overlap is needed once e and the exact commutant are given.
* However, even in the **known moonshine theory itself**, the partner-search cubic has strict local maxima corresponding to tricritical Ising charge 7/10, rather than Ising charge 1/2. They have a whole-neighborhood loss bound, not merely a Hessian observation. The same Virasoro sector gives an unconstrained saddle and, after centering with the remaining stress tensor, a constrained strict maximum.

This rules out the particular shortcut “run local ascent in the commutant and regard its stopping point as a partner.” It does not rule out a global argument, multistart methods, or a different structural existence proof. No algorithm for constructing either Ising vector is supplied, and **one-Ising existence has not been proved to force the pair**.

The tricritical subalgebra, its sigma-type representation content and its known commutant spectrum are established in Höhn–Lam–Yamauchi [HLY]. The explicit cubic-landscape interpretation and finite-radius estimate below are source-based corollaries, not a new discovery of those subalgebras or a new classification theorem. The exact moment calculation reproduces the prior spectrum without using group character data.

## 2. The exact commutant is a smaller partner arena

Let V be simple unitary rational C2-cofinite holomorphic of CFT type, c=24, V1=0, with the PCT-real positive form used in the project. Suppose an exact real Ising vector e is already known. Set

W = Com_V(Vir(e)),   eta = omega-e,   C = c_W = 47/2.

W inherits a positive real form, CFT-type integer grading and W1=0. Nothing here identifies an arbitrary W with the known Baby Monster algebra, assumes W holomorphic, or claims the full theory splits as a tensor product. W is the algebra of fields commuting with the selected Virasoro sector.

The Ising irreducible lowest weights are 0, 1/16, 1/2. On V2, there are no level-one descendants because V1=0; the single vacuum descendant e has e-zero-mode eigenvalue 2. Thus R_e=e_(1) has eigenvalues among 0,1/16,1/2,2. The first three trace identities, valid by the conformal-design replacement in [H], fix their multiplicities to

| Eigenvalue of R_e on V2 | Multiplicity |
|---|---:|
| 0 | 96256 |
| 1/16 | 96256 |
| 1/2 | 4371 |
| 2 | 1 |

This is also the familiar known-moonshine spectrum, but it is not inferred from an assumed Monster representation. The checker reconstructs it from a 4x4 moment system.

The zero eigenspace is exactly W2. For a vector in it, positive e-modes vanish by the unitary module decomposition, including e_(0) by the null level-one descendant of the vacuum module. An explicit orthogonal projector on V2 is

Q_0 = (I-16R_e)(I-2R_e)(I-R_e/2).

The primary partner space is

P_W = W2 intersect eta-perp,   dim P_W = 96255,

with projector

Q_P = Q_0 - (4/47)|eta><eta|,

since ||eta||^2=47/4. These are exact algebraic formulas; evaluating them on an unknown large algebra or implementing them experimentally has not been made efficient.

### What symmetry-free thermal information transfers

As a module for the rational Ising algebra, V decomposes into three isotypical pieces tensored with their multiplicity spaces. Höhn's derived-design theorem [H, Theorem 2.10] has the formula

t_derived = t+2-2s,

where s counts the distinct Virasoro lowest weights. With t=11 and s=3 it yields a conformal 7-design on each corresponding commutant energy space. It does **not** license reusing the whole eleven-design inside W.

The degree-two commutant traces, with d_W=96256 and C=47/2, are therefore supplied by the general formulas of [M] through order three. In particular

Tr_W2 R_a = 16384<a,eta>,

Tr_W2 R_a R_b = 2406<a,b> + 2584<a,eta><b,eta>,

Tr_W2 R_a R_b R_c = 479<a*b,c>
+ 328 Cyc(<a,b><c,eta>) + 384<a,eta><b,eta><c,eta>.

Here * is the full W2 product, not its primary projection. These numerical substitutions are checked exactly. This derivation does not require a fifth trace, the disputed alternating-form normalization, or a commutant character classification.

## 3. A coarse global witness suffices once the first Ising vector is given

For real unit x in P_W define f_W(x)=<x_(1)x,x>. Write mu_W for the primary-projected multiplication in W. At a sphere critical point,

mu_W(x,x)=lambda x,   lambda=f_W(x).

The corresponding Virasoro vector of charge r has the form

nu = (r/C)eta + Bx,

B^2 = r(C-r)/(2C),   B lambda = 2-4r/C.

Thus

lambda_C(r) = (2-4r/C)/sqrt(r(C-r)/(2C)),

lambda_C'(r) = -1/[2(r(C-r)/(2C))^(3/2)] < 0.

The ambient stress tensor must be eta of charge47/2, not the original omega of charge24. Confusing these normalizations changes the numerical cubic value.

The positive-energy unitary Virasoro classification has smallest positive charge1/2 and next charge7/10. The cyclic vacuum module of any nonzero real Virasoro vector here is positive energy: on its vacuum descendants its Virasoro energy equals the ambient degree. Hence the same group-independent argument as the previous bridge gives

max f_W <= M_W = sqrt(16200/1081).

If W contains no Ising vector, its global maximum is a non-Ising critical point, and therefore

max f_W <= Lambda_W = sqrt(195364/18753).

Numerically these are approximately3.87119 and3.22765. Consequently

f_W(x) > Lambda_W  ==>  W contains an Ising vector.

A convenient strictly stronger sufficient condition is f_W(x)>13/4. The resulting Ising vector is orthogonal to e because it lies in W. Applying [ALY, Theorem A.1] to the original V identifies V with V-natural.

This is a **conditional global witness**, not a proof that such an x exists and not a certificate that the supplied x itself is Ising. The maximizer can be elsewhere in W. The two possibilities max f_W=M_W and max f_W<=Lambda_W are uniformly separated, but only a proved lower bound above Lambda_W would force the desired branch. The exact classification credit remains with [ALY].

## 4. A genuine obstruction inside the target theory

The known moonshine theory contains the 2A dihedral algebra [HLY]. Its weight-two algebra is spanned by three Ising vectors e,f,g with

e*e=2e, f*f=2f, g*g=2g,

e*f=(e+f-g)/4,

and the cyclic versions of the last formula. Their squared norms are1/4 and their pairwise inner products are1/32. These data come from an actual embedded unitary VOA, not a proposed stand-alone cubic.

Its conformal vector is

Omega=(4/5)(e+f+g),   c_Omega=6/5.

Set

nu=Omega-e = -(1/5)e+(4/5)(f+g).

Then nu*nu=2nu, e*nu=0, and ||nu||^2=7/20. Thus nu is a tricritical Ising vector of charge7/10 in W. It is not an Ising partner, despite commuting with the first Ising field.

A key prior theorem is [HLY, Lemma3.6]: such a **derived** charge7/10 vector is of sigma type in W. This says that the irreducible Vir(nu) modules appearing in W have lowest weights only

0, 1/10, 3/5, 3/2.

The weights3/80 and7/16 from the full tricritical Kac table are absent. That is a representation-theoretic consequence of the embedded 2A extension, not something we assume for every charge7/10 field. The source proves it by decomposing the rational 2A algebra, and not by importing a character table for the Monster.

The known embedding and transitivity of Ising vectors also ensure that such derived fields exist for any choice of e in the known theory [HLY, proof of Theorem5.9]. These existence and transitivity statements are NOT transferred to an arbitrary unknown candidate.

## 5. Four moments determine every constrained curvature direction

On W2, a sigma-type nu of charge r=7/10 has possible eigenvalues 0,1/10,3/5,3/2 and the single vacuum-descendant eigenvalue2. All level-one descendants would start from W1 and are absent. The 7-design trace formulas give

Tr R_nu = 8192r,

Tr R_nu^2 = 1203r+646r^2,

Tr R_nu^3 = 479r+246r^2+48r^3.

Remove the known nu eigenvector of eigenvalue2. The remaining four multiplicities solve

[ [1,1,1,1],
  [0,1/10,3/5,3/2],
  [0,1/100,9/25,9/4],
  [0,1/1000,27/125,27/8] ] m
= [96255,28662/5,28866/25,58038/125]^T.

The determinant is567/10000, so the solution is unique:

| Eigenvalue | Multiplicity on W2 |
|---|---:|
| 0 | 48621 |
| 1/10 | 45696 |
| 3/5 | 1938 |
| 3/2 | 0 |
| 2 | 1 |

This reproduces [HLY, proof of Theorem5.13]. It is not a new spectral discovery. In particular the missing3/2 eigenspace is **derived**, not excluded in advance to manufacture a local maximum.

Center and normalize nu relative to eta:

x_0 = [nu-(r/C)eta]/B,

B^2=399/1175,   f_W(x_0)=Lambda_W=sqrt(195364/18753).

On the tangent space to the real unit sphere in P_W, the spherical Hessian is

Hess f_W = (6/B)(R_nu-I).

Removing the eta/nu plane removes the eigenvalue2 and one zero eigenvector. Thus the complete tangent Hessian has values

-6/B, -27/(5B), -12/(5B)

with multiplicities48620,45696,1938, respectively. There are96254 negative directions and no zero or positive direction. This is a strict local maximum in the entire constrained primary space, not merely in the tiny 2A span.

### A finite neighborhood, not just infinitesimal curvature

Let y be real unit with s=||y-x_0||<=1/10. Write y=q x_0+t v, with q=1-s^2/2, t=sqrt(1-q^2), v unit and tangent. Cubic expansion and criticality give

f_W(y)=Lambda_W q^3+3qt^2 C_W(x_0,v,v)+t^3 f_W(v).

The largest tangent eigenvalue of the primary multiplication is (3/5-2r/C)/B. The global cubic bound is |f_W(v)|<=M_W<4 and Lambda_W<4. Using q>0 and the standard chord inequalities yields

Lambda_W-f_W(y)
>= s^2[6/(5B) -(3/4)Lambda_W s^2-M_W s].

Since B^2=399/1175<9/25, the first term exceeds2. The bracket exceeds2-3/100-4/10=157/100>3/2. Therefore

**Lambda_W-f_W(y) >= (3/2)||y-x_0||^2 for ||y-x_0||<=1/10.**

Any continuous path from this point to a higher-scoring Ising maximum must first drop by at least3/200 on crossing the radius1/10 boundary. This excludes a guaranteed continuous monotone-ascent escape. It is not a no-go for a global search, a finite jump, restarts, or another algebraic argument.

The known commutant also contains an orthogonal Ising partner: the explicit norm-four lattice plus/minus pair in [LS] provides one, and known Ising conjugacy moves its first member to any chosen e. Thus this is an actual suboptimal local maximum, not a local maximum in a theory lacking the desired higher value.

## 6. Why fixing one component creates the obstruction

The same tricritical nu is not a maximum of the original unconstrained cubic in V2. The explicit vector

v=f-g

has positive norm7/16 and obeys

R_e v=(1/2)v,   R_nu v=(3/2)v.

It is perpendicular to omega and nu. For the ambient normalized critical direction, the Hessian along it is positive, proportional to6(3/2-1). There are also negative directions. For example with z=omega-Omega, the vector e-(5/228)z is perpendicular to omega and nu and has R_nu eigenvalue zero. Thus the unconstrained point is a saddle.

The two centered primary vectors are different: the ambient one subtracts (r/24)omega, while the commutant one subtracts (r/C)eta. One must not call them the same stationary point. There is also an exact escape curve through the actual constrained point x_0 itself. The vector v is perpendicular to x_0 and omega, but has e-energy1/2 and is not in the commutant. With v normalized, the original ambient cubic along cos(theta)x_0+sin(theta)v has zero first derivative and positive second derivative

3(1+r/C)/B > 0

at theta=0. This follows because eta_(1)v=(3/2)v. The exact four-coordinate control checks both derivatives. Thus the compatibility constraint really removes an uphill direction through the constrained point. The commutant spectrum shows that all remaining tangent directions are downhill. This conclusion does not rely on conflating the two stress-tensor normalizations.

This is a statement about the objective built from three-point coefficients. It is not a thermal metastable phase, a Hamiltonian energy barrier, an RG fixed-point stability theorem, or a new claim that tricritical Ising dynamics produces the Monster. The appearance of Ising, tricritical Ising and the Baby Monster commutant is established mathematical physics; the present point is what it means for this proposed selection argument.

## 7. Why a single-Ising character argument cannot replace the missing proof

An expected spectrum for the commutant does not identify its multiplication. Höhn–Möller [HM, Remark8.4] explicitly retain possible 'fake' shorter-moonshine objects and explain their relation to a hypothetical non-moonshine c24 current-free VOA with an Ising involution. The classification result does not automatically remove this case.

This is a source-depth warning, not evidence that another theory exists, and not a reason to abandon an existence proof. It prevents a circular argument in which one names the unknown commutant 'the Baby Monster VOA,' borrows its known Ising partner, and concludes the parent was moonshine.

Similarly, the local maximum above does not refute the implication 'one Ising forces a second.' It refutes one proposed method for proving it: that any local maximum of the constrained cubic is the required Ising component. The example is inside the desired theory, where the pair exists.

The remaining global target is exact:

Given e, show max_{unit x in P_W} f_W(x) > Lambda_W,

or supply a different structural route to a commuting Ising field. The simpler sufficient threshold13/4 may be convenient for a lower-bound certificate. No such lower bound has been proved from the bare assumptions in this pass. Nor has the first Ising field itself been forced. These are still the genuine selection obligations.

No new scalar constraint is added merely because it is computable. The low-order moment equations are fully compatible with the wrong local summit; additional global structure, rather than another local Hessian check, is needed.

## 8. Evidence, scope and prior work

The checker has72 exact rational checks. It reconstructs both4x4 moment systems from the general first-three-trace formulas, checks all entries of the small2A product with its positive metric, the centered critical equations, the explicit allowed/forbidden escape directions, Kac-table values, Hessian multiplicities and finite-radius inequalities. Its largest matrix and coefficient vector are4-dimensional. No Monster character table, full Griess tensor or huge operator is constructed.

The continuum local-basin proof is the analytic cubic estimate above. Imported VOA existence, representation, conformal-design and classification theorems are not proved by the finite checks. The code uses no fifth trace, no alternate five-form convention, no formal proof assistant and no stochastic numerical search. Diagnostic floating-point feasibility explorations were not used as proof and are not bundled.

The prior two-field checkpoint was extracted byte-for-byte, all14 hashes verified and all68 checks reproduced under normal/-O/-OO. The new72-check report is also reproduced in all three modes. Main and the pending branches remain unchanged unless an explicitly documented additive PR is created. Actual remote verification is recorded separately, with strict replay distinguished from unchanged bounded portability. No old evidence/tolerance is modified.

This is a scoped source-based derivation and falsification of a shortcut. [HLY] already proves the derived tricritical structure and its spectrum. The exact curvature, basin estimate and coarse partner-search formulation may be implicit in that literature; no exhaustive priority or independent specialist review is claimed. No manuscript, release, outreach, practical experiment or full moonshine uniqueness theorem is supplied.

### Primary sources and inspected scope

[ALY] T. Abe, C. H. Lam, H. Yamada, *A remark on Z_p-orbifold constructions of the Moonshine vertex operator algebra*, arXiv:1705.09022v4, Theorem A.1 and the Appendix hypotheses. The statement was rechecked; printed page10 was visually inspected. The previous checkpoint records the fuller Appendix read. No new proof of its orbifold/extension classification is claimed.
https://arxiv.org/abs/1705.09022

[H] G. Höhn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. Theorem2.10 and its finite Virasoro decomposition, Example2.11, and the trace-assumption replacement before Section3. Printed page9 was visually inspected. The design theorem is the noncircular reason for the commutant's seven-design, not an assumed Baby Monster action.
https://arxiv.org/abs/math/0701626

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1, Theorem2.1(1)-(3). The formulas and hypotheses were read; the previous c24 trace page was visually inspected. The general formulas are used with the explicit design replacement. No fifth-order formula is used.
https://arxiv.org/abs/math/0007169

[HLY] G. Höhn, C. H. Lam, H. Yamauchi, *McKay's E7 observation on the Baby Monster*, arXiv:1002.1777v2. The v2 PDF also contains the E6 sequel; all references here are to the FIRST paper. Section3.1, equations(3.3)-(3.4), Lemma3.1, Definition3.5, Lemma3.6 and its module-decomposition proof, Lemma5.3, the embedding argument in Theorem5.9 and the moment calculation in Theorem5.13 were read. Screenshot requests for PDF pages11,15,31,34 failed, so no visual inspection of those pages is claimed. The printed numerical spectrum is reproduced independently by the included rational moment system. The full dihedral/commutant/automorphism classification was not audited.
https://arxiv.org/abs/1002.1777

[HM] G. Höhn, S. Möller, *Classification of Self-Dual Vertex Operator Superalgebras of Central Charge at Most 24*, arXiv:2303.17190, Theorem8.3 and Remark8.4, printed54–55. The explicit unresolved shorter-moonshine case and character-versus-reconstruction distinction were read. This supplies a limit of the cited classification, not a proof that no later theorem could exist; targeted searches did not supply a stronger single-Ising uniqueness theorem.
https://arxiv.org/abs/2303.17190

[LS] C. H. Lam, H. Shimakura, *Ising vectors in the vertex operator algebra V_Leech^+ associated with the Leech lattice*, arXiv:0810.5395, explicit norm-four-lattice Ising pair. The prior checkpoint's construction was reread; inclusion in the known moonshine theory and Ising conjugacy are used only for the known-example attainment statement.
https://arxiv.org/abs/0810.5395

The positive-energy Virasoro classification and PCT conventions are the same imported interfaces as in the preceding checkpoint (Friedan–Qiu–Shenker as explicitly stated by Wassermann, arXiv:1012.6003, and Dong–Lin, arXiv:1308.2361). Their full proofs were not rederived. No downloaded papers or font files are bundled.
