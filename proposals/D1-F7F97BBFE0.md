# Episode 19 endpoint-provenance child: closure plus capture-aware negative control

Status: design only. No cohort count, fitted model, prevalence, effect estimate, or clinical conclusion is claimed.

Parent: `[prior hypothesis]`. This child preserves the parent's HCC population, `[t0+43,t0+181)` first-event estimand, O0/O1/O2 hierarchy, O3 intermediate endpoint, R42/R28 observation weighting, temporal patient-held-out split, elastic-net baseline, compact GRU alternative, uncertainty family, and clinical limits. It makes one substantive repair to the remaining endpoint threat: absence of a post-procedure source is no longer evidence for a planned-only label, and the strict provenance endpoint additionally requires a valid procedure closure time.

## Scientific opening and clinical importance

The strongest claim currently supported is narrow: among patients with a first dated exact-code TACE record and day-42 observation, a pre-index-to-day-42 assay trajectory may improve held-out prediction of a later operational TACE record over a day-42 snapshot after accounting for measured baseline severity, assay opportunity, observation, and care workflow. O0/O1/O2/O3 are records, not adjudicated treatment failure, radiographic progression, retreatment intent, response, survival, benefit, or utility.

The unresolved claim is whether the trajectory increment persists for a later record that is both administratively closed and followed by timed same-visit activity, while not appearing in a capture-adequate pattern that looks like an opened order without strict coherence. The leading explanation is that an assay trajectory contains information about a subsequent coherent procedure episode. The strongest rival is care-intensity/documentation selection: clinicians who order more tests and care may generate both assay trajectories and downstream examinations, orders, medications, and procedure codes. A second rival is asymmetric capture: candidates lacking post-source rows may simply have incomplete downstream observation, so the parent's planned-only negative control could be misclassified.

This matters clinically because a trajectory signal that survives stricter provenance and missingness checks would justify a blinded intent/imaging validation study. A signal that is equally present in the capture-adequate process pattern would redirect the work toward workflow prediction and endpoint acquisition, not assay biology. No available result can identify mechanism or treatment benefit. [K1] supports temporal modeling while explicitly noting learned data biases; [K2] supports selection/observation weighting but does not turn an administrative code into a clinical event; [K3] supports separating recorded time, biological time, decision time, and missingness. This child adds a local, computable provenance/missingness contrast beyond those general precedents.

## Hypothesis and estimand

Primary hypothesis:

> In the inherited HCC index population, the day-42 assay trajectory adds held-out information over the day-42 assay snapshot for a later **closed-coherent TACE proxy** (O4), and that increment is not reproduced by a capture-adequate pre-opened-order/no-strict-coherence process pattern.

This is a predictive/descriptive hypothesis about records. It is not causal and does not assert that O4 is completed treatment or that the assay trajectory is biological.

Retain the parent feature blocks:

- `A0=M0+B0+P_obs+P_care`;
- `A_snap42=A0+S42`;
- `A_traj42=A0+T42`;
- primary contrast `D_j=L_w(A_snap42,j)-L_w(A_traj42,j)`, with positive values favoring the trajectory model;
- secondary `L_w(A0,j)-L_w(A_traj42,j)`.

The primary endpoint becomes O4 for the endpoint-provenance decision, with O0 primary operational boundary, O1/O2 inherited semantic boundaries, and O3 retained as an intermediate. The same contrasts are computed for the capture-adequate process control `O_planproxy_cap`; it is not a clinical event and cannot support a clinical claim.

## Population and time boundaries

Use the first row in `procedures` whose Unicode-normalized, trimmed, case-folded `手术` equals `TACE`, with nonmissing `患者主索引`, `就诊号`, and `开始时间`. Call its start `t0`. Apply the parent's deterministic duplicate/alias audit, malformed-date exclusions, early-repeat exclusions, and all-source observation requirement through `t0+42 days` for R42. Preserve the R28 pre-day-42 arm.

Use only `患者主索引` for patient grouping and exactly `(患者主索引, 就诊号)` for visit-level joins. Do not use name, identity-card, phone, insurance-card, file order, or any incompatible identifier namespace.

Every later candidate procedure has a valid `tp` in the fixed window `[t0+43,t0+181)`. The 14-day risk grid remains `[43,57), [57,71), ..., [169,181)`; it is only a modeling grid. First-event handling, right censoring, R42/R28 weighting, and observation boundaries do not change.

## Endpoint repair

Retain the parent's operational endpoints exactly:

- **O0:** first later unique literal-code TACE.
- **O1:** O0 candidate satisfying the frozen semantic hepatic-arterial procedure rule plus valid same-patient/same-visit timed examination or order corroboration.
- **O2:** O1 plus the frozen same-visit medication corroboration.
- **O3:** O2 plus at least one qualifying examination, order, or medication row on the exact visit key with nonmissing event/start time `u` strictly after `tp` and no later than `tp+72 hours`. Orders must have nonblank status and must not contain the normalized cancellation tokens `取消`, `作废`, `撤销`, or `停用`. O3 remains an operational activity endpoint, not completion or intent.

Add one stricter nested endpoint:

- **O4 closed-coherent:** O3 plus a valid procedure `结束时间=te` from the same later `procedures` row, with parseable `te` and `0 <= te-tp <= 72 hours). A zero duration is allowed because timestamp granularity may collapse same-day start/end. A negative, missing, or longer-than-72-hour duration is `closure_unknown`, not a negative clinical event.

The 72-hour closure bound is frozen before held-out scoring and matches the downstream provenance window. It is a data-quality/administrative closure rule, not a claim about biological completion. O3 is retained so that O3-positive/O4-negative discordance is visible rather than silently discarded.

### Capture-aware process control

The parent’s raw “pre-opened order and no post-source” label is replaced by a narrower, explicitly nonclinical label:

- **post-window capture-adequate:** for the candidate’s exact visit key, set this flag to 1 if either (a) `encounters.出院时间` is valid and at least `tp+72 hours`, or (b) at least one non-procedure row with a valid time in `(tp,tp+72 hours]` is observed in `examinations.开始时间`, `orders.开始时间`, `medications.开始时间`, or `labs.检验时间`. Otherwise set it to 0. This is an observable-record rule, not proof of complete capture.
- **O_planproxy_cap:** a later literal TACE candidate with a same-visit order whose `开立时间` is valid and lies in `[tp-7 days,tp)`, with post-window capture-adequate=1, no O4 classification, and no qualifying O3 post-procedure examination/order/medication. It may contain a procedure closure or other sources; it is called a *pre-opened-order/no-strict-coherence process pattern*, never “planned treatment.”
- **unknown_provenance:** any candidate for which post-window capture-adequate=0 and no O4/O3 evidence classifies it. Missing post-source rows and missing order status/time are not treated as planned-only.
- If a candidate meets O4 and the pre-opened-order rule, classify it as O4 and retain an overlap flag; it is excluded from O_planproxy_cap. If it meets O3 but not O4, it is O3-only, not O_planproxy_cap. If it has a pre-opened order but no qualifying post-source and capture is inadequate, it remains unknown.

This rule does not remove care-intensity confounding: capture adequacy itself may reflect intensity. Its purpose is narrower and falsifiable—preventing differential absence of downstream records from being interpreted as evidence of planned documentation. Report the capture-adequate fraction and all unknown/invalid reasons by endpoint, time bin, and held-out split.

## Exact HCC source bindings

Use the frozen HCC snapshot `[source checksum]`. All twelve HCC members are ordinary files; no archive member is required. The following headers were directly checked in the read-only source files, and the parent’s catalog/schema audit supplies the snapshot lineage and hashes.

| table | exact source path; SHA-256 | columns used |
|---|---|---|
| `procedures` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`; index, O0–O4, `tp/te`, source-row and closure audit |
| `encounters` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`; joins, M0, care/observation features, capture-adequacy rule |
| `examinations` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `检查`, `检查所见`, `检查诊断`, `开始时间`, `检查号`; O1/O3/O4 corroboration and capture timing |
| `orders` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `医嘱(非药品)`, `开立时间`, `开始时间`, `结束时间`, `医嘱状态`, `频次`; O1/O3, pre-open process signal, status/time audit |
| `medications` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `用药`, `单次用药剂量`, `单次用药剂量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`; O2/O3 and capture timing; no drug indication invented |
| `labs` | `[internal dataset path]`; `[source checksum]` | `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`; unchanged B0/S42/T42, assay opportunity, capture adequacy |

`diagnoses`, `pathology`, and `clinical_documents` remain context/coverage-only under the parent audit. No validated event-time field, treatment-intent field, imaging report, response label, or outside-care record is invented from them. The source snapshot has no images, lab units/reference ranges, reliable narrative temporality, treatment indication, dose/technical TACE detail, toxicity, survival, utility, benefit, or expert adjudication.

## Baseline and learned alternative

Both methods receive the same eligible patients, endpoint rows, risk grid, right-censoring masks, source-derived endpoint classes, R42 weights, R28 arm, split, and uncertainty procedures. Endpoint class is never entered as a predictor.

**Transparent baseline.** Fit the parent’s elastic-net pooled-logistic discrete-time hazard with intercept and risk-bin indicators plus M0, B0, observation, care, assay-opportunity, and the specified snapshot/trajectory blocks. Alpha is 0.5; lambda, parser, token dictionary, assay-specific robust scaling, imputation, and R42 selection weights are fitted only inside grouped development folds. Compute O0/O1/O2/O3/O4 and O_planproxy_cap as separate first-event targets. Add a predeclared capture-indicator audit, not post-tp capture variables, to report missingness; do not leak post-endpoint rows into predictors.

**Substantive learned alternative.** Fit the same compact time-aware GRU from the parent: eight assay labels, numeric/qualitative/inequality content, sample type, relative time, inter-event time, and opportunity tag from `t0-365` through `t0+42`, with M0/workflow covariates at the hazard head. One GRU layer, hidden size 32, dropout 0.10, head 32/16, Adam 1e-3, weight decay 1e-4, at most 50 epochs, eight-epoch early stopping, and seeds 17/29/41. Use the same endpoint targets, masks, weights, folds, and outputs.

The baseline is selected for auditable endpoint-block, weighting, and missingness accounting. The GRU tests the substantive alternative that irregular ordering and nonlinear assay combinations add information that deterministic summaries lose. A GRU gain without O4/process-control separation is workflow-sensitive prediction, not liver biology. Defer transformers, narrative NLP, causal intent models, and mechanistic response models because the available HCC data lack validated timed intent/response labels, images/reports, assay units/reference ranges, and outside-care capture. Revisit those alternatives only after O4 support and capture adequacy pass.

## Split, outcomes, uncertainty, and falsification

Sort index patients by `t0); earliest 80% are development and latest 20% are untouched testing, with no patient in both. Use five grouped development folds for all preprocessing, weighting, hyperparameter, early-stopping, and seed decisions. Never use test endpoint classes to change the rule.

For every method and endpoint report patient-level paired log loss, Brier score, integrated Brier score, calibration, risk-bin counts, paired availability, and discrimination only as secondary. Use 1,000 patient-level paired bootstrap resamples of the untouched test set with one max-|t| simultaneous 95% family spanning O0/O1/O2/O3/O4/O_planproxy_cap, snapshot-versus-trajectory and A0-versus-trajectory contrasts, ordinary/R42 estimates, R28, and fixed falsifiers. Report O3/O4 overlap, closure-invalid/missingness reasons, capture-adequate fraction, unknown fraction, event/risk-set counts, R42/R28 ESS, and weight tails.

The decision gate is frozen as follows:

1. **Supportive:** O4 has a positive simultaneous lower 95% bound for `D_O4`, with direction retained in both elastic-net and GRU, ordinary and R42-weighted analyses, and the R28/late-window controls; O4 provenance counts are supported in the untouched test set; and `D_planproxy_cap` has an upper simultaneous 95% bound at or below zero in both methods. O0/O1/O2/O3 may be directionally concordant, but O4 is required for the strict provenance claim.
2. **Adverse:** O4 removes the O3/O0 increment; O4 is positive only in one method or one weighting arm; late-window removal, R28, workflow-only/time-only, or within-patient content permutation reproduces the increment; or `D_planproxy_cap` has a positive lower simultaneous bound. The latter directly falsifies the claim that the trajectory increment is specific to a more coherent endpoint.
3. **Inconclusive:** O4 event/ESS or capture-adequacy support is insufficient, closure fields are predominantly missing/invalid, unknown provenance dominates, paired test availability is unstable, simultaneous intervals are wide, or methods disagree. Do not relabel unknown cases, alter the 72-hour rule, pick a subgroup, or choose a favorable seed after test scoring.

Falsification runs are frozen once: remove assay content but retain timestamps/opportunity; remove late assay rows in `(t0+35,t0+42]`; compare R28 with R42; permute assay labels/content within patient while preserving timestamps and availability; compare O3 with O4; and compare O4 with O_planproxy_cap. A positive process-control result, survival of the within-patient content permutation, or O4 collapse with closure restriction is evidence against the assay-content/coherent-endpoint interpretation.

Supportive output establishes only that the trajectory predicts a narrower operational record with administratively closed procedure timing and downstream same-visit activity, and is not similarly predictive of the capture-adequate pre-opened-order/no-strict-coherence pattern. It does not establish treatment completion, intent, response, failure, mechanism, causality, benefit, or transport. Clinical adjudication of procedure intent, imaging response, outside-care capture, and patient-important outcomes would still be required.

## Actual deliverable and compute

The future experiment must newly produce:

- `endpoint_provenance_audit.csv`: one row per later TACE candidate with `tp`, `te`, closure validity/reason, O0–O4 flags, all qualifying pre/post source times and families, exact join key, order status rule, and overlap decisions;
- `capture_adequacy_audit.csv`: encounter-discharge and non-procedure timed-source evidence, capture-adequate flag, unknown reasons, and counts by split/time bin;
- `endpoint_class_counts.csv`: O0/O1/O2/O3/O4, O_planproxy_cap, O3-only, closure-unknown, capture-unknown, overlap, risk-set, R42/R28, and ESS/weight-tail counts;
- `heldout_predictions_losses.csv`: method, feature block, endpoint, weighting, patient-level loss, and risk-bin predictions;
- `selection_robust_contrasts.csv`, `endpoint_falsification.csv`, `trajectory_gru_sensitivity.csv`, `trajectory_support_freeze.json`, `trajectory_decision_gate.json`, and `claim_output_map.md`, with each conclusion linked to computed rows and simultaneous uncertainty.

Completion requires deterministic endpoint and capture audits, held-out predictions/losses from both methods, frozen support/ESS gates, simultaneous uncertainty, falsification outputs, and an output-linked conclusion. This proposal contains no fitted result.

The planned future workload remains within the parent envelope: source materialization/audits, elastic-net, weighting, bootstrap, and permutations approximately 4 CPUs and 16 GiB for 1–3 hours; compact GRU approximately 4 CPUs, 16 GiB, one allocated A100 for 2–5 hours across three seeds and shared folds. Estimates are unmeasured. If a GPU job is used, request one allocated GPU and use `cuda:0`; ordinary shell CUDA visibility is not a feasibility test. The future solver envelope remains 16 CPUs, 262,144 MiB, up to eight GPUs, and 28,800 seconds.

## What changed and what remains unresolved

Changed from `[prior hypothesis]`:

1. The parent’s asymmetrically observed planned-only label is replaced by `O_planproxy_cap`, restricted to a separately capture-adequate stratum.
2. Missing downstream source is assigned to `unknown_provenance`, never to planned-only.
3. A stricter nested O4 endpoint requires valid `procedures.结束时间` and O3 downstream activity; O3 is retained as a boundary so closure sensitivity is measurable.
4. Support now requires a nonpositive capture-adequate process-control contrast, not merely absence of a post-source row.

Not identifiable with this snapshot: whether the procedure was intended or completed, why it was performed, radiographic response/progression, outside-care events, biological mechanism, causal treatment effect, or patient benefit. Post-procedure examinations, orders, and medications can still be care-intensity/documentation consequences, and encounter discharge/non-procedure rows are only capture indicators. If O4 and the process control remain indistinguishable, abandon clinical assay interpretation and pursue intent/imaging/response adjudication or better longitudinal capture rather than adding model complexity.

## Compact bibliography

[K1] Shmatko A, Jung AW, Gaurav K, Brunak S, Mortensen LH, Birney E, Fitzgerald T, Gerstung M. Learning the natural history of human disease with generative transformers. Nature. 2025. DOI: 10.1038/s41586-025-09529-3.

[K2] Urbut SM, Ding Y, Nakao T, Koyama S, Misra A, Jiang X, Harish A, Gaffney L, Hornsby WE, Smoller JW, Gusev A, Natarajan P, Parmigiani G. A Bayesian framework for longitudinal EHR and genetic discovery. Nature. 2026. DOI: 10.1038/s41586-026-10780-5.

[K3] Liu Y, Liu Y, Zhao Y, Luo Y, Hao X. From static snapshots to longitudinal trajectories: artificial intelligence in women's reproductive and ovarian health. Frontiers in Endocrinology. 2026. DOI: 10.3389/fendo.2026.1893963.

