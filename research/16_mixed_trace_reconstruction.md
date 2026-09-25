# A universal mixed trace reconstructed without the disputed fifth-trace formula

**Date:** 25 September 2026. **Base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/mixed-trace-reconstruction`.

PR12 (`research/mixed-action`) proposes a normalization-dependent quintic restriction that fails an exact known-example audit. PR13 contains a separate normalization audit. This additive continuation preserves both branches and all main-branch evidence. It supplies an independent universal mixed-trace derivation; it neither imports PR12's false condition nor treats one example as proof of a universal correction. Number 15 remains reserved for the pending audit/mixed-action records.

## 1. Result and scientific consequence

In the physical class of Note12, let e be a real Virasoro primary of weight two and w,v real primaries of weight three. Normalize the positive Hermitian form by ||1||=1, use PCT-fixed real states, and write Y(a,z)=sum a_(n) z^(-n-1). Then

$$\boxed{\operatorname{Tr}_{V_2}\big(e_{(1)}w_{(2)}v_{(2)}\big)
=-104\langle w,e_{(1)}v\rangle.}\tag{1}$$

This is derived from the conformal-design trace rule and Virasoro/mode identities through weight eight. The disputed fifth-order multiplication-trace formula is not an input. No Monster group action, character decomposition, known multiplication table, or full matrix is used.

For Note13's onto map B:wedge^2 P2 -> P3, put

$$G=B^\dagger B=282\Pi=F_-+I/3,\qquad
\mathcal D_e(X)=L_eX+XL_e.$$

The corrected mixed coupling follows directly:

$$\boxed{T_e(x,y)=\langle Bx,e_{(1)}By\rangle
=\frac1{104}\langle x,G\mathcal D_eG y\rangle.}\tag{2}$$

Hence its null-state relations are automatic: G kills every input representing the zero physical state, on either side. The additional condition proposed in PR12 is not a selection condition for the actual theory. The normalized primary compression is

$$J_B^\dagger(\pi_3 e_{(1)}\pi_3)J_B
=\frac{141}{52}\Pi\mathcal D_e\Pi,
\qquad J_B=B/\sqrt{282}.\tag{3}$$

No assertion is made that e_(1) preserves P3 before compression. These are dimensionless interaction coefficients, not transition rates, a physical perturbation protocol, or gate-access costs.

Normalized alternation of (1) also fixes the disputed alternating component:

$$\boxed{\operatorname{Alt}_5\operatorname{Tr}(R_aR_bR_cR_dR_e)
=26\Omega(a,b,c,d,e),}\tag{4}$$

where Alt_5 includes 1/120 and Omega is defined by the original five-mode word in section 5. This proves the convention-compatible value for every admissible theory, not just the witness. It does not reconstruct every non-alternating term of the full fifth-trace formula or determine the intended convention of a version of record not inspected.

The scientific outcome is a universal low-energy coupling law and removal of a spurious restriction. It is not Monster uniqueness, a new physical selection principle, comprehensive priority clearance, independent expert review, or formal verification.

## 2. Inputs and signs

The admissible theories are the nontrivial simple unitary strongly rational bosonic holomorphic chiral theories with V1=0 and minimum positive central charge, as in Note12. That restricted optimization gives c=24, Z=J, and

$$V_2=\mathbb R\omega\perp P_2,\quad \|\omega\|^2=12,\quad \dim P_2=196883.$$

Holomorphicity/minimization are declared assumptions, not universal laws or a demonstrated dynamical selection mechanism. Höhn's prior extremal conformal-design theorem [H] implies, for a homogeneous a of weight at most eleven,

$$\operatorname{Tr}_{V_2}o(a)=\operatorname{Tr}_{V_2}o(\pi_{\rm vac}a),
\qquad o(a)=a_{(\mathrm{wt}(a)-1)}.\tag{5}$$

Only weights at most eight are required below. The design theorem is an external mathematical input, not proved by our code.

For a real primary of weight h, the invariant Hermitian/PCT convention [DL] gives

$$a_{(n)}^\dagger=(-1)^h a_{(2h-2-n)},\qquad L_m^\dagger=L_{-m}.$$

Thus w_(2),v_(2) are skew adjoint, while e_(1) is self-adjoint. The minus sign in (1) is essential. Calculations can be made on the real subspace and extended sesquilinearly; no assumption that an odd-spin real state is a pointwise Hermitian field is inserted.

## 3. Replace the product of zero modes by a finite state sum

For homogeneous a,b of weights h,k define the finite Zhu-type star product

$$a\star b=\sum_{i=0}^h\binom hi a_{(i-1)}b.$$

Here it is only an explicit sum of modes, not an invocation of a lowest-module theorem on V2. Summing the iterate identity [M, section1] gives the exact operator identity

$$o(a\star b)=o(a)o(b)
+\sum_{j\ge1}a_{(h-1-j)}b_{(k-1+j)}
+\sum_{j\ge0}b_{(k-2-j)}a_{(h+j)}.\tag{6}$$

On V2, because V1=0, only the potential vacuum-return terms survive besides o(a)o(b): a_(h-3)b_(k+1) and b_(k-3)a_(h+1). If b is primary of weight three, both vanish. In fact b_(4)V2=0, since b_(4)^dagger=-b_(0) and b_(0)1=0; the other term contains b_(0)1 as well. Consequently o(a star b)=o(a)o(b) on V2 for arbitrary homogeneous a when the right-hand b is weight-three primary.

Apply this twice, first to e,w and then to each homogeneous part with v. Therefore

$$\operatorname{Tr}_{V_2}e_{(1)}w_{(2)}v_{(2)}
=\operatorname{Tr}_{V_2}o(\Xi),$$

$$\Xi=(e\star w)\star v
=\sum_{i=0}^{2}\sum_{j=0}^{5-i}
\binom2i\binom{5-i}j(e_{(i-1)}w)_{(j-1)}v.\tag{7}$$

The summands have ordinary weights N=8-i-j, from three through eight. Equation (5) now reduces the entire trace to the vacuum Virasoro submodule. This bypasses the disputed fifth-trace coefficients completely.

## 4. A finite exact certificate for coefficient -104

Let t=<w,e_(1)v>. The following pairings are formal coefficients multiplying t, not expressions obtained by division by t. Thus the proof includes t=0.

At each weight N, use the vacuum basis

$$u_\lambda=L_{-\lambda_1}\cdots L_{-\lambda_l}1,
\quad\lambda_1\ge\cdots\ge\lambda_l\ge2,\quad\sum\lambda_i=N.$$

Let M_N be its Gram matrix, b_N the pairing of Xi_N with this basis (coefficient of t), and l_N the trace on V2 of its zero modes. The contribution is

$$l_N^T M_N^{-1} b_N\;t.\tag{8}$$

All three vectors/matrices follow from the Virasoro commutator, the primary Ward identity, and normal ordering. The largest system is 7 by 7. Their complete rational entries, including M_N, b_N, its solved projection, and l_N, are emitted in `results/mixed_trace_reconstruction.json`.

For independently reproducible conventions, the vacuum three-point initial coefficients are

$$\langle1,e_{(p)}w_{(q)}v\rangle=-(p-2)t
\quad(p\ge3,\ p+q=6),$$

$$\langle1,w_{(p)}e_{(q)}v\rangle=-(p-4)t
\quad(p\ge5,\ p+q=6),$$

and zero otherwise. Commute positive Virasoro modes using

$$[L_m,a_{(p)}]=((h_a-1)(m+1)-p)a_{(m+p)}.$$

For the composite terms use the full iterate formula

$$(e_{(r)}w)_{(s)}v
=\sum_{k\ge0}(-1)^k\binom rk
\big[e_{(r-k)}w_{(s+k)}v-(-1)^r w_{(r+s-k)}e_{(k)}v\big].$$

Degree bounds truncate its first part at k<=5-s and its second at k<=4. Generalized binomial coefficients include r=-1. This supplies every b_N, including all descendant terms, without fitting a trace to a desired answer.

To obtain l_N, evaluate the vacuum descendant zero mode on omega and on one abstract weight-two Virasoro highest-weight vector. Its latter scalar is repeated 196883 times. Normal ordering can be implemented by

$$\begin{aligned}
(L_{-m}u)_{(n)}={}&\sum_{j\ge0}\binom{j+m-2}{m-2}
L_{-j-m}u_{(n+j)}\\
&+\sum_{j\ge m-2}(-1)^{m-2}\binom j{m-2}
 u_{(n-1-j)}L_{j-m+1}.
\end{aligned}$$

The code evaluates these finite sums on the two module states, rather than importing a multiplication trace table.

| Weight N | Vacuum basis size | Contribution in (8), divided formally by t |
|---|---:|---:|
| 3 | 1 | 164070 |
| 4 | 2 | -1521466 |
| 5 | 2 | 4859280 |
| 6 | 4 | -7135443 |
| 7 | 4 | 4958560 |
| 8 | 7 | -1325105 |
| **Sum** | | **-104** |

The separate omega-state contributions cancel to zero. The summed coefficient per weight-two primary is -104/196883. The code checks each exact linear system, every positive leading Gram minor, each entry of this table, and both cancellations. Since equations (5)-(8) reduce the general trace to this exhaustive finite calculation, the table is an explicit rational certificate for (1), not a sample of theories or tensors.

An independent two-primary calculation by the same method gives

$$\operatorname{Tr}_{V_2}w_{(2)}v_{(2)}=-564\langle w,v\rangle.$$

It provides a sign and normalization check. Replacing primary e by omega does not satisfy (1): the two sides would be -1128<w,v> and -312<w,v>. The assumption that e is primary is necessary.

## 5. Recover the physical mixed operator and the five-form coefficient

For real a,b in P2, [a_(1),b_(1)]=B(a,b)_(2). In the full weight-two algebra with normalized stress direction, this commutator kills the stress direction and on P2 corresponds to the skew matrix sqrt(2)G(a wedge b). This is a direct contraction of the symmetric cubic and its stress component, as in Note13.

For x=a wedge b and y=c wedge d, the symmetric-matrix/skew-matrix trace identity gives

$$\operatorname{Tr}_{V_2}R_e[R_a,R_b][R_c,R_d]
=-\langle x,G\mathcal D_eGy\rangle.$$

Apply (1) with w=Bx and v=By. Its other expression is -104 T_e(x,y), proving (2). Dividing by the two normalization factors sqrt(282) yields (3). No previous five-form/tree decomposition is needed for this implication.

For the normalized five-form use exactly

$$\Omega(a,b,c,d,e)1=\operatorname{Alt}_5
[a_{(3)}b_{(2)}c_{(1)}d_{(0)}e],\quad
\operatorname{Alt}_5=\frac1{120}\sum_\sigma\operatorname{sgn}(\sigma).$$

Adjoints and the derivative subtraction defining B give Omega=-Alt_5 T_e(a,b;c,d). Derivative/stress-excursion terms vanish under complete alternation because they have a symmetric pair. Meanwhile cyclicity and expansion of the two commutators give

$$\operatorname{Alt}_5\operatorname{Tr}R_e[R_a,R_b][R_c,R_d]
=4\operatorname{Alt}_5\operatorname{Tr}R_aR_bR_cR_dR_e.$$

Equations (1)-(2) therefore imply (4). The checker verifies the factor four as an exact identity of formal noncommutative trace words, including 1/120, not on one numerical matrix example.

The audit's known-example ratio26 is thus supported by a distinct universal derivation. The literal use of52 with this same Omega definition cannot support PR12's proposed restriction. We do not claim to have inspected the published version of record or resolved its intended convention. Nothing here proves every other term in a full non-alternating fifth-trace formula.

## 6. What has been learned about physical selection

The first-level interaction algebra fixes this compressed interaction with the second primary level. Different pair superpositions representing one state necessarily give the same corrected mixed coupling. The proposed extra null-relation condition disappears because the correct expression has G on both sides.

This removes an invalid route to a new restriction; it does not select the full Monster, prove a competing physical CFT exists, or establish that all higher consistency conditions are redundant. The unknown weight-two product remains unclassified. Standard conformal-design and Virasoro machinery, not an independently discovered law of nature, supplies the present rigidity of couplings.

A concrete next boundary can be stated without starting another moment catalogue. Products of four weight-three zero modes can be reduced by (6) to a nested star product whose highest ordinary weight is twelve. Only its top term

$$((w_{(-1)}v)_{(-1)}u)_{(-1)}x$$

has weight twelve; all other terms have lower weight. The existing 11-design rule does not determine the nonvacuum trace of that top component. Note12 already identifies weight twelve as the first modularly allowed primary one-point response, proportional to Delta. This identifies a specific place where the present reduction needs additional data. It does not prove that the new response is free, nonzero, or independent of lower algebraic identities. Deriving its precise projection and shared-state constraints is a bounded next question. No Monster representation labels may be used to close it.

## 7. Reproduction, scopes and integration

```
python checks/verify_mixed_trace_reconstruction.py
python -O checks/verify_mixed_trace_reconstruction.py
python -OO checks/verify_mixed_trace_reconstruction.py
```

The checker has **65 labelled checks**, all exact integers/fractions. It emits the complete rational certificate rather than only -104. An independent three-boson oscillator control checks 280 Ward words, 42 composite pairings, 91 Gram entries and 42 descendant zero-mode actions. Its private intermediate cutoff is fourteen. The original Note13 helper is hash-checked and never modified; these c=3 controls check universal mode algebra, not the exceptional c=24 trace theorem. No full extremal OPE tensor, Monster character table or matrix is built. Maximum square Gram dimension is seven.

Normal/-O/-OO outputs agree locally. These checks make the finite arithmetic reproducible; they do not formally verify the conformal-design theorem or substitute for specialist review of the reduction. No comprehensive novelty clearance is claimed.

Runtime git access failed. A new additive PR is used, without merging or rewriting PR12 or PR13. Earlier main-branch files and snapshot manifest remain unchanged; a separate additive manifest covers this continuation's files. A dedicated read-only workflow verifies that manifest and runs the unchanged historical strict verifier and portability inspector on the pinned baseline and candidate, retaining their separate outcomes. Actual CI outcomes belong in the integration report, not an assumption of universal byte portability. No manuscript, release, outreach, old-evidence regeneration or tolerance change is authorized or performed.

## Sources and read depth

[H] G. Höhn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1. The extremal conformal-design theorem, definition of trace agreement, and end-of-section2 replacement of symmetry assumptions are the source inputs. Printed page12 was visually inspected. The theorem is not independently reproved here.
https://arxiv.org/abs/math/0701626

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Section1 mode/Virasoro conventions and equation2.2 define the comparison convention. The disputed fifth-order coefficient is NOT used to prove (1). Parsed passages were checked; a fresh printed-page4 screenshot failed in the browser service. No published-version correction is asserted without access to that version.
https://arxiv.org/abs/math/0007169

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1, Definitions2.1-2.2. Printed page3 was visually inspected. This supplies the positive Hermitian/PCT convention, including the odd-primary sign.
https://arxiv.org/abs/1308.2361

No downloaded papers or fonts are bundled. The current physical-selection assumptions and the prior source-depth limits remain in force.
