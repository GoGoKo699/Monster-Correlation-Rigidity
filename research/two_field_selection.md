# Two near-extremal fields suffice: a bounded bridge from correlations to moonshine

**Date:** 26 September 2026. **Read baseline:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Research role:** a source-based selection bridge after the readout-specificity audit. No pending PR or historical result is incorporated by reference as already merged.

## 1. The reduced target

Abe–Lam–Yamada proved a substantially smaller sufficient condition than the full weight-two multiplication hypothesis used earlier in this project. Their Theorem A.1 states: a simple, rational, C2-cofinite, holomorphic VOA of CFT type, with central charge 24 and V1=0, is the moonshine VOA if it contains **two mutually orthogonal Ising vectors** [ALY]. An Ising vector is a conformal vector generating the simple unitary Virasoro theory L(1/2,0).

This is prior work, not a new uniqueness theorem of this project. Its discovery changes the next research target: one need not first classify the entire Griess multiplication or construct 48 mutually orthogonal Ising vectors. The remaining existence question can be stated as finding one orthogonal pair. The original current-free holomorphic assumptions have NOT been shown here to force that pair.

We derive a sufficient version involving two real weight-two primaries, their two self-couplings, and their two-point overlap. It is robust to explicit deviations in these three numbers, within an EXACT admissible VOA. There is no assumption of an approximately consistent CFT, untrusted calibration, or arbitrary experimental noise.

### Derived correlation criterion

Assume a simple unitary, rational, C2-cofinite, holomorphic VOA V of CFT type with c=24 and V1=0. Let P2 be its real PCT-fixed weight-two primary space, with the positive two-point metric. For unit x in P2 define

f(x) = <x_(1)x,x>,   M = 46/sqrt(141).

If two unit real primaries x,y satisfy

f(x), f(y) >= M - 1/32768,

|<x,y> + 1/47| <= 1/128,

then **V is isomorphic as a VOA to the moonshine VOA**. In particular its algebraic chiral automorphism group is the Monster. The pair need not have been supplied as exact Virasoro vectors, critical points, or known symmetry axes.

The constants are sufficient, not optimal. Their role is transparent: each field is within 1/256 of an exact Ising primary direction; the allowed overlap error is smaller than the discrete spacing to a nonorthogonal Ising pair. The exact classification step is [ALY]; the discrete overlap step is Sakuma's theorem [S]. The quantitative reduction is an explicit corollary using standard cubic estimates, with its normalization checked below. No priority clearance for this robust formulation is claimed.

## 2. Physical data and logical boundaries

For real primaries a,b of weight two,

<a(z)b(0)> = <a,b>/z^4,

and the three-point function has coefficient C(a,b,c)=<a_(1)b,c> with the usual denominator z12^2 z23^2 z31^2. Set mu(a,b)=pi_P2(a_(1)b). The cubic C is symmetric and f(x)=C(x,x,x).

The complete product includes the stress tensor omega:

a*b = mu(a,b) + <a,b> omega/6,

omega*a = 2a,   <omega,omega> = 12.

All of these normalizations are fixed before naming the Monster. The number -1/47 below is not a group character or a fitted tensor entry. It is the overlap of the primary parts of two orthogonal charge-1/2 stress tensors inside total charge 24.

The assumptions c=24, no weight-one currents, holomorphicity, unitarity and the finiteness conditions remain essential to the stated implication. They define the class; two measured numbers alone cannot verify them. In particular the condition is NOT a device-independent test, an efficient algorithm to locate the fields, an operational gate certificate, or a stability theorem for approximate VOAs. The conclusion is the isomorphism type of an exact VOA, not a norm distance between approximately specified theories.

A holomorphic chiral theory has only its vacuum irreducible sector for the full extended chiral algebra. This does not mean it has only the vacuum Virasoro representation. Two commuting Ising subalgebras need not split the entire theory into two independent systems: extension sectors and the commutant remain crucial in [ALY].

The prior generic readout theorem is preserved as a supporting result. No tomography identity, fifth trace, special contraction multiplicity or assumed Monster action is a premise of the correlation criterion.

## 3. From a cubic critical point to a Virasoro sector

This section reconstructs the group-independent portion of the older extremum audit. Let x be a critical point of f on the real unit sphere. Symmetry of C gives

mu(x,x)=lambda x,   lambda=f(x).

Put D_lambda=sqrt(lambda^2+4/3) and

r = 12(1-lambda/D_lambda),
B = 2/D_lambda,
e_x = (r/24)omega + Bx.

The elementary relations

B^2=r(24-r)/48,   B lambda=2-r/6

give e_x*e_x=2e_x and ||e_x||^2=r/2, with 0<r<24. The other Virasoro vector is omega-e_x. Switching x to -x exchanges these two branches; it does not give a second positive maximum.

Because V1=0, every weight-two vector is quasi-primary. Skew symmetry and e_x*e_x=2e_x give e_x_(0)e_x=L_-1 e_x, e_x_(2)e_x=0 and e_x_(3)e_x=(r/2)1. Therefore the modes e_x_(m+1) generate a Virasoro algebra with central charge r.

On its cyclic vacuum module the e_x-energy equals the ambient nonnegative integer degree: both count the sum of the negative mode indices on vacuum descendants. The ambient positive form restricts positively and gives (L_m^e)^dagger=L_-m^e. The cyclic vacuum representation is irreducible: a hypothetical lowest positive-degree vector in a proper submodule is orthogonal to every vacuum descendant by adjointness, hence zero. Thus it is the unitary vacuum representation L(r,0), not an arbitrary quotient lacking the necessary positivity hypotheses.

The unitary Virasoro classification [FQS], in the explicit positive-energy form recalled by [W, p.2], implies

r in {1-6/[m(m+1)]: m=3,4,...} union [1,infinity).

In particular r>=1/2; if r is not 1/2, then r>=7/10. The original FQS full paper was not obtained in this pass; its statement was read in [W] and [CP], and the original publisher abstract was checked. This is an imported classification input, not a theorem proved by the scalar checks.

The inverse relation is strictly decreasing:

lambda(r) = (2-r/6)/sqrt(r(24-r)/48),

lambda'(r) = -1/[2 (r(24-r)/48)^(3/2)] < 0.

Compactness gives a sphere maximum; oddness of f gives its negative minimum. Hence

|f(x)| <= M = lambda(1/2)=46/sqrt(141)

for every real unit x. Every critical point not associated with r=1/2 has

f(x) <= M2 = lambda(7/10)=226/sqrt(4893) < 33/10.

Also 19/5<M<4. No Ising existence has been assumed to prove the cap or the non-Ising critical-value bound.

Conversely, a real Ising vector e gives

a = (24/sqrt(141))(e-omega/48),

which is a unit primary with f(a)=M. Consequently saturation is equivalent to existence of an Ising vector, and all saturating directions correspond to actual Ising vectors. For the known moonshine example these exist; for an unknown candidate their existence remains a separate issue.

## 4. Near saturation forces proximity to a real Ising direction

Let A={a: ||a||=1, f(a)=M}. It may initially be empty. If some x has f(x)>M2, its global maximum exceeds M2, so section 3 forces that maximum to have charge1/2. Thus A is nonempty.

### The local bound needs no Monster multiplicities

For an Ising vector e, rationality of L(1/2,0) gives the three allowed irreducible lowest weights 0,1/2,1/16 [S, p.2]. On ambient V2, V1=0 eliminates level-one descendants; the only level-two vacuum descendant is e itself. Thus the spectrum of R_e=e_(1) on V2 is contained in {0,1/16,1/2,2}, with its 2-eigenspace one-dimensional.

For a corresponding maximizing primary a,

e=omega/48+(sqrt(141)/24)a.

On the space perpendicular to omega and e, which is the primary tangent space a-perp,

R_e=I/24+(sqrt(141)/24)L_a.

Hence the tangent eigenvalues of L_a are among

-1/sqrt(141),   1/(2sqrt(141)),   11/sqrt(141).

No assertion about the sizes of these eigenspaces is needed. The sphere Hessian 6L_a-3M I is strictly negative there, with eigenvalues among -144/sqrt(141), -135/sqrt(141), -72/sqrt(141).

For s=||x-a||<=1/10 set q=1-s^2/2, t=sqrt(1-q^2), and x=qa+tv with v perpendicular to a and ||v||=1. Then

f(x)=Mq^3+3qt^2 C(a,v,v)+t^3 f(v).

Use C(a,v,v)<=11/sqrt(141), |f(v)|<=M and q>0. Elementary chord estimates give

M-f(x) >= s^2[36/sqrt(141)-(3M/4)s^2-Ms] >= 2s^2.

The bracket is in fact greater than 3-3/100-4/10=257/100 throughout this interval. A uniform sufficient constant2 is retained. In particular distinct maxima are separated by more than1/10; the compact set A is finite.

### The global entry step

The local estimate alone is not sufficient to localize all near-maximal fields. Let K be the complement of the open1/10-neighborhood of A in the sphere. A boundary point of K has loss at least1/50 by the local estimate. An interior maximizer of f on K is a critical point not in A, so its value is at most M2. Since M-M2>1/2>1/50, no point in K has f>M-1/50.

It follows that for any 0<=epsilon<1/50,

f(x)>=M-epsilon  ==>  there is an a in A with
||x-a|| <= sqrt(epsilon/2).

Uniqueness at the particular tolerances below follows from the1/10 separation. This proof does not assume the known Monster axes exhaust the maxima. It uses all actual maxima of the unknown candidate, identified only as Ising directions by positivity and critical values.

## 5. Three correlation numbers imply the full VOA identification

For exact maximizing primaries a,b, their Ising vectors obey

<e_a,e_b> = [1+47<a,b>]/192.

Thus <e_a,e_b>=0 is equivalent to <a,b>=-1/47. Orthogonality here means vanishing singular OPE and commuting Virasoro subalgebras; it does NOT mean that regular tensor-product states such as e_(-1)f vanish. It yields the commuting Ising tensor subalgebra used in [ALY]. Indeed R_e is positive semidefinite on V2 and <R_e f,f>=2<e,f>=0, so e_(1)f=0. The norm of e_(0)f is then 2<e_(1)f,f>=0 by the Virasoro adjoint relation; the higher singular products vanish by degree and orthogonality. It does not mean the original primary fields a,b are orthogonal: their stress subtraction produces the fixed negative overlap.

Sakuma's theorem for real positive-definite VOAs with V0=R1 and V1=0 classifies the inner products of pairs of Ising vectors [S, Theorems4.3-4.4]. Including the identical-vector case, the possible values are

0, 1/256, 5/1024, 3/512, 1/128, 13/1024, 1/32, 1/4.

Several types share the value1/256. Only the implication

|<e,f>|<1/256  ==>  <e,f>=0

is needed here. The theorem's general statement, not just a table for the known Monster, is the input.

More generally, if f(x),f(y)>=M-epsilon with epsilon<1/50, and

|<x,y>+1/47|<=delta,

delta+2sqrt(epsilon/2)<3/188,

then their localized Ising directions a,b obey

|<e_a,e_b>| <= (47/192)[delta+2sqrt(epsilon/2)] < 1/256.

They are therefore mutually orthogonal. [ALY, Theorem A.1] now identifies V with V-natural.

For the displayed simple dyadic choice epsilon=1/32768 and delta=1/128,

sqrt(epsilon/2)=1/256,

delta+2sqrt(epsilon/2)=1/64<3/188,

|<e_a,e_b>|<=47/12288<48/12288=1/256.

The strict margin is1/12288 in the Ising-vector inner product. This completes the derived criterion. There are two self-three-point coefficients and one cross-two-point coefficient; finding and normalizing the fields and certifying the ambient hypotheses are NOT free operations supplied by this theorem.

### The prior classification mechanism, not a new proof

[ALY] uses the orthogonal pair's involutions and Ising module decomposition to construct a Z2 orbifold with nonzero abelian weight-one Lie algebra. That orbifold is the Leech lattice VOA. Reversing the construction and using uniqueness of the simple-current extension identifies V with moonshine. The theorem, Appendix A's proof path, and the main intermediate statements were inspected. The rationality, commutant, fusion, extension and Leech-characterization inputs were NOT independently re-proved or comprehensively audited here.

## 6. A one-number extremality formulation

Within this exact class define a pair score

S(V)=max min{f(x),f(y)},

where the maximum is over real unit primaries with <x,y>=-1/47. The domain is compact and nonempty since dim P2=196883 in this class. Its definition refers to normalized low-energy two- and three-point data, not a group action or chosen multiplication table.

The known moonshine theory contains an explicit pair [LS, Theorem3.1]: for a Leech vector alpha of squared norm4, put A=alpha(-1)^2 1 and E=e^alpha+theta(e^alpha). Then e_+=A/16+E/4 and e_-=A/16-E/4 lie in V_Leech^+ inside V-natural. The weight-two identities A*A=16A, A*E=16E, E*E=A and norms <A,A>=32, <E,E>=2, <A,E>=0 verify e_+*e_+=2e_+, e_-*e_-=2e_- and <e_+,e_->=0 directly. Thus S(V-natural)=M. Conversely S(V)=M gives that pair and [ALY] yields V isomorphic to V-natural. Thus moonshine is the unique optimizer of this specified interaction objective. The robust criterion gives the uniform sufficient separation

V not isomorphic to V-natural  ==>  S(V)<M-1/32768.

This is conditional separation of any hypothetical other candidates, not evidence that such a candidate exists. It does not prove the original spectral/minimality assumptions themselves force S(V)=M. Adding this interaction maximization is an additional selection criterion; its physical attractiveness is not a demonstrated RG dynamics or experimental realization. We should not rename the unsolved existence implication as already proved.

The numerical overlap constraint is the normalized expression of two orthogonal minimal-charge Virasoro components. Its independent physical motivation should be discussed explicitly before promoting this optimization to the project's central selection principle.

## 7. Scope controls and limits of the route

### Holomorphicity cannot be dropped

The tensor product L(1/2,0)^(tensor48) is a simple unitary rational current-free c24 VOA. It has48 weight-two stress tensors, hence47 weight-two primaries, and is not holomorphic (each Ising factor has nonvacuum modules). It has many orthogonal Ising pairs. Centering any two factor stress tensors gives f(a)=f(b)=M and <a,b>=-1/47 exactly. Nevertheless it is not moonshine: its weight-two dimension is48 rather than196884.

The checker evaluates this negative control in the exact48-coordinate weight-two algebra, without constructing the full VOA. This is a genuine outside-class comparison, not a counterexample to [ALY] or to the criterion with holomorphicity included.

### A local maximum is not the same as saturation

Similarly, L(4/5,0)^(tensor30) has total c24 and V1=0. Its weight-two algebra consists of the30 factor stress tensors. All weight-two Virasoro vectors there are sums of factors, so the smallest nonzero component charge is4/5. A centered single-factor direction is a strict local (indeed global) cubic maximum, but its value is lambda(4/5)<M. This simple real-positive model rules out inferring saturation merely from criticality or a negative Hessian in the broader unitary class. It is nonholomorphic and does not settle the analogous holomorphic question.

The earlier Matsuo discussion of a W3(4/5) embedding in moonshine is not used to claim this counterexample lives inside moonshine: his cited version explicitly left that embedding's existence open. The tensor-product control avoids silently converting that conditional discussion into an existence theorem.

### What remains to be proved

The bare c24 current-free holomorphic assumptions do not yet yield an orthogonal Ising pair in this work. A single saturated direction gives one Ising vector, not the pair required by [ALY]. Finiteness of the symmetry group, simplicity of the primary algebra, or the generic5/6 readout thresholds cannot replace the missing pair-existence argument.

The useful reduction is that the missing object is now small and structurally recognizable: two compatible minimal Virasoro components, or the sufficient three-number correlation witness. No complete Griess table or preassigned Monster action is needed to FINISH the classification once this object is established. The question whether the spectral constraints FORCE it remains the next research obligation.

## 8. Evidence and attribution

The finite checker has **68 exact integer/fraction checks** of the charge/cubic conversions, cap and next-critical-value inequalities, local uniform constants, tangent spectra, complete discrete overlap list and separation margin, and exact tensor-product scope controls. Its largest square matrix is4x4 and its largest coefficient vector has length48. It also replays the inherited four-state Virasoro Gram normalization at selected rational charges. These are exact algebra/scalar controls; the continuum localization argument and source classification theorems are proofs/dependencies stated above, not conclusions inferred from sampling.

No Monster-sized operator, full OPE tensor, formal proof assistant, independent expert review, or comprehensive novelty audit is involved. The original MIT license and every prior result are preserved. The supplied readout-assumption archive is replayed separately and its claims are not reclassified as Monster-specific.

The result is a source-based corollary combining established Virasoro, Ising-pair and moonshine-classification mathematics with explicit norm estimates. The exact two-Ising uniqueness theorem belongs to Abe–Lam–Yamada. The local cubic estimate generalizes the old project extremum argument by removing its assumed Monster-axis identification. Priority of an equivalent robust correlation formulation is unresolved; targeted source searches do not establish originality.

No manuscript, release, outreach or practical implementation is supplied. Remote changes and actual verification outcomes, if any, are recorded in the integration record rather than assumed here.

### Primary sources and read depth

[ALY] T. Abe, C.H. Lam, H. Yamada, *A remark on Z_p-orbifold constructions of the Moonshine vertex operator algebra*, arXiv:1705.09022v4; Math. Z.290 (2018),683–697. Theorem A.1, Appendix A's decomposition, Propositions/Lemmas A.2–A.5 and Theorems A.6–A.8 inspected. Printed pp10 and12 visually inspected; requests for p11 screenshots failed, and its parsed proof was read. This is the imported full-VOA classification theorem, not a new project result.
https://arxiv.org/abs/1705.09022

[S] S. Sakuma, *6-transposition property of tau-involutions of vertex operator algebras*, arXiv:math/0608709v1; IMRN2007,rnm030. General real-positive hypotheses in section1, Ising decomposition, Theorems4.3–4.4 and the inner-product formulas inspected. Printed p2 visually inspected; p14 screenshot requests failed. The entire classification proof was not independently audited. The needed minimum positive overlap is1/256 in the norm ||e||^2=1/4 convention.
https://arxiv.org/abs/math/0608709

[FQS] D. Friedan, Z. Qiu, S. Shenker, *Details of the non-unitarity proof for highest weight representations of the Virasoro algebra*, CMP107 (1986),535–542. Original publisher abstract inspected; full-text access failed in this pass. The precise theorem is used through the explicit statements in [W] and [CP], with attribution retained. No fresh audit of the original proof is claimed.
https://doi.org/10.1007/BF01205483

[W] A. Wassermann, *Direct proofs of the Feigin–Fuchs character formula for unitary representations of the Virasoro algebra*, arXiv:1012.6003v1. Section1, pp1–2: positive-energy hypotheses, irreducible decomposition, and explicit unitary c,h series read. Its p2 screenshot request failed. The characterization is attributed there to FQS; no whole-paper character proof is claimed as read.
https://arxiv.org/abs/1012.6003

[CP] V. Chari, A. Pressley, *Unitary representations of the Virasoro algebra and a conjecture of Kac*, Compositio Math.67 (1988),315–342. Introductory unitary-series statement, printed316–317, read in parsed form; printed316 screenshot failed. Used as an independent published statement of the imported classification, not as a substitute claim to have read FQS's proof.
https://www.numdam.org/item/CM_1988__67_3_315_0/

[LS] C.H. Lam, H. Shimakura, *Ising vectors in the vertex operator algebra V_Leech^+ associated with the Leech lattice*, arXiv:0810.5395v1. Section3/Theorem3.1's explicit pair, the section1 inclusion in moonshine, and the Ising-module interface inspected. Printed p6 visually inspected. We independently check the relevant two-dimensional weight-two products and use singular-OPE/commuting-Virasoro orthogonality, not the literal all-modes-zero wording preceding that theorem. The full Ising-vector classification is not audited here.
https://arxiv.org/abs/0810.5395

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Weight-two conventions, Ising spectral interface and section4.2 comparisons checked; printed16 visually inspected earlier in this continuation. The conditional W3 discussion and its footnote were read, not upgraded to an existence result. No disputed fifth-order trace coefficient is used.
https://arxiv.org/abs/math/0007169

The positive/PCT adjoint interface is inherited from Dong–Lin arXiv:1308.2361 and the existing VOA extremum audit. The latter was read from actual live main before this calculation. Neither the full previous audit nor all foundational source proofs were independently repeated. No downloaded papers or font files are bundled.
