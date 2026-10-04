# Prospective translation of the conservative pulmonary-nodule handoff gate: silent validation followed, only after lane-specific gates, by a governed route-stratified workflow trial

## Decision question and substantive advance

The clinical decision is now prospective and staged: can the frozen, conservative admission-level pulmonary-nodule handoff gate operate on live, departure-frozen workflow events with sufficient route accuracy, temporal integrity, coverage, and safety to justify exposing clinicians to either of two distinct aids; and, only for a route that passes silent validation, does that aid improve the signed handoff without an unacceptable increase in inappropriate or conflicting plans?

This child does **not** revise the selected parent's retrospective population, chronology, route definitions, uncertainty handling, timing calibration, or intervention priority rule. The retrospective experiment remains a descriptive nomination study. Its strongest supportable claim is that, conditional on complete-source MIMIC reconstruction and explicit expert labels, a route may be sufficiently identifiable and frequent to merit a new prospective test. It cannot establish live trigger validity, clinician awareness, UI exposure, actual responsibility, outside plans, recommendation appropriateness, intervention effects, harm, or benefit.

The unresolved prospective hypotheses are deliberately separated:

1. **P1, silent validity hypothesis.** Among consecutive live admissions satisfying the frozen eligibility rubric, a versioned gate run only from information available at a locked predeparture landmark can reproduce an independent departure-frozen reference route. For the automation-nomination lane, the one-sided simultaneous 95% lower confidence bound for positive predictive value is at least 0.90 and the upper bound for a reference reconciliation/defer/closed case being nominated as automation is at most 0.05; route mixing, temporal leakage, missing critical events, and site drift also remain below governance-locked limits. The reconciliation lane has its own accuracy and feasibility gates and can advance even if the automation lane fails.
2. **P2, route-stratified workflow-effect hypothesis.** Within each P1-validated route and under cluster-period random assignment, the relevant clinician-facing workflow increases the probability of a departure-frozen, accepted, accountable signed plan by a governance-locked clinically material risk difference while satisfying a route-specific noninferiority safety margin for inappropriate, conflicting, or wrong-target content. The two routes are never pooled into one favorable composite.

P1 can falsify the gate without exposing treating clinicians. P2 can falsify either workflow even if P1 accuracy is excellent. Neither phase is a malignancy, adherence, or clinical-outcome efficacy study. A later study with longitudinal, cross-system outcome capture is required for those claims.

I considered a narrower repair that would add only timing calibration and import the strongest inherited lead-time branch. That is not scientifically preferable here: the selected parent already preserves `G`, `V/H/Z`, ordinary-discharge latency, radiology-lag controls, and 12/24/72-hour sensitivities. Another retrospective timing refinement cannot supply live report availability, UI exposure, clinician confirmation, contamination, or intervention effects. The consequential remaining gap is prospective translation. Live timing is therefore measured exactly below without changing or reinterpreting the frozen MIMIC clocks.

## Claims separated by evidence level

### Evidence already supported or frozen

The inherited complete-source, zero-sampling audit found 546,028 admissions, 2,321,355 radiology rows, 6,046,121 radiology-detail rows, 331,794 unique canonical `DS` admission keys, only 17 missing canonical `DS storetime` values, substantial ordinary discharge storage delay, and 3,764 retrieval-proxy pulmonary reports. The 3,764 reports are retrieval candidates, not adjudicated opportunities. No pulmonary opportunity prevalence, route burden, route accuracy, or intervention effect has yet been computed.

The parent also establishes a logically conservative policy: enumerate recommendation units, but route at admission level; never nominate structured propagation if any active unit is incomplete, conflicting, mixed, interaction-dependent, timing-limited, or decision-relevantly uncertain; and never allow silent insertion. That policy is a protocol specification, not validated clinical truth.

### Claim tested in P1

A locked implementation can reconstruct eligible recommendation units and assign `A_AUTO`, `A_RECON` (including `A_MIXED`), `A_DEFER`, `A_TIMING`, or `A_NOACTION` prospectively from events available by the route landmark, with accuracy, completeness, temporal integrity, and route yield adequate for a governed trial. Lane advancement is independent: failure of `A_AUTO` does not invalidate a sufficiently accurate reconciliation lane.

### Claim tested in P2

For admissions prospectively assigned to a P1-validated route, making the corresponding aid available causes a route-specific improvement in signed handoff quality under intention-to-treat cluster-period assignment, while meeting route-specific safety constraints. P2 does not test whether surveillance itself improves cancer outcomes.

### Claims requiring expert review or another study

Whether a radiology recommendation is guideline-appropriate for the individual patient; whether non-pursuit is clinically wise; whether a target-linked order is completed outside the system; whether surveillance changes stage, morbidity, mortality, or patient experience; and whether benefits exceed all downstream burdens require clinical governance, longitudinal cross-system evidence, and/or another trial. An automatic verifier can check event chronology, denominators, assignments, route code, confidence intervals, stopping rules, and whether conclusions match computed outputs. It cannot establish clinical appropriateness, causation outside the randomized workflow contrast, or patient benefit.

## Frozen retrospective MIMIC experiment: no design change

The entirety of the selected parent's retrospective experiment is retained. Compilation must treat any proposed change to this section's denominator, clocks, route, estimands, exclusions, uncertainty bounds, or falsification criteria as a scientific child requiring Lead review, not as a mechanical repair.

### Exact read-only provenance and source bindings

Use MIMIC snapshot `[source checksum]`. Core is supplied as MIMIC-IV 3.1; local note-version evidence supports 2.1. Timestamps are deidentified and shifted by subject: within-subject/admission intervals are usable, cross-subject calendar alignment is not. Source rows remain read-only; manifests, packet hashes, labels, code, and results are derived only in the workspace. No clinical text is sent to public services.

1. `[internal dataset path]`, [source checksum].
   * Archive member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema [source checksum]; columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`. Join key `(subject_id,hadm_id)`; departure boundary `D=dischtime`.
   * Archive member `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema [source checksum]; columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`. Join on `subject_id`; adult age is `anchor_age + year(admittime) - anchor_year >=18`, retaining the documented age representation.
   * Archive member `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema [source checksum]; columns `subject_id,hadm_id,transfertime,prev_service,curr_service`. Join `(subject_id,hadm_id)`; the last `curr_service` at or before `D` defines terminal-service family.
   * Archive member `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema [source checksum]; columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`. Use only for descriptive care-unit chronology.
   * Archive member `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema [source checksum]; columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`. Any exact admission-linked row defines ICU exposure.
   * Archive members `mimic-iv-3.1/hosp/poe.csv.gz` and `mimic-iv-3.1/hosp/poe_detail.csv.gz`. Table `hosp/poe`, schema [source checksum], has `poe_id,poe_seq,subject_id,hadm_id,ordertime,order_type,order_subtype,transaction_type,discontinue_of_poe_id,discontinued_by_poe_id,order_provider_id,order_status`. Table `hosp/poe_detail`, schema [source checksum], has `poe_id,poe_seq,subject_id,field_name,field_value`. Join details on `(subject_id,poe_id,poe_seq)` and admissions through `poe`. POE is excluded from primary retrospective adjudication because it lacks a validated recommendation-to-outpatient-order link, due date, recipient, UI exposure, and completion. A post-freeze appendix cannot change labels.
2. `[internal dataset path]`, [source checksum]; table `note/radiology`, schema [source checksum]; columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Join admissions on exact `(subject_id,hadm_id)`; note identity `(subject_id,note_id)`.
3. `[internal dataset path]`, [source checksum]; table `note/radiology_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`. Join `(subject_id,note_id)` and retain every ordinal and candidate report/addendum link field.
4. `[internal dataset path]`, [source checksum]; table `note/discharge`, schema [source checksum]; columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Restrict exactly to `note_type == "DS"`; join `(subject_id,hadm_id)`.
5. `[internal dataset path]`, [source checksum]; table `note/discharge_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`. Join `(subject_id,note_id)`, retain all rows, and do not treat `field_name` as a validated section ontology.

None of the prospective events specified later—report UI availability, viewing, draft edits, trigger execution, route display, clinician confirmation, assignment, patient communication, attributable orders, scheduling, outside-plan attestation, or live safety events—exists as a validated field in these MIMIC sources. Prospective records must not be simulated from MIMIC `storetime`, POE, or note text.

### Frozen denominator and chronology

Before discharge text, `DS_store`, later traces, comparator outcomes, or routes are read, hash the first-eligible-admission manifest `N_A`:

* adult; exact admission-linked radiology `charttime` in `[admittime-12h,D]`;
* incidental pulmonary nodule or indeterminate focal nodular pulmonary opacity;
* patient-specific unconditional chest/thoracic CT at exactly 3, 6, or 12 calendar months;
* exclude screening, established surveillance, cancer staging/oncologic surveillance, conditional or optional plans, explicit no-follow-up, in-hospital death, hospice/comfort-only transition under the locked rubric, and recommendations first introduced after `D`;
* never infer nodule size, smoking, malignancy risk, life expectancy, appropriateness, or missing context;
* one first eligible admission per subject, fixed before any outcome.

Reconstruct report/addendum chains only from reciprocal, subject-consistent, admission-consistent detail links. Every operative component must have `charttime<=D` and `storetime<=D`. A later material pre-`D` component supersedes only within a reciprocal chain. Missing/nonreciprocal/contradictory nodes, unresolved operative components, and missing or contradictory times are `U_R`, retained in cascade and bounds, never omissions. Eligibility reviewers are blind to discharge artifacts, `DS_store`, later events, and route.

The canonical artifact is the sole exact `note_type=="DS"` row per `(subject_id,hadm_id)`; a duplicate key stops confirmation. Missing artifact, text, link, or `storetime`, and unreadable/contradictory content remain unknown. `charttime` never substitutes for `storetime`.

For every `N_A` admission retain the exhaustive departure state `Y`: `F` faithful, `C_O` omission, `C_I` incomplete/conflicting, `R` text-supported alternate resolution, `A` known `DS_store>D` regardless of eventual content, and `U_D` unknown. They sum to `N_A`; later fidelity cannot change `A`.

Retain operative recommendation `R_store`, `DS_store`, and `G=DS_store-R_store` in hours. Retain `V={V_D,V_24,V_72,V_168,V_late,V_U}`, `H={H_stale,H_0_6,H_6_24,H_24_72,H_72plus,H_U}`, and eventual `Z={F_text,C_O_text,C_I_text,R_text,U_text}`. Publish every zero/unknown cell of `J_A=count(V,H,Z)/N_A` and its deterministic crosswalk to `Y`. The primary ample/departure-available stratum remains `E_A={V_D and H in (H_24_72,H_72plus)}`. No `G<0` or `DS_store>D` row enters primary content routing. Verify row-wise `D-R_store=(D-DS_store)+G`; the identity is not an alternate opportunity definition.

After `N_A` is frozen, enumerate `N_R` recommendation units without adding subjects/admissions. Unit `U=(target cluster, action/modality, due interval/date, polarity)` is the smallest operative tuple. Shared action/window for co-mentioned nodules is one unit; different actions/windows are separate; restatements are deduplicated; a material addendum updates the same unit. Boundary ambiguity is `U_BOUNDARY` with minimum/maximum compatible inventories. Each unit retains `(subject_id,hadm_id,unit_id)`, source `note_id`, operative component, `R_store`, source spans, action, interval/date, polarity, and boundary provenance. Compute `G_u=DS_store-R_store,u`; no admission is route eligible unless every active unresolved unit has `G_u>=24h`. Admission remains the decision, resampling, and multiplicity unit.

Only data stored by `D` enter packets. Preserve Panels A-C, all individual pre-consensus labels, evidence quotes, redaction audits, reviewer-compatible sets, unknown-compatible adverse assignments, and unit-boundary bounds. Panel A states observable context compatibility `K_OPEN/K_CLOSED/K_UNKNOWN`, never clinical appropriateness. Panel B states remain `S_DEC,S_DEF,S_EQ,S_CON,S_PART,S_0,S_UN` under the exact evidence hierarchy. Panel C classifies faithful, omitted, incomplete, conflicting, resolved, or unknown without route labels. Reviewers never vote directly for an intervention.

The frozen deterministic route remains:

* `U_RESOLVED` for `S_DEC/S_DEF/S_EQ`;
* `U_OPEN` for `K_OPEN + S_0/S_PART/S_CON + G_u>=24h`;
* `U_TIMING` for otherwise open unresolved units with `G_u<24h` or unresolved clock;
* `U_CLOSED` for noncontradictory `K_CLOSED`;
* `U_DEFER` for `K_UNKNOWN`, `S_UN`, `U_BOUNDARY`, unreadable content, or route-changing reviewer assignments.

Any defer makes `A_DEFER`; otherwise any timing-limited unit makes `A_TIMING`; all resolved/closed makes `A_NOACTION`. Among admissions with an open unit, `A_AUTO` requires every open unit to be a reproducible `K_OPEN + S_0 + wholly omitted` unit, all others resolved/closed, no boundary uncertainty, and no cross-unit conflict. Any incomplete, conflicting, interaction-dependent, or mixed admission is `A_RECON`; a pure omission plus any reconciliation unit is the named `A_MIXED` subset of `A_RECON`, never automation.

Preserve all all-`N_A` burdens per 100 (`B_AUTO,B_RECON,B_MIXED,B_DEFER,B_TIMING,B_NOACTION`), `RD_ROUTE=[n(A_AUTO)-n(A_RECON)]/N_A`, `RD_MIX=n(A_MIXED)/N_A`, recommendation-unit workload only as secondary, and `D_MIX=P(A_RECON or A_DEFER | at least one unit-level pure omission)`. Preserve individual-reviewer, unknown, and boundary bounds; subject-clustered fixed-seed bootstrap with at least 10,000 replicates; one simultaneous max-statistic 95% family; event/precision, reliability, redaction, source, chronology, overlap, comparator-portability, and sensitivity gates; and the governance-dependent retrospective priority rule. The inherited 0.10 `D_MIX` threshold is only a prospective-validation purity nomination margin, not a harm utility.

Preserve comparator `X`, portability labels, ordinary-discharge `O`, chest-radiology `I`, deterministic matched `M`, standardized availability at `b={0,24,72,168}`, exact `R_store-charttime` calibration, all overlap/effective-sample-size checks, and every inherited adversarial test. Preserve the complete noncausal limit: MIMIC storage chronology is not report finalization, visibility, signature, transmission, viewing, communication, receipt, responsibility, outside care, appropriateness, ordering, adherence, harm, or benefit.

## Prospective program governance and immutable locks

Before P1 enrollment, a multidisciplinary governance committee comprising hospital medicine, radiology, pulmonary medicine, primary care, nursing/care coordination, patient representation, informatics, privacy/security, human factors, biostatistics, and an independent safety chair must sign and timestamp a public-to-the-study protocol lock. The lock contains:

* eligibility and unit codebook; route engine source hash, container hash, model/rule version, and allowed input fields;
* exact event schema, event source owners, clock synchronization standard, UI build hash, and source-to-event mapping;
* all operating thresholds below, without access to P1 route-reference outcomes;
* route-specific estimands, multiplicity plan, maximum accrual, interim schedule, contamination rules, safety definitions, and stopping authority;
* named clinical owner for urgent exceptions and a downtime fallback that always defaults to usual care/manual review;
* prohibition of silent insertion and prohibition of using post-landmark data to calculate a route;
* a change-control rule: any change to eligibility, unit definition, landmark, route, outcome, margin, or estimand creates a new version and requires fresh silent validation. Pure bug fixes require replay of all prior prospective packets and independent confirmation that routes are unchanged; otherwise they are scientific changes.

Thresholds are governance operating requirements chosen before outcome review; they are not estimated harms, utilities, or evidence of patient benefit. Failure yields no-go or additional silent validation, never post hoc threshold relaxation.

## Prospective data contract

### General append-only event envelope

Every P1 and P2 event is immutable and append-only. Corrections create a new event referencing the prior event; no row is overwritten. Required columns and units are:

* `study_event_id` UUID; globally unique.
* `site_id`, `source_system_id`, `source_event_id`, `source_table_or_api`, `source_version` strings.
* pseudonymous `patient_key`, `encounter_key`, and, when applicable, `recommendation_unit_id`, `document_id`, `document_version_id`, `order_id`, `actor_key`, `team_key`, `cluster_period_id`, `randomization_id`.
* `event_type` from the locked vocabulary below.
* `event_time_utc` ISO-8601 UTC with millisecond precision: when the clinical/UI action occurred.
* `recorded_time_utc` UTC milliseconds: when the study collector received it.
* `source_timezone`, UTC offset, source clock identifier, and `clock_sync_error_ms`; all duration analyses use seconds and are reported in hours where specified.
* `event_sequence` monotonically increasing within source; `prior_event_id` for corrections/supersession; `correction_reason`.
* `actor_role`, `patient_location`, `service`, and `care_team` as locked categorical vocabularies; no free-text actor names.
* `payload_schema_version`, encrypted `payload_pointer`, canonicalized `payload_sha256`, and permitted derived fields. Clinical text stays within the governed environment.
* `route_engine_version`, `ui_build_version`, and `study_phase` (`P1_SILENT`, `P2_CONTROL`, `P2_AUTO`, `P2_RECON`).
* `ingest_status`, `duplicate_status`, `linkage_status`, and explicit missing-reason codes. Missing is never converted to absent.

Nightly reconciliation compares source-system counts/hashes to the event ledger. Duplicate source IDs, nonmonotone source sequences, UTC conversion failure, clock error above 1 second for UI/application servers or above 5 seconds for interfaced clinical systems, orphan document versions, or unresolvable encounter linkage are critical-data defects. Source clocks are synchronized to an institutional time service; clock-offset logs are retained.

### Required event vocabulary and payloads

#### Encounter and departure events

* `ADMISSION_OPENED`: encounter, admission type, age eligibility, service/team.
* `SERVICE_TRANSFERRED`: from/to service/team and effective time.
* `DISCHARGE_ORDER_PLACED`, `DISCHARGE_ORDER_CANCELLED`: source order and actor.
* `DEPARTURE_OCCURRED`: actual physical departure time from admission/ADT source; disposition. This is prospective `D_live` and is not inferred from note storage.
* `DEATH_BEFORE_DEPARTURE`, `HOSPICE_COMFORT_TRANSITION`: timestamp and source. These apply the frozen exclusion rubric.

#### Radiology and recommendation events

* `RAD_REPORT_CREATED`, `RAD_REPORT_PRELIMINARY`, `RAD_REPORT_FINALIZED`, `RAD_ADDENDUM_FINALIZED`, `RAD_REPORT_RETRACTED`.
* Each final/addendum payload includes report/version identifiers, `chart/acquisition_time`, authoring completion time, finalization time, first downstream EHR-availability time, modality/body region, report text pointer/hash, reciprocal predecessor/supersession links, and interface-delivery status.
* `RAD_REPORT_AVAILABLE_TO_TEAM`: first verified time the same version can be opened by the responsible inpatient team; source acknowledgment and recipient application. A database write alone is insufficient.
* `RAD_REPORT_VIEWED`: actor/team, report version, UI surface, open/close times, and whether recommendation section was visible. This is descriptive and never required to infer awareness.
* `RECOMMENDATION_UNIT_EXTRACTED`: deterministic unit ID; report/version; target/action/modality; exact due interval in calendar months or due-date range in ISO date; polarity; source character offsets; extraction engine/version; uncertainty flags; reciprocal-chain provenance.
* `RECOMMENDATION_UNIT_SUPERSEDED`: old/new unit IDs, report/addendum link, reason, effective time.

Define live recommendation availability `R_avail,u` as the first `RAD_REPORT_AVAILABLE_TO_TEAM` event for the final operative report/addendum version containing unit `u`. Finalization without verified availability does not start the live opportunity clock. If an addendum materially changes a unit, `R_avail,u` resets to the changed version's availability. The inherited MIMIC `R_store` remains unchanged and is never relabeled as `R_avail`.

#### Discharge-document lifecycle

* `DS_DRAFT_CREATED`; `DS_DRAFT_OPENED`; `DS_DRAFT_CLOSED`.
* `DS_VERSION_SAVED`: document/version IDs, actor/team, timestamp, canonical text hash/pointer, parent version, structured-field hashes.
* `DS_SECTION_EDITED`: section identifier, add/delete/replace operation, source (`manual`, `copy`, `AUTO_UI`, `RECON_UI`, other template), before/after span hashes and character counts. Store protected text separately.
* `DS_SIGN_ATTEMPTED`: immutable event before final commit. The first attempt satisfying live eligibility defines `T_gate`; payload includes document version and actor/team.
* `DS_SIGNED`, `DS_SIGNATURE_RETRACTED`, `DS_ADDENDUM_SIGNED`, `DS_TRANSMITTED`, `DS_PATIENT_PORTAL_RELEASED`, `DS_RECIPIENT_ACKNOWLEDGED` with version IDs and timestamps.
* `DS_FINAL_AT_DEPARTURE`: a derived, reproducible pointer to the latest signed version available at or before `D_live`; missing if none. Later documents never replace it in the primary endpoint.

`T_gate` is the first `DS_SIGN_ATTEMPTED` at or before `D_live` after at least one final eligible unit is available. If no such event occurs, the admission is not silently dropped: it is `LIVE_NO_PREDEPARTURE_LANDMARK`, mapped to timing/unavailable and retained in the all-eligible prospective denominator. A signature attempt after departure is postdeparture. If a material addendum appears after `T_gate` but before `D_live`, the route is invalidated, intervention content is suppressed, and the case is sent to urgent manual reconciliation; this is counted as `POST_GATE_CHANGE`, not reclassified favorably.

For each unit compute `L_u=(T_gate-R_avail,u)/3600` hours. The live ample opportunity rule is `L_u>=24.0` hours for **every** active unresolved unit. `L_u` is a prospective UI-availability clock and neither replaces nor recalibrates retrospective `G_u=DS_store-R_store,u`. Report live sensitivities at 12 and 72 hours, but only 24 hours determines P1/P2 eligibility.

#### Gate execution and provenance

* `GATE_INPUT_FROZEN`: complete list of event IDs and document/report versions available at `T_gate`, packet hash, prohibited-post-landmark scan result.
* `GATE_EXECUTED`: execution ID, engine/container/rules hash, start/end UTC, every unit state, uncertainty bit, admission route, reason codes, and computational error status.
* `GATE_ROUTE_SUPPRESSED`: reason (`critical_missing`, `clock_failure`, `post_gate_change`, `downtime`, `version_mismatch`, `safety_hold`). Suppression defaults to no automated content and manual/usual care.
* In P1, `GATE_EXECUTED` is written only to a restricted study ledger and cannot be delivered to treating clinicians, discharge templates, orders, trackers, or patient-facing systems.

#### UI exposure and clinician confirmation, P2 only

* `ROUTE_UI_ASSIGNED`: randomized condition, route stratum, cluster period, eligibility snapshot, and delivery status.
* `ROUTE_UI_RENDERED`: exact UI build, route, document/report versions, displayed fields, actor/team, screen open time.
* `ROUTE_UI_NOT_RENDERED`: reason including control assignment, downtime, clinician role, or stale version.
* `ROUTE_UI_ACTION`: one of `ACCEPT_EXACT`, `EDIT_AND_ACCEPT`, `REJECT`, `DEFER`, `ESCALATE_RECON`, `CLOSE_NO_ACTION`; action time and actor.
* `CLINICIAN_UNIT_CONFIRMATION`: for each unit, explicit values for `target_same_patient` (yes/no/uncertain), `recommendation_active` (yes/no/uncertain), `action_modality_confirmed`, `timing_confirmed`, `responsible_team_confirmed`, `outside_or_superseding_plan` (none/present/uncertain), `patient_preference_or_competing_context` (none/present/uncertain), and `final_disposition` (propagate/edit/reconcile/non-pursuit/defer). Actor must be a credentialed clinician on the responsible team. Timestamp and source report/document versions are mandatory.
* `CLINICIAN_REASON`: mandatory structured reason plus optional governed text for every edit, rejection, deferral, non-pursuit, uncertainty, or escalation. Reasons include wrong target, recommendation changed, already scheduled, outside plan, guideline/clinical disagreement, patient preference, competing illness, responsibility unclear, duplicate, insufficient context, and other.
* `CONTENT_INSERT_REQUESTED`, `CONTENT_INSERTED`, `CONTENT_INSERT_FAILED`: exact source unit/version, destination document/version, inserted span hash, actor, and confirmation event ID.
* `RECON_DECISION_RECORDED`: selected final state (`same plan`, `more protective plan`, `definitive replacement`, `informed non-pursuit`, `conflict unresolved`, `defer`), target/action/timing/accountable team, evidence source, actor, and time.

For `A_AUTO`, the UI may display a source-linked structured payload but cannot write it to the draft until the treating clinician confirms **all** unit fields and chooses `ACCEPT_EXACT` or `EDIT_AND_ACCEPT`. Inserted text remains editable and visually source-attributed until signature. No default-selected confirmation, bulk admission acceptance, timer acceptance, background insertion, or order placement is allowed. A clinician's edit is retained as an outcome, not overwritten by the engine.

For `A_RECON`, the UI displays the operative report/addendum beside the current draft and relevant contemporaneous target-linked plan evidence, highlights the disagreement/incompleteness without recommending a preferred clinical answer, and requires the clinician to record a final plan or explicit unresolved/defer state. It cannot copy a plan independently. `A_MIXED` always receives reconciliation UI for the whole admission.

Clinician confirmation is a measured decision and an intervention component, not ground truth. Independent endpoint adjudicators remain blinded to assignment, system route, UI actions, and downstream outcomes when judging departure-frozen plan state.

#### Responsibility, communication, ordering, and completion

* `RESPONSIBILITY_OFFERED`, `RESPONSIBILITY_ACCEPTED`, `RESPONSIBILITY_DECLINED`: named team role (not free-text person), time, channel.
* `TARGET_ORDER_PLACED`, `TARGET_ORDER_CANCELLED`, `TARGET_REFERRAL_PLACED`, `TARGET_APPOINTMENT_SCHEDULED`: unit ID, order/referral/schedule ID, modality, due window, actor, time, source version, and deterministic linkage rule.
* `HANDOFF_SENT`, `HANDOFF_RECEIVED`, `PATIENT_COMMUNICATION_DOCUMENTED`: recipient role, channel, time, unit ID. Receipt requires a system acknowledgment or explicit recipient action, not merely send status.
* `FOLLOWUP_COMPLETED`, `FOLLOWUP_OUTSIDE_ATTESTED`, `FOLLOWUP_UNKNOWN`, `DEATH_BEFORE_DUE_WINDOW`: unit-linked source and time. These are secondary and require validated linkage; absence is unknown, not failure.

Target linkage must be deterministic from unit ID or independently adjudicated. Generic orders/referrals cannot be credited. MIMIC POE is not used to validate this linkage.

#### Safety, burden, and contamination events

* `WRONG_PATIENT_CONTENT`, `WRONG_TARGET_CONTENT`, `STALE_RECOMMENDATION_PRESENTED`, `CONFLICTING_PLAN_INSERTED`, `INAPPROPRIATE_PLAN_ADJUDICATED`, `URGENT_DIAGNOSIS_DELAY_CONCERN`, `DISCHARGE_DELAY_ATTRIBUTED`, `PATIENT_DISTRESS_CONCERN`, `PRIVACY_SECURITY_EVENT`, `SERIOUS_ADVERSE_EVENT_REVIEW`.
* `ALERT_SHOWN`, `ALERT_DISMISSED`, `TIME_IN_UI_MS`, number of clicks, edits, escalations, and interruption count.
* `CONTROL_UI_EXPOSURE`, `CONTROL_PAYLOAD_COPY`, `OFF_PROTOCOL_TRACKER_USE`, `CONCURRENT_HANDOFF_INTERVENTION`, `CROSS_TEAM_ACTOR`, `ROUTE_CROSSOVER`, `INTERVENTION_NONDELIVERY`.

All safety events retain reporter, discovery time, admission/unit denominator, severity, relatedness categories (`unrelated`, `possible`, `probable`, `definite`), independent adjudication, and resolution. Safety reports are never hidden by later correction.

### Required prospective relational files

The executable study export contains at least:

1. `screening.csv`: one row per radiology-finalized admission candidate, including every inclusion/exclusion reason and timestamp.
2. `admissions.csv`: one row per frozen prospective eligible admission, `patient_key`, `encounter_key`, site/service/team, admission/departure times, first-eligible indicator, and all-denominator state.
3. `events.parquet`: append-only envelope above.
4. `report_versions.parquet`, `recommendation_units.parquet`, `document_versions.parquet`: source/version graph and hashes.
5. `gate_runs.parquet`: frozen inputs, unit states, routes, reasons, versions, errors.
6. `randomization.csv`: cluster-period schedule and admission assignment; write-protected and independently generated.
7. `ui_actions.parquet`, `clinician_confirmations.parquet`, `linked_actions.parquet`.
8. `reference_labels.parquet`: individual adjudicator labels, evidence pointers, uncertainty, consensus only as secondary.
9. `safety_events.parquet`, `contamination.parquet`, `source_reconciliation.parquet`.
10. `analysis_manifest.json`: source hashes, row counts, schema versions, code/container hashes, exclusions, frozen thresholds, and output hashes.

Join keys are pseudonymous `(patient_key,encounter_key)`; unit outcomes add `recommendation_unit_id`; document events add `(document_id,document_version_id)`; report events add `(report_id,report_version_id)`; P2 assignment adds `cluster_period_id,randomization_id`. A verifier must reject many-to-many joins not declared in the version graph.

## Phase P1: consecutive prospective silent validation

### Population, temporal boundaries, and denominators

P1 begins only after a two-week engineering shakedown using synthetic records; no real shakedown admission contributes to analysis. Then enroll all consecutive adult admissions at participating sites during a maximum of 12 months that trigger the pulmonary recommendation retrieval pathway. Freeze and publish the full screening cascade.

Apply the same clinical eligibility rubric as retrospective `N_A`, including first eligible admission per patient during P1, exact 3/6/12-calendar-month unconditional chest/thoracic CT recommendation, reciprocal final/addendum logic, and exclusions. Prospectively, however, the source of truth is the live report-version graph and `R_avail`, not MIMIC storage. The all-eligible silent denominator is `N_P1`: every first live admission whose operative recommendation is finalized and available by `D_live`, regardless of whether a predeparture signature attempt, complete event packet, ample lead time, or determinate route exists. Thus implementation failure cannot improve route accuracy by denominator deletion.

Partition `N_P1` exhaustively into:

* `P1_ROUTE_ELIGIBLE`: `T_gate<=D_live`, all active unresolved units have `L_u>=24h`, no critical missing event, and a route run completed;
* `P1_TIMING`: at least one active unresolved unit has `L_u<24h`, no predeparture landmark, or a material post-gate change;
* `P1_DEFER_DATA`: critical event/linkage/clock/version uncertainty;
* `P1_RESOLVED_NOACTION`: all units resolved/closed under the frozen reference;
* other frozen exclusion/unknown states retained in the screening cascade.

Report all route confusion matrices both over `P1_ROUTE_ELIGIBLE` and per 100 `N_P1`. Never report accuracy only after removing system errors or defers.

### Silent operation and reference standard

The gate executes at `T_gate` but its route and extracted payload are inaccessible to treating teams and cannot alter documents, orders, lists, alerts, or communication. Existing care proceeds unchanged. Access logs are audited; any treating-team access is contamination and temporal leakage.

Within 72 hours after departure, at least two independent physicians with pulmonary-nodule and discharge-workflow expertise review a packet frozen to events and chart content available by `T_gate`. They are blinded to gate route, UI/log outputs, later signed-document changes after the reference boundary, assignment (none in P1), downstream actions, and outcomes. They enumerate units and independently assign observable context, superseding-plan, content, uncertainty, and the deterministic reference route using the same codebook. They may inspect live fields unavailable in MIMIC—verified report availability, contemporaneous structured responsibility, active target-linked orders/schedules, and documented outside plans—but cannot infer missing facts. Pre-consensus labels remain primary compatible sets; consensus is secondary. A separate adjudicator, blinded to gate output, reviews route disagreements. Clinical appropriateness is recorded as `not adjudicable`, `review needed`, or an expert safety concern; route accuracy does not convert expert opinion into truth.

P1 primary unit is the admission. Patient and clinical team/site are clustering levels. Recommendation-unit accuracy is secondary and uses admission/patient cluster weights.

### P1 route-specific estimands

For route `r`, let `G_r` be gate nominations and `R_r` independent reference-compatible assignments. Unknown-compatible adverse assignments are primary.

1. **Automation PPV:** `PPV_AUTO=P(reference=A_AUTO | gate=A_AUTO)` over all gate `A_AUTO`, with reference uncertainty assigned non-auto. Denominator is every gate `A_AUTO`, including missing reference as nonconfirming in the primary bound.
2. **Unsafe automation nomination rate:** `UAN_AUTO=P(reference in {A_RECON,A_MIXED,A_DEFER,A_TIMING,A_CLOSED/NOACTION} | gate=A_AUTO)`. Report both per gate `A_AUTO` and per `N_P1`. A mere reference omission-unit match does not rescue an admission-level unsafe nomination.
3. **Mixed-admission miss:** `MM_AUTO=P(gate=A_AUTO | reference=A_MIXED)` and the fraction of gate auto admissions containing any reference conflicting/incomplete unit.
4. **Automation sensitivity/yield:** `P(gate=A_AUTO | reference=A_AUTO)` and `100*n(gate=A_AUTO)/N_P1`; these measure missed workload and feasibility, not safety.
5. **Reconciliation PPV:** `PPV_RECON=P(reference in {A_RECON,A_MIXED} | gate=A_RECON)`, uncertainty adverse.
6. **Reconciliation sensitivity/yield:** `P(gate=A_RECON | reference in {A_RECON,A_MIXED})` and per 100 `N_P1`.
7. **Under-routing to no-action:** `P(gate in {A_AUTO,A_NOACTION} | reference=A_RECON/A_MIXED)` and separately all dangerous direction changes.
8. **Deferral and timing rates:** `P(gate=A_DEFER)`, `P(P1_DEFER_DATA)`, `P(P1_TIMING)` per `N_P1` with reasons.
9. **Route agreement:** full confusion matrix, raw exact agreement, category-specific agreement, AC1 and kappa, plus route stability under each individual reference reviewer and compatible assignment.
10. **Event integrity:** critical-event completeness, source reconciliation, duplicate/orphan rate, clock failures, post-landmark input rate, route execution latency, and proportion with route ready before sign completion.
11. **Calibration/drift:** route metrics by site, terminal service, month, 3/6/12-month interval, one versus multiple units, and clinician team, with simultaneous intervals. These are validation checks, not subgroup claims of benefit.

Use simultaneous one-sided 95% confidence bounds from a patient-cluster bootstrap stratified by site, with clinical-team resampling sensitivity and at least 10,000 replicates. One max-statistic family covers the two lane PPVs, unsafe auto nomination, mixed miss, dangerous under-routing, critical missingness, leakage, route latency failure, and site drift. Report exact binomial bounds as sensitivity where clustering is absent. No lane passes based on consensus-only estimates.

### Governance-locked P1 gates

All thresholds below are locked before P1 enrollment and cannot be relaxed after seeing labels. They are operational validation requirements, not clinical utility weights.

#### Global gates required for any P2 lane

* At least 100 total gate-positive route admissions and at least 30 gate-positive admissions for each lane proposed for P2, or the 12-month maximum is reached. Fewer events is inconclusive/no-go for that lane, not evidence of absence.
* Critical event/linkage/version/clock completeness is at least 98%; its simultaneous one-sided lower 95% bound must be at least 0.98. No wrong-patient linkage is allowed.
* Post-`T_gate` input leakage and treating-team access to silent routes are zero observed; if the one-sided 95% upper bound exceeds 0.01, progression stops pending a new silent version.
* At least 90% raw exact route agreement and AC1 at least 0.70; individual-reviewer-compatible assignments cannot cross pass/fail.
* Monthly missingness or route-rate drift cannot differ from the first three complete months by more than 0.10 absolute after case-mix standardization; no site may have a dangerous-route error upper bound above 0.10. A site that fails is excluded from P2 only through a predeclared site-specific no-go, never by removing its P1 rows from pooled reporting.
* At least 95% of completed gate runs finish before the corresponding `DS_SIGNED` event, with lower 95% bound at least 0.95; median computation time no more than 2 seconds and 99th percentile no more than 10 seconds. This is engineering feasibility, not benefit.
* Source reconciliation is at least 99.5% each month, no unresolved duplicate report/document identities, and route replay from frozen inputs is bit-for-bit identical.

#### `A_AUTO` advancement gates

All must pass:

* simultaneous one-sided lower 95% bound `PPV_AUTO >=0.90`;
* simultaneous one-sided upper 95% bound `UAN_AUTO <=0.05`;
* simultaneous upper bound for mixed-admission miss `MM_AUTO <=0.10`;
* no observed wrong-patient, wrong-target, or post-gate superseded recommendation in a gate `A_AUTO` nomination;
* lower 95% bound for automation sensitivity at least 0.70 and lower bound for yield above zero, ensuring the lane is not a trivially pure near-empty subset;
* the inherited prospective purity condition remains satisfied: upper bound `D_MIX<=0.10` under live reference labels;
* the same pass result under every primary reviewer-compatible and unknown-adverse assignment, at 12-hour and 72-hour displayed sensitivities without directionally contradictory errors. The 24-hour rule remains primary.

Failure of any auto gate is an `AUTO_NO_GO`. It does not block a qualified reconciliation trial. A new auto algorithm/version must repeat P1 from zero prospective validation admissions; it cannot reuse outcomes for threshold tuning and confirmation.

#### `A_RECON` advancement gates

All must pass:

* simultaneous one-sided lower 95% bound `PPV_RECON >=0.80`;
* lower bound for reconciliation sensitivity at least 0.70;
* simultaneous upper bound for dangerous under-routing of reference `A_RECON/A_MIXED` to gate `A_AUTO/A_NOACTION` at most 0.05;
* lower bound for reconciliation yield above zero and at least 30 gate-positive admissions;
* route remains reconciliation under every reviewer-compatible and unknown-adverse assignment.

Failure is `RECON_NO_GO`, independent of the auto lane.

### P1 staged decisions

* **Both lanes pass:** proceed to a two-lane P2 with separate strata, outcomes, margins, and conclusions.
* **Only auto passes:** P2 may evaluate clinician-confirmed structured prepopulation only; reconciliation remains usual care/manual workflow and no inference is made about a reconciliation aid.
* **Only reconciliation passes:** P2 may evaluate side-by-side reconciliation only. This is the required outcome if automation purity or mixed-admission safety fails.
* **Neither passes:** no content workflow trial. Perform root-cause review; a materially changed gate requires a new P1.
* **Inconclusive:** maximum accrual reached with wide bounds, sparse route, reviewer instability, or unresolved data defects. Do not pool routes or loosen thresholds. A prespecified extension may add sites, but thresholds and version remain unchanged and prior rows remain included.

An independent validation committee, not the algorithm developers or treating teams, certifies the gate decision from locked outputs.

## Phase P2: governed route-stratified workflow trial

### Entry and population

P2 begins only after written independent certification of at least one P1 lane. P1 admissions are excluded from P2. Enroll every consecutive first eligible admission for the patient in a validated route during a maximum 24-month trial at P1-qualified sites. Eligibility and route are frozen at `T_gate`; randomization never changes the route. `A_TIMING`, `A_DEFER`, `A_NOACTION`, invalidated post-gate cases, and nonvalidated lanes receive usual care and remain in a screened observational ledger but are not randomized.

The P2 all-randomized denominator for lane `r`, `N_P2,r`, is every admission assigned within that route, including intervention nondelivery, clinician rejection, crossover, downtime after assignment, signature after departure, death/transfer after assignment, missing endpoint, and contamination. Missing primary outcomes are adverse in the primary binary analysis and addressed by prespecified bounds/sensitivity; they are never deleted.

### Randomization and contamination-resistant design

Use a pragmatic cluster-period design because patient-level UI exposure would readily contaminate control care. The randomization unit is the `site × responsible discharge service-team × 14-calendar-day period`. Before P2, an independent statistician creates concealed, reproducible permuted blocks of four periods within site and service-family, assigning two intervention-enabled and two usual-care periods. Assignment is released to the deployment service only at period start; outcome adjudicators remain blinded. All eligible admissions in a cluster period receive the period condition. A clinician crossing teams retains the admission's assigned condition; cross-team actors are recorded.

Intervention periods enable only P1-validated lane(s). Control periods retain usual care and cannot render route payloads. The backend still runs silently in controls solely to define the locked route; treating-team access is blocked and audited. There is no washout deletion. Period, site, service, calendar month, and cluster are retained in analysis. At least 12 independent service-team clusters and at least 40 cluster periods per tested lane are required for a positive claim; otherwise inference is inconclusive regardless of admission count.

Contamination is measured in both directions:

* control exposure: any route UI render, payload copy, study-specific tracker entry, or access to restricted route data;
* intervention nonexposure: eligible assigned intervention without UI render before signature;
* clinician carryover/cross-team exposure; concurrent nodule initiatives; route crossover; manual use of copied report text in controls.

Primary analysis is assignment-based intention-to-treat. No per-protocol analysis may replace it. A secondary treatment-received estimate may be reported only with explicit assumptions and cannot rescue a failed ITT result. If more than 10% of control admissions are directly exposed to the intervention UI/payload or the absolute control-exposure minus intervention-nondelivery contrast exceeds 0.10, the affected lane is contamination-inconclusive. Any wrong-condition software delivery pauses enrollment.

### Route-specific interventions

#### Validated `A_AUTO`: clinician-confirmed structured prepopulation

At `T_gate`, display the exact source-linked target, chest/thoracic CT action, 3/6/12-month due window/date, and proposed accountable team for every unit. Require unit-by-unit confirmation and an explicit accept/edit/reject/defer/escalate action. Only accepted content can be inserted into the current draft version; no order is placed automatically. A disagreement, uncertainty, changed report, or multiunit interaction converts the UI to manual reconciliation and is retained as an auto-lane intervention outcome, not relabeled into the recon trial stratum.

#### Validated `A_RECON`: side-by-side clinician reconciliation

At `T_gate`, display the operative source report/addendum, current discharge-plan text, and the exact element(s) missing or conflicting. Do not recommend which clinical plan is correct. Require a documented final disposition and responsibility or explicit unresolved/defer state before the UI can be closed, but do not block emergency departure or signature; bypass is always possible and recorded. No content or order is inserted without active clinician action.

### Independent endpoint adjudication

For every randomized admission, two blinded experts review a packet frozen at `D_live` containing the operative report/version, clinical context permitted by the codebook, and final signed artifact available by departure. They do not see assignment, route engine output, UI events/actions, study-generated source tags, cluster period, later orders/completion, or outcomes. Study-specific visual markers are removed. They classify each unit and admission under the frozen hierarchy, identify inappropriate/conflicting/wrong-target content, and state missing facts. Individual labels and compatible bounds are primary; consensus is secondary. A separate safety panel can access UI provenance and clinical outcomes after endpoint labels are frozen.

### P2 primary route-specific estimands and denominators

All estimands are admission-level cluster-period intention-to-treat risk differences, intervention-enabled minus usual-care, standardized only to the randomized lane distribution. Use small-sample-corrected GEE or randomization-based inference with service-team cluster and period, site/service stratification, and patient clustering if a patient is inadvertently randomized twice; the protocol otherwise retains first eligible P2 admission. Report unadjusted cluster-weighted risk differences as a robustness check. Recommendation-unit results are secondary with admission-level weights.

#### `A_AUTO` lane

* **Benefit endpoint `Q_AUTO`:** departure-frozen final signed artifact contains for every active unit a reference-compatible target, chest/thoracic CT action, exact compatible timing/date, and accountable recipient/team, or an explicit reference-compatible resolution, with no conflicting unit. Denominator: every randomized `A_AUTO` admission.
* **Primary benefit estimand:** `RD_Q_AUTO=P(Q_AUTO=1|Z=intervention)-P(Q_AUTO=1|Z=control)`.
* **Safety endpoint `S_AUTO`:** any intervention-compatible wrong-patient/wrong-target insertion, stale/superseded recommendation, inappropriate surveillance plan, less-protective unexplained conflict, or copied plan despite a documented preference/competing-context contraindication, as independently adjudicated. Missing safety review is adverse. Denominator: every randomized `A_AUTO` admission.
* **Primary safety estimand:** `RD_S_AUTO=P(S_AUTO=1|Z=intervention)-P(S_AUTO=1|Z=control)`.

The auto workflow is successful only if the simultaneous two-sided 95% lower bound for `RD_Q_AUTO` is greater than **+0.10** and the one-sided 95% upper bound for `RD_S_AUTO` is less than **+0.02**. Both conditions are intersection-union requirements. The +0.10 material benefit and +0.02 safety noninferiority margins are governance choices locked before P1 outcome review; they are not derived from MIMIC.

#### `A_RECON` lane

* **Benefit endpoint `Q_RECON`:** by departure the signed artifact contains one internally consistent, target-linked final disposition—compatible surveillance with exact action/timing/responsibility, explicit definitive replacement, explicit informed non-pursuit, or explicit unresolved/defer with accountable follow-up—without unexplained competing plans. Denominator: every randomized `A_RECON`, including `A_MIXED`, admission.
* **Primary benefit estimand:** `RD_Q_RECON` defined analogously.
* **Safety endpoint `S_RECON`:** any new or retained wrong-target, internally conflicting, unjustified less-protective, or falsely resolved plan attributable or potentially attributable to the workflow, plus any urgent concern that reconciliation delayed a more immediate diagnostic action. Missing safety review is adverse. Denominator: every randomized `A_RECON` admission.
* **Primary safety estimand:** `RD_S_RECON`.

The reconciliation workflow succeeds only if the simultaneous lower bound for `RD_Q_RECON` is greater than **+0.10** and the one-sided upper bound for `RD_S_RECON` is less than **+0.02**. `A_MIXED` is reported separately but cannot be removed from `A_RECON`.

No weighted or pooled auto-plus-recon composite is primary. One route may be supportive and the other adverse.

### Secondary estimands

For each lane, all per randomized admission unless explicitly unit-based:

* accepted content fidelity at `DS_SIGNED` and at `D_live`; no predeparture signed artifact;
* clinician accept/edit/reject/defer/escalate proportions and structured reasons;
* responsibility accepted; target-linked order/referral/scheduling by 7 days; verified handoff receipt by 7 days;
* UI time in minutes, clicks, alerts, correction burden, and attributed discharge delay in minutes;
* route crossover and post-gate report change;
* inappropriate content per UI-rendered admission and per inserted unit, secondary denominators shown alongside all-randomized rates;
* completion within the recommended due window plus 30 days, with death as a competing event and outside/unknown capture explicit. This is descriptive unless cross-system ascertainment meets a separately locked 95% completeness gate;
* patient communication and patient-reported understanding where consented and separately approved;
* heterogeneity by site and prespecified one/multiple-unit and 3/6/12-month strata, interaction estimates with multiplicity control, never a subgroup deployment rule.

Mediators such as UI acceptance, order placement, or responsibility acceptance are not adjusted for in the primary causal estimand.

### Sample-size lock and multiplicity

Before P2 enrollment, an independent statistician who sees only blinded pooled P1 rates, route prevalence, site/service cluster sizes, and intracluster correlation—not lane-by-gate performance or any P2 outcome—computes a fixed lane-specific sample size for 90% power to detect `RD_Q=+0.10` at two-sided familywise alpha 0.05, inflated for cluster-period design and 10% missingness. Safety precision must also permit a one-sided 95% upper bound below +0.02 under the planned event rate. The larger requirement determines the lane sample. The sample-size formula, nuisance inputs, integer cluster-period allocation, and simulation seed are escrowed before the first P2 assignment.

Caps are 1,200 randomized admissions per lane, 80 cluster periods per lane, and 24 months. The cap cannot be extended after unblinded results. If planned power/precision cannot be achieved under the cap, that lane does not open. If accrual stops at the time cap before fixed N, results are inconclusive unless a prespecified safety/harm boundary was crossed.

Use a closed testing/intersection-union strategy. Within each route, benefit superiority and safety noninferiority must both pass. Across the two route benefit hypotheses, use Holm control at two-sided familywise 0.05; safety retains one-sided 0.025 confidence limits and cannot be traded against benefit. Secondary outcomes use false-discovery-rate control within named families and are not allowed to overturn primary failure.

### Monitoring and stopping

An independent data and safety monitoring board reviews blinded operations monthly and unblinded safety at 25%, 50%, and 75% of planned lane information. One formal benefit/futility interim occurs at 50% using a prespecified Lan-DeMets O'Brien-Fleming efficacy boundary and a binding futility rule: stop a lane if conditional power for meeting **both** benefit and safety criteria is below 20%, calculated under the locked +0.10 effect. Early benefit declaration is prohibited until at least 50% information, at least 20 cluster periods, and all safety adjudication through 30 days are complete.

Immediate automatic pause for the affected lane/site occurs upon:

* any silent/background insertion without a valid `CLINICIAN_UNIT_CONFIRMATION`;
* any wrong-patient content delivery or route shown under the wrong randomized condition;
* two wrong-target insertions, stale/superseded presentations, or probable workflow-related serious safety events;
* one probable or definite serious harm involving delayed urgent diagnosis, inappropriate surveillance after documented non-pursuit, privacy breach, or a discharge delay with clinical deterioration;
* critical event completeness below 95% in a rolling month, source reconciliation below 99%, irreproducible gate replay, or clock/version failure affecting route order;
* control direct exposure above 10%, intervention nondelivery above 20%, or concurrent workflow changes that make the randomized contrast uninterpretable;
* monthly median attributed UI time above 10 minutes or 95th percentile discharge delay above 30 minutes for two consecutive reviews.

The board adjudicates restart only after root-cause correction and replay. A changed route/UI affecting content semantics requires a new P1; operational recovery with an identical content/route replay may resume under the original P2 version. All pauses remain in the trial timeline and all assigned admissions remain in ITT.

Stop for harm if the one-sided repeated-confidence lower bound for `RD_S` exceeds +0.02 or the DSMB determines a probable serious safety imbalance. Stop for futility under the binding rule. No sample-size increase, margin change, route pooling, endpoint substitution, or favorable exclusion is permitted.

## Falsification and adversarial verification across P1 and P2

1. **Retrospective immutability:** source hashes, schema hashes, `N_A`, first-admission rule, reciprocal chains, canonical `DS`, `Y`, `G`, `V/H/Z`, `E_A`, unit definitions, route logic, comparators, uncertainty bounds, and noncausal conclusions must reproduce the selected parent. Prospective data cannot rewrite MIMIC states.
2. **Prospective all-denominator invariance:** every screened candidate has one cascade state; every `N_P1` admission has one live status; every randomized admission remains in exactly one lane and assignment arm. System errors and missing endpoints remain in denominators.
3. **Clock ordering:** synthetic and real checks verify `R_avail,u <= T_gate <= D_live` for route-eligible rows and `L_u=(T_gate-R_avail,u)/3600`. Finalization without availability, signature after departure, and material post-gate addenda cannot be miscalled ample opportunity.
4. **Departure freeze:** inject later notes/orders/outcomes into packet stores; route and primary endpoint code must reject them. Later faithful documentation cannot upgrade P1 route accuracy or P2 departure outcome.
5. **Version graph:** retracted/superseded report and document versions cannot remain operative. Orphan or cyclic links suppress route.
6. **Unit boundary:** shared action/window is one unit; different windows are separate; repeated wording is deduplicated; unresolved coreference defers. Duplicating a unit cannot change admission route or bootstrap weight.
7. **Worst-case routing:** one conflict plus one omission is `A_MIXED/A_RECON`, never `A_AUTO`; uncertainty, missing critical context, or reviewer route disagreement prevents auto.
8. **No direct route voting:** reviewers assign evidence states; frozen code derives route. P1/P2 endpoint adjudicators cannot see engine route or UI.
9. **No silent insertion:** attempt content insertion without an active credentialed confirmation event; transaction must fail and trigger safety pause. Default selections, expired sessions, bulk acceptance, and wrong document versions also fail.
10. **Clinician rejection fidelity:** rejection/edit/escalation remains an intervention outcome and cannot be relabeled as algorithm error or removed from ITT.
11. **Randomization:** independently recreate cluster-period sequence from seed; detect allocation changes, control UI render, intervention suppression, cross-team access, and concurrent initiative exposure.
12. **Contamination:** synthetic 11% direct control exposure must force contamination-inconclusive even with a favorable endpoint; 9% is reported but does not automatically fail unless other gates do.
13. **Route separation:** favorable auto results cannot rescue failed recon safety or vice versa; route pooling and recommendation-unit weighting must be rejected.
14. **Intersection-union:** large fidelity improvement with safety upper bound `>=+0.02` is adverse/no success; safe but benefit lower bound `<=+0.10` is inconclusive or null, never supportive.
15. **Missingness:** missing reference or safety outcome is adverse in primary bounds. Complete-case favorable reversal cannot produce success.
16. **Stopping:** verify information fractions, alpha spending, conditional-power rule, time/N caps, and that all pre-stop randomized admissions remain analyzed.
17. **Unsupported conclusions:** a correct favorable process result described as reducing cancer mortality, proving guideline appropriateness, or improving completion without complete follow-up must fail verification. A correct adverse or inconclusive interpretation must pass even if it opposes the hypothesis.
18. **P1/P2 separation:** P1 admissions cannot enter P2; P1 route thresholds cannot be changed from P1 outcomes; a new semantic gate/UI version must not borrow prior validation.
19. **Site drift:** a failing site cannot disappear from pooled P1 reporting. Site-specific P2 exclusion follows only the locked no-go rule.
20. **MIMIC/prospective modality boundary:** any code attempting to infer live viewing, UI exposure, clinician confirmation, randomization, outside plans, communication receipt, or intervention effects from MIMIC fields must fail.

## Supportive, adverse, and inconclusive interpretations

### P1

**Supportive** means a named lane passes every global and lane-specific gate under simultaneous, reviewer-compatible, unknown-adverse analysis. It supports only opening that lane in P2 with the locked UI; it does not support clinical deployment or benefit.

**Adverse to automation** includes unsafe/reference-reconciliation nominations above margin, mixed-admission misses, wrong-target/stale nominations, trivial near-zero yield, route instability, or inability to freeze all unit clocks. The correct consequence is auto no-go; reconciliation may still advance. **Adverse to reconciliation** includes poor identification, dangerous under-routing, or inability to display a neutral, complete comparison. Global temporal, linkage, privacy, or replay failure is adverse to all lanes.

**Inconclusive** includes maximum accrual with sparse routes, wide simultaneous bounds, excessive unknowns, reviewer incompatibility, site drift, or incomplete prospective event capture. It does not justify threshold relaxation or route pooling.

### P2

**Supportive for an auto workflow** requires both `RD_Q_AUTO` superiority beyond +0.10 and `RD_S_AUTO` noninferiority below +0.02, with contamination, cluster, completeness, and stopping integrity intact. The strongest claim is that, in P1-qualified sites and prospectively gate-nominated auto admissions, availability of clinician-confirmed structured prepopulation improved departure-frozen signed-plan quality without exceeding the prespecified process-safety margin during the trial.

**Supportive for reconciliation** requires its separate benefit and safety conditions. A supportive recon result with adverse auto results supports reconciliation only, not a two-lane deployment.

**Adverse** includes a safety-margin failure, wrong-patient/silent insertion, serious probable harm, benefit in the wrong direction, excessive discharge burden, or contamination that plausibly destroys the randomized contrast. A process intervention can be accurate in P1 and harmful or ineffective in P2.

**Inconclusive** includes benefit lower bound not exceeding +0.10 despite no demonstrated harm, underaccrual, too few clusters, wide safety bounds, contamination above limits, missing endpoint capture, or early futility. Failure to prove superiority is not proof that usual care is equivalent. Safety noninferiority alone is not benefit.

A supportive P2 process result still does not show more completed CT, earlier cancer diagnosis, improved survival, cost-effectiveness, or net clinical benefit. Those stronger claims require validated cross-system longitudinal capture, longer follow-up, patient-centered outcomes, health-economic inputs, expert review, and a separately powered study.

## What changed and what remains uncertain

The parent ended with a broad requirement for silent validation and a route-stratified governed trial. This child makes that requirement prospectively executable without reopening retrospective science. It defines the exact live landmark, report-availability and document-version clocks, append-only event contract, UI transaction rules, active clinician confirmation, all-denominator prospective states, independent references, lane-specific accuracy and causal estimands, locked go/no-go margins, cluster-period assignment, contamination measurement, sample-size lock, safety monitoring, stopping, adversarial checks, and route-specific interpretations.

The substantive advance is not another classifier. It is a falsifiable bridge from retrospective chart QA to two sequential prospective decisions: first whether the gate is valid enough to expose clinicians, then whether either route-specific workflow improves a clinically meaningful handoff process safely. Automation can fail while reconciliation proceeds; accuracy can pass while intervention effect fails; and neither process result is promoted into patient benefit.

Uncertainty remains material. The proposed operating margins require governance ratification and may render the study infeasible; live eligible routes may be rare; report availability and physical departure interfaces may be unreliable; clinicians may cross teams; reference reviewers may disagree; site workflows may limit transport; and even a faithful signed plan may not produce communication, scheduling, completion, or benefit. Those are prospective results to be measured, not facts available in MIMIC.
