# Reproduce the current research package

[Overview](../README.md) · [Current status](RESEARCH_STATUS.md) · [Archive index](ARCHIVE.md)

## The current command

From the repository root, run:

```sh
python verify_current.py
```

This standard-library-only suite checks current file integrity, the selected
extraction proof's finite certificate, the calibration/sharpness certificate,
the adversarial core controls, the scale regressions, and active documentation.
Each checker runs in normal Python, `-O`, and `-OO`. Differences between those
outputs or a mismatching current exact fingerprint fail the command.

The recorded environment is **Python 3.13.5**. A virtual environment is recommended
but no third-party package is needed for this default command.

## The complete inventory and the historical comparisons

For the original NumPy-based small examples as well:

```sh
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-reproduce.txt
python verify_current.py --all
```

Use Python 3.13.5 when an exact match to the recorded interpreter is needed.
The dedicated requirements file pins NumPy 2.3.5. The original `requirements.txt`
is retained for historical compatibility; it is not the pinned reproduction file.

`--all` runs every current checker entry point, then reports historical
`verify.py` byte replay and the unchanged bounded-portability comparison
**separately**. NumPy and interpreter pins do not guarantee identical floating
point on every operating system, processor, or numerical backend.

| Outcome | Meaning | Default exit code |
|---|---|---:|
| Current exact/documentation suite passes | The selected code and finite certificates match their current records. | 0 |
| Known historical floating-report mismatch, bounded portability passes | Current checks passed; historical strict replay still failed. The JSON status explicitly reports both. | 0 |
| Current failure, changed exact fingerprint, unexpected historical failure, or failed bounded comparison | Investigation is required; no tolerance is automatically relaxed. | 1 |

For a strict archival gate instead, run:

```sh
python verify_current.py --all --require-strict-replay
```

That command returns nonzero for **any** failed historical strict replay,
including the known floating-report mismatch. It never relabels a bounded
comparison as strict equality.

Save individual stdout/stderr and a summary outside the checkout with:

```sh
python verify_current.py --all --output ../monster-verification
```

The output directory must be outside the repository, so verification cannot
silently alter a tracked source or manifest. The wrapper has bounded subprocess
timeouts and reports an exception or timeout as failure.

## Which fingerprints should match?

[Current report metadata](../results/current_reports.json) describes the current
implementation. The earlier report manifests are frozen evidence of earlier
commits, not assertions that every formatted document or repaired implementation
has the same bytes today. The [release manifest](../results/release_preparation.json)
records intentional source changes and all preserved files.

The square-root repair refines rational enclosures in the calibration report;
its current output is deliberately recorded separately from the older 74-check
output. The original logical checks remain. The extraction certificate retains
its original fingerprint. [The erratum](../audits/calibration_scale_erratum.md)
explains the change and its regression family.

## Mathematical rendering

The default command checks fenced/inline math extraction, delimiters, local
links, parser controls, and the expected expression inventory. CI additionally
parses the exported expressions with the existing MathJax 3.2.1 checker:

```sh
python checks/verify_display.py --export-math ../monster-math.json
npm install --prefix ../monster-renderer --ignore-scripts --no-audit --no-fund mathjax-full@3.2.1
NODE_PATH=../monster-renderer/node_modules node checks/render_math.cjs ../monster-math.json
```

This is syntax checking, not a promise about every GitHub browser, screen size,
or historical page. The [archive index](ARCHIVE.md) identifies legacy rendering
boundaries. No MathJax package, generated website, paper, or font is bundled.

## Evidence boundary

These programs check arithmetic, finite examples, implementation behavior,
source integrity, and documentation. They do not prove the imported VOA
classifications, simulate the full Monster tensor, establish practical
measurement complexity, or constitute independent human review.
