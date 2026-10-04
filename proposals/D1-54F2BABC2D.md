# Admission-anchored early physiology and a later recorded procedural transition in HCC

## Scientific deliverable

The future solver must construct and lock an adult first-observed HCC-coded admission cohort, a deterministic patient partition, a row-level time audit, and an exhaustive admission-anchored terminal-state outcome that does not require interpreting procedure or order strings. It must fit a transparent baseline (B0), an early-laboratory model (B1), and a useful irregular coupled-state alternative (B2) on the same patients, target, preprocessing policy and split; produce locked probabilities for every primary state; estimate the held-out laboratory increment with uncertainty and calibration; and run timestamp, label, opportunity and missing-time falsifications. It must also run the parent hypothesis as a secondary, tiered plan/procedure-family analysis only when exact dictionaries are frozen and adequately supported. A claim-to-output table must identify computationally checkable statements versus claims requiring clinical adjudication or another study.

This is a substantive repair of [prior hypothesis]. The parent’s H = Delta_Q - Delta_C depends on a sparse and unvalidated mapping of free-text orders and procedures to clinical pathway families and on selecting a clear-plan stratum. This version makes an all-admission, dictionary-independent recorded-transition estimand primary, retains the parent’s discordance contrast as a secondary mechanism estimand, and represents missing procedure times as uncertainty rather than “no care.” It resolves the main documentation/semantic ambiguity without claiming that a recorded row is intent, treatment, or benefit.

## Supported evidence, unresolved question and hypothesis

The verified HCC snapshot contains encounter admission/discharge times, diagnosis strings, numeric laboratory results with native laboratory times, non-drug orders with opening/start/end/status fields, and procedure rows with native start/end fields. The source headers and table metadata confirm these fields and the identity relationship. The available evidence does not establish that an HCC-like diagnosis is pathology-confirmed HCC, that an order is a recommendation or intent, or that a procedure row is completed, indicated, elective, urgent, beneficial, harmful, or caused by the observed physiology. Diagnoses have no native time; clinical documents and pathology have no native time; laboratory units/reference ranges are absent; and procedure start times can be missing.

The unresolved question is:

> Among adults with a first observed HCC-coded inpatient admission, does numeric hepatic/renal information observed during [0,24) hours improve calibrated prediction of the next time-orderable procedure-table transition during [24,72), across every eligible admission, after accounting for admission and pre-admission information and observation opportunity? In a secondary analysis, is any incremental information larger for a later recorded liver-directed-looking procedure without a matching pre-24 recorded order-family signal than for one with such a signal?

The primary hypothesis is a held-out information hypothesis, not a causal treatment hypothesis: B1 will improve outcome-linked multiclass log loss and Brier score over B0 for the admission-anchored terminal-state vector, with a stable direction for the probability of a procedure beginning in [24,72). The protocol-scale relevance threshold for the standardized P1 probability contrast is 0.01 absolute probability points; it is not a clinical utility threshold.

The secondary hypothesis preserves the parent’s ambition in a safer form. If a clinically reviewable procedure/order dictionary is supported, the early-laboratory increment will be larger for a later recorded liver-directed-looking procedure without a matching single-family pre-24 order proxy (Q) than for one with such a signal (C), H = Delta_Q - Delta_C > 0. Q means a recorded mismatch only. It does not mean unexpected, unplanned, inappropriate, treatment failure, recurrence, progression, or a clinical decision discordant with physiology.

## Clinical importance and substantive advance

A later procedural transition can be consequential in HCC care, but this snapshot cannot say why it occurred or whether it was appropriate. The useful uncertainty is whether early recorded physiology contains reproducible information absent from the admission/pre-admission record and whether that signal is concentrated in a documented-workflow mismatch. A positive result would justify prospective chart review and better time-stamped capture of indication, recommendation, scheduling, treatment receipt and outcomes before any decision-support use. A null result would discourage interpreting early laboratory values as a reliable signal for this recorded transition.

The advance is not a small predictive refinement. The primary result remains meaningful when no local procedure vocabulary can support a clinical family label, while the secondary analysis tests the more specific plan-mismatch mechanism without conditioning the whole study on a sparse clear-plan denominator. Missing-time rows become an explicit uncertainty state and sensitivity bound.

## Population, joins and admission anchor

Use HCC snapshot [source checksum]. The catalog is [internal dataset path] with [source checksum].

Join encounters to diagnoses exactly on (患者主索引, 就诊号), after whitespace/encoding normalization only. Include age >=18; valid native 入院时间 and 出院时间; nonnegative stay; admission in [2011-01-01, 2026-01-01); discharge before 2026-01-01; and at least one frozen lexical HCC rule reviewed in fitting/selection data. Because diagnoses has no diagnosis time, this is an encounter-level eligibility label, not onset or confirmation. Select the earliest eligible encounter per 患者主索引, ordered by native 入院时间 and then 就诊号; do not replace an invalid earliest encounter by a later one.

Every eligible admission remains in the primary risk set. Do not condition on discharge after 24/72 hours, a later row being present, a qualifying order, a liver-directed family, or a procedure being early. Report duplicate encounter keys, multiple diagnosis joins, unmatched joins, invalid/ongoing times, overlapping encounters, HCC lexical rule counts and cohort flow. Direct identifiers in encounters (name, ID number, phone, insurance/card and inpatient number) are excluded from derived features.

## Primary admission-anchored terminal outcome

Use procedures.开始时间 only when it parses as a native timestamp and can be compared with admission and discharge. Define mutually exclusive states, with the earliest demonstrable state taking priority:

- P0: a time-orderable procedure row starts in [0,24) hours after admission and before discharge.
- P1: no P0, and the first time-orderable procedure row starts in [24,72) hours after admission and before discharge.
- Uproc: no established P0/P1, but a procedure row has a missing/invalid 开始时间 that could change the [0,72) ordering, or an unresolved same-time/order conflict.
- D0: no P0/P1/Uproc and discharge occurs before 72 hours.
- N0: no P0/P1/Uproc, discharge is not before 72 hours, and no procedure row starts by 72 hours.

A valid procedure start after discharge or after 72 hours is retained for audit but cannot define P0/P1. If an unresolved row coexists with a demonstrably earlier valid P0/P1, retain the valid state and report the unresolved row separately; otherwise Uproc precedes D0/N0. No state means no clinical change, treatment receipt, intent, or outcome quality.

The primary estimand is the standardized locked-test probability of P1 and the full vector {P0, P1, Uproc, D0, N0}. Main incremental estimands are B1-minus-B0 multiclass log-loss reduction, multiclass Brier reduction, per-state calibration, and Delta_P1 = mean[p_B1(P1)-p_B0(P1)]. This is predictive information for a recorded procedural transition, not an intervention effect.

## Secondary family and documented-evidence analysis

Only in fitting/selection data, freeze a versioned clinician-reviewable exact-string procedure dictionary for descriptive families: E (therapeutic hepatic-artery embolization/interventional, potentially including exact TACE terms), A (liver-lesion ablation), S (liver resection), and X (mixed, transplant/other liver-directed-looking or unassignable). Preserve every exact string and exclusion. If the dictionary cannot be reviewed or a family is too sparse, the secondary analysis is inconclusive; the primary outcome is unchanged.

Use orders.开立时间—not 开始时间—to establish only that a matching order row was recorded before the relevant window. In [admission, admission+24) define K when exactly one E/A/S family has qualifying exact order evidence, M for multiple families or potentially therapeutic but unassignable evidence, N for no qualifying family, and U for potentially qualifying text with missing/invalid 开立时间. 医嘱状态, 医嘱期限, 频次, 开始时间 and 结束时间 are audit/sensitivity fields only; none proves intent, scheduling, completion or treatment.

For a time-orderable [24,72) family event, C is family equal to a K proxy and Q is family unequal to it. Keep X, M, N and U separate. The plan-adjusted secondary models add the frozen K/M/N/U proxy to otherwise identical B0/B1 inputs; H is the difference between B1-minus-B0 standardized event probability for Q and C. The primary all-admission result is never replaced by this selected or dictionary-dependent analysis. Report exact terms, order status/timing distributions, duplicate and missing-time rates, K/M/N/U support and all family counts before interpretation.

## Exact HCC data bindings

All source files are ordinary CSVs with archive member ordinary file; there are no archive members to unpack. All joins use (患者主索引, 就诊号) and duplicate/unmatched behavior must be reported.

Primary inputs:

- encounters, schema datasets/hcc/table-b743286cb1249287.json, source [internal dataset path] 患者主索引, 就诊号, 年龄, 性别, 身高, 体重, 就诊时间, 入院时间, 出院时间, 就诊科室. Use age, sex, admitting department, admission/era descriptors and valid admission/discharge times; exclude direct identifiers.
- diagnoses, schema datasets/hcc/table-12710723c3df0c99.json, source [internal dataset path] 患者主索引, 就诊号, 诊断名称, 诊断类型. Use for frozen encounter-level HCC eligibility and diagnosis-type descriptors; there is no diagnosis time.
- labs, schema datasets/hcc/table-38aad8c54471332f.json, source [internal dataset path] 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间. Use numeric 定量结果 and native 检验时间 in [admission, admission+24h), grouped by exact 检验 and retained with 标本类型.
- procedures, schema datasets/hcc/table-d5eae16f8f8093d9.json, source [internal dataset path] 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源. Use only native 开始时间 for primary ordering; retain 手术, 结束时间 and 手术来源 for secondary audit and missing-time bounds.
- orders, schema datasets/hcc/table-6b93dcf0ea823702.json, source [internal dataset path](非药品)_2062526727266216118.csv: 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次. Use 医嘱(非药品) and 开立时间 only for the secondary recorded-evidence tier.

Complete-catalog audit and exclusion reporting must also inspect, without promoting them into the primary endpoint:

- examinations, schema datasets/hcc/table-fd016d2731b9d6c6.json, source [internal dataset path], columns 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 机器型号, 检查号. It has a time field but no validated stage, burden, indication or resectability label.
- clinical_documents, schema datasets/hcc/table-66afca58512c2fca.json, source [internal dataset path], columns 患者主索引, 就诊号, 主诉, 现病史, 既往史, 个人史, 月经史, 婚育史, 家族史, 入院诊断, 入院情况, 入院诊断__duplicate_2, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过. It has no native time and its lexical detector is not validated for diagnosis, intent or plan.
- pathology, schema datasets/hcc/table-0a4ee86a446c605c.json, source [internal dataset path], columns 患者主索引, 就诊号, 病理, 检查所见, 检查诊断, 机器型号. It has no temporal field and cannot time-align confirmation.
- medications, schema datasets/hcc/table-4f6ecaeb6e8f69c2.json, source [internal dataset path], columns 患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型. Native times exist, but indication is unvalidated; audit only.
- vitals, schema datasets/hcc/table-8436de9cba74b8ca.json, source [internal dataset path], and transfers, schema datasets/hcc/table-320c20f732e71789.json, source [internal dataset path], each contain only the identity pair and are identifier-only.
- front_page, schema datasets/hcc/table-38b3224239acc33f.json, source [internal dataset path], contains only the identity pair and is identifier-only.

HCC metadata datasets/hcc/metadata.json records the many-to-one relationships to encounters and snapshot limitations. Sources remain read-only; dictionaries, cohort tables, predictions and audits are derived workspace files.

## Early laboratory inputs and matched alternatives

The exact assay set is albumin (白蛋白), total bilirubin (总胆红素), creatinine (肌酐), platelets (血小板) and one coagulation/prothrombin assay selected only after exact-name support review. Do not merge unlike assay strings, treat 定性结果 as numeric, or compute a validated liver score because units and reference ranges are absent.

B0 uses no early laboratory values. It includes age, sex, admitting department, admission-era descriptors, diagnosis-type descriptors, pre-admission encounter/procedure summaries ending before the index admission, and non-semantic opportunity covariates defined before 24 hours (counts of valid/invalid lab timestamps and total recorded order rows, with missingness explicit). It does not use order/procedure text, P0/P1/Uproc labels, discharge as a predictor, post-24 labs, post-24 orders/procedures, medications or narrative outcome fields.

B1 adds exact-assay early observations from [0,24): first/last value, change, elapsed time, count, distinct timestamps, missingness, density and slope only when at least two valid timestamps exist. B0 and B1 have the same patients, target, split, missingness policy and evaluation. A plan-adjusted B0P/B1P secondary pair adds only the pre-24 K/M/N/U recorded-order tier.

B2 is the substantive learned/mechanistic alternative. It receives the same exact early observations as B1 (and, secondarily, the same B0P/B1P plan proxy), plus each numeric token, exact assay identity, elapsed time, qualitative/missingness indicator and observation gap. It is an interpretable irregular continuous-time coupled-state model with two low-dimensional modelling coordinates labelled hepatic-reserve and renal-stress, assay-specific offsets/noise rather than pooled units, patient shrinkage, irregular observation updates and an explicit observation-intensity component, with state-specific prediction heads. The labels are modelling constructs, not diagnoses or validated physiology. B2 can reveal nonlinear timing, coupled movement and uncertainty that first/last/slope summaries lose; B1 remains the transparent comparator.

## Fitting, split, uncertainty and analysis

Assign every patient deterministically to buckets 0–59 (fit), 60–69 (selection) or 70–79 (locked test); buckets 80–99 are inaccessible. No patient crosses partitions. Fit parameters, dictionaries and frozen assay rules only in 0–59; choose state dimension, regularization, exact assay support, binning and observation-process terms using 0–59 plus 60–69; lock preprocessing before the single evaluation on 70–79.

Report locked-test multiclass log loss, multiclass Brier score, per-state calibration intercept/slope and observed-versus-predicted probabilities in prespecified risk bins; Delta_P1 and all B1-minus-B0 state contrasts; B2-minus-B1 scores/calibration/state changes on the same target/split; secondary family-specific and C/Q/H estimates only where support gates pass; event/state prevalence, valid/missing procedure-time fractions, exact assay support, measurement density, order-tier support and duplicate/unmatched join counts. Use at least 500 paired patient-clustered bootstrap resamples (1,000 preferred), preserving states and the locked split, with a consistent refit or documented locked-prediction procedure. Report intervals for score differences, state probabilities, Delta_P1, H and calibration. AUROC/PR-AUC are descriptive only.

## Falsification and leakage tests

1. Emit a row-level timestamp proof that every primary laboratory value is in [0,24), every P0/P1 procedure state uses native 开始时间 before discharge, and no discharge, post-24 observation, outcome label or later order enters a primary predictor.
2. Permute within-patient exact-assay laboratory timestamps while preserving values, assay identity, counts and missingness; additionally permute values within assay. A physiology-specific increment should attenuate.
3. Permute primary terminal labels within admitting-department/admission-era strata, preserving state frequencies; outcome-linked gain should disappear.
4. Remove/add pre-24 lab/order opportunity variables, valid-time fractions, gap and density terms. Strong attenuation identifies observation opportunity rather than physiology.
5. Test duplicate/same-assay/same-time handling, midnight-boundary and missing procedure-time rules. Bound Uproc by assigning unresolved rows to earliest plausible P0/P1 versus no-event states, and report analysis excluding Uproc.
6. Run exact-assay leave-one-out and, only secondarily, procedure-family/order-string leave-one-out and dictionary perturbation.
7. Permute the secondary P0-order tier within department/era, preserving tier frequencies. Survival of H weakens the plan-mechanism interpretation.
8. Use a same-source routine/central-line/venipuncture workflow endpoint as a negative-control workflow analysis, never assumed clinically null.
9. Report a complete-case K-only secondary diagnostic against the all-admission primary; it cannot replace the primary risk set.
10. Retain the parent’s [72,144) competing-risk family analysis as a labeled secondary audit only; it cannot rescue a failed primary or be silently pooled with [24,72) outcomes.

Primary interpretation is materially weakened if B1’s gain persists after laboratory timestamp/value permutation, disappears when opportunity is represented, is dominated by one assay/service/era, is driven by Uproc, or fails terminal-label permutation. Secondary plan interpretation is weakened by null/opposite H, survival after tier permutation, domination by U-order/unresolved rows, or dictionary instability.

## Supportive, adverse and inconclusive outcomes

Supportive primary evidence requires a complete cohort/time audit, adequate state support, calibrated B1, positive held-out B1-versus-B0 log-loss/Brier improvement with a two-sided interval excluding zero, stable Delta_P1 direction, attenuation under lab and terminal-label permutations, and no material dependence on Uproc or observation opportunity. Stronger model support requires B2 to improve calibrated state prediction beyond B1 and preserve the direction; B2 is not required to win if B1 captures the scientific signal.

Adverse evidence is a null/opposite or poorly calibrated increment, persistence under timestamp/label permutation, disappearance after opportunity adjustment, dominance by one assay/service/era, or instability under missing-time handling. It weakens this recorded-data hypothesis but does not prove physiology clinically irrelevant.

Inconclusive evidence includes dominant Uproc or N0 with inadequate P1 support, sparse exact assays or secondary families, fewer than 100 locked P1 events for a stable relevance contrast, wide intervals, nonconvergence, unresolved dictionary semantics, missing procedure times that cannot be bounded, incomplete local capture, or unsupported secondary strata. Negative findings remain valuable.

## Clinical evidence limits, compute and completion

A supportive result means only that early recorded laboratory information improves prediction of a subsequent recorded procedure-table transition in this HCC snapshot. It does not establish HCC confirmation, tumor stage/burden/vascular invasion/resectability, performance status, indication, recommendation, scheduling, treatment receipt, intent, appropriateness, benefit, harm, recurrence, progression, mortality, transplant, complications, reason for discharge or reason for plan change. It cannot establish that acting on the prediction improves care. Those claims require time-stamped clinical adjudication, treatment/outcome linkage, complete outside-hospital capture, prospective chart review and external validation.

Clinical documents lack native time and their lexical detector is unvalidated. Examinations and pathology can be audited but cannot time-align diagnosis, stage or indication. Medications have times but unvalidated indication. Vitals, transfers and front_page are identifier-only. The proposal does not claim expert dictionary review or clinical adjudication has already occurred.

B0 is transparent and CPU-first; B1 is the auditable laboratory increment; B2 is selected because irregular timing and coupled movement may be lost by summaries, not for complexity or GPU use. A GRU/temporal-attention model is deferred until B2 residuals show reproducible ordering error after opportunity adjustment. Text/image/multimodal methods are deferred because HCC images are unavailable, clinical documents lack native time and validated extraction, and the cancer main article/complete STAR Methods are unavailable. A validated liver score awaits units/reference ranges and adjudicated outcomes. A causal treatment-effect study is not identified.

Discovery used read-only source-header/schema inspection and a bounded streaming audit of the five primary source files; full cohort construction, B2 fitting and 500-bootstrap duration were not measured. The future solver planning envelope is up to 16 CPUs, 262144 MiB, 8 allocated A100 GPUs and 28800 seconds from inputs.json; these are unverified planning limits. CPU is sufficient for chunked aggregation, multiclass fits and bootstrap. B2 is CPU-first; an allocated GPU is optional for repeated irregular-state fitting, using only cuda:0 inside an allocated job that explicitly moves model/tensors to that device. The full study is not claimed to have been fitted.

The scientific deliverable is complete only when the solver emits the frozen cohort/rules, exact source and join audit, exhaustive primary states with row-level provenance and missing-time bounds, B0/B1/B2 locked predictions, scores/calibration/Delta_P1 with uncertainty, secondary C/Q/H outputs if support passes, all falsifications, and a claim-to-output/evidence-limit table. Readiness cannot establish clinical truth.

## Reference disposition and provenance

The three demonstrations were used as method context, not as a fixed topic or reproduction target. The natural-history materials support dated structured-history modelling and held-out calibration; local UK Biobank/Danish validation and genetic inputs are unavailable. The Bayesian materials support an EHR-only irregular latent-trajectory adaptation; this proposal changes target, assumptions and inputs and does not reproduce the paper’s genetic analysis. Only the cancer supplement was available for modality/ablation context; the main cancer article and complete STAR Methods remain unavailable, and no local HCC images exist. No stronger claim than the inspected files supports is made.

The HCC expert-seed guide was inspected; no HCC seed is imported. Source rows remain read-only and all derived files, dictionaries, audits and model outputs belong in the workspace. The unused parent estimand and secondary branches remain preserved as explicit alternatives.
