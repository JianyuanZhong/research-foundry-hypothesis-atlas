> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Coverage-gated prognostic meaning of persistent hyperlactatemia under improving versus worsening measured perfusion

## Selection-ready scientific deliverable

The future Harbor solver must newly fit and audit a leakage-controlled, competing-risk study of whether the prognostic association of persistent hyperlactatemia changes with the direction of measured systemic perfusion immediately before an observed live ICU exit.

Completion requires:

1. an all-eligible cohort flow and a separately reported, pre-specified coverage-complete cohort;
2. a machine-readable gate report produced before model fitting, containing schema/dictionary validity, clinical-plus-recording-time coverage, measurement-process balance, phenotype-cell counts, and event support;
3. the primary lactate-by-perfusion interaction and standardized 48-hour cumulative-incidence contrasts with subject-bootstrap uncertainty, or an explicit “not estimable” result if the gate fails;
4. matched held-out B0, B1, Bmask and Bdisc predictions, plus the deferred training-only M2 sensitivity, all on the same phenotype-complete population and subject split;
5. row-level provenance for every retained measurement and exact archive/member/item/unit/timing audits;
6. measurement-process, selection, timing, modality, endpoint and permutation falsifications; and
7. a claim ledger linking each conclusion to computed outputs and distinguishing prognostic association from microcirculatory diagnosis, fluid response, treatment effect, discharge appropriateness, utility and transportability.

This proposal contains no clinical result. Discovery coverage counts, if present in the supporting audit, are feasibility evidence only.

## Unresolved question and evidence boundary

The expert seed (mimic-04) proposes that persistently high lactate can have different meanings when perfusion is improving versus worsening, while explicitly warning that repeated measurements are selective and that these proxies cannot diagnose microcirculatory dysfunction. The local MIMIC documentation establishes source schemas and within-person timestamp conventions; it does not establish phenotype prevalence, event support, measurement exchangeability, or clinical validity. The inspected research-ambition demonstrations support considering structured longitudinal learning and latent-trajectory adaptations, but do not establish this MIMIC hypothesis; the cancer main article and full STAR Methods remain unavailable and are not used as evidence.

The strongest evidence-supported claim is only that these structured MIMIC-IV fields are available to construct candidate, pre-landmark trajectories. The unresolved claim is:

> Among first eligible live ICU exits with adequate, pre-landmark repeated lactate and paired perfusion coverage, is the excess 48-hour risk associated with persistent hyperlactatemia smaller when measured perfusion is improving than when it is worsening?

Primary estimand, reported as a risk-difference interaction at 48 hours:

`[CIF(R/D | persistent, improving) - CIF(R/D | nonpersistent, improving)] - [CIF(R/D | persistent, worsening) - CIF(R/D | nonpersistent, worsening)]`.

The directional hypothesis is negative. The primary clinically meaningful null region is [-2,+2] percentage points; a negative estimate inside this region is not supportive evidence.

A supportive result could justify a future prospective study that stratifies lactate interpretation by measured perfusion direction. It would not justify a fluid protocol, a discharge policy, a diagnosis of microcirculatory failure, or a claim that the association is causal. A null or adverse result would argue against adding this distinction to retrospective prognostic stratification. A gate failure is inconclusive about the biology, not evidence against it.

## Population, landmark and outcomes

Use one index per `hadm_id): the first `icu/icustays` row with valid `intime < outtime`, an observed live ICU exit at `t0=outtime`, and a complete 12-hour pre-landmark window. Set `tL=t0-1 hour` and require `intime <= tL-12 hours`. Exclude reversed/missing ICU intervals and exits with `admissions.deathtime <= t0`. Admissions without a matching admission row are linkage failures and remain in the flow. A `hospital_expire_flag=1` with missing `deathtime` is an unresolved death-ascertainment category: retain it in flow and exclude it from the timed primary analysis unless an adverse U-bound is separately reported.

Primary features use [tL-12h,tL], split into [tL-12h,tL-6h] and (tL-6h,tL]. A charted row is available only when both its clinical and recording timestamps are <= tL. A vasoactive interval requires valid `starttime/endtime`, `storetime <= tL`, and is clipped at tL; no end time after tL contributes. No feature may use `outtime`, ICU LOS, future transfers, a stay-end field, endpoint fields, notes, or any row after tL. Chart-time-only is a fixed sensitivity, not the primary analysis.

First mutually exclusive transition in (t0,t0+48h]:

- R: a different `stay_id` in the same `hadm_id`, with `intime > t0` and <= t0+48h;
- D: `admissions.deathtime` in the interval;
- S: alive `dischtime` in the interval before R or D, treated as an ascertainment/observation-boundary transition;
- N: no R, D or S while the admission is ascertainable through 48 hours;
- U: unresolved timed-death ascertainment, never silently relabeled N.

D precedes R at equal times. Report R, D, S, R/D and N with cause-specific hazards and 48-hour CIFs; 7-day and complete-ascertainment sensitivities and adverse/non-adverse U bounds are required. The primary model treats S as competing with R/D.

## Predeclared coverage and event-support gate

The gate is frozen before any outcome-based threshold, model comparison, interaction estimate, or sensitivity selection. It is not allowed to change the population, merge cells, relax timestamps, or choose a different cutoff after seeing outcomes or model performance.

The solver must emit counts for every stage:

`all eligible -> clinically timed complete -> lactate in both halves -> MAP in both halves -> pressor support in both halves -> primary phenotype complete -> each of four primary cells -> R/D events by cell`.

Gate G1, source validity, passes only if every required dictionary item is present, has the expected `linksto`, and has a compatible documented unit/field; rejected or unconvertible rows are counted. G1 also requires non-ambiguous joins, valid timestamps, interval clipping, duplicate handling, and no prohibited feature columns.

Gate G2, measurement-process adequacy, passes only if the primary cohort is defined by the dual clinical-plus-storetime rule, at least 200 eligible subjects are phenotype-complete, phenotype-complete subjects are at least 20% of all eligible live exits, and each of the four primary cells has at least 30 subjects. The solver must report, by cell and anchor-year group/current-unit stratum, the fraction with each domain observed in each half, number of measurements, time lag (storetime-charttime), chart-only additions, mixed MAP modality, and missingness indicators. A large chart-only expansion or a cell/unit with materially absent coverage is adverse to real-time interpretation even if G2 passes.

Gate G3, event support, passes only if each of the four cells has at least 10 observed 48-hour R/D events in the full phenotype-complete cohort before fitting. This is a fixed support safeguard, not an outcome-driven selection rule: the labels are counted once, before estimates, and cannot be used to redefine phenotype thresholds or retain favorable cells. If G1, G2 or G3 fails, the primary interaction is not estimable. The solver must still report the flow, coverage and event table, descriptive phenotype distributions, and the reason for failure; it must not replace the primary estimand with a pooled or post hoc alternative. The 30-subject/10-event thresholds are planning gates, not guarantees of narrow confidence intervals.

Within a passed gate, report any cell with fewer than 30 subjects, 10 R/D events, or fewer than 10 events of a component outcome as unsupported for that component. A wide interval, unstable calibration, poor overlap, or a failure of falsification can still make a gated analysis inconclusive.

## Phenotype

Persistent lactate requires valid lactate in each half, at least two valid results overall, and both half medians >=2.0 mmol/L after verifying units. A 4.0 mmol/L cutoff is a fixed sensitivity. Non-numeric values, incompatible units and unsupported conversions are rejected and counted; no held-out outcome selects thresholds.

Primary perfusion uses only predeclared measurements:

- MAP is the half-window median from `icu/chartevents` items 220052, 220181 and 225312, with dictionary `linksto`, labels and units verified. The primary change is late minus early MAP.
- Vasoactive support is minutes of valid overlap of `icu/inputevents` intervals for 221906, 222315, 221289, 229617, 221749, 229630, 229631, 229632, 221662, 221653 and 221986. This is support presence/duration, not dose or fluid responsiveness; rate units are not pooled.
- Improving requires MAP increase/nondecrease >=5 mmHg and late pressor minutes no greater than early.
- Worsening requires MAP decrease >=5 mmHg and late pressor minutes no less than early.
- All others are indeterminate, retained descriptively and never forced into either primary category.

The primary analysis requires at least one valid MAP and one valid pressor-support observation in each half. A sensitivity requires a single MAP modality (arterial 225312 or a fixed non-invasive item) in both halves; mixed modality is reported, not silently repaired. Foley corroboration is secondary: `icu/outputevents` item 226559, with output presence and log-volume sensitivities, and cannot rescue missing primary coverage.

Organ markers are secondary covariates/descriptors: ALT 50861, AST 50878, bilirubin 50885, creatinine 50912, bicarbonate 50882, hemoglobin 51222, platelets 51265 and WBC 51300. Values and testing indicators remain separate.

## Exact read-only source bindings

Source guide: `datasets/README.md`; MIMIC guide: `datasets/mimic/README.md`; full catalog: `[internal dataset path]`, [source checksum]. Snapshot: `[source checksum]`. Structured source is read-only archive `[internal dataset path]`, 10,551,747,784 bytes, [source checksum].

| Table; archive member | Required columns and use |
|---|---|
| `icu/icustays`; `mimic-iv-3.1/icu/icustays.csv.gz` | `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; join admissions on (subject_id,hadm_id); index/future R timing only. |
| `hosp/admissions`; `mimic-iv-3.1/hosp/admissions.csv.gz` | `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; context before tL; death/discharge only labels/eligibility. |
| `hosp/patients`; `mimic-iv-3.1/hosp/patients.csv.gz` | `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; join subject_id; use gender/age/year group; prohibit dod. |
| `icu/chartevents`; `mimic-iv-3.1/icu/chartevents.csv.gz` | `subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valuenum, valueuom, warning`; join stay_id; both times <=tL. |
| `icu/d_items`; `mimic-iv-3.1/icu/d_items.csv.gz` | `itemid, label, abbreviation, linksto, category, unitname, param_type, lownormalvalue, highnormalvalue`; verify MAP/pressor/Foley labels, units and linksto. |
| `icu/inputevents`; `mimic-iv-3.1/icu/inputevents.csv.gz` | `subject_id, hadm_id, stay_id, caregiver_id, starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom, orderid, linkorderid, ordercategoryname, secondaryordercategoryname, ordercomponenttypedescription, ordercategorydescription, patientweight, totalamount, totalamountuom, isopenbag, continueinnextdept, statusdescription, originalamount, originalrate`; clinical overlap clipped at tL; storetime<=tL. |
| `icu/outputevents`; `mimic-iv-3.1/icu/outputevents.csv.gz` | `subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom`; Foley 226559; both times <=tL. |
| `hosp/labevents`; `mimic-iv-3.1/hosp/labevents.csv.gz` | `labevent_id, subject_id, hadm_id, specimen_id, itemid, order_provider_id, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag, priority, comments`; join (subject_id,hadm_id); both times <=tL. |
| `hosp/d_labitems`; `mimic-iv-3.1/hosp/d_labitems.csv.gz` | `itemid, label, fluid, category`; verify lactate 50813 and organ-marker IDs. |
| `hosp/transfers`; `mimic-iv-3.1/hosp/transfers.csv.gz` | `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; use only intervals covering tL for descriptive current-unit audit. |

The four configured note tables remain accessible but are excluded; note text cannot be a hidden label or feature. `dod`, images and raw waveforms are unavailable or prohibited for this study. Other configured UKB, eICU and HCC data remain directly accessible but are not mixed into this MIMIC estimand.

## Fair baseline and substantive alternative

Freeze a deterministic subject-level 70/15/15 train/validation/test split before fitting, stratified only by endpoint and anchor-year group. No subject crosses partitions. All models below use the same phenotype-complete cohort, split, outcomes, censoring, gate and test set; preprocessing, clipping, scaling, imputation, calibration, q and learned assignments are training/validation only.

B0 is a transparent penalized discrete-time cause-specific complementary-log-log model for R, D and S, using admission/demographic/current-ICU context, terminal-bin physiology, terminal missingness and observation-process variables. It represents latest-state information.

B1 adds order-blind summaries in twelve one-hour bins over the same physiology, labs, output, pressor and observation-process fields. It tests generic late history without trajectory labels.

Bmask uses the same context, masks, counts, testing indicators, Foley charting and pressor-presence history with physiologic values removed. If Bdisc does not exceed Bmask, a physiology-specific interpretation fails.

Bdisc is the selected substantive alternative. It adds persistent-lactate status, improving/indeterminate/worsening perfusion, early/late lactate, MAP and pressor changes, interaction, organ markers and separate availability indicators to B1. The scientific output is the interaction and standardized CIF contrast, not a black-box score. It can reveal a cross-domain effect modification that B0's terminal state and B1's order-blind summaries lose.

M2 is a deferred learned sensitivity: fit a two-component diagonal-covariance Gaussian mixture on training-only standardized early-to-late change vectors (lactate, MAP, pressor minutes, secondarily output/organ markers), then enter posterior probability in the same cause-specific model. Label components only when training means satisfy fixed direction rules; otherwise keep them unlabeled. It may reveal nonlinear coupled trajectories, but is not primary because selective measurement can destabilize mixture labels and the scientific claim requires auditable categories.

A GRU/transformer is deferred because the parent branch already tests chronological representation against order-blind history, while this repair targets coverage and cross-domain interaction. A causal fluid-response model is deferred because `inputevents` has no fluid responsiveness, treatment intent, counterfactual treatment outcome, treatment limitations, or adequate time-varying confounding control. These are evidence-bound deferrals, not bans on neural networks, GPUs or structured data.

Future solver resource plan: CPU first, within the planning envelope of 16 CPUs, 262,144 MiB and up to 8 GPUs for 28,800 seconds. Discovery archive coverage scan uses 4 CPUs/32 GiB/no GPU; its runtime and all model/bootstrap runtimes are unverified until measured. Small tabular fits and M2 are expected CPU-feasible; an allocated A100 (`cuda:0`) is an allowed contingency for repeated matrix-intensive fitting, not a scientific requirement. No proposer/solver weight training is authorized.

## Analysis, uncertainty and falsification

Report held-out 48-hour CIF and transition-aware Brier scores for R, D, S, R/D and N; calibration intercept/slope; AUROC/AUPRC for component outcomes; paired Bdisc-B1 and B1-B0 differences; interaction estimates; and subject-bootstrap 95% intervals. Fixed 5/10/20% test-set review-capture tables are descriptive operating characteristics only, not clinical utility.

Repeat the parent’s outcome-free pooled ICU-stay-hour live-exit score q as a selection-stress sensitivity. q uses only pre-hour information; report overlap, positivity and effective sample size by phenotype/care unit. Non-exit hours have no observed post-exit outcome. q or stabilized odds tilting is not a discharge-policy counterfactual. Poor overlap or calibration makes this sensitivity inconclusive, not a reason to change the primary estimand.

Required checks:

1. dictionary labels/linksto/units, ranges, timestamps, interval clipping, joins, duplicates, first-exit selection and prohibited-field exclusion;
2. gate report before fitting, with row-level feature provenance;
3. Bdisc versus Bmask and phenotype-only process model;
4. early/late permutation within subject preserving counts/availability;
5. outcome permutation within partitions and refitting;
6. available-by-landmark versus chart-time-only matrices;
7. fixed sensitivities: lactate 4.0, arterial MAP only, fixed single MAP modality, MAP-only, pressor-only, Foley corroboration, continuous changes, 4/6/8 valid-bin thresholds, 7-day endpoints and U bounds;
8. R, D and S separately; gains confined to S/N do not support adverse perfusion biology;
9. phenotype prevalence, indeterminate fraction, measurement intensity, store-lag, q strata, time-local unit strata and anchor-year strata;
10. the six-hour live-exit negative-control process model. A much stronger phenotype signal for exit-process prediction than R/D supports selection/process explanation.

Support requires a passed gate; an interaction below -2 points with its 95% interval wholly below -2, lower persistent-lactate R/D CIF in improving than worsening, calibrated held-out R/D improvement of Bdisc over B1, Bdisc exceeding Bmask, and stability across fixed timing/unit/coverage/q/endpoint sensitivities. M2 can corroborate but cannot validate a proxy phenotype.

Adverse evidence is a null/reversed interaction, Bdisc matching B1/Bmask, process-only or chart-only explanation, modality/coverage/selection instability, gains confined to S/N, or resistance to outcome permutation. Inconclusive evidence is any failed gate, sparse component events, high indeterminate/U fraction, incompatible units, poor overlap/ESS, unstable calibration, or a wide interval.

Computationally checkable claims are source provenance, flow, timing, units, coverage, cell/event counts, joins, split integrity, model outputs, CIF/Brier/calibration, interaction, uncertainty and falsifications. Clinical adjudication or another study is required for microcirculatory dysfunction, lactate etiology, clinician intent, fluid responsiveness, treatment appropriateness, preventability, causal fluid/discharge effects, monitoring benefit, bedside utility, external transportability and recommendations.

## Supporting evidence and provenance

The read-only feasibility audit is `support/mimic_lactate_coverage_audit.json`, generated by `support/coverage_audit.py` from the six relevant archive members. It counts source coverage only; it does not fit a model or inspect outcomes. Its filtering is the same first eligible live-exit, 12-hour/1-hour pre-landmark and dual clinical-plus-storetime rule, with the primary item IDs above. Any scan interruption is recorded as unverified rather than treated as zero.

The inspected local materials were `datasets/README.md`, `datasets/mimic/README.md`, full MIMIC catalog metadata, `references/expert-seeds/README.md`, `references/expert-seeds/cards/mimic-04.md`, `references/research-ambition/README.md` and `methods-and-compute.md`. The parent’s frozen support record contains the current literature-search provenance; it is orientation, not proof. No unavailable paper text or supplementary methods are claimed as read.

Alternatives not chosen and revisit evidence are explicit: revisit M2 as primary only if the gate passes and learned component assignment is stable under resampling and coverage sensitivity; revisit a chronological neural model only if a new chronology estimand is justified beyond B1; revisit causal fluid modeling only if treatment intent, fluid responsiveness, confounding controls and counterfactual outcome ascertainment become available. The actual deliverable is newly fitted B0/B1/Bmask/Bdisc, optionally M2, the gate audit, interaction/CIF/uncertainty outputs and falsification/claim-ledger files.
