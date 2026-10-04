# Post-TACE liver-reserve trajectory and near-term hepatic decompensation in HCC

## Scientific question and hypothesis

Clinical decision: after a patient with hepatocellular carcinoma receives transarterial chemoembolization (TACE), should the team intensify early monitoring and reconsider repeat locoregional treatment because liver reserve is worsening, even when the pre-treatment laboratory level was acceptable?

Hypothesis: among patients with HCC receiving their first recorded TACE in this snapshot, worsening liver-reserve trajectory during days 3–14 after the procedure is associated with a higher risk of a new, subsequently recorded hepatic-decompensation event during days 15–90, and improves out-of-sample calibrated risk estimation beyond pre-TACE liver-reserve level and clinical history.

The estimand is prognostic, not causal: the contrast is the conditional 90-day risk associated with post-TACE trajectory, not the effect of assigning TACE. The study will not claim that TACE caused the trajectory or that changing treatment based on the model improves outcomes.

## What is already supported versus unresolved

The local source files establish that this is a liver-tumor-centered longitudinal hospital dataset with substantial HCC and TACE activity, and that albumin, bilirubin, PT/INR, platelets, creatinine and sodium are repeatedly recorded in the laboratory table. They do not establish that a diagnosis string is an adjudicated event, that all outpatient care or deaths are captured, or that the first recorded TACE is a true incident treatment.

The acquired public HCC literature supports the general premise that dynamic blood biomarkers can complement static measurements in prognostic models, but the retrieved study was a separate single-center cohort and used different treatment context and endpoints. Its results are not evidence that this HCC snapshot contains a valid post-TACE decompensation signal. The unresolved claim is therefore narrower and testable: does a leakage-safe, short post-TACE trajectory add clinically meaningful prognostic information for subsequent recorded decompensation in this real-world cohort, beyond the baseline state?

A positive result would justify prospective validation and clinical adjudication; it would not validate a treatment threshold, causal mechanism, or patient-benefit claim.

## Population, index, and temporal boundaries

Use only the HCC source snapshot [source checksum].

1. Read HCC/data_诊断_7504718184492840569.csv (diagnoses) and define HCC history by diagnosis names containing 肝细胞癌 or 肝癌, excluding names containing 疑似/待查 where applicable. Require a patient-level HCC diagnosis on or before the index encounter.
2. Read HCC/data_手术_8024330590283626027.csv (procedures). Define TACE as a procedure name containing TACE or the prespecified Chinese terms 经导管肝动脉栓塞术, 肝动脉化疗栓塞, 肝动脉栓塞化疗, or their parenthesized catheter variants. The index is the earliest recorded qualifying procedure start time per 患者主索引; exclude patients with a prior qualifying TACE in the available record. Keep the procedure's 就诊号 and 开始时间, and use 结束时间 when present.
3. Join encounters from HCC/data_基本信息_2500296761891079109.csv by (患者主索引, 就诊号) to obtain age, sex, admission/discharge timestamps and department. The patient is the unit of analysis; repeated TACE episodes are not independent.
4. Require at least one usable measurement in the baseline window [index start −14 days, index start] and at least one usable measurement in the post-treatment window [index start +3 days, index start +14 days] for each core trajectory component, with a prespecified complete-case primary analysis and a missingness-indicator sensitivity analysis. Measurements are matched by 患者主索引, 就诊号; laboratory time is 检验时间.
5. The primary core reserve vector is albumin (白蛋白), total bilirubin (总胆红素), INR (国际标准化比值) or PT (凝血酶原时间), platelet count (血小板计数), creatinine (肌酐) and sodium (钠). Do not pool assays with different names or units. Use the first value nearest each landmark per assay; if duplicate same-time values exist, retain the value according to a deterministic rule recorded in code. Numeric parsing must reject nonnumeric values and impossible sentinels rather than silently coerce them.
6. Follow-up starts at index start +14 days. Do not use any lab, diagnosis, medication or procedure after this landmark as a predictor. Follow to index +90 days or the last available encounter date, whichever comes first. The index treatment encounter and days 0–14 are excluded from outcome ascertainment.

## Outcome and evidence limits

Primary outcome: a new qualifying diagnosis on an encounter whose encounter/admission time is strictly after index +14 days and no later than index +90 days, using exact diagnosis-name matching after normalization:

- 腹腔积液 (including specified parenthetical variants);
- 肝性脑病;
- 肝衰竭 or 慢性肝衰竭/急性肝衰竭;
- 上消化道出血 or 消化道出血.

A qualifying label must be absent from all diagnosis records on or before index +14 days for that patient, to target incident recorded decompensation. Report each component separately and the composite. A secondary broader outcome may include a new post-landmark inpatient encounter, but it is utilization, not decompensation, and must not replace the primary outcome.

The source supports recorded diagnoses and timestamps, not expert adjudication of decompensation, grade/severity, transplant-free survival, radiographic recurrence, tumor response, cause of death, or outpatient completeness. No death endpoint will be invented from the 288 death-diagnosis rows without a validated death-capture definition. Clinical reviewers must adjudicate a sample of outcome-positive and outcome-negative charts, and an external dataset or registry is required before clinical deployment.

## Exposure representation and baselines

For each assay, standardize within the development set only. The primary trajectory feature is post-window value minus baseline value, with direction oriented so that worsening reserve is positive (albumin decrease, platelet decrease, sodium decrease, and increases in bilirubin, INR/PT, and creatinine). Also retain baseline value, post value, days between measurements, and whether the observation came from the index encounter or a subsequent encounter.

Primary baseline (predeclared): regularized logistic regression for the binary 90-day outcome using age, sex, pre-index HCC/cirrhosis/ascites history, index department, TACE history count (zero by construction but preserve procedure-context features), and the six baseline laboratory values plus laboratory recency and availability indicators. Do not include post-index data, post-treatment diagnoses, or procedure names that encode the outcome. Report calibration intercept/slope, Brier score, AUROC, AUPRC, and decision-curve net benefit over a prespecified clinically plausible risk range.

Trajectory baseline extension: add the six prespecified change scores to the same model. The primary scientific test is the incremental optimism-corrected Brier score and calibration improvement, with bootstrap confidence intervals, not a small AUROC chase.

Substantive learned alternative on the same question: a patient-level temporal gradient-boosted model (histogram gradient boosting or XGBoost if available) trained on the ordered laboratory observations from index −14 through index +14, with assay identity, value, time-from-index, baseline/post indicators, and measurement count. Constrain the feature vocabulary to the six reserve assays plus age, sex, prior diagnoses, and index procedure context. Use monotonic constraints only in a sensitivity analysis, not as an assumption of the primary learned model. Fit on patients, never rows; use a patient-level 70/15/15 split stratified by outcome and a later-index temporal holdout if event counts permit. Tune only within training/validation. Calibrate on validation and freeze before test evaluation.

The learned alternative can reveal nonlinear thresholds, interactions between reserve components, and whether the shape and timing of change carries information that a single delta loses. The simple model is preferable if the learned model does not improve calibration/Brier score with uncertainty, if temporal density creates unstable shortcut performance, or if the complete-case cohort is too small. The learned model must not be selected merely for a predictive gain without a clinically interpretable trajectory analysis.

## Analysis and uncertainty

Primary analysis:
- create one index row per eligible patient;
- report cohort flow, missingness, number of outcome events and component event counts;
- fit baseline and trajectory-extended logistic models on the training partition;
- evaluate in a locked patient-level test set and, if supported, a later-index holdout;
- estimate risk ratios/odds ratios for prespecified worsening-trajectory quartiles and per interquartile-range change, with 95% bootstrap CIs;
- use inverse-frequency weighting or precision-recall metrics for imbalance, but do not overinterpret AUROC;
- assess calibration plots, calibration intercept/slope, Brier score, bootstrap optimism, and decision curves;
- repeat with (a) 30-day and 90-day windows, (b) 0–30-day and 15–90-day outcome definitions, (c) index-encounter labs excluded from post measurements, (d) broader/narrower diagnosis matching, and (e) missingness indicators;
- cluster uncertainty by patient (one index row) and use hospital/site effects only if a reliable site identifier is discovered; 就诊科室 is a department, not a hospital.

The scientific deliverable is newly fitted, locked baseline and learned trajectory models, an estimated association of each reserve trajectory with the composite and its components, and a complete uncertainty/transportability report. Completion requires saved design matrix counts, fitted coefficients/model artifact, locked test predictions, calibration/Brier/AUROC/AUPRC/decision-curve tables, bootstrap intervals, feature-attribution summary, and falsification checks. A schema audit or a reference execution alone is not completion.

## Falsification and interpretation

Supportive result: worsening trajectory has a prespecified direction, a confidence interval excluding no association in the primary test, and the trajectory model improves test-set Brier/calibration or decision-curve net benefit over the baseline with stable results across reasonable windows and the later-index holdout. This supports prognostic utility for recorded decompensation and motivates prospective adjudicated validation.

Adverse result: no association, opposite-direction association, or no incremental out-of-sample calibration/utility after leakage controls. This would refute the proposed incremental trajectory claim for this dataset and argue against using early lab change as a monitoring trigger without another study. It would not prove that liver-reserve changes are clinically irrelevant.

Inconclusive result: too few complete cases/events, wide intervals, substantial assay-specific missingness, strong performance collapse in the later-index holdout, or sensitivity to diagnosis matching/measurement density. This means the dataset cannot resolve the claim; it is not evidence for or against the biology.

Automatic verification can check joins, temporal exclusion, one-row-per-patient construction, label definitions, split integrity, model fitting, prediction metrics, uncertainty calculations, and whether written conclusions match computed outputs. It cannot establish diagnosis validity, treatment appropriateness, causal effects, recurrence, mortality, or benefit from altered monitoring. Those require clinical adjudication, linkage to complete outcomes, and prospective or external validation.

## Exact data bindings and unavailable tables

Used:
- encounters: [internal dataset path]; columns 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室.
- diagnoses: [internal dataset path]; columns 患者主索引, 就诊号, 诊断名称, 诊断类型.
- procedures: [internal dataset path]; columns 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源.
- labs: [internal dataset path]; columns 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间.
- Optional sensitivity covariates: medications at [internal dataset path], columns 患者主索引, 就诊号, 用药, 开始时间, 结束时间, 用药方式, 药品类型; and clinical_documents at [internal dataset path], columns 患者主索引, 就诊号, 入院诊断, 入院情况, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过. Text is sensitivity-only because the guide documents an unvalidated lexical-context detector and no validated diagnosis extraction.

Not usable as clinical payload:
- vitals [internal dataset path], transfers [internal dataset path], and front_page [internal dataset path] contain only the identifier pair in this snapshot. They may be used only for identifier-consistency audits.
- examinations [internal dataset path] and pathology [internal dataset path] contain narrative fields and timestamps but no image files; they are not required for the primary hypothesis because radiographic response, tumor size, stage, and pathology adjudication are incomplete.

## Compute budget and reproducibility

Use CPU by default in ehr-campaign-cpu:20260908 or python:3.11-slim; declare source files read-only and write only derived design matrices, model checkpoints and result tables. Stream the 2.2 GB labs and 2.1 GB orders files; never load all rows into memory. Reserve at most 4 CPUs and 16 GB RAM for approximately 20–45 minutes for deterministic extraction and fitting; the gradient-boosted model is bounded to at most 500 trees and 10 hyperparameter configurations. Preserve a manifest with source snapshot/schema hashes, row counts, actual filters, split seeds and software versions. No GPU is scientifically necessary.

## Disposition of demonstrations and seeds

- Delphi-2M: concrete adaptation is the locked temporal trajectory-vs-baseline comparison above; missing UKB/Danish population and external validation prevent reproduction.
- ALADYNOULLI: not pursued as a reproduction because germline genetics are unavailable and the HCC question is a short post-procedure landmark; a latent longitudinal extension is deferred unless the simple trajectory signal is stable.
- Oncoformer: concrete lab-only adaptation is represented by the learned temporal model; chest X-rays and complete STAR Methods are unavailable, so no multimodal or reproduction claim is made.
- All 30 imported expert seeds were assessed and rejected for this episode because they target eICU, MIMIC-IV, or UK Biobank and cannot be bound to HCC rows or variables. No HCC expert seed was supplied.
- Deferred learned alternatives: a latent-class mixed model could estimate clinically interpretable reserve trajectories but adds assumptions and local-maxima/entropy diagnostics; it should be revisited if trajectory shape is scientifically central and event counts support it. A transformer/generative sequence model is deferred because the primary claim is a narrow 90-day prognostic increment, for which its extra complexity is not justified before establishing event validity and baseline adequacy.
