> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Residual instability at live ICU discharge: association first, sequence increment second

## Scientific deliverable

The future Harbor solver must newly construct a leakage-controlled cohort of live ICU discharges, estimate one prespecified association between a late-instability index and a timed 48-hour outcome, and then test a distinct secondary claim: whether chronological organization of the same pre-discharge measurements adds validated prognostic information beyond an order-blind aggregate baseline. Completion requires the cohort and label audit, feature provenance, the primary association estimate with uncertainty, matched baseline/GRU held-out predictions, calibration and discrimination outputs, the chronology-shuffle and missingness falsifications, and an interpretation tied to those outputs. Readiness or a favorable result is not completion.

This is a substantive child of the selected valid proposal `[prior hypothesis]`. It preserves the question and verified MIMIC-IV 3.1 bindings while making the association estimand and sequence-increment estimand separate. It does not claim to reproduce a demonstration paper or to have computed results.

## Unresolved question and evidence boundary

The clinically important question is whether a patient who is being transferred out of the ICU, but has persistently abnormal measurable physiology in the preceding 12 hours, represents a group needing additional review or monitoring. The primary hypothesis is an association hypothesis:

> Among minimally measurable, live ICU discharges, a higher prespecified 12-hour numeric late-instability index is associated with a higher probability of first ICU readmission or timed in-hospital death within 48 hours of ICU outtime, after adjustment for admission/ICU context and observation coverage.

The secondary, non-causal sequence hypothesis is:

> Using the same pre-outtime numeric and interval-support inputs, a chronological masked GRU has better held-out probabilistic accuracy and calibration than an order-blind aggregate logistic baseline; its advantage should attenuate when the order of preterminal bins is shuffled while the terminal bin and each patient's measurements are preserved.

The available evidence supports only that this snapshot contains ICU-stay boundaries, admission outcomes, and timestamped structured observations, and that the selected item IDs have the audited labels/units recorded in the support note. The MIMIC-IV documentation describes internally consistent within-subject time shifts; it does not validate this phenotype. The expert seed proposes residual instability before ICU discharge but supplies no cutoff or result. The research-ambition methods guide supports considering a bounded learned sequence adaptation, not its clinical value here. Neither source establishes preventability, discharge error, causal benefit, or sequence superiority. Those are the unresolved claims.

## Population, index and temporal boundaries

The source unit is an ICU stay linked to a hospital admission.

1. Read every `icu/icustays` row with non-null `subject_id, hadm_id, stay_id, intime, outtime`. Reject `outtime<=intime` and rows without a matching `hosp/admissions` record.
2. Define a live ICU discharge as `outtime < admissions.dischtime` and (`deathtime` is null or `deathtime > outtime`). The first eligible live discharge per `(subject_id,hadm_id)`, ordered by `outtime`, is the primary index. This prevents multiple ICU discharges in one admission from acting as independent primary observations. Analyze all eligible discharges secondarily with subject-and-hospitalization clustered uncertainty.
3. Let `t0=icustays.outtime`. Use a closed feature window `[t0-12 hours,t0]), divided into twelve backward one-hour bins. Use `charttime` for charted observations and clipped `starttime/endtime` for intervals. `storetime` is never used for temporal ordering, feature inclusion, or a missingness proxy. No feature may have a clinical time after `t0`.
4. The primary analytic population is the eligible first live ICU-discharge cohort with at least four bins containing at least two observed core numeric channels. Report all eligible discharges, coverage exclusions, and the coverage distribution; this makes the target population explicit rather than silently treating absent charting as normal.

Subject-specific date shifts allow within-subject interval arithmetic but prohibit cross-subject calendar alignment. All patient-level splitting is by `subject_id`.

## Outcomes and competing events

The primary binary endpoint is the first event in `(t0,t0+48 hours]):

- ICU readmission: a later `icu/icustays` row with the same `subject_id,hadm_id`, a different `stay_id`, and `intime>t0`, with `intime<=t0+48h`;
- timed in-hospital death: `hosp/admissions.deathtime>t0`, `deathtime<=t0+48h`, and within the admission's discharge boundary when that boundary is available.

For a same-time tie, assign death as the first cause in the cause-specific analysis; the binary composite is unaffected. A `hospital_expire_flag=1` without a usable `deathtime` cannot be assigned to the timed 48-hour death component and is reported as an untimed-death data-quality count, not given an artificial event time.

Prespecified secondary outcomes are the analogous 7-day same-hospitalization composite, ICU readmission alone at 48 hours and 7 days, timed death at 48 hours and 7 days, and in-hospital death through `dischtime`. For the last endpoint, `hospital_expire_flag` may identify death when `deathtime` is missing, but it is label-only. Report mutually exclusive readmission-first, death-first, and no-event categories and cause-specific cumulative-incidence estimates; treat death as a competing event for readmission and alive hospital discharge as administrative censoring for the same-admission risk set. Do not call any endpoint preventable or use any endpoint field as a feature.

## Exact data bindings and provenance

All sources are read-only. The frozen MIMIC source is:

- ZIP: `[internal dataset path]`
- ZIP [source checksum]
- MIMIC snapshot: `[source checksum]`
- Full catalog: `[internal dataset path]`
- Catalog [source checksum]

The exact table names, archive members, columns, joins, item IDs, and read-only audit are in [support/mimic-residual-instability-successor-audit.md](support/mimic-residual-instability-successor-audit.md). The operative bindings are:

- Index: `icu/icustays`, member `mimic-iv-3.1/icu/icustays.csv.gz`; use `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`.
- Admission/labels: `hosp/admissions`, member `mimic-iv-3.1/hosp/admissions.csv.gz`; use `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admission_location,discharge_location,hospital_expire_flag`. `admittime, admission_type, admission_location` are context; `dischtime,deathtime,hospital_expire_flag,discharge_location` are eligibility/label-only.
- Demographics: `hosp/patients`, member `mimic-iv-3.1/hosp/patients.csv.gz`; use `subject_id,gender,anchor_age,anchor_year_group`. `dod` is prohibited.
- Physiology: `icu/chartevents`, member `mimic-iv-3.1/icu/chartevents.csv.gz`; use `subject_id,hadm_id,stay_id,charttime,itemid,value,valuenum,valueuom,warning`, joined by `stay_id`. `storetime` is excluded.
- Dictionary: `icu/d_items`, member `mimic-iv-3.1/icu/d_items.csv.gz`; use `itemid,label,linksto,unitname,param_type` to verify meaning and units.
- Interval support: `icu/inputevents`, member `mimic-iv-3.1/icu/inputevents.csv.gz`; use `subject_id,hadm_id,stay_id,starttime,endtime,itemid,amount,amountuom,rate,rateuom`, joined by `stay_id`. Clip intervals to the window; exclude `storetime` and `statusdescription` from features.
- Optional sensitivity labs: `hosp/labevents`, member `mimic-iv-3.1/hosp/labevents.csv.gz`, joined on `(subject_id,hadm_id)` using `charttime<=t0`; verify lactate `50813`, creatinine `50912`, bicarbonate `50882`, hemoglobin `51222`, platelet `51265`, and WBC `51300` through `hosp/d_labitems` (`itemid,label,fluid,category`). Labs are not in the primary feature set.
- Optional urine sensitivity: `icu/outputevents`, member `mimic-iv-3.1/icu/outputevents.csv.gz`; Foley `226559`, `charttime<=t0), with missingness retained. It cannot define the primary cohort or exposure.

The support note records read-only header checks for these members and dictionary rows: HR `220045`; MAP `220052,220181,225312`; RR `220210`; SpO2 `220277`; temperature Celsius `223762`; FiO2 `223835`; O2 flow `223834,227287`; PEEP `220339,224700); and vasoactive input items `221906,222315,221289,229617,221749,229630,229631,229632,221662,221653,221986`.

## Primary exposure and association estimand

For each one-hour bin, clean numeric values using `valuenum/valueuom` and fixed ranges: HR 20–250, MAP 20–200, RR 2–80, SpO2 50–100, temperature 30–43 °C, O2 flow 0–100 L/min, PEEP 0–40 cmH2O; convert FiO2 values above 1.5 by dividing by 100 and retain 0.21–1.00. Use arterial MAP first, then non-invasive MAP, then ART MAP within a bin, with deterministic duplicate-time handling.

Core channels are HR, MAP, RR, SpO2, temperature, FiO2, O2 flow, and PEEP. Their fixed abnormal flags are respectively HR <50 or >120; MAP <65; RR <8 or >24; SpO2 <92; temperature <36 or >=38.5 °C; FiO2 >0.40; O2 flow >=4 L/min; and PEEP >5 cmH2O. A valid bin has at least two observed core channels. The primary late-instability index `LII` is the mean across valid bins of the fraction of observed core channels flagged abnormal. It is defined only for the primary coverage population (at least four valid bins). Preserve channel-level missingness and valid-bin count.

The primary association estimand is the covariate-standardized risk difference:

`RD75-25 = mean_i[p(Y48=1 | LII=Q75,Z_i) - p(Y48=1 | LII=Q25,Z_i)]`

from one prespecified logistic association model with LII as a linear per-IQR term and `Z` consisting of age, gender, anchor-year-group, first/last ICU care unit, ICU duration known at `t0`, admission type/location, number of earlier ICU stays in the same hospitalization, valid-bin count, and core-channel observation coverage. Report the per-IQR odds ratio, standardized absolute risks, and `RD75-25`; robust standard errors are clustered by subject, with a subject-level bootstrap interval as a sensitivity analysis. A prespecified three-knot restricted cubic spline and quintile estimates assess monotonicity and nonlinearity; they do not replace the primary linear estimand. The association is observational and conditional on this adjustment set, not a causal effect or a discharge-policy effect.

A prespecified secondary exposure analysis adds pressor/inotrope presence and clipped minutes in the window, grouped by presence/duration rather than incomparable drug dose. It reports whether pressor support is associated with the outcome but cannot separate treatment indication from physiology. Lab and Foley additions are paired sensitivity analyses, not outcome-driven feature selection.

## Secondary sequence-increment estimand

Use the same primary analytic population, outcome, feature whitelist, and subject-level split for both models.

The order-blind aggregate baseline is penalized logistic regression. It includes the shared context variables above plus, for each of the eight core channels, last-bin value and mask, window mean/median/minimum/maximum/SD/IQR, abnormal-bin fraction, valid-bin count, and overall channel-observation count/missingness. It adds pressor presence and total overlap minutes. These summaries are order-invariant except for the explicitly retained terminal snapshot; it does not include slope, reversal count, bin IDs, post-`t0` fields, or any other order-sensitive summary. This is an auditable discharge-summary comparator, not a no-model control.

The learned alternative is a small masked GRU over the same twelve one-hour bins and the same eight numeric channels, per-bin masks, abnormal flags, valid-channel count, and clipped pressor minutes/presence. Numeric scaling, imputation constants, and all categorical encodings are learned on training data only. Use one sigmoid head for the 48-hour composite, hidden size 32 or 64 selected on validation data, fixed dropout grid, early stopping on validation Brier score, and five prespecified random seeds. No text-valued oxygen-device items, notes, radiology, transfers, future ICU stays, labels, or admission outcome fields enter either model.

The secondary sequence-increment estimand is `DeltaBrier = Brier(GRU)-Brier(aggregate)` on the untouched test partition, with lower values favorable. Report paired differences in Brier score, calibration intercept/slope, AUROC, and AUPRC; Brier/calibration are primary for this comparison because the intended use is risk estimation rather than ranking alone. A last-bin-only logistic model is an additional descriptive comparator. The GRU's scientific value is the ability to represent persistence, recovery, fluctuations, and coupled channel ordering that the aggregate summaries discard; model complexity or a tiny predictive gain is not itself a clinical advance.

The key falsification ablation shuffles bins 1–11 within each test patient while holding the terminal bin fixed, preserving that patient's values, masks, and support totals. A secondary all-12-bin shuffle is reported with its changed terminal state explicitly acknowledged. If the GRU advantage is specifically temporal, its favorable `DeltaBrier` should attenuate under the preterminal shuffle and should not be recreated by a missingness-only model. Fit a mask-ablated GRU with the same imputation and architecture as a diagnostic for documentation-process learning; it is not a replacement primary model.

## Split, uncertainty and analysis plan

Freeze one deterministic 70/15/15 train/validation/test split by `subject_id`, approximately stratified on the primary composite after subject-level assignment; retain all stays from a subject in one partition. Fit preprocessing, association-model regularization, GRU hyperparameters, calibration maps, and any operating thresholds using training/validation data only. The primary association fit is prespecified and may use the full primary cohort because it is an estimand analysis rather than a tuned held-out predictor; no result is used to choose the exposure or endpoint.

For the association model, report 95% subject-cluster bootstrap intervals for LII contrasts, odds ratios, predicted risks, and spline curves; compare coverage-restricted and complete-case analyses, and a model with missingness/coverage terms removed. For the baseline/GRU, average the five seed predictions within each patient, then compute test metrics. Use 2,000 subject-level paired bootstrap replicates (or the largest prespecified number feasible within the execution limit) for metric intervals and `DeltaBrier`; report the exact number actually completed. Calibration plots use held-out predictions and bootstrap bands. Secondary endpoints, subgroups (first/last ICU care unit and respiratory-support proxy strata), and sensitivity features are labeled exploratory and do not redefine the primary claim.

The primary association is supportive only if the LII risk contrast is positive with an interval excluding zero, the prespecified spline is not materially inconsistent with monotonicity, and the direction is not explained solely by coverage or the minimum-four-bin restriction. The sequence hypothesis is supportive only if the GRU has a favorable held-out Brier/calibration increment over the matched aggregate baseline, with an interval excluding zero, no clinically important calibration worsening, and attenuation under preterminal order shuffling. Report the full estimates even if they do not meet these decision rules; no universal clinical threshold is asserted from this retrospective dataset. A statistically detectable but very small metric difference is not evidence of clinical utility.

## Falsification and interpretation

Adverse association evidence is a null or reversed LII gradient, a relationship that disappears after coverage/missingness adjustment, or instability confined to a care-unit/documentation stratum. Adverse sequence evidence is no reproducible increment over the aggregate baseline, a gain that persists after order shuffling, a gain that disappears when missingness masks are removed, or worse calibration despite better ranking. Such results would support the narrower conclusion that terminal status, documentation intensity, or treatment selection—not recoverable temporal physiology—contains the reproducible signal.

Results are inconclusive when timed death linkage is materially incomplete, event counts or coverage are too low for useful intervals, preprocessing/unit checks fail, calibration is unstable, or sensitivity analyses are too discordant to identify the information source. Inconclusive is not confirmation or refutation.

Computationally checkable claims are the source/member/column/item provenance, cohort counts, coverage exclusions, exact time filters, absence of prohibited fields, outcome linkage, split integrity, fitted model specifications, held-out predictions, metric/uncertainty calculations, and the observed effect of order shuffling. The data cannot establish whether a discharge was inappropriate, whether readmission/death was preventable, whether delaying transfer or adding monitoring would improve outcomes, why support was prescribed, whether charted oxygen variables reflect delivered physiology, or whether the result transports beyond this single-center snapshot. Those claims require clinician adjudication of discharge readiness and preventability, treatment/goals-of-care and operational context, prospective validation, and an external hospital cohort or intervention study. Raw waveforms and images are unavailable; the separate note sources exist but are deliberately excluded from this structured experiment.

## Alternatives and selection record

- Selected primary analysis: penalized/regularized logistic association model with a prespecified LII and standardized risk contrast. It is auditable and clinically interpretable, and it answers the association question without pretending to estimate a treatment effect.
- Selected secondary alternative: masked GRU on the same 12-bin numeric/interval inputs and split. It can reveal persistence and order that final-state plus order-blind summaries lose; its selection is justified by the explicit sequence hypothesis, not by neural-network novelty or a leaderboard target.
- Deferred Transformer/Delphi-style token sequence: the inspected methods guide documents a learned dated-history adaptation, but this 12-bin numeric window does not provide a verified longer-range scientific target. Reconsider only if the GRU/order test is positive, event/coverage support a more flexible model, and a new longer-range estimand is specified.
- Deferred mechanistic hidden-state/recovery model: no clinician-adjudicated stable/improving/deteriorating labels or validated oxygen-support ontology are available. Reconsider after expert ontology and adjudication; do not invent states from outcomes.
- Excluded narrative model: discharge and radiology notes can encode disposition, retrospective summaries, or other downstream information. A note-based question would need a separate timing/content adjudication and is not part of this experiment.
- Excluded downstream covariate analyses: `discharge_location`, `transfers`, `hospital_expire_flag`, death fields, later ICU stays, notes, and `dod` are not “sensitivity covariates”; they are prohibited from the feature matrix. This is the principal leakage repair.

## Compute, checkpoints and solver outputs

The current `inputs.json` gives a discovery science budget of 7,200 seconds and describes an 8-GPU A100 deployment; ordinary shells have no GPU allocation. No discovery model fit is claimed here. The compact logistic models and 12-bin GRU are expected to be CPU-feasible after chunked extraction. A future solver may request one allocated GPU for repeated GRU fits if measured runtime warrants it; GPU use is optional, and inside an allocation the model/tensors must explicitly use `cuda:0`. The parent planning record proposed up to 16 CPUs, 262,144 MiB, 8 GPUs, and 28,800 seconds for the future solver; those planning values are retained as unverified estimates because the current `inputs.json` does not expose a separate solver-planning field.

Checkpoint: frozen split; source/item manifest; cohort inclusion counts; feature table; preprocessing state; association fit; each GRU seed/model state; held-out predictions; bootstrap state; and interpretation audit. Required final files include a machine-readable cohort/label/coverage/leakage report, association estimates and curves, baseline/GRU configurations and coefficients where applicable, predictions, metrics with intervals, shuffle/mask ablations, endpoint and subgroup sensitivity tables, and a limitations report. The verifier can check these outputs and whether conclusions follow from them; it cannot adjudicate preventability or clinical benefit.

## Provenance and availability limitations

The dataset README, full local catalog, MIMIC table JSONs, read-only archive headers/dictionary rows, MIMIC-IV documentation material, expert seed card, and the research-ambition README/methods guide were inspected. The three demonstrations were used only to calibrate methodological ambition and bounded adaptation. The main cancer article and complete STAR Methods remain unavailable in the reference bundle and are not represented as read. No reproduction or external-validation claim is made. The exact source audit and measured-versus-unverified distinctions are preserved in [support/mimic-residual-instability-successor-audit.md](support/mimic-residual-instability-successor-audit.md).
