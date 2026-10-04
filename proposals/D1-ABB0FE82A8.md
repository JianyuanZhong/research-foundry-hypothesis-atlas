> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 15 evolution alternative — temporal transition corroboration from treatment records

Status: proposed competing substantive child of `[prior hypothesis]`. Design only. No cohort count, treatment prevalence, fitted coefficient, prediction, metric, interval, or scientific result is claimed.

## Scientific opening and the unresolved claim

The parent asks whether an early state/process vector predicts a later documented `respiratoryCare` interval start after minute 360, and whether that start is accompanied by a separate `respiratoryCharting` record. That is a useful reproducibility check, but proximity to a second chart row still leaves a temporal question: does the respiratory-care boundary occur in a reproducible operational sequence with a separately timestamped treatment record, or are the two rows merely documentation density, backfill, or discharge/EOL workflow?

This branch tests that remaining uncertainty rather than adding another treatment row as a cosmetic endpoint. It distinguishes the order `respiratoryCare start -> treatment record` from `treatment record -> respiratoryCare start`, same-window co-occurrence, and isolated records. The decision-relevant output is whether a prediction made at minute 360 identifies a reproducible, temporally ordered two-stream transition with useful calibration and alert burden. The parent’s charting concordance is retained only as a secondary cross-check; it is not used to define the primary event.

The strongest evidence actually inspected supports three bounded claims. [K1] describes eICU as a multi-center, linked archive containing treatment information while warning that only part of monitored information is archived for clinical documentation. [K2] supports testing temporal EHR representations across held-out centers while recognizing semantic interoperability limits. [K3] supports explicit, reproducible structured-EHR preprocessing, but only its abstract/provider response was inspected here. None establishes that an eICU `treatmentstring` denotes an intervention, that `treatmentoffset` is administration time, or that a respiratory-care row is a clinical ventilation start.

Hypothesis:

> Among adult first-ICU S6 stays with no valid documented active `respiratoryCare` interval at minute 360, the parent’s [0,360] state/process signal will predict a later documented respiratory-care start more robustly when the start is followed, within a prespecified 120-minute interval and before ICU exit, by an independently recorded treatment-table row than when it is defined by respiratoryCare alone. The ordered increment should remain directionally coherent in held-out hospitals and in a treatment-availability-adjusted analysis, while the reverse-order, same-window, shifted-window, discharge-adjacent and EOL controls should not explain it.

The primary estimand remains a recorded-documentation transition, not ventilation, treatment delivery, deterioration, benefit, or a causal effect. A supportive result establishes temporally ordered concordance of two records. It does not establish intervention identity or bedside timing.

## Competing explanations and what would separate them

The leading operational explanation is a reproducible care-documentation sequence: a respiratoryCare interval boundary is followed by a distinct treatment record because the same operational transition is represented in two streams. Its prediction is excess `R_to_T_doc` over a respiratoryCare-only start, with a lag distribution concentrated in the pre-specified [0,120] minute window, across held-out hospitals and timing conventions.

The important rivals are:

1. Availability/ascertainment: the process vector predicts whether treatment rows are archived, not a transition. It predicts `T_anyrow`, chart opportunity and row density as strongly as `R_to_T_doc`; treatment-availability weighting or restriction to observable stays attenuates the ordered increment.

2. Backfill or timestamp order: treatment rows are entered after the fact, so `R_to_T_doc` reflects documentation lag rather than a care sequence. The reverse-order and entry-delay audits are common, the lag is unstable by hospital, or a schedule-preserving treatment-time permutation reproduces the result.

3. Discharge/EOL workflow: both rows accumulate shortly before an alive/expired ICU exit or after an end-of-life discussion. The association is concentrated in a pre-specified exit band or EOL stratum and disappears when exit-adjacent pairs or post-EOL pairs are excluded.

4. Semantic overreach: a stable treatment string is not an intervention class, or the class is hospital-specific. A blinded vocabulary audit fails stability/positivity, or the generic any-row endpoint behaves like the putative intervention class. The clinical-intervention claim is then unavailable and deferred.

5. Duplicate or interval error: a respiratoryCare start is a duplicate, conflict, or continuation of a baseline episode. Excluding conflicts and requiring a strict baseline gap materially changes the result.

6. Genuine two-stream operational corroboration: the ordered endpoint, not just any treatment row, is directionally coherent in held-out hospitals; the process increment survives availability, exit, EOL, conflict and timing nulls; and no one hospital or generic row-density endpoint dominates. This still supports only a recorded transition.

These records cannot distinguish bedside treatment initiation from clinician choice, interface behavior, backfill, feed coverage, or EOL workflow. That missing clinical meaning is a planned adjudication boundary, not an assumption.

## Population, time zero, risk set and competing exits

Preserve the parent exactly:

- Time zero is ICU admission. Require finite `patientunitstayid`, `hospitalid`, `unitdischargeoffset`, and `unitdischargestatus`; `patient.unitvisitnumber = 1`, `patient.unitstaytype = admit`, numeric age >=18, retaining source age >89.
- For qualifying stays sharing `uniquepid`, retain the smallest finite `unitadmitoffset), then smallest `patientunitstayid`. `uniquepid` is used only for this patient-stay duplicate rule; it is never joined across tables.
- S6 eligibility is `unitdischargeoffset > 360`; survival to 720 is not required.
- Predictors use only [0,360], including offset 360. Follow-up is strictly (360,720], truncated at the earlier of 720 and `unitdischargeoffset`.
- The primary risk set is the parent’s operational absence group: no valid documented active respiratoryCare interval at minute 360. A valid interval has finite `ventstartoffset` and either finite `ventendoffset > ventstartoffset` or a missing end treated as open. This is not clinical absence.

Assign the first follow-up cause under a frozen tie rule:

- `R_start_doc`: earliest strict, unambiguous valid respiratoryCare interval start;
- `RT_doc`: earliest ordered two-stream event defined below;
- alive ICU exit before the relevant event when `unitdischargestatus = Alive`;
- expired ICU exit before the relevant event when `unitdischargestatus = Expired`.

For primary `RT_doc`, a respiratoryCare start and treatment row at exactly the same offset are classified as same-time, not as evidence of the directed R-to-T order. An exit at the same offset as a candidate event is an exit. An expired discharge supplies no inferred death time. Event-free stays are event-free for this recorded-documentation estimand only. Model cause-specific pooled hazards in (360,480], (480,600], and (600,720].

## Exact eICU bindings and source provenance

The configured eICU snapshot is `[source checksum]`. The full catalog is `[internal dataset path]`, [source checksum]. All listed eICU sources are read-only ordinary gzip files; archive member is ordinary file/null, not a nested zip/tar member. The binding-template entry for each source targets the corresponding read-only source payload under `[internal dataset path]` for execution packaging; the proposal retains the original source paths and hashes below.

Only documented `patientunitstayid` joins are permitted, except `patient.hospitalid = hospital.hospitalid` for hospital audit strata. No `uniquepid` join is allowed across clinical tables.

| table | exact read-only source path | source SHA-256 | schema SHA-256; required columns and time |
|---|---|---|---|
| patient | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `patientunitstayid, uniquepid, hospitalid, age, unitvisitnumber, unitstaytype, unitadmitoffset, unitdischargeoffset, unitdischargestatus` |
| respiratoryCare | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `respcareid, patientunitstayid, respcarestatusoffset, currenthistoryseqnum, airwaytype, ventstartoffset, ventendoffset, priorventstartoffset, priorventendoffset` |
| treatment | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `treatmentid, patientunitstayid, treatmentoffset, treatmentstring, activeupondischarge` |
| respiratoryCharting | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; secondary audit: `respchartid, patientunitstayid, respchartoffset, respchartentryoffset, respcharttypecat, respchartvaluelabel, respchartvalue` |
| vitalPeriodic | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; parent finite fields at `observationoffset`: `temperature, sao2, heartrate, respiration, systemicmean` |
| vitalAperiodic | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; parent finite `noninvasivemean` and inherited fields at `observationoffset` |
| hospital | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `hospitalid, numbedscategory, teachingstatus, region` |
| carePlanEOL | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `cpleolsaveoffset, cpleoldiscussionoffset` |
| apachePatientResult | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; `actualicumortality, apachescore, predictedicumortality, apacheversion` for audit only |
| lab | `[internal dataset path]` | `[source checksum]` | `[source checksum]`; inherited manifest requires `labresultoffset, labid, labtypeid, labname, finite labresult, labmeasurenamesystem` with interface fallback, `labresultrevisedoffset`, all confined to [0,360] and revisions known by 360 |

The inherited lab manifest and channel-selection/revision rule remain frozen from the parent. If that manifest is not resolved by the solver, readiness fails; no alternate lab source may be substituted.

## Endpoint construction: timing, availability and semantics are separate

All raw rows are saved before fitting. Preserve null, empty, whitespace-only, malformed and unknown values, raw `treatmentstring`, `activeupondischarge`, all respiratory fields, duplicate offsets and source row identifiers. Normalization produces an audit view only.

### Respiratory-care start

A valid respiratory interval has finite `ventstartoffset` and either missing `ventendoffset` (open) or finite `ventendoffset > ventstartoffset`. Save invalid, reversed, nonfinite and missing-start rows. Collapse only exact duplicates on `patientunitstayid, currenthistoryseqnum, ventstartoffset, ventendoffset, airwaytype`. Same-start/sequence rows differing in end, airway, status or prior boundary are conflict-flagged; conflicting start offsets are not a primary event. A valid interval active at 360 has start <=360 and end >360 or open.

`R_start_doc` is the earliest valid, strict, unambiguous `ventstartoffset` in (360,720] and before the earlier of 720 and discharge, with no baseline interval showing the same episode active at 360. It remains a documentation boundary; `airwaytype` is not translated to invasive/noninvasive support without adjudication.

### Treatment-record transition

First produce a treatment vocabulary/availability audit without using model predictions, follow-up outcomes, or mortality:

- retain raw `treatmentstring`, null/empty/whitespace status, exact duplicates, per-stay row counts, hospital prevalence, treatment offsets, and `activeupondischarge`;
- create a generic `T_anyrow` class for any finite `treatmentoffset` in the ICU stay, explicitly labeled as treatment-record availability, not intervention;
- freeze a candidate class only if an outcome-blinded, deterministic normalization of nonempty `treatmentstring` values is present in at least five viable hospitals, has at least one positive row in each of those hospitals, and has no unresolved same-offset contradictory class assignments. Do not map strings to mechanical ventilation, oxygen, airway, escalation, or benefit by intuition;
- if no semantic class meets this gate, the primary event remains `RT_anyrow_doc` using any-row availability and the semantic intervention claim is unavailable. This is a valid negative/deferral result, not permission to invent a class;
- `activeupondischarge` is an audit field only. It cannot establish treatment time or make a row active at minute 360.

For each eligible stay, save all treatment rows with finite `treatmentoffset` in [0, unitdischargeoffset], plus out-of-stay anomalies. A treatment row after discharge cannot corroborate an event.

Define the primary ordered endpoint `RT_doc`:

1. identify the strict `R_start_doc` time t;
2. require the first qualifying treatment row of the frozen class (or any-row fallback) at time u satisfying t < u <= t+120 and u <= unitdischargeoffset;
3. require no qualifying row of the same class in [0,360] that would make this a continuation of an already documented treatment stream; if such a baseline row exists, retain the stay in the audit but withhold it from the primary transition risk set;
4. store t, u, lag u-t, class status, raw treatment fields, source row IDs, duplicate/conflict flags, baseline treatment availability and exit relation.

Same-time rows are `RT_same_time_doc`, not directed transitions. A qualifying treatment row before R in [t-60,t) is `T_before_R_doc`, and a row in [t+120,t+240] is a shifted-window control. The mutually exclusive per-stay sequence labels are `R_to_T`, `T_before_R`, `same_time`, `R_only`, `T_only`, `neither`, `exit_before_transition`, and `ambiguous`. These labels are descriptive record sequences, not clinical courses.

The parent’s respiratoryCharting `C_start_doc` is a secondary concordance audit, using its frozen outcome-blind chart-class rule if available, and `C_entry_doc` remains a documentation-lag audit. It never supplies a treatment label and never enters X/T/P, weights, fold assignment or model-selection decisions.

### Availability and exits

Baseline strata are retained: documented support, documented no-active-vent only when a stable explicit non-support category exists, no respiratory record, and R0_unknown. Add baseline and follow-up treatment availability flags, chart availability flags, and treatment row counts as audit/observation variables only.

Report three estimands for `RT_doc`: all eligible stays with missing treatment treated as no ordered corroboration; treatment-observable stays with a qualifying opportunity; and a stabilized inverse-availability-weighted analysis. The availability model is fit inside each training fold using only [0,360] X/T/P, hospital training data, baseline respiratory stratum and baseline availability. Truncate weights at prespecified 1st/99th percentiles learned in training data; save positivity and effective sample size. Future treatment rows, event times, EOL-followup values and outcomes never enter the observation model.

Use `carePlanEOL` only for audit: any finite `cpleolsaveoffset` or `cpleoldiscussionoffset` in [0,360] is EOL_0_360, with save and discussion separated; events in follow-up are EOL_followup and do not define death. Retain EOL_0_360 in the primary analysis, report strata, restrict to EOL_0_360=0 as a sensitivity, and separately exclude transition pairs after the first EOL_followup offset. Report alive/expired exits as competing causes; do not infer death time.

## Predictors, model comparison, split and uncertainty

Preserve the parent’s exact finite vital state vector X, state vector T, process vector P, inherited lab revision rule, P12/S720/S6 mortality module, five contiguous hospital-held-out folds, fixed 20% patient-hash internal reference, preprocessing and observation-weight rules. No respiratoryCare, treatment, respiratoryCharting, EOL, post-360 discharge or outcome field enters predictors.

Fit the same outcomes for both alternatives: `R_start_doc`, primary `RT_doc` (or `RT_anyrow_doc` if semantic class is unavailable), `T_before_R_doc`, `RT_same_time_doc`, the parent’s recorded-start comparator, and alive/expired exits. The primary contrast is the paired held-out-hospital process increment Q_P^T for ordered `RT_doc` versus `R_start_doc`, plus the generic `T_anyrow` availability endpoint. Use the same three discrete follow-up intervals.

Simple baseline: elastic-net pooled discrete-time cause-specific logistic hazards. Alpha/lambda selection, imputation, scaling, channel selection, class handling and availability weights are fit within training hospitals only. It is the primary interpretable additive comparator.

Scientifically informative alternative: a discrete-time semi-Markov multi-state model with states `NoActiveR`, `R_only`, `T_before_R`, `RT_same_time`, `RT_ordered`, alive exit and expired exit. It uses the same X/T/P, target horizon, hospital folds, patient-hash reference, preprocessing, availability option, seeds, and paired hospital-cluster bootstrap. Its transition hazards include prespecified interactions between process features and current record state, and a fixed 120-minute R-to-T lag gate. The primary reported target is still the cumulative incidence of `RT_ordered` by 720 minutes, so model comparison is not a change in estimand. The multi-state representation is scientifically informative because it can reveal whether P is associated specifically with entry into an ordered sequence, with treatment-before-R/backfill states, or only with generic record availability; an additive model collapses those paths. It does not make the states clinical mechanisms.

A raw neural sequence model is deferred: treatment has one offset and an unverified free-text vocabulary, and the question is sequence ordering rather than maximal representation learning. Revisit it only if the blinded audit shows enough stable, temporally dense treatment classes and the fixed X/T/P summaries demonstrably lose relevant timing. A causal treatment-effect model is not justified because indication, intervention provenance, bedside time, exchangeability and outcomes under alternative treatment are unavailable.

Required outputs are: frozen cohort and competing-exit manifest; raw respiratoryCare, treatment and secondary respiratoryCharting audits; blinded treatment-class freeze record; per-stay sequence/lag/availability table; prevalence, positivity and effective sample size by hospital, stratum and exit band; fold-isolated predictions from both models; cumulative-incidence Brier score, time-dependent AUC, calibration-in-the-large and slope, observed/predicted incidence, alert burden and net benefit at 5%, 10% and 20% thresholds; Q_P^T process increments; state-specific transition estimates; unweighted and weighted analyses; paired 2,000 hospital-cluster bootstrap intervals; and a conclusion table linking each claim to output rows. Use inherited negligible margins of 0.01 AUC and 0.005 net benefit where defined, but do not treat a predictive margin as clinical benefit.

## Falsification and interpretation rules

Pre-specify and save:

- treatment schedule null: within hospital, baseline respiratory stratum, treatment-availability bin, exit-time band and row-density bin, permute treatment times while preserving treatment counts, class labels, censoring and hospital;
- order null: compare observed R-to-T and T-before-R sequence incidence with a schedule-preserving null; a result reproduced by reverse order weakens directed timing;
- shifted windows: compare [t+60,t+180] and [t+120,t+240] with the primary (t,t+120] gate, frozen before fitting;
- same-time/lag audit: report exact ties, lag quantiles and hospital-specific lag; a large or unstable lag is documentation timing, not intervention timing;
- availability null: test P against T_anyrow, chart opportunity, treatment opportunity and row density; if those dominate while RT_doc does not survive observability adjustment, classify as ascertainment;
- discharge/EOL nulls: exit-adjacent exclusion, exit-band results, EOL strata and post-EOL exclusion; no post-exit row is admissible;
- baseline and conflict nulls: high-confidence respiratory baseline only versus R0_unknown; exclude all interval and treatment duplicate/conflict/ambiguous records, then report flagged inclusions;
- chart cross-check: compare ordered treatment transition with parent C_start_doc/C_entry_doc without allowing chart fields into predictors or treatment classes;
- source independence: audit that treatment and respiratory fields, event times, availability flags, EOL fields and post-landmark rows do not enter X/T/P, folds, weights or model choices.

Supportive results require a frozen class or explicitly labeled generic endpoint; at least five viable hospitals with positive ordered-event and availability support; both models show coherent held-out-hospital Q_P^T for RT versus R; the direction persists in the treatment-observable and weighted analyses; lag and sequence are not explained by schedule, reverse-order, shifted-window, discharge, EOL, conflict or one-hospital nulls; and utility/calibration do not deteriorate in exchange for a small discrimination gain. This supports a reproducible ordered record transition and identifies whether the process signal is sequence-specific.

Adverse results include a strict R signal with no ordered treatment corroboration, strong treatment availability but weak RT signal, reverse-order equivalence, concentration near exit/EOL, large timing instability, one-hospital dependence, or a multi-state advantage only without calibration/utility or null robustness. If R persists but RT is null, retain the parent’s single-stream documented-start claim only. If RT_anyrow is positive but no blinded semantic class is available, retain only generic cross-stream documentation concordance. A learner or multi-state model that improves AUC without sequence-specific, calibrated or utility-relevant evidence is not a scientific advance.

Inconclusive/deferral includes fewer than five viable hospitals, poor positivity/effective sample size, no stable treatment class, too few strict starts, unresolved conflicts, intervals spanning meaningful and negligible margins, or source timing that cannot be bounded. An imprecise null is not refutation. A clinical intervention claim requires a blinded respiratory/critical-care adjudication of treatment strings and interval meaning, source/interface documentation or bedside order/administered-time evidence, and an external or prospective study. No result here establishes ventilation, deterioration, treatment efficacy, causality or a bedside action.

## Actual scientific deliverable, alternatives and compute

The actual deliverable is newly fitted, leakage-safe evidence: a row-level treatment/respiratory audit; a blinded semantic-class availability decision; mutually exclusive ordered/reverse/same-time sequence endpoints; timing, availability, EOL, discharge and schedule-null outputs; elastic-net and semi-Markov fold-isolated predictions on the same primary target; calibration/utility and hospital-cluster uncertainty; and a conclusion report mapping every claim to computed output rows. Readiness or a source audit alone is not study completion.

The simple elastic-net model is retained as the minimum interpretable baseline and is expected to be CPU-capable. The semi-Markov alternative is deferred only if its state counts or transition positivity fail the pre-specified audit; that is a scientific feasibility result, not a license to replace it with a more convenient endpoint. The future solver envelope inherited from the parent is up to 16 CPUs, 262144 MiB RAM, up to 8 GPUs and 28800 seconds; this extraction-, audit-, tabular-fit-, multi-state- and bootstrap-heavy design is provisionally CPU-capable and no GPU is required. Any GPU decision must follow the shared hardware rule: ordinary shell CUDA absence is not evidence of hardware absence; an allocated job would request `gpus=1` and use `cuda:0`. Discovery in this branch did not fit the proposed study.

The alternative not chosen is a raw sequence neural model over treatment strings and respiratory rows. It could reveal nonlinear timing and vocabulary interactions, but the configured treatment table has one offset, no entry-time field, and unverified string semantics. Evidence that would justify revisiting it is a blinded audit showing stable treatment classes across at least five hospitals, adequate event support, and measurable information loss when ordered records are reduced to X/T/P and the fixed state-machine representation. A causal intervention model is also not chosen; revisiting it requires treatment provenance, indication, reliable clinical time, exchangeability and a clinically adjudicated outcome.

The verifier can check source/schema hashes, read-only ordinary-file bindings, patientunitstayid/hospital joins, cohort and time boundaries, interval validity, treatment class freeze record, ordering/ties/lag logic, no post-exit leakage, competing exits, availability weights, folds, nulls, uncertainty and conclusion-to-output links. It cannot decide whether a treatment string means an intervention, whether an offset is bedside time, whether a respiratory boundary is ventilation, whether EOL documentation caused the transition, or whether care should change. Those claims require the missing evidence and expert review described above.

## Three key references

- [K1] Pollard et al. (2018), *The eICU Collaborative Research Database, a freely available multi-center database for critical care research*. Full-text passages were inspected. It bounds linkage, treatment-information availability and archive coverage; it does not validate treatment semantics or timing.
- [K2] Rajkomar et al. (2018), *Scalable and accurate deep learning with electronic health records*. Full-text passages were inspected. It motivates temporal, held-out-site comparisons and bounds semantic harmonization; it does not validate this endpoint.
- [K3] Tang et al. (2020), *Democratizing EHR analyses with FIDDLE: a flexible data-driven preprocessing pipeline for structured clinical data*. Only an Europe PMC abstract/provider response was inspected. It supports reproducible preprocessing; it does not establish treatment meaning or intervention timing.

Compact bibliography:

1. Pollard TJ, Johnson AEW, Raffa JD, et al. Scientific Data. 2018. DOI: 10.1038/sdata.2018.178.
2. Rajkomar A, Oren E, Chen K, et al. npj Digital Medicine. 2018. DOI: 10.1038/s41746-018-0029-1.
3. Tang S, Davarmanesh P, Song Y, Koutra D, Sjoding MW, Wiens J. Journal of the American Medical Informatics Association. 2020;27:1921–1934. DOI: 10.1093/jamia/ocaa139.

Receipt-linked UTF-8 excerpts and `key-references.json` are adjacent to this proposal. The K3 attachment is explicitly abstract-only/provider-response evidence.
