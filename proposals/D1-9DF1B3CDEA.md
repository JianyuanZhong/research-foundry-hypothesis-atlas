# Decision-relevant partial identification of recovery-pattern signal after first ICU discharge

## Scientific deliverable

The solver must newly fit a leakage-safe MIMIC-IV 3.1 first-ICU-discharge study with one explicit deliverable:

> Determine whether the recorded support/recovery pattern contains reproducible, held-out prognostic information about early post-discharge escalation beyond pre-landmark discharge-process and observation-intensity information, and whether that information can support a prespecified risk-review threshold when the clinically relevant transition is only partially identified.

The threshold is a prognostic classification device, not a discharge, treatment, or monitoring-policy recommendation. A completed study must produce, with hashes and provenance:

1. `run_manifest.json`: catalog/source hashes, archive members, schema hashes, item-label checks, locked rules, split seeds, software and resource use, and output hashes.
2. `cohort_audit.parquet`: one row per subject's earliest valid ICU stay, joins, exclusions, temporal checks, complete-window and coverage flags, and broad versus primary-analysis indicators.
3. `hourly_features.parquet`: twelve one-hour `[outtime-12h,outtime)` bins containing physiology, recorded support, source-specific masks, contradictions, and pre-landmark process/observation features.
4. `support_observation_audit.parquet`: the respiratory and vasoactive ledger, coverage/gap measures, positive and observed-non-positive evidence, durable/recent/active/discordant labels, and every locked `q)-recoding.
5. `process_observation_audit.parquet`: the pre-landmark process and observation-intensity variables, their timestamps, missingness, strata, and feature-to-landmark leakage checks.
6. `transfer_outcome_audit.parquet`: all later ICU candidates within 48 hours, all bridge candidates, clipped intervals, careunits, eventtypes, tie flags, and lower-bound/upper-bound labels.
7. `partial_id_bounds.parquet`: 6-, 24-, and 48-hour lower and upper CIFs, widths, competing death/discharge CIFs, and worst-case contrasts for every exposure, split seed, `q), and topology rule.
8. `baseline_test_predictions.parquet` and `latent_topology_test_predictions.parquet`: locked patient-level held-out predictions for observable causes and the compatible latent-transition interval.
9. `model_comparison.parquet`, `calibration.parquet`, `bootstrap_uncertainty.parquet`, `threshold_operating_characteristics.parquet`, `q_sensitivity.parquet`, `topology_sensitivity.parquet`, and `coverage_selection_audit.parquet`.
10. `falsification_outputs.parquet` and `interpretation_map.parquet`: all negative controls and each claim linked to computed output rows, uncertainty, bound width, event support, and an evidence limitation.

Completion requires these outputs to be generated from the locked data and held-out predictions. No result is claimed in this proposal.

## Supported evidence, unresolved claim, and hypothesis

The strongest available evidence is the parent's read-only topology audit under the adult earliest-first-ICU and 12-hour eligibility rule: 52,591 eligible first ICU outtimes, 2,661 later ICU returns within 48 hours, 2,060 returns with a qualifying documented non-ICU bridge, and 601 returns without one; 294 returns had multiple bridge candidates. This establishes material endpoint/documentation ambiguity. It does not establish a support association, a discharge-process effect, or a clinical escalation.

The parent correctly defines

- (L): CIF of a later ICU return preceded by the locked documented non-ICU bridge;
- (U): CIF of any later ICU return, regardless of bridge documentation;

with (L leq T leq U) for the latent transition-compatible risk. Death before return and alive hospital discharge before return/death are competing first events. The risk-difference interval for groups (a,b) is ([L_a-U_b,;U_a-L_b]). The 601 unconfirmed returns are ambiguity mass, not a biological event class.

The unresolved claim is whether a recorded recovery pattern is informative after accounting for the process that generated its measurements and the discharge pathway, rather than merely being a proxy for charting intensity or transfer documentation.

Primary hypothesis:

> Among adults at first ICU outtime with adequate recorded-support coverage, after standardization for pre-landmark discharge-process and observation-intensity variables, a prespecified recorded support/recovery pattern yields a reproducible held-out separation in 48-hour latent transition-compatible risk whose worst-case lower contrast exceeds the prespecified 2-percentage-point absolute gate, remains positive at 6 and 24 hours, and is stable over the declared missing-support and bridge-topology grids.

The 2-percentage-point value is an analysis gate inherited from the parent, not a validated bedside threshold. The same question is tested with a process/observation-only model: if the full support/recovery pattern does not improve held-out separation or calibration beyond that model, the physiologic/support claim is not supported. A positive aggregate-return result with a null lower-bound result is specifically an endpoint-ambiguity finding, not support for the stronger claim.

A secondary, policy-neutral threshold question is:

> For prespecified absolute-risk thresholds (	au in {0.02,0.05,0.10}) at 48 hours, can the study identify high-risk, low-risk, and indeterminate patients from held-out risk intervals with useful coverage and stable operating characteristics?

For each patient, ([r_L(x),r_U(x)]) is the model-based observable lower/upper risk interval, with uncertainty retained. A high-risk flag requires the lower endpoint to exceed (	au); a low-risk flag requires the upper endpoint to be below (	au); all overlapping cases are indeterminate. Thresholds are locked before test evaluation and reported as a frontier, not selected for the best result. The study reports coverage, sensitivity, specificity, PPV and NPV separately for the observable lower endpoint and aggregate upper endpoint, along with the fraction indeterminate and interval widths. These are retrospective risk-stratification operating characteristics. They cannot show that acting on a flag improves outcomes, that discharge should be delayed, or that a threshold is clinically acceptable.

The primary hypothesis is falsified by a non-positive worst-case lower contrast, failure of the 2-point gate, reversal across plausible `q)/topology settings, no incremental separation over process/observation-only inputs, or persistence after topology-label permutation. Threshold evaluation is inconclusive when uncertainty or the partial-identification interval leaves most patients indeterminate, overlap/positivity is inadequate, or operating characteristics are unstable across seeds.

## Clinical importance and substantive advance

An early ICU return can trigger higher-acuity review, monitoring, and resource planning, but an aggregate return mixes immediate ICU-to-ICU movement, documented ward/intermediate-care intervals, missing transfer paths, and hospital death/discharge processes. A clinically useful result would therefore be evidence that the pre-discharge recorded recovery pattern adds information beyond how intensively the patient was observed and how the discharge pathway was documented.

The advance over the parent is a decision-relevance layer with a defensible null:

- the primary estimand remains the nonparametric ([L,U]) interval;
- process/observation-only versus support/recovery-augmented models explicitly test whether the apparent signal survives adjustment;
- a held-out threshold produces high/low/indeterminate classifications only when the interval supports them;
- no utility, causal effect, discharge appropriateness, treatment benefit, or preventability is inferred.

## Population, joins, and temporal boundaries

Use the read-only MIMIC-IV 3.1 ZIP:

- source: `[internal dataset path]`
- declared [source checksum]
- snapshot: `[source checksum]`
- catalog: `[internal dataset path]`
- catalog [source checksum]

Select exactly one index stay per subject: the earliest valid `icu/icustays.intime` across admissions, tie-broken by smallest `stay_id). Require `patients.anchor_age >= 18`, valid `subject_id,hadm_id), `intime < outtime < admissions.dischtime`, non-null `dischtime), no `admissions.deathtime <= outtime), and a complete 12-hour pre-landmark window beginning no earlier than `icustays.intime`. Retain MIMIC top-coded `anchor_age=91). The landmark is `icustays.outtime).

Use patient-level, never row-level, 70/15/15 train/validation/test partitions with seeds 17, 29, and 43. Fit and tune only on train/validation; lock all preprocessing, threshold rules, `q), bridge rules, and calibration before test evaluation. Predictors are only in `[outtime-12h,outtime)). Use `charttime` for clinical observations and `starttime,endtime` for intervals; never use `storetime` as clinical time. No post-`outtime` field, transfer, discharge, death, or note enters a predictor.

Follow-up is `[outtime, min(outtime+48h, admissions.dischtime))). First observable events are: documented-bridge ICU return (lower-bound marker), any later ICU return without a qualifying bridge (ambiguity mass), hospital death before return, and alive hospital discharge before return/death. Collapse the first two for the exact aggregate-return comparator. Apply death-before-return for ties within one minute and non-discharge before alive discharge for tied events; repeat 0- and 5-minute sensitivity tolerances without choosing after inspecting results.

## Exact source bindings

Every run must recheck headers and save the listed schema hashes.

- `hosp/admissions`, archive member `mimic-iv-3.1/hosp/admissions.csv.gz`, catalog file `datasets/mimic/table-e8ec3e6e4c428559.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id). Use `admittime,dischtime,deathtime,admission_type,admission_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; `discharge_location` is outcome/audit only.
- `hosp/patients`, member `mimic-iv-3.1/hosp/patients.csv.gz`, `datasets/mimic/table-9154f8c46cade9af.json`, schema hash `[source checksum]`. Join on `subject_id). Use `gender,anchor_age,anchor_year_group); never use `dod).
- `icu/icustays`, member `mimic-iv-3.1/icu/icustays.csv.gz`, `datasets/mimic/table-7d5c8feb0fb0dbd4.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id); use `stay_id,first_careunit,last_careunit,intime,outtime,los`.
- `hosp/transfers`, member `mimic-iv-3.1/hosp/transfers.csv.gz`, `datasets/mimic/table-685b6b74d0d7c547.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id). Use pre-landmark `transfer_id,eventtype,careunit,intime,outtime` for process variables and all post-landmark rows only for the bridge audit.
- `hosp/services`, member `mimic-iv-3.1/hosp/services.csv.gz`, `datasets/mimic/table-491b3c713229062a.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id); use only `transfertime,prev_service,curr_service` strictly before `outtime) as service-transition process features.
- `icu/chartevents`, member `mimic-iv-3.1/icu/chartevents.csv.gz`, `datasets/mimic/table-8208609a785ea7e8.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id,stay_id); use `charttime,itemid,value,valuenum,valueuom,warning), with item labels verified through `icu/d_items`.
- `icu/d_items`, member `mimic-iv-3.1/icu/d_items.csv.gz`, `datasets/mimic/table-d1023acc404fd1d4.json`, schema hash `[source checksum]`. Use `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue` to verify IDs and units.
- `icu/inputevents`, member `mimic-iv-3.1/icu/inputevents.csv.gz`, `datasets/mimic/table-d193e854c19eb4ba.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id,stay_id); use valid `starttime,endtime,itemid,amount,amountuom,rate,rateuom,statusdescription`, not `storetime`. Vasoactive IDs: norepinephrine 221906; epinephrine 221289/229617; dopamine 221662; phenylephrine 221749/229630/229631/229632; vasopressin 222315.
- `icu/procedureevents`, member `mimic-iv-3.1/icu/procedureevents.csv.gz`, `datasets/mimic/table-f6493e8403a0abe7.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id,stay_id); use valid `starttime,endtime,itemid,statusdescription). IDs 224385 (intubation), 227194 (extubation), and 225794 (NIV) corroborate transitions only.
- `icu/outputevents`, member `mimic-iv-3.1/icu/outputevents.csv.gz`, `datasets/mimic/table-a7ad1c4cdcdbfe0a.json`, schema hash `[source checksum]`. Optional coverage audit only; use `charttime,itemid,value,valueuom).
- `note/discharge`, ordinary file `[internal dataset path]`, catalog file `datasets/mimic/table-69be322e2b58015b.json`, schema hash `[source checksum]`. Join on `subject_id,hadm_id); use only pre-landmark metadata `note_id,note_type,note_seq,charttime,storetime` to measure documentation intensity, exclude `text), and never use post-landmark notes as predictors.
- `note/discharge_detail`, ordinary file `[internal dataset path]`, `datasets/mimic/table-18d43f38e33d1fd2.json`, schema hash `[source checksum]`. Join on `note_id); use only for availability audit, never field values as predictors.

For physiology verify the parent item set against `d_items): HR 220045; arterial MAP 220052; NIBP MAP 220181; RR 220210; SpO2 220277; O2 flow 223834; FiO2 223835; PEEP 220339; temperature 223761/223762. Keep arterial and NIBP MAP separate, convert Fahrenheit with a locked rule, and do not compare across-subject calendar time because MIMIC timestamps are subject-shifted. MIMIC-CXR images and raw waveforms are unavailable.

## Exposure, process, and observation construction

Carry the parent's support ledger unchanged. In each half-window and hour, classify respiratory and vasoactive evidence as positive recorded evidence, observed non-positive, no qualifying row/interval, contradiction, or invalid/out-of-window timing. Respiratory positivity is valid O2 flow >2 L/min, FiO2 >0.21, PEEP >0, or corroborating intubation/NIV; vasoactive positivity is valid overlap of a listed input interval. Procedures corroborate transitions but do not imply continuous support.

Adequate primary coverage requires at least two respiratory observation bins per half and at least two MAP observation bins per half. Durable recorded-off means no positive respiratory or vasoactive evidence in either half. Recent respiratory withdrawal means positive respiratory evidence in the preceding half and none in the final half; define analogous vasoactive and joint-withdrawal states. Retain active/residual, uninformative, discordant, and inadequate-coverage strata. For each domain/half evaluate `q_dh in {0,0.10,0.25,0.50,0.75,1.00}), including shared-q, domain/half-specific, and higher-vasoactive-q scenarios; recode only uninformative no-row hours, never observed non-positive values.

Create two locked feature blocks from identical twelve-bin inputs:

- Support/recovery block (S): support states and durations, transition/withdrawal timing, robust HR/MAP/RR/SpO2/O2/FiO2/PEEP/temperature summaries and slopes, source-channel indicators, contradictions, and the durable/recent/active/discordant labels.
- Process/observation block (O): age/sex/year group, admission context, ICU LOS, first/last careunit, pre-index transfer count and last careunit, service-transition count and timing, pre-landmark note count/type metadata, chart-event row counts, observation fractions, maximum gaps, source-channel counts, and missingness/coverage indicators. This block is a description of documentation and discharge process, not a causal adjustment set.

All (O) features must be computed only before `outtime). The primary analysis is the adequate-coverage subset; broad-cohort standardization and coverage-selection diagnostics are retained. Include masks and (O) in every model comparison so that an apparent support signal cannot be credited merely to how often a channel was charted.

The locked bridge rule is the parent's rule: for the earliest later ICU stay in the same subject/admission with `later.intime > index.outtime` and before the 48-hour/discharge limit, inspect valid `hosp/transfers` rows with non-null `careunit), valid `intime < outtime), interval beginning no earlier than `index.outtime-5 minutes), and ending no later than `later.intime+5 minutes). Clip to the index-outtime/later-intime span, require at least 30 minutes, and require `careunit` not equal to the later ICU `first_careunit` or `last_careunit`. Tie-break by greatest clipped duration, earliest transfer `outtime), then smallest `transfer_id). Save every candidate. Sensitivities use endpoint tolerance 0/5 minutes, duration 0/15/30/60 minutes, careunit-only versus interval-only, `eventtype='discharge'` exclusion, and linked ICU-unit matching. The primary rule is locked before fitting.

## Matched baseline and substantive alternative

Both models use the identical cohort, twelve-bin data, (S), (O), q scenarios, topology audit, outcomes, and patient-level splits. They target the same observable competing-event hazards, ([L,U]), and threshold operating characteristics.

### Transparent baseline

Fit pooled one-hour cause-specific discrete-time hazards through 48 hours for confirmed return, unconfirmed return, death, and alive discharge, plus the aggregate-return/death/discharge model. Use fixed summaries and prespecified interactions. Fit nested versions:

- (M_O): process/observation block only;
- (M_{O+S}): (M_O) plus support/recovery and physiology;
- masks-only and support-only diagnostic models.

Standardize predictions to the common adequate-coverage population and, separately, to the broad cohort through a locked coverage model. Derive (L) from confirmed-return CIF and (U) by collapsing confirmed and unconfirmed returns. Bootstrap subjects, never hourly rows. This baseline is interpretable and makes the bound construction visible, but it loses detailed within-window order and duration beyond the fixed summaries.

### Observation-aware mechanistic/learned alternative

Fit a constrained observation-aware latent location/support semi-Markov model using the same raw twelve-bin (S) and (O) fields. The pre-landmark component has separate respiratory and hemodynamic duration/recovery states and an explicit observation model for masks, row counts, and source channels. The post-landmark component has ICU, documented non-ICU, and unknown-location states; ICU intervals are high-specificity state evidence and transfer rows are imperfect observations. Include (O) as a process/intensity channel, not as latent physiology.

Fit on training subjects, choose duration/state complexity, regularization, and q handling on validation, and lock test paths. Evaluate the same four observable hazards and latent-transition sensitivity on a predeclared grid of transfer-capture sensitivity and false-bridge rate. A model-implied latent interval outside ([L,U]) is a bug or model rejection. A narrower interval is only model-based sensitivity because transfer sensitivity and false-bridge rates are not clinically validated.

This alternative reveals ordered support persistence/withdrawal, duration in known versus unknown location, and compatibility of return timing with an intervening non-ICU state that the summary baseline loses. Its scientific value is endpoint and process interpretation, not a small AUROC gain. A generic GRU/TCN is deferred because it adds capacity without an explicit observation/topology model; it becomes worth revisiting only if the constrained model demonstrates reproducible order information that the state model cannot represent, with a new predeclared estimand.

## Evaluation, uncertainty, and gates

For each model and split seed report 6-, 24-, and 48-hour confirmed lower CIF, aggregate upper CIF, interval width, competing death/discharge CIFs, and worst-case group contrasts. Report the incremental held-out comparison (M_{O+S}) versus (M_O) using subject-bootstrap uncertainty for absolute calibration, IPCW Brier score, and threshold separation. AUROC is secondary and never establishes topology validity.

The threshold analysis uses (	au=0.02,0.05,0.10), locked before test scoring. A patient is high-risk only when the lower predicted endpoint exceeds (	au), low-risk only when the upper predicted endpoint is below (	au), otherwise indeterminate. Report test event counts, lower/upper endpoint calibration, 95% confidence intervals, sensitivity, specificity, PPV, NPV, fraction indeterminate, and subgroup/topology/q stability. Do not use a threshold selected on the test set.

Use subject-level bootstrap 95% intervals with retained draws, calibration intercept/slope, calibration plots, multicause/IPCW Brier scores, overlap, positivity, effective sample size, and missingness/coverage transport. Repeat for seeds 17, 29, and 43. Supportive evidence requires:

- the full model's worst-case lower high-minus-low contrast exceeds 0.02 at 48 hours, is positive at 6/24 hours, and is stable over the primary q/topology grid;
- the support/recovery model materially improves held-out calibration or bound separation over (M_O), not merely AUROC;
- event support, overlap, calibration, and coverage transport are adequate;
- no material storetime, single-channel, or one-rule dependence;
- transfer-careunit permutation removes topology-specific structure; and
- the learned model remains within the nonparametric bounds and is stable across splits.

This supports an association with a record-compatible escalation and a possible retrospective review stratum only. Adverse evidence includes a non-positive lower contrast, aggregate-only signal, reversal across q/topology settings, no incremental value over (M_O), threshold performance driven by documentation counts, signal persisting after topology permutation, non-positivity, or latent output outside the bounds. Inconclusive evidence includes wide bounds, sparse events, high indeterminate fraction, poor calibration/transport, unstable splits, high latent entropy, or unjustified sensitivity parameters. A positive upper endpoint alone is not supportive of the latent claim.

Predeclared falsifications are: timestamp/dependency audit for post-outtime leakage; within-window hour-label shuffle; `storetime) in place of `charttime) as a negative timing control; masks-only, process-only, support-only, and physiology-only models; removal of procedure corroboration; separation of arterial/NIBP MAP and O2-flow/FiO2/PEEP channels; all q/window/threshold/coverage sensitivities; bridge/tie/topology variants; transfer-careunit permutation within admission; +6-hour transfer shift; pre-landmark pseudo-return window; complete-case versus coverage-restricted versus broad-standardized analysis; first-careunit, admission-type, anchor-year, and transfer-density strata; and split-seed/latent-state reproducibility. The process/observation block must be audited for whether threshold performance collapses after matching or standardizing across observation-intensity strata.

## Compute, limits, and unavailable evidence

The measured discovery audit read the exact admissions, patients, icustays, and transfers archive members using 4 CPUs and 16,384 MiB in 22.2 seconds. It computed only the broad topology counts above; it did not fit support exposures, process-adjusted models, thresholds, uncertainty, or clinical outcomes. Those counts must be recomputed and are not study results.

The future solver planning envelope is up to 16 CPUs, 262,144 MiB RAM, 8 GPUs, and 28,800 seconds. CPU is appropriate for streaming extraction, bounds, and the transparent baseline. Unverified estimates are 10–30 minutes for extraction, 30–60 minutes for baseline/bounds/bootstrap, and 1–4 hours for repeated semi-Markov fits and q/topology grids. A bounded one-A100 profile may be requested for repeated matrix-heavy fitting using `cuda:0) inside the allocation, but no GPU timing has been measured and GPU use is not required. Preserve checkpoints, wall time, retries, package versions, and output hashes.

The design is an adaptation, not reproduction of any demonstration. It cannot establish discharge readiness, planned/unplanned intent, treatment limitation, preventability, ward surveillance adequacy, causality, clinical utility, or benefit/harm from acting on a threshold. Those claims require clinician-reviewed chart and intent adjudication, validated transfer semantics, treatment-limitation and ward-monitoring data, external validation, and preferably a prospective or causal study. Discharge-note text is available but excluded from predictors; MIMIC-CXR images and raw waveforms are unavailable. Results are limited to the MIMIC snapshot and its subject-shifted structured documentation.

## Deferred alternatives and revisit evidence

- A generic GRU/TCN is deferred pending evidence from the constrained alternative that ordered trajectories add reproducible information beyond summaries and that a flexible representation is needed for that same estimand.
- A causal discharge-policy model is deferred until treatment assignment, intent/readiness adjudication, treatment limitation, and a defensible intervention are available.
- Notes-as-intent modeling is deferred because text may describe plans retrospectively and no validated intent/readiness labels are available; note metadata may measure documentation intensity only.
- External validation is deferred because no second transfer-semantic MIMIC cohort is configured.
- Image/waveform and renal endpoint branches are deferred because the required local modalities or validated endpoint evidence are unavailable.

Revisit any deferred branch only with the stated dependency and a new proposal; do not mechanically replace the partial-identification estimand.
