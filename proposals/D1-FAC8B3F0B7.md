# POD3 recovery asynchrony and delayed discharge after HCC resection

## Clinical opening and hypothesis

This is a parentless restart. The prior biomarker-surveillance branch is transition context only; its exposure was too sparse for confirmation.

Existing evidence shows that preoperative factors associate with postoperative length of stay in selected HCC patients [K1], and that POD1 bilirubin plus clinical factors can predict adjudicated liver failure after major hepatectomy [K2]. Formal ISGLS liver failure, however, requires INR and bilirubin abnormalities relative to local reference limits on or after POD5 plus management-based grading [K3]. No inspected work establishes whether early cross-domain recovery discordance informs a subsequent discharge transition.

Hypothesis: among adults with HCC still in the index hospital 72 hours after a first qualifying liver resection, domain-specific asynchrony during hours 0–72—especially resolving hepatocellular injury with persistently adverse excretory, synthetic, renal, or platelet trajectories—contains transportable information about remaining hospitalized beyond POD7 that is not captured by static values, simple slopes, observation intensity, operative burden, or one shared recovery state.

This is prognostic, not causal. The leading explanation is nonparallel physiological recovery; rivals are common severity, treatment/testing intensity, and era-specific discharge practice. A robust gain would justify prospective adjudication of a POD3 review trigger. A precise adverse result would favor simpler summaries.

## Population, clock, and outcomes

1. In procedures, require dated 开始时间 and procedure text matching liver resection: 肝.{0,6}(部分|段|叶|半肝|肿瘤).{0,6}切除, 部分肝切除, 半肝切除, or 肝切除术. Exclude 供肝, 病肝切取, 移植, 活检, 穿刺, 切开, 引流, 囊肿, 脓肿, 复发, 再次.
2. Require age at least 18, nonmissing discharge, procedure time within admission minus/plus 24 hours, and same-encounter non-uncertain HCC diagnosis matching 肝细胞癌, 原发性肝癌, or 肝癌 but not 待排, 疑似, 可能, 除外, 复发, or 术后.
3. Collapse duplicates and select each patient's earliest qualifying operation ordered by patient, start time, encounter, procedure.
4. Landmark at procedure start +72 hours. Include only patients discharged after the landmark, so all have an identical exposure window.
5. Primary outcome: recorded index discharge after procedure start +168 hours (POD7). This is delayed recorded discharge, not complication, readiness, mortality, or avoidable stay.
6. Secondary: hours from landmark to discharge. A robustness endpoint is the first distinct local encounter beginning >24 hours and <=30 days after discharge. Call it local return, never all-cause or unplanned readmission.

No post-hour-72 event enters predictors. Do not condition on future testing or complete trajectories.

## Exact bindings

Snapshot: [source checksum]. Join within encounter on (患者主索引, 就诊号), across encounters on 患者主索引.

- encounters: [internal dataset path] Required columns 患者主索引, 就诊号, 年龄, 性别, 身高, 体重, 就诊时间, 入院时间, 出院时间, 就诊科室. Supplies cohort, endpoint, service, local return. Direct identifiers other than private linkage keys are never features or outputs.
- procedures: [internal dataset path] Columns 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源. Supplies index time, duration, source, and train-frozen laparoscopic/open and extent indicators.
- diagnoses: [internal dataset path] Columns 患者主索引, 就诊号, 诊断名称, 诊断类型. Supplies eligibility and baseline cirrhosis/portal-hypertension/comorbidity flags. It has no native time and cannot be a postoperative event.
- labs: [internal dataset path] Columns 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间. Use plain numeric exact labels 丙氨酸氨基转移酶 (ALT), 门冬氨酸氨基转移酶 (AST), 总胆红素 (TBIL), 白蛋白 (ALB), 国际标准化比值 (INR), 肌酐 (CREA), 血小板计数 (PLT), from -30d to <0 for baseline and [0,72h] for dynamics. Do not pool emergency-suffixed labels. Units/reference ranges are absent; use train-only robust transforms and make no threshold diagnosis.
- orders: [internal dataset path](非药品)_2062526727266216118.csv. Columns 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次. Before landmark derive 12-hour new/active counts, unique labels, train-frozen support groups, and observation masks.
- medications: [internal dataset path] Columns 患者主索引, 就诊号, 用药, 单次用药剂量, 单次用药剂量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型. Before landmark derive new/active counts, unique names/routes, and train-frozen albumin-product, diuretic, antimicrobial, vasopressor-label, and analgesic groups. These are treatment/workflow proxies, not administered treatments or indications.
- clinical_documents, pathology, and examinations are not inputs: documents/pathology lack native timestamps and can leak discharge knowledge; examinations add no needed endpoint data. Vitals, transfers, and front_page are identifier-only.

All four configured datasets remain read-only and directly accessible; this experiment uses HCC only.

## Common preprocessing and split

Split by index year before fitting: train 2012–2019, validation 2020–2022, locked test 2023–2025. Freeze vocabularies, transforms, imputation, interactions, hyperparameters, and recalibration on train/validation. Read test once.

For each exact lab, median duplicate same-time values and place observations in six 12-hour bins. Derive the last preoperative numeric value. Every model receives identical patients, windows, covariates, treatments, values, and observation masks. Missingness is explicit; no complete-case restriction or outcome-dependent interpolation.

Domains are injury (ALT/AST), excretory (TBIL), synthetic/nutritional (INR/ALB), renal (CREA), and hematologic reserve (PLT). These are measurement domains, not proven organs or mechanisms.

## Transparent baseline

Fit elastic-net logistic regression for POD7 delayed discharge, penalty selected by validation log loss. Inputs: demographics, service/year, approach/extent/source/duration, diagnosis flags, preoperative labs, hour-72 latest values, first-to-last change and robust slope, min/max, observed-bin counts, lab/order/medication intensity, missingness, and prespecified injury-minus-other-domain slope contrasts after train scaling. A demographic/operation/workflow model is the floor.

This strong baseline shows whether simple level, trend, or observation intensity drives risk. It loses exact order, nonlinear turns, irregular-sampling uncertainty, and correlated domain-specific recovery.

## Matched learned/mechanistic alternative

Fit two nested 12-hour state-space classifiers:

1. Shared-state rival: one latent recovery/severity state emits all seven labs and predicts POD7, with order, medication, and measurement intensity as time-varying covariates.
2. Asynchronous-domain model: shared state plus five domain-specific deviations shrunk toward it. Irregular observation masks enter the likelihood. Output posterior domain paths and hour-72 lag contrasts; the outcome head sees only states through hour 72.

Use a monotone-time prior only for shared recovery, not every observed lab. Fit three seeds and tune latent dimension/regularization on validation log loss. The alternative can reveal whether discordant timing survives representation of shared severity and care intensity. It cannot establish regeneration, intent, readiness, or treatment response.

Before fitting clinical data, require simulated shared-only, asynchronous, workflow-driven, and informative-missingness scenarios. Recover injected lag direction and do not invent useful lags in shared/workflow-only data. Failure stops mechanistic interpretation.

## Evaluation and falsification

Primary locked-test metrics: patient log loss, calibration intercept/slope, integrated calibration index. Secondary: AUROC, AUPRC, Brier, decision curves at validation-fixed top 10%, 20%, 30% review capacities, and time-to-discharge concordance/error. Use 2,000 paired patient bootstraps. Report year, sex, age, approach, extent, and cirrhosis subgroups.

Supportive evidence requires all: asynchronous versus transparent log-loss gain at least 0.01 with paired 95% CI excluding zero; versus shared-state gain at least 0.005 with CI excluding zero; locked-test direction preserved, calibration slope 0.8–1.2 after validation-frozen recalibration, no sign reversal in at least two of three test years; simulation gates pass; removing domain deviations degrades performance while removing care-intensity terms does not erase the gain. This supports prognostic information, not mechanism or discharge action.

Adverse evidence: the paired interval upper bound excludes 0.01 gain versus transparent baseline and no 0.005 gain versus shared state. This favors simpler common-severity/workflow summaries.

Inconclusive: broad intervals, simulation failure, calibration slope outside 0.8–1.2, year reversal, unresolved informative observation, or endpoint drift. Do not peek again, alter splits/thresholds, pool labels, or add post-72 data to rescue results.

## Executed feasibility observations

These are not hypothesis results.

- A streamed 8-CPU audit in 55.4 seconds found 25,021 eligible landmark patients; 15,752 had discharge after POD7. Local 30-day returns numbered 2,381 (9.5%), median day 24.
- Temporal support was train 10,656/8,457 delayed, validation 5,518/3,607, test 8,847/3,688. The prevalence shift (79.4%, 65.4%, 41.7%) motivates out-of-time calibration.
- A second 8-CPU audit in 46.7 seconds found at least two distinct postoperative bins in ALT 9,566, INR 8,746, TBIL 4,137, ALB 4,135, CREA 3,781, and exact PLT count 4,262 patients. An exploratory substring selector incorrectly chose mean platelet volume; the v2 exact-label audit corrected it.
- No clinical model was fit; no association has been observed.

Artifacts: work/hcc-transition-feasibility.json, work/hcc-transition-feasibility-v2.json, work/hcc-temporal-split-support.json and scripts.

## Solver deliverable and compute

The solver must newly fit floor, transparent, shared-state, and asynchronous models; run four simulations; produce locked-test uncertainty/calibration; and emit a threshold-linked supportive/adverse/inconclusive conclusion.

Measured preprocessing used 8 CPUs/64 GiB requested/no GPU, under one minute per audit. Planned maximum: baselines 16 CPUs/128 GiB/2h; state models and simulations 1 A100 80GB plus 16 CPUs/128 GiB/6h; bootstrap 16 CPUs/2h, total at most 8h. The GPU estimate is unverified and has no merit itself; checkpoint seeds and retain predictions.

Required outputs: cohort flow/timestamp checks, label/vocabulary manifests, split event/missingness tables, simulation report, coefficients/paths/checkpoints, deidentified row-level predictions, paired metrics/uncertainty, calibration/subgroup plots, and conclusion.json.

A verifier can check hashes, joins, landmark ordering, no post-72 leakage, exact labels, split isolation, common inputs, simulations, convergence, paired metrics, uncertainty, calibration, and conclusion gates. It must reject claims of liver failure, causality, readiness, benefit, all-cause readmission, or biological recovery.

Clinical review/additional data are required for necessity/safety of stay, planned returns, latent-state meaning, mortality, outside care, units/reference ranges, administered treatment, blood loss, ICU, complications, destination, and intent.

## Alternatives and revisit triggers

- POD5 ISGLS liver failure: deferred because units/reference limits and management grades are unavailable [K3].
- Local 30-day return: secondary only because outside events and planned status are absent.
- Static preoperative LOS: floor only; it does not test recovery ordering.
- Generic transformer: deferred because it does not directly separate shared recovery from domain lag; revisit only if state approximation fails while sequence ordering remains unresolved.
- Text model: deferred because documents lack timestamps and risk leakage.
- Prospective adjudicated discharge-readiness study: required before any clinical trigger if retrospective evidence is supportive.

## Bibliography

[K1] Li F, Ren Y, Fan J, Zhou J. The predictive value of the preoperative albumin-to-fibrinogen ratio for postoperative hospital length of stay in liver cancer patients. Cancer Medicine. 2023. doi:10.1002/cam4.6606. Full-text sections inspected.

[K2] Baumgartner R, Engstrand J, Rajala P, et al. Comparing the accuracy of prediction models to detect clinically relevant post-hepatectomy liver failure early after major hepatectomy. British Journal of Surgery. 2024. doi:10.1093/bjs/znad433. Full-text sections inspected.

[K3] Rahbari NN, Garden OJ, Padbury R, et al. Posthepatectomy liver failure: a definition and grading by the International Study Group of Liver Surgery (ISGLS). Surgery. 2011. doi:10.1016/j.surg.2010.10.001. Abstract only inspected.
