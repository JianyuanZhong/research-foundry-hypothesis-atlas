# Day-42 HCC: recorded assay state versus a pre-outcome review-workflow proxy

Status: substantive child of `[prior hypothesis]`. Design only. No cohort fit, clinical response label, or positive result is claimed.

## Scientific deliverable and repaired boundary

The parent question is retained:

> Among patients observable at day 42 after a first locally recorded exact-code TACE, does the recorded assay-state channel add patient-held-out information about a later exact-code repeat-TACE record beyond matched observation and care-process information?

The unresolved boundary is now operationalized. A pre-outcome order–examination pathway will be measured as an observation/review opportunity proxy, and a non-TACE procedure endpoint will be used as a negative-control-like care-process outcome. Neither is adjudicated imaging response. The primary endpoint remains the exact locally recorded procedure event, because this snapshot has no validated response or intent field.

The actual deliverable is newly fitted, leakage-safe models and weights on the frozen development patients, frozen proxy and negative-control definitions, held-out paired predictions/losses, subgroup support audits, calibration and uncertainty intervals, falsification outputs, and a claim-output map. Completion is these auditable artifacts, including an explicitly inconclusive result when a gate fails; completion is not confirmation of the state hypothesis.

The parent’s primary overall patient-held-out state contrast remains the computational anchor:
`D_state = loss(A) - loss(B)`, where `A=M0+P_obs+P_care` and `B=A+S`; positive means the added recorded assay-state channel lowers loss. This is predictive/descriptive evidence about recorded information, not a causal assay effect, tumor-response estimate, treatment-benefit estimate, or treatment rule.

The new decision-facing estimands are:

1. `D_state|W=1` and `D_state|W=0`: the same paired held-out assay increment within supported strata of the pre-outcome review-opportunity proxy `W_packet). These are conditional predictive contrasts, not causal effects of review.
2. `D_state,residual = loss(A*)-loss(B*)`, where `A*` contains M0, the explicitly defined proxy and process features with direct proxy duplicates removed, and `B*=A*+S`. This tests whether assay state retains information after the proxy is made visible as a named channel.
3. `D_NC = loss(A_NC)-loss(B_NC)` for the first non-TACE procedure in the same [43,181) horizon. This is a negative-control-like operational endpoint: a state increment of similar size for generic non-TACE care would support a general severity/measurement-process explanation, but a null result cannot prove biological specificity.

The next clinical-data decision is therefore explicit: if a supported assay increment persists after `W_packet`, lead-time controls, and process/value permutations, prioritize linkage to adjudicated imaging, treatment intent and outside-care events; if the proxy/process or negative-control-like endpoint accounts for the increment, prioritize scheduling, indication and workflow data; if support or precision fails, do not escalate either interpretation.

## Evidence and the competing explanations

[K1] shows that imaging radiomics/deep learning plus clinical features can predict repeat-TACE prognosis, but its external AUCs fall and the authors note overfitting and scanner/generalization limits. It uses CT and formal mRECIST assessment unavailable here. This proposal adds a routine-EHR, patient-held-out test of whether a recorded assay state adds information after an explicit observation pathway, rather than reproducing the imaging model.

[K2] establishes why a local examination row cannot be called response: HCC treatment evaluation uses modality- and criterion-specific imaging, including mRECIST/RECICL and treatment-related necrosis. The local `检查所见` and `检查诊断` fields are therefore not consumed as response labels or NLP predictors.

[K3] shows that recorded response estimates can be altered by undocumented outcomes, imaging ascertainment, exposure classification and confounding, without identifying a comparative treatment effect. It motivates treating the repeat-TACE code as an operational event and ascertainment/workflow as a live rival.

The strongest claim supported before this experiment is only that a later local repeat-TACE record may be predictable from longitudinal EHR information. The unresolved claim is whether assay values/qualitative states carry held-out information beyond the process that makes assays and reviews observable. The leading explanation is recorded patient state. The strongest rivals are:

- workflow/selection: an order, review, encounter, or planned retreatment creates both an assay record and a later procedure;
- lead-time: records near day 42 encode a near-term plan rather than a durable state;
- severity/measurement: assay recording, review intensity and later procedure all reflect unmeasured severity or access, and the assay increment is not state-specific.

They make different observable predictions. State-consistent evidence should survive making the pre-outcome review pathway explicit, removing the last 7 days of process/assay records, and assay value/time permutations, while being less transferable to generic non-TACE procedure care. Workflow-consistent evidence should be concentrated in `W_packet=1`, disappear with the lead-time removal or process controls, and/or predict the negative-control-like endpoint similarly. These comparisons remain observational and cannot distinguish biological state from all unmeasured severity.

## Population, index, timing and outcomes

All timing uses integer elapsed days from `T0=index_start`.

- Index: the first dated procedures row in this supplied HCC snapshot whose trimmed Unicode-case-folded `手术` equals the exact token `tace`, with nonmissing `患者主索引`, `就诊号`, and `开始时间`. “First” means first in this snapshot, not first-ever TACE. Collapse exact duplicate patient/start rows for event counting but retain duplicate counts. Undated strict-code rows are audited and excluded from the primary timed analysis.
- Eligibility: all-source observation reaches `T0+42 days`, using the maximum valid timestamp from bound sources as `obs_end`. Exclude later exact-code TACE rows with `0 < Delta < 43` from the primary risk set and retain them in `early_repeat_audit.csv`. An untimed repeat is not a timed negative.
- Primary event: first later unique patient/start exact-code TACE with `43 <= Delta < 181`, i.e. the exact operational [43,181) endpoint. Follow-up ends at the first primary event, all-source `obs_end`, or day 181. Primary bins are integer days 43–90 and 91–180; complete 180-day follow-up is sensitivity only.
- Negative-control-like event: first nonmissing-`开始时间` procedure row for the same patient with a trimmed Unicode-case-folded `手术` token not equal to exact `tace`, with `43 <= Delta < 181`. Exact-code TACE, undated procedures and duplicate patient/start rows are excluded from this secondary event. This is an administrative care event, not a clinical outcome and not assumed independent of severity.
- No feature uses future event rows, future counts, `obs_end`, post-index exact-code TACE, or any record after the feature cutoff.

The fixed timing controls remain: day-42 cutoff; remove all process/assay records in days 36–42; process features end at day 28; alternate valid `obs_end` definitions; and exclusion of undated strict-TACE histories. A signal present only in days 36–42 or only in the early portion of [43,181) is compatible with planned-retreatment/lead-time workflow.

## Exact HCC source bindings and observed schema

The source catalog is `[internal dataset path]`, [source checksum]. The HCC snapshot hash is `[source checksum]`. Sources are read-only; all derived files are in the solver workspace. Do not join UKB, MIMIC or eICU namespaces.

All HCC sources are ordinary CSV files, not archive members. The bounded schema audit verified the following columns; the solver must recheck the catalog hash, source hashes and complete schemas before materialization.

- `procedures`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`. Use `开始时间` for index and event times and valid `结束时间` for `obs_end`; exact-code TACE rows never enter predictors.
- `encounters`: `[internal dataset path]`, [source checksum]; columns include `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室` plus identifiers. Join only on `患者主索引`+`就诊号`; use valid encounter timestamps for `obs_end`, intensity and department marks. Never use names or identity/phone/insurance/hospital numbers.
- `examinations`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `检查`, `检查所见`, `检查诊断`, `开始时间`, `机器型号`, `检查号`. Join on `患者主索引`+`就诊号` when present. Use `检查` and valid `开始时间` only for the proxy; `检查所见` and `检查诊断` are retained only for a clinical-review inventory and are not response labels, NLP inputs, or adjudication.
- `labs`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`. Use `检验时间` for assay timing and `obs_end`; preserve qualitative/inequality/censoring flags. There is no units or reference-range column, so do not impose thresholds or call a value liver function or tumor burden.
- `medications`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `用药`, `单次用药计量`, `单次用药计量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`. Use valid medication start/end timestamps for `obs_end` and process timing.
- `orders`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `医嘱(非药品)`, `开立时间`, `开始时间`, `结束时间`, `医嘱期限`, `医嘱状态`, `频次`. Use `开立时间` as order availability and `开始时间`/`结束时间` only when valid and no later than the feature cutoff.
- `diagnoses`: `[internal dataset path]`, [source checksum]; columns `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`. No temporal column: use only pre-index counts through matched encounters; it cannot define follow-up or a post-index event.
- `clinical_documents`: `[internal dataset path]`; `pathology`: `[internal dataset path]`. Exclude from primary longitudinal features because they lack valid event time. Identifier-only vitals, transfers and front_page are not measurements.

Collapse exact duplicates before counts. Use no names, identity numbers, phones, insurance/hospital numbers, file order or incompatible identifier namespaces.

## Proxy and negative-control construction

All proxy dictionaries and support counts are frozen before fitting and are produced from development data only for model input; the descriptive raw audit is made once from all source rows without exposing private rows.

### Primary pre-outcome review-opportunity proxy

Define normalized strings by trim, Unicode case-fold and whitespace normalization only. Do not use semantic substring lists, free-text examination findings, or diagnosis text.

For each eligible patient and each index:

1. `E_any`: at least one examinations row with the same `患者主索引`+`就诊号` and valid `开始时间` in `(T0,T0+42 days]`. It means a recorded examination opportunity, not imaging response.
2. `O_open`: at least one orders row with valid `开立时间` in that interval. It means an order became available, not that it was completed.
3. `O_done`: an orders row with valid `结束时间` in the interval and the exact observed operational status `检查已完成`; retain all other status values as unknown/categorical audit levels rather than translating them into clinical completion.
4. `E_order_linked`: an examination and order row joined on `患者主索引`+`就诊号`, with normalized `检查` exactly equal to normalized `医嘱(非药品)`, valid `开立时间 <= examination 开始时间`, and, when `结束时间` is valid, examination start no later than that end. If the order end is missing, it is not an order-completed link; it may contribute only to `O_open`.
5. `W_packet=1` if `E_order_linked=1` or `O_done=1` in `(T0,T0+42]`. Record packet date, order-to-exam lag when linked, counts, and whether the status was known. The proxy is a documented review/completion pathway, not a pre-outcome adjudication of response.

The exact-string linked proxy is primary because it is reproducible and does not assume that a free-text finding means response. Broad `E_any`/`O_open` are named sensitivity proxies. If `W_packet` is sparse or has inadequate event support, its contrast is reported as support failure; the broad proxy cannot rescue it by post hoc substitution.

Add a pre-outcome workflow feature `P_plan` only as a named process audit: counts and timing of non-TACE procedure rows, orders and completed order/exam packets in days 0–42. No order text is interpreted as “planned TACE” and no exact-code TACE row is used. This avoids endpoint leakage while acknowledging that the available tables cannot directly encode scheduling intent.

### Negative-control-like endpoint

For `Y_NC`, repeat the same patient-held-out construction, day-42 landmark, [43,181) horizon, censoring and observation rules, but use the first non-TACE procedure start. Fit it only if the prespecified support gate passes. Compare assay-state and workflow increments using the same frozen feature definitions. Similar assay and workflow increments for `Y_NC` suggest generic care-process/severity information; a smaller or unsupported increment is compatible with TACE-specific information but does not prove it.

The proxy and `Y_NC` are not clinical adjudication. The data do not contain scheduling intent, imaging response criteria, outside-care events, assay units/reference ranges, mortality, harms, costs or expert severity review.

## Models, split and estimators

The transparent primary baseline is elastic-net pooled-logistic discrete-time hazards for bins 43–90 and 91–180, with fixed bins or a low-degree time spline. Use the parent’s model set unchanged: M0; M0+P_obs; M0+P_care; A=M0+P_obs+P_care; M0+P_obs+S; and B=A+S. S contains only the eight parent assay labels, audited numeric values, qualitative/inequality flags and assay-specific pre-index changes; it contains no request/missingness indicator. P_obs contains dated encounter, examination, medication/order/lab counts, distinct dates/gaps, assay-label request/result counts and availability indicators but no assay values/results. P_care contains non-TACE procedure tokens, non-drug-order tokens, medication starts/ends, department/visit marks and timing but no assay values/results.

Add, without replacing the parent models:

- `A*`: M0 + `W_packet` + process features excluding the direct components `E_any`, `O_open`, `O_done`, linked-packet counts/timing and their duplicate indicators; `B*=A*+S`.
- `C_W`: M0+`W_packet`; its held-out contrast against M0 is the named workflow-proxy increment.
- `A_NC`, `B_NC`: the same A/B feature sets fitted to `Y_NC), only if supported.
- Proxy-stratum scoring: score A/B and A*/B* within `W_packet=1` and `W_packet=0`; do not refit within strata or select a favorable stratum.

The learned alternative is a compact time-aware GRU over the same -365 through +42 stream, with elapsed-time decay, event category/label, audited numeric value, qualitative/inequality flags, relative time, time since prior event and channel tag. It receives the same parent ablations plus the frozen `W_packet` channel, target, split, weights, metrics and three fixed development seeds. It could reveal nonlinear trajectories and order-to-exam timing patterns that elastic-net summaries lose. It cannot recover intent, imaging, units, outside care or reference ranges. Elastic-net remains primary because the new proxy and channel ablations are auditable; the GRU is a matched sensitivity, not a reason to claim a small predictive gain is clinically important. Larger transformers and broad hyperparameter searches are deferred because they add flexibility without separating state from workflow.

The split is generated once before fitting: among eligible patients, stratify only on the primary event indicator, assign 20% test and 80% development with deterministic seed 271828, and freeze patient IDs, algorithm and counts in `frozen_patient_split.json`. No patient crosses partitions. Fit dictionaries, encoders, scaling, imputation, cutpoints, weight models, proxy lexicons, hyperparameters and permutations inside development folds. Score the untouched test once. Seeds 314159 and 161803 are fixed sensitivity splits and cannot be used to select a favorable result.

Parent overall gates remain: at least 50 primary events overall, 15 test events, 100 test patients, 15 development events, completed audits, finite weights and weighted ESS >=100. For each W stratum, require at least 100 test patients, 15 test events, 15 development events and ESS >=100 for a reported state contrast; otherwise write `inconclusive_support_failure`. For `Y_NC`, require at least 50 non-TACE events overall, 15 test events, 100 test patients and ESS >=100; otherwise do not report an NC estimate. These thresholds are feasibility gates, not clinical importance thresholds.

Fit all-source right-censoring weights within development folds. For S, fit cross-fitted day-42 assay-observation weights from M0, pre-day-42 P_obs and P_care. Report ordinary and observation-weighted estimates, finite-weight tails and ESS. Bootstrap test patients with all their person-days and weights for paired 95% intervals. Use one max-|t| family for the parent state/workflow contrasts and the two proxy-stratum contrasts; label learned-model, Y_NC and repeated-seed results sensitivities. Report weighted log loss, Brier/integrated Brier, calibration slope/intercept, AUROC/AUPRC secondarily, and paired held-out losses.

## Falsification and interpretation gates

Use the same split, folds, weights, support rules and output format for:

- within-patient assay/result timestamp permutations preserving assay/result multisets and process counts;
- assay numeric shuffles within calendar and baseline-severity blocks;
- process-mark permutations within calendar and event-count strata;
- `W_packet` label permutation within patient and index-calendar blocks;
- 7-day lead-time removal and day-28 process cutoff;
- undated-TACE and alternate-`obs_end` sensitivities;
- exact-code-only versus separately frozen high-specificity alias sensitivity;
- development outcome-label permutation scored on untouched true-label test outcomes.

Supportive state-consistent evidence requires: parent overall primary gate passes; simultaneous lower 95% bound for `D_state>0`; calibrated A/B predictions; consistent ordinary and observation-weighted direction; positive `D_state,residual` in a supported `W_packet=1` comparison; no disappearance under the 7-day control; no comparable increment after assay value/time permutation; and no evidence that the same state increment simply predicts `Y_NC`. This is still only compatible with reusable recorded patient-state information. It does not establish tumor biology, response, or benefit.

Workflow-dominant evidence is a positive `C_W`/process increment comparable to or larger than `D_state`, state attenuation after explicit proxy inclusion, concentration in `W_packet=1`, disappearance after lead-time removal, or similar increments for `Y_NC`. It redirects the next study toward intent, scheduling, availability and outside-care linkage.

Mixed evidence means both state and workflow increments persist, or state persists only in the observed-review stratum. That result is not proof of state biology: it may indicate assay availability conditioned on review. It justifies expert adjudication rather than a treatment rule. Adverse evidence is a reproduced assay increment under value/time permutation or an increment explained by process controls. An imprecise, sparse, or support-failing result is inconclusive and does not refute the hypothesis.

All decision rules are computational. Clinical response, assay meaning, treatment intent, causal mechanism, net benefit, harms and utility require expert adjudication or another cohort/study.

## Required outputs and claim map

In addition to the parent artifacts, require `review_workflow_proxy_audit.csv` with counts, exact status levels, linked-order/exam lag summaries and missing timestamps; `proxy_definition_and_leakage_report.json`; `proxy_stratum_counts_support.csv`; `negative_control_endpoint_audit.csv`; held-out predictions/losses for M0, C_W, A, B, A*, B* and supported NC models; `proxy_stratum_contrasts.csv`; `negative_control_contrasts.csv`; `state_workflow_contrasts.csv`; `falsification_results.csv`; `multiplicity_familywise_intervals.csv`; `decision_facing_summary.csv`; and `claim_output_map.md`.

The summary must state, for every parent contrast, proxy contrast, W stratum and NC sensitivity: split label; support flag and exact failure reason; patient/event counts; W_packet rate; assay-observation rate; weighted ESS; calibration; paired loss/Brier increment and interval; lead-time/permutation direction; and interpretation class. Unsupported W strata and NC endpoints must appear as explicit `inconclusive_support_failure` rows. Each prose conclusion must link to output rows and mark whether it is computationally checkable or requires clinical adjudication/another study.

## Alternatives and resource plan

The baseline and alternative answer the same state-versus-workflow question with identical index, endpoint, channels, split and evaluation. The elastic-net hazard model is primary because it makes the named proxy, ablation, interaction and loss differences inspectable and should fit on CPU in a small tabular run (planning estimate: 2–8 CPUs, 8–16 GiB, generally under an hour; unverified until solver execution). The GRU is the substantive alternative because it can preserve event order and order-to-exam lag rather than only aggregate counts; it is a sensitivity with three fixed seeds (planning estimate: 1 allocated A100, 4–8 CPUs, 16–32 GiB, approximately 1–3 hours; unverified). No GPU is required for the primary computation. GPU feasibility must be checked only in an allocated job; an unallocated shell CUDA result is not evidence of absence. The alternatives are not selected to chase a small predictive improvement: the learned model is retained only to test whether trajectory shape changes the state/workflow interpretation. The scientific direction is deferred or revised if the proxy is unsupported, if only the GRU changes the result, or if neither model separates state from workflow.

## Clinical limits and revisit rules

This snapshot does not supply imaging files or adjudicated mRECIST/RECICL response, treatment intent/scheduling, outside-care events, assay units/reference ranges, mortality, harms, costs or expert severity. Examination text is present but is not treated as adjudicated response. A positive recorded-state increment can justify an imaging/intent adjudication study only; it cannot support a patient-level treatment rule.

Continue to imaging/intent/outside-care linkage if the primary state gate, proxy residual and lead-time checks pass. Prioritize workflow/scheduling data if process or NC evidence dominates. Defer proxy-stratum or NC interpretation when their support gates fail. Abandon the assay-state validation direction only after adequately supported repeated controls show that process/permutation features match the assay increment or the increment disappears under leakage-safe timing. A failed GRU alone never refutes the hypothesis.

## Compact bibliography

[K1] Dai Y, Zhao S, Wu Q, Zhang J, Zeng X, Jiang H. *A CT-Based Deep Learning Radiomics Scoring System for Predicting the Prognosis to Repeat TACE in Patients with Hepatocellular Carcinoma: A Multicenter Cohort Study*. Journal of Hepatocellular Carcinoma. 2025;12:1647–1659. doi:10.2147/jhc.s525920. Full-text relevant excerpt inspected.

[K2] Tsurusaki M, Sofue K, Murakami T, Tanigawa N. *Radiological Assessment and Therapeutic Evaluation in Hepatocellular Carcinoma: Differentiation and Treatment Response with Japanese Guidelines*. Cancers (Basel). 2024;17(1):101. doi:10.3390/cancers17010101. Relevant full-text XML excerpt inspected.

[K3] Minh VL, Hung NV, Anh PT, Anh PT, Thong PM. *Recorded Early Imaging Responses After Transarterial Chemoembolization Plus Lenvatinib Versus Transarterial Chemoembolization Without Documented Lenvatinib for Unresectable Hepatocellular Carcinoma: A Vietnamese Cohort Study*. Journal of Clinical Medicine. 2026;15(17):6839. doi:10.3390/jcm15176839. Relevant full-text XML excerpt inspected.
