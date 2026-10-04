# Proposal: observed-trajectory specificity versus measurement-selection after TACE

## Episode, parent, and scientific deliverable

This episode-8 child evolves assessed parent [prior hypothesis]. It retains the validated day-45 landmark, exclusion/reporting of early liver-directed actions, competing recorded-care outcomes, capture controls, pre-index placebo, and transparent-versus-latent comparison. The substantive repair is to make measurement selection an explicit scientific uncertainty rather than treating the paired-biomarker population as transportable by default.

The solver must newly construct two linked manifests and fit prespecified models. Required outputs must report (i) the post-TACE trajectory association among patients with a paired observed trajectory and an eligible day-45 risk set; (ii) the full eligible index-population association of trajectory availability/missingness and observed trajectory categories; (iii) observation-adjusted and complete-follow-up sensitivities; (iv) competing cumulative incidences and calibration/log-score uncertainty; and (v) an interpretation map that forbids transport or clinical-response claims when selection diagnostics fail. Discovery has not solved the hypothesis.

## Unresolved question and falsifiable hypotheses

After TACE, clinicians decide whether early findings are compatible with routine surveillance or should prompt reassessment for additional liver-directed treatment. The strongest claim supported by the inspected local evidence is only that the frozen HCC snapshot contains dated TACE-like procedures, structured HCC diagnoses, AFP and hepatic-proxy laboratory rows, examination timing, and later recorded procedures. A bounded audit found 19,496 patients with a first TACE-like index; 15,605 had another procedure during days 0–45, 1,468 had a first TACE-like and 1,491 an alternate liver-directed procedure in days 46–365, and 4,524 had an encounter at least 365 days after index. These are feasibility/ascertainment facts, not response findings.

Primary observed-trajectory hypothesis H1: among adults with a structured HCC diagnosis, a first TACE-like index, no subsequent liver-directed procedure through day 45, and a paired numeric early trajectory, an AFP improvement plus non-deterioration in at least two prespecified hepatic proxies is associated with lower 46–365-day cumulative incidence of a first recorded liver-directed action after adjustment for day-45-known observation opportunity. The association is stronger for liver-directed than non-liver recorded procedures and weaker for a pre-index placebo trajectory.

Measurement-selection hypothesis H2: in the full eligible index population, paired-trajectory availability and day-45 encounter/laboratory opportunity are themselves associated with subsequent recorded action; after these variables are modeled, the H1 contrast is attenuated, non-specific to non-liver actions, or unstable if the apparent signal is primarily measurement/care capture rather than disease-linked information. H2 is a falsification/transport test, not proof of absence of biological signal.

These are prognostic associations with recorded care. A recorded action is not recurrence, viable tumor, treatment failure, treatment benefit, or a recommendation. Decision relevance is limited to whether a local EHR trajectory could justify a prospective reassessment trigger; it cannot establish that acting on it improves outcomes.

## Population, exposure, outcomes, and time

Use one index per patient. In the procedures table, define a TACE-like row as case-insensitive TACE, a name containing 动脉化疗栓塞, or a name containing both 肝动脉 and 栓塞; collapse qualifying rows within 24 hours and anchor the earliest 开始时间. Join encounters and diagnoses on (患者主索引, 就诊号), require age >=18 and nonmissing sex, and require 诊断名称 containing literal 肝细胞癌 in a joined encounter from 180 days before through 7 days after index. Use index dates through 2025-01-01 for the one-year horizon.

A day-45 risk set excludes a procedure after index+24 hours through day 45 whose name is repeat-TACE-like or alternate liver-directed. The early pathway is reported separately, not silently labeled a later non-event. Alternate liver-directed names contain 切除, 消融, 射频, or 微波, excluding TACE-like. The competing 46–365 outcomes are first repeat TACE-like, first alternate liver-directed procedure, and first non-liver procedure as a capture control. Report each category, combined liver-directed action, and cumulative incidence. A non-event is never called treatment success.

For AFP use the last parseable numeric value in days -30 to -1 and the first in days 7–45; define z=log1p(AFP) and AFP improvement as z_post <= 0.5*z_pre, retaining continuous change, qualitative/assay flags and missingness. For albumin, total bilirubin, 凝血酶原时间比值, and platelets use last pre-index and first early-post values. Non-deterioration is early >= pre for albumin/platelets and early <= pre for bilirubin/coagulation ratio. Do not call the observed assay INR, pool assays, compute ALBI/MELD, or use units, because no lab-unit field is available.

The paired estimand is H1 among the complete prespecified paired trajectory and landmark population. The full-index estimand includes every eligible index patient who reaches the day-45 landmark: model trajectory-availability indicators, counts and timing of assay/encounter opportunity, and an explicit missing-trajectory category; do not impute an unobserved biological response and do not call the full-index missingness contrast a transported response effect. A training-only stabilized inverse-probability analysis may estimate a transported observed-trajectory contrast only if positivity, weight overlap and calibration diagnostics pass; otherwise report transport as inconclusive.

Define local observation time as the latest dated joined encounter (admission, visit or discharge time) and censor at the first day after last observed local contact or day 365, whichever comes first, unless an action occurs first. Fit censoring models only on training data using baseline and day-45-known capture features, report overlap/truncation, and repeat in the selected stable-ascertainment subset with an encounter on/after day 365. No death or outside-care event is imputed.

Use the same pre-index placebo windows (days -120 to -91 and -90 to -46), without calling it response. A comparable placebo association or comparable non-liver-control association supports generic prognosis/capture rather than post-TACE disease specificity.

## Exact source bindings

All source data are read-only, ordinary CSV files in HCC snapshot [source checksum]; no archive member is used.

- encounters, datasets/hcc/table-b743286cb1249287.json, source [internal dataset path], [source checksum]. Required: 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室.
- procedures, datasets/hcc/table-d5eae16f8f8093d9.json, source [internal dataset path], [source checksum]. Required: 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源.
- diagnoses, datasets/hcc/table-12710723c3df0c99.json, source [internal dataset path], [source checksum]. Required: 患者主索引, 就诊号, 诊断名称, 诊断类型; diagnosis time comes only from joined encounter.
- labs, datasets/hcc/table-38aad8c54471332f.json, source [internal dataset path], [source checksum]. Required: 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间.
- examinations, datasets/hcc/table-fd016d2731b9d6c6.json, source [internal dataset path], [source checksum]. Required: 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 检查号. Use timing/counts/opportunity only; narrative lexical findings are an unvalidated sensitivity.
- Optional orders, datasets/hcc/table-6b93dcf0ea823702.json, source [internal dataset path](非药品)_2062526727266216118.csv: use only dated order/capture features from 开立时间, 开始时间, 结束时间; an order is not completion.
- clinical_documents and pathology have no temporal columns and are excluded from dated prediction. Identifier-only vitals, transfers, and front_page add no payload.

The solver must verify all hashes/schema hashes at runtime and preserve filtering counts, vocabulary audit, and raw-name audit.

## Models, baseline, alternative, and method selection

All models use the same patient-level splits, outcome definitions, censoring rules and locked test.

B0 is a regularized competing-risk discrete-time hazard model using age, sex, department/procedure-family, pre-index diagnosis/history and procedure counts, pre-window assay values/missingness, and day-45-known observation features. B1 adds the frozen AFP/hepatic trajectory and continuous changes in the paired estimand. B2 adds assay availability, encounter days, lab row/day counts, examination opportunity/timing/counts, non-liver procedure counts, plus an all-index missingness/availability version; censoring weights are fit on training data only.

M3 is a substantive irregular-time low-rank state-space model with AFP-informed latent activity and hepatic-function states, patient random intercepts/slopes, assay-specific informative-observation submodels, missingness/measurement intensity, and competing action hazards. Estimate the day-45 latent state using past data only and output posterior state/slope uncertainty.

B0/B1/B2 answer whether a transparent prespecified phenotype adds observation-adjusted information and whether that information survives an all-index selection audit. M3 can reveal whether asynchronous biomarker shape and informative measurement timing explain action-specific association that thresholds and missing categories lose; it cannot recover unmeasured tumor burden or access. A transformer adaptation is deferred because this single-site recorded-action endpoint makes observation identifiability and vocabulary auditing more scientifically informative than extra sequence capacity. The natural-history demonstration supports dated sequence learning but its Danish validation and complete disease histories are unavailable. The cancer demonstration's main article and full STAR Methods are unavailable and image files are absent; its lab/EHR idea is adapted only as B1/B2/M3. The Bayesian demonstration supports latent longitudinal modeling, but genetic inputs are unavailable and no genetic analysis is proposed. The expert-seed catalog contains no HCC seed, so non-HCC seeds are not forced onto this island.

## Splits, uncertainty, falsification, and interpretation

Primary split is by index date: 2010–2022 fit, 2023 tuning, 2024–2025-01-01 locked test; no patient crosses splits. If support fails, use deterministic participant-hash buckets and record the fallback. Freeze parsing, imputation, model settings, weights and vocabulary before locked-test outcomes. Use patient bootstrap or a declared robust interval method, with weight diagnostics and competing-risk prediction uncertainty.

Supportive evidence for H1 requires the locked-test observed-trajectory liver-directed contrast in the prespecified lower-risk direction with a 95% interval excluding null, stronger than the non-liver control and pre-index placebo, stable under literal vocabulary and 90/180-day sensitivity, and less than 30% attenuation after B2/IPCW. Support for a transported claim additionally requires acceptable positivity/overlap, stable weights, and concordant all-index availability analysis. M3 must improve mean log score by at least 0.02 without worse calibration to count as an informational, not merely predictive, advance.

Adverse evidence is reversal/null, strong attenuation after capture adjustment, comparable liver and non-liver associations, placebo as strong as post-index, unstable weights or complete-follow-up sensitivity, early-action/competing-action reversal, or M3 nonconvergence/calibration failure. An availability-only association with no robust trajectory contrast supports a measurement-selection explanation.

Inconclusive evidence includes too few paired risk-set patients/events, high local-loss censoring, failed positivity, sparse incomparable assays, uncertain procedure vocabulary, or unstable/failed M3. A supportive result establishes only a reproducible local recorded-care association and possibly a prospective reassessment hypothesis. It does not establish response, recurrence, causality, treatment benefit, survival, utility, or external validity. Those require expert radiology/pathology adjudication, treatment intent, units, mortality/outside-care linkage, an external institution, and prospective evaluation.

## Required artifacts and compute

Required outputs are index_manifest.csv, landmark_manifest.csv, split_manifest.csv, predictions.parquet, metrics.json, bootstrap_intervals.json, procedure_vocabulary_audit.csv, early_pathway.csv, availability_selection.csv, examination_proxy_audit.csv, observation_specificity.csv, negative_control.csv, weight_diagnostics.json, interpretation.json, and limitations.csv, carrying snapshot/schema hashes and filtering counts. Completion requires fitted coefficients and latent parameters, cause-specific predictions/cumulative incidences, calibration/log-score intervals, all-index and paired-estimand outputs, and an interpretation-to-output map.

The prior measured audit read all 105,044 encounter rows and 338,040 procedure rows in 3.27 seconds on a managed 8-CPU/32-GiB job; it is a feasibility diagnostic, not a solved result. Planned future solver envelope is up to 16 CPUs, 262,144 MiB, 8 GPUs and 28,800 seconds. B0–B2 should fit on CPU; M3 should first use sparse CPU fitting and may use one allocated A100 (inside the job, cuda:0) only if repeated optimization materially benefits. Full preprocessing, M3 convergence and bootstrap duration remain unverified. No GPU is required and no proposer/solver weights are trained.
