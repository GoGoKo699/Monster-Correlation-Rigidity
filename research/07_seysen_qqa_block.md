# A normalized, clean circuit for one Griess-isometry block

**Date:** 25 September 2026. **Base:** `ef7824945e92c12acc3652af21c5b617ce9ca8e8`.
**Branch:** `research/seysen-qqa-block`. The live branch and open-PR listings were read before work; no open PR was present.

This executes the bounded normalization/one-primitive assignment in the base work order. It constructs one block of the multiplication isometry, not a complete implementation of W or of the Monster test. The source block formulas are classical. Their circuit translation and the calculations here are project deductions; comprehensive priority and independent expert review are not established.

## 1. Result and precise domain

Write the source Euclidean representation as B_S = A direct-sum X direct-sum Q, with A the symmetric 24 by 24 matrices and Q = R^4096 tensor R^24. Let A_0 be the traceless symmetric matrices. In the normalized quantum-coordinate convention defined below,

$$V=A_0\oplus X\oplus Q,\qquad \dim A_0=299,\quad \dim X=98280,\quad \dim Q=98304.$$

For the project's normalized multiplication isometry W, and every A in A_0,

$$
(\Pi_Q\otimes\Pi_Q)W|A\rangle
=\sqrt{\frac{3072}{6929}}\,\mathcal V_Q|A\rangle,
$$

$$
\mathcal V_Q|A\rangle
=\frac1{64}\sum_{s=0}^{4095}\sum_{i,j=0}^{23}A_{ij}|s,i\rangle|s,j\rangle.
$$

Here the matrix-coordinate norm is Tr(A* A). The map V_Q is a genuine isometry: it is matrix vectorization and twelve Bell pairs, with tensor factors regrouped. Its clean elementary-gate circuit is supplied in [circuits/seysen_qqa.py](../circuits/seysen_qqa.py). It uses no measurement, postselection, amplification, quantum random-access memory, or oracle for arbitrary Monster matrices.

The squared output weights of W on this entire 299-dimensional input sector are

| Output sector | Squared weight for a normalized input in A_0 |
|---|---:|
| A_0 tensor A_0 | 77/6929 |
| X tensor X | 3780/6929 |
| Q tensor Q | 3072/6929 |

They sum to one. Only the normalized Q tensor Q branch is compiled here. Its weight is about 44.3354 percent **conditional on the input being in A_0**. A_0 is only 299/196883 of the full input dimension; this is not a claim to have compiled 44 percent of the entire W.

## 2. Source data, metric, and identity removal

Use [S], sections 6.1-6.2 and 10.1, with g_S the displayed Euclidean form and F_S the displayed symmetric trilinear form. On the symmetric-matrix part, g_S(A,B)=Tr(AB). An orthonormal basis consists of

$$D_i=E_{ii},\qquad F_{ij}=(E_{ij}+E_{ji})/\sqrt2\quad(i<j).$$

The source's off-diagonal basis vectors without the square root division are not unit computational vectors. On X and Q the source basis is orthonormal after choosing one of each equal/opposite pair. The source product star is defined by g_S(u star v,w)=F_S(u,v,w).

The three source restrictions containing an A argument are

$$F_S(A,B,C)=4\operatorname{Tr}(ABC),$$

$$F_S(X_r,X_r,A)=\lambda_r A\lambda_r^T,$$

$$F_S(q\otimes u,q'\otimes v,A)
=(q,q')\left[uAv^T+\tfrac18(u,v)\operatorname{Tr}A\right].$$

For distinct chosen X basis labels the middle restriction is zero. The last formula uses the natural real bilinear products before complexification. All computational norm statements use their Hermitian extensions. These are [S] equations (10.1.3), (10.1.4), and (10.1.6), not new algebra formulas. Short-vector coordinates in section 6 contain a factor 1/sqrt(8), so their **squared length** here is four.

### Identity

Put I = I_24 in A. Contraction of F_S with I acts as four times the metric on all three sectors: the A term is 4Tr(BC); the X term is ||lambda_r||^2=4; and the Q term is (24/8+1)(q,q')(u,v)=4(q,q')(u,v). Cross-sector terms vanish. Thus

$$e_S=I/4,\qquad g_S(e_S,e_S)=3/2,\qquad t_S=I/\sqrt{24},\qquad e_S=t_S/\sqrt{2/3}.$$

The orthogonal complement of the identity is precisely A_0 direct-sum X direct-sum Q. This is an exact subspace projection, not a coordinate dropped without changing the basis.

### Two equivalent normalization conventions

A convention compatible with the repository is to retain the source product on underlying algebra vectors and use g_VOA=2g_S. Then e_S has squared norm three, and a g_VOA-unit vector corresponding to a g_S-unit basis vector b is b/sqrt(2). Its cubic coefficient is

$$2F_S(b_a/\sqrt2,b_b/\sqrt2,b_c/\sqrt2)=F_S(b_a,b_b,b_c)/\sqrt2.$$

Equivalently, use the g_S-orthonormal basis as **computational coordinates**, divide the product and cubic by sqrt(2), and use the coordinate identity sqrt(2)e_S. In this convention the unit identity direction remains t_S and multiplication by it has coefficient 1/sqrt(3), exactly the repository's convention. These two descriptions must not be mixed: one rescales the metric on underlying vectors, the other rescales their coordinate product.

The unit norm alone would not establish equivalence of all traceless coefficients. Section 3 independently fixes their scale. More intrinsically, the source representation on V is the absolutely irreducible degree-196883 representation and its invariant cubic line is unique, as in the base character audit. An orthogonal intertwiner therefore identifies the nonzero restricted F_S with a scalar multiple of the project's cubic. Section 3 computes the magnitude of that scalar to be sqrt(2). Its remaining sign can be fixed by the orientation of the intertwiner; it has no effect on the projector WW*. No new proof of the Monster representation classification is claimed.

## 3. Independent contraction-normalization check

Let mu_S be the projected source product on V, and L^S_a its multiplication matrix. The contraction (mu_S)(mu_S)* commutes with the Monster action. Absolute irreducibility makes it a scalar kappa_S times the identity. It is enough to evaluate ||L^S_h||_F^2 on

$$h=(D_0-D_1)/\sqrt2.$$

Because a triple with one A argument is supported only on AAA, AXX, and AQQ, this multiplication matrix is block diagonal on A_0, X, Q.

### Symmetric-matrix block

On the full symmetric-matrix space,

$$R_h(B)=2(hB+Bh).$$

For a general real symmetric traceless A, diagonalizing A in the 24-dimensional coordinate space gives

$$\|R_A\|_F^2=16\sum_i a_i^2+4\sum_{i<j}(a_i+a_j)^2
=4(24+2)\|A\|_F^2=104\|A\|_F^2.$$

Removing the identity from both matrix indices removes two scalar-to-traceless entries of squared size 2/3 each. Hence

$$\|\Pi_{A_0}R_A\Pi_{A_0}\|_F^2=\frac{308}{3}\|A\|_F^2.$$

This subtraction is necessary; using 104 for the projected contribution gives the wrong normalization.

### X block: Leech fourth moments without a dense tensor

Section 6.2 of [S] indexes X by one vector from each antipodal short-vector pair. Its three shape counts are 552, 48576, and 49152. The 759 Golay octads have point incidence 253 and pair incidence 77. These incidence values also follow directly: minimum code distance eight makes two octads sharing five coordinates impossible, and 759 binomial(8,5)=binomial(24,5); thus the octads cover every five-subset exactly once, and double counting gives the two incidences.

For clarity, the resulting fourth moments, summed over the antipodal pairs, are

| Shape, in coordinates divided by sqrt(8) | Sum lambda_i^4 | Sum lambda_i^2 lambda_j^2, i != j |
|---|---:|---:|
| Two nonzero coordinates of magnitude 4 | 184 | 8 |
| Eight coordinates of magnitude 2 on an octad | 4048 | 1232 |
| One coordinate of magnitude 3, others of magnitude 1 | 3328 | 1280 |
| Total | 7560 | 2520 |

All fourth monomials with an odd coordinate exponent average to zero. For the first shape this follows from the independent signs. For the octad shape, even-parity signs on eight positions annihilate every nonconstant sign character involving at most four coordinates. For the last shape, self-duality and minimum distance eight of the Golay code annihilate such characters. Passing to antipodal pairs is legitimate for even-degree polynomials. This is a derivation of the needed moment, not an assumption of an unexplained spherical-design oracle.

Consequently, for every symmetric A,

$$\sum_r(\lambda_r A\lambda_r^T)^2
=2520\big[(\operatorname{Tr}A)^2+2\operatorname{Tr}(A^2)\big].$$

For traceless A this is 5040||A||_F^2. In particular h gives contributions 176+2816+2048=5040 from the three shapes. The checker constructs a 4096-word Golay realization and verifies its parameters/incidences; it does not enumerate Monster axes or matrices.

### Q block and total

For a traceless A the Q restriction is I_4096 tensor A, whose squared Frobenius norm is 4096||A||_F^2. Thus

$$\kappa_S=\frac{308}{3}+5040+4096=\frac{27716}{3}.$$

The quantum-coordinate cubic is T=F_S restricted to V, divided by sqrt(2). Therefore

$$\kappa=\kappa_S/2=\frac{13858}{3}.$$

This reproduces the existing kappa from a different calculation, using only a 24-coordinate block and short-vector moments. As a further consistency check, restoring the scalar cross terms gives 9240 in the source metric, or 4620 in the doubled metric, matching [M], Corollary 4.1 for traceless arguments. The matching is not used to derive 9240.

Dividing the three contributions by kappa_S proves the weights in section 1. Real polarization and complexification extend the norm identities to arbitrary complex superpositions in the quantum A_0 sector.

## 4. Clean matrix vectorization

The following specifies an input encoding instead of assuming an unpriced state-loader. Use two five-bit words x,y, initially in the subspace with basis labels

$$|i,j\rangle\ (0\le i<j<24),\qquad |k,k\rangle\ (1\le k<24).$$

The first labels represent F_ij. The diagonal labels represent the orthonormal traceless matrices

$$H_k=\frac{\sum_{i=0}^{k-1}D_i-kD_k}{\sqrt{k(k+1)}}.$$

The omitted label |0,0> represents the identity direction rather than a valid A_0 input. There are 276+23=299 valid labels. This encoding uses ten physical qubits, not an optimally packed nine-qubit label. It is a declared block interface, not an uncounted circuit from any other encoding.

The desired coordinate isometry J is

$$J|i,j\rangle=(|i,j\rangle+|j,i\rangle)/\sqrt2,$$

$$J|k,k\rangle=\frac{\sum_{i<k}|i,i\rangle-k|k,k\rangle}{\sqrt{k(k+1)}}.$$

No copy of the input label may remain in a work register: different H_k columns overlap on output labels and retaining k would destroy the intended coherent map.

### Off-diagonal inputs

Compute a diagonal flag c=[x=y]. On c=0 prepare a coin in |+>, conditionally swap x and y, and erase the coin by xoring [x>y] into it. Because the initial off-diagonal label is ordered, this comparator equals the swap coin on both branches. This produces the symmetric pair with the coin reset to zero. On a diagonal input the coin remains zero.

### Diagonal inputs

Conditioned on c=1, xor x into y, leaving y=0. Apply a fixed orthogonal H_24 to x, then xor x back into y. The first column of H_24 is the uniform vector, and column k>=1 is the diagonal coefficient vector of H_k.

There is a short explicit decomposition. For 1<=k<=23, define C_k as identity except on levels 0,k, where it is

$$C_k=\begin{pmatrix}\sqrt{k/(k+1)}&1/\sqrt{k+1}\\1/\sqrt{k+1}&-\sqrt{k/(k+1)}\end{pmatrix}.$$

Then H_24=C_1 C_2 ... C_23, with C_23 applied first. Induction gives the uniform first column and the stated Helmert columns. Each C_k is a real rotation after a sign gate on a two-level subspace. The emitted circuit implements those two levels using Gray-path reversible transpositions, a controlled Z, and controlled Ry. All comparisons and controls are decomposed into X, CNOT, and Toffoli gates with clean scratch.

Finally erase c by recomputing equality of the output coordinates. Diagonal outputs are still diagonal and off-diagonal outputs remain unequal, so this removes the flag without measuring it. All eleven work wires return to zero on the full valid input subspace, including arbitrary superpositions.

## 5. Bell pairs, gate counts, and precision

Append twelve independent Bell pairs on two twelve-qubit words s,s'. Their joint state is

$$|\Phi_{4096}\rangle=\frac1{64}\sum_{s=0}^{4095}|s\rangle|s\rangle.$$

Regroup the wires as (s,x) and (s',y). This is V_Q. The circuit acts unitarily on its full physical space and restricts to the stated clean isometry on the valid input subspace. The normalized branch succeeds deterministically. The number 3072/6929 is its weight **inside W**, not a heralding success probability imposed by this standalone circuit.

The unoptimized emitted circuit has the following exact instruction counts:

| Instruction | Count |
|---|---:|
| Toffoli | 799 |
| CNOT | 131 |
| Hadamard | 60 |
| Pauli X | 708 |
| Single-qubit Ry | 48 |
| Total | 1746 |

There are 45 wires: 34 output wires and 11 clean work wires. The output words each use twelve spinor bits and five coordinate bits. These counts assume arbitrary connectivity and the stated logical gate library. They exclude encoding/packing into a particular full 18-qubit representation, the other W blocks, fault-tolerant overhead, physical routing, and the cost of preparing an arbitrary input. They are counts of an emitted sequence, not optimality or hardware benchmarks.

In the mathematical circuit the angles are the exact expressions above. The Python generator serializes floating-point angles for reference/testing; it is not a certified high-precision or Clifford+T compiler. To approximate the ideal circuit to operator error zeta, it is sufficient to implement each of the 48 Ry gates to operator error zeta/48, with all other logical gates ideal. Telescoping gives the total error at most zeta, including coherent inputs entangled with a reference. Equivalently, an angular error at most zeta/24 per rotation suffices. Any angle-representation error and finite-gate-set synthesis error must share that budget. A Clifford+T resource count would additionally have to price each rotation at that precision and decompose Toffolis; no such numerical count is claimed here.

Multi-controlled gates in the code use explicitly clean conjunction chains. A k-controlled X uses k-2 clean scratch bits and 2k-3 Toffolis for k>=2. Controlled rotations compute the full conjunction into clean scratch, use a two-CNOT controlled-Ry decomposition, then uncompute. These are standard reversible-circuit techniques; [B] is prior work on controlled-gate decompositions, not a claim that the project invented them.

## 6. Reproduction and scope of checks

```sh
python circuits/seysen_qqa.py                 # resource report
python circuits/seysen_qqa.py --emit          # entire elementary-gate list
OPENBLAS_NUM_THREADS=1 python checks/verify_seysen_block.py
OPENBLAS_NUM_THREADS=1 python -O checks/verify_seysen_block.py
OPENBLAS_NUM_THREADS=1 python -OO checks/verify_seysen_block.py
```

The new checker has 50 labeled checks. It evaluates the full 21-wire coordinate circuit sparsely on all 299 valid basis inputs, two complex superpositions, and the inverse circuit. It tests both five-bit predicates on all 1024 input pairs and verifies scratch removal. It also checks the excluded identity input, the 23-step Helmert decomposition, the factor-of-two normalization, exact contraction weights, and the invalid norm obtained without off-diagonal normalization.

The largest dense matrix used is 24 by 24. The twelve Bell pairs are verified separately and their tensor product is proved analytically; a 45-qubit state is not expanded. Sparse floating simulation uses tolerance 1e-10 and explicitly bounds its accumulated pruning norm below 1e-11. These tests neither certify 1e-12 circuit accuracy nor constitute a full Monster simulation or formal proof. The deterministic report records scope and pass/fail checks, rather than machine-sensitive residuals. The archived scientific data and notes 01-06 are unchanged.

## 7. What is still missing

This circuit is not a replacement for the complete probe. A normalized isolated QQA branch does not have the full Monster stabilizer, and its sector decomposition is not preserved by every Monster element. Continuous rotations of the spinor factor already leave the Bell-pair identity invariant; keeping just this branch discards essential distinguishing structure.

The other two outputs for A_0 inputs, and the X and Q input sectors, remain to be compiled. Combining them must preserve linearity, branch amplitudes, relative signs, clean work registers and the exact global identity projection. Separately normalizing columns and keeping an input label is not an acceptable construction of W. No existing rigidity threshold or practical-trial requirement changes here.

The next bounded access target is the normalized A_0 -> X tensor X map with coefficients lambda_r A lambda_r^T. Its fourth-moment identity is now explicit, but coherent Leech indexing, signs, amplitude preparation and label erasure still have to be priced. In parallel, theorem-level priority of the robust-normalizer result remains open. A circuit subroutine is not a substitute for that comparison.

## References and source depth

[S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, sections 2.1, 6.1-6.2, 10.1, especially equations (10.1.1)-(10.1.6). https://arxiv.org/pdf/2002.10921v5

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169, Corollary 4.1 and Note 4.2. https://arxiv.org/pdf/math/0007169

[B] A. Barenco et al., *Elementary gates for quantum computation*, arXiv:quant-ph/9503016, sections 5-7. https://arxiv.org/pdf/quant-ph/9503016

The indicated PDF text and equations were read through the browser. Screenshot requests for Seysen pp.16,33-34 and the additional PDFs returned service errors; no successful visual PDF inspection is claimed. The normalization has the independent contraction cross-check above, but this does not replace expert review of source conventions. No downloaded papers or font files are bundled.
