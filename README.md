# Carbon project methodology due diligence: evidence and scenario risk

**An independent, research-grade computational companion**, authored by Ravindu Nawanjana. Carbon methodology evidence ledger, transparent assumptions, deterministic sensitivity and seeded Monte Carlo.

> **READ FIRST:** Numerical examples in this repository are **ILLUSTRATIVE SCENARIOS**, not field observations, verified emissions, project registrations, corporate work products, market rates, issued offsets or actual project financial results. Original source drafts remain private; this repository has no implied institutional endorsement.

## Project scope

**Languages and tools:** Python · Jupyter · Quarto. Model core in typed, stdlib-only Python; Quarto is a reproducible report; Jupyter notebooks are included only where exploration materially improves model transparency.

**Source documents:** `check list for baselin in CCR.docx`, `Individual Carbon Credit Value Development Activities | Ravindu Nawanjana.docx`, `Estimated carbon credits using only crop rotation....docx`, `Carbon Credit Price Comparisons for projects under VM0042 and VM00051 | Ravindu Nawanjana.docx`. See [the source audit](docs/SOURCE_REGISTER.md) for relevant authoritative links and limitations.

**What is built:** a documented input contract; tested computational engine; controlled illustrative examples; explicit uncertainty/sensitivity tools; reproducible tabular outputs; Quarto research narrative; GitHub Actions verification; citation and rights records.

## Research boundary

**Not verified:** Historic 10.8 tCO2e/ha/year planning assumption and US$70/credit quotation are unverified, not certified outcomes or current prices. Replacing toy input assumptions with undocumented figures is not a defensible improvement. Record source, measurement year, denominator, geospatial boundary, ownership and permission before changing a scenario to *observed*.

## Quick start (Python 3.10+)

```bash
python -m venv .venv
# Activate .venv with your shell-specific command.
python -m pip install -e '.[dev]'
python -m pytest
python scripts/run_all.py
python scripts/create_figures.py
```

Then install [Quarto](https://quarto.org/) and run `quarto render` to build the research companion in `_site/`. The rendered report is an auditable explanation of the model, not independently verified results. GitHub Actions automates tests and rendering. Run from the project root. For Jupyter: `python -m pip install -e ".[notebooks]"` and open `notebooks/exploratory_analysis.ipynb`.

## Read the repository like a research paper

1. [Research question and research agenda](docs/RESEARCH_AGENDA.md).
2. [Source register and provenance](docs/SOURCE_REGISTER.md).
3. [Units, data dictionary and model card](docs/DATA_DICTIONARY.md).
4. [Computational reproducibility protocol](docs/REPRODUCIBILITY.md).
5. [Methodology and limitations](reports/methods.qmd) and [worked analysis](reports/analysis.qmd).
6. [Rights and public-release review](RIGHTS_AND_USE.md).

## Repository tree

```text
src/                 Pure quantitative logic; reusable, testable
scripts/run_all.py   Single command to reproduce illustrative outputs
data/illustrative/   Demonstration inputs, never field measurements
data/templates/      Blank structured collection tools
tests/               Known-value, edge-condition and validation tests
reports/             Quarto research narrative
.github/workflows/   Automated tests and report build
outputs/             Locally generated tables; ignored by Git
```

## Worked example and quantitative results

[Open the generated illustrative results table](docs/ILLUSTRATIVE_RESULTS_PREVIEW.md) to inspect the calculations without installing anything. Every displayed quantity is a hypothetical scenario.

## Evidence-to-code crosswalk

The [claim-level evidence crosswalk](docs/EVIDENCE_CROSSWALK.csv) maps individual statements in the source materials to their status, how the code treats them, and what primary evidence would be required to upgrade them. **Draft source statements are not independently verified facts.**

## Interpretation and reuse

The analysis **cannot** confer Verra/CDM eligibility, demonstrate GHG additionality, prove operational implementation, validate a corporate or event inventory, or guarantee commercial/regulatory outcomes. The research question is primarily whether analytical assumptions can be made explicit, tested, and revised as evidence arrives. For public reuse and distribution terms see [RIGHTS_AND_USE.md](RIGHTS_AND_USE.md); no unrestricted licence has been applied.
