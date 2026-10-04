# Compiler-complete H120 recorded-topology experiment after first eligible hour-48 opportunity

Parents: `[prior hypothesis]` and `[prior hypothesis]`.

This successor integrates the valid earliest-broad-opportunity population repair with the valid null-time/null-key topology repair. It is self-contained: no scientific definition is imported by reference. The design tests one clinically consequential but deliberately narrow recorded association. It does not estimate an effect in this proposal.

## Clinical question, evidence, unresolved claim, and advance

At ICU hour 48, among adults in their first recorded broad prolonged-ventilation opportunity who have recent but not current recorded vasopressor delivery, marked positive recorded fluid balance, adequate recorded MAP, urine output, potassium, and no active recorded RRT/ECMO or recent loop course, is starting or restarting a qualifying ICU-input-system furosemide/bumetanide record during the next 12 hours associated with at least a five-percentage-point increase in the lower partial-identification probability of being alive and directly observed outside a MIMIC ICU at ICU day 7, without crossing prespecified recorded creatinine, RRT, death, or terminal-disposition harm margins?

The decision is clinically important because active fluid removal after shock could facilitate de-escalation from intensive care but could also accompany hypotension, kidney injury, dialysis, or death. Treatment selection may simply identify patients already improving. The available evidence does not resolve initiation versus avoidance in this exact phenotype. The 2026 systematic review and network meta-analysis by Kuriyama et al. (PMCID `PMC13476641`, DOI `10.1016/j.aicoj.2026.100120`; inspected frozen full XML source `[source checksum]`, [source checksum]) found 26 randomized trials with 1,652 participants, mostly clinically heterogeneous heart-failure or cardiovascular-surgery populations and predominantly low/very-low-certainty evidence. The 2026 RADAR-2 secondary analysis by McMullan et al. (PMCID `PMC13098782`, DOI `10.1097/CCE.0000000000001404`; inspected source `[source checksum]`, [source checksum]) found no statistically detectable worsening of lactate or kidney-injury biomarkers under a conservative-fluid/active-deresuscitation bundle, but emphasized modest sample size and imprecision. The 2024 sepsis fluid-accumulation review (PMCID `PMC11264678`, DOI `10.1186/s13613-024-01336-9`; inspected source `[source checksum]`, [source checksum]) reports associations of fluid accumulation with adverse outcomes but uncertainty in monitoring and treatment, and no established mortality benefit from protocolized deresuscitation. These papers support importance and equipoise, not this hypothesis.

The strongest claim currently supported by the frozen data is computational: after splitting participants, 7,682 retained subjects have at least one structurally valid broad hour-48 opportunity; 7,612 remain after selected-opportunity admission and age checks; 721 have multiple broad opportunities. Their `anchor_year_group` counts are 2,395, 1,615, 1,669, 1,373, and 560 across 2008–2010 through 2020–2022. This treatment- and outcome-blind result is frozen in parent artifact `episode80_population_precedence_audit.json`, [source checksum]. It establishes population impact and source computability only.

The old corrected null-safe topology artifact, [source checksum], classified H120/H168 topology in the obsolete 5,752-person earliest-any-ICU frame. It demonstrates the null/malformed-row algorithm and the better observability of H120 than H168, but its counts are stale for this successor and must never be used as expected output, final feasibility evidence, or effect evidence. Every topology count must be recomputed in the repaired population.

The unresolved, falsifiable hypothesis is:

> In both the primary retrospective recording set `E_R_pause` and its mandatory non-V0 as-recorded sensitivity `E_M_minus_V0`, the equal-clone A12-minus-B12 lower bound for H120-RINO exceeds +0.05 and its one-sided 95% subject-bootstrap lower limit exceeds +0.05; the pooled and era-standardized results agree; every population, exposure, temporal, topology, model, overlap, uncertainty, sensitivity, and harm gate passes.

H120-RINO means death-penalized recorded ICU nonoccupancy at a fixed time. A supportive result is not evidence of actual receipt, physiologic decongestion, extubation, recovery, causality, safety, or a treatment recommendation. The substantive advance is a reproducible first-opportunity estimand with one null-safe, destination-neutral endpoint and a conclusion contract that cannot silently substitute stale counts or stronger clinical language.

The research-ambition availability README was inspected. Its demonstrations are not used as clinical evidence here. In particular, no unavailable cancer main article or STAR Methods is claimed as inspected.

## Frozen sources and verified bindings

All source files are read-only. Code, row ledgers, models, and results must be written only in the workspace. The full catalog remains `[internal dataset path]`, [source checksum]. It retains direct access to HCC, MIMIC, eICU, and UKB. Only MIMIC is analyzed; the other datasets and reserved MIMIC participants are not external validation.

Use MIMIC-IV 3.1 snapshot `[source checksum]` in:

`[internal dataset path]`

Archive [source checksum].

The catalog schemas and actual gzip headers inside the archive were checked. Required members, tables, columns, joins, and clocks are:

- `mimic-iv-3.1/hosp/patients.csv.gz` / `hosp/patients`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; patient key `subject_id`; `dod` is date-level.
- `mimic-iv-3.1/icu/icustays.csv.gz` / `icu/icustays`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; exact ICU key is all three IDs.
- `mimic-iv-3.1/hosp/admissions.csv.gz` / `hosp/admissions`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,race,hospital_expire_flag`; admission key `subject_id,hadm_id`.
- `mimic-iv-3.1/hosp/transfers.csv.gz` / `hosp/transfers`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; join on `subject_id,hadm_id`.
- `mimic-iv-3.1/icu/procedureevents.csv.gz` / `icu/procedureevents`: the three ICU keys plus `starttime,endtime,storetime,itemid,value,valueuom,location,locationcategory,orderid,linkorderid,ordercategoryname,ordercategorydescription,statusdescription`.
- `mimic-iv-3.1/icu/inputevents.csv.gz` / `icu/inputevents`: the three ICU keys plus `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,statusdescription,patientweight,totalamount,totalamountuom,originalamount,originalrate`.
- `mimic-iv-3.1/icu/chartevents.csv.gz` / `icu/chartevents`: the three ICU keys plus `charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `mimic-iv-3.1/icu/outputevents.csv.gz` / `icu/outputevents`: the three ICU keys plus `charttime,storetime,itemid,value,valueuom`.
- `mimic-iv-3.1/hosp/labevents.csv.gz` / `hosp/labevents`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,value,valuenum,valueuom`; join on `subject_id,hadm_id`, with `labevent_id` retaining row identity.
- `mimic-iv-3.1/hosp/procedures_icd.csv.gz` / `hosp/procedures_icd`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`.
- Dictionaries: `mimic-iv-3.1/icu/d_items.csv.gz` (`itemid,label,abbreviation,linksto,category,unitname`), `mimic-iv-3.1/hosp/d_labitems.csv.gz` (`itemid,label,fluid,category`), and `mimic-iv-3.1/hosp/d_icd_procedures.csv.gz` (`icd_code,icd_version,long_title`). Join only on the stated dictionary key.
- `hosp/diagnoses_icd` (`subject_id,hadm_id,seq_num,icd_code,icd_version`) may provide only prior completed-admission history.
- Hospital `hosp/emar`, `hosp/emar_detail`, `hosp/pharmacy`, and `hosp/prescriptions` are documentation diagnostics only. They lack an exact shared `stay_id,itemid,orderid` bridge to an ICU input row; time/name proximity cannot relabel A12/B12 or prove dose, route, receipt, or avoidance.

Use strict parsing. IDs must be nonmissing unsigned base-10 integers without fractional or scientific notation. Timestamps must parse as MIMIC naive datetimes; blank, malformed, or nonfinite values are null. Never coerce null `outtime/dischtime/endtime` to infinity, zero, or another row’s value. Clinical intervals are half-open `[start,end)`. Exact duplicate event rows over all requested source columns collapse once; otherwise rows remain distinct. Emit raw-row number, member, source keys, parsed clocks, acceptance flag, and one exclusive rejection/ambiguity reason.

## Participant partition and first broad opportunity

This precedence governs every primary, sensitivity, bootstrap, and verifier fixture.

1. Start from every nonmissing `hosp/patients.subject_id`. Canonicalize to unsigned base-10 ASCII and compute SHA-256(`ehr-hypothesis-discovery-v1` + NUL + `mimic` + NUL + canonical ID), interpret the digest as an unsigned integer, and take modulo 100. Retain buckets 0–79. Do not inspect encounters, events, notes, treatments, or outcomes for buckets 80–99.
2. For every ICU stay of a retained subject, require valid `subject_id,hadm_id,stay_id,intime,outtime`, exactly one patients row, `intime<outtime`, and define `t0=intime+48h`. Require `intime<=t0<outtime`.
3. Join `icu/procedureevents` on all three ICU keys. A V0 crossing is one source row with `itemid=225792`, status exactly `FinishedRunning` or `Stopped`, valid `starttime<endtime`, and `starttime<=t0<endtime`. `storetime` cannot gate or alter V0. Exactly one accepted row must cross t0. Zero or more than one is not broad; do not merge distinct rows to manufacture uniqueness.
4. A broad opportunity consists only of steps 2–3. Order a subject’s broad opportunities by parsed `icustays.intime`, then numeric `stay_id`, and select the first. Earlier short, malformed, nonventilated, zero-crossing, or multiple-crossing stays are not broad and do not veto the first later broad opportunity.
5. Only after selection join `hosp/admissions` on `subject_id,hadm_id`. Require exactly one valid row with `admittime<dischtime` and `admittime<=t0<dischtime`. Require age `anchor_age + year(icustays.intime) - anchor_year >=18`, with all terms valid. Failure excludes the subject and never opens another opportunity.
6. Require `anchor_year_group` to equal exactly one of `2008 - 2010`, `2011 - 2013`, `2014 - 2016`, `2017 - 2019`, or `2020 - 2022`. Missing/unseen values exclude without reopening. `anchor_year` is allowed only in the within-person age formula; shifted event years must never represent cross-person era.
7. Apply the clinical phenotype below to the one selected opportunity. Any failure excludes without later reopening.

The selection ledger must contain all broad opportunities, ordering ranks, V0 source-row identity, reasons each earlier ICU stay was not broad, selected keys, every downstream exclusion, counts of zero/one/multiple broad opportunities, and the forbidden counterfactual count that would enter only if a later broad opportunity were allowed after the selected one failed. It must exactly reproduce 7,682 subjects with any broad opportunity, 7,612 after admission/age, 721 with multiple broad opportunities, and the five stated era counts before any treatment/outcome computation. Any mismatch is population-invalid and no directional result may be emitted.

## Baseline phenotype and all clocks

V0 is the selected, unique, outcome-independent baseline ventilation row. Set `C0=min(t0+12h,V0.endtime)`; assert `t0<C0<=t0+12h`. No extubation task, ICU exit, admission closure, death, transfer, post-t0 outcome, `V0.storetime`, or loop record may define or extend V0/C0.

All ICU events below join on `subject_id,hadm_id,stay_id`; labs and ICD rows join on `subject_id,hadm_id`.

- Recent pressor phenotype: accepted pressor items are 221289, 229617, 221662, 221749, 229630, 229631, 229632, 221906, and 222315. A valid delivery row has valid keys/times, positive finite amount or rate in the dictionary-compatible unit, status `FinishedRunning`, `ChangeDose/Rate`, `Stopped`, or `Paused`, and contributes only on its half-open interval. Require at least one accepted interval intersecting `(t0-24h,t0-6h]`; require no valid or ambiguous pressor row intersecting `(t0-6h,t0]`. The mandatory lookback variants replace 24 by 12 and 36 hours while preserving the six-hour pressor-free window.
- MAP: from items 220052 or 225312 first, otherwise 220181, accept finite `valuenum` with `valueuom=mmHg`, `warning` missing or 0, and `charttime in (t0-3h,t0]`. If arterial values exist use their median; otherwise use noninvasive values. Require at least two accepted measurements and median >=65.
- Weight: choose the earliest accepted item 226512 in `[intime-6h,intime+24h]`; if absent choose earliest item 224639 in that window. Require kg unit and finite 30–300 kg. Ties with values differing by >10% are ambiguous/excluded. `inputevents.patientweight` is diagnostic only.
- Urine: sum positive finite mL values in `(t0-6h,t0]` for items 226557, 226558, 226559, 226560, 226561, 226563, 226564, 226565, 226567, 226584, 226627, and 226631. Exclude mixed irrigant/pre-admission items 226566, 227489, and 226633. Require at least one accepted row and total/(weight*6)>0.1 mL/kg/h.
- Potassium: use the latest finite mmol/L `labevents` item 50971 in `(t0-12h,t0]`; if none, item 52610. Same-time discordance >0.5 mmol/L is ambiguous. Require >=3.0 mmol/L.
- Recorded balance: partition `[intime,t0)` into eight consecutive six-hour bins. Intake is positive `inputevents.amount` in mL or L×1000 for accepted delivered statuses; for positive-duration volume/rate rows allocate volume to bins in proportion to overlap, and place zero-duration boluses at `starttime`. Never convert medication mass, dose, units, mEq, mmol, or unknown units to fluid. Output is positive mL or L×1000 from `outputevents`, excluding 226633 and counting 227488 (GU irrigant volume in) as intake rather than output. Mixed irrigant-out rows 226566/227489 are excluded. Each bin must contain at least one valid input or item-227488 row and at least one valid non-irrigant output row; any unknown-unit candidate row is an ambiguity exclusion. Require cumulative (intake-output)/weight >=+50 mL/kg. Mandatory full-pipeline baselines use +30 and +100 mL/kg.
- Loop washout: no valid or ambiguous repaired loop interval may intersect `(t0-12h,t0]`.
- RRT at t0: exclude definite or possible active RRT. Procedure items 225441/225802/225803/225805/225809/225955 require valid positive-duration `FinishedRunning` or `Stopped` rows crossing t0. Input items 227536/227525 require valid positive-duration, positive recognized-unit, noncancelled rows crossing t0. Active-chart items are 226499, 224154, 225183, 227438, 224191, 225806, 225807, 228004, 228005, 228006, 224144, 224145, 224153, and 226457; item 225965 qualifies only when normalized value is exactly `In use`. An accepted value at t0 or the latest accepted “active” value within six hours with no later “off” value is active. ICD-9 3995/5498 and ICD-10-PCS 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z are date intervals `[chartdate 00:00,next 00:00)`; intersection with t0 is possible active RRT. Catheter/access-only evidence is diagnostic, not active.
- ECMO: exclude accepted procedure item 229529/229530 intervals crossing t0 or positive finite chart items 224660/229270/229842 at t0 or within six hours without a later off value. Null/malformed/contradictory candidate evidence is ambiguous and excludes.

Every positive criterion must be established by an accepted row; every unresolved candidate for a negative criterion causes exclusion. Report exclusive attrition and ambiguity counts.

## Pause-aware recorded-loop strategies and equal clones

Loop items are 221794, 228340, and 229639. After exact-row deduplication, require valid three-key linkage and clinical times.

A drug push is valid only when `ordercategoryname='05-Med Bolus'`, `ordercategorydescription='Drug Push'`, amount is positive finite mg, rate is missing, and `statusdescription='FinishedRunning'`. Its onset is `starttime`.

A continuous segment is valid only when `ordercategoryname='01-Drips'`, `ordercategorydescription='Continuous Med'`, amount is positive finite mg, rate is positive finite mg/hour, and status is one of `FinishedRunning`, `ChangeDose/Rate`, `Stopped`, or `Paused`. A Paused row contributes only on `[starttime,endtime)`; never carry delivery beyond endtime. Rows with the same nonmissing `linkorderid` may merge only when intervals touch or overlap. A positive gap is never bridged. Missing keys/times, `starttime>=endtime`, unknown/non-mg units, nonpositive values, literal status `Bolus`, cancelled/order-only/rewritten/flushed/unknown states, within-course contradictions, and an onset exactly at C0 are ambiguous.

Create one A12 and one B12 clone with initial weight 1 for every eligible subject; never sample or bootstrap clones independently. Use clinical `starttime` only.

- A12: initiate/restart the first valid repaired loop onset strictly in `(t0,C0)`.
- B12: have no valid repaired loop onset through C0.
- Divide `(t0,C0]` at one-hour boundaries plus C0. Before an onset both clones remain compatible. At a valid onset, A12 becomes satisfied and stops treatment censoring; B12 is censored immediately. At C0=t0+12h with no onset, B12 completes and A12 is censored. At early `C0=V0.endtime<t0+12h` with no onset, both still-compatible clones receive shared deterministic closure, remain in the estimand with treatment weight 1 from that closure onward, and the window never reopens. Exact-C0 or unresolved loop evidence censors both as ambiguous.
- Death, ICU exit, transfer, discharge, outcome, post-t0 physiology, and recording time cannot alter treatment labels or C0. Treatment after C0 is unrestricted and cannot relabel a clone.

Emit one row per subject/clone/hour with prior history, event source row, compatibility, satisfaction/closure/censoring state, censor reason, predicted probability, factor weight, and cumulative weight. Equal-clone reconciliation must hold before censoring.

`inputevents.storetime` is documentation timing only. It must never enter eligibility, V0/C0, washout, A12/B12, censoring, predictors, weights, endpoints, or conclusions about awareness, intent, availability, route, or receipt. Report `storetime-starttime` lag categories for qualifying rows only after labels are frozen.

## Analysis sets and recording-time safeguard

`E_R_pause` is the primary retrospective set above, using final recorded clinical event times and the pause-aware grammar.

`E_M_minus_V0` is a mandatory non-adding sensitivity. Start from E_R and re-evaluate every non-V0 pre-t0 phenotype/history row using only rows with nonmissing `storetime` no later than the decision boundary for that variable. A late/missing row cannot create a positive criterion; a late/missing candidate for a negative criterion makes that criterion ambiguous and excludes. V0 is intentionally exempt because its completion record is structurally delayed; its clinical interval remains fixed. E_M can only remove, never add, subjects. Require `|E_M|/|E_R|>=0.90` and subject-set Jaccard >=0.90. Rebuild clones, models, weights, outcomes, sensitivities, and bootstraps independently. E_M is not called decision-observable because storetime does not prove clinician awareness.

A full legacy sensitivity treats every Paused loop row as ambiguous, then rebuilds washout, assignment, histories, models, and outcomes. A branch/category change, either bound shift >=0.05, or midpoint sign reversal when both absolute midpoints are >=0.02 is a material exposure-semantics conflict.

## H120-RINO outcome with deterministic null handling

Set `H120=t0+120h=intime+168h`; assert exact equality. This is ICU day 7. Set `H72=t0+72h`, `H96=t0+96h`, and `H168=t0+168h=intime+216h`; H168 is ICU day 9 and must never be labeled day 7.

Scan all admissions for the same subject through each horizon; later admissions affect outcomes only. An admission row is valid only with nonmissing parseable `subject_id,hadm_id,admittime,dischtime` and `admittime<dischtime`; it is active iff `admittime<=H<dischtime`. A same-subject malformed admission whose `admittime` is not provably after H is an unknown-topology blocker, never active evidence. Rows with missing subject_id cannot be attached and are globally counted only.

Death has first precedence:

1. Any valid exact `deathtime<=H` is definite failure `[0,0]`, even if another field conflicts.
2. A closed admission with `hospital_expire_flag=1` or `discharge_location='DIED'`, `dischtime<=H`, and no clearly alive conflict is `[0,0]`; conflicting non-exact indicators are `[0,1]`.
3. Treat `patients.dod` as `[date 00:00,date+1d)`: if the interval ends at or before H, death is `[0,0]`; if it contains H, outcome is `[0,1]`; if it begins after H it does not establish death by H.

After death resolution, require exactly one valid active same-subject admission. For that admission, a transfer is an active candidate only if `subject_id,hadm_id,transfer_id,intime,outtime` are valid, `intime<outtime`, and `intime<=H<outtime`. Missing/null keys or times never become active evidence and receive exclusive reason counts; they are never assigned to an admission by proximity. Duplicate transfer_id or overlapping valid transfer candidates are conflicts.

Frozen ICU careunits are exactly: `Cardiac Vascular Intensive Care Unit (CVICU)`, `Coronary Care Unit (CCU)`, `Intensive Care Unit (ICU)`, `Medical Intensive Care Unit (MICU)`, `Medical/Surgical Intensive Care Unit (MICU/SICU)`, `Neuro Surgical Intensive Care Unit (Neuro SICU)`, `Surgical Intensive Care Unit (SICU)`, and `Trauma SICU (TSICU)`.

Frozen non-ICU careunits are exactly: `Cardiac Surgery`, `Cardiology`, `Cardiology Surgery Intermediate`, `Discharge Lounge`, `Emergency Department Observation`, `Hematology/Oncology`, `Hematology/Oncology Intermediate`, `Labor & Delivery`, `Med/Surg`, `Med/Surg/GYN`, `Med/Surg/Trauma`, `Medical/Surgical (Gynecology)`, `Medicine`, `Medicine/Cardiology`, `Medicine/Cardiology Intermediate`, `Neuro Intermediate`, `Neuro Stepdown`, `Neurology`, `Observation`, `Obstetrics (Postpartum & Antepartum)`, `Obstetrics Antepartum`, `Obstetrics Postpartum`, `Oncology`, `Psychiatry`, `Surgery`, `Surgery/Pancreatic/Biliary/Bariatric`, `Surgery/Trauma`, `Surgery/Vascular/Intermediate`, `Surgical Intermediate`, `Thoracic Surgery`, `Transplant`, and `Vascular`. PACU, Nursery, missing, and unseen labels are unknown.

The bounded endpoint is:

- `[0,0]`: definite death; or exactly one valid active admission with exactly one active ICU transfer, exactly one active `icu/icustays` interval in that admission covering H, and no active non-ICU transfer or other conflict.
- `[1,1]`: exactly one valid active admission with exactly one active transfer in the frozen non-ICU list, no active ICU transfer, no active ICU-stay interval, and no death conflict.
- `[0,1]`: no active admission after nonfatal closure; multiple active admissions; absent, malformed, duplicated, or overlapping topology; transfer/ICU-stay disagreement; unseen/PACU/Nursery location; boundary-compatible death; or any unresolved contradiction.

Thus nonfatal discharge is unknown, not success. Report mutually exclusive raw and weighted components: exact/consistent death, observed ICU failure, observed non-ICU success, nonfatal closure, date-boundary death, malformed-admission blocker, missing-key/time transfer, multiple admission, overlapping transfer, ICU/transfer disagreement, unseen location, and other conflict. Report exact discharge-location overlays separately; they never alter RINO. H120-RINO is not recovery, extubation, function, survival after discharge, or absence of ICU care outside MIMIC.

Mandatory endpoint baselines rebuild the full estimator at H72, H96, and strict H168; an index-admission-only H120; and sustained H120, where success additionally requires continuous non-ICU transfer coverage and no same-subject ICU interval over `(H120-24h,H120]`. A feasible baseline is materially discordant if either bound shifts >=0.05, the midpoint reverses sign with both absolute midpoints >=0.02, or the result branch changes. H168 infeasibility alone is a measurement limitation, not a reversal.

## Bounded renal, RRT, death, and terminal outcomes

All are arm-specific bounded risks, with death never allowed to appear renally favorable.

- `RCR48`: baseline creatinine is the latest finite item-50912 mg/dL in `(t0-24h,t0]`, ties resolved by `labevent_id`; follow-up is the maximum accepted value in `(t0,t0+48h]`. Definite harm is increase >=0.3 mg/dL or >=1.5× baseline. Complete measurements below both thresholds are `[0,0]`; missing/ambiguous baseline or follow-up is `[0,1]`.
- `RCRD48`: `[1,1]` if RCR48 is definite or definite death occurs by t0+48h; `[0,0]` only if both creatinine non-harm and survival through the window are definite; otherwise `[0,1]`.
- `RRT7`: any accepted exact procedure, active-chart, or positive-input RRT evidence with clinical time in `(t0,H120]` is `[1,1]`. An RRT ICD date interval wholly contained in the window is lower evidence; any intersection is upper evidence. No event with complete in-system observation is `[0,0]`; nonfatal closure, malformed evidence, or incomplete observation is `[0,1]`.
- `RRTD7`: definite RRT or definite death by H120 is `[1,1]`; only definite no RRT plus definite survival is `[0,0]`; otherwise `[0,1]`.
- `RTHD28`, H28=t0+28d: lower harm is exact/consistent recorded death or index discharge by H28 to `HOSPICE`, `CHRONIC/LONG TERM ACUTE CARE`, or `ACUTE HOSPITAL`. Upper additionally includes malformed/conflicting terminal fields and nonterminal closure with unavailable subsequent status. An active admission with no such event at H28 or a completely observed nonterminal destination is lower non-harm.
- True 28-day mortality: exact/consistent hospital death or DOD interval wholly before H28 is `[1,1]`; active hospitalization at H28 or DOD beginning after H28 establishes lower non-death; missing post-discharge vital status remains `[0,1]`.
- `ANHATD28` is favorable recorded alive non-hospice/non-acute-transfer index discharge by H28. Exact `HOME`, `HOME HEALTH CARE`, `ASSISTED LIVING`, `REHAB`, `SKILLED NURSING FACILITY`, `HEALTHCARE FACILITY`, or `PSYCH FACILITY` with no death conflict is `[1,1]`; death, hospice, LTAC, acute-hospital transfer, or ongoing index hospitalization at H28 is `[0,0]`; malformed/missing/conflicting closure is `[0,1]`. This is a recorded disposition, not recovery or survival thereafter.

Report each component and missingness reason. Support requires one-sided 95% upper limits for A-minus-B harm upper bounds below +0.03 for RCR48, RCRD48, and RTHD28, and below +0.05 for RRT7 and RRTD7. True mortality and ANHATD28 are mandatory bounded evidence-limit/adverse tests, not “safety” clearance gates when their upper bounds are structurally wide.

## Compatibility models, weights, estimand, and uncertainty

The target is the observed final eligible E_R mixture, not a treated-only, overlap-selected, or complete-case population. No baseline propensity, overlap tilt, numerator stabilization, endpoint imputation, or post-outcome selection is allowed.

Create deterministic five-fold subject splits by SHA-256(`ehr-hypothesis-h120-fold-v1` + NUL + canonical subject_id) modulo 5. At each nondeterministic clone-hour fit separate A12 and B12 logistic compatibility models on four folds and predict the held-out fold. Among clones compatible at interval start, the binary model target is 1 when the observed record remains compatible through interval end or A12 is satisfied in that interval, and 0 when an observed loop deviation/ambiguity censors that arm; early V0 shared closure is deterministic and is not modeled. Fixed predictors, all measured strictly before that hour, are: age; gender; race; admission_type; first_careunit; all five `anchor_year_group` indicators; baseline weight; +48h balance/kg and each of its eight bin balances; final-3h MAP median/count; final-6h urine/kg/h/count; latest potassium and creatinine plus ages; pressor item indicators, union hours in `(t0-24h,t0-6h]`, and hours since pressor end; repaired pre-t0 loop count/hours; prior completed-admission count and prior completed-admission diagnosis-code count; current hour; and a missingness indicator for every nullable predictor. No shifted calendar year/month/day, `outtime,dischtime,deathtime,last_careunit`, post-t0 transfer/location, post-hour laboratory/physiology, treatment-future field, endpoint component, or outcome is permitted.

Within each training fold, continuous predictors are winsorized at training 1st/99th percentiles, median-imputed, and standardized by training mean/SD (zero SD becomes 1); categorical variables use frozen levels plus `OTHER` and missing indicators. Fit L2 logistic regression with intercept, `C=1`, `solver='lbfgs'`, `max_iter=1000`, `tol=1e-8`, and no class weighting. If convergence fails, Hessian/coefficients are nonfinite, or either class has <10 training rows, refit once at C=0.1. If fallback fails or an arm-hour has one class, the replicate is model-infeasible; do not substitute an empirical probability.

For a compatible clone, multiply the reciprocal of the predicted probability of its observed compatibility transition; deterministic satisfaction/shared-closure intervals contribute factor 1. Clip each predicted probability to [0.01,0.99]. After clone follow-up, pool both arms’ cumulative weights and truncate to the pooled 1st/99th empirical percentiles; report untruncated results. Arm ESS is `(sum w)^2/sum(w^2)`.

For endpoint bounds `(L_i,U_i)`, normalized Hájek arm bounds are
`p_aL=sum(w_i L_i)/sum(w_i)` and `p_aU=sum(w_i U_i)/sum(w_i)`.
The A12-minus-B12 sharp association interval is
`DeltaL=p_AL-p_BU`, `DeltaU=p_AU-p_BL`.
Unknowns are never deleted or midpoint-imputed.

Era-standardize by final E_R proportions `q_g=N_g/N`. Compute within-era/arm Hájek bounds and `p_aL^G=sum_g q_g p_agL`, `p_aU^G=sum_g q_g p_agU`; then form `DeltaL^G,DeltaU^G`. A zero era-arm denominator is not imputed and makes support era-inconclusive. Repeat the complete pipeline in early (2008–2013) and late (2014–2022) strata and once with era intentionally omitted as diagnostics. All five era indicators must have weighted absolute SMD <0.10 in both E_R and E_M. A material era conflict is pooled-versus-standardized or pooled-versus-era-omitted bound shift >=0.05, midpoint sign reversal with both magnitudes >=0.02, or early-versus-late midpoint difference >=0.10/sign reversal. Each early/late analysis requires >=50 subjects, >=20 compatible per arm, and ESS>=15 per arm.

Run 1,999 successful full-pipeline subject bootstraps using NumPy PCG64 seed 480048, sampling subjects with replacement within E_R. Rebuild broad selection, downstream gates, clones, fold preprocessing, models, weights, era proportions, endpoints, sensitivities, and all statistics. Permit at most 2,499 attempts and <=5% failed attempts; duplicate sampled subjects receive unique replicate IDs but retain all their rows together. Use 5th/95th percentiles as one-sided 95% limits and report percentile two-sided 95% intervals. Orient every statistic so larger is evidence in its named direction: `S_H120=DeltaL_H120-0.05`; each harm statistic is its A-minus-B lower harm bound `DeltaL`; and `S_ANHAT=-DeltaU_ANHAT`. For B=1,999 successful draws compute the centered one-sided p-value `p=(1+sum_b I[(S_b-S_hat)<=-S_hat])/(B+1)`. Apply Holm step-down FWER 0.05 across exactly eight families: H120-RINO benefit beyond +0.05; positive RCR48, RCRD48, RRT7, RRTD7, RTHD28, and true-mortality harm; and negative ANHATD28 favorable-disposition contrast. Report raw and Holm p-values. An adverse family requires a validity-passing directionally adverse statistic and Holm rejection; point estimates or raw p-values alone are alerts only.

## Feasibility, diagnostics, and falsification

All counts are checked independently in E_R and E_M unless stated otherwise:

- required members, headers, schema/archive hashes, and population ledger reconcile;
- N>=200; A12 satisfiers>=100; B12 completions plus shared closures>=100;
- ESS>=75 in each arm;
- >=100 definite H120 successes and >=100 definite H120 failures;
- weighted H120 unknown fraction <=0.10 in each arm and absolute arm difference <=0.05;
- no predicted-probability clipping for >10% of at-risk clone-hours; no single final weight >10% of its arm total;
- held-out calibration slope 0.5–2.0, intercept absolute <=0.20, and Brier score below the intercept-only Brier score in every fitted arm with >=50 observations;
- every weighted baseline continuous/categorical indicator has absolute SMD <0.10; no prespecified variable worsens by >0.05 relative to unweighted;
- E_M retention/Jaccard gates pass; era gates pass; bootstrap/model gates pass; row/clone/state arithmetic reconciles exactly.

Falsification tests are mandatory. The exact population audit must reproduce its frozen counts. Synthetic fixtures must demonstrate that a malformed earlier non-broad stay does not veto a later first broad opportunity, but any downstream failure of the selected broad opportunity never reopens another stay. Null `outtime/dischtime/endtime` cannot be open-ended. Missing-hadm transfer rows cannot attach by time proximity. Exact death overrides location; boundary-date death is unknown; nonfatal closure is unknown; a later same-subject ICU readmission active at H120 is failure; overlapping/unseen topology is unknown; Paused delivery ends at endtime; linked positive gaps do not bridge; and exact-C0 loop onset is ambiguous.

Two pre-t0 placebo outcomes—six-hour urine slope over `(t0-12h,t0]` and six-hour balance slope over the same period—must have weighted |SMD|<0.10 and bootstrap intervals containing zero in both analysis sets. Failure is residual-confounding/measurement inconclusive, never evidence of harm or benefit. The H72/H96/H168, index-only, sustained, +30/+100 balance, 12/36-hour pressor, E_M, legacy-Paused, untruncated-weight, and era analyses must all be reported with the material-conflict rules above. Gates are frozen before outcomes and may not be relaxed, horizons changed, unknowns deleted, or reserved subjects opened after results.

## Deterministic result branches

Apply in this order:

1. **Population/computation invalid:** wrong archive/header/hash, reserved-subject access, population-count mismatch, earliest-any-ICU selection, later-opportunity reopening, silent null coercion, stale 5,752 topology fixture, nonreconciling rows/clones/states, or outcome/storetime leakage. No scientific direction is valid.
2. **Primary infeasible:** required source unavailable or either E_R/E_M fails cohort, arm, event, ESS, probability, model, bootstrap, or unknownness minima. Report only attrition and which minimum failed; no direction.
3. **Temporal/measurement/exposure inconclusive:** recording-time, placebo, calibration, balance, contamination, ambiguity, Paused, or required sensitivity gate fails or materially conflicts. Report computed estimates as descriptive, not directional evidence.
4. **Adverse-FWER:** a valid feasible analysis has any prespecified adverse family Holm-rejected. Name the outcome, bound, confidence limit, and adjusted p-value. This is a recorded concern, not toxicity or causal harm.
5. **Era/endpoint-horizon inconclusive:** era standardization/stability fails, or a feasible required H72/H96/H168/index/sustained endpoint analysis materially conflicts. H168 infeasibility alone is labeled a measurement limitation.
6. **Five-point margin falsified:** no higher-priority branch applies and the one-sided 95% upper limits of both pooled and era-standardized `DeltaU_H120` are <=+0.05. This rejects only the prespecified recorded-topology association; it is not equivalence, no subgroup benefit, or safety.
7. **Supportive recorded topology:** all gates and harm margins pass, no adverse family rejects, no material sensitivity conflict exists, and one-sided 95% lower limits for both pooled and era-standardized `DeltaL_H120` exceed +0.05 in E_R and E_M. This supports external replication or prospective randomization only.
8. **Statistically inconclusive:** valid feasible computation meets no prior directional branch.

Negative, adverse, inconclusive, and infeasible outcomes are valid resolutions. The verifier must accept correct interpretations independent of hypothesis direction and reject supportive prose attached to any higher-priority failure.

## Required outputs and claim limits

Write source manifest/hash checks; partition proof; broad-opportunity and no-reopening ledgers; all attrition/ambiguity counts; V0/C0 rows; balance-bin components; loop course repair and store-lag ledgers; subject/clone/hour transitions; model coefficients/fallbacks/calibration; raw/clipped/truncated weights and ESS; era proportions/balance; individual endpoint bounds and exclusive topology states; all arm risks/effect bounds; bootstrap draws/failures; Holm table; sensitivity conflict flags; feasibility booleans; final branch; and a machine-readable mapping from every numerical conclusion to output fields.

Automation can verify all source bindings, joins, parsing, ordering, interval arithmetic, treatment/outcome separation, state machines, models, weights, bootstrap/Holm calculations, thresholds, and conclusion-to-output consistency. Verifier fixtures must include correctly computed outputs paired with unsupported claims of administration/nonadministration, clinician intent, true shock resolution, congestion, decongestion, extubation/recovery, renal or mortality safety, causality, equivalence, live-policy value, transportability, or treatment recommendation; those submissions fail.

Automation cannot establish actual medication receipt or route, clinician awareness/intent, true shock resolution or fluid overload, accurate intake/output, actual ventilation or airway liberation, KDIGO AKI, true RRT outside recorded streams, functional recovery, destination appropriateness, outside-system ICU/death, goals of care, exchangeability, causality, transportability, or clinical actionability. Those stronger claims require blinded critical-care/pharmacy/nephrology adjudication, linked medication/device/vital-status data, external replication, and preferably a prospective randomized trial.

## Change note

This child freezes one self-contained compiler contract for the repaired first broad hour-48 opportunity population and the null-safe H120 topology state machine. It preserves pause-aware clinical-time loop reconstruction, outcome-independent V0/C0, equal clones, H120 ICU-day-7 timing, explicit unknownness, bounded renal/RRT/death/terminal outcomes, era and recording-time safeguards, full-pipeline uncertainty, feasibility minima, falsification, and noncausal limits. It requires full recomputation in the 7,612-person repaired broad frame and forbids the obsolete 5,752-person topology counts as expected output. No treatment effect or clinical recommendation is claimed.
