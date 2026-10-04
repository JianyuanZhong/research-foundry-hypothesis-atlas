# Corrected execution-ready POD2 signed assay-history experiment

Status: substantive endpoint-order repair child of [prior hypothesis]. The population, POD2 landmark, predictor boundary, signed-history estimand, matched models, temporal split, uncertainty, falsification, and claim limits are preserved. The outcome algorithm is corrected to classify every candidate procedure before selecting the first qualifying event. A bounded aggregate audit found 15 later qualifying events censored by the parent's first-match-then-classify implementation, changing event counts from 300 to 315. No outcome model was fitted.

## Clinical opening, supported claim, and hypothesis

At postoperative hour 48 after a first recorded HCC liver resection, clinicians must decide whether early laboratory history adds useful warning beyond current POD2 severity and observation practice. Intervention-requiring pleural or abdominal collections are clinically consequential: Wang et al. included thoracentesis and abdominal drainage in an adjudicated 30-day complication composite [K1]; Sakamoto et al. defined clinically relevant post-hepatectomy pleural effusion by thoracentesis or thoracic drainage and discussed fluid-retention and inflammatory explanations [K2]; Clavien-Dindo treats invasive intervention as grade III [K3]. None validates this extract's codes as unplanned complications or establishes that assay direction predicts intervention.

Strongest supported local claim: a full-census audit plus candidate-order reclassification found 315 patients with at least one context-supported recorded postoperative invasive pleural/abdominal fluid intervention. Fifteen had an earlier nonqualifying lexicon match before their first qualifying intervention and were missed by the parent's 300-event first-match implementation. This supports a reproducible phenotype of context-supported recorded intervention, not unplanned intent, causation, chronicity, benefit, or grade.

Unresolved hypothesis: among adults still hospitalized and endpoint-free at 48 hours after their first recorded HCC liver resection, signed 0-48-hour change direction in 国际标准化比值, 纤维蛋白原, 丙氨酸氨基转移酶, and 降钙素原 improves prediction of the first context-supported recorded invasive pleural/abdominal fluid intervention in (48,336] hours beyond both an identical latest-state/observation/treatment baseline and an unordered rival retaining elapsed span and absolute change magnitude.

This is prognostic temporal information, not a causal mechanism or treatment rule.

## Frozen population, corrected endpoint, and estimands

1. Age at least 18 and encounter diagnosis matching 肝细胞癌|肝细胞性肝癌|HCC.
2. Per patient, first encounter containing a procedure name with 肝 and 切除, excluding 移植|供体|供肝|活体供; require 手麻系统 in that encounter and set T0 to its earliest 开始时间.
3. Require T0 within one day of admission/discharge and discharge after T0+48 hours.
4. Exclude a primary-lexicon fluid procedure in [T0,T0+48h].
5. Restrict T0 to 2018-2025.
6. Enumerate every candidate procedure in (T0+48h,T0+336h], no later than discharge+2h, using the frozen pleural/abdominal lexicon.
7. Classify each candidate independently using candidate-relative postoperative examination, near-event procedure-specific non-drug order, and treatment-course-document context, with the frozen unrelated/transhepatic, planned/existing-drain, and pre-existing-fluid exclusions.
8. Y=1 if any candidate is context-supported; event time/source/component are from the earliest context-supported candidate after deterministic sorting by 开始时间, 手术, 手术来源. Earlier nonqualifying candidates do not censor later qualifying candidates. Y=0 otherwise.

Post-48-hour procedures, examinations, orders, and documents construct Y only and are forbidden predictors. Corrected N=17,733/events=315: development 2018-2021 6,991/81; tuning 2022 1,891/35; calibration 2023 2,968/45; locked test 2024-2025 5,883/154. Components are pleural 241, abdominal 69, combined-name 5.

Primary estimands after separate frozen 2023 recalibration are paired locked-test Brier(T1)-Brier(B0) and the decisive ordering contrast Brier(T1)-Brier(U1).

The historical outcome-blind structural diagnostic has N=8,883 because it used a narrower early-fluid exclusion than the authoritative risk set, whose 2018-2022 denominator is 8,882. Reproduce that diagnostic exactly as history, but recompute feature coverage and all event-linked G1 support using this corrected endpoint and authoritative population. Never use 8,883 as the model denominator.

## Exact read-only bindings

Snapshot: [source checksum]. All are ordinary CSVs. Read with utf-8-sig, join exact-string 患者主索引 + 就诊号, assert one encounters row per key, and many-to-one join all other tables.

- procedures: [internal dataset path]; 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源.
- encounters: [internal dataset path]; keys, 年龄, 性别, 入院时间, 出院时间.
- diagnoses: [internal dataset path]; keys, 诊断名称, 诊断类型; no timestamp.
- labs: [internal dataset path]; keys, 检验, 定性结果, 定量结果, 标本类型, 检验时间.
- medications: [internal dataset path]; keys, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型.
- orders: [internal dataset path](非药品)_2062526727266216118.csv; keys, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次; endpoint context only.
- examinations: [internal dataset path]; keys, 检查, 检查所见, 检查诊断, 开始时间, 检查号; endpoint context only.
- clinical documents: [internal dataset path]; keys, 主诉, 现病史, 既往史, first raw 入院诊断, 入院情况, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过. 入院诊断 is duplicated in the raw header; explicitly retain the first named field. No document timestamp; endpoint context only.

All source hashes match the catalog. Vitals/transfers are identifier-only. Lab units, fluid balance, urine/drain output, oxygen status, original images, scheduling intent, and outside events are unavailable.

Frozen exact lab labels: C反应蛋白（急）, 丙氨酸氨基转移酶, 中性粒细胞数, 国际标准化比值, 尿素, 总胆红素, 淋巴细胞数, 白蛋白, 纤维蛋白原, 肌酐, 钠, 门冬氨酸氨基转移酶, 降钙素原, 高敏感C反应蛋白. Do not pool synonyms or convert units.

## Preprocessing and matched models

Only [T0,T0+48h] timestamps form predictors. Parse 定量结果; median-collapse duplicate label-time values; development-only 1st/99th percentile winsorization and median/IQR scaling; drop zero-IQR channels with reasons; reuse transforms later.

For each label, retain latest standardized value, latest hour/hours to landmark, and missing indicators. For each ordered assay, median-bin [0,12), [12,24), [24,36), [36,48]; A=1 only for at least two bins spanning at least 12 hours; then h is midpoint span, M=absolute first-to-last rate, D=signed rate; otherwise h=M=D=0. Scale h/M/D using available development records.

Common inputs: age, sex, log valid operation duration plus missingness, year, laparoscopic and coarse major-resection flags; per-label missingness and time; ordered-assay row/bin counts and A; total unique lab timestamps; presence and first start hour for albumin, loop diuretic, vasopressor, antibiotic, and hemostatic frozen lexicons. Medication features are context, never treatment effects.

B0: unweighted ridge logistic on common/static/treatment/observation features and latest values for all 14 labels. U1: B0 plus h and M for four ordered assays. T1: U1 plus exactly four D features. T1-U1 therefore isolates retention of sign/order conditional on latest state, elapsed span, absolute change, and observed measurement process; it does not identify biological recovery.

Use an unpenalized intercept and explicit mean log loss plus separate L2 blocks. Select each block lambda from {0.001,0.01,0.1,1,10,100} by equal-weight leave-one-year-out 2018-2021 Brier, largest lambda within one SE across four folds; sequentially hold earlier block penalties fixed. Refit 2018-2022.

G0-latest: histogram gradient boosting on B0 inputs only, max leaves {3,7}, minimum leaf {50,100}, learning rate .05, 200 iterations, selected by the same annual-fold Brier rule. It tests nonlinear current severity.

The coupled-domain, dynamic-factor, GRU, and transformer alternatives remain deferred: historical observability was only 2.44% for all domains in two bins, 0.045% in three bins, and about 2.2% for repeated renal assays. Revisit only under the frozen density/event criteria. They would otherwise primarily learn observation masks rather than the proposed cross-domain process.

## Gates, uncertainty, and falsification

G0: hashes/headers, unique encounters, corrected first-satisfying endpoint counts, no predictor after 48h, no patient split overlap. Before fitting, freeze corrected cohort keys, candidate-level classifications, transforms, and hashes.

G1: reproduce the historical structural diagnostic, then report corrected-authoritative-cohort all-patient/by-year and event-linked coverage for at least one/two ordered channels. A null supports an adverse conclusion only with at least 1,500 development+tuning patients, 30 of 116 development+tuning events, and 40 of 154 test events with at least one ordered channel.

G2: 2022 may expose only coding/numerical failures; no design tuning.
G3: separate intercept/slope recalibration in 2023 for B0/U1/T1/G0-latest.
G4: open 2024-2025 once after prior artifacts/hashes freeze.

Report paired Brier contrasts, log loss, AUROC, AUPRC, calibration, and net benefit at 1%,2%,3%,5%. Use 2,000 paired patient bootstraps stratified by test year and 200 end-to-end patient bootstrap refits within year across all splits. End-to-end refits repeat transforms, tuning, recalibration, and metrics while preserving frozen definitions.

Required controls: 100 independent patient-assay direction-sign ablations within test year; timing-only; values-only and A>=1 subset; medication removal; G0-latest; inherited S1/S2/component/examination-free/order-free/union/cross-source endpoint sensitivities; annual and procedure-source analyses; 2020-2023-to-2024-2025 sensitivity; and +28-day within-encounter timestamp shift where possible.

Negative control: permute Y within calendar year only, preserving annual sample size and event prevalence while destroying patient-level association. Procedure-source analyses use only the unpermuted true endpoint. Above-chance negative-control performance triggers leakage investigation and an inconclusive result.

Supportive requires all frozen conditions: T1-B0 Brier <=-0.0010 with CI below zero; AUPRC gain >=.02 with CI above zero; recalibrated T1 slope .8-1.2/intercept -.20-.20; T1-U1 Brier CI below zero; direction ablation removes >=50% of gain and timing-only/G0 do not match; direction agrees across S1/S2 and examination-free/order-free outcomes without catastrophic era/source reversal. Support establishes incremental prognostic ordered-history information only.

Adverse requires adequate G1 support/stable coverage plus either the T1-B0 interval excluding benefit of -0.0010 or better, or no T1 advantage over U1 with >=75% apparent gain preserved after direction ablation. Prefer B0 and abandon direction for this endpoint.

Inconclusive includes sparse event-linked repetition, intervals spanning meaningful benefit and no benefit, failed calibration, source/era reversal, observation-only gain, endpoint reversal, bootstrap failure, or above-chance negative-control performance. An imprecise null does not refute direction.

## Deliverable and claim limits

The solver must reconstruct/checksum the corrected authoritative cohort; emit a candidate-level endpoint ledger that proves classification precedes earliest-event selection; fit B0/U1/T1/G0 and controls; recalibrate; open the test once; and emit private patient-keyed predictions, source/cohort/split/coverage/feature/transform/leakage artifacts, model specifications, metrics/bootstrap/calibration/decision outputs, ablations/sensitivities, phase_gates.json, and claims.json linking interpretation to frozen rules. Confirmation is not required.

Compute: 8 CPUs/64 GiB about 1-2 hours for preprocessing/fits; 8-16 CPUs/64-128 GiB about 2-4 hours for 200 refits; within 16 CPUs, 262,144 MiB, 8 hours. These are unverified planning estimates based on the low-dimensional tabular workload; GPU is not needed.

Computationally checkable: bindings, joins, boundaries, candidate-level endpoint rules/counts, first-satisfying selection, splits, transforms, fits, outputs, uncertainty, controls, and conclusion-rule compliance. Clinicians/other studies are required for unplanned intent, complication cause/grade, chronicity, drain chemistry/output, fluid balance, oxygen status, images, outside outcomes, mechanism, treatment effects, decision utility, and transportability.

## Exactly three key references

[K1] Wang RC, Niu WY, Lu XL, Lu ZF, Qian Y. Development and validation of a model for predicting short-term complications after hepatectomy in patients with primary liver cancer. J Gastrointest Oncol. 2026;17(2). doi:10.21037/jgo-2026-0213. Full-text sections inspected.

[K2] Sakamoto A, Sakamoto K, Shine M, et al. Postoperative cardiothoracic ratio on the first postoperative day is a predictor of postoperative pleural effusion drainage following hepatectomy. Research Square. 2023;v1. doi:10.21203/rs.3.rs-2807394/v1. Full-text sections inspected; preprint status retained.

[K3] Dindo D, Demartines N, Clavien PA. Classification of surgical complications: a new proposal with evaluation in a cohort of 6336 patients and results of a survey. Ann Surg. 2004;240:205-213. doi:10.1097/01.sla.0000133083.54934.ae. Full-text sections inspected.
