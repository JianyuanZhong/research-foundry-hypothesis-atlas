> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Provisional HCC trajectory-versus-care-process hypothesis

## Proposed relationship
Among adults with a documented HCC diagnosis and a valid admission time, an ordered 7-day laboratory trajectory may add held-out predictive information for a subsequent, non-routine inpatient procedure beyond an admission snapshot and measured care-process indicators. The primary contrast is a procedure-based escalation proxy, not death, ICU admission, or clinical harm.

The hypothesis is predictive and non-causal: it tests whether temporal laboratory information contains information that a snapshot loses. It does not claim that procedures represent deterioration, that treatment causes the endpoint, or that a trajectory is a biological mechanism.

## Grounding and unresolved claim
The strongest currently supported claim is only that the HCC snapshot contains joinable encounter, diagnosis, laboratory, and procedure records with enough timed procedure rows to make a bounded endpoint audit feasible. The unresolved claim is whether the ordered within-assay trajectory predicts a prespecified non-routine post-window procedure better than a snapshot after accounting for treatment indication, care intensity, and documentation intensity.

The leading rival is a care-process artifact: routine HCC treatment, treatment indication, prolonged observation, or documentation intensity may generate both laboratory patterns and procedures. A timing-shifted negative control and routine-procedure comparison are therefore essential.

## Exact available data binding
HCC snapshot: `[source checksum]`.
Catalog [source checksum].

- Encounters: `[internal dataset path]`, table `encounters`; use `患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室`.
- Diagnoses: `[internal dataset path]`, table `diagnoses`; use `患者主索引, 就诊号, 诊断名称, 诊断类型`, restricted to exact `诊断名称=肝细胞癌`.
- Labs: `[internal dataset path]`, table `labs`; use `患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间`, restricted to exact assays 白蛋白, 总胆红素, 国际标准化比值, 甲胎蛋白, 肌酐, 丙氨酸氨基转移酶, 血小板计数, 凝血酶原时间, and 尿素.
- Procedures: `[internal dataset path]`, table `procedures`; use `患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源`.
- Medications: `[internal dataset path]`, table `medications`; use `患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型` for time-zero treatment/process indicators.
- Clinical documents: `[internal dataset path]`, table `clinical_documents`; use `患者主索引, 就诊号, 入院诊断, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过` only for documentation counts.

All detail tables join to encounters on `患者主索引 + 就诊号`; no cross-database join is permitted. The catalog identifies these as ordinary CSV files, not archive members.

## Population, timing, endpoint, and analysis
Cohort: exact HCC diagnosis, nonempty admission time, and one of the four liver-tumor departments `肝肿瘤内科, 肝胆肿瘤与肝移植外科, 肝胆肿瘤内科, 肝肿瘤外科`; the unrestricted exact-diagnosis cohort is a sensitivity analysis.

Feature window: admission through admission + 7 days and no later than discharge. Primary features are within-assay values, time since admission, specimen type, missingness, and time-zero treatment/process indicators. Numeric assays are not pooled across assays because the labs table has no separate unit column.

Primary endpoint: the first timed procedure after day 7 and before discharge whose label is not in a frozen routine-HCC dictionary covering TACE/arterial embolization/arterial chemoembolization, hepatic resection, ablation, transplantation, and documented compound variants. Untimed procedures are excluded and reported as an ascertainment limitation. The broader procedure proxy is secondary. The endpoint dictionary and event counts must be frozen before fitting; clinical experts must adjudicate whether any procedure represents deterioration.

The parent audit reported 105,044 encounter rows, 101,457 valid admission times, 104,554 exact HCC patient/admission keys, 338,040 procedure rows, 321,207 timed HCC procedure rows, 15,774 untimed HCC procedure rows, and 20,052 HCC procedure rows after day 7 and before discharge (6,779 keys). These are feasibility/support counts, not endpoint validity or fitted results.

Baseline: penalized logistic regression using age, sex, department, first available assay values, time-zero routine-treatment and medication indicators, and documentation counts. Alternative: a patient-level ordered sequence/state-space model using the same covariates plus temporal assay information. Split by `患者主索引`, use nested time-aware validation and repeated bootstrap uncertainty. Evaluate held-out discrimination, calibration, and incremental difference. Use post-outcome measurements and within-patient order permutation as negative controls.

The alternative can reveal persistence, ordering, and cross-marker interactions that a snapshot loses. It is not selected for complexity: it is retained only if it tests the substantive uncertainty about temporal information versus process artifact. CPU is appropriate for the tabular baseline and bounded sequence fit; GPU is not required. A larger neural sequence model is deferred unless event support and runtime justify it.

## Falsification and interpretation
Supportive: a nontrivial held-out trajectory advantage for the non-routine endpoint, with uncertainty excluding a prespecified trivial margin, stable across department/documentation/missingness/assay sensitivities, and absent in the timing-shifted control.

Adverse: no improvement, degradation, an advantage confined to routine treatment, disappearance after process adjustment, or a positive timing-shifted negative control.

Inconclusive: sparse non-routine events, unstable dictionary, missing timing, imprecise intervals, or inability to adjudicate clinical meaning. An imprecise null does not refute the hypothesis.

No model has been fitted and no effect or clinical harm has been estimated. The source lacks separate lab units, validated death/ICU fields, and independent clinical adjudication. The future solver must newly fit both models, freeze the endpoint dictionary, estimate held-out performance and uncertainty, and report conclusions linked to computed outputs.

## Evidence context
[K1] Yang et al. (2026) reported that routine admission bilirubin, direct bilirubin, AST, and INR predicted day-7 total bilirubin in a small HBV cirrhosis cohort, supporting short-term laboratory response and motivating a snapshot comparator; it does not establish HCC prognosis or causality.

[K2] Bui et al. (2026) reported that stage, microvascular invasion, resection margin, and Child-Pugh status predicted postoperative disease-free survival in a retrospective HCC resection cohort, bounding the claim that static factors are already important; it does not test early inpatient trajectories or escalation.

[K3] Millarch et al. (2026) reported that a temporal EHR model using ordered vitals, labs, and medications predicted mortality across a nonlinear trauma trajectory and outperformed static severity scores, motivating the sequence alternative; it is not HCC evidence and does not transfer automatically.

## Compact bibliography
- [K1] Yang Y et al. *A Nomogram to Predict Day-7 Total Bilirubin in Hepatitis B Virus-Related Cirrhosis: An Early Treatment-Response Assessment Tool.* Infect Drug Resist. 2026. DOI:10.2147/IDR.S611768. Abstract inspected.
- [K2] Bui NT et al. *Prognostic Determinants of Disease-Free Survival After Curative Resection for Hepatocellular Carcinoma: A Retrospective Cohort Study.* Cancer Manag Res. 2026. DOI:10.2147/CMAR.S620097. Abstract inspected.
- [K3] Millarch AS et al. *Dynamic Prediction of Day Mortality in Patients With Trauma Using a Hybrid Neural Network Model: Model Development and Evaluation Study.* J Med Internet Res. 2026. DOI:10.2196/86202. Abstract inspected.
