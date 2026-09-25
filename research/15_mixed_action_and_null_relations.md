# Mixed interactions: the five-form is fixed, but null relations must survive

**Date:** 25 September 2026. **Base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/mixed-action`. PR11 was integrated first; its exact candidate tree is the baseline tree. The earlier physical-selection assumptions and all historical evidence are preserved.

## 1. Bounded result and unresolved independence

In the physical class of note12, the primary weight-two product determines not only the pair-production Gram on weight-three primaries but also their mixed action by a weight-two field. The apparently additional alternating five-form is fixed by the prior fifth-trace formula, whose coefficient is **52**, not zero. No Monster action, character decomposition, known multiplication table or axis system is assumed.

For real primary e and x,y in the unit exterior space wedge^2 P2, define

T_e(x,y)=<Bx,e_(1)By>,

where B is note13's onto map with B^dagger B=G=282 Pi and BB^dagger=282I. The primary compression of e_(1) is implicit: e_(1) itself need not preserve P3.

The derivation below gives the tensor-only formula

$$\boxed{T_e=\tfrac14\mathcal A_e+\tfrac1{208}G\mathcal D_eG.}\tag{1}$$

Here D_e and A_e are explicitly built from the still-unknown primary cubic. Since a zero pair-created state must have zero matrix elements against every probe, a physical candidate must satisfy

$$\boxed{G\mathcal A_e=282\mathcal A_e=\mathcal A_eG\quad\text{for every }e.}\tag{2}$$

This is a concrete quintic necessary identity (with lower-degree terms), not just an equality of spectral multiplicities. It is equivalent to quotient consistency of the mixed action **after** the full fifth-trace formula is used. It is not claimed to be algebraically independent of the previously imposed identities, or to distinguish the Monster already. This continuation does not establish whether (2) follows from the full fifth-trace system or even from the earlier fourth-order system. That polynomial implication is now an explicit bounded question rather than an unspecified higher-OPE obstruction.

The physical meaning is that different superpositions of pairs representing the same state must give the same mixed three-point data. One may not replace a failed null-relation test by projecting the proposed answer: that changes the mode-derived interaction.

## 2. Source inputs and an important attribution refinement

The admissible class remains nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs, V1=0, minimizing positive c. This fixes c=24 and the J spectrum in the stated restricted class; it is not a universal physical law or a demonstrated RG selection process.

The needed fifth-trace theorem is [M, Theorem2.1(5), Corollary4.1]. The conformal-design replacement explained by [H] remains valid. A more direct source passage is now recorded: **Matsuo Remark4.3, printed p.17, already states that the Norton trace formulae hold for rational selfdual c=24, V1=0, C2-finite VOAs.** Thus the symmetry-free applicability of these trace formulae is explicitly prior, not a new implication supplied by this project. The indicated remark was read in parsed text; its screenshot failed. Printed pages7 and16, including the quinary definition and coefficient52, were visually inspected successfully.

For five primary inputs write

H(a,b;e;c,d)=<a*b,e*(c*d)>,

where * is the FULL V2 product. Put

$$\Omega(a,b,c,d,e)=\operatorname{Alt}_5\big[a_{(3)}b_{(2)}c_{(1)}d_{(0)}e\big],$$

with the vacuum coefficient understood and Alt normalized by 1/120. The source fifth-trace formula on primary inputs is

$$\operatorname{Tr}R_1R_2R_3R_4R_5
=30\operatorname{Cyc}H(1,2;3;4,5)
+4\operatorname{Cyc}H(1,4;3;2,5)
-22\operatorname{Cyc}H(1,5;3;2,4)
+8\operatorname{Sym}C_{123}g_{45}+52\Omega_{12345}.\tag{3}$$

Cyc has five terms and Sym here has the ten distinct pair/triple partitions. Every tree or metric-times-cubic term has a symmetric pair, so full alternation kills it. Therefore

$$\boxed{\Omega=\frac1{52}\operatorname{Alt}_5\operatorname{Tr}(R_aR_bR_cR_dR_e)
=\frac1{52}\operatorname{Alt}_5\operatorname{Tr}(L_aL_bL_cL_dL_e).}\tag{4}$$

The R are full multiplication operators; L are primary-projected ones. The difference of the two five-traces consists of stress-excursion trees, also killed by alternation. Formula (4) does not permit retaining only the alternating part of (3) while discarding its other constraints. Both are needed at distinct steps below.

As an equivalent evaluation with full multiplication matrices, cyclicity and metric adjoints give

$$\operatorname{Alt}_5\operatorname{Tr}(R_aR_bR_cR_dR_e)
=\tfrac1{12}\operatorname{Tr}R_e\big([R_a,R_b][R_c,R_d]-[R_a,R_c][R_b,R_d]+[R_a,R_d][R_b,R_c]\big).$$

No fifth-trace theorem is needed for this last elementary identity. It checks the normalized alternation convention separately.

## 3. General five-label mode reduction

This section works in a unitary V1=0 VOA before imposing extremal trace constants. Use the PCT-fixed real subspace and positive Hermitian form of [DL]. For real weight-two quasiprimary a, a_(n)^dagger=a_(2-n), while the odd-weight primary adjoint carries its usual minus sign. All uses of odd modes below retain that sign.

Define

G(a,b;c,d)=<B(a,b),B(c,d)>=<a*c,b*d>-<a*d,b*c>,

and let t_e(a,b;c,d) denote the following ten-tree expression:

$$\begin{aligned}
2t_e(a,b;c,d)={}&-H(b,c;a;d,e)+H(b,d;a;c,e)
+H(a,c;b;d,e)-H(a,d;b;c,e)\\
&-H(a,d;c;b,e)+H(a,e;c;b,d)
+H(a,c;d;b,e)-H(a,e;d;b,c)\\
&-H(a,c;e;b,d)+H(a,d;e;b,c).
\end{aligned}\tag{5}$$

Then the exact general mode identity is

$$\boxed{\langle B(a,b),e_{(1)}B(c,d)\rangle=t_e(a,b;c,d)-\Omega(a,b,c,d,e).}\tag{6}$$

The five-form is not generically zero. A small even-three-boson control below has a nonzero value.

### Derivative subtractions and proof of the remaining ambiguity

Let N_e=<a_(0)b,e_(1)c_(0)d>. Since L1D=4 on V2 and [L1,e_(1)]=e_(2), direct adjoint manipulations give

$$N_e=T_e+\tfrac12G(e,a*b;c,d)+\tfrac12G(e,c*d;a,b)
+\tfrac32H(a,b;e;c,d).\tag{7}$$

All products in this equation include the stress tensor. The two derivative corrections cannot be replaced by a single primary-only term.

For a useful explicit mode relation, put V(a,c,d)=a*(c*d)-c*(a*d)+(a*c)*d. Commuting a_(2) through e_(1)c_(0), using [a_(1),c_(1)]=B(a,c)_(2), and using odd-primary skew symmetry yields

$$\begin{aligned}
T_e(a,b;c,d)+T_b(a,e;c,d)={}&<b,e*V(a,c,d)>+\tfrac12<b,V(a*e,c,d)>\\
&+\tfrac32G(a,e;b,c*d)-\tfrac12G(e,a*b;c,d)
-\tfrac12G(e,c*d;a,b)-\tfrac32H(a,b;e;c,d).
\end{aligned}\tag{8}$$

For example, the odd-primary step is

<b,B(a,e)_(3)c_(0)d>=-T_b(a,e;c,d)+(3/2)G(a,e;b,c*d).

Expanding the products verifies that (5) satisfies (8). Subtract it from an unknown T. The homogeneous relation says that the remainder changes sign upon exchanging the singled-out e with b. Combined with antisymmetry in each pair and symmetry between the two pairs, these transpositions generate complete alternation in all five inputs. Hence the sole remaining tensor type is an alternating five-form. With five independent labels the elementary linear system has rank14 on its15 canonical pair-partition entries; the symbolic check verifies this, but the generating-transposition argument proves it in arbitrary dimension.

The full alternation of t is zero. On the other hand the source word in Omega equals the alternation of N_c(b,a;d,e). Equation (7)'s tree corrections vanish under alternation. Moving the third input to the final slot is even and reversing the first pair is odd. Consequently Omega=-Alt T, proving the minus sign in (6). This establishes the full expression, not just its value on repeated or decomposable input pairs.

## 4. Primary-only operator form

Return to c=24 and note12's primary product mu on P=P2. In an orthonormal real primary basis let C_eij=<e,mu(e_i,e_j)> and

$$F(X)=\sum_iL_iXL_i,\quad
\mathcal D_e(X)=L_eX+XL_e,\quad
\mathcal F_e(X)=\sum_{ij}C_{eij}L_iXL_j,$$

all restricted to skew matrices under the unit exterior/Frobenius identification. The actual five-label operator built from the trees is

$$\boxed{\mathcal A_e=F\mathcal D_e+\mathcal D_eF+\tfrac13\mathcal D_e-\mathcal F_e,
\qquad t_e=\tfrac12\mathcal A_e.}\tag{9}$$

To check the stress coefficient, use the full block multiplication

R_e=[[0,s e^T],[s e,L_e]], with s^2=1/3.

The pair Gram is G=F+s^2I. In (5), the four terms where e acts on an external leg combine to G D_e+D_e G. The two central-leg terms subtract the kernel

<a*c,e*(b*d)>-<a*d,e*(b*c)>,

whose primary operator is F_e+s^2D_e. The result is exactly (9). Every operator in (9) is self-adjoint on the real exterior space. The real five-form defines a self-adjoint Omega_e there because exchange of two pairs is even. Thus (6) becomes T_e=A_e/2-Omega_e.

All quantities in (9) have at most cubic degree in the unknown C. This is not a representation action inferred from a Monster decomposition.

## 5. Use the FULL fifth-trace relation and isolate quotient consistency

For x=a wedge b, the full commutator [R_a,R_b] kills the stress direction and restricts on P to the skew matrix sqrt(2)Gx. This follows directly from the symmetric cubic and the stress block. In the normalized exterior metric,

$$\operatorname{Tr}R_e[R_a,R_b][R_c,R_d]
=-\langle x,G\mathcal D_eG y\rangle.\tag{10}$$

Antisymmetrize (3) in (a,b) and (c,d), with e in the first trace slot. Its totally symmetric metric-cubic term vanishes. The tree terms become -104t_e=-52A_e, while the quinary term becomes208Omega_e. The coefficient identity is checked symbolically for all15 distinct five-leaf tree contractions, not numerically fitted to a group tensor. Hence

-G D_e G=-52A_e+208Omega_e.

Combining with (6) gives (1).

Since Bx=0 for x in ker G, the genuine mixed form has T_e=Pi T_e Pi. The second term of (1) is already supported on Pi, so

T_e=Pi T_e Pi iff A_e=Pi A_e Pi.

As G=282Pi, this is exactly (2). Its highest degree is five: G is quadratic plus a constant and A_e is cubic plus a linear term. The two displayed sides are adjoints, so either suffices for real e once all stated Hermitian conventions hold.

When (2) holds, J_B=B/sqrt(282) identifies im Pi isometrically with P3. The compressed physical action pulled back by this identification is

$$J_B^\dagger(\pi_3e_{(1)}\pi_3)J_B
=\frac{\mathcal A_e}{1128}+\frac{141}{104}\Pi\mathcal D_e\Pi.\tag{11}$$

This is a statement about normalized three-point couplings involving two weight-three primaries and one weight-two primary. It is not a claim that the primary subspace is invariant under e_(1), or that the displayed compression gives the complete energy splitting of the entire degenerate V3 level.

## 6. What is and is not a new selection restriction

Equations (4), (6), and (1) remove a possible false freedom: the alternating five-form cannot be chosen independently once the candidate obeys the extremal fifth-trace formula. The mixed action is then determined by the original cubic, up to the already known orthogonal choice of basis for P3.

Equation (2) is an explicit necessary condition that a candidate can be tested against. However, deriving it from an actual VOA does not show that it is independent of the algebraic identities already obtained from source theorems. In particular, the full fifth-trace identity itself imposes non-alternating constraints on Tr R1...R5. Only its alternating part fixes Omega. We have not shown whether its remaining components already imply (2), nor whether lower-order identities alone imply it. No novel polynomial classification theorem, full Monster selection or alternative CFT is claimed.

A small control shows why one cannot skip this logical question. In the even subalgebra of three free bosons, P2 has a rational orthogonal basis of five primaries. Its exterior Gram is a scaled rank-three projector G^2=5G, with a seven-dimensional kernel. The actual mixed action respects that kernel. But the tree part A_e alone does not: for the first diagonal field the residual (I-G/5)A_e has rank6 and an entry -12/5. Its nonzero quinary form cancels the obstruction in (6). The same example has Omega=3 and Alt Tr R^5=7/2 in the recorded basis, so the extremal relation Alt Tr R^5=52Omega is false there. Thus it is NOT a counterexample to (2) in the physical-selection class. It is a control against inferring the exceptional result from positivity, a pair projector, or generic VOA consistency alone.

The next deliverable is a finite symbolic implication calculation for (2), not another higher-weight four-point coefficient. Reduce G A_e-282A_e using the explicit quartic and fifth-trace relations, preserving external labels and normalized alternation. A derivation of redundancy is as informative as a genuinely independent residual. A failed symbolic simplification or an arbitrary small tensor is not proof of independence from the full system.

## 7. Bounded check of the preceding closure result and integration

Before this continuation, PR11 was still open. Its mode expansion and six-operator joint-diagonalization argument were reconstructed at the level needed here. No additional unproved equality of embedded projectors is needed for its stated conditional Gram-positivity comparison: Virasoro descendant subtraction is scalar on each primary multiplicity space, so it preserves the fixed six-sector operator algebra. The known unitary realization proves nonnegativity of its scalar coefficients, not equality of candidate component correlators. This scoped check does not audit every VOA analytic convergence or source-theorem input; it supports only the conditional statement actually used.

PR11 was merged at base09e3f98. The retained actual logs for workflow36115164030/job108007422695 have recognized strict average-toy replay failures on BOTH trees. Both separate unchanged bounded-portability comparisons pass with all_reports_byte_identical=false. Its65-check exact report passes. The merge message records these outcomes, rather than calling the overall green job a strict replay pass.

## 8. Verification and preservation

The new checker has **62 labelled exact checks** under normal/-O/-OO. It evaluates3157 five-label mixed entries and3157 raw-word descendant corrections in even two-/three-boson controls, plus all relevant quotient tests. The three-boson five-form is evaluated by its original120-term mode definition and independently through the primary-subtracted mixed form. Full multiplication matrices give a separate alternating trace check. Formal fifteen-tree calculations verify the -104 and208 coefficients and the rank14 ambiguity. Operator reconstruction in nonunit rational bases checks every stress correction and dual-metric weight.

Largest square matrix:10x10; largest symbolic coefficient system:121x15; oscillator cutoff:weight4. Arithmetic is integers/fractions only. The small examples are not holomorphic c24 minimizers. No full extremal cubic, Monster data, infinite OPE system or source theorem is verified. The block-algebra quotient control is labelled as such, not a VOA example. The prior oscillator helper is loaded privately and hash-checked; its file and standalone historical outputs are unchanged.

Runtime network cloning and raw download attempts failed. Local execution of these checks is not a live-main root replay. Actual pinned-baseline/candidate verification is delegated to the read-only workflow and its outcomes must be inspected before integration. No old report or tolerance is regenerated. Notes01-14, previous code/results/audits/ledgers, archives, license and verification policies remain intact. No manuscript, release or outreach is performed.

## Primary sources and inspected passages

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1; CMP224(2001),565-591. Section1 mode conventions; equation(2.2); Theorem2.1(5); section2.2; Corollary4.1 and Remark4.3 were read. Printed pages7,9,16 were visually inspected successfully. Screenshot of printed page17 failed; its Remark4.3 was read in parsed text. This directly supplies the coefficient52 and symmetry-free applicability, not a new project trace theorem.
https://arxiv.org/abs/math/0007169

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. Theorem3.1 and the trace-hypothesis replacement remain prior dependencies from note12; they are not reproved here.
https://arxiv.org/abs/math/0701626

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1; J.Algebra397(2014),252-277. Positive Hermitian/PCT invariance in Definitions2.1-2.2 supplies the adjoint convention; the relevant parsed definition was checked. No fresh complete proof audit is claimed.
https://arxiv.org/abs/1308.2361

[T] M.P. Tuite, *Exceptional Vertex Operator Algebras and the Virasoro Algebra*, arXiv:0811.4523v1, section3/Theorems3.3-3.4. Prior-generation context was checked; no new generation novelty is asserted. This source is not used to prove (1) or independence of (2).
https://arxiv.org/abs/0811.4523

These scoped reads and derivations do not establish comprehensive priority clearance or independent specialist/formal review. No downloaded papers are bundled.
