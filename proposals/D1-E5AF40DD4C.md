# Patient-state versus hospital-documentation signal in eICU testing-process transportability

Status: proposed child of assessed valid [prior hypothesis]. No fitted study result is claimed. The bounded prefix diagnostic is recorded separately as observed feasibility evidence.

## Scientific opening and unresolved claim

The parent establishes a useful but incomplete comparison: a value-only model versus the same nonlinear learner augmented with early laboratory-result presence, count, and timing. A larger internal-to-hospital-held-out loss for the augmented model would be consistent with workflow dependence, but it would not distinguish a hospital/documentation shortcut from ordinary case-mix or an unmeasured severity signal. The available evidence supports three narrower premises: rich EHR representations can predict mortality across centers [K1]; the presence and timing of EHR measurements can be predictive and can shift across settings [K2]; and external mortality models can retain discrimination while local data patterns affect calibration and adaptation [K3]. None establishes the unresolved patient-state/documentation distinction in eICU.

Leading explanation: patient-level process features (what was recorded, how often, and when) partly encode hospital-specific testing and documentation practice. They will show excess internal-to-hospital-held-out degradation, especially in calibration and decision utility; a within-hospital process-permutation negative control will preserve the hospital's process distribution but remove patient alignment, exposing any residual site/workflow signature.

Strong rival: process features are stable proxies for latent acuity or care intensity not captured by the observed laboratory values. In that case the aligned process model should retain incremental held-out discrimination/calibration, and within-hospital permutation should remove its incremental patient-level signal. A second rival is selection: conditioning on stays observed beyond six hours and on hospitals meeting the size threshold may change the case mix. The design reports this conditioning explicitly, uses only outcome-independent hospital eligibility, and does not interpret a residual association as causal.

### Falsifiable hypothesis

Among adult first eligible ICU stays with one unique patient stay, under observation beyond 6 hours, the process-aware model has a larger internal-to-hospital-held-out deterioration than the value-only model. The sharpened claim is that this excess deterioration is documentation/workflow-consistent if all of the following prespecified patterns occur:

1. aligned VP-GBM has positive paired excess deterioration in AUROC, Brier score, or absolute calibration-slope error, with the corresponding 95% hospital-cluster bootstrap interval excluding zero in at least one primary metric;
2. VP-GBM has lower held-out decision-curve net benefit at at least two of fixed 5%, 10%, and 20% thresholds, and this is not explained by an adverse value-only calibration pattern;
3. a within-hospital permuted-process negative-control model retains more of the internal advantage than the aligned-process model but loses it on held-out hospitals, or otherwise shows a larger internal-to-held-out gap. This pattern indicates that hospital/process distribution alone can create a transport penalty. If permutation collapses both performance and degradation to V-GBM, the patient-state rival is strengthened and the workflow interpretation is not supported.

The parent-level hypothesis is falsified when aligned VP-GBM is no less transportable than V-GBM with no adverse calibration or utility pattern. The sharpened documentation interpretation is falsified when the aligned process model retains held-out incremental value and the permuted-process model does not show a transport penalty. Discordant or imprecise results are inconclusive, not evidence for either mechanism.

This is a descriptive prognostic transportability estimand, not a causal effect of ordering or documenting a test. It cannot establish that changing testing changes mortality.

## Clinical importance and advance

If a model depends on local recording practice, an apparently safe mortality score can mis-rank patients or misstate absolute risk after deployment. A documentation-consistent result would justify omitting process features, requiring site validation/recalibration, or harmonizing laboratory feeds before a silent prospective evaluation. A patient-state-consistent result would justify retaining process information only with external validation and measurement review; it would not make testing an intervention.

The substantive advance over the parent is a testable decomposition of the process signal. The aligned-versus-within-hospital-permuted contrast preserves the same hospital-specific process distributions while breaking patient-level alignment. The time-reversal check preserves the same event set and analyte values while testing whether the result depends on chronology. The future-window check is a deliberate positive leakage control, not a clinical model. These checks separate descriptive patient-aligned information, site-distribution information, and timing artifacts more directly than a single external performance gap.

## Actual scientific deliverable

The solver must newly produce:

- a frozen cohort manifest, repeat-patient exclusions, outcome-independent hospital eligibility, and deterministic hospital folds;
- leakage-safe 0–360 minute patient features and three model prediction sets for every held-out eligible stay: V-Logit, V-GBM, and VP-GBM;
- an additional within-hospital process-permuted VP-GBM diagnostic and a time-reversed process diagnostic, each with exact random seed and permutation manifest;
- a temporal additive model (T-Logit) using three 120-minute bins, to test whether explicit chronology changes the interpretation;
- patient predictions, per-hospital AUROC/AUPRC/Brier/calibration intercept and slope/net benefit, and 2,000-replicate hospital-cluster bootstrap intervals for all prespecified contrasts;
- a report that labels supportive, adverse, and inconclusive outcomes and links each conclusion to computed output files.

Completion is not a favorable result. It requires predictions for all primary models, the permutation/time-shift outputs, the cohort/fold manifest, uncertainty estimates, and an interpretation that does not exceed the estimand.

## Population, time zero, horizon, and outcome

Time zero is ICU admission. eICU offsets are minutes relative to ICU admission. Include rows from the patient table with:

- unitvisitnumber = 1 and unitstaytype = admit;
- age parsed as numeric and age >= 18, retaining the eICU >89 category as adult;
- nonmissing patientunitstayid, hospitalid, uniquepid, unitdischargeoffset, and unitdischargestatus;
- unitdischargeoffset > 360 minutes, not >=360, so the primary cohort is observed beyond the landmark rather than allowing a death/discharge exactly at the boundary.

Exclude duplicate patientunitstayid rows and exclude any uniquepid with more than one otherwise eligible primary stay in the snapshot. The latter is a leakage repair: the source may contain repeated patients across health-system stays or hospitals, and a hospital-held-out split cannot otherwise guarantee that the same de-identified patient is not represented in training and held-out hospitals. Report the count and assess the excluded-repeat cohort descriptively, without reintroducing it to the primary estimand. If uniquepid is not unique/nonmissing as required, stop and report infeasibility rather than silently reverting to stay-level splitting.

The primary outcome is Y=1 when unitdischargestatus equals Expired and Y=0 for a non-Expired ICU discharge. It is all-cause ICU mortality by the end of the ICU stay, not 24-hour mortality or complete hospital mortality. The estimand is conditional on this cohort being under ICU observation beyond 360 minutes. unitdischargeoffset and unitdischargestatus are eligibility/label fields only and never predictors. Compare the discharge-status label descriptively with apachePatientResult.actualicumortality by patientunitstayid; do not replace the primary label or use any Apache field as a feature. A discordance audit cannot resolve the absence of a death timestamp.

## Exact data binding

Catalog: [internal dataset path]
Catalog [source checksum]
eICU snapshot: [source checksum]

All four configured sources are read-only ordinary gzip CSV files; no archive member is used.

1. Patient anchor: source path [internal dataset path] 2.0数据/patient.csv.gz; catalog source [source checksum]; table JSON datasets/eicu/table-ab037c09d7df9a3c.json; schema [source checksum]. Join key patientunitstayid. Cohort keys/fields: patientunitstayid, patienthealthsystemstayid, uniquepid, hospitalid, unitvisitnumber, unitstaytype, age, gender, ethnicity, admissionweight, unitadmitoffset, unitdischargeoffset, unitdischargestatus. uniquepid is used only for repeat-patient exclusion and grouped internal splitting, never as a model feature.

2. Hospital/site: source path [internal dataset path] 2.0数据/hospital.csv.gz; catalog [source checksum]; table JSON datasets/eicu/table-811df7b2ef435e12.json; schema [source checksum]. Columns hospitalid, numbedscategory, teachingstatus, region. Join only patient.hospitalid=hospital.hospitalid. Site columns are eligibility/stratification/reporting only, never predictors.

3. Laboratory events: source path [internal dataset path] 2.0数据/lab.csv.gz; catalog [source checksum]; table JSON datasets/eicu/table-79bdb33275339b1a.json; schema [source checksum]. Required columns labid, patientunitstayid, labresultoffset, labtypeid, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface, labresultrevisedoffset. Join only lab.patientunitstayid=patient.patientunitstayid. Use labresultoffset in [0,360] and retain a row only when labresultrevisedoffset is blank or in [0,360]. Parse finite numeric labresult; exclude labresulttext from predictors. Analyte key is normalized labname plus labmeasurenamesystem, falling back to labmeasurenameinterface when the system is blank. There is no order status, specimen collection time, interface audit trail, reason for missingness, or clinician rationale.

4. Outcome audit: source path [internal dataset path] 2.0数据/apachePatientResult.csv.gz; catalog [source checksum]; table JSON datasets/eicu/table-754bebf64d3d9909.json; schema [source checksum]. Join by patientunitstayid and audit actualicumortality only. Exclude all Apache scores, predicted/actual mortality and LOS fields from predictors.

The exact binding audit and bounded header/timing diagnostic are attached beside this proposal.

## Feature construction and leakage controls

Construct all feature selection, category levels, medians, scaling, and model fitting separately within each outer training fold. Select the top 30 analyte keys by distinct eligible training-stay coverage, subject to at least 1% training-stay coverage. If fewer than 30 meet the rule, retain all and report the number. Never select analytes from held-out hospitals.

For V features, use age, gender, ethnicity, admissionweight, and the latest finite numeric value per selected analyte in [0,360]. Do not carry values from outside the window. Impute a missing value with the training-fold analyte median; missingness is intentionally represented only in process models. Preserve unknown categories as explicit levels and learn category handling in training.

For aligned process P, add per-analyte result-present indicators, valid-result count, distinct-result-offset count, first and last valid-result offsets, overall valid-lab row count, and overall distinct-offset count. Counts use only rows meeting both result and revision timing rules. P represents observed result documentation/measurement, not confirmed testing orders.

For the temporal alternative, use three bins [0,120], (120,240], (240,360]. For each selected analyte and bin, use the last valid value, presence indicator, and valid-result count, plus the same static predictors. Fit a fixed elastic-net logistic model; training-fold medians and category rules only. This preserves temporal order that latest-value VP-GBM loses, while keeping process and value channels explicit.

A timing audit must verify that no source row with result or revision offset >360 enters any primary feature. A code-level manifest must show that discharge fields, hospital id/metadata, Apache fields, diagnosis, notes, therapies, and post-landmark events are absent from model matrices.

## Models and method alternatives

The simple additive baseline is V-Logit: elastic-net logistic regression with static predictors and 30 latest imputed values, fixed alpha and regularization chosen before fitting. It is transparent and tests whether conclusions depend on a familiar additive value model.

The parent’s capacity-matched nonlinear ablation is primary: V-GBM is a fixed histogram gradient-boosting classifier with only V; VP-GBM is the identical implementation, seed, preprocessing, class-weight policy, and hyperparameters with aligned P added. The paired VP-GBM minus V-GBM contrast is the main process attribution comparison. No held-out metric selects a model.

The scientifically substantive temporal/mechanistic alternative is T-Logit, not a generic larger neural model: separate 120-minute value/process channels test whether chronology and delayed documentation carry information lost by latest-value summaries. It can reveal whether an apparent process effect is concentrated in early versus late measurement and whether value trajectories explain the internal advantage. It is intentionally not used to rescue an unfavorable VP result.

A temporal neural sequence model was considered and deferred. It could preserve every event ordering and nonlinear interaction, but the available lab table lacks order/specimen/collection semantics, so it would learn the same ambiguous observation process with less attribution clarity. Revisit it only if T-Logit and VP-GBM show a reproducible timing signal and a readiness check demonstrates adequate events per hospital. This is a selection/deferral decision, not a categorical rejection of neural or GPU methods.

## Split and estimands

First retain hospitals with at least 100 eligible primary-cohort stays, using no outcomes or laboratory features. If fewer than five such hospitals remain, stop as infeasible. Sort hospital IDs by SHA-256 of eicu-transport-v2 + NUL + hospitalid and assign contiguous hospitals to five folds by greedy balancing of eligible stay counts. All stays from a hospital remain in one outer fold.

Within each outer training set, an internal 20% reference sample is selected by a deterministic hash of uniquepid, stratified only using training labels and grouped so all stays of an included patient are together. It is a reference for internal performance, not external validation. The primary transport estimand compares the same fitted model on this internal reference with its held-out hospitals.

For model m, define AUC deterioration D_AUC(m)=AUC_internal(m)-AUC_external(m). Define Brier deterioration as Brier_external(m)-Brier_internal(m), and calibration deterioration as the increase in absolute calibration-slope error externally versus internally. The primary paired process contrast is D_AUC(VP-GBM)-D_AUC(V-GBM); secondary paired contrasts use Brier and slope. Report direct held-out VP-GBM minus V-GBM metrics and per-hospital paired values.

Compute AUROC (primary discrimination), AUPRC, Brier score, calibration intercept and slope, reliability summaries without site recalibration, and decision-curve net benefit at 5%, 10%, and 20%. The modeled action is trigger senior review/goals-of-care and monitoring review, not a treatment recommendation. Use a hospital-cluster bootstrap with 2,000 resamples, preserving all predictions within sampled hospitals, for 95% intervals. Report event prevalence, fold/hospital counts, and effective hospital sample sizes; no patient bootstrap is the sole uncertainty method.

## Prespecified negative controls and time-shift falsification

### Within-hospital process permutation

Within every hospital in each outer training fold, randomly permute the complete aligned P vector across eligible stays, preserving that hospital's process distribution and the marginal analyte/event counts while breaking its patient-level alignment with V and Y. Use a recorded seed and permutation manifest. Fit the same VP-GBM to V plus P-permuted. For held-out hospitals, apply an independent within-hospital permutation to P before prediction, using no labels. This is a diagnostic, not a selected model.

If P-permuted retains internal signal and loses it at held-out hospitals, that is evidence that a hospital/process distribution can mimic an apparent patient process effect. If P-permuted loses incremental signal while aligned VP-GBM retains held-out value, the patient-state rival is strengthened. If both are unstable or intervals are wide, call the distinction inconclusive. This control does not prove a hospital mechanism because the same process vector can encode residual case mix.

### Time-reversal placebo

Within [0,360], replace each retained event offset t with 360-t before calculating first/last offsets and the three temporal-bin features; keep patient, analyte, numeric value, revision eligibility, and event count unchanged. Refit/predict the prespecified reversed-P and reversed-T diagnostics with no retuning. A large loss only for timing-sensitive features supports a chronology-dependent observation pattern; unchanged performance says timing order is not needed for the observed association. Neither result identifies why a test was obtained.

### Future-window positive leakage control

For stays with unitdischargeoffset >720, build a separate 360–720-minute process feature vector using rows with result offset in (360,720] and revision offset <=720. Fit the same fixed learner only as a code audit. Its predictions and metrics must never enter the primary cohort, model comparison, bootstrap, or conclusions. A large signal is expected because it is post-landmark and confirms why the 360-minute boundary matters; any accidental use of this feature in a primary model is a readiness failure. This is the required time-shift/label-timing falsification check, not evidence supporting the clinical hypothesis.

## Interpretation rules, limitations, and missing evidence

Supportive of documentation/workflow dependence: the primary paired deterioration contrast is positive with its 95% interval excluding zero, VP-GBM has worse held-out calibration or net benefit at at least two thresholds, and the permutation/time-reversal pattern is consistent with hospital-distribution or timing sensitivity. State only that observed process signals are transportability liabilities consistent with documentation dependence.

Adverse: VP-GBM is at least as transportable and useful, or its held-out advantage is retained while P-permuted collapses; this favors stable patient-state information or another explanation and revises the documentation claim. It does not prove biological stability.

Inconclusive: intervals span zero, too few hospitals/events, repeat-patient exclusion or analyte selection makes the cohort unstable, primary and negative-control patterns disagree, or calibration and discrimination point in different directions without a prespecified utility interpretation.

Remaining unidentifiable evidence includes test orders, specimen collection, canceled orders, interface outages, clinician rationale, bedside acuity not measured in labs, care pathways, end-of-life decisions, and a death timestamp. Hospital-held-out folds do not randomize testing practice and cannot eliminate case-mix or selection bias. Clinical adjudication is required to interpret individual missing results and workflow causes. Prospective silent deployment, external data with order/interface fields, and an impact study are required before clinical use.

## Feasibility, compute, and selection record

Measured bounded diagnostic: direct header/hash verification completed in 1.49 seconds and the first 100,000 lab rows were summarized in 1.08 seconds on the discovery shell. These are not full-study runtime measurements.

Unverified solver planning estimate: CPU only, 16 CPUs, 64–128 GiB RAM, and 2–6 hours for full lab feature extraction, five hospital folds, three primary models, negative controls, and 2,000 hospital-bootstrap replicates; reserve within the parent’s stated 8-hour/16-CPU/256-GiB planning envelope. V-Logit/T-Logit should fit in minutes to under an hour; V/VP-GBM and feature extraction dominate. No GPU is required because this is a tabular, fixed-feature experiment; an allocated GPU is not prohibited but would not resolve the missing order/documentation semantics. A future readiness job must measure one fold and confirm memory before full execution.

Selected T-Logit because it tests a substantive temporal explanation at low, inspectable cost. Deferred temporal neural sequence model because it requires a larger, less interpretable representation while the key missing dependency is clinical event semantics, not model capacity. Revisit only under the rule above. No result from either model is claimed here.

## Three inspected works

[K1] Rajkomar et al. reports multi-center mortality prediction with rich sequential EHR data. It supports the feasibility and importance of cross-center prediction, but not a testing-process mechanism. This child adds a prespecified patient-process ablation, hospital-held-out transport estimand, and negative controls.

[K2] Gao et al. reports predictive value of missing indicators and cautions that missingness shifts can impair transportability. It is single-institution CLABSI work; this child tests an ICU mortality outcome across held-out eICU hospitals and separates aligned from within-hospital-permuted process.

[K3] Hadler et al. reports external mortality validation despite fragmentation and improved local adaptation, with calibration and data-availability burdens. It does not isolate laboratory process or patient state; this child measures unadapted transport and explicitly avoids causal interpretation.

## Evidence attachments

The three inspected source excerpts and their structured receipts are attached as:
- work/episode2-evolution/K1-rajkomar-2018-inspected-excerpt.txt
- work/episode2-evolution/K2-gao-2026-inspected-excerpt.txt
- work/episode2-evolution/K3-hadler-2026-inspected-excerpt.txt
- work/episode2-evolution/key-references.json

The exact source binding and bounded diagnostic are attached as:
- work/episode2-evolution/source-binding-audit.md
- work/episode2-evolution/bounded-schema-timing-diagnostic.md

Source excerpts are labeled provider/full-text extractions rather than claimed copies of unavailable original PDFs. Private source rows were not sent to public search.
