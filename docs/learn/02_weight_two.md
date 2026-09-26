# 2. Turn fields into geometry

[Previous](01_correlations.md) · [Learning path](README.md) · [Next](03_ising.md)

**Question:** how does the coefficient problem become geometry on a sphere?

Use Gaberdiel Section 3.6 for conformal structure and revisit Section 3.4 for modes. The formulas below unpack [core Q0](../../research/uniform_extraction_core.md); Yamauchi Section 4, equation (4.2), is the secondary algebraic reference.

## Keep one conformal grade

Let $V_2$ be the space of weight-two states. It is finite dimensional by the ambient assumptions. It is not the whole theory. Let $\omega$ be the state corresponding to the **ambient** stress tensor $T(z)$, and write $c=24$ for the ambient central charge. The vacuum has norm one, so

```math
\langle\omega,\omega\rangle=c/2=12.
```

The notation $V_1=0$ means there are no weight-one states. Under this hypothesis, a weight-two state perpendicular to $\omega$ is primary. Restricting throughout to the specified real subspace, this identifies the primary space as

```math
P_2=\{x\in V_2:\langle\omega,x\rangle=0\}.
```

Why? $L_1x$ would have weight one, so it vanishes. $L_2x=\langle\omega,x\rangle\mathbf1$ vanishes by orthogonality. Higher positive modes land in negative weight and also vanish. This argument uses the grading assumptions; orthogonality alone is not a universal test for primarity in every theory.

## First project, then normalize

For a real weight-two state $w$, subtract its component along the known stress tensor:

```math
z=w-\frac{\langle\omega,w\rangle}{12}\omega.
```

This is the familiar orthogonal-projection formula from linear algebra. Its squared norm is

```math
N=\langle w,w\rangle-\frac{\langle\omega,w\rangle^2}{12}.
```

When $N>0$, set $x=z/\sqrt N$. Then $x$ is a real unit primary. When $N=0$, $w$ was pure stress and supplies no primary direction. It cannot be normalized into a valid input.

**Worked calculation.** Suppose $w=2x+\omega$, where $x$ is already a unit primary. Then $\langle\omega,w\rangle=12$ and $\langle w,w\rangle=16$. Projection gives $z=2x$ and $N=4$, so normalization recovers exactly $x$.

## The product is one OPE coefficient

VOA notation writes the field as

```math
Y(a,z)=\sum_{n\in\mathbb Z}a_{(n)}z^{-n-1}.
```

For a weight-two field, a physicist's weight-preserving mode is the coefficient of $z^{-2}$. It is $a_{(1)}$ in this convention, not $a_{(0)}$. Equivalently, if $\phi_a(z)=\sum_m(\phi_a)_m z^{-m-2}$, then $a_{(1)}=(\phi_a)_0$.

Define

```math
a*b=a_{(1)}b.
```

It lies in weight two because $2+2-1-1=2$. This is the state that multiplies the double-pole term in the OPE. The weight-two product is commutative here, but generally **not associative**. It is not multiplication of ordinary numbers or matrices.

It obeys $\omega*a=2a$ and has an invariant inner product. Consequently

```math
C(a,b,u)=\langle a*b,u\rangle
```

is symmetric in its three real weight-two arguments. For primaries, the product splits into a primary part and an ambient-stress part:

```math
a*b=\mu(a,b)+\frac{\langle a,b\rangle}{6}\omega.
```

The factor $1/6$ follows by pairing with $\omega$: metric invariance gives $\langle a*b,\omega\rangle=2\langle a,b\rangle$, and the stress norm is twelve. The notation $\mu$ means “project the product back into $P_2$.”

## A cubic on a sphere

For a primary $x$,

```math
f(x)=\langle\mu(x,x),x\rangle.
```

Restricting to $\langle x,x\rangle=1$ removes the artificial scaling freedom. We now have a real cubic evaluated on a finite-dimensional unit sphere. Distances such as $\|x-a\|$ are distances between normalized field states in this metric, not distances in physical space.

Only selected coefficients are needed for the criterion. The argument does not ask the reader to construct the entire weight-two multiplication table.

## Check your understanding

**1.** If $w=3\omega$, what remains after stress subtraction? A: a nonzero primary. B: zero, so this field cannot be used as a normalized primary input.

**2.** For a weight-two field, which VOA mode preserves the conformal grade of the state it acts on? A: $a_{(0)}$. B: $a_{(1)}$.

<details>
<summary>Answers and explanations</summary>

**1: B.** Its component perpendicular to $\omega$ vanishes. Dividing by its projected norm would divide by zero.

**2: B.** A mode $a_{(n)}$ shifts the weight by $2-n-1$. The shift is zero for $n=1$. The index differs from the physicist's zero-mode label.

</details>

**Next:** [Why does Ising appear?](03_ising.md). A stationary direction of this cubic produces an internal Virasoro stress tensor.
