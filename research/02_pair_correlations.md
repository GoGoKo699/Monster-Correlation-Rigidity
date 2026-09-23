# Monster symmetry from bipartite correlations

**Research checkpoint for Ruge Lin — 23 September 2026**  
**Status:** exploratory mathematical derivations from established Griess-algebra trace identities. The deductions below have explicit proofs and limited reproducibility checks; they have not received independent mathematical review, and their novelty is not established. This is not a manuscript or a claim of efficient experimental implementation.

## Executive statement

Let $V$ be the $d=196883$ dimensional real traceless Griess module, complexified when used as a quantum register. Its projected multiplication tensor defines an isometry $W:V\to V\otimes V$. Put $P=WW^\dagger$, $\sigma=P/d$, and let $|\tau\rangle$ be the normalized symmetric cubic tensor.

The deductions in this checkpoint are:

1. The full spectrum of the normalized multiplication channel $\mathcal E(X)=\kappa^{-1}\sum_iL_iXL_i$ is calculable from the second, third and fourth Norton–Matsuo trace identities.
2. The collective unitary stabilizers of $\sigma$ and of the ray $[\tau]$ are both exactly $U(1)\rho(\mathbb M)$. A separate metric probe is unnecessary.
3. The three-register Hamiltonian $H_3=(I-P)_{12}+(I-P)_{23}$ has unique ground state $\tau$ and exact gap $11161/13858$ when each projector has unit strength. It gives a global fidelity bound for arbitrary input states.
4. Preparing $\sigma$, applying two ordinary forward calls to $U$, and measuring $P$ gives a perfectly complete membership test with positive rejection for every $U\notin U(1)\rho(\mathbb M)$. No one-query perfectly complete test for an irreducible representation can reject any unitary, even with ancillas. This is a restricted query-minimality statement, not a finite-shot exact decision algorithm.
5. The pair test has an explicit local gate-distance bound, under an operator-norm logarithm promise of radius $\pi/4$.
6. A useful explicit global distance-to-Monster bound is **not** established. Global state certification and global gate certification must not be conflated.

All register-locality statements refer to $d$-dimensional registers, not individual physical qubits.

## 1. Literature inputs, normalization and provenance

### 1.1 Sources actually used

**[M00]** A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169. The mathematical inputs are Corollary 4.1, printed p. 16, together with the invariant-form and multiplication conventions. The displayed PDF formulae were inspected directly.

**[N96]** S. P. Norton, *The Monster algebra: some new formulae*, in *Moonshine, the Monster, and Related Topics*, Contemporary Mathematics 193 (1996), pp. 297–306. This is the original source referenced by [M00]. The present checkpoint did not obtain and audit the complete original chapter. It must be checked in a priority audit.

**[HS25]** G. Höhn and M. Seysen, *The Order of the Monster Finite Simple Group*, arXiv:2508.01037, Theorem 5.7. This restates and proves the classical identification of the full Griess-algebra automorphism group with the Monster; the identification is not a new result here.

**[BCLY18]** M. Brannan, B. Collins, H. H. Lee and S.-G. Youn, *Temperley–Lieb quantum channels*, arXiv:1810.08001, Section 2.3. Intertwining isometries followed by a partial trace are an established construction of Clebsch–Gordan channels. Our $\mathcal E$ belongs to that framework.

**[C+11]** M. Cramer et al., *Efficient quantum state tomography*, arXiv:1101.4366, Eq. (3), printed p. 3. The general conversion of a unique-ground-state gap into an energy/fidelity witness is established; our contribution under examination is the particular tensor, exact spectrum, and associated symmetry conclusions.

**[LRW23]** M. L. LaBorde, S. Rethinasamy and M. M. Wilde, *Testing symmetry on quantum computers*, Quantum **7**, 1120 (2023), arXiv:2105.12758. Generic quantum symmetry testing is existing research, not a novelty claim of this checkpoint.

A search of these surrounding literatures has **not** established priority or publishability for the particular construction below. In particular, equivalent spectra and recoupling identities may already occur in older Griess-algebra calculations.

### 1.2 Real algebra and the removed identity direction

Let $B=\mathbb Rt\oplus V$ be the positive-definite real Griess algebra, where

$$
\dim V=d=196883,\qquad t=\omega/\sqrt{12},\qquad s=1/\sqrt3.
$$

The algebra identity is $\omega/2=t/s$; $t$ is the normalized identity direction, not the algebra identity itself. With $a,b\in V$,

$$
t^2=st,\quad ta=sa,\quad ab=\mu(a,b)+s\langle a,b\rangle t.
$$

Define $L_ab=\mu(a,b)$ and, in a real orthonormal basis $\{e_i\}$,

$$
T_{ijk}=\langle\mu(e_i,e_j),e_k\rangle.
$$

$T$ is real and completely symmetric. Multiplication by $a\in V$ on the full algebra is

$$
R_a=\begin{pmatrix}0&s a^T\\s a&L_a\end{pmatrix}.
$$

The full trace identities restricted to $V$ have coefficients $4620$ at order two, $900$ at order three, and $166,-116,166,52$ in the relevant order-four contractions. These are literature inputs, not numerical fits.

Subtracting the scalar blocks gives

$$
\operatorname{Tr}L_a=0,\qquad
\operatorname{Tr}(L_aL_b)=\kappa\langle a,b\rangle,
\qquad\kappa=4620-2s^2=\frac{13858}{3},
$$

$$
\operatorname{Tr}(L_aL_bL_c)=899T(a,b,c).
$$

The coefficient $899=900-3s^2$ is important: using $900$ after removing the identity direction gives the wrong channel spectrum.

## 2. Isometry, tensor state and bipartite state

Define

$$
W|a\rangle=\frac1{\sqrt\kappa}\sum_{ij}T_{aij}|ij\rangle,
\qquad
P=WW^\dagger,
\qquad
\sigma=\frac Pd.
$$

The second trace identity implies $W^\dagger W=I$ and $\operatorname{rank}P=d$.

Also define

$$
|\tau\rangle=\frac1{\sqrt{d\kappa}}\sum_{ijk}T_{ijk}|ijk\rangle,
\qquad
|\Phi\rangle=\frac1{\sqrt d}\sum_i|ii\rangle.
$$

By tensor symmetry,

$$
|\tau\rangle=(W\otimes I)|\Phi\rangle=(I\otimes W)|\Phi\rangle,
$$

$$
\operatorname{Tr}_3|\tau\rangle\langle\tau|=\sigma,
\qquad
\operatorname{Tr}_2\sigma=\operatorname{Tr}_1\sigma=I/d.
$$

All pair marginals of $\tau$ agree, and every single register is maximally mixed. The Monster intertwiner relation is

$$
W\rho(g)=(\rho(g)\otimes\rho(g))W.
$$

## 3. The multiplication channel and its entire spectrum

Let

$$
\mathcal F(X)=\sum_iL_iXL_i,
\qquad
\mathcal E(X)=\mathcal F(X)/\kappa.
$$

Since $L_i=L_i^T$ and $\sum_iL_i^2=\kappa I$, $\mathcal E$ is completely positive, trace preserving, unital and self-adjoint in the Hilbert–Schmidt inner product. It commutes with transpose. It also equals either partial trace of the isometric encoding $W X W^\dagger$.

### 3.1 Projected fourth trace identity

Write

$$
\alpha=\frac{496}{3},\qquad\beta=-116,
\qquad u=\frac{965}{9},\qquad v=\frac{40}{3}.
$$

Block subtraction in [M00] gives

$$
\begin{aligned}
\operatorname{Tr}L_aL_bL_cL_e={}&
\alpha\big[\langle\mu(a,b),\mu(c,e)\rangle+
\langle\mu(a,e),\mu(b,c)\rangle\big]\\
&+\beta\langle\mu(a,c),\mu(b,e)\rangle\\
&+u\big[\langle a,b\rangle\langle c,e\rangle+
\langle a,e\rangle\langle b,c\rangle\big]
+v\langle a,c\rangle\langle b,e\rangle.
\end{aligned}
$$

For clarity, the general scalar-block subtraction at fourth order removes

$$
2s^2\big[\langle\mu(a,b),\mu(c,e)\rangle+
\langle\mu(a,e),\mu(b,c)\rangle\big]
+s^4\big[\langle a,b\rangle\langle c,e\rangle+
\langle a,e\rangle\langle b,c\rangle\big].
$$

### 3.2 A polynomial identity for the channel

Define

$$
m(X)=\sum_{pq}X_{pq}\mu(e_p,e_q),\qquad Q(X)=L_{m(X)}.
$$

$Q$ is $\kappa$ times the orthogonal projection onto $L(V)$, and vanishes on skew matrices. Direct contraction gives

$$
(\mathcal F^2)_{ab,pq}=\operatorname{Tr}(L_aL_pL_qL_b).
$$

Therefore

$$
\mathcal F^2(X)=\alpha\mathcal F(X)+\beta\mathcal F(X^T)
+\alpha Q(X)+uX+vX^T+u\operatorname{Tr}(X)I.
$$

On symmetric matrices,

$$
\mathcal F^2=\frac{148}{3}\mathcal F+\frac{496}{3}Q
+\frac{1085}{9}\mathcal I+\frac{965}{9}\operatorname{Tr}(\cdot)I.
$$

The scalar and multiplication sectors have eigenvalues $\kappa$ and $899$, respectively. On their orthogonal complement in the symmetric matrices, the polynomial roots are $155/3$ and $-7/3$.

On skew matrices,

$$
\left(\mathcal F+\frac13\mathcal I\right)^2
=282\left(\mathcal F+\frac13\mathcal I\right),
$$

so the roots are $845/3$ and $-1/3$, agreeing with the previous local-rigidity checkpoint.

### 3.3 Spectrum and multiplicities

| Sector | Transpose parity | Eigenvalue of $\mathcal E$ | Dimension |
|---|---:|---:|---:|
| Scalars | $+$ | $1$ | $1$ |
| $L(V)$ | $+$ | $2697/13858$ | $196883$ |
| Symmetric complement, first root | $+$ | $155/13858$ | $842609326$ |
| Symmetric complement, second root | $+$ | $-7/13858$ | $18538750076$ |
| Skew, first root | $-$ | $845/13858=5/82$ | $21296876$ |
| Skew, second root | $-$ | $-1/13858$ | $19360062527$ |

The dimensions can be recovered without assuming an irreducible decomposition, using the dimensions of the symmetric/skew matrix spaces and

$$
\operatorname{Tr}_{\mathrm{sym}}\mathcal F=d\kappa/2,
\qquad
\operatorname{Tr}_{\mathrm{skew}}\mathcal F=-d\kappa/2.
$$

As checks, the multiplicities sum to $d^2$, $\operatorname{Tr}_{\mathrm{super}}\mathcal E=0$, and $\operatorname{Tr}_{\mathrm{super}}\mathcal E^2=d$.

The largest singular value away from the scalar fixed point is

$$
r=\frac{2697}{13858}=0.194616827825\ldots.
$$

The underlying spectrum may already have an equivalent form in algebraic literature. Expressing it as a quantum channel is not, by itself, a priority claim.

## 4. A three-register parent Hamiltonian with exact gap

Under row-vectorization of matrices, direct contraction gives

$$
(W\otimes I)^\dagger(I\otimes W)=\mathcal E.
$$

The two isometries have ranges $\operatorname{ran}P_{12}$ and $\operatorname{ran}P_{23}$. Their principal-angle cosines are the singular values of $\mathcal E$. The singular value one is simple, and its vector is $\Phi$. Both isometries map it to $\tau$. Thus

$$
\operatorname{ran}P_{12}\cap\operatorname{ran}P_{23}=\mathbb C\tau.
$$

Set

$$
H_3=(I-P)_{12}+(I-P)_{23}.
$$

For two projections whose nontrivial principal-angle cosine is $s$, the corresponding energies of their complementary-projector sum are $1-s$ and $1+s$. This follows by diagonalizing the associated two-dimensional principal-angle block. Remaining orthogonal directions have energy two. Consequently $H_3$ has a unique zero-energy ground state and exact gap

$$
\boxed{\Delta=1-r=\frac{11161}{13858}=0.805383172175\ldots.}
$$

This is the gap of a specified finite three-register Hamiltonian, not a thermodynamic or scalable-spin-chain gap.

For every density matrix $\omega$ on the three registers,

$$
\boxed{1-\langle\tau|\omega|\tau\rangle\le
\frac{\operatorname{Tr}(H_3\omega)}\Delta.}
$$

This implication is the established energy-witness argument [C+11]; the exact Monster-derived $\Delta$ is the calculation here. It makes no purity or local-calibration assumption about $\omega$. It does assume trusted access to the Hamiltonian terms or their measurements.

## 5. Exact collective unitary stabilizers: the metric probe is redundant

The distinction between real orthogonal and arbitrary complex unitary transformations is essential. A finite real algebra automorphism group alone does not settle the complex unitary ray stabilizer of its tensor.

### 5.1 Recovering transpose from the pair state

Let $S|a,b\rangle=|b,a\rangle$ be swap. Under vectorization, it is matrix transpose. Let $C=P^{\Gamma_2}$, the partial transpose of **$P$**, not of $\sigma$.

Direct contraction yields

$$
C=\mathcal E S=S\mathcal E.
$$

On the six sectors in Section 3, the spectrum of $C$ is

$$
1,\quad\frac{2697}{13858},\quad\frac{155}{13858},\quad
-\frac7{13858},\quad-\frac{845}{13858},\quad\frac1{13858}.
$$

The first four belong to transpose-even matrices and the last two to transpose-odd matrices. These sets are disjoint. Therefore a real interpolation polynomial $f$ exists such that

$$
S=f(C),
$$

with $f=+1$ on the first four spectral values and $f=-1$ on the last two. This is not a separation by the sign of $C$: each parity contains an eigenvalue of the other sign.

### 5.2 Stabilizer proof

Suppose $(U\otimes U)P(U\otimes U)^\dagger=P$. Taking a partial transpose shows that $U\otimes\overline U$ commutes with $C$, hence with $S$. Therefore

$$
U\otimes\overline U=\overline U\otimes U.
$$

Equality of these nonzero simple tensors forces $U$ and $\overline U$ to be proportional. Unitarity then gives

$$
U=e^{i\theta}O,\qquad O\in O(d).
$$

Furthermore, preservation of $P$ makes $U^{\otimes3}$ commute with $H_3$. Its unique ground state implies that $U^{\otimes3}\tau$ is a phase times $\tau$. Removing the phase of $U$, reality gives $O^{\otimes3}T=\pm T$. In the minus case replace $O$ by $-O$ and absorb the change into global phase.

An orthogonal transformation preserving $T$ preserves $\mu$. Extending it by fixing $t$ preserves the full Griess multiplication. The classical automorphism theorem [HS25] then identifies it with a Monster element. The converse follows immediately from invariance of the algebra.

Thus

$$
\boxed{\operatorname{Stab}_{\rm collective}(\sigma)
=U(1)\rho(\mathbb M).}
$$

If a unitary preserves the ray of $\tau$, it preserves its pair marginal $\sigma$, so also

$$
\boxed{\operatorname{Stab}_{\rm collective}([\tau])
=U(1)\rho(\mathbb M).}
$$

The same group is the **collective on-site** symmetry group of $H_3$. The full commutant of $H_3$ in $U(d^3)$ is much larger; no claim is made about independent local transformations or arbitrary global unitaries.

## 6. A two-query membership test and a one-query obstruction

Assume a trusted preparation of $\sigma$ and trusted projective measurement $\{P,I-P\}$. Apply the same unknown unitary $U$ once to each register. Its rejection probability is

$$
\varepsilon_P(U)=1-\frac1d\operatorname{Tr}
\left[P U^{\otimes2}P(U^\dagger)^{\otimes2}\right].
$$

Both subspaces have dimension $d$, so zero rejection is equivalent to their equality. Section 5 gives

$$
\varepsilon_P(U)=0\quad\Longleftrightarrow\quad
U\in U(1)\rho(\mathbb M).
$$

Every outsider has positive rejection, but this does not mean one or finitely many trials decides exact membership with certainty. There is no uniform positive rejection probability as outsiders approach the group.

### 6.1 Why one ordinary forward query cannot suffice with perfect completeness

Let $\rho:G\to U(d)$ be any complex irreducible representation. Orthogonality of irreducible matrix coefficients implies

$$
\operatorname{span}_{\mathbb C}\{\rho(g):g\in G\}=\operatorname{End}(\mathbb C^d).
$$

Any one-query test with arbitrary ancilla, preprocessing and postprocessing can be written as a pure input $\psi$, one application of $U\otimes I$, and an acceptance effect $A$. Mixed inputs and discarded systems can be purified and included in the ancilla.

Perfect completeness for every $\rho(g)$ implies

$$
(I-A)^{1/2}(\rho(g)\otimes I)|\psi\rangle=0
\quad\text{for all }g.
$$

Linearity and the span identity imply the same equation for **every** matrix $U$, in particular every unitary. Thus the test accepts every unitary.

Applied to the $196883$-dimensional Monster module, this proves that two ordinary forward queries are minimal for the narrow property: perfect completeness and some rejecting power against every outsider. This is not a lower bound for approximate-completeness tests, controlled-oracle models, general channel promises, or bounded-error property testing at fixed distance. Its novelty is not claimed.

## 7. Explicit local robustness of the pair test

Define

$$
\operatorname{dist}_{\mathbb M}(U)=
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}.
$$

Suppose a unitary has a logarithmic local representation

$$
U=e^{i\theta}\rho(g)e^{iH},\qquad
H=H^\dagger,\quad\operatorname{Tr}H=0,
\quad\|H\|_{\rm op}\le\pi/4.
$$

Then

$$
\boxed{
\varepsilon_P(U)\ge\frac{12528}{1681\pi^2}
\frac{\|H\|_F^2}{d}
\ge\frac{12528}{1681\pi^2}
\operatorname{dist}_{\mathbb M}(U)^2.
}
$$

Equivalently,

$$
\operatorname{dist}_{\mathbb M}(U)
\le1.150781461617\ldots\sqrt{\varepsilon_P(U)}.
$$

The logarithm condition is a promise; small measured rejection has not yet been proved to imply this condition globally.

### 7.1 Quadratic form

Let $K=H\otimes I+I\otimes H$ and

$$
q(H)=\frac1d\operatorname{Tr}\left[PK(I-P)K\right].
$$

Using the isometry,

$$
W^\dagger KW=2\mathcal E(H),
$$

$$
q(H)=\frac1d\left[
2\operatorname{Tr}H^2+2\operatorname{Tr}\big(H\mathcal E(H^T)\big)
-4\operatorname{Tr}\mathcal E(H)^2\right].
$$

For a Hermitian component with transpose parity $\eta\in\{+1,-1\}$ and channel eigenvalue $\lambda$,

$$
q(H)=h_\eta(\lambda)\frac{\|H\|_F^2}{d},
\qquad h_\eta(\lambda)=2+2\eta\lambda-4\lambda^2.
$$

For parity $-1$, Hermitian matrices are $i$ times real skew matrices. The six coefficients, in the spectrum order of Section 3, are

$$
0,\quad\frac{107435786}{48011041},\quad
\frac{97072052}{48011041},\quad\frac{95973530}{48011041},\quad
\frac{3132}{1681},\quad\frac{96029010}{48011041}.
$$

The first is the scalar phase direction, removed by $\operatorname{Tr}H=0$. Hence

$$
q(H)\ge\frac{3132}{1681}\frac{\|H\|_F^2}{d}.
$$

### 7.2 Finite-radius conversion

For a projection $P$ and a unitary $V$,

$$
\varepsilon_P(e^{iH})=
\frac1{2d}\|[P,e^{iK}]\|_F^2.
$$

The logarithm promise places the spectrum of $K$ in $[-\pi/2,\pi/2]$. For any two eigenvalues $x,y$ in that interval,

$$
|e^{ix}-e^{iy}|^2\ge\frac4{\pi^2}(x-y)^2.
$$

Therefore

$$
\varepsilon_P(e^{iH})\ge\frac4{\pi^2}q(H).
$$

Finally, $\|e^{iH}-I\|_F\le\|H\|_F$ and invariance under phases/Monster operations proves the displayed bound.

Conditional on ideal probes and the local promise, distance at least $\delta$ implies rejection at least $c\delta^2$, $c=12528/(1681\pi^2)$. Independent repetitions can then suppress false acceptance below $\alpha$ using $N\ge\log(1/\alpha)/(c\delta^2)$ trials, rounded upward. This is a query count conditional on probe access, not an efficient circuit construction.

## 8. Global reductions that do hold, and the global statement still missing

### 8.1 Global comparison with the cubic return loss

Let

$$
\ell_3(U)=1-|\langle\tau|U^{\otimes3}|\tau\rangle|^2.
$$

Symmetry of $\tau$ gives the exact identity

$$
\langle\tau|(U^\dagger)^{\otimes3}H_3U^{\otimes3}|\tau\rangle
=2\varepsilon_P(U).
$$

The spectral bounds $\Delta(I-|\tau\rangle\langle\tau|)\le H_3\le2(I-|\tau\rangle\langle\tau|)$ imply, for every unitary,

$$
\boxed{\varepsilon_P(U)\le\ell_3(U)\le\frac2\Delta\varepsilon_P(U).}
$$

Thus the pair test globally controls the cubic state's damage. This still does not quantitatively round an arbitrary $U$ to a nearby Monster element.

### 8.2 A global real-structure bound

Let

$$
\ell_2(U)=1-|\langle\Phi|U^{\otimes2}|\Phi\rangle|^2.
$$

The minimum spectral separation between opposite transpose parities of $C=P^{\Gamma_2}$ is

$$
g_{\rm par}=\frac8{13858}=\frac4{6929}.
$$

Blockwise spectral comparison gives

$$
\|[S,Z]\|_F\le\frac2{g_{\rm par}}\|[C,Z]\|_F,
\qquad Z=U\otimes\overline U.
$$

The two squared norms are

$$
\|[S,Z]\|_F^2=2d^2\ell_2(U),\qquad
\|[C,Z]\|_F^2=2d\varepsilon_P(U).
$$

For the second equality, use unitary conjugation and the Hilbert–Schmidt isometry of partial transpose. Consequently

$$
\boxed{\ell_2(U)\le\frac{48011041}{787532}\varepsilon_P(U)
=60.963924\ldots\,\varepsilon_P(U).}
$$

Polar decomposition of the real part of a phase-rotated $U$ also gives

$$
\min_{\theta,O\in O(d)}\frac{\|U-e^{i\theta}O\|_F^2}{d}\le\ell_2(U).
$$

One proof chooses a phase with $\operatorname{Tr}UU^T\ge0$, writes $U=A+iB$, and observes $AA^T+BB^T=I$. If $s_j$ are the singular values of $A$, then $0\le s_j\le1$ and $\sum_js_j\ge\sum_js_j^2=d-\|B\|_F^2$. Orthogonal Procrustes gives a squared distance at most $2\|B\|_F^2=d(1-|\operatorname{Tr}UU^T|/d)\le d\ell_2(U)$.

This globally controls distance to phase times a real orthogonal transformation. The remaining unresolved step is explicit quantitative global rounding within the orthogonal group to an exact Griess-algebra automorphism.

Compactness provides an unspecified modulus because the exact zero set is known and finite projectively. That observation is not a useful explicit global robustness theorem.

## 9. Why this is not automatically a scalable frustration-free chain

Let $H_4=(I-P)_{12}+(I-P)_{23}+(I-P)_{34}$. Define the projections onto a pure tensor state on each overlapping triple,

$$
Q_{123}=|\tau\rangle\langle\tau|_{123}\otimes I_4,
\qquad
Q_{234}=I_1\otimes|\tau\rangle\langle\tau|_{234}.
$$

Complete symmetry and a maximally mixed single marginal give

$$
(\langle\tau|_{123}\otimes I_4)(I_1\otimes|\tau\rangle_{234})=I/d,
\qquad \|Q_{123}Q_{234}\|=1/d.
$$

Since $2H_4\ge H_{123}+H_{234}$,

$$
H_4\ge\frac\Delta2(2I-Q_{123}-Q_{234})
\ge\frac\Delta2\left(1-\frac1d\right)I.
$$

Numerically and exactly,

$$
\boxed{H_4\ge\frac{26797561}{66546454}I
=0.40268954075\ldots I.}
$$

Thus a four-site chain of these same projectors is already frustrated. No zero-energy extension of the three-site state exists. This excludes a particular naive scalable extension; it does not exclude other Monster-symmetric many-body constructions.

## 10. General principle isolated by the example

A real symmetric cubic tensor with isotropic second contraction defines $W$, $P$, $\tau$, and a self-adjoint channel $\mathcal E$ as above. Two verifiable conditions suffice for the exact stabilizer reduction:

- The scalar fixed point of $\mathcal E$ is the unique singular-value-one direction, and all other singular values are strictly below one.
- The spectra of $\mathcal ES$ on transpose-even and transpose-odd subspaces are disjoint.

The first makes the two pair supports determine a unique cubic ray. The second reconstructs the real structure from the pair support. Together they identify the collective unitary stabilizer with phase times the orthogonal automorphism group of the cubic algebra. The first also gives the exact three-register parent gap from the second singular value.

The mechanism is a general tensor/channel criterion, not an appeal to the size of a finite group. Determining whether this criterion and the Monster specialization add something substantive beyond existing recoupling, tensor-stabilizer, and parent-Hamiltonian literature is the next priority task.

## 11. Operational boundaries and claim ledger

**Algebraic inputs:** established Griess algebra, irreducible traceless Monster module, trace identities, and full algebra automorphism group. Not novel here.

**Derived in this checkpoint:** channel spectrum in the stated normalization; pair-support and cubic-ray collective unitary stabilizers; exact three-site gap; two-query test; one-query obstruction in the stated model; explicit local pair-test robustness; global state/loss/reality reductions; obstruction to a naive four-site frustration-free extension. These have written proofs but not independent review.

**Not established:** publication novelty, a useful global gate-distance bound, an efficient preparation of $W$ or $\sigma$, an efficient measurement of $P$, practical quantum advantage, fault tolerance, leakage handling, device-independent certification, or general noisy-channel certification.

**Register count:** $d<2^{18}$, so padding uses 18 qubits per queried register: 36 for the bipartite probe and 54 for the cubic state. These are not total gate counts or full workspace bounds. Every logical operation must preserve a specified $d$-dimensional subspace. Unused padding directions are not certified by these theorems.

**Noise:** the global state-fidelity inequality allows an arbitrary mixed state $\omega$, but requires trusted measurements. The gate theorems assume a fixed unitary used consistently on both registers. General channels and temporally correlated errors need separate analysis.

**Metric:** normalized Frobenius distance is not worst-case channel distance. The test identifies membership, not which Monster element was used.

## 12. Reproducibility and limits of the checks

`verify_exact.py` uses only the Python standard library. It checks rational coefficients, roots, multiplicities, gaps, parity separation and tangent constants. It also independently checks the relevant tensor-index contractions on symmetric integer tensors of dimensions 3 and 4. Its checks use explicit exceptions, not `assert`, and produce identical output under normal Python and `python -O`.

`verify_toy.py` requires NumPy and constructs two small projected coordinatewise algebras, of dimensions 3 and 4. It checks the isometry, recoupling, partial transpose, unique three-site ground state, exact principal-angle gap formula, pair-test Hessian, finite-radius sine inequality, energy/loss identity, and four-site bound. The largest matrix is $256\times256$. These toy algebras do **not** stand in for the Monster's unitary-stabilizer theorem; their transpose-parity spectra need not satisfy the Monster criterion.

The previous standard-library verifier was rerun without changing the previous checkpoint. All tests described here passed. They do not construct the full Monster tensor, verify the original literature from first principles, establish novelty, or replace independent review of the proofs.

Run:

```bash
python verify_exact.py
python -O verify_exact.py
OPENBLAS_NUM_THREADS=1 python verify_toy.py
```

The attached JSON reports record the actual outcomes and their stated scope.
