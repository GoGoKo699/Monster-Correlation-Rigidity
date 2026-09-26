# Selection bridge: two compatible minimal Virasoro components

26 September 2026. Baseline main: `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.

## What changed

Abe–Lam–Yamada's prior Theorem A.1 (arXiv:1705.09022) identifies any simple rational C2-cofinite holomorphic c24 CFT-type VOA with V1=0 and two orthogonal Ising vectors as moonshine. The earlier project target of reconstructing the entire Griess multiplication is sufficient but not necessary to finish classification. The existence of one compatible pair is a smaller exact target.

The new [two-field note](../research/two_field_selection.md) derives a sufficient correlation criterion in the additionally unitary, PCT-real setting. For two real unit weight-two primaries x,y,

- both self-three-point coefficients at least `46/sqrt(141) - 1/32768`;
- cross-two-point overlap within `1/128` of `-1/47`;

imply an exact orthogonal Ising pair and hence the underlying moonshine VOA. These inequalities refer to an EXACT admissible VOA and fixed field normalization. They do not test approximate VOA axioms or supply field finding, calibration, or an efficient experiment.

The quantitative proof uses the unitary Virasoro critical-value gap, a uniform near-maximum estimate, and Sakuma's discrete Ising overlap gap. All exact classification credit belongs to the source theorems. Priority of an equivalent robust formulation is not established.

## Claims kept distinct

| Claim | Status |
|---|---|
| General low-weight readout has a sharp5/6 cutoff in broad current-free unitary settings | Prior project assumption audit; not evidence of Monster-specific physics |
| Two orthogonal Ising vectors classify the c24 current-free holomorphic VOA | Imported Abe–Lam–Yamada theorem |
| The displayed finite-error correlation data imply such a pair | New source-based quantitative corollary with a written proof and68 scoped exact checks |
| The known moonshine theory attains the exact correlation condition | Explicit lattice Ising pair, prior Lam–Shimakura construction and checked normalization |
| Bare spectral/minimality assumptions force the pair | NOT established |
| A single Ising vector forces the whole classification | NOT established here; not a substitute for the two-vector hypothesis |
| Three data numbers identify arbitrary CFTs without class assumptions | False; the nonholomorphic product of48 Ising theories is a countercontrol |

## Next bounded research question

Determine whether the exact holomorphic/current-free/extremal hypotheses force a compatible pair, rather than only bounding every real cubic value. Any proposed implication must avoid assuming an Ising frame, the full Griess algebra, or a Monster action. A forced single saturated direction would be progress, but its compatibility with a second direction remains an obligation.

The one-number pair-score formulation in the note is an optional additional interaction optimization criterion. It must not be presented as already forced by the original spectral assumptions, and is not a demonstrated dynamical selection mechanism.

## Evidence and boundaries

The scalar/algebra checker uses integers and fractions, largest matrix4x4 and largest coefficient vector48. It does not verify the source classification proofs, construct a full VOA, or simulate a Monster tensor. All historical files and pending PRs are preserved; no manuscript, release or outreach is performed. See the integration record for actual CI and repository outcomes, not an assumed strict-replay pass.
