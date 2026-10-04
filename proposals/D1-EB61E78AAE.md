> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Target-linked handoff falsification child of [prior hypothesis]

## What is inherited and locked

This is a targeted child, not a replacement protocol. It preserves the parent's first-eligible adult, one-admission-per-subject MIMIC pulmonary-opportunity frame; admission chronology; reciprocal pre-discharge report/addendum chronology; exactly one canonical discharge summary (DS); exact atom `g=(E, terminal curr_service, W)`; sealed route-concealed C/S panels; H1/H2/H3 and holistic controls; all-unit adverse precedence; positive-probability two-phase whole-admission design; additive distinct-admission ledger; finite-population HT/Hajek inference; and the silent-bridge-only, noncausal conclusion ceiling. No target, population, route, unit, sample, endpoint, or allocation may be switched, pooled, rescued, replaced, or learned from phase-1 or phase-2 labels.

The inherited primary estimand remains the admission-level finite-population adverse indicator for one exact target atom-route cell. The new layer is a pre-registered secondary documentation-falsification estimand and a necessary *additional* gate before a silent workflow bridge could even be considered. It does not turn documentation into workflow, completion, appropriateness, clinical truth, safety, benefit, or causality.

## Unresolved clinical question and advance

The parent can establish that one exact radiology-text route is reproducibly measurable under a design-valid all-unit protocol. That remains weaker than evidence that the route is carried into the artifact most likely to communicate a plan at discharge. The unresolved, falsifiable question is:

> For the frozen exact target atom-route, does the canonical pre-discharge DS contain an explicit, non-conditional, non-negated instruction that preserves the target's modality and due interval, at a rate distinguishable from a fixed non-target recommendation control, after accounting for unreadable/conflicting text and missing/outside-care information?

A positive result would support only a target-linked *documentation handoff* construct: the recommendation survived into the DS. It would not show that anyone received, viewed, accepted, ordered, scheduled, completed, or benefited from follow-up. A negative result would falsify the proposed handoff construct for this exact cell and block silent-bridge priority even if the inherited radiology route itself is reproducible. This makes the protocol clinically more consequential without claiming an unavailable real-world action.

## Exact MIMIC binding

Use the frozen snapshot `[source checksum]` and read-only sources:

- `[internal dataset path]`, [source checksum]; archive members `mimic-iv-3.1/hosp/admissions.csv.gz`, `mimic-iv-3.1/hosp/services.csv.gz`, `mimic-iv-3.1/icu/icustays.csv.gz`, and `mimic-iv-3.1/hosp/transfers.csv.gz`.
- `[internal dataset path]` and `[internal dataset path]`.
- `[internal dataset path]` and `[internal dataset path]`.

Schema artifacts in this workspace are:

- `datasets/mimic/table-e8ec3e6e4c428559.json` for `hosp/admissions`, columns `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; join `(subject_id,hadm_id)` and `D=dischtime`.
- `datasets/mimic/table-491b3c713229062a.json` for `hosp/services`, columns `subject_id, hadm_id, transfertime, prev_service, curr_service`; terminal `curr_service` is the last nonmissing `transfertime < D` value.
- `datasets/mimic/table-7d5c8feb0fb0dbd4.json` for `icu/icustays`, columns `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; it remains only the inherited pre-D ICU proxy.
- `datasets/mimic/table-685b6b74d0d7c547.json` for diagnostic `hosp/transfers`, columns `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; it is not substituted for actual departure.
- `datasets/mimic/table-1ffcd77c4cbdaeda.json` for `note/radiology`, columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; join `(subject_id,hadm_id)` and note key `(subject_id,note_id)`.
- `datasets/mimic/table-2972dbfe5cb661c0.json` for `note/radiology_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`; join `(subject_id,note_id)` to radiology and retain `field_ordinal`.
- `datasets/mimic/table-69be322e2b58015b.json` for `note/discharge`, with the same eight note columns as radiology; join `(subject_id,hadm_id)`, retain only `note_type == 'DS'`, and apply the inherited canonical-D/S rule.
- `datasets/mimic/table-18d43f38e33d1fd2.json` for `note/discharge_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`; join `(subject_id,note_id)` to the canonical DS and retain `field_ordinal`.

No cross-subject timestamp comparison is allowed because MIMIC timestamps are subject-shifted. Every radiology and DS record used in this layer must have `charttime < D` and `storetime < D`; the reciprocal report/addendum chain must use only subject/admission-consistent fields available in the files. The DS's existence and uniqueness are inherited frame/support inputs, not target-linked outcome labels.

## Handoff construct and unit of analysis

A phase-2 unit is the inherited recommendation unit within an admission and exact atom-route, with its source radiology note/addendum provenance. Freeze the target and all target memberships before any phase-1 clinical label is exposed. For each sampled admission, two fresh independent C readers and two fresh independent S readers perform the inherited route/adverse task. In addition, two fresh independent, route-concealed **H readers** inspect only the already-frozen source report unit and canonical DS packet, with H rosters disjoint from phase 1, C, S, task, and inherited rosters.

H readers assign one mutually exclusive status for the target unit:

- `H+` (documented handoff): the canonical DS contains an explicit instruction referring to the same target cluster `E`, the same action modality, and the same due interval/date `W`, with an attributable sentence/field span; it is affirmative rather than negated, historical, hypothetical, uncertain, optional/conditional, or merely “follow up” without the atom's modality and interval.
- `H-` (documented discordance/omission): the canonical DS is available and readable, but no such exact affirmative atom-preserving instruction is present, or the DS explicitly says no follow-up / a conflicting modality or interval.
- `H_U` (unresolved/unavailable): DS text/field is unreadable or truncated, the report-to-DS linkage or reciprocal chronology is unresolved, H readers disagree after the registered adjudication rule, or the relevant source unit is too ambiguous to identify. `H_U` is not treated as H-.

The unit-level secondary outcome is `A=1` only when both independent H readers return `H+`; otherwise `A=0` is not asserted. H disagreement, nonresponse, and an incomplete packet are `H_U` at original path weight. A conservative admission-level handoff failure `F_H=1` is assigned if any target unit has `H-` or `H_U`, or if any sampled target unit lacks a positive H+ determination. Thus a minority adverse/uncertain unit cannot be hidden by a majority. This is a documentation rule, not a clinical correctness rule.

The exact lexical/interval matching dictionary, token normalization, calendar-month arithmetic, negation/uncertainty/conditionality examples, and adjudication rule must be frozen before phase-1 labels. Automated lexical flags may assist packet navigation only; they cannot overrule either H reader. Do not use the parent's unvalidated cirrhosis detector as a pulmonary diagnosis extractor.

## Target-linked controls and falsification

The new layer is not accepted merely because target strings appear in DS text. Before phase-2 access, freeze a control roster using only frame/support fields and the already sealed target. Use the following positive-probability controls without adding a post-label selection:

1. **Within-admission non-target recommendation controls.** Where a sampled admission contains a distinct, explicit non-target recommendation unit in the same pre-D radiology corpus and a canonical DS, select the first fixed-order eligible non-target unit by a registered report/note/ordinal order. It is processed by the same H readers, who are blinded to target membership. Its atom is not substituted for the target and it cannot affect the target's primary outcome. If no eligible control exists, record structural absence; do not manufacture one.
2. **Route-scrambled documentation controls.** For each control packet, use a pre-label cryptographic permutation of modality/interval tokens drawn from the fixed target/control pool, retaining the report and DS provenance but not presenting the scrambled atom as a clinical recommendation. This tests whether generic follow-up language is being scored as exact handoff. It is a measurement control only; a scrambled match is a failure of specificity, not a clinical event.
3. **Admission-level non-target control.** If no within-admission control exists, a fixed pre-label control-only admission may be used under the parent's `T_control_only` component and positive inclusion probability. It is never a replacement for an ineligible target or a reason to alter the target cell.

The principal falsification contrast is the design-weighted difference in exact H+ rate between frozen target units and eligible non-target controls, with a pre-specified minimum separation and simultaneous confidence bound. If the target rate is no better than controls, or if route-scrambled controls are frequently H+, the target-linked specificity claim fails even if the parent primary route construct passes. Because controls can be structurally absent, the contrast is reported only for the registered control estimand with its observed positive-support domain; missing control support is inconclusive, not evidence of superiority.

## Sampling, ledger, censoring, and analysis

The inherited phase-1 master (at most 900 admissions), first fixed-order target/`NO_SELECTION` rule, post-label `d=(h,z)` and target/non-target `e` strata, exhaustive allocation, floors, and all-unit adverse precedence are unchanged. The H packets use the same sampled whole admissions and are charged in the already sealed `t2_max_minutes_per_unit`/fixed-control workload certificate. If an additional control-only admission is necessary, it is included once under `T_control_only`; it is not duplicated when it also satisfies another role. The authoritative ledger remains

`T = T_micro + T_floor + T_target_extra + T_non_target_extra + T_control_only`,

with `120 <= T <= 300`, target quota at most 180, charged reading plus fixed-control minutes plus one `ceil(0.15 * raw_minutes)` reserve at most 84,000 minutes, and inherited reviewer, weekly, roster, and 32-week constraints. No mean rehearsal time or post-label top-up is permitted.

Retain `pi1_i`, `pi1_ij`, conditional `q_i`, conditional `q_ij`, and sequential path weights exactly as inherited. Estimate the target admission-level H-failure total and denominator using sequential HT and the corresponding Hajek ratio. For target/control contrasts, use a registered joint finite-population estimator with positive pair support; if any requested pair inclusion probability is zero or undefined, fail closed for that contrast while retaining separately estimable first-order totals. Compute law-of-total-variance uncertainty with at least 20,000 nested Rao-Wu-style replicates, reconstructing phase-1 bands and conditional phase-2 SRS. H nonresponse remains `H_U` at original weight, never complete-case deletion or replacement.

The following are explicitly not outcomes: actual departure, whether a report was delivered or viewed/acknowledged, named responsibility, patient preference, outside plans or outside-care follow-up, an order/referral/scheduling event, completed imaging, image findings, burden, safety, benefit, or causal outcome. `discharge_location`, `hospital_expire_flag`, `deathtime`, ICU stay, services, and transfers can describe inherited eligibility/proxy strata only; they cannot impute a completed outpatient action. In-hospital death, hospice/comfort exclusions and post-D evidence remain exactly as inherited. A DS omission may mean missing documentation, care elsewhere, or a clinical decision not to pursue follow-up; these possibilities are not separable in MIMIC and are all represented as the narrow H documentation outcome or `H_U`, not as patient nonadherence or unsafe care.

## Pre-registered gates and interpretation

In addition to every inherited primary gate, a silent bridge is eligible for consideration only if all of the following hold for the frozen target cell:

- the inherited primary route construct passes its simultaneous precision, event/ESS, positive-probability, shared-error, and workload gates;
- H+ and H- definitions were sealed before labels and H readers remain blinded/roster-disjoint;
- the target handoff estimate has positive support and a simultaneous interval of registered width;
- the target-versus-control contrast has positive pair support and its simultaneous bound excludes the registered negligible-specificity margin in the favorable direction;
- route-scrambled H+ is below the registered specificity ceiling; and
- no H packet, target-freeze, ledger, chronology, or nonresponse invariant fails.

**Supportive:** The exact radiology route is reproducible, target H-failure is bounded below the inherited adverse margin, the target-control specificity contrast is favorable, and scrambled controls are rare. This supports only that a target-linked instruction is reproducibly documented in the canonical DS and permits consideration of a separately approved prospective silent workflow bridge with outputs suppressed or `DEFER`. It does not support delivery, viewing, responsibility, action, completion, appropriateness, safety, benefit, or causality.

**Adverse:** Any target unit with H- or H_U under all-unit precedence, a target-control contrast no better than controls, frequent scrambled matches, or a primary route failure falsifies the exact cell's bridge-readiness construct. Exclude this exact cell from bridge priority; do not convert H_U to RECON, switch cells, or search for a favorable subgroup.

**Inconclusive:** `NO_SELECTION`, sparse/undefined pair support, control structural absence, failed calibration or adjudication, nonresponse, missing DS/report linkage, invalid sealing, or insufficient simultaneous precision maps to `DEFER`. It is not evidence that the route is safe, clinically wrong, or absent in outside care. Actual workflow and clinical truth require prospective delivery/view logs, orders/referrals/scheduling, named responsibility, patient preference, longitudinal outside-care linkage, completed imaging and expert adjudication.

## Falsification and verification requirements

Fail closed on target selection after any clinical label; any altered or replaced target; H roster leakage; post-D evidence; use of `discharge_location`, death, transfer, or ICU as completed follow-up; generic “follow up” scored H+ without exact modality and interval; negated/conditional/historical text scored H+; route leakage; omission of an adverse/uncertain unit; deleted nonresponse; zero/undefined pair division; scrambled-control construction after labels; control selection after H labels; omitted fixed-control or reserve charge; duplicate admission counting; or any claim beyond stored-text documentation.

The compiler must produce machine-readable per-unit provenance: `(subject_id,hadm_id,note_id,field_ordinal,charttime,storetime,D)`, target/control membership frozen-state hash, H reader statuses and adjudication, exact matched DS span/field or reason code, inclusion probabilities, and ledger role. The verifier must independently test the target-freeze permutation invariant, chronology and one-canonical-DS rules, exact atom matching, all-unit adverse precedence, positive-support/pair guards, weighted target/control totals, scrambled specificity control, additive distinct-admission ledger, reserve charge, and nested variance. A passing fixture establishes only computational feasibility; it cannot verify that the DS was read, that a patient acted, or that a recommendation was clinically appropriate.

## Substantive change and remaining uncertainty

The substantive change is a source-bound, target-frozen handoff layer: it tests whether the exact recommendation survives from radiology text into the canonical DS, against fixed non-target and route-scrambled falsification controls, and makes that evidence necessary for any later silent-bridge consideration. The population, chronology, canonical artifact, atom-route, adverse precedence, two-phase probability design, ledger, inference, and causal ceiling are unchanged. The remaining uncertainty is deliberately explicit: MIMIC has no reliable actual workflow trace, no outside-care data, no proof of delivery/viewing or responsibility, no patient preference or completed follow-up, no images, and no adjudicated clinical truth. Therefore this child advances actionability only from “stored route measurable” to “stored target-linked discharge documentation measurable,” never to action or benefit.
