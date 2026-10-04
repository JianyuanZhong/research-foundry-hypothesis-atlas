# Renal–respiratory discordance at first ICU discharge

## Scientific deliverable

The future solver must newly construct and fit a leakage-safe MIMIC-IV 3.1 first-ICU-discharge study of whether a renal recovery phenotype changes the meaning of a recorded respiratory transition among patients with low final recorded burden. Completion requires locked, patient-level held-out outputs, not readiness alone:

1. `run_manifest.json`: catalog and source hashes, MIMIC snapshot, archive members, schema hashes, verified dictionary labels, item/code lists, thresholds, tie and topology rules, split seeds, software versions, and output hashes.
2. `cohort_audit.parquet`: one earliest eligible ICU stay per subject, join/exclusion counts, window and coverage flags, weight availability, respiratory/vasoactive/renal state counts, and primary/audit strata.
3. `hourly_ledger.parquet`: twelve one-hour rows in [outtime-12h,outtime), with physiology, respiratory and vasoactive evidence, renal measurements, urine-source selection, observation masks, process variables, and no post-outtime inputs.
4. `phenotype_audit.parquet`: raw values, source provenance, contradictions, half-window states, unknown states, and the reachable respiratory-by-renal cross-product.
5. `outcome_topology.parquet`: all candidate later ICU stays, transfer bridges, tie status, and lower/upper endpoint classification.
6. `cif_contrasts.parquet`, `test_predictions.parquet`, `calibration_uncertainty.parquet`, `falsification.parquet`, and `interpretation.md`, linking every reported claim to held-out estimates, counts, confidence intervals, overlap and sensitivity results.

The actual scientific work is to estimate the prespecified interaction and competing-event cumulative-incidence contrasts, then compare an auditable baseline with a matched observation-aware multi-organ sequence model. No association or clinical conclusion is claimed in this proposal.

## Unresolved question and hypothesis

The expert seeds on asynchronous organ recovery, discordant AKI recovery, and residual instability support only a clinically plausible question. The local evidence verifies dated respiratory/support records, creatinine and urine-output fields, and post-ICU topology; it does not establish that a creatinine fall represents renal recovery, that charted urine output is complete, or that an ICU return is adjudicated deterioration.

The unresolved claim is whether apparent respiratory recovery at ICU discharge has different early failure implications when renal clearance/urine-output evidence is discordant. This matters because a patient can meet a respiratory-looking low-burden snapshot while having low urine output and a changing creatinine, a pattern that could indicate unresolved systemic illness or fluid/measurement effects. A positive result could motivate targeted renal review when considering post-ICU monitoring; a null result would argue against treating this sparse renal pattern as a distinct discharge-risk phenotype.

Primary falsifiable hypothesis:

> Among adults at the first valid ICU outtime who have low final recorded respiratory and MAP burden and adequate observation, the 48-hour risk of a return-compatible ICU escalation is higher for an invasive-liberation-compatible or oxygen-only respiratory transition accompanied by renal discordance (falling/stable creatinine with low recorded urine output) than for the same respiratory transition with concordant renal recovery (falling/stable creatinine with adequate recorded urine output). The renal-by-respiratory interaction will remain directionally present after adjustment for final burden, support intensity, measurement intensity, and observable discharge process.

This is a prognostic record-association hypothesis. It is not an effect of extubation, diuresis, discharge, or a recommendation to delay discharge.

## Population, time and phenotype construction

Use read-only source `[internal dataset path]`, [source checksum], snapshot `[source checksum]`, and catalog `[internal dataset path]`, [source checksum]. Archive members below are read-only.

Select one earliest valid `icu/icustays` stay per `subject_id`, ordered by `intime) and tied by smallest `stay_id`. Require `hosp/patients.anchor_age >= 18` (retain top-coded age 91), valid `subject_id/hadm_id` joins to `hosp/admissions`, `intime < outtime < dischtime`, non-null `dischtime), no `deathtime <= outtime`, and at least 12 hours from `intime` to `outtime`. The index is `icustays.outtime`. Predictors are strictly in [outtime-12h,outtime), using `charttime` for point observations and `starttime,endtime` for intervals; `storetime` is audit-only and a negative-control feature. Follow-up is [outtime,min(outtime+48h,dischtime)).

Respiratory states are derived independently of renal and vasoactive states. Reuse the parent's auditable items: `icu/chartevents` item IDs 220277 SpO2, 223834 O2 Flow, 223835 Inspired O2 Fraction, 220339 PEEP set, 220210 Respiratory Rate; `icu/procedureevents` 224385 Intubation, 227194 Extubation, 225794 Non-invasive Ventilation. An invasive-liberation-compatible state requires extubation evidence 227194, preceding PEEP or FiO2 evidence, and no final-half PEEP/FiO2 positive evidence; an oxygen-transition state requires preceding O2-flow (>2 L/min) or FiO2 (>0.21), no final-half positive O2/FiO2, and no locked-window PEEP/NIV/invasive marker. Keep durable recorded-off and other/unknown states. These are compatible chart evidence, never proof of continuous ventilation or successful liberation.

Vasoactive states are independently derived from valid overlapping `icu/inputevents` intervals for norepinephrine 221906, epinephrine 221289/229617, dopamine 221662, phenylephrine 221749/229630/229631/229632, and vasopressin 222315. A cessation state has a valid listed interval in the preceding half and none in the final half; active has overlap in the final half; no-recorded-interval and unknown remain explicit. Do not infer physiologic off from absence.

Renal states use the same two six-hour halves. Primary serum creatinine uses `hosp/labevents` item 50912 (Creatinine, blood chemistry), with the latest valid value per half; `icu/chartevents` item 220615 (Creatinine serum) and 229761 (Creatinine whole blood) are prespecified sensitivity sources, not silently pooled with the primary source. Require a value in each half for a directional creatinine state. A fall/stable state is final <= prior x 1.10; a rise is >10%; threshold is locked before test evaluation and varied in an audit grid. This phenotype is not measured GFR.

Primary urine output uses `icu/outputevents` item IDs 226559 Foley, 226560 Void, 226561 Condom Cath, 226563 Suprapubic, 226564 right nephrostomy and 226565 left nephrostomy, with `charttime,value,valueuom`. Exclude irrigant/drain items. Bin nonnegative volumes by hour. To avoid double counting, use Foley as the primary source when present in a bin, otherwise aggregate the non-overlapping alternative urine sources; preserve all source rows and compare source-specific/maximum-source sensitivities. Require at least 8 of 12 hourly bins observed. If a valid `patientweight` from `icu/inputevents` is available in the window, primary adequacy is >=0.5 mL/kg/hour; use 30 mL/hour and weight-available-only as prespecified sensitivity analyses. Low output is not proof of oliguria when charting is incomplete.

The primary renal discordance is falling/stable creatinine plus low recorded urine output; concordant recovery is falling/stable creatinine plus adequate output. Rising-creatinine and unknown/contradictory states are retained as audit strata, not forced into either comparison. Form reachable cross-products with respiratory state and, secondarily, vasoactive state. The primary contrast is invasive-liberation-compatible × renal-discordant versus invasive-liberation-compatible × renal-concordant; oxygen-transition × renal-discordant versus oxygen-transition × renal-concordant is a prespecified replication contrast. If cells are sparse or overlap is poor, report inconclusive rather than merge phenotypes.

The primary low-burden restriction requires final-half respiratory positive evidence in fewer than one third of one-hour bins and final-half MAP below the training-locked low-MAP threshold in fewer than one third of valid bins, with at least two respiratory and two MAP bins in each half. MAP uses `icu/chartevents` 220052 arterial mean and 220181 non-invasive mean. All raw states, observation counts, and contradictions remain available for audit.

## Outcomes and estimands

Primary competing events over 6, 24 and 48 hours are:

- L: a later ICU stay preceded by a documented non-ICU transfer bridge;
- U: any later `icu/icustays` stay for the same `hadm_id`;
- in-hospital death before return;
- alive hospital discharge before return.

The unobserved true escalation is bounded only as L <= T <= U. A bridge requires a `hosp/transfers` interval with non-null `careunit`, beginning after outtime and before later ICU intime, lasting at least 30 minutes, with careunit distinct from the later ICU stay's first/last careunit. Never call return planned, unplanned, or deterioration. Apply one-minute ties and report 0- and 5-minute sensitivities. For any exposure contrast A-B, report the compatible interval [L_A-U_B, U_A-L_B], not a midpoint or a false point truth. Death and alive discharge are first-event competitors.

For each respiratory stratum, estimate standardized 48-hour CIF contrasts for renal discordance versus concordance and the interaction contrast (discordance effect in invasive-liberation-compatible minus discordance effect in oxygen-transition). Secondary horizons are 6 and 24 hours; full cohort, alternate weight/output/creatinine grids, and vasoactive cross-products are secondary. Multiplicity is controlled by declaring one primary 48-hour interaction and labeling all grids exploratory.

## Baseline and substantive alternative

Use fixed subject-level 70/15/15 train/validation/test splits with seeds 17, 29 and 43; all thresholds, imputation, model parameters and standardized weights are fit without test data.

The transparent baseline is a pooled one-hour discrete-time cause-specific competing-hazard model for L, U, death and discharge, plus an aggregate-return model. It includes the respiratory-by-renal phenotype and interaction, final/preceding HR, MAP, RR, SpO2, support evidence/intensity, creatinine and urine-output summaries, source-specific masks, row counts, pre-index transfer-process proxies, admission context, age, gender, anchor-year group and ICU LOS. Report nested models: physiology/support only; renal phenotype added; interaction added; observation/process added; full. Use held-out CIF calibration intercept/slope, IPCW Brier, overlap/effective sample size, and subject-bootstrap 95% intervals.

The substantive alternative is an observation-aware factorized hidden semi-Markov model with respiratory states (invasive-compatible, PEEP/NIV, oxygen-only, off, unknown), hemodynamic states (vasoactive, off, unknown), and renal states (creatinine falling/stable/rising/unknown crossed with urine-output adequate/low/unobserved). It models duration-dependent transitions over eight six-hour intervals and a separate observation-mask/intensity process; post-landmark location is ICU, documented non-ICU, or unknown. It uses the same underlying ledgers, patient split and outcomes as the baseline. It can reveal ordered, duration-dependent asynchronous organ trajectories and whether observation patterns create the apparent interaction, which half-window summaries lose. It cannot recover unobserved ward care, true ventilation, intent, measured filtration, or clinical deterioration. Reject any latent escalation estimate outside [L,U].

The baseline is scientifically sufficient and primary if the latent states are not identifiable, have high entropy, fail split stability, or do not replicate the observable-bound result. A GRU/TCN is deferred: additional flexible capacity would not resolve the specific renal measurement and outcome-topology uncertainty. Causal treatment-policy emulation, discharge-readiness classification, NLP for intent, waveforms, imaging, external validation and outside-hospital events require unavailable data or another study.

## Falsification and interpretation

Falsification tests include: removal of renal values while retaining masks; mask-only and physiology-only models; storetime substitution; urine-source removal; creatinine-source substitution; within-window order shuffling; respiratory/procedure removal; 6/12/24-hour window changes; q/measurement-coverage grids; bridge-duration and careunit/topology permutations; +6-hour transfer shifts; pre-outtime pseudo-landmarks; discharge-as-censoring; and admission-type/careunit strata. A renal interaction that appears at a pseudo-landmark, survives topology permutation, depends on one charting channel, or reverses under minimal source/tie changes is not supportive of the proposed biological interpretation.

Supportive results require adequate events and overlap, a stable interaction direction and worst-case lower/upper bound, uncertainty excluding the prespecified null for the primary direction, calibrated predictions, agreement between baseline and alternative on observable outcomes, and attenuation under mask/topology falsifications. An adverse result is null/reversal, disappearance after process adjustment, an effect confined to U but absent from L, or a result driven by a single sparse source. Inconclusive means broad topology-compatible intervals, sparse discordant/concordant cells, high unknown prevalence, poor positivity, unstable thresholds, high latent entropy, or failure to verify source coverage.

Supportive results establish only a reproducible association in this MIMIC snapshot between recorded renal/respiratory evidence and recorded outcomes. They cannot establish that a creatinine fall is true renal recovery, that low output reflects oliguria, that ICU return is deterioration, or that acting on the phenotype improves monitoring or discharge safety. Clinical adjudication of deterioration, ventilation status, treatment limitations, discharge intent and ward surveillance; external validation; and a prospective or causal study are required for those claims.

## Exact data bindings and availability

All required data are present in the verified catalog and local source files:

- `hosp/admissions`, archive member `mimic-iv-3.1/hosp/admissions.csv.gz`, schema `datasets/mimic/table-e8ec3e6e4c428559.json`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`.
- `hosp/patients`, `mimic-iv-3.1/hosp/patients.csv.gz`, schema `datasets/mimic/table-9154f8c46cade9af.json`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`.
- `icu/icustays`, `mimic-iv-3.1/icu/icustays.csv.gz`, schema `datasets/mimic/table-7d5c8feb0fb0dbd4.json`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`.
- `hosp/transfers`, `mimic-iv-3.1/hosp/transfers.csv.gz`, schema `datasets/mimic/table-685b6b74d0d7c547.json`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `icu/chartevents`, `mimic-iv-3.1/icu/chartevents.csv.gz`, schema `datasets/mimic/table-8208609a785ea7e8.json`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `icu/d_items`, `mimic-iv-3.1/icu/d_items.csv.gz`, schema `datasets/mimic/table-d1023acc404fd1d4.json`: `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; assert labels and links before fitting.
- `icu/inputevents`, `mimic-iv-3.1/icu/inputevents.csv.gz`, schema `datasets/mimic/table-d193e854c19eb4ba.json`: `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,patientweight,` plus order/status fields; use valid interval overlap and patientweight only as specified.
- `icu/procedureevents`, `mimic-iv-3.1/icu/procedureevents.csv.gz`, schema `datasets/mimic/table-f6493e8403a0abe7.json`: `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,value,valueuom,location,locationcategory,` plus order/status fields.
- `icu/outputevents`, `mimic-iv-3.1/icu/outputevents.csv.gz`, schema `datasets/mimic/table-a7ad1c4cdcdbfe0a.json`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom`.
- `hosp/labevents`, `mimic-iv-3.1/hosp/labevents.csv.gz`, schema `datasets/mimic/table-bf701d962c63287c.json`: `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments`.
- `hosp/d_labitems`, `mimic-iv-3.1/hosp/d_labitems.csv.gz`, schema `datasets/mimic/table-57ae65f0eb6cf1a6.json`: `itemid,label,fluid,category`; verify item 50912 label Creatinine and use only blood chemistry in the primary.
- `icu/outputevents` urine item labels and the respiratory/vasoactive item labels were directly checked in `icu/d_items`; archive headers were directly read. Joins are `subject_id/hadm_id), with `stay_id` for same-stay ICU event joins. MIMIC timestamps are subject-shifted; do not align calendar dates across subjects.

## Evidence limits, demonstrations and deferred alternatives

The natural-history demonstration was read as methodological context: its dated sequence adaptation supports the idea of evaluating ordered trajectories, but its UKB/Danish cohorts and external data are not reproduced. The Bayesian demonstration motivates latent longitudinal structure, but verified genetic inputs are absent; this proposal is an explicitly different EHR-only adaptation. The cancer demonstration's supplement was available, but its main text/full STAR Methods were unavailable and chest-X-ray files are absent, so full multimodal reproduction is not claimed; a lab/EHR adaptation is deferred.

The ten MIMIC expert seeds were inspected. Seeds 01 (asynchronous recovery), 03 (discordant AKI recovery), and 10 (residual instability) motivate this exact adaptation. Seed 02 (diuretic timing) and 08 (creatinine during diuresis) need a treatment-policy/acute-heart-failure design with stronger time-varying confounding controls; they are deferred. Seed 04 (lactate/perfusion), 05 (stress glycemia), 06 (sedation), 07 (antimicrobial de-escalation), and 09 (transfusion ischemia) address different exposures or unavailable adjudication and are not silently substituted. Imported UKB/eICU seeds remain available but are not MIMIC parents.

Method comparison before selection is explicit. The baseline tests the interaction transparently and provides calibrated competing-event estimates; the factorized HSMM can reveal duration/order and observation-process structure that the baseline's half-window summaries lose. The alternative is selected only if latent-state diagnostics and observable-bound replication support it; otherwise it is deferred. Approximate future solver envelope is <=16 CPUs, 262144 MiB RAM, <=8 A100 80GB GPUs, <=28800 seconds. Baseline is expected CPU-suitable; the HSMM should start on CPU and may request one allocated A100 only if profiling demonstrates a matrix bottleneck. These are planning estimates, not measured full-study runtimes. Discovery facts measured here are the exact catalog/schema/archive/header/dictionary availability and the configured 7,200-second allowance; full event counts, cell sizes, bootstrap and HSMM runtime remain unmeasured.

MIMIC lacks raw waveforms, continuous support between observations, measured GFR, complete urine collection, clinician intent/goals of care/treatment limitations, discharge rationale, ward monitoring, adjudicated deterioration, validated transfer semantics, and external outcomes. Keep sources read-only; write all derived outputs in the workspace and never publish clinical rows or notes.
