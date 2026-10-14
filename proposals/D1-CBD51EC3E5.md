> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Provisional HCC trajectory-versus-care-process hypothesis

## Proposed relationship
Among adults with an exact inpatient HCC diagnosis and a valid admission time, an ordered 7-day laboratory trajectory will add held-out information about a subsequent, prespecified non-routine procedure beyond an admission snapshot and care-process indicators. The primary endpoint is a procedure after admission+7 days and before discharge whose label is not in a frozen routine-HCC-treatment dictionary. This is a predictive/proxy hypothesis, not a claim that the procedure represents deterioration, death, ICU admission, or clinical harm.

## Evidence and exact source locations
The HCC catalog binds the question to the following read-only files and tables:
- `[internal dataset path]`, table `encounters`, columns `患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室`.
- `[internal dataset path]`, table `diagnoses`, columns `患者主索引, 就诊号, 诊断名称, 诊断类型`, with exact `诊断名称=肝细胞癌`.
- `[internal dataset path]`, table `labs`, columns `患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间`, restricted to the prespecified liver, coagulation, renal, and tumor-marker assays.
- `[internal dataset path]`, table `procedures`, columns `患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源`.
- `[internal dataset path]`, table `medications`, columns `患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型`.
- `[internal dataset path]`, table `clinical_documents`, columns `患者主索引, 就诊号, 入院诊断, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过`.

All detail tables join to encounters on `患者主索引 + 就诊号`; no cross-database join is permitted. The catalog snapshot is `[source checksum]`. The parent audit reported 104,554 exact HCC patient/admission keys, 321,207 timed HCC procedure rows, 15,774 untimed HCC procedure rows, and 20,052 HCC procedure rows after day 7 and before discharge (6,779 keys); these are support counts, not endpoint validity.

## Uncertainties and missing evidence
The procedure dictionary is not yet frozen; routine HCC treatments, compound labels, and untimed records create selection and ascertainment uncertainty. The dataset lacks separate laboratory units, validated death/ICU fields, and independent clinical adjudication. The literature pass is provisional and must be completed with exactly three inspected works before final delivery. No model has been fitted and no clinical effect is claimed.

## Falsifiable test
Fit a snapshot penalized logistic model and a patient-level ordered temporal/state-space model on the same cohort, features, and held-out patient split. Compare held-out discrimination, calibration, and incremental performance with bootstrap uncertainty. Require a nontrivial trajectory advantage for the non-routine endpoint, stability to department/documentation/missingness sensitivities, and disappearance under a timing-shifted negative control. A null, process-only, unstable, or negative-control-positive result is adverse or inconclusive rather than evidence for a mechanism. Clinical meaning requires expert adjudication or another study.
