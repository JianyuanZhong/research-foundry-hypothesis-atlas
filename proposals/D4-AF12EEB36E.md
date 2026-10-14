> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: body-fat distribution separates metabolic from functional/fall trajectories

## Status and scientific deliverable

This is a provisional, data-bound hypothesis, not an observed result. The deliverable is a newly fitted, held-out comparison of a simple total-adiposity baseline with a prespecified body-composition model. It tests whether visceral fat and posterior-thigh muscle fat infiltration (MFI) identify distinct subsequent metabolic and functional/fall trajectories. Completion requires cohort and overlap counts, a temporally ordered event table, fitted estimates with uncertainty, held-out calibration/discrimination or trajectory summaries, and a conclusion classified as supportive, adverse, or inconclusive. No association or clinical conclusion has been computed in this episode.

## Proposed relationship and unresolved question

At similar total body fat, does higher visceral fat predict subsequent metabolic disease more specifically, while higher posterior-thigh MFI predicts subsequent functional decline or falls more specifically? This matters because separating these phenotypes could justify targeted body-composition assessment rather than treating adiposity as one generic risk factor. A positive result would support outcome-specific assessment; a negative result would challenge separating these phenotypes for clinical risk stratification. The substantive advance is a temporally ordered, same-cohort test of outcome-specific divergence, rather than a generic association or incremental diabetes-prediction model.

## Evidence boundary and closest inspected work

The available evidence supports only that myosteatosis/MFI is associated with metabolic and functional outcomes [K1], that intermuscular adipose tissue/MFI spans metabolic, cardiovascular and oncologic settings but is heterogeneous across imaging and disease contexts [K2], and that UK Biobank abdominal MRI phenotypes including visceral fat improve internal prediction of incident type 2 diabetes [K3]. These works do not establish the proposed divergence, causality, or clinical utility. The UK Biobank seed and schema checks provide a data opening, not a result.

## Population, timing, variables and outcomes

Use UK Biobank participants with valid second assessment (53-2.0), complete baseline MRI composition at that assessment, and no prevalent metabolic disease using diagnosis arrays available before or at baseline. Time zero is the second-assessment date. Primary exposures are standardized visceral fat volume (21085-2.0), mean left/right posterior-thigh MFI (23355-2.0 and 23356-2.0), and body-fat percentage (23099-2.0). Covariates are sex (31-0.0), age/birth year (34-0.0), ethnicity (21022-0.0), baseline grip (46/47), and available medication/activity fields. Exclude prevalent metabolic disease and baseline functional limitation/falls where feasible.

The primary metabolic outcome is incident type 2 diabetes (E10/E11) after a prespecified lag; secondary outcomes include broad metabolic disease and diabetes subtypes. The primary functional outcome is grip-strength decline from assessment 2 to 3; secondary outcomes are new falls (2296) and incident musculoskeletal/fracture diagnoses, interpreted cautiously because falls are self-reported and fracture capture is incomplete. Use a one-year lag as the primary analysis, with no-lag and longer-lag sensitivity analyses.

## Exact data bindings and verified feasibility

The read-only Parquet views are:
- datasets/population_multiomics/table-6fc0a334db7f533b.json: [UKB data file], 502,370 rows, eid, assessment/MRI/functional fields;
- datasets/population_multiomics/table-03f57283ab9ae48b.json: [UKB data file], 502,370 rows, eid, 41270-* diagnosis codes and 41280-* dates;
- datasets/population_multiomics/table-674bd55f4152a860.json: [UKB data file], 502,370 rows, eid, sex, birth year and ethnicity.

Join only on eid within this UKB namespace. The source catalog records hashes [source checksum], [source checksum], and [source checksum] for these views. A prior managed diagnostic found 36,320 complete second-assessment MRI/total-fat participants. Post-baseline code-specific counts were E10 65, E11 729, M16 628, M17 757, M18 65, M19 1,332, M25 531, M54 754, S72 133, S82 119, S42 98, S52 227, and T17 3. These are feasibility counts, not hypothesis results.

## Baseline, alternative and analysis

The simple baseline is a penalized logistic/Cox model with age, sex, ethnicity, body-fat percentage, baseline grip and medication/activity indicators. The substantive alternative is a composition model adding visceral fat and MFI, with a prespecified exposure-by-outcome interaction and separate outcome models. It can reveal whether fat distribution carries information lost by total adiposity and whether the two exposures have different outcome-specific contrasts. Fit within participant-level train/test splits, with preprocessing and feature selection inside training folds. Report standardized contrasts, 95% confidence intervals, calibration slope/intercept, Brier score, C-index/AUC, and bootstrap or cluster-robust uncertainty.

A learned trajectory model (regularized multistate or recurrent model using repeated grip/falls) is deferred: it could capture time-varying functional trajectories lost by a single-change model, but current event support and missingness make its added complexity scientifically uninterpretable without a prespecified validation target. Revisit only if the composition model shows reproducible residual temporal structure. The selected CPU tabular design is feasible within the solver envelope; no GPU is required.

## Falsification and interpretation

Supportive: visceral fat has a positive metabolic contrast and MFI has a positive functional/fall contrast, both remain directionally distinct after lag, selection and baseline-function checks, with credible intervals and acceptable held-out calibration. Adverse: contrasts are absent/reversed, or composition adds no information beyond total adiposity and demographics; this challenges the proposed divergence. Inconclusive: sparse events, unstable estimates, poor calibration, or large missingness/selection differences; this does not refute the hypothesis. A supportive association would not establish mechanism or treatment benefit. Causal claims require longitudinal biomarkers, treatment data, residual-confounding analysis or a prospective intervention study. Clinical adjudication is needed for fall/fracture validity and for interpreting medication and activity data.

## Demonstration dispositions and method record

The natural-history/Delphi demonstration is not pursued as a reproduction: its dated disease-history sequence is not needed to answer this fat-distribution question, and a sequence model would add complexity without a clear scientific contrast. The Bayesian/ALADYNOULLI demonstration is deferred: latent longitudinal structure could be useful for repeated functional trajectories, but the current design first needs the simpler composition comparison and stronger event support. The Oncoformer demonstration is not applicable because the full multimodal image experiment and main methods are unavailable; a lab-only adaptation would not answer this question. The selected CPU tabular design is feasible within the solver envelope; no GPU is required.

## Key references

[K1] Roe LS, Zmuda JM, Miljkovic I. Myosteatosis: an emerging biomarker of aging. Front Aging. 2026. doi:10.3389/fragi.2026.1868010. Abstract inspected.
[K2] Ding F et al. Intermuscular Adipose Tissue as a Multimodality Quantitative Imaging Biomarker: Evidence Across Metabolic, Cardiovascular and Oncologic Diseases. J Cachexia Sarcopenia Muscle. 2026. doi:10.1002/jcsm.70366. Abstract inspected.
[K3] Peng R et al. Abdominal MRI-Derived Liver, Visceral Fat, and Pancreatic Phenotypes Improve Prediction of Incident Type 2 Diabetes. Diabetes Metab Res Rev. 2026. doi:10.1002/dmrr.70235. Abstract inspected.
