# Hopf-style presentation integration

Baseline: `7653d6cef036f40db2746b3379e84dc161b18f55`.
Style reference: `GoGoKo699/Hopf-Frame-Compilation` at `231ac31265a02ea4bd63239e364fefc0a239c6a3`, particularly its README and `docs/HOPF_INTERFACE.md`.

## Reader-facing scope

The eight changed Markdown pages are the main README, five physics lessons, and two active proofs. They use native fenced `math` displays, short standalone equations, and compact proof navigation. The paired Taylor expansion is split into two displays; equation numbers remain ordinary Markdown labels. Gaberdiel remains the primary anchor and selected Yamauchi Section 4 material the secondary supplement. The two learning-reference pages are unchanged.

These eight files match the source preview byte-for-byte. The originating preview archive has SHA256 `6210e1877ceed3825bdee1554cabb24cf3828118f49e55e406536170eda0f706`. Its local HTML/CSS and screenshots are not installed on GitHub or bundled in the repository. GitHub controls its own page styling; this change adopts portable source conventions.

`presentation_transform` in the display checker reproduces each changed page from the actual frozen baseline with only four kinds of edits: display delimiters, four README inline expressions, two navigation lines, and the Taylor-display split. The full-source equality check is stronger than comparing only numeric literals. It does not constitute a new proof audit.

## Regression and preservation

The display parser now reads fenced mathematics before discarding ordinary code. It checks every one of the 445 expressions, including 80 displays and 365 inline expressions across ten active pages. Twenty-one negative controls cover malformed braces, unsupported macros, empty expressions, unclosed/mismatched fences, incorrect math labels, and stray delimiters. Eight positive controls check ordinary code isolation, expression ordering, escaped dollars, inline code, GitHub's backtick-inline syntax, and both fence characters. The existing 82 teaching arithmetic/structure checks are retained.

The current [manifest](../results/hopf_style_changes.json) declares eleven modified files and two additions including itself. Beyond the eight Markdown files, only the display checker, quantitative workflow, and snapshot metadata change. Only the README record changes in the snapshot. All other baseline bytes remain unchanged, including scientific Python, mathematical results, historical manifests and audits, archives, LICENSE, the learning-reference pages, and the prior teaching entry point.

Historical integration, teaching, and math-repair checks run on their original frozen checkouts. Current presentation checks run separately against the pre-style baseline. No previous manifest is updated to pretend its original evidence describes a new document version.

## Evidence boundary

Local checks recovered the original eight pages with their prior fingerprints and reproduced the preview exactly. All 445 current expressions parsed using the unchanged MathJax 3.2.1 renderer. The original snapshot and workflow were reconstructed with matching hashes; the new workflow's YAML and embedded Python parsed. The preview HTML passed twenty local Chromium page/viewport cases at widths 1060 and 430: no page-width overflow, renderer error elements, or displayed-equation height above 150 pixels. This is not GitHub's live renderer, and it does not prove every client will render identically.

Network git checkout was unavailable locally. Full tracked-file preservation, current link targets, the unchanged 63/74/23 exact scientific reports in normal/-O/-OO, and strict-versus-bounded historical replay are therefore verified by the actual GitHub workflow. Its results must be read from the PR job logs; an aggregate green status is not a strict-byte-replay claim. Neither saved output nor replay tolerance is changed.

No new scientific assertion, manuscript, release, or unrelated pending branch is included. Manuscript drafting remains on hold.
