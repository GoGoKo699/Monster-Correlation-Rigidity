# The uncontracted mixed-action condition is already forced

**Date:** 26 September 2026. **Read base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Intended additive branch:** `research/operator-factorization-closure`.

## 1. Result: settle the outstanding implication, rather than add another moment

The six-label operator condition introduced in Note18 is a consequence of the earlier real cubic trace identities through order five and the positive metric. It is **not an independent selection condition** on admissible physical interaction tensors. This answers the implication question left unresolved in Notes18–23. It does not classify the tensors or select the Monster uniquely.

The simplification is to calculate one positive squared mismatch instead of comparing every matrix entry. After rescaling three six-index tensors, their exact Gram matrix is a positive scalar times

$$
\begin{pmatrix}
17069&221&17290\\
221&349&570\\
17290&570&17860
\end{pmatrix}.
$$

Its third row is the sum of its first two, so the squared norm of the first tensor plus the second minus the third is zero. Positive definiteness of the real tensor inner product makes the tensors equal. The nonzero two-by-two minor is 5908240, so this is their only linear relation up to scale.

The Gram calculation is a finite exact contraction certificate, not a numerical evaluation of a known Monster tensor. Three scalar contractions, fixed by three instances of the non-alternating fifth trace, finish the reduction. Their coefficient matrix has determinant 11/18. The entire reduction record is emitted by the checker.

No value of the disputed coefficient of the alternating five-form is used: that term is eliminated before the calculation starts. No additional weight-nine Ward identity, canonical thermal field, state-readout theorem or pure-state witness is an input to this implication proof.

The conclusion is for **real symmetric cubics in a positive Euclidean space**. The argument is a positive sum-of-squares implication, not a claim of membership in the ordinary complex polynomial ideal. Over an indefinite or complex bilinear metric a zero square would not suffice.

## 2. Physical question and precise algebraic premises

The owner seeks a physical reason for the Monster's exceptional role, not recognition of an imposed symmetry. The ongoing admissible class is nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs, with no weight-one currents, minimizing positive central charge. These are declared restrictions and an extremality criterion, not universal physical necessities or a demonstrated RG mechanism. Prior modular/design results give c=24 and the lower trace inputs used here, without assuming a Monster action [H, M].

The theorem itself is algebraic. Let C be a real fully symmetric cubic on V=R^d with its positive inner product. Put (L_a)_{ij}=C(a,e_i,e_j), mu(a,b)=L_a b, and

$$d=196883,\quad\kappa=13858/3,\quad\nu=899.$$

Assume the following identities for all external vectors:

$$\operatorname{tr}L_a=0,\qquad
\operatorname{tr}(L_aL_b)=\kappa\langle a,b\rangle,\qquad
\operatorname{tr}(L_aL_bL_c)=\nu C(a,b,c).\tag{A1--A3}$$

The fourth trace is

$$\begin{aligned}
\operatorname{tr}(L_aL_bL_cL_e)={}&\alpha\bigl(\langle\mu(a,b),\mu(c,e)\rangle+
\langle\mu(a,e),\mu(b,c)\rangle\bigr)\\
&+\beta\langle\mu(a,c),\mu(b,e)\rangle\\
&+u\bigl(\langle a,b\rangle\langle c,e\rangle+
\langle a,e\rangle\langle b,c\rangle\bigr)
+v\langle a,c\rangle\langle b,e\rangle,
\end{aligned}\tag{A4}$$

where (alpha,beta,u,v)=(496/3,-116,965/9,40/3). These are the primary-projected coefficients in main Note02, rather than the full V2 constants.

For five vectors define primary-only trees

$$H(a,b;c;d,e)=\langle\mu(a,b),\mu(c,\mu(d,e))\rangle,$$

$$T_1=\operatorname{Cyc}H(1,2;3;4,5),\quad
T_2=\operatorname{Cyc}H(1,4;3;2,5),\quad
T_3=\operatorname{Cyc}H(1,5;3;2,4),$$

$$M_a=\operatorname{Cyc}\langle1,2\rangle C(3,4,5),\qquad
M_n=\operatorname{Cyc}\langle1,3\rangle C(2,4,5).$$

Cyc is the sum of five rotations, not their average. Alt5 is the normalized signed average over all120 permutations. The fifth input is only

$$\boxed{\operatorname{tr}(L_1L_2L_3L_4L_5)
-\operatorname{Alt}_5\operatorname{tr}(L_1L_2L_3L_4L_5)
=\frac{89}{3}T_1+4T_2-22T_3+\frac{185}{9}M_a+\frac{10}{3}M_n.}\tag{A5}$$

This is an explicit polynomial identity in C. It contains no unspecified alternating tensor. The known existence of an admissible cubic is not established by the checker; it is supplied by the known moonshine theory and the source framework. Small controls below do not pretend to satisfy these exceptional numerical premises.

## 3. Why A5 is independent of the five-form normalization dispute

For the full weight-two algebra write R_a as the block matrix

$$R_a=\begin{pmatrix}0&s a^T\\s a&L_a\end{pmatrix},\qquad s^2=\gamma=1/3.$$

Let the full-product trees be denoted by a superscript full. Direct block multiplication and scalar-direction separation give

$$T_1^{\rm full}=T_1+2\gamma M_a,\quad
T_2^{\rm full}=T_2+2\gamma M_n,\quad
T_3^{\rm full}=T_3+\gamma(M_a+M_n),$$

$$\operatorname{tr}(R_1\cdots R_5)-\operatorname{tr}(L_1\cdots L_5)
=\gamma T_1+\gamma^2M_a.\tag{1}$$

The full non-alternating fifth-trace coefficients are (30,4,-22,8,8) [M, Corollary4.1]. The separate coefficient r multiplying its alternating five-form is immaterial: taking Alt5 and subtracting removes r times that form for **any** convention. Each tree or metric-times-cubic structure has zero total alternation because it has a symmetric pair.

After (1), the projected coefficients are

$$(30-\gamma,\ 4,\ -22,\ 8+38\gamma-\gamma^2,\ 8-14\gamma),$$

which at gamma=1/3 give A5. Thus neither choosing26 nor choosing52 is part of this proof. This does not rehabilitate PR12's false condition; it uses the safe portion of the trace identity that never involved that convention.

The checker independently verifies all the scalar-block subtraction formulas using ordinary block matrices for arbitrary small symmetric cubics at three rational values of s. These controls test the conversion, not the exceptional trace theorem itself. Its fifth-form alternation check uses five independent external labels and all120 permutations.

## 4. The operator condition to be proved

Identify a wedge b with ab^T-ba^T and use half the Frobenius product on skew matrices. Define

$$F(X)=\sum_iL_iXL_i,\quad G=F_-+I/3,\quad
\mathcal D_a(X)=L_aX+XL_a.$$

A1--A4 imply G^2=282G, so G=282Pi for an orthogonal projector Pi. For

$$x=\sum_{a<b}x_{ab}e_a\wedge e_b,$$

put

$$\mathcal Q_x=\sum_{a<b}x_{ab}
(\mathcal D_aG\mathcal D_b-\mathcal D_bG\mathcal D_a),
\qquad \operatorname{ad}_x(Y)=xY-Yx.$$

All these act on the real exterior space. The target is

$$\boxed{G\bigl(9\mathcal Q_x+24336\operatorname{ad}_x
-2704\operatorname{ad}_{Gx}\bigr)G=0\quad\text{for every }x.}\tag{2}$$

The statement with Pi in place of the two outside factors is equivalent. It is exactly the uncontracted condition of Note18, not merely its trace. In particular x in ker G gives the null-state requirement. No rank assumptions on individual x are imposed.

## 5. The positive-norm proof

For x=a wedge b, y=c wedge d and z=e wedge f, define three real six-linear tensors

$$\begin{aligned}
A(a,b,c,d,e,f)&=\frac9{2704}\langle Gz,\mathcal Q_xGy\rangle_-,\\
B(a,b,c,d,e,f)&=9\langle Gz,\operatorname{ad}_xGy\rangle_-,\\
C_0(a,b,c,d,e,f)&=\langle Gz,\operatorname{ad}_{Gx}Gy\rangle_-.
\end{aligned}\tag{3}$$

Their ordinary Euclidean tensor inner product sums over **six ordered basis indices**. Each is alternating within each pair and under interchange of the last two pairs. This permits a16-term signed symmetry reduction; the checker verifies that its expanded boundary projection leaves the tensors unchanged.

The exact contraction certificate in the next section yields

$$\operatorname{Gram}(A,B,C_0)=K
\begin{pmatrix}
17069&221&17290\\
221&349&570\\
17290&570&17860
\end{pmatrix},\quad
K=107700439863024387072>0.\tag{4}$$

Consequently

$$\|A+B-C_0\|^2=0.$$

The metric is positive and the tensors are real, so A+B=C0 component by component. Multiply by2704 and use that decomposable exterior vectors span wedge^2 V. This proves (2) for all x and all matrix elements.

The leading two-by-two minor of the displayed integer matrix is5908240>0. Thus A and B are linearly independent and C0=A+B is the unique linear relation among these three tensors, up to overall scale. This uniqueness is limited to this specified three-dimensional ansatz. It does not classify all multilinear identities or the cubic itself.

The proof is not the assertion that a small set of physical examples has zero residual. It calculates the universal norm from A1--A5 and then uses positivity. It proves implication on the physical real solution set; it does not exhibit a polynomial ideal-membership certificate over an arbitrary complex field.

## 6. Exact contraction certificate for equation (4)

A graph represents an Einstein contraction of copies of the fully symmetric cubic C. Every internal vertex has degree three; an edge contracts two indices; six labelled one-valent boundaries represent the six external fields. Closed graphs are scalars. An isolated contracted delta loop contributes d. Dummy-index graph isomorphisms are only a notation reduction, not additional algebraic hypotheses.

A1 deletes a self-trace loop. A2 collapses a two-edge loop with factor kappa; A3 collapses a triangle with factor nu. A4 replaces a square by its three two-vertex pairings and three delta pairings, with the coefficients displayed in A4. These rules strictly reduce the number of cubic vertices. The complete emitted certificate records every local replacement, with the selected cycle and exact coefficients.

After expanding the norms of (3), these reductions leave only the empty contraction and three closed cubic graphs, denoted P,A12,B12. Their edge lists are below; graph vertices are numbered from0, and have nothing to do with group elements.

```
P (10 vertices):
01 02 03 14 15 26 27 38 39 46 48 57 59 69 78

A12 (12 vertices):
01 02 03 14 15 26 27 38 39 46 48 57 59 (6,10) (7,11)
(8,11) (9,10) (10,11)

B12 (12 vertices):
01 02 03 14 15 26 28 37 39 46 (4,11) 57 (5,10) (6,10)
(7,11) 89 (8,11) (9,10)
```

Apply A5 to the pentagon (0,1,4,6,2) in each graph. Normalized alternating traces can be expanded over12 representatives of S5/D5, because trace is cyclic and reversal-invariant for real symmetric matrices and reversal of five labels is even. Reduce the resulting short cycles by A1--A4. The three equations, with their constants retained, are

$$\frac{11}{12}P+\frac{214927328638240223720}{243}=0,$$

$$\frac{155}{9}P+\frac56A12+\frac16B12
-\frac{497099520224112030008927}{729}=0,$$

$$-\frac{224}{9}P+\frac16A12+\frac56B12
+\frac{1881408102488381175074405}{729}=0.\tag{5}$$

The coefficient matrix has determinant11/18, so the values are fixed:

$$P=-\frac{78155392232087354080}{81},\quad
A12=\frac{370415245037399715987080}{243},\quad
B12=-\frac{833649013146827440152746}{243}.$$

These signed contractions are not themselves squared norms; their negative values do not violate positivity.

For a shorter check of the final cancellation, the unscaled residual in (2), paired with exterior inputs as above, has squared norm

$$\begin{aligned}
&922900921397634135853733913856
+60784328448P\\
&\hspace{12mm}-103063104A12+206126208B12=0.\tag{6}
\end{aligned}$$

The stronger full Gram result (4), not just this one zero, is emitted by the same reduction. The report includes the original boundary tensor expansions, every raw scalar Gram polynomial, its short-cycle reduction, the three fifth-trace contexts and the136 local short-cycle replacements. No unreduced invariant is assigned a value by comparison with the desired answer. The only numerical inputs are d and A1--A5.

The largest symbolic graph has16 cubic vertices. This is a bound on the complexity of an index-contraction proof, not a16-dimensional physical model. The actual field space stays symbolic throughout.

## 7. Physical interpretation: the two routes already agree

For the previously established onto map B from exterior pairs to weight-three primaries, G=B^dagger B=282Pi. The corrected mixed action reads

$$H_a\simeq\frac{282}{104}\Pi\mathcal D_a\Pi.$$

Using the normalized descendant identification L_-1/2, the primary compression of the full mode commutator includes the excursion term

$$\pi_3 B(a,b)_{(2)}\pi_3
=[H_a,H_b]+\frac14(b_ab_b^\dagger-b_bb_a^\dagger),\qquad b_a(v)=B(a,v).\tag{7}$$

The separately reconstructed primary3,3,3 law gives

$$B^\dagger K_{Bz}B=\frac1{36}G\operatorname{ad}_{Gz}G.$$

Substitution of the two actions into (7) produced the proposed extra condition (2). The present result proves that it is already forced by the preceding trace system. Every real positive candidate satisfying A1--A5 passes this particular compatibility test. It cannot eliminate additional candidates or be counted as independent evidence of unique physical selection.

The physical action formulas retain their previously recorded source and normalization obligations. The new pure-algebra implication does not depend on accepting their derivations: it proves exactly the displayed equation from A1--A5. It also does not extend a primary-projected commutator into a Lie algebra or justify imposing Jacobi on the truncated primary product.

An apparently new uncontracted restriction has therefore collapsed to a positive norm identity. The remaining selection problem is not an ever-growing list of variants of (2): it is whether the real positive cubic solutions of the original trace system are unique up to field-basis change, or which genuinely independent higher OPE information distinguishes them. This note constructs no competing solution and supplies no classification theorem.

## 8. Tests, preservation and limits

The checker has95 labelled exact checks. It recomputes the certificate rather than loading the3x3 Gram as a premise. It independently evaluates the original tensor contractions on arbitrary small cubics by two routes: direct matrix actions and dense Einstein contractions with a separate contraction order. These agree on all six independent Gram entries in dimensions2 and3. The dimension-three control does NOT obey the desired operator law, as expected because it does not satisfy A1--A5. In dimension two the exterior space is one-dimensional and its skew action vanishes identically; this is a boundary control, not a physical countermodel.

Separate generic block-matrix controls at dimension six verify full-to-primary fifth-trace subtraction for three scalar couplings, and all120 permutations check the vanishing alternating part of its tree RHS. All tests use integers and fractions, including NumPy object-array contractions. There is no floating tolerance. Largest explicit square matrix:6x6. Largest numerical tensor:729 entries. No Monster character data, representation, or full extremal tensor is constructed.

A symbolic contraction proof implemented in ordinary Python is not proof-assistant formal verification, an independent specialist review, or comprehensive priority clearance. The source trace theorems remain inputs. The complete certificate is intended to make a fresh mathematical and code audit possible rather than replace it. Its use of a positive metric is essential and openly stated.

The supplied preceding pure-state checkpoint was preserved and replayed: all13 payload hashes and all119 checks under normal/-O/-OO agree. The present proof does not need the state-readout result. The historical main, all pending branches and old evidence are to be preserved. Runtime Git networking failed at DNS resolution; local new checks are not a local checkout/replay of live main. Any remote verification outcome is recorded separately only after actual execution and log inspection. No archived report or tolerance may be changed to conceal a mismatch.

No manuscript, release, outreach, physical implementation, efficient algorithm, new general trace theorem, independent selection axiom, or moonshine uniqueness is claimed.

## Primary sources and read depth

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1, Corollary4.1, Note4.2 and Remark4.3. Printed page16 was visually inspected in this continuation; Remark4.3's extension to rational holomorphic c24 theories with the stated shape was read in parsed text. The lower trace formulas and the NON-ALTERNATING fifth identity are used. The disputed numerical coefficient of the five-form is eliminated, not adopted. The entire underlying Casimir proof is not independently rederived here.
https://arxiv.org/abs/math/0007169

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. The project inherits Theorem3.1 and the design-to-trace replacement recorded in Note12. This source remains the reason the trace system is applicable without assuming a Monster action, not a theorem proved by this graph calculation.
https://arxiv.org/abs/math/0701626

Project inputs: main Note02, section3.1 for the projected fourth trace; Note12 for the physical-source interface; pending Note18 at commit9254b954ed7e3d1fb2033175e66552fdf0092823 for the exact unresolved equation; the supplied fifth-trace reconstruction for an independent audit of the non-alternating coefficients. No complete original Norton1996 chapter was obtained or reviewed in this continuation. A scoped search is not a novelty certificate. No downloaded paper or font is bundled.
