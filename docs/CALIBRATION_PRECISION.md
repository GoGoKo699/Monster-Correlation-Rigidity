# Scale-safe calibration arithmetic

[Overview](../README.md) · [Calibration identities](../research/sharpness_and_calibration.md) · [Reproduction](REPRODUCIBILITY.md)

## What was repaired

The exact seven-scalar identities do not depend on a field's positive overall
scale. The original square-root implementation nevertheless used a fixed
absolute dyadic grid. For very small positive norms, its lower square-root bound
could become zero and cause division by an interval containing zero.

The current `sqrt_bounds` chooses the grid from the size of the exact rational
radicand. It never replaces exact interval arithmetic with floating point, and
it never changes the theorem's comparison thresholds. The
[implementation erratum](../audits/calibration_scale_erratum.md) gives the concrete
failing input and separates the code correction from the unchanged theorem.

## Why the lower bound stays positive

Write a positive rational as $x=p/q$, with positive integers $p,q$. Let $g$ be
the bit length of $q$ minus the bit length of $p$. Then

```math
x>2^{-g-1}.
```

For the requested bit count $b$, the implementation sets

```math
h=\frac{1}{2^{b+e}},
\qquad e=\max\left(0,\left\lfloor\frac{g+2}{2}\right\rfloor\right).
```

Consequently $x\,2^{2e}>1$, so even when $b=0$ the lower grid point is positive.
An integer square root computes

```math
k=\left\lfloor\sqrt{\left\lfloor x/h^2\right\rfloor}\right\rfloor.
```

The returned lower endpoint is $kh$. The upper endpoint is the same number
when its square equals $x$, and otherwise $(k+1)h$. Therefore

```math
0<kh\le\sqrt{x}\le(k+1)h.
```

The enclosure width is at most $h$. In particular it is at most $2^{-b}$,
and for positive $x$ it is less than $2^{-b}\sqrt{x}$. The zero radicand is
handled exactly as the interval $[0,0]$. All comparisons are rational/integer
operations; the square root above explains the integer algorithm, not an
uncertified floating-point operation.

Since each certified projected norm is strictly positive, its root's lower
endpoint is positive. The same holds for the cross-norm product. Division by
these outward denominator enclosures is therefore well-defined.

## Work limit and input contract

The dyadic precision is capped at **16,384 bits**. This bounds the extra
square-root grid work, not the total memory or runtime for arbitrarily large
input integers. `sqrt_bounds` raises a typed `SquareRootPrecisionLimit` when
that limit is exceeded. The public `calibrated_criterion` catches precisely that
condition and returns `certified: false` with an explicit inconclusive reason.
It does not catch arbitrary programming errors and call them physical failures.

Supply seven `Interval` values with exact `Fraction` endpoints. Negative
radicands, reversed intervals, wrong types, and a norm interval that reaches zero
are not silently normalized or accepted. A broad uncertainty interval can remain
inconclusive even when the underlying fields happen to be ideal.

The scale tests cover tiny and large positive scales, independently scaled
fields, stress shifts, finite-width intervals, sign/duplicate/cap controls,
and the work-limit return. Exact squared inequalities independently check
outward root containment. These tests do not prove the ambient physical premises,
replace source classification proofs, or guarantee that every valid pair passes
a sufficient criterion.
