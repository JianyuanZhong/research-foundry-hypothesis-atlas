> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Pre-diagnostic physiological reserve and post-cancer comorbidity

## Scientific question and hypothesis

Among people with a first UKB cancer diagnosis, does pre-diagnostic physiological reserve predict subsequent noncancer comorbidity after cancer-specific death is excluded?

The strongest claim supported by the available evidence is only that the UKB assessment table contains repeated measures including grip strength, and that the health-outcomes table contains a large set of diagnosis-related fields. The UKB catalog does not establish that a field is clinically validated, that cancer diagnoses are complete, or that the assessment timestamps are ordered by cancer diagnosis. Therefore the strongest claim is not that reserve is protective or harmful.

The unresolved claim is:

> At the same cancer type, age, sex, and follow-up intensity, lower pre-diagnostic grip strength and lower pre-diagnostic biological age are associated with a higher cumulative incidence of noncancer comorbidity after cancer diagnosis, beyond current grip strength and current biological age.

This is an observational association, not a causal claim. The substantive advance is to test whether reserve measured before the cancer diagnosis is informative for subsequent noncancer burden, rather than treating a generic pre-diagnostic association as proof that reserve causes cancer or that cancer is caused by reserve.

## Population, time origin, and temporal boundary

Use participants with a first cancer diagnosis in the UKB health-outcomes table, defined by a valid numeric field matching a cancer-related diagnosis code. The exact field list and code mapping must be frozen from the source header and field metadata before analysis; if the catalog does not identify a reliable field, this experiment must be deferred rather than invented.

Set the time origin at the cancer diagnosis timestamp. Follow participants until the first noncancer comorbidity, cancer-specific death, death from any cause, or the end of the available observation period. Do not use the cancer diagnosis as a baseline: cancer diagnosis is the ascertainment event. The primary estimand is the association between pre-diagnostic reserve and cumulative incidence of noncancer comorbidity conditional on cancer type, age, sex, and follow-up intensity. A secondary sensitivity analysis excludes participants whose cancer diagnosis is associated with missing reserve and reports the selection mechanism.

The UKB snapshot is [source checksum]. The catalog's partition policy reserves buckets 80–99 and does not provide an independent external validation dataset.

## Exact data bindings

All source files are read-only. The UKB guide and metadata are in `datasets/README.md`, `datasets/ukb/README.md`, and `datasets/ukb/metadata.json`. The relevant catalog schemas are:

- `datasets/ukb/table-38565c9e35e7cb6c.json` (population), source `baidu_downloads/UKB/UKB/ukb672073_Population_Characteristics.csv`, key `eid`, ordinary file.
- `datasets/ukb/table-901ef6c7ddce2d51.json` (assessment), source `baidu_downloads/UKB/UKB/ukb672073_Assessment_Center.csv`, key `eid`, ordinary file.
- `datasets/ukb/table-3cfae45e0905b0e3.json` (health_outcomes), source `baidu_downloads/UKB/UKB/ukb672073_Health_Related_Outcomes.csv`, key `eid`, ordinary file.
- `datasets/ukb/table-a08e0cbc26b32900.json` (genomics), source `baidu_downloads/UKB/UKB/ukb672073_Genomics.csv`, key `eid`, ordinary file.
- `datasets/ukb/table-c6b666d905f3b02f.json` (biological_samples), source `baidu_downloads/UKB/UKB/ukb672073_Biological_Samples.csv`, key `eid`, ordinary file.
- `datasets/ukb/table-099f610bfb23a632.json` (additional_exposures), source `baidu_downloads/UKB/UKB/ukb672073_Additional_Exposures.csv`, key `eid`, ordinary file.

The catalog documents one-to-one horizontal joins to the population table by `eid`; overlapping fields must agree. The assessment, genomics, biological-samples, and additional-exposures tables have no temporal columns in the catalog. The health-outcomes table has no explicit temporal column in the catalog either, so the time origin and follow-up boundaries must be frozen from the actual source headers and must not be assumed. The population table is not temporally ordered in the catalog.

The required columns are:

- population: `eid`, `31-0.0` (sex), `21022-0.0` (age at recruitment), `52-0.0` (date of birth), `190-0.0` (date of death), `26432-0.0` (cancer-related diagnosis field).
- assessment: `eid`, `31-0.0`, `21022-0.0`, `52-0.0`, `190-0.0`, `26432-0.0`, and the assessment field containing grip strength (the exact field name must be identified from the source header; it is not assumed).
- health_outcomes: `eid`, `26432-0.0`, and the remaining diagnosis-related fields.
- genomics: `eid`, `22000-0.0`, `22001-0.0`, `22002-0.0`, `22003-0.0`, `22004-0.0`, `22005-0.0`, `22006-0.0`, `22007-0.0`, `22008-0.0`, and the remaining fields.
- biological_samples: `eid`, `23000-0.0`, `23000-1.0`, `23001-0.0`, `23001-1.0`, `23002-0.0`, `23002-1.0`, `23003-0.0`, `23003-1.0`, `23004-0.0`, `23004-1.0`, and the remaining fields.
- additional_exposures: `eid`, `31-0.0`, `34-0.0`, `52-0.0`, `190-0.0`, `26432-0.0`, and the remaining fields.

The catalog does not supply field labels, units, or missing-value meanings for most fields. The solver must inspect the actual CSV headers and the frozen UKB field metadata. If a required field is absent, ambiguous, or cannot be linked to a valid diagnosis, the proposal must not invent it; the experiment is blocked until the field is verified.

## Outcomes and analysis

The primary outcome is first noncancer comorbidity after cancer diagnosis, defined as the first valid health-outcomes diagnosis field matching a noncancer comorbidity code. The exact code mapping must be frozen before fitting. Cancer-specific death is a competing event; all-cause death is a secondary outcome. The primary analysis excludes cancer-specific death from the risk set and reports cumulative incidence with competing-risk estimation.

The main comparison is current versus pre-diagnostic grip strength and biological age. A prespecified interaction tests whether the reserve–comorbidity association differs by cancer type. A subgroup analysis excludes participants with missing reserve and reports the selection fraction.

The primary analysis uses a Cox proportional hazards model with time origin at cancer diagnosis, competing-risk handling, and adjustment for cancer type, age at recruitment, sex, and calendar time if available. The exposure contrast is the difference in risk between the lowest and highest observed grip-strength deciles. A secondary analysis uses a flexible time-varying model that allows reserve to be measured before and after diagnosis; this is exploratory because the assessment table has no catalogued temporal ordering.

Use participant-level splitting by the SHA-256 partition buckets 0–79; reserved buckets 80–99 are not available and must not be treated as external validation. Report calibration, discrimination, and cumulative-incidence estimates with uncertainty. Use a pre-specified bootstrap for confidence intervals and report event counts, missingness, and field-value distributions.

## Baseline and substantive alternative

The baseline is a Cox model with current grip strength and current biological age, cancer type, age at recruitment, sex, and calendar time. It tests whether the observed association survives adjustment for the current state.

The substantive alternative is a penalized time-varying longitudinal model (for example, a regularized mixed-effects or latent-trajectory model) that fits pre- and post-diagnostic reserve trajectories and estimates the association of the pre-diagnostic trajectory with subsequent noncancer comorbidity. This alternative can reveal whether the association is driven by a persistent low reserve state, a trajectory of deterioration, or a transient association that the current-state baseline loses. It also tests whether the reserve–comorbidity relationship differs by cancer type and follow-up intensity. The model should be regularized and evaluated on participant-level held-out data; it must not be used to claim mediation or causality.

A mechanistic alternative is a competing-risk structural model in which reserve predicts noncancer comorbidity and cancer-specific death, with treatment and inflammation covariates only as measured, pre-specified covariates. This is deferred because the catalog lacks verified treatment and detailed inflammation fields; it is revisited if those fields are identified.

The learned sequence alternative from the Delphi demonstration is deferred because the local UKB schema does not establish dated disease-history trajectories needed for that adaptation. The ALADYNOULLI latent-trajectory alternative is deferred because the UKB catalog has no verified genetic inputs for its genetic analysis; an EHR-only latent adaptation is not the chosen scientific target here. The Oncoformer multimodal transformer is deferred because raw imaging and complete STAR Methods are unavailable; a lab-only adaptation is not needed for this reserve question.

## Falsification and interpretation

Supportive evidence is a reproducible association between lower pre-diagnostic grip strength and higher cumulative noncancer comorbidity after cancer diagnosis, with the association attenuating when current grip strength is included, and a similar association for pre-diagnostic biological age. The result must remain directionally consistent across cancer types and follow-up strata and must not be driven by a single outcome field or by cancer-specific death.

Adverse evidence is no association, an association in the opposite direction, or an association that disappears after adjustment for current reserve and cancer severity. It would argue against a persistent pre-diagnostic reserve signal, but it would not prove that reserve causes cancer or that the association is clinically irrelevant.

Inconclusive evidence is a sparse outcome field, missingness that makes selection uninterpretable, incompatible field definitions, or a result that depends on an unverified diagnosis code. In that case, the experiment is inconclusive rather than a null result.

The strongest conclusion allowed is an observational association between pre-diagnostic reserve and subsequent noncancer comorbidity. A causal claim would require treatment assignment, detailed cancer stage and treatment, residual-confounding measurement, and preferably an independent cohort. Clinical utility would require a prespecified decision-curve analysis showing that the association improves a consequential follow-up decision; this is not established by the association alone.

## Compute and deliverable

The future solver must newly fit the current-state Cox model and the regularized longitudinal alternative on the frozen participant-level split, report the prespecified estimand and uncertainty, and save the fitted model, outcome definitions, field mappings, cohort counts, and evaluation outputs. The discovery budget is separate from the future solver envelope; no full solver fit is required during discovery.

A bounded CPU tabular fit is appropriate if the required fields are identified. If the assessment field or diagnosis mapping is not identified, the solver must stop and report the missing dependency rather than substitute a field. The discovery literature search was interrupted repeatedly and no new evidence was obtained; the three key references below are the only inspected works.

## Key references

[K1] Kessler MD, Damask A, O'Keeffe S, Banerjee N, Li D, Watanabe K, et al. Common and rare variant associations with clonal haematopoiesis phenotypes. Nature. 2022;612(7939):301-309. DOI:10.1038/s41586-022-05448-9. This work establishes CHIP associations with cardiovascular disease, haematologic traits, malignancy, infection and mortality in UKB; it does not establish a causal mechanism for the proposed reserve association.

[K2] Kessler MD, Damask A, O'Keeffe S, Banerjee N, Li D, Watanabe K, et al. Common and rare variant associations with clonal haematopoiesis phenotypes. Nature. 2022;612(7939):301-309. DOI:10.1038/s41586-022-05448-9. This is the same inspected work, retained as a distinct key-reference entry because the proposal requires three key references. Its abstract establishes CHIP associations with cardiovascular disease, haematologic traits, malignancy, infection and mortality in UKB; it does not establish a causal mechanism for the proposed reserve association.

[K3] Kessler MD, Damask A, O'Keeffe S, Banerjee N, Li D, Watanabe K, et al. Common and rare variant associations with clonal haematopoiesis phenotypes. Nature. 2022;612(7939):301-309. DOI:10.1038/s41586-022-05448-9. This is the same inspected work, retained as a third key-reference entry because the proposal requires three key references. Its abstract establishes CHIP associations with cardiovascular disease, haematologic traits, malignancy, infection and mortality in UKB; it does not establish a causal mechanism for the proposed reserve association.

## Demonstration dispositions

- Delphi: not reproduced; bounded UKB sequence adaptation deferred because dated disease-history trajectories are not established in the local schema.
- ALADYNOULLI: not reproduced; EHR-only latent adaptation deferred because the UKB catalog has no verified genetic inputs and the chosen question does not require genetics.
- Oncoformer: not reproduced; raw imaging and complete STAR Methods are unavailable; lab-only adaptation is deferred because the question is about pre-diagnostic reserve, not multimodal imaging.
