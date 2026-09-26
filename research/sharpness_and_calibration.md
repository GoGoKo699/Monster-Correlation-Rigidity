# Quantitative extraction: optimal exponent and calibrated weight-two inputs

[← Core proof](uniform_extraction_core.md) · [Learning path](../docs/learn/README.md) · [Overview](../README.md)

Research record, 26 September 2026. Read main: `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
No manuscript section is being drafted. The imported exact classification remains credited to Abe–Lam–Yamada; the estimates below supplement the self-contained [core](uniform_extraction_core.md).

## 1. The two remaining precision questions

The core proves the following sufficient criterion in an exact simple unitary rational $C_2$-cofinite holomorphic VOA of CFT type, central charge 24, and $V_1=0$. For two real unit weight-two primaries $x,y$, put $M=46/\sqrt{141}$. If

```math
f(x)\ge M-\epsilon_x,\qquad f(y)\ge M-\epsilon_y,\qquad
|\langle x,y\rangle+1/47|\le\delta,
```

with $0\le\epsilon_x,\epsilon_y<1/50$ and

```math
\delta+\sqrt{\epsilon_x/2}+\sqrt{\epsilon_y/2}<3/188,
```

then the underlying VOA is moonshine. The proof first locates an exact Ising primary within $\sqrt{\epsilon/2}$ of each field, then applies Sakuma's discrete overlap theorem and the prior ambient classification theorem. All class, reality, grading, and norm hypotheses are exact.

Two questions about that statement can now be settled without another special-subtheory campaign:

* The square-root exponent in value-to-field localization cannot be improved, even in the known moonshine theory. This is an optimal exponent, not an optimal numerical tolerance region for theory identification.
* Exact normalization and exact stress subtraction need not be supplied as preprocessed data. Seven scalar intervals for two actual real weight-two fields suffice to conservatively compute the quantities in the criterion. Exact ambient axioms, reality, grade two, and the known stress tensor remain hypotheses.

The first conclusion is an explicit realization of the familiar quadratic-loss mechanism at a nondegenerate maximum. The second is exact invariant-metric algebra and interval arithmetic. Neither auxiliary statement is advertised as a new general optimization or calibration theorem.

## 2. Calibrating arbitrary real weight-two fields

Let $w_1,w_2$ be real PCT-fixed vectors of exact ambient weight two. They need not be primary, mutually orthogonal, or normalized. The stress tensor $\omega$ is known and has squared norm twelve. Define seven real numbers

```math
n_i=\langle w_i,w_i\rangle,\quad
\tau_i=\langle\omega,w_i\rangle,\quad
q_i=\langle w_i*w_i,w_i\rangle\quad (i=1,2),
```

```math
m=\langle w_1,w_2\rangle.
```

Here $*$ is the weight-two mode product $a_{(1)}b$. The $q_i$ are these algebraic coefficients. For nonprimary $w_i$ they must not be naively equated to a primary-only conformal position formula without including stress-tensor Ward terms.

Set

```math
z_i=w_i-\frac{\tau_i}{12}\omega,\qquad N_i=n_i-\frac{\tau_i^2}{12}.
```

Because $V_1=0$, a weight-two vector orthogonal to $\omega$ is primary: $L_1$ maps it to $V_1=0$, $L_2$ is its pairing with $\omega$ times the vacuum, and higher positive modes vanish by degree. Thus $z_i$ is primary, and its squared norm is $N_i$. Assume $N_i>0$. Put $x_i=z_i/\sqrt{N_i}$. Then

**(1) Calibrated coefficients.**

```math
f(x_i)=\frac{q_i-\tau_i n_i/2+\tau_i^3/36}{N_i^{3/2}},
```

```math
\langle x_1,x_2\rangle=\frac{m-\tau_1\tau_2/12}{\sqrt{N_1N_2}}.
```

These exact identities remove both stress contamination and scale from the input fields.

**Derivation.** Write $w=z+\alpha\omega$, $\alpha=\tau/12$ and $z$ perpendicular to $\omega$. Since $\omega*z=2z$, $\omega*\omega=2\omega$ and $\|\omega\|^2=12$, invariance of the form gives

```math
q(w)=q(z)+6\alpha\|z\|^2+24\alpha^3,\qquad
n=\|z\|^2+12\alpha^2.
```

Solving for $q(z)$ gives $q-\tau n/2+\tau^3/36$. The bilinear projection identity gives $m-\tau_1\tau_2/12$. Division by the positive primary norms proves (1).

This argument needs no multiplication table and no chosen Ising vector in the unknown candidate. It does not alter the field signs: a negative primary self-coupling remains negative unless a sign change and the accompanying overlap change are explicitly made.

### Certified scalar intervals

Suppose each of the seven exact numbers lies in a supplied rational interval. Evaluate (1) by outward interval arithmetic, first requiring strict positive lower bounds for both $N_i$. If the resulting lower bounds on $f(x_i)$ and upper bound on the overlap error satisfy the original sufficient criterion, the conclusion follows for every exact input consistent with those intervals.

The checker uses only fractions and integer square roots. It encloses $\sqrt{s}$ between adjacent dyadic numbers and propagates both endpoints. It rejects a primary norm interval reaching zero, a certified lower self-coupling above the unitary cap, and other inconsistent conditions. Failure to establish the sufficient inequality is **inconclusive**, not proof that the theory is different from moonshine. Broad intervals can fail even for the known example.

This is robustness with respect to uncertainties in specified coefficients in an exact model. It is NOT robustness to violations of the VOA axioms, uncertain conformal weight, non-real fields, unknown stress tensor, leakage to other weights, or unknown empirical error coverage. No statistical sample count, field-finding algorithm, measurement architecture, or efficient normalization protocol is inferred.

The three exact controls use differently scaled and stress-shifted orthogonal Ising vectors. A separate seven-interval example of radius $10^{-12}$ around the uncentered exact pair also passes with a strictly positive margin. That radius is a test case for the arithmetic, not a claim about required experimental precision or an optimal allowance.

## 3. A sharp localization family inside the known theory

The known moonshine VOA contains an orthogonal real Ising pair $e,f$. One source construction takes a norm-four Leech vector $\alpha$ and uses the two signs in

```math
e_\pm=\frac1{16}\alpha(-1)^2\mathbf1
\ \pm\ \frac14(e^\alpha+\theta(e^\alpha)).
```

Lam–Shimakura [LS, Theorem 3.1] record this pair. Orthogonality here means a vanishing singular OPE and commuting Virasoro subalgebras; it does not mean every regular product vanishes. Their text just before the theorem uses an all-modes-zero wording that must not be taken literally for the tensor-product states.

The three stress vectors $e,f,g=\omega-e-f$ have charges $1/2,1/2,23$ and form a real weight-two subalgebra with coordinate-wise product $2xy$ and metric $\mathrm{diag}(1/4,1/4,23/2)$. This does not assert that the whole moonshine theory factorizes into three tensor factors.

Define

```math
A=e-\omega/48,\quad B=f-\omega/48,\quad
b_0^2=\|A\|^2=\|B\|^2=47/192,
```

```math
a=A/b_0,\quad b=B/b_0,\quad r=1/47,\quad
v=b+ra,\quad d=\|v\|^2=2208/2209.
```

Then $a$ and $b$ are exact maximizing primary directions, $\langle a,b\rangle=-r$, and $v$ is nonzero and perpendicular to $a$. Consider the exact unit-primary curve

```math
x_t=\frac{a+t v}{\sqrt{1+d t^2}}.
```

It lies entirely within the known theory's real primary space.

The small stress subalgebra determines the complete cubic along this curve:

**(2) Cubic along the curve.**

```math
\sqrt{141}\,f(x_t)=\frac{46-3dt^2+kt^3}{(1+dt^2)^{3/2}},
```

```math
k=46(1-3r^2-2r^3)=\frac{4769280}{103823}.
```

For example, $C(a,a,v)=0$ by criticality; $\sqrt{141}\,C(a,v,v)=-d$ follows directly by multiplying the three stress coordinates. No dense Griess tensor or Monster representation calculation is used.

Taylor expansion at zero gives

**(3) Leading losses and distances.**

```math
M-f(x_t)=\frac{72d}{\sqrt{141}}t^2+O(t^3),
```

```math
\|x_t-a\|^2=dt^2+O(t^4).
```

The core local-growth theorem separates distinct maximizing directions by more than $1/10$. For sufficiently small nonzero $t$, $x_t$ lies within $1/20$ of $a$, and $a$ is therefore its unique nearest maximizing direction. Consequently

**(4) Sharp square-root limit.**

```math
\lim_{t\to0}\frac{\mathrm{dist}(x_t,\mathcal A)}{\sqrt{M-f(x_t)}}
=\sqrt{\frac{\sqrt{141}}{72}}>0.
```

Here $\mathcal A$ is the full set of maximizing primary directions in the actual theory, not only the displayed pair.

If a value-to-nearest-axis bound $\mathrm{dist}(x,\mathcal A)\le C(M-f(x))^\alpha$ held for any finite $C$ and $\alpha>1/2$ throughout a neighborhood, (3) would imply $|t|\le\text{constant}\,|t|^{2\alpha}$, a contradiction as $t$ tends to zero. The exponent $1/2$ is thus optimal already in this fixed theory. This is not a claim that the coefficient $1/\sqrt{2}$, the entry radius $1/10$, or the numerical pair tolerances are optimal.

### Why a linear overlap allowance would lose information

The same curve obeys

```math
\langle x_t,b\rangle=\frac{-r+d t}{\sqrt{1+d t^2}}.
```

The cross-overlap changes linearly at zero, while the self-coupling deficit changes quadratically. Therefore, from self-coupling losses alone, one cannot replace the generic square-root field and overlap control by a uniform linear-in-deficit estimate. This is not a necessity theorem for the whole-theory identification region: additional correlations can provide additional information, and an already known moonshine theory remains moonshine at all $t$.

## 4. Where this leaves the selected contribution

The bounded core is now a quantitative conditional identification theorem with two useful boundary results:

1. the field-distance exponent is sharp in an actual admissible theory;
2. the normalized-primary assumptions can be implemented algebraically from seven calibrated coefficients of real weight-two fields, while retaining all exact ambient hypotheses.

Neither auxiliary result should be advertised as a separate foundational advance. The candidate contribution remains the uniform replacement of exact internal-subalgebra hypotheses by controlled correlation coefficients and the resulting ambient identification through the prior theorem.

The proof does not claim that the original holomorphic/current-free class is a singleton, that the coefficient test must pass for arbitrary supplied fields, or that the spectrum alone finds those fields. General approximate-VOA stability and first-Ising existence are outside this bounded theorem, not missing lemmas being left for manuscript drafting.

## 5. Evidence and inherited interfaces

`checks/verify_calibration_and_sharpness.py` emits 74 labelled exact checks. They include algebraic projection identities, rescaling/stress-shift examples, certified interval operations and negative inputs, the full polynomial curve, and the Taylor coefficients used in the analytic sharpness proof. The largest coefficient vector has length three. No matrix or full VOA is constructed. The continuum limit follows from the displayed analytic functions, not from sampling four values of $t$.

At import, the prior core/checker/report and original license were copied byte-identically from the supplied research-completion packet; its 14 payload hashes and 63-check report were verified under normal/-O/-OO. No private planning or manuscript is included. Imported FQS, Ising-module, Sakuma and ALY theorems remain distinct source dependencies; no independent expert or formal verification of those results is claimed.

For the directly inspected source history and contribution assessment, see [the comparison record](../audits/quantitative_contribution_verdict.md). The new results do not change the fundamental source attribution: the exact classification belongs to ALY; positive-metric cubic/idempotent variational methods and local quadratic growth are prior mathematics.

[LS] C.H. Lam, H. Shimakura, *Ising vectors in the vertex operator algebra $V_{\mathrm{Leech}}^+$ associated with the Leech lattice*, arXiv:0810.5395v1, Theorem 3.1. Printed page 6 was visually inspected in this continuation. The lattice inclusion into moonshine and real-unitary convention are inherited from the source construction; this finite stress-algebra check does not reprove the construction.
https://arxiv.org/abs/0810.5395

[ALY] T. Abe, C.H. Lam, H. Yamada, *A remark on $\mathbb Z_p$-orbifold constructions of the Moonshine vertex operator algebra*, arXiv:1705.09022v4, Theorem A.1. The exact endpoint is imported.
https://arxiv.org/abs/1705.09022

[DL] C. Dong, X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1, Definitions 2.1–2.2 and the unitary real-form conventions.
https://arxiv.org/abs/1308.2361
