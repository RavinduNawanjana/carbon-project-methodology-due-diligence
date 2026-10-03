# Unverified claims, methodology eligibility and risk analysis

## Source-derived claims requiring external substantiation

- The supplied document **Estimated carbon credits using only crop rotation....docx** sets out an *illustrative planning* estimate of 10.8 carbon units/tCO₂e per hectare per year after excluding reduced tillage from an assumed multi-practice stack. It does **not** provide a verified baseline, measured SOC changes, CH₄ fluxes, N₂O fluxes, eligible area proofs or credit issuance record. The number is preserved in `source_claims_to_verify.csv`, **not used as a certified emission-reduction factor**.
- A July 2025 carbon-price draft describes US$70/credit as a purported market benchmark. Its supporting transaction evidence is unverified. The number is logged as a **pricing claim to verify** and **is not used** to estimate revenue or current prices.
- The baseline checklist requests field management records, irrigation evidence, soil tests, proof of historic practice and traceable QA. It is an **evidence acquisition plan**, not proof these records exist.

## Quantification is deliberately non-crediting

The screening identity is `Q = hectares × years × (baseline_proxy − project_proxy − leakage_proxy)` (tCO₂e). A separate reserve proportion produces an arithmetic after-reserve scenario. **It neither measures nor predicts registrable units**: the engine always returns `credit_units_issued = 0` as a code-level disclosure, not a claim about a project registry. Methodology baselines, quantification units, additionality, crediting dates, leakage, uncertainty, non-permanence and programme requirements must be applied under the correct current standard before claiming reductions or removals.

## Monte Carlo scope

The seeded, explicitly illustrative triangular draws are computational demonstrations of *assumed* parameter uncertainty. Percentiles describe the hypothetical sampling distribution of the technical arithmetic conditional on those ranges, not confidence bounds for actual emissions or field-study sampling variability.

## Audit questions

1. Which standard, activity type, project start and methodology version really apply?
2. Which baseline data sources are independently corroborated and dated?
3. Are AWD, tillage, residue, fertilisation and rotation terms non-overlapping?
4. Which emission factors and global-warming potentials are justified for the geography/time period?
5. Are property rights, permission, leakage and permanence evidenced?
6. Has monitoring been independently validated/verified? No such finding is supplied here.
