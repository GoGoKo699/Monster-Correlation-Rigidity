"""Exact Virasoro/vacuum Ward algebra for Note 16, not a VOA construction.

All coefficients are rational. The Ward coefficient is formal in
T=<w,e_(1)v>; no division by a possibly zero physical three-point function.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb


def bc(n, k):
    """Generalized integer binomial coefficient, including negative n."""
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1)**k * comb(k-n-1, k)


def add(*terms):
    out = {}
    for coefficient, state in terms:
        for word, value in state.items():
            out[word] = out.get(word, F(0)) + coefficient*value
    return {word: value for word, value in out.items() if value}


class Vir:
    """PBW Virasoro module; h=0 means the vacuum quotient L_-1|0>=0."""
    def __init__(self, c=24, h=0):
        self.c, self.h = F(c), F(h)

    @lru_cache(None)
    def ins(self, k, word):
        if not word:
            return {} if k == 1 and self.h == 0 else {(k,): F(1)}
        b, tail = word[0], word[1:]
        if k >= b:
            return {(k,)+word: F(1)}
        return add((1, self.apply(-b, self.ins(k, tail))),
                   (b-k, self.ins(k+b, tail)))

    @lru_cache(None)
    def act(self, m, word):
        if m < 0:
            return self.ins(-m, word)
        if m == 0:
            return {word: self.h+sum(word)} if self.h+sum(word) else {}
        if not word:
            return {}
        k, rest = word[0], word[1:]
        out = add((1, self.apply(-k, self.act(m, rest))),
                  (m+k, self.act(m-k, rest)))
        if m == k:
            out = add((1, out), (self.c*F(m**3-m, 12), {rest: F(1)}))
        return out

    def apply(self, m, state):
        return add(*[(value, self.act(m, word)) for word, value in state.items()])

    def gram(self, left, right):
        state = {right: F(1)}
        for m in left:
            state = self.apply(m, state)
        return state.get((), F(0))

    @lru_cache(None)
    def mode(self, lam, index, word):
        """Mode of vacuum descendant L_-lam|0> acting on this module.

        Uses Y(L_-m u,z)=:partial^(m-2)T(z)/(m-2)! Y(u,z):.
        Finite ranges follow from the nonnegative descendant level.
        """
        if not lam:
            return {word: F(1)} if index == -1 else {}
        m, rest = lam[0], lam[1:]
        k, weight, level = m-2, sum(rest), sum(word)
        out = {}
        for j in range(max(-1, level+weight-index-1)+1):
            out = add((1, out), (bc(j+k, k),
                      self.apply(-j-m, self.mode(rest, index+j, word))))
        for j in range(k, level+m):
            inner = self.act(j-m+1, word)
            term = add(*[(v, self.mode(rest, index-1-j, w)) for w, v in inner.items()])
            out = add((1, out), ((-1)**k*bc(j, k), term))
        return out


def parts(n, top=None):
    """Partitions of n with all parts >=2, in descending order."""
    if n == 0:
        return [()]
    if n < 2:
        return []
    top = n if top is None else top
    return [(k,)+tail for k in range(min(top, n), 1, -1)
            for tail in parts(n-k, k)]


@lru_cache(None)
def word_pair(left_modes, p, q, h1, h2):
    """Formal coefficient of <0|L_left a_p b_q|v>, wt(v)=3.

    Outer weights are (2,3) or (3,2); their vacuum three-point sign is
    negative with the PCT-fixed real convention for the odd primary.
    """
    if not left_modes:
        if p+q != h1+h2+1:
            return F(0)
        level = p-(2*h1-1)
        return F(0) if level < 0 else -F(bc(h1+h2-4+level, level))
    m, rest = left_modes[-1], left_modes[:-1]
    return (((h1-1)*(m+1)-p)*word_pair(rest, p+m, q, h1, h2)
            + ((h2-1)*(m+1)-q)*word_pair(rest, p, q+m, h1, h2))


def composite_pair(lam, r, s):
    """Vacuum-descendant pairing with (e_r w)_s v, coefficient of T."""
    left = tuple(reversed(lam))
    out = F(0)
    for k in range(max(5-s, 4)+1):
        coefficient = (-1)**k*bc(r, k)
        if k <= 5-s:
            out += coefficient*word_pair(left, r-k, s+k, 2, 3)
        if k <= 4:
            out -= coefficient*(-1 if r % 2 else 1)*word_pair(left, r+s-k, k, 3, 2)
    return out


def pair_primary(lam, p):
    """Coefficient of <w,v> in <L_-lam 0, w_p v>, wt(w)=wt(v)=3."""
    coefficient = F(-1)
    for m in lam:
        coefficient *= 2*(m+1)-p
        p += m
    return coefficient if p == 5 else F(0)


def solve(matrix, rhs):
    """Exact Gaussian elimination, failing rather than silently using a pseudoinverse."""
    n = len(rhs)
    rows = [list(map(F, row))+[F(b)] for row, b in zip(matrix, rhs)]
    for i in range(n):
        pivot = next((j for j in range(i, n) if rows[j][i]), None)
        if pivot is None:
            raise ValueError('Singular descendant Gram matrix')
        rows[i], rows[pivot] = rows[pivot], rows[i]
        scale = rows[i][i]
        rows[i] = [v/scale for v in rows[i]]
        for j in range(n):
            if j != i:
                scale = rows[j][i]
                rows[j] = [a-scale*b for a, b in zip(rows[j], rows[i])]
    return [row[-1] for row in rows]


def reconstruct():
    """Return every rational certificate entry, not just the final coefficient."""
    vac, primary = Vir(24, 0), Vir(24, 2)
    output = []
    total = F(0)
    for n in range(3, 9):
        basis = parts(n)
        gram = [[vac.gram(a, b) for b in basis] for a in basis]
        rhs = [sum((bc(2, i)*bc(5-i, j)*composite_pair(lam, i-1, j-1)
                    for i in range(3) for j in range(6-i) if 8-i-j == n), F(0))
               for lam in basis]
        projection = solve(gram, rhs)
        vacuum_trace = [vac.mode(lam, n-1, (2,)).get((2,), F(0)) for lam in basis]
        primary_trace = [primary.mode(lam, n-1, ()).get((), F(0)) for lam in basis]
        trace = [v+196883*p for v, p in zip(vacuum_trace, primary_trace)]
        contribution = sum((p*v for p, v in zip(projection, trace)), F(0))
        total += contribution
        output.append({'weight': n, 'partitions': basis, 'gram': gram, 'pairing': rhs,
                       'projection': projection, 'trace': trace,
                       'vacuum_part': sum((p*v for p, v in zip(projection, vacuum_trace)), F(0)),
                       'per_primary_part': sum((p*v for p, v in zip(projection, primary_trace)), F(0)),
                       'contribution': contribution})
    return total, output


def reconstruct_two_point():
    vac, primary = Vir(24, 0), Vir(24, 2)
    total, rows = F(0), []
    for i in range(4):
        n = 6-i
        basis = parts(n)
        gram = [[vac.gram(a, b) for b in basis] for a in basis]
        rhs = [pair_primary(lam, i-1) for lam in basis]
        projection = solve(gram, rhs)
        trace = [vac.mode(lam, n-1, (2,)).get((2,), 0)
                 +196883*primary.mode(lam, n-1, ()).get((), 0) for lam in basis]
        raw = sum((a*b for a, b in zip(projection, trace)), F(0))
        total += bc(3, i)*raw
        rows.append({'weight': n, 'raw_trace': raw, 'star_coefficient': bc(3, i)})
    return total, rows
