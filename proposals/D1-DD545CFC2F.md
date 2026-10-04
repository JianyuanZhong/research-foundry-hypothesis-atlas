> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Residual instability before ICU-to-ward transfer: timing- and competing-state interpretation

Status: substantive child of `[prior hypothesis]`. No predictor model has been fit and no hypothesis result is claimed. The adult first ICU-to-frozen-general-ward-transfer population, `t0`, final-24-hour exposure, strict decision-time availability rules, fixed 48-hour target, primary S0-versus-T1 estimand, subject split, and exact MIMIC-IV 3.1 bindings are unchanged.

## Why this child is warranted

The parent correctly separates incremental prediction, materiality, signal source, and endpoint validity, but two remaining interpretation problems are consequential.

First, its fixed-horizon four-state analysis discards event timing. Live hospital discharge changes the opportunity to observe a same-admission ICU return, while ICU return and death occur throughout the 48-hour window. A single 48-hour class probability therefore cannot show whether trajectory information identifies early ward events, late events among patients still hospitalized, death rather than return, or discharge-selection patterns.

Second, threshold decision-curve net benefit is not demonstrated clinical utility. It assumes an exchange rate between false-positive and false-negative classifications and an available action, but MIMIC supplies neither intervention effect nor monitoring/ICU capacity, staffing, harm, cost, or actual contemporaneous occupancy. Subject-specific date shifting also prevents reconstructing real hospital-wide capacity at a calendar time. The study can test prognostic materiality and hypothetical prioritization under fixed quotas; it cannot show that delaying transfer, assigning monitoring, or retaining an ICU bed benefits patients.

A bounded chronology audit supports, but does not answer, this concern. In the unchanged 49,157-transfer cohort it reproduced 2,002 ICU returns and 661 deaths within 48 hours (2,607 unique adverse composites). Exact first transitions were 2,001 ICU returns, 606 deaths, 9,928 live discharges, and 36,622 still alive in hospital without an adverse transition at 48 hours. First ICU returns occurred 629/553/819 in 0–12/12–24/24–48 hours; first deaths 198/174/234; and first live discharges 194/3,098/6,636. These are endpoint-feasibility counts, not evidence for T1.

## Evidence boundary and falsifiable claim

The strongest inspected evidence supports only these claims. A MIMIC-IV/external-hospital study found a longitudinal GRU-D++ model predicted seven-day ICU readmission/death better than SWIFT, while explicitly noting short-timescale averaging, operational factors, DNR status, and composite-component limitations [K1]. A systematic review found that longitudinal routinely collected predictors can improve ICU-readmission models, but outcome windows and composite definitions vary and bias is common [K2]. EHR measurement timing and frequency encode healthcare processes as well as patient state [K3].

Those works do not establish that final-24-hour value trajectories add decision-time 48-hour information beyond endpoint state in this fixed transfer cohort; whether any increment occurs before or after substantial live discharge; whether it concerns ICU return or death; or whether a risk ranking would remain useful under a fixed review capacity.

**Primary hypothesis, unchanged.** In the fixed cohort, T1's prespecified trajectory-value summaries improve held-out prediction of the fixed 48-hour three-state outcome over S0 after enforcing decision-time availability. Incremental information, prespecified materiality, temporal/component interpretation, and hypothetical prioritization are separate claims.

**Time-structure hypothesis.** If the fixed-horizon T1 increment reflects clinically interpretable post-transfer risk rather than chiefly discharge or pathway selection, a matched competing-state model should show calibrated incremental prediction for ward-to-ICU-return and/or ward-to-death transitions across prespecified times, not merely a shift in live-discharge probability, and the direction should not reverse in adequately supported destination, observed-treatment-limit, or operative-context strata.

No result can establish biological residual instability, causal benefit, preventability, or a treatment mechanism.

## Frozen population, landmark, exposure, and split

Retain the parent verbatim:

- unit: each hospitalization's first eligible adult ICU-to-frozen-general-ward transfer after ICU LOS at least 24 hours;
- `t0 = icu/icustays.outtime`, with exact successor `hosp/transfers.intime = t0` on `subject_id,hadm_id`;
- the same 17-value frozen primary general-ward destination set and unchanged step-down sensitivity set;
- exposure window exactly `[t0-24h,t0)`;
- strict real-time chart predictors require both `charttime < t0` and `storetime < t0`;
- input/procedure predictors require exposure-window interval overlap and `storetime < t0`;
- frozen subject split seed 20260923, 60/20/20 train/validation/test, all admissions of a subject together, one test opening, and subject-cluster bootstrap.

The parent's S0 features, T1 trajectory definitions, plausibility limits, two-hour bins, training-only preprocessing, oxygen-device dictionary, O1 observation-process comparator, and value/process/order ablations remain available. The scientific deliverable in this child prioritizes S0/T1, O1, and the timing model; the parent's GRU-D/two-stream TCN remain secondary source/order benchmarks, not substitutes for the competing-state analysis.

## Fixed 48-hour baseline and primary estimand

The simple baseline remains the parent's ridge multinomial models on the same three-state target at 48 hours:

1. adverse composite: first same-admission ICU return or in-hospital death in `(t0,t0+48h]`;
2. live hospital discharge before an adverse event by 48 hours;
3. alive and in hospital without an adverse event at 48 hours.

S0 contains endpoint values, freshness and measurement-process terms, age/sex, admission type, source ICU, exact ward destination, latest service, ICU LOS, prior ICU-stay count, transfer hour/night, GCS, recent ventilation/vasopressor state, and code status. T1 adds only the frozen final-24-hour persistence, run, transition, volatility, slope, early-minus-late, worst-value, and coverage features.

The primary estimand remains paired test-set `Brier(S0)-Brier(T1)` for the fixed 48-hour multinomial target. The 0.002 material bound, validation-only calibration, and 2,000 subject-cluster bootstrap replicates remain unchanged. This is the anchor result even if the timing model performs differently.

## Competing-state alternative on the same question

Fit matched ridge-penalized discrete-time models M0 and M1 using two-hour intervals from `t0` through 48 hours. Every patient begins in the post-transfer ward state W. The first observed transitions are:

- W→R: first later same-admission `icu/icustays.intime`;
- W→D: `hosp/admissions.deathtime`;
- W→H: live `hosp/admissions.dischtime`;
- remaining in W through 48 hours.

M0 uses exactly S0 predictors. M1 uses exactly T1 predictors. Thus M1-versus-M0 tests the same trajectory increment, not a new population or exposure. Use a pooled multinomial hazard with a flexible baseline function of time (prespecified restricted cubic spline or interval indicators), ridge penalty chosen only on validation log loss, and validation-only recalibration. Do not add post-`t0` covariates.

At each interval, the earliest transition wins. Frozen tie precedence is death, then ICU return, then live discharge; report all ties. Live discharge is an observed competing absorbing state for this same-admission endpoint, not independent censoring and not 48 hours of demonstrated ward stability. Death after a prior ICU return is not a first transition and does not redefine the primary composite; report such paths descriptively from the same exact times.

Required outputs at 6, 12, 24, and 48 hours are transition-specific cumulative incidence, W-state occupancy, calibration-in-the-large/slope, time-dependent multiclass Brier score and log loss, and paired M0-versus-M1 differences with subject-bootstrap 95% intervals. Also report integrated Brier score over 0–48 hours and differences in the T1 increment across 0–12, 12–24, and 24–48 hours.

This alternative reveals information the fixed-horizon baseline loses: when the increment appears; whether it concerns ICU return, death, or live discharge; how much observable return opportunity remains after discharge; and whether a 48-hour gain is concentrated in one operational pathway. It does not identify why a transition happened or what intervention would change it.

The timing model is scientifically useful if calibrated state/transition probabilities materially clarify a positive or null fixed-horizon result. A tiny score improvement alone is not a reason to prefer it.

## Event context, destination, treatment limitation, and planned-pathway bounds

### Live discharge and event chronology

Construct one chronology row per index transfer, not just positives: exact `t0`, horizon, first ICU-return time, death time, live-discharge time, first-transition state/time, source ICU, destination, latest service, admission type, transfer hour/night, and all intervening transfer states. Verify that 48-hour state probabilities from M0/M1 sum to one and reconcile with the fixed-horizon S0/T1 labels.

### Destination and operational selection

Exact destination remains an S0/M0 input. Report calibration, event counts, fixed-horizon T1 increment, and M1 transition probabilities by exact destination and by frozen broad families:

- medical/cardiac: Medicine, Medicine/Cardiology, Cardiology, Med/Surg;
- neurologic: Neurology;
- surgical/trauma/vascular/gynecologic/thoracic: Cardiac Surgery, Surgery, Surgery/Trauma, Med/Surg/Trauma, Vascular, Med/Surg/GYN, Medical/Surgical (Gynecology), Surgery/Pancreatic/Biliary/Bariatric, Thoracic Surgery;
- hematology/oncology/transplant: Hematology/Oncology, Oncology, Transplant.

A stratum with fewer than 50 adverse first transitions in test data is descriptive only. Source ICU, latest service, admission type, transfer hour, and night are measured selection context, not complete operational adjustment. Weekend/day-of-week is prohibited because MIMIC date shifting does not preserve shared institutional weekdays.

MIMIC lacks valid bed occupancy, staffing ratios, ward monitoring intensity, rapid-response availability, transfer queues, clinician intent, and transport delays. Surviving adjustment or stratification cannot establish independence from capacity selection.

### Treatment limitation

Use only the last decision-time-available `chartevents.itemid=223758` record. Freeze exact-text mapping before test opening into explicit full code, documented DNR/DNI, documented comfort-measures-only, other documented, and undocumented. Undocumented is never full code.

Report:

1. all transfers;
2. **no documented treatment limitation** (excludes observed DNR/DNI/comfort measures but retains undocumented);
3. explicitly documented full code only;
4. documented treatment limitation, descriptively if sparse.

The phrase “no treatment limitation” is not permitted for group 2. Reversal between all-patient and explicit-full-code results makes death interpretation treatment-limit-sensitive; it does not prove that a preference caused the reversal. True goals of care, expected death, and treatment refusal require blinded clinical adjudication of decision-time notes, which are not available as a validated pre-transfer note stream here.

### Planned postoperative pathways

No structured field identifies a planned ICU return. Report two pre-`t0` context proxies separately: `admission_type` equal to ELECTIVE or SURGICAL SAME DAY ADMISSION, and latest service in the observed surgical service codes (CSURG, SURG, NSURG, ORTHO, TSURG, VSURG, PSURG, ENT, GYN, GU). Also report source ICU and surgical-family destination; none is a planned-return label.

For an outcome-path sensitivity, report both:

- any exact `hosp/transfers.careunit='PACU'` state between `t0` and ICU return;
- PACU as the immediately preceding transfer state before ICU return.

The bounded audit found 81 and 75 returns under these respective definitions. Exclude each proxy in separate sensitivities. Do not combine them or label remaining returns “unplanned.” Discharge notes at the configured `note/discharge.csv.gz` source may support a future blinded adjudication sample but are post-decision/outcome-contaminated and prohibited as predictors.

## Prediction materiality versus decision claims

Retain threshold decision curves at 2%, 5%, and 10%, but label them **hypothetical threshold net benefit**, conditional on the implied false-positive/false-negative exchange rate. Positive net benefit is not evidence that monitoring or ICU retention works.

Add capacity-quota prioritization at frozen quotas of 1%, 2%, 5%, and 10% of transfers flagged. On the untouched test set report, per 1,000 transfers:

- number flagged;
- observed adverse first transitions captured by 12, 24, and 48 hours;
- positive predictive value and sensitivity;
- excess events captured by T1 versus S0 and M1 versus M0;
- destination, code-status, and operative-context composition of flagged patients;
- 2,000 subject-bootstrap intervals.

Because true contemporaneous capacity cannot be reconstructed, quotas apply to the held-out population ranking, not to real daily beds or monitors. Call this capacity-constrained prioritization performance, not clinical utility. Claims of operational benefit require a defined action, cost/harm model, real capacity/time data, prospective workflow evaluation, and preferably randomized or quasi-experimental impact evidence.

## Interpretation and falsification

Report five separate axes.

**A. Fixed-horizon incremental information**

- Supported: paired `Brier(S0)-Brier(T1)>0` with 95% CI entirely above zero, adequate coverage/events, and acceptable validation-only recalibration.
- Material bound ruled out: 95% upper bound below 0.002.
- Inconclusive: interval crosses zero or readiness/calibration/coverage gates fail.

**B. Prespecified prediction materiality**

- Demonstrated by contract: point Brier gain at least 0.002 and positive hypothetical net benefit versus S0 at at least two frozen thresholds, with risk-category/clinical counts reported.
- Not demonstrated: A is supported but a materiality criterion fails.
- Inconclusive: uncertainty spans the bound or calibration invalidates the comparison.

This axis must not be called demonstrated patient benefit.

**C. Timing and competing-state interpretation**

- Coherent: M1 improves integrated Brier over M0 with CI above zero; transition probabilities are calibrated at 12/24/48 hours; and the fixed-horizon increment is attributable to ICU-return and/or death transitions rather than only live-discharge prediction.
- Component/time-specific: gain is confined to a stated transition or interval.
- Endpoint/timing-ambiguous: fixed-horizon gain is positive but M1 is uncalibrated, improves only discharge prediction, or adverse-transition direction materially reverses across time.
- Inconclusive: component events or precision are inadequate.

A component/time-specific result can still support A; it only narrows interpretation.

**D. Operational and treatment-limit robustness**

Report quantitative interaction/stratum estimates. A reversal in explicit-full-code, destination-family, admission-type, surgical-service, daytime, or PACU-proxy analyses makes the result context-sensitive. It does not automatically falsify incremental prediction and cannot identify capacity, plannedness, or treatment preference as a cause. Sparse strata are inconclusive.

**E. Capacity-quota prioritization**

- Promising for external workflow evaluation: T1 or M1 captures more adverse transitions than its matched baseline at at least two quotas, with CI above zero and acceptable subgroup calibration/composition.
- No incremental prioritization: upper intervals exclude a prespecified minimum of 2 additional adverse transitions captured per 1,000 at all quotas.
- Inconclusive: intervals include both possibilities or quota rankings are unstable.

Even “promising” does not establish clinical utility.

An overall supportive report requires A supported and must state B–E separately. An adverse report is justified only when adequate precision rules out the 0.002 fixed-horizon material gain or when value history adds no information beyond S0/O1; it does not prove physiologic stability. Calibration failure, sparse death/full-code strata, or unresolved reversals require an inconclusive or qualified report.

The verifier must reject claims of biological mechanism, preventable deterioration, benefit of delaying transfer/monitoring, true unplanned return, complete treatment-preference adjustment, or real capacity utility.

## Exact MIMIC bindings

Read-only archive:
`[internal dataset path]`
([source checksum]).

Required members, columns, keys, and times:

- `mimic-iv-3.1/icu/icustays.csv.gz` (`icu/icustays`): `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; `stay_id` and `subject_id,hadm_id`; `outtime=t0`; later `intime` defines ICU return.
- `mimic-iv-3.1/hosp/transfers.csv.gz` (`hosp/transfers`): `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; exact successor and post-transfer path.
- `mimic-iv-3.1/hosp/admissions.csv.gz` (`hosp/admissions`): `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; death and live discharge times.
- `mimic-iv-3.1/hosp/patients.csv.gz` (`hosp/patients`): `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; age; `dod` is not the primary in-hospital death time.
- `mimic-iv-3.1/hosp/services.csv.gz` (`hosp/services`): `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`.
- `mimic-iv-3.1/icu/chartevents.csv.gz` (`icu/chartevents`): `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; join `stay_id`; primary predictors require `charttime in [t0-24h,t0)` and `storetime<t0`.
- `mimic-iv-3.1/icu/d_items.csv.gz` (`icu/d_items`): `itemid,label,abbreviation,linksto,category,unitname,param_type`; fail on mismatch.
- `mimic-iv-3.1/icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription`.
- `mimic-iv-3.1/icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription`.

Retain exact item mappings: HR 220045; invasive/noninvasive SBP 220050/220179; invasive/noninvasive MAP 220052/220181; RR 220210; SpO2 220277; temperature F/C 223761/223762; O2 flow 223834; FiO2 223835; O2 device 226732; GCS 220739/223900/223901; code status 223758; invasive ventilation 225792; vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315.

Configured discharge notes remain read-only at
`[internal dataset path]`
with `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; they are not model inputs. All derived files stay in the workspace. Other configured datasets remain accessible but are not silently substituted for an external validation cohort.

## Outputs, uncertainty, and compute

The scientific deliverable is newly fitted S0/T1/O1 and M0/M1 models and a conclusion mechanically linked to:

1. `cohort_flow.csv`, `endpoint_chronology.parquet`, tie audit, state counts, and exact event reconciliation;
2. frozen split, preprocessing, item/device/code-status dictionaries, and strict `charttime/storetime` leakage assertions;
3. `fixed_horizon_predictions.parquet` and primary paired metrics;
4. `transition_predictions.parquet`, state occupancy/cumulative incidence at 6/12/24/48 hours, integrated and interval-specific metrics;
5. destination, treatment-limit, operative-context, PACU-proxy, daytime, and step-down sensitivity outputs;
6. `capacity_quota_metrics.json` and hypothetical threshold decision curves;
7. `interpretation_axes.json` and `conclusion.md` with estimates, intervals, status, and exact output paths.

Use 2,000 subject-cluster bootstrap replicates for all paired uncertainty; retain all admissions for a subject in each resample. Report absolute estimates and event counts, not p-values alone.

Measured discovery work: the bounded small-table chronology probe ran in about 15 seconds in ordinary shell and reproduced the frozen cohort/component counts. Full predictor extraction remains the parent's measured/estimated workload. Estimated future solver budget: 8 CPUs/64 GiB for extraction (2–4 h); 8 CPUs/64 GiB for S0/T1/O1, M0/M1, and bootstrap (2–5 h); optional retained neural source/order benchmarks on one allocated A100 plus 8 CPUs/64 GiB (3–6 h). The required timing repair is CPU-feasible and fits the configured 16 CPU/262,144 MiB/8 GPU/28,800-second envelope. GPU capacity is deployment-verified; no discovery GPU probe was needed.

## Alternatives and revisit conditions

- **Fixed-horizon model only:** rejected as the sole interpretation because it loses exact event and live-discharge timing; retained as the primary estimand.
- **Discrete-time competing-state M0/M1:** selected because it uses the identical population, predictors, split, and horizon while exposing transition timing and discharge opportunity.
- **Cause-specific Cox/Fine–Gray models:** acceptable sensitivity but not the primary alternative; separate hazard scales are less direct for coherent multiclass state probabilities. Revisit if pooled multinomial calibration fails.
- **Parent GRU-D/two-stream TCN:** retained for value/process/order attribution but not selected to resolve endpoint timing. Revisit as required if S0/T1 shows a trajectory increment whose source remains unclear.
- **Joint latent physiology/observation/capacity model:** deferred because staffing, occupancy, monitoring, policy changes, and identifiable latent-state anchors are unavailable.
- **Causal transfer-delay or monitoring policy model:** deferred until treatment/action, capacity, intervention uptake, and outcomes are measured; prediction alone cannot identify benefit.
- **Clinician adjudication:** required to estimate true planned return, expected death, treatment intent, and preventability. Use a blinded stratified sample with dual review before those labels enter any claim.

## Exactly three key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.
