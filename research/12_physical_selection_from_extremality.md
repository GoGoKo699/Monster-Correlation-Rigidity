# Physical selection before symmetry recognition

**Date:** 25 September 2026. **Base:** `109e1cffd3c61f374635fec0a36f97e972d373e5`.
**Branch:** `research/physical-selection`. Live main, branches and open PRs were inspected before work; no open PR was present.

## 1. The changed scientific question

The owner has explicitly redirected the project: investigate whether the Monster is special for an independently meaningful physical reason, not merely whether an engineered tensor has a recognizable finite symmetry. This instruction supersedes the previous coarse gate-soundness work order. Notes 01–11 and their evidence remain intact as a subsidiary mathematical record; their existence does not dictate the new objective.

The distinction is between choosing the Griess algebra and then recognizing its symmetry, and deriving restrictions on a quantum field theory without inserting the algebra or group first. This checkpoint takes the second route. It reconstructs a known spectral extremality criterion, uses a prior theorem that does **not** assume a symmetry group, and derives a bridge to the previously used OPE tensor identities.

The outcome is a partial selection statement, not a proof of the full moonshine uniqueness conjecture or a claim of new fundamental physics. The central charge, character, thermal one-point constraints, and several precise low-energy contraction identities are forced in the stated class. The complete weight-two multiplication and its Monster automorphism group have not been derived from those assumptions here.

## 2. An admissible class and an objective stated without the Monster

Consider nontrivial, simple, unitary, strongly rational **bosonic holomorphic chiral** conformal field theories. In VOA language: CFT type (unique vacuum and nonnegative integer weights), rationality and C2-cofiniteness, an invariant positive Hermitian form, and a single irreducible module for the full chiral algebra. Use its PCT-compatible real weight-two subspace, with positive invariant metric, when taking real tensor coordinates below. Unitarity supplies the Virasoro decomposition used in [H].

Holomorphicity here does **not** mean that there are no Virasoro primary fields: there are many. It means that there is only one irreducible sector for the *extended* chiral algebra. This is a substantial restriction, not a universal requirement on physical CFTs. The chiral theory may be paired with its complex-conjugate right-moving theory to obtain the nonchiral model discussed below.

Impose absence of conformal-weight-one fields, V1=0, so there are no chiral spin-one currents in this algebra. Among this class, minimize the positive chiral central charge c. Central charge controls the finite-size vacuum energy and the universal thermal/entanglement coefficients; it is an independently meaningful physical quantity. Minimal c is an optimization criterion, not a claim that an unspecified renormalization-group flow dynamically minimizes it.

No Monster action, Griess multiplication, character table, Ising-axis orbit, Virasoro frame or lattice construction is an input. In particular the large-symmetry condition called class S^n in Matsuo is **not** assumed.

This is a restricted theoretical selection problem. Removing holomorphicity, integrality, unitarity, the current-free condition or the minimization changes the problem. Neither a material realization nor a universal selection law across all physical systems is asserted.

## 3. The spectral minimum is c=24, without choosing that number first

For the stated holomorphic bosonic class, c is a positive multiple of eight. This is part of the modular character framework reviewed in [H, section 3]; it is not inferred from the Monster representation dimension. If eta is the Dedekind eta function, eta^c Z is a modular form of weight c/2, with its vacuum coefficient fixed. At c=8 and c=16 the corresponding modular-form spaces are one-dimensional. Therefore

Z_8 = E4 / eta^8,

Z_16 = E4^2 / eta^16.

Their expansions begin

Z_8 = q^(-1/3)(1 + 248q + ...),

Z_16 = q^(-2/3)(1 + 496q + ...).

Both necessarily have weight-one currents. At c=24, modular invariance and the single vacuum pole give

Z_24 = j + (dim V1 - 744).

Thus V1=0 forces

$$Z(\tau)=J(\tau)=j(\tau)-744
=q^{-1}+196884q+21493760q^2+\cdots.$$

Existence is supplied by the known moonshine theory, so the minimum of this constrained optimization is indeed 24. This use of a known example proves attainability, not uniqueness of the minimizer. The primary theorem used to constrain other candidates never assumes that they are that example.

Every minimizer has dim V2=196884. One state is the stress tensor omega; its orthogonal complement P2 consists of d=196883 Virasoro primary weight-two fields. The equality 196884=1+196883 is established here as a count of states, **not** as a decomposition into irreducible Monster representations.

As a physical corollary, in the diagonal nonchiral completion V tensor conjugate(V), the scalar gap is four: scalar operators have h=bar h; no weight-one states exist, and the first positive weights are two. In particular there is no nontrivial local scalar with scaling dimension below or equal to two. This removes relevant and marginal scalar perturbations in the Lorentz-invariant conformal-perturbation sense. It is not proof of a lattice realization, an RG attraction basin, robustness to Lorentz-breaking perturbations or to coupling additional sectors. The chiral central charges are c_L=c_R=24, not a total central charge of 24.

## 4. Extremality constrains thermal responses, not just state counts

For a Virasoro primary v of positive integer weight s, let o(v)=v_(s-1) be its degree-preserving zero mode and define the unnormalized torus one-point function

$$F_v(\tau)=\operatorname{Tr}_V\big(o(v)q^{L_0-1}\big).$$

Zhu modularity in the form used by [H, Theorem 3.1] makes this a weight-s modular form with trivial character at c=24. Its potential vacuum-pole coefficient is zero because a positive-weight primary has zero vacuum zero mode, and its constant term is zero because V1=0. Therefore F_v is a cusp form. For s=1,...,11 there are no such nonzero modular forms for the full modular group, so

$$F_v(\tau)=0,\qquad
\operatorname{Tr}_{V_n}o(v)=0\quad\text{for every }n.$$

This is the c=24 case of Hoehn's prior **conformal 11-design theorem**. More generally the trace on each homogeneous energy space of every field through weight eleven equals the trace of its projection onto the Virasoro vacuum module. Descendants of the identity are not set to zero: their responses are fixed by conformal symmetry.

The physical reading is microcanonical and thermal: the equally weighted average over an energy eigenspace cannot have a nonzero one-point response to one of these primary zero modes. This is NOT a claim that every eigenstate has the same diagonal matrix element, that all correlation functions vanish, that the whole OPE is Gaussian, or that eigenstate thermalization holds. No large finite symmetry group was assumed to make the cancellation occur.

At weight twelve the same argument leaves

$$F_v(\tau)=a_v\Delta(\tau),\qquad
\Delta=q-24q^2+252q^3-\cdots.$$

The coefficient a_v is a linear functional on weight-twelve primaries, not fixed by this genus-one argument. It may be zero for a particular v. Weight twelve is the first *modularly allowed primary one-point response*, not a claim that all CFT data below weight twelve are uniquely determined or that two theories could first differ there. The unknown weight-two three-point tensor is already present. Also vanishing is not monotone in weight: weights 13,14,15 vanish again because M1=M2=M3=0. This is a concrete boundary on what the thermal argument establishes.

## 5. The noncircular bridge to weight-two interactions

Write B=V2 and R_a b=a_(1)b. Because V1=0, B is a commutative metrized nonassociative algebra with unit omega/2. It is often generically called a Griess algebra in VOA terminology; that term does **not** establish that it is the particular Conway–Griess algebra.

Matsuo's trace theorem [M, Theorem 2.1] is usually presented under a large-automorphism-group assumption. Using that assumption here would defeat the physical-selection purpose. The needed replacement is explicit in [H, printed page 12, paragraph immediately before section 3]: Matsuo's proof remains valid when class S^(2k) / finite automorphism hypotheses are replaced by the statement that V_l for l<=n are conformal 2k-designs. Theorem 3.1 supplies those designs from extremality. For n=2 and k<=5, its hypotheses hold, and the invariant metric is nondegenerate by unitarity.

Thus we may use the trace identities without assuming Monster symmetry, Aut(V) finite, or that the weight-two algebra is already the Conway–Griess algebra. The source polynomials are regular at c=24. Substitution of c=24 and dim B=196884 yields, for primary a,b,c,

$$\operatorname{Tr}_B R_a=0,\qquad
\operatorname{Tr}_B R_aR_b=4620\langle a,b\rangle,\qquad
\operatorname{Tr}_B R_aR_bR_c=900\langle a_{(1)}b,c\rangle.$$

These are source-theorem consequences, not fitted coefficients or new trace formulae.

Normalize primary fields O_a by their two-point functions delta_ab/z^4. Their OPE begins

$$O_a(z)O_b(0)=\frac{\delta_{ab}}{z^4}
+\frac{\delta_{ab}T(0)/6+\sum_c C_{abc}O_c(0)}{z^2}
+O(z^{-1}),$$

where C_abc is real and fully symmetric in a PCT-compatible real orthonormal basis. The coefficient 1/6=2h/c is fixed by the stress-tensor Ward identity for h=2,c=24. The z^(-1) and regular parts include descendants and higher-weight primaries; they must not be deleted when testing crossing or associativity.

Let t=omega/sqrt(12), s=1/sqrt(3), and let L_a denote the primary-projected multiplication. Then

$$R_a=\begin{pmatrix}0&s a^T\\s a&L_a\end{pmatrix}.$$

Subtracting the two scalar cross terms at second order and the three at third order gives

$$\operatorname{Tr}L_a=0,\qquad
\operatorname{Tr}L_aL_b=\kappa\langle a,b\rangle,\quad
\kappa=4620-2/3=13858/3,$$

$$\operatorname{Tr}L_aL_bL_c=(900-1)C_{abc}=899C_{abc}.$$

In particular, the **physical three-point coefficients** obey

$$\boxed{\sum_{b,c}C_{abc}C_{a'bc}=
\frac{13858}{3}\delta_{aa'}.}$$

Every normalized linear combination of the first primary fields has the same total squared coupling strength to pairs of first primary fields. The complete squared tensor norm is d*kappa=2728404614/3. This total-strength statement does not determine which couplings are nonzero or their individual values.

This is the important change of logical direction: kappa is now a consequence of an independently specified extremal CFT class and prior modular/trace theorems, not an input obtained by naming the Monster algebra.

## 6. A further derived corollary: the contraction spectrum also is forced

The same replacement of hypotheses gives the fourth trace identity. Removing the stress-tensor direction as in note 02 gives its coefficients

alpha=496/3, beta=-116, u=965/9, v=40/3.

Define the unnormalized contraction operator F(X)=sum_i L_i X L_i on End(P2), the tensor map m(X)=sum_ij X_ij mu(e_i,e_j), and Q(X)=L_(m(X)). Then direct index contraction gives

$$F^2(X)=\alpha F(X)+\beta F(X^T)+\alpha Q(X)
+uX+vX^T+u\operatorname{Tr}(X)I.$$

This is the same finite-dimensional calculation as note 02, but its present inputs are the conformal-design trace theorem, not an assumed group action. Q is kappa times the orthogonal projector onto L(P2). Also F(I)=kappa I, F(L_a)=899L_a, and F preserves transpose parity. Therefore the roots on the symmetric complement satisfy

x^2-(148/3)x-1085/9=0,

and on skew matrices satisfy

(x+1/3)^2=282(x+1/3).

The multiplicities are determined from dimensions and superoperator traces, without a Monster character table. Since Tr L_i=0 and sum_i Tr L_i^2=d*kappa,

Tr_End F=0,

Tr_Sym F=d*kappa/2,

Tr_Skew F=-d*kappa/2.

For E=F/kappa the result is

| Subspace defined without a group action | Eigenvalue | Dimension |
|---|---:|---:|
| Scalar matrices | 1 | 1 |
| Multiplication operators L(P2) | 2697/13858 | 196883 |
| Symmetric complement, positive root | 155/13858 | 842609326 |
| Symmetric complement, negative root | -7/13858 | 18538750076 |
| Skew matrices, positive root | 845/13858 = 5/82 | 21296876 |
| Skew matrices, negative root | -1/13858 | 19360062527 |

The eigenvalues and multiplicities coincide with the previously computed ones. Here they are **not labelled as Monster irreducible representations**: no action of that group has been established on a general candidate. Degeneracy of this contraction operator is not evidence by itself for a specific symmetry group.

The second trace identity also gives a well-defined isometry W_C from C_abc and a normalized three-leg coefficient state with maximally mixed single-leg marginals. These are derived encodings of OPE data, not newly prepared laboratory states or automatically available operations in the CFT. The existing purely algebraic two-projection calculation then has the same nontrivial contraction norm 2697/13858 and the same three-register parent-gap value 11161/13858. This last implication retains note 02's proof dependency; the new scalar checker verifies its arithmetic, not its operator proof. It is not a claim that a CFT excitation gap equals this auxiliary finite-dimensional parent gap.

No full-group stabilizer identification, Monster-axis classification or global distance-to-Monster theorem follows from the spectral corollary alone. Those are precisely the conclusions that remain inappropriate to import from the known Moonshine example into an unknown extremal candidate.

## 7. What has been selected, and the unresolved interaction problem

The chain established within the stated assumptions is

**minimal positive c, holomorphic bosonic theory, no currents**

-> **c=24 and the J spectrum**

-> **conformal 11-design thermal constraints**

-> **specific OPE contraction identities and spectrum**.

The missing implication is that the complete multiplication is, up to an orthogonal change of basis, the Conway–Griess multiplication. Only after that may the classical automorphism theorem identify the group as the Monster. The sum rules are nonlinear constraints on the unknown C_abc; their existence is not a reconstruction of C_abc. Nor has this work exhibited another full physical theory satisfying the same hypotheses. Logical insufficiency of the current proof is not evidence of an alternative CFT.

The conditional theorem of Dong–Griess–Lam [DGL] shows why weight two is a meaningful target: under its regularity/holomorphic hypotheses, the c=24, V1=0 VOA is moonshine if its V2 product is the Griess algebra. Its last hypothesis must be proved, not treated as a consequence of the character. We checked its statement, not its entire proof in this continuation.

A relevant current-source update is Carpi–Codogni [CC26], which replaces the withdrawn older arXiv:1901.03079 entry. It still records moonshine uniqueness as open and distinguishes reconstruction of a full VOA from equality of partition functions. Its all-genus partition-function equality is conditional on a slope conjecture, and its reconstruction results have additional hypotheses. Consequently “compute one more partition function and declare the algebra unique” is not a justified plan. Only the indicated statements were checked; the geometric theorem proofs were not independently audited.

The new work order is an OPE consistency calculation with independent external field labels: derive the weight-two four-point constraints, including the weight-three primary and descendant channels, and determine which constraints go beyond the contracted trace relations above. A first bounded target is the Gram form of the antisymmetric weight-three OPE map and its consistency with the available weight-three primary multiplicity 21296876. The matching number in the contraction spectrum is a lead, not an assumed surjectivity or representation identification. No Monster irreducible decomposition may be used to close this calculation.

This is a route toward selection of interactions from physics. It is not another optimization of a recognition circuit, and it does not change the old gate-certification thresholds.

## 8. Attribution, evidence and limits

The minimal-character calculation, conformal-design theorem and trace formulae are established mathematics. The present contribution is their explicit noncircular assembly and conversion into the project's primary OPE normalization and contraction spectrum. Treat this as a derived corollary and research-direction correction, not a cleared novelty claim or a newly solved uniqueness theorem.

`checks/verify_physical_selection.py` contains **37 exact scalar checks** using integers and fractions only. It expands the relevant characters to weight 16, evaluates modular-form dimensions, checks scalar OPE normalizations and the polynomial/multiplicity reconstruction. It uses no Monster character data, no group matrices and no full OPE tensor. These checks do not verify the VOA existence/classification or the source theorems. Normal, -O and -OO outputs agree exactly locally.

Network git access was attempted and failed in the runtime. The unchanged historical root verification must therefore be run separately on the actual pinned baseline and candidate through the read-only workflow. Local execution of this new scalar checker is not advertised as local verification of a current-main checkout. Old report bytes and the existing portability policy are not altered. Report actual CI outcomes before integration.

The active status is now `PHYSICS_STATUS.md`; `STATUS_CURRENT.md` remains the unchanged ledger for the previous certification track. README and CURRENT state this distinction explicitly. All research notes 01–11, existing checks/circuits/data/results/audits, provenance archives, original status and license are preserved. No manuscript, release, researcher outreach or large simulation is performed.

## Primary sources and inspected passages

[H] Gerald Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1 (2007), Theorems 2.3–2.4, the trace-formula replacement paragraph at the end of section 2 (printed p.12), and Theorem 3.1/proof (printed pp.13–14). These passages were read; printed pages 12 and 13 were visually inspected successfully. In particular, the design-to-trace replacement is explicitly sourced rather than inferred from similar terminology.
https://arxiv.org/abs/math/0701626

[M] Atsushi Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1; Communications in Mathematical Physics 224 (2001), 565–591. Theorem 2.1, its normalization/Casimir setup, Corollary 4.1 and Note 4.2 were read. Printed page 16 was visually inspected successfully. The corollary is displayed for moonshine; its applicability here comes from the general theorem and [H]'s replacement, not an assertion that the unknown algebra is already Griess.
https://arxiv.org/abs/math/0007169

[DGL] Chongying Dong, Robert L. Griess Jr., Ching Hung Lam, *On the uniqueness of the moonshine vertex operator algebra*, arXiv:math/0506321; American Journal of Mathematics 129 (2007), 583–609. Conditional uniqueness Theorem 1 and introductory discussion inspected; printed page 2 was visually checked. Full proof not audited in this continuation.
https://arxiv.org/abs/math/0506321

[CC26] Sebastiano Carpi and Giulio Codogni, *Vertex operator algebras, partition functions and Teichmueller modular forms*, arXiv:2605.26972 (26 May 2026), introduction Corollary 1.2, Conjecture 1.3, Theorem 1.4; section 9 Corollaries 9.1/9.3 and Question 9.4; section 14 uniqueness discussion. Indicated parsed passages were read and printed page 6 was visually inspected. This supersedes arXiv:1901.03079, withdrawn as superseded on 29 May 2026. We do not use an all-genus equality or reconstruction statement as an unconditional theorem identifying the Monster.
https://arxiv.org/abs/2605.26972

Source notational caution: some extracted/displayed digits in [CC26]'s introductory McKay illustration appear inconsistent with the standard q expansion. None is used as numerical data; our coefficients are independently generated from E4^3/Delta. The current-source uniqueness discussion, not those digits, is the reason for citing it. No downloaded paper or font file is bundled.
