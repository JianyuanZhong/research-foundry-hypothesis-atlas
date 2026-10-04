> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Residual physiologic instability in the final ICU day and failed transition

Parent: [prior hypothesis] (repaired imported expert seed `[starting question]`)
Dataset: MIMIC-IV v3.1 snapshot `[source checksum]`

## Question, hypothesis, and advance

The unresolved question is whether the *trajectory* of physiologic recovery during the final 24 hours of an ICU stay predicts what happens immediately after ICU discharge beyond a conventional last-value assessment.

Primary hypothesis (falsifiable): among adults discharged alive from an index ICU stay, a longitudinal model using the ordered, irregularly observed final-day vital-sign/oxygen-support sequence will improve held-out 48-hour cause-specific risk estimation for ICU readmission, while preserving calibration for death, compared with a prespecified interpretable model using only last observed values, support at discharge, observation recency, and baseline covariates.

The seed's supported motivation is only that residual oxygen needs and fluctuating vital signs are clinically plausible warning signs. The available evidence does not establish the proposed association in this snapshot, the size of any improvement, or that changing discharge timing would improve outcomes. Public search found prior last-24-hour and MIMIC-based prediction studies, so novelty is not “using final-day data” or “using machine learning.” The substantive advance is a direct same-cohort, patient-held-out comparison of ordered multivariate trajectories against last-state summaries, with ICU readmission and ward death modeled as competing first events. It tests whether persistence, recovery, oscillation, and missingness carry information that a last value loses.

Clinical importance: ICU readmission or death soon after transfer can trigger escalation, monitoring, or review of discharge readiness. A reliable prognostic signal could support targeted observation or prospective validation. It cannot by itself support a discharge rule.

## Population and index stay

Use the configured MIMIC source, not a public substitute:

- Source archive: `[internal dataset path]`, [source checksum].
- `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`: `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`.
- `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`: `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admission_location, discharge_location, hospital_expire_flag`.
- `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`: `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`.

Select one index stay per `hadm_id): the chronologically first ICU stay by `intime), joined to its admission on `subject_id, hadm_id`. Require computed `outtime > intime`, ICU duration at least 24 hours, and an ICU discharge alive: `deathtime` is null or strictly later than `outtime`. Require at least one valid primary physiologic observation in at least six distinct hourly bins in the exposure window; retain a sensitivity cohort without this observability restriction and report all exclusions. Do not select stays based on outcome data.

This is an index ICU transition, not every ICU discharge. The restriction avoids correlated multiple rows per admission and makes a later ICU stay a meaningful return event. Report the number of admissions with multiple ICU stays and the number excluded for death/timing/observability.

## Exposure window and exact variables

For each index stay, define the final-day window as `[outtime - 24 hours, outtime)`. No value with timestamp at or after `outtime` may enter a feature. MIMIC dates are subject-specific shifted timestamps; use within-subject/stay intervals only, never cross-subject calendar matching.

Structured observations come from:

- `mimic-iv-3.1/icu/chartevents.csv.gz`, table `icu/chartevents`, columns `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom, warning`; join `itemid` to
- `mimic-iv-3.1/icu/d_items.csv.gz`, table `icu/d_items`, columns `itemid, label, abbreviation, linksto, category, unitname, param_type, lownormalvalue, highnormalvalue`.

The primary item allowlist is:

- HR: `220045`, label Heart Rate, bpm.
- RR: `220210`, Respiratory Rate, insp/min.
- SpO2: `220277`, O2 saturation pulseoxymetry, %.
- Non-invasive mean BP: `220181`, Non Invasive Blood Pressure mean, mmHg.
- Arterial mean BP: `220052`, Arterial Blood Pressure mean, mmHg.
- Temperature C: `223762`, Temperature Celsius, °C.
- Temperature F: `223761`, Temperature Fahrenheit, °F; convert to C as `(F-32)*5/9`.
- Oxygen flow: `223834`, O2 Flow, L/min.
- Inspired oxygen fraction: `223835`, Inspired O2 Fraction (FiO2).
- Delivery device: `226732`, O2 Delivery Device(s), text.

Use numeric `valuenum` when present, preserve source `valueuom`, and apply prespecified physiologic validity filters (HR 20–250 bpm; RR 3–80/min; SpO2 50–100%; mean BP 20–200 mmHg; temperature C 25–45; oxygen flow 0–80 L/min; FiO2 0.21–1.0, allowing 21–100% values only after explicit normalization). Values failing these checks become missing and are counted. If both arterial and non-invasive mean BP are present in a bin, use the arterial value; otherwise use non-invasive. Keep a source indicator. Do not use alarm items as physiologic values.

Respiratory-support intervals come from `mimic-iv-3.1/icu/procedureevents.csv.gz`, table `icu/procedureevents`, columns `subject_id, hadm_id, stay_id, starttime, endtime, itemid, value, ordercategoryname, statusdescription` and related fields. Use item `225792` (Invasive Ventilation) and `225794` (Non-invasive Ventilation), identified in `icu/d_items` as procedure-linked. An interval is active when its time range intersects a 6-hour bin; clip intervals to the exposure window. Include the maximum support class active per bin and an active-at-`outtime` indicator. This is not a complete ventilator waveform or respiratory-device record.

Optional prespecified secondary physiologic labs are from `mimic-iv-3.1/hosp/labevents.csv.gz`, table `hosp/labevents`, columns `subject_id, hadm_id, charttime, storetime, itemid, value, valuenum, valueuom, flag, comments`, joined to `mimic-iv-3.1/hosp/d_labitems.csv.gz`, table `hosp/d_labitems`, columns `itemid, label, fluid, category`: blood lactate `50813` (and `52442` only if source fluid/unit validation confirms equivalence), creatinine `50912`, sodium `50983`, hemoglobin `51222`, and WBC `51300`. Join labs to the index admission on `subject_id, hadm_id` and retain only `charttime` in the same final-day window. Labs are secondary because their measurement is clinically selected and sparse; the primary hypothesis is tested without them.

Do not use discharge-note text, radiology text, prescriptions, or post-outtime measurements as primary predictors. The configured note sources are available but text extraction is explicitly unvalidated for comprehensive clinical concepts; using them would add leakage and an unneeded measurement question.

## Feature construction

Partition the final day into four consecutive 6-hour bins, half-open at the right boundary. For each numeric domain and bin, store median, last value, minimum, maximum, standard deviation when at least two measurements exist, count, and time from bin end to last observation. For the learned input, use the bin median/last value, observation count, mask, and time since observation; standardize using training data only. Keep values missing rather than imputing without a mask.

The interpretable baseline uses only the most recent valid value before `outtime` (prefer an observation in the final 6 hours), source/support at discharge, time since last measurement, counts, missingness, and the following prespecified covariates: `anchor_age, gender, admission_type, admission_location, first_careunit, last_careunit, ICU duration`, and destination.

Destination is derived, without using `hosp/admissions.discharge_location` (which is the later hospital disposition), from `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, columns `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`. Select the first transfer row for the same `subject_id, hadm_id` whose `intime` is at or after index `outtime` and within six hours; save `careunit` and an unmatched category. Report matching diagnostics. This destination is a prognostic covariate/stratum, not an intervention.

## Outcomes and competing risks

Follow from index ICU `outtime), ending at the earliest of the horizon, hospital `dischtime`, a first event, or loss of valid event timing.

Primary horizon: 48 hours. Secondary horizon: 7 days.

Cause 1, ICU readmission: the first later row in `icu/icustays` for the same `subject_id, hadm_id` with `intime > index outtime` and `intime <= outtime + horizon`. Use its `intime` as event time. The tables do not reliably encode planned versus unplanned returns; the primary event is therefore “any subsequent ICU admission.” Report a sensitivity excluding returns with an explicitly prespecified procedural/transfer pattern only if that pattern is validated from available fields; do not claim an unplanned-readmission estimate without adjudication.

Cause 2, death before readmission: `hosp/admissions.deathtime > outtime`, within the horizon, and earlier than the first later ICU `intime`. This is ward/hospital death as a competing first event. If death follows a readmission, it is not cause 2; report subsequent death descriptively.

Censor at alive hospital `dischtime` before the horizon. If `hospital_expire_flag=1` but `deathtime` is missing, mark event ordering unresolved and exclude that record from the primary timed competing-risk analysis; report its count and a sensitivity that treats death as occurring at `dischtime` only when no later ICU admission is recorded. This is an evidence limitation, not a hidden imputation. Also report deaths identified by `deathtime` and `hospital_expire_flag` separately.

The estimand is the cause-specific cumulative incidence of first ICU readmission and first death by 48 hours/7 days under the observed discharge process, conditional on the defined index population and covariates. The overall “failed transition” probability is the sum of the two CIFs, but causes must always be shown separately.

## Analysis

Fit the interpretable baseline as a regularized pooled-logistic discrete-time competing-risk model with one row per person-bin, interval fixed effects, and cause-specific hazards for readmission and death. Use a small prespecified interaction set (SpO2×FiO2 and support×device), with coefficients and missingness effects retained. Convert predicted hazards to CIFs.

Fit the learned alternative as a one-layer 64-unit GRU-D-style encoder over the four 6-hour bins, with mask and delta-time channels, dropout 0.1, and two cause-specific hazard heads at each bin. Optimize the discrete-time competing-risk negative log likelihood with early stopping on validation loss. Use the exact same inputs/domains and covariates available to the baseline; the difference is ordered history, not extra data. No tuning on the test set.

Split by `subject_id`: deterministic 70/15/15 train/validation/test, with five fixed hash seeds as a robustness analysis. Standardization, device mapping, and imputation parameters are learned on training only. Save split manifests containing only internal IDs in derived workspace artifacts; do not publish source rows.

Primary comparison: paired test-set cause-specific Brier score at 48 hours for readmission and death, calibration intercept/slope and calibration plots, with a prespecified clinically meaningful benchmark of at least 0.005 absolute readmission Brier reduction without material death-calibration degradation. Treat the benchmark as an interpretation aid, not proof of utility. Secondary metrics: CIF calibration at 7 days, cause-specific AUROC/AUPRC, integrated Brier score, and decision-curve net benefit across thresholds chosen before test evaluation. Use 2,000 subject-level bootstrap replicates for paired 95% intervals; report all estimates, not only those favoring the hypothesis.

Sequence ablations: last-bin-only, time-order permutation, and removal of mask/delta-time channels. A trajectory claim requires improvement over the full baseline plus degradation under order permutation or last-bin-only ablation in the same held-out data. If improvement persists after order permutation, it is evidence for aggregate measurement/support information rather than trajectory ordering.

## Falsification and interpretation

Supportive results would be a reproducible held-out improvement in 48-hour readmission CIF calibration/Brier score over the baseline, with reasonable death calibration, and sequence ablations indicating that ordered persistence/recovery contributes. This supports prognostic information value and justifies prospective validation of monitoring-risk stratification; it does not show that delaying discharge or adding monitoring prevents events.

Adverse results include no improvement, worse calibration, unstable performance across subject splits, or no loss under order permutation. These falsify the specific claim that ordered final-day trajectories add useful information beyond last-state summaries, though residual instability may still be clinically real or poorly measured.

Inconclusive results include too few events, broad intervals crossing no effect, high missingness, poor destination linkage, unresolved death timing, or a sequence model that fails validation convergence. These do not prove absence of association; they require a larger/more complete dataset, better measurement ascertainment, or expert adjudication.

Computationally checkable claims are cohort counts, joins, window exclusion, item mapping, event-time ordering, model fitting, held-out metrics, calibration, uncertainty, and ablation behavior. Clinical claims that require additional evidence are whether returns were unplanned, whether treatment limitations or clinician intent caused discharge, whether an oxygen/device measurement represents actual support, whether a prediction changes clinician behavior safely, and whether a policy improves outcomes. The available data lack reliable treatment-intent/goals-of-care labels, functional readiness, bedside nursing assessment, and adjudicated plannedness. Retrospective association is not a causal discharge-policy effect.

## Availability and provenance limits

The exact source catalog is `[internal dataset path]`, catalog [source checksum]. MIMIC metadata records deidentified subject-specific time shifts, and the source README identifies all table relationships and archive members. The configured snapshot includes radiology reports but not MIMIC-CXR images or raw waveforms. All source files remain read-only; derived tables, split manifests, checkpoints, metrics, and logs belong in the workspace.

This is a bounded adaptation informed by the inspected research-ambition methods guide and dataset documentation. It is not a reproduction of any demonstration or prior paper.
