# 5. Work through the certificate

[Previous](04_rounding.md) · [Learning path](README.md) · [Assumptions and sources](assumptions_and_sources.md)

**Question:** can we apply the sufficient criterion without confusing its conclusion with its assumptions?

Everything below is arithmetic or explanation of [core Q4–Q5](../../research/uniform_extraction_core.md) and [sharpness and calibration](../../research/sharpness_and_calibration.md). It is not a simulated experiment.

## An example using the repository's stated thresholds

Assume the exact ambient class and two actual real unit primaries. Suppose certified bounds establish

```math
f(x),f(y)\ge M-\frac1{32768},\qquad
\left|\langle x,y\rangle+\frac1{47}\right|\le\frac1{128}.
```

The two self-coupling deficits are below $1/50$, so the field-localization theorem applies. Each field is within

```math
\sqrt{\frac{1/32768}{2}}=\frac1{256}
```

of an exact Ising direction. The total primary-overlap error is at most

```math
\frac1{128}+\frac1{256}+\frac1{256}=\frac1{64}<\frac3{188}.
```

The corresponding exact Ising-stress overlap therefore has magnitude at most

```math
\frac{47}{192}\frac1{64}
=\frac{47}{12288}
<\frac{48}{12288}=\frac1{256}.
```

The gap forces zero overlap. The prior classification theorem now identifies the ambient VOA as moonshine. The spare margin is $1/12288$ in the Ising-stress overlap; it is not an optimal tolerance or an experimental resolution requirement.

## A failed test is not a different theory

Keep the same deficits but increase the certified overlap allowance to $1/64$. The sum becomes $3/128$, which is larger than $3/188$. This sufficient certificate no longer establishes the conclusion.

It does **not** follow that the VOA is not moonshine. The intervals might simply be too broad, or the supplied fields might be unsuitable. Even within the known moonshine theory, supplying the same maximizing direction twice fails the pair test: its mutual overlap is one rather than $-1/47$.

Likewise, a lower bound claiming $f(x)>M$ is inconsistent with the model and normalization. It is not “better than perfect” evidence and must not be clipped to a zero deficit.

## Optional second pass: what if the fields are not normalized primaries?

Let $w_1,w_2$ be actual real states of **exact weight two**, with the known ambient stress tensor $\omega$. Seven scalar inputs are used:

```math
n_i=\langle w_i,w_i\rangle,\quad
\tau_i=\langle\omega,w_i\rangle,\quad
q_i=\langle w_i*w_i,w_i\rangle\quad(i=1,2),
```

and $m=\langle w_1,w_2\rangle$. The symbols $q_i$ are mode-product coefficients; for nonprimary fields they must not be read from the primary-only three-point position formula without the appropriate stress-tensor terms.

Set $N_i=n_i-\tau_i^2/12$. Provided both $N_i>0$, stress subtraction and normalization give

```math
f(x_i)=\frac{q_i-\tau_i n_i/2+\tau_i^3/36}{N_i^{3/2}},
```

```math
\langle x_1,x_2\rangle=
\frac{m-\tau_1\tau_2/12}{\sqrt{N_1N_2}}.
```

**Single-field calculation.** Reuse $w=2x+\omega$ from Lesson 2 and write $F=f(x)$. Its scalars are $n=16$, $\tau=12$, and $q=8F+48$. The corrected cubic numerator is

```math
(8F+48)-12\cdot16/2+12^3/36=8F.
```

Since $N=4$, division by $N^{3/2}=8$ returns $F$. The apparently large raw cubic contained known stress contributions, not a stronger primary signal.

With intervals rather than exact scalars, every operation must enclose all permitted exact values. In particular, require a strictly positive lower bound for each projected norm and use conservative upper bounds for the error budget. The existing calibration checker performs outward interval arithmetic. This does not certify uncertain conformal grade, non-real inputs, unknown stress tensor, or empirical coverage of measurement errors.

## Why the square root is natural—and sharp here

A small displacement along a unit-sphere curve through a smooth nondegenerate maximum changes the value quadratically but changes the field direction linearly. Thus a loss of order $t^2$ naturally controls distance of order $|t|$, or the square root of the loss.

The project does not rely only on this picture: its sharpness note constructs such a curve inside the actual moonshine VOA and shows that the nearest maximizing direction remains the selected one. Hence no larger uniform exponent can replace $1/2$ near that example. This does not prove the numerical constants or the whole identification region are optimal.

## Check your understanding

**1.** The overlap intervals are too wide to pass the criterion. What is established? A: the theory is not moonshine. B: this certificate is inconclusive.

**2.** Seven-scalar calibration replaces which input requirement? A: preprocessed normalization and stress subtraction for actual real weight-two fields. B: all exact VOA, grading, and reality assumptions.

<details>
<summary>Answers and explanations</summary>

**1: B.** A sufficient condition need not be necessary. A failed bound can result from uncertainty or from the choice of fields.

**2: A.** The ambient theory, exact grade, real structure, and known stress tensor remain hypotheses. Calibration does not verify them.

</details>

## Continue into the research

Read [the core proof](../../research/uniform_extraction_core.md) in order Q0–Q4. Match Q0 to Lessons 1–2, Q2–Q3 to Lesson 3, and Q1/Q4 to Lesson 4. Then read [sharpness and calibration](../../research/sharpness_and_calibration.md).

To reproduce the unchanged selected certificates, run from the repository root:

```sh
python checks/verify_extraction_core.py
python checks/verify_calibration_and_sharpness.py
python checks/audit_quantitative_core.py
```

These are finite arithmetic and implementation checks, not proofs of the imported VOA classifications. No full Monster tensor is simulated.
