# Projected Jordan multiplication and a clean complete A0 sector

**Date:** 25 September 2026. **Base:** `c51e5ffaf06b90101c70df1d4f5347aa03b9cc14`.
**Branch:** `research/jordan-a0-sector`. Main, branches, and open PRs were read before work; no open PR was present.

This note completes the remaining A0 output branch and supplies a constructive coherent combination of all three branches, in a declared tagged encoding. It does **not** complete W on its 196883-dimensional input space. The result is an ideal-angle circuit construction and resource upper bound, not a practical implementation, new amplification algorithm, or novelty clearance for the rigidity theorem.

## 1. Result and boundaries

Let A0 be the 299-dimensional complexified space of symmetric traceless 24 by 24 matrices. Let E_b be the real orthonormal basis from note 07, with inner product Tr(A*B). Define

$$J_A|A\rangle=\frac1{\sqrt{308/3}}\sum_{b,c}4\operatorname{Tr}(AE_bE_c)|b,c\rangle.$$

Then J_A is an isometry. Its circuit in `circuits/jordan_aaa.py` has **16957 instructions on 33 wires**, of which 20 are native output labels and 13 are clean workspace. A Bell-insertion/projected-transfer primitive has squared singular value **77/288 on all A0**. Dilution by squared amplitude **72/77** changes this to 1/4, so **one amplification round** implements the normalized isometry exactly in the ideal-angle model. Both output identity directions are excluded.

Combining J_A with the previously constructed J_X and V_Q gives

$$W_{A0}|A\rangle=
\sqrt{77/6929}\,J_A|A\rangle+
\sqrt{3780/6929}\,J_X|A\rangle+
\sqrt{3072/6929}\,V_Q|A\rangle,$$

where the three terms occupy mutually orthogonal, tagged AA, XX and QQ output sectors. This is the restriction of the normalized source multiplication isometry to A0, in the basis convention of notes 07-08 and section 6 below. The selectors and all temporary work are erased coherently. The explicit hierarchical composition in `circuits/a0_sector.py` costs **135774249 logical instructions on 105 wires**, with **40 output wires and 65 clean work wires**.

Each output register uses **20 physical qubits**, not a canonical 18-qubit packing: two sector bits and an 18-bit payload. The valid subspace still has logical dimension 196883. No conversion to an existing canonical Monster-register implementation is supplied or priced. The input covers only **299/196883** of the full logical dimension. Neither this restricted isometry nor any isolated branch is a replacement for the full Monster test.

All counts use X, H, CNOT, Toffoli and arbitrary-angle Ry, with unrestricted logical connectivity. They exclude fault-tolerant synthesis, physical routing and arbitrary classical input loading. No postselection, QRAM, unknown-U call or unpriced coherent table oracle occurs in these branch constructions. The combined count is large because it includes the explicit Leech loader and controlling every elementary instruction.

## 2. Source product and Bell-insertion factorization

The source restriction is [S, Eq. (10.1.3)]

$$F_S(A,B,C)=4\operatorname{Tr}(ABC).$$

On real symmetric matrices this corresponds to R_A(B)=2(AB+BA). On A0 both multiplication indices must be projected to the traceless subspace. Note 07 derives the squared contraction 308/3 and the source-to-quantum cubic scale 1/sqrt(2). No source scaling or earlier threshold is changed here.

For general n define the orthogonal Hilbert-space projection

$$\Pi_0(B)=\frac{B+B^T}{2}-\frac{\operatorname{Tr}B}{n}I.$$

Transpose here is linear, not conjugate transpose; Pi_0 is nevertheless an orthogonal projector for the complex Hermitian Frobenius inner product. Define the isometry D by

$$D(A)_{ij,kl}=\frac{A_{ik}\delta_{jl}}{\sqrt n}.$$

A circuit realizes D by vectorizing A, adjoining |Phi_n>=sum_j|j,j>/sqrt(n), and swapping the two middle coordinate words. The raw projected transfer is

$$T_n=(\Pi_0\otimes\Pi_0)D.$$

For real symmetric basis matrices E_b,E_c and symmetric A,

$$\langle E_b\otimes E_c,D(A)\rangle
=\operatorname{Tr}(AE_bE_c)/\sqrt n.$$

Consequently on A0,

$$T_n(A)=\frac{\mu_0^\dagger(A)}{4\sqrt n},\qquad
\mu_0^\dagger(A)=\sum_{b,c}4\operatorname{Tr}(AE_bE_c)E_b\otimes E_c.$$

The factor 4 sqrt(n) is essential. The tensor is not obtained by preparing two copies of the unknown A; D appends one *known* Bell state.

## 3. Full operator calculation, not equal column norms

Put S_1,S_2 for the swaps within the two output pairs and Q=|Omega><Omega|/n for their normalized identity projections. Expanding

$$(\Pi_0\otimes\Pi_0)=((I+S_1)/2-Q_1)((I+S_2)/2-Q_2)$$

and contracting D gives the following identity for **every complex n by n matrix B**:

$$
T_n^\dagger T_n(B)=
\frac{n+2}{4n}B+\frac{\operatorname{Tr}B}{4n}I
-\frac{B+B^T}{n^2}+\frac{\operatorname{Tr}B}{n^3}I.
\tag{1}
$$

For example the symmetrizer-only contribution is ((n+2)B+(Tr B)I)/(4n). Each single trace-subtraction term contributes -(B+B^T)/(2n^2), and the double subtraction adds (Tr B)I/n^3. This supplies a direct derivation of (1), without invoking an irreducibility assumption for the orthogonal group.

On A0 the result is

$$T_n^\dagger T_n=p_n I_{A0},\qquad
p_n=\frac{(n+4)(n-2)}{4n^2}.$$

In particular

$$p_{24}=77/288,\qquad16\cdot24\cdot p_{24}=308/3.$$

This proves both the normalization and that A0 is an eigenspace of the **full** source operator, with no coupling into other source directions. The formula also shows why the input promise matters. At n=24 the antisymmetric eigenvalue is 13/48 and the identity eigenvalue is 299/576. Padding coordinates outside 0,...,23 add kernel directions because both outputs are projected into the 24-coordinate spaces.

Omitting trace removal gives 13/48 instead of 77/288 on A0. The missing difference 1/288 is the contribution of the two identity cross terms. It is not permissible to use the full symmetric-matrix product in place of its projected version, even though the numerical difference is small.

For n=2 this Jordan branch vanishes; the normalized construction here is for n=24. The general formula is a calculation within ordinary symmetric-matrix multiplication, not a new exceptional-algebra theorem or a claim that every n has the same amplification schedule.

## 4. An all-input-clean basis change is required

The original `seysen_qqa.py` circuit guarantees clean workspace on its **valid** input subspace. It does not promise that behavior on every intermediate coordinate state. Its descending off-diagonal inputs can leave an orientation bit set. This does not invalidate notes 07-08, which use the vectorization on its specified domain, but prevents treating that circuit as an all-input-clean ambient coordinate unitary without further work.

The new `clean_basis()` circuit extends the same valid-input map to an orthogonal unitary U_J on all 32 by 32 coordinate labels, while restoring all eleven temporary wires for every coordinate input.

For an off-diagonal input, compute c=[x=y] and an orientation bit b=[x>y], sort x,y conditionally on b, apply H to b only when c=0, unsort conditionally on b, and erase b by xoring the final comparison [x>y]. Thus

$$|i,j\rangle\mapsto(|i,j\rangle+|j,i\rangle)/\sqrt2\quad(i<j),$$

$$|j,i\rangle\mapsto(|i,j\rangle-|j,i\rangle)/\sqrt2\quad(i<j).$$

Diagonal inputs bypass that H and undergo the same 23-step Helmert transform as in note 07; levels 24,...,31 are unchanged. Recomputing equality erases c. Each comparison and multi-control conjunction also restores its scratch.

The logical A0 labels are exactly

$$\mathcal L=\{(i,j):0\le i\le j<24\}\setminus\{(0,0)\}.$$

Consequently

$$U_J\Pi_{\mathcal L}U_J^\dagger=\Pi_0$$

on the coordinate space. Both U_J and its inverse are clean on every superposition, including padded or antisymmetric inputs. The construction is new code; the historical vectorization circuit is not rewritten.

The membership predicate has a short reversible implementation. On five-bit words, y<24 is the negation of y_4 AND y_3. Hence validity is [x<=y<24] XOR [(x,y)=(0,0)]. Compute [x>y], toggle the validity flag with these conditions, then uncompute the comparator. The checker tests every 1024 input labels with both initial target-bit values.

## 5. One clean amplification round and its relative phase

Use four five-bit coordinate words x,y,z,t and a flag f. The first pair holds the arbitrary native A0 input; the second pair and the flag begin at zero. Define L as the chronological sequence

1. U_J on x,y;
2. prepare |Phi_24> on z,t;
3. swap y,z;
4. U_J^dagger on each output coordinate pair;
5. rotate f with successful amplitude c=sqrt(72/77).

The Bell circuit prepares a uniform five-bit coordinate less than 24 and copies it to its partner; its cost is explicitly included. For all valid inputs the accepted part of L is (1/2)J_A|A> with flag one. The fixed source and good projectors are

$$P_s=I_{xy}\otimes|0_{zt},0_f\rangle\langle0_{zt},0_f|,$$

$$P_g=\Pi_{\mathcal L}^{xy}\otimes\Pi_{\mathcal L}^{zt}\otimes|1_f\rangle\langle1_f|.$$

They do not reflect about the unknown input. Equation (1) gives P_s L^dagger P_g L psi=(1/4)psi on every valid source state. The higher-rank two-projection calculation from note 08 therefore applies with angle pi/6: one standard amplification iterate sends the success amplitude sin(pi/6) to sin(pi/2)=1. Known-success dilution/amplification is established prior work [BHMT, section 2.1/Theorem 4]; the domain and normalization here are explicitly checked rather than assumed from a rank-one search analogy.

The actual chronological emitted sequence is

$$L,\quad(I-2P_g),\quad L^\dagger,\quad(I-2P_s),\quad L.$$

This differs by a minus sign from one standard amplification round, so its output is **-J_A|A> with f=1**. This phase is immaterial for an isolated state but matters when combining branches. The code applies Z_f, implemented as H-X-H, followed by X_f. This corrects the minus sign and clears the flag, giving +J_A|A> with every work wire zero. The checker compares amplitudes rather than fidelity alone and includes the uncorrected-minus-sign countercheck.

Native Jordan resources are

| Instruction | Count |
|---|---:|
| Toffoli | 7657 |
| CNOT | 1571 |
| H | 447 |
| Ry | 444 |
| X | 6838 |
| Total | 16957 |

There are 33 wires: twenty output-label wires, the flag, two validity flags, one comparator bit and nine reusable scratch wires. The output is a native pair of A0 basis labels, not two vectorized 24 by 24 matrices.

## 6. Coherent combination in one declared logical encoding

A statement that three separately normalized branches exist does not itself provide their coherent combination. We specify the branch controls, output layout, relative signs, routing and selector erasure.

Each output register has an 18-bit payload and a two-bit sector tag:

| Sector tag | Valid payload |
|---|---|
| 0 = A0 | i+32j in low ten bits, (i,j) in L; upper eight bits zero |
| 1 = X | the complete 18-bit native Leech label from note 08 |
| 2 = Q | s+4096i with s<4096, i<24; payload bit 17 zero |
| 3 | outside the logical space |

This is an orthonormal tagged encoding with valid dimension 299+98280+98304=196883. It uses twenty physical qubits per output. Compatibility with an existing packed 18-qubit implementation is **not** a free operation and is outside this bound.

The source A0 basis and the Q coordinate basis use the same 24-coordinate frame as the Leech rows. The inherited source restrictions AAA, AXX and AQQ have the same positive scale after the common 1/sqrt(2) conversion. An X basis sign occurs twice in AXX and cancels; changing a Leech representative to its antipode also cancels. The Q spinor inner product is basis independent. Thus these three branches define one consistent restricted source cubic, not three independently adjustable phases. This uses note 07's identification of the source cubic with the project cubic. It does not fix or compile the remaining XXX/QQX blocks or a canonical Parker-loop labelling.

Prepare a two-bit selector with amplitudes sqrt(77/6929), sqrt(3780/6929), sqrt(3072/6929) on 0,1,2, and zero on 3. For each selector value, compute a branch-control bit and apply the corresponding **elementwise controlled** clean circuit. The implementations give phases +1,+1,+1: the Jordan odd-round phase was corrected above; the Leech construction has fourteen rounds; the Bell/vectorization branch has the specified positive amplitudes.

All branches share a ten-bit source matrix label, initially containing |A>. Reserve ten extra coordinates for AAA, twenty-four spinor wires for QQA, seventeen shared work wires, and two initially blank tagged output registers. Route the AAA output labels or QQA coordinate/spinor words into those output payloads using controlled swaps; XXA writes directly to the common output payloads. Set both sector tags from the active branch control. Then uncompute that control using the unchanged selector.

After the three controlled operations, the state is

$$\sum_{s=0}^2\sqrt{w_s}\,|s\rangle_R|s,s;J_sA\rangle_{\rm outputs}|0\rangle_{\rm work}.$$

Xoring the first output's sector tag into R clears the selector. The tag is part of each logical output register, not an uncounted garbage register. The final map is the coherent sum in section 1 with all other wires zero. Tracing out R **before** this erasure would instead remove coherence between the three branches.

No unknown input is copied, measured, reflected about or re-prepared. The argument is linear and therefore extends to inputs entangled with a reference. It also proves norm preservation: the three ranges are orthogonal and the three weights sum to one. Since all nonzero source-cubic restrictions containing A are precisely AAA, AXX and AQQ, this is a complete A0 sector, not merely a list of branches.

## 7. Controlling circuits is charged, including Hadamard phases

The combined reference circuit is a hierarchical program over fully specified elementary components. The Leech portion is intentionally not expanded into millions of instructions by default. `a0_sector.plan()` provides each component, its wire map, inverse rule, selector control and routing. The prior Leech emission functions and explicit flag angle specify that component without a free oracle.

One extra clean bit is sufficient for the following controlled lifts:

| Base instruction | Controlled decomposition |
|---|---|
| X | one CNOT |
| CNOT | one Toffoli |
| Toffoli | three Toffolis, computing/uncomputing one conjunction |
| H | two H, three CNOT, two Ry |
| Ry | two CNOT, two Ry |

For H use H=Ry(pi/2)Z, retaining the relative phase of controlled-Z. A channel-only control assumption is not used. For each base instruction `lift_gate` gives the actual decomposition; the checker tests every computational column of these small controlled circuits, including the extra scratch bit.

The overhead outside these controlled branch circuits is 60 Toffolis, 116 CNOTs, three Ry and eighteen X: selector preparation, two computations of each branch predicate, 54 controlled swaps, setting tags and erasing the selector. The combined cost is

| Instruction | Count |
|---|---:|
| Toffoli | 103134594 |
| CNOT | 25628550 |
| H | 2206382 |
| Ry | 4804705 |
| X | 18 |
| Total | 135774249 |

The 105-wire interface consists of 10 source bits, 10 extra coordinates, 24 spinor bits, 17 shared work bits, 40 output bits, 2 selector bits, 1 branch-control bit and 1 controlled-gate scratch bit. Exactly forty wires remain as outputs; the other sixty-five end in zero on the valid domain. These counts are a sufficient unoptimized construction, not a lower bound or a practical-efficiency claim.

If the 4804705 rotation occurrences each have operator error at most zeta/4804705 and all other logical gates are exact, telescoping gives total operator error at most zeta. Angle representation, controlled decomposition, inverse reuse and finite-gate-set synthesis must all fit this worst-case budget; statistical independence is not assumed. Binary floating reference angles and the numerical checks below do not establish such a synthesis at zeta=1e-12. A Clifford+T or physical-resource budget remains absent.

The known branch amplification does not amplify the unknown-U membership experiment, relax its rejection threshold, or reduce its previously reported statistical trial requirement. All claims C01-C21 retain their previous scope.

## 8. Verification, reproducibility and limits

```sh
python circuits/jordan_aaa.py
python circuits/jordan_aaa.py --emit
python circuits/a0_sector.py
python circuits/a0_sector.py --plan
OPENBLAS_NUM_THREADS=1 python checks/verify_a0_sector.py
OPENBLAS_NUM_THREADS=1 python -O checks/verify_a0_sector.py
OPENBLAS_NUM_THREADS=1 python -OO checks/verify_a0_sector.py
```

The new checker has **81 labeled checks**. It verifies every one of the 1024 ambient basis-change columns and every membership-predicate input. It checks equation (1) by actual tensor projections for n=2,3,4,5,24, and checks the full-operator eigenvector identity for all 299 valid A0 basis inputs at n=24. It sparsely simulates the **complete 16957-instruction, 33-wire Jordan circuit on three inputs**, including a complex superposition, and its inverse on that superposition. This is not full-circuit simulation on every A0 input.

The checker also tests the unamplified amplitudes and the omitted-phase counterexample, exact controlled primitive matrices, injective wire maps, branch predicate truth tables, every routed bit, selector amplitudes and coherent selector erasure. The combination proof remains analytic; the full 105-wire, 135-million-instruction circuit is **not simulated**. Existing XXA/QQA evidence is inherited with its original limitations rather than upgraded by the composition.

Largest dense matrix: 299 by 299 for expected Jordan output coefficients on sampled inputs. Largest coefficient tensor: 24 by 24 by 24 by 24 (331776 entries). No 196883-dimensional multiplication tensor is formed. Sparse simulation enforces a one-million-entry support ceiling and accumulated pruning norm below 1e-11; comparison tolerance is 1e-10. These are small structured checks, not formal proof or 1e-12 precision certification.

Normal, -O and -OO outputs agree byte-for-byte locally. The earlier 51-check Leech report also replays byte-identically from the mounted checkpoint, whose dependency hashes match the pinned repository manifest. Network cloning was attempted and failed in this runtime. The read-only GitHub workflow therefore separately executes the unchanged root verifier on the exact baseline and candidate; a replay of a mounted seed is not substituted for live-main verification. Its strict versus bounded-portability outcomes remain distinct. No old scientific report, root verifier or portability tolerance is changed.

All earlier notes 01-08, prior audits, existing circuits/checkers/results, provenance, import-era STATUS.md and original MIT license are preserved. Current README, STATUS_CURRENT, work order, workflow and snapshot manifest are intentionally updated. No manuscript, release or outreach is performed.

## 9. What this checkpoint closes and what follows

This closes the three-branch **A0-sector** access assignment in the declared tagged ideal-angle model. It leaves all X and Q input sectors of full W uncompiled. The restricted sector is not Monster invariant, does not prepare the full sigma=P/d, and does not implement the full P measurement. The original test's operational assumptions remain unfulfilled as a complete device proposal.

The next bounded priority is a theorem-level precursor comparison for the repaired fixed-target normalizer claim C11, rather than indefinitely extending the circuit catalogue. The criterion is whether existing results already give the same prescribed finite image, norm, averaged-error assumptions, dimension constraint and conclusion. A circuit construction does not establish publication novelty of the rigidity theorem. The remaining full-W blocks are a separate access obligation, not an automatic next claim of practical relevance.

The Jordan product, Bell contraction, projectors, exact known-success amplification and controlled-gate decompositions are existing mathematical and quantum techniques. This note makes a concrete specialization and prices its interfaces. No new general amplification or quantum-advantage theorem is claimed.

## Primary sources and read depth

[S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, section 10.1, equations (10.1.3), (10.1.4), (10.1.6). https://arxiv.org/pdf/2002.10921v5

[BHMT] G. Brassard, P. Hoyer, M. Mosca, A. Tapp, *Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055v1, section 2.1 and Theorem 4. https://arxiv.org/pdf/quant-ph/0005055

The indicated parsed source formulas were read again in this continuation. BHMT printed page 11 was visually inspected successfully. Seysen screenshot requests for printed pages 33-34 returned service errors; no successful visual inspection of those pages is claimed. The all-input operator derivation above and the explicit phase-checked circuits are supplied independently of those rendering failures. No downloaded paper is bundled. Imported source conventions and notes 07-08 remain mathematical dependencies requiring specialist scrutiny.
