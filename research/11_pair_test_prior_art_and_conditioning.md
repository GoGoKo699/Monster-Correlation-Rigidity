# Pair-correlation certification: prior tests and the conditioning that remains

**Date:** 25 September 2026. **Base:** `85215c45005a3241485b99b57b2dc9de63b85702`.
**Branch:** `research/pair-test-priority`. Live main and branches were inspected; no open PR was present.

This is the bounded C04–C13 precursor comparison requested after note 10. It gives exact reductions, a finite-set query benchmark, and two elementary conditioning examples. It is not a comprehensive novelty audit or independent expert review. No historical theorem, threshold, report, or circuit is modified. In particular, no improved Monster rejection threshold or full probe compiler is supplied.

## 1. Conclusions before technical details

**Already established in general:** testing support in a known subspace and expressing acceptance as maximum supported-state fidelity; property testing membership in any known finite set of unitaries in a phase-insensitive Frobenius metric; and fixed-order correlation tests for a distinguished finite unitary group such as the Clifford group. The pair experiment fits the first framework exactly, and Wang's finite-set theorem already covers the existence of a Monster-membership test at the query level. These cannot serve as novelty claims.

**Also automatic for a fixed projector:** if its collective stabilizer is finite modulo phase, its rejection controls squared distance to that stabilizer with some finite constant. A local derivative calculation and compactness prove this. The square-root exponent alone is therefore not the distinctive result. Compactness supplies no useful numerical constant or explicit global small-error radius.

**What still needs the specific estimates:** identification of the low-order Griess projector's full complex collective stabilizer with phase times the Monster, and an explicit, normalized passage from its rejection probability to gate distance. The project provides particular spectral numbers, local constants and sufficient global thresholds. Whether their combination is a significant new quantitative specialization, or is subsumed by further primary results, remains unresolved.

Two examples make the distinction precise. A rank-two pair projector on two qubits has the same finite projective stabilizer for every parameter t>0, while its tangent sensitivity tends to zero. A real binary cubic family has a fixed finite ray stabilizer and a uniformly positive tangent sensitivity, yet develops a distant almost-symmetry with arbitrarily small loss. Neither family satisfies all Griess/Monster hypotheses, and neither falsifies C13. They separate local conditioning from the global exclusion of distant almost-symmetries.

## 2. The object under comparison

Let P be a rank-r orthogonal projector on C^d tensor C^d, with 0<r<d^2. For a fixed unknown U in U(d), write V_U=U tensor U and

$$\omega_U=V_U(P/r)V_U^\dagger,\qquad
\epsilon_P(U)=1-\operatorname{Tr}(P\omega_U).$$

The same U acts on both registers; preparation of P/r, measurement of P, and the d-dimensional logical subspace are trusted. A trial uses two forward U calls. This counts neither the preparation nor the measurement cost. The model is not arbitrary unknown channels, device-independent testing, uncontrolled leakage, or an adversarially changing sequence of gates.

The elementary identities are

$$\epsilon_P(U)=\frac{\|P-V_UPV_U^\dagger\|_F^2}{2r}
=\frac{\|[P,V_U]\|_F^2}{2r}.
\tag{1}$$

For the project, r=d=196883 and P=WW^dagger is the Griess multiplication projector. The exact stabilizer is H_P=U(1)rho(M), conditional on the already recorded source identifications and audits. The active C13 states

$$\epsilon_P(U)\le10^{-12}\Longrightarrow
D_{\mathbb M}(U)^2\le\frac{1681\pi^2}{12528}\epsilon_P(U),$$

with the real-orthogonal sufficient threshold 10^-10. Here D_M minimizes ||U-e^{i theta}rho(g)||_F/sqrt(d). It is not operator or diamond distance. Notes 01–10, including their repairs and access limitations, remain the dependencies; this comparison does not independently reprove all of them.

## 3. Exact reduction to a prior support-symmetry test

Set S_P=2P-I. It is a Hermitian unitary, and the two-element group C2 has the representation e -> I, a -> S_P. Its invariant-subspace projector is

$$\Pi^{C_2}=\frac{I+S_P}{2}=P.$$

LaBorde–Rethinasamy–Wilde [LRW], Algorithm 1 and Theorem 3.1, test G-Bose symmetry by measuring the group-average projector. On the representation above and input omega_U, their accepting probability is exactly 1-epsilon_P(U). One controlled S_P between two Hadamards is the corresponding C2 circuit.

This is a direct reduction of the *acceptance experiment*, not a computation of Monster generators. The auxiliary symmetry is C2, not M. Efficient access to S_P has not been created by renaming P: controlled reflection and probe preparation must still be implemented. LRW's section 3 states its preparation/representation access assumptions. Its Algorithm 1 is traced there to generalized phase estimation, and Harrow's thesis [H], section 8.1.1, gives the controlled-representation/Fourier procedure and its explicit dependence on representation and Fourier-transform costs.

With squared Uhlmann fidelity, Theorem 3.1 gives

$$\operatorname{Tr}(P\omega)=
\max_{\tau=P\tau P,\ \operatorname{Tr}\tau=1}F(\omega,\tau).
\tag{2}$$

The special-projector identity can also be proved immediately. Measurement of {P,I-P} bounds the fidelity from above by p=Tr(P omega). For p>0, tau=P omega P/p attains it: if A=sqrt(omega)P sqrt(omega), then sqrt(omega)tau sqrt(omega)=A^2/p, so the square-root trace is sqrt(p). This is not a new operational-fidelity interpretation.

**Ordinary invariance is a different property.** For P=|0><0|, the state |1><1| commutes with S_P but has zero support-test acceptance. LRW's Algorithm 2/Theorem 3.2 addresses ordinary G-symmetry through a different, prover-assisted optimization. It cannot be substituted for Algorithm 1 without changing the test.

**Limits of a converse reduction.** Any Bose projector can be represented as the positive sector of a reflection, but LRW accepts arbitrary input states. They need not lie on the restricted orbit U tensor U (P/r) U^dagger tensor U^dagger, need not have a known rank spectrum, and need not encode an unknown gate with finite collective stabilizer. For example, the full symmetric-subspace projector commutes with U tensor U for every U. The general support theorem cannot infer a finite gate group from those data alone.

### A Choi commutation version and its normalization

Put n=d^2 and |V_U>=vec(V_U)/sqrt(n). On this channel-Choi space define

$$Q_P=\frac{I+S_P\otimes\overline{S_P}}2.$$

It projects onto vectorized operators commuting with P. Direct vectorization of (1) gives

$$1-\langle V_U|Q_P|V_U\rangle
=\frac{\|[P,V_U]\|_F^2}{n}
=\frac{2r}{d^2}\epsilon_P(U).
\tag{3}$$

Thus the uniformly weighted Choi commutation experiment has the same zero set but a different rejection normalization. For the Griess rank r=d, its signal is 2/d times the tailored pair signal. It can also be prepared with two forward U calls, now on halves of entangled pairs; the associated known measurement is still not free. Equation (3) is a comparison of two specified tests, not a lower bound for all Choi-based or general quantum procedures.

## 4. Finite-unitary membership was already testable

Wang [W], Theorem 9 and Algorithm 5, explicitly test any finite set of known unitaries using copies of their Choi states. Its distance is our phase-minimized normalized Frobenius distance divided by sqrt(2). The paper distinguishes query complexity from implementing its general collective measurement efficiently. It does not require an efficient enumeration or matrix representation of an enormous finite group as an input-cost-free fact.

Here is a self-contained Gram-matrix form of that existing method, stated in our metric. This also shows exactly how it applies to a logical dimension that is not a power of two; no unknown padding action or altered phase convention is introduced.

Let S={W_1,...,W_M} have M>=2 projectively distinct target unitaries, let

$$|v_j\rangle=\operatorname{vec}(W_j)/\sqrt d,\qquad
0<a=\max_{i\ne j}|\langle v_i,v_j\rangle|<1.$$

Prepare K copies of |v(U)>=vec(U)/sqrt(d) with K forward U calls. Measure the projector onto the span of {|v_j>^(tensor K)}. All target rays are accepted with certainty. Let B_K have these tensor-power columns and G_K=B_K^dagger B_K. Then

$$\lambda_{\min}(G_K)\ge1-(M-1)a^K.$$

If D_S(U):=min_{theta,j}||U-e^{i theta}W_j||_F/sqrt(d)>=eta, with 0<eta<sqrt(2), then

$$\max_j|\langle v_j,v(U)\rangle|\le b:=1-\eta^2/2.$$

Whenever (M-1)a^K<1, the accepting probability is bounded by

$$p_{\mathrm{acc}}=c^\dagger G_K^{-1}c
\le\frac{M b^{2K}}{1-(M-1)a^K},
\qquad c=B_K^\dagger|v(U)\rangle^{\otimes K}.
\tag{4}$$

A sufficient choice for one-sided soundness p_acc<=1/3 is

$$K=\left\lceil\max\left\{
\frac{\log[2(M-1)]}{-\log a},\quad
\frac{\log(6M)}{-2\log(1-\eta^2/2)}
\right\}\right\rceil.
\tag{5}$$

This is a conservative explicit specialization of the existing finite-set tester, not a new testing algorithm. Different constants from Wang's displayed sufficient choice reflect the elementary Gram bound and the chosen failure probability.

**A proof-reading distinction.** Near its finite-set proof, the retrieved text describes the distinct one-copy Choi rays as linearly independent. Distinct rays need not be independent; more than d^2 such vectors cannot be. The argument only needs the K-copy Gram matrix at the selected K to be nonsingular, which the bound above proves. Thus this sentence is not a reason to discard Theorem 9. The checker includes six distinct projective D3 matrices whose one-copy Choi span has dimension four, while their four-copy Gram matrix has full rank six. No false raw-column independence hypothesis is imported.

### The actual Monster query benchmark

The unchanged, previously audited character excerpt gives

$$|\mathbb M|=808017424794512875886459904961710757005754368000000000,$$

$$d=196883,\qquad
\max_{g\ne e}|\chi(g)|=4371,\qquad a=4371/196883.$$

The *absolute* character maximum is needed for projective overlaps. A signed maximum alone would be insufficient. The exact target rays are projectively distinct, and the first Gram-separation term in (5) requires only 33 copies. The distance-dependent term dominates the following sufficient budgets:

| Promised phase-normalized Frobenius distance eta | K in (5), forward calls to U |
|---|---:|
| 0.1 | 12561 |
| 0.01 | 1259151 |
| 0.001 | 125918152 |

These are query-level constructions with an **uncompiled collective measurement on K Choi copies**. They are not practical algorithms, memory-efficient implementations, optimal query bounds, or quantum-advantage claims. The source theorem was introduced for qubit registers; the proof just supplied uses maximally entangled logical d-dimensional states and applies without changing the unknown gate outside that subspace.

For comparison, the current pair theorem by itself guarantees, for a promised D_M(U)>=eta,

$$\epsilon_P(U)\ge\min\{10^{-12},\ \eta^2/c^2\},
\qquad c^2=1681\pi^2/12528.$$

At each displayed eta, its available lower guarantee is only 10^-12. Repeating independent pair trials and accepting only if none rejects has false-acceptance probability at most 1/3 once

$$N=\left\lceil\frac{\log(1/3)}{\log(1-10^{-12})}\right\rceil
=1098612288668$$

trials have been used, or 2197224577336 forward U calls. This compares **sufficient upper bounds obtained from the currently proved estimates**. It is not a lower bound on the pair experiment, which could have much larger loss for these inputs, nor a proof of optimality of (5). It also ignores implementation costs on both sides. Nevertheless, two U calls *per trial* cannot be promoted to a two-query complete property test or a query advantage over prior finite-set testing.

### Fixed-order correlations are also an existing strategy

Gross–Nezami–Walter [GNW], Theorem 3.3, give a six-copy pure-state stabilizer test with a quantitative inverse statement. Remark 3.7 applies the Choi-state construction to Clifford-unitary testing without inverse-U access. Their test has structure making it efficiently implementable, unlike an arbitrary finite-set projector.

This is a direct conceptual precursor for rigid finite-unitary identification from fixed-order correlations, not a statement that their stabilizer/Clifford theorem automatically holds for the Griess projector. The groups, states, symmetry algebra, copy number, and quantitative inverse estimates differ. No Clifford-specific constant or nearest-stabilizer conclusion is silently transferred to the Monster. The relevant theorem and remark were read, not every proof in the entire paper.

## 5. For a fixed finite projective stabilizer, a square-root law is generic

### Proposition 1: fixed-projector estimate with unspecified constants

For a fixed rank-r P as in section 2, suppose

$$H_P=\{U\in U(d):[P,U\otimes U]=0\}$$

has finite quotient by U(1). Then there is a finite C_P such that every U satisfies

$$D_P(U)^2\le C_P^2\epsilon_P(U),\qquad
D_P(U)=\min_{R\in H_P}\|U-R\|_F/\sqrt d.
\tag{6}$$

This elementary compact-orbit consequence supplies neither a universal constant nor an explicit computable global radius from the stabilizer group alone. It is not claimed as a new stability theorem.

**Proof.** For a trace-zero Hermitian H, write K_H=H tensor I+I tensor H and

$$q_P(H)=\frac{\|[P,K_H]\|_F^2}{2r}.$$

The kernel consists exactly of infinitesimal stabilizers: [P,K_H]=0 if and only if exp(itH) lies in H_P for every real t. A finite projective stabilizer has only the scalar infinitesimal direction. Hence

$$\lambda_P:=\min_{\operatorname{Tr}H=0,\ \|H\|_{2,d}=1}q_P(H)>0.$$

If ||H||_op<=pi/4, the eigenvalues of K_H lie in [-pi/2,pi/2]. The chord inequality on this interval gives

$$\epsilon_P(e^{iH})\ge\frac4{\pi^2}q_P(H)
\ge\frac{4\lambda_P}{\pi^2}\|H\|_{2,d}^2
\ge\frac{4\lambda_P}{\pi^2}D_P(e^{iH})^2.
\tag{7}$$

A phase can be removed from a sufficiently small logarithm near any R in H_P so that H is centered. Left multiplication by R leaves both loss and distance unchanged. These neighborhoods form an open neighborhood N of H_P on which (7) applies. Its complement is compact and contains no zero of epsilon_P. If nonempty, its loss minimum m_P is strictly positive. Finally D_P(U)^2<=2, because U(1)I is contained in H_P and one can optimize the trace phase. Thus

$$C_P^2=\max\{\pi^2/(4\lambda_P),\ 2/m_P\}$$

suffices. If the complement is empty the local constant suffices. This proves (6). The number m_P is only existential in this proof.

For the Griess projector the earlier local calculation gives lambda_P=3132/1681, so (7) reproduces the already recorded squared prefactor 1681pi^2/12528. It does **not** determine the global entry threshold 10^-12. That threshold came from the explicit cubic/axes/involution/normalizer route, not from the abstract existence of m_P.

## 6. Fixed dimension and exact group do not control the tangent coefficient

### Proposition 2: a rank-d two-qubit family

For 0<t<=1/2, let

$$|\psi_t\rangle=\frac{(1+t)|00\rangle+(1-t)|11\rangle}{\sqrt{2(1+t^2)}},\qquad
P_t=\Pi_{\mathrm{sym}}-|\psi_t\rangle\langle\psi_t|.$$

Every P_t is a rank-two projector on C^2 tensor C^2. Its collective unitary stabilizer is exactly

$$H_{P_t}=U(1)\{I,Z\},\qquad Z=\operatorname{diag}(1,-1).$$

To prove completeness, collective unitaries already preserve Pi_sym, so they must preserve the ray psi_t. In matrix form U D_t U^T=e^{i phi}D_t, where D_t has distinct positive diagonal entries. Multiplying by its adjoint gives U D_t^2 U^dagger=D_t^2; thus U is diagonal. The two diagonal phases agree modulo pi, giving exactly the displayed group. This is not inferred from a numerical search.

Let R_theta be the real planar rotation. At the fixed rotation theta=pi/4,

$$D_{P_t}(R_{\pi/4})^2=2-\sqrt2,$$

$$\epsilon_{P_t}(R_{\pi/4})=
\frac12\left(1-\frac1{(1+t^2)^2}\right)\longrightarrow0.
\tag{8}$$

The Pauli X,Y,Z matrices are an orthonormal centered Hermitian basis in ||.||_(2,2). The three eigenvalues of q_(P_t) in this basis are

$$\frac2{1+t^2},\qquad
\frac{2t^2}{1+t^2},\qquad
\frac{2(1-t^2)^2}{(1+t^2)^2}.$$

The minimum is 2t^2/(1+t^2) on the stated interval. Thus a fixed dimension, fixed rank, and even the same exact finite projective stabilizer do not give a uniform local sensitivity. In the limit t=0 an extra continuous rotation symmetry appears.

This example concerns general pair projectors, not the special symmetric-cubic isometry of the project. In particular, it does not impose its balanced-marginal or Griess spectral identities. It obstructs a purported conclusion based solely on finite stabilizer/rank/dimension data, not one using those additional hypotheses.

## 7. Positive tangent sensitivity alone does not determine a global radius

### Proposition 3: a real cubic with a distant almost-symmetry

The following is a separate real O(2) tensor example. Define orthonormal symmetric tensors

$$v_3=\tfrac12(|000\rangle-|011\rangle-|101\rangle-|110\rangle),$$

$$v_1=\tfrac{\sqrt3}{2}|000\rangle+
\tfrac1{2\sqrt3}(|011\rangle+|101\rangle+|110\rangle),\qquad
v_t=\frac{v_3+t v_1}{\sqrt{1+t^2}},\quad0<t\le1.$$

Under planar rotations their two invariant subspaces have angular frequencies three and one, respectively. The reflection Z fixes both displayed tensors. Projecting a putative real ray symmetry onto the weight-one subspace forces its angle to be zero or pi. Therefore, for every t>0, the complete **real** ray stabilizer is the same four-element group

$$H_t=\{I,-I,Z,-Z\}.$$

For the ray loss ell_t(R)=1-|<v_t,R^(tensor 3)v_t>|^2, the local coefficient at the identity is

$$\lim_{\theta\to0}\frac{\ell_t(R_\theta)}{\theta^2}
=\frac{9+t^2}{1+t^2}\ge5.
\tag{9}$$

The tangent convention is normalized Frobenius: ||R_theta-I||_F^2/2=theta^2+O(theta^4). Since the stabilizer is discrete, this is the only tangent direction in O(2); the coefficient is uniformly positive.

Nevertheless R_(2pi/3) stays squared distance one from H_t and

$$\ell_t(R_{2\pi/3})=
1-\left(\frac{1-t^2/2}{1+t^2}\right)^2
=\frac{3t^2(1+t^2/4)}{(1+t^2)^2}\longrightarrow0.
\tag{10}$$

At t=0 the tensor acquires an extra *discrete* rotation symmetry, not a new infinitesimal symmetry. This produces a vanishing global barrier while (9) stays bounded away from zero. Consequently no uniform global-entry threshold follows merely from a lower bound on the local quadratic coefficient and a fixed exact finite stabilizer for all positive parameters.

The example is not an assertion about the full complex unitary stabilizer, an isometric Griess cubic, or the specific Monster constants. Its purpose is to distinguish two independent controls: local tangent conditioning and the loss cost of distant almost-symmetries. Both are explicitly supplied, in much more structured form, by the project-specific global argument.

## 8. Tensor-conditioning precursor and exact comparison boundary

Pfeffer–Seigal–Sturmfels [PSS], section 7 and Theorem 7.3, study congruence recovery from a real cubic tensor and bound an inverse-distance quantity called numerical non-identifiability. The theorem assumes a tensor with **trivial GL stabilizer**. It involves the conditioning of the input matrix and smallest flattening singular values. The authors separately define a local recovery condition number in equation (21) and explicitly distinguish its relation to their inverse-distance quantity.

It would be incorrect to replace their trivial-stabilizer assumption by the project's nontrivial finite stabilizer, to identify these two conditioning quantities without proof, or to treat their input as a unitary acting on a pair marginal. The checked theorem does not directly give C13's constants. Conversely the Monster result does not prove their generic tensor-recovery theorem: it uses a particular compact-group orbit and particular structural identities.

The positive message of the comparison is not that every unmatched phrase creates novelty. Generic inverse-orbit conditioning is already an established problem; Propositions 1–3 give elementary reasons the exact conditioning data matter here. The original source dependencies in notes 01–10, including missing original Norton/Zisser and earlier stability proofs, remain separately recorded. This continuation does not close those gaps.

## 9. Updated classification of the proposed contribution

| Statement or mechanism | Classification after this bounded comparison |
|---|---|
| Measure a known projector; acceptance is maximum supported-state fidelity | Direct C2 specialization of LRW Theorem 3.1 and earlier generalized phase estimation |
| Existence of a phase-insensitive membership tester for the finite Monster matrix set | Already covered by Wang's finite-unitary-set method; explicit Gram specialization above |
| Identify distinguished finite unitaries by fixed-order correlations without inverse U | Prior strategy, with the Clifford example in GNW; Monster constants do not follow automatically |
| Square-root loss-to-distance law for one fixed finite-projective-stabilizer P, with unspecified constant | Elementary compact-orbit consequence, Proposition 1; not a novelty claim |
| Exclude local ill-conditioning or distant almost-symmetries from exact group information alone | Not valid in general; Propositions 2–3 distinguish the missing controls |
| Full complex collective stabilizer of this low-order Griess projector is U(1)M | Source-dependent project-specific identification; further priority comparison remains necessary |
| Explicit parent gap, local coefficient, and global entry radius for that projector | Specific quantitative estimates; neither their novelty nor publication significance is established by this comparison |
| Efficient, practical, or query-superior Monster test | Not established; full W/P is not compiled and existing sufficient query bounds do not support this claim |

The remaining candidate is narrower than “quantumly test Monster membership” or “small error implies nearby symmetry.” It is an explicitly normalized, low-order correlation realization of this exceptional symmetry together with quantitative conditioning estimates. Whether that package is new and substantial remains a research question, not an endorsement inferred from passing scripts or failed searches.

## 10. Verification and reproduction

```
OPENBLAS_NUM_THREADS=1 python checks/verify_pair_prior_art.py
OPENBLAS_NUM_THREADS=1 python -O checks/verify_pair_prior_art.py
OPENBLAS_NUM_THREADS=1 python -OO checks/verify_pair_prior_art.py
```

The checker has **105 labeled checks**. They cover small random projector/reflection identities, the Choi dilution, the supported-fidelity optimizer, the ordinary-invariance countercontrol, powered finite-set Gram matrices, both conditioning families, and the Monster scalar query budgets. The dependency `data/monster_character_excerpt.json` is unchanged and its recorded SHA-256 is checked before use. Displayed character maxima are recomputed from the retained excerpt; the underlying full character-table audit is inherited, not rerun here.

Largest square matrix: 81 by 81. Largest state vector: length 256. A rectangular 256 by 6 matrix holds the small D3 tensor-power states. The large-group Gram matrix, full Monster matrices/tensor, and full probe circuits are not constructed. Stabilizer completeness, the compact-orbit proof, and the global counterexample conclusions are analytic arguments, not numerical searches or formal verification. Numerical tolerance is 1e-10; logarithmic budgets use 90-digit Decimal arithmetic, not a certified transcendental interval package.

Normal/-O/-OO reports agree locally. The unchanged original seed's twelve scientific replays were run, but this is not represented as a checkout or local replay of live main: network cloning failed. The read-only workflow separately checks the exact baseline and candidate. Strict historical byte mismatches and the unchanged bounded-portability comparison must remain distinct. No old recorded report or tolerance is changed.

All notes 01–10, prior checkers/circuits/data/results/audits, provenance, STATUS.md, root verifier, portability policy and original MIT license are preserved. Current summaries, work order, workflow and snapshot manifest are intentionally updated. No manuscript, release, outreach or large cloud simulation is performed.

## Primary sources and read depth

[LRW] M. L. LaBorde, S. Rethinasamy and M. M. Wilde, *Testing symmetry on quantum computers*, arXiv:2105.12758v3; Quantum 7, 1120 (2023). Section 3 assumptions; Algorithm 1, Theorem 3.1 (equation 42); Algorithm 2/Theorem 3.2; Appendix B.1. Relevant parsed statements and the support-fidelity proof were read. Published PDF printed page 6 (algorithm and access circuit) was visually inspected successfully.
https://arxiv.org/abs/2105.12758
https://quantum-journal.org/papers/q-2023-09-25-1120/

[H] A. W. Harrow, *Applications of coherent classical communication and the Schur transform to quantum information theory*, PhD thesis (2005), arXiv:quant-ph/0512255. Chapter 8, section 8.1.1, printed pages 157–159, generalized phase estimation. This is an actual dependency cited by LRW. The parsed derivation was read, and printed page 158 was visually inspected.
https://arxiv.org/abs/quant-ph/0512255

[W] G. Wang, *Property testing of unitary operators*, arXiv:1110.1133; Physical Review A 84, 052328 (2011). Metric in equations (4)–(6); Theorem 9/Algorithm 5 and proof, printed page 8; computational-cost boundary immediately after the permutation example. The relevant parsed proof was read. Screenshot requests for the metric/theorem pages failed, so no successful visual inspection is claimed. The powered-Gram argument here supplies the needed independence explicitly rather than inheriting a false raw-column assertion.
https://arxiv.org/abs/1110.1133
https://doi.org/10.1103/PhysRevA.84.052328

[GNW] D. Gross, S. Nezami and M. Walter, *Schur–Weyl duality for the Clifford group with applications: Property testing, a robust Hudson theorem, and de Finetti representations*, arXiv:1712.08628; Communications in Mathematical Physics 385, 1325–1393 (2021). Theorem 3.3 and Remark 3.7. Relevant statements and Choi discussion were read; printed page 20 containing the Clifford remark was visually inspected successfully. This is not a full audit of their stabilizer-testing proof.
https://arxiv.org/abs/1712.08628
https://doi.org/10.1007/s00220-021-04118-7

[PSS] M. Pfeffer, A. Seigal and B. Sturmfels, *Learning paths from signature tensors*, arXiv:1809.01588; SIAM Journal on Matrix Analysis and Applications 40(2), 394–416 (2019). Section 7, especially equations (19), (21), Theorem 7.3 and proof, and Corollary 7.4. Relevant parsed statements and proof were read; the requested PDF screenshot failed. Their numerical non-identifiability is not silently relabelled the local condition number.
https://arxiv.org/abs/1809.01588
https://doi.org/10.1137/18M1212331

No downloaded papers or font files are bundled. Every primary-source limitation remains explicit; a source being cited is not a claim that its entire paper or all of its dependencies were independently audited.
