> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Detection-aware first-day monitored invasive-MAP burden and subsequent creatinine-defined AKI

## Status, fixed design, and actual deliverable

This is a substantive outcome-ascertainment child of `[prior hypothesis]`. It preserves the parent's outcome-blind one-person index, invasive MAP exposure in the half-open interval `[0,1440)`, hour-24 landmark, pair-timed creatinine rule using only values strictly after minute 1,440, frozen hospital split, and noncausal scope. It does not reopen exposure construction: the parent's preregistered pseudo-missingness experiment remains the measurement gate and selected `M=24*n(MAP<65)/n(valid)` as the transparent primary monitored-time summary.

This child changes the primary outcome estimand for a scientific reason. Conditioning the main analysis on having a later creatinine leaves an unresolved selection question: a burden signal could reflect who is tested or remains in the ICU long enough to be tested. The primary population is therefore all 10,998 fixed landmark-eligible people, and the primary outcome is the cumulative incidence by ICU minute 10,080 of *detected*, pair-timed creatinine AKI before documented live ICU discharge or ICU death. Untested people are never relabeled as biological non-cases. The parent's later-tested estimand remains a secondary conditional estimand so that selection can be seen rather than hidden.

No post-hour-24 creatinine value, detected-AKI label, burden-outcome association, discharge/death gradient, or fitted outcome model was inspected in this discovery episode. The future solver must construct the event ledger, fit the transparent and ordered models, estimate held-hospital contrasts with uncertainty, and issue a conclusion through the frozen gates below. The deliverable is complete only when those new fitted objects and linked outputs exist; readiness or the inherited exposure audit is not an outcome result.

## Scientific opening, evidence-supported claim, and unresolved claim

A systematic review found highly heterogeneous ICU hypotension definitions; most studies favored associations with mortality and AKI, but the pooled AKI analysis was not confirmatory [K1]. FINNAKI reported that lower time-adjusted MAP during the first 24 hours was associated with AKI progression in 423 severe-sepsis patients with prospectively collected, dense hemodynamic data [K2]. This supports a clinically important association in a narrower setting, not transport to this eICU population, not duration below 65 versus nadir, and not causality. KDIGO defines AKI using timed serum-creatinine changes or urine output and explicitly notes inconsistent implementation, missed cases when analyses rely on documented creatinine increases, and clinical discretion in monitoring frequency [K3].

The strongest claim supported by current study-specific evidence is narrower still: the fixed monitored-time burden passed its preregistered outcome-blind internal-gap stress test, while outcome-blind audit data showed that later-creatinine opportunity varied with MAP observation geometry. The parent observed logical full-clock interval widths of 1.50/3.67/5.50 hours at the median/p75/p90, missing day boundaries in 46.9%, and an 11.3 percentage-point decline in post-hour-24 testing opportunity across logical-width quartiles. Those are measurement and opportunity findings, not evidence that burden predicts AKI.

The unresolved hypothesis is:

> In the frozen 10,998-person hour-24 opportunity cohort, greater first-day 24-hour-equivalent monitored invasive-MAP<65 burden contains held-hospital information beyond a flexible invasive-MAP nadir model for the day-7 cumulative incidence of pair-timed *detected* creatinine AKI before live ICU discharge or ICU death; that information appears in the probability that a performed creatinine test crosses the frozen AKI threshold and is not explained solely by creatinine-test intensity, longer ICU retention, death, measured MAP-observation geometry, or hospital convention.

The leading interpretation is that cumulative low pressure carries prognostic renal-risk information lost by nadir. The strongest rival is a coupled care/ascertainment process: illness severity, arterial-line retention, testing practice, and ICU retention jointly make both burden and AKI detection more observable. The designs differ observably. The leading interpretation predicts a positive held-hospital detected-AKI contrast and incremental information in positive-versus-negative creatinine marks after the ordered test/exit process is represented. The rival predicts that burden principally improves test-intensity or retention/death components, with little or no held-site improvement in the positive mark or the detected-AKI cumulative incidence once all landmark-eligible people are included. Neither pattern identifies renal hypoperfusion, the effect of changing MAP, or latent AKI among untested people.

Resolution matters because an incremental burden signal robust to detection opportunity would justify preserving cumulative hypotension in prospective renal-risk measurement rather than relying on a single minimum. An ascertainment-only or precise adverse result would argue against promoting this noisier summary from retrospective eICU data. No result selects a MAP treatment target.

## Exact read-only data bindings

Dataset snapshot: `[source checksum]`. All sources are gzip CSV ordinary files; archive member is `null`. The complete catalog JSON and actual source headers were rechecked in this episode. Event tables join to `patient` on `patientunitstayid`; `patienthealthsystemstayid` groups a hospitalization, `uniquepid` a person, and `hospitalid` a transport cluster. Numeric offsets are minutes from ICU admission.

- `patient`: `[internal dataset path]`; [source checksum]; catalog `datasets/eicu/table-ab037c09d7df9a3c.json`. Required columns: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `hospitalid`, `age`, `gender`, `ethnicity`, `unitvisitnumber`, `unitstaytype`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`, `unitadmitsource`, `hospitaladmitsource`, `unittype`, `apacheadmissiondx`, `admissionweight`. `unitdischargeoffset` is the competing-exit time; normalized `unitdischargestatus='expired'` defines documented ICU death and `'alive'` defines documented live ICU discharge. Any other/missing status is retained as unknown exit, reported, and bounded rather than silently imputed.
- `vitalPeriodic`: `[internal dataset path]`; [source checksum]; catalog `datasets/eicu/table-a22c6d6981a32279.json`. Required: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `systemicmean`, `systemicsystolic`, `systemicdiastolic`. These are five-minute summaries, not raw waveforms.
- `lab`: `[internal dataset path]`; [source checksum]; catalog `datasets/eicu/table-79bdb33275339b1a.json`. Required: `labid`, `patientunitstayid`, `labresultoffset`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`, `labresultrevisedoffset`. Biological event time is `labresultoffset`; `labresultrevisedoffset` is audit-only.
- `infusionDrug`: `[internal dataset path]`; [source checksum]; catalog `datasets/eicu/table-18e1a8caaa91eb44.json`. Required: `infusiondrugid`, `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `patientweight`. Fixed case-insensitive names identify norepinephrine/Levophed, epinephrine, phenylephrine, vasopressin, and dopamine. Units are too heterogeneous for dose equivalence; presence and timing only are used.
- `apacheApsVar`: same source root, `apacheApsVar.csv.gz`; [source checksum]; catalog `datasets/eicu/table-67711a86e012835e.json`. Key `patientunitstayid`; use `dialysis`, `intubated`, `vent`, `wbc`, `temperature`, `respiratoryrate`, `sodium`, `heartrate`, `ph`, `hematocrit`, `albumin`, `pao2`, `pco2`, `bun`, `glucose`, `bilirubin`, `fio2`; −1 is missing. Its `meanbp`, `creatinine`, and `urine` are not used to define exposure, endpoint, or primary renal trajectory.
- `apachePatientResult`: same root, `apachePatientResult.csv.gz`; [source checksum]; catalog `datasets/eicu/table-754bebf64d3d9909.json`. Required: `patientunitstayid`, `apacheversion`, `acutephysiologyscore`, `apachescore`; freeze one version on training hospitals and use composites only in sensitivity analysis.
- `vitalAperiodic`: same root, `vitalAperiodic.csv.gz`; [source checksum]; catalog `datasets/eicu/table-72ace5b89971196b.json`. Required: `patientunitstayid`, `observationoffset`, `noninvasivemean`, `noninvasivesystolic`, `noninvasivediastolic`. This is a separate-modality sensitivity and is never merged into invasive MAP.

HCC, MIMIC, UKB, all eICU rows, and notes remain available read-only. This experiment needs only these seven eICU tables. All event ledgers, models, and reports must be written under `work/outcome-ascertainment-evolution/`.

## Frozen index, split, exposure, and landmark covariates

Before reading MAP or post-landmark creatinine support, map `age='> 89'` to 90 and retain age ≥18, `unitvisitnumber=1`, `unitstaytype='admit'`, and `unitdischargeoffset>1440`. Keep the smallest eligible `patientunitstayid` per `patienthealthsystemstayid`. For each nonmissing `uniquepid`, rank eligible encounters by MD5 of `"eicu-map-aki-index-20260924:" + patienthealthsystemstayid`, then health-system stay and unit-stay ID; retain one. This is a reproducible outcome-blind index, not the first-ever encounter because cross-hospital dates are unavailable.

Freeze hospitals with SHA-256 salt `eicu-map-aki-20260924-rotation1:`. Reproduce the inherited 10,998 opportunity-cohort people across 165 hospitals and split counts 5,428/3,057/2,513 for train/validation/test before outcome construction. Reproduce the later-tested 4,517/2,438/2,026 people and 103/23/34 contributing hospitals as a secondary support check. Any mismatch stops fitting. All preprocessing, knots, penalties, interval widths, and decisions use training/validation hospitals; test hospitals are opened once.

Exposure is unchanged: `0 <= observationoffset < 1440`; minute 1,440 is excluded. Form bins `[5k,5(k+1))`, k=0,…,287. Parse `systemicmean`, reject values <20 or >180 mmHg, median-collapse duplicate stay/offset values, then median within stay/bin. Require at least 202 observed bins. Primary exposure is `M=24*n(bin MAP<65)/n(valid bins)`; comparator is invasive-MAP nadir. Retain observed low hours, monitored fraction, logical full-clock interval and width, first/last support, boundary/internal gaps, gap starts and re-entry after low state, six-hour sampling density, maximum gap, source multiplicity/off-grid values, physiologic-triplet flags, adjacent changes >40 mmHg, 24 hourly low fractions/nadirs/masks/time-since-observation, longest low run, episode count, and pressor timing/adjacency. `M` is monitored-time burden, never literal full-clock duration.

Landmark-only covariates shared by every outcome model are age; sex; ethnicity; admission source; unit type; weight; admission and last pre-landmark creatinine; pre-landmark creatinine change, slope, count, and recency; the complete exposure-observation geometry above; non-BP/non-creatinine `apacheApsVar` physiology with missing indicators; and day-1 pressor agent presence, entry counts, first/last entry, hourly masks, and gap-boundary adjacency. Future test count, future creatinine, future discharge, and future death are never baseline predictors. Pressor adjustment is a treatment/measurement sensitivity because it may be response, confounder, mediator, or collider.

The inherited exposure gate remains binding. Exact rerun of D0 is materially adverse if held-test absolute bias is ≥0.50 h with interval excluding zero, MAE >1 h, p90 error >2 h, or p25/p75 class discordance >10%. The ordered D1 cannot replace D0 unless all inherited replacement criteria pass. Exposure-gate failure stops outcome fitting; the prior passing run is evidence only for the specified pseudo-missingness process, not true line presence.

## Pair-timed strictly post-hour-24 creatinine process

Select rows with `lower(trim(labname))='creatinine'`, compatible mg/dL system/interface units, and numeric `labresult` 0.1–20 mg/dL. Median-collapse same-stay/same-offset values and report all unit conflicts and discordant duplicates. Admission creatinine is the earliest valid value in `[-360,360]`. Require at least one valid value in `(-360,1440]`. Exclude any person who has progressed through and including minute 1,440: value ≥admission+0.3 mg/dL or ≥1.5×admission.

Let `t_last` and `c_last` be the last valid creatinine at or before 1,440 and `t_adm,c_adm` the admission pair. A valid later test is any selected value at `1440 < t <= min(10080,unitdischargeoffset)`. It is a positive detected-AKI mark if either:

1. `c(t)-c_last >= 0.3` and `0 < t-t_last <= 2880`; or
2. `c(t) >= 1.5*c_adm` and `0 < t-t_adm <= 10080`.

The first positive mark is absorbing detected AKI. A valid test that meets neither rule at its event time is a negative mark; it is not proof of no biological AKI. Same-minute creatinines are collapsed before marking. Because the frozen endpoint includes values at `unitdischargeoffset`, a positive mark at exactly that offset precedes the discharge/death exit; otherwise exact offset order is used.

From minute 1,440 until `H=10080`, every opportunity-cohort person occupies one observable state: U (alive in ICU, no later test yet), N (alive in ICU, at least one negative later test, no detection), A (detected AKI, absorbing), L (documented live ICU discharge before detection, absorbing), D (documented ICU death before detection, absorbing), or X (unknown-status ICU exit, absorbing). Remaining U/N at H are administratively retained without detection. X is always reported; if it exceeds 0.5% in any partition, the main interpretation is inconclusive pending source review. Otherwise bound X once as all-live and once as all-death. Urine-output AKI, timed RRT, pre-illness baseline, post-ICU testing, etiology, and community-acquired AKI remain unobserved.

## Primary and secondary estimands

The primary estimand is a held-hospital, model-standardized descriptive contrast in day-7 cumulative incidence of observed A in all 10,998 landmark-eligible people:

`Δdet = mean_i[P(A by H | M=p75_s, nadir stratum s, X_i) - P(A by H | M=p25_s, nadir stratum s, X_i)]`.

Training-hospital p25/p75 values are defined within prespecified 5-mmHg nadir strata and restricted to empirical common support. Risk ratio and observed-scale calibration accompany the risk difference. “Replacing” M for standardization is a prediction contrast, not an intervention.

Required companion contrasts are day-7 probabilities of any later creatinine test, live ICU discharge, ICU death, unknown exit, and retention without detection. The original later-tested standardized contrast is secondary and explicitly conditional on at least one valid later test. Stabilized inverse-observation weighting for testing by hour 72, truncated at training-derived 1st/99th percentiles, is a sensitivity for that conditional estimand; it does not turn untested people into known cases and does not identify latent AKI.

## Transparent baseline and same-input ordered alternative

Both approaches use exactly the same 10,998 people, hospital split, source rows, landmark covariates, M/nadir definitions, event ledger, horizon, and bootstrap hospitals. Their only scientific difference is whether the post-landmark test/exit order is collapsed or represented.

### P0/P1: transparent endpoint baseline

P0 is a ridge-penalized multinomial landmark model for the mutually exclusive day-7 state `A/L/D/X/R`, where R means retained in ICU without detection and is separately tabulated as U or N. It uses restricted cubic splines for nadir and continuous landmark covariates. P1 adds a restricted cubic spline of M and frozen `M×nadir`, `M×logical-width`, and `M×gap-after-low` terms. No feature search is allowed.

In parallel, O0/O1 are transparent pooled logistic models for at least one valid creatinine in `(1440,min(4320,unitdischargeoffset)]`: O0 uses the same P0 landmark inputs; O1 adds the same burden terms as P1. They report held-hospital calibration, Brier/log loss, overlap, standardized test-probability contrasts, and observed test/exit state tables by burden, nadir, logical width, D0 error-risk features, and hospital. P0/P1 answer the detected-outcome question directly but discard negative-test timing and repeated-testing order.

### J0/J1: ordered, selection-aware marked-process alternative

J0/J1 factor the same event ledger from minute 1,440 through H into: (a) intensity of a valid creatinine test while in U/N; (b) probability that a performed test has a positive rather than negative frozen mark; and (c) cause-specific live-discharge, death, and unknown-exit hazards while undetected. Use 24 prespecified six-hour baseline-hazard intervals with exact within-interval event ordering. Negative tests update U→N or recur in N; positive tests update U/N→A; exits update U/N→L/D/X. At each negative mark, only past history—current U/N, prior test count, last observed creatinine and change, and time since last test—may update the next risk set. These post-landmark quantities are outcomes/history in the joint likelihood, not landmark confounders.

J0 uses the P0 landmark inputs and flexible nadir; J1 adds exactly the P1 M terms to each test, mark, and exit component. Group ridge penalties are selected on validation hospitals. From each fitted process, simulation or product integration yields the same `P(A by H)` and `Δdet` as P0/P1. Report held-hospital joint log score, component log scores, integrated Brier score, A/L/D cumulative-incidence calibration at hours 48, 72, and 168, and observed-versus-predicted state occupancy.

The ordered model can show where burden information enters. Report:

- `Δtest`: standardized change in probability of any test before exit;
- `Δmark`: standardized change in probability that the next performed test is positive over empirical test-event histories;
- `ΔL` and `ΔD`: live-discharge and death contrasts;
- an equalized-process diagnostic using J0 test/exit equations with J1's burden-sensitive mark equation; and
- the converse diagnostic using J1 test/exit equations with J0's mark equation.

These nonlinear decompositions need not sum exactly; report the remainder. They are model diagnostics, not effects of forcing tests or preventing discharge. P loses event order and repeated testing; J can reveal whether apparent burden information is concentrated in test opportunity, the positive mark, or competing exit. J still cannot recover AKI that was never measured.

A temporal convolutional model is deferred. It would add exposure morphology but would not better identify the outcome-observation process, and the inherited 1,456 aggregate events are below the parent's 1,500-event revisit gate. Revisit only if J establishes stable residual ordered information and additional event support exists. A latent-AKI imputation model is also deferred because no local gold-standard urine-output/RRT/adjudication labels can validate it.

## Fitting, evaluation, and uncertainty

Fit on training hospitals, select penalties and spline complexity once on validation hospitals, then lock and evaluate test hospitals once. No patient crosses partitions. Use 1,000 hospital-cluster bootstrap replicates with full refitting; preserve failed replicates and percentile intervals. Also report equal-hospital summaries, within-hospital estimates for sites with at least 20 detections and both burden-support levels, leave-one-hospital-out influence, and random-effects heterogeneity as descriptive checks.

Primary model comparisons are P1 versus P0 one-versus-rest detected-AKI log loss plus full multinomial log loss, and J1 versus J0 mark log loss plus joint log score. Also report Brier score, calibration intercept/slope, calibration curves, AUC only as secondary, common-support counts, weight effective sample size, and p25/p75 standardized contrasts. A model with better discrimination but materially worse calibration is not supportive.

Frozen sensitivities are: fixed testing through hour 72; at least two later tests; excluding tests in `(1440,1500]`; ≥90% MAP coverage with both boundaries supported; 60% and 80% coverage thresholds; triplet/artifact exclusion; D1 exposure; noninvasive-MAP separate modality; pressor-rich model; within-hospital/equal-hospital weighting; removal of the most influential hospital; six-hour versus 12-hour J intervals; and X all-live/all-death bounds. Pattern-mixture analyses multiply the modeled odds of an unobserved positive mark in untested U intervals by 0.5, 0.75, 1, 1.5, and 2; these are sensitivity scenarios, not identified latent outcomes.

## Frozen falsification and interpretation gates

Support for the primary claim that burden adds information not explained solely by ascertainment requires all of:

1. P1 `Δdet>0` with a 95% hospital-bootstrap interval excluding zero, and held-test detected-AKI log-loss gain over P0 with its interval excluding zero.
2. P1 does not worsen full-state Brier score by >0.01 and has detected-AKI calibration intercept between −0.05 and 0.05 and slope 0.8–1.2 on test hospitals after the locked validation recalibration.
3. J1 has positive held-test joint-log-score and positive-mark-log-score gains over J0, each with a 95% interval excluding zero; its `Δdet` agrees in direction with P1.
4. The J equalized-process diagnostic that freezes testing and exit at J0 retains a positive `Δdet` with a 95% interval excluding zero. Thus a burden signal in test intensity or retention may coexist, but cannot be the only modeled path.
5. Direction persists under fixed-hour-72 testing, inverse-observation weighting with adequate overlap/effective sample size, ≥90%-coverage/boundary support, D1 exposure, artifact exclusion, within/equal-hospital analyses, X bounds, and removal of the most influential hospital.

Evidence for the ascertainment rival is a positive later-tested burden contrast accompanied by no opportunity-cohort P1 improvement, no J1 positive-mark improvement, and a positive J1 test-intensity or retention component with interval excluding zero. This would show that the apparent signal is concentrated in observation opportunity under the fitted models; it would not prove biological absence of association.

Adverse evidence against clinically meaningful incremental burden information is either (a) upper 95% bounds ≤+1 absolute risk point for both P1 `Δdet` and the J equalized-process `Δdet`, together with no held-test detected-AKI or positive-mark log-loss gain, or (b) a stable reverse association across hospitals and ascertainment sensitivities. It argues against promoting monitored burden beyond nadir for this detected endpoint, not that hypotension is harmless.

The result is inconclusive if intervals include both zero and +1 point; P and J disagree in direction; test/mark/exit calibration fails; common support or observation-weight effective sample size is inadequate; any partition has fewer than 100 detections; unknown exit exceeds 0.5%; hospital influence dominates; results reverse under D1, fixed testing, boundary support, interval-width, or X bounds; or a positive complete-case result disappears without a stable ascertainment decomposition. An imprecise null is not adverse evidence.

Support establishes only transportable incremental prognostic information for *detected creatinine AKI under eICU testing and retention practices*. It does not establish biological AKI incidence, a renal-perfusion mechanism, causality, benefit from raising MAP, an optimal threshold, or a vasopressor effect. Stronger claims require pre-ICU renal baselines, reliable urine output and RRT timing, post-ICU labs, fluids/cardiac output/nephrotoxins, line/device validation, clinical adjudication of AKI cause, external validation, and ultimately prospective study.

## Solver outputs, resources, and verifier boundary

Required outputs are: immutable source/header/hash manifest; frozen person and hospital-split manifest; cohort and exclusion flow; MAP bin/boundary/gap/pressor audit; creatinine unit/duplicate/pair audit; exact event ledger with U/N/A/L/D/X transitions; split-level state and support counts; P0/P1/O0/O1/J0/J1 fitted objects and formula/penalty manifests; held predictions; state occupancy and cumulative-incidence tables; component and joint scores; standardized contrasts; common-support and weight diagnostics; 1,000-replicate hospital bootstrap file; sensitivity grid; hospital-influence report; and a claim ledger mapping every conclusion to cells and uncertainty. Checkpoints are required every 50 bootstrap fits.

Planned solver budget is 16 CPUs, 128 GiB RAM, no GPU, and at most 7.5 hours in the configured 16-CPU/262,144-MiB/28,800-second envelope. This is an unverified full-study estimate; the measured inherited exposure diagnostic used 12 CPUs, 64 GiB, no GPU, and 106.75 seconds. CPU is appropriate for approximately 11,000 people, a modest event ledger, penalized multinomial/marked-process models, and parallel hospital bootstraps. GPU use would not resolve outcome ascertainment and adds no current computational advantage.

An automatic verifier can check source hashes/headers, one-person selection, keys, half-open exposure bins, strict post-1,440 outcome times, pair windows, tie precedence, state transitions, split isolation, no future leakage, model formulas, full-refit bootstrap, metrics, gates, and whether conclusions match computed outputs. Fixtures must include: supportive burden and mark information; later-tested support caused only by testing/retention; precise adverse results; imprecise null; P/J disagreement; unknown-exit overflow; and correct computations paired with unsupported causal or latent-AKI conclusions.

A verifier cannot establish true arterial-line presence, pressure in undocumented intervals, whether missing tests conceal AKI, AKI etiology, clinical intent, causal treatment effects, or actionability. These require clinician review, missing evidence, or another study. Readiness checks packaging and bounded probes only; no reference solution is required and readiness is not scientific completion.

## Alternatives and demonstration dispositions

The transparent P path and ordered J path are specified at matched detail on the same records and target. P is the smallest interpretable check and exposes the observable competing outcomes. J preserves test order and factorizes the selection process that P loses. J is selected as the substantive alternative because the uncertainty is about detection opportunity, not because complexity is intrinsically valuable. A TCN and latent-AKI imputation are explicitly deferred for the evidence-based reasons above.

The shared methods-and-compute guide and demonstration manifest were inspected. Delphi supports asking whether order adds information but does not prescribe a transformer; the marked process is the smaller adaptation. ALADYNOULLI shows that fitted longitudinal structure should be compared against a transparent same-question baseline, but no genetic or GP reproduction is claimed. Oncoformer's main article and full STAR Methods remain unavailable in the bundle; only its general ablation discipline is relevant, and no claim is based on unavailable text.

## Exactly three reinspected key works

[K1] Schuurmans J, van Rossem BTB, Rellum SR, et al. *Hypotension during intensive care stay and mortality and morbidity: a systematic review and meta-analysis.* Intensive Care Medicine. 2024;50:516–525. doi:10.1007/s00134-023-07304-4.

[K2] Poukkanen M, Wilkman E, Vaara ST, et al.; FINNAKI Study Group. *Hemodynamic variables and progression of acute kidney injury in critically ill patients with severe sepsis: data from the prospective observational FINNAKI study.* Critical Care. 2013;17:R295. doi:10.1186/cc13161.

[K3] Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. *Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1).* Critical Care. 2013;17:204. doi:10.1186/cc11454.

All three works were re-inspected through frozen Europe PMC full-text XML. The attached UTF-8 files are accurately labeled provider excerpts, not complete XML. K1 supports the heterogeneity and nonconfirmatory pooled-AKI opening; K2 supports but narrowly bounds first-day MAP–AKI evidence; K3 supports the timed criteria and directly bounds creatinine-only ascertainment. None establishes this hypothesis.
