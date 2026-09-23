# Monster correlation probes: an explicit local-rigidity calculation

**Research checkpoint — 22 September 2026**

This is a derivation and audit note, not a submission-ready manuscript or a claim of novelty. The algebraic inputs below are established results. The quantum reformulation, contraction calculation, and finite-radius bound are derived here from those inputs. They have not received independent specialist review. The accompanying script verifies rational arithmetic and general contraction identities on small tensors; it does not construct the Monster tensor.

## 1. Operational question and scope

Let $V$ be the real, absolutely irreducible 196883-dimensional Monster module and let $\rho:\mathbb M\to O(V)$ be its Griess-algebra realization. Complexify $V$ when treating it as a quantum register. The task is to test whether an unknown unitary $U$ belongs, up to phase, to $\rho(\mathbb M)$ by testing preservation of fixed correlation states.

The model assumes a known logical space, a fixed memoryless unitary applied independently and identically to each register, and trusted preparation and measurement of the probe states. It does not assume an efficient preparation circuit. Leakage, general channels, independent unknown operations on different registers, and device-independent certification are outside the theorem.

Set $d=196883$ and use the normalized Frobenius distance

$$
\operatorname{dist}_{\mathbb M}(U)
=\min_{g\in\mathbb M,\,\theta\in\mathbb R}
\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}.
$$

This is an average-case matrix metric, not a worst-case channel metric.

## 2. Literature inputs and normalization

Use the real Euclidean Griess algebra $B$ in the VOA normalization of Matsuo [1]. Its dimension is $196884$, its conformal vector satisfies

$$
\omega a=2a,\qquad \langle\omega,\omega\rangle=12,
$$

and its multiplication is commutative with invariant positive inner product:

$$
\langle ab,c\rangle=\langle a,bc\rangle.
$$

The full automorphism group is the Monster [2]. This is a classical theorem, not a new claim of this note.

Write

$$
B=\mathbb Rt\oplus V,\qquad t=\omega/\sqrt{12},\qquad
V=\omega^\perp,\qquad s=1/\sqrt3.
$$

For $a,b\in V$, define the projected multiplication

$$
\mu(a,b)=P_V(ab),\qquad L_a b=\mu(a,b).
$$

Then the full product is reconstructed by

$$
t^2=st,\qquad ta=sa,\qquad
ab=\mu(a,b)+s\langle a,b\rangle t.
$$

The full multiplication operator $R_a$ for $a\in V$ therefore has block form

$$
R_a=\begin{pmatrix}0&s a^T\\s a&L_a\end{pmatrix}.
$$

The necessary instances of Norton’s trace identities, as given in Matsuo [1, Corollary 4.1, printed page 16], are

$$
\operatorname{Tr}R_a=0,\qquad
\operatorname{Tr}(R_aR_b)=4620\langle a,b\rangle
\quad(a,b\in V),
$$

and, for $a,b,c,e\in V$,

$$
\begin{aligned}
\operatorname{Tr}(R_aR_bR_cR_e)
={}&166\langle ab,ce\rangle-116\langle ac,be\rangle
+166\langle ae,bc\rangle\\
&+52\big(\langle a,b\rangle\langle c,e\rangle
+\langle a,c\rangle\langle b,e\rangle
+\langle a,e\rangle\langle b,c\rangle\big).
\end{aligned}
$$

Products inside these last inner products are the **full** product in $B$, not the projected product. Terms containing an inner product with $\omega$ vanish because all four arguments lie in $V$.

Subtracting the two scalar-block contributions gives

$$
\operatorname{Tr}(L_aL_b)=\kappa\langle a,b\rangle,
\qquad \kappa=4620-\frac23=\frac{13858}{3}.
$$

Also $\operatorname{Tr}L_a=0$.

## 3. Probe states and their exact symmetry

In a real orthonormal basis of $V$, set

$$
T_{ijk}=\langle\mu(e_i,e_j),e_k\rangle.
$$

The tensor is completely symmetric and real. The second trace identity implies

$$
\sum_{jk}T_{ijk}T_{i'jk}=\kappa\delta_{ii'},
\qquad \|T\|^2=d\kappa=\frac{2728404614}{3}.
$$

Define

$$
|\Phi\rangle=\frac1{\sqrt d}\sum_i|ii\rangle,
\qquad
|\tau\rangle=\frac1{\sqrt{d\kappa}}\sum_{ijk}T_{ijk}|ijk\rangle.
$$

Each one-register marginal of $|\tau\rangle$ is exactly $I/d$. The same is true for $|\Phi\rangle$.

For a unitary $U$, define

$$
\ell_2(U)=1-|\langle\Phi|U^{\otimes2}|\Phi\rangle|^2,
\qquad
\ell_3(U)=1-|\langle\tau|U^{\otimes3}|\tau\rangle|^2,
\qquad L(U)=\ell_2(U)+\ell_3(U).
$$

**Exact characterization.**

$$
L(U)=0\quad\Longleftrightarrow\quad
U=e^{i\theta}\rho(g)\quad\text{for some }g\in\mathbb M.
$$

**Proof.** Pair-state ray preservation gives $UU^T=e^{i\alpha}I$. Removing half this phase produces a unitary $O$ satisfying $OO^T=I$, hence a real orthogonal matrix. Since $T$ is real, cubic ray preservation gives $O^{\otimes3}T=\pm T$. If the sign is negative, replace $O$ by $-O$, which changes only the projective representative and reverses the cubic sign. Preservation of the metric and cubic means preservation of $\mu$. The reconstruction formulas in Section 2 extend $O$ by fixing $t$ to an automorphism of $B$, hence to a Monster element. Conversely, Monster automorphisms preserve both probes. QED.

The same $U$ acts on each **entire** register. A register requires 18 qubits under binary padding; the pair and triple probes use 36 and 54 qubits respectively. These counts say nothing about preparation depth or precision.

## 4. A commutator operator that is a scaled projection

On the real skew matrices $\mathfrak{so}(V)$ with Frobenius inner product, define

$$
\mathcal F(A)=\sum_i L_{e_i} A L_{e_i},
\qquad
\mathcal G=\mathcal F+\frac13\mathcal I.
$$

These maps are self-adjoint, and they preserve the skew sector. The following identity follows from the trace inputs:

$$
\boxed{\mathcal G^2=282\mathcal G.}
$$

**Derivation.** Let $X_{ab}=ab^T-ba^T$. Tensor symmetry gives

$$
\mathcal F(X_{ab})=[L_a,L_b],
\qquad
[R_a,R_b]=0\oplus\mathcal G(X_{ab}).
$$

Antisymmetrizing the fourth trace identity cancels the fully symmetric metric terms and yields

$$
-\operatorname{Tr}([R_a,R_b][R_c,R_e])
=564\big(\langle ac,be\rangle-\langle ae,bc\rangle\big).
$$

On the other hand,

$$
\langle X_{ab},\mathcal G(X_{ce})\rangle_F
=2\big(\langle ac,be\rangle-\langle ae,bc\rangle\big).
$$

Thus

$$
\langle\mathcal G(X_{ab}),\mathcal G(X_{ce})\rangle_F
=282\langle X_{ab},\mathcal G(X_{ce})\rangle_F.
$$

The $X_{ab}$ span the skew matrices. Self-adjointness proves the displayed operator identity. Therefore

$$
\mathcal P=\frac1{282}\mathcal G
$$

is an orthogonal projection. This derivation does not require materializing any matrix of dimension $d$ or its tensor powers. No novelty assertion is attached to the projection identity; an equivalent construction may already occur in the algebra literature.

## 5. Exact quadratic loss spectrum for orthogonal errors

For $A^T=-A$, let

$$
\mathcal D_A T=(A\otimes I\otimes I+I\otimes A\otimes I+I\otimes I\otimes A)T.
$$

A direct contraction gives

$$
\|\mathcal D_A T\|^2
=3\kappa\|A\|_F^2-6\langle A,\mathcal F(A)\rangle_F
=13860\|A\|_F^2-1692\|\mathcal P A\|_F^2.
$$

After normalizing $T$,

$$
\boxed{
\|\mathcal D_A\tau\|^2
=\frac{108}{41}\frac{\|\mathcal P A\|_F^2}{d}
+\frac{20790}{6929}\frac{\|(I-\mathcal P)A\|_F^2}{d}.}
$$

Consequently, for fixed $A$,

$$
\ell_3(e^{\epsilon A})
=\epsilon^2\|\mathcal D_A\tau\|^2+O(\epsilon^4).
$$

The fourth-order remainder follows because the real return amplitude is even in $\epsilon$. The two **quadratic loss coefficients**, relative to $\|A\|_F^2/d$, are

$$
\gamma_-=\frac{108}{41}\simeq2.63414634,
\qquad
\gamma_+=\frac{20790}{6929}\simeq3.00043296.
$$

They are not the Hessian eigenvalues under the convention with a factor $1/2$ in Taylor’s theorem: those would have an extra factor two.

### Multiplicities without a character-table calculation

For a symmetric matrix $L$, the trace of $A\mapsto LAL$ on skew matrices is

$$
\frac12\big((\operatorname{Tr}L)^2-\operatorname{Tr}L^2\big).
$$

Since every $L_{e_i}$ is traceless,

$$
\operatorname{Tr}_{\mathfrak{so}(V)}\mathcal F=-\frac{d\kappa}{2}.
$$

Writing $m=d(d-1)/2=19381359403$,

$$
\operatorname{rank}\mathcal P
=\frac{-d\kappa/2+m/3}{282}=21296876,
$$

and the complementary rank is $19360062527$. Both coefficients therefore occur. This argument determines dimensions of the eigenspaces; it does not by itself prove that they are irreducible Monster representations.

## 6. Finite-radius local theorem for arbitrary unitary errors

**Theorem.** Suppose

$$
U=e^{i\theta}\rho(g)e^{iH},\qquad
H=H^\dagger,\quad \operatorname{Tr}H=0,\quad
\|H\|_{\mathrm{op}}\le\frac\pi6.
$$

Then

$$
\boxed{
L(U)\ge\frac{432}{41\pi^2}\frac{\|H\|_F^2}{d}
\ge\frac{432}{41\pi^2}\operatorname{dist}_{\mathbb M}(U)^2.}
$$

Equivalently,

$$
\operatorname{dist}_{\mathbb M}(U)
\le\sqrt{\frac{41\pi^2}{432}}\sqrt{L(U)}
\simeq0.96783189\sqrt{L(U)}.
$$

The existence of the displayed factorization with the stated logarithm bound is a **promise**, not a conclusion inferred from small loss.

**Proof.** Loss is invariant under the left factor $e^{i\theta}\rho(g)$, so take $U=e^{iH}$. Write

$$
H=S+iA,\qquad S^T=S\text{ real},\qquad A^T=-A\text{ real}.
$$

Then $\operatorname{Tr}S=0$ and $\|H\|_F^2=\|S\|_F^2+\|A\|_F^2$. For $k=2,3$, set

$$
H^{(k)}=\sum_{r=1}^k I^{\otimes(r-1)}\otimes H\otimes I^{\otimes(k-r)}.
$$

Flat one-register marginals imply zero generator mean in both probes. The pair probe has

$$
\operatorname{Var}_{\Phi}(H^{(2)})=4\|S\|_F^2/d.
$$

The real and imaginary vectors $S^{(3)}\tau$ and $iA^{(3)}\tau$ have no real cross term in their norm. Hence Section 5 gives

$$
\operatorname{Var}_{\tau}(H^{(3)})
\ge\frac{108}{41}\frac{\|A\|_F^2}{d}.
$$

Adding proves

$$
\operatorname{Var}_{\Phi}(H^{(2)})+
\operatorname{Var}_{\tau}(H^{(3)})
\ge\frac{108}{41}\frac{\|H\|_F^2}{d}.
$$

For completeness, if a Hermitian $K$ has spectrum in $[-\pi/2,\pi/2]$, a spectral decomposition with weights $p_a$ gives

$$
\begin{aligned}
1-|\langle e^{iK}\rangle|^2
&=2\sum_{a,b}p_ap_b\sin^2((\lambda_a-\lambda_b)/2)\\
&\ge\frac4{\pi^2}\operatorname{Var}(K).
\end{aligned}
$$

This uses $|\sin x|\ge2|x|/\pi$ for $|x|\le\pi/2$. Both $H^{(2)}$ and $H^{(3)}$ meet the spectral restriction because $\|H\|_{\rm op}\le\pi/6$. Applying this inequality twice gives the first claim. Finally,

$$
\operatorname{dist}_{\mathbb M}(U)
\le\|e^{iH}-I\|_F/\sqrt d\le\|H\|_F/\sqrt d,
$$

which gives the distance bound. QED.

## 7. A conditional statistical test

In each trial choose either probe with equal probability, apply $U$ to every register, and project onto the original probe. The rejection probability is $q=L(U)/2$.

Under the local promise, alternatives with $\operatorname{dist}_{\mathbb M}(U)\ge\delta$ satisfy

$$
q\ge\frac{216}{41\pi^2}\delta^2.
$$

With independent trials and acceptance only if every trial passes, the false-acceptance probability is at most

$$
\exp\left(-\frac{216}{41\pi^2}N\delta^2\right).
$$

Thus $N=O(\delta^{-2}\log(1/\alpha))$ trials suffice for error probability $\alpha$, conditional on trusted exact probe access. There are two or three calls to $U$ per trial. There is no established efficient preparation or measurement circuit, so this is not an end-to-end gate-complexity result.

The test establishes membership near **some** Monster element. It cannot determine which Monster element was used, because every element preserves both probes. It does not certify an assigned generator or the correctness of a complete group representation.

## 8. A global reduction that does not solve global stability

The pair probe alone controls the distance to phase-orthogonal matrices globally. Set

$$
a=|\operatorname{Tr}(UU^T)|/d,\qquad \ell_2(U)=1-a^2.
$$

Choose a phase so that $W=e^{-i\theta}U=X+iY$ has $\operatorname{Tr}(WW^T)=da\ge0$. Then

$$
\|Y\|_F^2=\frac d2(1-a),\qquad XX^T+YY^T=I.
$$

All singular values of $X$ are at most one. Taking a nearest orthogonal matrix $O$ to $X$ gives

$$
\frac{\|W-O\|_F^2}{d}
=2\left(1-\frac{\|X\|_*}{d}\right)
\le1-a\le\ell_2(U).
$$

Thus

$$
\min_{\theta,O\in O(d)}\frac{\|U-e^{i\theta}O\|_F}{\sqrt d}
\le\sqrt{\ell_2(U)}.
$$

Flat marginals also give the telescoping bound

$$
\|(W^{\otimes3}-O^{\otimes3})\tau\|
\le3\|W-O\|_F/\sqrt d.
$$

This reduces a global unitary-stability question to a global orthogonal cubic-stability question. It does not supply an explicit global constant for the latter, nor does a small normalized Frobenius distance imply the operator-norm radius required in Section 6.

Because the projective unitary group is compact and the exact zeros are isolated with nondegenerate transverse quadratic loss, some global square-root bound exists with an unspecified constant. Mere existence of this constant is not the research target. A useful explicit bound or a carefully demonstrated obstruction is needed.

## 9. Interpretation as a quantum reference frame

The pair of probe rays has collective stabilizer $\mathbb M$ inside $PU(d)$. Its orbit is therefore $PU(d)/\rho(\mathbb M)$: it specifies an orientation up to a finite Monster ambiguity. This is a reference-frame interpretation, not a way to distinguish Monster elements.

On the orthogonal tangent sector the tensor probe's Fubini--Study metric is the quadratic form in Section 5; the pure-state quantum Fisher information is four times that form. The continuous response is therefore known exactly even though the exact residual symmetry is finite. The resource-theoretic roles of symmetry subgroups and quantum geometric tensors are treated in [4]; no Monster-specific asymptotic conversion theorem is claimed here.

There is also a restricted probe-order statement. Absolute irreducibility gives no invariant vector in $V$ and only one invariant vector in $V\otimes V$, namely the metric state. Since the Monster has no nontrivial one-dimensional character, invariant rays add no exception. Consequently pure invariant probes with at most two copies, transforming collectively by this representation, cannot remove the continuous orthogonal ambiguity. A cubic probe together with the metric can. This is not a lower bound against arbitrary mixed-state, observable, or independently controlled protocols.

## 10. What remains before a publication claim

**Established literature:** Griess multiplication and automorphism group; trace identities; general quantum symmetry-testing and asymmetry frameworks.

**Derived in this note:** the normalized tensor contraction, scaled-projection reduction, exact orthogonal quadratic loss spectrum and multiplicities, local arbitrary-unitary bound, and conditional sample bound.

**Not established:** novelty of these deductions; a useful explicit global stability constant; efficient probe preparation; an advantage over simpler finite-symmetry probes; robustness to preparation error, leakage, nonunitary noise, or correlated uses; worst-case channel certification; a complete representation-verification protocol.

The most valuable next problem is quantitative global stability, followed by a resource analysis of preparing or replacing the cubic probe. Searching for equivalent projection or rigidity statements in Norton and subsequent Griess/Majorana-algebra literature is necessary before presenting the algebraic calculation as new. General symmetry testing already exists [3]; merely recasting an automorphism theorem as a fidelity test is not a sufficient novelty claim.

## 11. Reproducibility

Run `python verify_monster_local.py`. The script uses only the Python standard library. It reproduces the rational constants and multiplicities from the displayed input coefficients, checks the second-trace coefficient against Matsuo's general central-charge formula, and verifies the general contraction and commutator block identities on two small integer-valued symmetric tensors. It was also run with `python -O`, with byte-identical output. Checks use explicit exceptions rather than assertions.

The included `verification.json` is the captured output. These checks are not a computer construction or a numerical simulation of the Monster.

## References

[1] Atsushi Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169. Section 1.1 fixes normalization; Corollary 4.1 gives the trace inputs. https://arxiv.org/abs/math/0007169

[2] Gerald Höhn and Martin Seysen, *The Order of the Monster Finite Simple Group*, arXiv:2508.01037. Theorem 5.7 restates/proves the classical full-automorphism theorem and attributes its original proof to Tits. https://arxiv.org/abs/2508.01037

[3] Margarite L. LaBorde, Soorya Rethinasamy, and Mark M. Wilde, *Testing symmetry on quantum computers*, arXiv:2105.12758. This is relevant prior art, not a source of the Monster constants. https://arxiv.org/abs/2105.12758

[4] Koji Yamaguchi, Yosuke Mitsuhashi, Tomohiro Shitara, and Hiroyasu Tajima, *Quantum geometric tensor determines the pure-state i.i.d. conversion rate in the resource theory of asymmetry for any compact Lie group*, arXiv:2411.04766v4. https://arxiv.org/abs/2411.04766
