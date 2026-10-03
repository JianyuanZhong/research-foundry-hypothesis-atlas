# Episode 11 child: site-stratified transportability of the post-360 recorded-vital transition

Status: proposed substantive child of `[prior hypothesis]`. This is a design and source-validation plan. It reports no fitted coefficient, event count, prediction, metric, or scientific result.

## Scientific opening and falsifiable hypothesis

The parent asks whether a [0,360] laboratory/vital recording-process vector P, beyond measured state T, predicts a later persistent severe vital excursion before ICU exit. The unresolved boundary is transportability: P may be patient-linked if it reflects latent acuity and remains after state adjustment in hospitals not used for fitting; it may instead be hospital workflow if it varies with capacity, teaching status, region, measurement feed, future observation, or discharge timing.

The strongest relevant evidence inspected supports only bounded prior claims. Rajkomar et al. [K1] support cross-center prediction from temporally structured EHR data, not a recording-process mechanism or validated deterioration timestamp. Gao et al. [K2] (abstract-only) support that information presence/missingness can be predictive in dynamic competing-risk work and can shift across settings, not that eICU vital rows measure physiology. Hadler et al. [K3] support external validation with calibration and local data-pattern effects, not a clinical action or hospital-workflow mechanism. The parent is a proposed experiment, not an observed positive result.

H1: among adult first ICU stays eligible at 360 minutes, the parent’s early process increment Q_P^T for a later, source-defined persistent recorded-vital transition is patient-linked and transportable if it remains directionally coherent in held-out hospitals after T, future-measurement adjustment, and discharge-time diagnostics, with no dominant heterogeneity by hospital workflow strata.

The competing workflow hypothesis predicts that P will predict whether a qualifying future measurement exists, attenuate after observation weighting, reproduce a discharge-time pattern, or vary materially by capacity/teaching/region and fail in held-out hospitals. These are descriptive prognostic hypotheses, not causal tests of monitoring, staffing, treatment, clinician action, or discharge policy.

A supportive result would justify a clinical measurement/adjudication study of a patient-linked early-warning signal; an adverse result would prevent transport or clinical interpretation of the parent process signal; an inconclusive result identifies missing measurement or endpoint evidence.

## Population, temporal boundaries, and endpoint

All offsets are ICU-relative. Use the parent’s unchanged adult first-ICU construction: `unitvisitnumber=1`, `unitstaytype=admit`, numeric `age >=18` (retain `>89`), finite `patientunitstayid`, `hospitalid`, `unitdischargeoffset`, `unitdischargestatus`; among duplicate qualifying rows sharing `uniquepid`, retain the smallest finite `unitadmitoffset`, then smallest `patientunitstayid`. Primary risk set S6 is `unitdischargeoffset >360`. Parent P12, S720 and ICU-discharge-mortality modules remain unchanged secondary replication modules.

Predictors use only valid rows in [0,360], with offset 360 in the predictor window and never the event window. Follow-up is (360,720] or the earlier recorded ICU exit. Exit is a competing event, never a physiologic negative observation.

The primary endpoint is D_ST, a *recorded persistent severe-vital transition*, not “clinical deterioration”:

1. Use finite post-360 values from `vitalPeriodic.temperature`, `sao2`, `heartrate`, `respiration`, `systemicmean`, and `vitalAperiodic.noninvasivemean`.
2. Fixed source-audited thresholds are `sao2 <88`, `heartrate <40 or >140`, `respiration >35`, `systemicmean` or `noninvasivemean <55`, or `temperature <35 or >39.5`.
3. D_ST occurs when the same channel has two abnormal values at distinct offsets no more than 120 minutes apart, the first strictly in (360,720], and both before ICU exit. The first qualifying pair defines event time. No carry-forward, interpolation, discharge field, treatment, or label creates an event.
4. Retain a one-reading endpoint only as a prespecified sensitivity. The primary claim is an operational transition in recorded values.
5. Audit units, channel semantics, duplicate timestamps, impossible values, and whether two rows are distinguishable as distinct observations. Before clinical interpretation, a critical-care expert must review the source-defined threshold/semantics. If validation fails, D_ST is not a clinical endpoint: report descriptive recorded-value feasibility only and defer the clinical transport claim.

Define M as at least one finite candidate vital value in (360,720] before exit and M2 as a pair eligible for D_ST. Report both; missing future observation is not evidence of physiologic stability. ICU exits before D_ST are competing risks, separated into `unitdischargestatus == "Alive"` and `"Expired"`; an expired discharge is not a death time. Stays in ICU at 720 are event-free only for this horizon and after the observation/exit audit.

The primary estimand is six-hour cumulative incidence of D_ST before ICU exit in S6 on held-out hospitals. Estimate cause-specific discrete-time hazards in (360,480], (480,600], (600,720] for D_ST, alive exit and expired exit. Report patient-weighted pooled and equal-weight hospital-macro estimands; macro is the principal transportability summary.

## Why hospital metadata are justified

Join `patient.hospitalid=hospital.hospitalid` and use `hospital.numbedscategory`, `teachingstatus`, and `region` only for prespecified stratified estimands, audits and heterogeneity summaries. They are not prediction, process-permutation or observation-model features. The restriction is essential: direct site-feature prediction would show site identity, not a patient-linked process signal.

The fields are justified because the workflow rival predicts gradients: capacity can change monitoring density, teaching status can change rounding/documentation, and region can proxy feed or implementation. They are not adjudicated staffing, device integration, order/specimen semantics, or clinical-practice measures. Keep blank values as unknown; do not impute a workflow class. Report coverage and counts. Require >=100 S720 stays per viable hospital and >=5 viable hospitals. Rare category contrasts are descriptive, not causal.

For each held-out evaluation fold report by hospital and metadata stratum: S6 denominator, D_ST, M, M2, competing exits, measurement coverage, Q_P^T, Q_P^X, calibration and intervals. Summarize site-specific process increments minus the macro mean and interaction/heterogeneity summaries for each descriptor. Heterogeneity is a transport boundary, not proof the metadata cause workflow.

## Exact eICU bindings and source validation

Inherited catalog/snapshot: `[internal dataset path]`, [source checksum]; eICU snapshot `[source checksum]`. Sources are ordinary read-only gzip files, not archive members.

- Patient: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-ab037c09d7df9a3c.json`, [source checksum]. Join `patientunitstayid`; `uniquepid` only handles duplicates. Required cohort fields include `patientunitstayid,uniquepid,hospitalid,age,unitvisitnumber,unitstaytype,unitadmitoffset,unitdischargeoffset,unitdischargestatus,gender,ethnicity,admissionweight`.
- Lab: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-79bdb33275339b1a.json`, [source checksum]. Join `patientunitstayid`; time `labresultoffset`; use finite `labresult`, `labid`, `labtypeid`, `labname`, `labmeasurenamesystem`, fallback `labmeasurenameinterface`, `labresultrevisedoffset`; never `labresulttext`; parent rows require [0,360] and revised offset blank or <=360.
- Periodic vitals: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-a22c6d6981a32279.json`, [source checksum]. Join `patientunitstayid`; time `observationoffset`; parent channels are `temperature,sao2,heartrate,respiration,cvp,etco2,systemicsystolic,systemicdiastolic,systemicmean,pasystolic,padiastolic,pamean,st1,st2,st3,icp`; endpoint uses six named fields.
- Aperiodic vitals: `[internal dataset path]`, SHA-256 `8b23e5a50f8aabc6cb62fc69e2dcdf755a2e5649b1439a7ca413a7c5b2d5a9a`, schema `datasets/eicu/table-72ace5b89971196b.json`, [source checksum]. Join/time `patientunitstayid/observationoffset`; endpoint uses `noninvasivemean`; parent also uses the listed PA/cardiac/SVR fields.
- EOL: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-4a60395475cf75e7.json`, [source checksum]. Join `patientunitstayid`; finite `cpleolsaveoffset,cpleoldiscussionoffset`; do not use `activeupondischarge`.
- Apache: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-754bebf64d3d9909.json`, [source checksum]. Join only `patientunitstayid`; audit `actualicumortality,apachescore,predictedicumortality,apacheversion`; use none for D_ST or prediction.
- Hospital: `[internal dataset path]`, [source checksum], schema `datasets/eicu/table-811df7b2ef435e12.json`, [source checksum]. Exact header is `hospitalid,numbedscategory,teachingstatus,region`; join only through `patient.hospitalid=hospital.hospitalid`. A bounded source check observed 208 rows, bed categories `<100`, `100 - 249`, `250 - 499`, `>= 500` plus blank, teaching `f/t), and regions Midwest/Northeast/South/West plus blank. This validates availability, not cohort results.

Inherit parent X/T/P exactly: X is age, gender, ethnicity, admissionweight, up to 30 training-fold-selected lab analytes and 20 vital channels represented by latest valid [0,360] values with fold-wise median imputation; T adds [0,120), [120,240), [240,360] medians; P has lab/vital row counts, distinct offsets/bins, channel presence, last-offset gap, empty-run and empty-bin summaries. P is a recording proxy, not an order, specimen, bedside measurement, device, interface, or action. No post-360 value, exit, EOL, Apache, or hospital descriptor predicts D_ST.

## Split, matched baseline/learner, uncertainty

Use parent’s external split: viable hospital IDs sorted by SHA-256(`"eicu-transport-v2\\0"+hospitalid`) and greedily balanced by S720 stays into five contiguous hospital folds. Hold out complete hospitals. Internal reference is 20% patient-hash SHA-256(`"eicu-internal-v2\\0"+patientunitstayid`), not external validation. Selection, medians, standardization, risk models, weights, class handling and tuning are training-fold-only; descriptors appear only in held-out summaries.

Baseline: elastic-net pooled discrete-time cause-specific logistic hazards for D_ST, alive exit and expired exit in the three intervals, paired X versus X+P and T versus T+P. Learned alternative: capacity-matched histogram gradient boosting for the same hazards, inputs, folds, preprocessing, weighting option, seeds and tuning budget. GBM is retained to detect nonlinear state-by-process interactions; agreement is required, not a small-score chase.

Report cumulative-incidence Brier, time-dependent AUC, calibration-in-the-large/slope, observed-versus-predicted D_ST incidence, alert burden and net benefit at predicted-incidence 5%, 10%, 20%. Define Q_P^T=metric(T+P)-metric(T), Q_P^X=metric(X+P)-metric(X), A_T=Q_P^X-Q_P^T; use inherited 0.01 AUC and 0.005 net-benefit negligible margins where defined. Primary transport contrast is hospital-macro Q_P^T on held-out hospitals, paired with pooled estimates, M/M2 and metadata strata.

Use 2,000 identical hospital-cluster bootstrap resamples for macro, pooled, site-stratum, learner, state version and null contrasts. Preserve per-site counts, coverage, positivity and effective sample size. Fit a training-fold observation model for M2 from X,T,P and at-risk/exit history; truncate weights only at prespecified 1st/99th percentiles. Unweighted results remain the main ascertainment evidence.

## Falsification, interpretation, and decision

1. Inherit X-state and trajectory-state nulls: cyclically reassign complete P within hospital and training-fold risk/state cells without outcomes or P values.
2. Inherit unrestricted within-hospital process permutation and +180-minute process-offset displacement.
3. Compare P→M, P→M2 and P→D_ST; an increment for future availability that disappears after weighting supports ascertainment selection.
4. Within hospital, T-risk cells and exit bands (360–480, 480–720, >720), permute complete P without changing D or exit. Reproduction supports discharge/observation timing.
5. Repeat pair, one-reading, and no-pre-360-pair endpoint versions; large changes are a boundary warning.
6. Enforce no post-window predictors, no hospital-feature leakage, no patient cross-fold, no exit-as-negative coding, and no Apache/EOL leakage.

Support requires source/threshold audit, >=5 viable hospitals, adequate per-site D_ST/M2/exit support and positivity; both learners show coherent held-out macro Q_P^T beyond T, paired interval excluding the 0.01 AUC margin plus coherent calibration or 10% net-benefit contrast; survival of weighting and state/discharge nulls; and no one-site dominance. The exact supportive claim is only that early recording process is associated with a later recorded persistent severe-vital transition under this eICU risk set. It is not physiology, deterioration, monitoring effect, treatment benefit or a clinical recommendation.

Adverse means adequate endpoint support but no transportable increment, or a selection-sensitive/site-concentrated increment; retain only a bounded recording/discharge association and abandon the clinical interpretation. Inconclusive means failed unit/threshold/duplicate validation, <5 viable hospitals, sparse strata, invalid joins/offsets, poor M2 positivity/effective sample size, wide intervals spanning the margin, or no clinical adjudication. An imprecise null is not refutation. No monitoring, treatment, discharge or EOL change follows.

Continue to clinical measurement/adjudication only if the endpoint passes source review and the held-out weighted increment survives T, state, future-observation and discharge diagnostics with cross-site coherence. Revise toward workflow/measurement validation if signal tracks M/M2, exit time or strata. Defer/abandon temporal clinical interpretation if endpoint validity, support or positivity fails.

## Alternatives, compute, and required deliverable

The elastic-net baseline and histogram-GBM alternative use identical [0,360] inputs, S6, competing exits, three intervals, folds, nulls, metrics and bootstrap. Future planning is CPU: up to 16 CPUs, 262,144 MiB RAM, 28,800 seconds; this is inherited planning, not a measured full-study runtime. No GPU is required because it cannot resolve endpoint semantics or ascertainment. The observed source-header/category audit is bounded; extraction, fitting and bootstrap are uncomputed.

A raw-event neural sequence model is deferred because current fields lack order/specimen/device/interface semantics; revisit only after endpoint adjudication and a diagnostic show fixed bins lose clinically meaningful timing. A hospital random-effects model is deferred as primary because held-out hospitals are the scientific estimand; revisit descriptively if stable macro/pooled residuals remain unexplained. Do not shrink the question to discovery compute.

The solver must newly save: frozen S6 plus inherited P12/S720/S6 manifests and duplicate/EOL/Apache/hospital/exit audits; fold-isolated X/T/P and process audit; threshold/unit/timestamp validation and D_ST/M/M2/exit times; paired baseline/GBM predictions unweighted and weighted; pooled/macro/site-stratum metrics, interactions, 2,000-bootstrap intervals and all nulls; and a conclusion report linking every supportive/adverse/inconclusive statement to output rows and intervals plus machine-checkable binding/leakage checks. Completion is either a supported transport result or an explicit endpoint-invalid/under-supported deferral.

## Missing evidence and verifier boundary

eICU cannot establish whether a lab/vital row is an order, specimen, bedside measurement, device aggregate, interface transmission, or clinician action. It lacks reliable death time, staffing/workflow logs, treatment assignment, device provenance and adjudicated deterioration. carePlanEOL is recorded, not goals-of-care adjudication; missing rows do not mean no decision. actualicumortality is an Apache audit field, not a D_ST gold standard. Hospital categories are coarse descriptors, not causal workflow measures.

A verifier can check hashes, columns, joins, fold membership, offsets, pair logic, competing exits, no post-window predictors, no hospital leakage, training-only preprocessing/weights, saved predictions, bootstrap intervals and conclusion-to-output links. It cannot establish true deterioration, mechanism or clinical action; those require expert review and another study.

## Key evidence and bibliography

The three inspected works are inherited unchanged from the parent; no new literature mapping is claimed.

[K1] Rajkomar et al. supports cross-center prediction from temporally structured EHR representations, but not recording-process physiology or a validated eICU deterioration endpoint.

[K2] Gao et al. (abstract-only) supports dynamic competing-risk evaluation where presence/missingness can be predictive and transport-sensitive, but not these eICU thresholds.

[K3] Hadler et al. supports external validation with calibration and local data-pattern/harmonization constraints, but not a causal workflow mechanism or clinical action.

The parent’s receipt-hashed key-references.json and three UTF-8 inspected excerpts are unchanged evidence attachments; preserve their original receipts, URIs, hashes, and inspection limits. No inaccessible supplementary methods or unavailable paper text is claimed.
