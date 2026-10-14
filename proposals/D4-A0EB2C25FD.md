> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repair: fat-distribution divergence versus rival explanations

## Proposed relationship

At comparable total body adiposity, higher visceral fat and higher posterior-thigh muscle-fat infiltration (MFI) may identify different subsequent clinical trajectories: visceral fat may be more specific to incident metabolic disease, while MFI may be more specific to later functional limitation or falls. This is a provisional hypothesis, not an observed result. The substantive question is whether body-composition distribution contains clinically useful information that total adiposity alone loses, rather than merely whether a more complex model predicts better.

## Evidence and uncertainty boundary

The parent candidate links inspected evidence that myosteatosis/MFI is associated with metabolic and functional outcomes, that IMAT/MFI evidence is heterogeneous across imaging and disease contexts, and that UKB abdominal MRI phenotypes including visceral fat improve internal prediction of incident T2D. Those findings motivate the question but do not establish divergence, causality, or clinical utility. No new association, event count, model estimate, or clinical conclusion has been computed in this branch. The key works and frozen receipts are inherited from the parent and must be rechecked before final selection.

## Rival explanations to stress-test

1. **Baseline severity:** people with more visceral fat or MFI may already have subclinical metabolic disease, inflammation, frailty, or other severity. The test must exclude prevalent disease where identifiable and report baseline disease, comorbidity, and functional status; a result that disappears after prespecified severity adjustment is adverse to the divergence claim.
2. **Measurement timing:** MRI, diagnosis, and repeated functional measurements may occur at different assessment instances. Time zero must be explicitly defined at the second assessment, with outcomes strictly later and a prespecified lag. Date-only or instance-only ordering must be labeled as a limitation; no-lag and longer-lag analyses are sensitivity checks, not replacements for the primary temporal estimand.
3. **Selection into MRI:** MRI participation is not random and may select healthier, more affluent, or more symptomatic people. The analysis must report MRI-eligible versus MRI-participant characteristics, missingness by key covariates, and selection-weighted or overlap-restricted sensitivities only if the available fields support them. A result confined to a highly selected MRI subset is not generalizable.
4. **Outcome ascertainment:** incident disease may be coded differently over time, and falls/repeated functional measures may be measured only in participants who remain available. The study must distinguish coded incident outcomes from prevalent codes, report follow-up/ascertainment support, and avoid treating missing later measurements as normal. Falls and functional decline require explicit ascertainment definitions; if dates or event support are unavailable, defer that endpoint rather than infer it.

## Data-bound experiment (provisional, pending exact schema verification)

Use only UK Biobank `eid` within the documented UKB namespace. The parent identifies candidate read-only Parquet views for MRI/body-composition fields (`53-2.0`, `21085-2.0`, `23355-2.0`, `23356-2.0`, `23099-2.0`, grip/fall fields `46/47` and `2296`), diagnosis codes/dates (`41270-0.*`, `41280-0.*`), and demographics (`31-0.0`, `34-0.0`, `21022-0.0`). The exact catalog paths, archive members, columns, and source hashes must be re-inspected before execution; naming these fields is not a result.

Population: participants with valid baseline total adiposity, visceral fat, and posterior-thigh MFI at the second assessment, identifiable baseline index, and required covariates. Exclude prevalent metabolic disease and baseline functional limitation/falls where identifiable. Preserve source-specific identifiers and do not join incompatible namespaces.

Primary comparison: a simple total-adiposity model versus a prespecified composition model adding visceral fat and MFI, with age, sex, ethnicity, and measurement timing as covariates. The scientific output is outcome-specific contrast estimates and uncertainty, not only predictive gain. A held-out temporal split and calibration/overlap diagnostics are required. A learned sequence model is deferred unless repeated functional measurements and temporal support are verified; it could reveal nonlinear or time-varying decline patterns that a single cross-sectional composition contrast loses, but it is not needed to answer the primary question.

## Falsification and interpretation

Supportive: visceral fat and MFI show prespecified, outcome-specific associations with uncertainty excluding the null after total-adiposity and severity adjustment, with stable direction under timing, selection, and ascertainment sensitivities. This supports distinct descriptive risk phenotypes, not mechanism or treatment benefit.

Adverse: composition adds no stable outcome-specific information, effects reverse, or the pattern is explained by baseline severity, MRI selection, measurement timing, or outcome ascertainment.

Inconclusive: sparse events, poor overlap, missing dates, unstable calibration, or wide uncertainty. This motivates a larger or differently ascertained study.

Causal, mechanistic, and treatment claims require additional longitudinal/interventional evidence, clinical adjudication, and covariates not guaranteed by the available files.

## Actual deliverable and next checks

The future solver must newly estimate cohort/overlap counts, temporally ordered event counts, baseline and composition-model contrasts with uncertainty, calibration/selection diagnostics, and classify the result as supportive, adverse, or inconclusive. Immediate next checks are exact catalog/schema verification, date and endpoint availability, and a bounded missingness/selection diagnostic. No computation is claimed here.
