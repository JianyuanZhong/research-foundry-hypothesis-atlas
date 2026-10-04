# Episode 64: competing-state endpoint repair for the hour-48 post-shock loop policy

Parents: `[prior hypothesis]` and `[prior hypothesis]`.

## Substantive advance and unresolved question

This child preserves the assigned Episode-61 population, decision-time chronology, A12/B12 equal-clone policy question, treatment-before-airway boundary, recording-time objects, multisource RRT definition, bounded endpoints, bootstrap/Holm uncertainty, and noncausal evidence boundary. It repairs a different problem: the primary airway endpoint is not a coherent competing-outcome description when follow-up ends in an ICU gap, live hospital discharge, or incomplete same-admission observation. Those states are not equivalent to airway failure, but they can be assigned the broad `[0,1]` endpoint interval. Reporting continuous-ICU, off-ICU, chart-augmented, and ward-gap variants separately does not force the clinical interpretation to distinguish liberation from informative observation loss.

The clinically important question remains:

> Among adults still invasively ventilated at ICU hour 48 after recent recorded vasopressor support and six recorded pressor-free hours, with marked recorded fluid accumulation and adequate recorded MAP, urine output and potassium, is follow-up compatible with initiating/restarting an ICU-recorded furosemide or bumetanide delivery during the next 12 hours associated with a greater probability of confirmed airway liberation by day 5 without a compensating increase in death or airway failure before confirmation, compared with remaining compatible with no such initiation?

The strongest evidence-supported claim remains only that fluid-removal timing is clinically important and incompletely standardized, and that MIMIC contains computable but imperfect recorded treatment, airway, physiology, RRT, disposition, and mortality proxies. The inspected Bircher et al. 2026 full XML and the parent-inspected limited-evidence guideline/trial materials support uncertainty and the importance of timing; they do not establish efficacy, safety, exchangeability, or validity of this phenotype. No treatment or outcome contrast was estimated while developing this child. The unresolved claim tested here is a recorded-policy association with a mutually exclusive airway/competing-observation endpoint. It is not an effect of received furosemide, proof of durable extubation, renal safety, or a treatment recommendation.

## Exact source, provenance, and availability

Use only the MIMIC-IV 3.1 archive, read-only:

- Archive: `[internal dataset path]`
- Archive [source checksum]
- Snapshot: `[source checksum]`
- Catalog: `[internal dataset path]`
- Catalog [source checksum]

The exact source catalog and `datasets/README.md`, `datasets/mimic/README.md`, and the research-ambition README were inspected. The configured HCC, eICU, and UKB sources remain accessible but are not validation cohorts. MIMIC note files exist, but this experiment does not use note text to manufacture an airway state or clinical adjudication. Raw waveforms and radiology images are unavailable and unused.

Before clinical inspection, retain only subject buckets 0--79 from
`SHA256("ehr-hypothesis-discovery-v1"+NUL+"mimic"+NUL+canonical_base10_subject_id mod 100`; buckets 80--99 remain untouched. Preserve within-subject time intervals; never align subjects by calendar date.

The required archive members and exact bindings are:

- `mimic-iv-3.1/icu/icustays.csv.gz`, `icu/icustays`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los` join on all three encounter IDs; ICU observation clocks are `intime,outtime`.
- `mimic-iv-3.1/hosp/admissions.csv.gz`, `hosp/admissions`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,race,hospital_expire_flag`; join on `subject_id,hadm_id`; terminal/discharge clocks are `deathtime,dischtime`.
- `mimic-iv-3.1/hosp/patients.csv.gz`, `hosp/patients`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; join on `subject_id`; `dod` is date-only and has no availability clock.
- `mimic-iv-3.1/hosp/transfers.csv.gz`, `hosp/transfers`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; join on `subject_id,hadm_id`; use only for same-admission observation topology and positive-gap ICU exit.
- `mimic-iv-3.1/icu/procedureevents.csv.gz`, `icu/procedureevents`: `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,value,valueuom,orderid,linkorderid,statusdescription`; join on all encounter IDs; clinical interval is `starttime,endtime`, database clock is `storetime`.
- `mimic-iv-3.1/icu/inputevents.csv.gz`, `icu/inputevents`: encounter IDs plus `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,statusdescription,patientweight,totalamount,totalamountuom`; pressor, loop, fluid-input, sedative, and positive-input RRT clocks are `starttime,endtime`, with `storetime retained for the inherited E_T/E_M/E_G analysis.
- `mimic-iv-3.1/icu/chartevents.csv.gz`, `icu/chartevents`: encounter IDs plus `charttime,storetime,itemid,value,valuenum,valueuom,warning`; clinical clock is `charttime, recording clock is `storetime.
- `mimic-iv-3.1/icu/outputevents.csv.gz`, `icu/outputevents`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom`; urine and output balance use `charttime, recording-time analysis uses `storetime.
- `mimic-iv-3.1/hosp/labevents.csv.gz`, `hosp/labevents`: `labevent_id,subject_id,hadm_id,specimen_id,itemid,charttime,storetime,valuenum,valueuom`; creatinine and potassium use `charttime`, with `storetime` in recording-time branches.
- `mimic-iv-3.1/hosp/procedures_icd.csv.gz`, `hosp/procedures_icd`: `subject_id,hadm_id,seq_num,chartdate,icd_code,icd_version`; date-bracketed RRT only, no recording clock.
- `mimic-iv-3.1/icu/d_items.csv.gz`, `icu/d_items`: validate `itemid,label,abbreviation,linksto,category,unitname,param_type`.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`, `hosp/d_labitems`: validate `itemid,label,fluid,category`.
- `mimic-iv-3.1/hosp/d_icd_procedures.csv.gz`, `hosp/d_icd_procedures`: validate `icd_code,icd_version,long_title`.

The cataloged schema for `icu/procedureevents` includes `starttime,endtime,storetime,itemid,orderid,linkorderid,statusdescription`; `icu/icustays` includes `intime,outtime`; `hosp/transfers` includes `eventtype,careunit,intime,outtime`; and `hosp/admissions` includes `deathtime,dischtime,discharge_location,hospital_expire_flag`. The cataloged `icu/outputevents` and `icu/chartevents` schemas include both their clinical and recording clocks. Their schema hashes are, respectively, `[source checksum]`, `[source checksum]`, `[source checksum]`, `[source checksum]`, `[source checksum]`, and `[source checksum]`.

## Inherited population and decision-time protocol

The following Episode-61 protocol is normative and is not to be silently simplified by the compiler.

Freeze the earliest adult ICU stay ordered by `(intime,stay_id)`, with `t0=intime+48h` strictly before both `outtime` and `dischtime`, at or after `admittime`, and accepted same-stay invasive ventilation procedure item 225792 satisfying `starttime<=t0<endtime`, `endtime>starttime`, coherent encounter keys, and accepted status `FinishedRunning` or `Stopped`. Approximate age as `anchor_age+calendar_year(intime)-anchor_year`. Do not reopen a later stay.

Retain only final clinical-time opportunities satisfying all inherited gates: a valid pressor course from items 221289, 229617, 221662, 221749, 229630, 229631, 229632, 221906, 222315 in the recent window `(t0-24h,t0-6h]` and none valid or ambiguous in `(t0-6h,t0]`; MAP items 220052/225312 preferentially or 220181 with median at least 65 mmHg in `(t0-3h,t0]`; weight items 226512 or 224639, 30--300 kg; urine items 226557, 226558, 226559, 226560, 226561, 226563, 226564, 226565, 226567, 226584, 226627, 226631 above 0.1 mL/kg/h in `(t0-6h,t0]`, excluding 226566, 227489, 226713; potassium 50971 preferentially or 52610, at least 3.0 in `(t0-12h,t0]`; no ECMO from procedure items 229529/229530 or active-flow chart items 224660/229270; no active RRT from inherited procedure/input/chart/ICD item and code set; unit-safe balance from `intime` through `t0` at least +50 mL/kg with eight six-hour coverage bins; and no qualifying or ambiguous loop course in `(t0-12h,t0]`. Mandatory balance thresholds are +30 and +100 mL/kg; pressor-course robustness includes recent union >=1h, >=6h, maximum contiguous >=6h, and all-prior union >=6h. Retain the inherited ambiguity rules, exact deduplication, half-open intervals, units, statuses, tie handling, and no cross-admission carryover.

A qualifying loop is inputevents item 221794, 228340, or 229639 with coherent keys, `endtime>starttime`, accepted status `FinishedRunning`, `ChangeDose/Rate`, or `Stopped`, and positive finite amount in mg or rate in mg/hour; exact duplicates collapse; unknown units, nonpositive/contradictory rows, `Paused`, literal `Bolus`, cancelled/order-only rows, and exact ties are ambiguous. Routine one-minute accepted drug pushes remain eligible. Group by `linkorderid`; onset is earliest qualifying `starttime`, and `storetime` never moves the clinical event time.

Create equal-weight A12 and B12 clones at `t0`. Let `G12=t0+12h`. Select the linked same-stay ventilation interval V for the earliest accepted extubation task X (item 227194, `FinishedRunning`) with `V.starttime<X` and `X-2h<=V.endtime<=X+6h`, breaking ties by absolute endtime distance, latest V start, numeric orderid, numeric linkorderid, missing last. Set `C=min(X,V.endtime)`. A12 requires first qualifying loop onset strictly in `(t0,min(G12,C))`; B12 has no qualifying onset through `min(G12,C)`. A loop exactly at C is ambiguous. If V ends without linked X, its earliest verified end is shared closure and airway status is unknown. Apply precedence: resolved death, exact loop/airway ambiguity, positive-gap ICU exit, strictly ordered loop versus C, then G12. Never use post-t0 information to define eligibility, baseline covariates, or weights.

Retain the inherited recording-time objects: E_T is an audit-only maximal timestamped-gate as-of reconstruction allowing timestamped rows only when nonmissing `storetime<=t0`, while clockless structural and ICD facts remain flagged; E_M is the non-adding strict intersection `E_R∩E_T∩{late_conflict=false}`; E_G is nested in E_M and requires every accepted or gate-relevant ambiguous row for a timestamped pre-t0 gate to have `storetime<=t0`. Rebuild covariates, folds, models, weights, endpoints, and uncertainty independently in each feasible branch. Require Jaccard(E_R,E_T)>=0.90 and retained E_M/E_R>=0.90 for temporal concordance; otherwise the recording-time result is validity-inconclusive, not adverse evidence.

## Repaired endpoint: fixed-horizon competing states

Set `D5=t0+5d` and `H7=t0+7d`. The existing RHA-E48-D5 remains a secondary endpoint exactly as inherited: first accepted linked X by D5 with 48h event-free follow-up; death or observed airway failure is zero; unresolved linkage/conflict or inadequate coverage is `[0,1]`; report chart-augmented, continuous-ICU, off-ICU/open-admission, early-live-discharge, and missing/conflicting variants.

The new primary endpoint is a set-valued, mutually exclusive state at H7. It is evaluated without changing treatment assignment or decision clocks. For each clone, determine the earliest applicable state under the following fixed precedence:

1. **Confirmed airway liberation (S1).** An accepted X=item 227194 occurs by D5, is linked to V by the inherited rule, and from X through X+48h there is no accepted recurrent intubation/ventilation (224385 or 225792), unplanned extubation (225468/225477), tracheostomy (225448/226237), or accepted chart-derived invasive/tracheostomy state using items 226732, 223849, 229314 under the inherited pinned-value rules. The required 48h period must remain same-admission observed; a positive ICU gap or live discharge before X+48h is not success. This is a recorded liberation proxy, not confirmed tube removal or durable physiologic independence.

2. **Competing death before S1 confirmation (S2).** A definite death time `admissions.deathtime` or a death-disposition record with a time no later than H7 occurs before S1 is confirmed. Use the inherited lower/upper death rules: exact `deathtime` is lower-bound evidence; `hospital_expire_flag=1`, `discharge_location=DIED`, and date-only `patients.dod` supply only their prespecified upper brackets. Do not treat a date-only death as an exact time.

3. **Competing airway failure before S1 confirmation (S3.** An accepted recurrent invasive ventilation/intubation, unplanned extubation, or tracheostomy event occurs before S1 confirmation, using the same procedure/chart item/status and encounter-key rules. If a later X would otherwise satisfy S1, S3 still wins because the first attempted liberation was not failure-free.

4. **Observed persistent ventilation at H7 (S4.** There is no S1--S3 and an accepted V or chart-derived invasive state crosses H7, with continuous same-admission/ICU observation to H7. This state means no recorded liberation by the fixed horizon, not clinical treatment failure.

5. **Observation/disposition loss before classification (S5.** There is no S1--S4, but same-admission observation ends before the required state can be determined because of a positive-gap ICU exit, live hospital discharge before H7, or early record closure. Use `icu/icustays` and `hosp/transfers` for ICU gaps, and `hosp/admissions.dischtime/discharge_location/hospital_expire_flag` for discharge. A positive-gap ICU exit is not reclassified as airway success or failure. If death is also bracketed but timing is unresolved, retain a set-valued S2/S5 state.

6. **Unresolved/contradictory (S6.** Conflicting exact-time airway linkage, unresolved event status/tie, missing clinical times, or insufficient data to distinguish S1--S5. S6 is not a treatment outcome and cannot be called harm or benefit.

For each subject, save the allowable state set, the reason, first state time, source table/item, and whether the state is lower-bound definite or only upper-bound possible. Do not force S6 or S5 to S1/S3. Use deterministic states when evidence is sufficient and set-valued states otherwise. State sets must obey the fixed precedence and sum to one across S1--S6 for each clone.

This endpoint explicitly separates three clinically different findings that the inherited binary endpoint can conflate: confirmed recorded liberation, persistent ventilation, and observation/disposition loss. It also prevents a live ICU exit or early discharge from being presented as airway improvement. It does not establish why an observation gap occurred or whether an extubation reflected readiness, goals of care, or actual tube removal.

## Estimand and analysis

For every feasible population E_R, E_M, and E_G, estimate the A12-minus-B12 arm risk-difference vector
`Delta_s = P(S=s | A12 policy) - P(S=s | B12 policy)`, s=1,...,6, under the inherited equal-clone measured-overlap clone-censor estimand. Use the inherited five subject folds, cross-fitted arm-specific hourly compatibility models using only pre-interval X0 and pre-interval history, stabilized inverse-probability compatibility weights, [0.01,0.99] denominator clipping, pooled 1st/99th weight truncation, and normalized Hájek risks. Never use complete cases or midpoint imputation.

For a state set A_i, its arm-specific lower state indicator is 1 only when S_i={s}; its upper indicator is 1 when s is in A_i. Use
`Delta_s^L=p^L_{A,s}-p^U_{B,s} and
`Delta_s^U=p^U_{A,s}-p^L_{B,s}.
Report the full state vector, its interval widths, sum-to-one diagnostics for definite and possible masses, unknown-state mass, and all reasons for S5/S6. These bounds are conservative and do not assume that discharge is favorable, death timing is exact, or unknown airway states are negative.

The formal primary contrast is the prespecified liberation-versus-competing-harm pair:
- `Delta_1: S1 confirmed liberation;
- `Delta_{2+3}: S2 or S3 before S1 confirmation.

Treat S4, S5, and S6 as essential interpretability diagnostics, not evidence of success or harm by themselves. A primary supportive-recorded branch requires `Delta_1 lower one-sided 95% limit >+0.05, `Delta_{2+3} upper one-sided 95% limit <=+0.03, no increase in S5 upper limit >+0.03, and no adverse RCR/RRT/terminal/disposition family under the inherited margins. It also requires the inherited E_R validity, Jaccard/retention, positivity, balance, ambiguity, observation, timing, contamination, and process checks. If S1 improves but S5 also increases materially, classify the airway interpretation as observation-sensitive, not supportive.

Run 1,999 successful subject-level full-pipeline bootstraps with PCG64 seed 480048, at most 2,499 attempts and no more than 5% failed attempts. Each draw independently rebuilds states, allowable sets, folds, preprocessing, models, overlap, weights, all state bounds, and inherited outcomes. Use joint subject bootstrap resampling for the six-state vector and the formal S1/S2+S3 contrasts. Keep the inherited centered one-sided p-values and Holm step-down FWER 0.05 across the eight inherited families; within the airway family use a max-statistic over the S1 improvement, S2+S3 harm, and S5 observation-loss alerts so the new endpoint does not create unadjusted multiplicity. Pointwise state intervals and raw p-values are descriptive.

Retain inherited minima: eligible n>=200, A12 satisfaction >=100, B12 completion/shared closure >=100, ESS>=75 per arm, and >=100 definite primary events. Add endpoint-feasibility diagnostics, not a new post hoc threshold: definite-state mass, S5+S6 mass, state-vector interval width, and whether the formal S1/S2+S3 contrasts are estimable. If the state vector is too unresolved for the formal contrasts, classify the competing-state endpoint as endpoint-inconclusive while preserving the inherited RHA result as secondary; do not call that adverse or supportive.

## Falsification and interpretation

- **Supportive-recorded:** inherited E_R computation and validity pass; the formal S1 improvement and S2+S3 non-harm criteria pass; S5 does not increase beyond +0.03; no inherited renal/RRT/terminal/disposition adverse family is Holm-rejected; all required temporal branches meet their criteria; and no mandatory variant materially reverses the primary branch.
- **Adverse-FWER:** a prespecified inherited adverse family or the max-statistic airway competing-harm component is Holm-rejected with validity passing. This is a record-defined observational concern, not toxicity or causality.
- **Margin-falsified:** no adjusted adverse family and the upper limit for S1 improvement is <=+0.05, or the S2+S3 upper limit exceeds +0.03. This rejects the proposed recorded-policy benefit/safety margin, not every deresuscitation strategy.
- **Observation-sensitive:** S1 appears favorable but S5 upper increase exceeds +0.03 or the S5/S6 mass makes state classification materially unresolved. No airway benefit claim follows.
- **Endpoint-inconclusive:** computation succeeds but set-valued state uncertainty prevents the formal competing-state contrasts or the endpoint feasibility diagnostic fails. RHA is reported only as its bounded secondary.
- **Temporal-validity-inconclusive:** E_R/E_T concordance, E_M retention, or late-conflict computation fails. No treatment direction follows from that branch.
- **Recording-time-inferential-infeasible:** M or G fails inherited computational minima; no direction from that branch.
- **Validity-inconclusive:** any other source, join, chronology, positivity, calibration, balance, ambiguity, contamination, observation, bootstrap, multiplicity, or material-reversal gate fails.
- **Statistically inconclusive:** all required computation and validity checks pass but no prespecified branch is met.
- **Infeasible:** required source, state classification, model, or bootstrap computation cannot be completed; no direction follows.

A supportive state-vector result still supports only external validation or randomization. It cannot establish actual loop delivery, dose, route, clinician awareness, shock resolution, congestion, extubation readiness, tube removal, durable airway independence, KDIGO AKI, renal safety, goals of care, exchangeability, causality, transportability, or actionability. These require validated administration/airway linkage, fuller notes or adjudication by blinded critical-care/nephrology reviewers, external outcome linkage and replication, and preferably prospective randomization.

## Compiler and verifier contract

The compiler must reproduce the inherited archive/hash/header assertions, discovery partition, exact gates, encounter joins, half-open intervals, E_R/E_T/E_M/E_G equations, A12/B12 transition rules, `C=min(X,V.endtime)`, treatment-before-C ordering, inherited endpoints, and bootstrap/Holm contract. It must additionally test:

- exact H7/D5 boundary inclusion and X+48h closure;
- procedure/chart item and accepted-status fixtures for S1--S4;
- positive-gap ICU transfer and live-discharge fixtures that must yield S5, never S1;
- death-time versus date-only death fixtures yielding set-valued S2/S5 rather than an exact state;
- first-failure precedence when a later extubation occurs;
- unresolved airway-linkage and conflicting-timestamp fixtures yielding S6;
- state-set sum-to-one, lower/upper state-mass bounds, `Delta_s interval construction, and max-statistic airway family adjustment;
- independently rebuilt E_M/G state endpoints and no reuse of E_R fits;
- correct computation paired with unsupported causal, safety, receipt, durable-extubation, equivalence, or recommendation language.

Automatically checkable claims are source hashes/schemas, joins, row clocks, cohort membership, state precedence, item/status rules, allowable state sets, outcome bounds, weights, state contrasts, bootstrap/Holm outputs, diagnostics, and whether prose matches the branch. Automatic computation cannot establish the clinical truth represented by S1, actual liberation, why an ICU gap occurred, intent, readiness, goals of care, exchangeability, causality, safety, or actionability. The verifier must therefore fail unsupported stronger claims and must test supportive, adverse, margin-falsified, observation-sensitive, endpoint-inconclusive, temporal-validity-inconclusive, statistically inconclusive, and infeasible fixtures.

## Change note

This is a substantive endpoint repair, not a compiler edit. It keeps the inherited decision-time population and all source/time bindings, but makes the primary outcome a fixed-horizon state vector that explicitly separates confirmed recorded liberation, death, airway failure, persistent ventilation, and observation/disposition loss. The inherited RHA-E48-D5 remains a secondary diagnostic. The remaining uncertainty is the clinical validity of structured airway and observation proxies, unresolved death timing, and observational exchangeability; these are preserved as bounded or adjudication-dependent rather than converted into clinical truth.
