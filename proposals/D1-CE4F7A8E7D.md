# Red-cell transfusion under observed oxygen-supply/demand stress: a noncausal MIMIC-IV experiment

## Status and deliverable

This is a substantive, data-bound child of imported expert seed [prior hypothesis] / [starting question]. It preserves the seed question—whether the observed relationship between red-cell transfusion and subsequent deterioration differs at similar hemoglobin when a patient has oxygen supply/demand stress—but makes no causal or ischemia claim.

No prevalence, fitted result, effect estimate, or clinical conclusion is claimed. The future Harbor solver must produce an auditable cohort flow, record-defined stress phenotype, treatment/outcome table, transparent baseline and chronological learned-model predictions, standardized observed-risk contrasts by stress state, uncertainty, support/overlap diagnostics, falsifications, and a conclusion ledger linking claims to outputs.

## Unresolved question and evidence boundary

The strongest supported claim is only that transfusion decisions may have different clinical meaning at similar hemoglobin in physiologically stressed versus apparently stable patients, while indication confounding and incomplete ischemia measurement are serious threats. The seed is not evidence for effect modification.

The falsifiable claim is:

> Among adult ICU decision episodes with hemoglobin 6.5–8.0 g/dL and no prior red-cell exposure in the preceding 12 hours, is the adjusted observed 24-hour deterioration association for receiving PRBC within the next 6 hours different between record-defined low-stress and high observed oxygen-supply/demand-stress strata, after conditioning on the same pre-decision physiology, severity, bleeding proxies, care context and observation intensity?

The primary estimand is explicitly a noncausal standardized association. For stress stratum s, let Delta_s equal the observed-outcome risk fitted with T=1 minus the observed-outcome risk fitted with T=0, both standardized to the measured covariate distribution in s. H = Delta_high - Delta_low is the heterogeneity contrast. It is not a counterfactual treatment effect and must not be described as transfusion benefit, harm, appropriateness, or ischemia-specific effect.

The substantive advance over hemoglobin-only work is to test whether the observed association varies by a prespecified physiologic context, with the same treatment definition and adjustment set in both strata. A robust null is clinically useful: it would argue against using these available EHR proxies to enrich or stratify a future transfusion trial.

## Cohort and time zero

Use MIMIC-IV 3.1, one row per adult ICU stay and first qualifying decision episode.

Start with icu/icustays: subject_id, hadm_id, stay_id, intime, outtime, first_careunit, last_careunit, los. Join hosp/admissions on subject_id, hadm_id for admittime, dischtime, deathtime, admission_type, discharge_location and hospital_expire_flag; join hosp/patients on subject_id for gender, anchor_age and anchor_year_group. Keep age >=18; report age 91 as MIMIC's >89 representation.

Use the first ICU stay in each hospitalization with a qualifying hemoglobin and at least 18 hours remaining before outtime or in-hospital death. The first hemoglobin in that stay meeting the rule below defines t0. A patient contributes at most one episode.

Require a primary hemoglobin 6.5–8.0 g/dL from hosp/labevents item 51222 (Hemoglobin, Blood, Hematology), using charttime as clinical time and storetime <= t0 as availability. The sensitivity source is item 50811 (Hemoglobin, Blood, Blood Gas). In the six-hour pre-t0 window use the nearest valid result; ties use latest charttime then smallest labevent_id.

Exclude a PRBC record in the previous 12 hours, a PRBC administration already in progress at t0, and episodes lacking a complete six-hour treatment ascertainment window. Episodes exiting ICU or dying during that window are treatment-window censored and reported, not silently assigned T=0. Exclude a record-defined major-bleeding proxy before t0: procedureevents item 229620 (Massive Transfusion), PRBC volume >=2,000 mL in the prior six hours, or an active operative/trauma procedure from a frozen hosp/procedures_icd code list. Do not call the remainder nonbleeding; call it no observed major-bleeding proxy. A sensitivity retains the proxy-positive episodes.

Time zero is the hemoglobin charttime, not transfusion start. Every feature must have clinical time <=t0 and recording time <=t0. All windows are within-subject relative windows because MIMIC timestamps are subject-shifted; raw cross-subject calendar comparisons are invalid.

## Treatment

T=1 if any PRBC administration starts in [t0,t0+6h) in icu/inputevents item IDs 220996 (Packed Red Cells), 225168 (Packed Red Blood Cells), 226368 (OR Packed RBC Intake), or 227070 (PACU Packed RBC Intake). Require starttime in the window and audit endtime, amount, amountuom, rate, totalamount, statusdescription and order fields. Cancelled or discontinued orders without administration-compatible status are not counted. The primary exposure is any start; sensitivity exposures are >=1,000 mL recorded PRBC and first-start-only. FFP, platelets and autotransfusion are not PRBC exposure.

This resembles a six-hour target-trial decision episode but remains observational. MIMIC does not measure clinician intent, blood availability, refusal, exact indication, completed-unit status or treatment contamination. A secondary target-trial-like table may be reported, but no per-protocol or intention-to-treat causal language is permitted.

## Record-defined stress phenotype

Use a pre-t0 12-hour window, requiring clinical and store time <=t0. Build separate supply and demand/support components.

Supply evidence includes lactate >=2 mmol/L from hosp/labevents items 50813, 52442 or 53154; MAP <65 from icu/chartevents items 220052 or 220181; active vasoactive input from icu/inputevents items 221289/229617 epinephrine, 221653 dobutamine, 221749/229630/229631/229632 phenylephrine, 221906 norepinephrine, 221986 milrinone and 222315 vasopressin; troponin items 51002, 51003 or 52642 only if positivity can be harmonized using local units/reference ranges; and low arterial oxygen evidence from labevents 50821/50817 or chartevents 220227/220277, interpreted with support context.

Demand/respiratory evidence includes HR 220045 >=110, RR 220210 >=24, oxygen flow 223834, FiO2 223835, PEEP 220339, ventilator type/mode 223848/223849, and procedureevents 225792 invasive or 225794 non-invasive ventilation.

Primary high observed stress requires at least one supply component and one demand/support component, or two independent supply components. Low observed stress is the absence of those rules with adequate coverage. Indeterminate/insufficient coverage is retained in the flow and excluded from the primary contrast after an endpoint-independent gate; a sensitivity treats it as a third category. Thresholds, units, and item validity are frozen before outcomes are inspected.

This is an EHR stress proxy, not myocardial ischemia, tissue hypoxia, microcirculatory failure, or a measured oxygen-delivery/consumption imbalance. Report each component separately so the composite cannot conceal which signal drives the result.

## Covariates and outcomes

Pre-t0 adjustment includes hemoglobin, lactate, MAP, HR, RR, SpO2/SaO2, pO2, FiO2/O2 flow, PEEP/support, vasoactive exposure, recent input totals, creatinine 50912/52546, platelet 51265/53189, INR 51237/51675, pH 50820 and bicarbonate 50882 when dictionary/unit checks pass; missingness and time-since-last-observation; age, sex, anchor_year_group, admission type, first/last care unit, time since intime, hospital day and prior ICU/hospitalization count; diagnosis/procedure proxies for infection, cardiac/respiratory disease, surgery and bleeding; transfer context; and counts of labs, vitals and support records in the 12-hour window. No post-t0 variable is adjusted for. Text is excluded from the primary model.

Primary Y is any event in (t0,t0+24h]: death, new invasive ventilation, new vasoactive support, or new renal replacement therapy. Death uses admissions deathtime or compatible expiry. New support requires absence in the pre-t0 six-hour window and a post-t0 start. Ventilation uses procedureevents 224385 intubation or 225792 invasive ventilation. Renal replacement uses procedureevents 225441 hemodialysis, 225802 CRRT, 225803 CVVHD, 225809 CVVHDF, 225955 SCUF or 225805 peritoneal dialysis. Vasoactive starts use the listed pressor items. Death supersedes simultaneous nonfatal support in mutually exclusive tables.

Secondary outcomes are death, invasive ventilation, vasoactive support and renal replacement separately, a 48-hour repeat composite, and first-event competing-risk categories: death, nonfatal escalation, ICU exit/readmission before 24 hours, or no observed event. ICU exit is an ascertainment limitation, not recovery.

Report crude rates, adjusted standardized Delta_s and H, two-sided 95% intervals, calibration and overlap. No automatic verifier should treat an observed contrast as clinical adjudication or causality.

## Matched methods

B0 is a penalized logistic model for observed 24-hour Y with treatment, stress, treatment-by-stress interaction, spline hemoglobin, the adjustment blocks, missingness and observation intensity. Separate cause-specific models are sensitivity analyses.

M1 is a masked chronological GRU, or gated temporal convolution if GRU is unavailable, over twelve one-hour bins of exactly the same selected streams, masks and time-since-observation channels. Treatment is a separate label token; two heads predict observed outcomes under the two labels, and their standardized difference remains noncausal. M1 can expose persistence, ordering, irregular sampling and joint trajectories lost by B0's aggregate summaries, but cannot recover unrecorded intent or true ischemia. Compare both on the same subject-level 60/20/20 split: held-out Brier score and calibration slope/intercept primary, AUROC/AUPRC secondary, and stability of H. A small predictive gain is not itself clinical value.

Use 2,000 subject-level bootstrap replicates for held-out prediction contrasts, with any reduced refit sensitivity predeclared. Never bootstrap rows independently. Require before interpretation: >=50 treated and >=50 untreated episodes per stress stratum; >=20 primary events per treatment-by-stress cell; propensity overlap >=0.05 after trimming; effective sample size >=100 per cell; and adjusted standardized mean difference <=0.25. If a gate fails, the corresponding estimand is not estimable and only descriptive results are reported. Do not merge strata or move thresholds to rescue support.

## Falsification and interpretation

Run within hemoglobin/care-unit/anchor-year strata treatment-label permutations; shift exposure labels 24 hours earlier; replace stress by measurement intensity alone; ablate lactate/troponin and separately ablate treatment/process variables; test non-RBC blood-product exposure and an unrelated near-term procedure as negative controls; and repeat using blood-gas hemoglobin, 7.0–8.0 g/dL, excluding OR/PACU PRBC IDs, and excluding troponin. Assess care unit, anchor-year, hospital-day and observation-intensity stability.

Supportive means a stable interaction across B0 and M1, adequate support, calibration, and no comparable process/negative-control interaction. It supports a prospective silent-mode validation or randomized trial enrichment hypothesis only. Adverse means no interaction, opposing model directions, or explanation by observation intensity/bleeding/pressor recording; this argues against this MIMIC proxy as a reliable stratifier, not against biological effect heterogeneity. Inconclusive means failed coverage, overlap, event or coding gates; it requires better measurement or prospective adjudication rather than model escalation.

## Exact bindings and limitations

Source archive: [internal dataset path], configured source [source checksum]; dataset snapshot [source checksum].

The required archive members and schemas are:

- icu/inputevents.csv.gz, table-d193e854c19eb4ba.json: subject_id/hadm_id/stay_id, starttime/endtime/storetime, itemid, amounts, units, status and order fields.
- hosp/labevents.csv.gz, table-bf701d962c63287c.json: subject_id/hadm_id, itemid, charttime/storetime, value/valuenum/valueuom, flags and reference ranges.
- hosp/d_labitems.csv.gz, table-57ae65f0eb6cf1a6.json: itemid, label, fluid and category.
- icu/chartevents.csv.gz, table-8208609a785ea7e8.json: subject_id/hadm_id/stay_id, charttime/storetime, itemid, value/valuenum/valueuom.
- icu/d_items.csv.gz, table-d1023acc404fd1d4.json: itemid, label, linksto, category, unitname, param_type and normal ranges.
- icu/procedureevents.csv.gz, table-f6493e8403a0abe7.json: stay keys, starttime/endtime/storetime, itemid, value and status/order fields.
- icu/icustays.csv.gz, table-7d5c8feb0fb0dbd4.json; hosp/admissions.csv.gz, table-e8ec3e6e4c428559.json; hosp/patients.csv.gz, table-9154f8c46cade9af.json; hosp/transfers.csv.gz, table-685b6b74d0d7c547.json.
- hosp/diagnoses_icd.csv.gz, table-b12f3369d4b2601b.json, and hosp/procedures_icd.csv.gz, table-c4d6d5363d8de8c7.json for frozen codes.
- hosp/emar.csv.gz, table-3e9915414fcfc36b.json, is a sensitivity source keyed by subject_id/hadm_id with charttime, scheduletime, storetime, medication and event_txt; it is not the primary exposure.
- note/discharge.csv.gz, table-69be322e2b58015b.json, is available but excluded from the primary design.

MIMIC lacks clinician intent, complete bleeding adjudication, bedside examination, ECG interpretation, echo/cardiac-output context, direct oxygen delivery/consumption, ischemia adjudication, blood availability/refusal, completed-unit verification, randomized assignment and complete post-ICU outcome ascertainment. MIMIC-CXR images and raw waveforms are not in the configured snapshot. The dataset metadata records subject-shifted timestamps and unavailable modalities. Thus this experiment cannot establish ischemia, causal benefit/harm, appropriateness or current-practice transportability.

## Compute and selection

Streaming extraction over the 10.6-GB archive and B0 fit are CPU-first. The future solver planning envelope is 16 CPUs, 262144 MiB, up to 8 GPUs and 28800 seconds; these are planning limits, not measured runtime. M1 should begin with a bounded CPU pilot; if runtime materially exceeds the envelope, use one allocated A100 and cuda:0 in the cached GPU image. No GPU is required or rewarded. Current discovery audited schemas/item support but did not fit either model.

A causal g-formula/TMLE analysis is deferred because intent, time-varying confounding, censoring and support are not verified; it would require a new Lead estimand decision. A text model is deferred because local text extraction is not a validated ischemia/indication adjudicator. Select this candidate only if the solver can report the noncausal H estimand and gates; preserve a failed-gate result as informative rather than altering the scientific question.
