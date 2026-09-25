# Weight three cannot be closed: a weight-five interaction is unavoidable

**Date:** 26 September 2026. **Live base:** `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
**Branch:** `research/odd-channel-nonclosure`. Pending PRs12–17 were inspected. This additive result does not merge or rewrite any of them.

## 1. The result in physical terms

In the declared extremal holomorphic class, the weight-three primary fields cannot supply a commutator-closed system of actions on the first primary level. Some pair necessarily produces a nonzero component carried by weight-five primaries:

\[
\boxed{\text{There exist }u,v\in P_3\text{ with }\pi_5(u_{(0)}v)\ne0.}
\]

The stronger algebraic statement proved first is that the positive eigenspace of the weight-three Gram operator is **not a Lie subalgebra of the skew matrices**. It follows from the already derived lower OPE identities and the classical classification of compact symmetric spaces. It does not use the disputed fifth-trace coefficient or the still-unresolved operator polynomial from Note18.

Identifying the nonzero complementary component specifically with the weight-five OPE uses pending PR17's odd-mode completeness and mixed trace result. That dependency is explicit: its note was read, but its full 79-check Ward certificate was not independently rerun or audited here. The core nonclosure theorem does not depend on that new certificate.

This strengthens the earlier description of the omitted channel: it is not only a possible correction to a truncated commutator; it cannot vanish for every pair. It does not say every pair has such a coupling, that pairs from P3 span all P5, or that a positive universal lower bound on its size has been proved. It also does not prove that the primary-projected bracket violates Jacobi: nonclosure in a matrix algebra alone does not imply that stronger statement.

The conclusion is a derived consequence of the current constraints, not an additional selection axiom or a classification of the original weight-two interaction tensor. The Monster has not yet been uniquely selected. The geometry used below is an auxiliary algebraic construction from OPE coefficients, not a claim that the CFT's spacetime has 196883 dimensions or is a symmetric space.

## 2. Inputs with no assumed Monster action

Retain Note12's class: nontrivial simple unitary strongly rational bosonic holomorphic chiral CFTs, V1=0, minimizing positive central charge. These are declared restrictions, not universal physical necessities or a demonstrated RG mechanism. The modular/design argument gives c=24 and the character J. Put V=P2, the real PCT-fixed weight-two primary space.

Let C be its real symmetric three-point tensor and L_a b=mu(a,b) its primary-projected multiplication. The only algebraic inputs to the core theorem are

\[
\dim V=d=196883,\qquad \operatorname{tr}L_a=0,\qquad
\operatorname{tr}(L_aL_b)=\kappa\langle a,b\rangle,\quad\kappa=13858/3,
\]

and, on the antisymmetric square,

\[
F(X)=\sum_iL_iXL_i,\qquad
R:=F_-+\gamma I=p\Pi,\quad\gamma=1/3,\quad p=282,
\tag{1}
\]

where Pi is an orthogonal projector. Note12 derives (1) from the fourth-order trace identity, using Hoehn's explicit conformal-design replacement of Matsuo's large-automorphism assumption. No Monster character table or irreducible-representation label enters these inputs. The third/fifth numerical traces and the corrected mixed-action law are unnecessary for the nonclosure proof.

Identify a wedge b with the skew matrix ab^T-ba^T and use the positive metric

\[
\langle X,Y\rangle_-=-\tfrac12\operatorname{tr}(XY).
\]

Thus e_i wedge e_j for i<j is orthonormal. Let h=im Pi, regarded as a subspace of so(V). Note13 identifies this with the zero-mode image M(P3), where M_w=w_(2)|P2, and gives rank Pi=21296876. The argument below can instead obtain the rank from its Ricci trace.

## 3. The interaction Gram is an algebraic curvature operator

Full symmetry of C gives, directly in indices,

\[
F_-(a\wedge b)=[L_a,L_b].
\]

Consequently

\[
R(a,b):=R(a\wedge b)=[L_a,L_b]+\gamma(a\wedge b).
\tag{2}
\]

This has pair symmetry, since F_- is self-adjoint, and the first Bianchi identity

\[
R(a,b)c+R(b,c)a+R(c,a)b=0.
\tag{3}
\]

Indeed the commutator part cancels by commutativity of mu, and the constant-curvature wedge term cancels separately. No associativity or Jacobi identity is assumed for mu.

With the convention

\[
\operatorname{Ric}_R(a,b)=\sum_i\langle R(a\wedge e_i),b\wedge e_i\rangle_-,
\]

we obtain

\[
\operatorname{Ric}_R(a,b)=\left[\gamma(d-1)-\kappa\right]\langle a,b\rangle
=61008\langle a,b\rangle.
\tag{4}
\]

For completeness, the contraction before tracelessness is

\[
\operatorname{Ric}_F(a,b)
=\langle\mu(a,b),\sum_i\mu(e_i,e_i)\rangle
-\operatorname{tr}(L_aL_b).
\]

The sum in the first term is zero because all L_a are trace-free. The scalar curvature identity is

\[
\operatorname{tr}\operatorname{Ric}_R=2\operatorname{Tr}_{\wedge^2 V}R,
\]

so the independently recorded rank obeys

\[
61008\cdot196883=2\cdot282\cdot21296876.
\tag{5}
\]

The word curvature here describes the tensor symmetries and contractions of (2), not a new physical background metric.

## 4. If the image were closed, it would produce a compact symmetric pair

Assume, for contradiction, [h,h] is contained in h. The trace metric on so(V) is ad-invariant. Therefore ad_A for A in h preserves both h and its orthogonal complement, and the projection Pi, hence R, is h-equivariant.

Construct the vector space g=h direct sum V with brackets

\[
[A,B]=AB-BA,\qquad [A,u]=Au,\qquad [u,v]=-R(u\wedge v).
\tag{6}
\]

The three types of Jacobi identity are precisely the representation property, equivariance of R, and the Bianchi identity (3), together with Jacobi on h. Thus (6) is a Lie algebra. Its metric

\[
\langle(A,u),(B,v)\rangle_g=\frac1p\langle A,B\rangle_-+\langle u,v\rangle
\tag{7}
\]

is positive and invariant. The minus sign in (6) is needed: <[u,v],A>_g=-<u wedge v,A>_- equals <u,[v,A]>.

The involution (A,u) -> (A,-u) makes this a compact symmetric pair. It is effective because h consists of actual matrices acting on V, and [V,V]=h since R maps onto h. There is no center: its h component would act trivially on V, while a central vector in V has R(u wedge v)=0 for every v, contradicting positive Ricci (4). The center is preserved by the involution, so treating its two components separately is legitimate. Thus g is compact semisimple and has no flat symmetric factor.

This is the standard curvature-to-symmetric-Lie-algebra construction, with its Jacobi and metric checks supplied here. The same construction appears in [BG, section4]. We use classical compact symmetric-pair decomposition and Cartan's classification, not a new classification theorem.

Decompose into irreducible symmetric factors V_j with effective isotropy h_j. The curvature operator on each factor still has nonzero eigenvalue p=282, and its Ricci scalar is still61008. Mixed planes have zero curvature. Applying (5) on each factor gives

\[
\boxed{\frac{\dim h_j}{\dim V_j}=\frac{61008}{2\cdot282}=\frac{5084}{47},\qquad
0<\dim V_j\le196883.}\tag{8}
\]

This step does not assume that the original h action or the curvature tensor is irreducible. Each possible factor must separately meet (8).

## 5. Exact exclusion of every symmetric-space possibility

Cartan's classification consists of the seven classical families, the group-type family, and twelve exceptional irreducible compact spaces, up to covers and the usual small-rank coincidences. We use the family inventory reproduced in [KOT, section5, Theorems5.4 and5.8]; no claim to have independently rederived Cartan's classification is made.

Four classical families have effective isotropy-to-tangent ratio at most two:

| Family | Tangent dimension m | Isotropy dimension h | Ratio |
|---|---:|---:|---:|
| AI, SU(n)/SO(n) | (n-1)(n+2)/2 | n(n-1)/2 | n/(n+2) |
| AII, SU(2n)/Sp(n) | (n-1)(2n+1) | n(2n+1) | n/(n-1), n>=2 |
| CI, Sp(n)/U(n) | n(n+1) | n^2 | n/(n+1) |
| DIII, SO(2n)/U(n) | n(n-1) | n^2 | n/(n-1), n>=2 |

Small-rank presentations with ineffective isotropy can only reduce the effective ratio. Group type K x K / diagonal K has ratio one. Each exceptional case has ratio at most9/4; the full twelve dimension pairs are retained in the exact report. None reaches5084/47>108.

The remaining three Grassmann families, with positive integers r<=q, have

| Family | m | h |
|---|---:|---:|
| BDI | rq | [r(r-1)+q(q-1)]/2 |
| AIII | 2rq | r^2+q^2-1 |
| CII | 4rq | r(2r+1)+q(2q+1) |

For AIII the **effective** isotropy is S(U(r) x U(q)). The presentation U(r+q)/(U(r) x U(q)) has a common ineffective central circle; subtracting that circle is required when computing the isotropy dimension. Using r^2+q^2 without the minus one would be incorrect.

The bound h/m>108 implies q/r>215 for BDI and AIII, and q/r>214 for CII. Together with m<=196883, these imply

\[
r\le30\text{ (BDI)},\qquad r\le21\text{ (AIII)},\qquad r\le15\text{ (CII)}.
\]

For those ranges, equation(8) is respectively

\[
47q^2-(47+10168r)q+47r(r-1)=0,
\]

\[
47q^2-10168rq+47(r^2-1)=0,
\]

\[
94q^2+(47-20336r)q+47(2r^2+r)=0.
\tag{9}
\]

The report provides all **66 exact discriminants**, their integer square-root floors, and all rational roots when the discriminant is square. Only two discriminants are squares: r=1 in BDI and AIII. Their nonzero roots are10215/47 and10168/47 respectively, not integers; their other root is zero and inadmissible. All other discriminants are nonsquares. Hence no factor exists.

This is a finite exhaustive arithmetic certificate after an external classification theorem, not an optimization over a sampled set of Lie groups. Equations(6)–(9) contradict the assumption that h is closed. We have proved

\[
\boxed{[\operatorname{im}\Pi,\operatorname{im}\Pi]\not\subseteq\operatorname{im}\Pi.}\tag{10}
\]

## 6. Why the missing component is a genuine weight-five interaction

Pending PR17, head `fde92a04964def3a12c5a8cc75362c4fced96c73`, gives the orthogonal zero-mode decomposition

\[
\mathfrak{so}(P_2)=M(P_3)\perp M(P_5),
\quad\langle M_u,M_v\rangle_-=282\langle u,v\rangle\ (u,v\in P_3),
\]

with norm coefficient two on M(P5). It also gives

\[
[M_u,M_v]=\frac6{47}M_{\beta_3(u,v)}+M_{\gamma_5(u,v)},
\quad\beta_3(u,v)=\pi_3(u_{(2)}v),\quad\gamma_5(u,v)=\pi_5(u_{(0)}v).
\tag{11}
\]

These are its design-based pair/mixed trace results, not consequences of Cartan classification. The core theorem(10) uses only the earlier Gram/curvature data; applying(11) translates it into the opening nonvanishing statement. Since M(P3)=im Pi and M on P5 is injective, nonclosure forces gamma5 to be nonzero for some inputs in **every** admissible candidate.

This does not identify every skew matrix with a physical symmetry. The matrices act on a degenerate energy level, and preserving the full OPE is an additional requirement. It introduces no weight-one currents and makes no statement about the distinct infinite-dimensional Monster Lie algebra.

## 7. An explicit check in the known theory

There is a separate, direct normalization witness inside the even-Heisenberg part of the known moonshine theory. It is not used in the universal nonclosure proof.

Choose unit skew matrices A=E01-E10 and B=E12-E21 on three of the24 oscillator directions. Their commutator C has unit half-Frobenius norm. The primary fields

\[
w_A=\tfrac12\sum_{ij}A_{ij}h_i(-2)h_j(-1)1
\]

have this same norm, and the earlier direct mode calculation gives beta3(w_A,w_B)=(5/2)w_C. Their zero-mode actions on V2 are ad_A on the symmetric oscillator block, zero on the diagonal Leech block, and A/4 on the4096-fold vector block. These actions follow by taking commutators of the explicit multiplication blocks [S] in the inherited physical normalization.

The squared norm of their full matrix commutator is

\[
26+4096/16^2=42.
\]

Its P3 component is (15/47)M_wC, of squared norm1350/47. The orthogonal P5 component therefore has squared norm624/47. Since M on P5 has squared norm multiplier two,

\[
\boxed{\|\gamma_5(w_A,w_B)\|^2=312/47>0.}\tag{12}
\]

The same624/47 is obtained by separately squaring the two block differences, not only by subtracting totals. No giant matrix is constructed. The factor26 is the Sym^2 real trace index n+2 at n=24; the checker also evaluates that index directly at n=3. Equation(12) is a witness in the known example, not a uniform lower bound for every admissible theory or every pair.

## 8. What this settles, and what remains open

The first generated odd level cannot be an autonomous matrix-commutator sector. The next odd OPE channel is forced, not optional. This gives a structural explanation for retaining the extra interaction identified by the other workspace.

It does not prove nonzero projected Jacobi defect, onto generation of P5 from P3 pairs, or a minimal nonzero coupling size. It also does not identify the automorphism group of the original cubic. A physically forced interaction pattern can be common to all admissible candidates without deciding whether the candidate itself is unique.

The earlier operator condition

\[
\Pi[9\mathcal Q_x+24336\operatorname{ad}_x-2704\operatorname{ad}_{Gx}]\Pi=0
\]

still has no implication/independence certificate. A bounded diagram-contraction attempt in this continuation reduced parts of its expansion using lower trace and reconstructed fifth-order relations, but did not eliminate the full residual. A nonzero remainder in a chosen rewrite system is not a countermodel or a proof of independence. This attempt is not used in(10) and is not included as finished verification code.

The present theorem is instead a classification-based corollary of the existing physical data. Its particular formulation has not received exhaustive priority review. No new general curvature theorem, independent selection axiom, complete VOA reconstruction, or proof of Monster uniqueness is claimed.

## 9. Evidence and source depth

The new checker emits135 exact integer/fraction checks and the entire66-case discriminant certificate. It checks curvature/Bianchi/Ricci contractions on arbitrary small symmetric cubics; the compact symmetric-pair construction, all Jacobi basis triples and positive invariant metric on a sphere and a product of spheres; and a negative control showing Bianchi plus positive Einstein projector does not itself imply Lie closure. It checks the known-example leakage normalization by two routes.

Largest square matrix15x15; largest explicitly tested Lie-algebra vector dimension12. The exceptional dimension inventory and Cartan exhaustion are external mathematical inputs; scalar checks do not prove that classification. No extremal cubic, full Monster representation or complete CFT is constructed. The pending PR17 Ward reconstruction retains its independent proof-audit obligation. All new reports agree under normal Python, -O and -OO.

The source inventory was read in parsed primary text. Screenshots of KOT's classification tables failed in the browser; they are not claimed visually inspected. Hoehn printed page12 and Matsuo printed page16 were successfully visually inspected. Cartan's original1926 bibliographic record was located, but its PDF retrieval failed and its original proof was not read. BG's section4 was read in author-posted primary text; its arXiv PDF retrieval failed. These are declared source-depth limits, not proofs replaced by numerical checks.

The patch is additive from live main and preserves all its files, existing ledgers, license, archives, root verifier and portability policy. It leaves all other pending PRs intact. A dedicated read-only workflow checks actual baseline/candidate root replay, reports recognized strict-byte failures separately from bounded portability, and verifies the new report in three modes. Local Git network access failed; local new tests are not advertised as local historical main replay. No manuscript, release, outreach or physical implementation is performed.

### Sources

[H] G. Hoehn, *Conformal Designs based on Vertex Operator Algebras*, arXiv:math/0701626v1, Theorem3.1 and the end-of-section2 design-for-symmetry replacement. https://arxiv.org/abs/math/0701626

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1, traces through order four. The disputed fifth-order numerical coefficient is not a premise here. https://arxiv.org/abs/math/0007169

[KOT] S. Kaji, A. Ohsita, S. Theriault, *Mod p decompositions of the loop spaces of compact symmetric spaces*, Algebraic & Geometric Topology15(2015),1771–1811; arXiv:1409.7958. Classification context in the introduction; seven classical families in section5.1/Theorem5.4, twelve exceptional families in section5.2/Theorem5.8. Only the homogeneous-space inventory is used, not their p-local homotopy hypotheses or conclusions. Standard matrix-group dimensions are computed independently. The AIII effective-center conversion is explicit above. https://arxiv.org/abs/1409.7958

[BG] I. Biswas, N. L. Gammelgaard, *Vassiliev Invariants from Symmetric Spaces*, arXiv:1410.6440; J. Knot Theory Ramifications25(10)(2016),1650055, section4. Standard reconstruction of a symmetric triple from an equivariant curvature tensor. The proof needed here is supplied in section4 of this note. https://arxiv.org/abs/1410.6440

[Ca] E. Cartan, *Sur une classe remarquable d'espaces de Riemann*, Bull. Soc. Math. France54(1926),214–264, DOI10.24033/bsmf.1105. Original classification proof not independently audited. https://numdam.org/articles/10.24033/bsmf.1105/

[S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, sections7.4 and10.1; block normalization as in the prior audit and Note18. Used only for the known-example control, not the universal theorem. https://arxiv.org/abs/2002.10921

The separately supplied local `19_interaction_indivisibility.md` is preserved, and is distinct from PR17's `19_odd_mode_completeness.md`. The new filename20 avoids that numbering collision. No downloaded papers or fonts are bundled.
