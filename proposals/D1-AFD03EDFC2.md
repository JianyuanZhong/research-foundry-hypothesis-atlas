# Episode 20 child: pre-endpoint documentation-conditioned assay contrast

Status: design only. No cohort count, prevalence, fitted result, effect estimate, or clinical conclusion is claimed.

Parent: [prior hypothesis]. This child makes one substantive advance beyond the Episode-19 closed-coherent endpoint repair: it asks whether the assay-trajectory increment remains when patients are compared at the same level of pre-endpoint documentation intensity. It preserves the fixed HCC estimand, O0/O1/O2/O3/O4 provenance classes, capture-adequate O_planproxy_cap, unknown-provenance rules, temporal split, matched elastic-net/GRU methods, uncertainty family, and non-adjudication limits.

## Scientific opening and importance

The strongest claim supported by the inherited evidence is narrow: in patients with a first dated exact-code TACE record and observation through day 42, an assay trajectory may improve held-out prediction of a later operational TACE record over a day-42 assay snapshot after measured severity, assay opportunity, observation, and care-workflow features are considered. O0–O4 are record-defined outcomes. They are not adjudicated treatment completion, intent, response, progression, failure, survival, benefit, or utility.

The unresolved claim is whether an incremental trajectory signal is more specific to the later closed-coherent TACE record than to residual documentation/capture intensity. A trajectory can encode biology or clinical state, but the same trajectory can also be a marker that a patient has repeated encounters and many recorded orders, examinations, and medications. Episode 19 made the endpoint provenance stricter and removed absence-based “planned-only” labeling. It did not yet test whether a trajectory increment survives explicit equalization of the observable care-documentation process before the prediction window.

This matters because a signal that remains after pre-endpoint process conditioning would justify a blinded clinical/imaging validation study focused on whether the assay sequence carries information beyond recorded care activity. A signal that disappears, or is equally strong for the capture-adequate pre-opened-order process pattern, would redirect the work toward workflow prediction and endpoint acquisition. Neither result establishes a biological mechanism or treatment effect. The available HCC data do not contain validated intent, imaging response, outside-care capture, or patient-important outcomes.

[K1] demonstrates that ordered health-record histories can support temporal prediction while also revealing biases learned from the records; it does not validate an HCC TACE code or establish assay biology. [K2] shows that an explicit longitudinal likelihood can support inverse-probability adjustment for selection, but it does not make observational weighting causal or supply HCC intent/response labels. [K3] distinguishes recorded time from biological and decision time and bounds interpretation of temporal models without calibrated action/outcome validation. This child adds a single, predeclared, data-bound process-conditioned contrast to those general lessons.

## Hypothesis and single estimand contrast

Primary hypothesis:

> Within equalized strata of pre-endpoint non-assay documentation intensity, the assay trajectory has a larger held-out incremental loss reduction for the inherited closed-coherent TACE proxy O4 than for the inherited capture-adequate pre-opened-order/no-strict-coherence process pattern O_planproxy_cap.

This is a predictive/descriptive hypothesis about records. It is not a causal, mechanistic, intent, completion, response, or benefit hypothesis.

Retain the inherited feature blocks:
- A0 = M0 + B0 + P_obs + P_care;
- A_snap42 = A0 + S42;
- A_traj42 = A0 + T42;
- primary trajectory-versus-snapshot loss contrast D_j = L_w(A_snap42,j) − L_w(A_traj42,j), where positive values favor the trajectory model.

The one new contrast is process-conditioned and is computed identically for the two fixed endpoint labels:
- Define Q_pre using only non-lab records in [t0−365 days, t0+42 days].
- Fit/predict the inherited models without any post-t0+42 input.
- For endpoint j, let R_Q(j) be the equal-Q_pre-stratum average of endpoint-specific baseline-relative patient-level loss reductions, with the inherited ordinary or R42 weighting:
  R_Q(j) = (1/5) sum over q=1..5 of [(L_w,q(A_snap42,j) − L_w,q(A_traj42,j)) / L_w,q(A_snap42,j)].
  The denominator is the snapshot loss for the same endpoint, split, Q stratum, weighting arm, and test resample; a stratum with a zero or non-estimable denominator is missing, not silently pooled.
- Report the single primary process-conditioned contrast:
  C_Q = R_Q(O4) − R_Q(O_planproxy_cap).

C_Q > 0 means the assay increment is larger for O4 than for the process pattern after equalizing the observed pre-endpoint documentation process, on an endpoint-specific relative-loss scale. C_Q ≤ 0 is adverse to the proposed specificity claim. This is the only new inferential contrast; raw endpoint losses, component R_Q values, and the O0–O3/O4 sequence are descriptive support and falsification diagnostics, not additional selection criteria. O_planproxy_cap remains a record process pattern, never planned treatment.

The conditioning is strictly pre-endpoint: Q_pre cannot use the later candidate procedure, tp, procedure closure te, downstream rows, the O4/O3 classes, the O_planproxy_cap class, or any data after t0+42. The prediction risk window starts at t0+43, so Q_pre is frozen before endpoint follow-up begins. It is an audit/standardization variable, not a claim that documentation intensity is a sufficient confounder.

## Population and temporal boundaries

Use the first row in procedures for each patient whose Unicode-normalized, trimmed, case-folded 手术 equals TACE, with nonmissing patient index, visit number, and parseable 开始时间. Call its start t0. Apply the inherited deterministic duplicate/alias audit, malformed-date exclusions, early-repeat exclusions, and all-source observation requirement through t0+42 days for R42. Preserve the R28 pre-day-42 arm.

Use only 患者主索引 for patient grouping and exactly (患者主索引, 就诊号) for visit-level joins. Never join using name, identity card, phone, insurance card, file order, or an incompatible identifier namespace.

Each later candidate has a valid tp in [t0+43, t0+181). Use the inherited 14-day risk grid [43,57), [57,71), ..., [169,181) only for modeling. Retain first-event handling, right censoring, R42/R28 weighting, and observation boundaries exactly. Q_pre is computed before the risk grid and is not a post-index endpoint feature.

### Exact Q_pre definition

For each eligible index patient, in [t0−365,t0+42] count:

1. n_enc: distinct encounter keys (患者主索引, 就诊号) in encounters with parseable 就诊时间 (the key is counted only once);
2. n_ord: order rows in orders with nonblank parseable 开立时间, nonblank 医嘱状态, and status not containing normalized cancellation tokens 取消, 作废, 撤销, or 停用;
3. n_exam: examination rows in examinations with parseable 开始时间;
4. n_med: medication rows in medications with parseable 开始时间.

Do not count labs in Q_pre; labs are reserved for B0, S42, T42, assay opportunity, and the trajectory/snapshot comparison. Do not use clinical text, endpoint rows, procedure closure, or post-window sources. Counts are source-row counts after the stated validity rules; duplicate visit keys are de-duplicated only for n_enc, and all duplicate source rows are retained in the audit.

Fit the development-only scalar Z_pre = log1p(n_enc) + log1p(n_ord) + log1p(n_exam) + log1p(n_med). Cut it into five equal-frequency development quintiles, using development patients only. Freeze those cutpoints and apply them to the untouched temporal test set; values outside the development range use the nearest boundary stratum. If a patient has no valid non-lab record, retain Q_pre=Q1, record the zero-count reason, and do not treat missingness as low biology. Report the four component counts, tied cutpoints, boundary assignments, and test availability. Q_pre is not an outcome-derived feature and cannot change the fixed endpoint classes.

## Fixed endpoint provenance and unknown rules

Retain all inherited operational classes:

- O0: first later unique literal-code TACE.
- O1: O0 satisfying the frozen semantic hepatic-arterial procedure rule plus valid same-patient/same-visit timed examination or order corroboration.
- O2: O1 plus frozen same-visit medication corroboration.
- O3: O2 plus at least one qualifying examination, order, or medication row on the exact visit key with nonmissing event/start time u strictly after tp and no later than tp+72 hours. Orders have nonblank status and do not contain normalized cancellation tokens.
- O4 closed-coherent: O3 plus a valid procedure 结束时间=te from the same later procedures row, parseable with 0 ≤ te−tp ≤ 72 hours. Zero duration is allowed. Negative, missing, or longer-than-72-hour closure is closure_unknown, not a negative clinical event.

Retain the Episode-19 capture-aware process comparator exactly:

- post-window capture-adequate: for the exact candidate visit key, 1 if either encounters.出院时间 is valid and at least tp+72 hours, or at least one non-procedure row with valid time in (tp,tp+72 hours] is observed in examinations.开始时间, orders.开始时间, medications.开始时间, or labs.检验时间; otherwise 0. This is observable-record evidence, not proof of complete capture.
- O_planproxy_cap: later literal TACE candidate with a same-visit order whose 开立时间 is valid in [tp−7 days,tp), post-window capture-adequate=1, complete provenance-rule audit, no O4 classification, and no qualifying O3 post-procedure examination/order/medication. A complete audit requires every relevant post-source time and every used order status to be present and valid; orders cannot be cancellation tokens.
- unknown_provenance: any candidate for which post-window capture-adequate=0 and no O4/O3 evidence classifies it; missing post-source rows and missing order status/time are not planned-only evidence. If a required provenance field is missing, classify unknown rather than using another observed row to rescue it.
- If a candidate meets O4 and the pre-opened-order rule, classify O4 and retain an overlap flag; exclude it from O_planproxy_cap. O3 without O4 is O3-only, not O_planproxy_cap. A pre-opened order with inadequate capture remains unknown.

Unknown, closure-invalid, and unresolved classes must be reported by split and time bin. They are never relabeled to make C_Q estimable. For any inherited target/censoring treatment of unresolved classes, use the parent’s fixed risk-set rule and expose the resulting audit; do not use unknown_provenance as a negative process-control event.

## Exact HCC bindings and availability

Snapshot: [source checksum]. The HCC catalog lists 12 ordinary CSV files; every member is ordinary file and no archive member is unpacked.

| table | exact source path and SHA-256 | columns/times used |
|---|---|---|
| procedures | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源; t0, tp/te, O0–O4, closure audit |
| encounters | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 就诊时间, 入院时间, 出院时间, 就诊科室; joins, M0, P_obs/P_care, n_enc, capture adequacy |
| examinations | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 检查号; O1/O3, n_exam, capture timing |
| orders | [internal dataset path](非药品)_2062526727266216118.csv; [source checksum] | 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱状态, 频次; O1/O3, n_ord, pre-open audit, status/time audit |
| medications | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 用药, 单次用药剂量, 单次用药剂量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型; O2/O3, n_med, capture timing; no drug indication invented |
| labs | [internal dataset path]; [source checksum] | 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间; B0/S42/T42, assay opportunity, capture adequacy |
| vitals | [internal dataset path]; [source checksum] | identifiers only: 患者主索引, 就诊号; coverage audit only, no payload |
| transfers | [internal dataset path]; [source checksum] | identifiers only: 患者主索引, 就诊号; coverage audit only |
| clinical_documents | [internal dataset path]; [source checksum] | context/coverage only; no validated event-time or intent field |
| front_page | [internal dataset path]; [source checksum] | nominal/identifier-only table; not used as evidence |
| pathology | [internal dataset path]; [source checksum] | context only; no validated timed response field |
| diagnoses | [internal dataset path]; [source checksum] | context/coverage only; lexical flags are not diagnoses or temporally complete outcomes |

All source tables are read-only. The catalog documents many-to-one child-table relationships to encounters on (患者主索引, 就诊号) and requires duplicate verification. HCC local encounter dates are available only as released local dates; exact dates are not released. Lab units/reference ranges are absent, and nominal vitals/transfers contain identifiers only. Images, validated procedure intent/scheduling, radiology response, outside-care capture, technical TACE detail/dose, toxicity, survival, utility, treatment benefit, and expert adjudication are unavailable. These limits prohibit biological, causal, response, failure, intent, benefit, or transport claims.

## Baseline and substantive learned alternative

Both methods receive the same eligible patients, risk grid, right-censoring masks, O0–O4/O_planproxy_cap labels, Q_pre audit, R42 weights, R28 arm, and split. Endpoint class and post-tp variables are never predictors. Q_pre is used only for the predeclared equal-stratum evaluation of C_Q.

Transparent baseline: fit the inherited elastic-net pooled-logistic discrete-time hazard with intercept, 14-day risk-bin indicators, M0/B0/observation/care/assay-opportunity blocks, and nested snapshot/trajectory blocks. Use alpha 0.5. Fit lambda, parser, token dictionary, assay-specific robust scaling, imputation, and R42 selection weights only inside grouped development folds. Produce separate first-event targets for O0/O1/O2/O3/O4 and O_planproxy_cap under the inherited unknown/censoring rule.

Matched learned alternative: fit the inherited compact time-aware GRU with the same eight assay labels, numeric/qualitative/inequality content, sample type, relative time, inter-event time, and opportunity tag from t0−365 through t0+42, plus M0/workflow covariates at the hazard head. Use one GRU layer, hidden size 32, dropout 0.10, head 32/16, Adam 1e−3, weight decay 1e−4, at most 50 epochs, eight-epoch early stopping, and fixed seeds 17/29/41. The GRU tests whether irregular ordering/nonlinear assay combinations add information that deterministic summaries lose. A GRU gain without C_Q separation is representation-sensitive workflow prediction, not evidence of biology.

The baseline is retained for auditable feature blocks, source-family counts, weighting, Q strata, and provenance. The GRU is retained because it tests a substantive representation uncertainty on the same scientific question; complexity and GPU use are not evidence of value. Defer transformers, narrative NLP, causal-intent models, mechanistic response models, and imaging models because required validated intent/response labels, image/report availability, lab units/reference ranges, and outside-care capture are absent. Revisit only after O4 support and the process-conditioned gate pass.

## Split, uncertainty, falsification, and decision gates

Sort eligible index patients by t0; earliest 80% are development and latest 20% are untouched testing, with no patient in both. Use five grouped development folds for all preprocessing, Q cutpoints, weighting, hyperparameters, early stopping, and seed decisions. Do not use test endpoint classes to change Q, provenance, or model rules.

For every method and endpoint report patient-level paired log loss, Brier score, integrated Brier score, calibration, risk-bin counts, paired availability, and discrimination only as secondary. Primary inference is C_Q for O4 versus O_planproxy_cap. Use 1,000 patient-level paired bootstrap resamples of the untouched test set with one max-|t| simultaneous 95% family covering C_Q, component D_Q values, ordinary/R42 estimates, R28, O0–O4, O_planproxy_cap, and fixed falsifiers. Report Q counts/cutpoints, component counts, O3/O4 overlap, closure-invalid and unknown reasons, capture-adequate fraction, event/risk-set counts, R42/R28 ESS, weight tails, and paired availability by Q stratum.

Falsification runs are frozen once:
1. remove assay content but retain assay timestamps/opportunity;
2. remove late assay rows in (t0+35,t0+42];
3. compare R28 with R42;
4. permute assay labels/content within patient while preserving timestamps and availability;
5. compare O3 with O4 and report O3-only/closure-unknown;
6. compare inherited O4 and O_planproxy_cap labels within the same Q strata.

Supportive: C_Q has a positive simultaneous lower 95% bound; the O4 component is directionally positive in both elastic-net and GRU, ordinary and R42-weighted analyses, and the R28/late-window controls; O_planproxy_cap does not have a comparable positive trajectory increment; O4 provenance and Q strata have adequate untouched-test support; and no fixed content/time permutation reproduces the effect. This supports only a trajectory increment for a narrower closed-coherent operational record that is not equally explained by the tested pre-endpoint documentation intensity or process pattern.

Adverse: C_Q is nonpositive or its O4 gain disappears after Q conditioning; O_planproxy_cap shows a comparable or larger gain; the result is reproduced by within-patient content permutation, time-only features, late-window artifacts, or workflow-only inputs; O4 collapses relative to O3; or elastic-net and GRU disagree materially. This supports at most association with documentation/care workflow and does not justify more complex modeling.

Inconclusive: O4 or O_planproxy_cap events/risk sets are too sparse, Q strata have unstable paired availability, unknown/closure-invalid provenance dominates, Q cutpoints are tied or test support is absent, ESS/weight tails are inadequate, simultaneous intervals are wide, or methods/seeds disagree. Do not relabel unknowns, alter windows, choose a favorable stratum/seed, or reselect the contrast after test scoring. Continue only with better longitudinal capture or adjudication.

Computationally checkable claims are the deterministic Q and provenance audits, leakage-free split, model fits, losses, C_Q, uncertainty, and falsification outputs. Clinical adjudication is required for whether a procedure was intended/completed, whether an assay reflected tumor/liver biology, whether a record reflects outside care, and whether any signal relates to response, failure, survival, benefit, or actionability. No automatic verifier can establish those claims.

## Actual deliverable and completion criterion

The future experiment must newly produce:
- endpoint_provenance_audit.csv: every later TACE candidate, exact visit key, tp, te, O0–O4, O3-only, closure reason, all qualifying source-family times/statuses, pre-opened order, capture-adequacy, O_planproxy_cap, unknown/overlap decisions;
- pre_endpoint_process_audit.csv: patient, t0, four Q component counts, valid-time/status exclusions, Z_pre, frozen cutpoint version, Q stratum, and no post-t0+42 fields;
- endpoint_class_counts.csv: population, risk sets, O0–O4, O_planproxy_cap, unknown/closure reasons, Q support, R42/R28 support, ESS and weight tails;
- heldout_predictions_losses.csv: patient/risk-bin losses for both methods, feature block, endpoint, weighting, Q stratum, and split;
- selection_robust_contrasts.csv: endpoint-specific R_Q(O4), R_Q(O_planproxy_cap), C_Q, denominators, ordinary/R42/R28 and simultaneous intervals;
- trajectory_falsification.csv, trajectory_gru_sensitivity.csv, trajectory_support_freeze.json, trajectory_decision_gate.json, and claim_output_map.md.

Completion requires deterministic pre-endpoint and provenance audits, both held-out methods, frozen Q cutpoints, patient-level simultaneous uncertainty, fixed falsification outputs, and a conclusion linked to computed rows and intervals. This proposal contains no fitted result.

## Deferred alternatives and compute

Deferred alternatives are: (a) Q-adjusted regression with interactions, deferred because it would change the inherited hazard parameterization and is unnecessary for the first bounded process-conditioned check; (b) propensity-score matching or inverse-odds weighting on the four Q components, deferred because the observed process is not known to satisfy a treatment/selection model and extreme weights could replace a transparent diagnostic; (c) a negative-control outcome built from a different pre-index procedure, deferred because it would not preserve the fixed later-O4 HCC estimand; (d) transformer/narrative/imaging/mechanistic models, deferred for the unavailable validated modalities above. Revisit (a)/(b) only if C_Q is supportive but Q strata show severe imbalance or residual process dependence and expert review supplies a defensible selection model.

Discovery feasibility is bounded and does not shrink the future scientific question: inspect/materialize relevant columns and deterministic audits on CPU; approximate 4 CPUs and 16 GiB for 1–3 hours. Future elastic-net, grouped preprocessing, 1,000 bootstrap, and frozen permutations remain approximately 4 CPUs/16 GiB for 1–3 hours; the compact GRU remains approximately 4 CPUs/16 GiB and one allocated A100 for 2–5 hours across three seeds. These are unmeasured estimates. If the GRU is run, request one allocated GPU and use cuda:0; ordinary shell CUDA visibility is not a feasibility test. The future solver envelope remains 16 CPUs, 262,144 MiB, up to eight GPUs, and 28,800 seconds. No solver/proposer training is authorized by this design.

## Three inspected works

[K1] Shmatko A, Jung AW, Gaurav K, Brunak S, Mortensen LH, Birney E, Fitzgerald T, Gerstung M. “Learning the natural history of human disease with generative transformers.” Nature. 2025;647:248–256. DOI 10.1038/s41586-025-09529-3. The inspected abstract and temporal-method passage report ordered health-record trajectory modeling, held-out/external validation, and learned biases. It supports using time-ordered records while bounding interpretation of documentation-derived patterns. It does not validate HCC TACE provenance or assay biology. This proposal adds a pre-endpoint process-conditioned provenance contrast.

[K2] Urbut SM, Ding Y, Nakao T, Koyama S, Misra A, Jiang X, Harish A, Gaffney L, Hornsby WE, Smoller JW, Gusev A, Natarajan P, Parmigiani G. “A Bayesian framework for longitudinal EHR and genetic discovery.” Nature. 2026;656:924–935. DOI 10.1038/s41586-026-10780-5. The inspected abstract states that an explicit likelihood enables inverse-probability weighting for selection bias while preserving biological signal. It supports treating observation selection as an estimand/uncertainty issue, not proof of causality. It does not supply HCC procedure intent or response. This proposal uses fixed R42/R28 arms and a transparent Q audit rather than claiming causal correction.

[K3] Liu Y, Liu Y, Zhao Y, Luo Y, Hao X. “From static snapshots to longitudinal trajectories: artificial intelligence in women’s reproductive and ovarian health.” Front Endocrinol (Lausanne). 2026;17:1893963. DOI 10.3389/fendo.2026.1893963. The inspected full-text abstract and discussion passage distinguish recorded/calendar, biological, and decision time and report limited evidence linking temporal outputs to calibrated action and prospective outcomes. It bounds the claim: HCC assay timing is recorded time, not biological time, and O4 is not a clinical decision outcome. This proposal makes that boundary operational through a pre-endpoint audit and explicit non-adjudication gates.

See key-references.json and the three attached UTF-8 excerpts. All three inspections are limited to the cited retrieved passages; no unavailable paper or supplement is claimed.
