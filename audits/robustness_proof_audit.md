# Robustness proof audit: completion of the eight listed obligations

**Date:** 23 September 2026.

**Audited base:** [`a450e022781c4109609ff8f274787942c513df1a`](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/tree/a450e022781c4109609ff8f274787942c513df1a), the merge of [PR #1](https://github.com/GoGoKo699/Monster-Correlation-Rigidity/pull/1).

**Branch:** `audit/robustness-proof`. No open PR or existing branch with this name was found before starting. The owner explicitly authorized the preceding merge and continuation. Historical research notes, original data, checkers, reports, archives, and LICENSE remain unchanged.

## Verdict and boundaries

**The eight obligations in [CURRENT.md](../work_orders/CURRENT.md) have now been reconstructed, with no blocking gap found in the Monster specialization after the explicit repairs recorded here and in the [VOA audit](voa_extrema_audit.md).** This is an assistant proof audit with separate reconstructions of the spectral, group, and bootstrap arguments. It is not independent human/expert review or formal verification.

Two new issues need a narrow repair:

- The general normalizer lemma omits the domains of $\beta,t,L$. Its proof requires $0\le\beta<1$, $t>0$ and $L\in\mathbb Z_{\ge1}$; we also restate $0\le q<1$, already implicit in its operator-norm hypothesis. The displayed scalar inequalities alone permit values for which its intermediate walk claim is false. The Monster choices satisfy the repaired conditions.
- The recorded source range for the character-table centralizers omits the last source line. All 194 stored values nevertheless match the pinned source. Correct the locator, not the data.

The prior audit's zero-error corrections remain necessary: rounded error bounds must use $\le$ at zero. In particular the literal strict C12 summary is false at the identity. No change to the exact coefficient, sufficient thresholds, or recorded scientific values is indicated. The earlier HS25 complementary-norm typo is also retained as an external-source erratum.

This report completes the **eight specified proof obligations**, including their channel and source inputs as described below. It does not assert that every ancillary claim in all five notes has received an exhaustive audit, that all foundational literature proofs were independently reproduced, or that priority and probe-access feasibility are resolved. Those remain separate work orders.

## Findings ledger

PASS denotes a reconstructed implication using the named classical inputs. ERROR denotes an explicit erroneous statement, incomplete proof specification, or inaccurate source locator. UNRESOLVED denotes an unanswered question, not an inferred counterexample.

| ID / obligation | Verdict | Target and evidence | Affected claims |
|---|---|---|---|
| R01 / 1 | PASS | Note 03 §4: full idempotent, unitary cyclic vacuum module, branch exclusions, and classification; proof and primary-source checks in [voa_extrema_audit.md](voa_extrema_audit.md), V01–V06. | C02, C07, C08, C12, C13 |
| R02 / 2 | PASS | Note 02 §§1.2,3 and note 05 §3: scalar-block subtraction, channel spectrum, and the two distinct factors of $1/d$ reconstructed in §§1–3 below from [M]. | C02–C06, C08, C09, C12, C13 |
| R03 / 3 | PASS | Note 03 §5 and note 04 §§4–6: both finite-radius bounds, compact-complement argument, and injective good-match completion; prior audit V07–V10. The global upper-deficit estimate needed by C12 does not need the critical-value gap. | C07, C08, C12, C13 |
| R04 / 4 | PASS with stated source depth | Note 05 §4: [DMPZ] §3.3 and Theorem 3.1(4) supply the four-conjugate bound. Both plus- and minus-eigenspace arguments reconstructed in §4. Zisser's original proof has not been read. | C10–C13 |
| R05 / 5 | PASS under R09 domains | Note 05 §5 step 1: deletion preserves the constant complement and gives a norm bound even for a noncentral walk. Exact-length support follows from a transition-entry bound, not from mere generation. See §5. | C11–C13 |
| R06 / 6 | PASS under R09 domains | Note 05 §5 steps 2–4: separate proofs of word independence, unique nearest elements, exact multiplication, injectivity, nonzero intertwiner, and the final averaged bound. See §5. | C11–C13 |
| R07 / 7 | PASS | Note 05 §6: source-checked character moments give the invariant cubic line; the actual cubic plus metric reconstructs the full Griess product. A general normalizer-to-group inference would be false. See §6. | C14, C12, C13; moment inputs in C07/C08 |
| R08 / 8 | PASS with prior endpoint repair | Note 05 §7 and note 02 §7: preliminary Frobenius bounds, dimensional conversion, principal logarithm, and centering all meet the local theorem hypotheses. See §7. | C03, C12, C13 |
| R09 | ERROR — omitted domains | The parameter choices preceding note 05 (5.1) need explicit domains. The exact $A_5$ witness in §5 satisfies every printed scalar condition but makes the asserted walk bound negative. It disproves that unrestricted proof step, not the intended lemma conclusion. | C11 statement; no Monster parameter change |
| R10 | ERROR — source locator | `data/monster_character_excerpt.json` says centralizers are on lines 2110–2129. At the pinned commit the array is on **2114–2130**; line 2130 contains its final ten entries. Note 03 §2 repeats the incomplete range. Stored arrays match exactly. | Provenance supporting C07/C08/C12–C14; no value changes |
| R11 | UNRESOLVED — separate work | Original Norton/Zisser proof-level comparison, comprehensive priority, efficient probe access, noisy-channel extensions, and practical implementation. Existing scalar/toy checks cannot establish these. | No novelty or implementation status upgrade |

## 1. Projected multiplication and channel spectrum

The normalization remains $d=196883$, $s^2=1/3$, $t=\omega/\sqrt{12}$, and

$$
R_a=\begin{pmatrix}0&sa^T\\sa&L_a\end{pmatrix},\qquad a\in V=t^\perp.
$$

[M], Corollary 4.1, printed p.16, provides the full-product trace identities. Multiplying the blocks rather than reusing the full coefficients gives

$$
\operatorname{Tr}(L_aL_b)=(4620-2s^2)\langle a,b\rangle
=\kappa\langle a,b\rangle,\quad\kappa=13858/3,
$$

$$
\operatorname{Tr}(L_aL_bL_c)=(900-3s^2)T(a,b,c)=899T(a,b,c).
$$

For the fourth trace, write $A,B,C$ for the three pairings of projected products in the order $(ab,ce),(ac,be),(ae,bc)$, and $p,q,r$ for the corresponding scalar pairings. The block correction is $2s^2(A+C)+s^4(p+r)$. Converting the full products in [M] to projected ones then gives

$$
\operatorname{Tr}(L_aL_bL_cL_e)
=\frac{496}{3}(A+C)-116B+\frac{965}{9}(p+r)+\frac{40}{3}q.
$$

For example the coefficient of $p$ is $166s^2+52-s^4=965/9$; that of $q$ is $-116s^2+52=40/3$. This checks the full-versus-projected distinction at the source of the channel calculation.

Put $\mathcal F(X)=\sum_iL_iXL_i$, $\mathcal E=\mathcal F/\kappa$, and $Q(X)=L_{m(X)}$ with $m(X)=\sum_{pq}X_{pq}\mu(e_p,e_q)$. The map $a\mapsto L_a$ has adjoint $m$, and $m(L_a)=\kappa a$, so $Q=\kappa\Pi_{L(V)}$. Direct indices give

$$
\mathcal F_{ab,pq}=\sum_iT_{iap}T_{iqb},\qquad
(\mathcal F^2)_{ab,pq}=\operatorname{Tr}(L_aL_pL_qL_b).
$$

Substitution yields exactly note 02's polynomial

$$
\mathcal F^2(X)=\frac{496}{3}\mathcal F(X)-116\mathcal F(X^T)
+\frac{496}{3}Q(X)+\frac{965}{9}X+\frac{40}{3}X^T
+\frac{965}{9}\operatorname{Tr}(X)I.
$$

The third trace gives $\mathcal F(L_a)=899L_a$, while $\mathcal F(I)=\kappa I$. On the remaining symmetric sector the roots are $155/3,-7/3$; on the skew sector they are $845/3,-1/3$. Self-adjointness excludes Jordan blocks. The traces on these parity sectors are $\pm d\kappa/2$, since the full superoperator trace is zero and the trace after composing with transpose is $d\kappa$. Dimension and trace therefore determine the multiplicities without assuming a decomposition into irreducible Monster modules:

| Sector | $\mathcal E$ eigenvalue | Multiplicity |
|---|---:|---:|
| Scalars | $1$ | $1$ |
| $L(V)$ | $2697/13858$ | $196883$ |
| Symmetric complement | $155/13858$ | $842609326$ |
| Symmetric complement | $-7/13858$ | $18538750076$ |
| Skew | $845/13858$ | $21296876$ |
| Skew | $-1/13858$ | $19360062527$ |

All six sectors occur. The unique singular-value-one direction and the next singular value $r_E=2697/13858$ are therefore established, not assumed from a numerical diagonalization. The two skew values also recover note 01's normalized cubic-response coefficients $108/41$ and $20790/6929$ through $3-6\lambda$.

## 2. Quantum-loss and real-structure transfers

The tensor normalization gives $W^\dagger W=I$, $P=WW^\dagger$, $\operatorname{Tr}_1P=\operatorname{Tr}_2P=I$, and $\tau=T/\sqrt{d\kappa}$. For $A=W\otimes I$ and $B=I\otimes W$, their overlap is

$$
(A^\dagger B)_{ab,pq}=\kappa^{-1}\sum_jT_{apj}T_{qjb}
=\mathcal E_{ab,pq}.
$$

For an eigenvector $v$ of $\mathcal E$ with eigenvalue $\lambda$, the parent Hamiltonian obeys $H_3Av=Av-\lambda Bv$ and $H_3Bv=Bv-\lambda Av$. If $|\lambda|<1$, this is a genuine two-dimensional block with energies $1\pm\lambda$. For the unique $\lambda=1$ vector $\Phi$, the two vectors coincide: $A\Phi=B\Phi=\tau$. The orthogonal complement of both ranges has energy two. Thus

$$
\Delta=1-r_E=11161/13858,\qquad
\Delta(I-|\tau\rangle\langle\tau|)\preceq H_3
\preceq2(I-|\tau\rangle\langle\tau|).
$$

The gap is exact because the $r_E$ sector has positive multiplicity. The pair marginal is $P/d$, so the energy of $U^{\otimes3}\tau$ is exactly $2\epsilon(U)$. This proves $\epsilon\le\ell_3\le2\epsilon/\Delta$ for every unitary without a gate-proximity assumption. It also proves the stated arbitrary-state energy/fidelity implication; the latter alone does not certify a gate.

For the real-structure reduction, define $\ell_2(U)=1-|\operatorname{Tr}(UU^T)/d|^2$. Let $C=P^{\Gamma_2}=\mathcal ES$, where $S$ is transpose under vectorization, and set $Z=U\otimes\overline U$. The minimum distance between the two parity spectra of $C$ is $g=8/13858$. Spectral blocks give

$$
\|[S,Z]\|_F\le(2/g)\|[C,Z]\|_F,
\quad\|[S,Z]\|_F^2=2d^2\ell_2(U),
\quad\|[C,Z]\|_F^2=2d\epsilon(U).
$$

The second norm identity uses covariance under local unitary conjugation and the Hilbert–Schmidt isometry of partial transpose, not positivity of partial transpose. Consequently

$$
\ell_2(U)\le\frac4{dg^2}\epsilon(U)
=\frac{48011041}{787532}\epsilon(U)=K_R\epsilon(U).
$$

After choosing the phase so that $\operatorname{Tr}(UU^T)\ge0$, write $U=X+iY$. For $a=|\operatorname{Tr}(UU^T)|/d$, $XX^T+YY^T=I$ and $2\|Y\|_F^2=d(1-a)$. The singular values of $X$ lie in $[0,1]$, so real orthogonal Procrustes gives

$$
\min_{O\in O(d)}\|U-O\|_F^2
=2d-2\|X\|_*\le d(1-a)\le d(1-a^2).
$$

An orthogonal polar factor exists even when $X$ is singular, by extending its partial isometry. This supplies the required real approximation globally. Flat marginals make each tensor-factor telescoping term have norm equal to the normalized Frobenius error. Thus the transfer to real cubic overlap in note 05 §2 item 5 is valid.

## 3. Axis errors to involution conjugation errors

The previous audit verifies the axis spectrum. More explicitly, the radial eigenvalue of $L_a$ is $46/\sqrt{141}$, with tangent eigenvalues $-1/\sqrt{141}$, $11/\sqrt{141}$ and $1/(2\sqrt{141})$. Their multiplicities are $1,96255,4371,96256$, respectively. Passing from the full algebra removes one zero-eigenvector of $R_e$, not one vector from its Miyamoto minus sector.

Define $J(A)=I-2\Pi_\nu(A)$, where $\nu=1/(2\sqrt{141})$. Then $J_a=J(L_a)$ is precisely the represented 2A involution. Its separating spectral gap is $g_*=3/(2\sqrt{141})$. For two symmetric matrices with the prescribed spectrum,

$$
\|J(A)-J(B)\|_F^2\le\frac4{g_*^2}\|A-B\|_F^2
=\frac{752}{3}\|A-B\|_F^2.
$$

To verify this globally, expand both squared norms in $\operatorname{Tr}(P_\lambda Q_\mu)\ge0$. Every nonzero indicator difference for the $\nu$-projection has $|\lambda-\mu|\ge g_*$. There is no small operator-perturbation assumption.

Let $\mathscr D=O^{\otimes3}T-T$. Contraction with $Oa$ gives

$$
\mathscr D(Oa,\cdot,\cdot)=OL_aO^T-L_{Oa}.
$$

The tight frame supplies the first factor $1/d$ and the matrix norm convention supplies the second:

$$
\mathbb E_a\|OL_aO^T-L_{Oa}\|_{2,d}^2
=\frac{\|\mathscr D\|_F^2}{d^2}
=\frac\kappa d\|O^{\otimes3}\tau-\tau\|^2.
$$

Also $\|L_x-L_y\|_{2,d}^2=(\kappa/d)\|x-y\|^2$. The spectral comparison is applied to **$OL_aO^T$ and $L_{\pi(a)}$**, which have the prescribed spectrum. The intermediate $L_{Oa}$ need not have it and is used only in the triangle inequality. This distinction closes a possible misuse of the projection estimate.

Set $z^2=\mathbb E_a\|OJ_aO^T-J_{\pi(a)}\|_{2,d}^2$. Writing $\alpha=\langle T,O^{\otimes3}T\rangle/(d\kappa)$, Minkowski gives

$$
z^2\le\frac{752\kappa}{3d}
\left[\sqrt{2(1-\alpha)}+
\sqrt{\mathbb E_a\|Oa-\pi(a)\|^2}\right]^2.
$$

Using the real sign and matching from note 04 yields $z^2\le B(1-|\alpha|)$ with $B<508$. The already-audited localization/matching estimate is used only here. With the prior zero-endpoint erratum, the resulting uniformly valid statements are

$$
z^2\le1300\epsilon(O),\qquad
z^2\le170000\epsilon(U)
$$

in the real case and for the real approximation to complex $U$, respectively. Strict coefficient comparisons may still be stated when the error is positive.

## 4. Four generators and the absolute class gap

[DMPZ], §3.3 and Theorem 3.1(4), printed p.10, explicitly supplies the upper bound four for the number of conjugate 2A generators, with the 2A improvement credited to Zisser. This is a published imported theorem. The audit read that statement and its surrounding argument; it did not obtain Zisser's original proof or construct four Monster matrices.

Let $\psi$ be a nontrivial complex irreducible of degree $m$. If a same-sign eigenspace of an involution had dimension $k>3m/4$, four conjugate copies would have intersection of dimension at least $4k-3m>0$. A vector in that intersection spans a line stable under every generator, hence under the whole group. This contradicts irreducibility when $m>1$. For $m=1$, nonabelian simplicity excludes any nontrivial linear character. The reasoning works for the **minus** spaces too; one must not restrict it to fixed vectors.

Thus both eigenvalue multiplicities are at most $3m/4$, and

$$
\left|\frac{\chi_\psi(c)}m\right|\le\frac12.
$$

Class averaging is central, so this bounds its operator norm on every nontrivial irreducible, and hence on the constant complement of the regular representation. It also bounds the class-conjugation operator on traceless endomorphisms, because the irreducible defining representation has only scalar invariant endomorphisms. The **absolute** bound is what prevents a hidden period-two obstruction in the subsequent walk.

## 5. Normalizer lemma: explicit hypotheses and reconstruction

The narrow repair to note 05 §5 is to specify the domains of $\beta,t,L$. Including the already implicit range for the operator-norm bound $q$, the complete conditions in addition to its group and assignment hypotheses are

$$
0\le q<1,\quad 0\le\beta<1,\quad t>0,\quad
L\in\mathbb Z_{\ge1},
$$

$$
z^2\le\beta t^2,\quad r=\frac{q+\beta}{1-\beta}<1,\quad
(|G|-1)r^L<1,\quad Lt<1,\quad3Lt<s_0.
$$

The conclusion remains exactly $\min_{s=\pm1}\|O-sR\|_{2,d}^2\le z^2/(1-q)$ for an orthogonal normalizer $R$.

**Why the domains cannot be inferred from the display (R09).** Use the standard real four-dimensional representation of $A_5$ and its 15 double transpositions. It has $q=1/3$ and $s_0^2=3/2$. Set $O=I$, $h_c=c$, $z=0$, $\beta=2$, $t=1/100$, $L=1$. Every displayed scalar inequality in the unqualified historical statement holds: $r=-7/3<1$, $59r<1$, $Lt<1$, and $3Lt<s_0$. Nevertheless the good walk is the full class walk, of nontrivial norm $1/3$, so the asserted norm bound by $r=-7/3$ is false. The identity also cannot be a word of exactly one nonidentity involution.

The new [exact witness checker](../checks/audit_parameter_domains.py) verifies the group assumptions using a $60\times60$ integer adjacency matrix $A$: its eigenvalues are $15,-5,0,3$ with multiplicities $1,18,16,25$. A valid-domain control with $\beta=0$, $L=5$ has positive five-step entries and satisfies the intended inequalities. This is a counterexample to the unrestricted **proof specification**, not to the normalizer conclusion: the selected $O=I$ already normalizes the group. No counterexample under the corrected domains was found.

**Conditioning and exact-length support.** For the actual bad fraction $\beta'\le\beta$, averaging translations preserves both constants and their orthogonal complement, even without conjugacy invariance. On that complement,

$$
T_{\rm good}=\frac{T_C-\beta'T_{\rm bad}}{1-\beta'},
\qquad \|T_{\rm good}\|\le\frac{q+\beta'}{1-\beta'}\le r.
$$

If $\beta'=0$, omit the zero bad-set term rather than define an average over the empty set. Every step is an involution, making the good walk self-adjoint. With counting measure, the vectors $\delta_g-\mathbf1/n$ have norm $\sqrt{1-1/n}$. Therefore

$$
\left|T_{\rm good}^L(e,g)-1/n\right|
\le(1-1/n)r^L<1/n.
$$

Every transition entry is positive. Thus every group element has a word of **exactly** $L$ good steps; no unproved word-padding argument is needed.

**Discrete rounding.** Replacing the factors of such a word by their assignments costs at most $\delta=Lt$ by bi-invariance and telescoping. Two candidate group matrices within $\delta$ would be less than $s_0$ apart, so the candidate is unique and independent of the chosen word. It is also the globally nearest group matrix: any closer competitor would itself lie within $\delta$. Call the map $\phi$.

The matrices assigned to $gh$ and to $\phi(g)\phi(h)$ differ by at most $3\delta<s_0$, proving exact multiplication. If $\phi(g)=\phi(h)$, the original matrices differ by at most $2\delta<s_0$, proving injectivity. Finiteness makes $\phi$ onto; faithfulness identifies the matrix equalities with group equalities. For every original class element, including discarded ones, this actual nearest choice has error no larger than its original assignment. This last point is needed to recover an average bound without a word-length factor.

**Nonzero intertwiner.** Put $\sigma=\rho\circ\phi$ and

$$
A_0=\mathbb E_g\sigma(g)^{-1}O\rho(g).
$$

Reindexing $k=gh$ gives $A_0\rho(h)=\sigma(h)A_0$, with the orientation printed in the note. Each summand is within $\delta$ of $O$, so $\|A_0-O\|_{2,d}\le\delta<1=\|O\|_{2,d}$; hence $A_0\ne0$. Absolute irreducibility gives $A_0^TA_0=a^2I$, $a>0$. Thus $R=A_0/a$ is orthogonal and implements $\phi$. Equivalence of the two representations has been proved by this construction, not silently assumed.

**Sharp average conclusion.** For $Q=R^TO$, $m=\operatorname{Tr}(Q)/d$, and $Q_0=Q-mI$, let $\mathcal C$ be class conjugation averaging. Its only invariant line is $\mathbb RI$. Keeping all the original assignments gives

$$
z^2\ge\mathbb E_c\|Q\rho(c)-\rho(c)Q\|_{2,d}^2
=2\langle Q_0,(I-\mathcal C)Q_0\rangle_{2,d}
\ge2(1-q)(1-m^2).
$$

Finally $\min_{s=\pm1}\|Q-sI\|_{2,d}^2=2(1-|m|)\le2(1-m^2)$. This proves the stated coefficient and explains why $L$ does not multiply the final error estimate.

## 6. Character data and signed-Monster identification

The pinned GAP source [GAP] was retrieved through the GitHub connector and compared with the retained transcription. **All 194 centralizers and all 194 degree-196883 character entries match.** Its returned source blob is the recorded `cece771b31a8d764cc3c34428cffa7959fa0747a`. Exact rational averaging gives

$$
\sum_C\frac{\chi(C)^k}{|C_G(g_C)|}=1,0,1,1,6
\quad(k=0,1,2,3,4).
$$

The correct array locators are centralizers **2114–2130** and the character row **2264–2270**; the table header begins at 2110. The historical centralizer range ended one line early and omitted the final ten entries from the locator, not from the transcription. The data file remains unchanged, with this report serving as its provenance erratum.

The full pinned file was also retrieved transiently to inspect the degrees of its 194 ordinary irreducible rows, resolving the `GALOIS` row references at the degree level. There is one degree-one row, minimum nontrivial degree 196883, and a unique row of that degree. A nontrivial Monster representation of dimension 196883 must consequently be this irreducible; nontriviality of the traceless Griess action follows already from the Ising involution spectrum. This checks the identification of the row, rather than relying on a matching integer degree alone. GAP was not executed; the complete character table and its construction were not independently validated or bundled.

In particular the full tensor-invariant space $(V^{\otimes3})^{\mathbb M}$ has dimension one and is spanned by the nonzero real symmetric tensor $T$. The axis third moment is therefore $\mathbb E_a a^{\otimes3}=M T/(d\kappa)$, since contraction with $T$ gives $M$. The second moment is $I/d$ by irreducibility and trace. These are moment identities, not a spherical-three-design assertion.

If an orthogonal $R$ normalizes the represented Monster, it preserves that real invariant line, hence $R^{\otimes3}T=\pm T$. Odd tensor degree allows a common sign change to fix $T$. Metric and cubic preservation imply preservation of the projected product, and extending the map to fix $t$ preserves the full product. The classical full-automorphism theorem [HS], Theorem 5.7, then gives

$$
N_{O(d)}(\rho(\mathbb M))=\{\pm\rho(g):g\in\mathbb M\}.
$$

There is no appeal to the false general assertion that a finite group's normalizer equals the group. The existing $A_5$ odd-permutation negative control illustrates that distinction but is not the proof of the Monster case.

The maximum nonidentity character value is 4371, so the ordinary normalized group-matrix separation is

$$
s_0^2=2-2\frac{4371}{196883}=\frac{8192}{4189}>\frac{25}{16}.
$$

This is separation of the actual group matrices used in word rounding, not a silently substituted projective separation.

## 7. Numerical margins, local theorem, and logarithm bootstrap

The Monster parameters $q=1/2$, $\beta=1/16$, $t=1/600$, $L=250$ satisfy every repaired domain. They give $r=3/5$, $Lt=5/12<1$, and $3Lt=5/4<s_0$. The exact order from [GAP] gives $(|G|-1)(3/5)^{250}<1$. The admissible average error is $z^2\le1/5760000$, and the normalizer result becomes $D_{\mathbb M}(O)^2\le2z^2$.

The proposed loss thresholds leave the following exact positive margins:

$$
\frac1{5760000}-1300\cdot10^{-10}=\frac{157}{3600000000},
\qquad
\frac1{5760000}-170000\cdot10^{-12}=\frac{13}{3600000000}.
$$

They first imply $D_{\mathbb M}(O)\le52\sqrt\epsilon$ and $D_{\mathbb M}(U)\le600\sqrt\epsilon$. These preliminary, deliberately loose coefficients suffice because

$$
d\,52^2\,10^{-10}=\frac{33273227}{625000000}<\frac19,
\qquad
d\,600^2\,10^{-12}=\frac{1771947}{25000000}<\frac19.
$$

Thus the **ordinary operator norm** distance to a phase times a Monster element is below $1/3$. This uses $\|X\|_{\rm op}\le\sqrt d\|X\|_{2,d}$, and does not use the sharper final coefficient circularly. For real $O$, a minimizing phase can be chosen as a sign, since all group overlaps are real.

For the resulting unitary $X$ near identity, the principal Hermitian logarithm $K$ has $\|K\|_{\rm op}\le2\arcsin(1/6)$. Centering requires the factor two:

$$
H=K-\frac{\operatorname{Tr}K}{d}I,
\qquad \|H\|_{\rm op}\le4\arcsin(1/6)
\le\frac4{\sqrt{35}}<\frac\pi4.
$$

The mean is absorbed into the common phase. The trace-zero and radius hypotheses of the local theorem are now proved.

For completeness, reconstruct that local theorem using $K_H=H\otimes I+I\otimes H$. Tensor symmetry gives $W^\dagger K_HW=2\mathcal E(H)$, so

$$
q(H)=\frac{2\operatorname{Tr}H^2+2\operatorname{Tr}[H\mathcal E(H^T)]
-4\operatorname{Tr}\mathcal E(H)^2}{d}.
$$

On a Hermitian component of parity $\eta$ and channel eigenvalue $\lambda$, the coefficient is $2+2\eta\lambda-4\lambda^2$. The nonscalar minimum is $3132/1681$. For odd parity the Hermitian matrices are $i$ times real skew matrices; $\operatorname{Tr}H^2=\|H\|_F^2$ still has the positive sign. The unique scalar kernel is removed by centering.

The rejection is $\|[P,e^{iK_H}]\|_F^2/(2d)$. Since the spectrum of $K_H$ is in $[-\pi/2,\pi/2]$, the eigenvalue chord bound gives

$$
\epsilon(e^{iH})\ge\frac4{\pi^2}q(H)
\ge\frac{12528}{1681\pi^2}\frac{\|H\|_F^2}{d}
\ge\frac{12528}{1681\pi^2}D_{\mathbb M}(e^{iH})^2.
$$

This confirms the prefactor in C13. At zero error all these inequalities remain valid with $H=0$.

For C12, the optimal transport sign need not maximize $\alpha$. The prior audit's global upper-deficit estimate nevertheless gives $1-\alpha\le2\mathsf W^2$. Section 3 then gives

$$
z^2\le A_W\mathsf W^2,\qquad A_W=10421216/196883,
$$

$$
\frac1{5760000}-A_W\frac3{10^9}
=\frac{1117313}{75402000000000}>0.
$$

Thus the corrected statement is $D_{\mathbb M}(O)^2\le(20842432/196883)\mathsf W(O)^2\le106\mathsf W(O)^2$ at the stated transport threshold. The last comparison is strict only for positive transport error.

## 8. Integration consequences and validation

The reconstructed chain supports C11 with the explicit domains, C14 with the checked invariant-cubic input, and C12/C13 with the corrected endpoint convention and unchanged constants. The spectral/transfer dependencies of C03–C06 and C08 have also been checked as recorded above. C09's full independent-device analysis is not a separate deliverable of this continuation.

The integration workspace should apply the prior report's README/STATUS endpoint and audit-status corrections, add the parameter domains when restating C11, and use the corrected source locators when citing the character excerpt. These are narrow corrections, not changes to the archival notes or original data. This PR does not edit shared front-door files.

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py` passed before and after these changes: snapshot/import checks passed and all twelve scientific replays were byte-identical to their retained reports. The new parameter-domain checker passed all 20 checks separately under normal Python, `-O`, and `-OO`, with identical 3299-byte stdout (SHA-256 `a63c896d5094225dfc35a31396023b1440a7a190b4d545826d1daf6d9aa3b005`). It uses explicit exceptions, not removable assertions. This exact arithmetic verifies the witness and control; the analytical and imported-source conclusions rest on the reconstructions above.

The only new matrix computation is the exact 60-state $A_5$ walk for the omitted-hypothesis witness. The largest matrix in the preserved historical replays remains $256\times256$. No full Monster tensor, Monster matrices, or axis enumeration was used. No downloaded literature or source table is bundled. The manifest records the new audit artifacts and the intentionally updated audit index; all original scientific manifest entries remain unchanged.

## Source register

- **[M]** A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, [arXiv:math/0007169v1](https://arxiv.org/pdf/math/0007169v1). §1.1, printed pp.4–5; Corollary 4.1, p.16; §4.2, p.17. Used for the full-product trace and Ising spectral inputs. The original Norton chapter remains a separate source/priority obligation.
- **[DMPZ]** L. Di Martino, M. A. Pellegrini and A. E. Zalesski, *On generators and representations of the sporadic simple groups*, [arXiv:1210.6152v1](https://arxiv.org/pdf/1210.6152v1), §3.3 and Theorem 3.1(4), printed p.10; Communications in Algebra **42** (2014), 880–908. The 2A upper bound four is explicitly attributed there to Zisser. No claim is made to have read Zisser's original proof.
- **[GAP]** ATLAS-origin ordinary character table in `jmichel7/gap3-jm`, [commit `64365f30757f5374c86511b377d7d98eb15c1e02`, `tbl/ctomonst.tbl`](https://github.com/jmichel7/gap3-jm/blob/64365f30757f5374c86511b377d7d98eb15c1e02/tbl/ctomonst.tbl), blob `cece771b31a8d764cc3c34428cffa7959fa0747a`. Centralizers: lines 2114–2130; degree-196883 row: lines 2264–2270. The source file, rather than only the retained JSON, was retrieved for this comparison. Full-table character-theoretic construction was not re-proved.
- **[HS]** G. Höhn and M. Seysen, *The Order of the Monster Finite Simple Group*, [arXiv:2508.01037v1](https://arxiv.org/html/2508.01037v1), Lemmas 2.4 and 2.14, Theorems 5.7–5.8. Full automorphism and Ising inputs are imported classical facts with the normalization/source audit in the preceding report; its V12 records the source's nonblocking complement-norm typo.
- **[VOA audit]** [voa_extrema_audit.md](voa_extrema_audit.md), audited base `0376cbfb8e8640d1b278b5c55c4815d83f5b6ca1`, merged at this report's base. Supplies the reconstructed extrema/localization dependency and the exact references for full-VOA unitarity and the necessary Virasoro classification. Its V13 is the endpoint erratum used throughout this continuation.
