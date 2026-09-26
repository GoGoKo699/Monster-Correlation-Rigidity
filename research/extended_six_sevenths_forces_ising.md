# An extended charge-6/7 component forces Ising in the extremal class

26 September 2026. Read baseline: `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
Proposed additive branch: `research/extended-six-sevenths-ising`.

## 1. Result and the extra hypothesis that matters

**Source-based corollary.** Let V be a simple unitary rational C2-cofinite holomorphic VOA of CFT type with central charge 24 and V1=0. If V contains a real extendable Virasoro vector v of central charge 6/7, then V contains a real Ising vector.

“Extendable” means that v is the conformal vector of a subalgebra isomorphic to the standard simple-current extension

$$W(6/7)=L(6/7,0)\oplus L(6/7,5).$$

A bare charge-6/7 Virasoro vector is NOT being assumed extendable automatically. The extra weight-five primary and its consistent extension products are a genuine additional hypothesis. This corollary does not show the original physical assumptions force v or its extension to exist, nor does it supply an orthogonal second Ising vector or identify the whole VOA.

The route differs from the preceding shared-field lemma: no charge-4/5 component, no commuting partner, and no prescribed joint weight-(2/3,4/3) state are required. Instead, the ambient trace constraints force a two-dimensional weight-two eigenspace with v-energy 4/3. A two-sign cubic test using any real unit vector in that space crosses the previously justified no-Ising bound.

The unitary minimal-model classification, extension module list, and trace theorems are prior mathematics. This is a derived sufficient condition, not a newly classified extension, a completed physical selection of the Monster, or a priority-cleared new theorem.

## 2. Why the extended component has exactly two required fields

Put R_v=v_(1)|V2. For any real Virasoro vector e, positivity and the commuting complement omega-e give nonnegative internal conformal energies bounded by the ambient energy. At ambient weight two, all states other than the vector e itself are highest-weight states for Vir(e): an internal level-one descendant would originate in V1=0; an internal level-two vacuum descendant is e. Thus the eigenvalue 2 has multiplicity one.

For W(6/7), the nine irreducible modules have the following underlying Virasoro forms [HLY, section 2.2 of the second paper]:

$$L(6/7,0)\oplus L(6/7,5),\quad
L(6/7,1/7)\oplus L(6/7,22/7),\quad
L(6/7,5/7)\oplus L(6/7,12/7),$$

$$L(6/7,4/3)^\pm,\quad L(6/7,1/21)^\pm,\quad L(6/7,10/21)^\pm.$$

There are nine modules, but only six distinct lowest weights. The weight-12/7 companion is one internal level above 5/7, so its appearance at ambient weight two would require a nonzero ambient weight-one bottom state. It is excluded. The 22/7 and 5 companions exceed ambient weight two. Twisted W-modules do not occur in the ambient VOA viewed as a module over its actual extended subalgebra.

Consequently, on E=v-perp in V2 the allowed eigenvalues are

$$0,\quad 1/21,\quad 1/7,\quad 10/21,\quad 5/7,\quad 4/3.$$

These are not Monster representation labels. They come from the standard unitary extension representation theory.

For a charge-r component the inherited repeated trace formulas are

$$\begin{aligned}
p_0(r)&=196884,\\
p_1(r)&=16407r,\\
p_2(r)&=r(1271r+2310),\\
p_3(r)&=3r(31r^2+155r+300),\\
p_4(r)&=r(13r^3+120r^2+534r+864)/2,\\
p_5(r)&=r(7r^4+100r^3+740r^2+2720r+3840)/16.
\end{aligned}$$

Here p_k=Tr(R_e^k). Matsuo [M, Corollary 4.1, equation (4.1), Remark 4.3] and Hoehn's explicit design replacement [H, end of section 2] justify their use without assuming a Monster action. The alternating term in the disputed fifth-order formula vanishes for repeated arguments. The proof uses no mixed alternating normalization.

At r=6/7, the six-by-six Vandermonde system

$$\sum_h n_hh^k=p_k(6/7)-2^k,\qquad k=0,\ldots,5$$

has the unique solution

| v-energy h | Multiplicity in E |
|---|---:|
| 0 | 35973 |
| 1/21 | 123556 |
| 1/7 | 29394 |
| 10/21 | 7176 |
| 5/7 | 782 |
| 4/3 | 2 |

Adding v restores dim V2=196884. In particular the required 4/3 eigenspace is nonzero and real under PCT.

A shorter certificate isolates that one eigenspace. The polynomial

$$P(z)=\frac{z(z-1/21)(z-1/7)(z-10/21)(z-5/7)}{2600/2401}$$

is its spectral projector on E. Its coefficient vector in increasing degree is

$$\left(0,\frac1{468},-\frac7{104},\frac{12397}{23400},-\frac{9947}{7800},\frac{2401}{2600}\right).$$

Substitution of the five traces gives Tr_E P(R_v)=2. The complete solution and this scalar projector calculation are independently checked in the accompanying exact program.

## 3. The ambient no-Ising bound, with the competing saddle excluded

For clarity the prior threshold is reconstructed here instead of used as an unexplained numerical premise. Let P2=omega-perp in V2, and define f(x)=<x_(1)x,x> on its real unit sphere. The stress convention is ||omega||^2=12 and omega*a=2a.

At a critical point, mu(x,x)=lambda x. The element

$$e=\frac r{24}\omega+b_rx,\qquad
b_r=\sqrt{\frac{r(24-r)}{48}},\qquad
\lambda=\lambda(r)=\frac{2-r/6}{b_r}$$

is a real Virasoro vector. For a positive critical value, 0<r<12. Its cyclic vacuum module is unitary with its positive-energy grading inherited from the ambient mode degrees. The FQS unitary classification, as explicitly recalled in [W], restricts positive r below one to 1-6/[m(m+1)], m>=3. Also

$$\lambda'(r)=-\frac1{2b_r^3}<0.$$

The first charges are 1/2,7/10,4/5. At a charge-7/10 vector, the six allowed nonstress weights are

$$0,\quad 3/80,\quad 1/10,\quad 7/16,\quad 3/5,\quad 3/2.$$

The same six trace equations fix their multiplicities to

$$51054,\quad91392,\quad47634,\quad4864,\quad1938,\quad1.$$

This includes a compulsory 3/2 tangent direction. The sphere Hessian is

$$\operatorname{Hess}f=\frac6{b_r}(R_e-I)$$

on omega,e-perp. That direction has positive curvature; a charge-7/10 point cannot be a global maximum. All other tangent directions have negative curvature. This uses all ambient tangent directions, not a restriction to an Ising commutant.

Compactness supplies a global maximum. A nonzero cubic is already ensured below by the supplied charge-6/7 component. If the theory had no Ising vector, that maximum would have r>=4/5, whence

$$\boxed{\max_{\|x\|=1} f(x)\le\frac{28}{\sqrt{87}}.}$$

This necessary no-Ising bound depends on the exact ambient trace constraints and unitarity. It is not a generic fact about arbitrary positive metrized algebras or arbitrary c24 nonholomorphic theories.

## 4. The 4/3 response crosses the bound without knowing its self-coupling

Center and normalize v relative to the AMBIENT charge-24 stress:

$$a=\frac{v-\omega/28}{9/14}.$$

Then a is a unit primary, f(a)=26/9, and b_(6/7)=9/14 is rational. Choose any unit real y in the forced 4/3 eigenspace. It is orthogonal to v and omega, hence is an ambient primary perpendicular to a. Its known mixed coefficients are

$$C(a,a,y)=0,\qquad C(a,y,y)=\frac{4/3-1/14}{9/14}=\frac{53}{27}.$$

No condition is imposed on k=C(y,y,y) or on off-plane components of y*y. The two unit trial fields

$$x_+=\frac45a+\frac35y,\qquad x_-=\frac45a-\frac35y$$

satisfy

$$f(x_\pm)=\frac{3572}{1125}\pm\frac{27}{125}k.$$

Their average is fixed, so one trial has

$$f(x_\pm)\ge\frac{3572}{1125}>\frac{31}{10}>\frac{28}{\sqrt{87}}.$$

For an exact comparison, the squared difference from the no-Ising bound is 39266336/36703125>0. The no-Ising bound is contradicted, proving the corollary.

The supplied extended component is itself a saddle of the ambient cubic: it has exactly two increasing tangent directions (the 4/3 eigenspace) and 196880 decreasing directions. Merely observing positive curvature would not prove that a path exceeds the relevant finite threshold. The explicit 4:3 mixture does so, with the unknown self-coupling cancelled by the two signs.

This proof does not locate the exact Ising vector near either trial, does not claim the trials are Ising, and does not supply a global search algorithm. It proves that the actual global maximum must be an Ising direction. It also does not prove the Ising vector lies in W(6/7), whose own weight-two space has only its stress tensor. The ambient 4/3 module states are essential.

## 5. What the initial shared-sector test actually showed

The first attempted route in this continuation asked whether the previous joint weight-(2/3,4/3) field was forced for a supplied commuting charge-4/5 and charge-6/7 pair. The finite mixed moments through total degree five do not suffice, even when the allowed low-energy spectra of both extensions are imposed.

Here is an exact nonnegative integral *spectral relaxation* with no such shared field. Rows are the 4/5 energies (0,1/15,2/5,2/3); columns are the 6/7 energies (0,1/21,1/7,10/21,5/7,4/3):

$$\begin{pmatrix}
9019&38200&7554&2460&242&2\\
25200&78192&20700&4536&540&0\\
1303&6300&888&180&0&0\\
450&864&252&0&0&0
\end{pmatrix}.$$

Add the two stress directions at joint energies (2,0) and (0,2), each once. All 21 mixed moments Tr(R_u^a R_v^b), a+b<=5, agree exactly with the inherited symmetric trace formulas. In particular the desired last-row/last-column multiplicity is zero; the two unavoidable 4/3 states lie instead at u-energy zero.

The checker obtains the moments by polarizing Tr R_(u+t v)^n. The five-form vanishes identically on a repeated argument, and u*v=0 makes every source contraction explicit. It records the complete resulting moment dictionary and verifies this integer table. No general nonlinear programming output is used as proof; an exploratory small linear-program search only suggested the table, whose exact certificate is supplied.

This is NOT claimed to be an actual VOA, a fusion-consistent tensor, a counterexample to full shared-sector forcing, or an Ising-free candidate. Additional mixed products and extension fusion may rule it out. It establishes only that this finite trace relaxation cannot force the field's location. The new proof avoids this issue: it uses the 4/3 space wherever it is in the ambient theory and needs no charge-4/5 partner.

## 6. Why neither the extension nor the ambient class may be omitted

### Bare charge 6/7 remains a separate case

The unextended Virasoro Kac table has more allowed weights. The following multiplicities, all at energies below one, reproduce the same first five ambient moments after adding v at energy two:

| h | 0 | 1/56 | 1/21 | 5/56 | 1/7 | 3/8 | 10/21 | 33/56 | 5/7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| n_h | 8153 | 62974 | 68688 | 26908 | 21287 | 2244 | 5670 | 34 | 925 |

This exact moment list has no 4/3 state and would pass the local Hessian maximum inequality. It is not constructed as a VOA and is not a claim about a possible actual global maximum. It proves that removing the extension hypothesis from the present proof is unjustified on these trace data alone. Existence of a bare 6/7 component has not been shown here to force Ising.

### A genuine outside-class control

The tensor product W(6/7)^(tensor28) is a unitary rational current-free c24 theory, but is nonholomorphic. Its weight-two space consists of 28 factor stress tensors. Every weight-two Virasoro idempotent is a sum of factors, so its positive charge is an integer multiple of 6/7, never 1/2. It contains many extended 6/7 components and no Ising vector.

It fails the extreme character/trace inputs: dim V2=28 rather than196884 and Tr R_v=2 rather than p1(6/7). Thus there is no contradiction. The upper theorem is not a generic claim about every c24 theory containing the same minimal-model extension. Unitarity/rationality of the standard extension are inherited source results; the checker verifies only its factorwise weight-two algebra and charge accounting, not the full tensor-product VOA.

## 7. What the result does not finish

The extension and unitary representation theory are being used as genuine extra structure, not as a disguised supplied Ising vector. The module theorem forces two ordinary weight-two response fields; the variational argument forces a charge-1/2 component elsewhere. Neither the 3A table nor a Monster automorphism is a premise.

The original holomorphic/current-free assumptions have not been shown to force an extendable 6/7 vector. A bare component, an extendable component, and a component derived from an already supplied 3A subalgebra are distinct hypotheses. The last would already build in Ising structure; it is not used here.

A second mutually orthogonal Ising vector is also unforced. The Abe-Lam-Yamada classification endpoint still requires that pair, with all its ambient hypotheses. The present result supplies only the first under an alternative sufficient hypothesis. It does not make the earlier shared-field lemma obsolete: that lemma did not require the extension or the holomorphic c24 trace system, so the two sets of assumptions are not identical.

This is an interaction/representation existence lemma, not a new physical axiom, a dynamical mechanism, or a completed proof that nature selects the Monster. The proper next question is whether the original constraints force suitable extendability or another structure guaranteeing the same large response; it must not be assumed merely because the known example has it.

## 8. Evidence, provenance, and source depth

The program uses integers and fractions only. It emits both six-by-six Vandermonde certificates; the exact spectral projector; the two-sign polynomial; the full joint-moment certificate and both scope controls. It also checks the field coefficients on the known small positive 3A algebra as a witness, not as the proof's premise. The largest square matrix is 6x6; no 196884-dimensional matrix, full VOA, Monster character table, or random simulation is used.

The supplied previous shared-field checkpoint was replayed unchanged: all eleven file hashes and all58 checks reproduce under normal/-O/-OO. New report counts and fingerprints are stated in the integration record after execution. The universal implication is the analytic representation/variational proof above, not a conclusion inferred from small examples.

Live main and pending branches were inspected. In particular PR26's mixed-square extraction and Ising-free code subtheory were read at the description level only; its complete certificate was NOT independently audited here. That result and this one are compatible: the present lemma uses the full ambient extremal trace system, not the trace on an Ising-free smaller subtheory. No other branch is merged or rewritten.

Runtime git access failed at DNS resolution. Local checks are not a live-main historical replay. Any additive PR uses a separate manifest and read-only workflow to preserve every baseline byte and report actual strict and bounded-portability outcomes separately. No old result or tolerance is changed. No formal verification, independent specialist review, comprehensive priority clearance, manuscript, release, or outreach is claimed.

### Primary sources inspected

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Corollary4.1, repeated formulas(4.1), Remark4.3 and the general source contractions were read. Printed page16 was visually inspected. The page17 screenshot request failed, but Remark4.3 was read in parsed text. No disputed mixed alternating coefficient is used.
https://arxiv.org/abs/math/0007169

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. End of section2's explicit replacement of Matsuo's large-Aut hypotheses and Theorem3.1 context. Printed page12 was visually inspected. These are imported trace/design theorems, not newly re-proved modular results.
https://arxiv.org/abs/math/0701626

[HLY] G. Hoehn, C.H. Lam, H. Yamauchi, arXiv:1002.1777v2, SECOND paper, *McKay's E6 observation on the largest Fischer group*. Section2.2: Theorem2.7, Definition2.8, Theorem2.11 and the full W(6/7) module list; printed page12 (PDF index55) visually inspected. The extension theorem and module classification there are attributed to [LLY,LY]; their original full proofs were not independently audited in this pass. Section4's 3A product table supports only the separate small-model control. No known group action is transferred to an unknown candidate.
https://arxiv.org/abs/1002.1777

[W] A. Wassermann, *Direct proofs of the Feigin-Fuchs character formula for unitary representations of the Virasoro algebra*, arXiv:1012.6003v1, introduction pp1-2. The exact FQS unitary series and positive-energy hypotheses were read in parsed text; its page2 screenshot request failed. The classification is imported with original attribution, not proved by the finite spectrum checks.
https://arxiv.org/abs/1012.6003

Scoped searches did not establish priority for this sufficient corollary. An unmatched search is not originality evidence. No downloaded papers or fonts are bundled.
