# HCC process-conditioned assay innovation after day-42 TACE

Status: design-only substantive child of `[prior hypothesis]`. No cohort fit, model result, or favorable clinical finding is claimed. The parent’s landmark, endpoint, temporal split, channel ablations, support gates, and source bindings are retained. This child adds one bounded representation test: whether assay content not explained by the recorded pre-assay observation/care process adds held-out information for the same operational event.

## Scientific opening, claim boundary, and advance

The parent establishes an important unresolved boundary but its raw `A` versus `A+S` contrast can still mix two kinds of information: assay content and the process that makes a result available. A patient scheduled for close follow-up can have more orders, encounters, lab opportunities, and an eventual repeat-TACE code; the same process can also determine which assay values are recorded. A better sequence score does not resolve that ambiguity if it uses timing or missingness.

The strongest available evidence supports only narrower statements. [K1] reports a selected imaging-rich multicenter repeat-TACE prognosis model, but external AUCs fell and the authors identify generalization concerns. [K2] makes the clinical measurement boundary explicit: HCC treatment response depends on imaging modality and criteria, including necrosis and mRECIST/RECICL, not an arbitrary laboratory or procedure row. [K3] shows how documented imaging response comparisons remain vulnerable to missing outcomes, ascertainment, exposure classification, and treatment-selection confounding. None establishes that a routine assay signal is portable beyond care workflow, and none validates this snapshot’s exact-code endpoint.

The unresolved, falsifiable claim is narrower:

> Among patients eligible at the day-42 landmark, does the content of the eight recorded assay labels that is not predictable from pre-assay observation and care process add patient-held-out information about a later locally recorded exact-code repeat TACE, beyond the parent’s `A=M0+P_obs+P_care` channel?

This is a predictive/descriptive estimand for a recorded event, not a causal, mechanistic, response, benefit, or treatment-policy claim. The substantive advance is an explicit process-conditioned assay-innovation contrast with cross-fitted nuisance functions, so “assay information” is no longer defined solely as whatever improves a model after process features are added. It does not declare process-predictable assay content clinically irrelevant: clinically meaningful state can be predictable because clinicians measure it. It asks whether a less process-explained component is reproducibly useful.

The leading rival remains workflow/timing: measurement opportunity, planned follow-up, severity-driven care, or a near-term retreatment pathway creates both process marks and repeat-code probability. A secondary rival is current severity incompletely represented in `M0`. A positive innovation after the stated controls supports only reusable recorded content for this operational event. It does not separate biology from residual severity and cannot establish intent to retreat.

## Scientific deliverable

The required new deliverable is a newly fitted, leakage-audited process-conditioned assay-innovation sensitivity:

1. a frozen nuisance specification and support audit for assay observation and assay content;
2. cross-fitted development-only nuisance predictions and test innovations;
3. paired held-out predictions for `A`, raw `B=A+S`, and `B_PCAS=A+R`;
4. weighted log-loss/Brier/calibration estimates with patient-bootstrap uncertainty;
5. timestamp, missingness, permutation, and lead-time falsification outputs; and
6. a claim-output map that labels computationally checkable conclusions versus clinical-adjudication dependencies.

Completion is these outputs plus an honest supportive, adverse, or inconclusive interpretation. Readiness, a successful fit, or an incremental score alone is not completion.

## Population, outcome, and temporal boundaries (unchanged)

Index is the first row in the supplied HCC snapshot for which Unicode-case-folded, trimmed `手术` equals exactly `tace`, with nonmissing `患者主索引`, `就诊号`, and `开始时间`. “First” means first in this snapshot, not first-ever TACE. Exact duplicate patient/start rows are collapsed for event counting and retained in a duplicate audit. Other procedure strings are not primary TACE events; strict-code rows with missing `开始时间` are audited but excluded from timed analyses.

Exclude any later strict-code TACE with `0 < Delta < 43` days. Require all-source observation through `index_start + 42 days`. The primary outcome is the first later unique patient/start strict-code TACE with `43 <= Delta < 181` days. Follow-up ends at that event, all-source `obs_end`, or day 181. An untimed repeat is not a timed negative. Integer hazard bins are [43,90] and [91,180]. Fixed sensitivities are [43,90), [91,181), day-28 process truncation, removal of the last seven feature days, alternate valid `obs_end`, and the parent’s undated-history audit. No predictor uses `obs_end`, future event rows/counts, post-index exact-code TACE, or the outcome.

Development is the earliest 80% of index dates and untouched test is the latest 20%; no patient crosses the boundary. Use the parent’s five grouped development folds, frozen before outcome scoring. All dictionaries, numeric transforms, nuisance fits, censoring/observation weights, model fits, and cutpoints are development-only. Score the untouched test once. Parent support gates remain binding: unsupported strata stay `unsupported/inconclusive`, are never merged or deleted, and cannot be rescued by a learned model.

## Exact HCC source bindings and availability

The authoritative catalog is `[internal dataset path]`, [source checksum]. The HCC snapshot is `[source checksum]`. Every HCC source is an ordinary CSV (`member=null`); no archive member is used. Source files remain read-only. The checked headers and catalog schemas are bound as follows.

| Catalog table and schema | Read-only source, source SHA-256 | Required fields, join and time use |
|---|---|---|
| `procedures`, `datasets/hcc/table-d5eae16f8f8093d9.json` | `[internal dataset path]`, `[source checksum]` | `患者主索引, 就诊号, 手术, 开始时间, 结束时间` and `手术来源`; `开始时间` defines index/events and valid `结束时间` contributes to `obs_end`. Exact TACE rows never enter predictors; non-TACE dated rows are `P_care`. |
| `encounters`, `datasets/hcc/table-b743286cb1249287.json` | `[internal dataset path]`, `[source checksum]` | Join all child tables on `(患者主索引, 就诊号)`; use `年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室` for `M0`, `P_obs`, `P_care`, and `obs_end`. Names, identity numbers, phone, insurance/card and other direct identifiers are excluded. |
| `examinations`, `datasets/hcc/table-fd016d2731b9d6c6.json` | `[internal dataset path]`, `[source checksum]` | Use `患者主索引, 就诊号, 检查, 开始时间` as timed observation/opportunity marks. `检查所见` and `检查诊断` are non-adjudicated narrative text and are not response labels or PCAS inputs. `检查号` and machine number are not used as clinical state. |
| `labs`, `datasets/hcc/table-38aad8c54471332f.json` | `[internal dataset path]`, `[source checksum]` | Use `患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间`. `检验时间` is assay time. The eight exact labels are 甲胎蛋白, 白蛋白, 前白蛋白, 总胆红素, 直接胆红素, 丙氨酸氨基转移酶, 血小板, 血小板计数. Preserve numeric, qualitative and inequality/censoring information; there is no unit or reference-range column. |
| `medications`, `datasets/hcc/table-4f6ecaeb6e8f69c2.json` | `[internal dataset path]`, `[source checksum]` | Use `患者主索引, 就诊号, 用药, 开始时间, 结束时间, 用药方式, 药品类型`; valid starts/ends are dated care-process marks and contribute to `obs_end`. |
| `orders`, `datasets/hcc/table-6b93dcf0ea823702.json` | `[internal dataset path]`, `[source checksum]` | Use `患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱状态, 频次`. `开立时间` is order availability; other times count only if no later than the feature cutoff. Orders are process/opportunity inputs, not assay values. |
| `diagnoses`, `datasets/hcc/table-12710723c3df0c99.json` | `[internal dataset path]`, `[source checksum]` | Use `患者主索引, 就诊号, 诊断名称, 诊断类型`; there is no event-time field. Use only matched-encounter pre-index counts for `M0`; never define follow-up or a post-index event from this table. |
| excluded longitudinal tables | `[internal dataset path]`, SHA `[source checksum]`; `[internal dataset path]`, SHA `[source checksum]` | No valid event time, so no time imputation. Identifier-only vitals, transfers, and front-page tables contain no usable payload for this question. Images, waveforms, units, reference ranges and outside-care data are unavailable. |

The composite patient/visit join is used only to assign child records to an encounter; modeling and bootstrap units are patients. Duplicate counts, missing times, label exactness, numeric-scale/calendar drift, and row availability are audited before fitting. No private row or clinical note is sent to public search.

## Inherited channels retained as primary context

Use the parent’s disjoint channels and all six primary ablations on the same split and person-day rows:

- `M0`: pre-index age, sex, department and encounter/admission history; matched-encounter pre-index diagnosis/procedure counts; pre-index summaries of the eight assays.
- `S`: the eight assay labels’ post-index numeric values and qualitative/inequality flags in (0,42], plus valid assay-specific pre-index change; no request or missingness indicators.
- `P_obs`: dated encounter, examination, order, medication and lab opportunity/missingness counts and timing in (0,42], without assay values or result flags.
- `P_care`: dated non-TACE procedures, non-drug orders, medication starts/ends and department/visit process marks, without assay values.
- `A=M0+P_obs+P_care`; `B=A+S`.

Fit `M0`, `M0+S`, `M0+P_obs`, `M0+P_care`, `A`, and `B` first. The parent’s overall `loss(A)-loss(B)` remains the primary state-versus-process context. PCAS is a prespecified secondary representation analysis, not a replacement estimand or a reason to omit an adverse parent ablation.

## Process-conditioned assay innovation (PCAS)

### Exact assay target and cutoff

For patient i and index start `t0`, the assay cutoff is exactly `c=t0+42 days`; the admissible assay window is strictly `t0 < 检验时间 <= c`. For each of the eight exact `检验` labels j:

1. collapse exact duplicate rows with the same patient, visit, label, timestamp, result fields and specimen type, retaining a duplicate audit;
2. select the latest valid timestamp `t_{ij}` in the window;
3. if multiple nonduplicate rows for j share `t_{ij}`, retain a deterministic within-label summary: median of parseable numeric values, and the complete set of qualitative/inequality tokens; do not mix labels or impose a clinical threshold;
4. define the raw target `Z_{ij}` as the resulting numeric value/rank component, qualitative category indicators, inequality/censoring indicators, and (when a valid pre-index value exists in [-365,0)) the assay-specific change component.

Numeric transforms are label-specific, development-fold robust/rank scaling only. The target is not “normal” versus “abnormal”: no unit conversion, reference range, biological name, or cross-assay threshold is available or allowed. Patients without a recorded j in the window have no imputed assay content in the innovation channel. Their observation/missingness remains in `P_obs` and in the parent’s observation-weight audit.

### Exact process inputs for nuisance fitting

For every selected assay record j at time `t_{ij}`, define `P_{ij}(t^-)` from information strictly earlier than `t_{ij}`:

- `M0), elapsed time from index, prior assay-label counts and prior dated assay opportunities, but never the current assay’s value/result;
- encounters: department, age/sex where already part of `M0`, visit/admission/discharge times, distinct visits and gaps;
- examinations: exact `检查` tokens and `开始时间` strictly before t, as opportunity marks only; no free-text findings/diagnosis;
- orders: exact non-drug order token, `开立时间`, and valid start/end times strictly before t;
- medications: exact medication/type/route token and valid start/end times strictly before t;
- procedures: non-TACE `手术` and valid start/end times strictly before t; the index and any later exact-code TACE are excluded;
- labs: prior label/opportunity/specimen/time marks with `检验时间 < t`, but no numeric, qualitative or inequality result from any assay at or after t;
- diagnoses only through matched-encounter pre-index counts because the table has no valid event time.

A current lab row, any same-timestamp assay row, any future process mark, `obs_end`, repeat-TACE information, censoring outcome, or post-cutoff row is prohibited in `P_{ij}(t^-)`. A feature-leakage report must enumerate every field and its timestamp rule.

### Cross-fitted nuisance and innovation construction

Use two fixed nuisance stages, fitted only in development:

1. **Observation nuisance.** For each label j and each fixed 7-day window (0,7], (7,14], …, (35,42], fit a regularized logistic model for whether j is observed by that window from `M0` and process marks available before the window. This estimates the opportunity/missingness process but its prediction is not included in `R`; opportunity remains `P_obs`.
2. **Content nuisance.** Among observed selected j records, fit fixed-penalty ridge/multinomial models for the numeric/rank component, qualitative category, inequality/censoring component, and valid pre-index change, conditioned on `P_{ij}(t^-)`, label and elapsed time. No outcome, repeat code, censoring status, future row, or outcome-derived tuning is allowed.

For each development fold, fit nuisance models on the other four development folds and generate out-of-fold `m_hat` for the held-out fold. For untouched test, fit the nuisance models once on all development patients and apply them without refitting. Dictionaries, category vocabularies, scaling and penalties are frozen in the corresponding training data. The innovation is:

- numeric/rank residual `R=Z-m_hat`;
- qualitative and inequality one-hot residual `R=onehot(Z)-m_hat`;
- valid change residual `R_delta=DeltaZ-m_hat_delta`.

Set `R=0`/structurally absent when j is unobserved; do not add an observation indicator, missingness flag, predicted observation probability, or assay timestamp to `R`. These process signals remain in `P_obs`. The test feature file must contain patient ID only as an internal join key, assay label/component, selected assay time, observed flag for audit, `R), nuisance fold/training boundary, and no outcome columns; the observed flag is forbidden in the prediction matrix.

The core PCAS comparison is `B_PCAS=A+R`. Report raw `A
ightarrow B` and process-conditioned `A
ightarrow B_PCAS` side by side. A null PCAS contrast does not prove that process-predictable assay state lacks clinical value; it means this design cannot separate that component from the recorded process.

## Models, target, uncertainty, and alternative representation

The transparent confirmatory model is pooled-logistic discrete-time hazard regression for days 43–180 with the parent’s fixed low-degree time spline/day bins, fold-fitted imputation/scaling/dictionaries and elastic-net penalty. Fit the six inherited ablations plus `B_PCAS`. The target is the first later strict-code repeat TACE with all-source right censoring. Primary metric is paired patient-level all-source IPCW weighted log loss over at-risk intervals; secondary metrics are weighted Brier/integrated Brier, calibration slope/intercept, AUROC and AUPRC. Report ordinary and weighted analyses separately.

The primary context remains the parent’s support-gated `Delta_state=loss(A)-loss(B)`. The PCAS sensitivity is `Delta_PCAS=loss(A)-loss(B_PCAS)`. Positive means lower held-out loss after adding the named channel. Use patient bootstrap preserving person-days, weights and paired predictions. Keep the parent’s frozen support thresholds, effective sample size/weight-tail checks, early/late horizon labels, five transport axes, and simultaneous max-t family. PCAS, sequence, permutation, seed and calendar outputs are secondary and cannot rescue a failed primary support gate.

The learned alternative is a compact one-layer time-aware GRU (hidden size 64; fixed three development seeds) over the same -365 through +42 event stream: event category/label, audited numeric value, qualitative/inequality flag, relative time, elapsed time since prior event, and channel tag. Use the same `M0/P_obs/P_care/S` ablations and an innovation-token variant replacing assay content with `R`, with the same day-42 target, temporal split, censoring/observation weights, metrics, paired patient bootstrap and support rules. It could reveal ordered trajectories, transient deviations, cross-assay interactions and irregular timing that latest-value/change summaries lose. That information could matter scientifically if it remains after process controls; a score gain alone cannot adjudicate workflow.

The GRU is deferred from the confirmatory conclusion because its extra flexibility can encode timing/missingness, its per-stratum behavior is harder to audit, and an incomplete fit would not answer the process/state question. Revisit it only after the transparent PCAS pipeline has complete overall support, finite weights, auditable nuisance overlap and artifact controls that are not positive. A failed GRU is not evidence against assay innovation.

Approximate future solver envelope: the transparent ablations plus PCAS should be a CPU job using about 8 CPUs/32 GiB and roughly 1–3 hours after one chunked source scan; this is a planning estimate, not measured. The compact GRU is a separate optional 1-GPU job, about 2–6 hours for three fixed seeds, also unverified. The deployment documents permit allocated A100 use, but GPU use is a feasibility tradeoff, not a scientific requirement. The compiler must reconcile estimates with the configured solver limits; this discovery branch does not launch solver fitting.

## Falsification controls

Run each control with the same frozen split, nuisance folds, support rules, weights and held-out outcome scoring.

- **Process-matched value/flag permutation:** permute assay content within exact label, calendar window, assay-observation propensity decile, and pre-index support block while preserving each patient’s process schedule. A comparable positive `Delta_PCAS` is adverse to a state-content interpretation.
- **Process-only pseudo-state:** use held-out process-model predictions without observed assay content. It must not add beyond `A`; a positive gain identifies residual process/measurement-model leakage.
- **Timestamp control:** permute assay timestamps within patient while preserving result multisets and process counts, and separately include timestamp-only summaries without assay content. A retained gain is timing-compatible, not state evidence.
- **Missingness control:** match or weight on assay observation opportunity and compare `A
ightarrow B_PCAS` after the parent’s observation weighting. If the gain disappears only after this control, label it observation/missingness-compatible.
- **Lead-time controls:** recompute with process and assay cutoff at day 28, and with the last seven days removed from the day-42 window. A gain confined to (35,42] or disappearing after the removal is compatible with near-term scheduling/planned-retreatment workflow.
- **Negative label control:** permute development assay content labels or outcomes within the frozen temporal blocks and score against untouched true test outcomes. Any systematic gain indicates implementation leakage.
- **Timing/data-boundary controls:** repeat the parent’s alternate `obs_end`, undated-TACE history and early/late horizon sensitivities; no control can be selected after seeing a favorable result.

A supportive pattern requires positive raw `Delta_state` and positive `Delta_PCAS` on held-out weighted loss, calibrated direction, agreement of ordinary/weighted estimates, persistence after last-seven-day removal, and null-like process-only, timestamp/value-permutation and label-permutation controls. This supports reusable recorded assay content for the operational event and justifies prioritizing a study linking assay values to imaging/intent; it does not establish biology.

An adverse pattern is a matched process-only or permuted gain, disappearance after observation weighting or lead-time removal, or a PCAS gain confined to one unsupported/high-opportunity/calendar cell. That directs effort toward scheduling, order, intent, outside-care and measurement capture rather than assay-state interpretation. It is not evidence that the assays are clinically meaningless.

An inconclusive pattern is sparse assay support, scale/calendar drift, non-overlap, unstable nuisance fits, finite-weight failure, wide intervals, unsupported strata, or an incomplete GRU. A negative but imprecise estimate is not refutation. Conclusions must cite the exact loss, calibration, support and control rows; no favorable stratum may replace a failed overall gate.

## Unavailable clinical evidence and interpretation boundary

This snapshot does not supply adjudicated imaging response, tumor burden/necrosis, treatment intent, planned versus rescue TACE, outside-care procedures, death/transplant, harms, costs, assay units/reference ranges, complete specimen context, or expert current-severity review. Examination narrative is not a validated response abstraction, and no image payload is available. Therefore the experiment cannot establish a treatment effect, mechanism, tumor response, treatment necessity, clinical utility, or a rule to give/withhold/repeat TACE. Those claims require clinical adjudication, missing linkage, expert review, or a new prospective/external study.

The clinically consequential next decision is data acquisition: proceed to imaging/intent/outside-care adjudication only if raw and PCAS innovations survive process/timing controls with adequate support; prioritize workflow/intent linkage if only raw assay state helps; defer if precision or scales are inadequate; abandon assay-state validation if adequately supported process and permutation controls repeatedly match the innovation.

## Alternatives not chosen and revisit evidence

- Chosen transparent pooled-logistic hazard: its fixed estimand, paired ablations, support table and coefficient/loss audit directly expose the scientific comparison.
- Chosen PCAS: it is the smallest new analysis that tests content beyond pre-assay process at fixed endpoint and split.
- Deferred compact GRU: retained as a matched sensitivity because ordered trajectories may reveal information summaries lose, but deferred from the decision until PCAS and artifact checks are complete.
- Not chosen larger transformers or continuous-time point-process models: they add timing flexibility without an independent observation/intent label and would make the central rival harder to audit.
- Not chosen causal treatment-policy, mediation, or response modeling: intent, imaging, outside-care and valid treatment timing are unavailable. Additional complexity cannot repair those missing dependencies.
- Not chosen free-text examination modeling: `检查所见`/`检查诊断` lack validated adjudication and could import response-label leakage.

Revisit the learned model if PCAS has complete support and the GRU can be run inside the approved envelope; revisit imaging/intent linkage if PCAS is positive and falsification controls are null-like; revise toward workflow measurement if PCAS is null but raw state is positive; abandon this direction if adequately supported process-only and permutation controls match raw and PCAS state repeatedly.

## Three inspected works

[K1] Dai et al. was inspected in relevant full text. It supports the closest imaging-rich repeat-TACE prediction precedent and bounds generalization; this child adds a routine assay/process representation test rather than reproducing it.

[K2] Tsurusaki et al. was inspected abstract-only. It bounds the response measurement claim: imaging criteria and necrosis matter, so this operational endpoint cannot be called response.

[K3] Minh et al. was inspected abstract-only. It supplies the consequential ascertainment/missingness/selection rival that motivates the explicit falsification controls.

The hash-linked UTF-8 evidence files and receipts are in `key-references.json` and the three files under `evidence/`; exactly three works are attached.
