"""Exact outward square-root bounds with scale-aware dyadic precision.

This is arithmetic support, not a test of the supplied physical premises.
"""
from fractions import Fraction as Q
from math import isqrt

MAX_ROOT_BITS = 16384


class SquareRootPrecisionLimit(ArithmeticError):
    """The required dyadic denominator exceeds the declared work budget."""


def sqrt_bounds(x: Q, bits: int = 80) -> tuple[Q, Q]:
    """Enclose sqrt(x), retaining positive lower bounds for positive x.

    `bits` controls relative resolution for small values and absolute
    resolution for values at least one. Only exact rational inputs are used.
    Exceeding MAX_ROOT_BITS raises a typed, recoverable precision exception.
    """
    if isinstance(bits, bool) or not isinstance(bits, int):
        raise TypeError('integer bit count required')
    if not isinstance(x, (int, Q)) or isinstance(x, bool):
        raise TypeError('exact integer or Fraction radicand required')
    x = Q(x)
    if x < 0 or bits < 0:
        raise ValueError('nonnegative radicand and bit count required')
    if x == 0:
        return Q(0), Q(0)
    gap = x.denominator.bit_length() - x.numerator.bit_length()
    extra = max(0, (gap + 2) // 2)
    precision = bits + extra
    if precision > MAX_ROOT_BITS:
        raise SquareRootPrecisionLimit('square-root precision budget exceeded')
    d = 1 << precision
    k = isqrt(x.numerator * d * d // x.denominator)
    lo = Q(k, d)
    hi = lo if lo * lo == x else Q(k + 1, d)
    return lo, hi
