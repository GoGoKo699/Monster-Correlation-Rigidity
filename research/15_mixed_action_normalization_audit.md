# A null-state audit blocks the proposed mixed-interaction selection condition

**Date:** 25 September 2026. **Base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `audit/mixed-normalization`. Audited pending work: PR12, head
`b0d7224bbc20d0d8aeb217e1caf4014fd3c298d1`, file
`research/15_mixed_action_and_null_relations.md`. That candidate was not merged.
Its branch and evidence are preserved; this is a separate audit from live main.

## 1. Outcome and physical significance

**ERROR in the proposed new selection condition.** The pending quintic null
relation rejects a concrete subspace of the actual Griess algebra. It is not
an additional necessary condition for the physical-selection class. The failure
can be exposed by five symmetric matrices supported on only three coordinates,
without constructing a Monster group element or a large multiplication matrix.

The physical check is elementary: a pair that creates the zero state must have
zero matrix elements against every observable. The pending mixed-action formula
assigns such a pair a nonzero element, 24 in the explicit normalization below.
The true value is zero. This falsifies that proposed formula and the inferred
extra constraint; it does not falsify the known moonshine CFT, the physical
selection assumptions, or the earlier weight-three and weight-four results.

The discrepancy is localized to a five-form normalization. The retrieved
Matsuo arXiv v1 defines a normalized 120-term alternating mode expression and
prints a coefficient 52 multiplying it. Independent mode and full Griess-block
calculations instead require coefficient **26** for the tested trace-polynomial
shape. The appendix has a further inconsistent literal specialization. These
are actual displayed source values, not an OCR-only suspicion. The journal
version was not available to this audit, so no claim is made about whether its
normalization was corrected.

**Conditional repair, not a rederived universal trace theorem.** Keeping the
standard trace-polynomial shape with coefficient 26 makes the mixed action
`G D_e G / 104`, which is automatically supported on the physical quotient.
This explains exactly why the apparent extra null condition disappears. The
all-input fifth-trace theorem has not been independently reconstructed here;
that universal replacement remains conditional pending source/Casimir
reconciliation. The finite contradiction to PR12's claimed necessity does not
depend on proving the replacement universally.

## 2. The candidate under audit

From note13, on the primary weight-two space P2, set

$$B(a,b)=a_{(0)}b-\tfrac12L_{-1}(a*b),\qquad
G=B^\dagger B=F_-+\tfrac13 I=282\Pi.$$

The full weight-two product `*` contains the stress direction; mu is its
primary projection. Exterior vectors use
`a wedge b <-> (ab^T-ba^T)/sqrt(2)`. For a primary e put

$$T_e(x,y)=\langle Bx,e_{(1)}By\rangle,\quad
\mathcal D_e(X)=L_eX+XL_e,\quad
\mathcal F_e(X)=\sum_{ij}C_{eij}L_iXL_j,$$

$$\mathcal A_e=F\mathcal D_e+\mathcal D_eF+\tfrac13\mathcal D_e-\mathcal F_e.$$

PR12 proposes

$$T_e=\tfrac14\mathcal A_e+\tfrac1{208}G\mathcal D_eG,\tag{P1}$$

and from zero-state consistency infers

$$G\mathcal A_e=282\mathcal A_e=\mathcal A_eG.\tag{P2}$$

The true elementary condition `T_e=Pi T_e Pi` is not in question. The issue is
whether (P1) is the correct expression for T_e. A failed (P2) cannot be repaired
by manually projecting A_e: that would replace, rather than validate, the
proposed interaction. It also cannot be used to exclude the known theory.

For reference, define the full-product tree

$$H(a,b;e;c,d)=\langle a*b,e*(c*d)\rangle.$$

The generic ten-tree part t, as used in PR12, is

$$\begin{aligned}
2t_e(a,b;c,d)={}&-H(b,c;a;d,e)+H(b,d;a;c,e)
+H(a,c;b;d,e)-H(a,d;b;c,e)\\
&-H(a,d;c;b,e)+H(a,e;c;b,d)
+H(a,c;d;b,e)-H(a,e;d;b,c)\\
&-H(a,c;e;b,d)+H(a,d;e;b,c).
\end{aligned}\tag{1}$$

It has `2t_e=A_e` in the stated primary normalization. The generic mode
expression is `T_e=t_e-Omega_e`, where

$$\Omega(a,b,c,d,e)=\frac1{120}\sum_{p\in S_5}\operatorname{sgn}(p)
\,[a_{p1,(3)}a_{p2,(2)}a_{p3,(1)}a_{p4,(0)}a_{p5}]_{\mathbf1}.\tag{2}$$

Our independent oscillator calculation checks this generic relation on all
120 permutations of the chosen fields. It does not infer the normalization of
Omega from a trace formula; it evaluates the original mode word directly.

## 3. A counterexample inside the known theory, not a competing toy CFT

Use Seysen's A block of symmetric 24 by 24 matrices [S, section10.1]. In the
VOA normalization compatible with notes07,12,13,

$$A*B=2(AB+BA),\qquad \langle A,B\rangle=2\operatorname{Tr}(AB),
\qquad\omega=I_{24}/2.$$

Thus the unit is I/4, its squared norm is 3, and `||omega||^2=12`, as required
at central charge24. In the even Heisenberg subalgebra, a source matrix A is
represented by

$$a_A=\sum_{ij}A_{ij}h_i(-1)h_j(-1)\mathbf1.$$

Wick contraction gives exactly the product and metric above. This is twice the
matrix argument of the frequently used state `(1/2)sum A_ij h_i h_j`. Failure to
track that factor rescales a five-linear expression by32. The even
Heisenberg algebra sits in `V_Lambda^+`, hence in the moonshine extension
`V_Lambda^+ + V_Lambda^{T,+}`; [ALY] records that extension. The first three
coordinates below are active and the other21 are spectators. Evaluating their
modes in a three-boson Fock calculation is exact for these fields; it does not
pretend that a standalone c=3 theory is an extremal c=24 candidate.

Embed the following trace-zero matrices in the first three coordinates:

$$
a=\operatorname{diag}(1,-1,0),\quad
b=\operatorname{diag}(1,0,-1),\quad
c=E_{01}+E_{10},\quad d=E_{02}+E_{20},\quad e=E_{12}+E_{21}.\tag{3}
$$

Because a and b commute, the note13 Gram gives

$$\|B(a,b)\|^2
=\langle a*a,b*b\rangle-\|a*b\|^2
=32\operatorname{Tr}(a^2b^2)-32\operatorname{Tr}(a^2b^2)=0.$$

Positivity implies `B(a,b)=0`. The same conclusion follows directly from the
oscillators, in which B is proportional to the matrix commutator. Therefore

$$T_e(a\wedge b,c\wedge d)=0.\tag{4}$$

There is also a full-algebra check of `G(a wedge b)=0`. For a traceless A,
Seysen's multiplication operator is block diagonal:

- on Sym24, `X -> 2(AX+XA)`;
- on the 98280-dimensional X block, diagonal entries `lambda_r^T A lambda_r`;
- on the Q block, `I_4096 tensor A`.

The a,b operators commute in all three blocks. Their full commutator kills
both the stress and primary spaces. The general identity
`[R_a,R_b]|P2=sqrt(2)G(a wedge b)` therefore independently gives a zero column
of G. No eigenvalue-fitting or incomplete search over the large algebra is
used in this argument.

In contrast, direct substitution of (3) into (1) gives

$$2t_e(a,b;c,d)=96,\qquad t_e=48,\qquad
\langle a\wedge b,\mathcal A_e(c\wedge d)\rangle=96.\tag{5}$$

For transparency, the ten signed contributions to `2t_e` are
`0,0,0,0,32,0,0,32,0,32`. Since x=a wedge b is in kerG, any supported operator
`Pi A_e Pi` must have zero matrix element in this row. Equation(5) proves that
(P2) fails. Equation(P1) would assign this row the value96/4=24, contradicting
(4). This is a decisive counterexample to the proposed *necessary* selection
condition using the very theory it was intended to select.

This use of the known algebra is a falsification control, not an assumption
that an unknown physically admissible theory already has that algebra.

## 4. Independent full-trace normalization

We evaluate traces over all196884 dimensions by exact small blocks, rather than
replacing the full trace by a three-coordinate trace. Let J_A act by AX+XA on
Sym3. For five fields supported on those coordinates,

$$\operatorname{Tr}_{\mathrm{Sym24}}R_1\cdots R_5
=32\left(\operatorname{Tr}_{\mathrm{Sym3}}J_1\cdots J_5
+21\operatorname{Tr}_{\mathbb R^3}A_1\cdots A_5\right).\tag{6}$$

The 21 cross-coordinate three-dimensional blocks give the second term. The
remaining Sym21 block is killed by all these operators. The Q block contributes
`4096 Tr_3(A_1...A_5)`. The X block contributes
`sum_r product_i (lambda_r^T A_i lambda_r)`. All98280 labels are accounted for.

Normalized alternation over (3) gives

$$\operatorname{AltTr}_{3}(abcde)=\tfrac14,\quad
\operatorname{AltTr}_{\mathrm{Sym3}}(J_aJ_bJ_cJ_dJ_e)=\tfrac74.$$

The X contribution is symmetric in the five arguments, hence has zero
alternation. Consequently

$$\boxed{\operatorname{AltTr}_{V_2}R_aR_bR_cR_dR_e
=32(7/4+21/4)+4096/4=1248.}\tag{7}$$

The original120-term mode definition(2), evaluated without any trace formula,
gives

$$\boxed{\Omega(a,b,c,d,e)=48.}\tag{8}$$

Their ratio is26. The normalized mode form would have to be halved for a
coefficient52 to describe the same trace, and the generic formula `t-Omega`
would then have to become `t-2Omega`. One cannot change only one convention.

We also check the **un-alternated** trace, so the conclusion is not based on
throwing away the polynomial part. Write `P5` for the Corollary4.1 primary-input
polynomial with its `30 Cyc H + 4 Cyc H' -22 Cyc H'' +8 Sym Cg` terms. Streaming
the Leech rows yields X-trace288 for the product of the five distinct fields;
the shape contributions are0,0,288. For every permutation w of the five fields,

$$\operatorname{sgn}(w)
\left(\operatorname{Tr}_{V_2}R_{w1}\cdots R_{w5}-P5(w)\right)=1248.\tag{9}$$

For the ordering(a,b,c,d,e), for example, the A, Q and X contributions are64,
0 and288, so the total trace is352. The polynomial is-896. Its remainder is
1248=26*48, not52*48. All120 orderings satisfy the same normalized coefficient.
As safeguards against an overall product/metric error, the same block
construction passes25 second-trace,5 third-trace and6 fourth-trace controls
using the previously accepted constants4620,900,166,-116,52.

## 5. What the retrieved source actually says

Matsuo arXiv:math/0007169v1, equation(2.2), defines exactly the normalized
alternating mode form(2). Corollary4.1 prints `+52(a1,a2,a3,a4,a5)`. Both pages
were visually inspected in this continuation, so this conflict is not resolved
by blaming parsed-text loss. We do not claim an author-approved correction or
that the journal version has the same issue; only the retrieved version was
available in full.

A further internal check is the appendix coefficient H and denominator
D10(c). Their literal printed substitution at c=24, dimV2=196884 gives

$$H/D10=13/60,$$

not52. Multiplication by120 gives26, which is a useful normalization lead but
not a justified alteration of the printed theorem. The appendix H page was also
visually inspected. Other sampled appendix coefficients specialize to30,-22
and8 as in the corollary. The source-level reconciliation must keep normalized
versus unnormalized alternation explicit.

The universal trace formula shape may still be correct after numerical or
convention repair. Our exact witness determines the five-form coefficient
within that shape, but a single family of evaluations is not a reconstruction
of its general Casimir proof. **The corrected all-input theorem is left
unresolved here**, rather than promoting a likely correction into a new
physical-selection premise.

## 6. Coefficient-parametrized reduction: why the extra condition is spurious

Retain a symbolic coefficient h for the normalized mode form in the standard
fifth-trace polynomial. Double antisymmetrization in(a,b) and(c,d), with e in
the trace, gives

$$-G\mathcal D_eG=-104t_e+4h\Omega_e=-52\mathcal A_e+4h\Omega_e.$$

The coefficient calculation is exact in the15 five-leaf tree contractions and
10 metric-times-cubic contractions; the latter cancel. Combining this relation
with `T=t-Omega` gives, for nonzero h,

$$\boxed{T_e=\left(\tfrac12-\frac{13}{h}\right)\mathcal A_e
+\frac1{4h}G\mathcal D_eG.}\tag{10}$$

For h=52 this reproduces the rejected pending formula. For the only h compatible
with(3)-(9), h=26, it reduces to

$$\boxed{T_e=\frac1{104}G\mathcal D_eG.}\tag{11}
$$

Then the zero-state quotient is respected identically, without an additional
constraint on A_e. With `J_B=B/sqrt(282)`, the corresponding normalized primary
compression would be `(141/52)Pi D_e Pi`. Equation(11) and this compression are
**conditional on the reconciled universal fifth-trace relation**, not separately
proved universal formulas in this audit.

The result already suffices to answer the proposed implication task as posed:
it cannot establish new physical selection from(P2), because(P2) is false on
the target algebra. The apparent independent restriction came from incompatible
normalizations. We have not shown that all mixed interactions are redundant,
that the primary cubic is uniquely determined, or that the physical programme
cannot select the Monster. The earlier spectral and four-point questions are
not settled by this correction.

## 7. Evidence and reproducibility

`checks/verify_mixed_normalization.py` has37 labelled exact checks, using only
integer/fraction arithmetic. It verifies the unchanged hashes of the old
oscillator and Leech-label helpers. It evaluates the original mode alternation,
all120 mixed permutations of the witness, the full block-trace remainders,
lower-order normalization controls, and the symbolic coefficient reduction.
Matrices explicitly formed are at most6 by6. Leech rows are streamed one at a
time, with24 integer entries each; no196884-dimensional operator or full
Monster tensor/group representation is materialized. The Fock cutoff is4.

This is not a generic c=3 countermodel being mislabelled a c=24 minimizer:
the local mode calculation uses fields of the actual even Heisenberg
subalgebra, while the trace uses the actual full Griess A/X/Q blocks. It does
not construct every moonshine OPE or prove all imported source identifications.
The nonzero null-row obstruction is analytic as above, with arithmetic checks.

The new report is compared under normal Python,-O,-OO. The old root verifier,
archived reports and bounded-portability policy remain unchanged. Network
checkout was attempted but failed in this runtime, so new local checks are not
claimed as a local live-main root replay. Actual baseline/candidate root
outcomes must be read from the read-only CI logs. A green workflow alone is not
a strict-replay result. No source papers are redistributed.

PR12 remains unmerged with a blocking audit comment at its pinned head. Main's
notes01-14, previous scientific code/data/results/audits/ledgers, provenance and
MIT license are preserved. No manuscript, researcher outreach, large simulation,
independent specialist review or comprehensive novelty clearance is claimed.

## 8. Next bounded deliverable

Reconcile the universal normalized fifth trace from its Casimir/mode derivation
or a checked corrected primary text, using equations(3)-(9) as mandatory exact
regression tests. Establish the true all-input mixed action, not just a
coefficient fitted on one sector. Only then decide which mixed factorization
constraints remain independent. Do not continue a polynomial-ideal search
against(P2), manually project its residual away, or claim that the known CFT
violates positivity. Physical selection remains the objective; the correction
prevents an algebraic artefact from being mistaken for a physical principle.

## Sources and read depth

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex
Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Equation2.2,
Theorem2.1(5), Corollary4.1, equation1.14 and AppendixA.2 were read. Printed
pages7,16,26 were visually inspected. The attempted journal PDF URL redirected
to the article page; its full text and any correction were not checked.
https://arxiv.org/pdf/math/0007169
https://doi.org/10.1007/s00220-001-0565-3

[S] M. Seysen, *A computer-friendly construction of the monster*,
arXiv:2002.10921v5, section10.1, especially equations10.1.3,10.1.4,10.1.6 and
its list of zero block triples. Relevant parsed formulas read; the page33
screenshot failed. The earlier source-to-VOA conversion is independently
checked on the product, metric, identity and low-order traces here.
https://arxiv.org/pdf/2002.10921v5

[ALY] T. Abe, C. H. Lam and H. Yamada, *A remark on Z_p-orbifold constructions
of the Moonshine vertex operator algebra*, arXiv:1705.09022. Section4's
identification of `V^natural=V_Lambda^+ + V_Lambda^{T,+}` was read in parsed text.
This is used only to locate the even Heisenberg controls in the known theory,
not as a new uniqueness assumption for an arbitrary candidate. No full proof
audit of that source was performed.
https://arxiv.org/pdf/1705.09022

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361,
is the unchanged positive-Hermitian/Heisenberg convention dependency from
note13. That earlier source attribution is retained; no fresh whole-paper
proof audit is claimed.
