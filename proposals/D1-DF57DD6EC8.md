# Episode 20: eMAR-observable post-shock loop initiation with a single terminal-state resolver

**Parent:** `[prior hypothesis]`

## Why a substantive child is required

This child preserves the hour-48 post-shock delivered-loop question, fluid/weight phenotype, two-clock retrospective ventilation repair, 24-hour grace period, overlap-targeted clone-censor analysis, ANHATD28 outcome, bounded recorded-harm outputs, margins, and strict noncausal boundary. It repairs two source-demonstrated defects that remain in Episode 19.

First, arm B is called “no actual loop by any route,” but its only all-route administration source is `hosp/emar`. In an unchanged, treatment-blind audit of the 7,733 first adult discovery-partition landmarks with a completed/stopped invasive-ventilation interval spanning `t0`, only 4,242 (54.9%) index admissions had any eMAR row, 3,885 (50.2%) had a clinical-time eMAR row by `t0`, and 3,884 (50.2%) had one with both `charttime<=t0` and `storetime<=t0`. Coverage ranged from 23.2% in `anchor_year_group=2008 - 2010` to 98.1% in `2020 - 2022`. Absence of a loop row in the remaining admissions cannot mean no administration. The 1,298 broad landmarks with a raw loop-name eMAR row during grace are label matches before detail/dose adjudication, not exposures or effects.

Second, the parent requires only `icustays.outtime>t0`. The same audit found 70/7,733 broad landmarks with `admissions.dischtime<=t0`, and many postbaseline administrative contradictions: 156 `deathtime>dischtime`, 43 live-flag rows with destination `DIED`, 19 death-flag rows with another destination, and five death-flag rows missing `deathtime`. These require one executable admission-state resolver shared by assignment closure and outcomes.

The audit read all rows of `patients`, `admissions`, `icustays`, `procedureevents`, and `emar` needed for discovery buckets 0–79; it did not inspect treatment-detail rows, apply shock/fluid/renal eligibility, estimate adherence, or inspect outcomes by strategy. Script `episode20_observability_audit.py` SHA-256 is `[source checksum]`; output `episode20_observability_audit.json` SHA-256 is `[source checksum]`. These are observability counts, not treatment evidence.\n\nA second treatment-blind audit applied the exact resolver below. After excluding the 70 baseline-impossible timelines, 305/7,663 landmarks closed assignment during `(t0,G]`: 248 valid death times, 20 death-flag dischtime fallbacks, and 37 live-flag discharges (31 valid and six invalid outcome states); one closure was exactly at G. Across follow-up, 141/2,248 death states required dischtime fallback, including 136 with deathtime after dischtime and five with missing deathtime. Script `episode20_terminal_resolver_audit.py` SHA-256 is `[source checksum]`; output SHA-256 is `[source checksum]`. These counts establish exposure to resolver choices, not effects.

The repair makes baseline all-route administration observability explicit, calls arm B “no **recorded** administration,” excludes impossible admission timelines, and uses one deterministic death/discharge resolver. An all-era ICU-only contrast is mandatory but cannot rescue the primary all-route-recorded claim.

## Evidence boundary and hypothesis

Relevant passages were inspected in the frozen full XML of McMullan et al.’s 2026 RADAR-2 secondary analysis (DOI `10.1097/CCE.0000000000001404`; source `[source checksum]`). The trial secondary analysis compared a conservative-fluid plus active-deresuscitation bundle with usual care, found no statistically detectable between-group differences in lactate, AKIRisk, urinary cystatin-C, or vascular-injury biomarkers, and explicitly notes modest size and imprecision. Relevant full-text XML passages were also inspected for Wang et al.’s operational EHR target-trial review (DOI `10.1038/s41746-026-02563-z`; source `[source checksum]`) and Garcia-Albeniz et al.’s grace-period study (DOI `10.1002/cam4.71950`; source `[source checksum]`). They support data-constrained trial realization and retention of early outcomes, not the clinical effect here.

**Strongest supported claim:** a protocolized conservative-fluid/active-deresuscitation bundle can change fluid management without a detected biomarker-harm signal in a modest randomized study; grace-period analyses that condition on surviving long enough to initiate can be biased. This does not establish benefit, renal/respiratory/mortality safety, or the effect of isolated loop initiation.

**Unresolved falsifiable hypothesis:** among baseline eMAR-observable, mechanically ventilated adults meeting the prespecified post-shock readiness/fluid phenotype and measured overlap, assignment at `t0` to initiate a qualifying ICU-recorded delivered furosemide/bumetanide event before the earlier of 24 hours or an assignment-closing index-hospital event, versus no recorded furosemide/bumetanide/torsemide/ethacrynic-acid administration by any route before the same boundary, increases ANHATD28 by more than 5 percentage points while ruling out more than 3 points higher RTHD28 and more than 5 points higher observed RRT through day 7.

The advance is a specific, delivery-coherent post-shock decision rather than a fluid bundle, with source-observable assignment and competing events. A supportive result prioritizes external validation and a pragmatic trial only.

## Frozen source, partition, and joins

Use read-only MIMIC-IV 3.1 snapshot `[source checksum]`:

`[internal dataset path]`

Source [source checksum]. Catalog [source checksum]. Every core member below is under `mimic-iv-3.1/`.

Before inspecting eligibility compute
`bucket=int(SHA256("ehr-hypothesis-discovery-v1"+NUL+"mimic"+NUL+canonical_base10(subject_id))) mod 100`.
Use buckets 0–79 only and never inspect 80–99. Emit namespace, canonical ID, digest, and bucket. Evaluate ICU stays chronologically and retain the first qualifying stay per subject. All folds and bootstraps are by subject, never clone.

Primary joins are `patients.subject_id=admissions.subject_id`; `icustays.(subject_id,hadm_id)` to admissions; ICU events on `subject_id,hadm_id,stay_id` with dictionary on `itemid`; eMAR to every detail sibling on `subject_id,emar_id,emar_seq` while retaining `parent_field_ordinal`; hospital diagnoses/procedures/services/transfers on `subject_id,hadm_id`. Assert one admissions row per `hadm_id`, matching subjects on every joined key, and an ICU-event time compatible with the linked stay; emit rather than silently repair violations.

## Population, clocks, and eligibility

Set `t0=icustays.intime+48h`; require nonmissing `intime,outtime`, `intime<=t0<outtime`, and `admissions.admittime<t0<admissions.dischtime`. Age is `patients.anchor_age+year(admissions.admittime)-patients.anchor_year>=18`.

Retrospectively reconstruct invasive ventilation at `t0` from `icu/procedureevents` item 225792 (audited dictionary label “Invasive Ventilation”): valid keys; nonmissing `starttime,endtime,storetime`; `starttime<endtime`; `starttime<=t0<endtime`; final `statusdescription` in `FinishedRunning,Stopped` (`Paused` sensitivity). This is the parent’s single baseline-state exception: `storetime` may exceed `t0`. In analytical files retain only the Boolean; prohibit post-`t0` duration, exact future end, final status changes, or store lag from eligibility beyond interval crossing, covariates, overlap, censoring models, effect modification, prognosis, or outcomes. Keep raw provenance and lag only in an audit table. Report the strict `storetime<=t0` count separately.

Require baseline eMAR observability without using a loop label: at least one `hosp/emar` row on the index `subject_id,hadm_id` with `admittime<=charttime<=t0`, nonmissing `storetime<=t0`, and at least one matching `emar_detail` sibling. Emit exclusions by `patients.anchor_year_group`. This proves source presence, not completeness, and creates a documented-medication subpopulation; transport beyond it is not claimed.

Before assignment require:

- positive delivered vasopressor before `t0-6h` and none overlapping `(t0-6h,t0]`, from `inputevents` items 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315;
- median MAP at least 65 mmHg in `(t0-3h,t0]`, `chartevents` 220052/220181/225312;
- cumulative unit-safe fluid balance at least +50 mL/kg from ICU `intime` through `t0`;
- decision-available weight 30–300 kg;
- urine output greater than 0.1 mL/kg/hour in `(t0-6h,t0]`, summing positive mL/L `outputevents.value` only for dictionary-confirmed items 226559 Foley, 226560 Void, 226627 OR Urine, 226631 PACU Urine, and 226713 Incontinent/void estimate; mixed urine/irrigant items 226566 and 227489 are excluded;
- latest numeric potassium `labevents.itemid` 50971 or 52610 in `(t0-12h,t0]` at least 3.0 mmol/L;
- no decision-available active ECMO, defined as positive numeric L/min flow in `chartevents` item 224660, 229270, or 229842 during `(t0-2h,t0]` with `storetime<=t0` (six-hour window sensitivity); no exact-timed delivered RRT `procedureevents` item 225441/225802/225803/225805/225809/225955 with `starttime<=t0<endtime`, final `FinishedRunning/Stopped`, and `storetime<=t0` (report a retrospective-final-state sensitivity); and no recorded loop administration by the ICU/eMAR union in `(t0-12h,t0]`.

Physiology, covariates, and censor-model histories require clinical/event time at or before their boundary and nonmissing `storetime` at or before that boundary. Two retrospective ascertainment exceptions are explicit: the masked ventilation Boolean, and delivered-loop classification (including the 12-hour washout), which uses the clinical event time but may use later final status/detail to decide whether delivery occurred. Neither exception is a prospective EHR decision rule. Emit clinical-only, two-clock-available, retrospectively confirmed, late-confirmed, and excluded counts.

Fluid input is positive delivered `inputevents.amount` in mL (L ×1000); recognized mL/hour infusions crossing a boundary accrue only to the boundary. Never convert drug mass/dose, mcg, units, mEq, mmol, unknown units, or `totalamount` to fluid. Accepted final statuses are `FinishedRunning,ChangeDose/Rate,Stopped,Paused,Bolus`; deduplicate overlapping segments only within `orderid/linkorderid`. Output is positive `outputevents.value` in mL (L ×1000), with `charttime,storetime<=boundary`, `d_items.linksto=outputevents`, and a frozen Output/Drains category set, excluding item 227488 and pre-admission item 226633. Decision-available positive-mL item 227488 is input. Require at least one valid input and one valid output. Sort accepted fluid-record clinical times from `intime` through `t0`, insert both endpoints, and require no adjacent gap over six hours; report this strict gate and a terminal-six-hour-only sensitivity. Emit every included item/unit/conversion.

Weight is earliest decision-available kg in `[intime-6h,intime+24h]`, hierarchy 226512 then 224639; item 226531 is pounds divided by 2.20462 only after unit confirmation. `inputevents.patientweight` is sensitivity only.

## Recorded interventions and assignment-closing state machine

Let `G=t0+24h`.

**A, initiate:** the first qualifying `icu/inputevents` event with clinical `starttime in (t0,G]` and before terminal closure, item 221794, 228340, or 229639 (audited labels furosemide, furosemide 250/50, bumetanide); same subject/index admission; `stay_id` linked to an ICU stay containing the start; nonmissing start/end/store; status `FinishedRunning,ChangeDose/Rate,Stopped`; and either positive `amount` with mg-convertible `amountuom`, or positive mg/hour `rate` over `endtime>starttime`. `Paused` is sensitivity. Unknown units, nonpositive values, canceled/not-started rows, and orders are not delivery. A positive mg bolus need not be assigned an invented duration.

**B, avoid recorded loop:** no recorded administered furosemide, Lasix, bumetanide, Bumex, torsemide, Demadex, ethacrynic acid, or Edecrin by any route before the same boundary. Normalize `emar.medication` and `emar_detail.product_description` with Unicode NFKC, casefolding, punctuation-to-space, whitespace collapse, and token-boundary matching to that frozen list. An eMAR event is administered only when `event_txt` normalizes to `Administered, Delayed Administered, Administered in Other Location, Partial Administered, Started, Started in Other Location,` or `Restarted`, and at least one detail sibling has positive numeric `dose_given` or `product_amount_given` with that sibling’s trimmed/case-folded `complete_dose_not_given` not in the frozen affirmative set `{1,true,t,yes,y}`. Aggregate siblings once per `subject_id,emar_id,emar_seq`; missing route still violates B. Use `charttime` as the recorded clinical clock, never `scheduletime`; `storetime` is the documentation clock. Orders in `prescriptions/pharmacy` are diagnostics only.

Aggregate concordant ICU/eMAR evidence before transition ordering. A qualifying ICU event satisfies A and censors B once. Any other recorded loop before A satisfaction censors both unsatisfied A and B. Final facts may confirm delivery retrospectively, but timing remains clinical `starttime/charttime`; report store lag and a contemporaneous-storetime sensitivity.

Resolve assignment-closing `T` only from `admissions`, never date-only `patients.dod`:

1. Baseline already requires `admittime<t0<dischtime`.
2. If `hospital_expire_flag=1` and `t0<deathtime<=dischtime`, set `T=deathtime`, death.
3. If `hospital_expire_flag=1` but that death time is missing/invalid, set `T=dischtime`, recorded-death fallback, and emit the anomaly reason.
4. If `hospital_expire_flag=0`, set `T=dischtime` for every destination. A nonmissing `deathtime`, missing destination, or exact `DIED` destination makes the day-28 state invalid but does not prevent shared assignment closure.
5. Invalid flags/links or no defensible post-`t0` exact endpoint are ineligible/infeasible, never imputed. `icustays.outtime` is not hospital discharge.

Clone to A and B at `t0`. Use exact event times; hourly rows are model intervals, not coarsened transition times. At ties: `T` first, qualifying A second, other loop third, G last; reverse terminal/treatment ties in sensitivity. If `T<=G` occurs while a clone is compatible, mark `closed_by_terminal_while_compatible`, retain its outcome, do not censor or assign it to B, and ignore later medication. Otherwise qualifying A satisfies A/censors B; earlier other loop censors unsatisfied A and B; at G censor unsatisfied A and complete loop-free B. Stop exposure censoring after A satisfaction. Emit one event row and one clone-hour row with prior/next state, exact clinical/store times, provenance, probability, terminal category, satisfaction, and censor reason.

Report ICU exit before G and A-compatible hours outside any ICU because qualifying ICU delivery is then structurally unobservable. A secondary ICU-availability estimand closes both requirements at first ICU exit and retains both compatible clones; it is not the primary and cannot rescue it.

## Estimand and analysis

The primary data-defined estimand is the A-minus-B ANHATD28 risk difference in the eMAR-observable baseline population whose cross-fitted baseline probability
`e0(X0)=P(qualifying A before other recorded loop, T, or G | X0)`
lies in `[0.10,0.90]`. Estimate this competing-risk probability from baseline variables only. Never use realized treatment, T, destination, or outcomes to select overlap. Apply common tilt `e0(1-e0)` identically to both clones.

Fit arm-specific, subject-cross-fitted pooled-logistic artificial-censoring hazards using prior decision-available history. Denominator is `Pr(no strategy-deviation censor in j+1 | compatible through j,Hj,arm)`; numerator uses frozen baseline only. Terminal closure is a competing outcome, not censoring. Stop weight multiplication at A satisfaction, T, artificial censoring, or B completion. Truncate cumulative stabilized weights at the 1st/99th percentiles and report untruncated results.

Prespecified variables are demographics; `anchor_year_group`, admission type/era, service/care unit and transfer location; prior completed-admission diagnoses and recorded loop exposure; weight; fluid-balance and urine trajectories; creatinine, potassium, lactate; MAP, pressor dose/cessation; FiO2, PEEP, oxygenation/ventilation measurements; sedation; crystalloid/albumin; procedures; and missingness. Later diagnoses, notes, response, terminal destination, and outcomes are forbidden predictors.

Report four baselines: crude observed strategies; common-overlap clone risks without artificial-censor weights; overlap-plus-clone-censor risks; and observed-odds multipliers 0.5/0.75/1/1.33/2, labeled stochastic-policy sensitivities. Also report an all-era symmetric ICU-only contrast in which B means no ICU-inputevent loop; it cannot be described as all-route or used for the primary branch. Use at least 500 subject bootstraps rerunning folds, overlap, models, truncation, and outcomes. Report calibration, standardized differences, arm/event/terminal counts, eMAR attrition, route/missing-route, lag, ICU exit, probability/weight tails, ESS, negative-control pre-`t0` slopes, and the frozen readiness/goals-of-care tipping grid.

## Bounded outcomes

At `H28=t0+28d`, apply the same resolver to exactly one index-admission state: recorded death by H28; exact `HOSPICE`; exact `ACUTE HOSPITAL`; recorded alive other destination; prolonged hospitalization beyond H28; invalid/discordant. ANHATD28 is recorded alive non-hospice/non-acute discharge by H28. Report any-live discharge, exact HOME/HOME HEALTH CARE, chronic/LTAC-as-failure, all destinations, days 14/21, era/service/unit, anomaly-excluded, same-system readmission, and recorded-DOD sensitivities. Discharge is not recovery, function, or survival.

RTHD28 lower is recorded index death or exact HOSPICE by H28. Its upper additionally treats invalid/discordant states as harmful. Acute-hospital transfer fails ANHATD but is not RTHD without death/hospice evidence. For every bounded binary outcome compute arm `pL,pU` and sharp effect interval `DeltaL=pA_L-pB_U`, `DeltaU=pA_U-pB_L`, with one-sided bootstrap limits.

True day-28 mortality is mandatory. Exact resolved in-hospital death by H28 is definite. Treat date-only `patients.dod=d` as `[d 00:00,d+1d)`: full containment before H28 is definite death; intersection is possible death; DOD beginning at/after H28 is known no death by H28. A flag-live patient continuously hospitalized through H28 is known alive then. A live discharge before H28 with missing DOD remains `[0,1]`. Report bounds, widths, and unknown fractions; no mortality-safety claim is allowed.

ALDL7 is favorable and bounded: accepted extubation item 227194/225468/225477 with final `FinishedRunning` by `t0+5d`, continuous linked-ICU observation through day 7, no subsequent invasive-ventilation 225792 or intubation 224385, and recorded survival through day 7 gives lower=upper=1. Resolved death by day 7 or continuous observed nonliberation gives 0; observation gaps/early nonterminal discharge or transfer give [0,1]. Death takes precedence.

Observed RRT through day 7 is harmful, not new RRT/AKI. Exact ICU evidence is `procedureevents` 225441/225802/225803/225805/225809/225955 with `starttime in (t0,t0+7d]`, final `FinishedRunning/Stopped` (`Paused` sensitivity). Hospital evidence is `procedures_icd` ICD-9 3995/5498 or ICD-10 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z, dictionary-confirmed. Treat `chartdate` as a full-day interval: full containment is lower evidence, any horizon intersection upper evidence. Deduplicate and report prior-timed, earlier-date, same-date-indeterminate, and no-prior strata. Death/discharge is a competing state, never proof of renal safety.

## Falsification and gates

The >5-point claim is magnitude-supported only if the lower one-sided 95% limit of ANHATD28 RD exceeds +0.05; margin-falsified if its upper limit is at most +0.05; otherwise unresolved.

**Harbor-supportive** requires magnitude support; RTHD28 conservative `DeltaU` upper limit below +0.03; observed-RRT conservative upper-effect upper limit below +0.05; no ALDL7 adverse trigger; no destination reversal; and all source, eMAR, temporal, terminal, unit, overlap, calibration, negative-control, weight, bound, and bias diagnostics passing. It supports trial prioritization only.

**Adverse** occurs if ANHATD28 upper limit is at most 0; RTHD28 `DeltaL` lower limit is at least +0.03; RRT lower-effect lower limit is at least +0.05 under both date brackets; or ALDL7 `DeltaU` upper limit is below -0.05. These are recorded signals, not biological proof.

**Inconclusive** is every other result, including a precise +2-point RD (margin falsification, not no benefit), wide bounds, eMAR-sensitive or ICU-only disagreement, destination conflict, plausible residual-bias tipping, or failed diagnostics.

Declare infeasible/inconclusive before effects if the detail-joined baseline eMAR population is under 200; either strategy has fewer than 100 adherent/compatible-complete subjects; ESS is below 75; more than 10% person-hours have denominator probabilities below .01 or above .99; over 1% eligible rows have unresolved temporal/state contradictions; anomaly imbalance exceeds 10 points; late-confirmation or ICU-exit observability is materially differential; negative controls fail; or state/bound arithmetic does not reconcile. Never silently broaden to eMAR-absent admissions.

## Exact archive bindings and verification

Required members/columns, whose headers were directly inspected, are:

- `hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`.
- `hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`.
- `icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime`.
- `icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,patientweight,statusdescription,totalamount,totalamountuom`.
- `icu/outputevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom`.
- `icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription,continueinnextdept,orderid,linkorderid`.
- `icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname`.
- `hosp/labevents.csv.gz`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom,flag`; `hosp/d_labitems.csv.gz`: `itemid,label,fluid,category`.
- `hosp/emar.csv.gz`: `subject_id,hadm_id,emar_id,emar_seq,charttime,medication,event_txt,scheduletime,storetime`.
- `hosp/emar_detail.csv.gz`: `subject_id,emar_id,emar_seq,parent_field_ordinal,administration_type,complete_dose_not_given,dose_given,dose_given_unit,product_amount_given,product_unit,product_description,route,infusion_rate,infusion_rate_unit`.
- `hosp/procedures_icd.csv.gz`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; `hosp/d_icd_procedures.csv.gz`: `icd_code,icd_version,long_title`.
- `hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; `hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `hosp/diagnoses_icd.csv.gz` plus `hosp/d_icd_diagnoses.csv.gz`: prior completed admissions only. `hosp/prescriptions.csv.gz` and `hosp/pharmacy.csv.gz`: order-only diagnostics.

Optional radiology is the separate read-only `[internal dataset path]` with `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; exclude it unless a frozen timely parser and blinded adjudication are supplied. Images/waveforms are unavailable. HCC, eICU, UKB, and MIMIC remain directly readable through `datasets/README.md`; identifiers are not shared and only MIMIC is analyzed. Sources remain read-only and derived files stay in the workspace.

Required outputs are partition/attrition proof; ventilation raw audit and masked Boolean; eMAR sentinel/detail join coverage; raw two-clock ICU/eMAR evidence and normalized-label dictionary; one subject/clone/event and clone/hour row; terminal resolver/anomalies; fluid/weight components; overlap/weights/ESS; complete outcome states and bounds; bootstrap endpoints; sensitivities; gates; magnitude status; and final branch. Every numerical conclusion must name output fields.

Fixtures must reject eMAR-absent admissions classified as B; a loop-name row without qualifying event/detail evidence; `dischtime<=t0` eligibility; date-only DOD closing grace; post-terminal adherence changes; asymmetric early-event retention; future ventilation duration as a predictor; and correct computations paired with claims of IV route, causality, safety, recovery, survival, or recommended practice. They must accept terminal-first ties, death-time fallback, invalid-live shared closure, and appropriate supportive, adverse, margin-falsified, and sparse/inconclusive interpretations.

The verifier can establish hashes, headers, keys, partition, clocks, item/status/unit rules, eMAR aggregation, state transitions, weights, bounds, margins, arithmetic, and whether a reported computational conclusion follows. It cannot establish complete eMAR capture, actual route when missing, true baseline ventilator physiology, clinician readiness/intent, congestion, goals of care, hospice appropriateness, functional recovery, complete external death/readmission/dialysis, exchangeability, transportability, causal benefit, safety, or treatment recommendation. Those require blinded clinical review, external linkage/validation, expert review, and preferably randomization.
