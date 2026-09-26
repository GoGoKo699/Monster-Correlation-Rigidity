# The Potts alternative is a real local maximum inside moonshine

**Date:** 26 September 2026. **Read baseline:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Additive branch:** `research/potts-local-maximum`.

## 1. What this continuation establishes

The charge-4/5 spectral list in the preceding local checkpoint is not merely feasible moment data. It is realized by an extended three-state-Potts Virasoro component inside the actual moonshine VOA. Its centered unit primary is a strict local maximum of the SAME ambient cubic objective on the full 196883-dimensional first primary space. It is nevertheless below the Ising global maximum.

This is a genuine obstruction to replacing the Ising-existence problem by local ascent or by excluding all nonsaturating local maxima. It is not a counterexample to the preceding large-correlation sufficient condition, and not a proof that a hypothetical different holomorphic theory exists. The known Potts embedding and its spectrum are prior mathematics. The present work extracts the full-space Hessian, a uniform local loss barrier, and an exact finite path to an Ising direction from that structure.

The main quantitative statements are:

- At the Potts-centered unit primary a, f(a)=28/sqrt(87), and every tangent Hessian eigenvalue is strictly negative.
- Whenever ||x-a||<=1/8, f(a)-f(x)>=||x-a||^2. Any continuous route to a higher value therefore crosses a loss of at least 1/64.
- A known four-dimensional interaction subalgebra, with the complementary stress direction added, contains an explicitly verified path which first descends and then reaches the Ising value 46/sqrt(141).

The barrier concerns an optimization over normalized field directions. It is not a thermodynamic free-energy barrier, an RG metastability theorem, or a complexity lower bound for global algorithms. The explicit path uses specified interaction fields already present in the known example; it is not an algorithm that finds them in an arbitrary candidate.

The remaining physical-selection question is unchanged: do the original holomorphic/current-free assumptions force an Ising component, and an orthogonal partner? Neither is proved here. What is now ruled out is the proposed shortcut that consistent mixed interactions must eliminate the charge-4/5 LOCAL maximum.

## 2. Assumptions, source update, and the extension distinction

Retain the class used in the preceding selection notes: a simple, unitary, rational, C2-cofinite, holomorphic VOA of CFT type, central charge 24, and V1=0. Use the PCT-fixed real form and its positive invariant metric. This is a restricted exact class, not a universal physical law or a statement about approximate VOA axioms.

Write B=V2, P2=omega-perp in V2, and use a*b=a_(1)b. Then

||omega||^2=12, omega*a=2a,

a*b=mu(a,b)+<a,b>omega/6 for a,b in P2.

The objective is f(x)=<x*x,x> on the real unit sphere in P2. The earlier unitarity argument gives |f(x)|<=M=46/sqrt(141). No assertion that this bound is saturated in every candidate is used.

A bare charge-4/5 Virasoro vector u generates L(4/5,0). It is called **extendable** if the ambient theory contains the extension

W(4/5)=L(4/5,0) plus L(4/5,3)

with the additional weight-three field and its consistent products. Extendability is extra structure, not automatic from u*u=2u and ||u||^2=2/5. Lam–Yamauchi [LY, Definition 2.3 and Theorem 2.5] explicitly distinguish these possibilities.

Matsuo's earlier arXiv version [M, section 4.1] listed the extended Potts spectrum but stated in a footnote that an embedding into moonshine was not then known to the author. That limitation should not be carried forward as a claim of current nonexistence. The later work of Höhn–Lam–Yamauchi [HLY], second paper, equation (4.1), Lemma 4.2 and Theorem 5.1, records and proves the needed actual moonshine structure. The earlier Potts/moonshine construction of Kitazume–Lam–Yamada [KLY] is also relevant prior work; its full text was not obtained here.

Thus the real-existence input is a primary-source theorem, not a tensor inferred from matching dimensions. The small calculation below does not itself construct the full moonshine VOA or reprove its embedding theorem.

## 3. Extendability gives the complete low-energy spectrum

The rational extension W(4/5) has six irreducible modules [LY, Theorem 2.5]. As Virasoro modules their types are

L(4/5,0) plus L(4/5,3),
L(4/5,2/5) plus L(4/5,7/5),
L(4/5,2/3) with two extension labels,
L(4/5,1/15) with two extension labels.

For the degree-preserving action R_u=u_(1) on ambient V2, V1=0 excludes an occurrence of the 7/5 component: it is one internal level above the bottom 2/5 component of the same W-module and would require that bottom at ambient weight one. The spin-three extension state is not in V2. The only eigenvalue-2 direction is u itself. The remaining possible eigenvalues are therefore

0, 1/15, 2/5, 2/3.

This is the representation-theoretic input, not a claim about a general bare L(4/5,0) embedding. The same exclusion is discussed by [LY, Lemma 2.10 and Remark 3.1].

The first repeated trace formulas, whose hypotheses are supplied by the established extremal design-to-trace argument, are

p0(r)=196884,
p1(r)=16407r,
p2(r)=r(1271r+2310),
p3(r)=3r(31r^2+155r+300),
p4(r)=r(13r^3+120r^2+534r+864)/2,
p5(r)=r(7r^4+100r^3+740r^2+2720r+3840)/16.

For r=4/5 subtract the one eigenvalue-2 direction. A nonsingular four-by-four Vandermonde system using p0 through p3 determines the four multiplicities; p4 and p5 provide separate exact checks:

| Eigenvalue of R_u | Multiplicity in V2 |
|---:|---:|
| 0 | 57478 |
| 1/15 | 129168 |
| 2/5 | 8671 |
| 2/3 | 1566 |
| 2 | 1 |

This agrees with the known moonshine decomposition in [HLY, equation (5.2)]. No Monster character table is used in the reconstruction. The repeated fifth trace contains no alternating-five-form contribution, so the earlier disputed mixed normalization is irrelevant here.

## 4. This is a strict local maximum in the full primary space

For a proper real Virasoro vector e of charge r, put

b_r=sqrt(r(24-r)/48),
a_e=(e-r omega/24)/b_r.

Then a_e is a unit primary critical point with

f(a_e)=(2-r/6)/b_r.

On the real tangent space perpendicular to omega and e, direct differentiation gives

Hess f=(6/b_r)(R_e-I).

At the extendable Potts component,

r=4/5, b_r^2=29/75, b_r=sqrt(87)/15, f(a_e)=28/sqrt(87).

Removing u and the one zero-eigenvector proportional to omega-u gives the following COMPLETE tangent Hessian:

| Hessian eigenvalue | Multiplicity |
|---:|---:|
| -6/b_r | 57477 |
| -28/(5b_r) | 129168 |
| -18/(5b_r) | 8671 |
| -2/b_r | 1566 |

All 196882 directions decrease to second order. Hence the normalized Potts field is a nondegenerate strict local maximum of the ambient f, not just a maximum within its tiny generating algebra or a commutant.

This is different from the charge-7/10 component in the preceding local checkpoint: its ambient spectrum has a compulsory 3/2 tangent eigenvalue and is a saddle. It is also different from pending PR24, which studies a charge-7/10 maximum after restricting to the commutant of an already supplied Ising vector. The spaces, centerings, and charges in those statements must not be conflated.

### An explicit radius and exit loss

Let a=a_e, s=||x-a||<=1/8, q=1-s^2/2, and x=qa+t v with v perpendicular to a, ||v||=1, t=sqrt(1-q^2). Symmetry of the cubic gives

f(x)=q^3 f(a)+3qt^2 C(a,v,v)+t^3 f(v).

The largest tangent multiplication value is

C(a,v,v)<=((2/3)-(1/15))/b_r=3/(5b_r).

Using |f(v)|<=M, q t^2<=s^2, t<=s and 1-q^3>=3s^2/2-3s^4/4 yields

f(a)-f(x)>=s^2[1/b_r-(3f(a)/4)s^2-Ms].

The exact inequalities 1/b_r>8/5, f(a)<31/10 and M<4 give, throughout the chosen ball,

1/b_r-(3f(a)/4)s^2-Ms
>8/5-(93/40)(1/8)^2-4/8
=2723/2560>1.

Thus f(a)-f(x)>=s^2. Any continuous path from a to a point with strictly larger f must leave this ball, and at its first radius-1/8 crossing has lost at least 1/64. This is a sufficient lower bound, not the optimal escape barrier in the full sphere.

## 5. A small actual interaction algebra contains both the local and global peaks

The known moonshine 3A subalgebra has a four-dimensional weight-two part [HLY, Lemma 4.2]. In its complex basis it has orthogonal stress vectors u,v of charges 4/5 and 6/7, plus conjugate fields X+ and X-. Take the positive real basis

Y=X++X-, Z=i(X+-X-),

and add the complementary ambient stress vector w=omega-u-v. This is a five-dimensional real algebra, with diagonal metric

< u,u >=2/5, < v,v >=3/7, < Y,Y >=< Z,Z >=162, < w,w >=391/35.

The internal 3A central charge is 58/35; w has charge 782/35. The ambient stress is omega=u+v+w and still has norm twelve. All nonzero products are

u*u=2u, v*v=2v, w*w=2w,
u*Y=(2/3)Y, u*Z=(2/3)Z,
v*Y=(4/3)Y, v*Z=(4/3)Z,
Y*Y=270u+504v+20Y,
Z*Z=270u+504v-20Y,
Y*Z=-20Z.

The cross products u*v and all products of w with the other four basis vectors vanish. All 125 invariant-metric identities and the five multiplication matrices are checked exactly. The product table and its embedding are PRIOR WORK converted to a positive real basis, not a newly discovered exceptional algebra.

An explicit Ising vector is

e=(5/32)u+(7/16)v+(1/32)Y.

Directly, e*e=2e and ||e||^2=1/4. This is [HLY, equation (4.2)], not a new existence theorem. Therefore the same actual theory has the Potts local maximum and the higher Ising value M.

There is a useful algebraic form of this construction:

e=(1/1152)(Y*Y)+(1/72)Y-(5/64)u.

The Ising direction can be recovered by one explicitly known mixed square rather than climbing the self-cubic. This is a computation INSIDE THE SUPPLIED 3A ALGEBRA. It does not assert that every arbitrary charge-4/5 vector has an available field Y with this product relation. Proving such an embedding or mixed relation from the original assumptions would be additional work.

### Charge alone does not determine the local geometry

The same five-coordinate calculation contains another charge-4/5 Virasoro vector

x=(1/16)u+(7/8)v-(1/48)Y.

It satisfies x*x=2x and ||x||^2=2/5, but

x*Z=(13/8)Z, <Z,x>=<Z,omega>=0.

Its centered primary therefore has an increasing tangent direction, despite having the SAME self-cubic value as the Potts maximum. It is not extendable; [HLY, Lemma 4.3] gives the corresponding representation obstruction. The model-specific comparison prevents transferring the local-maximum conclusion from an extended Potts component to every bare charge-4/5 vector.

## 6. An exact descending-then-ascending route

The barrier is not an absence of a route to larger couplings. In the actual algebra above set

A=u-omega/30, B=e-omega/48,
z(t)=(A+t B)/sqrt(D(t)), t>=0.

The needed inner products are

||A||^2=29/75, ||B||^2=47/192, <A,B>=13/240.

The complete objective along this curve is f(z(t))=N(t)/D(t)^(3/2), with

D(t)=(1175t^2+520t+1856)/4800,
N(t)=(135125t^3+89700t^2+87360t+207872)/288000.

Its derivative has the sign of

2N'(t)D(t)-3N(t)D'(t)=3t(3521t-2608)/12800.

Thus it decreases from the Potts point until t*=2608/3521 and then increases all the way toward the Ising point. At the single interior minimum,

f(z(t*))^2=505485828592144/64205847970317,

or f approximately 2.80587. The starting value is approximately 3.00192. Already at t=2 the value is larger than 28/sqrt(87); the limit t->infinity is M=46/sqrt(141).

This is an exact curve in the full normalized primary sphere, using the complementary stress direction when centering. The minimum along the curve is not claimed to be a critical point of the full sphere, nor is the curve claimed to minimize the escape barrier. Its construction uses the specified Ising endpoint, so it is not an unsupervised search algorithm.

The small 3A algebra contains three Ising vectors with nonzero mutual overlaps, not an orthogonal Ising pair. The displayed formula does not by itself meet the two-orthogonal-vector premise of the Abe–Lam–Yamada classification theorem. The known ambient moonshine theory has other orthogonal pairs; their existence is not newly derived from this local calculation.

## 7. The local-maximality spectral relaxation has exactly three rows at charge 4/5

This calculation records what remains open rather than interpreting one known example as an exhaustive classification of possible maxima.

For a bare unitary charge-4/5 Virasoro vector, the Kac weights are

0, 1/40, 1/15, 1/8, 2/5, 21/40, 2/3, 7/5, 13/8, 3.

Ambient positivity and the local-maximum Hessian exclude eigenvalues greater than one, apart from the vector's own eigenvalue two. The seven possible remaining weights are the first seven entries. Using all six moments p0 through p5 gives a rank-six Vandermonde system with one free parameter q=1566-n_(2/3). Its complete affine solution is

n(q)=(57478,0,129168,0,8671,0,1566)
+q(-4862/27,56576/135,-1768/5,1088/9,-1547/135,832/135,-1).

Since n_(1/40)>=0 and q is integral, q>=0; gcd(56576,135)=1 forces 135 to divide q. Nonnegativity of n_0 gives q<=775953/2431, strictly between 270 and 405. Only q=0,135,270 remain, and all three rows are nonnegative integers:

| q | n0 | n1/40 | n1/15 | n1/8 | n2/5 | n21/40 | n2/3 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 57478 | 0 | 129168 | 0 | 8671 | 0 | 1566 |
| 135 | 33168 | 56576 | 81432 | 16320 | 7124 | 832 | 1431 |
| 270 | 8858 | 113152 | 33696 | 32640 | 5577 | 1664 | 1296 |

Only the q=0 row is supplied here with an actual VOA realization. The other rows are complete solutions to this necessary spectral relaxation, not demonstrated multiplication algebras, actual CFTs, or possible global maxima. Additional fusion, mixed products, and commutant consistency remain untested for them. This finite enumeration does not replace those obligations.

## 8. Consequence for the research plan

The attempted exclusion of the charge-4/5 case cannot succeed if it means excluding its existence or its local maximality: both occur inside the target theory. A potential argument excluding it as the GLOBAL maximum of an arbitrary candidate would need additional nonlocal interaction information, as the known 3A example demonstrates.

The next justified target is therefore to understand when the large eigenspaces of a putative maximizing component force a small mixed-product closure containing a higher-coupling direction, or otherwise force an Ising vector. The identity recovering e from u and Y shows what such a constructive mechanism looks like, but no theorem is supplied that makes Y available in every candidate. One must not impose a 3A table or assume a Monster element to manufacture the conclusion.

This result does not refute the preceding conditional threshold: a value strictly greater than 28/sqrt(87) still forces some Ising component. It shows the threshold's boundary is populated by an actual nonsaturated local peak. It also does not establish that a single Ising component forces an orthogonal partner.

The known structure is an example within a theory that already possesses the Monster symmetry. It is not evidence that another holomorphic candidate exists, and it does not settle uniqueness. This is a bounded landscape and source audit, not an additional postulated physical selection principle.

## 9. Exact evidence and preserved records

The new checker has 80 labelled integer/fraction checks, with identical output under normal Python, -O and -OO. It emits the multiplicity systems, tangent spectrum, barrier bounds, exhaustive one-parameter spectral relaxation, the complete five-coordinate real product table, and the exact curve coefficients. The largest square matrix actually formed is 5x5. There is no random sampling, floating-point eigensolver, character-table lookup, full Griess tensor or full VOA construction.

The preceding supplied Ising-existence checkpoint was preserved: all ten payload hashes and its 89-check report reproduce in all three modes. Its original scope statement says that spectral lists alone are not full VOAs. The present note supplies a later literature-based realization for one list, rather than rewriting that historical record.

The continuum barrier proof, embedding, rationality, and unitary-module classification are analytic arguments or imported theorems, not established by the finite checks. No proof-assistant verification, independent specialist review, or comprehensive priority clearance is claimed. Equivalent landscape consequences might be implicit in the earlier axial-algebra literature.

Read main and all pending work remain preserved. Pending PR24's commutant tricritical peak is explicitly a different result. Remote writes and actual workflow outcomes, if any, are recorded in the integration record, not assumed here. No manuscript, release, outreach, large simulation or physical implementation is performed.

## Primary sources and read depth

[HLY] G. Höhn, C. H. Lam and H. Yamauchi, arXiv:1002.1777v2 (2011 revision), two papers in one PDF. The relevant SECOND paper is *McKay's E6 observation on the largest Fischer group*. Equation (4.1), Lemmas 4.2–4.3, equations (4.2)–(4.3), and equation (5.2)/Theorem 5.1 were inspected in parsed text, together with the stated embedding and representation interfaces. Its printed page 24 (PDF index 67), including the nonextendable 13/8 example, was visually inspected. Repeated screenshot requests for printed pages 22, 23, and 29 failed; successful visual inspection of their table/diagram is not claimed. The explicit product constants are checked for metric invariance and the cited vector identities here. This is not an independent audit of the complete embedding or classification proofs.
https://arxiv.org/abs/1002.1777

[LY] C. H. Lam and H. Yamauchi, *On 3-transposition groups generated by sigma-involutions associated to c=4/5 Virasoro vectors*, arXiv:1311.2829v1. Definition 2.3, Theorem 2.5, Lemma 2.10 and Remark 3.1 were read. Printed page 5 (PDF index 4), with the extension definition and full module list, was visually inspected. Their extension/module theorems and attributions are retained as imported results. No general bare charge-4/5 vector is silently declared extendable.
https://arxiv.org/abs/1311.2829

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. The repeated-field trace formulas and the Potts discussion/footnote on printed page 19 were reread. The spectrum is prior mathematics; the later embedding theorem resolves the historical source limitation. The mixed alternating fifth-order coefficient is not used.
https://arxiv.org/abs/math/0007169

[KLY] M. Kitazume, C. H. Lam and H. Yamada, *3-State Potts Model, Moonshine Vertex Operator Algebra, and 3A-Elements of the Monster Group*, IMRN 2003(23), 1269–1303. The publisher abstract/bibliographic record was obtained. Its full text was not read; [HLY] is the directly inspected source for the explicit construction used here.

The universal cubic cap, critical-point centering, and Hessian relation are reconstructed in the supplied earlier note and used with its stated positive-real assumptions. No foundational unitary Virasoro classification proof is newly supplied. No downloaded papers or font files are bundled.
