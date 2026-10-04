> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.


# Early post-TACE reserve change and subsequent recorded decompensation: an ascertainment-aware HCC study

## Deliverable and decision relevance

The scientific deliverable is a newly fitted, locked comparison of (1) a prespecified static liver-reserve baseline and (2) a temporal, nonlinear laboratory model, together with an estimate of whether early post-procedure reserve change adds reproducible information about a subsequent recorded decompensation episode. Completion requires a cohort-flow/ascertainment table, one index row per patient, fitted model artifacts and coefficients, locked test predictions, calibration/Brier/AUROC/AUPRC and decision-curve tables, bootstrap intervals, and procedure/outcome-definition sensitivity results. A schema audit alone is not completion.

The clinical question is whether a patient whose pre-TACE laboratory level looks acceptable but whose reserve worsens in days 3–14 should receive intensified surveillance and multidisciplinary reconsideration before another locoregional treatment is contemplated. This is prognostic, not an estimate of the causal effect of TACE or of a monitoring intervention.

## Hypothesis and evidence boundary

Hypothesis: among patients with HCC and a first recorded, high-specificity TACE in this snapshot, an early worsening trajectory in albumin, bilirubin, coagulation, platelets, creatinine or sodium during index+3 through index+14 is associated with a higher probability/hazard of a new recorded hepatic-decompensation diagnosis during index+15 through index+90, and improves out-of-sample calibration and decision-curve net benefit beyond pre-TACE reserve and history.

The local evidence establishes abundant HCC/TACE-coded activity and repeated laboratory and encounter records; it does not establish that a procedure label is a complete incident-treatment registry, that a diagnosis label is expert-adjudicated decompensation, that death is captured, or that all outpatient care is present. Current public HCC literature supports the broad importance of balancing tumor control and liver reserve, but does not validate this local trajectory or a clinical threshold. The unresolved claim is specifically incremental, leakage-safe prognostic information for recorded outcomes in this snapshot.

## Population and temporal design

Use only snapshot [source checksum].

1. Resolve every procedure row to its encounter and parse start time; discard unparseable times. Primary TACE exposure is high-specificity: procedure name equals TACE case-insensitively, or contains an explicit hepatic-artery chemoembolization combination (a hepatic-artery term such as hepatic artery or transcatheter hepatic artery and embolization/chemo terms such as embolization plus chemotherapy), including observed names hepatic artery chemoembolization, transarterial angiography and chemoembolization procedure（TACE）, and parenthesized catheter variants. Save the exact normalized vocabulary and counts. A sensitivity exposure adds transcatheter hepatic artery embolization, hepatic artery embolization, and equivalent labels, with non-TACE embolizations flagged separately. Do not infer TACE from medication or narrative text alone.

2. Define the index as the earliest qualifying primary TACE start per Patient Master Index. Exclude patients with any earlier qualifying primary TACE in the available procedure record. Require an HCC diagnosis on or before index, using normalized names containing hepatocellular carcinoma or the prespecified liver cancer term but excluding suspected/under investigation and non-HCC mixed malignancy labels unless clinically reviewed. The HCC diagnosis may be on another encounter; retain its linked encounter time.

3. Read encounters from HCC/data_basic_information_2500296761891079109.csv and resolve by (patient master index, visit number). Use age, sex, visit time, admission time, discharge time, visit department; do not treat department as hospital. Require a valid index encounter/time relationship and retain the procedure encounter. The unit is the patient, not procedure rows.

4. Resolve laboratory rows from HCC/data_Laboratory_609065997844652188.csv to encounters by (Patient Master Index, Encounter Number), then relate them to index using patient ID and parsed Laboratory Time. This patient-level temporal join is essential because post-index labs may be on a subsequent encounter. Baseline is [index−14 days, index]; post-treatment is [index+3 days, index+14 days]. Use the nearest valid observation to each landmark per assay, deterministic tie-breaking by timestamp then source row order; save observation delays.

5. Core assays are exact normalized names for albumin (Albumin), total bilirubin (Total Bilirubin), INR (International Normalized Ratio) or PT (Prothrombin Time), platelets (Platelets), creatinine (Creatinine) and sodium (Sodium). Do not pool assays or units by substring; produce an assay dictionary and reject ambiguous mappings, nonnumeric values and impossible sentinels. If INR and PT are both available, prespecify INR as primary and PT as a sensitivity replacement. Primary analysis requires all six components in both windows; report component-specific cohorts and a missingness-indicator analysis.

6. Follow-up begins strictly after index+14. Primary outcome interval is index+15 through index+90. Diagnosis rows have no time field, so event time is the linked encounter’s visit time, falling back to admission time only if prespecified and valid; never use the diagnosis row as timestamped. Exclude labels present on or before index+14 at patient level. Ascertainment-complete negatives require an observed encounter at or beyond index+90. Patients without that proxy are right-censored at their last linked encounter and excluded from the primary complete-window binary analysis but included in a time-to-recorded-event sensitivity analysis. This is an observed-care estimand and must be reported as such.

## Outcomes and evidence limits

Primary composite: first new qualifying diagnosis after index+14 through index+90 among Ascites, Hepatic encephalopathy, Liver failure/acute liver failure/chronic liver failure, or Upper gastrointestinal bleeding/gastrointestinal bleeding, with exact normalized matching and each component reported separately. A label present through index+14 is not incident. A secondary new recorded inpatient encounter is utilization, not decompensation.

Use HCC/data_diagnosis_7504718184492840569.csv columns Patient Master Index, Encounter Number, Diagnosis Name, Diagnosis Type; encounter linkage supplies timing. Do not use death-diagnosis rows as a death endpoint. There is no validated death capture, decompensation grade, transplant-free survival, tumor response/recurrence, radiographic staging, reliable hospital identifier, or complete outpatient history. Clinical adjudication of outcome-positive and outcome-negative charts and external validation are required before deployment.

## Baseline, alternative, estimand and analysis

The static baseline is regularized logistic regression for the complete-window composite using age, sex, index department, pre-index HCC/decompensation history, laboratory recency/availability, and six baseline values. No post-index variable or outcome-encoding procedure label is allowed.

The trajectory extension adds six direction-oriented deltas (albumin/platelets/sodium decrease and bilirubin/INR-or-PT/creatinine increase), observed delays, and a prespecified complete-case rule. The primary contrast is optimism-corrected test Brier/calibration improvement and decision-curve net benefit, not a small AUROC gain. Estimate associations per training-set interquartile range and worsening quartiles with 95% patient-bootstrap intervals.

The substantive learned alternative uses patient-level temporal gradient-boosted trees over ordered lab observations from index−14 through index+14. Each observation retains assay identity, value, time-from-index, baseline/post indicator, measurement count and missingness; vocabulary is limited to the six assays plus age, sex, prior diagnosis history and index procedure context. Fit and tune on patient-level 70/15/15 train/validation/test partitions stratified by outcome, with a later-index temporal holdout if event counts permit; calibrate only on validation and lock test. At most 500 trees and 10 tuning configurations are allowed. A monotonic model is sensitivity-only.

This alternative can reveal nonlinear thresholds, interactions and whether timing/shape contains information lost by a single delta. Defer it if event counts are inadequate, temporal density creates shortcut performance, or it adds no calibrated/decision-analytic information with uncertainty. A latent mixed-effects trajectory model is also deferred: it could estimate interpretable patient-specific slopes, but adds missing-data and local-optimum assumptions without being necessary for the primary claim. No GPU is necessary; use up to 4 CPUs and 16 GB RAM, stream the 2.2 GB laboratory file, and target 20–45 minutes extraction/fitting.

Use patient-level bootstrap for metrics, coefficients and associations; report calibration intercept/slope, Brier, AUROC, AUPRC and decision curves. Repeat with 30-day and 90-day horizons, broader/narrower TACE vocabulary, 0–30 versus 15–90 outcomes, index-encounter labs excluded from post measurements, PT replacing INR, component outcomes, missingness indicators, and censored time-to-recorded-event analysis. Preserve split seed, source/schema hashes, row counts, exact filters, code/software versions and exclusions.

## Falsification and interpretation

Supportive: worsening has the prespecified direction, its interval excludes no association in the locked primary test, and trajectory improves test Brier/calibration or net benefit over static baseline with stable direction across definition and temporal-holdout sensitivities. This supports incremental prediction of recorded decompensation.

Adverse: no association, reverse association, no incremental locked-test calibration/utility, or collapse after high-specificity procedure and leakage controls. This refutes the local incremental claim and argues against using these changes as a monitoring trigger without another study; it does not show biological irrelevance.

Inconclusive: too few complete cases/events, wide intervals, differential follow-up, assay ambiguity, strong dependence on diagnosis vocabulary or measurement density, or no ascertainment-complete negatives. This means the snapshot cannot resolve the claim.

Automatic verification can check joins, one-row-per-patient indexing, temporal exclusion, TACE vocabulary, incident-label logic, censoring, split integrity, artifacts, metrics, intervals and conclusion-to-output consistency. It cannot establish clinical diagnosis validity, unrecorded deaths, causal effects, treatment appropriateness, tumor response or benefit from altered monitoring.

## Exact bindings and alternatives not chosen

Primary sources:

- encounters: [internal dataset path]; patient master index, visit number, age, sex, visit time, admission time, discharge time, visit department.
- procedures: [internal dataset path]; Patient Master Index, Encounter Number, Surgery, Start Time, End Time, Surgery Source.
- diagnoses: [internal dataset path]; patient master index, encounter number, diagnosis name, diagnosis type.
- labs: [internal dataset path]; patient master index, encounter number, test, qualitative result, quantitative result, specimen type, test time.

The join key for payload tables is (patient master index, visit number); lab alignment and event timing additionally use patient ID and time. vitals, transfers and front_page are identifier-only. examinations, pathology, clinical_documents, orders and medications are optional sensitivity/audit sources, not substitutes for missing adjudication; no images, waveforms, stage or hospital table is available. All source files remain read-only; derived matrices, manifests, models and results are workspace outputs.

The selected method is static regularized regression plus bounded temporal boosting because both test the same incremental prognostic estimand and the learned model can expose nonlinear timing information. A latent mixed-effects model and transformer/generative sequence model are explicitly deferred pending stable event validity and evidence that trajectory shape, rather than incremental prediction alone, is the scientific uncertainty. The three demonstrations are disposed as follows: Delphi becomes the temporal trajectory adaptation but its UKB/Danish reproduction is unavailable; ALADYNOULLI is not reproduced because genetics are unavailable and its latent assumptions are unnecessary here; Oncoformer becomes a lab-only temporal adaptation because images and complete STAR Methods are unavailable. All 30 imported expert seeds target other dataset islands and cannot be bound to HCC rows, so none is used as a parent.
