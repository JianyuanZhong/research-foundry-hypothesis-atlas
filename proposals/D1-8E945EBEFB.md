> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# A pre-registered, label-independent control universe for target-linked pulmonary discharge handoff

## Parent, purpose, and scope of this repair

This is a targeted child of `[prior hypothesis]`. It preserves the parent's frozen pulmonary discharge-text estimand and all constraints. In particular, it does not alter the first-eligible adult, one-admission-per-subject, all-opportunity MIMIC frame; exact atom/route `g=(E, terminal curr_service, W)`; reciprocal pre-discharge report/addendum chronology; canonical discharge artifact; all-unit adverse routing; label-independent control universe; positive-probability two-phase whole-admission sampling; finite-population inference; workload ledger; or silent-validation-only conclusion ceiling.

The only addition is a fully pre-label, target-cell-specific bridge protocol. It makes a supportive retrospective documentation contrast decision-relevant by specifying what a future silent workflow study must actually measure, how its target and negative-control opportunities are selected, how support and workload are guaranteed, and which results are adverse or inconclusive. The bridge is frozen before any phase-1 or phase-2 clinical label is exposed. It is a nomination protocol, not a change to the retrospective estimand and not authorization for a live alert, order, referral, copied recommendation, or patient-facing communication.

## Evidence boundary and unresolved decision

The parent can test only whether the exact pulmonary recommendation atom is preserved in stored canonical discharge text. Its strongest supported claim remains a target-linked stored-text reproducibility/specificity result. MIMIC does not record actual delivery, viewing, responsibility, ordering, scheduling, completion, outside care, patient preference, appropriateness, safety, or benefit.

The unresolved bridge question is narrower and falsifiable:

> For the one frozen atom/route cell nominated by the retrospective protocol, can a future site measure, with actual calendar timestamps, whether the recommendation is available to a resolvable responsible workflow by its prescribed interval, and is that availability meaningfully more target-linked than for a pre-registered matched non-target documentation control?

A supportive bridge result would establish feasibility and an observed workflow-availability contrast under a silent, target-cell-specific protocol. It would not establish that the recommendation was clinically appropriate, that anyone acted on it, that imaging was completed, or that care or outcomes improved.

## Pre-label bridge freeze

Before `PHASE1_LABELS_SEALED`, the compiler must append a bridge manifest to the inherited manifest. The manifest contains the immutable retrospective target IDs `(E*,M*,W*)`, route, dictionary/parser hash, exact control rule, prospective site and fixed calendar window, sampling seed, field-level missingness codes, timestamp precedence, outcome definitions, support floors, gates, and the separate future workload ledger below. The manifest is signed and hashed before any retrospective H status, route, reviewer preference, or target-linked result is available.

No retrospective result may choose the site, extend the calendar window, select a second atom, alter the control, change a threshold, or decide which prospective fields are collected. If retrospective selection is `NO_SELECTION`, or the target/control contrast is adverse or inconclusive, the bridge status is `DEFER` and no prospective data collection is triggered under this protocol.

The bridge has one fixed participating site, one fixed 16-week actual-calendar collection window, and one fixed target cell. A site or week with no eligible opportunity is retained as zero exposure, not dropped. There is no adaptive extension, site replacement, favorable-subgroup selection, or post hoc pooling. The site must use an approved production-like read-only shadow feed; all shadow outputs are suppressed from clinicians, patients, orders, referrals, scheduling, and copied text.

## Prospective population and exact data binding

The future site must implement the inherited frozen parser and exact target atom, without changing its lexical dictionary or route. An eligible prospective opportunity is the first finalized radiology report in an encounter whose parsed report unit yields `g*=(E*,M*,W*)`, has a resolvable encounter and actual discharge timestamp when discharge is part of the inherited route, and occurs in the fixed window. Multiple target units in one report are retained under the inherited unitization and all-unit adverse rule; they are not collapsed by a reader. A deterministic SHA-256 hash of `(site_id, encounter_id, report_id, unit_ordinal)` is used only for the fixed human-review sample; it does not change eligibility.

For each eligible target opportunity, the site must export one row in an append-only bridge table with these exact columns:

- `site_id`, `patient_pseudonym`, `encounter_id`, `report_id`, `unit_ordinal`, `source_report_version`, `source_finalized_at`, `actual_discharge_at`, `target_E_id`, `target_M_id`, `target_W_id`, `route_id`, `parser_version`, and `dictionary_hash`;
- `report_available_at`, `report_delivered_at`, `first_view_at`, `first_view_user_role`, `first_view_user_id_pseudonym`, `responsible_service_id`, `responsible_clinician_id_pseudonym`, `responsibility_resolved_at`, and `responsibility_resolution_code`;
- `shadow_emit_at`, `shadow_suppressed_flag`, `ui_version`, `ui_location`, `ui_edit_or_override_flag`, and `shadow_payload_hash`;
- `target_order_id`, `target_referral_id`, `target_scheduled_at`, `target_completion_at`, `target_result_review_at`, `outside_care_indicator`, `outside_care_source`, `patient_preference_code`, and `patient_refusal_at`; and
- `data_capture_batch_id`, `source_row_hash`, `missingness_code`, and `bridge_exclusion_code`.

Identifiers are pseudonymous inside the governed site; no row, note, or patient identifier is sent to a public search service. The retrospective source binding remains exactly the parent's MIMIC binding: `hosp/admissions` (`subject_id,hadm_id,admittime,dischtime`), `hosp/services` (`subject_id,hadm_id,transfertime,prev_service,curr_service`), `icu/icustays` as the inherited proxy, `note/radiology` (`note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`), `note/radiology_detail` (`note_id,subject_id,field_name,field_value,field_ordinal`), `note/discharge` with `note_type='DS'`, and `note/discharge_detail`, from the exact snapshot, archive members, absolute files, schema hashes, joins, and pre-D rules already specified in the parent. The bridge adds no MIMIC field and treats no retrospective timestamp as a delivery or view event.

## Prospective negative control, fixed before outcomes

For each target encounter, construct a candidate negative-control universe before any bridge outcome is read. A control must be a same-encounter, same-report-stream recommendation unit that is non-target (`E != E*`), affirmative, patient-specific, and has exactly the same canonical modality `M*` and due interval/date `W*` under the inherited dictionary. It must be disjoint from the target unit and source span, and must pass the same report-finalization and encounter-link rules. The first control under the inherited order `(report_finalized_at, report_id, unit_ordinal, source_span_start)` is fixed; no control is replaced if it lacks a workflow event. If no such unit exists, record `control_absence=structural` and do not impute a control or substitute a control-only encounter.

The future control row carries the same columns as the target row, with `control_E_id`, `control_M_id`, `control_W_id`, `control_parser_version`, and `control_dictionary_hash` replacing the target atom fields. Control rows are a process-specific negative control, not a clinical negative control. They test whether observed workflow availability is specific to the frozen target rather than generic documentation behavior. They cannot rescue an absent or adverse target result.

## Actual-calendar time rules and outcomes

The future site uses synchronized, timezone-aware UTC timestamps and retains the original local timestamp and timezone offset. The opportunity clock is `t0=source_finalized_at`; only events with valid encounter/report linkage and `t >= t0` are eligible. The prescribed due time is calculated from the frozen `W*` function in the bridge manifest using actual calendar arithmetic; if `W*` is an interval, the manifest's exact interval endpoint is used, and if it is a date, only the normalized date in the target's actual calendar is accepted. No timestamp is borrowed across patients or encounters.

The following are distinct binary/timestamp outcomes, never collapsed:

1. `Dlv=1` if `report_delivered_at` exists and is no later than the due time; `Dlv=0` if a valid delivery audit exists after the due time; `Dlv=U` if delivery logging is absent, contradictory, or cannot be linked.
2. `Vw=1` if a named accountable workflow role has a valid first view at or before the due time; `Vw=0` if a valid role-linked view occurs after it; `Vw=U` otherwise. A report being stored is not a view.
3. `Rsp=1` if `responsible_service_id`, `responsible_clinician_id_pseudonym`, and `responsibility_resolution_code` are independently resolved by the due time; `Rsp=U` when responsibility is unavailable or disputed. The service code is a workflow field, not proof of acceptance or clinical responsibility.
4. The primary feasibility outcome is `Avail=1` only when `Dlv=1`, `Vw=1`, and `Rsp=1` by the due time; it is `Avail=0` only when all three audit streams are present, linked, and at least one required component is definitively late; otherwise it is `Avail=U`. This is availability to a resolvable workflow, not action, completion, appropriateness, safety, or benefit.
5. `Act`, `Sched`, `Comp`, and `Review` separately record target-linked order/referral, scheduling, completion, and result review. `Outside`, `Pref`, and `Refusal` are separate states. None is inferred from absence of an in-system row, discharge location, death, or the silent shadow event.

A due-time event is included (`event_at <= due_at`); an event after due time is late, not timely. Delivery and view may precede discharge or occur after discharge; the protocol reports their actual timing separately and never calls a post-discharge event pre-discharge. If a target has multiple units, admission-level availability is positive only if every required target unit has `Avail=1`; any `Avail=0` or `Avail=U` is retained under the inherited all-unit adverse precedence. A missing or contradictory required unit is not deleted.

## Prospective sampling, support, and positivity

The fixed 16-week window is a census of all target opportunities and all first eligible controls. To bound human workload without outcome-dependent sampling, every opportunity is captured electronically, and a human audit sample is selected by a seed committed before the window using `SHA256(seed || site_id || encounter_id || report_id || unit_ordinal)`. The sample is the first 300 target opportunities and their first controls if the fixed hash is below the pre-registered threshold; if more than 300 are eligible, the threshold is set before launch to select exactly 300 in expectation and the realized inclusion probability is recorded. The selection probability is independent of delivery, view, responsibility, action, completion, or clinical labels. If the window contains fewer than 120 target opportunities, the bridge is `DEFER`; no extension is allowed.

For a decision-relevant paired process contrast, at least 120 target opportunities and at least 60 target/control pairs must be present in the fixed window. Each participating service-workflow stratum defined before launch by `(site_id, terminal_service_group, calendar_week)` must have positive target capture probability and positive control capture probability whenever its source-only control universe is nonempty. Any occupied stratum with zero inclusion probability, an unresolvable sampling denominator, or an unrecorded seed is a positivity failure and maps to `DEFER`. Structural control absence is reported as a count and rate; it is not treated as a missing outcome and cannot be used to manufacture paired support.

The primary prospective estimands are finite-window quantities: the target `Avail` rate over all eligible target opportunities, the paired control `Avail` rate over the frozen set with a control, and `Delta_bridge = Avail_T - Avail_C` on that same paired domain. Human-audit estimates use the recorded inclusion probabilities and design weights; electronic census fields are not silently treated as complete when their audit stream is unavailable. Unknown outcomes remain unknown in the primary report and are accompanied by conservative bounds that count `U` adversely for a release gate. No complete-case denominator or post-outcome control replacement is permitted.

## Separate future workload ledger

The inherited retrospective ledger is unchanged and remains authoritative:

`T = T_micro + T_floor + T_target_extra + T_non_target_extra + T_control_only`,

`reserve_minutes = ceil(0.15 * (phase2_reading_minutes + fixed_controls_minutes))`,

`charged_minutes = phase2_reading_minutes + fixed_controls_minutes + reserve_minutes <= 84,000`,

with `120 <= T <= 300`, target quota at most 180, no unit sampling, and reviewer-hours at most 1,400. The prospective bridge is not inserted into, or allowed to relax, that ledger. Its future operational ledger is separately budgeted before launch so a retrospective pass cannot conceal a later staffing requirement.

The bridge's maximum manual workload is fixed as follows: 300 target packets plus 300 first-control packets = 600 packets; 8 active minutes per packet for one abstractor (`4,800` minutes); independent duplicate audit of 20% of the maximum packets, `ceil(0.20*600)=120` packets at 8 minutes (`960` minutes); fixed codebook/training `480` minutes; and fixed governance/adjudication charge `ceil(36*20)=720` minutes for at most 36 unresolved or contradictory cases. Base workload is therefore `4,800+960+480+720=6,960` minutes. The future reserve is exactly `ceil(0.15*6,960)=1,044` minutes, for `8,004` charged minutes (`133.4` hours), below the separately approved 160-hour bridge cap. Electronic event ingestion and suppression monitoring are automated and logged, not substituted for the manual bound. If the maximum sample, duplicate audit, or any fixed charge cannot fit this ledger, the bridge is not launched; no lower-cost post-label allocation is allowed. A prospective human adjudicator never changes retrospective H labels or route.

## Pre-registered bridge gates and interpretations

All gates are fixed before retrospective labels and before prospective data collection.

**Supportive/actionable-feasibility result.** The bridge may be considered only if the retrospective parent and added H gates pass, the future window contains at least 120 target opportunities and 60 paired controls, every occupied sampled stratum has positive inclusion probability, timestamp/linkage completeness is at least 95% for delivery, view, and responsibility fields, and the conservative simultaneous one-sided 95% lower bound for target `Avail` is at least 0.70 and for `Delta_bridge` is at least 0.10. These are operational feasibility thresholds, not safety thresholds. The result supports only proceeding to a separately approved silent workflow evaluation with suppressed output.

**Adverse workflow evidence.** With adequate support and valid audit streams, a target lower bound below 0.70, a paired contrast upper bound below 0.10, or a control availability rate at least as high as the target blocks promotion of this atom to a workflow-availability priority. A target `Avail=0` or `Avail=U` under the all-unit rule is retained as an adverse or uncertain workflow observation, never translated into unsafe care or clinical error. Adverse retrospective documentation or prospective availability does not imply that the recommendation was wrong or that follow-up failed.

**Inconclusive result.** Fewer than the support floors, any zero/undefined inclusion probability, timestamp or identity contradiction, delivery/view/responsibility completeness below 95%, a non-finite or overly wide simultaneous interval, missing suppression logs, unresolvable accountability, structural absence of paired controls, or an outside-care/patient-preference state that cannot be ascertained maps to `DEFER`. No duration, site, atom, subgroup, control, threshold, or denominator may be changed to avoid `DEFER`. Completion, result review, outside care, refusal, appropriateness, safety, and benefit remain descriptive unknowns unless directly measured.

## Evidence that still requires future adjudication

The bridge must obtain independent clinical adjudication, outside the retrospective H roster, for whether the finding was real, whether the recommendation was appropriate under the contemporaneous clinical context, whether the eventual action and timing were safe, and whether an apparent non-action was clinically justified. It must also obtain actual patient preference/refusal, accountable clinician confirmation, outside-care linkage, completed imaging and result review, and any adverse event ascertainment. These fields are not available in the configured MIMIC sources and cannot be reconstructed from `hosp/admissions`, `hosp/services`, `icu/icustays`, transfers, note storage times, discharge text, or the parent's control universe.

The silent bridge may log the shadow atom, delivery/view/accountability events, and separately collected actions, but must suppress any alert, copied text, order, referral, scheduling action, or patient-facing message. Only a later governed comparative study with an intervention, contemporaneous control, actual-calendar follow-up, patient-level outcomes, and independent safety/appropriateness adjudication could test utility, harm, equity, or benefit.

## Falsification and verification additions

The compiler must fail closed if the bridge manifest is written after any clinical label; if the future parser, target IDs, control rule, site/window, seed, threshold, field definitions, or gates differ from the manifest; if a shadow event is delivered to a clinician or patient; if delivery is scored from storage, viewing from availability, responsibility from service alone, or action/completion from absent records; if a control is selected after workflow outcomes; if `U` is deleted; if an occupied stratum lacks positive sampling support; or if the future ledger is charged to an unregistered lower-cost assumption.

The verifier must independently replay the bridge manifest, exact target/control construction, actual-calendar due-time comparisons, audit inclusion probabilities, paired finite-window estimands, unknown-state bounds, and the `6,960 + ceil(0.15*6,960) = 8,004` minute ledger. It must test suppression logs and prove that no retrospective result can alter prospective eligibility or collection. A fixture can verify schemas, joins, time arithmetic, support, ledger, and fail-closed mechanics only. It cannot establish that a report was clinically appropriate, that a workflow action benefited a patient, or that the bridge is safe; those claims require the unavailable adjudication and a later governed study.

## Substantive advance and remaining uncertainty

This child adds no new retrospective outcome or hidden surrogate. It converts the parent's broad recommendation for a future silent study into a source- and field-bound, pre-label bridge contract with an actual-calendar target-cell population, a deterministic matched process negative control, explicit delivery/view/responsibility/action/completion separation, positive-support rules, conservative unknown handling, and an independently budgeted workload. It therefore makes a retrospective stored-text contrast more useful for deciding whether a silent workflow feasibility study can be run, while preserving the inherited pulmonary discharge-text estimand and every inherited constraint.

The central uncertainty remains fundamental. MIMIC's subject-shifted storage and chart clocks cannot supply prospective delivery or clinical truth; the retrospective H outcome is not a surrogate for the bridge's availability outcome; a workflow view is not acceptance or action; and a supportive bridge result is not evidence of safety, appropriateness, completion, benefit, or causality. No empirical bridge result is claimed here.
