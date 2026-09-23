# VOA-to-extremum proof audit

**Date:** 23 September 2026.

**Audited base:** [`0376cbfb8e8640d1b278b5c55c4815d83f5b6ca1`](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/tree/0376cbfb8e8640d1b278b5c55c4815d83f5b6ca1).

**Branch:** `audit/voa-extrema`.

**Assignment:** the first bounded assignment in [INDEPENDENT_AUDIT.md](../work_orders/INDEPENDENT_AUDIT.md).

## Outcome and scope

**PASS for the bounded VOA-to-extremum dependency, with the explicit proof details below. No blocking gap or counterexample was found in this dependency.** Two nonblocking errors are recorded: a complementary-norm typo in an external source (V12), and downstream strict inequalities that fail at zero error (V13). The latter needs a correction to the literal C12 statement. This is a fresh assistant reconstruction, with separate checks of the VOA hypotheses, axis correspondence, and localization argument. It is not independent human or specialist review, formal verification, or a correctness certificate for all five notes.

The potentially dangerous implication is valid here because the algebra is the weight-two part of the **positive real moonshine VOA**, not merely a positive metrized algebra. The Virasoro classification is applied to the cyclic vacuum module of the reconstructed vector. Its grading, adjoints, and closure can all be justified without assuming that vector is already an Ising vector. The proof does not need positivity of its energy operator on the entire ambient VOA.

The narrow repair is to make rounded error bounds non-strict at zero, and add an explicit proof supplement: cite full-VOA positivity precisely, distinguish the two conformal vectors, justify the cyclic module, and give the exact source for the Ising normalization. No theorem constant or threshold needs changing on the evidence of this audit. Historical notes, data, checkers, reports, archives, and LICENSE are unchanged. The integration workspace retains responsibility for claim-ledger edits and the rest of the proof audit.

The repository was freshly cloned before mathematical work. Both Git refs and the GitHub branch listing showed only `main` and `staging/monster-seed`; the GitHub PR search returned no pull requests. The audited commit was the current `main`, verified rather than assumed from the assignment. The unused audit branch was created from that commit.

## Findings

Here **PASS** means the stated dependency follows from the specified imported results and the reconstructed argument. **ERROR** means a demonstrated false statement; **UNRESOLVED** means a stated question is not established by this audit. A PASS does not certify the proof of every foundational external theorem.

| ID | Verdict | Exact target | Evidence, limitation, and affected claims |
|---|---|---|---|
| V01 | PASS | Note 01 §2; note 02 §1.2; note 03 §4, full product and identity | Reconstructed in §1 below from the VOA product and invariant form, using [M] §1.1. The unit is $\omega/2$, not the unit vector $t$. Direct input to C02 and the extrema chain. |
| V02 | PASS | Note 03 §4, critical point to idempotent and $\lambda(n)$ | Both nontrivial branches are complementary idempotents. The positive traceless coefficient fixes the branch; zero and identity have no unit traceless direction. See §1. Affects C07, C08, C12, C13. |
| V03 | PASS | Note 03 §4, Virasoro action and $c=8n$ | The self-OPE and mode commutator in §2 recover the factor eight. [M] §1.1, printed pp.4–5, agrees. No use of the extremum theorem in constructing the action. |
| V04 | PASS | Note 03 §4, unitarity, positive energy, closure | Full-VOA positivity is stated in [M] §4.2, printed p.17; [DL] Definition 2.2 and Theorem 4.15 provide another precise unitarity reference. The explicit cyclic-module proof in §2 supplies finite levels, adjoints, and its own conformal vector. Positive norm on $B$ alone would leave a blocking gap, but that is not the imported moonshine input. |
| V05 | PASS | Note 03 §4, exclusion of $c=0$ and central-charge gap | $L^u_{-2}\mathbf1=u\ne0$ and its squared norm is $c/2$. [FQS] Theorem 1 gives the necessary discrete-series restriction for $c<1$; [W] pp.1–2 agrees. Neither source implies that $c=7/10$ occurs inside moonshine. See §3. |
| V06 | PASS | Note 03 §4, all maximizers and orientation | [HS] Definition 2.12, Theorem 2.13, Lemma 2.14, Theorems 5.7–5.8 supply completeness of the Ising/2A correspondence. Monotonicity of $\lambda(n)$ then identifies exactly the positively oriented traceless axes. See §3. Affects C02 and all four target claims. |
| V07 | PASS | Note 03 §5, tangent spectrum and Hessian | [HS] Lemmas 2.4 and 2.14 give the required scaling; the restriction calculation in §4 gives all three tangent eigenvalues. There is no hidden identity eigenvector in the tangent space. |
| V08 | PASS | Note 03 §5, radius $1/10$ and compact-complement argument | Exact cubic expansion, the sign of its coefficients, and the boundary/interior alternatives give the claimed strict-superlevel localization. See §4. This supplies the relevant input to C07. |
| V09 | PASS | Note 04 §4, radius $1/2$ extension | The polynomial minorant, derivative bound, and endpoint comparison hold on the whole interval. Distinct-axis separation makes the target unique. See §4. Used by C08's upper bound and C13. |
| V10 | PASS | Note 04 §§3,5–7; note 05 §§2–3,8, uses of the extrema result | Real arguments are kept real; the global upper-deficit bound needs $\lvert f\rvert\le M$, but not the gap. The map in §5 distinguishes C12 from C13 and separates the synchronization part of C09. |
| V11 | UNRESOLVED — outside this bounded audit | Full statements C07, C08, C12, C13 and priority | This report validates their specified extrema inputs and tracks their use. It does not finish the channel-spectrum, character-data, robust-normalizer, or logarithm-bootstrap audit. It establishes no novelty. No downstream theorem is promoted to fully audited status. |
| V12 | ERROR — nonblocking external-source arithmetic | [HS] v1, Lemma 2.5 proof, printed p.9 | The squared norm of $\mathbf1_B-v/16$ is $47/32$ in the HS form, not the printed $3/2$. Both PDF and HTML contain the error. The computation below repairs this single number; the source's uniqueness argument and the project's branch conversion survive. No C02/C07/C08/C12/C13 constant changes. |
| V13 | ERROR — zero-error endpoint | Note 05 Theorem 2 and §8; STATUS C12; related strict chains in notes 03–05 | $O=I$ has $\epsilon=\mathsf W=D_{\mathbb M}=z=0$. Thus $D_{\mathbb M}^2<106\mathsf W^2$ is false as written. Replace by $\le$, or qualify strictness by $\mathsf W>0$. The exact-coefficient non-strict conclusion survives this counterexample. See §5 for the related C07/C08/C13 displays. |

## 1. Reconstruct the algebra and both branches

Use $\mathbf1$ for the VOA vacuum and $\mathbf1_B=\omega/2$ for the Griess algebra identity. They are different vectors in different weights. In [M] §1.1 the weight-two product and form are

$$
ab=a_{(1)}b,\qquad a_{(3)}b=\langle a,b\rangle\mathbf1,
\qquad \omega a=2a,\qquad\langle\omega,\omega\rangle=12.
$$

Set $t=\omega/\sqrt{12}$ and $s=1/\sqrt3$. Then $\|t\|=1$, $t^2=st$, and $tx=sx$. For $x,y\perp t$, invariance gives

$$
\langle xy,t\rangle=\langle x,yt\rangle=s\langle x,y\rangle,
\qquad xy=\mu(x,y)+s\langle x,y\rangle t.
$$

Thus $\mathbf1_B=t/s$ has norm squared three. These formulas match both earlier notes and do not use any extremal constant.

For $f(x)=\langle\mu(x,x),x\rangle$ on $S(V)$, symmetry gives $df_x(h)=3\langle\mu(x,x),h\rangle$. Hence criticality is equivalent to

$$
\mu(x,x)=\lambda x,\qquad \lambda=f(x),\qquad\|x\|=1.
$$

Writing a full idempotent as $e=\alpha t+bx$, its two coefficient equations are

$$
s(\alpha^2+b^2)=\alpha,\qquad 2s\alpha b+\lambda b^2=b.
$$

The $b=0$ cases are exactly $0$ and $\mathbf1_B$; they cannot encode a traceless unit direction. For $b\ne0$, eliminate $\alpha=(1-b\lambda)/(2s)$ to obtain

$$
b^2(\lambda^2+4s^2)=1.
$$

Take the branch $b=1/\sqrt{\lambda^2+4/3}>0$. Defining $n=\|e\|^2$, the scalar equation yields

$$
\alpha=sn,\qquad
n=\frac32\left(1-\frac{\lambda}{\sqrt{\lambda^2+4/3}}\right),
\qquad 0<n<3.
$$

The other branch is $\mathbf1_B-e$. In particular $e(-x)=\mathbf1_B-e(x)$: the opposite direction is not another copy of a positive maximum. Conversely any real idempotent other than $0,\mathbf1_B$ has a nonzero traceless part; normalizing that part recovers a critical point and the positive-$b$ branch. No spurious solution was introduced by squaring.

**Source arithmetic correction (V12).** In the HS normalization let $e'=v/16$. Invariance gives $(\mathbf1_B,e')_{\rm HS}=(e',e')_{\rm HS}=1/32$, so

$$
\|\mathbf1_B-e'\|_{\rm HS}^2=\frac32-\frac1{32}=\frac{47}{32}.
$$

The last entry in the list of idempotent norms in [HS] Lemma 2.5 should therefore be $47/32$, not $3/2$. After multiplying these three nonzero idempotents by 16, their squared norms are $384,8,376$, respectively, so the claimed uniqueness at squared norm eight still holds. In the project's VOA form the complement has norm squared $47/16=3-1/16$, already consistent with $n\mapsto3-n$. This is an external-source erratum recorded here, not a change to a historical project note.

Eliminating $\alpha$ gives

$$
b^2=n-n^2/3,
\qquad\lambda(n)=\frac{1-2n/3}{\sqrt{n-n^2/3}},
\qquad\lambda'(n)=-\frac1{2(n-n^2/3)^{3/2}}<0.
$$

The special case $\lambda=0$ is legitimate: $n=3/2$, not a zero-charge or identity branch.

## 2. Construct the unitary positive-energy vacuum module

Use the positive real form $V^\natural_{\mathbb R}$ whose weight-two part is the project's real Griess algebra $B$; its conjugation fixes $e$. Let $u=2e\in(V^\natural_{\mathbb R})_2$ and define $L^u_m=u_{(m+1)}$. The ambient VOA is of CFT type, with finite-dimensional weight spaces and $(V^\natural)_1=0$. Its grading, skew symmetry, and $u_{(1)}u=2u$ give

$$
u_{(0)}u=Du,\quad u_{(1)}u=2u,\quad u_{(2)}u=0,
\quad u_{(3)}u=\|u\|^2\mathbf1,\quad u_{(j)}u=0\ (j\ge4),
$$

where $D=L^\omega_{-1}$ is ambient translation. For example skew symmetry gives $2u_{(0)}u=D(u_{(1)}u)$, since the other derivative terms vanish. The VOA commutator formula now gives

$$
[L^u_m,L^u_k]=(m-k)L^u_{m+k}
 +\frac{m^3-m}{12}\,c\,\delta_{m+k,0}I,
\qquad c=2\|u\|^2=8\|e\|^2=8n.
$$

This verifies the central-charge normalization directly, agreeing with [M] §1.1. An abstract Griess algebra without an ambient VOA would not supply these mode identities.

The precise space needed is

$$
\mathcal H_u=U(\mathrm{Vir}_u)\mathbf1
 =\operatorname{span}_{\mathbb C}
 \{L^u_{-m_1}\cdots L^u_{-m_k}\mathbf1:m_i\ge2\}.
$$

The vacuum axiom gives $L^u_m\mathbf1=0$ for $m\ge-1$. Reordering modes proves the displayed spanning statement and invariance under every $L^u_m$.

**Positive form and adjoints.** Extend the moonshine positive real bilinear form sesquilinearly: $H(v,w)=\langle v,\overline w\rangle$, with the bracket extended bilinearly and conjugation taken in the specified real form. This is a positive Hermitian form. Reality of $u$ matters. Since $L^\omega_1u\in(V^\natural)_1=0$, the weight-two adjoint identity is

$$
(u_{(j)})^\dagger=u_{(2-j)},\qquad (L^u_m)^\dagger=L^u_{-m}.
$$

These are formal adjoints on the algebraic finite-energy domain; no assertion about bounded operators is needed. [M] §4.2 states positivity on the entire real moonshine VOA, not just weight two. [DL] supplies a further reference for ambient unitarity. We do not apply a subalgebra inheritance theorem requiring the same conformal vector: generally $u\ne\omega$.

**Energy and finite levels.** Both commutators

$$
[L^u_0,L^u_{-m}]=mL^u_{-m},\qquad
[L^\omega_0,L^u_{-m}]=mL^u_{-m}
$$

hold, and both zero modes kill the vacuum. Each spanning monomial therefore has eigenvalue $m_1+\cdots+m_k$ for both operators. Thus $L^u_0=L^\omega_0$ on $\mathcal H_u$, which is an algebraic orthogonal sum of nonnegative integer eigenspaces, each contained in an ambient finite-dimensional weight space. This proves precisely the positive-energy hypothesis used in [W]. It does not assert this equality on all of $V^\natural$.

**Vertex closure and translation.** The vertex subalgebra generated by $u$ and the vacuum is spanned by iterated $u$-modes; the VOA iterate identity expresses modes of these descendants in the same span. It is therefore $\mathcal H_u$. Moreover

$$
[D,L^u_m]=-(m+1)L^u_{m-1}=[L^u_{-1},L^u_m].
$$

Their difference kills the vacuum and commutes with the generating modes, so $D=L^u_{-1}$ on this subalgebra. Along with the grading above, this makes $u$ its own conformal vector. No assertion that all ambient conformal modes coincide on it is necessary.

**Irreducibility when identifying Ising vectors.** Every algebraic submodule is graded: a vector has finitely many energy components, and polynomial spectral projections in $L^u_0$ isolate them inside the submodule. A nonzero proper Virasoro submodule of $\mathcal H_u$ would therefore contain a lowest positive-level vector $w$ annihilated by every positive mode. Such a vector is orthogonal to every vacuum descendant: move the negative modes in the descendant to positive modes on $w$. It is also orthogonal to the vacuum by level. Since descendants span $\mathcal H_u$, positivity forces $w=0$, a contradiction. A submodule meeting level zero already contains the cyclic vacuum and is the whole module. Thus $\mathcal H_u\cong L(c,0)$, and in particular $c=1/2$ gives the simple Ising VOA, not merely a nonsimple universal Virasoro algebra.

## 3. Exclude unwanted charges and identify all maxima

The level-two norm is already decisive at zero charge:

$$
L^u_{-2}\mathbf1=u\ne0,\qquad
\|L^u_{-2}\mathbf1\|^2=c/2=4n>0.
$$

The identity branch would instead give $u=\omega$, $c=24$, but was excluded algebraically by $b>0$ and $n<3$.

Only the **necessity** part of the unitary classification is needed. [FQS] Theorem 1, printed p.535, excludes $c<1$ outside the discrete series. Applied to the positive vacuum module, this gives

$$
c\in\left\{1-\frac6{m(m+1)}:m=2,3,\ldots\right\}\cup[1,\infty).
$$

Equivalently, pull its inner product back to the Verma module $M(c,0)$. A negative-norm vector excluded by [FQS] cannot be removed by a unitary quotient: a vector mapping to zero would have zero pulled-back norm. This also establishes the necessary charge restriction without relying on the irreducibility argument above.

After excluding zero, $c\ge1/2$; if $c\ne1/2$, then $c\ge7/10$. Hence $n\ge1/16$, and otherwise $n\ge7/80$. No existence assertion at $7/10$ is inferred.

The remaining input is genuinely Monster-specific. [HS] proves the bijection between Ising vectors and 2A-like involutions and then identifies these with the single Monster 2A class. Its Lemma 2.14 explicitly compares the two forms. With its axis $v$, the conversions are

$$
\langle\ ,\ \rangle_{\rm VOA}=2(\ ,\ )_{\rm HS},
\qquad u=v/8,\qquad e=v/16,\qquad\|e\|^2=1/16.
$$

This is an imported axis-completeness theorem, not a consequence of knowing only the spectrum of one displayed axis. Its use does not invoke the project's extremum or robustness theorems.

Compactness ensures that a global maximum is critical. Strict monotonicity of $\lambda(n)$ bounds it above by $\lambda(1/16)$; existing Ising axes attain that value. Conversely equality forces $n=1/16$, hence an Ising vector and therefore one of the known axes. We obtain

$$
M=\frac{46}{\sqrt{141}},\qquad
\operatorname{argmax}_{S(V)}f=\mathcal A,
\qquad e=\frac{t}{16\sqrt3}+\frac{\sqrt{141}}{48}a.
$$

The coefficient of $a$ is positive. Oddness gives the minimum $-M$ precisely on $-\mathcal A$ and gives $|f(x)|\le M$ on the entire real unit sphere. Every other critical point has

$$
f(x)\le\lambda(7/80)=\frac{226}{\sqrt{4893}}<\frac{33}{10},
\qquad M>\frac{19}{5}.
$$

The gap is therefore strictly greater than $1/2$. These inequalities bound **all** nonmaximal real critical points, including negative and zero values. Complex critical points are outside this argument and are not used by the localization lemmas.

## 4. Curvature, finite radii, and the global boundary argument

The spectrum of $R_e$ on $B$ is $\{1,0,1/4,1/32\}$ with a one-dimensional 1-eigenspace. Let $E=\{t,e\}^\perp=a^\perp\cap V$. It is $R_e$-invariant: $R_e$ is self-adjoint, $R_ee=e$, and $R_et=se$. On $E$,

$$
R_e=\frac1{48}I+\frac{\sqrt{141}}{48}L_a.
$$

On $E$ the 1-eigenvalue is absent; the removed plane contains that eigenvector and one zero eigenvector. Rescaling the remaining eigenvalues gives the tangent $L_a$ eigenvalues

$$
\frac{-1}{\sqrt{141}},\qquad\frac{11}{\sqrt{141}},
\qquad\frac1{2\sqrt{141}}.
$$

The sphere Hessian is $6L_a-3MI$ on $E$, giving exactly the three negative eigenvalues in note 03 §5. This is only infinitesimal information; the following estimates are necessary for the claimed finite neighborhoods.

For $r=\|x-a\|$, set $q=1-r^2/2$ and $\tau=\sqrt{1-q^2}\ge0$, and write $x=qa+\tau v$ with $v\perp a$ and $\|v\|=1$. The case $r=0$ is immediate. Criticality cancels the term linear in $v$, so

$$
f(x)=Mq^3+3q\tau^2T(a,v,v)+\tau^3 f(v).
$$

Both radii under consideration have $q>0$, so using the upper tangent eigenvalue in the second term preserves the required inequality direction. The global bound $|f(v)|\le M$ was established before, rather than inferred from a local Hessian.

For $0\le r\le1/10$, $1-q^3\ge(3/2)r^2-(3/4)r^4$, $q\tau^2\le r^2$, and $\tau^3\le r^3$ give

$$
M-f(x)\ge r^2\left(\frac{36}{\sqrt{141}}-\frac{3M}{4}r^2-Mr\right)
\ge2r^2.
$$

The last step follows from $36/\sqrt{141}>3$ and $M<4$: the bracket exceeds $3-3/100-4/10=257/100>2$. The estimate in note 03 is conservative but valid throughout its interval.

For $0\le r\le1/2$, retain the exact polynomial terms instead:

$$
M-f(x)\ge\frac{r^2}{\sqrt{141}}
\left[36-\frac{39}{4}r^2+\frac{13}{8}r^4
-46r(1-r^2/4)^{3/2}\right].
$$

Since $(1-r^2/4)^{3/2}\le1-r^2/4$, the bracket is bounded below by

$$
p(r)=36-46r-\frac{39}{4}r^2+\frac{23}{2}r^3+\frac{13}{8}r^4.
$$

On that interval,

$$
p'(r)=-46-\frac{39}{2}r+\frac{69}{2}r^2+\frac{13}{2}r^3
\le-\frac{585}{16}<0,
\qquad p(1/2)=\frac{1549}{128}>\sqrt{141}.
$$

For an exact endpoint comparison, $1549^2-141\cdot128^2=89257>0$. Therefore $M-f(x)\ge r^2$ for the whole radius-one-half ball. No sampling of the interval is used.

For separation, the first-coordinate values in [HRS] Lemmas 8.2–8.3 give, for distinct norm-one axes, inner product at most $1/8$. Passing to the VOA idempotents and subtracting the identity component gives

$$
\langle a,b\rangle=\frac{48q-1}{47},\qquad
\|a-b\|^2\ge\frac{84}{47}>1.
$$

Thus the radius-one-half balls are disjoint; the smaller balls are too. Only separation, not uniqueness of the Norton–Sakuma type from one inner product, is needed here.

For either radius $R$, remove the union of open radius-$R$ balls from the sphere, giving a compact set $K_R$. If it is empty the localization claim is immediate. Otherwise a maximum of $f$ on $K_R$ exists. At a boundary point its distance to at least one axis is exactly $R$, so the appropriate finite-radius estimate applies. At an interior point all constraints are inactive and the point is a sphere critical point outside $\mathcal A$, so its deficit exceeds $1/2$. These exhaust the possibilities; connectedness or a gradient-flow assertion is unnecessary. Consequently

$$
\begin{aligned}
M-f(x)<1/50&\ \Longrightarrow\ \exists!a:\ \|x-a\|<1/10,
\quad\|x-a\|^2\le(M-f(x))/2,\\
M-f(x)<1/4&\ \Longrightarrow\ \exists!a:\ \|x-a\|<1/2,
\quad\|x-a\|^2\le M-f(x).
\end{aligned}
$$

The strict superlevel conditions correctly exclude equality at the sphere-ball boundaries.

## 5. Downstream dependency map and limits of the conclusion

The global upper-deficit estimate is a separate dependency. For $h=x-a$, $r=\|h\|\le2$, one has $\langle a,h\rangle=-r^2/2$. Cubic expansion and the minimum tangent eigenvalue give

$$
\begin{aligned}
M-f(x)&=\frac32Mr^2-3T(a,h,h)-f(h),\\
T(a,h,h)&\ge\frac M4r^4-\frac1{\sqrt{141}}(r^2-r^4/4),\\
M-f(x)&\le Mr^2\left(\frac{36}{23}+r-\frac{141}{184}r^2\right)
<2Mr^2\quad(r>0).
\end{aligned}
$$

The last quadratic has maximum $6134/3243<2$. This uses $|f(h)|\le M\|h\|^3$ globally, but it uses neither the critical-value gap nor the localization argument. This distinction matters for C12.

| Claim | Precise use of the audited dependency | Consequence of this bounded audit |
|---|---|---|
| C02 | The full/VOA normalization, real Ising identification, spectrum and axis correspondence | These particular inputs pass; the entire trace-identity ledger was not re-proved. |
| C07 | Note 03 §§7–8 turn small tensor error into $M-f(Oa)$ for every real axis, then use §5 radius-$1/10$ localization before finite-alphabet rounding | The extrema and localization input is valid. The finite-alphabet/character and local gate arguments remain separate proof obligations. |
| C08, upper bounds | Note 04 §3 averages the nonnegative deficits; §4 localizes axes with deficit $<1/4$; §6 completes an injective good matching; §7 transfers to complex $U$ through real $O$ | The required real extrema and radius-$1/2$ bounds pass. The good map is injective because two preimages of one target would be less than one apart; bad matches cost at most $4\le16\delta_a$. The whole transport theorem still imports the moment and quantum-loss identities. |
| C08, lower bound | Note 04 §§5–6 use the global upper-deficit bound and the orbit third moment | Needs the global maximum and tangent spectrum, but not the gap/localization. This input passes. |
| C12 | Note 05 §8 starts with an existing optimal transport assignment and uses note 04 §5 to get $1-\alpha(O)\le2\mathsf W(O)^2$ | Does not need the gap, either localization radius, or a sign maximizing $\alpha$. It does need the global maximum bound and axis spectrum, which pass here. The normalizer argument is outside this report. |
| C13 | Note 05 §2 item 3 and equations (3.3)–(3.6) use the matching produced by C08, then invoke normalizer rounding and the local theorem | Inherits the localization input through C08. This report clears that dependency, not the rest of the improved threshold proof. |
| C09 | Note 04 §8 synchronization and exact product stabilizers use the pair/channel spectrum and exact collective stabilizer; §8.1 additionally invokes C08 for transport | The synchronization inequality and exact stabilizer do not depend on the extrema argument. Its supplementary transport consequences do. |
| C01, C03–C06, C10–C11, C14 | Their stated proofs do not rely on the classification of real cubic extrema | No verdict on their full proofs is supplied by this assignment. In particular C11 is a general group lemma, not a consequence of a VOA classification. |

Complex-unitary transport in notes 03–05 first selects a phase and a real orthogonal $O$. Cubic localization is then applied to $Oa$, never to a general complex vector. The sign of a real cubic overlap can be changed by $O\mapsto-O$ and a compensating common phase. This does not enlarge the positive axis set to $\mathcal A\cup-\mathcal A$ or permit axis-dependent phases.

**Zero-error correction (V13).** At $O=I$, take the identity axis matching. Then $\mathsf W=0$, $D_{\mathbb M}=0$, $\alpha=1$, and $z=0$. The literal statement in note 05 Theorem 2/§8, README, and STATUS C12, $D_{\mathbb M}^2<106\mathsf W^2$, is therefore false at an allowed input. Its narrow repaired form is

$$
\mathsf W(O)^2\le3\times10^{-9}
\quad\Longrightarrow\quad
D_{\mathbb M}(O)^2\le\frac{20842432}{196883}\mathsf W(O)^2
\le106\mathsf W(O)^2.
$$

The last inequality is strict only when $\mathsf W(O)>0$. This identifies an endpoint error, not a counterexample to the exact-coefficient bound. The remaining proof of that bound still needs its separate audit.

The same convention must be corrected wherever a strict coefficient comparison is multiplied by an error allowed to be zero: note 03 §1 and note 05 Theorem 1's final $<1.151\sqrt\epsilon$ (C07/C13), note 04 §6's $<154\epsilon$ derivation (the formal Theorem A is already non-strict), and note 05 equations (3.5)–(3.6), (7.1)–(7.2). For example $z^2<1300\epsilon$ becomes $z^2\le1300\epsilon$ for all errors. Subsequent threshold comparisons such as $1300\cdot10^{-10}<1/5760000$ remain strictly valid. The constants, sufficient thresholds, and principal non-strict gate bounds are unaffected. This report is the erratum; the preserved notes have not been rewritten.

If the full-VOA positivity premise had been unavailable, the charge restriction, global maximum and localization would have remained unresolved; C07, C08's upper bounds, and C13 would have required an explicit conditional extrema hypothesis. C12 would still require its weaker global maximum input. The cited moonshine sources and reconstruction above supply these premises, so this audit does **not** recommend withdrawing those claims on this ground.

## 6. Narrow integration recommendation

Keep this report as a separately named proof supplement to note 03 §4 and notes 03–04's localization sections. In any later integrated exposition:

1. State that $B$ is the real weight-two algebra of the positive real moonshine VOA and cite [M] §4.2, with [DL] as an additional unitarity reference.
2. Define $\mathcal H_u$ explicitly and include the adjoint, grading, and translation arguments of §2. Specify that it has conformal vector $u$, generally different from $\omega$.
3. Cite [FQS] Theorem 1 for necessity and [HS] **Lemma 2.14** for the factor-of-two form conversion. Keep nonattainment at $c=7/10$ unasserted.
4. Preserve the distinct dependencies of C12 and C13. A completed bounded audit is not a completed audit of either theorem.

5. Correct the literal strict C12 summary in README/STATUS at integration, and use the V13 convention in future statements of the related bounds. Correct the single external-source norm from V12 whenever that argument is restated.

These are proof/source clarifications and endpoint corrections; they change no scientific data and do not authorize manuscript preparation or integration into `main`.

## 7. Verification and preservation record

Before changes, `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py` exited zero using Python 3.12.14. All eight scientific verifiers completed, giving twelve successful replays; their output matched the recorded reports byte-for-byte. License, preserved seed/imports, and snapshot checks passed.

After the audit changes, the same command exited zero again: all twelve replays matched the recorded reports, and all provenance and snapshot checks passed. The completed report's manifest hash was also checked before submission. `git diff --check` passed. No new test script is added: the existing scalar checks already cover the numerical identities here, while the substantive new evidence is the analytic reconstruction and primary-source reading.

Verification does not establish the VOA input or prove these arguments. The largest matrix in the replayed historical toy checks is $256\times256$; the current normalizer checks use matrices at most $60\times60$. No full Monster multiplication tensor, full Monster matrices, or axis enumeration was used. No downloaded paper is bundled.

The only intended repository changes are this audit report and a new entry for it in `snapshot_manifest.json`, with a description of the enlarged manifest scope. All pre-existing manifest entries and all preserved scientific bytes remain unchanged. Recorded test results are not overwritten.

## Primary references inspected

The locators below refer to the versions read on 23 September 2026. Page numbers are printed page numbers, not zero-based PDF page indices. The source statements needed for the dependency were read; this audit does not claim to reproduce the foundational classifications or all of their cited proofs.

- **[M]** Atsushi Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. [PDF](https://arxiv.org/pdf/math/0007169v1). §1.1, pp.4–5, equations (1.1)–(1.8): grading, product, Virasoro vector, adjoint; §1.2, p.5, equations (1.9)–(1.13): vacuum module; §3.2, p.14: real charge-$1/2$ case; §4.2, pp.17–18: positive moonshine real form and Ising decomposition. Corollary 4.1, p.16, is the earlier notes' trace source, not a replacement for full-VOA positivity.
- **[DL]** Chongying Dong and Xingjun Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1. [PDF](https://arxiv.org/pdf/1308.2361v1). Definition 2.2, p.3, and §4.5, Theorem 4.15, p.27. Used for ambient unitarity only; a same-conformal-vector subalgebra result is not invoked for $u\ne\omega$.
- **[FQS]** Daniel Friedan, Zongan Qiu and Stephen Shenker, *Details of the Non-Unitarity Proof for Highest Weight Representations of the Virasoro Algebra*, Communications in Mathematical Physics **107** (1986), 535–542. [Author-hosted PDF](https://www.physics.rutgers.edu/~friedan/papers/Commun_Math_Phys_107_535_1986.pdf), [DOI](https://doi.org/10.1007/BF01205483). Theorem 1 and equations (4)–(5), p.535; the level/Gram-matrix setup is on p.536. This is the original necessary-condition theorem used here.
- **[W]** Antony Wassermann, *Direct proofs of the Feigin–Fuchs character formula for unitary representations of the Virasoro algebra*, arXiv:1012.6003v1. [PDF](https://arxiv.org/pdf/1012.6003v1). Introduction, pp.1–2: definition and classification of positive-energy unitary modules; Gomes lemma, p.12: zero charge. Used as a consistency check and a precise formulation of the hypotheses, not credited as the origin of the FQS classification.
- **[HS]** Gerald Höhn and Martin Seysen, *The Order of the Monster Finite Simple Group*, arXiv:2508.01037v1. [HTML](https://arxiv.org/html/2508.01037v1), [PDF](https://arxiv.org/pdf/2508.01037v1). Lemma 2.4; Definition 2.12 and Theorem 2.13; **Lemma 2.14**; Theorems 5.7–5.8. These provide spectrum, scale conversion, and completeness of the Ising/2A identification. Lemma 2.5, printed p.9, contains the nonblocking arithmetic error V12. The Griess automorphism theorem is classical, not attributed as new to this project.
- **[HRS]** J. I. Hall, F. Rehren and S. Shpectorov, *Universal axial algebras and a theorem of Sakuma*, arXiv:1311.0217. [PDF](https://arxiv.org/pdf/1311.0217). §6 for form coefficients; Lemmas 8.2–8.3 and the table on printed p.22 for the finite axis inner-product values. Used for the separation bound; a single inner product is not claimed to determine all nine types.
