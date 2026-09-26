# Mixed-square target: verify the right closure, not just a small closure

26 September 2026. Baseline: `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.

The [new note](../research/mixed_square_extraction.md) replaces a preselected Ising endpoint with a finite, testable construction. From a Potts Virasoro vector u and a nonzero field y with u*y=(2/3)y, the formula

`d = y*y - (3/2)u*(y*y) + (10/3)||y||^2 u`

extracts a nonzero commuting component. Normalize it as

`v = 4||y||^2 d / (3||d||^2)`.

Its squared norm gives a candidate central charge, but it is not declared a Virasoro vector until v*v=2v is checked. The equality v*y=(4/3)y must also be checked; the automatic Rayleigh quotient is weaker.

In the known monstrous 3A core these checks give charge6/7 and a two-dimensional harmonic cubic of the required amplitude. Its stationary lines recover three Ising vectors without inputting one of them as an endpoint. They are not an orthogonal pair. The cubic algorithm is a conditional finite extraction, not a proof that the ambient assumptions provide the core.

A genuine counter-subtheory inside moonshine shows why closure alone is insufficient. The ternary repetition-code VOA M_D has central charge12/5 and five-dimensional weight-two space. A Potts component and a generic mixed seed again close in dimension4, but the companion has charge8/5. All32 idempotents of the complete weight-two algebra are explicitly classified; none has charge1/2. Even unrestricted successive modes of fields in that sub-VOA cannot produce an Ising vector. Adding the complementary ambient stress does not change this conclusion. Other ambient fields remain available; no global obstruction to moonshine is inferred.

| Claim | Status |
|---|---|
| One mixed square isolates the commuting channel | Derived from minimal-model fusion and invariant metric |
| A normalized companion is automatically a Virasoro vector | NOT claimed; residuals are required |
| A verified 3A-type plane determines its Ising directions | Explicit finite extraction; prior product structure |
| Any small positive mixed closure must contain Ising | False in the source-realized code subtheory |
| One arbitrary Potts eigenvector can always lead to an Ising field | Not established; the code subtheory is a counterexample to the unrestricted assertion |
| The original holomorphic/current-free assumptions force a suitable seed/core | Still open in this project |
| The extraction supplies an orthogonal pair and full classification | Not claimed |

The next selective statement must concern existence of an appropriate seed or compatibility across different closed sectors. Repeatedly expanding a trapped set of generators or improving its self-coupling does not address that existence step. Do not impose a known small table and then claim it has been derived from the physical assumptions.

All previous main files, pending branches, source attributions and license are preserved. No manuscript, release, outreach, full Monster simulation, practical field-finding algorithm, independent expert review or comprehensive novelty clearance is supplied.
