# Does a physiology-only six-hour risk summary transport better than one that learns laboratory practice?

## Decision question and falsifiable hypothesis

At the six-hour ICU landmark, clinicians may want a risk summary to decide who needs intensified kidney surveillance. The unresolved question is whether a summary built from early recorded physiology transports across hospitals better than an otherwise matched summary augmented with early laboratory values and the local laboratory-testing process.

The primary hypothesis is:

> Among adult eICU unit stays that remain in the ICU at minute 360 and have an ascertainable baseline creatinine, a physiology-only model trained in other hospitals will have better out-of-hospital transport performance for a later observed creatinine-rise phenotype than a matched model that additionally uses laboratory values, laboratory availability/missingness, and testing intensity.

“Better transport performance” is prespecified as lower hospital-held-out 48-hour Brier score and better calibration (smaller absolute calibration intercept error and calibration slope closer to 1), averaged over held-out hospital folds. Discrimination (AUROC and area under the precision-recall curve) is secondary. The null is no reproducible difference, or an advantage for the augmented model, after the observation and leakage checks below.

This is a noncausal, conditional prognostic comparison. It does not test whether physiology causes kidney injury, whether ordering more tests changes outcome, whether a hospital provides better care, or whether either score has clinical utility.

## What is supported and what remains unknown

The strongest evidence available before execution is structural: the frozen eICU snapshot and catalog contain repeated ICU-relative vital observations, timestamped laboratory results with name and measurement-system/interface fields, patient-stay and hospital identifiers, and discharge status. The imported eICU-02 seed makes the related transportability concern explicit, while the prior eICU candidates establish a feasible six-hour landmark and an observed-creatinine ascertainment framework. Those materials do not establish that physiology is more portable, that testing-process features are harmful, or that the endpoint is adjudicated AKI.

The experiment tests the unresolved transport claim directly by fitting both model classes on the same training hospitals, with the same outcome, preprocessing discipline, model family, tuning budget, and held-out hospitals. A supportive result would show a transport difference attributable to the added lab/testing-process block, not merely a difference in model complexity.

## Population, landmark, and outcome

Use one ICU unit stay per patientunitstayid; do not collapse repeated stays by uniquepid in the primary analysis. Include:

- age at least 18 from patient.age (eICU values coded > 89 are reported as 90); missing age is an explicit exclusion/flow state;
- patient.unitdischargeoffset >= 360, so the exposure is complete through minute 360;
- at least three valid primary MAP observations in minutes 0–360 and at least 60 minutes of covered physiology under the gap rule;
- a valid numeric baseline creatinine in minutes 0–360 for the primary ascertainable-outcome cohort.

The full physiology-eligible flow must also retain stays without a baseline creatinine. They are not silently dropped as normal: report them as baseline-unknown and describe their hospital distribution and early observation features. If too few stays have an ascertainable baseline or too few hospitals contribute outcome events, the comparison is infeasible/inconclusive rather than rescued by changing the endpoint.

The landmark is minute 360 after ICU admission. All predictors must be computed only from observations whose clinical/result timestamp is in [0, 360]. Follow-up begins strictly after minute 360 and ends at the earliest of ICU discharge, ICU death, minute 2,880 (48 hours), or the last usable creatinine observation before censoring.

Define baseline creatinine as the earliest valid numeric lab.labresult with normalized labname='creatinine' in [0,360], tie-broken by labid. Accept only values in a prespecified plausibility range of 0.1–30 mg/dL after a unit audit using labmeasurenamesystem and labmeasurenameinterface. Use labresultoffset as result timing, never labresultrevisedoffset. If labels or units are ambiguous, do not silently convert them; classify the affected endpoint as infeasible/inconclusive.

The primary outcome is the first later numeric creatinine at 360 < labresultoffset <= 2880 that is at least 0.3 mg/dL above the baseline. Also report the maximum rise and timing of the first qualifying value. This is explicitly a later observed creatinine-rise phenotype, not adjudicated KDIGO AKI.

Every eligible stay receives an ascertainment state:

1. observed creatinine rise;
2. post-landmark creatinine observed without the rise;
3. ICU death or discharge before a qualifying follow-up test;
4. no post-landmark creatinine before the horizon or censoring, so ascertainment is unknown.

A follow-up value below the event threshold does not guarantee later absence of a rise. No-test stays are never coded as non-events in the primary analysis. Death and discharge are competing events when they occur before a qualifying follow-up test; their counts, timing, discharge status, and hospital distribution are reported separately.

## Exact source bindings and joins

Snapshot: [source checksum].

The catalog is [internal dataset path] (catalog [source checksum]). The eICU guide is datasets/eicu/README.md; all listed members are ordinary files inside the cataloged .csv.gz files, not nested archives. Relevant schema JSONs were inspected locally.

All longitudinal tables join to patient by patientunitstayid. The only hospital join is hospital.hospitalid = patient.hospitalid. No cross-dataset join is used.

- Patient/stay source: [internal dataset path] 2.0数据/patient.csv.gz, table patient, catalog schema datasets/eicu/table-ab037c09d7df9a3c.json. Required columns are patientunitstayid, uniquepid, age, gender, ethnicity, hospitalid, hospitaladmitsource, unittype, unitstaytype, unitdischargeoffset, unitdischargestatus, and unitdischargelocation. ICU-relative admission is represented by offsets; calendar/time-of-day fields are not exposures.

- Hospital source: [internal dataset path] 2.0数据/hospital.csv.gz, table hospital, schema datasets/eicu/table-811df7b2ef435e12.json. Required columns are hospitalid, numbedscategory, teachingstatus, and region. Hospital is a grouping/transport stratum, not a treatment instrument or quality ranking variable.

- Primary physiology source: [internal dataset path] 2.0数据/vitalAperiodic.csv.gz, table vitalAperiodic, schema datasets/eicu/table-72ace5b89971196b.json. Required columns are vitalaperiodicid, patientunitstayid, observationoffset, and noninvasivemean.

- Additional structured physiology source: [internal dataset path] 2.0数据/vitalPeriodic.csv.gz, table vitalPeriodic, schema datasets/eicu/table-a22c6d6981a32279.json. Required columns are vitalperiodicid, patientunitstayid, observationoffset, temperature, sao2, heartrate, respiration, systemicmean, and pamean. The catalog metadata identifies this as five-minute summary observations, not raw waveforms.

- Laboratory source: [internal dataset path] 2.0数据/lab.csv.gz, table lab, schema datasets/eicu/table-79bdb33275339b1a.json. Required columns are labid, patientunitstayid, labresultoffset, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface, and labresultrevisedoffset. The raw header and sample rows were inspected. labresultoffset, not the revised offset, defines availability for the six-hour predictors and outcome.

- End-of-life sensitivity source: [internal dataset path] 2.0数据/carePlanEOL.csv.gz, table carePlanEOL, schema datasets/eicu/table-4a60395475cf75e7.json, with patientunitstayid, cpleolsaveoffset, cpleoldiscussionoffset, and activeupondischarge. Use only for a prespecified sensitivity exclusion/stratification when an EOL record is documented by minute 360. Absence of a row is not evidence that treatment limitations were absent.

intakeOutput is not used to construct the primary endpoint: its dialysistotal, outputtotal, celllabel, and cellvaluenumeric fields do not provide complete, validated KDIGO urine-output or dialysis adjudication. Apache aggregate tables are excluded from primary predictors because their timing/first-24-hour aggregation can overlap the landmark or outcome; they may be used only in a labeled leakage sensitivity.

## Predictor blocks

All extraction, label inventories, unit decisions, imputation values, scaling, and model tuning are fit within training hospitals and then frozen for the held-out fold. No outcome-derived label or preprocessing decision may use the held-out hospital.

M0, context-only baseline, contains only predeclared patient/stay variables: age, gender, ethnicity, hospital admission source, unit type, and unit stay type. It contains no hospital identifier, laboratory field, or post-landmark information.

Mphys, the primary physiology-only model, adds fixed summaries of the pre-landmark fields from vitalAperiodic and vitalPeriodic:

- noninvasive mean pressure: median, minimum, maximum, last value, interquartile range, and linear slope;
- heart rate, temperature, respiration, and oxygen saturation: median, minimum, maximum, last value, and linear slope;
- where present, systemicmean and pamean: the same summaries, but kept as separate modalities and never pooled as though identical.

Accept valid physiologic values only within fixed physiologic plausibility bounds established before outcome inspection; invalid values are missing. Primary Mphys uses training-hospital median imputation without missingness indicators, so the primary score does not encode laboratory or monitoring-process proxies. A prespecified sensitivity adds physiology observation counts, covered fraction, maximum gap, and modality indicators to both M0/Mphys and reports whether the result is driven by measurement density.

Mlab adds a fixed laboratory-value block to Mphys. The predeclared analyte label inventory is the normalized exact-name set creatinine, bun, sodium, potassium, chloride, bicarbonate, glucose, and lactate, where normalization is only lower-case plus trim. The preparation audit must list every encountered exact label and system/interface combination. No synonym or unit conversion is introduced after looking at outcome performance. For each analyte with a unit-compatible numeric value in [0,360], use first, last, minimum, maximum, and slope; retain an analyte-available flag for missing-value handling. If an analyte is absent or unit-incompatible, it remains missing and the limitation is reported.

Maug, the primary augmented model, adds the testing-process block to Mlab. This block uses only pre-landmark laboratory observation metadata: total lab-row count, number of distinct lab result timestamps, number of distinct analytes from the fixed inventory, per-analyte observation indicators/counts, time from ICU admission to first lab result, time from last lab result to minute 360, median inter-test interval, and maximum inter-test gap. These are descriptors of recorded testing, not measurements of clinician intent. Duplicate rows are deduplicated only by the exact source row identifier labid within stay; no rows are joined in a way that multiplies observations.

The primary scientific contrast is Maug versus Mphys. Mlab versus Mphys decomposes the contribution of measured laboratory values; Maug versus Mlab estimates the additional contribution of testing process. M0 supplies a nonphysiology baseline. All three model classes use the same discrete-time model family, regularization search, feature budget, and preprocessing rules.

## Analysis and hospital-held-out uncertainty

Fit a pooled discrete-time cause-specific hazard model over four follow-up bins: 6–12, 12–24, 24–36, and 36–48 ICU hours. The event hazard is first observed creatinine rise; ICU death or discharge before a qualifying test is a competing absorbing hazard. No-test follow-up is treated as censoring/unknown, not as a negative outcome.

The primary transport analysis uses five grouped hospital folds, assigned by a fixed hash of hospitalid; every stay from a hospital remains in one fold. Tuning, label/unit adjudication, imputation, scaling, and calibration are performed inside the training hospitals. Report paired held-out predictions from M0, Mphys, Mlab, and Maug for every fold and hospital.

Because creatinine observation is informative, report two complementary evaluation views:

1. a state-aware view in which the four ascertainment states are tabulated and unknown is a separate state, with multiclass Brier/log loss and the event one-versus-rest metrics reported without pretending unknown means no rise;
2. a primary ascertainable-event view using inverse-probability-of-observation/censoring weights estimated from pre-landmark information only. The common weight model includes M0 variables, early physiology summaries and density, early lab counts/availability, hospital, unit type, admission source, and baseline creatinine availability/value; positivity and weight truncation diagnostics are mandatory. It estimates performance for the observed-creatinine event under the stated observation process, not for unobserved biological AKI.

For each held-out fold and hospital, report event, competing-event, known-no-rise, and unknown counts; AUROC; area under the precision-recall curve; Brier score; calibration intercept and slope; and the paired Maug–Mphys differences. Summarize uncertainty with hospital-cluster bootstrap intervals (resampling hospitals, not rows) and fold-level ranges. A sensitivity uses leave-one-hospital-out predictions and a person-cluster check that keeps all stays of a uniquepid together. Hospital effects are used for grouping and weighting diagnostics only; no hospital ranking or hospital-specific treatment recommendation is made.

The primary support criterion is a directionally consistent Mphys advantage in held-out Brier/calibration across multiple hospitals, with an interval excluding no difference and no dependence on a single fold, sparse testing stratum, or one calibration adjustment. If Maug improves discrimination but worsens held-out calibration, that is not automatically a clinical win: it supports only a trade-off between local information and transport calibration.

## Missingness, observation, and falsification

Prespecified adverse/falsifying patterns include:

- Mphys does not outperform Maug on held-out Brier/calibration, or its direction changes across hospitals;
- any apparent Mphys advantage disappears after the common density/gap sensitivity, unit/interface stratification, or leave-one-hospital-out check;
- Maug's apparent improvement occurs only in random patient splits, only in complete-follow-up cases, or only when revised timestamps or Apache aggregates are allowed;
- a pre-landmark negative-control creatinine change (for example, change between two creatinine values both within [0,360]) shows the same transport contrast after matching its ascertainment structure;
- shuffling lab-process features within hospital and broad physiology/coverage strata leaves the augmented model's advantage unchanged, suggesting the signal is not tied to the claimed process block;
- swapping hospital labels in the evaluation or permuting process features within stay destroys/does not change performance in a way inconsistent with the claimed mechanism;
- performance is dominated by lab-result availability alone, with no stable value contribution, or by a single analyte whose label/unit audit is ambiguous.

Inconclusive conditions are too few events or hospitals, poor overlap of predictor distributions across held-out hospitals, nonpositive or highly unstable observation weights, substantial unresolved unit/label ambiguity, excessive unknown ascertainment, or an inability to separate discharge/death from missing laboratory follow-up. These conditions do not support a relaxed endpoint, post hoc exclusion, or a claim that testing practice is harmless.

Supportive results would mean that a physiology-only early summary is more calibrated and/or has lower held-out prediction error for this recorded creatinine-rise phenotype across hospitals, while the augmented model's local advantage fails to transport. They would support a transportable prognostic design principle: early physiologic summaries may be safer to move between institutions than features that encode local laboratory practice. They would not prove that labs are clinically unnecessary, that testing causes error, or that the physiology score should trigger surveillance.

Adverse results would mean that laboratory values/testing process transport as well as or better than physiology-only, or that any physiology advantage is unstable. This would reject the primary transport hypothesis for this endpoint, not show that physiology is unimportant or that laboratory testing should be reduced.

Inconclusive results would mean the snapshot cannot resolve portability because observation, event support, unit semantics, or hospital overlap is insufficient. A stronger study would need independently adjudicated AKI (including pre-ICU baseline and urine/dialysis criteria), raw waveform and device-quality data, validated laboratory order/collection/administration semantics, richer treatment and goals-of-care context, and prospective multi-hospital evaluation. Clinical utility would additionally require clinician review, decision thresholds, harms/costs, and prospective or quasi-experimental impact assessment.

## Demonstration dispositions

The three demonstrations were inspected within the availability limits in references/research-ambition/README.md and are not evidence for this hypothesis.

1. Learning the natural history of human disease with generative transformers (DOI 10.1038/s41586-025-09529-3): the local article text and available supplementary material were inspected. Its longitudinal temporal ordering and external-validation ambition motivate hospital-held-out testing here. eICU lacks its lifetime population, genetic/lifestyle context, and disease-trajectory target, so no transformer, generative trajectory, or disease-burden claim is imported.

2. Advancing cancer detection and treatment using longitudinal routine clinical data (DOI 10.1016/j.cell.2026.07.009): the README states that the main article and full STAR Methods remain unavailable; only bibliographic metadata and the supplementary PDF/text were inspected. No claim about unavailable main-paper methods is made. Its cancer, imaging, genomics, and prospective-screening dependencies are not used in this eICU proposal; the supplement's missingness-robustness theme is not treated as validation of the present hypothesis.

3. A Bayesian framework for longitudinal EHR and genetic discovery (DOI 10.1038/s41586-026-10780-5): the local article text and available supplementary/reporting material were inspected. The proposal adopts only the general discipline of explicit uncertainty and selection/observation awareness. eICU has no configured germline genetic modality or comparable longitudinal population history, so no genetic discovery or latent biological signature claim is made.

## Seed and data-scope disposition

The imported eICU-02 seed ([prior hypothesis]) is preserved as the conceptual starting point—testing-process features may be hospital-specific—but its broad outline did not itself specify this endpoint, landmark, missingness states, exact labels, or falsification. The present proposal makes the portability comparison primary and uses eICU-03 hypotension work only as a compatible physiology/outcome foundation, not as evidence that the hypothesis is true. The transfer seed ([prior hypothesis]) is not co-primary because pre-arrival history and a distinct transport question would confound the focus. MIMIC-IV, UK Biobank, and HCC are not joined: their configured sources remain read-only and accessible, but no cross-dataset evidence is claimed.

## Explicit unavailable evidence

This experiment can computationally verify source integrity, exact joins, feature-window compliance, cohort flow, model matching, held-out predictions, calibration, uncertainty, and the listed permutations/negative controls. It cannot verify adjudicated AKI, true renal reserve before ICU admission, completeness or intent of laboratory ordering, validity of all pressure measurements, cause of discharge/death, treatment intent, causal effects, clinical utility, or benefit from intensified surveillance. Those claims require clinical adjudication, missing modalities, expert review, or another prospective/quasi-experimental study.
