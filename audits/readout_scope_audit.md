# Assumption audit: the sharp readout threshold is not Monster-specific

Date: 26 September 2026. Read baseline: `09e3f98ad79034eefab43f4fb9ea432368fc19e7`.
This is the owner's requested revision/consolidation pass, not another extension of the extremal moment catalogue. All archived statements and evidence are retained. The existing readout theorems are not falsified; their proposed use as evidence of Monster-specific physics needs revision.

## 1. Finding

The following package does **not** require holomorphicity, rationality, central-charge minimization, the J character, the conformal 11-design theorem, the exceptional trace identities, or the six Monster-sized contraction eigenspaces:

* Primary modes through weight five strictly identify any pure state on P2, even against mixed alternatives.
* The trace-distance bound has the same sufficient constants 5/2 and 9 at c=24.
* Primary modes through weight six linearly identify arbitrary states on P2.

These conclusions follow for any unitary VOA of CFT type with finite-dimensional grades, V1=0 and P2 nonzero. We use its PCT-real structure and positive Hermitian form. The central charge is necessarily at least one under these conditions. No group action is an input. The proof below removes the unnecessary hypotheses instead of asserting that their absence in examples is sufficient evidence.

The cutoffs are simultaneously sharp in the elementary current-free rational lattice fixed-point VOA

U = V_L^+,  L = sqrt(6) Z^24.

It has c=24 and dim P2=299, not 196883, and is not holomorphic. In U the exact universal pure-state cutoff is five and the all-state linear cutoff is six. The earlier four-oscillator witnesses lie in this VOA too. This does not disprove moonshine uniqueness in the holomorphic class: the comparator is explicitly outside that class.

This distinction matters for the research narrative. The readout theorem can remain a general mathematical-physics result. It cannot, by itself, explain why the exceptional Monster is selected. The unusually long **thermal** cancellation and the special extremal contraction spectrum are NOT transferred to this larger class.

## 2. Conventions and minimal assumptions

Write P=P2 for the first Virasoro-primary space and d=dim P. The two-point metric is real and positive on PCT-fixed fields. A primary w of weight h has compressed zero mode

M_h(w)=pi2 w_(h-1) pi2,

which is symmetric for even h and skew for odd h. Use the Hermitian observable A_h(w)=M_h(w) for even h and i M_h(w) for odd h. All observable coefficient bases are orthonormal in the field two-point metric. This is the same dimensionless, unwhitened data convention used in the local stability note; it is not a per-observable error budget or a physical measurement implementation.

Define the primary product mu, real symmetric cubic C, and matrices L_a by

C(a,b,c)=<mu(a,b),c>,  L_a b=mu(a,b).

Set gamma=8/c. The FULL weight-two product is

a*b=mu(a,b)+sqrt(gamma)<a,b>t,  t=omega/sqrt(c/2).

No assumption Tr L_a=0 or Tr L_a L_b=kappa<a,b> is used. In particular there is no assumption of isotropic multiplication matrices. Define linear maps on matrices

F(X)=sum_i L_i X L_i,
Q(X)=sum_i L_i Tr(L_i X),
J(X)=Tr(X)I.

For an orthonormal real basis w_(h,alpha) of P_h, including mode-kernel vectors, define the positive frame map on Hermitian matrices

K_h(X)=sum_alpha A_h(w_(h,alpha)) Tr(A_h(w_(h,alpha))X).

K2=Q. Each even K_h kills the imaginary-skew input sector and each odd K_h kills the real-symmetric one. Different weights need NOT have mutually orthogonal images in the general theory. The proofs do not assume they do.

## 3. Four finite channel identities replace the exceptional spectrum

Let I_s and I_a be the identity maps on real symmetric and imaginary-skew Hermitian matrices, respectively. Direct mode commutation followed by Virasoro descendant subtraction gives

K3 = 2(F_- + gamma I_a),

K4 = F_+ + (2+gamma)I_s + a Q + j J,

K5 = 4 I_a + t K3,

K6 = 4 I_s + r K4 + s Q + z J,

where the maps in the second and fourth lines are restricted to the symmetric input sector, and

a=(c-88)/(2(5c+44)),
j=4(c-44)/(c(5c+22)),
t=2(c-25)/(7c+114),
r=2(c-40)/(9(c+24)),
s=-c(5c^2-572c+11220)/(2(c+15)(5c+44)(35c-34)),
z=-8(c^2-55c+748)/((2c-1)(5c+22)(7c+68)).

Here I_s and I_a are superoperator identities, not physical identity fields. These equations concern actual primary mode frames, so positivity of their left sides is physical input. They are not a construction of a VOA from an arbitrary symmetric cubic.

### Derivation and descendant bookkeeping

For four primary external fields a,b,c,d let

A=<a,b><c,d>, B=<a,c><b,d>, C0=<a,d><b,c>,
X=<a*c,b*d>, Y=<a*b,c*d>, Z0=<a*d,b*c>.

The unprojected pair states at levels 0,1,2,3 have Grams A,0,Y,Y+X-Z0. At 4<=n<=6 the Gram is

binom(n-1,3) B + delta_(n4) C0 + (n-2)X+Y-Z0.

This follows by commuting a_(n-1) past c_(3-n). No trace theorem is involved. The primary part of a_(0)b is B3(a,b)=a_(0)b-(1/2)D(a*b). Its full four-label Gram is X-Z0; all stress terms are retained. This is the standard VOA mechanism behind Norton positivity.

The weight-four subtraction uses vacuum descendants with Gram

[[5c,3c],[3c,c(c+8)/2]],

and level-two descendants of a unit weight-two primary with Gram

[[8+c/2,12],[12,40]].

Their pair overlap vectors are (6,8) and (4,6). The weight-three derivative is also removed. This gives K4 as displayed. Its derivation is valid without the class-S assumptions appearing later in Matsuo's trace theorem.

For the higher subtractions, the scalar descendant coefficients needed here are

b35=2(6c+139)/(7c+114),
b46=(25c+728)/(9(c+24)),
b26=(250c^3+15185c^2+180482c-179520)/(2(c+15)(5c+44)(35c-34)),
b06=4(100c^3+3257c^2+23724c-11968)/(c(2c-1)(5c+22)(7c+68)).

For b35 and b46 the primary Gram matrices and overlap vectors are respectively

[[12+c/2,18],[18,84]], (5,12),
[[16+c/2,24],[24,144]], (6,20).

b26 uses the five level-four partitions of the weight-two module. b06 uses the four vacuum partitions of six. The checker recomputes these finite rational systems rather than loading their values. All denominators are nonzero for c>=1.

On skew inputs the raw level-five Gram is 4I_a+2K3. Subtracting b35 K3 gives t=2-b35. On symmetric inputs the raw level-six Gram is 3K4+4I_s+(1-3a)Q+(gamma-3j)J. Subtraction of b46 K4, b26 Q and b06 J gives the final line. This proves the general finite identities.

## 4. General pure-state witness

For any complex pure projector P define

W_P=Q(P)-F(P)+(2+gamma)(I-P).

The four-label B3 Gram implies

Q(P)-F(P)+gamma(I-P)=sum_alpha K_alpha P^T K_alpha^T,

where K_alpha are real skew matrices coming from an orthonormal P3 basis. This is a positive sum; the transpose is essential. Each term annihilates the target vector because z^T K_alpha z=0 for every complex z. Therefore

W_P P=0,  W_P>=2(I-P).

Substitute the generic frame identities. With

A_c=2(5c+44)/(5c+22),
b_c=11c/(2(5c+44)),
e_c=(5c+164)/(2(7c+114)),

one obtains the exact measured-span expression

W_P=A_c I+b_c K2(P)-e_c K3(P)-K4(P)-(1/2)K5(P).

Thus weight-five primary expectations determine the expectation of a positive witness whose only zero direction is the target, regardless of the target's phase or the rank of an alternative state. Real targets need only even weights two and four. No J-character, contraction multiplicity, fourth trace or fifth trace appears in this proof.

## 5. The old stability constants survive with no extremal assumptions

The unitary real-cubic bound also needs less than the old statement assumed. At a real unit maximum m=C(x,x,x), mu(x,x)=m x. Combining x with t produces a Virasoro vector of charge

c_u=(c/2)(1-m/sqrt(m^2+32/c)).

Its four level-six vacuum descendants have Gram determinant

(3/4)c_u^4(2c_u-1)(5c_u+22)^2(7c_u+68).

Positivity forces c_u>=1/2. Since c_u<=c/2, a nonzero P2 implies c>=1. Rearranging gives the group-free norm cap

M_c^2=32(c-1)^2/[c(2c-1)].

The real Banach symmetric-tensor theorem then bounds ||mu(a,b)|| by M_c||a||||b||. For complex psi=x+i y, the vector z=mu(x,x)+mu(y,y) has norm at most M_c. Hence ||Q(P)||op<=M_c^2 and

2(I-P)<=W_P<=B_c(I-P),  B_c=M_c^2+2+8/c.

For data m_(<=5) in the unwhitened two-point-normalized primary bases, the witness coefficient norm is bounded by

C_c^2=A_c+(b_c^2+b_c)M_c^2.

To see the cancellation, let r_h=Tr(P K_h(P))>=0. The target-kernel identity is A_c+b_c r2-e_c r3-r4-r5/2=0. The coefficient norm is

b_c^2 r2+e_c^2 r3+r4+r5/4
=A_c+(b_c^2+b_c)r2+(e_c^2-e_c)r3-r5/4.

Since 0<e_c<1 and r2<=M_c^2, the bound follows. Orthogonality between different primary-mode images is not used.

For density matrices rho,sigma put delta=||m_(<=5)(rho)-m_(<=5)(sigma)||2 and eta(rho)=1-lambda_max(rho). The same negative-eigenvector witness lemma as the archived stability note gives

(1/2)||rho-sigma||1 <= (C_c/2)delta+(B_c/2)eta(rho).

Briefly, write sigma-rho=X_+-X_- and let P be a largest-eigenvalue direction of X_-. The negative tail after this direction has trace at most eta(rho), by min-max; it is not claimed that X_-<=rho as an operator. The lower witness gap sees X_+ and its upper bound controls this tail. The coefficient norm controls its pairing with measured data. Exchanging states gives the smaller impurity tail if desired.

At c=24,

C_24^2=135249252/5609497<25, B_24=815/47<18.

Thus the previously announced inequality with 5/2 and 9 is **valid unchanged in this much larger class**. It remains an aggregate deterministic-data bound, not an efficient tomography protocol or a statement of optimal constants. It does not require the primary dimension to be196883. This is a correction of specificity, not a refutation of the theorem.

## 6. General all-state completeness by weight six

Let X be Hermitian, trace zero, and invisible to every primary mode through weight six. Then K_h(X)=0 for h=2,...,6. Split X into its real-symmetric and imaginary-skew parts.

On the skew part, K5=4I_a+tK3 immediately implies X_a=0. On the symmetric part, K6=4I_s+rK4+sQ+zJ and Tr X_s=0 imply X_s=0. Hence X=0.

Every state on P2 is therefore linearly identified by this field family. There is no assumption that its images are orthogonal or have the exceptional dimensions. In general the inverse is not the special five-sector Parseval expression in the extremal note; the displayed frame identities replace it. Completeness is an information statement conditional on known fields, not calibrated access to them.

## 7. A controlled comparison outside the holomorphic class

Take the positive even lattice L=sqrt(6) Z^24 and its sign-reversal fixed-point VOA U=V_L^+. Its central charge is24. Single oscillator currents are odd, and the shortest nonzero momentum fields have weight3, so U1=0 and U2 is just Sym^2 R^24, of dimension300. Removing the stress tensor gives dim P2=299.

The lattice and fixed-point unitarity results are in Dong-Lin; rationality is established by Dong-Jiang-Lin. Their stated C2-cofiniteness and irreducible-module classification give the remaining standard finiteness properties. In particular V_L^- is a non-vacuum U-module with a weight-one bottom space, so U is NOT holomorphic. This is a genuine different VOA, not an invented finite-dimensional cubic. No claim about its full automorphism-group classification is needed.

The local four-oscillator examples from the archived pure-state note belong to U without modification. Two disjoint diagonal quadratic primaries u,v give orthogonal states (u +/- i v)/sqrt(2). All even expectations agree and their weight-three pair is zero, so weight four fails. The antisymmetric derivative product at weight five separates them.

Similarly set a=h1h2, b=h3h4, c=h1h3, d=h2h4 at oscillator level one. The two normal products a_(-1)b and c_(-1)d are literally the same four-oscillator monomial. The symmetric pair difference X=a odot b-c odot d has eigenvalues (+1/2,+1/2,-1/2,-1/2), and all its raw pair channels through weight five vanish. The states I_U/4 +/- X/2 on this four-dimensional span are positive rank-two states with orthogonal supports and identical data through five. The next primary pair has nonzero norm and a weight-six action distinguishing them.

The upper theorems now apply to this entire comparison theory, so its pure and all-state linear cutoffs are EXACTLY five and six. Sharpness is not asserted for every current-free VOA: some smaller examples complete earlier. The general bound is sharp in a class containing this explicit example.

This comparator changes the class, rather than disputing minimality or uniqueness within holomorphic current-free theories. It keeps central charge24 and absence of currents fixed, but removes holomorphicity. We do not call it another holomorphic extremal theory.

## 8. What actually differs in the comparison

The absence of special trace identities is not cosmetic. In the comparison P2 is the traceless quadratic oscillator algebra. With q_A=(1/2)sum A_ij h_i(-1)h_j(-1)1, its metric is Tr(AB)/2 and full product is q_(AB+BA).

1. **Thermal cancellation does not persist to eleven.** The primary part R4 of sum_i e_i(-1)e_i has norm

||R4||^2=6n(n-1)^2(n+2)/(5n+22), n=24,

so ||R4||^2=990288/71>0. Its trace on U2 equals this norm by the Casimir/Riesz pairing. Thus it has a nonzero primary thermal one-point function already at weight four. This contrasts with the extremal class's vanishing through weight eleven; it does not transfer a holomorphic modular transformation law to U.

For verification, the quadratic algebra has kappa_osc=2(n+4)(n-2)/n. This follows by restricting the symmetric-square action and removing the scalar row and column. The generic K4 applied to I then gives the displayed norm. Direct Fock projections at n=2 and3 check it independently.

2. **The unitarity cap need not be saturated.** Any weight-two Virasoro vector q_A in U satisfies A^2=A. Its central charge is rank A, so its smallest nonzero charge is1, not1/2. The real normalized primary cubic has maximum squared 8(n-2)^2/[n(n-1)]=484/69 at n=24, below the cap2116/141. This can also be obtained by maximizing Tr A^3 under Tr A=0, Tr A^2=2; the stationary eigenvalues take two values and the maximum has multiplicities1 and n-1.

The known moonshine theory contains c=1/2 Ising Virasoro vectors and saturates the corresponding cubic cap. These facts are classical and were inputs/objects of the older extremum audit. They are not consequences of the new generic readout proof. The comparison shows why saturation, unlike the readout cutoff, is a plausible discriminator. It does not prove that holomorphic extremality forces saturation, or that one Ising vector identifies the entire VOA.

The next physical-selection target should be a precisely audited missing implication involving such genuinely restrictive structure, not another refinement of the generic tomography constants. The question of which positive solutions of the exceptional trace system are realized/classified remains open in this project.

## 9. Prior-work and audit verdict

Baldwin-Deutsch-Kalev already establish the distinction between completeness among pure/rank-bounded states and strict completeness against all positive states, together with robustness. Their result is general tomography; it does not by itself say which VOA fields form a strictly complete family. The present derivation provides that field-theoretic sufficient condition with weaker assumptions and explicit c-dependent constants. Its originality as a general VOA theorem has not received comprehensive priority clearance.

Audit outcomes:

* PASS within stated assumptions: the archived stable inequality and pure-state certificate; their old proofs use more assumptions than necessary, not too few.
* SCOPE CORRECTION: neither the5/6 readout thresholds nor the displayed c24 stability constants establish Monster-specific behavior. A genuine rational comparison theory shares them.
* RETAINED AS EXTREMAL-SPECIFIC INPUTS: the J spectrum, eleven-design cancellation, exceptional sector ranks and the canonical first response at weight12. They were unnecessary for the readout proof, not disproved.
* NOT AUDITED HERE: the full symbolic PR21 operator-redundancy certificate, all higher OPE consistency, uniqueness of the original cubic, and independent novelty/physical significance of every earlier checkpoint.
* REJECTED HISTORICAL INPUT STILL EXCLUDED: PR12's normalization-dependent null-state condition. No fifth trace of either convention is used here.

The exact checks validate finite computations and assumptions of the sampled controls, not all VOA axioms or a universal theorem by finite sampling. The universal result is the analytic finite-channel and positivity proof above.

## 10. Evidence and source depth

The fresh checker has191 labelled integer/fraction checks. It independently projects oscillator products in even c2 and c3 free-boson algebras, checks the full four-label generic Grams and genuinely complex witnesses with the nonorthogonal primary metric retained. Largest square matrix38x38; oscillator cutoff6. It certifies six generic rational Ward coefficients by exact univariate polynomial determinants (not interpolation), also evaluates finite Ward systems at seven central charges, the c24 constants, and the sharpness examples on four oscillator directions. These small controls are not the full c24 comparator or a Monster tensor. No exceptional character table or trace constant enters the generic tests.

The archived stable package was extracted without changing bytes: its thirteen payload hashes,101 new checks and119 prior checks reproduce under normal/-O/-OO. The new checker independently reproduces the c24 constants from the generic formulas. It is not an independent expert review or proof-assistant verification.

The live main was read at the pinned baseline. Historical repository execution and any remote write/CI outcome are recorded separately, never inferred from a local archive replay. No main file or earlier note is silently edited. New files use descriptive audit paths to avoid the existing two different 'Note24' names. No manuscript, release, outreach or full experimental implementation is performed.

### Primary sources inspected

[DL] C. Dong and X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361v1. Definition2.2, Lemma2.5, Corollary2.7, Theorem4.12 and the lattice involution construction were read. The requested page4 screenshot failed. This supplies the positive-mode convention and the lattice/fixed-subalgebra example, not the new readout argument. https://arxiv.org/abs/1308.2361

[M] A. Matsuo, *Norton's Trace Formulae for the Griess Algebra of a Vertex Operator Algebra with Larger Symmetry*, arXiv:math/0007169v1. Section1 modes, metric algebra and Virasoro vacuum Gram conventions; section3.2 and Note3.6 for Ising-vector context. Relevant parsed text was inspected; the page4 screenshot failed. No class-S trace theorem or exceptional numerical trace formula is assumed in this audit. https://arxiv.org/abs/math/0007169

[DJL] C. Dong, C. Jiang and X. Lin, *Rationality of vertex operator algebra V_L^+: higher rank*, arXiv:1011.5526v2; PLMS104(4),799-826(2012). Main rationality statement, Theorems3.2-3.3 and the positive-lattice setup were read. The C2 statement is attributed there to earlier authors; their original proof was not newly audited. The page2 screenshot failed. https://arxiv.org/abs/1011.5526

[BDK] C. H. Baldwin, I. H. Deutsch and A. Kalev, *Strictly-complete measurements for bounded-rank quantum-state tomography*, arXiv:1605.02109. Corollary2, its assumptions and AppendixA were inspected; printed page4 was visually inspected successfully. The general positivity/robustness principle is prior work. https://arxiv.org/abs/1605.02109

[FL] S. Friedland and L.-H. Lim, *Nuclear Norm of Higher-Order Tensors*, arXiv:1410.6072, real symmetric tensor norm theorem, inherited as recorded in the archived stability audit. Only the real norm is used; complex states are handled by real and imaginary parts. No original1938 Banach proof was obtained. https://arxiv.org/abs/1410.6072

Targeted searches for the precise VOA/readout combination did not settle priority. An unmatched search is not evidence of originality. No papers or fonts are bundled.
