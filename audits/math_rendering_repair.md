# Active-proof mathematics rendering repair

Baseline: `96d3c7011645ace358844d3494eef0bef657d104`.

## Defect and correction

The reported core Q3 formula used a macro rejected by the user's GitHub renderer. The earlier teaching check covered the README and lesson pages but omitted the two canonical proof documents. This explains why that check passed without catching the reported defect.

Both active proofs now use a basic roman distance label instead of the rejected operator macro. Inline formulas formerly written as plain ASCII now have mathematical delimiters, subscripts, Greek symbols, inequalities and roots. Display delimiters occupy their own lines. The calibration formulas are split into shorter displays, with equation labels (1)–(4) in ordinary Markdown rather than explicit TeX tags. The source-history sentence in the calibration note is made past tense to distinguish the original byte-identical import from this formatting revision.

No hypothesis, conclusion, constant, error budget, equation-label reference or research section anchor is intentionally changed. The original numeric-literal multisets are preserved in both documents; this is a transcription guard, not proof of semantic equivalence. The mathematical statements and changed passages were also compared directly with the baseline. All scientific Python, numerical reports, snapshots, historical manifests, archives and LICENSE remain byte-identical.

## Regression coverage

The new display check covers ten active pages: README, seven learning pages, and both canonical proofs. It rejects the reported macro, explicit equation-tag macros, malformed dollar delimiters, unmatched braces, and selected raw mathematical expressions in the proofs. Six negative controls exercise these failures. The original teaching arithmetic, reading-order, self-check and link checks also run on the candidate. The old teaching entry-point delegates to the current display manifest when that manifest exists, so its ordinary command remains usable.

The workflow replays the historical integration and original teaching audits on their frozen trees, without rewriting their evidence. It then verifies every baseline byte outside the four declared edits, checks the new fingerprints and full file delta, and runs the candidate checks in normal, -O and -OO modes. All active-page expressions are additionally parsed with MathJax 3.2.1. The exact scientific reports and strict historical replay remain separate from the unchanged portability comparison.

## Inspection depth

The two edited baseline sources and the original teaching checker/workflow were reconstructed locally with matching source hashes. Local checks parsed 238 mathematical expressions in the two repaired proofs. Local Chromium/MathJax previews of core Q3 and the calibration equations were visually inspected, with no page-width overflow at a 1060-pixel viewport. This is a local rendering inspection, not a claim to have executed GitHub's live browser renderer. Full repository preservation, all ten pages, and scientific replay are checked on the GitHub runner; actual outcomes are recorded in the PR discussion.

Syntax guidance: [GitHub's mathematical-expression documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). The submitted screenshot, rather than a claim about every TeX engine, is the evidence for the rejected macro.

The current formatted-source fingerprints are in `results/math_rendering_changes.json`. Older source manifests remain historical records tied to their original commits. No manuscript, new scientific result, release or unrelated pending branch is included.
