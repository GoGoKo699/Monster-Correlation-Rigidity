# Maintenance scope

Maintain the [correlation criterion](../research/uniform_extraction_core.md),
[sharpness and calibration](../research/sharpness_and_calibration.md), tutorial,
and reproducible certificates. Use [results and assumptions](../docs/RESEARCH_STATUS.md)
as the scientific scope and [AGENTS.md](../AGENTS.md) for repository rules.

Changes should resolve a concrete proof, source, implementation, or documentation
issue. Record intentional source changes and their before/after fingerprints in
the current integrity manifest. Preserve the original license, scientific
records, provenance archives, recorded outputs, and replay tolerances.

Run `python verify_current.py --all` and inspect current checks, strict historical
replay, and bounded portability separately. Imported mathematical results retain
their source attribution.
