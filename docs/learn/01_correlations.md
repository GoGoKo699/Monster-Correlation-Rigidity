# 1. What are the data?

[Learning path](README.md) · Next: [Turn fields into geometry](02_weight_two.md)

**Question:** what three numbers does the normalized version of the theorem use?

Read Gaberdiel Sections 2.1, 3.1, 3.4, and 3.5 for the state, amplitude, OPE, and inner-product language. These notes specialize that language to the conventions in [core Q0](../../research/uniform_extraction_core.md).

## A state and its field are two descriptions of the same input

Write a chiral state as $x$ and its field as $\phi_x(z)$. The state–field correspondence makes the field depend linearly on the state. A linear combination of states therefore specifies a linear combination of fields. We are not choosing an arbitrary classical function of position.

The chiral conformal weight is the eigenvalue of $L_0$. In this project, the supplied fields have **exact weight two**:

$$
L_0x=2x.
$$

“Low energy” refers here to a low conformal grade. It is not a numerical energy in joules, an experimental bandwidth, or a claim that a laboratory can isolate that grade.

A primary state also obeys $L_nx=0$ for every positive integer $n$. This is stronger than merely having weight two. The ambient stress tensor has weight two but is not primary at nonzero central charge.

## Remove the known position dependence

For real weight-two primaries in the normalization of the core, the two-point function is

$$
\langle \phi_x(z_1)\phi_y(z_2)\rangle
=\frac{\langle x,y\rangle}{(z_1-z_2)^4}.
$$

The bracket on the left is a vacuum correlation function. The bracket in the numerator is the invariant inner product of the corresponding real states. Thus the two-point coefficient is an inner product, not the entire position-dependent function.

For three such primaries,

$$
\langle \phi_x(z_1)\phi_y(z_2)\phi_u(z_3)\rangle
=\frac{C(x,y,u)}{(z_{12}z_{23}z_{31})^2},
$$

where $z_{ij}=z_i-z_j$. The coefficient $C$ contains information about the state-field product. Conformal symmetry fixes the displayed position dependence, but does not by itself supply this coefficient.

For a unit vector $x$, define its self-three-point coefficient by

$$
f(x)=C(x,x,x).
$$

The normalized theorem takes $f(x)$, $f(y)$, and $\langle x,y\rangle$ as input. “Three coefficients” does not mean three individual measurement shots; the theorem does not specify a measurement protocol or sample complexity.

## Why normalization cannot be skipped

Linearity gives a useful calculation. Replacing a field by $2\phi_x$ multiplies its self-two-point coefficient by four and its self-three-point coefficient by eight. An unnormalized cubic can therefore be made large without changing the underlying direction at all.

For a nonzero real primary $w$, the scale-corrected quantity is

$$
\frac{C(w,w,w)}{\langle w,w\rangle^{3/2}}.
$$

It is invariant under positive rescaling. Under a negative rescaling, its sign changes. Flipping only $x$ also changes the sign of $\langle x,y\rangle$, so the two signs cannot be chosen independently just to make each inequality look favorable.

Throughout the proof, “real” means fixed by the theory's specified unitary conjugation, often called its PCT involution. On this subspace the metric is positive definite and the cubic is real. Real does not mean merely writing coordinates that look real in an arbitrary complex basis. No choice of a complex phase is silently absorbed into the hypotheses.

## The physical question

Suppose an exact candidate theory and two appropriate fields are supplied. Can unusually large normalized self-couplings, together with their mutual overlap, force that theory to have a particular algebraic identity?

This is a conditional identification question, not a procedure for discovering the fields. It also does not reconstruct a full nonchiral theory or an apparatus from correlator samples. The [assumptions page](assumptions_and_sources.md) separates what is assumed from what is concluded.

## Check your understanding

**1.** You double a primary field without renormalizing it. Its cubic becomes eight times larger. Have you moved closer to the theorem's extremal direction? A: yes. B: no; only the scale changed.

**2.** You replace $x$ by $-x$ while leaving $y$ fixed. Which changes sign? A: only $f(x)$. B: both $f(x)$ and $\langle x,y\rangle$.

<details>
<summary>Answers and explanations</summary>

**1: B.** After dividing by the norm, the unit direction is unchanged. The theorem bounds the normalized coefficient.

**2: B.** The cubic has three copies of $x$, and the overlap has one. Both acquire a minus sign. The two-point norm of $x$ is unchanged.

</details>

**Next:** [Turn fields into geometry](02_weight_two.md). The full theory is infinite dimensional, but the quantitative part of the argument uses a finite-dimensional weight-two space.
