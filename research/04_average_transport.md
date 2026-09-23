# Average orbit transport and independent-device synchronization from Monster correlations

**Research checkpoint for Ruge Lin — 23 September 2026**

**Status.** Written derivations extending the supplied local, bipartite, and global-rounding checkpoints. Scalar/polynomial checks and small non-Monster tensor examples are reproducible. The arguments have not received independent review; novelty and efficient implementation are not established. The useful all-error bound below is for average transport of the axis ensemble, **not** a replacement for the previous tiny-threshold gate-to-Monster theorem.

## 1. Main statements

Use the traceless real Griess module, complexified for quantum operations, with

$$d=196883,\qquad\kappa=13858/3,\qquad M=46/\sqrt{141},\qquad\Delta=11161/13858.$$

Let $T$ be the real symmetric multiplication tensor, $\tau=T/\sqrt{d\kappa}$,

$$W|a\rangle=\kappa^{-1/2}\sum_{ij}T_{aij}|ij\rangle,\qquad P=WW^\dagger,\qquad\sigma=P/d.$$

Let $\mathcal A$ be the finite set of normalized traceless Ising axes, oriented so that $T(a,a,a)=M$. The pair-test rejection is

$$\epsilon(U)=1-\frac1d\operatorname{Tr}[P U^{\otimes2}P(U^\dagger)^{\otimes2}].$$

For a real orthogonal operation define the projective orbit-transport cost

$$\mathsf W(O)^2=\min_{s\in\{+1,-1\},\,\pi\in\operatorname{Sym}(\mathcal A)}
\frac1{|\mathcal A|}\sum_{a\in\mathcal A}\|sOa-\pi(a)\|^2.$$

For arbitrary complex unitary operations use

$$\mathsf W_{\mathbb C}(U)^2=\min_{\theta\in\mathbb R,\,\pi\in\operatorname{Sym}(\mathcal A)}
\frac1{|\mathcal A|}\sum_{a\in\mathcal A}\|e^{-i\theta}Ua-\pi(a)\|^2.$$

The same phase is used for every axis. No axis-dependent phases occur in these definitions. For real $O$, the complex phase optimization reduces to a sign, so these definitions agree. This follows because each assignment's averaged overlap is real. These costs match the canonically oriented vectors, modulo one common phase; they are not defined by independently optimizing the phase of each quantum ray. They bound the average output-state infidelity for the selected matching, but equivalence with a ray-only matching metric is not claimed.

**Theorem A — all-error real-orthogonal equivalence.** For every $O\in O(d)$,

$$\boxed{\frac14\epsilon(O)\le\mathsf W(O)^2\le
\min\left\{2,\frac{32M}{\Delta}\epsilon(O)\right\}
\le\min\{2,154\epsilon(O)\}.}$$

The numerical coefficient $32M/\Delta=153.9202296047\ldots$ has no hidden factor of $d$, $|\mathcal A|$, or $|\mathbb M|$. This is a theorem at the specified Monster dimension, not a claim about a dimension-parametrized family of Monsters.

**Theorem B — arbitrary complex unitaries.** For every $U\in U(d)$,

$$\boxed{\mathsf W_{\mathbb C}(U)^2\le\min\{2,23000\epsilon(U)\}.}$$

The calculated coefficient is $22684.629442\ldots$; 23000 is a rationally certified convenient overestimate. No prior real-structure or local-calibration promise is made. The price for complex operations comes from the earlier global real-structure reduction.

**Theorem C — two potentially different devices.** Define

$$\epsilon(U,V)=1-\frac1d\operatorname{Tr}[P(U\otimes V)P(U^\dagger\otimes V^\dagger)].$$

For arbitrary unitaries $U,V$,

$$\boxed{\epsilon(U,V)\ge\frac\Delta2
\left(1-\left|\frac{\operatorname{Tr}(U^\dagger V)}d\right|^2\right).}$$

Consequently, with projective normalized Frobenius distance

$$D_{\rm rel}(U,V)=\min_\theta\frac{\|U-e^{i\theta}V\|_F}{\sqrt d},$$

one has

$$D_{\rm rel}(U,V)\le\frac2{\sqrt\Delta}\sqrt{\epsilon(U,V)}<2.229\sqrt{\epsilon(U,V)}.$$

In particular, the full product-unitary stabilizer of $\sigma$ consists exactly of the pairs

$$(U,V)=(e^{i\theta}\rho(g),e^{i\phi}\rho(g)),\qquad g\in\mathbb M.$$

Thus equality of the two devices need not be assumed in the ideal unitary model: the same test enforces it projectively. This does not extend the result to arbitrary channels, leakage, or correlated multi-use noise.

## 2. Inputs retained and audited

The previous checkpoint derived the following facts from established Griess/VOA theory, using Norton's trace identities as presented by Matsuo, the real positive moonshine VOA, unitary Virasoro classification, and the Ising-axis identification. They remain mathematical inputs to the present continuation.

1. $\|T\|_F^2=d\kappa$ and all one-register marginals of $\tau$ are $I/d$.
2. $f(x):=T(x,x,x)$ on the real unit sphere has maximum $M$ exactly at $\mathcal A$. Every other sphere critical point has value at most $226/\sqrt{4893}$, more than $1/2$ below $M$.
3. For $a\in\mathcal A$, $L_a a=Ma$, while $L_a$ on $a^\perp$ has eigenvalues $-1/\sqrt{141}$, $11/\sqrt{141}$, and $1/(2\sqrt{141})$.
4. Distinct axes have distance at least $\sqrt{84/47}>1$.
5. The orbit moments obey
   $$\mathbb E_a aa^T=I/d,\qquad
   J:=\mathbb E_a a^{\otimes3}=\frac{M}{d\kappa}T.$$
6. The pair test and cubic ray-return loss satisfy globally
   $$\epsilon(U)\le\ell_3(U):=1-|\langle\tau|U^{\otimes3}|\tau\rangle|^2
   \le\frac2\Delta\epsilon(U).$$
7. With $K_R=48011041/787532$, there are a phase and an orthogonal $O$ such that
   $$\|e^{-i\theta}U-O\|_F/\sqrt d\le\sqrt{K_R\epsilon(U)}.$$
8. The matrix operator $C=P^{\Gamma_2}=\mathcal E S$, with $S$ swap/transposition and $\mathcal E(X)=\kappa^{-1}\sum_iL_iXL_i$, is self-adjoint. Its unique scalar eigenvalue is 1; its largest other eigenvalue is $r=2697/13858=1-\Delta$.

Item 2 uses the real positive-energy vacuum representation generated by a real idempotent; arbitrary complex critical points are not classified by that argument. All uses below respect this distinction. Item 5 uses the unique invariant cubic, verified in the previous checkpoint from exact character moments. It is not a spherical-three-design assertion: the cubic moment is nonzero.

The finite axis set is not generated or enumerated in this computation. Its moment identities and separation are used symbolically. The exact average relation in the next section is a deduction from item 5, not an independently sampled numerical observation.

## 3. The averaging identity that avoids the old dimension loss

For real $O$, put

$$\alpha(O)=\frac{\langle T,O^{\otimes3}T\rangle}{d\kappa}.
$$

Then

$$\mathbb E_a f(Oa)=\langle T,O^{\otimes3}J\rangle=M\alpha(O).$$

Because each $Oa$ is a real unit vector, every deficit

$$\delta_a(O):=M-f(Oa)$$

is nonnegative. Therefore

$$\boxed{\mathbb E_a\delta_a(O)=M[1-\alpha(O)].}$$

Replacing $O$ by $-O$ changes the sign of $\alpha$. With the better sign,

$$s(O)=1-|\alpha(O)|\in[0,1],\qquad
\ell_3(O)=s(O)[2-s(O)].$$

The previous uniform argument bounded each deficit by $\|O^{\otimes3}T-T\|_F$, bringing in the large norm $\sqrt{d\kappa}$. The exact average above does not contain that factor and is linear in the ray deficit rather than its square root.

The third moment determines this particular averaged cubic observable; it does not in general determine arbitrary probability distributions. The global localization of the maxima is essential to the subsequent inference.

## 4. A stronger finite-radius localization lemma

This section improves an intermediate radius, not the final gate-rounding theorem.

Fix an axis $a$, a real unit vector $x$, and $r=\|x-a\|\le1/2$. Write

$$q=\langle a,x\rangle=1-r^2/2,\qquad
x=qa+tv,\qquad v\perp a,\ \|v\|=1,\quad t^2=r^2(1-r^2/4).$$

Criticality of $a$ and cubic symmetry give

$$f(x)=Mq^3+3qt^2T(a,v,v)+t^3 f(v).$$

Since $q\ge7/8$, $T(a,v,v)\le11/\sqrt{141}$, and $f(v)\le M$,

$$M-f(x)\ge\frac{r^2}{\sqrt{141}}
\left[36-\frac{39}{4}r^2+\frac{13}{8}r^4
-46r(1-r^2/4)^{3/2}\right].$$

For $0\le r\le1/2$,

$$(1-r^2/4)^{3/2}\le1-r^2/4.$$

Thus the square bracket is at least

$$p(r)=36-46r-\frac{39}{4}r^2+\frac{23}{2}r^3+\frac{13}{8}r^4.$$

On this interval,

$$p'(r)\le-46+\frac{69}{8}+\frac{13}{16}=-\frac{585}{16}<0.$$

Also

$$p(1/2)=1549/128>\sqrt{141}.$$

Hence

$$\boxed{\|x-a\|\le1/2\quad\Longrightarrow\quad M-f(x)\ge\|x-a\|^2.}$$

The radius-$1/2$ balls around distinct axes are disjoint. Remove their interiors from the real unit sphere. The maximum on the remaining compact set lies either on a boundary, where the deficit is at least $1/4$, or at another sphere critical point, whose deficit exceeds $1/2$. It follows that

$$\boxed{M-f(x)<1/4\quad\Longrightarrow\quad
\text{a unique }a\in\mathcal A\text{ obeys }\|x-a\|<1/2,
\quad\|x-a\|^2\le M-f(x).}$$

No initial proximity is assumed in this last statement.

## 5. A global upper bound on deficit in terms of displacement

For any real unit $x$ and any axis $a$, put $h=x-a$, $r=\|h\|\le2$. Criticality and $a\cdot h=-r^2/2$ yield

$$M-f(x)=\frac32Mr^2-3T(a,h,h)-f(h).$$

Decompose $h=-(r^2/2)a+h_\perp$ and use the smallest tangent eigenvalue of $L_a$:

$$T(a,h,h)\ge\frac M4r^4-\frac1{\sqrt{141}}(r^2-r^4/4).$$

Since $f$ is homogeneous and odd, $|f(h)|\le Mr^3$. Consequently

$$M-f(x)\le Mr^2
\left[\frac{36}{23}+r-\frac{141}{184}r^2\right].$$

The scalar quadratic has maximum

$$\frac{36}{23}+\frac{46}{141}=\frac{6134}{3243}<2.$$

Therefore

$$\boxed{0\le M-f(x)\le2M\|x-a\|^2.}$$

This holds over the entire real unit sphere, not only near an axis.

## 6. Completing the good matches to a bijection

First fix the sign of $O$ so that $\alpha(O)\ge0$. Call an axis $a$ good when $\delta_a(O)<1/4$. By Section 4, it has a unique target $b(a)\in\mathcal A$ with

$$\|Oa-b(a)\|<1/2,\qquad \|Oa-b(a)\|^2\le\delta_a(O).$$

The map on good axes is injective. Otherwise, two distinct axes would have transformed distance less than one, contradicting their separation. Because the source and target sets have the same finite size, complete this injection arbitrarily to a bijection $\pi$ on all axes.

On a bad axis, any such match costs at most four, while $\delta_a\ge1/4$. Thus

$$\|Oa-\pi(a)\|^2\le16\delta_a$$

for every axis, and

$$\mathsf W(O)^2\le16M[1-|\alpha(O)|].$$

Conversely, Section 5 gives for any sign and bijection

$$M[1-\alpha(sO)]\le2M\mathbb E_a\|sOa-\pi(a)\|^2.$$

Minimizing shows

$$\boxed{\frac12[1-|\alpha(O)|]\le\mathsf W(O)^2
\le16M[1-|\alpha(O)|].}$$

This is an explicit comparison between a quantum overlap deficit and the classical quadratic transport distance between the two uniformly weighted finite point sets, modulo a global sign. The permutation form suffices as the definition; no algorithm for optimizing over all axes is asserted.

Since $s\le\ell_3\le2s$ and $\epsilon\le\ell_3\le2\epsilon/\Delta$,

$$\frac14\epsilon(O)\le\mathsf W(O)^2\le\frac{32M}{\Delta}\epsilon(O)<154\epsilon(O).$$

Finally, $\mathbb E_a a=0$ by nontrivial irreducibility. Averaging the assignment cost over uniformly random permutations gives exactly two. Therefore an assignment of cost at most two exists, justifying the stated trivial cap.

A slightly sharper real-orthogonal estimate, when $2\epsilon/\Delta\le1$, is

$$\mathsf W(O)^2\le16M\left[1-\sqrt{1-2\epsilon(O)/\Delta}\right],$$

whose leading small-error coefficient is $16M/\Delta\approx76.9601$. The coarse 154 coefficient is valid at every error level without cases.

## 7. Complex-unitary transfer with an explicit constant

Let $\epsilon=\epsilon(U)$. The earlier real-structure theorem supplies $\theta$ and $O$ with

$$\delta_R=\|e^{-i\theta}U-O\|_F/\sqrt d\le\sqrt{K_R\epsilon}.$$

The one-site maximally mixed marginals of $\tau$ and tensor-factor telescoping give

$$\|(e^{-i\theta}U)^{\otimes3}\tau-O^{\otimes3}\tau\|\le3\delta_R.$$

Pure-state ray distance obeys $d_{\rm ray}^2=2(1-|\langle v,w\rangle|)\le2\ell_3$. Using the triangle inequality for ray distance and the pair-to-cubic comparison gives

$$\sqrt{2[1-|\alpha(O)|]}
\le\left(3\sqrt{K_R}+\frac2{\sqrt\Delta}\right)\sqrt\epsilon.$$

Set

$$A_0=3\sqrt{K_R}+2/\sqrt\Delta,\qquad B_0=A_0^2/2.$$

Then $\mathsf W(O)^2\le16M B_0\epsilon$. Select its sign and optimal assignment, adjusting $\theta$ by $\pi$ if necessary. The tight-frame identity and the triangle inequality in the direct sum of axis-vector spaces yield

$$\mathsf W_{\mathbb C}(U)
\le\delta_R+\mathsf W(O)
\le\left[\sqrt{K_R}+\sqrt{8M}\,A_0\right]\sqrt\epsilon.$$

The squared coefficient is $22684.629442\ldots<23000$. A rational certificate uses

$$\sqrt{K_R}<781/100,\quad M<1937/500,
\quad 2/\sqrt\Delta<2229/1000,\quad\sqrt{8M}<557/100,$$

and squares the resulting rational upper bound. Thus Theorem B is global. The cap two follows as in Section 6, using $\mathbb E a=0$ even for complex $U$.

For any minimizing assignment and phase, Markov's inequality gives

$$\Pr_{a\sim\mathcal A}\{\|e^{-i\theta}Ua-\pi(a)\|\ge t\}
\le\min\{1,23000\epsilon(U)/t^2\}.$$

For real operations the coefficient is 154. Average pure-state output infidelity is also at most the corresponding assignment cost because

$$1-|\langle x,y\rangle|^2\le\|x-y\|^2$$

for unit vectors. These are average statements over the axis ensemble, not worst-case channel guarantees.

For example, a real orthogonal operation with ideal rejection at most $10^{-6}$ has RMS matched axis displacement at most $\sqrt{154\cdot10^{-6}}<0.01241$. There exists one bijection and one common sign for which no more than 1.54% of axes have displacement at least 0.1. For arbitrary complex unitaries, rejection $10^{-8}$ similarly bounds the RMS cost by $\sqrt{23000\cdot10^{-8}}<0.01517$ and that fraction by 2.3%. These are conditional mathematical illustrations, not experimental results or claims of feasible probe access.

## 8. Synchronization of independently chosen local unitaries

Let $S$ be swap and $\omega=(U\otimes V)\sigma(U^\dagger\otimes V^\dagger)$. Since the support of $P$ is symmetric,

$$I-P\succeq (I-S)/2.$$

Write $D=U^\dagger V$. Using $SP=P$,

$$\operatorname{Tr}(S\omega)
=\frac1d\operatorname{Tr}[P(D\otimes D^\dagger)]
=\frac1d\langle\operatorname{vec}D,C\operatorname{vec}D\rangle,$$

where $C=P^{\Gamma_2}=\mathcal E S$. The last identity follows directly from the real symmetric tensor contractions; it is checked on small complex-unitary examples by the new verifier.

The scalar eigenspace of $C$ is spanned by $\operatorname{vec}I$, with eigenvalue one, and $C\le rI+(1-r)|\Phi\rangle\langle\Phi|$. Since $\|D\|_F^2=d$,

$$\operatorname{Tr}(S\omega)\le r+(1-r)|\operatorname{Tr}D/d|^2.$$

Therefore

$$\epsilon(U,V)\ge\frac{1-\operatorname{Tr}(S\omega)}2
\ge\frac\Delta2[1-|\operatorname{Tr}D/d|^2].$$

Let $a=|\operatorname{Tr}D|/d\in[0,1]$. Then

$$D_{\rm rel}(U,V)^2=2(1-a),\qquad
1-a^2\ge D_{\rm rel}(U,V)^2/2,$$

which proves the announced distance estimate.

At zero rejection, $D$ is scalar, so $U$ and $V$ agree projectively. The earlier collective stabilizer theorem then implies that both equal the same Monster element up to separate phases. This identifies the full product-unitary stabilizer of $\sigma$; it is not the much larger stabilizer under arbitrary entangling unitaries on the entire bipartite space.

The same argument applied to all pair marginals shows that the product-unitary ray stabilizer of $\tau$ consists of triples

$$(U_1,U_2,U_3)=(e^{i\theta_1}\rho(g),e^{i\theta_2}\rho(g),e^{i\theta_3}\rho(g)).$$

### 8.1 Reducing the unequal-device test to the previous test

Use the phase aligning $U$ and $V$. The leakage amplitude expression and $\operatorname{Tr}_1P=I$ give

$$\sqrt{\epsilon(U,U)}
\le\sqrt{\epsilon(U,V)}+D_{\rm rel}(U,V)
\le(1+2/\sqrt\Delta)\sqrt{\epsilon(U,V)}.$$

The same holds for $V$. Consequently

$$\mathsf W_{\mathbb C}(U)^2,\;\mathsf W_{\mathbb C}(V)^2
\le240000\epsilon(U,V),$$

using $23000(1+2/\sqrt\Delta)^2<240000$. These transport assignments need not be identical; the separate relative-unitary estimate supplies the direct synchronization statement.

No averaging over random Kraus operators is used. Extending these inequalities to general noisy channels requires additional arguments and is not claimed here.

## 9. What this does not prove

The transport permutation is an arbitrary bijection of the finite axis set. At nonzero error we have not proved that it is induced by one Monster element. In particular,

$$\mathsf W_{\mathbb C}(U)\le D_{\mathbb M}(U)$$

follows by restricting assignments to actual group actions and using the tight frame, but the reverse implication with a useful explicit constant remains unestablished. The old $10^{-25}$ sufficient threshold for a small-prefactor gate-distance certificate is not silently replaced by $10^{-6}$ or $10^{-8}$.

The all-error result gives an operationally different, weaker conclusion: the axis ensemble is nearly preserved as an unlabeled geometric distribution. Both distances have exactly the same zero set, but that does not make them quantitatively interchangeable.

There is no efficient computation of the best assignment, nearest axis, or nearest Monster element. The proof uses the huge orbit analytically; it does not enumerate it. Likewise, trusted preparation of $\sigma$ and measurement of $P$ remain resources whose efficient implementation is unproved. Sampling estimates must include confidence bounds; an observed frequency is not automatically the exact ideal rejection probability.

The synchronization theorem removes the equality-of-two-unitaries assumption. It does not remove unitarity, known logical-subspace, no-leakage, trusted-probe, or temporal-independence requirements for repeated statistical trials. Nor does it certify a specified named Monster generator.

## 10. General principle and priority comparison

The matching proof extends beyond the Monster. Suppose a real cubic has a finite set $\mathcal A$ of unit maximizers, its third orbit moment is proportional to its coefficient tensor, and the maxima are uniformly quadratically isolated within disjoint balls. A gap below the top critical value makes the quadratic isolation a global near-maximizer statement. Averaged cubic deficit then controls a bijective quadratic transport cost: retain the injective good matches and complete the few bad matches arbitrarily. A global upper bound of deficit by squared displacement provides the converse comparison.

This is not a general theorem that finitely many moments determine all distributions, and it does not prove quantitative rounding to an exact automorphism for arbitrary point sets.

Existing spherical-code rigidity and stability results are relevant but answer different questions. Cohn, Jiao, Kumar, and Torquato study deformations of spherical packings up to global isometry. Böröczky and Glazyrin study stability of Delsarte-tight codes under relaxed maximal-inner-product constraints, including E8 and Leech cases. Here $O\mathcal A$ already has exactly the same internal Gram matrix as $\mathcal A$ under its original labels, so a theorem comparing shapes after an arbitrary global isometry does not by itself identify whether that isometry lies near the discrete stabilizer. We instead compare both copies in the same ambient coordinates through a cubic overlap.

The mechanism, the quantum test, and the special constants still require a full priority audit. No search result establishes that these deductions are new. Norton's original 1996 chapter has still not been obtained and completely read. The quantum symmetry-testing and reference-frame literature also remains necessary context, not a novelty claim.

## 11. Sources and readback scope

- **Matsuo (2000):** *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, https://arxiv.org/abs/math/0007169. Section 1.1 supplies the idempotent-to-Virasoro identification; Section 3.2, printed p. 14, gives the c=1/2 multiplication spectrum. The latter page was inspected with the PDF screenshot tool in this continuation. Corollary 4.1 was the trace input to the earlier checkpoint.
- **Wassermann (2010):** *Direct proofs of the Feigin–Fuchs character formula for unitary representations of the Virasoro algebra*, https://arxiv.org/abs/1012.6003. The introduction states the positive-energy unitary classification used for the critical-value gap. Text was read; the attempted screenshot did not load.
- **Höhn–Seysen (2025):** *The Order of the Monster Finite Simple Group*, https://arxiv.org/abs/2508.01037. Lemma 2.4 and the full-automorphism/Ising-axis identifications are algebraic inputs, with the normalization conversion recorded in the prior checkpoint. HTML and parsed PDF text were read; attempted PDF screenshots did not load in this continuation.
- **Hall–Rehren–Shpectorov (2013):** *Universal axial algebras and a theorem of Sakuma*, https://arxiv.org/abs/1311.0217. The finite inner-product alphabet, read and transcribed in the prior checkpoint, is used here only through axis separation greater than one.
- **Cohn–Jiao–Kumar–Torquato (2011):** *Rigidity of spherical codes*, https://arxiv.org/abs/1102.5060. Existing rigidity context; the abstract was checked, not the complete paper.
- **Böröczky–Glazyrin:** *Stability of optimal spherical codes*, https://arxiv.org/abs/1711.06012; published in *Monatshefte für Mathematik* 205 (2024), 455–475. Definitions and Theorems 2–4 were read in the preprint text. The comparison above does not rely on its tables.
- **LaBorde–Rethinasamy–Wilde (2023):** *Testing symmetry on quantum computers*, https://arxiv.org/abs/2105.12758. Existing quantum symmetry-testing framework; the abstract was checked again in this continuation, not the complete paper.
- **Prior project checkpoints:** all algebraic normalizations, channel spectrum, pair/cubic comparison, real-structure reduction, unique invariant cubic, and tiny-threshold gate theorem are preserved unchanged in `previous/Monster_Global_Rounding_Checkpoint.zip` and its nested earlier archives.

## 12. Reproducibility and claim ledger

`verify_average.py` uses the standard library and checks exact polynomial identities, rational inequalities certifying the constants, and the prior-archive hash. Checks are explicit exceptions, not removable assertions. Normal, `-O`, and `-OO` execution must produce the same deterministic JSON report.

`verify_average_toy.py` uses NumPy with deterministic small examples in dimensions 3 and 4. It checks orbit-moment averaging, explicit good-match completion, exact optimal assignment by enumerating at most 120 permutations, pair/cubic comparisons, and the complex-unitary swap/synchronization contractions. It does not numerically test the full Monster tensor or independently establish the Monster's geometric inputs. The largest matrix in the new toy checks has dimension 64.

`rerun_previous.py` replays the old global, pair-exact, pair-toy, and local verifiers in temporary directories, comparing their output byte-for-byte with the preserved reports. It verifies the nested archive manifests before execution. A new manifest covers this checkpoint's payload; the previous archive is unchanged.

**Derived here:** average cubic-deficit identity as used for transport; radius-1/2 localization; all-error orbit-transport bounds; product-unitary synchronization and full local-unitary stabilizers; a general good-matching completion lemma.

**Established inputs:** Griess/Monster/VOA structure, unitary Virasoro classification, Ising-axis geometry, and the sources underlying the previous derived channel identities.

**Not established:** novelty; independent review; practical probe preparation or measurement; useful all-error rounding to a single Monster gate; general channels; device independence; leakage handling; worst-case channel-error or quantum advantage claims.
