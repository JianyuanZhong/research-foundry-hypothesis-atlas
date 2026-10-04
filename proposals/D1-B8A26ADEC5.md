> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: discordant AKI recovery in MIMIC-IV

Status: provisional repair draft. No cohort counts, model fits, or clinical results are claimed.

## Proposed relationship

Among adults in their first MIMIC-IV ICU stay with a documented creatinine-based AKI episode and adequate pre-landmark urine-output monitoring, a creatinine-improved but urine-output-impaired phenotype is associated with worse subsequent in-hospital death and/or persistent or worsening kidney dysfunction than concordant creatinine-and-urine-output recovery. This is a prognostic association, not a causal or mechanistic claim.

The principal rival explanation is measurement/monitoring artifact: creatinine sampling is clinician-selected, urine output depends on catheterization or bedside collection, and fluid balance is a treatment/monitoring summary. The study must therefore include monitoring intensity and treatment proxies and must not infer tubular injury, fluid overload, or treatment benefit from association.

## Evidence boundary and unresolved question

The inherited branch supplies a concrete MIMIC-IV ZIP binding and verified archive members, but it does not establish that discordant recovery is clinically meaningful, nor that the proposed association is present. The unresolved claim is whether discordance adds prognostic information after accounting for severity, creatinine trajectory, monitoring, and treatment proxies. A supportive result would be a prespecified incremental association with uncertainty that persists under monitoring-adjusted and fixed sensitivity analyses. An adverse result would be no incremental association, disappearance after monitoring adjustment, or reversal. An imprecise null is inconclusive. True AKI, recovery, fluid overload, and treatment indication require clinical adjudication unavailable from these tables.

## Exact source binding

Read-only source: `[internal dataset path]`
Catalog: `[internal dataset path]`
Catalog [source checksum].

Required members and joins:
- `mimic-iv-3.1/icu/icustays.csv.gz` (catalog `icu/icustays`): `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; join `stay_id` to ICU events and `subject_id,hadm_id` to hospital tables. Time origin is `intime`; ICU discharge is `outtime`.
- `mimic-iv-3.1/hosp/admissions.csv.gz` (catalog `hosp/admissions`): `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; join `subject_id,hadm_id` to ICU. Outcomes use `dischtime`, `deathtime`, and `hospital_expire_flag`.
- `mimic-iv-3.1/hosp/patients.csv.gz` (catalog `hosp/patients`): `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; join `subject_id`. Adult age must use a fixed derivation from anchor age and ICU time; no row-level admission-age column is assumed.
- `mimic-iv-3.1/hosp/labevents.csv.gz` (catalog `hosp/labevents`): `labevent_id, subject_id, hadm_id, specimen_id, itemid, order_provider_id, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag, priority, comments`; join `subject_id,hadm_id`. Use `charttime` for clinical time and `storetime` for availability auditing; there is no `stay_id` in this table.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz` (catalog `hosp/d_labitems`): `itemid,label,fluid,category`; candidate serum creatinine IDs are 50912 and 52546, both labeled Creatinine, fluid Blood, category Chemistry. A prespecified audit of `valueuom`, numeric completeness, and temporal coverage is required before selection; urine/ascites/joint/pleural creatinine items are excluded.
- `mimic-iv-3.1/icu/outputevents.csv.gz` (catalog `icu/outputevents`): `subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom`; join `stay_id` to ICU and `subject_id,hadm_id` to admissions. Candidate urine-output items are 226559 Foley, 226560 Void, 226561 Condom Cath, 226563 Suprapubic, 226564 R Nephrostomy, 226565 L Nephrostomy, 226566 Urine and GU Irrigant Out, 226567 Straight Cath, 226627 OR Urine, and 226631 PACU Urine, with listed unit mL. Items 226557/226558 are ureteral-stent outputs and require a separate sensitivity category; text/estimated outputs are not numeric volumes. Missing output rows are not anuria.
- `mimic-iv-3.1/icu/inputevents.csv.gz` (catalog `icu/inputevents`): `subject_id, hadm_id, stay_id, caregiver_id, starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom, orderid, linkorderid, ordercategoryname, secondaryordercategoryname, ordercomponenttypedescription, ordercategorydescription, patientweight, totalamount, totalamountuom, isopenbag, continueinnextdept, statusdescription, originalamount, originalrate`; join `stay_id`. Use `starttime,endtime` for event intervals and `storetime` for availability. A fluid-balance whitelist must be frozen from `icu/d_items` by `linksto=inputevents`, category/label, `amountuom`, and numeric status, excluding medications, dialysis replacement/dialysate components, and non-fluid items unless separately defined.

## Population, timing, outcomes, and analysis

Population: adults in the first ICU stay per `subject_id`, with a documented creatinine-based AKI episode and sufficient pre-landmark urine-output monitoring. The AKI baseline/reference rule and numeric thresholds must be fixed before outcome analysis; a single post-landmark value cannot define AKI.

Primary landmark: 48 hours after ICU `intime`. Exposure construction uses only clinical timestamps at or before this landmark: creatinine trajectory, urine-output category/trajectory, and secondary fluid-balance category. Events after the landmark are excluded from exposure construction.

Primary comparison: creatinine-improved/urine-output-impaired versus concordant recovery. Secondary comparisons: discordance versus creatinine-improved/urine-output-recovered, and prespecified monitoring-stratified analyses.

Outcomes: in-hospital death through `admissions.dischtime`/`deathtime`, and a prespecified post-landmark kidney outcome (persistent/worsening creatinine and/or renal replacement therapy), with follow-up through hospital discharge or a fixed 7-day window and explicit competing-risk handling. Exact outcome thresholds and RRT item definition remain unresolved and must be fixed before fitting.

Simple baseline: prespecified logistic or cause-specific Cox model with age, sex, admission type, pre-landmark severity, creatinine value/trajectory, urine-output category, fluid-balance category, and monitoring intensity. It tests whether discordance adds interpretable prognostic information beyond creatinine recovery.

Substantive alternative: a time-aware landmark model using ordered pre-landmark creatinine, urine-output, and fluid-balance trajectories (discrete-time survival or regularized recurrent/functional model), with the same patient split, outcome, calibration, and uncertainty evaluation. It can reveal whether sequence and slope matter; it cannot establish mechanism. Compare incremental discrimination, calibration, and bootstrap uncertainty against the baseline. CPU is appropriate for the baseline; the alternative may use CPU or one allocated GPU only if trajectory fitting is materially slower.

## Coverage plan and limitations

Before fitting, run a bounded coverage audit: count eligible first ICU stays, creatinine item/unit coverage for 50912 versus 52546, pre-landmark urine-output item coverage and monitoring presence, and candidate fluid-input whitelist coverage. Report denominators, missingness, and timestamp distributions without interpreting them as clinical findings. Freeze inclusion/exclusion and all item rules before examining outcomes. Exact AKI/outcome definitions, RRT mapping, cohort/event coverage, and the required three inspected key-reference receipts remain unresolved. No result is claimed.
