# Episode 18: observable safety contract for post-shock delivered-loop initiation

**Parent:** `[prior hypothesis]`

## Substantive repair

This successor preserves the parent's consequential hour-48 post-shock decision, corrected participant partition, delivery-coherent 24-hour strategies, destination-aware primary outcome, clone-hour state machine, common overlap target, conservative partial-identification arithmetic, observed-RRT provenance, and noncausal boundary. It repairs a decision-changing mismatch between the hypothesis and what MIMIC can identify.

The parent requires the upper confidence limit of a sharp true day-28 mortality effect bound to be below +3 percentage points for a supportive result, while correctly refusing to treat missing post-discharge death as survival. A direct treatment-blind audit of the exact source found that among 7,733 first adult discovery-partition ICU stays with procedure-recorded invasive ventilation spanning hour 48, true day-28 vital status is unknown for 4,347 (56.2%) under that rule. The same frame has 2,105 recorded index-hospital deaths by day 28, 4,563 live index discharges, and 999 patients still in the index hospital at day 28. The audit also found only seven missing destinations among live discharges, while prior frozen source work found ALDL7 unknown for 3,261/7,733 (42.2%). These are broad observability counts before shock, fluid, renal, washout, overlap, or treatment eligibility; they are not treatment effects.

Therefore the parent can almost never satisfy its claimed mortality-safety branch even if the recorded data favor initiation. This child does not convert missing DOD to survival. It changes the resolvable hypothesis to use **recorded terminal/hospice disposition by day 28 (RTHD28)** as the safety guard, retains strict true-mortality and ALDL7 bounds as mandatory evidence-limit outputs and adverse-signal tests, and renames the positive branch **Harbor-supportive evidence**, not clinical safety or a treatment recommendation. True 28-day mortality safety requires external vital-status linkage or another study.

## Clinical question, supported claim, and unresolved hypothesis

For a mechanically ventilated adult at ICU hour 48 who has survived vasopressor-treated shock, is now off pressors, remains at least +50 mL/kg fluid positive, has adequate MAP, urine output and potassium, and lies in measured treatment overlap, should clinicians initiate an ICU-recorded delivered loop diuretic during the next 24 hours?

The full XML of the 2026 RADAR-2 secondary analysis was inspected (McMullan et al., DOI `10.1097/CCE.0000000000001404`; frozen source `[source checksum]`). It studied a conservative-fluid plus active-deresuscitation bundle, not isolated loop initiation at this landmark, and reported no detected between-group differences in lactate, AKIRisk, urinary cystatin-C, or vascular-injury biomarkers; modest sample size and imprecision limit stronger conclusions. The full XML of Wang et al.'s 2026 operational EHR target-trial review was also inspected (DOI `10.1038/s41746-026-02563-z`; frozen source `[source checksum]`). It supports explicit trial specification but emphasizes that encounter-driven missingness, fragmented exposure, and design realization constrain identifiability; cloning and flexible models do not recover unavailable outcomes or exchangeability.

The strongest supported claim is that protocolized deresuscitation can alter fluid management without a demonstrated biomarker safety signal in a modest randomized secondary analysis. It does not establish patient-centered benefit, renal safety, mortality safety, or the effect of this delivered-loop decision.

**Falsifiable unresolved hypothesis:** In the prespecified measured-overlap population, assignment at `t0` to initiate a qualifying ICU-recorded delivered furosemide/bumetanide segment by `t0+24h`, versus no actual loop administration by any route through `t0+24h`, increases recorded alive non-hospice/non-acute-hospital index discharge by day 28 (ANHATD28) by more than 5 percentage points, while ruling out more than 3 points higher RTHD28 and more than 5 points higher observed post-landmark RRT use through day 7.

This advances bundle-level fluid-balance evidence to a specific, delivery-coherent decision and a patient-centered but administrative destination outcome. Even Harbor-supportive evidence only prioritizes external validation and a pragmatic trial.

## Data, partition, population, and time

Use MIMIC-IV 3.1 snapshot `[source checksum]` from read-only ZIP:

`[internal dataset path]`

Source SHA-256 is `[source checksum]`; catalog SHA-256 is `[source checksum]`.

Before inspecting eligibility, compute
`bucket = int(SHA256("ehr-hypothesis-discovery-v1" + NUL + "mimic" + NUL + canonical_base10(subject_id))) mod 100`.
Use buckets 0–79 only; never inspect 80–99. Emit namespace, canonical ID, digest and bucket. Select the first chronological qualifying ICU stay per subject; bootstrap subjects, never clones.

Set `t0=icu/icustays.intime+48h`; require `intime<=t0<outtime`, age at admission `anchor_age+year(admittime)-anchor_year>=18`, and a positive-duration `icu/procedureevents` item 225792 with `starttime<=t0<endtime` and status `FinishedRunning` or `Stopped` (`Paused` sensitivity).

Before assignment require:

- a positive delivered vasopressor segment before `t0-6h` and none overlapping `(t0-6h,t0]`, using inputevent items 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315;
- median MAP >=65 mmHg in `(t0-3h,t0]`, chartevent items 220052/220181/225312;
- cumulative unit-safe balance >=+50 mL/kg from ICU `intime` through `t0`;
- decision-available weight 30–300 kg;
- urine output >0.1 mL/kg/h in `(t0-6h,t0]`;
- latest decision-available potassium item 50971 or 52610 in `(t0-12h,t0]`, numeric and >=3.0 mmol/L;
- no active ECMO, no exact-timed delivered RRT overlapping `t0`, and no actual loop by any route in `(t0-12h,t0]`.

Eligibility and clone histories require both clinical/event time and nonmissing `storetime` no later than the boundary. Retrospective delivery reconstruction may use final event facts only to classify whether delivery occurred; it may not feed future end time, final status, total amount, or later-stored content backward into covariates. Emit clinical-only, decision-available, late-entry and retrospective-delivery counts by source.

Freeze the fluid/weight implementation. Input volume is positive delivered `inputevents.amount` in mL (or L ×1000); crossing infusions with recognized mL/hour rates accrue only through the boundary. Never convert medication mass, dose, mcg, units, mEq, mmol, unknown units, or `totalamount` to fluid. Accepted fluid statuses are `FinishedRunning`, `ChangeDose/Rate`, `Stopped`, `Paused`, and `Bolus`; deduplicate only overlapping segments sharing `orderid/linkorderid`. Output is positive `outputevents.value` in mL (or L ×1000), with `charttime/storetime<=t0`, dictionary `linksto=outputevents`, Output/Drains categories, excluding item 227488 and pre-admission item 226633. Count decision-available positive mL item 227488 as input. Require at least one valid input and output and no six-hour pre-`t0` recording gap. Weight is earliest valid decision-available kg in `[intime-6h,intime+24h]`, preferring admission weight 226512, then daily weight 224639; convert pounds item 226531 by 2.20462 after unit confirmation. `inputevents.patientweight` is sensitivity only.

## Strategies and grace period

**A:** first qualifying ICU-recorded delivered furosemide/bumetanide in `(t0,t0+24h]`: `icu/inputevents.itemid` 221794, 228340 or 229639; valid subject/hadm/stay keys; nonmissing start/end/store times; status `FinishedRunning`, `ChangeDose/Rate`, or `Stopped`; and positive amount convertible to mg or positive mg/hour rate over positive duration. `Paused` is sensitivity. Unknown units, nonpositive, cancelled, not-started and order-only rows are not delivery.

**B:** no actual furosemide, bumetanide, torsemide or ethacrynic-acid administration by any route through hour 24. Join `hosp/emar` to every `hosp/emar_detail` sibling by `subject_id,emar_id,emar_seq`, retain `parent_field_ordinal`, then aggregate once per eMAR event. Use a frozen case-folded punctuation-normalized whole-drug dictionary. Require positive `dose_given` or `product_amount_given`, no true `complete_dose_not_given`, and event evidence `Administered`, `Delayed Administered`, `Administered in Other Location`, `Partial Administered`, `Started`, `Started in Other Location`, or `Restarted`. Report each accepted label; all others are nonadministration or unknown. Missing route still deviates B. Orders never define treatment.

The primary exposure is ICU-recorded delivered loop, not verified IV loop. Route-explicit IV eMAR and ICU/eMAR ±15-minute concordance are sensitivities. Sparse route coverage cannot invalidate the route-agnostic primary.

Clone each subject to A and B at `t0`. In hourly intervals `j=0,...,23`, compute `H_j` from prior decision-available values only. Priority is: (1) death or explicit live discharge/acute transfer is an outcome in every compatible clone; (2) qualifying ICU loop satisfies A and censors B, while a nonqualifying actual loop censors still-unsatisfied A and B; (3) otherwise both remain compatible; (4) at hour 24 censor unsatisfied A, while B remains adherent if loop-free. Stop A exposure-related censoring after qualifying initiation. Treatment after hour 24 is unrestricted. Reverse ties in sensitivity. Emit every subject/clone/hour transition, event time, history provenance, probability, compatibility and censor reason.

## Estimand and analysis

The primary data-defined estimand is the A-minus-B ANHATD28 risk difference among baseline subjects with cross-fitted cumulative probability of qualifying A initiation before a terminal event `e0(X0) in [0.10,0.90]`. Fit `e0` from baseline covariates only, treating nonqualifying loop and terminal events as competing events; never condition on realized future treatment or outcome. Apply common tilt `e0(1-e0)` identically to both clones.

Fit cross-fitted pooled-logistic artificial-censoring models separately by arm. Denominator: `Pr(C[j+1]=0 | C[j]=0,H_j,arm)`; numerator: the same using frozen baseline only. Include A hour-24 satisfaction and B hourly loop-free decisions. Stop multiplying after A initiation, terminal outcome or censoring. Truncate cumulative stabilized weights at 1st/99th percentiles and report untruncated results.

Prespecified baseline/history variables are demographics, admission era/type, service/careunit, prior completed-admission diagnoses and loop exposure, weight, balance and urine trajectories, creatinine/potassium/lactate, MAP/pressor dose and cessation time, FiO2/PEEP/oxygenation/ventilation, sedation, crystalloid/albumin, procedures, transfer location and missingness. Later diagnoses, notes, response and outcomes are forbidden.

Estimate crude, common-overlap and overlap-plus-clone-censor risks/RDs, using subject-level cross-fitting and at least 500 subject bootstraps. Report calibration, standardized differences, arm/event counts, adherence, probability tails, weight tails and ESS. Observed-odds multipliers 0.5/0.75/1/1.33/2 are stochastic-policy analyses, not unmeasured-confounding tests. Separately report the parent's binary readiness/goals-of-care tipping grid. Prespecified pre-`t0` slopes are placebo outcomes.

## Outcomes and exact interpretation

At `H28=t0+28d`, deterministically classify `hosp/admissions` into: recorded index-hospital death; exact `HOSPICE`; exact `ACUTE HOSPITAL`; recorded alive non-hospice/non-acute destination; prolonged hospitalization; and invalid/discordant state. For flag-confirmed death, use valid `deathtime`, otherwise valid post-`t0` `dischtime`. A live discharge with missing or `DIED` destination is invalid, not success. ANHATD28 is the recorded alive non-hospice/non-acute state. Report any live discharge, exact HOME/HOME HEALTH CARE, CHRONIC/LONG TERM ACUTE CARE-as-failure, each destination, day 14/21, era/service/unit, anomaly-excluded, same-system readmission and recorded DOD sensitivities. Binary risk must reconcile with weighted multistate cumulative incidence. Discharge is not recovery or survival.

RTHD28 is harmful. Lower indicator is recorded index-hospital death or exact HOSPICE discharge by H28. Upper additionally includes live discharges with missing/`DIED` destination and irreconcilable death/discharge states by H28. Compute sharp arm and effect bounds `Delta_L=pA_L-pB_U`, `Delta_U=pA_U-pB_L`, with one-sided bootstrap limits. It is a recorded terminal-disposition signal, not true mortality or appropriateness of hospice.

True day-28 mortality remains mandatory: exact in-hospital death plus date-only `hosp/patients.dod` interval `[00:00,+1d)`; missing post-discharge vital status remains `[0,1]`. Report arm risks, sharp effect bounds, interval widths and unknown fractions. This outcome cannot support a mortality-safety claim without external linkage.

ALDL7 remains a mandatory bounded secondary outcome using extubation items 227194/225468/225477, invasive ventilation 225792, intubation 224385, linked ICU intervals and death precedence exactly as in the parent. Its 42.2% broad-frame unknown fraction prevents absence of detected harm from being called respiratory safety. A sharp upper effect bound entirely below -0.05 can still trigger an adverse signal.

Observed post-landmark RRT through day 7 is harmful but is not new RRT, AKI or renal safety. ICU evidence is `procedureevents` items 225441/225802/225803/225805/225809/225955 with accepted delivered status and start in `(t0,t0+7d]`. Hospital delivered dialysis is `procedures_icd` ICD-9 3995/5498 or ICD-10 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z, dictionary-confirmed; exclude access/imaging codes. Treat `chartdate` as `[00:00,+1d)`; full containment is lower evidence and any intersection upper evidence. Deduplicate evidence and report prior-timed, earlier-date, same-date-indeterminate and no-prior strata.

## Falsification, gates, and result branches

The >5-point primary hypothesis is supported only if the lower one-sided 95% limit of ANHATD28 RD is >+0.05; it is margin-falsified if the upper limit is <=+0.05; otherwise unresolved.

**Harbor-supportive evidence** requires primary magnitude support; RTHD28 conservative upper-effect upper limit <+0.03; observed-RRT conservative upper-effect upper limit <+0.05; no ALDL7 definitive adverse trigger; no qualified destination sign reversal; and every temporal, state, unit, overlap, calibration, negative-control, weighting, bound and bias diagnostic passing. This supports trial prioritization only. It does not rule out true mortality, respiratory, renal or functional harm.

**Adverse evidence** occurs if ANHATD28 upper limit <=0; RTHD28 lower-effect lower limit >=+0.03; observed-RRT lower-effect lower limit >=+0.05 under both date brackets; or ALDL7 upper-effect upper limit <-0.05. These are recorded adverse signals, not biological proof.

**Inconclusive** covers every other pattern, including primary margin falsification without harm, wide true-mortality/ALDL bounds, plausible residual bias sufficient to reverse the primary, destination conflict, or failed diagnostics. A precise +2-point estimate falsifies the >5-point claim but does not prove no benefit.

Before effects, declare infeasible/inconclusive if either strategy has <100 adherent subjects, ESS <75, >10% person-hours have denominator probability <.01 or >.99, >1% temporal/state contradictions, >10-point anomaly imbalance, material differential late entry, failed negative controls, or nonreconciling state/bound arithmetic. Report final attrition and overlap; the broad audit cannot satisfy these gates.

## Exact source bindings

All core members are under `mimic-iv-3.1/` in the exact ZIP:

- `hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`.
- `hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,dod`.
- `icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime`.
- `hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,patientweight,statusdescription,totalamount,totalamountuom`.
- `icu/outputevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom`.
- `icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription,continueinnextdept,orderid,linkorderid`.
- `icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname`; join all ICU dictionaries by `itemid`.
- `hosp/labevents.csv.gz`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom,flag`; `hosp/d_labitems.csv.gz`: `itemid,label,fluid,category`.
- `hosp/emar.csv.gz`: `subject_id,hadm_id,emar_id,emar_seq,charttime,storetime,medication,event_txt`; `hosp/emar_detail.csv.gz`: `subject_id,emar_id,emar_seq,parent_field_ordinal,administration_type,complete_dose_not_given,dose_given,dose_given_unit,product_amount_given,product_unit,product_description,route,infusion_rate,infusion_rate_unit`.
- `hosp/procedures_icd.csv.gz`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; `hosp/d_icd_procedures.csv.gz`: `icd_code,icd_version,long_title`.
- `hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`.
- `hosp/diagnoses_icd.csv.gz` plus `hosp/d_icd_diagnoses.csv.gz`: prior completed admissions only.
- `hosp/prescriptions.csv.gz` and `hosp/pharmacy.csv.gz`: order-only diagnostics.

Optional radiology is the separate read-only gzip `[internal dataset path]`, columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; exclude it unless a frozen timely parser and blinded clinical adjudication are supplied. No images or waveforms are available. All four configured datasets remain directly readable; only MIMIC supplies this linked ICU-hour-48 contract. Derived files remain in the workspace.

## Verifier and evidence limits

Required outputs are partition proof and attrition; one row per subject/clone; raw row and both-clock provenance; fluid/weight components; aggregated treatment/route evidence; every clone-hour transition/probability; overlap, weights and ESS; complete destination states; ANHATD28, RTHD28, true-mortality, ALDL7 and RRT individual/arm/effect bounds; bootstrap endpoints; sensitivity estimates; gate booleans; magnitude status; and branch. Every numerical sentence must reference an output field.

The verifier can check hashes, headers, joins, partition, item/status/unit rules, two-clock exclusions, eMAR sibling aggregation, clone transitions, terminal priority, weight arithmetic, state reconciliation, bound orientation, margins and branch logic. Fixtures must reject correct computations paired with unsupported “IV,” “causal,” “safe,” “recovery,” “28-day survival,” or practice conclusions, and must accept appropriate interpretations of synthetic supportive, adverse, margin-falsified and sparse/inconclusive outputs.

No automatic verifier can establish actual route where missing, clinician intent/readiness, bedside congestion, goals of care, hospice appropriateness, functional recovery, complete external death/readmission/dialysis, exchangeability, transportability, renal safety, mortality safety or causal benefit. Those require blinded clinical adjudication, external linkage/validation, expert review and preferably randomization.
