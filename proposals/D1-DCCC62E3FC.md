> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 21 evolution-b — respiratory-specific recording acceleration versus generic observation

Status: proposed substantive child of assessed-valid `[prior hypothesis]`. This is a computable design, not an executed analysis. No cohort count, fitted coefficient, prediction, metric, confidence interval, or hypothesis result is claimed.

## Scientific opening, importance, and unresolved claim

The parent asks whether a pre-landmark treatment/process signal and later strict `respiratoryCare` interval-start remain associated after adjustment for a six-channel recorded vital trajectory, selection, and timing audits. Its strongest remaining rival is a dynamic observation process. A deteriorating patient may receive more respiratory-specific records because clinicians react to respiratory change, but the same episode may also generate more nursing, vital, and other documentation. Shared charting intensity can therefore make respiratory rows appear informative even when they only mark generic observation.

The strongest inspected evidence supports only bounded claims. [K1] describes eICU as a multi-center archive with vital signs, care-plan documentation and treatments, while noting that only a fraction of bedside monitoring streams is archived. It does not validate any row as a bedside action or physiologic onset. [K3] shows that missingness masks and observation intervals can predict outcomes; it does not establish a biological mechanism. [K2] supports temporally structured EHR inputs and held-out-center prediction; it does not identify treatment provenance or physiology.

The unresolved claim is whether a respiratory-specific *lead-lag acceleration* remains associated with the parent endpoint after a prespecified generic observation process from vital and nursing tables is included, and whether it is selective for the respiratory endpoint rather than a generic nursing-documentation endpoint. The leading explanation is a reproducible recorded operational respiratory signal beyond measured generic observation. The strongest rival is shared observation/documentation. A third rival is backfill/timing: rows are entered at or after the endpoint.

This distinction changes the next clinical decision. A source-specific prospective pattern merits order/device/bedside adjudication. A generic-only pattern argues for workflow calibration and against calling chart density a respiratory deterioration marker. This is a bounded, noncausal recorded-association study, not a treatment-effect or alert study.

## Falsifiable hypothesis and estimands

Primary hypothesis H1:

> In the parent adult first-ICU population reaching minute 360, a prespecified respiratory-specific process block built from respiratoryCare, respiratoryCharting and treatment recording changes retains an incremental association with the first strict documented respiratoryCare interval-start in (360,720], after the parent vital trajectory, generic nursing/vital observation features, six-hour continuation weighting, and hospital-held-out evaluation. The respiratory-specific contrast is larger for the respiratory endpoint than for a generic nursing-charting endpoint, and is not reproduced by schedule-preserving source swaps.

H0 predicts attenuation to near zero after generic process and `W6`, similar respiratory and nursing contrasts, concentration in dense/source-complete/EOL strata, or persistence under source swaps. The timing rival predicts that the apparent signal is confined to rows after minute 360, after the endpoint, exact ties, or respiratoryCharting entry offsets after clinical offsets.

The primary estimand is the held-out-hospital incremental recorded association for `R_start_doc`, comparing a transparent model with parent state + generic process against the same model plus respiratory process. Report unweighted S6 and selection-standardized S6 results using `W6`; neither is causal. The secondary estimand repeats the contrast for `N_start_doc`, the first occupied 30-minute bin after 360 containing a valid `nurseCharting`, `nurseAssessment`, or `nurseCare` row before ICU exit. This is a workflow negative control, not a clinical outcome.

The all-eligible estimand remains the parent’s six-hour continuation/observation audit among all adult first-ICU stays, with early alive and expired ICU discharge retained as observed competing selection states. It does not impute a post-discharge respiratory event. The S6 endpoint association is standardized only to the measured pre-landmark all-eligible distribution under positivity.

## Population, boundaries, and outcomes

Time zero is ICU admission and offsets are ICU-relative minutes.

- Read `patient.csv.gz`; require finite `patientunitstayid`, `hospitalid`, `unitdischargeoffset`, and `unitdischargestatus`; `unitvisitnumber=1`, `unitstaytype=admit`, age >=18. Preserve the source’s `age>89` category. Within each `uniquepid`, retain the smallest finite `unitadmitoffset`, breaking ties by `patientunitstayid`. Use `uniquepid` only for this deduplication; never join it.
- Report all adults after deduplication and the parent four minute-360 states: (A) a valid respiratoryCare interval covers 360; (B) respiratoryCare rows exist but no auditable active invasive interval covers 360; (C) no respiratoryCare row is available in [0,360]; (D) unknown/contradictory state. Primary explanatory strata are B/C; A is secondary; unresolved D is audited then excluded.
- For every adult, retain an all-eligible prefix through `u_i=min(360,max(0,unitdischargeoffset))`, exact exit offset and alive/expired status. Do not manufacture a death time.
- Preserve `R_start_doc`: first strict documented respiratoryCare interval-start in (360,720] before the earlier of 720 and `unitdischargeoffset`; finite `ventstartoffset`; finite `ventendoffset` only if strictly greater than start, or explicitly open; no valid interval covering the preceding minute. Retain all `respcareid`, malformed, duplicate, contradictory, same-offset, post-discharge and ambiguous rows for audit. `R_stop_doc` is secondary only.
- In 30-minute bins after 360, model first valid R_start_doc, ICU exit before it (retaining unitdischargestatus), and administrative end at 720 as mutually exclusive. No post-exit event is assigned.
- Define `N_start_doc` as the first post-360 occupied 30-minute bin with any valid row from nurseCharting, nurseAssessment or nurseCare before exit. It is explicitly a documentation opportunity endpoint. A first vital-occupied bin is a secondary opportunity sensitivity.
- Predictors are outcome-blind and use inclusive [0,360] only. No post-360 row enters predictors or W6. Repeat with [0,330] plus a 30-minute gap before the endpoint window.

## Exact eICU bindings and schema verification

The guide is `datasets/eicu/README.md`; the complete catalog is `[internal dataset path]`, [source checksum]. Snapshot: `[source checksum]`. Every source is a read-only gzip ordinary file with an ordinary-file member; there is no inner archive. Fail closed if catalog, source, schema, or raw-header hashes differ.

All joins use `patientunitstayid`, except `patient.hospitalid=hospital.hospitalid`. No other identifier is joined.

| Source | Required columns/time fields | SHA-256; inspected schema JSON |
|---|---|---|
| `patient.csv.gz` | `patientunitstayid,uniquepid,hospitalid,age,unitadmitoffset,unitvisitnumber,unitstaytype,unitdischargeoffset,unitdischargestatus` | `[source checksum]`; `datasets/eicu/table-ab037c09d7df9a3c.json` |
| `vitalPeriodic.csv.gz` | `patientunitstayid,observationoffset`; `temperature,sao2,heartrate,respiration,systemicmean`; row ID | `[source checksum]`; `table-a22c6d6981a32279.json` |
| `vitalAperiodic.csv.gz` | `patientunitstayid,observationoffset,noninvasivemean`; row ID | `[source checksum]`; `table-72ace5b89971196b.json` |
| `respiratoryCare.csv.gz` | `patientunitstayid,respcareid,respcarestatusoffset,ventstartoffset,ventendoffset,priorventstartoffset,priorventendoffset`; airway audit fields | `[source checksum]`; `table-75bd08623beb504f.json` |
| `respiratoryCharting.csv.gz` | `patientunitstayid,respchartid,respchartoffset,respchartentryoffset,respcharttypecat,respchartvaluelabel,respchartvalue` | `[source checksum]`; `table-339bf06c7eef27e0.json` |
| `treatment.csv.gz` | `patientunitstayid,treatmentid,treatmentoffset,treatmentstring,activeupondischarge` | `[source checksum]`; `table-5461361964176606.json` |
| `nurseCharting.csv.gz` | `patientunitstayid,nursingchartid,nursingchartoffset,nursingchartentryoffset,nursingchartcelltypecat,nursingchartcelltypevallabel,nursingchartcelltypevalname,nursingchartvalue` | `[source checksum]`; `table-767106f2b4c8cb91.json` |
| `nurseAssessment.csv.gz` | `patientunitstayid,nurseassessid,nurseassessoffset,nurseassessentryoffset,cellattributepath,celllabel,cellattribute,cellattributevalue` | `[source checksum]`; `table-a782000603e9e364.json` |
| `nurseCare.csv.gz` | `patientunitstayid,nursecareid,celllabel,nursecareoffset,nursecareentryoffset,cellattributepath,cellattribute,cellattributevalue` | `[source checksum]`; `table-58a7011a0975a52f.json` |
| `carePlanEOL.csv.gz` | `patientunitstayid,cpleolid,cpleolsaveoffset,cpleoldiscussionoffset,activeupondischarge` | `[source checksum]`; `table-4a60395475cf75e7.json` |
| `hospital.csv.gz` | `hospitalid,numbedscategory,teachingstatus,region`; patient-only join | `[source checksum]`; `table-811df7b2ef435e12.json` |
| `lab.csv.gz` | inherited finite/revised rules: `patientunitstayid,labresultoffset,labresultrevisedoffset,labname,labresult,labmeasurenamesystem,labmeasurenameinterface` in [0,360] | `[source checksum]`; `table-79bdb33275339b1a.json` |

The exact source directory is `[internal dataset path]`. The readiness audit must verify all paths, headers, hashes, finite-offset rules and row/ID integrity. The inspected metadata states that offsets are minutes from ICU admission, vitalPeriodic is a five-minute summary rather than raw waveform, public narrative notes are removed, and raw waveforms are unavailable. `treatment` has no entry timestamp; no source establishes treatment order, administration, dose, delivery, indication, device state or bedside time.

## Variables and process decomposition

Retain the parent six-channel trajectory: finite vitalPeriodic temperature, sao2, heartrate, respiration and systemicmean plus vitalAperiodic noninvasivemean on 12 30-minute bins in [0,360], with within-bin medians, counts, masks, early/late summaries, change and last-observation timing. These are recorded values, not adjudicated physiology.

For each 30-minute bin k in [0,360], construct raw counts, occupied-bin flags, last offsets, gaps and source completeness:

- Vp: vitalPeriodic count, finite payload-channel count, occupied flag.
- Va: vitalAperiodic count and occupied flag.
- Rc: respiratoryCare rows, interval-status/open/contradictory flags.
- Rch: respiratoryCharting rows, occupied flag, distinct `respcharttypecat`; clinical-to-entry lag if both offsets finite.
- T: parent treatment count/occupancy, respiratory/non-respiratory vocabulary blocks and duplicate/string-offset flags.
- Nc, Na, Nca: nurseCharting, nurseAssessment and nurseCare count, occupied flag, distinct structural label/category count and last offset. Do not use nursing free-text content.

Define generic observation G from Vp, Va, Nc, Na and Nca only. Define respiratory process R from Rc, Rch and T only. This is a source partition, not a claim that either is a clinical action. Derive frozen early totals [0,180], late totals [300,360], late-minus-early rate, last-30 versus first-30 presence, recency, and bins where R follows G in the previous 30 minutes. Residualize each R feature within the training fold against G, 30-minute bin, training hospitals, starting state, EOL-prefix flags and parent trajectory; retain residual and missingness flag. This is descriptive orthogonalization, not causal adjustment.

The prespecified nested transparent contrasts are:

A: baseline + parent state + generic G + EOL/selection audit;
B: A + raw respiratory R;
C: A + residual R + lead-lag/synchrony terms;
D: A + total all-source count/occupied bins with source labels removed.

Report B-A and C-A as respiratory-process contrasts, D-A as generic documentation, and C-B as separation gained by source-specific residual process. No feature may use endpoint labels or any post-360/post-start row.

## Selection and weighting

Use the all-eligible prefix cohort to model remaining through minute 360 in 30-minute bins. At each t <=330 use only baseline patient/hospital fields, observed discharge opportunity, EOL offsets <=t, Vp/Va/Rc/Rch/T/Nc/Na/Nca counts/occupied bins/last offsets <=t, interval integrity known by t, and inherited lab availability <=t. Fit hospital-held-out stabilized denominator/numerator models, prespecify 0.05–0.95 probability truncation, multiply to W6, and report unclipped/clipped quantiles, maximum, positivity, hospital influence and ESS. If positivity or ESS fails, the weighted estimand is inconclusive. The parent unweighted S6 analysis remains primary, with W6 as selection sensitivity.

Report early exit by alive/expired status, hospital and starting state. Stratify by generic-density quartile, source-complete status, early EOL activity, and exit status only as selection audits. Do not condition on post-360 rows for weights or predictors.

## Matched analysis and compute plan

The transparent baseline is a cause-specific discrete-time elastic-net hazard for R_start_doc, ICU exit and administrative follow-up, and the same model for N_start_doc. Standardize/impute within training fold; choose penalty/mixing by training-fold likelihood with a one-standard-error rule. Report signed grouped contrasts, calibration, Brier score, cumulative incidence at 720, and incremental held-out deviance/log likelihood; AUROC/PR-AUC are secondary.

The matched learned alternative is a small two-layer temporal convolution over the same 12-bin state/mask/process channels plus the same scalar audit features and three cause-specific hazard heads. Fix channel order, parameter budget, optimizer, early stopping, target, W6 handling and missingness before held-out evaluation. It is scientifically useful because flattening/additivity can lose short respiratory-after-vital sequences, cross-source synchrony and nonlinear density thresholds. A predictive gain without a stable process contrast is not supportive.

Group all stays from each hospital into one fold; require at least five viable held-out hospitals. Use the same folds, target, weights, uncertainty and missingness for both alternatives. Report per-hospital, starting-state, density, source-complete, EOL and early-exit estimates; pooled cluster-weighted summaries secondarily; calibration-in-the-large/slope, Brier, cumulative incidence, incremental deviance/log likelihood and secondary discrimination. Use 2,000 hospital-cluster bootstrap replicates or a predeclared equivalent if unstable. Report intervals for B-A, C-A, C-B and respiratory-versus-nursing contrast.

The future solver envelope recorded by the parent is <=16 CPUs, 262144 MiB RAM, <=28,800 seconds, up to eight GPUs. Discovery limits are 2 concurrent jobs, 2 GPU slots and 9,000 science seconds. Gzip scans, joins, binning, sparse elastic-net and bootstrap are CPU-first. A single explicitly allocated GPU is optional only if profiling shows a temporal-model bottleneck; inside the allocation use `cuda:0`. The 4–8 hour full-audit estimate is unmeasured. No model was fitted in discovery.

## Falsification and interpretation

Freeze a manifest before fitting with all source/catalog/schema/header hashes, flows, vocabularies, bins, residualization, endpoints, weights, folds, nulls and output names.

1. **Generic attenuation:** compare A/B/C unweighted and W6-weighted. Disappearance of C-A with a remaining G contrast supports generic observation.
2. **Negative-control selectivity:** repeat A-D for N_start_doc. Similar respiratory and nursing contrasts support workflow; H1 requires respiratory selectivity.
3. **Lead-lag/timing:** require support using rows ending <=360 and persistence with [0,330]+gap. Concentration in (360,R_start_doc], post-start, exact ties, or respiratoryCharting entry offsets after clinical offsets is adverse timing evidence.
4. **Source-swap null:** within hospital × starting-state × generic-density strata, permute whole respiratory process trajectories between stays while preserving generic process and trajectory; refit with a frozen seed. Unchanged contrast is not source-specific.
5. **Schedule nulls:** cyclically shift respiratory offsets within stay and permute nursing/vital trajectories within hospital × time-bin × starting-state while preserving counts and masks. These are measurement nulls, not independence proofs.
6. **Trajectory null:** permute vital trajectories within hospital × starting state while preserving masks, counts and density; report whether model reliance is process-only.
7. **Endpoint controls:** repeat for R_stop_doc, first respiratoryCharting row after 360, and the inherited frequency-matched non-respiratory treatment control.
8. **Transport/weights:** no pooled support if one hospital/stratum dominates. Fewer than five viable hospitals, low ESS, positivity failure, unstable residualization or broad intervals means inconclusive.
9. **Landmark audit:** show all-eligible continuation/exit flow beside S6. A material W6 change or early-exit concentration supports selection; do not extrapolate events to early exits.

Supportive results require a pre-landmark C-A contrast with stable direction in both models, valid W6 positivity/ESS, stronger respiratory than nursing selectivity, no dense/EOL/early-exit concentration, no source-swap explanation, and at least five held-out hospitals. This establishes a reproducible recorded association compatible with a respiratory-specific operational process beyond measured generic observation; it does not establish physiologic deterioration, treatment delivery or causality.

Adverse results are W6 attenuation, nursing-endpoint replication, source-swap persistence, post-landmark/post-start or entry-lag concentration, generic/control replication, schedule-null failure or hospital non-transport. These favor selection, source availability, shared documentation or backfill. Inconclusive results do not refute clinical deterioration; they identify missing timing or adjudication evidence.

## Alternatives, deliverable, and limits

Elastic-net is retained because the scientific target is an auditable incremental provenance contrast with grouped coefficients and nested deviance. The matched temporal convolution is retained because it can reveal cross-source timing and nonlinear synchrony that an additive baseline loses. A raw event transformer is deferred because treatment lacks an entry timestamp and the question needs source attribution and falsification, not maximal prediction. Causal treatment-effect and mechanistic ventilator models are deferred because assignment, indication, administration, device state, FiO2, waveforms and bedside time are unavailable. Revisit only with richer provenance or expert adjudication; no method is excluded merely for neural/GPU use.

Completion requires: verified manifest and adult/all-eligible/S6 flow; 12-bin state/process table; W6/ESS/positivity report; A-D transparent estimates for R_start_doc and N_start_doc; matched temporal-model estimates; hospital/stratum uncertainty; all timing/source/schedule/trajectory/boundary nulls; and a claim-to-output table. Computationally checkable claims are source counts, ICU-relative timing, endpoint integrity, continuation weights under stated assumptions, held-out associations and falsification outputs. Treatment order/administration, dose/delivery, device state, raw waveform physiology, bedside time, true onset, death time, mechanism and causality require clinical adjudication and another study.

## Key reference claim discussion

[K1] Pollard et al. support the eICU monitoring/documentation provenance boundary and multi-center design. This child adds generic nursing/vital observation, source-specific residual process, all-eligible selection, and a nursing negative control; it does not borrow the paper’s published counts as this snapshot’s result.

[K2] Rajkomar et al. support matched temporally structured learned inputs and held-out-center evaluation. This child adds a provenance estimand and falsification design that predictive accuracy alone cannot provide.

[K3] Che et al. support preserving observation masks and timing gaps as potentially informative. This child tests whether respiratory-specific process survives generic observation adjustment and source/nursing nulls; it does not interpret predictive missingness as physiology.

Compact bibliography: [K1] Pollard TJ et al. (2018), DOI 10.1038/sdata.2018.178. [K2] Rajkomar A et al. (2018), DOI 10.1038/s41746-018-0029-1. [K3] Che Z et al. (2018), DOI 10.1038/s41598-018-24271-9.

The attached excerpts are small UTF-8 records of inspected source passages, not complete papers. The dataset README, full eICU README, metadata and relevant schema JSONs were inspected directly. No unavailable paper text or supplement is claimed. Source data remain read-only; all files in this branch are derived evidence/design files.
