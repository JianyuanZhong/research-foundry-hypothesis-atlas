# Episode 7 generation: residual instability at ICU discharge

Status: candidate-ready competing MIMIC-IV design; no cohort scan, model fit, or scientific result was run. This is a distinct discharge-instability question, not a mechanical repair of the inherited discordant-AKI design.

## Decision and scientific opening

The inherited candidate ([prior hypothesis]) is the stronger current anchor for the AKI direction. Its separate hospital-death and ICU-recorded-RRT estimands address a concrete ascertainment flaw and retain explicit severity and observation-process checks. A distinct discharge-instability experiment remains worthwhile because it asks a different clinical question: can clinicians recognize residual physiologic risk at the moment of ICU discharge, before readmission or inpatient death?

The closest inspected evidence supports only a bounded opening. [K1] reports a single-center surgical cohort in which post-ICU-transfer vital/laboratory flags were associated with ICU readmission or death within 48 hours; this supports near-term prognostic signal, not a MIMIC discharge phenotype, independence from destination, or benefit from monitoring. [K2] compares associative and causal-fused AI for MIMIC-IV ICU readmission prediction, showing why predictive discrimination and causal/actionable interpretation must be separated; its causal claims do not supply valid treatment-intent data for this proposal. [K3] links post-ICU discharge dependency and respiratory-support indicators with long-term mortality in a small, single-center cohort of ICU survivors aged 80+, but it does not establish a short-term, multi-domain instability contrast or generalize to MIMIC.

Unresolved claim:

> Among adults alive at an index ICU discharge, does persistent multi-domain physiologic instability observed strictly in the final 24 hours identify higher 48-hour risk of first ICU readmission or hospital death, after accounting for observation opportunity and describing (not causally adjusting away) immediate discharge destination?

Primary hypothesis: patients with at least two persistent abnormal domains, including respiratory/oxygen support when present, have higher 48-hour cumulative incidence of the composite readmission-or-death than patients with no persistent domain, with a reproducible signal in adequately observed patients and across destination strata.

This is a prognostic association. It does not test whether delaying discharge, increasing monitoring, changing oxygen, or any other intervention improves outcomes. The clinically consequential decision it could inform is whether a discharge-time warning phenotype merits prospective bedside adjudication and intervention testing.

## Leading explanations and falsification

The leading explanation is residual physiologic instability: abnormalities persist within destination strata, in observation-complete patients, and for both readmission and death components.

The strongest rivals have distinct predictions:

- Destination/selection: the contrast is concentrated in specific immediate care units or discharge locations and attenuates after destination-stratified standardization. Destination is post-landmark selection, so this is descriptive, not causal adjustment.
- Residual severity: the contrast disappears within prespecified strata of pre-window creatinine, lactate, hemoglobin, platelet/WBC/glucose, ICU length/timing, and support/procedure intensity.
- Observation process: instability is more common in dense monitoring, and a non-instability documentation-density gradient is comparable; an apparent signal then may reflect surveillance/acuity.
- Treatment limitation: death is concentrated among patients with goals-of-care limits. No reliable structured treatment-limitation field is verified in this snapshot; destination, discharge_location, hospital_expire_flag, or death cannot substitute.
- Measurement meaning: oxygen flow/FiO2 can reflect chronic support or planned weaning rather than hypoxemia; structured MIMIC fields do not establish work of breathing, home oxygen, clinician intent, or respiratory failure.

Supportive results establish only a replicable prognostic association. Adverse results include disappearance after observation/destination/severity checks, a process-only gradient of similar size, a signal only for oxygen support but not physiologic abnormalities, or readmission/death divergence inconsistent with the composite. These weaken the physiologic interpretation. Inconclusive results include sparse events, a large unknown state, dictionary/unit mismatch, or intervals that cannot exclude a clinically material effect.

## Actual scientific deliverable

The future Harbor solver must newly construct and save:

1. A flow from adult first ICU stay through alive discharge, classifiable exposure, and each first event; include deaths at/before discharge, missing opportunities, unknown exposure, and every destination.
2. A dictionary and unit audit for all exposure itemids, with invalid-value counts and source/catalog hashes.
3. Four prespecified exposure states: stable/no persistent domain, one persistent domain, at least two persistent domains, and unknown/insufficient observation. Report oxygen-support and physiologic components separately.
4. At 48 hours after ICU outtime, Aalen-Johansen cumulative incidence for first ICU readmission, hospital death, alive hospital discharge, and event-free status; report absolute risk differences for the primary composite and components, with bootstrap uncertainty.
5. Predeclared destination strata, severity strata, observation-density quartiles, adjacent-bin volatility, at-least-1/3-bin and all-4-bin sensitivities, and the process-only falsification table.
6. A transparent fixed-summary competing-risk baseline and a learned temporal alternative evaluated on identical held-out people, with calibration, cause-specific Brier score, discrimination as secondary, and phenotype-specific risk contrasts.
7. A manifest linking each estimate to the data fields, cutoff, risk set, competing-event rule, split, model, counts, uncertainty, and interpretation.

Completion requires computed outputs and linked uncertainty; readiness or a favorable model score is not completion.

## Population, time windows, and estimands

Unit: one adult hospital admission with the earliest valid ICU stay for that admission.

- From `hosp/patients`, retain `anchor_age >= 18`; join on `subject_id`.
- From `icu/icustays`, require `intime < outtime`, then select the smallest `intime` per `(subject_id, hadm_id)`. Let `t_d = icustays.outtime`.
- Join `icu/icustays` to `hosp/admissions` on `(subject_id, hadm_id)`. Retain patients not dead at or before `t_d`: `deathtime` null or `deathtime > t_d`. Do not require survival after discharge.
- Every immediate destination is retained, including ward, intermediate/step-down, hospice/palliative, and unknown. Do not restrict the primary cohort to non-ICU transfers.
- Primary exposure window is the half-open `[t_d - 24 hours, t_d)`, divided into four 6-hour bins. A value at `t_d` or later is excluded. `charttime` is the clinical time; `storetime` is only a documentation-lag sensitivity.
- A classifiable primary exposure requires a valid core observation in at least 3 of 4 bins. Missing is unknown, never normal. Report at-least-2 and all-4-bin sensitivities without changing thresholds after outcome inspection.

Primary estimand: among adults alive at the observed ICU-discharge landmark with classifiable exposure, the standardized 48-hour risk difference for first ICU readmission or hospital death between at-least-two persistent domains and stable/no persistent domain. This is conditional on surviving to ICU discharge and on observed classifiability; it is not an onset-cohort, discharge-policy effect, or causal effect.

Outcome window is `[t_d, t_d + 48 hours)):

- First ICU readmission: later `icu/icustays.intime` for the same `(subject_id, hadm_id)`, with `intime >= t_d` and `intime < t_d+48h`; exclude the index stay.
- Hospital death: `hosp/admissions.deathtime` in the same window.
- Alive hospital discharge: `hosp/admissions.dischtime` in the window, only if no earlier death/readmission; competing event for observed in-hospital readmission.
- Event-free at 48 hours: alive, no readmission, and not discharged before the boundary.

Assign a first event by earliest clinical timestamp. Ties between death and readmission are retained as integrity flags and handled in a prespecified sensitivity. Report the composite, components, and competing discharge separately. Use Aalen-Johansen descriptive CIFs and 6-hour cause-specific discrete-time hazards for readmission, death, and alive discharge, standardized over the observed risk set. Treat post-discharge readmission outside the same admission as unavailable, not as an assumed outcome.

## Exact exposure and data bindings

The read-only source is `[internal dataset path]`, MIMIC-IV 3.1 snapshot `[source checksum]`, [source checksum]. The full catalog is `[internal dataset path]`, [source checksum]. These source paths are read-only; only derived files in this branch are writable.

Required schema bindings (the frozen JSON schemas were inspected and a bounded source-header audit read each listed archive header; audit output hash [source checksum]):

| Purpose | table and archive member | exact columns used / join and time |
|---|---|---|
| Index ICU | `icu/icustays`; `mimic-iv-3.1/icu/icustays.csv.gz`; schema `datasets/mimic/table-7d5c8feb0fb0dbd4.json` | `subject_id, hadm_id, stay_id, intime, outtime, first_careunit, last_careunit, los`; earliest `intime` per `(subject_id,hadm_id)`; `intime/outtime` |
| Admission outcomes/destination | `hosp/admissions`; `mimic-iv-3.1/hosp/admissions.csv.gz`; `table-e8ec3e6e4c428559.json` | `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, discharge_location, hospital_expire_flag`; join `(subject_id,hadm_id)`; `admittime/dischtime/deathtime` |
| Demographics | `hosp/patients`; `mimic-iv-3.1/hosp/patients.csv.gz`; `table-9154f8c46cade9af.json` | `subject_id, gender, anchor_age, dod`; join `subject_id` |
| Immediate destination | `hosp/transfers`; `mimic-iv-3.1/hosp/transfers.csv.gz`; `table-685b6b74d0d7c547.json` | `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; first row with `intime >= t_d`, join `(subject_id,hadm_id)` |
| Vitals/oxygen | `icu/chartevents`; `mimic-iv-3.1/icu/chartevents.csv.gz`; `table-8208609a785ea7e8.json` | `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom, warning`; join `stay_id`, clinical time `charttime` |
| Item dictionary | `icu/d_items`; `mimic-iv-3.1/icu/d_items.csv.gz`; `table-d1023acc404fd1d4.json` | `itemid, label, abbreviation, linksto, category, unitname, param_type, lownormalvalue, highnormalvalue`; readiness verifies labels/units |
| Severity labs | `hosp/labevents`; `mimic-iv-3.1/hosp/labevents.csv.gz`; `table-bf701d962c63287c.json` | `labevent_id, subject_id, hadm_id, itemid, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag`; join `(subject_id,hadm_id)` and pre-`t_d` `charttime` |
| Lab dictionary | `hosp/d_labitems`; `mimic-iv-3.1/hosp/d_labitems.csv.gz`; `table-57ae65f0eb6cf1a6.json` | `itemid, label, fluid, category`; verifies creatinine 50912 and all selected labs |
| Support/procedure opportunity | `icu/procedureevents`; `mimic-iv-3.1/icu/procedureevents.csv.gz`; `table-f6493e8403a0abe7.json` | `subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, value, valueuom, ordercategoryname, ordercategorydescription, statusdescription`; pre-`t_d` support markers |
| Observation opportunity | `icu/inputevents`; `mimic-iv-3.1/icu/inputevents.csv.gz`; `table-d193e854c19eb4ba.json` | `subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom, totalamount, totalamountuom, statusdescription`; counts only, no post-`t_d` predictors |
| Urine/opportunity | `icu/outputevents`; `mimic-iv-3.1/icu/outputevents.csv.gz`; `table-a7ad1c4cdcdbfe0a.json` | `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom`; counts only, pre-`t_d` |
| Evidence boundary | `note/discharge`; ordinary file `[internal dataset path]`; `table-69be322e2b58015b.json` | `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; excluded from predictors because it may be written after `t_d` |
| Evidence boundary | `note/discharge_detail`; ordinary file `[internal dataset path]`; `table-18d43f38e33d1fd2.json` | `note_id, subject_id, field_name, field_value, field_ordinal`; not used as a verified treatment-limitation field |

Primary chart item set, audited by `icu/d_items` at readiness:

- 220045 Heart Rate; 220052 Arterial Blood Pressure mean; 220210 Respiratory Rate; 220277 O2 saturation pulseoxymetry.
- 223834 O2 Flow; 223835 Inspired O2 Fraction; 223761 Temperature Fahrenheit; 223762 Temperature Celsius.
- 226732 O2 Delivery Device(s) is descriptive/device sensitivity only.

For each 6-hour bin use the median of vital signs and maximum oxygen flow/FiO2. Convert Fahrenheit to Celsius. A domain is persistent when flagged in at least 2 of 4 bins:

- Respiratory/oxygen: SpO2 <92%, O2 Flow >0 L/min, or FiO2 >0.21.
- Hemodynamic: MAP <65 mmHg, heart rate >100 or <50 beats/min.
- Ventilatory pattern: respiratory rate >24 or <8 breaths/min.
- Temperature: <36.0 or >38.3 Celsius.

Do not call oxygen support respiratory failure. Do not impute missing bins. Report oxygen-support and measured-hypoxemia components separately. The primary contrast is at least two persistent domains versus stable/no persistent domain; retain one-domain and unknown states in all flows.

## Baseline versus learned temporal alternative

The baseline is an auditable fixed-summary competing-risk analysis on the same risk set: persistent-domain state, last/median/min/max/slope of each final-24-hour channel, adjacent-bin changes, pre-window severity labs (creatinine 50912, lactate, hemoglobin, platelet, WBC, glucose after `d_labitems` verification), age/sex/admission type, ICU timing/LOS, procedure/support markers, and observation counts. Fit separate 6-hour cause-specific logistic hazards for readmission, death, and alive discharge; standardize 48-hour CIFs and risk differences. Report unadjusted and severity/observation strata. A destination-stratified descriptive sensitivity includes immediate `transfers.careunit`, while keeping it out of the primary pre-landmark model.

The learned alternative uses the same final-24-hour boundary and subject-level split: 12 two-hour bins, the eight numeric physiologic channels, missingness masks, elapsed time, observation counts, domain flags, and pre-window static severity. Use a small GRU with separate hazard heads for ICU readmission, death, and alive discharge. Fix a 70/15/15 train/validation/test split by `subject_id`, training-only normalization, and at most three prespecified random seeds. Primary evaluation is held-out 48-hour cause-specific Brier score and calibration; AUROC/AUPRC are secondary. Compare both models on identical test subjects and report the same phenotype-specific CIF contrast with bootstrap uncertainty.

The learned model can reveal persistence, volatility, and informative missingness that fixed summaries lose. The baseline reveals whether a clinically legible state contrast survives competing-event accounting and is primary for interpretation. Prediction improvement without a stable, destination/observation-robust phenotype contrast is predictive utility only, not evidence of a discharge policy or mechanism. A complex causal-fused model is deferred because treatment limitation, discharge rationale, and a valid intervention are unavailable.

Planning estimate, not an executed result: derived-table construction and baseline are CPU work (2–4 CPUs, 8–16 GiB after materialization); the small GRU is approximately 2–4 CPUs and 8–16 GiB, or one allocated A100 if a bounded probe shows benefit. Future solver envelope must be checked against `inputs.json` (`science_seconds=9000`, compute concurrency 2, GPU slots 2); ordinary shell CUDA is not evidence of hardware absence. No GPU is required for this discovery proposal, and no proposer/solver training is authorized. The header audit job is a readiness check, not a study result.

## Unavailable evidence and non-reproduction boundary

MIMIC-IV snapshot does not provide verified clinician goals-of-care/treatment-limitation intent, the rationale and availability timing of the ICU discharge decision, bedside work of breathing, chronic/home oxygen, complete ward observation, post-discharge readmission outside the same hospital admission, or a gold standard for respiratory failure. Discharge notes exist but can be charted after the landmark and are excluded; narrative review would require blinded clinical adjudication not available here. Destination and hospital death are outcomes/selection markers, not substitutes for treatment limitation. MIMIC cannot establish that a warning would improve care, nor transportability or causal effects.

The design is a bounded adaptation, not a reproduction of [K1]–[K3] or any demonstration paper. The three demonstrations in `references/research-ambition/README.md` and their method guide were inspected as examples: Delphi motivates a possible dated sequence adaptation but does not require a transformer or GPU; ALADYNOULLI demonstrates longitudinal latent modeling but missing genetic inputs and mechanism claims do not transfer; Oncoformer’s full main paper/STAR Methods are unavailable and images are absent, so no multimodal reproduction is claimed. The learned GRU is selected because it is matched to this question and data, not because complexity is inherently valuable.

## Alternatives not chosen and selection/deferral rule

- Further AKI-recovery repair is the preferred current direction: its key remaining question is ascertainment validity with better-separated outcome clocks, while this discharge design cannot resolve treatment limitation and destination selection.
- The composite readmission-or-death alone is insufficient; components and competing discharge are mandatory.
- Conditioning the primary cohort on a particular non-ICU destination is rejected because it changes the population and bakes selection into the estimate.
- Notes or a post-discharge text model are excluded because note timing can leak future information and treatment-limitation adjudication is unavailable.
- Causal-fused or treatment-effect modeling is deferred; no reliable intervention, intent, or exchangeability data exist.
- A transformer or large sequence model is deferred; it would add capacity without resolving the central rivals.
- If dictionary audit or event support fails, stop this direction. If support is adequate but destination/observation stratification leaves wide uncertainty, retain it as an inconclusive descriptive study and seek prospective adjudication. If the signal survives, continue to external/clinical validation. If the process-only gradient dominates, abandon the physiologic interpretation while retaining a documentation/acuity finding.

## Key references

Exactly three distinct inspected works are mapped below and attached as UTF-8 excerpts. [K1] is abstract-only; [K2] and [K3] are full-text XML inspections. These works support, challenge, or bound the proposed claim; none establishes it.

[K1] Rens NE, Rajotte JJ, Deng H, Meng J, Mueller AL, Houle TT, Wiener-Kronish JP, Safavi KC, Ruscic KJ. “Association of Vital Sign and Laboratory Abnormalities Detected via Remote Monitoring with ICU Readmission and Mortality: An Observational Cohort Study.” Joint Commission Journal on Quality and Patient Safety. 2026;52:177–186. doi:10.1016/j.jcjq.2026.02.001; PMID 41856853. Abstract-only inspection via Europe PMC metadata/abstract response; full text was not read for this proposal.

[K2] Remoundou K, Koumantakis E, Roussaki I. “Mitigating Clinical Confounding in AI Models: A Comparative Analysis of Associative and Causal-Fused AI for ICU Readmissions.” Healthcare (Basel). 2026;14(14):2067. doi:10.3390/healthcare14142067; PMCID PMC13409962. Full-text XML inspection, especially abstract and introduction; the proposal uses it only to bound predictive-versus-causal interpretation.

[K3] Gülen D, Ekin S, Özyaprak B, Ceylan I. “One-Year Outcomes After ICU Discharge in Patients Aged 80 Years and Older: Functional and Clinical Factors Associated with Mortality in a Retrospective Observational Cohort.” Journal of Clinical Medicine. 2026;15(14):5324. doi:10.3390/jcm15145324; PMCID PMC13410107. Full-text XML inspection, especially abstract and introduction; small single-center cohort, long-term outcome, and not a direct replication.

## Readiness evidence and honest status

Inspected: `datasets/README.md`, `datasets/mimic/README.md`, the full MIMIC table catalog entries used above, `references/research-ambition/README.md`, and `methods-and-compute.md`; the inherited candidate proposal and its assessment; and the three key-work responses identified in `key-references.json`. A managed, bounded archive-header audit confirmed presence and exact headers for every listed structured member; its output is `source-header-audit.txt` ([source checksum]) and is not a scientific result. The source archive and ordinary note files are listed with hashes in the dataset guide. No rows, cohort counts, fitted parameters, or study conclusions were computed in this branch.

## Attached files

- `key-references.json`
- `evidence-rens-2026.txt`
- `evidence-remoundou-2026.txt`
- `evidence-gulen-2026.txt`
- `source-header-audit.txt` (readiness-only header audit; no cohort results)
