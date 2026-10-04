# Can eICU hospitals be compared on sustained liberation after bounding source-dependent ascertainment?

## Status, scientific opening, and deliverable

This is a narrow substantive child of `[prior hypothesis]` and a planned measurement-first experiment, not an executed clinical result. It preserves that parent's population, clocks, endpoint, two-stage probability sample, direct and learned measurement models, <=3-point comparability gate, competing events, and matched recovery models. It corrects one consequential source-availability error: eICU has a structured `note` table containing Extubation and Intubation procedure-note fields. Those events add an independent corroboration and false-negative sentinel, but their severe hospital concentration prevents treating them as a gold standard.

The strongest evidence-supported claim is that ventilator-discontinuation practices vary, death before a weaning attempt is common [K1], and successful liberation must remain free of reintubation or death for a defined period while transfer is handled explicitly [K2]. Longitudinal respiratory models can derive transition states from EHR measurements, but their labels and transport remain dependent on local documentation [K3]. The attached eICU audits add observed data facts, not clinical conclusions: `notetype=Extubation` yields 1,431 unique stay-offset events in 1,340 stays across 20 hospitals, but 78.5% of those stays are at hospital 420 and only four hospitals have at least 20; `notetype=Intubation` yields 1,337 unique stay-offset events in 1,174 stays across 31 hospitals. None of these observations establishes clinical truth, comparable source sensitivity, or different patient recovery across hospitals.

**Primary measurement hypothesis (tested first):** after probability-sampled clinician review of both phenotype-positive and phenotype-negative complete episodes, hospital-specific sensitivity and PPV of the frozen sustained-liberation phenotype are sufficiently high and comparable that source-dependent misclassification alone could induce no more than a 3-percentage-point P90–P10 hospital contrast in standardized 14-day liberation risk.

**Conditional recovery hypothesis (tested only if the measurement gate passes):** among adults invasively ventilated 24 hours after a documented first IMV start, the target-standardized 14-day cumulative incidence of true/adjudication-calibrated sustained liberation differs across eligible hospitals after baseline severity adjustment, with a P90–P10 contrast at least 10 percentage points and a 95% lower bound above 5 points in both a transparent multistate baseline and a learned longitudinal alternative.

The deliverable is therefore ordered: (1) freeze the cohort and phenotype; (2) estimate or conservatively bound sensitivity, PPV, specificity, timing error, and ascertainment-only hospital contrast; (3) issue a machine-readable GO/NO-GO/UNRESOLVED decision; and only after GO, (4) fit the recovery models. Measurement comparability is not itself evidence of recovery heterogeneity, and recovery heterogeneity is not a causal practice or quality effect.

## Population, clocks, and frozen observed phenotype

Build one hospital timeline per `patienthealthsystemstayid` by joining all `patient` unit rows. For any event at unit-relative offset (u), hospital-relative time is (u-	exttt{hospitaladmitoffset}). Verify that `hospitalid` is constant within each hospital stay; exclude and report discordant chains. Stitch linked ICU units, including “Other ICU” transfers, before defining outcomes.

A high-confidence first IMV start (t0) is the earliest valid nonzero `priorventstartoffset` or `ventstartoffset` with either (a) a valid respiratoryCare interval and invasive airway, or (b) temporally concordant invasive ventilator/device charting or mechanical-ventilation treatment evidence. APACHE `intubated=1` and `vent=1` corroborate status but cannot timestamp it. Freeze exact label dictionaries before review. Noninvasive CPAP/BiPAP and tracheostomy are not oral/nasal endotracheal IMV.

The landmark is (L=t0+24) hours. Include adults age >=18 who are demonstrably in state V at L, have an observed hospital timeline through L, and have a hospital identifier. Exclude tracheostomy at/before L and unparseable age. Use one episode per hospital stay. Repeated people remain eligible, but all `uniquepid` records share split and bootstrap membership. Index-state ascertainment is audited separately; chart silence never establishes continuous IMV.

Follow from L through L+14 days, hospital death, or observation-ending discharge/transfer. The frozen observed algorithm (A) has states:

- V: invasively ventilated at L.
- P: provisional liberation at a valid historical interval end or explicit RT Vent On/Off off/suspended event. The trigger and its source are retained. A structured Extubation note can corroborate and time-bound P but cannot create P by itself in the primary phenotype.
- S: alive and observed for 48 hours after P with no high-confidence invasive restart.
- R: high-confidence IMV reinstitution within 48 hours after P; later P is allowed.
- T: tracheostomy after L, a separate competing transition.
- D: death in V/P/R, using unit/hospital discharge status and timing.
- X: alive hospital discharge, external transfer, or an unstitched observation-ending ICU exit before respiratory state can be established through 48 hours.
- C: administratively still V/P/R at day 14.

A later valid interval start, explicit RT start/continued with invasive settings, or concordant treatment plus invasive-device evidence defines R. A structured Intubation note can corroborate and time-bound R but cannot create R by itself in the primary phenotype. Treatment “ventilator weaning” is context, not liberation. Structured note values such as self-extubation, trial/extubation reason, perceived support need, or immediate reintubation are contextual evidence for adjudication, never automatic truth. Silence is neither P nor S. Seven-day sustained liberation is a prespecified sensitivity analysis. The primary unit is the hospital stay; timing tolerance is +/-6 hours for source concordance.

Hospitals enter measurement sampling if they have >=50 frozen index episodes; there is no pre-validation filter on detected endpoints or source mix, because either would preferentially remove low-sensitivity hospitals. At least 30 hospitals must pass the later measurement gate and retain an effective clinician-estimated count of >=20 true S events for recovery modeling; these thresholds are not relaxed after seeing results.

## Measurement experiment: a denominator, not another positive-event audit

Let (Z) be clinician-adjudicated sustained liberation by day 14 and (A) the frozen structured phenotype. The target quantities in every hospital (h) are:

- sensitivity (Se_h=P(A=1|Z=1,h));
- PPV (PPV_h=P(Z=1|A=1,h));
- specificity and NPV as secondary completeness checks;
- absolute event-time error among true-positive pairs;
- the P90–P10 contrast in (Se_h);
- the P90–P10 observed-risk contrast that the fitted measurement process would produce under a common true risk and the observed hospital source mix (“ascertainment-only bias”).

### Two-phase probability sample

After cohort and (A) are frozen, review **every A=0 episode** in every eligible hospital. This negative census supplies the denominator needed to find false negatives. Prespecify A=0 strata for Extubation note within the risk window, Intubation note after a plausible unrecognized liberation, other non-trigger sentinels, and no sentinel; the note-positive strata enrich the review frame descriptively without changing census inclusion probability (one). Within each hospital review a deterministic-hash sample of (min(40,N_{h,A=1})) A=1 episodes, stratified across trigger-source signature (including note-corroborated versus not), event-time quartile, and reconstructed R status; sample all cells with fewer than the allocated count. Record each inclusion probability. No outcome/model result may alter the sample.

The bounded proxy audit found 4,652 stays in 33 hospitals under the explicit approximation “adult first ICU unit, APACHE intubated=vent=1, observed beyond ICU hour 24, prior respiratoryCare interval spanning hour 24, hospital >=50.” It contained 4,501 candidate interval ends and 151 negatives. Reviewing all negatives plus up to 40 positives/hospital would require 1,471 packets (2,942 independent first-pass reviews). This is a feasibility estimate, not the final t0-based cohort or an estimate of phenotype validity. The final sample size is generated from the frozen cohort and reported.

Two ICU clinicians independently review every packet; a third resolves disagreements. Packets show a recentered structured timeline from t0 through follow-up: normalized airway/device states, ventilator settings, RT on/off entries, treatment events, deduplicated Extubation/Intubation note paths and values, subsequent invasive starts, tracheostomy, death, and exits. Private raw note fields remain in the workspace and are rendered only into coded reviewer packets; hospital/ward identifiers, candidate label, derived state, and source table names are hidden. Reviewers label IMV at L; liberation yes/no/indeterminate; earliest plausible transition interval; reinstitution within 48 hours; tracheostomy; death; X; and confidence. They cannot infer an event from silence or regard a note row as a gold standard.

To expose incorporation bias, review is locked in two passes. Pass 1 suppresses the exact non-note row family that triggered A for positive packets while leaving a temporally concordant Extubation/Intubation note visible as an independent corroboration channel; pass 2 reveals the complete structured packet. Record separately whether a decision was supported by the note channel under trigger suppression and repeat the measurement summaries with the note family suppressed. An event supported only after trigger reveal, or only by a structured note, is labeled **source-dependent**, not independently confirmed. Negative packets have no algorithm trigger to suppress and show all available evidence, with note-positive windows explicitly flagged only in the hidden sampling metadata. The primary reference has three levels: definite, no, and unresolved (probable, source-dependent, disagreement, or insufficiently observed). Raw reviewer labels are retained; arbitration does not convert missing evidence into truth. This design can validate or bound a structured-record phenotype, but no clinician can recover an extubation that left no trace in any available structured field.

### M0: direct design-weighted measurement baseline

Use Horvitz–Thompson weights from the frozen sampling fractions to estimate each hospital’s confusion table and timing-error distribution. Cluster uncertainty by person and use stratified survey bootstrap intervals. Report complete-case estimates and nonparametric ambiguity bounds. For example, the lower sensitivity bound assigns every unresolved A=0 episode to a missed true event and no unresolved A=1 episode to a true event; the upper bound makes the reverse assignments. Apply the analogous worst cases to PPV. Report effective sample sizes and simultaneous 95% intervals across hospitals.

M0 is transparent and makes minimal modeling assumptions. It loses temporal ordering and information in source overlaps; estimates can be wide in smaller hospitals.

### M1: hierarchical multi-source hidden semi-Markov alternative

On the same cohort, review sample, state definitions, and six-hour grid, fit a Bayesian hidden semi-Markov measurement model with latent V/P/S/R/T/D/X states. Emissions are source-family indicators from respiratoryCare intervals/airways, respiratoryCharting devices/settings/RT on-off, treatment ventilation/weaning/reintubation/tracheostomy, the separate structured-note Extubation/Intubation family, and disposition. Death and verified exits are constrained absorbing states. Hospital-specific source sensitivities and false-positive rates are partially pooled, with source-pair interaction terms to relax conditional independence. Note-family parameters are not transported from note-rich to note-sparse hospitals without direct support; hospital 420 is never allowed to identify a universal note sensitivity. Reviewer-specific confusion matrices are learned from duplicate review; definite consensus labels anchor the latent states, while unresolved labels contribute only their observed uncertainty. `actualventdays` and note events are auxiliary emissions, never timestamps of truth or gold standards.

Assign reviewed packets to five deterministic `uniquepid` folds within hospital/source stratum. Generate cross-fitted latent-state probabilities for every reviewed episode, then evaluate held-out log score, Brier score, calibration, transition-time coverage, and source-pattern posterior predictive checks against M0. Fit priors and all tuning without access to hospital recovery contrasts. The final measurement posterior may use all review data only after model form and diagnostics are frozen.

M1 can use overlap patterns, clinical state persistence, and reviewer error to estimate where direct hospital tables are sparse. It is scientifically useful only if it improves held-out adjudication and passes conditional-dependence/source-removal stress tests; partial pooling is not evidence that unsupported hospitals are comparable. If M0 and M1 disagree materially, the measurement question is unresolved and recovery modeling is prohibited.

## Pre-recovery comparability gate

Issue GO only if every condition is met:

1. At least 30 hospitals retain >=50 index episodes and an effective design-weighted count of >=20 clinician-estimated true S events; no hospital is selected on raw A-positive count.
2. Pairwise clinician kappa and Gwet AC1 for S are both >=0.70; at least 90% of packets receive a definite consensus after full review. Report agreement by hospital and source signature.
3. The pooled point estimates of sensitivity and PPV are each >=0.85 and their conservative 95% lower bounds are each >=0.80.
4. For every retained hospital, sensitivity and PPV have simultaneous 95% interval width <=0.20; no hospital has a conservative lower bound below 0.70.
5. Under M0 and M1 separately, the 97.5th percentile of the ascertainment-only P90–P10 standardized risk contrast is <=3 percentage points. M0 and M1 point estimates of that contrast differ by <=2 points.
6. The 95% upper bound for the hospital P90–P10 sensitivity difference is <=0.10. Trigger-suppressed and full-packet analyses cannot differ in standardized hospital contrast by >3 points.
7. Leave-one-source-family-out fits (including complete removal of the note family), note-rich-hospital exclusion, seven-day sustain, +/-6-hour timing perturbation, and treating all unresolved cases in worst directions retain the <=3-point ascertainment-bias bound. M1 also passes held-out calibration and source-pattern posterior predictive checks.

A failure with precise estimates is **NO-GO** and supports source-dependent noncomparability. Wide intervals, excess unresolved packets, weak inter-reviewer agreement, insufficient hospitals, or M0/M1 disagreement are **UNRESOLVED**. Both outcomes terminate the between-hospital recovery analysis. They are not invitations to exclude inconvenient hospitals, relax thresholds, or replace the endpoint with `actualventdays`.

## Conditional recovery experiment after GO

The primary estimand for hospital h is the 14-day cumulative incidence of S if h’s fitted transition process applied to the pooled eligible-cohort baseline distribution, preserving D, X, R, and T as competing events. Primary heterogeneity is the P90–P10 absolute standardized risk difference. Fit the observed endpoint and adjudication-calibrated multiple imputations drawn from the frozen measurement model; a supportive result must hold in both.

### B: transparent competing-risk baseline

Fit a hierarchical semi-Markov piecewise-exponential model for V→P, P→S, P→R, R→P, and V/P/R→D, X, or T, with six-hour intervals on days 1–3 and daily intervals thereafter. Inputs end strictly before L: demographics, admission context, APACHE severity/comorbidity, pre-L EOL documentation, and prespecified first/last/min/max/slope/burden/count summaries of respiratory settings, oxygenation, vital signs, labs, sedative/opioid/pressor exposure, missingness, and entry delay. Use restricted cubic splines and partially pooled hospital transition intercepts. Standardize by g-computation over the pooled baseline distribution.

### L: learned physiology-versus-observation alternative

Using the identical inputs, patients, folds, transition targets, and estimand, fit a two-layer 64-unit GRU over four pre-L six-hour bins. Separate a physiologic state, trained to reconstruct next-bin respiratory/oxygenation/hemodynamic burden, from an observation state trained to reconstruct label availability, counts, and entry delays. Both feed the same allowed transition heads. A gradient-reversal penalty limits conditional hospital prediction from physiology; hospital effects appear only in transition heads. Reject L if leakage macro-AUROC exceeds 0.65, multistate calibration is worse than B, or ablations show that its claimed separation is unsupported.

Both models use five deterministic patient-grouped folds with every `uniquepid` in one fold and every hospital represented. All preprocessing and tuning occur within training folds. Compare transition likelihood, integrated Brier score, state calibration at days 3/7/14, reintubation calibration, standardized risks, competing-event tradeoffs, and hospital-order stability. Use 1,000 bootstraps resampling hospitals then people. B preserves interpretable pathways but loses within-day order and nonlinear covariation; L tests whether recovery ordering versus observation dynamics explains variance that B assigns to hospitals.

## Exact read-only eICU bindings

All sources are ordinary gzip CSV files under:

`[internal dataset path]`

Catalog snapshot [source checksum]. Files remain read-only; derived packets contain coded rows only and remain private.

- `patient.csv.gz` / `patient`: join key `patientunitstayid`; hospitalization/person keys `patienthealthsystemstayid`, `uniquepid`; `hospitalid`, `wardid`, `age`, `gender`, `ethnicity`, `apacheadmissiondx`, height/weight, `hospitaladmitoffset`, admission sources, `unitvisitnumber`, unit type, and unit/hospital discharge offsets, locations, and statuses.
- `respiratoryCare.csv.gz` / `respiratoryCare`: `patientunitstayid`, `respcarestatusoffset`, `currenthistoryseqnum`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`. Zero offsets are treated as sentinels unless row logic establishes otherwise.
- `respiratoryCharting.csv.gz` / `respiratoryCharting`: `patientunitstayid`, clinical time `respchartoffset`, entry time `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`. Freeze FiO2, PEEP, ventilator rate, tidal volume, pressures, respiratory rate, O2 device, ETT placement, and RT Vent On/Off dictionaries.
- `treatment.csv.gz` / `treatment`: `patientunitstayid`, `treatmentoffset`, `treatmentstring`, `activeupondischarge`; use ventilation, weaning, reintubation, and tracheostomy strings as source indicators.
- `note.csv.gz` / `note` (ordinary gzip CSV; [source checksum]): `noteid`, join key `patientunitstayid`, clinical event time `noteoffset`, entry time `noteenteredoffset`, `notetype`, `notepath`, `notevalue`, and `notetext`. Restrict the prespecified procedure-note channel to exact `notetype` values Extubation and Intubation; normalize but retain `notepath`/`notevalue`/`notetext`. Group repeated path/value rows into one event by `patientunitstayid`, `notetype`, and `noteoffset`, retaining contributing `noteid` values. Convert both clocks to hospital-relative minutes as `noteoffset-hospitaladmitoffset` and `noteenteredoffset-hospitaladmitoffset`; retain entry delay `noteenteredoffset-noteoffset` as an observation-process feature. Use these events only for corroboration, source strata, trigger-suppressed review, A=0 sentinel strata, and the M1 note emission.
- `apacheApsVar.csv.gz` / `apacheApsVar`: `patientunitstayid`, `intubated`, `vent`, GCS, urine, vital/laboratory severity fields and `fio2`.
- `apachePatientResult.csv.gz` / `apachePatientResult`: `patientunitstayid`, `apacheversion`, `acutephysiologyscore`, `apachescore`, predicted mortality/LOS, `actualventdays`, `unabridgedactualventdays`. Freeze one IVa row; actual ventilation duration is audit-only.
- `apachePredVar.csv.gz` / `apachePredVar`: `patientunitstayid`, `ventday1`, `oobventday1`, `oobintubday1`, comorbidities, `electivesurgery`, `admitdiagnosis`, day-one GCS and PaO2/FiO2.
- `vitalPeriodic.csv.gz` / `vitalPeriodic`: `patientunitstayid`, `observationoffset`, temperature, `sao2`, heart rate, respiration, `etco2`, and systemic pressures.
- `lab.csv.gz` / `lab`: `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labname`, numeric/text result, unit fields; freeze plausible units for pH, PaO2, PCO2, bicarbonate, lactate, creatinine, WBC, platelets, bilirubin, albumin.
- `infusionDrug.csv.gz` / `infusionDrug`: `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `patientweight`; map pre-L sedatives, opioids, and pressors with unknown-unit flags.
- `carePlanEOL.csv.gz` / `carePlanEOL`: `patientunitstayid`, `cpleoldiscussionoffset`, `cpleolsaveoffset`, `activeupondischarge`.
- `hospital.csv.gz` / `hospital`: `hospitalid`, bed-size category, teaching status, region.

Every clinical table, including `note`, joins to `patient` on `patientunitstayid`; `hospital` joins on `hospitalid`. The computational analysis does have structured Extubation/Intubation procedure-note evidence, including path/value/text fields and event/entry clocks. It does **not** have a universal external procedure log, bedside source chart, ventilator waveforms, SBT performance, cuff-leak results, complete readiness judgments, sedation targets, staffing, mobility, or independently verified extubation timestamps. Because note recording is severely site-concentrated, its presence can corroborate but its absence cannot refute an event. “True liberation” therefore remains what ICU clinicians can establish or conservatively bound from all available structured evidence.

## Results and claims contract

- **Measurement supportive / GO:** all seven gate conditions pass. This supports hospital comparability of the structured sustained-liberation endpoint within the audited cohort; it does not support recovery heterogeneity.
- **Measurement adverse / NO-GO:** a precise source-related sensitivity/PPV difference, trigger dependence, or ascertainment-only bias exceeds a gate. Conclude that source-dependent ascertainment can explain a clinically material hospital contrast; do not fit or report recovery effects.
- **Measurement inconclusive:** uncertainty, indeterminacy, reviewer disagreement, sparse support, or model conflict crosses both acceptable and unacceptable regions. Defer the recovery question.
- **Recovery supportive:** after GO, both B and admissible L show calibrated, raw and adjudication-corrected P90–P10 contrasts >=10 points with lower 95% bounds >5; fold/sensitivity ordering Spearman >=0.70; source/timing sensitivities preserve direction; and lower S is not exchanged for lower D/X/R/T. This supports persistent adjusted hospital-context heterogeneity in sustained liberation.
- **Recovery adverse:** after GO, either admissible model has contrast <5 points or interval including zero, ordering is unstable, correction removes/reverses the contrast, or competing-event tradeoffs explain it. This argues against stable recovery heterogeneity in these data.
- **Recovery inconclusive:** intervals span both <5 and >=10 points, models disagree without a diagnostic resolution, or calibration/leakage fails.

No outcome identifies weaning, sedation, staffing, mobility, referral, or goals-of-care as a mechanism. Causal practice claims need reliable time-varying treatment/readiness measurements, expert causal review, positivity and an external prospective or quasi-experimental study. Public ranking or feedback requires site verification, fairness review, contemporary external validation, and governance.

## Required outputs, compute, and alternatives retained

Required outputs are `cohort_flow.json`, `phenotype_spec.json`, `note_event_audit.json`, `review_sampling_frame.parquet`, `review_inclusion_probabilities.csv`, `reviewer_labels.csv`, `review_agreement.json`, `M0_confusion_by_hospital.csv`, `M0_bounds.json`, `M1_manifest.json`, `M1_oof_predictions.parquet`, `source_emissions_by_hospital.csv`, `ascertainment_bias_draws.parquet`, `measurement_gate.json`; and only after GO, the parent’s transition, model, standardized-risk, bootstrap, sensitivity, ablation, and claim-mapping outputs. The verifier can check note schemas, event grouping, clock conversion, sampling weights, bounds, folds, state logic, arithmetic, thresholds, and conclusion/result consistency. It cannot establish that a note denotes the true bedside event, recover undocumented events, judge reviewer expertise, identify causal mechanisms, or certify hospital quality.

Measured feasibility work: the new seven-file source-support audit took 21.9 seconds with 4 CPUs/16 GiB. The proxy sample implies about 1,471 packets and 2,942 independent reviews; at 5–10 minutes each this is approximately 245–490 clinician-hours plus arbitration, an unverified human-resource requirement outside compute. Proposed solver compute: packet construction and M0 on 8 CPUs/32 GiB (<2 hours); M1 on 16 CPUs/64 GiB (2–6 hours, checkpointed); conditional B on 16 CPUs/64 GiB (2–4 hours); conditional L on one allocated A100-80GB, 8 CPUs/64 GiB (approximately 1–3 hours/fold). These are planning estimates within the configured 8-hour/16-CPU/8-GPU envelope except that clinical review cannot be automated or replaced by GPU compute.

Alternatives retained: (a) review of positives only is rejected because it cannot estimate sensitivity; (b) promoting Extubation notes to a gold standard or sole P trigger is rejected because 78.5% of note-bearing extubation stays come from one hospital and only four hospitals have >=20; (c) `actualventdays` substitution is rejected because it has no event time and may share documentation bias; (d) capture–recapture without adjudication is rejected because source independence is implausible; (e) M1 alone is rejected because latent-class identifiability cannot manufacture truth in source-empty hospitals; (f) a universal external procedure log or prospective bedside observation would be superior and should reopen the branch if obtainable. The direct M0 audit remains sufficient to stop the study; note evidence and M1 can increase information but cannot override failed direct bounds.

## Exactly three key references

[K1] Burns KEA, Rizvi L, Cook DJ, et al. “Ventilator Weaning and Discontinuation Practices for Critically Ill Patients.” *JAMA*. 2021;325:1173–1184. doi:10.1001/jama.2021.2384. Abstract inspected.

[K2] Pham T, Heunks L, Bellani G, et al. “Weaning from mechanical ventilation in intensive care units across 50 countries (WEAN SAFE).” *Lancet Respir Med*. 2023;11:465–476. doi:10.1016/S2213-2600(22)00449-0. Abstract inspected.

[K3] Hüser M, Lyu X, Faltys M, et al. “RMS: a ML-based system for ICU respiratory monitoring and resource planning.” *npj Digital Medicine*. 2025;8:775. doi:10.1038/s41746-025-02081-4. Full-text XML inspected.
