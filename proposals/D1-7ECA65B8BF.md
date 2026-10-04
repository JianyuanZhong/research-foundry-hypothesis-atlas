# Early hypotension burden beyond minimum MAP for subsequent creatinine-defined kidney injury

## Parentage and substantive change

This is a substantive child of the assessed eICU parents `[prior hypothesis]` (duration of hypotension), `[prior hypothesis]` (testing-practice dependence), `[prior hypothesis]` (residual instability and competing discharge), and `[prior hypothesis]` (arrival selection and unavailable pre-ICU history).

The principal change is to convert the seed's broad question into a landmark, time-ordered, computable estimand. It defines the exposure in the first 6 ICU hours, separates minimum MAP from duration/depth burden, starts outcome follow-up only after hour 6, makes creatinine observation explicit, and treats death/discharge and incomplete laboratory ascertainment as limitations rather than negative outcomes. The testing-practice seed becomes a prespecified transportability and measurement-density stress test. The transfer and nighttime-discharge ideas are not added as co-primary questions: they motivate selection and competing-event diagnostics, but their causal mechanisms are not identifiable here.

## Clinical question and hypothesis

The decision question is whether an early bedside summary of hypotension should contain time-under-threshold/depth information in addition to the lowest recorded blood pressure when clinicians decide how intensively to monitor for kidney injury. The result would not define a vasopressor target.

Strongest evidence-supported claim: the configured eICU snapshot contains ICU-relative, patient-stay-linked blood-pressure observations, creatinine-labeled laboratory observations, discharge/death offsets, hospital identifiers, and infusion records. These fields permit a reproducible observational comparison of minimum MAP with early burden and a later creatinine trajectory. The seed and public literature establish this as clinically plausible, but do not establish this eICU association or a treatment effect.

Untested claim: among adult ICU stays that remain in the ICU at a 6-hour landmark, and conditional on the minimum MAP during hours 0–6, greater time-weighted hypotension burden during hours 0–6 is associated with a higher risk of subsequently observed creatinine-defined kidney injury during hours 6–48, and improves transportable risk prediction beyond minimum MAP alone.

Falsifiable null: after the prespecified covariates and hospital effects, duration/burden has no residual association with the later creatinine outcome and does not improve held-out calibration or discrimination beyond the minimum-MAP model. A positive association is not evidence that hypotension caused AKI or that raising MAP would prevent it.

## Population, temporal boundaries, and estimands

Use the eICU snapshot `[source checksum]`, with all calendar dates removed and offsets in minutes from ICU admission.

Index unit is one `patientunitstayid`. Include adults with numeric `patient.age >= 18`; retain eICU's `> 89` as age 90 for this eligibility rule, and report missing-age exclusion. Do not collapse repeated ICU stays by `uniquepid`; the primary analysis is a stay-level question. A secondary cluster-robust analysis uses `uniquepid` to acknowledge recurrent stays.

Exposure window: `0 <= observationoffset <= 360` minutes after ICU admission. Require at least three valid MAP observations and at least 60 minutes of covered exposure time under the gap rule below. This is an observability criterion, not evidence that other patients had normal blood pressure. Exclude implausible MAP values outside 20–200 mmHg and missing values. Use noninvasive MAP as the primary harmonized signal.

Landmark: retain stays with `unitdischargeoffset >= 360` minutes and no ICU discharge/death before the landmark. This makes exposure fully observed before follow-up and prevents immortal-time attribution of an outcome that occurs before exposure completion. Report the number and characteristics of stays discharged/dead before 6 hours rather than silently treating them as controls.

Follow-up: from minute 360 through minute 2,880 (48 hours after ICU admission), ending at the earliest of ICU discharge, ICU death, 2,880 minutes, or last usable creatinine observation. The main kidney estimand is the cause-specific risk of a first observed creatinine-defined AKI event, with discharge/death before that event recorded as a competing event. A parallel three-state report is required: observed AKI, death/discharge before observed AKI, and no observed AKI/unknown ascertainment. Patients with no post-landmark creatinine must not be labeled as no AKI.

## Exact source bindings

All listed sources are read-only. Each is an ordinary file in the archive, not a nested archive member.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/patient.csv.gz`, table `patient`, archive member `ordinary file`. Join key `patientunitstayid`; use `age`, `hospitalid`, `gender`, `ethnicity`, `hospitaladmitsource`, `unittype`, `unitstaytype`, `unitadmit.../unitadmittime24` only for indexing, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`, and `uniquepid`. The exact catalog columns are `patientunitstayid`, `patienthealthsystemstayid`, `gender`, `age`, `ethnicity`, `hospitalid`, `wardid`, `apacheadmissiondx`, `admissionheight`, `hospitaladmittime24`, `hospitaladmitoffset`, `hospitaladmitsource`, `hospitaldischargeyear`, `hospitaldischargetime24`, `hospitaldischargeoffset`, `hospitaldischargelocation`, `hospitaldischargestatus`, `unittype`, `unitadmittime24`, `unitadmitsource`, `unitvisitnumber`, `unitstaytype`, `admissionweight`, `dischargeweight`, `unitdischargetime24`, `unitdischargeoffset`, `unitdischargelocation`, `unitdischargestatus`, and `uniquepid`.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/vitalAperiodic.csv.gz`, table `vitalAperiodic`, archive member `ordinary file`. Join by `patientunitstayid); time `observationoffset`; exposure value `noninvasivemean`. Preserve `vitalaperiodicid` for audit. Primary MAP is not a waveform: the dataset guide describes these as structured observations, so do not call them continuous or raw monitor data.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/vitalPeriodic.csv.gz`, table `vitalPeriodic`, archive member `ordinary file`. Join by `patientunitstayid); time `observationoffset`; sensitivity values `systemicmean`, `systemicsystolic`, `systemicdiastolic`, `heartrate`, `temperature`, `sao2`, and `respiration`. The catalog confirms that this is a five-minute summary table, not raw waveform data. Do not pool its `systemicmean` with noninvasive MAP in the primary exposure.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/lab.csv.gz`, table `lab`, archive member `ordinary file`. Join by `patientunitstayid); time `labresultoffset`; identify serum creatinine only with a prespecified normalized `labname` rule (initially `lower(trim(labname)) = 'creatinine'`; audit and list any additional exact creatinine labels before analysis). Use numeric `labresult`, `labresulttext` only for audit, and retain `labmeasurenamesystem` and `labmeasurenameinterface` to verify that the included values share units. Exclude nonnumeric values and implausible values outside 0.1–30 mg/dL after unit verification. `labresultrevisedoffset` is not the specimen time and must not replace `labresultoffset`.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/infusionDrug.csv.gz`, table `infusionDrug`, archive member `ordinary file`. Join by `patientunitstayid`; time `infusionoffset`; audit `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, and `patientweight`. A prespecified, reported name dictionary may identify norepinephrine, epinephrine, vasopressin, phenylephrine, dopamine, and milrinone. These records are treatment-context descriptors only; rates and order completeness are not assumed. Do not adjust the primary model for a vasopressor measured after a low-MAP observation.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/diagnosis.csv.gz`, table `diagnosis`, archive member `ordinary file`. Join by `patientunitstayid`; use `diagnosisoffset`, `diagnosisstring`, `icd9code`, `diagnosispriority`, and `activeupondischarge` only in a sensitivity adjustment for recorded baseline renal/cardiovascular/critical illness diagnoses. These are coded clinical records, not adjudicated comorbidity histories.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/admissionDx.csv.gz`, table `admissionDx`, archive member `ordinary file`. Join by `patientunitstayid`; use `admitdxenteredoffset`, `admitdxpath`, `admitdxname`, and `admitdxtext` to describe admission diagnosis and conduct a sensitivity adjustment. The structured note fields are not assumed to be complete or independently adjudicated.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/hospital.csv.gz`, table `hospital`, archive member `ordinary file`. Join `hospital.hospitalid = patient.hospitalid`; use `numbedscategory`, `teachingstatus`, and `region` for descriptive transport strata, not as an instrumental variable.

- `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/carePlanEOL.csv.gz`, table `carePlanEOL`, archive member `ordinary file`. Join by `patientunitstayid`; use `cpleolsaveoffset`, `cpleoldiscussionoffset`, and `activeupondischarge` in a sensitivity exclusion/stratification for documented end-of-life planning. Absence of a row is not proof that treatment limitations were absent.

The catalog also contains `apacheApsVar` and `apachePatientResult`, but their fields aggregate acute physiology over a period that can overlap the exposure and outcome. They are therefore excluded from the primary covariate set. A clearly labeled leakage-sensitive secondary analysis may use `apacheApsVar.meanbp`, `creatinine`, `urine`, `dialysis`, `heartrate`, `temperature`, `wbc`, `bun`, and `apachePatientResult.apachescore` only to quantify how much conclusions depend on first-24-hour summaries; these fields cannot support a clean 0–6-hour causal interpretation.

## Exposure construction

For each stay, sort valid `vitalAperiodic` observations in the first 360 minutes.

1. Minimum MAP is the minimum valid `noninvasivemean`.
2. For each observation at time (t_i), carry that value to the next observation only when the gap is no more than 30 minutes. Do not bridge longer gaps. Let covered minutes be the sum of these accepted intervals within 0–360.
3. Primary duration is the total accepted minutes for which carried-forward MAP is below 65 mmHg.
4. Secondary depth burden is area below 65: \\(\sum_i max(0,65-MAP_i)\times\Delta t_i\\), in mmHg-minutes.
5. Also retain fraction of covered time below 65, number of valid MAP observations, covered minutes, median inter-observation gap, and maximum gap. These are measurement-process variables and must be reported.
6. The primary model enters minimum MAP and duration as prespecified continuous variables using restricted cubic splines with knots fixed before seeing outcomes. A simple linear-logistic model with minimum MAP and duration in clinically interpretable units is the required baseline. AUC is a separate secondary exposure, not a post-hoc replacement selected because it fits better.

Sensitivity analyses repeat the construction with thresholds 60 and 70 mmHg, a maximum accepted gap of 15 and 60 minutes, at least six MAP observations, and the `vitalPeriodic.systemicmean` signal alone where available. If the added burden signal is only present under sparse or long-gap carry-forward, that is evidence of measurement dependence rather than robust clinical information.

## Outcome construction and observability

Define baseline creatinine as the earliest valid creatinine at `0 <= labresultoffset <= 360` minutes, with a deterministic tie-break by `labid`. Define an observed AKI event as the first later creatinine at `360 < labresultoffset <= 2880` with value at least 0.3 mg/dL above that baseline. This is a computable creatinine-rise phenotype, not a complete KDIGO adjudication: baseline kidney function before ICU admission, urine output, dialysis indication, and clinician adjudication are incomplete or unavailable for this question.

For every eligible stay report: baseline creatinine availability; any follow-up creatinine; number and timing of follow-up creatinine tests; maximum rise; observed AKI; discharge alive before a qualifying test; death before a qualifying test; and no follow-up/unknown. Never impute an absent post-landmark creatinine as no AKI in the primary report.

The primary association analysis is a cause-specific discrete-time hazard or pooled-logistic model for the first observed AKI event over 6–48 hours, with death and ICU discharge as competing absorbing events and with laboratory-observation censoring explicitly reported. The complete-case observed-AKI analysis is a secondary, transparent estimate among stays with at least one follow-up creatinine. A sensitivity analysis uses inverse-probability-of-observation weights based only on pre-landmark variables: baseline creatinine, early MAP minimum/burden/density, demographics, admission source, unit type, hospital, and counts of early laboratory observations. Weight diagnostics and positivity must be reported; weighting does not repair unmeasured clinical indication for testing.

## Covariates and confounding

The clinical baseline model includes baseline creatinine; minimum MAP; age, gender, ethnicity, admission source, unit type, hospital fixed effect or hospital-stratified intercept; early heart rate/temperature/respiratory rate summaries from `vitalPeriodic` when recorded; and admission diagnosis categories derived from the exact `admissionDx` fields. A second adjustment set adds diagnosis/past-history indicators only when their timestamps precede the landmark. Do not use future creatinine, future labs, discharge fields, APACHE first-24-hour summaries, or post-exposure vasopressor rate as baseline confounders.

Treatment feedback is unavoidable: low MAP may trigger a vasopressor, and treatment may change later MAP and kidney risk. Use `infusionDrug` to report and stratify by any identifiable vasoactive infusion beginning in 0–6 hours, and test an exposure-by-infusion interaction descriptively. Do not interpret that interaction as effect modification of a treatment intervention, and do not claim an adjusted vasopressor effect.

## Statistical comparison and uncertainty

The required nested models are:

- M0: baseline clinical covariates and hospital effect, without blood-pressure summaries.
- M1: M0 plus minimum MAP.
- M2: M1 plus early hypotension duration.
- M3: M1 plus depth AUC, as a distinct secondary model.

The seed question is tested by M2 versus M1. Report the adjusted duration association with 95% confidence interval, likelihood-ratio test, calibration intercept/slope, Brier score, AUROC and area under the precision-recall curve. Use hospital-clustered bootstrap confidence intervals or cluster-robust standard errors. Pre-specify a grouped hospital split: five folds, with all stays from a hospital in one fold; do not let repeated stays cross folds. The final reported incremental performance is the distribution of M2 minus M1 on held-out hospitals, not resubstitution performance.

A useful prognostic signal must be consistent in direction across most held-out folds, retain calibration, and not be explained by BP observation density. For a transparent computational threshold, call the incremental prediction result weak if the held-out AUROC change is below 0.01 and the Brier improvement is below 0.005 with confidence intervals spanning zero; these are reporting gates, not clinical utility claims. A clinically meaningful monitoring policy still requires an external decision threshold, cost/benefit analysis, and clinician review, none of which eICU alone supplies.

## Falsification and adverse-result criteria

The hypothesis is computationally falsified for this eICU estimand if, after the prespecified analysis:

- the duration coefficient is null or reverses across density-adjusted specifications and the 95% interval excludes the prespecified clinically relevant direction;
- M2 does not improve held-out calibration/discrimination over M1, or any apparent improvement disappears in hospital-held-out validation;
- the association is present only when long gaps are bridged, only in one hospital, or only when APACHE first-24-hour variables leak into the model;
- a negative-control analysis using a pre-landmark creatinine change (when two baseline-window creatinines exist) shows a comparable association, suggesting selection or confounding rather than future prediction;
- permutation of the exposure within hospital and baseline-MAP strata leaves the apparent signal intact, indicating coding or leakage error;
- the duration signal is materially attenuated after including MAP count, covered minutes, gap summaries, and early laboratory-testing intensity, indicating measurement density rather than physiology.

Supportive results are a reproducible positive duration/AUC association conditional on minimum MAP, stable across gap/threshold definitions, with better held-out calibration and a small but nonzero incremental performance in multiple hospitals. This supports added prognostic information about an observed creatinine-rise phenotype. It does not support a MAP treatment target, a vasopressor strategy, or a causal kidney-injury mechanism.

Adverse results include no incremental value, a density-dependent result, a hospital-specific result, or a result dominated by discharge/death. These would favor minimum MAP alone for this dataset or show that the added measure is not transportable; they remain scientifically informative. Inconclusive results include too few observed follow-up creatinines, poor overlap of duration at a given minimum MAP, unstable observation weights, or wide hospital-fold intervals. In that case the correct conclusion is inadequate evidence, not support for the null.

## Missing evidence and required follow-up

The snapshot cannot adjudicate pre-ICU creatinine baseline, urine-output AKI criteria, dialysis indications/timing, clinician-confirmed AKI, invasive-versus-noninvasive measurement equivalence, waveform artifact, vasopressor dose completeness, fluid balance intent, shock etiology, or the clinical reason for ordering follow-up creatinine. Narrative notes are not a substitute: the catalog says public eICU narrative note sections were removed and retained note fields are not assumed to be genuine narrative. The absence of bed-capacity/staffing data also prevents mechanism claims about discharge or monitoring practice.

A stronger clinical conclusion would require expert review of creatinine/urine/dialysis records and blood-pressure artifacts, an external ICU cohort with adjudicated AKI and richer treatment timing, and preferably a prospective monitoring or intervention study. This candidate therefore claims only evidence-bounded observational prognosis and transportability.

## Research-ambition demonstrations

The three demonstrations were inspected but are not treated as evidence for this hypothesis. The natural-history transformer paper was used only as a reminder to respect temporal prediction, calibration, and competing events; its UK Biobank/Danish lifetime disease setting and generative model are not reproduced because eICU has short ICU-relative follow-up and lacks those modalities. The cancer demonstration's main article remains unavailable, as stated in its README; only its supplement was inspected. Its multimodal imaging/longitudinal routine-data setting is not available here, so no main-paper or STAR-Methods claim is made. The Bayesian EHR/genetic paper was inspected, but its genetic longitudinal biobank inputs and latent disease-signature objective are absent from eICU; its explicit time-varying likelihood lesson does not justify importing the model. These are design-context dispositions, not citations establishing the present hypothesis.

## Harbor deliverable

The compiler should implement one reproducible CPU analysis with source files read-only and derived tables in the workspace. It must first emit an audit table with row counts, unique stays, exact creatinine labels/units, MAP density, follow-up ascertainment, competing-event counts, and vasoactive drug-name coverage. It must then emit a stay-level exposure/outcome table, model specifications and coefficients, held-out hospital metrics, density/threshold/gap sensitivity results, negative-control/permutation checks, and a conclusion table mapping each claim to its computed output and uncertainty. No result may be reported from an uncomputed envelope, and no causal or clinically adjudicated claim may be generated automatically.
