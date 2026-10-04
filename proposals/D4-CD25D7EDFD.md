> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Repaired UKB seed 23: repeated CBC discordance and cancer-site risk

Status: planned study design; counts marked “observed feasibility” are bounded source audits, not hypothesis-test results. Parent: [prior hypothesis]. Seed origin: [starting question].

## Scientific opening and deliverable

The observed opening is not merely that a new dataset is available. Prior clinical work finds that common blood-test abnormalities can precede colorectal-cancer diagnosis and may differ by cancer site [K1]. A recent retrospective CRC-only study reports that serial CBC trajectories, especially haemoglobin decline and inflammatory indices, may precede aggressive CRC [K2]. A 90-study scoping review says the trend literature remains fragmented and exploratory, with informative observation a recurring bias and limited evidence for how trends should be used [K3]. None of these inspected works resolves whether the same person's repeated haemoglobin/RDW/platelet/WBC change contains site-specific information distinguishing future colorectal from hematologic cancer in people cancer-free at a defined landmark.

The new scientific deliverable is one prespecified, independently computable estimate: the CRC-versus-hematologic contrast in cause-specific risk associated with repeated CBC discordance after adjustment for the second CBC's levels, baseline covariates, the interval between samples and measured inflammation. Completion requires a fitted primary competing-risk model, a held-out learned comparison, estimates with 95% uncertainty intervals, calibration/discrimination outputs, lag and outcome-code sensitivity analyses, and a conclusion classified as supportive, adverse or inconclusive under the rules below. No fitted result is claimed here.

## Hypothesis and competing explanations

Primary hypothesis (H1): among participants with complete CBC at assessment instances 0 and 1 and no registry-coded malignant neoplasm by the second assessment, a trajectory combining falling haemoglobin, rising RDW and rising platelets with relatively stable WBC is more associated with subsequent colorectal cancer than hematologic cancer; a trajectory combining falling haemoglobin with a material WBC or platelet change and without the CRC-like combination is more associated with hematologic cancer. The prespecified clinically meaningful alternative is that the CRC-to-hematologic cause-specific hazard contrast per one-SD trajectory contrast is at least 1.5, after adjustment.

The continuous primary exposure is the four-vector of within-person changes:
Delta_j = (X_j,instance1 - X_j,instance0) / s_j, for j in {WBC, haemoglobin, RDW, platelets}, where s_j is the instance-0 standard deviation estimated in the development partition only. CBC units are retained from the source: WBC and platelets are 10^9 cells/Litre, haemoglobin is grams/decilitre and RDW is percent. The primary model tests the prespecified exposure-by-outcome interaction in a stacked CRC/hematologic cause-specific model. For an interpretable secondary contrast, “CRC-like” means Delta_Hb <= -0.5, Delta_RDW >= +0.5, Delta_platelet >= +0.5 and |Delta_WBC| < 0.5. “Heme-like” means Delta_Hb <= -0.5 and either |Delta_WBC| >= 0.5 or Delta_platelet <= -0.5, excluding CRC-like. All remaining trajectories are the reference; these thresholds are design thresholds, not diagnostic cutoffs.

The strongest rival is occult disease/proximity: the pattern is a consequence of an already developing cancer and increased testing or hospital ascertainment near diagnosis, not a durable site-specific precursor. It predicts a much larger effect within 0–1 year of the landmark and attenuation after a two-year exclusion, with little evidence in longer-lag events.

The second rival is inflammation or another non-specific systemic process: CRP, infection, chronic disease, nutrition or medication changes drive WBC, platelets and RDW. It predicts similar associations for other cancers or non-cancer inflammatory outcomes and substantial attenuation after CRP adjustment or restriction to stable/low-CRP measurements.

The third rival is selection and measurement: repeat attendees are healthier and differ in observation frequency, sample interval, assay conditions and regression to the mean. It predicts imbalance in repeat participation, dependence on the interval or assessment calendar, and instability when inverse-probability weighting, interval adjustment, reversed change or the inpatient-code sensitivity outcome is used. Even a surviving association would be descriptive/predictive, not proof of occult blood loss, marrow failure, clonal haematopoiesis or another mechanism.

## Exact data binding and observed feasibility audit

Primary source and table:

- Catalog table: ukb671626.csv (Parquet), table metadata datasets/ukb/table-5d49a6760e7ffdbd.json, identifier namespace ukb671626.
- Read-only convenience source: [internal dataset path], [source checksum], 502,371 rows and 502,371 unique eid.
- Original source lineage: [internal dataset path], source ID [UKB data file], [source checksum]; archive member is ordinary file. The Parquet view preserves source columns as strings; the solver must cast values explicitly.
- Join key: eid, only within ukb671626. No participant join to ukb672073, olink or dta is used or authorized.

Required exposure and timing columns, all in this same table and namespace:

- Landmark: 53-0.0 and 53-1.0, “Date of attending assessment centre”. Entry is the date in 53-1.0.
- CBC at the two assessments: 30000-0.0/1.0 WBC; 30020-0.0/1.0 haemoglobin; 30070-0.0/1.0 RDW; 30080-0.0/1.0 platelets. The source metadata identifies these as three-instance blood-sample fields; only instances 0 and 1 are used for the primary two-visit design.
- Prespecified adjustment/rival fields: 31-0.0 sex, 34-0.0 year of birth, 21001-0.0/1.0 BMI, 20116-0.0/1.0 smoking status, and 30710-0.0/1.0 CRP. 53-1.0 - 53-0.0 is the sample interval. Assessment-centre identity is not needed for a participant join; if available as a source field, it may be included as a fixed effect only if its exact column is documented before fitting.
- Primary cancer registry outcome: paired arrays 40006-0.0 through 40006-21.0 (“Type of cancer: ICD10”) and 40005-0.0 through 40005-21.0 (“Date of cancer diagnosis”). Each non-missing type is paired by the same array index with its date.
- Death competing event: 40000-0.0 and 40000-1.0 (“Date of death”). Administrative follow-up ends at the maximum non-missing primary registry date observed in this frozen source, 2022-06-01; the solver must recompute and report this checksum rather than assume it.
- Outcome sensitivity source in the same table: paired 41270-0.0 through 41270-258.0 (“Diagnoses - ICD10”) and 41280-0.0 through 41280-258.0 (“Date of first in-patient diagnosis - ICD10”), with the same array-index pairing. These fields are not used to silently replace the registry outcome.

Observed feasibility checks performed in this branch: instance-0 complete CBC was 478,033; complete CBC at both instances 0 and 1 was 18,377; the second-assessment landmark dates among those were 2012-08-01 through 2013-06-07. Applying the primary registry arrays and broad families below, 1,801 had any C00–C97 code on or before the landmark, leaving 16,576 registry-cancer-free participants. Among them, first post-landmark target events were 173 colorectal and 118 hematologic. These counts are source audits only; they are not adjusted estimates, do not establish event completeness, and were not used to choose a favourable result.

## Population, outcomes and temporal estimands

Include participants with non-missing and clinically castable values for all four CBC measures at both 53-0.0 and 53-1.0, with a valid second-assessment date strictly after the first. Exclude anyone with a first registry cancer date on or before t0 for any ICD-10 malignant-neoplasm code C00–C97 in 40005/40006, and exclude impossible dates or a second assessment after the administrative cancer-data end. Do not replace missing values by zero. Record the flow table, missingness, repeat interval and comparison of included versus instance-0 CBC-complete non-repeat attendees.

Normalize ICD-10 strings only by trimming, uppercasing and removing punctuation for family matching; retain the original code for audit. The primary families are colorectal C18–C20 (including all subcodes) and hematologic C81–C96 (including all subcodes). Codes outside those families are not silently assigned to either target. The primary event is the earliest dated target-family cancer after t0. A same-day CRC and hematologic pair is a tie: report it separately and exclude it from the mutually exclusive primary contrast, with a sensitivity assigning it to the first array entry. Other C00–C97 cancers are competing events. Non-cancer death before a target event is a competing event. Follow-up is from t0 to the first target, other cancer, death or T_admin = 2022-06-01, whichever comes first.

The primary estimand is the cause-specific hazard-ratio contrast for the four-vector trajectory between CRC and hematologic cancer:
log(HR_CRC,trajectory) - log(HR_HEME,trajectory).
Report also five-year cumulative-incidence functions for CRC and hematologic cancer, their absolute risk difference between the prespecified CRC-like and heme-like patterns, and 95% confidence intervals. Cause-specific hazards are the primary etiologic/descriptive estimand; cumulative incidence is the clinically interpretable competing-risk summary. Neither is a causal effect of changing a CBC.

Secondary temporal estimands repeat the model after excluding cancer events within 1 year and within 2 years after t0, and report event counts and intervals. A signal limited to the near-diagnosis window is evidence for proximity/ascertainment rather than a stable long-horizon precursor. Secondary analyses use 1-, 3- and 5-year horizons where supported by event counts.

## Analysis, baseline and substantive learned alternative

Primary inferential model: construct one row per person per cause in a stacked cause-specific Cox model, with an outcome-by-trajectory interaction. Adjust for age at t0 (from 34-0.0 and 53-1.0), sex, baseline CBC values at instance 0, second CBC values at instance 1, the CBC change vector, sample interval, BMI, smoking and baseline CRP. Use prespecified missingness indicators plus development-partition medians for optional covariates; do not impute a missing primary CBC. Use restricted cubic splines only for age and interval if the spline specification is fixed before fitting. Use robust participant-clustered standard errors and report proportional-hazard diagnostics. A penalized version may stabilize the hematologic endpoint, but it must report the penalty and sensitivity to unpenalized fitting.

The simple baseline is a cause-specific Cox model using age, sex, interval, BMI, smoking, baseline CBC levels and baseline CRP but no within-person CBC changes. The primary incremental check adds the four change terms and their outcome interactions. This baseline is scientifically necessary: if changes do not add calibrated site discrimination beyond the second CBC/current state, a complicated trajectory model cannot support a new precursor claim.

The substantive learned alternative is a CPU gradient-boosted competing-risk classifier fitted to exactly the same landmark population and targets, using baseline and repeat CBC values, the four changes, interval, age, sex, BMI, smoking, CRP and explicit missingness flags. It may use nonlinear interactions and monotonicity-free trees because the rival explanations allow non-monotone patterns; tuning is restricted to the development partition. It must output 1-, 3- and 5-year CRC, hematologic, other-cancer/death and no-event probabilities. The alternative could reveal threshold-free combinations and interactions that the additive Cox baseline loses, such as a falling haemoglobin being informative only when RDW and platelets move together. It cannot identify a biological mechanism and must not be selected merely for a small AUC gain.

Use a deterministic participant-level hash split (60% development, 20% validation, 20% held-out test), performed after defining eligibility and before standardization or imputation. All tuning and feature scaling use development only. Compare the baseline, linear change model and learned model on the held-out set using cause-specific time-dependent AUC, integrated Brier score, calibration slope/intercept and calibration plots at 1, 3 and 5 years; bootstrap participants for intervals. Report the prespecified trajectory interaction and cumulative incidence regardless of predictive ranking. A model with better discrimination but poor calibration or no stable site-specific interaction does not establish the hypothesis.

Selection/measurement checks: estimate repeat-attendance weights from instance-0 CBC-complete participants using observed age, sex, BMI, smoking, baseline CBC, CRP and assessment date; truncate only under a predeclared rule and report the unweighted and weighted estimates. Adjust for the exact interval and include a negative-control analysis with the sign of the change vector reversed or participant-level assessment order permuted; this should not reproduce the prespecified directional contrast. The permutation is a diagnostic, not an additional discovery opportunity.

## Falsification and interpretation rules

Supportive: the held-out and inferential analyses show the prespecified directional CRC-like versus heme-like contrast, with the primary 95% interval entirely above the design threshold of 1.5 for the CRC-to-hematologic hazard contrast, stable direction after the 1- and 2-year exclusions and registry/inpatient outcome sensitivity, and acceptable held-out calibration. This would support a reproducible descriptive site-discrimination signal worth external validation; it would not justify clinical referral thresholds or a mechanism.

Adverse: the primary contrast is directionally opposite with a 95% interval excluding the null, or the prespecified pattern is associated more strongly with hematologic than colorectal cancer, or the effect disappears/reverses in the predeclared registry/inpatient replication and weighting checks. This would falsify the stated directional hypothesis and should stop a CRC-specific interpretation, while leaving open a different broad-cancer or hematologic question.

Inconclusive: the interval includes both no meaningful contrast and the 1.5 threshold, particularly with sparse hematologic events, or the long-lag and held-out estimates are too imprecise. Do not call this a negative mechanistic result. Continue only with a larger or clinically richer cohort, not with repeated exploratory threshold searches.

A pattern restricted to 0–1 year, a strong association with other cancers/non-cancer inflammatory diagnoses, or major attenuation after CRP and observation weighting supports the proximity/inflammation/selection rivals rather than H1. A modest learned-model improvement without a stable prespecified interaction is predictive utility at most, not evidence that CBC discordance distinguishes disease biology.

## Missing clinical evidence and decision boundary

The source lacks ferritin, transferrin saturation, reticulocyte count, stool blood/FIT, menstrual or gastrointestinal symptoms, infection timing, medication exposure, primary-care test-ordering context, pathology, cancer stage, morphology, flow cytometry, cytogenetics, molecular subtype, treatment and systematic external validation. Total WBC, RDW, haemoglobin and platelets cannot adjudicate iron deficiency, occult gastrointestinal blood loss, marrow infiltration or clonal haematopoiesis. The assessment-centre repeat sample is not equivalent to routine longitudinal primary-care CBC monitoring, and repeat attendance creates healthy-volunteer selection.

Therefore the computable claim is limited to whether these coded, timed repeated measurements show a reproducible association with later registry-coded cancer families. Clinical adjudication is required to label a trajectory as occult bleeding or hematologic production abnormality; a primary-care validation with test-ordering context and complete cancer staging is required for clinical utility; a prospective impact study is required before changing referral or surveillance. Even a supportive result cannot establish causality or recommend a patient-specific action.

## Alternatives considered and selection record

A static abnormality/threshold analysis was deferred as the main method because it discards within-person change and is useful only as a negative comparator. A linear cause-specific Cox model was retained as the primary explanatory baseline because it gives an interpretable estimand and uncertainty with approximately 16,576 eligible participants and 118 hematologic events. A gradient-boosted competing-risk model was retained as a substantive learned alternative because it can expose nonlinear CBC interactions while remaining feasible on CPU. A neural sequence model was deferred: only two complete CBC visits define the primary cohort, so its extra capacity would not resolve a scientific uncertainty and would risk treating observation patterns as biology; it can be revisited only if a future design uses additional dated CBC observations.

Measured discovery resource facts: reading the selected CBC columns took about 6 seconds in the local Parquet audit; the registry outcome scan and bounded counting took about 32 seconds after data loading. Future fitting estimates are unverified: approximately 4–8 CPU cores, under 16 GB RAM, 10–30 minutes for the linear/boosted fits and 1–3 hours for participant bootstrap and calibration. No GPU is required or assumed. The future solver planning envelope is 16 CPUs, 256 GB memory and up to 8 GPUs for 28,800 seconds; this design requests CPU by default and does not spend GPU capacity for a small tabular problem.

## Key references

[K1] Rafiq et al., 2024, Cancer Medicine. Pre-diagnostic primary-care blood-test abnormalities differ between colorectal and lung cancer, but the study does not compare hematologic cancer or establish mechanism. Inspected full text; attached excerpt and receipt in key-references.json.

[K2] Sala et al., 2026, Translational Oncology. Serial CBC trajectories may precede aggressive CRC in a single-centre CRC-only cohort, but the proof of concept requires prospective external validation and does not answer site discrimination. Inspected full text; attached excerpt and receipt in key-references.json.

[K3] Zhu et al., 2026, Diagnostic and Prognostic Research. The trend literature is broad but fragmented, with informative observation and implementation gaps. Inspected full text; attached excerpt and receipt in key-references.json.

These are exactly three distinct inspected works. The attached excerpts are UTF-8, each under 1 MiB, and their hashes are the hashes of the attached bytes rather than URLs or unavailable original PDFs.
