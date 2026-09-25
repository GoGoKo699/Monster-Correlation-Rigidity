# Probe access and calibration: what the two-query theorem costs

Date: 25 September 2026. Initial live main: `a450e022781c4109609ff8f274787942c513df1a`.
Mathematical baseline: audit branch `c48f2c7798f0c507d657cb43e9ce7c41d7d5b83d` (PR #2), incorporating the separately preserved VOA audit.

## Scope and outcome

This is the third deliverable of the original work order: an access-model assessment, not a new rigidity threshold or a claim of efficient implementation. The reductions below are elementary deductions or explicitly attributed applications of existing algorithms. Their novelty is not claimed. The first-pass priority comparison is [separate](../audits/priority_matrix.md).

The two uses counted by C13 are calls to the unknown fixed unitary U. They do not pay for the trusted state and effect. We identify a sufficient coherent oracle, compare two weaker access routes, and give a confidence statement with preparation/measurement error. No Monster-sized tensor, matrix, or axis list is constructed.

Use V=C^d with d=196883, kappa=13858/3, W an isometry V -> V tensor V, P=WW*, and sigma=P/d. In an orthonormal real basis W_(ij,a)=T_aij/sqrt(kappa). Let Q=U tensor U and

$$\epsilon(U)=1-\operatorname{Tr}(PQ\sigma Q^*)=1-\operatorname{Tr}(PQPQ^*)/d.$$

Every inequality here uses a non-strict endpoint at zero, as required by the prior audit. The ideal gate theorem used below is C13, including both audit supplements; this note does not re-prove its Monster-specific algebraic inputs.

## 1. A sufficient coherent-access model

Suppose a specified unitary circuit A on two logical d-dimensional registers satisfies

$$A(|a\rangle\otimes|0\rangle)=W|a\rangle,\qquad 0\le a<d.$$

Additional work registers are permitted only if they return to a common known state. Equivalently enlarge the fixed input subspace and explicitly include the workspace-zero test. Existence of a unitary extension in finite dimension is not an efficient synthesis theorem.

Let Pi_in=I_d tensor |0><0|. Then A Pi_in A*=P. Choose a uniformly using classical randomness, prepare |a,0>, and apply A. Forgetting the classical label prepares exactly sigma. After Q, apply A* and measure Pi_in. The acceptance effect before A* is exactly P. Thus a trial uses two forward U calls, one A, one A*, and a simple input-subspace measurement. Random-basis preparation is sufficient; a coherent maximally entangled state is not required for this route.

If C_A(eta) is the elementary-gate cost of a suitably accurate clean implementation, the cost per trial is at least accounted for by

$$2C_U+C_A(\eta_{\rm prep})+C_{A^*}(\eta_{\rm meas})+C_{\rm basis}+C_{\rm membership}.$$

No bound on C_A is proved here. For a fixed exceptional dimension, bare asymptotic claims in d are particularly weak; concrete gate counts, ancillas, and precision dependence are needed.

**Padding boundary.** On 18-qubit registers, D=2^18>d. The correct input projection is Pi_V tensor |0><0|, not I_D tensor |0><0|. Otherwise the d valid input labels are replaced by D labels and the accepted subspace has rank D, not d. For example |d,0> is accepted by the naive test and rejected by the correct one. Under an arbitrary extension A, its image remains an unwanted accepted state. Workspace and logical-subspace checks must be part of the effect. This is not a leakage-tolerance theorem.

## 2. Channel access prepares the probe, but does not specify its measurement

The multiplication channel is

$$\mathcal E(X)=\frac1\kappa\sum_k L_kXL_k.$$

Its normalized Choi state in the chosen real basis is exactly sigma:

$$J(\mathcal E)=(\operatorname{id}\otimes\mathcal E)(|\Phi_d\rangle\langle\Phi_d|)=P/d.$$

Indeed, with Phi_d=d^(-1/2) sum_a |a,a>,

$$J(\mathcal E)_{ai,bj}=\frac1{d\kappa}\sum_kT_{kia}T_{kjb}=P_{ai,bj}/d.$$

Full tensor symmetry supplies the last equality. Thus an implementation of E plus a maximally entangled input prepares sigma with no postselection. This is a Choi identity, not a new channel-construction paradigm: using an intertwining isometry followed by partial trace is the established Clebsch-Gordan-channel construction [BCly, section 2.3]. We do not claim this particular channel is a Temperley-Lieb channel merely because that is the title of [BCly].

A channel oracle for E does not *specify* a reversible dilation or its inverse. This route consequently leaves P measurement as a separate requirement. Copies of J(E) and coherent access to a clean chosen dilation must not be treated as interchangeable oracles. No universal separation theorem for all such oracles is proved here.

Conversely, if a genuine P measurement is available, postselecting I_(d^2)/d^2 succeeds with probability Tr(P)/d^2=1/d and outputs sigma. The mean number of attempts is d=196883. This is a valid but circular proposal if P was the missing resource. It is not a lower bound on preparation by other methods.

## 3. A repeated SWAP test is not the same membership experiment

Assume access to independent copies of sigma, but do not assume P measurement. Put omega=Q sigma Q*. Comparing sigma and omega with an ordinary SWAP measurement gives

$$\operatorname{Tr}(\sigma\omega)=\frac{1-\epsilon}{d},\qquad p_+=\frac12+\frac{1-\epsilon}{2d}.$$

The desired rejection signal is suppressed by d relative to the measured expectation. Given N independent binary SWAP outcomes, the estimator hat epsilon=1-d(2 hat p_+-1) has additive error at most delta with failure probability at most alpha whenever

$$N\ge\frac{2d^2}{\delta^2}\log\frac2\alpha.$$

This follows from the elementary bounded-Bernoulli concentration inequality for |hat p_+-p_+|<=delta/(2d). Clipping the estimator to [0,1] cannot increase its error.

There is also a restricted lower bound. For two admissible losses separated by delta, their Bernoulli probabilities differ by delta/(2d), and lie in [1/2,3/4] for d>=2. With natural logarithms,

$$\operatorname{KL}(\operatorname{Ber}(p)\|\operatorname{Ber}(q))\le\frac{(p-q)^2}{q(1-q)}\le\frac{4\delta^2}{3d^2}.$$

For equal-prior decision error <=1/3, the N-outcome laws need total variation at least 1/3. Pinsker and KL additivity give N>=d^2/(6delta^2). This proves quadratic scaling for experiments whose complete data are these independent binary SWAP outcomes, including arbitrary classical processing of them. It is **not** a lower bound for general collective quantum measurements, purified/coherent access, or all tests of the fixed Monster probe. The simple upper and lower constants refer to their separately stated estimation/decision tasks, not identical success specifications.

Here d^2=38762915689. At delta=10^-12 the scale d^2/delta^2 is about 3.88 x 10^34. This is why replacing the projector with the ordinary repeated SWAP measurement is not a practical shortcut under the present gate-certificate precision. It says nothing about an as-yet-unconstructed structure-aware measurement.

## 4. Copy-based simulation does yield a projector, at a large sufficient cost

Flat spectrum gives the exact identity

$$e^{-i\pi d\sigma}=I-2P.$$

Measuring P via interference requires a **controlled** reflection with its relative phase fixed. Access only to the channel of an unknown reflection does not by itself provide that control: R and -R have the same conjugation channel but different controlled operations.

A valid sample-based construction is to use the flagged program state

$$\sigma_f=|1\rangle\langle1|\otimes\sigma.$$

Density-matrix exponentiation on the target control-plus-pair system, for t=pi d, approximates the channel of

$$e^{-i\pi d\sigma_f}=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes(I-2P).$$

Prepare the target control in |+>, apply this simulation, and measure X. The minus outcome is the P outcome. This explicitly produces the control rather than assuming controlization of a channel oracle.

The non-asymptotic DME bound in [GKPPW, Theorem 2] gives normalized diamond error <=4t^2/n when n>t. For 0<eta<=1 and this t, n=ceil(4 pi^2 d^2/eta) satisfies the condition and bounds every outcome-probability error by eta. Each program copy uses one fresh sigma and a known flag. The coefficient 4 pi^2 d^2 is approximately 1.53 x 10^12. At eta=10^-12 this generic sufficient budget is approximately 1.53 x 10^24 program copies for one such measurement, before preparing the tested probe.

These are **upper budgets supplied by this generic simulation theorem**, not necessary costs or a lower bound for the known Griess projector. The source's worst-case lower bound over arbitrary program states cannot be specialized into a lower bound for this single known state without another argument. Ideal program copies and partial-SWAP gates are assumed; their inaccuracies and synthesis costs are additional resources. A structure-aware construction of A or P can be much better and has not been ruled out.

## 5. Calibration and finite-sample theorem

Retain a fixed ideal U on the specified logical subspace. Suppose the prepared density matrix and acceptance effect satisfy

$$\tfrac12\|\widetilde\sigma-\sigma\|_1\le a,\quad 0\le\widetilde P\le I,\quad\|\widetilde P-P\|_{\rm op}\le b.$$

Writing tilde epsilon=1-Tr(tilde P Q tilde sigma Q*),

$$|\widetilde\epsilon-\epsilon|\le a+b=:\eta.$$

To see this, add and subtract Tr(tilde P Q sigma Q*). The first term is bounded by trace distance because tilde P is an effect; the second by its operator-norm error against a normalized state. No dimension factor is introduced. This is a trusted-error-budget extension around a fixed U, **not** certification of arbitrary unknown noisy channels.

For independent identical Bernoulli trials with k rejections out of N, let p_up be a one-sided binomial upper confidence bound of coverage 1-alpha. For k<N it is the solution of

$$\sum_{j=0}^{k}\binom Nj p_{\rm up}^{j}(1-p_{\rm up})^{N-j}=\alpha,$$

and take p_up=1 if k=N. With probability at least 1-alpha, epsilon<=min(1,p_up+eta). If the a,b bounds themselves are probabilistic, their failure budgets must also be included, for example by a union bound.

Consequently, whenever u=p_up+eta<=10^-12, C13 implies at the same confidence

$$D_{\mathbb M}(U)\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt u\le1.151\sqrt u.$$

For zero rejections, p_up=1-alpha^(1/N). At alpha=.05 and eta=0 the minimal sufficient integer count is recorded in the checker; it is approximately 2.996 x 10^12. Allocating half the loss threshold to eta doubles this to approximately 5.991 x 10^12. If eta>=10^-12, this particular conservative certificate cannot be triggered at any finite N. This is a limitation of the stated theorem and budget, not an impossibility theorem for all noise-aware protocols.

An approximate clean A with operator error zeta changes each pure prepared vector by at most zeta and hence gives preparation trace error at most zeta after mixing. Its pulled-back projection differs by at most 2zeta. This supplies one sufficient translation from circuit synthesis accuracy to a,b. It does not assert these worst-case estimates are tight.

## 6. A concrete compilation target, not an efficiency claim

Seysen's v5 construction [S, section 10.1, equations (10.1.1)-(10.1.7)] gives five nonzero types of a real symmetric cubic on the full 196884-dimensional space, using blocks of dimensions 300, 98280, and 4096 x 24. Basis normalization is not uniform: off-diagonal symmetric-matrix basis vectors have norm sqrt(2). The cubic formulas, rather than the mere availability of generator matrices, are a plausible start for constructing W. They are existing algebraic data, not a project discovery.

Before a gate count can be claimed, translate this full cubic and its invariant metric to an orthonormal basis with the project's product normalization; remove the identity direction; construct coherent index/sign and amplitude routines; uncompute work registers; and account for any normalization amplification or postselection. Efficient classical arithmetic modulo an odd integer is not a unitary preparation circuit. No full tensor should be materialized to perform this assessment.

The next bounded access deliverable is the metric/identity conversion and one block-level coherent primitive with all amplitudes and costs stated. It need not presuppose that the complete construction is efficient. Proof-level priority of the assembled rigidity theorem remains a separate outstanding task.

## 7. Evidence and attribution

The new checker tests abstract access identities on d=2,3 isometries and a small symmetric d=3 tensor. It includes a padding counterexample, a controlled-reflection calculation, and exact/decimal confidence arithmetic. Its largest matrix is 81 x 81. It does not test the Monster tensor, complete compilation, statistical power on a physical device, or the claimed novelty of any result.

Primary references, accessed 25 September 2026:

- [BCly] M. Brannan, B. Collins, H. Lee, S.-G. Youn, *Temperley-Lieb quantum channels*, arXiv:1810.08001, section 2.3 (printed p.7). https://arxiv.org/abs/1810.08001
- [GKPPW] B. Go, H. Kwon, S. Park, D. Patel, M. M. Wilde, *Sample-based Hamiltonian and Lindbladian simulation: Non-asymptotic analysis of sample complexity*, arXiv:2412.02134v3, Theorem 2 and equation (30), Quantum Sci. Technol. 10 045058 (2025). https://arxiv.org/html/2412.02134v3
- [S] M. Seysen, *A computer-friendly construction of the monster*, arXiv:2002.10921v5, section 10.1, printed pp.33-34. https://arxiv.org/abs/2002.10921v5

Source-depth boundary: the indicated parsed PDF passages and the DME HTML theorem were read. PDF screenshot requests failed in the browser service; no successful visual verification of those PDF pages is claimed in this checkpoint. No downloaded paper is bundled. For C01-C14 dependencies and corrections, use the two existing audit reports, not this access note as a substitute.
