# Global small-loss rounding of the Monster correlation test

**Research checkpoint for Ruge Lin — 23 September 2026**

**Status:** a written derivation using established Griess/VOA facts and the previous bipartite-correlation checkpoint. The scalar calculations and character-data identities are reproducibly checked; this is not an independent review of the proof, a novelty claim, or an efficient experimental protocol. The explicit threshold obtained below is far too small for a practical sampling-based certificate.

## 1. Main statement and what changed

Let $V$ be the real traceless Griess module, $d=196883$, complexified for quantum operations. Retain the previous normalization

$$
\kappa=\frac{13858}{3},\qquad
W|a\rangle=\frac1{\sqrt\kappa}\sum_{ij}T_{aij}|ij\rangle,
\qquad P=WW^\dagger,\qquad\sigma=P/d.
$$

For a fixed unitary $U\in U(d)$ define the ideal pair-test rejection probability

$$
\epsilon(U)=1-\frac1d\operatorname{Tr}\left[P U^{\otimes2}P(U^\dagger)^{\otimes2}\right],
$$

and normalized projective gate distance

$$
D_{\mathbb M}(U)=\min_{\theta\in\mathbb R,\,g\in\mathbb M}
\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt d}.
$$

**Derived theorem.** For every such $U$,

$$
\boxed{\epsilon(U)\le10^{-25}\quad\Longrightarrow\quad
D_{\mathbb M}(U)\le
\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}
<1.151\sqrt{\epsilon(U)}.}
$$

There is **no prior proximity or calibration promise**. The threshold applies to the true ideal rejection probability, not an unqualified empirical frequency. Trusted access to $\sigma$ and $P$, a known invariant logical subspace, and the same fixed unitary on both queried registers are assumed. General noisy channels, leakage, unknown probe preparations, and worst-case channel distance are not covered.

The previous theorem gave the same square-root estimate conditional on a small operator-norm logarithm around a Monster operation. The new argument first puts an arbitrary low-loss unitary into that neighborhood, using the finite geometry of the Ising axes and a critical-value gap supplied by unitary Virasoro representation theory.

An all-loss, very weak consequence is

$$
D_{\mathbb M}(U)\le
\min\{\sqrt2,\sqrt{2\cdot10^{25}}\sqrt{\epsilon(U)}\}.
$$

This follows from the displayed theorem below the threshold and the trivial projective bound $D_{\mathbb M}\le\sqrt2$ above it. It is included to make the global quantifiers explicit, not as a useful robustness constant.

## 2. Literature and computational inputs

**[M00]** A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169, https://arxiv.org/abs/math/0007169. Section 1.1 identifies a weight-two vector $v$ satisfying $v^2=2v$ with a Virasoro action of central charge $2\langle v,v\rangle$, with the mode adjoint relation provided by the invariant form. Corollary 4.1 supplies the trace identities used in the previous checkpoint. The positive real form of the moonshine VOA is essential. Matsuo uses “idempotent” for $v^2=2v$; this note reserves that word for $e^2=e$, so $v=2e$ and $c=8\|e\|^2$.

**[W10]** A. Wassermann, *Direct proofs of the Feigin–Fuchs character formula for unitary representations of the Virasoro algebra*, arXiv:1012.6003, https://arxiv.org/abs/1012.6003. Introduction, pp. 1–2, states the Friedan–Qiu–Shenker unitary classification: $c\ge1$ or $c=1-6/[m(m+1)]$, $m\ge2$; $c=0$ gives the trivial representation. Thus nonzero unitary vacuum representations have $c\ge1/2$, and any value other than $1/2$ is at least $7/10$. The classification is an established input, not derived here.

**[HS25]** G. Höhn and M. Seysen, *The Order of the Monster Finite Simple Group*, arXiv:2508.01037, https://arxiv.org/abs/2508.01037. Lemma 2.4 gives the axis multiplication spectrum; Definition 2.12 and Theorem 2.13 identify Ising vectors and 2A-like involutions; Theorems 5.7–5.8 identify the complete automorphism group and show the axes constitute the 2A orbit. These are used as statements of established Monster theory. Their Griess inner product is half the VOA-normalized form used here. Their axis $v$ has $v^2=16v$; our true idempotent is $e=v/16$, with VOA norm squared $1/16$.

**[HRS13]** J. I. Hall, F. Rehren and S. Shpectorov, *Universal axial algebras and a theorem of Sakuma*, arXiv:1311.0217, https://arxiv.org/abs/1311.0217. Section 6 defines the form coefficients; Lemmas 8.2–8.3 and the table on printed p. 22 give the finite inner-product alphabet for axes of norm one. The table was inspected as an image. The two types 3C and 4B have the same first inner-product value; we use a set of values, not a claim that a single inner product distinguishes all nine types.

**[ATLAS/GAP]** Thomas Breuer's ordinary character table of the Monster, ATLAS origin, distributed in `jmichel7/gap3-jm`, commit `64365f30757f5374c86511b377d7d98eb15c1e02`, file `tbl/ctomonst.tbl`, blob `cece771b31a8d764cc3c34428cffa7959fa0747a`. Centralizer orders and the degree-196883 character were read through the GitHub connector, lines 2110–2129 and 2264–2270. The integer arrays in `monster_character_excerpt.json` are a transcription, not a byte-identical source archive. Pinned source: https://github.com/jmichel7/gap3-jm/blob/64365f30757f5374c86511b377d7d98eb15c1e02/tbl/ctomonst.tbl . Official table metadata: https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/M.html . The official current package archive was not downloaded; no claim is made to have run GAP or audited the entire character table.

**[PAIR]** The preceding checkpoint, *Monster symmetry from bipartite correlations*, preserved unchanged in the attached prior archive. Its relevant derived inputs are reproduced in Section 3. The verifier reruns do not independently prove its Monster-sized spectral identities.

Priority remains unestablished. In particular, Norton's original 1996 chapter, *The Monster algebra: some new formulae*, has not been obtained and completely audited. Searches did not produce a reliable exhaustive comparison with prior approximate-automorphism or tensor-rigidity results. Absence of a matching search result is not evidence of novelty.

## 3. Previous quantum-test bounds used in the proof

Set

$$
\Delta=\frac{11161}{13858},\qquad
K_R=\frac{48011041}{787532},\qquad
c_{\rm loc}=\frac{12528}{1681\pi^2}.
$$

Let $|\tau\rangle=T/\sqrt{d\kappa}$ and $|\Phi\rangle=d^{-1/2}\sum_i|ii\rangle$.

The preceding checkpoint proves, for all $U$,

$$
\ell_3(U):=1-|\langle\tau|U^{\otimes3}|\tau\rangle|^2
\le\frac2\Delta\epsilon(U),
$$

$$
\min_{\theta,O\in O(d)}\frac{\|U-e^{i\theta}O\|_F^2}{d}
\le\ell_2(U):=1-|\operatorname{Tr}(UU^T)/d|^2
\le K_R\epsilon(U).
$$

The first uses the unique-ground-state gap of $(I-P)_{12}+(I-P)_{23}$. The second uses the separation of opposite transpose parities in the partial-transpose spectrum of $P$, followed by a real-part polar decomposition. Both are global but neither alone rounds to the Monster.

The local result is

$$
U=e^{i\theta}\rho(g)e^{iH},\quad \operatorname{Tr}H=0,
\quad\|H\|_{\rm op}\le\pi/4
\quad\Longrightarrow\quad
\epsilon(U)\ge c_{\rm loc}D_{\mathbb M}(U)^2.
$$

All single-register marginals of $\tau$ are $I/d$.

## 4. Cubic critical points become Virasoro subalgebras

Write the full real Griess algebra as $B=\mathbb Rt\oplus V$, with

$$
t=\omega/\sqrt{12},\qquad s=1/\sqrt3,
\qquad t^2=st,\quad tx=sx,\quad
xy=\mu(x,y)+s\langle x,y\rangle t.
$$

The identity is $t/s$ and has squared norm 3. Define

$$f(x)=T(x,x,x),\qquad \|x\|=1.$$

The Lagrange-multiplier equation at a sphere critical point is

$$\mu(x,x)=\lambda x,\qquad\lambda=f(x).$$

For any real $\lambda$ solving this equation put

$$
D_\lambda=\sqrt{\lambda^2+4/3},\qquad
b=D_\lambda^{-1},\qquad
n=\frac32\left(1-\frac\lambda{D_\lambda}\right),\qquad
\alpha=sn,
$$

$$e=\alpha t+bx.$$

Direct substitution gives

$$e^2=e,\qquad\|e\|^2=n,\qquad0<n<3.$$

For example, the $x$ coefficient condition is $2s\alpha+b\lambda=1$, and the scalar condition is $s(\alpha^2+b^2)=\alpha$. Equivalently,

$$
b^2=n-n^2/3,\qquad
\lambda(n)=\frac{1-2n/3}{\sqrt{n-n^2/3}},
\qquad
\lambda'(n)=-\frac1{2(n-n^2/3)^{3/2}}<0.
$$

The vector $2e$ generates a Virasoro vacuum representation with central charge

$$c=8n.$$

This vacuum representation is positive-energy and unitary: the real invariant positive form gives $L_m^\dagger=L_{-m}$, and descendants of the vacuum carry their usual nonnegative integral Virasoro levels, also equal to their original VOA weight. Thus the unitary classification applies even though a general idempotent is not assumed in advance to be an Ising axis.

The smallest nonzero possible $n$ is $1/16$, and any different $n$ is at least $7/80$. The $n=1/16$ vectors are precisely the real Ising idempotents. Their normalized traceless parts form a finite Monster orbit $\mathcal A$.

It follows that

$$
\boxed{M_f:=\max_{\|x\|=1}f(x)=\frac{46}{\sqrt{141}},
\qquad\operatorname{argmax}f=\mathcal A.}
$$

Every other sphere critical point obeys

$$
f(x)\le\lambda(7/80)=\frac{226}{\sqrt{4893}}\approx3.2308800248.
$$

Here $M_f\approx3.8738988369$. In particular,

$$M_f>19/5,\qquad \lambda(7/80)<33/10,$$

so the top critical-value gap is greater than $1/2$. We do **not** claim that the next allowed bound $\lambda(7/80)$ is attained in the moonshine algebra; an upper bound is sufficient.

## 5. Quantitative isolation of the maxima

For an Ising idempotent $e$, the multiplication spectrum on $B$ is

$$\operatorname{spec}R_e=\{1,0,1/4,1/32\},$$

with the 1-eigenspace one-dimensional. Its decomposition is

$$e=\frac1{16\sqrt3}t+\frac{\sqrt{141}}{48}a,\qquad a\in\mathcal A.$$

The space $a^\perp\cap V$ is orthogonal to both $t$ and $e$ and invariant under $R_e$. On it, the possible eigenvalues of $L_a$ are

$$\frac{-1}{\sqrt{141}},\qquad
\frac{11}{\sqrt{141}},\qquad
\frac{1}{2\sqrt{141}}.$$

The sphere Hessian $6L_a-3M_fI$ therefore has eigenvalues $-144/\sqrt{141}$, $-72/\sqrt{141}$ and $-135/\sqrt{141}$.

A finite-radius bound, rather than just a Hessian statement, is needed. Let $r=\|x-a\|\le1/10$, $q=\langle a,x\rangle=1-r^2/2$, and write $x=qa+tv$ with $v\perp a$, $\|v\|=1$, $t^2=1-q^2\le r^2$. Tensor symmetry and criticality imply

$$f(x)=M_fq^3+3qt^2T(a,v,v)+t^3f(v).$$

Using $T(a,v,v)\le11/\sqrt{141}$ and $|f(v)|\le M_f$ gives

$$
M_f-f(x)\ge
\left[\frac{36}{\sqrt{141}}-\frac{3M_f}{4}r^2-M_fr\right]r^2
\ge2r^2.
$$

The last inequality follows already from $36/\sqrt{141}>3$, $M_f<4$, $r\le1/10$.

**Global superlevel localization.** Remove all open radius-$1/10$ balls around the finite set $\mathcal A$ from the unit sphere. A maximum of $f$ on the remaining compact set is either on a ball boundary, where $f\le M_f-1/50$, or is a sphere critical point outside $\mathcal A$, where $f<M_f-1/2$. Therefore

$$
\boxed{M_f-f(x)<1/50\ \Longrightarrow\
\exists a\in\mathcal A:\quad
\|x-a\|<1/10,\quad\|x-a\|^2\le\frac{M_f-f(x)}2.}
$$

The axis is unique because distinct normalized axes have separation greater than one, as shown next. This is a global lemma: no initial proximity to any axis is assumed.

## 6. A finite alphabet turns approximate axis motion into an exact symmetry

The Norton–Sakuma alphabet for norm-one axes is

$$Q=\{1,0,1/8,1/64,13/256,1/32,3/128,5/256\}.$$

In our VOA normalization $\langle e,e'\rangle=q/16$. For normalized traceless axes $a,b$ this becomes

$$\langle a,b\rangle=\frac{48q-1}{47},\qquad q\in Q.$$

The minimum separation between different allowed inner-product values is

$$\eta=3/752,$$

and the minimum Euclidean distance between distinct axes is at least

$$s_{\mathcal A}=\sqrt{84/47}>1.$$

Suppose $O\in O(d)$ and for every axis $a$ there is $\pi(a)\in\mathcal A$ with

$$\|Oa-\pi(a)\|\le h,\qquad 2h<\min\{\eta,s_{\mathcal A}\}.$$

The map $\pi$ is injective, hence a permutation of the finite axis set. Also,

$$|\langle\pi(a),\pi(b)\rangle-\langle a,b\rangle|\le2h<\eta.$$

Both quantities belong to the finite alphabet, so they are equal. The axes span $V$ because they form a nonzero orbit in an irreducible module. Thus $\pi$ extends to an orthogonal linear map $R$.

To identify $R$ with a Monster element, rather than merely an axis-code isometry, use the exact character identities checked from the supplied table excerpt:

$$
\frac1{|\mathbb M|}\sum_{g\in\mathbb M}\chi(g)^m
=\sum_{\text{classes }C}\frac{\chi(C)^m}{|C_{\mathbb M}(g_C)|}
=\begin{cases}1&m=0,\\0&m=1,\\1&m=2,\\1&m=3,\\6&m=4.\end{cases}
$$

In particular $\dim(V^{\otimes3})^{\mathbb M}=1$. The real cubic $T$ spans this invariant line. The orbit moments satisfy

$$
\frac1{|\mathcal A|}\sum_{a\in\mathcal A}aa^T=I/d,
\qquad
J:=\frac1{|\mathcal A|}\sum_{a\in\mathcal A}a^{\otimes3}
=\frac{M_f}{d\kappa}T.
$$

The second identity follows by invariance and $\langle T,J\rangle=M_f\ne0$. Any orthogonal permutation of the axes preserves $J$ and hence $T$. Extending $R$ to fix $t$ therefore gives an automorphism of the full Griess algebra. By [HS25], $R=\rho(g)$ for some $g\in\mathbb M$.

Finally, the tight-frame identity yields

$$
\boxed{\frac{\|O-R\|_F^2}{d}
=\frac1{|\mathcal A|}\sum_{a\in\mathcal A}\|Oa-Ra\|^2\le h^2.}
$$

The character moments and alphabet gaps are checked using exact integer/rational arithmetic. This is not a numerical construction of all axes or a classification proof from first principles.

## 7. From observed-test parameter to uniformly approximate axis preservation

Let $\epsilon=\epsilon(U)$. Section 3 gives a phase and $O\in O(d)$ such that

$$\delta_R:=\frac{\|e^{-i\theta}U-O\|_F}{\sqrt d}\le\sqrt{K_R\epsilon}.$$

Since $\tau$ has single-register marginals $I/d$, telescoping the three tensor factors gives

$$\|(e^{-i\theta}U)^{\otimes3}\tau-O^{\otimes3}\tau\|
\le3\delta_R.$$

Indeed each of the three telescoping summands has squared norm $\|e^{-i\theta}U-O\|_F^2/d$; unitaries on the other registers do not change that norm.

For pure-state rays, $d_{\rm ray}(v,w)=\sqrt{2-2|\langle v,w\rangle|}\le\sqrt{2(1-|\langle v,w\rangle|^2)}$. Consequently

$$
d_{\rm ray}(O^{\otimes3}\tau,\tau)
\le\left(3\sqrt{K_R}+\frac2{\sqrt\Delta}\right)\sqrt\epsilon.
$$

Because $O$ and $T$ are real and the tensor degree is odd, replacing $O$ by $-O$ if necessary makes the overlap nonnegative. Adjusting the phase by $\pi$ preserves $\delta_R$. Thus, with this sign choice,

$$
\|O^{\otimes3}T-T\|_F\le C_T\sqrt\epsilon,
$$

$$
C_T=\sqrt{d\kappa}\left(3\sqrt{K_R}+\frac2{\sqrt\Delta}\right)
=773609.503738\ldots<800000.
$$

For every axis $a$, the same norm bounds

$$0\le M_f-f(Oa)\le C_T\sqrt\epsilon.$$

Here the contraction uses $(O^T)^{\otimes3}T-T$; its norm equals that of $O^{\otimes3}T-T$ by orthogonality. This is the deliberately coarse average-to-uniform step in the argument.

## 8. Explicit threshold and removal of the local promise

Assume $\epsilon\le10^{-25}$. Use the rational overestimates

$$
\sqrt\epsilon<\frac1{3\cdot10^{12}},\qquad
C_T<800000,
$$

so

$$
C_T\sqrt\epsilon<\frac{800000}{3\cdot10^{12}}
<\frac1{2000000}=2\left(\frac1{2000}\right)^2<\frac1{50}.
$$

Global superlevel localization places every $Oa$ within $h=1/2000$ of a unique axis. Since $2h=1/1000<3/752$, Section 6 gives $R=\rho(g)$ with

$$\|O-R\|_F/\sqrt d<h.$$

Also $K_R<64$ and $\sqrt d<444$, hence

$$
\|e^{-i\theta}U-R\|_{\rm op}
\le\sqrt d\left(\delta_R+h\right)
<444\left(\frac8{3\cdot10^{12}}+\frac1{2000}\right)<\frac14.
$$

Put $Q=R^\dagger e^{-i\theta}U$. Its principal logarithm $H_0$ is Hermitian and satisfies

$$\|H_0\|_{\rm op}\le\frac\pi2\|Q-I\|_{\rm op}<\pi/8.$$

This is the elementary eigenphase chord inequality on $[-\pi,\pi]$. Subtracting the mean eigenphase gives

$$H=H_0-\frac{\operatorname{Tr}H_0}{d}I,
\qquad\operatorname{Tr}H=0,\quad\|H\|_{\rm op}<\pi/4.$$

Absorbing the subtracted scalar into the global phase yields precisely the hypothesis of the previous local theorem. Applying it proves Section 1.

All coarse numerical implications above are certified by rational comparisons. Decimals are for readability only. The original threshold can be improved by optimizing the estimates, but that alone would not address the large losses in converting average correlation damage to preservation of every axis.

## 9. General mechanism isolated by this example

A real cubic with a finite maximizing orbit can provide a global rounding mechanism when three ingredients are controlled: a gap between its top critical value and every other critical value, quantitative local curvature at the maxima, and a separated finite alphabet of pairwise inner products whose preserving permutations determine the intended symmetry.

The critical-value gap excludes distant nearly maximizing components. Curvature converts height deficit into distance from the finite orbit. Alphabet separation converts approximate preservation into exact relations. A frame identity then translates motion of the finite orbit into matrix distance. Local differential rigidity can finally upgrade the exponent from the coarse rounding estimate to a square-root gate bound.

For the Monster, the extra source of global information is unitary Virasoro representation theory. This is more specific than invoking compactness and is distinct from the earlier parent-Hamiltonian gap, which certifies states rather than operations.

The spherical-code language is geometric. No quantum error-correcting code, recovery channel for arbitrary quantum information, or fault-tolerance theorem is constructed here. Nor does the proof supply an efficient procedure for finding the nearest axis or Monster element: the rounding is existential and uses the whole finite orbit in the analysis.

## 10. What remains open in this project

**Mathematical priority.** The classical characterization of axes and the underlying geometry are not new. The exact overlap with existing Griess rigidity, spherical-code stability, and symmetry-testing literature is not settled. The present proof must not be sold as a first result without further audit.

**Useful robustness.** The explicit $10^{-25}$ threshold removes a logical promise but is not useful for ordinary sampling. With independent Bernoulli trials and zero rejections, the one-sided $(1-\alpha)$ confidence upper limit is $1-\alpha^{1/N}$. To put this below $10^{-25}$ at 95% confidence requires approximately $2.996\times10^{25}$ trials, even with perfect preparation and measurement. This is a property of the current conservative certificate, not a proven lower bound on all possible Monster tests.

**Better route.** Avoid controlling every axis by the Frobenius norm of the full multiplication tensor. A robust, average-case version of the finite relational geometry, or a better operator-to-axis estimate, could reduce the threshold loss. Merely polishing the displayed constants is unlikely to make the certificate experimentally useful.

**Operational scope.** Efficient preparation of $\sigma$, efficient measurement of $P$, leakage, general channels, temporal correlations, device independence, and worst-case gate-error bounds remain untreated. The register counts from earlier notes are not implementation costs.

**Review.** This checkpoint supplies a proof for mathematical scrutiny, not independent validation. Verification scripts check the exact scalar and character identities and replay earlier small examples; they do not simulate the 196883-dimensional Monster representation or reproduce the VOA classification from first principles.

## 11. Reproducibility

Run `python verify_global.py` or `python -O verify_global.py`. Both use only the standard library, fail with explicit exceptions rather than removable assertions, and emit identical deterministic reports. The verifier checks the character moments, finite alphabet, normalization and idempotent scalar identities, critical-value and curvature comparisons, and every coarse threshold inequality used in the proof. It also verifies the SHA-256 of the character-data file.

The previous checkpoint ZIP is preserved byte-for-byte in `previous/`. Its original exact and NumPy toy verifiers were rerun in a temporary extraction with single-threaded linear algebra; reports and exit statuses are recorded in `verification_previous_rerun.json`. The old archive is not silently edited to insert the new claims. A SHA-256 manifest records all payload files of this checkpoint.
