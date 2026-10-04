> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 19: retrospective baseline-state repair for post-shock delivered-loop initiation

**Parent:** `[prior hypothesis]`

## Substantive successor and source audit

This successor preserves the parent's clinically consequential hour-48 post-shock loop-diuretic decision, discovery partition, fluid/weight phenotype, delivered 24-hour strategies, overlap-targeted clone-censor analysis, destination-aware primary outcome, bounded recorded-harm outcomes, and strict noncausal boundary. It repairs a structural contradiction between the parent's eligibility rule and its feasibility audit.

The parent defines invasive ventilation at `t0` from `icu/procedureevents` item 225792 with `starttime<=t0<endtime`, but later says every eligibility event must also have nonmissing `storetime<=t0`. A treatment-blind audit of the exact MIMIC-IV 3.1 source, using the configured namespaced discovery partition and first adult qualifying ICU stay, found 7,733 completed/stopped invasive-ventilation intervals spanning hour 48, all with nonmissing store time, but only 25/7,733 (0.32%) stored by `t0`. Median store lag from `t0` was 68.9 hours (5th, 25th, 75th and 95th percentiles 4.25, 24.86, 157.88 and 426.82 hours). Thus, applying the written rule makes the design structurally infeasible and invalidates the broad feasibility count.

The repair treats one fact—"the patient was invasively ventilated at `t0`"—as a **retrospectively reconstructed baseline clinical state**. For this Boolean only, a final procedure interval may be used despite `storetime>t0`. Its post-`t0` duration, exact future end, later status changes, and store lag may not enter eligibility beyond proving that the interval crosses `t0`, any covariate, treatment model, effect modifier, prognosis, censoring model, or outcome. Every other baseline/history variable remains decision-available by its source-specific clinical and storage clocks. This is an observational target-trial emulation, not a prospective EHR decision rule. A prospective rule would require a separately validated real-time ventilation-state algorithm or another data source.

The audit also found 298/7,733 broad landmarks with an absorbing event during the 24-hour grace period: 261 recorded index deaths and 37 live discharges, including nine acute-hospital and one hospice destination. These are observability counts before shock, fluid, renal, washout, treatment, or overlap eligibility—not treatment effects. They motivate an explicit shared competing-event truncation rule rather than exclusion.

## Clinical question, evidence boundary, and hypothesis

For a mechanically ventilated adult at ICU hour 48 who survived vasopressor-treated shock, is now off pressors, remains at least +50 mL/kg fluid positive, has adequate MAP, urine output and potassium, and lies in measured treatment overlap, should clinicians initiate an ICU-recorded delivered loop diuretic during the next 24 hours unless index-hospital death or discharge occurs first?

The full XML of the 2026 RADAR-2 secondary analysis was inspected (McMullan et al., DOI `10.1097/CCE.0000000000001404`; frozen source `[source checksum]`). It randomized 179 patients to a conservative-fluid/active-deresuscitation bundle or usual care and found no statistically detectable between-group differences in lactate, AKIRisk, urinary cystatin-C, or vascular-injury biomarkers; its authors emphasize modest size and imprecision. This supports feasibility and absence of a detected biomarker signal for a bundle, not patient-centered benefit, renal safety, mortality safety, or the effect of isolated loop initiation at this landmark. The full XML of Wang et al.'s 2026 EHR target-trial review was also inspected (DOI `10.1038/s41746-026-02563-z`; frozen source `[source checksum]`); it distinguishes trial specification from EHR realization and warns that healthcare-driven missingness and fragmented exposure constrain identifiability.

**Strongest supported claim:** protocolized conservative fluid management with active deresuscitation can alter fluid management without a detected biomarker-harm signal in a modest randomized study. It does not establish this drug decision's clinical benefit or safety.

**Falsifiable unresolved hypothesis:** in the prespecified measured-overlap population, assignment at `t0` to initiate a qualifying ICU-recorded delivered furosemide/bumetanide segment before the earlier of `t0+24h` or an absorbing index-hospital event, versus no actual loop administration by any route before that same boundary, increases recorded alive non-hospice/non-acute-hospital index discharge by day 28 (ANHATD28) by more than 5 percentage points, while ruling out more than 3 points higher recorded terminal/hospice disposition by day 28 (RTHD28) and more than 5 points higher observed post-landmark RRT use through day 7.

A supportive result would prioritize external validation and a pragmatic trial. It would not establish recovery, survival, renal safety, causal benefit, or a bedside recommendation.

## Source, partition, population, and clocks

Use read-only MIMIC-IV 3.1 snapshot `[source checksum]` from:

`[internal dataset path]`

Source [source checksum]; catalog [source checksum].

Before inspecting eligibility, compute `bucket=int(SHA256("ehr-hypothesis-discovery-v1"+NUL+"mimic"+NUL+canonical_base10(subject_id))) mod 100`; use buckets 0–79 only and never inspect 80–99. Emit namespace, participant ID, digest, and bucket. Select the first chronological qualifying ICU stay per subject. Cross-fit and bootstrap by subject, never clone.

Set `t0=icu/icustays.intime+48h`; require `intime<=t0<outtime` and age `anchor_age+year(admittime)-anchor_year>=18`. Retrospectively reconstruct invasive ventilation at `t0` from positive-duration `icu/procedureevents` item 225792 (dictionary label "Invasive Ventilation"), valid subject/admission/stay keys, `starttime<=t0<endtime`, and `statusdescription` in `FinishedRunning,Stopped`; `Paused` is a sensitivity. Require nonmissing start/end/store time, but do not require `storetime<=t0` for this Boolean. Record raw row provenance and lag. After deriving the Boolean, mask `endtime` at `t0`; no duration-after-`t0`, future end, or store lag can be used analytically.

Before assignment require:

- at least one positive delivered vasopressor segment before `t0-6h` and none overlapping `(t0-6h,t0]`, using inputevent items 221289/229617, 221662, 221749/229630/229631/229632, 221906, and 222315;
- median MAP at least 65 mmHg in `(t0-3h,t0]`, chartevent items 220052/220181/225312;
- cumulative unit-safe fluid balance at least +50 mL/kg from ICU admission through `t0`;
- decision-available weight 30–300 kg;
- urine output greater than 0.1 mL/kg/hour in `(t0-6h,t0]`;
- latest decision-available potassium item 50971 or 52610 in `(t0-12h,t0]` numeric and at least 3.0 mmol/L;
- no active ECMO, no exact-timed delivered RRT overlapping `t0`, and no actual loop by any route in `(t0-12h,t0]`.

Except for the single reconstructed ventilation Boolean, eligibility and clone histories require clinical/event time at or before the boundary and nonmissing storage time at or before that boundary. Retrospective treatment delivery may use final event facts only to classify whether delivery occurred; future end time, final total, response, and later content never become covariates. Emit clinical-only, decision-available, retrospective-state, late-entry, and excluded counts separately.

Fluid is positive delivered `inputevents.amount` in mL (L ×1000), with crossing recognized mL/hour infusions accrued only to the boundary. Never convert drug mass, dose, mcg, units, mEq, mmol, unknown units, or `totalamount` to fluid. Accepted statuses are `FinishedRunning,ChangeDose/Rate,Stopped,Paused,Bolus`; deduplicate overlapping segments only within `orderid/linkorderid`. Output is positive `outputevents.value` in mL (L ×1000), with both clocks by `t0`, dictionary `linksto=outputevents`, Output/Drains categories, excluding item 227488 and pre-admission item 226633; decision-available positive-mL item 227488 counts as input. Require valid input and output and no six-hour pre-`t0` recording gap. Weight hierarchy is earliest decision-available kg in `[intime-6h,intime+24h]`: item 226512 then 224639; item 226531 pounds divided by 2.20462 after unit confirmation. `inputevents.patientweight` is sensitivity only.

## Interventions and absorbing-event state machine

Let `Q=min(t0+24h,T_absorb)`, where `T_absorb` is the first valid post-`t0` index-hospital death or any index-hospital discharge. Discharge to an acute hospital or hospice is absorbing and remains a classified outcome, not censoring. ICU exit without hospital discharge is not absorbing.

**A:** before `Q`, initiate a qualifying ICU-recorded delivered furosemide/bumetanide segment from `icu/inputevents.itemid` 221794, 228340, or 229639, with valid keys/times, status `FinishedRunning,ChangeDose/Rate,Stopped`, and positive amount convertible to mg or positive mg/hour over positive duration. `Paused` is sensitivity. Unknown units, nonpositive, canceled/not-started, and order-only rows are not delivery.

**B:** before `Q`, have no actual furosemide, bumetanide, torsemide, or ethacrynic-acid administration by any route. Join `hosp/emar` to all `hosp/emar_detail` siblings on `subject_id,emar_id,emar_seq`, retain `parent_field_ordinal`, aggregate once per eMAR event, and apply a frozen normalized whole-drug dictionary. Actual administration requires positive `dose_given` or `product_amount_given`, no true `complete_dose_not_given`, and event text among `Administered, Delayed Administered, Administered in Other Location, Partial Administered, Started, Started in Other Location, Restarted`. Missing route still deviates B. Orders never define treatment. The primary exposure is ICU-recorded delivered loop, not verified IV loop; explicit-IV eMAR and ICU/eMAR ±15-minute concordance are sensitivities.

At `t0`, clone each subject to A and B. For hourly intervals 0–23 use prior decision-available history only. Within an interval:

1. A valid absorbing event before or tied with treatment is recorded in every still-compatible clone; neither clone is artificially censored.
2. Earlier qualifying ICU loop satisfies A and censors B.
3. Earlier nonqualifying actual loop censors unsatisfied A and B.
4. Otherwise both remain compatible.
5. At hour 24, censor unsatisfied A; B remains adherent if loop-free.

Stop A exposure-related censoring after qualifying initiation. Treatment after `Q` is unrestricted. Reverse exact treatment/event ties in sensitivity. Emit subject/clone/hour, event and storage clocks, history provenance, compatibility, probability, absorbing-event type, satisfaction time, and censor reason. The intervention is therefore a grace-period policy truncated by a shared absorbing event, not guaranteed drug receipt among patients who die or leave the index hospital first. Excluding early events is forbidden in the primary analysis because it would condition on postbaseline survival/disposition.

## Estimand, baselines, and analysis

The primary data-defined estimand is the A-minus-B ANHATD28 risk difference among baseline subjects with cross-fitted probability of qualifying A initiation before an absorbing event `e0(X0)` in [0.10,0.90]. Estimate `e0` using baseline covariates only with nonqualifying loop and absorbing event as competing events; never condition overlap membership on realized future treatment or outcome. Apply common tilt `e0(1-e0)` identically to both clones.

Fit arm-specific cross-fitted pooled-logistic artificial-censoring hazards. Denominator is `Pr(C[j+1]=0|C[j]=0,H_j,arm)`; numerator uses frozen baseline only. Include A satisfaction and B hourly loop-free decisions; stop weight multiplication after A initiation, absorbing outcome, or censoring. Truncate cumulative stabilized weights at 1st/99th percentiles and report untruncated estimates.

Prespecified baseline/history variables are demographics; admission era/type, service/care unit and transfer location; prior completed-admission diagnoses and loop exposure; weight; fluid balance and urine trajectories; creatinine, potassium and lactate; MAP, pressor dose and cessation; FiO2, PEEP, oxygenation and ventilation measurements; sedation; crystalloid/albumin; procedures; and missingness. Later diagnoses, notes, outcomes, and treatment response are forbidden.

Report four baselines: unadjusted observed-strategy risks, baseline common-overlap clone risks without artificial-censor weights, overlap-plus-clone-censor risks, and the prespecified stochastic observed-odds multipliers 0.5/0.75/1/1.33/2. The latter are policy sensitivities, not unmeasured-confounding tests. Use subject-level cross-fitting and at least 500 subject bootstraps. Report arm/event counts, grace-period absorbing events, adherence, calibration, standardized differences, probability/weight tails, ESS, negative-control pre-`t0` slopes, and the parent's binary readiness/goals-of-care tipping grid.

## Outcomes, uncertainty, and falsification

At `H28=t0+28d`, classify `hosp/admissions` into recorded index death; exact `HOSPICE`; exact `ACUTE HOSPITAL`; recorded alive other destination; prolonged hospitalization; and invalid/discordant state. For flag-confirmed death use valid `deathtime`; otherwise use valid post-`t0` `dischtime`. A live discharge with missing or `DIED` destination is invalid. ANHATD28 is recorded alive non-hospice/non-acute discharge. Report any-live-discharge, HOME/HOME HEALTH CARE, chronic/LTAC-as-failure, day 14/21, era/service/unit, anomaly-excluded, readmission, and recorded-DOD sensitivities. Discharge is not recovery or survival.

RTHD28 is harmful. Its lower indicator is recorded index death or exact HOSPICE by H28; its upper indicator additionally includes missing/`DIED` live destinations and irreconcilable death/discharge states. Compute sharp arm and effect bounds `Delta_L=pA_L-pB_U`, `Delta_U=pA_U-pB_L` with one-sided bootstrap limits. This is an administrative signal, not mortality or hospice appropriateness.

True day-28 mortality remains mandatory: combine exact in-hospital death with date-only `hosp/patients.dod` interval `[00:00,+1d)`; missing post-discharge status remains [0,1]. Report arm risks, sharp effect bounds, widths, and unknown fractions. ALDL7 remains a mandatory bounded respiratory outcome using extubation items 227194/225468/225477, ventilation 225792, intubation 224385, linked ICU intervals, and death precedence. Observed post-landmark RRT through day 7 uses ICU procedure items 225441/225802/225803/225805/225809/225955 with delivered status and hospital `procedures_icd` ICD-9 3995/5498 or ICD-10 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z. Date-only `chartdate` contributes full-containment lower and any-intersection upper evidence; deduplicate and report timing strata. Neither absence of recorded RRT nor ALDL bounds establish renal or respiratory safety.

The >5-point hypothesis is magnitude-supported only if the lower one-sided 95% limit of ANHATD28 RD exceeds +0.05; it is margin-falsified if the upper limit is at most +0.05; otherwise unresolved.

**Harbor-supportive evidence** requires magnitude support, RTHD28 conservative upper-effect upper limit below +0.03, observed-RRT conservative upper-effect upper limit below +0.05, no ALDL7 definitive adverse trigger, no destination sign reversal, and all temporal/state/unit/overlap/calibration/negative-control/weight/bound/bias diagnostics passing. This supports trial prioritization only.

**Adverse evidence** occurs if ANHATD28 upper limit is at most 0; RTHD28 lower-effect lower limit is at least +0.03; observed-RRT lower-effect lower limit is at least +0.05 under both date brackets; or ALDL7 upper-effect upper limit is below -0.05.

**Inconclusive** covers every other pattern, including a +2-point precise estimate (which falsifies the >5-point claim but does not prove no benefit), wide RTHD28/RRT bounds, destination conflict, plausible residual bias sufficient to reverse the primary, or failed diagnostics.

Declare infeasible/inconclusive before interpreting effects if either strategy has fewer than 100 adherent subjects, ESS below 75, over 10% of person-hours have denominator probabilities below .01 or above .99, over 1% temporal/state contradictions, over 10-point anomaly imbalance, material differential late entry, failed negative controls, or unreconciled state/bound arithmetic. Separately report the strict `procedureevents.storetime<=t0` ventilation count; its expected sparsity is an observability limitation, not a reason to substitute an undisclosed cohort. If the reconstructed ventilation state cannot be implemented without using post-`t0` duration or outcomes, the experiment is infeasible.

## Exact source bindings

All ZIP members are under `mimic-iv-3.1/`:

- `hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`.
- `hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,dod`.
- `icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime`.
- `hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription,continueinnextdept,orderid,linkorderid`.
- `icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,patientweight,statusdescription,totalamount,totalamountuom`.
- `icu/outputevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom`.
- `icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname`; join ICU dictionaries on `itemid`.
- `hosp/labevents.csv.gz`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom,flag`; `hosp/d_labitems.csv.gz`: `itemid,label,fluid,category`.
- `hosp/emar.csv.gz`: `subject_id,hadm_id,emar_id,emar_seq,charttime,storetime,medication,event_txt`; `hosp/emar_detail.csv.gz`: `subject_id,emar_id,emar_seq,parent_field_ordinal,administration_type,complete_dose_not_given,dose_given,dose_given_unit,product_amount_given,product_unit,product_description,route,infusion_rate,infusion_rate_unit`.
- `hosp/procedures_icd.csv.gz`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; `hosp/d_icd_procedures.csv.gz`: `icd_code,icd_version,long_title`.
- `hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`.
- `hosp/diagnoses_icd.csv.gz` plus `hosp/d_icd_diagnoses.csv.gz`: prior completed admissions only.
- `hosp/prescriptions.csv.gz` and `hosp/pharmacy.csv.gz`: order-only diagnostics.

Optional radiology is the separate read-only `[internal dataset path]`, columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; exclude it unless a frozen timely parser and blinded clinical adjudication are supplied. Images and waveforms are unavailable. HCC, eICU, and UKB remain directly accessible but do not share MIMIC identifiers and are not pooled. Derived files remain in the workspace; every source remains read-only.

## Verifier contract and stronger claims

Required outputs are partition proof and attrition; the ventilation reconstruction row, masked Boolean and store-lag audit; one row per subject/clone; raw row and both-clock provenance; fluid/weight components; aggregated treatment/route evidence; every clone-hour transition; overlap, weights and ESS; complete destination states; ANHATD28, RTHD28, true-mortality, ALDL7 and RRT individual/arm/effect bounds; bootstrap endpoints; sensitivities; gate booleans; magnitude status; and branch. Every numerical conclusion must reference an output field.

The verifier can check source hashes/headers, joins, partition, item/status/unit rules, the one-field retrospective exception, masking of post-`t0` ventilation duration, decision-time exclusions elsewhere, eMAR sibling aggregation, absorbing-event priority, clone transitions, weights, state reconciliation, bound orientation, margins, and branch logic. Fixtures must reject: applying `storetime<=t0` to the primary ventilation Boolean while claiming the 7,733-frame feasibility; using future ventilation duration/end as a predictor; censoring an early death or discharge asymmetrically; excluding early events; or pairing correct computation with claims of IV route, causality, safety, recovery, survival, or recommended practice. They must accept appropriate synthetic supportive, adverse, margin-falsified, and sparse/inconclusive interpretations.

Automatic verification cannot establish true baseline ventilation physiology, clinician intent/readiness, bedside congestion, goals of care, hospice appropriateness, functional recovery, complete external death/readmission/dialysis, exchangeability, transportability, renal/mortality safety, or causal benefit. Baseline-state validity and destination meaning require blinded clinical review; complete mortality and post-discharge outcomes require linkage; treatment recommendations require external validation and preferably randomization.
