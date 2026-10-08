# Assumptions, notation, and source roles

[Learning path](README.md) · [Canonical proof](../../research/uniform_extraction_core.md)

## Exact assumptions

The ambient object is an **exact simple unitary, rational, C2-cofinite, holomorphic bosonic VOA of CFT type**, with central charge 24, no weight-one states, and finite-dimensional grades. The following explanations orient a physics reader to the formal hypotheses of [core Q0](../../research/uniform_extraction_core.md).

| Term | Meaning needed for this reading path |
|---|---|
| VOA | A graded state space with a vacuum, a conformal stress tensor, and a state-field map satisfying exact algebraic consistency identities. It organizes chiral OPE data. |
| Simple | No nonzero proper ideal of the VOA. |
| CFT type | Nonnegative integer grading and a one-dimensional weight-zero vacuum space. |
| Unitary | A positive Hermitian form and compatible antilinear conjugation giving the specified mode adjoints. |
| Real fields | States fixed by that conjugation; not arbitrary complex states with a convenient phase choice. |
| Rational | Complete reducibility of admissible modules in the VOA sense used in the core. This is a representation-theoretic condition, not “all coefficients are rational numbers.” |
| C2-cofinite | The quotient by the span of states of the form u(-2)v is finite dimensional; here u(-2) denotes the VOA mode indexed by -2. |
| Holomorphic | The VOA itself is its only irreducible module, up to isomorphism, in the setting of the theorem. This is stronger than analytic dependence on a chiral coordinate. |
| No weight-one states | The entire first conformal grade vanishes. This is not merely a choice to ignore currents. |

Gaberdiel's “meromorphic” terminology should not silently be replaced by the stronger holomorphic-module condition above. His Section 2.1 explicitly flags a terminology distinction, and Appendix A discusses differing rationality definitions. Yamauchi's OZ-type setting means one-dimensional grade zero and vanishing grade one, with the positive-real assumptions relevant to Section 4. Those low-grade conditions alone do not supply all the ambient classification hypotheses.

The normalized criterion additionally assumes two actual real unit weight-two primaries. The calibration extension begins with two actual real weight-two fields and a known stress tensor, then removes their stress components and normalizes them. Both versions retain the exact ambient class, conformal grade, and real structure as assumptions.

## A compact translation dictionary

| Notation | Read it as |
|---|---|
| V, V2, P2 | The whole chiral state space; its weight-two part; the real weight-two primary subspace used for the geometry. |
| omega | The ambient stress-tensor state, with squared norm 12. |
| a*b = a(1)b | The weight-two product, equivalently the physicist's weight-preserving zero-mode action for a weight-two field. |
| mu(a,b) | The primary projection of that product. |
| C(a,b,u), f(x) | The symmetric cubic coefficient and its diagonal value on a unit primary. |
| e, a | An internal Ising stress tensor; its centered, normalized ambient-primary direction. They are not the same vector. |
| c, r | Ambient charge 24; charge of an internal Virasoro subalgebra. |
| eps_x, eps_y, delta | Upper bounds on two normalized self-coupling deficits and the target-overlap error. They need not be equal. |

The mathematical formulas, rather than these plain-text table labels, define the mode conventions in [Lesson 2](02_weight_two.md).

## Which source does which job?

**Teaching anchors.** [Gaberdiel, hep-th/9910156v2](https://arxiv.org/html/hep-th/9910156v2) supplies the physics-first route. [Yamauchi, 2201.06887v1](https://arxiv.org/html/2201.06887v1), selected parts of Section 4, supplies the specialized algebraic supplement. The reading map uses section, equation, and theorem labels, so it does not depend on browser page numbering.

**Imported proof inputs.** The core attributes unitary conventions to [Dong–Lin, 1308.2361](https://arxiv.org/abs/1308.2361), and mode/product conventions to [Matsuo, math/0007169](https://arxiv.org/abs/math/0007169). The unitary Virasoro necessity theorem is attributed to Friedan–Qiu–Shenker via its explicit statement in [Wassermann, 1012.6003, pp. 1–2](https://arxiv.org/abs/1012.6003). The discrete Ising overlaps come from [Sakuma, math/0608709, Theorem 4.4](https://arxiv.org/abs/math/0608709). The ambient identification is [Abe–Lam–Yamada, 1705.09022v4, Theorem A.1](https://arxiv.org/abs/1705.09022v4).

These research references supply the imported theorem statements; the anchors provide the teaching route.

**Project argument.** [Uniform extraction](../../research/uniform_extraction_core.md) supplies the quantitative localization, overlap propagation, and composition with the prior endpoint. [Sharpness and calibration](../../research/sharpness_and_calibration.md) gives the additional bounds.

## Conclusion

The conclusion is an isomorphism of the **underlying VOA** to the moonshine VOA, conditional on the supplied fields satisfying the coefficient bounds. The numerical criterion is sufficient. Its field-distance exponent is sharp; its numerical tolerances are sufficient bounds.

See [results and assumptions](../RESEARCH_STATUS.md) for the theorem and supporting results.
