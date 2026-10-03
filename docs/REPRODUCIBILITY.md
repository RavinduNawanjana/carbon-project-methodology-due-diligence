# Reproduction and scientific-computing protocol

Run from the repository root. Keep input templates distinct from illustrative demonstrations. Python modules intentionally use only the standard library for core arithmetic, avoid mutable global parameters, reject inconsistent physical units and raise explicit errors for negative/nonfinite quantities. The automated workflow starts with isolated unit tests, then runs examples and renders the Quarto report. R code, where used, must be executed in an R-enabled environment; no R results are asserted without execution logs.

**Provenance of outputs:** numerical tables under `outputs/` are generated and ignored; release any outputs only with their exact input files, software versions and source dates. Fixed random seeds do not remove model uncertainty or confer empirical status on results.

## Execution and evidence checklist

1. Clone the repository and install only documented runtime requirements.
2. Run tests before generating tables, recording versions and the clean commit SHA.
3. Verify the input data status and source document dates; do not promote an illustrative record to an observation without independent evidence.
4. Compare outputs with known dimensional or accounting identities and any externally reported target **without fitting to the target**.
5. Render the Quarto pages and inspect figures for consistent units and claims.
6. Retain outputs, runtime logs, run date and links to primary evidence when making a substantive claim.
