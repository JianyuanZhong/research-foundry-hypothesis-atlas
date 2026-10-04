# Episode 83 integration: first-opportunity, null-safe H120 recorded-topology experiment

Parents: `[prior hypothesis]` and `[prior hypothesis]`.

This child integrates the valid first-broad-hour-48 population repair with the valid null-time/null-key topology repair. It has highest precedence for opportunity enumeration, null and malformed-row handling, care-unit classification, aggregate audit fixtures, and the required downstream rebuild. It preserves the parents' post-shock clinical question, outcome-independent baseline ventilation interval, pause-aware A12/B12 recorded-input strategies, equal-clone noncausal estimand, H120 day-7 endpoint, renal/RRT/death/terminal harms, era and recording-time safeguards, 1,999-bootstrap/Holm analysis, and evidence limits.

## Unresolved question, clinical importance, and evidence boundary

At the first ICU stay in which an adult is still recorded as invasively ventilated at ICU hour 48, recently received vasopressors but has no current recorded vasopressor delivery, is markedly fluid positive, and meets prespecified perfusion, urine, potassium, RRT and ECMO safeguards, is starting or restarting a qualifying furosemide/bumetanide input record during the next 12 hours associated with at least a five-percentage-point increase in being alive and directly observed outside a recorded MIMIC ICU at approximately ICU day 7, without crossing prespecified recorded renal, RRT, death, or terminal-disposition harm margins?

This is consequential because clinicians must decide when to begin active fluid removal after shock, yet a plausible respiratory/de-escalation benefit competes with renal hypoperfusion and confounding by expected recovery. The inspected full XML of Kuriyama et al. 2026 (PMCID `PMC13476641`, DOI `10.1016/j.aicoj.2026.100120`, frozen source `[source checksum]`, retrieved-file [source checksum]) reports 26 randomized trials with 1,652 participants. Comparisons were clinically heterogeneous, largely heart-failure or post-cardiovascular-surgery populations, and most outcome evidence was low or very-low certainty; it does not test initiation/restart versus avoidance in this phenotype. The inspected full XML of Orieux et al. 2026 (PMCID `PMC13218125`, DOI `10.1016/j.aicoj.2026.100083`, frozen source `[source checksum]`, retrieved-file [source checksum]) calls ICU renal congestion hypothesis-generating and says interventional evidence and clinical utility are unestablished. These sources support uncertainty and biologic plausibility, not benefit, safety, the five-point margin, or causality.

The three research-ambition demonstrations were inspected through `references/research-ambition/README.md` for their availability and limitations; they motivate rigor but are not clinical evidence for this question. In particular, no unavailable cancer-paper body or STAR Methods is claimed as read.

The strongest claim supported before the experiment is narrower: the frozen MIMIC snapshot contains the required clocks and fields, first-broad selection changes the broad population materially, and H120 strict topology is more observable than H168 under an explicit null/care-unit contract. No final eligible cohort, treatment contrast, overlap, harm contrast, or effect has been computed.

The unresolved, falsifiable hypothesis is:

> In the frozen final eligible population, the assignment-compatible A12-minus-B12 lower partial-identification contrast for H120 recorded ICU nonoccupancy (`DeltaL_H120`) exceeds +0.05 and its one-sided 95% subject-bootstrap lower confidence limit exceeds +0.05, while every population, exposure, temporal, topology, overlap, model, era, sensitivity and harm gate passes.

A negative, adverse, infeasible, or inconclusive result is scientifically valid.

## Exact data and access

All sources remain read-only. The catalog is `[internal dataset path]`, actual file [source checksum]. It retains direct access to HCC, MIMIC, eICU, and UKB. This experiment analyzes only MIMIC; the other datasets and reserved MIMIC participants are not external validation.

MIMIC snapshot: `[source checksum]`. Read-only archive: `[internal dataset path]`, [source checksum].

Required archive members, catalog tables, columns, joins and clocks are:

- `mimic-iv-3.1/hosp/patients.csv.gz` / `hosp/patients`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; participant and age/era source; join by `subject_id`.
- `mimic-iv-3.1/hosp/admissions.csv.gz` / `hosp/admissions`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; join by `(subject_id,hadm_id)`.
- `mimic-iv-3.1/hosp/transfers.csv.gz` / `hosp/transfers`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; join by `(subject_id,hadm_id)`.
- `mimic-iv-3.1/icu/icustays.csv.gz` / `icu/icustays`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; stay key is all three IDs.
- `mimic-iv-3.1/icu/procedureevents.csv.gz` / `icu/procedureevents`: the three IDs and `starttime,endtime,storetime,itemid,value,valueuom,orderid,linkorderid,ordercategoryname,ordercategorydescription,statusdescription`; V0, airway, ICU RRT and ECMO records.
- `mimic-iv-3.1/icu/inputevents.csv.gz` / `icu/inputevents`: the three IDs and `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,statusdescription,originalamount,originalrate`; pressor, fluid input and loop records.
- `mimic-iv-3.1/icu/chartevents.csv.gz` / `icu/chartevents`: three IDs and `charttime,storetime,itemid,value,valuenum,valueuom,warning`; MAP, weight and inherited ECMO/airway checks.
- `mimic-iv-3.1/icu/outputevents.csv.gz` / `icu/outputevents`: three IDs and `charttime,storetime,itemid,value,valueuom`; urine/output. The inspected catalog and source header include `storetime`.
- `mimic-iv-3.1/hosp/labevents.csv.gz` / `hosp/labevents`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom`; potassium and creatinine; join dictionary `hosp/d_labitems` by `itemid`.
- `mimic-iv-3.1/hosp/procedures_icd.csv.gz` / `hosp/procedures_icd`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; date-only delivered-dialysis evidence; join `hosp/d_icd_procedures` on `(icd_code,icd_version)`.
- `mimic-iv-3.1/hosp/diagnoses_icd.csv.gz` / `hosp/diagnoses_icd`: `subject_id,hadm_id,seq_num,icd_code,icd_version`; baseline history only, with no event-time claim.
- `mimic-iv-3.1/icu/d_items.csv.gz` / `icu/d_items` and `mimic-iv-3.1/hosp/d_labitems.csv.gz` / `hosp/d_labitems`: item dictionaries. Direct inspection confirmed item 225792 is Invasive Ventilation; 221794/228340 are furosemide and 229639 bumetanide; the named MAP, weight, urine, RRT and ECMO IDs below exist with the stated links/units.

All ICU event joins use `(subject_id,hadm_id,stay_id)`; no admission-only event is assigned to a stay. Clinical intervals are half-open. `storetime` is a documentation/completion clock, not proof of clinician awareness or bedside receipt.

## Population and temporal contract

1. Split participants before reading encounters: canonical unsigned base-10 ASCII `subject_id`; retain buckets 0–79 of SHA-256(`ehr-hypothesis-discovery-v1` + NUL + `mimic` + NUL + canonical ID) modulo 100. Buckets 80–99 and every modality belonging to them remain untouched.
2. For every ICU stay of a retained participant, require nonmissing parseable `subject_id,hadm_id,stay_id,intime,outtime` and `intime<outtime`. Define `t0=intime+48h` and require `intime<=t0<outtime`.
3. A broad opportunity also requires exactly one distinct same-three-key `procedureevents` row with `itemid=225792`, status exactly `FinishedRunning` or `Stopped`, parseable `starttime<endtime`, and `starttime<=t0<endtime`. Do not merge rows to manufacture uniqueness. This row is `V0`; its `storetime` is completion-lag audit data only.
4. Among all broad opportunities, select the earliest by `(icustays.intime,stay_id)`. A preceding short, malformed, nonventilated, zero-V0 or multiple-V0 stay does not block the first valid broad opportunity.
5. Only after selection, require one matching admission with parseable `admittime,dischtime` and `admittime<=t0<dischtime`; age `anchor_age + year(icustays.intime) - anchor_year >=18`; and nonmissing accepted `anchor_year_group`. Failure excludes the participant and never reopens a later opportunity.
6. Apply every remaining phenotype gate to this one opportunity, without reopening: accepted pressor delivery during `(t0-24h,t0-6h]` and no valid or ambiguous pressor delivery during `(t0-6h,t0]`; final-three-hour median MAP >=65 mmHg; weight 30–300 kg; final-six-hour urine >0.1 mL/kg/h; most recent recorded potassium through t0 >=3.0 mmol/L; unit-safe cumulative balance from ICU entry through t0 >=+50 mL/kg with all eight six-hour bins observed; no active RRT or ECMO; and no valid or ambiguous loop segment intersecting `(t0-12h,t0]`.
7. Required pressor IDs are 221289, 229617, 221662, 221749, 229630, 229631, 229632, 221906 and 222315. MAP priority is 220052/225312 then 220181; weight priority is 226512 then 224639. Non-irrigant urine IDs are 226557, 226558, 226559, 226560, 226561, 226563, 226564, 226565, 226567, 226584, 226627 and 226631. Potassium is 50971 then 52610. Active ICU RRT uses 225441, 225802, 225803, 225805, 225809 and 225955; hospital dialysis uses ICD-9 3995/5498 and ICD-10-PCS 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z, with lower/upper date brackets because `chartdate` has no time. ECMO uses 229529/229530 plus the frozen chart checks.
8. Clinical-time primary `E_R_pause` uses valid clinical times retrospectively. `E_M_minus_V0` is a complete non-adding sensitivity requiring all other timestamped eligibility/covariate rows to have nonmissing `storetime<=t0` (or clone hour for post-t0 treatment-confounder histories); V0 is excluded because its storetime is a completion clock. Neither cohort supports a live decision-availability claim.

For balance, include only finite nonnegative `inputevents.amount` with volume units convertible to mL and finite nonnegative `outputevents.value` with volume units convertible to mL; exclude mg, dose, units and unknown dimensions. Exact-deduplicate source rows before summation. Each of the eight consecutive six-hour bins `[intime+6k,intime+6(k+1))`, k=0…7, must contain auditable input/output observation support; otherwise balance eligibility is unknown and excluded, not zero-imputed. Weight and amount ambiguities are counted.

## Treatment strategies

Set `C0=min(t0+12h,V0.endtime)` before reading extubation or outcomes. Loop IDs are 221794, 228340 and 229639.

Exact-deduplicate first. A valid push has order category `05-Med Bolus`, component `Drug Push`, positive finite mg amount, missing rate, and `FinishedRunning`. A valid continuous segment has order category `01-Drips`, component `Continuous Med`, positive finite mg amount, positive finite mg/hour rate, and status `FinishedRunning`, `ChangeDose/Rate`, `Stopped`, or `Paused`. A Paused row contributes delivery only on its own `[starttime,endtime)`; never bridge a positive gap. Merge linked rows only when their `(subject_id,hadm_id,stay_id,itemid,orderid,linkorderid)` identity is valid and their intervals touch/overlap. Unknown units, malformed keys/times, literal `Bolus`, cancellation/order-only states, contradictory duplicates, and onset exactly at C0 are ambiguity events.

Create equal A12 and B12 clones for every eligible participant. A12 remains compatible only if the first repaired loop onset occurs strictly in `(t0,C0)`; B12 remains compatible only if no repaired onset occurs through C0. Early V0 closure is a shared strategy closure, retains both compatible clones, and never reopens. Outcomes, extubation tasks and post-C0 events cannot alter eligibility, C0, arm assignment, treatment history or predictors.

The treatment is an ICU `inputevents` recorded-delivery state. It is not proven order intent, all-route administration, receipt, dose response or clinician awareness. Admission-level eMAR/pharmacy evidence may be reported as non-gating concordance and can limit interpretation, but absence never certifies B12 or relabels exposure.

## Primary endpoint and fresh source audit

Set `H120=t0+120h=intime+168h`, approximately ICU day 7. Scan all same-subject MIMIC admissions and ICU stays at H120; later admissions are outcome-only.

Definite death is `[0,0]`: any exact `admissions.deathtime<=H120`; or a `hospital_expire_flag=1` or `discharge_location='DIED'` admission with `dischtime<=H120`; or a `patients.dod` date interval whose upper boundary is <=H120. A DOD date interval straddling H120 is unknown. Exact death has first precedence.

A transfer row can provide active topology only with valid `subject_id,hadm_id,intime,outtime`, `intime<outtime`, and `intime<=H120<outtime`; malformed rows are excluded with reason counts. The frozen ICU set is: Medical Intensive Care Unit (MICU), Cardiac Vascular Intensive Care Unit (CVICU), Medical/Surgical Intensive Care Unit (MICU/SICU), Surgical Intensive Care Unit (SICU), Trauma SICU (TSICU), Coronary Care Unit (CCU), Neuro Surgical Intensive Care Unit (Neuro SICU), and Intensive Care Unit (ICU). Blank, UNKNOWN/Unknown, PACU, Nursery and Special Care Nursery (SCN) cannot supply a topology class. Every other nonblank catalog-observed careunit is non-ICU. An unseen row is ignored only when valid rows leave one unconflicted class; it never creates success alone.

- `[0,0]` observed ICU failure: exactly one active admission and at least one covering valid ICU transfer or `icustays` interval, with no active valid non-ICU row.
- `[1,1]` observed non-ICU success: exactly one active admission, exactly one valid non-ICU class after dropping rows that cannot supply topology, no covering ICU transfer/stay, and no definite or boundary-compatible death.
- `[0,1]` unknown: nonfatal admission closure, zero/multiple active admissions, date-boundary death, ICU/non-ICU conflict, multiple non-ICU classes, only unseen/malformed topology, or any unresolved contradiction.

Report raw and weighted death, ICU, non-ICU, nonfatal-closure and other-unknown masses plus discharge overlays. H120-RINO means recorded MIMIC topology, not extubation, recovery, function, survival after discharge, or outside-system ICU freedom.

The treatment/effect-blind script `episode83_firstop_topology_audit.py` ([source checksum]) ran in compute job `[research job]` on the exact archive. Output `episode83_firstop_topology_audit.json` has [source checksum]. It found 291,603 discovery participants, 52,281 with a structurally valid ICU stay, 7,682 with any broad opportunity, 721 with multiple broad opportunities, and 7,612 after admission/age/era gates; its prior-branch anchor is 5,752.

In the repaired broad population, H120 states were 1,024 death, 4,177 observed ICU, 1,785 observed non-ICU, 466 closed unknown and 160 other unknown: 626/7,612 (8.2239%) unknown. H168 states were 1,288 death, 3,171 ICU, 2,003 non-ICU, 981 closed unknown and 169 other unknown: 1,150/7,612 (15.1077%) unknown. The audit read no phenotype gates, loop exposure, treatment arm, harm or effect. It supports population materiality, source execution and the H120-versus-H168 observability gradient only. It cannot satisfy final arm-specific weighted unknownness or feasibility.

## Estimand, models and uncertainty

Primary estimand: the `E_R_pause` equal-clone A12-minus-B12 interval association for H120-RINO in the measured-overlap population.

At each clone hour through C0, fit arm-specific L2 logistic compatibility models in five deterministic subject-level folds. Preprocess within training folds only. Predictors are fixed pre-hour data: sex, age, anchor-year-group indicators, care unit/service, admission type; baseline diagnosis/history groups; time since pressor end and pressor type/dose trajectory; MAP level/slope/missingness; urine intensity; potassium and creatinine level/slope/missingness; weight source; input/output/balance level and completeness; baseline ventilation/oxygenation proxies; prior loop ambiguity; RRT/ECMO history; and hour. No treatment numerator model is used. No post-hour, extubation, topology, discharge, death or future laboratory field enters a risk set.

Use numerator-free inverse-denominator products, clip probabilities to [0.01,0.99], pool arms for 1st/99th percentile weight truncation, and normalize within arm. Report weighted standardized differences, calibration, probability histograms, truncation mass and effective sample size. Calculate normalized Hájek bounds:
`p_aL=sum(w_i L_i)/sum(w_i)`, `p_aU=sum(w_i U_i)/sum(w_i)`;
`DeltaL=p_A,L-p_B,U`, `DeltaU=p_A,U-p_B,L`.

Rebuild participant split, first-opportunity selection, phenotype, clones, folds, preprocessing, models, weights, endpoints, harms and sensitivities in 1,999 successful subject bootstraps using PCG64 seed 480048, with at most 2,499 attempts and <=5% failed attempts. Report percentile and centered one-sided 95% limits. Apply Holm FWER 0.05 jointly to H120-RINO and seven adverse families: creatinine-rise-or-death by 48h (RCRD48), creatinine rise by 48h (RCR48), new recorded RRT by day 7 (RRT7), RRT-or-death by day 7 (RRTD7), recorded terminal/hospice/death by day 28 (RTHD28), bounded true mortality, and alive non-hospice/non-acute-transfer disposition by day 28 (ANHATD28). New RRT is the union of exact-time ICU RRT and date-bracketed delivered hospital dialysis after excluding baseline-active RRT. Creatinine uses the last eligible pre-t0 value and a >=0.3 mg/dL rise by 48h, with death composites reported. Preserve +0.03 adverse margins for creatinine and terminal-disposition families and +0.05 for RRT/death families. Missing post-ICU/post-discharge physiology is never called no harm.

Mandatory baselines/sensitivities are: unweighted state/arm tables; the frozen 5,752 earliest-any-stay branch as a population comparator; H72 and H96 topology; strict H168; index-admission-only H120; sustained H120 with no ICU interval in `(H120-24h,H120]`; destination-bearing AIFD7; recorded airway endpoints ARDL7/RHA; the complete legacy Paused-ambiguous exposure pipeline; `E_M_minus_V0`; +30 and +100 mL/kg balance gates; 12/24/36-hour recent-pressor variants; pooled and direct-standardized five-era analyses; and early-versus-late era stability. These are complete pipeline rebuilds, not outcome-selected substitutions.

## Feasibility and falsification

Before direction is reported, separately for `E_R_pause` and `E_M_minus_V0`, require: N>=200; >=100 A12 satisfiers; >=100 B12 completions/shared closures; ESS>=75 per arm; >=100 definite H120 successes and >=100 definite failures; weighted unknown <=0.10 in each arm; absolute arm difference in weighted unknown <=0.05; no probability-clipping/truncation domination; prespecified calibration and balance limits; and inherited retention/Jaccard, ambiguity, timestamp, contamination and era-support gates. Full attrition and reason counts must reconcile. Failure is never repaired after looking at outcomes by changing population precedence, opening a later opportunity, using reserved participants, loosening the horizon, deleting unknowns or changing care-unit labels.

Branch priority:

1. **Population/computation invalid:** wrong split; earliest-any-stay selection; later-stay reopening after a selected opportunity fails; stale parent counts used for the repaired population; silent null coercion; malformed transfer used as topology; script/output hash mismatch; non-reconciled ledgers; source/schema mismatch; or incorrect interval/model/bootstrap arithmetic. No result is interpretable.
2. **Primary infeasible:** required source, final cohort, arm, event, ESS, model or bootstrap minimum fails. Report no effect direction.
3. **Exposure/temporal/topology/era inconclusive:** valid computation but Paused reconstruction, E_M retention/Jaccard, exposure ambiguity/contamination, timestamp, overlap, calibration, balance, weighted unknownness, care-unit conflict, era support or stability gate fails.
4. **Adverse recorded outcome:** a prespecified adverse family Holm-rejects or its harm margin fails. Name the family, estimate, interval and adjusted result; do not call it toxicity or causality. This takes precedence over support.
5. **Supportive recorded de-escalation:** all gates and harm margins pass; one-sided 95% lower limit for `DeltaL_H120` >+0.05; and no required H168, sustained-H120, airway, population, era, exposure or component sensitivity materially conflicts.
6. **Margin-falsified:** valid/feasible, no adjusted adverse family, and one-sided 95% upper limit for `DeltaU_H120` <=+0.05. This rejects only the prespecified five-point recorded-topology association.
7. **Horizon/construct inconclusive:** a feasible H168, sustained-H120, population or component comparison shifts either bound >=0.05, reverses midpoint sign when both absolute midpoints are >=0.02, or changes the result category. H168 infeasibility alone is a measurement limitation.
8. **Statistically inconclusive:** valid and feasible but no directional branch is met.

Thus support means a robust measured-record association consistent with the hypothesis; adverse means a prespecified recorded harm signal; margin-falsified means the data exclude the stated five-point lower-bound association under the model; and inconclusive/infeasible means the data or design cannot resolve it. None is converted into a clinical recommendation automatically.

## Verification and limits on conclusions

The automatic verifier can recompute file/header hashes, the participant split, all broad opportunities, unique V0, ordering/no-reopening, null exclusions, exact aggregate audit, V0/C0, phenotype/item/unit rules, pause-aware exposure, equal clones, topology states, interval bounds, models/weights, bootstrap/Holm results, sensitivity gates and conclusion-to-output consistency. It must test correct computations paired with unsupported conclusions and accept appropriately bounded supportive, adverse, margin-falsified, inconclusive and infeasible interpretations regardless of hypothesis direction.

It must reject claims of actual receipt or nonreceipt, physiologic decongestion, true shock resolution, true airway liberation/recovery, renal safety, equivalence, causal benefit/harm, live-policy value or treatment recommendation. It also cannot establish urine accuracy, goals of care, clinician intent/awareness, exchangeability, outside-system outcomes or transportability.

Those stronger claims require blinded critical-care, pharmacy and nephrology adjudication using source notes/MAR context; linked post-discharge and outside-system outcomes; external replication in a distinct health system; and preferably a prospective randomized trial with actual administration, congestion/perfusion measurements, patient-centered outcomes and protocolized safety review. MIMIC discharge and radiology notes are available for an adjudication study but are not automatically converted into ground truth here.

## Substantive advance

The advance over the selected parents is not a new model. It makes one coherent target population and endpoint executable: first broad opportunities are enumerated before selection; malformed earlier stays do not veto a later true opportunity; downstream failures do not reopen the population; null/malformed transfers cannot create outcome evidence; care-unit classes are explicit; every downstream object must rebuild; and a fresh hash-bound audit demonstrates that the repaired 7,612-person frame retains the intended H120 observability while H168 remains substantially more missing. The treatment effect remains unresolved by design.
