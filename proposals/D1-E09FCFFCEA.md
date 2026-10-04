# Renal–nutrition vulnerability during measurable insulin infusion

## Scientific deliverable

The future solver must newly construct a leakage-safe, six-hour person-period cohort from the frozen eICU snapshot and fit/compare two prespecified models of the same prospective question:

1. a hierarchical pooled-logistic baseline with transparent splines and a prespecified renal-change × documented-feed-drop interaction; and
2. a compact temporal GRU that consumes the same information in hourly bins and tests whether nonlinear trajectory/timing information materially changes transportable hypoglycemia risk assessment.

Completion is established by a cohort-flow/data-audit artifact, fitted coefficients and uncertainty for the primary interaction, held-out hospital predictions from both models, calibration/discrimination/alert-burden results, feature-ablation results for renal and nutrition history, and all prespecified falsification analyses. A positive model result is prognostic evidence only; it is not a causal insulin-treatment effect.

## Unresolved question and hypothesis

Insulin-associated hypoglycemia is a consequential, potentially preventable ICU safety event. The unresolved claim is:

> Among adult ICU stays with a directly rate-coded insulin infusion observation and a recent glucose above the hypoglycemia threshold, is a recent measurable deterioration in creatinine combined with a documented loss of enteral formula delivery associated with higher risk of a new glucose <=70 mg/dL in the following six hours, after accounting for current glucose, insulin intensity, recent glucose trajectory and illness severity?

The primary estimand is the adjusted prospective risk difference at six hours between two prespecified covariate profiles: (a) no documented enteral-delivery drop and zero creatinine change, and (b) documented enteral-delivery drop with the observed creatinine change distribution at the same current glucose and insulin-intensity distribution. The model-based risk difference is standardized to the held-out cohort. The main regression estimand is the interaction contrast for creatinine change and documented feed drop, with a 95% hospital-cluster bootstrap interval. This is an association/forecasting estimand, not an intervention effect.

The strongest available evidence supports only that the snapshot contains timestamped insulin infusion records, glucose and creatinine laboratory measurements, and structured intake/output records. Public eICU documentation and the read database paper distinguish continuous infusion records from medication orders, while the medication table is not guaranteed administration. A public search excerpt for an eICU nutrition/glucose curation study also reports substantial hospital variation in nutrition capture. These facts motivate the conservative exposure definitions below; they do not establish the hypothesis. The local paper acquisition for that nutrition curation preprint returned HTTP 403, so its full text was not inspected or cited as if read.

The substantive advance is to test a clinically specific vulnerability state—renal trajectory plus documented loss of enteral delivery at comparable insulin exposure—rather than merely report that insulin, illness severity, or a single low glucose predicts hypoglycemia. If transportable, it could motivate a prospective rule that prompts reassessment of insulin and monitoring when feed delivery is documented to stop in a patient whose renal function is worsening. It would not by itself justify changing insulin doses.

## Population, index, time and outcome

The unit is an ICU stay identified by `patientunitstayid`; `uniquepid` is used to prevent a person appearing in more than one data split. Include adult stays (`patient.age` parsed as >=18), with valid `unitadmitoffset` and `unitdischargeoffset`, `unitdischargeoffset > 0`, and at least one eligible directly rate-coded insulin observation. Use `unitstaytype = admit` as the primary cohort; report a sensitivity analysis including other unit-stay types. The time origin is ICU admission, not hospital admission. Analyze 0 through min(unitdischargeoffset, 72*60) minutes, retaining only intervals with at least six minutes remaining in the follow-up window. Exclude an interval after ICU discharge, and do not use observations whose event timestamp is after the prediction time.

Create non-overlapping six-hour bins aligned to the ICU time origin. For each decision time t at a bin boundary, require:

- an eligible insulin observation in [t-360,t);
- at least one valid glucose measurement in [t-360,t), with the latest prior glucose >70 mg/dL;
- no low glucose in [t-360,t), so the outcome is incident rather than recurrent;
- t+360 <= unitdischargeoffset.

The primary outcome is the first valid glucose measurement <=70 mg/dL in (t,t+360]. A secondary outcome is <=54 mg/dL. Use `labresultoffset` as the clinical observation time, not `labresultrevisedoffset`; deduplicate same-stay, same-time, same-assay revisions by a prespecified earliest-result rule and report the number removed. Restrict the primary glucose outcome to `labname` equal to `glucose` or `bedside glucose` and a laboratory unit explicitly compatible with mg/dL in `labmeasurenamesystem` or `labmeasurenameinterface`; implement and report a frozen unit-normalization table before fitting. Do not silently combine incompatible units.

### Insulin exposure

Use `infusionDrug`, not `medication`, for the primary continuous-infusion exposure. Select case-insensitive `drugname` values containing insulin, with numeric `drugrate` and `infusionoffset` in the ICU window. The primary dose strata are:

- `drugname` containing `units/hr` (including the explicitly named 250-unit formulation), retaining `drugrate` in units/hr;
- `drugname` containing `units/kg/hr`, retaining it as a separate dose-unit stratum and not pretending it is units/hr.

Within each six-hour history, summarize the latest rate, median rate, maximum rate, any rate increase, and time since the last rate observation. Standardize rates within dose-unit stratum using training-set quantiles. Do not convert `ml/hr`, `mg/hr`, blank-unit or unknown-unit insulin to units/hr without a validated concentration. Include those rows only in a binary-any-insulin sensitivity cohort, and report them separately. Because `infusionDrug` has a single event offset and no guaranteed stop time, define exposure from observed rate records and do not claim continuous administration between records. A separate sensitivity analysis carries the last observed rate forward only for a prespecified maximum gap of 60 minutes; this is a modeling assumption, not observed administration.

Do not use `medication` insulin orders as administration. It may be used only in a descriptive audit of order-versus-infusion concordance, using `drugorderoffset`, `drugstartoffset`, `drugstopoffset`, `drugname`, `dosage`, `routeadmin`, `frequency`, `drugordercancelled` and `prn`.

### Renal trajectory

From `lab`, identify creatinine by `labname` and retain only numeric results with compatible creatinine units in the two lab-measure-name/interface fields. At t, require at least two creatinine observations with `labresultoffset < t) and the latest two separated by no more than 48 hours. Define renal change as latest minus preceding creatinine, with elapsed-time slope as a secondary representation. Keep creatinine level, BUN trajectory and time since measurement as separate predictors. This is not a KDIGO AKI adjudication: no baseline creatinine outside the ICU, urine-output criterion, clinician diagnosis, dialysis timing, or reliable pre-ICU renal reserve is guaranteed.

### Documented nutrition state

Use `intakeOutput` as the primary nutrition source. Before outcome labeling, freeze an allowlist of labels whose text explicitly denotes delivered enteral formula/feeding volume, including observed labels such as `Enteral Formula Volume/Bolus Amt (mL)`, `Enteral/Gastric Tube Intake #1` and `Enteral Tube Intake: ...`. Use `cellvaluenumeric`, `intakeoutputoffset`, `cellpath` and `celllabel`; exclude flushes, residual discarded, enteral medications, bodyweight and generic fluids. Do not infer feeding from a missing row.

For each t define W0=[t-360,t) and W-1=[t-720,t-360). A documented enteral-feed drop is present only if W-1 has positive eligible enteral volume, W0 has at least one eligible enteral row, and the sum of eligible W0 volume is zero. If W0 is not observable, label the drop as missing/unknown rather than zero; retain observability indicators and report a complete-observable sensitivity analysis. The primary model therefore tests documented zero delivery, not an unobserved cessation. Secondary analyses separately describe parenteral/dextrose-like labels and must not equate carrier fluid with nutrition or calories.

## Covariates, exclusions and confounding limits

All predictors are computed from timestamps <=t. Include latest glucose and 6/12-hour glucose slope and measurement count; insulin rate summaries; creatinine level/change and BUN; enteral volume and observability; urine-output features only when an explicit numeric urine label can be validated; heart rate, mean arterial pressure and temperature from valid prior vital observations; age, sex, ethnicity, admission weight, unit type, admission source and hospital; and admission severity/diagnosis variables from `apacheApsVar`, `apachePredVar`, `apachePatientResult`, `admissionDx` and `diagnosis`. Keep hospital as a grouping variable, not a treatment instrument.

Flag and report stays with `carePlanEOL` records (`cpleolsaveoffset`, `cpleoldiscussionoffset`) before t. The primary analysis excludes intervals within 12 hours after an end-of-life discussion/save event and intervals within 12 hours of ICU discharge; a sensitivity analysis includes them with an indicator. This addresses care limitation and terminal monitoring changes without claiming the EOL table is complete. Also report intervals around transfer/discharge and hospitals with low insulin or nutrition interface coverage.

The data do not contain reliable bedside confirmation that a dose was administered for subcutaneous orders, a guaranteed infusion start/stop interval, delivered calories, feed interruption reason, dextrose rescue administration, symptoms, or adjudicated AKI. These are essential clinical dependencies for a causal or patient-safety intervention claim. No result may be described as showing that renal decline or feed cessation causes hypoglycemia, that reducing insulin improves outcomes, or that a threshold is a treatment target.

## Baseline model and substantive learned alternative

### Transparent baseline

Fit a pooled logistic discrete-time hazard model with hospital random intercept (or hospital fixed effects if convergence permits), patient/stay-clustered robust uncertainty, restricted cubic splines for current glucose, insulin rate, creatinine level/change and time since ICU admission, and prespecified main effects for all covariates above. Include one prespecified renal-change × documented-feed-drop interaction. Fit preprocessing, unit mappings, spline knots, imputation rules and any class weights on training hospitals only.

The baseline is scientifically adequate because it directly estimates the proposed interaction and its standardized six-hour risk contrast, is auditable, and provides a clinically recognizable comparator. It loses information about irregular event order, nonlinear lagged combinations and evolving missingness patterns.

### Learned alternative

Fit a compact GRU sequence model to the same question. For each decision time, input the preceding 12 one-hour bins, with the same clinical variables, last-value/carry-forward values only within a prespecified 6-hour maximum gap, time-since-measurement features, insulin dose-unit indicators, enteral-delivery/observability features, and explicit missingness indicators. Predict the next six-hour incident hypoglycemia outcome. Use a one-layer GRU (hidden size selected from a small prespecified grid such as 32/64 on the training set), dropout, weighted binary cross-entropy, early stopping on validation Brier score, and a fixed random seed set. No future values, post-outcome rescue treatment, or revised laboratory result can enter an input.

The GRU is not justified merely by a possible AUROC increase. Its substantive role is to test whether the clinically meaningful renal/nutrition relationship is a trajectory phenomenon: abrupt feed loss after sustained delivery, renal change timing relative to insulin-rate changes, and irregular measurement patterns may be represented more faithfully than a hand-selected summary. Evaluate this directly by removing renal-history features, removing nutrition/observability features, and time-shuffling those histories within hospital. Compare the full model with an otherwise identical model that omits those feature blocks. A performance difference without a stable, calibrated renal/nutrition ablation pattern is not evidence for the proposed clinical mechanism.

A mechanistic glucose–insulin state-space model was considered but deferred. It could expose latent insulin sensitivity, renal clearance and carbohydrate balance, which the regression and GRU cannot identify directly. It would require reliable administered insulin, infusion concentrations and stop times, carbohydrate/calorie delivery, dextrose exposure and a validated glucose mass-balance model; these dependencies are absent or heterogeneous here. It is scientifically useful for a future prospective or richer retrospective study, but inventing latent physiology from these fields would reduce validity.

## Splits, analysis and uncertainty

The primary split is by hospital: approximately 60% of hospitals for fitting, 20% for validation/model selection, and 20% held out once for transport evaluation. Assign all stays from the same `uniquepid` to one partition; stratify hospital assignment using only eligible insulin-stay counts, without using outcomes. If a hospital has too few eligible stays for stable validation, retain it in descriptive coverage tables and predeclare the minimum count for inferential hospital estimates rather than silently pooling it into another hospital. A secondary patient-level split within training hospitals estimates internal performance but cannot replace the hospital holdout.

Report baseline incidence, cohort flow, event counts, missingness and coverage by hospital before modeling. The primary metrics are held-out Brier score, calibration intercept/slope and calibration plots, AUROC and area under the precision-recall curve, plus sensitivity, positive predictive value and alerts per 100 insulin-exposed decision times at a threshold selected on validation hospitals. Report standardized six-hour risk differences and the baseline interaction contrast with 95% confidence intervals. Use 1,000 resamples of hospitals for transport intervals (or all feasible resamples if fewer hospitals), and patient/stay-clustered bootstrap within training data for fitted coefficients. Do not report a p-value as the sole evidence.

Sensitivity analyses are: severe <=54 mg/dL; 24-hour recurrent low-glucose burden; direct units/hr only versus direct units/hr plus units/kg/hr; no carry-forward versus 60-minute carry-forward; complete-observable nutrition only; high nutrition-interface hospitals; inclusion of EOL-adjacent intervals; and omission of any covariate block that may be downstream of t. Missingness is analyzed as data quality/process information, not silently imputed as clinical absence.

## Falsification and interpretation

Prespecified falsification checks include:

- a timestamp audit demonstrating that every feature used for t is <=t and that future-only “lead” features are absent from the submitted design matrix;
- within-hospital permutation of renal/nutrition histories across decision times, which should remove the proposed interaction and its ablation signal while preserving broad event prevalence;
- a negative temporal control using the preceding six-hour low-glucose outcome after excluding intervals with a prior low glucose, where a strong new prospective-only effect should not be reproduced merely by timestamp or patient selection artifacts;
- a documentation-density analysis using counts and gaps of lab/intake rows; an association explained entirely by measurement density or hospital interface membership is adverse evidence for a clinical interpretation;
- leave-one-hospital-out estimates and comparison of hospitals with versus without adequate paired nutrition observations; and
- a model-leakage control that intentionally exposes future values only in a diagnostic run, which must show that any performance gain from such values is not present in the submitted models.

Supportive results require a positive, reasonably monotone renal-change/feed-drop risk contrast, a prespecified interaction consistent in the hospital holdout, improved calibration or transport performance when the feature blocks are retained, and survival of the observable-data and unit-definition sensitivities. This would support a risk-stratification hypothesis and justify prospective chart-reviewed evaluation of a feed-loss/insulin monitoring alert.

Adverse results include a null or reversed interaction, no held-out transport, instability across insulin unit definitions, or an effect explained by missingness/interface density. That would refute the proposed measurable risk marker in this dataset or show that the available fields cannot support it. It should not be converted into evidence that insulin is safe or that nutrition is irrelevant.

Inconclusive results include too few decision times with paired creatinine and observable nutrition, excessive hospital exclusion, major discordance between direct rate units and all-insulin sensitivity analyses, or unresolvable glucose-unit/revision ambiguity. The correct conclusion is that eICU cannot resolve the question. Stronger clinical conclusions require adjudicated retrospective chart review or a prospective multi-ICU study linking administered insulin, actual feed interruptions, calories/dextrose rescue, symptoms, KDIGO AKI and patient outcomes.

## Exact data bindings and provenance

Dataset: eICU snapshot `[source checksum]`, source catalog [source checksum]. Offsets are minutes relative to ICU admission; `patientunitstayid` is the join key for all clinical tables. Every listed archive member is an ordinary file in its source `.csv.gz`; no hidden archive member is assumed.

Primary source bindings:

- `patient`, table JSON `datasets/eicu/table-ab037c09d7df9a3c.json`, source `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/patient.csv.gz`; keys `patientunitstayid`, `uniquepid`; fields `age`, `hospitalid`, `unitadmitoffset`, `unitdischargeoffset`, `unitstaytype`, `unittype`, `unitvisitnumber`, `admissionweight`, `hospitaladmitsource`, `unitadmitsource`.
- `hospital`, table JSON `datasets/eicu/table-811df7b2ef435e12.json`, source `.../hospital.csv.gz`; join `hospitalid`; fields `numbedscategory`, `teachingstatus`, `region`.
- `infusionDrug`, table JSON `datasets/eicu/table-18e1a8caaa91eb44.json`, source `.../infusionDrug.csv.gz`; fields `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, `patientweight`.
- `medication`, table JSON `datasets/eicu/table-d31d6bb023397bc2.json`, source `.../medication.csv.gz`; fields `patientunitstayid`, `drugorderoffset`, `drugstartoffset`, `drugstopoffset`, `drugname`, `dosage`, `routeadmin`, `frequency`, `drugordercancelled`, `prn`.
- `lab`, table JSON `datasets/eicu/table-79bdb33275339b1a.json`, source `.../lab.csv.gz`; fields `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `intakeOutput`, table JSON `datasets/eicu/table-ebba5dc91b1d37e7.json`, source `.../intakeOutput.csv.gz`; fields `patientunitstayid`, `intakeoutputoffset`, `intakeoutputentryoffset`, `cellpath`, `celllabel`, `cellvaluenumeric`, `cellvaluetext`, `intaketotal`, `outputtotal`, `nettotal`.
- `vitalPeriodic`, table JSON `datasets/eicu/table-a22c6d6981a32279.json`, source `.../vitalPeriodic.csv.gz`; time `observationoffset`; fields `temperature`, `heartrate`, `systemicmean`, `systemicsystolic`, `systemicdiastolic`, `sao2`.
- `vitalAperiodic`, table JSON `datasets/eicu/table-72ace5b89971196b.json`, source `.../vitalAperiodic.csv.gz`; time `observationoffset`; fields `noninvasivemean`, `noninvasivesystolic`, `noninvasivediastolic`.
- `apacheApsVar`, table JSON `datasets/eicu/table-67711a86e012835e.json`, source `.../apacheApsVar.csv.gz`; fields `creatinine`, `glucose`, `meanbp`, `dialysis`, `vent`, `intubated`, `urine`, `fio2`, `pao2`.
- `apachePredVar`, table JSON `datasets/eicu/table-b1f86cc4a8d9f2a2.json`, source `.../apachePredVar.csv.gz`; fields `diabetes`, `creatinine`, `admitdiagnosis`, `ventday1`, `diedinhospital`, `sicuday`.
- `apachePatientResult`, table JSON `datasets/eicu/table-754bebf64d3d9909.json`, source `.../apachePatientResult.csv.gz`; fields `acutephysiologyscore`, `apachescore`, `predictedicumortality`, `actualicumortality`, `actualventdays`, `unabridgedunitlos`.
- `admissionDx`, table JSON `datasets/eicu/table-2e48e1043e7eaa89.json`, source `.../admissionDx.csv.gz`; fields `admitdxenteredoffset`, `admitdxpath`, `admitdxname`, `admitdxtext`.
- `diagnosis`, table JSON `datasets/eicu/table-5d5ab99e8c359037.json`, source `.../diagnosis.csv.gz`; fields `diagnosisoffset`, `diagnosisstring`, `icd9code`, `diagnosispriority`.
- `carePlanEOL`, table JSON `datasets/eicu/table-4a60395475cf75e7.json`, source `.../carePlanEOL.csv.gz`; fields `cpleolsaveoffset`, `cpleoldiscussionoffset`, `activeupondischarge`.

Availability audit performed on the read-only raw sources found 200,859 patient rows, 410,760 insulin-named `infusionDrug` rows, 4,495,331 glucose-named `lab` rows and 1,277,760 creatinine-named `lab` rows by streaming/counting records. These are raw row counts, not the eligible cohort and may include revisions/duplicates. Insulin names included approximately 252,838 `units/hr`, 817 `units/kg/hr`, 128,016 `ml/hr` and 14,139 blank-unit records; feeding labels included 79,227 `Enteral Formula Volume/Bolus Amt (mL)` and 63,979 `Enteral/Gastric Tube Intake #1` rows. The full catalog and `datasets/eicu/metadata.json` were inspected; the catalog relationship for every clinical table is a `patientunitstayid` join to `patient`, and the metadata records that narrative text and raw waveforms are unavailable.

References used are the local `references/research-ambition/README.md` and `methods-and-compute.md`, the read local eICU database paper acquired as source `[source checksum]`, and the model-mediated public search evidence recorded by the research tools. The three demonstration papers were treated as ambition examples, not as required topics or reproduced methods. No unavailable supplementary or main-paper text is claimed as inspected.
