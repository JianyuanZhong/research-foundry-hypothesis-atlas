# HCC repeat-TACE episode validity: a decision-facing adjudication gate

Status: substantive Episode 11 successor to [prior hypothesis]. Design only; no cohort fit, model result, prevalence estimate, or clinical conclusion is claimed.

## Scientific opening and exact advance

The inherited question is whether recorded assay state at day 42 adds held-out information for a later locally recorded repeat-TACE event after accounting for measurement opportunity and care workflow. The remaining validity problem is narrower and consequential: does a dated procedure record represent a sufficiently specific operational treatment episode to support the next research decision, or is it mainly site/workflow documentation? The parent already supplies O0 (literal procedure), O1 (semantic procedure plus same-visit examination/order corroboration), O2 (O1 plus medication corroboration), lead-time controls, workflow/state contrasts and matched elastic-net/GRU alternatives.

This child makes one substantive advance: it adds a pre-specified, auditable three-way decision gate that uses the computed O0/O1/O2 contrasts and the audited availability of corroborating fields to decide whether to (a) proceed to blinded clinical episode adjudication, (b) redirect toward scheduling/documentation acquisition, or (c) defer because the endpoint is unsupported. It also audits pathology and diagnoses as possible context, but explicitly refuses to treat their visit linkage as event timing. This is the smallest change that can alter the next clinical research action without pretending that an EHR code is intent or imaging response.

The hypothesis is:

> In the inherited day-42 population, if the assay-state increment is reproducible for O1, it will remain positive after the parent’s workflow and lead-time controls, with O1 supported by timed examination/order evidence rather than by untimed pathology/diagnosis coverage; this pattern should justify a clinical adjudication study of the operational episode. If O1 collapses to O0, to process-matched permutations, or to untimed-documentation coverage, the reusable episode interpretation should be abandoned and the next study should obtain scheduling/intent and outside-care data.

This tests incremental predictive/descriptive validity of a recorded operational endpoint. It does not test treatment efficacy, clinical benefit, treatment intent, radiologic response, viable tumor, causal mechanism, or whether repeat TACE should be offered.

### What is already supported versus unresolved

The three inspected works are used as bounded evidence, not as a topic list. [K1] supports treatment-adjacent repeat-TACE prediction from CT/radiomics in a selected multicenter cohort, while showing external-performance and generalization limits. [K2] bounds HCC response as an imaging- and necrosis-aware construct, not a procedure label. [K3] shows why documented post-TACE comparisons are vulnerable to ascertainment, missing outcome documentation, selection and comparator-exposure limitations. None validates this site's procedure code or composite.

The strongest available claim is therefore only that locally recorded assay state might predict a later locally recorded operational repeat-TACE event. The unresolved claim is that O1 is a clinically meaningful treatment-episode proxy rather than a more complete workflow/documentation marker. The leading rival is workflow/ascertainment: visits, orders, examination availability and medication documentation can generate both assay state and an O1/O2 record. A severity/selection rival is residual disease burden or clinician selection not represented in the available structured fields. The pathology/diagnosis alternative is not a rival that can be tested temporally here because those tables lack event-time fields.

The advance over existing evidence is a decision rule connecting endpoint robustness to the next required study. A supportive result licenses only a blinded adjudication effort; an adverse result redirects data acquisition; an inconclusive result prevents more modeling. It does not convert predictive regularity into a causal or mechanistic conclusion.

## Population, temporal boundaries and inherited estimand

All of the following are frozen from the parent.

1. Index is the first dated procedures row with Unicode-normalized, trimmed, case-folded 手术 equal to TACE, with nonmissing 患者主索引, 就诊号 and 开始时间.
2. Collapse exact duplicate patient/start rows for event counting but retain duplicate counts and raw-label hashes in the audit.
3. Require all-source observation end at least 42 days after index start.
4. Exclude any later literal-code TACE with 0 < elapsed days < 43.
5. O0 is the first later unique patient/start literal-code TACE with 43 <= elapsed days < 181.
6. Follow-up ends at the event, all-source obs_end, or day 181; [43,90] and [91,181) remain fixed sensitivities.
7. Untimed procedure rows are neither timed negatives nor imputed events. A dated procedure with a blank end time is valid for event timing; its end-time deficiency is audited for observation/censoring.
8. Patient joins use 患者主索引. Visit joins use (患者主索引, 就诊号). No incompatible identifier namespace, names, identity numbers, phones, insurance/hospital numbers or file order is used.
9. The day-42 feature cutoff, parent observation/censoring construction, leakage exclusions and all-source obs_end are unchanged. O0/O1/O2 evidence after the feature cutoff is outcome evidence only.

O1 remains the first later procedure p satisfying semantic procedure predicate P, valid procedure start t, a same-patient/same-visit encounter link, and at least one timed same-visit corroborator:

- P is exact normalized TACE or a label containing hepatic-artery plus embolization and at least one chemotherapy or infusion term, excluding radiofrequency, microwave, ablation, biopsy, puncture and drainage terms.
- An encounter link is valid if encounter 就诊时间 is within two elapsed days of t, or valid 入院时间 <= t <= 出院时间. Missing discharge makes the second route false.
- The timed examination/order corroborator is an examination type or non-drug order type matching the frozen liver/arterial/upper-abdomen plus contrast/enhancement/CT/MRI/ultrasound dictionary, or the frozen hepatic-arterial/TACE order dictionary, with examination 开始时间 or order 开立时间 in [t-42,t+7].
- Event time is the qualifying procedure start t, never the earlier corroborator.
- A qualifying procedure lacking corroboration is a timed negative for O1/O2 only when its follow-up window is observed; it remains a near-miss audit row.
- O2 is O1 plus same-visit medication predicate M in [t-1,t+1]. M uses only the frozen medication-name dictionary and timing; dose, unit, route and drug class are audited but do not establish intent.

Early semantic procedures in (0,43) remain an early-alias history sensitivity. Untimed semantic rows are flagged only. O1/O2 are operational endpoint definitions, not treatment intent, response or benefit.

## Actual HCC bindings and field audit

The immutable dataset catalog is [internal dataset path], [source checksum]. Dataset snapshot is HCC [source checksum]. Every source is an ordinary file, not an archive member.

| table | exact source path and source SHA-256 | required columns and use |
|---|---|---|
| procedures | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源. P/O0/O1 time, duplicate audit and obs_end. |
| encounters | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室. Visit join, encounter route, timing and obs_end. |
| examinations | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 机器型号, 检查号. Only 检查 and 开始时间 enter timed O1; narrative is retained for later expert review and never auto-scored as response. |
| orders | [internal dataset path](非药品)_2062526727266216118.csv; [source checksum] | 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次. Order type, availability and timing corroboration; not intent. |
| medications | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型. M timing/name and completeness audit; drug indication is not inferred. |
| labs | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间. Inherited eight exact parent assay labels and missingness/measurement-opportunity channels; no cross-assay unit interpretation because no unit/reference-range column. |
| pathology | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 病理, 检查所见, 检查诊断, 机器型号. Same-visit coverage flag and expert-review context only. No event-time field. |
| diagnoses | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 诊断名称, 诊断类型. Same-visit coverage flag and expert-review context only. No event-time field. |
| clinical_documents | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, narrative fields including 诊疗经过, 出院情况, 手术名称, 手术经过. Expert-review context only because no event-time field. |
| vitals/transfers/front_page | exact HCC files bound in datasets/hcc/README.md; schemas are identifier-only | 患者主索引, 就诊号 only. Read for relationship/audit if needed; no payload or timing, never used as corroboration. |

The complete field audit is in hcc-field-audit.md. It records actual header/first-two-row sampling, schema availability and the source limitations. Pathology and diagnoses do contain clinically suggestive text fields, but the absence of event time means a same-visit join cannot establish temporal order. Neither is allowed to rescue O1/O2 or to label intent, response, or an operational episode.

## Decision-facing adjudication gate

The gate is evaluated once on the frozen held-out outputs and frozen support audit. It is not tuned after looking for a favorable result.

### Gate A: computational admissibility

For each O0/O1/O2, require the inherited support conditions: at least 50 overall events for O1/O2, at least 15 development and 15 test events per reported stratum, weighted ESS at least 100, nondegenerate observation/censoring support and no frozen weight-tail failure. Report exact event, risk-set, censoring, missing-time, near-miss, pathology-coverage and diagnosis-coverage counts.

If any primary O1 condition fails, label O1 unsupported/inconclusive. Do not pool O1 with O0, treat unavailable timing as a negative, or allow O2 to rescue O1.

### Gate B: endpoint-discrimination evidence

Use the parent’s paired held-out metrics and one simultaneous max-|t| patient-bootstrap family. For endpoint j define:

- Delta_S,j = L(A_j) - L(B_j), the recorded-state increment after the matched workflow channels;
- Delta_W,j = L(M0+P_obs) - L(A_j), the workflow-accounting increment;
- G_j = Delta_S,j - Delta_W,j, a descriptive state-versus-workflow contrast, not causal adjustment.

The primary outcome is O0 and the boundary-validation outcome is O1; O2 is secondary. Support requires O0 and O1 to meet support gates, Delta_S to be positive with simultaneous lower bound above zero, G_O1 > 0 so workflow does not explain the entire increment, and the sign to persist under the fixed pre-procedure [-42,-1] corroborator control. The 0.005 weighted-log-loss margin inherited from the parent is an operational resolution margin, not a clinical MCID.

Process/timestamp permutations, [−28,−1] and [−7,−1] lead-time windows, removal of process/assay records in (35,42], early-alias exclusion and ordinary versus development-fold observation weighting are falsification controls. If a process-matched or timestamp-permuted composite reproduces the increment, or the pre-procedure restriction erases it, the reusable-state interpretation is adverse.

### Gate C: three-way next-decision rule

1. SUPPORTIVE / escalate to adjudication: O0 and O1 pass Gate A; the simultaneous lower bound for Delta_S,O1 is above zero; G_O1 > 0; the pre-procedure control retains direction; and no workflow/timestamp permutation matches. This supports only a reproducible recorded operational episode signal. The next action is a blinded clinical episode-adjudication study, not a treatment rule. The minimum auditable adjudication packet is every O0/O1 discordant and O1/O2 discordant case, plus a fixed random sample of 25 O0/O1 concordant cases (seed and patient IDs frozen before review). If the discordant set exceeds 50 patients, review a pre-specified 50-patient patient-stratified sample and retain the complete unreviewed discordance ledger. Reviewers must see procedure name/start/end/source, encounter timing, examination type/start/findings/diagnosis, order name/timing/status, medication name/timing/dose/unit/route, same-visit pathology/diagnosis/document presence, and external images or scheduling/intent fields if obtained. Reviewers assign treatment-episode present/absent/uncertain and intent documented/absent/uncertain, with imaging response not scored unless actual images and validated criteria are available. Agreement and adjudication sampling uncertainty are reported.

2. ADVERSE / redirect acquisition: O0 passes but O1 fails, O1 is workflow-dominated (G_O1 <= 0), the pre-procedure control erases the increment, semantic aliases drive the difference, or a process/timestamp permutation matches. The next decision is to retain O0 only as a literal recorded-event estimand, stop describing O1 as a more specific episode, and obtain scheduling/intent, standardized imaging/report timestamps, outside-care capture and validated medication indication data. Do not use an adverse result to claim that assay state has no clinical value; it rejects only this narrow endpoint-validity interpretation under the measured snapshot.

3. INCONCLUSIVE / defer: Gate A fails, O1/O2 have sparse or wide support, ESS/weight support fails, required times are missing, or the direction is unstable without a clear adverse falsification. Do not enlarge the model or choose a favorable subgroup. The next decision is a bounded data audit or independent validation; abandon neither the underlying assay question nor the endpoint until the missing evidence is resolved.

The pathology/diagnosis coverage flags can change which cases enter the adjudication packet or reveal documentation-site imbalance, but cannot move an endpoint to SUPPORTIVE by themselves. A same-visit pathology or diagnosis row is not a timed diagnostic corroborator.

## Matched baseline and learned alternative

The alternatives answer the same scientific question, with the same patient-held-out split, outcomes and uncertainty.

The simple confirmatory baseline is a pooled-logistic discrete-time hazard with frozen M0 covariates and fixed parent observation/censoring weighting. M0 is the parent pre-index demographic/history/time baseline; M0+P_obs adds measurement opportunity; M0+P_care adds care-process/order/encounter channels; A=M0+P_obs+P_care; B=A+S adds the inherited recorded assay state. Fit each model for O0, O1 and O2, with exact and semantic procedure event rows excluded from predictors. Use earliest 80% of eligible index dates for development and latest 20% untouched test, patient-disjoint, with five grouped development folds. Freeze dictionaries, encoding, imputation/scaling and weighting in development.

The learned alternative is a compact time-aware GRU over the identical allowed event stream from day -365 through day +42, with separate O0/O1/O2 discrete-time hazard heads, the same parent channel ablations, split, weighting and held-out metrics, and three fixed development seeds. The sequence model can expose nonlinear trajectories and ordering of observations, examination/order timing and assay missingness that summary features lose. It cannot create intent, imaging response, assay units, or outside-care events. A neural alternative is scientifically useful here because the uncertainty is about temporal workflow/state information, not because it is more complex.

Evaluate ordinary and all-source-censoring-weighted log loss, Brier/integrated Brier, calibration, AUROC/AUPRC with event/risk-set counts, ESS and weight tails. Compare models by paired patient bootstrap and the one max-|t| family. Report endpoint-specific results and do not use a small predictive gain as clinical value. The elastic-net hazard is selected for the primary decision because it is transparent, easier to audit and sufficient for the endpoint-validity contrast. The GRU is a deferred sensitivity: it is retained if the future solver budget allows it and must not be used to override an unsupported O1.

Planning estimates, not measured runtime: elastic-net materialization, weighting, fits and bootstrap require about 1–4 hours on 4 CPU / 16 GiB; the GRU requires about 2–6 hours on 4 CPU / 16 GiB with one allocated A100 (80 GiB), using cuda:0 inside the allocation. Discovery time and the 28,800-second solver-planning envelope in inputs.json are separate. No GPU is required for the tabular primary; availability of a future allocated GPU is an infrastructure dependency, not a scientific premise. No model has been fitted in this episode.

Alternatives explicitly not chosen are a larger transformer, automated NLP of findings/pathology, a latent causal/intent model and a mechanistic response model. They are deferred because the available files lack event-time documentation for pathology/diagnosis, validated narrative temporality/coreference, scheduling intent, actual images, treatment indications, laboratory units/reference ranges, outside-care capture and adjudicated response. The evidence that would justify revisiting them is a timed, externally validated intent/response corpus or a blinded expert-labeled subset with reliable image/report timestamps. The GRU remains the substantive learned alternative; complexity alone is not a reason to reject it.

## Falsification and interpretation

Supportive computation means only that a timed, corroborated operational record carries a state increment not explained by the prespecified workflow controls. It does not establish that TACE was intended, that response occurred, that a repeat was beneficial, or that assay state causes treatment.

Adverse computation means the operational episode definition is indistinguishable from workflow or fails to generalize across its fixed controls. This changes the next research decision toward acquisition of intent/scheduling and outside-care evidence. It does not prove that the assay has no prognostic value.

Inconclusive computation means the available data cannot distinguish the rival explanations. Sparse events, missing timing, non-overlap, imprecise uncertainty and weight failure are evidence limits, not null results.

Clinical adjudication requires expert review of source records and, for response, actual imaging with a validated mRECIST/RECICL-style protocol. The snapshot contains no image files; examinations are CSV report rows, not adjudicated response. It also lacks reliable treatment intent/scheduling fields, outside-care capture, validated drug indications, laboratory units/reference ranges and clinical outcomes such as benefit, survival or toxicity. Those claims require another study and cannot be established by an automatic verifier.

## Newly fitted deliverable and completion criteria

The future solver’s actual deliverable is not a narrative assertion. It must newly fit the endpoint-specific held-out hazards and produce:

- endpoint_definition.json with frozen O0/O1/O2 dictionaries and version;
- endpoint_event_audit.csv with hashed patient keys, timing routes, duplicate/untimed/near-miss and pathology/diagnosis coverage flags;
- field_availability_audit.json with source hashes, schemas, missing timing and units;
- endpoint_support_freeze.json with event/risk-set/ESS/weight support before outcome inspection;
- endpoint_heldout_predictions_losses.csv with O0/O1/O2, model/channel, split, weights and metrics;
- endpoint_workflow_state_contrasts.csv with Delta_S, Delta_W and G;
- endpoint_leadtime_ascertainment.csv for all fixed controls;
- endpoint_adjudication_gate.json containing one of SUPPORTIVE, ADVERSE or INCONCLUSIVE and the exact ledger/sample rule;
- endpoint_simultaneous_multiplicity.json and claim_output_map.md linking every conclusion to computed outputs and uncertainty.

Completion requires the files above, a frozen support audit, paired uncertainty, all three gate paths evaluated, and an explicit statement of which claims remain unavailable. A readiness/package check is not a solved endpoint-validity question. The current branch contains no fitted result.

## Key references

[K1] Dai Y, Zhao S, Wu Q, Zhang J, Zeng X, Jiang H. A CT-Based Deep Learning Radiomics Scoring System for Predicting the Prognosis to Repeat TACE in Patients with Hepatocellular Carcinoma: A Multicenter Cohort Study. Journal of Hepatocellular Carcinoma. 2025;12:1647–1659. doi:10.2147/JHC.S525920. Full-text excerpt inspected.

[K2] Tsurusaki M, Sofue K, Murakami T, Tanigawa N. Radiological Assessment and Therapeutic Evaluation in Hepatocellular Carcinoma: Differentiation and Treatment Response with Japanese Guidelines. Cancers. 2024;17(1):101. doi:10.3390/cancers17010101. Abstract-only inspection.

[K3] Minh VL, Hung NV, Anh PT, Anh PT, Thong PM. Recorded Early Imaging Responses After Transarterial Chemoembolization Plus Lenvatinib Versus Transarterial Chemoembolization Without Documented Lenvatinib for Unresectable Hepatocellular Carcinoma: A Vietnamese Cohort Study. Journal of Clinical Medicine. 2026;15(17):6839. doi:10.3390/jcm15176839. Abstract-only inspection.

The structured receipts and exact attached UTF-8 excerpts are in key-references.json, support-K1-dai2025-excerpt.txt, support-K2-tsurusaki2024-abstract.txt and support-K3-minh2026-abstract.txt. Each receipt hashes the attached bytes.
