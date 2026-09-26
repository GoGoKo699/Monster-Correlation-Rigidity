# 3. Why does Ising appear?

[Previous](02_weight_two.md) · [Learning path](README.md) · [Next](04_rounding.md)

**Question:** why should a large three-point coefficient have anything to do with the Ising model?

Gaberdiel Sections 3.7.3 and 4.4 introduce the relevant Virasoro and Ising background. Yamauchi Section 4, Lemma 4.3 and equations (4.8)–(4.9), supplies the weight-two viewpoint. This lesson explains the specialized conversion in [core Q2–Q3](../../research/uniform_extraction_core.md).

## An Ising vector is an internal stress tensor

Do not picture a spin variable on a lattice. Here an **Ising vector** $e$ is a weight-two state whose field generates an internal unitary Virasoro theory with central charge $1/2$. It is that subtheory's stress tensor. It is not the Ising spin primary of weight $1/16$.

In the product convention of Lesson 2,

```math
e*e=2e,\qquad \langle e,e\rangle=\frac14.
```

More generally, an internal Virasoro vector of central charge $r$ has squared norm $r/2$. The letter $r$ denotes the **internal** charge; the ambient charge remains $c=24$. An internal stress tensor need not be a primary for the ambient stress tensor.

Some algebra references call $e/2$ an idempotent because $(e/2)*(e/2)=e/2$. Thus “idempotent” and “Virasoro vector” may differ by a factor of two. We retain $e*e=2e$ throughout.

## Stationarity forces a special self-product

Let $a$ be a stationary point of $f$ on the unit sphere in $P_2$, and put $\lambda=f(a)$. Differentiating the symmetric cubic in a tangent direction $v$ gives

```math
D f(a)[v]=3\langle\mu(a,a),v\rangle.
```

Stationarity says this vanishes for every $v$ perpendicular to $a$. Therefore $\mu(a,a)$ is parallel to $a$. Pairing with $a$ fixes the coefficient:

```math
\mu(a,a)=\lambda a,\qquad a*a=\lambda a+\frac16\omega.
```

The self-product stays in the two-dimensional span of $a$ and $\omega$. This is the crucial simplification.

A suitable combination $e=(r/24)\omega+ba$ then satisfies $e*e=2e$. In the exact unitary setting of the core, its modes generate an internal unitary Virasoro vacuum representation. This uses VOA identities and positivity, not just the formal resemblance of two quadratic equations.

<details>
<summary>Second pass: the conversion formula</summary>

The coefficients are constrained by

```math
b^2=\frac{r(24-r)}{48},\qquad b\lambda=2-\frac r6.
```

Taking $b>0$ yields

```math
\lambda(r)=\frac{2-r/6}{\sqrt{r(24-r)/48}},\qquad 0<r<24.
```

The core constructs $r$ for every stationary $\lambda$ and proves that this is a genuine Virasoro vector. Direct differentiation gives

```math
\lambda'(r)=-\frac{1}{2[r(24-r)/48]^{3/2}}<0.
```

Thus smaller allowed internal charge means larger stationary self-coupling. This is an algebraic relation, not an RG flow or a dynamical relaxation law.

</details>

## Unitarity leaves a gap

The unitary Virasoro classification restricts the nonzero internal charges below one to the discrete series

```math
r=1-\frac{6}{m(m+1)},\qquad m=3,4,5,\ldots.
```

The first two are $1/2$ and $7/10$; charges at least one are also allowed. The trivial zero-charge case sometimes listed with $m=2$ is excluded here by the positive norm of the constructed nonzero vector. Yamauchi numbers the same series with a shifted index; it is the charge values, not the index name, that matter.

Since $\lambda(r)$ decreases, the largest possible cubic value is

```math
M=\lambda(1/2)=\frac{46}{\sqrt{141}}.
```

At any other stationary point, the value is at most

```math
M_2=\lambda(7/10)=\frac{226}{\sqrt{4893}}<M.
```

The bound $f\le M$ holds throughout each admissible primary sphere because a maximum is stationary. **This does not say every candidate attains $M$.** Attainment is equivalent to possessing an Ising direction. Lesson 4 explains why sufficiently near-extremal input already forces attainment.

The classification is an imported theorem. The reference giving its precise necessity statement, with attribution to Friedan–Qiu–Shenker, is recorded on the [source page](assumptions_and_sources.md).

## Why the target overlap is negative

For an Ising vector $e$, subtract the ambient stress and normalize:

```math
A=e-\frac{\omega}{48},\qquad
\|A\|^2=\frac{47}{192},\qquad
 a=\frac{A}{\sqrt{47/192}}.
```

Equivalently, $e=\omega/48+(\sqrt{141}/24)a$. This $a$ is the associated maximizing primary direction, also called an Ising direction in the core. It is not the unnormalized vector $e$.

Take two exact Ising vectors $e_a,e_b$ and their directions $a,b$. Expanding their inner product gives

```math
\langle e_a,e_b\rangle=\frac{1+47\langle a,b\rangle}{192}.
```

If the Ising stress tensors are orthogonal, the left side is zero, so $\langle a,b\rangle=-1/47$. Subtracting a shared component can turn zero overlap into negative overlap. No negative norm is involved.

## Check your understanding

**1.** Does an internal Ising vector change the ambient central charge from 24 to $1/2$? A: yes. B: no; $1/2$ is the internal subalgebra's charge.

**2.** Must two orthogonal Ising stress tensors give orthogonal normalized ambient primaries? A: yes. B: no; their primary overlap is $-1/47$.

<details>
<summary>Answers and explanations</summary>

**1: B.** The ambient stress tensor is still $\omega$. The internal stress tensor $e$ defines a smaller Virasoro subalgebra.

**2: B.** Both stress tensors contain a common component along $\omega$. Removing it gives the displayed negative overlap.

</details>

**Next:** [From nearly extremal to exact](04_rounding.md). The input fields need not already be exact Ising directions.
