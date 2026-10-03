# HCC hypothesis and Harbor experiment

Status: proposed design, not an executed study. This file records the Lead's scientific deliverable and the exact HCC bindings. The bounded counts below are feasibility diagnostics, not endpoint results.

## Scientific opening and hypothesis

The clinically important opening is the boundary between a transient post-embolization laboratory flare and a clinically meaningful loss of hepatic reserve after TACE. The strongest inspected evidence supports three narrower claims: baseline hepatic reserve is associated with post-locoregional-therapy decompensation [K1]; a baseline Child-Pugh/APRI/FIB-4 nomogram can predict an acute post-intervention hepatic-dysfunction label in a small internal-validation cohort [K2]; and liver-function measurements before and five days after TACE can distinguish acute injury patterns [K3]. None of those claims establishes that a within-patient, multianalyte trajectory observed during the first seven days after TACE improves prediction of a later clinical decompensation event beyond baseline reserve and treatment context.

Primary hypothesis: among adult HCC patients with a first recorded TACE in the observable HCC history and no documented decompensation before that TACE, a 0–7-day trajectory dominated by worsening synthetic/renal reserve (total bilirubin, albumin, INR/PT ratio, creatinine and sodium, with platelet count as a portal-hypertension proxy) predicts a new decompensation-coded admission after the index discharge and between days 8 and 90 better than a prespecified baseline-only model. A short-lived AST/ALT rise without synthetic/renal deterioration is the leading rival pattern: it may represent expected hepatocellular injury or measurement intensity rather than impending decompensation.

This is a predictive/descriptive hypothesis, not a causal claim that TACE caused the event or that changing a laboratory value would prevent it. If supported, the substantive advance is evidence that post-procedure surveillance should distinguish a reserve-loss trajectory from an enzyme-only flare and that a simple baseline risk estimate may be insufficient for post-TACE follow-up. It would justify expert review and prospective validation of a small early-warning rule; it would not by itself justify withholding TACE or changing treatment.

The closest relevant work actually inspected is [K1]–[K3]. The novelty claim is deliberately bounded: I did not perform an exhaustive literature review, and this is not a reproduction of any cited paper. The advance is the explicit incremental, held-out test of routine-care multiday trajectories against a baseline comparator and clinically later outcome, in a longitudinal HCC-only source where imaging pixels, exact external dates, assay units and adjudicated outcomes are unavailable.

## Leading explanation and rivals

The leading explanation is early post-TACE loss of effective hepatic reserve: coordinated bilirubin/albumin/coagulation/renal changes should precede decompensation-coded care more specifically than an isolated aminotransferase peak.

Rivals with different predictions are:

1. Baseline severity: patients with poor reserve already have higher event risk; the post-TACE trajectory will add little after baseline labs, diagnoses and prior utilization are included.
2. Surveillance/measurement intensity: patients who are about to deteriorate have more labs and encounters, so apparent trajectory value will disappear after lab-count/timing features and negative-control tests.
3. Treatment selection and technical intensity: procedure subtype, extent and patient selection drive both laboratory change and outcomes. The observational design cannot identify a treatment effect; include procedure-context covariates and do not interpret coefficients causally.
4. Expected transient injury: AST/ALT can rise after embolization without subsequent clinical decompensation. A model whose signal is limited to this pattern should not be described as a reserve-loss mechanism.

The data can separate baseline severity from early trajectory, and can partially test measurement intensity and enzyme-only alternatives. It cannot identify ischemia, embolic territory, drug dose, inflammatory mechanism, or causal treatment harm.

## Exact population, temporal boundaries and estimands

Use only the HCC dataset. The source encounter table observed dates from 2010-07-27 through 2026-01-01 in the bounded scan; therefore require a complete 90-day observable follow-up and exclude index TACE dates after 2025-10-03, unless Harbor computes a later administrative maximum from the same frozen source and applies the equivalent 90-day rule.

Index procedure: the first observed procedure per patient whose 手术 contains one of TACE, 肝动脉化疗栓塞, 经导管肝动脉栓塞, or 动脉化疗栓塞, with a parseable 开始时间 and a join to an encounters row. Require an HCC diagnosis before or on the index encounter using transparent exact/regex flags in diagnoses.诊断名称 (at minimum 肝细胞癌 or 肝恶性肿瘤), and age >=18 from encounters.年龄 at index. A sensitivity analysis should restrict to procedure names containing explicit chemotherapy embolization/TACE and exclude bland embolization terms; record both cohorts.

Exclude patients with a pre-index decompensation flag at any prior or index encounter: explicit diagnoses containing 腹水, 肝性脑病, 消化道出血, 食管胃底静脉曲张, 肝肾综合征, 急性肝衰竭, 肝功能衰竭, 自发性腹膜炎, or 黄疸, plus a separately reported broader 肝硬化失代偿 flag. The flag is a screening phenotype, not a validated diagnosis. Do not exclude a patient solely for missing labs; missingness is part of the feature report.

Time zero is the earliest matched TACE 手术.开始时间. Baseline is the closest usable lab in [-14 days, 0] before time zero, with a secondary baseline window [-30 days, 0]. The trajectory window is [0, 7 days] after time zero; retain the exact local timestamps and the number/timing of observations. To avoid label leakage, do not use data after day 7 in features. Start the primary outcome clock at the later of index encounter 出院时间 and time zero + 7 days; count only a new encounter admission after the index discharge. The primary estimand is the test-set difference in calibrated risk and discrimination between the baseline-only model and the dynamic model for a new decompensation-coded admission during days 8–90. A prespecified short-horizon secondary outcome uses days 8–30.

Primary outcome: a new post-discharge encounter containing a decompensation flag in diagnoses.诊断名称, using the high-specificity terms above, with a sensitivity definition requiring the same concept in clinical_documents.入院诊断, 出院诊断, 入院情况, 出院情况, or 诊疗经过. Report separate component outcomes (ascites, encephalopathy, bleeding, renal/hepatic failure, jaundice) and the composite. A new admission is not automatically unplanned; the source does not provide a validated planned/unplanned field. Secondary outcomes are (a) any new admission in days 8–90, (b) repeat TACE-like procedure in days 8–90, and (c) a documented liver-reserve deterioration phenotype without a decompensation code. The latter is exploratory and cannot substitute for the primary clinical endpoint.

The bounded diagnostic found 17,944 patients with a first TACE-like procedure under a broader procedure regex, 6,002 with a later admission within 90 days, 171 with a later broad decompensation-coded encounter and 58 within 30 days. These figures include no final baseline exclusion, no adjudication and a broad lexical screen; Harbor must recompute them from the frozen data and report denominators.

## Data binding

All joins are within HCC and use the documented composite key (患者主索引, 就诊号). Verify duplicate keys before aggregation and preserve patient-level identity. All listed HCC files are ordinary files, not archive members. The raw source paths, hashes and binding targets are:

| table | raw source and binding target | columns used |
|---|---|---|
| encounters | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室 |
| diagnoses | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 诊断名称, 诊断类型 |
| labs | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间 |
| procedures | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源 |
| clinical_documents | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 入院诊断, 入院诊断__duplicate_2, 出院诊断, 入院情况, 出院情况, 诊疗经过, 手术名称, 手术经过 |
| medications | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型 |
| examinations | raw [internal dataset path], [source checksum]; target [internal dataset path] | 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 检查号 |
| orders | raw [internal dataset path](非药品)_2062526727266216118.csv, [source checksum]; target [internal dataset path](非药品)_2062526727266216118.csv/data_医嘱(非药品)_2062526727266216118.csv | 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次 |

vitals, transfers and front_page are not inputs: their schemas contain only 患者主索引 and 就诊号 and the catalog marks them identifier-only. pathology is not required for the primary model; it can support an adjudication sample using 病理, 检查所见, 检查诊断, but it has no timestamp. Do not join any MIMIC or eICU source and do not infer equivalence from matching identifiers.

Laboratory features must be assay-specific. The catalog states that numeric lab results have no separate unit column; therefore do not pool numeric thresholds across assays or compute a clinically valid ALBI/MELD unless an expert verifies units and the exact assay mappings. Candidate exact 检验 names observed in the bounded sample include 总胆红素, 直接胆红素, 白蛋白, 血小板计数, 凝血酶原时间, 凝血酶原时间比值, 肌酐, 钠, 丙氨酸氨基转移酶, 天门冬氨酸氨基转移酶/谷草转氨酶, and 甲胎蛋白. Harbor must freeze the exact name dictionary after a schema/value audit, parse only numeric 定量结果, retain qualitative values separately, and use within-assay standardized deltas or ranks when units are unresolved. Candidate lab names are not evidence that every patient has every assay.

Medication features are exposure proxies only: prior/around-index use of diuretics, lactulose, antibiotics, albumin and antiviral agents, plus count and route; do not infer adherence or indication. Orders and examinations can provide measurement intensity and imaging/report context. Narrative text is not automatically a diagnosis: the catalog says the local lexical detector is unvalidated and supports only limited explicit context flags for cirrhosis. All primary endpoint flags require transparent string rules plus a blinded clinician adjudication sample before clinical interpretation.

## Baseline and substantive alternative

### Simple baseline

Fit a patient-level, temporally split regularized logistic regression for the primary binary outcome using only information available at time zero: age, sex, department, HCC/cirrhosis/portal-vein-thrombus and prior-decompensation flags, counts of prior encounters/procedures/medications/orders, TACE name/source, and the closest pre-index assay-specific lab levels plus missingness indicators. Add a fixed, prespecified baseline-only variant with the same variables but no labs to quantify laboratory contribution. Do not fit ALBI or Child-Pugh from unverified local units. Use standardized training-set transformations only.

### Mechanistic alternative

Fit a multivariate measurement-error state-space model on the same patients and same base covariates. The latent state is an unobserved hepatic reserve/injury state with a slow reserve component and a transient injury component; assay-specific observations from 0–7 days update the state, with irregular sampling and missingness explicitly modeled. The model must report posterior state trajectories and separate the contribution of (i) synthetic/renal reserve indicators (bilirubin, albumin, INR/PT, creatinine, sodium, platelets) from (ii) AST/ALT enzyme-flare indicators. The outcome head predicts the day-8-to-90 composite using only the posterior state at day 7 and the same baseline covariates. This is a mechanistic representation of competing explanations, not proof of a biological pathway.

The information the alternative may reveal that the baseline loses is whether coordinated reserve deterioration, rather than a single baseline level or isolated enzyme peak, precedes the event; its cost is stronger modeling assumptions and sensitivity to missing/unit ambiguity. A neural temporal transformer is explicitly deferred: it could encode event ordering, but the first scientific comparison is state separation and calibration, not a small predictive gain. It can be revisited only if the state-space model is inadequate and a larger, independently held-out study has sufficient outcome support.

### Split, fitting target and uncertainty

Use index-TACE calendar splits fixed before outcome inspection: train 2010-07-27 through 2018-12-31, validation 2019-01-01 through 2021-12-31, and test 2022-01-01 through 2025-10-03, with all rows from a patient in one split. If any split lacks enough events, preserve the chronological order and report the predeclared merged split rather than resampling patients randomly. Select regularization and state-space complexity on train/validation only. Fit each index patient once; do not let repeated procedures of the same patient enter the primary analysis.

Report test-set PR-AUC, ROC-AUC, Brier score, calibration intercept/slope and calibration-in-the-large, sensitivity/specificity at a prespecified high-sensitivity threshold, and decision-curve net benefit over clinically stated threshold probabilities. Use patient-cluster bootstrap resampling of the test set for 95% intervals, with stratified resampling only as a sensitivity analysis. Report the number of eligible patients, missingness, assay coverage, outcome events and censoring before reporting model metrics. Compare dynamic versus baseline predictions with paired patient-level bootstrap intervals. Also report the coefficient/state loading pattern and a plot/table of the posterior reserve-loss versus enzyme-flare states.

The actual deliverable is newly fitted baseline and state-space models, frozen held-out predictions, calibration/uncertainty summaries, a component-outcome table, and negative-control results. Readiness or a successful import is not a scientific result.

Approximate future Harbor resources: preprocessing and the regularized baseline should fit on 4–8 CPU cores and <32 GB RAM, likely tens of minutes after chunked CSV parsing (unmeasured). The state-space fit and bootstrap should request 16 CPUs, 64–128 GB RAM and no GPU, with a 4–8 hour budget estimate (unmeasured). The run envelope permits 16 CPUs, 262,144 MiB memory, 8 GPUs and 28,800 seconds; GPU use is not necessary for this tabular state-space workload. Full laboratory parsing is the dominant I/O uncertainty: the interactive scan of the 2.2-GB lab file exceeded 120 seconds, so the solver must use a managed job and checkpointed selected-column parsing.

## Falsification and interpretation

Negative controls are mandatory. First, repeat the dynamic model after permuting each patient's post-TACE lab timestamps within the 0–7-day window while preserving values and observation count; improvement that survives indicates ordering/measurement artifact. Second, use an analogous pre-index pseudo-window (days -7 to 0, with a matched prediction horizon) to test whether a purported post-TACE effect exists before treatment. Third, include lab-count/timing and encounter-count features; if the dynamic signal disappears, measurement intensity is a leading explanation. Fourth, perform a restricted analysis of patients with at least one baseline and one day-3-to-7 measurement, and a missingness-stratified analysis.

Supportive result: on the untouched temporal test set, the dynamic model improves calibration/Brier and PR-AUC over the baseline with uncertainty excluding no meaningful improvement, the reserve-loss state—not merely AST/ALT—precedes events, and the timestamp/peri-index negative controls do not reproduce the effect. This supports an incremental prognostic trajectory claim and justifies prospective validation and clinician review.

Adverse result: baseline-only performs as well or better, the dynamic advantage disappears after measurement-intensity adjustment, or the signal is confined to the enzyme-flare state. This falsifies the stated incremental reserve-loss hypothesis in this dataset; it does not show that liver tests have no clinical value.

Inconclusive result: the primary event count is too small, assay coverage is too sparse, the temporal splits lack events, calibration intervals are wide, or a clinician cannot adjudicate code-based events. This should defer the direction to a larger linked cohort rather than be reported as a null. If findings are robust only for repeat procedure or any readmission, that is a different utilization association and cannot be relabeled as decompensation.

## Claims requiring additional evidence

Computationally checkable claims are: cohort construction under the stated rules; key integrity; timestamp ordering; assay-specific feature extraction; held-out predictions; calibration/discrimination; uncertainty; negative-control behavior; and whether the dynamic model adds prognostic information.

Clinical adjudication is required for whether an encounter represents new/worsening ascites, variceal bleeding, encephalopathy, hepatorenal syndrome or post-TACE liver failure; whether it was planned; whether the code/document is temporally and clinically valid; and whether the event reflects TACE injury versus HCC progression or another illness. The dataset lacks exact released dates outside local timestamps, validated assay units, Child-Pugh components, INR/albumin unit mapping, bilirubin assay harmonization, viral loads, ECOG status, imaging pixels, tumor measurements, embolized territory, drug/dose, portal-pressure data, death linkage and external validation. The primary study therefore cannot establish mechanism, treatment causality, mortality benefit, or a safe clinical action threshold. Those stronger claims require expert adjudication, richer procedural/imaging data, and prospective or external validation.

## Inspectable evidence

The three distinct inspected hypothesis-specific works are [K1], [K2] and [K3], with abstract-only limits preserved in the attached excerpts and key-references.json.

[K1] Sanai FM et al. Predictors and outcomes of hepatic decompensation following transarterial locoregional therapy in hepatocellular carcinoma. Scientific Reports, 2026. DOI: 10.1038/s41598-026-54466-4. Supports the consequence of decompensation and baseline-reserve framing; it does not test this routine-lab trajectory.

[K2] Xu L et al. Development and validation of a nomogram model for predicting acute hepatic dysfunction post-intervention in primary hepatocellular carcinoma: a retrospective case-control study. World Journal of Surgical Oncology, 2025. DOI: 10.1186/s12957-025-04100-w. Provides the baseline-only comparator precedent; its abstract reports internal rather than external validation.

[K3] You R et al. Comparison of liver injury and inflammatory response following conventional and drug-eluting bead transcatheter chemoembolization in hepatocellular carcinoma. Discover Oncology, 2025. DOI: 10.1007/s12672-025-02286-9. Supports a day-5 laboratory injury window; it does not establish later decompensation prediction.

Reference source excerpts are hcc_ref_K1_excerpt.txt, hcc_ref_K2_excerpt.txt, and hcc_ref_K3_excerpt.txt; each is <=1 MiB, UTF-8, and explicitly labeled abstract-only.
