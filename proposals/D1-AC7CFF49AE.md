> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode-12 observable-outcome successor: competing-risk live index-hospital discharge after post-shock IV-loop initiation

**Parent:** `[prior hypothesis]`

## Substantive repair and scientific boundary

This child preserves the parent's namespaced discovery partition, hour-48 landmark, eligibility, two-clock event/measurement contract, unit-safe cumulative fluid phenotype and weight hierarchy, delivered 24-hour IV-loop strategies, measured-overlap population, trajectory-calibrated clone-censor analysis, recorded mortality/RRT safety gates, exact MIMIC-IV 3.1 bindings, and limits on causal interpretation.

It repairs the parent's principal unresolved limitation: ALDL7 is frequently not identified after ICU exit. A source-row audit on the parent-compatible broad frame—adult patients invasively ventilated at ICU hour 48, discovery buckets 0–79, first broad landmark per subject, before shock/fluid/renal/treatment eligibility—found 3,261/7,733 (42.2%) ALDL7-unknown. In the same 7,733 landmarks, `hosp/admissions.dischtime` was complete and deterministically classified 4,563 (59.0%) recorded live index-hospital discharges by day 28, 2,105 (27.2%) in-hospital deaths before live discharge by day 28, and 1,065 (13.8%) with no live discharge or in-hospital death by day 28. These are endpoint-feasibility counts, not the final cohort and not treatment-effect evidence.

The primary endpoint becomes **recorded live index-hospital discharge by day 28 (LHD28)**, analyzed with in-hospital death as a competing event. “Live discharge” means the recorded disposition at `dischtime`; it does **not** mean alive at day 28, days alive outside hospital, recovery, freedom from later hospitalization, or post-discharge survival. A patient discharged alive on day 5 satisfies LHD28 even if later death is recorded. Post-discharge death, where recorded, remains a separate safety outcome and never licenses survival inference from its absence.

The strongest evidence currently supports only that the randomized RADAR-2 protocolized conservative-fluid/active-deresuscitation strategy removed fluid without statistically detectable worsening of lactate, AKIRisk or urinary cystatin-C in a modest, imprecise secondary analysis; clinically important effects were not excluded (McMullan et al., *Critical Care Explorations* 2026;8:e1404, DOI `10.1097/CCE.0000000000001404`, inspected frozen source `[source checksum]`). This is not evidence for an individual observational IV-loop initiation effect. Boyle et al. describe the ascertainment, interpretability and competing-event problems of critical-care endpoints and note that endpoint ranking rules require sensitivity analysis (*Am J Respir Crit Care Med* 2026;212:1702–1709, DOI `10.1093/ajrccm/aamag238`, PMCID `PMC13424680`, inspected full-text XML source `[source checksum]`). That perspective does not validate LHD28 or this observational design.

The unresolved, falsifiable claim is:

> Among invasively ventilated adults at ICU hour 48 who have recovered from vasopressor-treated shock, have unit-safe cumulative fluid balance at least +50 mL/kg, retain urine output, have potassium at least 3.0 mmol/L, and lie in measured treatment overlap, initiating an actually delivered ICU IV loop within the next 24 hours increases the 28-day cumulative incidence of recorded live discharge from the index hospital by more than 5 percentage points versus withholding loops for that window, without excess recorded 28-day death or observed new RRT.

The advance is a more resolving, patient-relevant index-hospital estimand that retains death explicitly and can be computed for every temporally coherent admission, while keeping ALDL7 as an observation-bounded mechanistic secondary. It tests a decision-relevant association and can prioritize a pragmatic trial. It cannot establish exchangeability, clinical readiness, discharge appropriateness, survival after discharge, external readmission, renal safety, net benefit, or a treatment recommendation.

## Target trial retained

### Partition, unit, population and time

Before eligibility-row inspection or model fitting, calculate

`SHA256(ASCII("ehr-hypothesis-discovery-v1") + NUL + ASCII("mimic") + NUL + ASCII(canonical base-10 subject_id)) mod 100`.

Buckets 0–79 are discovery; 80–99 remain reserved and are not external validation. Emit namespace, canonical identifier, digest, bucket and partition checksum. After all eligibility criteria, select the first chronologically eligible ICU stay per subject. No row-level random split is allowed; cross-fitting and at least 500 bootstrap replicates keep subjects and both clones together.

Set `t0 = icu/icustays.intime + 48 hours`. The strategy/grace window is `(t0,t0+24h]`; primary follow-up is `(t0,t0+28d]`. Require a linked admission with `admittime <= intime <= t0 < dischtime`; missing or impossible admission/ICU boundaries are explicit exclusions and counts, not imputations.

Eligibility is unchanged: age >=18; accepted invasive-ventilation item 225792 with positive duration and `starttime <= t0 < endtime` (`FinishedRunning` or `Stopped`; `Paused` sensitivity); at least one positive delivered vasopressor segment before `t0-6h` and none overlapping `(t0-6h,t0]`; median MAP >=65 mmHg in `(t0-3h,t0]`; unit-safe cumulative balance >=+50 mL/kg from ICU admission through t0; valid weight 30–300 kg; urine output >0.1 mL/kg/h in `(t0-6h,t0]`; latest decision-available blood potassium 50971/52610 in `(t0-12h,t0]` >=3.0 mmol/L. Exclude active ECMO or delivered RRT at t0 and any delivered loop by any route in `(t0-12h,t0]`. Earlier loop exposure is allowed; never-loop-since-ICU-admission is a sensitivity.

Vasopressors remain epinephrine 221289/229617, dopamine 221662, phenylephrine 221749/229630/229631/229632, norepinephrine 221906 and vasopressin 222315. MAP items remain 220052/220181/225312. ICU joins require `subject_id,hadm_id,stay_id`; hospital joins require `subject_id,hadm_id`.

### Two-clock and unit contracts retained

Delivered clinical events/states in `icu/inputevents` and `icu/procedureevents` use clinical `starttime,endtime`; `storetime` is provenance, not a reason to erase an event retrospectively. At any boundary tau, only the clinical-time portion through tau may define status. Future end times, final totals, status, or post-tau segments cannot enter eligibility or covariates. For a crossing infusion, use observed positive rate times elapsed duration through tau; never prorate a future final total. Boluses occur at `starttime`.

Decision-available measurements in `chartevents,outputevents,labevents,emar` and optional radiology require clinical/chart time <=tau and nonmissing `storetime <=tau`; radiology detail inherits both times from its report. Date-only ICD procedure `chartdate` never enters eligibility or weights. Emit clinical-time-only counts, decision-available counts, late-entry exclusions and arm-specific missingness. Material reversal under charttime-only sensitivity is inconclusive.

Input volume includes delivered `inputevents` rows with coherent keys/times, accepted status and positive mL amount (L x1000), or positive mL/hour rate times elapsed duration for an infusion crossing t0. Exclude dose/mass/electrolyte/unknown units even when `totalamountuom` is mL; `totalamount` is not delivered patient volume. Accepted statuses are `FinishedRunning, ChangeDose/Rate, Stopped, Paused, Bolus`; deduplicate only overlapping segments sharing `orderid/linkorderid`.

Output uses positive `outputevents.value` in mL (L x1000), `charttime in [intime,t0]`, `storetime<=t0`, and dictionary categories Output/Drains with `linksto=outputevents`. Exclude item 227488 (GU Irrigant Volume In), pre-admission item 226633, unknown units and nonpositive values; add 227488 to input only when positive mL and decision-available. Require at least one input and output and no six-hour recording gap before t0. Complete-hour coverage and +30/+100 mL/kg thresholds are sensitivities.

Weight is the earliest valid decision-available kg measurement in `[intime-6h,intime+24h]`, preferring 226512 then 224639. Convert 226531 lb/2.20462 only after dictionary/value confirmation. Exclude primarily if absent; `inputevents.patientweight` is sensitivity only. Emit source, times, conversion and >10% competing-weight disagreement.

### Strategies, cloning, overlap and trajectories retained

Strategy A is first qualifying actually delivered ICU IV furosemide 221794/228340 or bumetanide 229639 in `(t0,t0+24h]`. Strategy B is no actual furosemide, bumetanide, torsemide or ethacrynic acid by any route in that interval. ICU delivery requires coherent clinical/start/end/store times, accepted delivered status and positive dose convertible to mg or positive mg/hour over positive duration. Exclude canceled, rewritten, not-started, order-only, nonpositive and unknown-unit rows; deduplicate only overlapping same `orderid/linkorderid` segments.

For any-route washout/deviation, join `hosp/emar_detail` to `hosp/emar` on `subject_id,emar_id,emar_seq`, inherit `hadm_id,charttime,storetime`, and accept actual-administration text with positive dose/product amount. Blank route is unknown, never IV. Same-drug ICU/eMAR events within 15 minutes are concordant evidence, not two doses. Report concordant-ICU and explicit-IV-eMAR sensitivities.

Clone each eligible patient to A and B at t0. Censor each clone at first recorded strategy deviation through 24 hours; death before the grace-window end remains a competing outcome, never censoring. ICU exit before A initiation censors A if it precedes death or live hospital discharge. For the repaired endpoint, live hospital discharge is a terminal primary event, not “loss to follow-up” and not B censoring; adherence is evaluated only until `min(t0+24h, death, live discharge)`. Events before a strategy has deviated are retained according to clone-grace rules. Post-hour-24 care is unrestricted. Report only the weighted per-protocol contrast as decision-relevant; crude initiator and all-eligible associations are descriptive.

The target population is unchanged: measured overlap defined before outcome inspection by estimated 24-hour A-initiation probability `0.10 <= e(X) <= 0.90`, conditional only on decision-available pre-t0 demographics, admission type/year/unit/service, prior completed-admission comorbidity and loop exposure, weight, cumulative balance and six-hour slope, urine rate/slope, creatinine/lactate/potassium and slopes, MAP/pressor history and cessation time, FiO2/PEEP/support trajectories, sedation, crystalloid/albumin, prior oxygenation and validated time-eligible radiology flags. Summaries at t0 and t0-3/-6/-12h include missingness indicators. Index-discharge diagnoses, future notes and endpoint components are prohibited.

Use overlap weights for the baseline target and stabilized inverse-probability adherence/censor weights, updated hourly from lagged decision-available respiratory, hemodynamic, renal, fluid, sedation and imaging histories; truncate at 1st/99th percentiles. Treatment-confounder feedback belongs in censor weights, not baseline adjustment. Report calibration, overlap distributions, standardized differences and positivity by prespecified respiratory, renal and hemodynamic trajectory strata. Retain the parent's residual-indication grid: the minimum prevalence/odds-ratio strength of an unmeasured binary clinical-readiness factor needed to move the primary RD to 0 and +0.05, with pre-t0 physiologic slopes as negative-control outcomes. This is not proof of exchangeability.

Any arm with <100 adherent subjects, ESS <75, >10% eligible person-hours with treatment probability <0.01 or >0.99, large mass outside overlap, post-weight trajectory imbalance >0.10, or failed pre-t0 temporal falsification makes the per-protocol interpretation infeasible/inconclusive.

## Repaired endpoint and estimands

### Primary estimand: competing-risk LHD28

For the index `hadm_id`, define live discharge time as `admissions.dischtime` when `hospital_expire_flag=0`. Primary success is

`Y_LHD28 = 1{t0 < dischtime <= t0+28d AND hospital_expire_flag=0}`.

All remaining patients have `Y_LHD28=0`, including death before live discharge, discharge after day 28 and continued index hospitalization at day 28. No absence of a later death record is used. `discharge_location`, `deathtime`, and `patients.dod` are consistency/safety fields, not silent substitutions for the primary flag.

In-hospital death before live discharge is the competing event. Because the source audit found 745/546,028 admissions with `deathtime > dischtime` and 11 expire-flag admissions missing `deathtime`, emit both timestamps and use two prespecified event-time conventions for `hospital_expire_flag=1`: primary `deathtime` when present (otherwise `dischtime`), and administrative-time sensitivity `dischtime`. Boundary disagreements at day 28 are bracketed. They cannot change an expire-flag admission into live discharge.

The primary estimand is

`psi_LHD28 = CIF_A^LHD(28) - CIF_B^LHD(28)`

in the measured-overlap population under the sustained 24-hour strategies, where death before live discharge is competing and no event by day 28 is the third state. This is a per-protocol standardized risk difference conditional on the recorded-data assumptions. The directly supported computational claim is the weighted MIMIC association under the specified emulation, not a causal bedside effect.

Estimate absolute day-28 risks with a subject-level cross-fitted augmented inverse-probability estimator using overlap and adherence/censor weights. Separately emit weighted Aalen–Johansen live-discharge, death and no-event state probabilities at days 7, 14 and 28, plus cause-specific hazards; do not substitute a Kaplan–Meier curve that censors deaths. Use at least 500 subject bootstraps for percentile and normal-based 95% intervals and report risk ratio/number-needed-to-treat only as secondary transforms when mathematically stable.

### Fully observed timing and destination sensitivities

Report **restricted mean time not yet live-discharged through day 28**,

`RMTNLD28 = integral_0^28 [1 - CIF_LHD(t)] dt`,

with A-minus-B contrast; negative is favorable. A death remains not live-discharged through day 28. Do not rename this “hospital-free days,” “days alive out of hospital,” or survival time, because post-discharge state is unavailable.

Repeat LHD at 14 and 60 days. Display destination-specific cumulative incidence using `discharge_location`: home/home health; SNF/rehab/assisted living; LTAC/acute hospital; hospice; AMA/other/missing. A strict sensitivity treats hospice, acute-hospital transfer and LTAC as non-success; missing destination is failure, then a best/worst bound. A supportive interpretation fails if the apparent benefit is wholly attributable to hospice/acute/LTAC discharge or destination missingness.

A recorded index-hospital ICU secondary uses the union of linked half-open `icustays [intime,outtime)` intervals. Define the first positive gap after t0 as ICU exit; success is live ICU exit by day 7 with no later linked ICU interval beginning before `min(t0+7d,dischtime)`. Death by day 7 and remaining in ICU at day 7 are failures. Live hospital discharge closes index-hospital observation but does not establish freedom from outside-hospital ICU readmission. Report this endpoint only as “recorded live ICU exit without index-hospital ICU readmission by day 7.”

### ALDL7 and safety retained

ALDL7 remains a key observation-bounded respiratory secondary with the parent's exact bounds. Use the union of linked ICU intervals; never bridge a positive gap, ward interval or discharge by absence of procedures/notes. Extubation items 227194/225468/225477 and intubation 224385 require `FinishedRunning`; invasive ventilation 225792 accepts `FinishedRunning/Stopped`. Death in `(t0,t0+7d]` is definite failure. Definite success requires accepted extubation by day 5, continuous ICU observation through day 7, survival and no recurrence. Continuous observation without liberation is failure; otherwise `L=0,U=1`. Compute weighted `pA_L,pA_U,pB_L,pB_U` and `RD_L=pA_L-pB_U, RD_U=pA_U-pB_L` with subject bootstrap. Unknown is never success. ALDL7 no longer controls primary endpoint observability, but a clearly adverse identified respiratory result blocks a favorable mechanistic interpretation.

Preserve recorded 28-day death as a separate safety endpoint. Use exact `admissions.deathtime` for in-hospital death and date-bracketed `patients.dod` when it falls after discharge; absence of `dod` is “no additional recorded death,” not known survival. Report in-hospital and any-recorded mortality separately. Preserve observed new RRT through day 7: ICU items 225441/225802/225803/225805/225809/225955 with delivered status; hospital dialysis ICD-9 3995/5498 and dictionary-confirmed ICD-10 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z, excluding access/imaging. Date-only `chartdate` uses lower/upper boundary brackets and competing death. A null is no detected excess recorded RRT, not renal safety.

Secondary process/clinical outcomes remain VFD28 bounds, documented extubation/recurrence, ICU-free time, hospital LOS, 24/48-hour balance/urine, creatinine/potassium/KDIGO, MAP<55 and new pressor.

## Falsification, sensitivity and result branches

Before outcome fitting, emit sequential attrition, all timestamp/unit/status exclusions, strategy/deviation evidence, terminal events during grace, overlap, weights, ESS, destination/mortality conflicts, ALDL7 classes and all model-ready rows.

Validity checks remain: eventual strategy must not predict pre-t0 six-hour creatinine, urine or MAP slopes after adjustment (absolute standardized difference >0.10 or multiplicity-controlled P<0.05 blocks causal language); all prespecified trajectories must balance to <=0.10; 24-hour urine/balance should respond in the exposure-process direction but cannot establish clinical benefit. Repeat inherited washout/initiation, never-treated, balance/coverage, weight, ventilation/extubation, fluid, cardiac/heart-failure, KDIGO, albumin, era, first-ICU, eMAR concordance and overlap-threshold sensitivities.

Endpoint-specific checks require: no primary event at/before t0; `dischtime` completeness and admission-order coherence; arm-specific conflict rates among `hospital_expire_flag,deathtime,dischtime,discharge_location`; both hospital-death time conventions; destination decomposition; 14/60-day horizons; RMTNLD28; recorded ICU-exit sensitivity; and ALDL7 bounds. >1% missing/impossible admission endpoints, >2 percentage-point arm difference in endpoint conflicts/missing destination, a boundary-bracket conclusion change, or reversal after excluding hospice/acute/LTAC makes the result inconclusive. Discharge practice, goals-of-care and clinical-readiness residual-bias analyses are mandatory.

**Supportive:** `psi_LHD28` point estimate >+0.05 with 95% lower limit >0; upper 95% excess any-recorded day-28 death <+0.03; upper 95% excess observed RRT <+0.05 under both date brackets; overlap/adherence/ESS, balance, temporal and endpoint-integrity gates pass; RMTNLD28 favors A; destination decomposition does not show benefit solely from hospice/acute/LTAC transfer; and no material conflict appears across trajectory, exposure, horizon, death-time or ALDL7 sensitivities. Only a 95% lower limit above +0.05 supports the magnitude threshold itself; otherwise the branch supports a positive association of clinically material point-estimate size for trial prioritization. It does not support >28-day survival, causality or prescribing.

**Adverse/falsifying:** with validity gates passed, the 95% upper limit for `psi_LHD28` is <=+0.05, falsifying the prespecified clinically consequential >5-point claim; label separately whether it still permits a smaller positive association. A 95% upper limit <=0 is evidence against any LHD28 benefit. Independently, a 95% lower limit for excess recorded death >=+0.03, observed RRT >=+0.05, or the 95% upper confidence limit for ALDL7 `RD_U` <=0 is a respiratory harm signal. Faster diuresis cannot override these results.

**Inconclusive:** the LHD28 interval includes +0.05 while support fails; a safety upper gate fails without clear harm; overlap, adherence, ESS or events are sparse; endpoint/date/destination conventions disagree; unmeasured-confounding strength needed to reverse the finding is modest; trajectory restriction changes the branch; two-clock or exposure sensitivities conflict; or temporal falsification fails. Nonsignificance is not equivalence, safety or absence of benefit.

## Exact MIMIC bindings and source audit

Read-only source: `[internal dataset path]`, [source checksum], archive root `mimic-iv-3.1/`, snapshot `[source checksum]`, catalog [source checksum].

Required members/columns are:

- `hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,hospital_expire_flag,discharge_location,admission_type,race`; `hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,dod`.
- `icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime`; `hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,patientweight,statusdescription,totalamount,totalamountuom`.
- `icu/outputevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom`; `icu/d_items.csv.gz`: `itemid,label,linksto,category,unitname`.
- `icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription,continueinnextdept`; `icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; optional `icu/datetimeevents.csv.gz` only for dictionary-confirmed datetime variables.
- `hosp/labevents.csv.gz`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom,flag`; `hosp/d_labitems.csv.gz`: `itemid,label,fluid,category`.
- `hosp/emar.csv.gz`: `subject_id,hadm_id,emar_id,emar_seq,charttime,storetime,medication,event_txt`; `hosp/emar_detail.csv.gz`: `subject_id,emar_id,emar_seq,administration_type,complete_dose_not_given,dose_given,dose_given_unit,product_amount_given,product_unit,product_description,route,infusion_rate,infusion_rate_unit`.
- `hosp/procedures_icd.csv.gz`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; `hosp/d_icd_procedures.csv.gz`: `icd_code,icd_version,long_title`; diagnoses/dictionaries only for prior completed-admission covariates.

Join ICU tables on `subject_id,hadm_id,stay_id`, hospital tables on `subject_id,hadm_id`, patients on `subject_id`, eMAR detail on `subject_id,emar_id,emar_seq`, and dictionaries on item or ICD code/version. Within-subject shifted intervals are valid; cross-subject dates are not.

Optional radiology/discharge notes remain separate read-only ordinary gzip files with the parent's exact paths/hashes; notes never define LHD28 or survival and future discharge notes are prohibited from predictors. All four configured datasets (MIMIC, EICU, HCC, UKB) remain directly available read-only through their catalog guides; this experiment requires MIMIC only and does not alter or copy any source. Derived scripts/results stay in the workspace.

The endpoint audit ran as job `[research job]` using `endpoint_audit_e12.py` [source checksum]; output `endpoint_audit_e12.json` [source checksum]. It inspected the listed archive rows and exact headers. It intentionally did not apply final shock, fluid, renal, washout, overlap or treatment rules.

## Required outputs and verifier boundary

The executable Harbor job must emit row-level cohort/clone data, partition/checksum, attrition, temporal provenance, unit-safe balance and weight components, exposure/deviation/grace events, overlap/propensity/adherence diagnostics, trajectory strata, weights/ESS, the three-state day-28 endpoint classification, both death-time conventions, destination categories, recorded mortality/RRT, ALDL7 intervals, RMTNLD28, bootstrap draws, residual-bias grid and final branch. Every reported number and conclusion must link to these outputs.

The verifier can check hashes, headers, joins, partition, clocks, units, eligibility, strategy delivery, clone censoring, overlap, trajectories, endpoint classification, competing-risk/AIPW arithmetic, death-time brackets, destination sensitivities, ALDL7 bounds, safety gates, uncertainty and whether supportive/adverse/inconclusive language follows the computed outputs. It must test correct computation paired with unsupported conclusions: calling live discharge day-28 survival; calling RMTNLD hospital-free or alive-out-of-hospital days; censoring deaths in Kaplan–Meier; treating ALDL7 unknown as success; treating discharge to hospice/acute transfer as unqualified recovery; calling absent recorded RRT renal safety; or making a causal treatment recommendation must fail.

The verifier cannot establish true survival after discharge, external readmission, destination appropriateness, clinical extubation/dialysis truth, completeness of death/RRT capture, bedside awareness, clinician intent/readiness, goals of care, discharge-policy effects, exchangeability, transportability, patient preferences, causal truth or net clinical utility. These need clinical adjudication, external linkage/validation and preferably randomization.

## What changed and what remains uncertain

Changed: LHD28 replaces ALDL7 as the primary endpoint; death is a competing event; a fully recorded restricted-mean timing summary and destination sensitivities prevent “hospital-free survival” overclaiming; live hospital discharge is terminal rather than adherence censoring; and ALDL7 becomes a bounded mechanistic secondary. The source audit demonstrates a large observability gain without claiming a treatment effect.

Unchanged: scientific population, t0, 24-hour strategies, measured-overlap estimand, trajectory-aware clone-censor weighting, residual-confounding diagnostics, two clocks, unit-safe fluid/weight rules, mortality/RRT gates, exact source provenance and observational limits.

Still uncertain: final eligible size, overlap, adherence, treatment effects, unmeasured readiness/goals of care, discharge-policy confounding, destination meaning, post-discharge survival/readmission and true renal/respiratory outcomes. Those uncertainties can make this study inconclusive and cannot be solved by a more complex model.
