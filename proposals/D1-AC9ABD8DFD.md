# Does early laboratory documentation transport across ICUs because of workflow or acuity?

Status: Lead episode-2 proposal; substantive child of `[prior hypothesis]`. This is an eICU-native adaptation of expert seed `[starting question]`, not a reproduction of an expert demonstration or paper.

## Scientific deliverable and hypothesis

The deliverable is a newly fitted, hospital-held-out comparison of clinical-value-only and clinical-value-plus-testing-process mortality models, together with a training-fold-only acuity residualization and falsification analysis. Completion requires the cohort/support audit, fold assignments, fitted models, held-out predictions, uncertainty tables, calibration/decision summaries, process-versus-values contrasts, residualization diagnostics, and an interpretation tied to those files. No fitted result exists yet.

The unresolved clinical question is whether an early ICU risk model that uses laboratory documentation patterns is learning a portable signal of patient state or a site-specific mixture of patient acuity and local workflow. This matters because a score used for escalation, transfer, monitoring intensity, or bed allocation can appear accurate in development hospitals yet become miscalibrated when test ordering, assay interfaces, result latency, or documentation habits differ.

Primary falsifiable hypothesis:

> In adults alive at a six-hour ICU landmark, adding early laboratory process features to the same measured clinical values will increase the development-site-to-held-out-hospital transport loss more than the values-only model. The excess loss will remain directionally present after process features are residualized against measured clinical acuity, but residual process features will be interpreted only as information not explained by measured acuity—not as proof of workflow or a causal effect of testing.

For metric (m), in each outer fold define a transport loss (G_m) as internal-minus-external AUROC (larger is worse transport) and external-minus-internal Brier score (larger is worse transport). The primary contrast is
`Delta_m = G_m(values + process) - G_m(values only)`.
The confirmatory direction is `Delta_AUROC > 0`; Brier and calibration are co-primary clinical interpretations. A predeclared absolute contrast of 0.02 is a practical, not biological, threshold: a 95% interval wholly above zero supports direction; an interval whose lower bound exceeds 0.02 supports a clearly non-trivial transport penalty. Estimates and intervals are reported even when neither condition is met.

This is a prognostic transportability study. It does not test whether ordering a laboratory test causes death, whether a hospital’s workflow is good or bad, or whether a process-dependent score changes care.

## Evidence boundary and substantive advance

The local audit supports feasibility, not the hypothesis: 140,801 qualifying stays across 207 hospitals, 2,339,035 early laboratory rows, and 117,368 stays with at least one qualifying early laboratory row were found in the parent’s full, unsampled audit. The audited names include the proposed channels, with heterogeneous hospital-level coverage. No model performance or clinical effect was estimated.

The imported seed asks whether testing-frequency/missingness models lose performance at another hospital. The parent made that test executable. This child advances it by separating three claims that otherwise collapse into “workflow”:

1. Does process add information conditional on measured values?
2. Does that increment transport less well across hospitals?
3. Is the increment still present after a training-only prediction of process from measured acuity, and does it survive integrity checks?

A remaining process residual is evidence of an unmeasured or documentation-linked predictive component. It cannot identify clinician intent, order failure, staffing, capacity, or patient acuity that was not recorded.

Current public searches remain context rather than validation of this eICU hypothesis: frozen Europe PMC searches are `[source checksum]` and `[source checksum]`. Their excerpts show active work on external calibration, missingness, and workflow-associated fragility, but do not establish this specific eICU estimate. The research-ambition files were inspected within their stated availability limits; the cancer demonstration’s main article and full STAR Methods remain unavailable.

## Population, target, and temporal boundary

Use the read-only source

`[internal dataset path]`

catalog table `patient`, `datasets/eicu/table-ab037c09d7df9a3c.json`. The catalog and header were verified. Join key: `patientunitstayid`; person grouping key: `uniquepid`; hospital key: `hospitalid`.

Include one index ICU stay satisfying:

- numeric `age >= 18`;
- `unitstaytype = 'admit'`;
- `unitvisitnumber = 1`;
- `unitdischargestatus` is `Alive` or `Expired`;
- `unitdischargeoffset >= 360` minutes.

If a `uniquepid` has multiple qualifying rows, retain the row with the smallest non-negative `hospitaladmitoffset), then the smallest `patientunitstayid`. Apply this before any split. The analysis unit is `patientunitstayid`, but no person may cross fitting and validation.

The prediction landmark is ICU-relative minute 360. Eligible clinical observations have offsets in [0, 360]. The primary outcome is `unitdischargestatus = 'Expired'`, representing death before ICU discharge after the landmark. `unitdischargeoffset`, `unitdischargetime24`, `unitdischargelocation`, all hospital-discharge fields, and all APACHE outcome fields are excluded from predictors. This is not admission mortality and excludes people who die or leave before six hours by design.

For descriptive site characterization only, join

`[internal dataset path]`

catalog table `hospital`, `datasets/eicu/table-811df7b2ef435e12.json`, on `hospitalid`; retain `numbedscategory`, `teachingstatus`, and `region`. Hospital ID and descriptors are never model predictors.

## Exact measurements and process construction

All longitudinal joins use `patientunitstayid` and ICU-relative observation fields. Every named source is an ordinary file archive member; no nested archive member is assumed.

Clinical values come from:

- `[internal dataset path]`, table `lab`, `datasets/eicu/table-79bdb33275339b1a.json`. Use `patientunitstayid`, `labresultoffset`, `labresult`, `labname`, `labmeasurenamesystem`, `labmeasurenameinterface`, and `labresultrevisedoffset`.
- `[internal dataset path]`, table `vitalPeriodic`, `datasets/eicu/table-a22c6d6981a32279.json`. Use `patientunitstayid`, `observationoffset`, `temperature`, `sao2`, `heartrate`, `respiration`, and `systemicmean`.
- `[internal dataset path]`, table `vitalAperiodic`, `datasets/eicu/table-72ace5b89971196b.json`. Use `patientunitstayid`, `observationoffset`, and `noninvasivemean`.

The source convention is that these are ICU-relative minutes, that `vitalPeriodic` is a five-minute summary rather than raw waveform data, and that calendar dates and genuine narrative text are not available.

The fixed canonical laboratory panel is: sodium (mmol/L), potassium (mmol/L), chloride (mmol/L), bicarbonate (mmol/L), BUN (mg/dL), creatinine (mg/dL), glucose (mg/dL), Hgb (g/dL), Hct (%), platelets x 1000 (K/mcL), WBC x 1000 (K/mcL), lactate (mmol/L), pH (blank/missing unit), paO2 (mm Hg), and paCO2 (mm Hg). Match `labname` case-insensitively and require the stated `labmeasurenamesystem` (blank/missing for pH). A numeric finite `labresult` is eligible only when `0 <= labresultoffset <= 360` and, if numeric and non-empty, `labresultrevisedoffset <= 360`. If the revision field is empty, use the result offset. The job must emit per-analyte and per-hospital coverage and stop as a prerequisite failure if any required name/unit pair is absent; it must not substitute similarly named tests.

For each of the six vital channels named above and each canonical lab channel, create first, last, mean, minimum, and maximum over [0,360]. Context variables from `patient` are `gender`, `age`, `ethnicity`, `admissionheight`, `admissionweight`, `hospitaladmitsource`, `unitadmitsource`, `unittype`, and `unitstaytype`. Unknown is an explicit categorical level; numeric imputation uses outer-training medians. No outcome-derived values enter construction.

Raw process vector P contains, for each of the 15 canonical analytes: count, any-result indicator, minutes from zero to first result, minutes from last result to 360, and number of distinct result timestamps; plus total eligible lab rows and number of distinct canonical analytes. Process features use no `labid`, interface label, hospital ID, or unselected lab name. They encode recorded testing opportunity, not a confirmed order.

To address acuity versus workflow, construct residual process vector R separately within every outer training fold. Apply fixed transforms (log1p for counts/totals, logistic encoding for binary indicators, and bounded/scaled timing variables), fit a training-only ridge/multitask predictor of each transformed P feature from the complete clinical/context vector V, and retain standardized residuals. The predictor, imputation, scaling, and residual standard deviations are fit on outer-training data only. Apply them unchanged to internal and held-out hospitals. R means “not explained by the measured V under this model”; it is not a workflow label and is not a causal adjustment. Report the training-fold cross-validated residual explained variance and its site distribution.

Do not use `apacheApsVar` (`datasets/eicu/table-67711a86e012835e.json`), `apachePredVar` (`datasets/eicu/table-b1f86cc4a8d9f2a2.json`), or `apachePatientResult` (`datasets/eicu/table-754bebf64d3d9909.json`) in the primary analysis. Their verified schemas have no defensible six-hour observation timestamp and include day-1/summary or outcome fields. In particular, `actualicumortality`, `actualhospitalmortality`, `predictedicumortality`, `diedinhospital`, and discharge fields are not predictors. `note`, `diagnosis`, medication, treatment, and narrative-derived variables are also outside this question.

## Primary estimand and model comparison

Use five repetitions of five-fold whole-hospital cross-validation. Assign eligible hospitals, not stays, to folds with fixed seeds and approximate balance of stays and deaths. Require at least 200 eligible stays and 10 ICU deaths per contributing hospital. If fewer than 20 hospitals qualify, report a prerequisite failure and descriptive estimates only, not a definitive transport conclusion. Within each outer training set, reserve a grouped 10% patient-level validation subset from training hospitals for learned-model stopping only.

For every outer fold, obtain:

- internal validation predictions from the fitted model on the patient-held-out subset of training hospitals; and
- external predictions for all eligible stays in the held-out hospitals.

No external outcome, preprocessing statistic, threshold, or test-hospital process distribution is used for fitting or stopping.

Model family A is the prespecified static L2 logistic baseline. V-only includes context plus the five summaries for the six vital channels and 15 labs. V+P adds the fixed raw process vector. V+R is a secondary acuity-residualized process analysis. Fit one outer-training-only imputer/scaler/one-hot encoder and logistic regression with L2 `C=1`, a deterministic solver, and class-weighted loss disabled unless predeclared by the implementation; use ordinary likelihood with class weighting only as a sensitivity analysis. The primary output is predicted probability.

Model family B is the substantive temporal alternative, not a complexity contest. Represent the same eligible observations in twelve 30-minute bins over [0,360]. For each channel/bin use the mean and final within-bin value time. The values-only sequence is median-filled from outer training and has no masks, counts, or timing. The process sequence adds canonical-lab observed-in-bin masks, within-bin result counts, time since latest qualifying result capped at 360, and the fixed early-window totals. Append context to the final hidden state. Fit a one-layer GRU (hidden width 64, dropout 0.1, Adam 1e-3, batch 256, maximum 30 epochs, patience 5 on the grouped 10% training-hospital validation subset), with five fixed seeds 20260913–20260917. Fit values-only and values+process on identical folds and report the same V+R residual diagnostic where feasible.

The static baseline is necessary because it provides transparent, auditable estimates of the exact transport contrast and shows whether any finding requires temporal capacity. The GRU can reveal ordering, rise/fall trajectories, irregular timing, and interactions lost by first/last/mean/min/max summaries. A GRU improvement alone is not clinically meaningful; it matters only if it changes the process-versus-values transport conclusion. If it fails to converge within the approved budget, preserve the complete logistic result and label the GRU branch computationally deferred; do not change the hypothesis.

## Outcomes, uncertainty, and clinical interpretation

Report pooled out-of-fold and unweighted hospital-level AUROC, AUPRC, Brier score, calibration intercept and slope, fixed-bin calibration curves/ECE, and descriptive decision-curve net benefit at 5%, 10%, and 20% thresholds. Threshold curves are not recommendations because harms, benefits, actions, and resource constraints are unavailable.

Primary inference uses paired hospital bootstrap resampling of complete hospital prediction sets (2,000 replicates), preserving the value/process pairing. Report 95% percentile intervals for `Delta_AUROC`, `Delta_Brier`, calibration differences, and the V+P versus V+R contrasts, alongside per-hospital distributions and the number/size of contributing sites. A hospital with one outcome class contributes to Brier/calibration summaries but not site AUROC; pooled denominators must be explicit.

A supportive result requires process augmentation to add internal information and show a larger external transport loss than V-only, directionally reproducible in logistic and GRU families, with the primary interval above zero and integrity checks passing. If V+R retains a meaningful increment, it supports the narrower claim that measured acuity does not explain all predictive process information. A site-level process association or residual does not identify workflow.

An adverse result is no incremental process information, no excess held-out loss, or equal instability of V-only and V+P. This weakens/falsifies the hypothesis for this eICU snapshot and definition; it does not prove process features are safe or portable elsewhere.

An inconclusive result includes fewer than 20 qualifying hospitals, missing canonical coverage, unstable one-class site metrics, wide intervals spanning zero and 0.02, disagreement between model families, or GRU non-convergence that prevents the planned comparison. Report estimates and the exact failure. Do not select a favorable point estimate.

## Falsification and integrity criteria

1. Permute death labels within hospital using a fixed seed and refit. AUROC should approach 0.5, AUPRC should approach permuted prevalence, and no reproducible process-specific transport contrast should remain. A large signal indicates leakage or split failure.
2. Compare the valid revision-time rule with a deliberately permissive run that ignores `labresultrevisedoffset`. Material change flags delayed-result leakage; the permissive run is not a valid estimate.
3. Permute each patient’s P vector among patients within the same hospital, preserving hospital process distributions but breaking patient-linked process. The process increment should collapse toward V-only. If it does not, inspect hospital leakage, feature coding, and label alignment.
4. Shuffle eligible lab offsets within stay while preserving values and counts for the temporal analysis. Timing-specific effects should attenuate while count effects may remain. Failure to separate these patterns limits the temporal interpretation.
5. Verify no hospital ID, patient/person identifier, discharge field, APACHE outcome, or post-360 row enters features, and that every preprocessing/residualization object is outer-training-only.
6. Report a patient-random split with hospital overlap only as an optimistic descriptive contrast. A process effect seen only with hospital overlap is consistent with site/process dependence; similarity across splits does not prove transportability.
7. Report process-feature hospital intraclass summaries and V-to-P residual explained variance descriptively. High site concentration plus a held-out penalty is workflow-consistent evidence, not proof of staffing, ordering intent, or interface mechanism.

## What remains unavailable

The files record results, not the complete testing process. They cannot distinguish no order, order cancellation, interface loss, delayed result, or deliberate clinical choice; they do not provide staffing, bed capacity, laboratory turnaround, clinician intent, complete pre-ICU history, or an instrument for hospital preference. Removed calendar dates prevent calendar-drift analysis; public note text is not genuine narrative; vitalPeriodic is not raw waveform. ICU discharge mortality is observational and not cause-specific.

Clinical expert adjudication is needed to review analyte harmonization, physiologic plausibility/range exclusions, whether the residualization is clinically interpretable, and whether a proposed risk threshold corresponds to an action. External-system validation and prospective silent deployment are required before claims of clinical deployment, harm, improved decisions, causal testing policy, or quality ranking. An automatic verifier can check the cohort, feature cutoff, split, fitted outputs, metric calculations, bootstrap, and whether conclusions match those outputs. It cannot adjudicate workflow semantics, unmeasured acuity, clinical usefulness, or causation.

## Demonstration dispositions

- Delphi/natural-history demonstration: its inspected article describes a generative transformer trained on UK Biobank trajectories and externally validated in Danish data. Neither that cohort nor the Danish validation data exists in this eICU island. Disposition: do not reproduce; adapt only the general principle that sequence order can carry information, operationalized here by the bounded GRU on eICU measurements. No generative or lifetime-disease claim is made.
- ALADYNOULLI Bayesian demonstration: its inspected article integrates longitudinal EHR, age, and genetics across biobanks. Verified eICU inputs here do not include germline genetics or the multi-disease follow-up required for that analysis. Disposition: do not reproduce; retain only the motivation for an explicit, bounded longitudinal alternative. The GRU is a different EHR-only predictive adaptation, not ALADYNOULLI.
- Oncoformer cancer demonstration: the research-ambition README says the main article and complete STAR Methods remain unavailable; only publisher metadata and supplement are available, and images are not configured. Disposition: do not claim to have read or reproduce the full method; no image or multimodal claim is used. A lab/process-only adaptation would be a different question and is deferred because the present eICU estimand is already specific and testable.

## Expert-seed provenance and dispositions

All ten eICU imported candidates were retrieved and have current Lead assessments; original numbering is an identifier, not a rank. The seed workbook SHA-256 is `[source checksum]`.

- eICU-01, `[prior hypothesis]`, repairable: vasopressor timing/strategy is relevant, but dose semantics and treatment confounding require a distinct observational design. Retain as a future branch; do not merge into this prediction estimand.
- eICU-02, `[prior hypothesis]`, valid and the scientific parent: testing frequency/missingness and hospital-held-out transport are retained and sharpened here.
- eICU-03, `[prior hypothesis]`, repairable: hypotension burden is feasible, but artifact handling, recording density, AKI ascertainment, and urine-output completeness need a separate bounded study.
- eICU-04, `[prior hypothesis]`, repairable: blood gas/FiO2 timing is available in principle, but exposure harmonization and pulmonary-status ascertainment are unresolved; no causal oxygen claim.
- eICU-05, `[prior hypothesis]`, repairable: ventilation and liberation are promising, but mechanics/body-size coverage, extubation semantics, and competing death require a separate audit.
- eICU-06, `[prior hypothesis]`, repairable: discharge timing is observable, but staffing, capacity, destination, and residual confounding are unavailable; retain as an association study only.
- eICU-07, `[prior hypothesis]`, repairable: admission-source comparisons are feasible, but pre-ICU course and transfer selection prevent causal transfer claims.
- eICU-08, `[prior hypothesis]`, repairable: reduced testing/deterioration is closely related, but missingness cannot be equated with de-escalation and discharge/interface/end-of-life explanations need separate rules.
- eICU-09, `[prior hypothesis]`, repairable: insulin, glucose, kidney, and intake/output records support a possible adverse-event study, but administration semantics and nutrition completeness are unresolved.
- eICU-10, `[prior hypothesis]`, repairable: recovery-speed heterogeneity is feasible, but competing outcomes and treatment confounding prevent quality rankings or treatment-effect claims.

These branches are not rejected for being scientifically unimportant; they are deferred because this episode has a more mature, auditable parent and each needs distinct dependency audits. Revisit them only with the stated evidence.

## Alternatives not selected and revisit evidence

- APACHE tables: no six-hour timestamp and leakage-prone summary/outcome fields. Revisit only with a defensible timestamped extraction.
- Process-only prediction: useful descriptive evidence about practice predictiveness, but it cannot answer incremental transport conditional on clinical state. Revisit as a secondary analysis only if it clarifies site concentration.
- Large transformers: no evidence that capacity beyond the bounded GRU is needed. Revisit if residual temporal diagnostics show reproducible clinically meaningful structure unexplained by the static model and the budget is approved.
- Causal testing-policy analysis: revisit only with order/cancellation records, turnaround, staffing/capacity data, or a defensible external design.
- Cross-dataset validation: not available because eICU, MIMIC, UKB, and HCC are separate configured islands without a patient join key.

## Compute, resource, and provenance boundary

The configured `inputs.json` permits 7,200 science seconds, concurrency two, and eight GPU slots; no GPU is mandatory. A sequential one-pass feature extraction from the four primary sources, materialized derived features, deterministic logistic fits, and bounded GRU should be submitted as a resource-managed job with declared source inputs and output checkpoints. Expected use is one CPU and 4–8 GiB RAM for extraction/logistic, with CPU GRU within the 7,200-second budget; GPU is optional and a tradeoff, not evidence of clinical value. Preserve raw audit tables, fold assignments, preprocessing/residualization objects, predictions, bootstrap seeds, and logs. Sources remain read-only and all derived files remain in the workspace.

The study’s computationally checkable claims are the filtering counts, canonical coverage, feature cutoff, split integrity, fitted predictions, metrics, intervals, and falsification outputs. Its clinical claims remain bounded by the unavailable evidence above. Until those outputs exist, this is a proposal, not a completed clinical result.
