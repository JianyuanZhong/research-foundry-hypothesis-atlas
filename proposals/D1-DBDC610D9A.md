> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Source-concordant renal-support documentation after a recorded creatinine rise

## Scientific deliverable and substantive advance

The solver must newly construct the validated parent’s eICU first-rise cohort and an auditable source-specific event ledger, then estimate whether a clinically consequential downstream endpoint—newly documented renal support after the rise—is reproducible across two distinct documentation systems.

The primary clinical estimand is the development-hospital 90th-minus-10th percentile spread in the standardized 48-hour cumulative incidence of either-source renal-support documentation after a first qualifying recorded creatinine rise among stays with no strict support record through that rise:

H_E = Q90_h(q_E,h) - Q10_h(q_E,h).

Here E is the first post-rise event from either (a) a prespecified treatment modality string or (b) a prespecified high-specificity intake/output label. The clinically consequential part is the downstream renal-care documentation state, not a predictive score. The source-specific estimates H_T and H_IO, their difference, cross-source hospital ordering, and the percentage of either-source events corroborated by the other source are mandatory co-reports. The primary hypothesis is supported only if the either-source spread is materially positive and the source-specific analyses replicate it; a union-only result is treated as ascertainment heterogeneity, not source-robust clinical evidence.

This is a new child estimand. The parent established a documented renal-escalation composite after a strict no-prior-support gate; this child makes the unresolved mechanism primary: does its support component persist when separately measured in treatment documentation and high-specificity flowsheet documentation? It therefore tests source robustness and discordance directly rather than treating a pooled support label as self-validating.

## What is known and what remains unresolved

The inspected eICU data paper describes intakeOutput as a volume/documentation table containing running intake, output, dialysis and net totals, and notes that hospitals customize workflows and that completeness varies by hospital or ICU. Official eICU documentation likewise describes flowsheet-derived intake/output and warns that absent measurements are not evidence of absent care and that cumulative values can be duplicated. The source paper’s support is documentation and schema evidence, not validation of either source as a dialysis-initiation or treatment-receipt gold standard.

The frozen snapshot and full-file audit establish that the required fields exist and that candidate records are nonempty. The audit found 39,800 broad treatment candidates in 8,258 stays and 9,155 usable rows with named high-specificity flowsheet labels in 270 stays; only 117 candidate stays overlapped at any time and 60 within 60 minutes. These are unrestricted feasibility counts, not prevalences or rates in the target cohort. Treatment candidates include catheter/access strings and must be narrowed. The flowsheet count is sparse enough that source-specific support may fail.

The unresolved claim to test is:

> After excluding any prior strict support record and standardizing observed severity and pre-rise renal surveillance, a hospital-level spread in 48-hour post-rise renal-support documentation is present in the either-source endpoint and is qualitatively reproducible in treatment and high-specificity intake/output records.

This does not claim that a creatinine rise is biological AKI, that either source proves renal replacement initiation, that missing flowsheet data means no support, or that hospitals differ in treatment quality.

## Population, landmark, and temporal boundary

Use eICU snapshot [source checksum]. The unit is patientunitstayid; repeated unit stays remain separate. Use uniquepid only for clustering and connected-component split checks.

Retain the parent population exactly:

- adult patient.age >= 18, parsing age > 89 as 90 and retaining an age-censored flag;
- at least two valid vitalPeriodic.systemicmean values in minutes 0–360, restricted to 20–200 mmHg;
- a valid baseline creatinine at or before the first raw low-MAP observation;
- first raw periodic systemicmean < 65 in [0, 360];
- no qualifying baseline-plus-0.3 mg/dL creatinine rise through minute 360; and
- patient.unitdischargeoffset > 360.

Let U = unitdischargeoffset and E = min(2880,U). Every source row is eligible only when its ICU-relative event time is t < U. At a boundary, discharge takes precedence over an event at U when U <= 2880; an event at exactly 2880 is eligible only when U > 2880. Do not concatenate later ICU stays. unitdischargestatus=Expired is recorded unit death, Alive is alive unit exit, and NULL is unknown-status censoring; NULL is never recoded as alive.

Use the parent’s raw MAP and creatinine construction: deduplicate exact vitalperiodicid and labid; use raw vitalPeriodic.observationoffset and primary lab.labresultoffset; require case-folded labname=creatinine, numeric labresult in [0,60], and explicit mg/dL agreement in labmeasurenamesystem and labmeasurenameinterface. Conflicting or unverified units are excluded. Baseline is the earliest qualifying result; first rise is the first post-landmark qualifying result at least 0.3 mg/dL above baseline, after the no-rise-through-360 rule, and before E. The first-rise record is not itself a support event.

## Strict support gate and two source definitions

For each first-rise stay, define S_prior=1 if either source has any strict support record at ICU time 0 through the first-rise time inclusive. Exclude S_prior=1 from the primary incident-escalation risk set. Retain this group as a descriptive secondary labelled ongoing-or-new documentation; do not infer unobserved pre-ICU support absence.

Treatment support T uses a case-folded, normalized treatment.treatmentstring taxonomy restricted to explicit renal replacement modalities: hemodialysis, peritoneal dialysis, SLED, CVVH/CVVHD/CAVHD and equivalent explicit renal dialysis modality paths. The solver must bind the exact observed strings and report the retained dictionary. Exclude strings containing catheter insertion, venous access, arteriovenous shunt/access surgery, line/flush language, generic electrolyte correction without an explicit modality, and ultrafiltration described as fluid removal only. treatmentid is the deduplication key and treatmentoffset is the primary event time. activeupondischarge is descriptive only; it does not establish administration, initiation, duration or receipt.

Flowsheet support IO uses only exact case-insensitive intakeOutput.cellpath or celllabel values: Dialysis (ml)|In, Dialysis (ml)|Out, CRRT Actual Pt Fluid Removed, CRRT Out, CRRT - UF removed, CRRT- UF removed, or Hemofiltration. Require finite nonzero cellvaluenumeric or finite nonzero dialysistotal; do not use dialysistotal from an unlabeled row as a standalone support endpoint. Deduplicate exact intakeoutputid; use intakeoutputoffset as primary event time and retain intakeoutputentryoffset for a timing sensitivity. cellvaluetext is audit context only. A negative/positive fluid value remains a documented flowsheet value, not proof of a treatment session.

The primary support event is the earliest eligible T or IO time after the first rise and before E. Same-time events retain both source indicators. A secondary concordance state is present when both sources occur in the same stay within 60 minutes of the earlier source event; 30- and 120-minute windows are prespecified sensitivities. Later source evidence is retained in the ledger rather than backdated. Neither source is called dialysis initiation.

## Prior surveillance and standardization variables

Before the first rise, derive only information available by that time:

- creatinine test count, time since prior qualifying creatinine and valid-lab coverage from lab.labresultoffset;
- presence, count and timing density of urine-labelled intakeOutput rows for observation-process surveillance only;
- first-low MAP, burden, coverage, low-MAP runs and recovery from vitalPeriodic.observationoffset/systemicmean;
- baseline creatinine, first-rise value, delta and time from landmark;
- age, gender, ethnicity, unitadmitsource, unittype;
- admission descriptors from apacheApsVar and apachePatientResult: acutephysiologyscore, apachescore, predictedicumortality; and
- hospital context from hospital: numbedscategory, teachingstatus, region, joined on hospitalid.

No post-rise lab value, support-source indicator, confirmation-row metadata or future documentation is a predictor. Urine labels are not converted into oliguria or KDIGO criteria because collection intervals and denominators are not validated.

Standardize all hospital estimates to the development risk-set distribution of the same covariates, including pre-rise creatinine-testing and urine-observability variables. Report an unadjusted/common-case-mix estimate and the surveillance-adjusted primary estimate. This adjustment is a robustness/ascertainment test, not a causal mediation analysis.

## Primary analysis and support gates

For each development hospital h, let q_E,h be the 48-hour CIF of E after first rise, with unit death and alive unit exit as competing events and unknown-status discharge censored. Estimate H_E after development-only standardization. Separately estimate H_T and H_IO under the identical risk set, covariates, clock, split and standardization; report H_E-H_T, H_E-H_IO, source-specific event counts, and the proportion of E events with both-source corroboration.

A hospital is source-supported for the concordance claim only with at least 50 eligible first-rise/no-prior-support stays and at least 10 post-rise events in each source. The primary either-source spread requires at least 10 hospitals with at least 50 eligible stays and at least 10 either-source events. If the intersection of source-supported hospitals has fewer than 10 hospitals, source-concordance is inconclusive even if the union endpoint is estimable. Report all support failures rather than relaxing thresholds.

The source-robust hypothesis is supportive only if all are met:

1. H_E >= 5 percentage points and its two-sided 95% hospital-cluster interval excludes zero;
2. on the source-supported intersection, H_T and H_IO are both positive, have the same qualitative hospital ordering as H_E, and each has a two-sided interval excluding zero;
3. the 95% interval for H_T-H_IO lies within the prespecified practical-discordance band [-5,+5] percentage points, and the bootstrap median rank correlation of hospital estimates is at least 0.50; and
4. at least half of the either-source spread remains after adding pre-rise surveillance variables and competing-exit processes, with no domination by a single source in the component decomposition.

These are evidence rules for a documented process; the 5-point and 50% values are not clinical treatment thresholds.

## Matched transparent baseline

Fit regularized additive cause-specific pooled-logistic models on identical 30-minute intervals and risk sets. Model the first post-rise T, IO, either-source support, both-source corroboration, unit death, alive exit and unknown-status censoring as explicitly defined processes. Include prespecified linear/spline elapsed-time terms, common slopes, transition/source-specific hospital random intercepts and hospital context where estimable.

Nested baseline fits are:

- B0: case mix and common elapsed-time effects, no hospital heterogeneity;
- B1: B0 plus source-specific hospital random intercepts;
- B2: B1 plus pre-rise creatinine-testing and urine-observability surveillance terms;
- B3: B2 plus source indicator/process decomposition, yielding H_T, H_IO, H_E, discordance and corroboration;
- B4: B3 without hospital-by-time slopes as a stability reference.

The additive model is transparent and supplies the required standardized CIFs, component contrasts and observed-versus-predicted curves. It treats source pathways as parallel cause-specific documentation processes and therefore loses the order and waiting-time information needed to distinguish treatment-first, flowsheet-first, corroborated, and source-discordant sequences.

## Ordered multi-state alternative

Fit a piecewise-exponential multi-state model on exactly the same cohort, 30-minute grid, covariates, split, standardization distribution and bootstrap. Start at first rise. Transitions are:

- no post-rise support -> treatment-only documentation;
- no post-rise support -> flowsheet-only documentation;
- either source-only -> both-source corroboration when the other source occurs within 60 minutes;
- from every non-exit state -> recorded unit death or alive exit;
- unknown-status exit -> censoring.

The model retains later noncorroborating source records and separately reports source-first order, waiting time to corroboration, and confirmation-versus-support timing. Use transition-specific shrunken hospital effects and fixed hospital context only where supported. The multi-state model can reveal whether hospital variation occurs at treatment documentation, flowsheet observability, corroboration, or competing exit. This information is lost in the parallel additive baseline. Agreement on the primary H_E and source-specific spreads is robustness; disagreement is model uncertainty, not a license to choose the favorable model.

A learned longitudinal model is deferred, not prohibited. Revisit only if both prespecified models show reproducible shape-specific held-out miscalibration in the same source-decomposed estimand, and a learned model can preserve the no-prior-support gate, source-specific outcomes, component decomposition, calibration and hospital-held-out transport. A causal pressor model remains deferred because infusionDrug does not validate administration, dose, indication, intent or complete exposure.

## Hospital-held-out transport and uncertainty

Hash hospitalid deterministically into 80% development and 20% held-out hospitals before cohort summaries, label pooling, missingness handling, fitting, thresholds or standardization. Keep any uniquepid connected hospital component together and report coverage loss. Use a second fixed hash as a sensitivity.

Fit and standardize only in development hospitals. Apply frozen models to held-out hospitals with no local refitting, tuning or recalibration; set unobserved held-out hospital random effects to the prespecified population mean. Report source-specific and either-source observed-versus-predicted 48-hour CIFs, Brier scores, calibration, event counts, timing overlap, and aggregate process discrepancies. Held-out hospital descriptive estimates cannot tune the model. Transport is inconclusive with fewer than 10 held-out hospitals, sparse source events, inadequate category overlap, extreme weights, failed convergence or calibration failure.

Use 500 hospital-cluster bootstrap replicates for H_E, H_T, H_IO, their difference, rank correlation, corroboration, model differences, and parent contrasts. Add a uniquepid-clustered sensitivity. Report effective sample size, supported hospitals, source event counts, hospital shrinkage, overlap, missing-status dependence and convergence. Checkpoint the cohort ledger, source dictionaries, fits and bootstrap summaries within the 16-CPU/262144-MiB/up-to-8-A100/28,800-second future solver envelope. The tabular fits are CPU-first; GPU is optional only after allocated profiling and explicit cuda:0 use. Discovery scans were measured; full ledger, multi-state fit and 500-bootstrap runtimes remain unmeasured.

## Falsification and interpretation

The central discordance falsification is prespecified: if H_T is positive but H_IO is null/reversed, if treatment-first versus flowsheet-first ordering is unstable, if the difference exceeds the ±5-point equivalence band, or if the union spread is driven by one source without corroboration, the source-robust hypothesis fails. This would support source-specific ascertainment heterogeneity, not a renal-treatment effect.

Adverse evidence also includes disappearance after pre-rise surveillance adjustment, loss after strict catheter/access exclusions, instability across 30/60/120-minute corroboration windows, unit-boundary or timing-clock sensitivities, or strong dependence on NULL discharge status. A large either-source spread with no source-specific replication is a documentation-capture result. A large corroboration spread with no source-only spread may indicate selective dual documentation and is not evidence of treatment variation.

Inconclusive evidence includes fewer than 10 supported hospitals, fewer than 10 events per source per supported hospital, sparse either-source events, inadequate timing overlap, poor held-out calibration, extreme weights, failed convergence, unstable bootstrap intervals, strong missingness dependence, or model disagreement. Do not downgrade an inconclusive result to a positive finding.

Computationally checkable claims include source hashes and headers, exact string dictionaries, joins, deduplication, unit verification, time boundaries, prior-support exclusion, source-specific state transitions, split, fits, standardization, event counts, uncertainty, calibration and reproducibility. Clinical adjudication or another study is required to determine whether a creatinine rise is biological AKI; whether a treatment or flowsheet record means actual renal replacement initiation, delivery or intent; whether chronic dialysis preceded the ICU stay; whether urine output is oliguria; and whether source absence reflects no care versus missing documentation. The study cannot establish renal benefit/harm, hospital quality ranking, a causal effect, a treatment threshold or a policy change.

## Exact data bindings, source provenance and availability

Catalog: [internal dataset path]; catalog [source checksum]. eICU snapshot: [source checksum]. The full eICU guide lists 31 tables; every source is a read-only gzip ordinary file with no internal archive member.

- Patient/index and exits: [internal dataset path] 2.0 data/patient.csv.gz, SHA [source checksum]; schema datasets/eicu/table-ab037c09d7df9a3c.json, SHA [source checksum]. Join patientunitstayid; use age, gender, ethnicity, hospitalid, unitadmitsource, unittype, unitdischargeoffset, unitdischargelocation, unitdischargestatus, uniquepid.
- Periodic MAP: [internal dataset path] 2.0 data/vitalPeriodic.csv.gz, SHA [source checksum]; schema datasets/eicu/table-a22c6d6981a32279.json, SHA [source checksum]. Use vitalperiodicid, patientunitstayid, observationoffset, systemicmean.
- Creatinine: [internal dataset path] 2.0 data/lab.csv.gz, SHA [source checksum]; schema datasets/eicu/table-79bdb33275339b1a.json, SHA [source checksum]. Use labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labmeasurenameinterface, labresultrevisedoffset; labtypeid is retained for audit, not assumed assay identity.
- Treatment source: [internal dataset path] 2.0 dataset/treatment.csv.gz, SHA [source checksum]; schema datasets/eicu/table-5461361964176606.json, SHA [source checksum]. Join patientunitstayid; use treatmentid, treatmentoffset, treatmentstring, activeupondischarge.
- Flowsheet source: [internal dataset path] 2.0 data/intakeOutput.csv.gz, SHA [source checksum]; schema datasets/eicu/table-ebba5dc91b1d37e7.json, SHA [source checksum]. Join patientunitstayid; use intakeoutputid, intakeoutputoffset, intakeoutputentryoffset, dialysistotal, cellpath, celllabel, cellvaluenumeric, cellvaluetext.
- Severity/APACHE: [internal dataset path] 2.0 data/apacheApsVar.csv.gz, SHA [source checksum]; schema datasets/eicu/table-67711a86e012835e.json, SHA [source checksum]; join patientunitstayid and use admission severity descriptors. [internal dataset path] 2.0 data/apachePatientResult.csv.gz, SHA [source checksum]; schema datasets/eicu/table-754bebf64d3d9909.json, SHA [source checksum]; join patientunitstayid and use acutephysiologyscore, apachescore, predictedicumortality only. Never use actual outcomes as predictors.
- Hospital context: [internal dataset path] 2.0 data/hospital.csv.gz, SHA [source checksum]; schema datasets/eicu/table-811df7b2ef435e12.json, SHA [source checksum]; join hospitalid; use numbedscategory, teachingstatus, region.

The source files are ordinary files, not archives; no archive member is applicable. Narrative notes, diagnosis rows, generic medication rows and incomplete urine labels do not supply validated renal adjudication or treatment receipt.

## Alternatives retained and actual selection

The simple additive baseline is mandatory because it provides auditable component-wise hospital CIFs, competing exits, standardization and transparent uncertainty on the exact estimand. The ordered multi-state model is selected as the substantive alternative because source order, corroboration waiting time and competing exits are the scientific mechanism under test; these are not recoverable from parallel additive components. Both use identical inputs, split, gates, outcomes and bootstrap.

A learned sequence model is explicitly deferred, not rejected. Revisit if held-out calibration shows reproducible nonlinear timing/source misfit in both prespecified models, enough source-specific events exist to preserve the same estimand, and added complexity improves process explanation rather than only a small predictive metric. A urine-output/KDIGO branch is deferred until collection intervals, denominators and adjudication are validated. A causal pressor branch is deferred until administration, dose, indication, intent and complete exposure are available. None of these dependencies is present in the configured data.

The actual deliverable is newly fitted source-specific and either-source CIF/process models, a frozen event ledger, source dictionaries, hospital spreads, source discordance/corroboration summaries, held-out transport diagnostics, uncertainty intervals, and sensitivity ledgers. Discovery produced no fitted results and this proposal claims none.
