# Episode 58 v3: explicit measurement-time boundary for the recent-pressor design

Parent: [prior hypothesis].

## Successor defect and substantive repair

The parent correctly repairs the course-window mismatch and the structurally impossible end-confirmed minimum. One remaining clinically consequential defect is temporal observability: its bedside framing and its “decision-available” eligibility language are not valid for the urine and balance gates. The catalogued icu/outputevents member has charttime but no storetime; unlike inputevents, procedureevents, chartevents, and hosp/labevents, it contains no database recording-time field. Therefore a urine amount charted at or before t0 cannot be certified as available at t0. The same limitation applies to any fluid-balance quantity that uses outputevents. A charttime<=t0 rule is a clinical-time/charted-time proxy, not a decision-availability rule.

This can change clinical interpretation: a patient may enter the proposed “hour-48 decision” population because of a retrospectively charted six-hour urine or balance value that was not available when the loop decision was made. The parent’s pressor information-time funnels do not repair this because they do not supply an output availability clock. The treatment/outcome-blind audit analysis/episode58_observability_audit.json records the exact archive members, keys, temporal columns and this finding. No loop rows, endpoint rows, treatment contrast or effect was read for that audit.

The repair is to freeze two meanings rather than conflate them:

1. The feasible primary remains the parent’s retrospective clinical-time, all-eligible, equal-clone recorded-policy estimand. It must be called retrospective throughout and cannot be presented as a bedside decision rule, real-time policy effect, actual receipt comparison, safety result or recommendation.
2. Add a mandatory, non-gating information-time audit of every pre-t0 gate. For inputevents, procedureevents, chartevents, and hosp/labevents, require storetime<=t0 when testing decision observability. For outputevents, report the urine/balance gate as availability not computable because no storetime exists; do not substitute charttime. The fully t0-observable population is consequently not an inferential branch in this snapshot. The audit reports counts and attrition for the pressor/lab/chart portions and explicitly reports the missing output clock.

This is a change to the estimand’s claim boundary, not a treatment-effect estimate. It preserves the parent’s clinically useful retrospective robustness test while preventing a result from being misread as evidence about what was actionable at hour 48.

## Evidence boundary and unresolved hypothesis

The inspected full XML of Bircher et al. 2026 (PMCID PMC13154636, DOI 10.1016/j.aicoj.2026.100075, frozen source [source checksum]) supports that timing, volume, duration and phenotype-guided fluid removal remain uncertain. The inspected Europe PMC record for the 2025 ESICM guideline (PMID 40828463; DOI 10.1007/s00134-025-08058-x) supports only a conditional, limited-evidence setting. The inspected full public HTML of the 65 Trial (PMCID PMC7064880; DOI 10.1001/jama.2020.0930) provides precedent for a prospective pressor-duration judgment, which is unavailable here. These sources support importance and uncertainty, not efficacy, renal safety, a validated six-hour retrospective phenotype, or exchangeability. The unavailable cancer main article and STAR Methods are not claimed as read.

The strongest claim supported by the available MIMIC audit is only that the prior course definition was materially misaligned: 645/764 broad opportunities had at least six all-prior union hours, versus 367/764 with six hours inside (t0-24h,t0-6h]; the separate information-time audit found 196 broad all-prior end-confirmed opportunities and one under its strict all-contributor rule. These are treatment/outcome-blind population and recording facts.

The falsifiable hypothesis is therefore:

> In the namespaced MIMIC population passing the frozen retrospective hour-48 eligibility, the A12 versus B12 recorded-policy association meets the prespecified airway-improvement and renal/terminal-harm bounds, and the direction is not materially reversed by complete-pipeline restriction to a sustained valid pressor course inside (t0-24h,t0-6h].

This is a retrospective association hypothesis. It does not assert that urine, fluid balance, pressor cessation, loop administration, shock recovery, airway independence, renal safety, or treatment intent was known at t0.

## Source, partition and frozen opportunity

Use only MIMIC-IV 3.1 from the read-only archive [internal dataset path], archive [source checksum], snapshot [source checksum]. The catalog is [internal dataset path], [source checksum]. HCC, eICU and UKB remain configured and directly accessible, but are not analyzed or treated as validation cohorts.

Before clinical inspection use SHA256("ehr-hypothesis-discovery-v1"+NUL+"mimic"+NUL+canonical_base10_subject_id) mod 100; retain buckets 0–79 only. Sort icu/icustays by (intime,stay_id) per subject. Freeze the earliest adult stay with t0=intime+48h, inside both ICU and admission, with accepted icu/procedureevents item 225792 crossing t0; never reopen a later stay.

## Exact MIMIC bindings

All joins and times below are fixed to the catalogued archive members.

- icu/icustays / mimic-iv-3.1/icu/icustays.csv.gz: subject_id,hadm_id,stay_id,intime,outtime,first_careunit,last_careunit; join encounters on all three IDs and use intime,outtime for ICU clocks.
- hosp/patients / mimic-iv-3.1/hosp/patients.csv.gz: subject_id,anchor_age,anchor_year,gender,dod; join on subject_id.
- hosp/admissions / mimic-iv-3.1/hosp/admissions.csv.gz: subject_id,hadm_id,admittime,dischtime,deathtime,discharge_location,hospital_expire_flag; join on subject_id,hadm_id.
- icu/procedureevents / mimic-iv-3.1/icu/procedureevents.csv.gz: subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,value,valueuom,statusdescription,orderid,linkorderid; supplies ventilation 225792, extubation 227194, ECMO and procedure/RRT evidence.
- icu/inputevents / mimic-iv-3.1/icu/inputevents.csv.gz: subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,statusdescription; supplies pressors, loop records, fluid input, sedatives and positive-input RRT evidence.
- icu/chartevents / mimic-iv-3.1/icu/chartevents.csv.gz: subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning; supplies MAP, physiology, airway and active-chart RRT evidence.
- icu/outputevents / mimic-iv-3.1/icu/outputevents.csv.gz: subject_id,hadm_id,stay_id,charttime,itemid,value,valueuom; supplies urine/output. It has no storetime; no decision-availability claim may use this member.
- hosp/labevents / mimic-iv-3.1/hosp/labevents.csv.gz: labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom; supplies creatinine 50912 and potassium 50971/52610.
- hosp/procedures_icd / mimic-iv-3.1/hosp/procedures_icd.csv.gz: subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version; date-bracketed RRT evidence.
- hosp/transfers / mimic-iv-3.1/hosp/transfers.csv.gz: subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime; admission/observation topology.
- icu/d_items / mimic-iv-3.1/icu/d_items.csv.gz: itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue; dictionary verification.
- hosp/d_labitems / mimic-iv-3.1/hosp/d_labitems.csv.gz: itemid,label,fluid,category; laboratory dictionary verification.
- hosp/diagnoses_icd / mimic-iv-3.1/hosp/diagnoses_icd.csv.gz: subject_id,hadm_id,seq_num,icd_code,icd_version; prior completed-admission history only.
- hosp/emar and hosp/emar_detail / mimic-iv-3.1/hosp/emar.csv.gz and mimic-iv-3.1/hosp/emar_detail.csv.gz: contamination-only joins on subject_id,emar_id,emar_seq, retaining administration_type,complete_dose_not_given,dose_given,dose_given_unit,product_amount_given,product_unit,product_description,route,infusion_complete,parent_field_ordinal; never use these to relabel ICU input exposure.

The source catalog confirms the exact temporal-column difference central to this repair: storetime is present for inputevents, procedureevents, chartevents and labevents, but absent from outputevents. The local MIMIC metadata also records shifted within-subject timestamps and absent raw waveforms/images; cross-subject calendar alignment and unavailable modalities are not used.

## Retrospective eligibility and course variants

The retrospective primary retains the parent’s exact clinical-time rules: age at least 18; valid pressor delivery in (t0-24h,t0-6h]; no valid or ambiguous pressor intersecting (t0-6h,t0]; median three-hour MAP at least 65; weight 30–300 kg; six-hour urine above 0.1 mL/kg/h; latest 12-hour potassium at least 3.0 mmol/L or mEq/L; unit-safe cumulative balance at least +50 mL/kg with all eight six-hour bins represented; no ECMO; 12-hour loop washout; and no definite/possible active multisource RRT. The +30/+100 mL/kg, weight/observation and inherited sensitivity variants remain mandatory. “Six-hour urine,” MAP, potassium and balance use their inherited item, unit, tie and ambiguity rules; their clinical-time values are not called available at t0.

Pressor IDs are 221289, 229617, 221662, 221749, 229630, 229631, 229632, 221906 and 222315. A valid row has coherent encounter keys, endtime>starttime, status FinishedRunning, ChangeDose/Rate, Rate or Stopped, and positive typed amount or positive typed rate. Exact-deduplicate selected fields. Paused, Bolus, cancelled/order-only, missing-time, nonpositive, contradictory and otherwise unaccepted rows are ambiguous and never add duration. Clinical intervals are half-open [starttime,endtime). In the recent window L=t0-24h,R=t0-6h, clip valid intervals to [max(starttime,L),min(endtime,R)), merge overlapping or touching segments across agents, and sum union duration without double-counting simultaneous agents. Any positive gap breaks contiguity.

Full-pipeline course variants remain: recent-window union ≥1h; recent-window union ≥6h (principal); recent-window maximum contiguous segment ≥6h; all-prior [intime,t0-6h] union ≥6h (provenance only); and recent-window ≥6h using rows with starttime<=storetime<=t0. Each rebuilds eligibility, equal clones, folds, models, weights, endpoints, 1,999 successful subject bootstraps and Holm. The start-confirmed and conservative end-confirmed branches are recording-time stress tests only. They cannot establish real-time knowledge, cessation, receipt or live actionability.

## Information-time audit and no-live-decision rule

In addition to the parent’s post_end_recorded_recent funnel, compute an all_gate_information_time audit among the retrospective opportunities and report each gate’s numerator, missingness and attrition under storetime<=t0 where that field exists.

For inputevents, procedureevents, chartevents and labevents, a row can contribute to this audit only if its storetime<=t0; retain the clinical starttime/endtime/charttime rule separately. For outputevents, report availability_clock_missing=true and do not label charttime<=t0 as decision-available. A chart-time-only urine/balance sensitivity may be shown as a retrospective timing sensitivity, but it is not an information-time branch and cannot restore a live-decision claim. If an external adjudicated output availability field is later supplied, it is a new data-dependent child/study, not a compiler repair.

The primary retrospective pipeline is not invalid merely because output availability is unavailable. It is invalid to interpret it as a t0 bedside policy effect. A decision-observable inferential branch is not computable in this snapshot; do not manufacture a minimum, impute availability, or silently drop the urine/balance gates. If downstream results are reported, their title, tables and conclusion must say “retrospective MIMIC recorded-policy association.”

## Treatment, endpoints, and analysis

Preserve the parent’s treatment-before-airway construction exactly. Loop items are furosemide 221794/228340 and bumetanide 229639 in icu/inputevents. The first qualifying ICU-input start is strictly in (t0,min(t0+12h,C)), where C is the inherited shared airway/terminal closure from the selected same-stay ventilation 225792 and extubation 227194 records. A12 receives the first qualifying recorded loop policy; B12 avoids through the boundary. Equal A/B clones are created for every eligible subject. No post-t0 selection, eventual-initiation label, baseline propensity, overlap restriction, or X0-dependent numerator is allowed.

Preserve bounded RHA-E48-D5, chart/continuous-ICU airway variants, RCR48/RCRD48, multisource RRT7_M/RRTD7, RTHD28, bounded mortality and ANHATD28. Use arm-normalized Hájek means, endpoint states and observation bounds; for a bounded contrast use DeltaL=pA_L-pB_U and DeltaU=pA_U-pB_L. Every mandatory variant independently rebuilds five subject folds, denominator-only numerator-free inverse compatibility weights, 1,999 successful subject bootstraps (PCG64 seed 480048; at most 2,499 attempts; no more than 5% failures) and the eight-family centered-p-value/Holm FWER 0.05 procedure. Minimums remain eligible ≥200, A12 satisfaction ≥100, B12 completion/shared closure ≥100, ESS ≥75 per arm and ≥100 definite primary events. A required inferential variant below a minimum is validity-inconclusive, never evidence for/against treatment and never permission to alter a threshold.

## Falsification and result meaning

A course branch is materially reversed by a directional change, movement of either airway bound ≥0.05, or midpoint sign reversal with both absolute midpoints ≥0.02. Any failed required computation, ambiguity control, positivity/calibration diagnostic, observation bound, renal ascertainment, or recent-window variant is validity-inconclusive. Sparse end confirmation remains a reported measurement limit. The missing output availability clock is a permanent interpretation limit in this snapshot, not adverse evidence.

Supportive-recorded requires the parent’s airway and renal/terminal criteria, feasible valid principal recent-window variants, no material reversal, and all diagnostics passing. It supports external validation or randomization only, and must retain the word retrospective. Adverse-FWER is an adjusted adverse signal with validity passing; it is an observational concern, not toxicity. Margin-falsified rejects only the prespecified recorded-proxy improvement. Other feasible validity-passing results are statistically inconclusive. None establishes benefit, harm, equivalence, safety, causal effect, actual receipt, or a recommendation.

The verifier must check archive/catalog hashes, headers, exact joins, partition, earliest opportunity, clinical interval boundaries, information-time gating, the explicit absence of outputevents.storetime, equal clones, no post-t0 labels, full variant rebuilds, weights, bounds, bootstrap/Holm accounting and output-linked wording. It must reject “decision-available urine,” “live policy,” causal, safety, actual-receipt and recommendation prose. It should test correct computation paired with unsupported conclusions and correct supportive, adverse, margin-falsified, validity-inconclusive, statistical-inconclusive, retrospective-limit and infeasible interpretations.

Automation cannot establish true shock recovery, congestion, perfusion, actual pressor/loop/RRT receipt, airway readiness or durability, KDIGO AKI/renal safety, intent/goals, exchangeability, causality, transportability or actionability. Those require blinded critical-care/nephrology adjudication with fuller notes, imaging/hemodynamics or linked outcomes, external replication and preferably randomization.
