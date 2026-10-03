# Residual physiologic instability before ICU discharge: a leakage-safe 48-hour MIMIC-IV test

Status: candidate-ready scientific design; no cohort scan, model fit, or study result was run.

Parent/seed: expert-20260913-mimic-10, imported as [prior hypothesis]. This is an independent discharge-instability direction, not an extension of the selected AKI-recovery branch.

## Scientific opening and falsifiable hypothesis

The seed asks whether high oxygen requirements or fluctuating vital signs before ICU discharge identify patients who return to the ICU or die soon afterward. The closest inspected evidence is [K1], a small single-center surgical cohort in which ward vital/laboratory flags were associated with ICU readmission or death within 48 hours. That supports a near-term prognostic signal, but not an intrinsic discharge-time phenotype, independence from destination, or actionability. [K3] shows why respiratory support, dependency, and destination must be separated: it found prognostic discharge-phase indicators in a small very-elderly cohort, did not have systematic treatment-limitation data, and explicitly did not interpret them causally. [K2] demonstrates that MIMIC-IV temporal models can be compared with tabular models for ICU-readmission prediction, but a causal-fused predictor is not evidence for a discharge policy.

Strongest supported claim: residual abnormal observations after ICU transfer can mark short-term adverse outcomes in some settings, and discharge-phase respiratory/dependency variables may carry prognostic information. Unresolved claim:

> Among adults discharged alive from an index ICU stay, after restricting predictors to the final 24 hours before ICU outtime and accounting for observation opportunity and discharge destination, is a prespecified persistent multi-domain instability phenotype associated with higher probability of first ICU readmission or hospital death within 48 hours?

Primary hypothesis: compared with adequately observed patients with no persistent abnormal domain, those with at least two persistent instability domains, including respiratory oxygenation/support when present, have higher 48-hour cumulative incidence of first ICU readmission or death. This is prognostic association only, not a claim that delaying discharge, increasing monitoring, or changing oxygen therapy would improve outcomes.

Rivals and predictions:

- Physiologic instability: the association persists within next-destination strata, among adequately observed patients, and across readmission/death components.
- Destination/selection: it is concentrated in particular next-care-unit or ultimate-disposition groups and attenuates after destination stratification. Destination is not a pre-discharge confounder, so this is descriptive standardization, not causal adjustment.
- Treatment limitation: death risk is concentrated among patients with goals-of-care limits. No reliable structured treatment-limitation field is verified; destination, hospital_expire_flag, or death cannot substitute.
- Observation process: instability is found mainly in densely monitored patients and a non-instability documentation-density control has a similar association.
- Residual severity: the contrast vanishes within bounded pre-discharge severity strata.
- Competing death/discharge: readmission is impossible after death and selectively observed while a patient remains in hospital.

Supportive results establish only a reproducible prognostic association. Adverse results weaken the seed. Sparse events, high unknownness, or missing treatment-limitation evidence are inconclusive, not null findings.

## Scientific deliverable

The future Harbor solver must produce: a cohort/observation flow; a dictionary audit with exact item labels, units, invalid-value rules and source hashes; four prespecified exposure states; 48-hour competing-risk counts and cumulative incidences; absolute risk differences and bootstrap intervals; destination- and observation-stratified estimates; a process-only falsification table; and a transparent-baseline versus learned-temporal comparison. Completion requires computed outputs, uncertainty, counts, missingness flow, model specifications, and interpretations linked to outputs. Readiness is not a result.

## Population and time boundary

Use MIMIC-IV 3.1. Unit is one adult admission and first valid ICU stay.

- patients.anchor_age >= 18, joined on subject_id.
- icustays with intime < outtime; earliest intime per subject_id, hadm_id.
- Join icustays to admissions on subject_id, hadm_id. Let t_d = icustays.outtime. Retain only patients not dead at or before t_d: admissions.deathtime null or after t_d. Do not require hospital survival after t_d.
- Retain every destination, including ward, intermediate/step-down if represented, hospice/palliative, and unknown.
- No predictor uses a timestamp or value at or after t_d. Primary window is [t_d-24 hours, t_d), four 6-hour bins. charttime is the clinical time; storetime is only a lag sensitivity.
- Classifiable exposure requires a valid core observation in at least 3 of 4 bins. A missing bin is unknown, never normal. The primary estimand is the observed alive-ICU-discharge prognostic estimand; report the all-eligible flow separately and do not call it an onset-cohort or causal effect.

Sensitivity requirements are fixed before outcome inspection: at least one SpO2 or oxygen-support record in 3 bins, and all 4 bins.

## Exact exposure and item bindings

Use icu/chartevents fields subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom, warning; join stay_id and filter to the primary window. Join itemid to icu/d_items and verify label, abbreviation, linksto, category, unitname, param_type, lownormalvalue, and highnormalvalue.

Primary item set:

- 220045, Heart Rate.
- 220052, Arterial Blood Pressure mean.
- 220210, Respiratory Rate.
- 220277, O2 saturation pulseoxymetry.
- 223834, O2 Flow.
- 223835, Inspired O2 Fraction.
- 223761, Temperature Fahrenheit; 223762, Temperature Celsius. Convert Fahrenheit to Celsius.
- 226732, O2 Delivery Device(s), descriptive/device sensitivity only.

The readiness audit must read these dictionary rows from the frozen source and stop on label, linksto, or unit mismatch. Values are finite numeric values with dictionary-confirmed units; text-only values are invalid. For each bin use the median for vital signs and maximum oxygen flow/FiO2. Do not impute missing bins.

Fixed domain thresholds:

- Respiratory/oxygen: SpO2 <92%, or O2 Flow >0 L/min, or Inspired O2 Fraction >0.21.
- Hemodynamic: MAP <65 mmHg, or heart rate >100 or <50 beats/min.
- Ventilatory pattern: respiratory rate >24 or <8 breaths/min.
- Temperature: <36.0 or >38.3 Celsius.

A domain is persistent when flagged in at least 2 of 4 bins. Primary exposure states are stable/no persistent domain, one persistent domain, at least two persistent domains, and unknown/insufficient. Primary contrast is at least two versus stable. Report oxygen-support components separately because support may reflect chronic need and is not hypoxemia. Report adjacent-bin changes and within-window ranges as secondary volatility descriptors. Do not choose cutoffs after seeing outcomes.

The fields do not establish chronic home oxygen, device setting, work of breathing, or whether a value was available to the discharge decision. Do not call the oxygen signal respiratory failure without clinical adjudication.

## 48-hour outcomes and competing events

Use the first event in [t_d,t_d+48 hours):

- ICU readmission: subsequent icustays.intime for the same subject_id, hadm_id with intime >= t_d and < t_d+48h; do not count the index stay.
- Hospital death: admissions.deathtime in the interval.
- Alive hospital discharge before 48h: admissions.dischtime in the interval with no earlier death/readmission; a competing event for observing further in-hospital readmission.
- Event-free at 48h: alive, no readmission, not discharged before 48h.

If death and readmission tie, assign the earliest clinical time and report a data-integrity flag. Primary outcome is the composite of readmission or death, but always report both components and competing discharge. Use Aalen–Johansen cumulative incidence descriptively. For adjusted analysis, fit cause-specific discrete-time hazards in 6-hour intervals for readmission, death and alive discharge, then standardize 48-hour cumulative incidences. A first-event multinomial model is sensitivity only.

A hospice/palliative or other treatment-limited destination is not physiologic recovery. It is a destination/competing-event category.

## Destination, limitation, severity, and observation rivals

Immediate destination comes from hosp/transfers fields subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime: first row after t_d joined on subject_id, hadm_id. If absent, unknown. Ultimate destination is separately admissions.discharge_location; never substitute it for immediate ICU destination.

The catalog has note/discharge with note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text and note/discharge_detail with note_id, subject_id, field_name, field_value, field_ordinal. Discharge-note text can be charted after t_d and contain future information. It is excluded from primary predictors and adjustment. No reliable structured treatment-limitation variable is verified. hosp/omr (subject_id, chartdate, seq_num, result_name, result_value) is not a verified goals-of-care field. A future external study could use blinded pre-t_d clinical adjudication; this Harbor experiment cannot resolve treatment limitation.

Residual severity uses only pre-t_d information: age/sex/admission type from patients/admissions; ICU timing and length from icustays; pre-window creatinine, lactate, hemoglobin, platelet, WBC, and glucose from labevents plus d_labitems; and pre-window support/procedure indicators from procedureevents. Required labevents fields are labevent_id, subject_id, hadm_id, itemid, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag. Primary creatinine itemid is 50912, with d_labitems label/unit verification. Never adjust for post-t_d data, outcomes, or learned predictions.

Observation diagnostic: per 6-hour bin count valid core chartevents and all non-core chartevents, labevents, inputevents, and outputevents. Estimate outcomes over prespecified quartiles of non-instability documentation density. A similar process-only gradient or strong attenuation after density stratification weakens the physiologic interpretation. This is not a negative-control outcome.

## Exact source bindings and provenance

Catalog: [internal dataset path]; [source checksum]; snapshot [source checksum].

MIMIC archive: [internal dataset path]; [source checksum].

Required archive members and bindings:

| purpose | table/member | required columns and join |
|---|---|---|
| index ICU | icu/icustays; mimic-iv-3.1/icu/icustays.csv.gz | subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los; earliest intime per subject_id,hadm_id |
| hospital outcomes | hosp/admissions; mimic-iv-3.1/hosp/admissions.csv.gz | subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, discharge_location, hospital_expire_flag; join subject_id,hadm_id |
| demographics | hosp/patients; mimic-iv-3.1/hosp/patients.csv.gz | subject_id, gender, anchor_age, dod; join subject_id |
| immediate destination | hosp/transfers; mimic-iv-3.1/hosp/transfers.csv.gz | subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime; first intime after t_d |
| physiologic data | icu/chartevents; mimic-iv-3.1/icu/chartevents.csv.gz | subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom, warning; join stay_id |
| item dictionary | icu/d_items; mimic-iv-3.1/icu/d_items.csv.gz | itemid, label, abbreviation, linksto, category, unitname, param_type, lownormalvalue, highnormalvalue |
| severity labs | hosp/labevents; mimic-iv-3.1/hosp/labevents.csv.gz | labevent_id, subject_id, hadm_id, itemid, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag |
| lab dictionary | hosp/d_labitems; mimic-iv-3.1/hosp/d_labitems.csv.gz | itemid, label, fluid, category |
| support/procedures | icu/procedureevents; mimic-iv-3.1/icu/procedureevents.csv.gz | subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, value, valueuom, ordercategoryname, ordercategorydescription, statusdescription |
| observation opportunity | icu/inputevents; mimic-iv-3.1/icu/inputevents.csv.gz | subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom, totalamount, totalamountuom, statusdescription |
| urine/opportunity | icu/outputevents; mimic-iv-3.1/icu/outputevents.csv.gz | subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom |
| treatment evidence boundary | note/discharge; [internal dataset path] | SHA-256 c194a975571df5e1c2486c094a52fef7cb3e183b03556cff0c23cea55878578; note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text; excluded from primary predictors |
| note detail | note/discharge_detail; [internal dataset path] | [source checksum]; note_id, subject_id, field_name, field_value, field_ordinal |

The catalog verifies these schemas and provenance. Final readiness must still read the actual item dictionary rows. Source data are read-only and no archive payload is copied into this branch.

## Transparent baseline versus learned temporal alternative

The transparent baseline directly fits the scientific question: four-state exposure, persistent domain flags, final-24h last/median/min/max/slope summaries, pre-window severity, age/sex/admission type, ICU timing and observation counts. Fit cause-specific discrete-time logistic models and standardize 48-hour CIFs with bootstrap uncertainty. Report unadjusted contrasts, destination strata, and a sensitivity including next destination as a post-landmark selection variable. Do not call any of this causal.

The learned alternative is a small GRU competing-risk model on the same patients and final-24h boundary. The primary learned representation is 12 two-hour bins with the eight physiologic channels, missingness masks, elapsed time, observation counts, domain indicators and pre-window static severity. The output has cause-specific hazards for readmission, death and alive discharge. Split by subject_id, fixed 70/15/15 train/validation/test, with training-only normalization and no patient in more than one split. Primary model evaluation is held-out cause-specific Brier score and calibration at 48h; AUROC/AUPRC are secondary. Compare on identical subjects/outcomes/boundary.

This alternative can reveal whether persistence, volatility and missingness carry information lost by fixed summaries; saliency is not mechanism. The baseline is primary because it is auditable. The GRU is retained because it tests a distinct temporal uncertainty. Causal-fused and transformer models are deferred: without measured treatment limitation, clinician intent, discharge timing rationale or a valid intervention, extra causal machinery/capacity would not resolve the central rivals. Revisit only after independent treatment-limitation adjudication.

Planning estimate, not a result: archive scanning/derived-table construction is managed CPU work; baseline 2–4 CPUs and 8–16 GiB after materialization; small GRU hidden size 32–64, batch 128, at most three prespecified seeds, one allocated GPU or documented CPU fallback. Readiness must check the approved solver limits and preserve a checkpoint. No proposer/solver training is authorized.

## Falsification and interpretation

Supportive: multi-domain instability has higher standardized 48-hour composite incidence than stable; the association is present in adequately observed patients and not confined to one destination; components are directionally coherent; and ordered features improve held-out calibration/Brier or distinguish persistent from transient instability. Conclusion remains prognostic association compatible with residual instability.

Adverse: no primary contrast; signal only for oxygen support but not hypoxemia/vital domains; disappearance in severity/destination strata; comparable documentation-density gradient; or strong dependence on discharge-before-observation. This favors severity, destination, or observation explanations. Predictive improvement without a stable phenotype contrast is predictive utility only.

Inconclusive: sparse events, high unknown fraction, dictionary/unit failure, or intervals too wide to exclude clinically meaningful effects. Do not move thresholds or merge states after viewing outcomes. Resolution requires a larger/completer cohort, external validation, direct oxygen-device data, clinician adjudication of treatment limitation/discharge intent, or a prospective intervention study.

## Inspected works

[K1] Rens et al., 2026. Abstract-only; supports the short-term instability/outcome opening but is limited by a small single-center surgical setting and inaccessible full text.

[K2] Remoundou et al., 2026. Full text; bounds the MIMIC temporal-model comparison and reinforces that associative prediction is not causal inference.

[K3] Gülen et al., 2026. Full text; supports separating respiratory support, destination, dependency, and unavailable treatment limitation in discharge-phase prognosis.

See key-references.json and the three attached UTF-8 evidence excerpts for hash-linked receipts. Exactly three distinct works are used.
