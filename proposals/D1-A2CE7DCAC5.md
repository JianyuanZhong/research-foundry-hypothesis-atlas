> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 4 branch: temporal hypotension signal versus care-process artifacts

Status: proposed substantive child of [prior hypothesis]. No cohort scan, label fit, model fit, or result has been computed. This branch preserves the selected eICU question and adds a discriminating temporal/process design; it is not a reproduction of any cited paper.

## Scientific opening, claim, and clinical importance

The unresolved question is whether cumulative systemic hypotension duration carries prognostic information for subsequent creatinine-defined AKI beyond minimum MAP. A residual duration association could still be an artifact of when clinicians measure, how they respond, or how sick patients are at ICU entry. Conversely, a duration signal that is temporally ordered, fixed-nadir, density-robust, and transportable would be useful as a prognostic summary for monitoring and for stratifying a future BP-management study.

H1: in adult first ICU stays that pass BP and creatinine ascertainment gates, covered minutes with systemic MAP <65 during ICU minutes 0–360 add held-out prognostic information for a first creatinine rise during minutes 360–2880 beyond nadir MAP, early physiologic severity, baseline creatinine, and observation-process features; the information has a forward-lag pattern and is not explained by recorded infusion response or hospital-specific practice.

This is not a claim that MAP <65 causes renal injury, that 65 mmHg is a treatment target, that vasopressors help or harm, or that the variable identifies a renal mechanism. The strongest inspected evidence supports narrower premises: hypotension duration/trajectory summaries can be associated with complications in a selected perioperative cohort [K1]; creatinine changes are relevant to AKI definitions [K2]; and randomized BP-target evidence cautions against converting an observational MAP association into a treatment claim [K3]. The unresolved claim is incremental, temporally ordered, transportable prognostic information in eICU after explicit process and treatment diagnostics.

The leading explanation is cumulative hemodynamic stress. The strongest rivals are (1) severity/selection, where duration summarizes unmeasured shock or baseline kidney vulnerability; (2) observation density, where sicker patients are measured more often and both exposure and outcome become easier to observe; (3) treatment response, where low MAP prompts recorded pressor starts; and (4) measurement/timing artifacts from five-minute monitor summaries, modality substitution, lab ordering, and discharge processes. The design can separate these as prognostic/process explanations only. It cannot establish renal hypoperfusion or a causal treatment effect.

## Scientific deliverable

The solver must newly produce a frozen cohort flow and label-readiness audit; held-out predictions and calibrated estimates for B0, B1, and M; a lagged duration table; hospital-cluster uncertainty; fixed-nadir curves; process, treatment, density, modality, threshold, and negative-control outputs; and a decision table classifying results as supportive, adverse, or inconclusive. Readiness or an observed association is not completion. Completion requires all three fits and their falsification outputs, or an explicit label/process stop report that prevents fitting.

## Population, boundaries, joins, and censoring

Use only the read-only eICU 2.0 snapshot [source checksum] and catalog [source checksum]. The catalog is datasets/eicu/README.md, with full metadata in datasets/eicu/metadata.json and relevant schemas in datasets/eicu/table-*.json. The source directory is [internal dataset path] database/EICU 2.0 data/. Source archives are gzip files with ordinary CSV members.

Join only on patientunitstayid; use uniquepid only to select the first ICU stay and keep all stays for one uniquepid in one split. Select lowest unitvisitnumber, then earliest unitadmittime24 as tie-break. Adults are numeric age >=18; preserve the >89 category and run a documented age-90 sensitivity. ICU admission is time zero; offsets are minutes relative to admission. There is no unitadmitoffset field.

Eligibility at minute 360 is survival/in-ICU observation through 360, at least 12 valid five-minute BP bins, at least 240 minutes between first and last covered bin, and a valid pre-index serum-creatinine baseline in -24–0. These are exclusions, not imputed negatives.

The primary grid is 72 five-minute bins. Prefer valid vitalPeriodic.systemicmean; if absent use vitalAperiodic.noninvasivemean and retain modality. Do not average modalities and do not use vitalPeriodic.pamean, which is pulmonary-artery mean. Reject MAP outside 30–180 mmHg (20–200 sensitivity), do not interpolate gaps over 10 minutes, and treat absence as missing. Exposure is covered minutes with MAP <65, retaining low-time fraction, nadir, area below 65, episode count, first-low offset, recovery slope, covered count, median gap, modality mix, and missingness. Threshold sensitivities are 60 and 70.

Primary outcome is the first accepted numeric serum-creatinine result in 360–2880 at least 0.3 mg/dL above the last accepted baseline result in -24–0. Deduplicate same clinical labresultoffset by latest labresultrevisedoffset. Accept only after a frozen audit of labname, labmeasurenamesystem, and labmeasurenameinterface. lab.csv has no units column: never silently convert. If vocabulary or scale is not reproducible, stop the primary fit and report label-readiness failure. Do not parse labresulttext, substitute BUN, or use apacheApsVar.creatinine as a timed outcome. A 1.5-times-baseline/7-day endpoint is a distinct sensitivity, not automatically full KDIGO AKI.

Death before 2880 after eligibility is a competing event. ICU discharge/transfer before 2880 without AKI is censoring, not a negative. A negative requires adequate ascertainment, including an accepted creatinine at or after 2880; otherwise censor. Use patient.unitdischargeoffset, unitdischargestatus, and unitdischargelocation for follow-up status. Fit cause-specific discrete-time and inverse-probability-of-censoring/observation sensitivities, and report event, competing, censoring, and unclassified counts. carePlanEOL is a process flag, not evidence of intent.

## Exact source bindings

All bindings use the cataloged source path, archive member, table, key, time field, and SHA-256 below.

- patient.csv.gz / table patient / member patient.csv / [source checksum]. Key patientunitstayid; grouping uniquepid; fields hospitalid, age, gender, ethnicity, unitadmittime24, unitvisitnumber, unitdischargeoffset, unitdischargestatus, unitdischargelocation, unittype, unitstaytype.
- vitalPeriodic.csv.gz / table vitalPeriodic / member vitalPeriodic.csv / [source checksum]. Key patientunitstayid; time observationoffset; fields systemicmean, systemicsystolic, systemicdiastolic, heartrate, respiration; exclude pamean.
- vitalAperiodic.csv.gz / table vitalAperiodic / member vitalAperiodic.csv / [source checksum]. Key patientunitstayid; time observationoffset; fields noninvasivemean, noninvasivesystolic, noninvasivediastolic.
- lab.csv.gz / table lab / member lab.csv / [source checksum]. Key patientunitstayid; times labresultoffset and labresultrevisedoffset; fields labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface.
- infusionDrug.csv.gz / table infusionDrug / member infusionDrug.csv / [source checksum]. Key patientunitstayid; time infusionoffset; fields drugname, drugrate, infusionrate, drugamount, volumeoffluid, patientweight.
- hospital.csv.gz / table hospital / member hospital.csv / [source checksum]. Key hospitalid; fields numbedscategory, teachingstatus, region.
- carePlanEOL.csv.gz / table carePlanEOL / member carePlanEOL.csv / SHA-256 [source checksum]. Key patientunitstayid; times cpleolsaveoffset and cpleoldiscussionoffset; field activeupondischarge.
- apacheApsVar.csv.gz / table apacheApsVar / member apacheApsVar.csv / [source checksum]. Key patientunitstayid; fields creatinine, dialysis, urine, meanbp, heartrate, vent, intubated. No time field: adjustment sensitivity only.
- intakeOutput.csv.gz / table intakeOutput / member intakeOutput.csv / [source checksum]. Key patientunitstayid; times intakeoutputoffset and intakeoutputentryoffset; fields outputtotal, dialysistotal, nettotal, cellpath, celllabel, cellvaluenumeric, cellvaluetext. Use only after label/unit/timing adjudication.

The eICU metadata records vitalPeriodic as five-minute summary observations, not raw waveforms, and public narrative notes are removed. Thus raw-waveform and clinician-intent conclusions are unavailable.

## Discriminating experiment

B0 is regularized logistic/discrete-time cause-specific regression for the same target using baseline creatinine, age, gender, ethnicity, hospital/ICU type, initial and terminal observed HR/respiration/MAP summaries, nadir MAP, BP modality, covered count, median gap, BP missingness, and pre-index creatinine/BP observation counts. It excludes duration and all post-index fields.

B1 adds covered MAP<65 duration, low-time fraction, episode count, first-low offset, recovery slope, and a restricted duration spline, interpreted within fixed-nadir bands. The primary estimand is held-out incremental Brier score, log loss, and calibration intercept/slope; AUROC/AUPRC are secondary. This is a descriptive prognostic association, not a treatment estimate.

Predefine exposure subwindows 0–120, 120–240, and 240–360 and future outcome intervals 360–720, 720–1440, and 1440–2880. Fit the same cause-specific model with subwindow low-minute terms and time-appropriate censoring weights. A temporal pattern must be forward-lagged, coherent across prespecified intervals, survive fixed-nadir adjustment, and not reduce to terminal coverage or last-bin variables. Near-event-only association favors impending care/measurement processes.

Fit a process-only model using coverage, gaps, modality, missingness, pre-index lab/BP counts, hospital/ICU type, and early HR/respiration, but no MAP duration or nadir. Repeat B0/B1 after common-density thinning, systemic/noninvasive stratification, and thresholds 60/65/70. Freeze a pre-index negative-control outcome: among stays with valid creatinine in -48–24 and a distinct result in -24–0, apply the same +0.3 rule. The 0–360 exposure cannot temporally precede it; a strong association is adverse evidence for severity, selection, or measurement.

For a broken-linkage null, within hospital × nadir-MAP band × coverage stratum reassign complete 0–360 trajectories between stays while outcomes and B0 covariates remain fixed. Duration association and incremental performance should disappear. This is a falsification test, not a clinical effect estimate.

From infusionDrug, freeze a lower-case name map before fitting for norepinephrine/noradrenaline, epinephrine, phenylephrine, vasopressin, and dopamine. Because there is no end time or verified dose/unit field, derive only pressor-start-in-bin, pressor-seen-before-bin, and a name-audit count; do not infer active exposure or dose response. Compare treatment-masked B0/B1/M (primary), treatment-inclusive B1/M, a pressor-only/process model, and a descriptive table of low-MAP bins followed by a pressor start within 30 minutes. Loss after the recorded treatment proxy or near-total co-location is compatible with response/severity and cannot be called an independent hypotension signal. Persistence weakens, but does not eliminate, the rival.

## Learned alternative, compute, split, and uncertainty

M is a small temporal convolution or one-layer GRU over the same 72 bins: systemic/noninvasive MAP, HR, respiration, modality, observation mask, time-since-last-observation, frozen pressor indicators, and B0 variables. Treatment-masked M is primary; treatment-inclusive and coverage-only variants are ablations. Fit on training hospitals, early-stop/calibrate on validation hospitals, and evaluate once on held-out hospitals.

M can reveal persistence, oscillation, recovery timing, and BP-treatment alignment that B1's scalar duration/nadir loses. Jointly rotate complete observed five-minute rows within a stay (values, masks, modality, treatment), preserving marginal burden and treatment count but breaking order. Compare original and rotated M on held-out hospitals and refit a predeclared rotated sensitivity. Equal performance indicates process/distribution information rather than temporal ordering. B1 remains preferred if stable and M adds no reproducible ordering information; M matters only if its stable pattern changes the scientific duration summary, not because of a small score gain.

Use whole-hospital 60/20/20 train/validation/test assignment; every uniquepid stays in one split. If hospital count is unstable, use prespecified repeated grouped-hospital cross-validation and state the limitation. Fit maps, scalers, regularization, model selection, and calibration without test information. Use hospital-cluster bootstrap intervals, report hospital/patient counts per replicate, and report held-out ΔBrier, Δlog loss, calibration, fixed-nadir curves, time-specific risks, and hospital heterogeneity.

Tabular fits should use CPU. GPU is optional only for a measured sequence bottleneck; with allocation use cuda:0 and never infer GPU absence from ordinary shell. The future solver envelope is 16 CPU, up to 8 GPU, 262144 MiB, and 28800 seconds; these are planning limits, not measured discovery results.

## Falsification and interpretation

Support requires label readiness; B1 held-out improvement over B0 with hospital-cluster uncertainty excluding no improvement; a coherent forward-lag/fixed-nadir pattern; persistence after density, modality, threshold, process, and treatment diagnostics; no material pre-index negative-control association; broken-linkage null behavior; and reproducible ordered information from M beyond its rotated counterpart. This supports only a transportable prognostic summary.

Adverse results include label failure, null/non-monotone duration, process-only or pre-index-control performance comparable to B1, loss under density thinning or hospital holdout, a last-interval-only signal, disappearance after recorded-treatment adjustment, pressor co-location, or no original-versus-rotated M difference. These favor severity, observation, treatment-response, or non-temporal explanations.

Inconclusive results include wide hospital intervals, too few hospitals, inadequate creatinine ascertainment, exposure-dependent censoring, unstable vocabulary/scale, or unresolved B1/M disagreement. An imprecise null does not refute H1. The next step is label adjudication, external validation, better treatment/urine semantics, or a narrower descriptive BP-process study.

## Limits, alternatives, and references

Unavailable essentials are clinician-adjudicated AKI, reliable pre-ICU kidney function, verified lab units, raw arterial waveforms, complete fluid balance, pressor stop times/dose units/indications, renal-replacement indication and intent, staffing/bed context, and independent external validation. apacheApsVar cannot supply a time-aligned creatinine or dialysis event; intakeOutput cannot supply urine/dialysis meaning without adjudication. Critical-care/nephrology review is required before a KDIGO-concordant label or treatment-sensitive interpretation. Causal claims require a target-trial or prospective study.

The three inspected works attached to this child are: [K1] Ren Y, Liu C, Wang X, Zhang M, Li H. Intraoperative hypotension trajectories and their predictive value for major postoperative complications: a retrospective cohort study (2025; inspected full-text HTML passages); [K2] Miyamoto Y, Sugawara Y, Oshima M, Nagasu H, Kuwabara T, Sofue T, Nakagawa N, Iwagami M. Review no. 3: handling of longitudinal creatinine data to define acute kidney injury (2026; abstract-only inspection); [K3] Yoshimoto H, Fukui S, Higashio K, Endo A, Takasu A, Yamakawa K. Optimal target blood pressure in critically ill adult patients with vasodilatory shock: A systematic review and meta-analysis (2022; abstract-only inspection). K1 supports the temporal-duration opening; K2 bounds creatinine/urine endpoint interpretation; K3 bounds treatment-target interpretation. These works do not establish the eICU label, causality, mechanism, or transportability. No unavailable paper text or supplement is claimed.

A pure duration/nadir regression is insufficient because it cannot distinguish the assigned artifacts. A large transformer, latent trajectory classes, and a renal state-space model are deferred because they add capacity or untestable structure without available waveform, perfusion, congestion, biomarker, urine, or renal-adjudication inputs. A causal vasopressor analysis is deferred because infusion rows lack end times, verified dose units, indications, and treatment assignment. Revisit only if a small M shows reproducible held-out temporal ordering or if those missing clinical dependencies are supplied.
