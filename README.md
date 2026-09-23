# Monster Correlation Rigidity

**Research project for Ruge Lin.** Exceptional finite symmetry as an operational property of quantum correlations, rather than merely a group representation embedded in a small Hilbert space.

This repository collects five mathematical checkpoints and reproducible checks. The results are written derivations, **not independently reviewed theorems or established novelty claims**. There is no efficient implementation, practical verification, or quantum-advantage claim.

## Start here

The current task is a falsification-oriented proof and source audit, not manuscript preparation. Read [the claim ledger](STATUS.md) for the mathematical boundaries and [the workspace contract](WORKSPACES.md) before starting parallel work. A dedicated [independent-workspace audit brief](work_orders/INDEPENDENT_AUDIT.md) is ready; no such audit has been completed yet.

## Current derived result

A two-register mixed state derived from the Griess multiplication has collective projective unitary stabilizer exactly the Monster. For the corresponding ideal two-use unitary membership test, the latest derivation gives

$$\epsilon(U)\le10^{-12}\quad\Longrightarrow\quad
\min_{\theta,g}\frac{\|U-e^{i\theta}\rho(g)\|_F}{\sqrt{196883}}
\le\sqrt{\frac{1681\pi^2}{12528}}\sqrt{\epsilon(U)}
<1.151\sqrt{\epsilon(U)}.$$

The implication applies to every complex unitary on the specified logical space satisfying the loss threshold, without prior calibration. For real orthogonal operations the sufficient threshold is $10^{-10}$.

These thresholds are conservative proof guarantees, not claims of optimality. Reaching the complex threshold through zero-rejection independent sampling at 95% confidence would require about $3\times10^{12}$ ideal trials. Probe preparation and measurement costs have not been solved.

## The scientific mechanism

The quantum probe encodes a nonassociative multiplication. Its extremal vectors form the Ising-axis configuration. Each axis determines a genuine Monster involution through a spectral projection. Approximate preservation of the correlations therefore implies approximate conjugation of many involutions. A conjugacy-class spectral gap lets a large set of accurately conjugated involutions determine the whole group. Discrete rounding, an averaged intertwiner, and the invariant cubic then identify a nearby **single Monster operation**.

The general robust-normalizer lemma in the latest note is not specific to the Monster. Its assumptions and proof are separated from the Monster-specific tensor and group inputs.

## Read in this order

Start with [STATUS.md](STATUS.md), then the main statements and general lemma in [the latest normalizer-rounding note](research/05_normalizer_rounding.md). The five chronological notes are preserved as a proof-development record:

| Note | What it supplies | Important boundary |
|---|---|---|
| [01 — Local rigidity](research/01_local_rigidity.md) | Exact local sensitivity of a Griess cubic probe | Prior small-error promise |
| [02 — Pair correlations](research/02_pair_correlations.md) | Bipartite probe, exact stabilizer, channel spectrum, parent gap | State certification is not gate certification |
| [03 — Uniform axis rounding](research/03_uniform_axis_rounding.md) | First explicit global gate theorem | Old $10^{-25}$ sufficient threshold |
| [04 — Average transport](research/04_average_transport.md) | All-error ensemble transport and independent-device agreement | Matching initially need not be a Monster action |
| [05 — Normalizer rounding](research/05_normalizer_rounding.md) | Average-to-one-symmetry rounding and improved gate thresholds | Still not a practical or novelty-cleared protocol |

Earlier notes are unchanged and may describe a then-unresolved issue that a later note addresses. The current claim ledger, not the last paragraph of an old checkpoint, is the status authority.

## Other retained results

The pair state is $\sigma=P/d$, where $P=WW^\dagger$ is the rank-$d$ range projector of the normalized multiplication isometry. Both one-register marginals are maximally mixed. The same spectral data yield a unique three-register parent ground state with exact projector-normalized gap $11161/13858$.

The all-error real-orthogonal transport bound remains

$$\epsilon(O)/4\le\mathsf W(O)^2\le\min\{2,154\epsilon(O)\}.$$

The new result relates this to one symmetry under an explicit sufficient condition:

$$\mathsf W(O)^2\le3\times10^{-9}\quad\Longrightarrow\quad
D_{\mathbb M}(O)^2<106\mathsf W(O)^2.$$

For two potentially different fixed unitary devices, the pair test also gives

$$\min_\theta\|U-e^{i\theta}V\|_F/\sqrt d
\le2\sqrt{\epsilon(U,V)/\Delta}.$$

Exact preservation forces the same Monster element on both factors, up to their independent phases. None of these statements covers arbitrary noisy channels or device-independent self-testing.

## Reproduce the recorded checks

The exact checker uses only the Python standard library. The small-example and earlier numerical checks additionally require NumPy. The recorded environment is Python 3.13.5 and NumPy 2.3.5; neither is a mathematical assumption.

```sh
python checks/verify_normalizer.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python checks/verify_normalizer_toy.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py
```

The root verifier checks the preserved license and original seed, validates the current snapshot and preserved imports, runs both new verifiers under normal Python, `-O`, and `-OO`, and replays six earlier scientific verifiers in temporary directories under normal Python. It never edits a preserved checkpoint. Reports are compared to the recorded outputs; a difference is reported rather than silently overwriting evidence. Floating-point portability differences, if any, require inspection and are not automatically a mathematical failure.

The new checks use no matrix larger than $60\times60$. Historical toy checks include a $256\times256$ matrix. No full Monster matrix or multiplication tensor is generated.

## What a repository is for now

The next work is [the proof/priority audit](work_orders/CURRENT.md), not an unbounded expansion of speculative applications. The main goals are to independently check the assembled argument, identify exactly which statements are new relative to the algebra and stability literature, and determine whether probe access has a credible resource model.

Maintain [AGENTS.md](AGENTS.md) across workspaces. Preserve the original checkpoint archives, distinguish imported theorems from project deductions, and record changes with their affected claims and verification scope.

## Provenance and license

The original four archives and four readable notes are retained byte-for-byte; see [the import manifest](provenance/import_manifest.json). The character excerpt is a declared transcription from a pinned ATLAS-derived GAP source, not the full original source file. Its provenance is included in the JSON and research notes.

Canonical repository: [GoGoKo699/Monster-Correlation-Rigidity](https://github.com/GoGoKo699/Monster-Correlation-Rigidity). The original MIT [LICENSE](LICENSE), Copyright (c) 2026 Ruge Lin, is preserved unchanged from the owner's initial commit. All five research notes, all original scientific checks and recorded reports, and the four checkpoint archives retain their seed bytes. The complete original seed is also preserved. See [the repository-import record](provenance/repository_import.json) and [COPYING.md](COPYING.md).
