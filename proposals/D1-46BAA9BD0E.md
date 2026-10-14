> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Provisional HCC hypothesis: temporal laboratory information versus care-process artifact (episode 18)

## Proposed relationship

Among adults with an exact documented diagnosis of 肝细胞癌 (HCC) and a valid inpatient admission time, an ordered 7-day within-assay laboratory trajectory from admission through day 7 may add held-out information about a subsequent, prespecified non-routine inpatient procedure beyond an admission laboratory snapshot and measured treatment/documentation-process variables.

The primary estimand is predictive: compare a time-aware model with a snapshot model on the same patient-level held-out split. The procedure is a computable escalation proxy, not death, ICU admission, decompensation, clinical harm, or a validated treatment endpoint. The direction and magnitude are not assumed.

## Strongest supported claim and unresolved claim

The strongest claim currently supported by the available evidence is only that the frozen HCC snapshot contains joinable encounter, diagnosis, laboratory, and procedure records, with timed procedure rows that make a bounded endpoint audit feasible. The unresolved claim is whether temporal laboratory information predicts a later non-routine procedure after accounting for routine HCC treatment, care intensity, and documentation practice. A positive result would justify expert review of temporal monitoring; it would not establish a biological mechanism, causality, or clinical benefit.

## Exact data binding

Use HCC snapshot `[source checksum]`. All source files are read-only.

- Encounters: `[internal dataset path]`, table `encounters`; required columns `患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室`.
- Diagnoses: `[internal dataset path]`, table `diagnoses`; required columns `患者主索引, 就诊号, 诊断名称, 诊断类型`. Restrict the primary cohort to exact `诊断名称=肝细胞癌`.
- Labs: `[internal dataset path]`, table `labs`; required columns `患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间`. Use a prespecified within-assay liver, coagulation, renal, and tumor-marker mapping; do not pool numeric results across assays because the source has no separate unit column.
- Procedures: `[internal dataset path]`, table `procedures`; use its documented procedure label and timing columns, joining only on `患者主索引 + 就诊号`. The solver must freeze and version a routine-HCC-treatment dictionary and report ambiguous, untimed, duplicate, and invalid-time records.

All detail tables are many-to-one to encounters on `患者主索引 + 就诊号`; verify duplicate keys before aggregation. Use only within-participant time intervals. The nominal vitals and transfers tables are identifier-only, and the front-page table is not a usable clinical feature source.

## Experiment and falsification

Define the index as the first valid admission for each patient/admission with exact HCC diagnosis and a valid `入院时间`. The feature window is admission through admission+7 days. The primary outcome is a procedure with a valid start time strictly after admission+7 days and before discharge, whose procedure label is outside the frozen routine dictionary. Exclude procedures without valid timing from the primary endpoint and report them as ascertainment limitations.

Baseline: a regularized logistic or survival model using admission snapshot values, age/sex, admission department, pre-window treatment/procedure indicators, and documentation intensity. Temporal alternative: a prespecified time-aware representation of the same within-assay measurements, including time since admission, slope/level and missingness indicators, fitted without post-window information. Compare patient-level held-out predictions with bootstrap or repeated-split uncertainty, calibration, discrimination, and a prespecified minimum clinically meaningful margin.

Negative controls: (1) compare the same temporal representation against a timing-shifted procedure endpoint that cannot plausibly be downstream of the feature window; (2) compare routine-treatment procedures with non-routine procedures; and (3) permute or shift trajectory order while preserving marginal values. A supportive result requires incremental held-out information for the non-routine endpoint, a smaller or absent routine-endpoint increment, and no increment in the negative control. An adverse result is no reproducible increment or a timing/control artifact. An inconclusive result is an imprecise interval, inadequate endpoint support, unresolved assay mapping/units, or failure of the frozen dictionary audit.

## Missing evidence and limits

The following are not established and must not be inferred: the clinical meaning of the procedure endpoint; whether it represents deterioration or harm; laboratory units and cross-assay comparability; a validated routine-procedure dictionary; external validation; and any causal or treatment claim. Clinical adjudication, validated outcome data, and expert review are required for those stronger conclusions. No model has been fitted and no effect estimate is claimed.

## Method comparison and deliverable

The simple baseline is scientifically adequate for testing whether temporal ordering adds information. The substantive alternative is a time-aware representation of the same measurements; it can reveal persistence, within-assay change, and missingness patterns that a snapshot discards. A neural sequence model is deferred because the current question is answerable with a transparent temporal representation and because assay units, endpoint semantics, and event support remain unresolved; it could be revisited only if those dependencies are resolved and the temporal alternative shows reproducible incremental information. The solver must newly fit both models, estimate held-out uncertainty, run the controls, and produce an output-linked conclusion classified as supportive, adverse, or inconclusive.
