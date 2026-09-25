# Coherent Leech quadratic-form encoding from a flat frame block

**Date:** 25 September 2026. **Base:** `5428fffc82ccd1ede8a4203b1e73acb6816de289`.
**Branch:** `research/leech-xxa-block`. Live branches and open PRs were checked; no open PR was present.

This completes a constructive ideal-angle implementation of the normalized A_0 -> X tensor X branch requested by the base work order. It is a second branch on the same 299-dimensional input sector, not the full Griess isometry or a standalone Monster test. The construction specializes standard projected-unitary encoding and exact amplitude amplification. It is not claimed as a new amplification algorithm, a quantum advantage, or a completed priority audit.

## 1. Target and result

Let A_0 be the complexified traceless symmetric 24 by 24 matrices, with Hermitian Frobenius inner product. The input is already a quantum state |A> in the explicit orthonormal basis of note 07, not a classical matrix loaded for free. Let lambda_r be one representative of each antipodal Leech short-vector pair, of squared length four, and N=98280. The target is

$$J_X|A\rangle=\frac1{\sqrt{5040}}\sum_{r=1}^{N}(\lambda_r^T A\lambda_r)|r,r\rangle.$$

Row/column placement here is a coordinate convention; all lambda_r are real. The amplitude is linear in A, including when A has complex entries. Note 07's fourth-moment identity implies J_X is an isometry on A_0. With the inherited Griess normalization,

$$(\Pi_X\otimes\Pi_X)W|A\rangle=\sqrt{3780/6929}\,J_X|A\rangle.$$

We give a clean deterministic ideal-angle circuit for J_X. A primitive coherent transfer has success probability **1/312, independent of A**. A known-angle dilution followed by **14 amplification rounds**, using 29 transfer/inverse calls, makes the transfer exact in ideal arithmetic without measuring or retaining an input label. Explicit hard-wired row preparation replaces a free loader assumption.

The unoptimized reference compiler specifies **57,349,301 logical instructions on 63 wires**, with 36 output wires and 27 workspace wires returned to zero on valid inputs. This is a sufficient finite construction, not a small-cost or optimal implementation. The gate library is X, H, CNOT, Toffoli, and arbitrary-angle Ry. Physical routing, fault-tolerant synthesis, input loading and canonical full-representation packing are excluded. No QRAM or call to an unknown Monster operation is used.

## 2. The frame identity and its complete input-space meaning

Set v_r=lambda_r/2. Then ||v_r||=1. In note 07's chosen coordinates,

$$\frac1N\sum_r(v_r)_i(v_r)_j(v_r)_k(v_r)_l
=\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}}{24\cdot26}.$$

This is the needed real fourth-moment identity; it does not require a uniform complex-state design. It follows from the explicit three-shape/Golay calculation in note 07. Writing |Omega>=sum_i|i,i>, the row frame operator is

$$F:=\frac1N\sum_r|v_r,v_r\rangle\langle v_r,v_r|
=\frac{I+S+|\Omega\rangle\langle\Omega|}{24\cdot26}.$$

On the 24 by 24 coordinate space its eigenvalues are

- 1/312 on the 299-dimensional symmetric traceless subspace;
- 1/24 on the one-dimensional identity direction;
- zero on the 276-dimensional antisymmetric subspace.

Padding coordinates 24,...,31 add kernel directions. The trace check is 299/312+1/24=1. In particular, for a complex matrix A,

$$F\operatorname{vec}(A)=\frac{\operatorname{vec}(A+A^T+(\operatorname{Tr}A)I)}{624}.$$

Thus the traceless symmetric subspace is an **eigenspace**, not merely a set of basis inputs having equal success probabilities. This stronger fact is essential: equal column norms alone would not establish input-independent amplification for arbitrary superpositions or exclude coupling to other source directions.

For a real fourth-moment design in dimension n, the same calculation gives success probability 2/[n(n+2)] on traceless symmetric matrices. The dependence on the number of sample vectors cancels from this scalar. It does **not** cancel the circuit cost of coherently preparing their labels and rows. The general frame-block construction is an elementary specialization of the established projected-unitary/singular-value framework [GSLW], not a novelty claim.

## 3. Coherent transfer and input-label erasure

Use two five-bit coordinate words x,y and an 18-bit row label R. Let R_N be a known circuit preparing

$$R_N|0\rangle=N^{-1/2}\sum_r|r\rangle.$$

Let B be a controlled row loader with

$$B|r\rangle|0\rangle|0\rangle=|r\rangle|v_r\rangle|v_r\rangle.$$

The implementation in section 5 leaves its scratch zero on **every** coordinate input, since each controlled rotation or phase computes and uncomputes a conjunction whose controls it leaves unchanged. Thus B restricts to a unitary on label and coordinate registers and can be inverted coherently.

Start with the note 07 vectorization J|A>=vec(A), prepare the uniform row label, and apply B^dagger. Projection of the two coordinate words onto zero would give

$$K\operatorname{vec}(A)=\frac1{\sqrt N}\sum_r(v_r^T A v_r)|r\rangle
=\frac1{\sqrt{312}}\frac1{\sqrt{5040}}\sum_r(\lambda_r^T A\lambda_r)|r\rangle.$$

The numerical identity is 16N=312*5040. Since K^dagger K=F, every unit input in A_0 has success probability 1/312. The successful component contains only the output row label; the original matrix label/coordinate state has been coherently contracted into amplitudes. No which-input record survives.

Simply measuring this predicate would be a probabilistic transfer and could destroy an unknown input on failure. It is not a repeat-until-success procedure on a freely re-preparable unknown state. Instead, the complete construction below is unitary and performs no such measurement.

## 4. Exact higher-rank amplification without reflecting about an unknown state

Let theta=arcsin(1/sqrt(312)). Choose m=14, beta=pi/58, and

$$c=\sqrt{312}\sin\beta<1.$$

The factor c is realized by a known flag rotation |0> -> sqrt(1-c^2)|0>+c|1>. Let L consist of uniform-label preparation, the two inverse row loaders, and this rotation. Define the source projector and the good projector, on the always-clean scratch sector, by

$$P_0=|0_R,0_f\rangle\langle0_R,0_f|\otimes I_{xy},\qquad
P_g=I_R\otimes|0_x,0_y,1_f\rangle\langle0_x,0_y,1_f|.$$

Neither projector depends on A. In particular P_0 does **not** test the 299-dimensional input subspace or require reflection about |A>. For a valid input psi=|0_R,0_f>vec(A),

$$P_0L^\dagger P_gL\,\psi=\sin^2\beta\,\psi.$$

This follows from the complete eigenvalue statement in section 2, so includes absence of coupling to the identity or padded modes. Define normalized vectors

$$g_A=P_gL\psi/\sin\beta,\qquad b_A=(I-P_g)L\psi/\cos\beta.$$

Both depend linearly on A. Put Pi=LP_0L^dagger. Direct calculation gives

$$\Pi g_A=\sin^2\beta\,g_A+\sin\beta\cos\beta\,b_A,$$
$$\Pi b_A=\sin\beta\cos\beta\,g_A+\cos^2\beta\,b_A.$$

Consequently the two-dimensional span is invariant under (2Pi-I)(I-2P_g), which rotates sin(beta)g_A+cos(beta)b_A into sin(3beta)g_A+cos(3beta)b_A. The same calculation holds simultaneously for every A and for inputs entangled with a reference. It is a high-rank singular-subspace calculation, not ordinary amplitude amplification with an unavailable reflection about an unknown input.

After 14 rounds, (2m+1)beta=pi/2, so the output is exactly g_A. The emitted phases implement L(I-2P_0)L^dagger(I-2P_g), the negative of that iterate. Fourteen is even, so their common minus signs cancel, including the relative sign needed in a future coherent branch combination. Clear the now-certain flag with X and copy the computational row label into a blank 18-bit word with 18 CNOTs. This copying is the isometry sum_r z_r|r> -> sum_r z_r|r,r>, not cloning arbitrary states.

This uses 15 forward L calls and 14 inverse L calls, 14 source and 14 good reflections, one initial J and one final label copy. Source reflection is an explicit phase conditioned on 19 bits; good reflection is conditioned on 11 bits. The mathematical dilution method is the known-success construction in [BHMT], section 2.1/Theorem 4. Projected-unitary and oblivious amplification are established more generally in [GSLW], especially the introduction and Theorem 28. The eigen-subspace argument above supplies the exact domain distinction for our broader source projector.

**Domain countercheck.** The identity direction has undiluted probability 1/24, not 1/312, so the same sequence does not yield the desired deterministic transfer on it. The input promise A in A_0 is not optional. The verifier checks this counterexample and a rank-three coherent amplification model.

## 5. Label convention and explicit finite row preparation

Write the label as tag + 4*payload, with two low tag bits and a 16-bit payload. All unused bits start at zero. Tag 3 is unused; invalid labels are outside the preparation support, although the compiled gates define unitaries there too.

**Tag 0: 552 pair rows.** Enumerate i<j in lexicographic order, rank k<276. Store k in payload bits 0,...,8 and one sign bit s in bit 9. The integer row a has a_i=4, a_j=4(-1)^s, other entries zero. Physical lambda=a/sqrt(8), and v=a/sqrt(32).

**Tag 1: 48,576 octad rows.** Enumerate the 759 Golay octads by increasing 24-bit codeword. Store octad rank k in ten bits and six independent signs in the remaining six. For ordered support i_0<...<i_7, fix sign at i_0 positive, use six free signs at i_1,...,i_6, and use their parity at i_7. This gives exactly the 64 even-parity sign patterns modulo simultaneous negation. Nonzero integer entries are +/-2.

**Tag 2: 49,152 full-support rows.** Store the exceptional coordinate k<24 in five bits and an eleven-bit Golay message in the remaining eleven. Use the extended cyclic Golay realization from note 07, with generator polynomial x^11+x^9+x^7+x^6+x^5+x+1 and its parity coordinate. Its generator rows 1,...,11 have coordinate zero equal to zero and span C_0={c in C:c_0=0}. This selects one representative of every codeword/complement pair. Set a_i=(-3 if i=k else 1)(-1)^(c_i).

These are the three source shapes in [S], section 6.2, in a specified Golay coordinate convention. Golay codes with these parameters are unique up to coordinate permutation [S], section 2.1. The native labels are not asserted to be Seysen's low-level Parker-loop labels or an existing canonical full-register encoding; converting to such a convention remains part of full-W integration. The quadratic coefficients are independent of the choice between lambda and -lambda, and using the same X basis sign on both outputs also cancels. No unspecified sign calibration of the full other cubic blocks is solved here.

The checker enumerates all 98,280 length-24 rows, checks norm, uniqueness up to antipodes, the lattice/Golay congruences, label inversion and exact fourth-moment contractions in batches. It does not generate the enormous Monster axis orbit.

### Uniform label preparation

Prepare shape amplitudes sqrt(552/N), sqrt(48576/N), sqrt(49152/N). Conditioned on the shape, prepare a uniform valid rank (276, 759 or 24) and use Hadamards on the free sign/message bits (1, 6 or 11). Every valid complete label then has amplitude 1/sqrt(N).

### Unsigned row loading

There are only 276+759+24=1059 unsigned magnitude templates. Each is a 32-entry vector of squared integer weights, padded by eight zeros, summing to 32. At each binary coordinate prefix, let w_0,w_1 be the sums below its two children. Apply a rotation by

$$2\operatorname{atan2}(\sqrt{w_1},\sqrt{w_0})$$

on its next bit, controlled by the shape/rank and that prefix. Zero subtrees are skipped. This is a finite direct gate construction with hard-wired small classical templates, not a query to a free coherent data-access device. The template scan cost is charged in full.

### Signs

For pair rows, condition a phase on the second coordinate and its sign bit. For octads, each free sign controls a phase at its own support position and at the last support position; there are twelve such linear terms per octad. For full-support rows, the distinguished coordinate contributes a minus sign and the eleven fixed Golay generators supply linear message-controlled sign phases. All phases are implemented by controlled Z decompositions, so there are no uncomputed sign registers.

Each controlled gate computes a conjunction into clean scratch, applies its target gate, and uncomputes. These target gates do not change the controls. The prior explicit X/H/CNOT/Toffoli/Ry decompositions are reused unchanged from circuits/seysen_qqa.py. At most 16 scratch bits are needed by the row, uniform or reflection components. On a quantum superposition of labels, this realizes the block-diagonal controlled loader, not an incoherent choice of classical circuit.

## 6. Resource count and error budget

The instruction count is produced by running the actual elementary-gate emission templates through a counting sink, then composing the fixed 29-call plan. It is not an asymptotic oracle estimate.

| Logical instruction | Entire normalized J_X circuit |
|---|---:|
| Toffoli | 33,936,255 |
| CNOT | 1,298,699 |
| Hadamard | 1,102,684 |
| X | 19,712,995 |
| Arbitrary-angle Ry | 1,298,668 |
| Total | 57,349,301 |

One single-coordinate controlled row loader has 575926 Toffoli, 21314 CNOT, 18992 H, 334006 X and 21314 Ry instructions. There are 58 such loader/inverse calls. The report separately prices the uniform loader, both reflections and the inherited 1722-instruction matrix vectorization. This is a deliberately direct finite upper bound; better table/control compilation may lower it considerably. It is not an optimality or practical-efficiency claim.

The 63-wire interface is: ten coordinate wires, one amplification flag, sixteen scratch wires, and two 18-bit output labels. The second label is untouched until the final copy. The initial J reuses the flag and some scratch and restores them before L begins. At the end coordinates, flag and scratch are zero: 27 clean work wires. No physical connectivity is assumed beyond availability of the stated logical gates. The independent cost of converting the native X label into a prescribed full Griess encoding is excluded.

Exactness means exact mathematical rotations. The reference Python angles use binary floating point. If every one of the 1,298,668 rotation occurrences has operator error at most zeta/1,298,668 and all discrete gates are ideal, telescoping bounds the entire circuit's operator error by zeta. This includes angle representation, synthesis and coherent reuse of the same gate; errors may not be assumed independent. For zeta=1e-12, reference double precision is not a justified worst-case synthesis certificate. No fault-tolerant T count, physical gate fidelity or 1e-12 hardware construction is supplied.

The ideal amplification removes postselection from **this known branch transfer**. It does not amplify the unknown-U membership test or improve the 1e-12 rejection threshold, nor does it change the old large statistical trial counts. The probability 1/312 and the Griess branch weight 3780/6929 refer to different operations and must not be interchanged.

## 7. Reproduction and validation scope

```sh
python circuits/leech_xxa.py                  # resource counts
python circuits/leech_xxa.py --plan           # complete hierarchical time order
python circuits/leech_xxa.py --emit-row       # stream one full row-loader gate list
OPENBLAS_NUM_THREADS=1 python checks/verify_leech_xxa.py
OPENBLAS_NUM_THREADS=1 python -O checks/verify_leech_xxa.py
OPENBLAS_NUM_THREADS=1 python -OO checks/verify_leech_xxa.py
```

The hierarchical plan plus the emission functions specifies every component, including inverses, flag angle, phase predicates and final CNOTs. It does not store or expand 57 million instructions by default. A new symbolic-angle/finite-gate-set compiler is not claimed.

The 51-check verifier validates exact row and frame arithmetic, all 1059 unsigned preparation trees, the three uniform-rank trees, 30 specialized signed elementary row circuits and their inverses, three tensor-square row circuits, a large coherent control conjunction, both reflected subspaces, and a rank-three coherent amplification model. Specialization fixes the label classically and removes inactive block controls; it is not simulation of the entire controlled loader on an arbitrary 18-bit quantum label. The control-decomposition check and the block-diagonal proof address that remaining composition analytically.

Largest dense operator dimension: 32. Largest dense state vector length: 1024. Largest row batch: 1024 by 24 integer coordinates. No 98280 by 299 encoding matrix, full 63-wire state, full amplified circuit simulation, or Monster multiplication tensor is formed. The numerical tolerance is 1e-10, with explicit sparse pruning budget 1e-11. Negative controls distinguish the identity mode and show the coherence loss from retaining an input label. Normal/-O/-OO reports agree locally. The results do not replace proof review or high-precision circuit verification.

Network cloning in this runtime failed. The original mounted seed's twelve scientific replays were rerun locally, but this is not a claim of local current-main reconstruction. The read-only PR workflow separately runs the unchanged root verifier on the exact current baseline and candidate. Recognized historical floating-report differences must retain both strict-failure and bounded-portability outcomes; no archived evidence or tolerance policy is changed.

## 8. Remaining work and attribution

The A_0 -> A_0 tensor A_0 component is still missing, as are the X/Q input sectors and their coherent combination into full W. Even the two now-constructed A_0 output branches are not a full probe and do not inherit the Monster stabilizer separately. Their native output encodings and relative signs must be reconciled before claiming a combined circuit.

This result is an access construction, not a new normalizer/rigidity theorem. The flat-frame observation, block encoding and amplification are standard mathematical/quantum techniques; the project contribution here is an explicit, normalized Leech specialization with priced loader and label erasure. Whether any part deserves a separate novelty claim has not been established. The original fixed-target normalizer priority audit remains outstanding.

Primary sources checked in this continuation:

- [S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, sections 2.1, 6.1-6.2 and equation (10.1.4). https://arxiv.org/pdf/2002.10921v5
- [BHMT] G. Brassard, P. Hoyer, M. Mosca, A. Tapp, *Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055v1, section 2.1 and Theorem 4. https://arxiv.org/pdf/quant-ph/0005055
- [GSLW] A. Gilyen, Y. Su, G. H. Low, N. Wiebe, *Quantum singular value transformation and beyond*, arXiv:1806.01838v1, introduction's projected-unitary encoding and Theorem 28. https://arxiv.org/pdf/1806.01838

Parsed passages were read. BHMT's printed pages 10-11 were also visually inspected successfully. Seysen screenshot requests failed, so no successful visual inspection of those pages is claimed. The normalization/frame proof from note 07 is an explicit dependency. No downloaded papers are bundled, and no source's full proof is claimed to have been independently rederived merely because its theorem was consulted.
