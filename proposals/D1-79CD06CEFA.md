# Episode 17: bound-coherent safety and grace-period repair of post-shock delivered-loop initiation

**Parent:** `[prior hypothesis]`

## Substantive repair

This child preserves the parent's corrected participant partition, ICU-hour-48 population, delivery- and route-limited exposure, unit-safe fluid phenotype, destination-aware primary outcome, observation-bounded respiratory outcome, provenance-bounded RRT outcome, and default noncausal interpretation. It repairs four decision-changing defects:

1. The parent's “supportive” rule requires only that the *upper* confidence limit for the optimistic ALDL7 effect exceed zero. That does not exclude clinically important respiratory harm. It also tests mortality using a lower-bound contrast when noninferiority requires the conservative upper bound.
2. Sparse route-explicit eMAR coverage is simultaneously listed as a primary infeasibility gate and said not to invalidate the route-agnostic primary exposure.
3. “Hour-by-hour treatment and censoring models” do not state exactly when an A clone is artificially censored, which histories enter each denominator, or when weighting stops.
4. Multiplying observed treatment odds is a stochastic-policy sensitivity, not a quantitative sensitivity to unmeasured clinical readiness.

The repaired experiment uses confidence limits on partial-identification effect bounds, removes route coverage from primary feasibility, freezes the clone-hour state machine and weight denominator, and separates a stochastic policy analysis from an explicit unmeasured-confounding tipping grid.

## Clinical question, supported evidence, and unresolved hypothesis

For an invasively ventilated adult at ICU hour 48 who has survived vasopressor-treated shock, is off pressors, remains substantially fluid positive, has adequate MAP, urine output and potassium, and lies in measured treatment overlap, should a loop diuretic be initiated during the next 24 hours?

The strongest supported claim is narrower. RADAR-2 tested a two-stage conservative-fluid plus active-deresuscitation bundle, not isolated loop initiation at this landmark. Its 2026 full-text secondary analysis found no statistically detectable differences in lactate, AKIRisk, urinary cystatin-C, or vascular-injury biomarkers, while emphasizing modest sample size and imprecision (McMullan et al., DOI `10.1097/CCE.0000000000001404`; full XML inspected, frozen source `[source checksum]`). A 2026 full-text operational review of EHR target trials states that cloning/censoring can address time-zero alignment, but fragmented exposure, evolving clinical decisions, irregular outcome capture and residual confounding can shift the estimand to a data-defined contrast; analytic sophistication cannot recover an unsupported estimand (Wang et al., DOI `10.1038/s41746-026-02563-z`; full XML inspected, frozen source `[source checksum]`). Thus, current evidence supports that protocolized deresuscitation can alter fluid management without a demonstrated biomarker safety signal; it does not establish patient-centered benefit, renal safety, or the effect of this particular delivered-loop decision.

**Falsifiable unresolved hypothesis:** In the prespecified measured-overlap population, assignment at `t0` to initiate a qualifying ICU-recorded delivered furosemide/bumetanide segment by `t0+24h`, versus no actual loop administration by any route through `t0+24h`, increases 28-day recorded alive non-hospice/non-acute-hospital index-discharge risk (ANHATD28) by more than 5 percentage points, while ruling out more than 5 points lower alive documented durable liberation by day 7 (ALDL7), more than 3 points higher recorded day-28 mortality, and more than 5 points higher observed post-landmark RRT through day 7.

Resolution would advance existing knowledge from bundle-level fluid-balance evidence to a patient-centered, delivery-coherent decision policy with explicitly bounded safety. Even a supportive result prioritizes external validation or a pragmatic trial; it is not a bedside recommendation.

## Dataset, partition, population, and time

The configured dataset is MIMIC-IV 3.1 snapshot `[source checksum]`. The primary read-only source is:

`[internal dataset path]`
(source ID `baidu_downloads/eicu_mimic/mimic数据库/mimic-iv-3.1.zip`, [source checksum]).

Use only discovery subjects:
`bucket = int(SHA256("ehr-hypothesis-discovery-v1" + NUL + "mimic" + NUL + canonical_base10(subject_id))) mod 100`; retain 0–79 and never inspect 80–99. Emit namespace, canonical ID, digest, bucket, and catalog checksum. Select the first chronological qualifying ICU stay per subject; all resampling is by subject.

Set `t0 = icu/icustays.intime + 48h`; require `intime <= t0 < outtime`, age ≥18 from `hosp/patients.anchor_age, anchor_year` and `hosp/admissions.admittime`, and invasive ventilation at `t0` from `icu/procedureevents` item 225792 with positive duration, `starttime <= t0 < endtime`, status `FinishedRunning` or `Stopped` (`Paused` sensitivity only).

Before assignment require:

- a positive delivered vasopressor segment before `t0-6h` and none overlapping `(t0-6h,t0]`, inputevent items 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315;
- median MAP ≥65 mmHg in `(t0-3h,t0]`, chartevent items 220052/220181/225312;
- cumulative valid fluid balance ≥+50 mL/kg from ICU `intime` through `t0)`, using only recognized mL/L intake and output units, never medication mass;
- decision-available weight 30–300 kg, with a frozen source hierarchy and no future `patientweight`;
- urine output >0.1 mL/kg/h in `(t0-6h,t0]`;
- latest decision-available potassium, lab item 50971 or 52610, in `(t0-12h,t0]`, numeric ≥3.0 mmol/L;
- no active ECMO, no exact-timed delivered RRT overlapping `t0`, and no actual loop by any route in `(t0-12h,t0]`.

For a measurement to enter eligibility or a clone-hour history, both its clinical/event time and nonmissing `storetime` must be no later than that boundary. Actual delivery may be reconstructed retrospectively from event start/end, but future end time, final status, total amount or later-stored content cannot be used as an earlier covariate. Report clinical-only, decision-available, late-entry and retrospective-delivery counts by source.

## Treatment strategies and exposure contract

**A:** first qualifying ICU-recorded delivered furosemide/bumetanide in `(t0,t0+24h]`: inputevent item 221794, 228340 or 229639; valid subject/hadm/stay keys; nonmissing start/end/store times; status `FinishedRunning`, `ChangeDose/Rate`, or `Stopped`; positive amount convertible to mg or positive mg/hour rate over positive duration. `Paused` is sensitivity only. Unknown units, nonpositive/cancelled/not-started/order-only rows are excluded.

**B:** no actual furosemide, bumetanide, torsemide or ethacrynic-acid administration by any route in `(t0,t0+24h]`. Join `hosp/emar` to all `hosp/emar_detail` sibling rows by `subject_id, emar_id, emar_seq`, retain `parent_field_ordinal`, and aggregate before classifying an administration. Require compatible medication/product text, administration evidence, no complete-dose-not-given contradiction, and positive `dose_given` or `product_amount_given`. Missing route remains an any-route B deviation. `prescriptions` and `pharmacy` are order-only diagnostics and never treatment.

The primary is “ICU-recorded delivered loop,” not “IV loop.” Route-explicit IV eMAR and ICU/eMAR ±15-minute concordance are sensitivities. Sparse route evidence makes the IV-specific question unavailable; it does **not** make the route-agnostic primary infeasible.

A non-ICU actual loop before qualifying A initiation makes A incompatible. Once qualifying A begins, exposure-related A censoring stops. Any actual loop makes B incompatible. Treatment after hour 24 is unrestricted.

## Frozen clone-hour state machine and analysis

Clone each subject to A and B at `t0`. Divide the grace period into intervals `j=0,…,23`, `[t0+jh,t0+(j+1)h)`, with the final endpoint including events exactly at `t0+24h`. At each interval start, compute `H_j` only from prior-hour values, missingness indicators and prespecified slopes available by both clinical time and storetime. Candidate histories are MAP/hypotension; pressor dose and time since cessation; urine and valid cumulative balance; FiO2/PEEP/oxygenation/ventilation; creatinine/potassium/lactate; delivered crystalloid/albumin/pressors/procedures; and transfer location. Never use post-boundary values, future final statuses, outcomes, destinations or later diagnoses.

Within each interval apply this priority:

1. recorded death or live discharge/acute transfer occurs as an outcome while every still-compatible clone remains assigned; no artificial censoring precedes it;
2. a qualifying ICU loop makes A adherent and censors B; a nonqualifying actual loop censors both still-untreated clones as appropriate;
3. absent a terminal event or treatment, both remain compatible;
4. at hour 24, censor A if qualifying A never began; B remains adherent if no loop occurred.

Reverse tie priority is a required sensitivity. Emit one transition row per subject/clone/hour with previous state, `H_j` provenance, event type/time, compatibility, censor reason and weight factors.

Fit cross-fitted pooled-logistic artificial-censoring models separately by assigned clone. The denominator is `Pr(C_{j+1}=0 | C_j=0, H_j, arm)`; the numerator conditions only on frozen baseline history. For A, this includes the hour-24 satisfaction decision; for B it includes remaining loop-free each hour. Stop multiplying weights after A initiation, terminal outcome, or censoring. Truncate cumulative stabilized weights at the 1st/99th percentiles and report untruncated estimates. Administrative end-of-source observation is modeled separately from treatment incompatibility.

Define baseline `e_0(X_0)` as the cross-fitted cumulative incidence of qualifying A initiation by 24 hours before a terminal competing event, estimated from baseline covariates without using realized future status as a predictor. Restrict to `e_0 in [0.10,0.90]` and apply the same `e_0(1-e_0)` tilt to both clones. Report crude, common-overlap, and overlap-plus-clone-censor estimates, arm counts, event counts, calibration, standardized differences, probabilities, tails and ESS. If overlap targeting cannot be fit without conditioning on a post-`t0` event, the primary is infeasible.

Estimate weighted arm risks and A-minus-B risk differences with subject-level cross-fitting and at least 500 subject bootstraps. The observed-odds multipliers 0.5, 0.75, 1, 1.33 and 2 are labeled a **stochastic initiation-policy sensitivity**, not an unmeasured-confounding analysis. Separately report a tipping grid for a binary unmeasured readiness factor over prevalence differences 0–0.30 and outcome risk ratios 1–3; this is a bias sensitivity, not proof that such a factor exists. Pre-`t0` slopes are placebo outcomes and must not materially differ after weighting.

## Outcomes and bound arithmetic

Primary ANHATD28 at `H28=t0+28d` uses `hosp/admissions.dischtime, deathtime, hospital_expire_flag, discharge_location`. Deterministically classify and report: in-hospital death; exact `HOSPICE`; exact `ACUTE HOSPITAL`; recorded alive non-hospice/non-acute destination; prolonged hospitalization; invalid/discordant state. Reconcile binary risk to state probabilities and an Aalen–Johansen cumulative incidence. Report any live discharge, HOME/HOME HEALTH CARE, destination-specific, day-14/day-21, era/service/careunit, anomaly-excluded, same-system readmission and recorded post-discharge DOD sensitivities. Recorded discharge is not recovery or known 28-day survival.

ALDL7 is favorable and bounded: accepted extubation (procedure items 227194/225468/225477, status `FinishedRunning`) by day 5, continuous linked-ICU observation through day 7, no recurrent invasive ventilation item 225792 or intubation item 224385, and recorded survival. Death or complete observed nonliberation is failure; observation gaps are individual `[0,1]`.

Recorded day-28 mortality is bounded where date-only `hosp/patients.dod` intersects the horizon; exact in-hospital `deathtime` is definite. Missing out-of-system death is not survival and remains an evidence limitation.

Observed RRT through day 7 is not new RRT, AKI or renal safety. ICU evidence is `procedureevents` item 225441/225802/225803/225805/225809/225955, start in `(t0,t0+7d]`, status `FinishedRunning` or `Stopped`. Hospital delivered dialysis is `hosp/procedures_icd` ICD-9 3995/5498 or ICD-10 5A1D00Z/5A1D60Z/5A1D70Z/5A1D80Z/5A1D90Z, dictionary-confirmed in `hosp/d_icd_procedures`; access/imaging codes are excluded. Treat `chartdate` as `[00:00,+1d)`: full containment is lower evidence and any intersection upper evidence. Deduplicate ICU/hospital evidence and report prior-timed, strictly earlier date-only, same-date-indeterminate and no-prior strata.

For every bounded binary outcome, estimate arm risks `p_A^L,p_A^U,p_B^L,p_B^U` and the sharp no-assumption effect interval:
`Delta^L=p_A^L-p_B^U`, `Delta^U=p_A^U-p_B^L`.
Bootstrap the bound endpoints and report one-sided lower/upper 95% confidence limits. For favorable ALDL7, non-harm uses the lower confidence limit of `Delta^L`; for harmful mortality/RRT, non-harm uses the upper confidence limit of `Delta^U`. Never substitute an optimistic endpoint.

## Falsification, feasibility, and interpretation

Primary magnitude support requires the lower 95% limit of ANHATD28 RD >+0.05; the >5-point claim is margin-falsified if its upper 95% limit is ≤+0.05; otherwise unresolved.

A **supportive clinical branch** additionally requires:

- ALDL7 lower-bound-effect lower limit >−0.05;
- recorded mortality upper-bound-effect upper limit <+0.03;
- observed-RRT upper-bound-effect upper limit <+0.05;
- no qualified destination sign reversal;
- all temporal, state, balance/unit, overlap, calibration, negative-control, weighting, bound and stochastic/bias diagnostics pass.

An **adverse branch** occurs if ANHATD28 upper limit ≤0; or ALDL7 upper-bound-effect upper limit <−0.05; or mortality lower-bound-effect lower limit ≥+0.03; or RRT lower-bound-effect lower limit ≥+0.05. These mean evidence of no discharge benefit or a recorded harm signal, not biological proof.

All other patterns are **inconclusive**, including primary margin falsification without harm, optimistic-only safety, wide bounds, route unavailability, sign conflict, bias tipping under plausible settings, failed placebo tests, poor overlap or sparse events.

Before effect estimation, declare infeasible/inconclusive if either strategy has <100 adherent subjects, ESS <75, >10% person-hours have denominator probability <.01 or >.99, >1% temporal/state contradictions, >10-point arm anomaly imbalance, material differential late entry, failed negative controls, or nonreconciling state/bound arithmetic. Route-explicit coverage is reported but is not this primary gate.

## Exact source bindings

All archive members below are under `mimic-iv-3.1/` in the exact ZIP:

- `hosp/admissions.csv.gz`: `subject_id, hadm_id, admittime, dischtime, deathtime, discharge_location, hospital_expire_flag`.
- `hosp/patients.csv.gz`: `subject_id, gender, anchor_age, anchor_year, dod`.
- `icu/icustays.csv.gz`: `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime`.
- `hosp/transfers.csv.gz`: `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`.
- `icu/inputevents.csv.gz`: `subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom, orderid, linkorderid, patientweight, statusdescription, totalamount, totalamountuom`.
- `icu/outputevents.csv.gz`: `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom`.
- `icu/procedureevents.csv.gz`: `subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, statusdescription, continueinnextdept, orderid, linkorderid`.
- `icu/chartevents.csv.gz`: `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom, warning`.
- `icu/d_items.csv.gz`: `itemid, label, abbreviation, linksto, category, unitname`; join ICU events by `itemid`. Direct source inspection confirmed the specified loop, ventilation, extubation/intubation and RRT item labels; no patient rows are cited.
- `hosp/labevents.csv.gz`: `labevent_id, subject_id, hadm_id, itemid, charttime, storetime, valuenum, valueuom, flag`; `hosp/d_labitems.csv.gz`: `itemid, label, fluid, category`.
- `hosp/emar.csv.gz`: `subject_id, hadm_id, emar_id, emar_seq, charttime, storetime, medication, event_txt`.
- `hosp/emar_detail.csv.gz`: `subject_id, emar_id, emar_seq, parent_field_ordinal, administration_type, complete_dose_not_given, dose_given, dose_given_unit, product_amount_given, product_unit, product_description, route, infusion_rate, infusion_rate_unit`.
- `hosp/procedures_icd.csv.gz`: `subject_id, hadm_id, seq_num, chartdate, icd_code, icd_version`; `hosp/d_icd_procedures.csv.gz`: `icd_code, icd_version, long_title`.
- `hosp/services.csv.gz`: `subject_id, hadm_id, transfertime, prev_service, curr_service`.
- `hosp/diagnoses_icd.csv.gz` plus `hosp/d_icd_diagnoses.csv.gz`: completed prior admissions only.
- `hosp/prescriptions.csv.gz` and `hosp/pharmacy.csv.gz`: order-versus-administration diagnostics only.

Optional radiology is the separate read-only ordinary gzip `[internal dataset path]`, columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; it is excluded unless a frozen timely parser and blinded clinical adjudication are supplied. No images or waveforms are available. All four configured datasets remain readable, but only MIMIC realizes this linked contract; derived files stay in the workspace.

## Verifier and evidence limits

Required outputs are partition proof and attrition; one row per subject/clone; raw row provenance and both clocks; exposure status/unit/route aggregation; every clone-hour transition and probability; overlap, weights and ESS; competing states; all individual and arm bounds; bootstrap endpoints; destination and route sensitivities; stochastic-policy and confounding grids; gate booleans; magnitude status; and clinical branch. Every numerical sentence must point to an output field.

The verifier can check hashes, headers, joins, partition, times, item/status/unit rules, eMAR sibling aggregation, route labels, state transitions, terminal precedence, weight arithmetic, state sums, bound orientation, margins and branches. Challenge fixtures must include: correct computation plus an unsupported “IV/causal/safe” conclusion (reject); primary benefit with ALDL lower-limit below −.05 (inconclusive, not supportive); optimistic RRT nonharm with conservative upper bound above +.05 (inconclusive); each adverse trigger; route-unavailable but otherwise valid primary output; and sparse/failed-overlap output.

No automatic verifier can establish bedside congestion/readiness, clinician intent, actual route where absent, goals of care, destination appropriateness, functional recovery, complete external death/readmission/dialysis, exchangeability, transportability, renal safety or causal benefit. These require blinded clinical adjudication, external linkage/validation, and preferably randomization.
