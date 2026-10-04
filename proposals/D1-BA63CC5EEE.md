# Prospective-silent bridge with separate documentation and actionability estimands

## Status, parentage, and scope

This is a targeted child of `[prior hypothesis]`. It preserves every inherited decision-defining element: the first-eligible adult one-admission-per-subject pulmonary opportunity population; the all-opportunity denominator; reciprocal pre-`D` radiology chronology; the exact canonical `DS` artifact; the inherited unit clocks and exhaustive `Y,V,H,Z` states; exact atom `g=(E, terminal curr_service, W)`; all-unit adverse routing and `AUTO`/`RECON`/`TIMING`/`DEFER` precedence; route-blinded panels; the positive-probability two-phase design; the <=900-admission and <=300-challenge retrospective workload ledger; compatible-set partial identification; finite-population inference; no-rescue rules; and the noncausal, prospective-silent conclusion ceiling.

Nothing in this amendment changes the retrospective population, sampling strata, inclusion probabilities, route predicate, atom, time boundary, or retrospective estimand. It adds a separately sealed **bridge protocol** that may be run only after a retrospective allow-list has been selected. The bridge does not feed labels, workflow observations, or outcomes back into retrospective route certification. It makes the next decision clinically informative by separating four questions that the MIMIC files cannot answer:

1. **Documentation reproducibility:** can an independent reviewer reconstruct the route-defining unit and route from the specified artifact?
2. **Clinical actionability:** given the complete contemporaneous clinical context, is the candidate plan actionable, actionable only after clarification, not actionable, or impossible to judge?
3. **Workflow delivery:** was the information actually visible to and acted upon by the responsible team, with a traceable order/referral or communication when one was required?
4. **Observed outcomes:** what happened during prespecified follow-up, including completion and adverse events, without attributing those outcomes to the silent route?

The bridge is silent: no generated route, warning, ranking, or recommendation may be shown to clinicians, patients, or operations staff, and no care may be delayed, changed, or withheld. A bridge result can support only a later governance decision to design an interventional or non-silent study; it cannot establish safety, benefit, appropriateness, or causality.

The bridge protocol hash, codebooks, source-field manifest, enrollment rule, packet transformations, adjudication roster, missingness codes, analysis code, and stopping rules must be signed and sealed before the first bridge encounter is enrolled and before any bridge reviewer sees a case. The generated route and retrospective panel results remain sealed until documentation and actionability labels, workflow extraction, and the outcome follow-up window are all append-only sealed.

## Strongest supported and unresolved claims

The available MIMIC evidence supports construction of a reproducible, admission-linked artifact frame and an observable documentation-audit functional. It supports use of `hosp/services.curr_service` and pre-discharge ICU exposure as frozen workflow **proxies** for the retrospective atom. It does not establish actual visibility at departure, finalization or signature semantics, responsible-team identity, communication, order or referral execution, scheduling, patient preference, appropriateness, follow-up, harm, utility, or benefit. The shifted dates cannot support cross-subject calendar comparisons.

The unresolved claim is narrower and falsifiable: among the exact signatures that pass the retrospective compatible-set audit, a route-blinded prospective bridge will show both (a) reproducible documentation and (b) sufficiently low disagreement between documentation and independently judged actionability, while directly measuring whether workflow delivery and follow-up evidence exist. The bridge is specifically designed to detect the common failure in which an artifact is reproducible but the plan is not actionable, is assigned to no responsible team, is not delivered, or has no observable outcome trace.

The primary hypothesis, stated without a clinical-benefit claim, is:

> For each retrospective allow-listed atom and route, the lower simultaneous bound for documentation reproducibility will meet the inherited route-specific gate, the upper simultaneous bound for an actionability mismatch will be at most 0.10 for `AUTO` and at most 0.20 for `RECON`, and at least 0.95 of enrolled cases will have a directly auditable workflow and 7-day outcome record. Any atom failing a bound, or lacking the required workflow/outcome evidence, will be withheld from any later non-silent study rather than treated as a documentation success.

An adverse or inconclusive bridge result is scientifically useful: it distinguishes a failure of the artifact, a failure of clinical actionability, and a failure of delivery or evidence capture. It does not imply that the route causes harm.

## Frozen MIMIC source bindings and prospective handoff

The retrospective extraction uses dataset snapshot `[source checksum]` and read-only sources exactly as follows.

* Core archive `[internal dataset path]`, [source checksum]; archive members `mimic-iv-3.1/hosp/admissions.csv.gz`, `mimic-iv-3.1/hosp/patients.csv.gz`, `mimic-iv-3.1/hosp/services.csv.gz`, `mimic-iv-3.1/hosp/transfers.csv.gz`, and `mimic-iv-3.1/icu/icustays.csv.gz`.
* `hosp/admissions` (`subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`), key `(subject_id,hadm_id)`, with `D=dischtime`.
* `hosp/patients` (`subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`), joined on `subject_id`; only the inherited widened possible-calendar class is used, never a raw shifted calendar date.
* `hosp/services` (`subject_id,hadm_id,transfertime,prev_service,curr_service`), joined on `(subject_id,hadm_id)` and restricted to `transfertime < D`. `curr_service` is a workflow proxy, not a validated responsible-team label.
* `hosp/transfers` (`subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`) and `icu/icustays` (`subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`) are diagnostic/proxy inputs only; ICU exposure is admission-linked `intime < D`.
* `note/radiology` is `[internal dataset path]`, [source checksum], with exactly `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; join `(subject_id,hadm_id)` and identify reports by `(subject_id,note_id)`.
* `note/radiology_detail` is `[internal dataset path]`, [source checksum]b`, with exactly `note_id,subject_id,field_name,field_value,field_ordinal`; join only `(subject_id,note_id)`, retain every ordinal, and do not invent unavailable `parent_note_id`, `addendum_note_id`, or author ontologies.
* `note/discharge` is `[internal dataset path]`, [source checksum], with the same eight note columns; use exact `note_type == DS` and the canonical `(subject_id,hadm_id)` discharge artifact.
* `note/discharge_detail` is `[internal dataset path]`, [source checksum], with exactly `note_id,subject_id,field_name,field_value,field_ordinal`; retain fields but do not treat `author` as an ontology.

`hosp/poe` and `hosp/poe_detail` remain prohibited from all retrospective packets, labels, routes, domains, estimands, and gates. The bridge may not retroactively use them to repair a MIMIC gap.

The MIMIC artifact manifest is converted to a prospective **signature manifest**, not a patient roster. For every allow-listed atom, store the frozen atom code, route eligibility, permitted artifact types, unit parser version, and exact field-level requirements. No MIMIC subject or shifted date is sent to the prospective site. The site independently identifies cases using contemporaneous data that are mapped to the same observable signature definition. A mapping failure is `SIGNATURE_UNMAPPED`, not an assumed match.

The following bridge evidence is unavailable in all listed MIMIC tables and is therefore a required new prospective capture, not a MIMIC-derived variable: physical viewing/access audit event and timestamp; note finalization/signature and version history; responsible person/team and acknowledgement; communication recipient and timestamp; order/referral creation, status, scheduling, completion, cancellation, and outside-plan status; patient preference and feasibility; actual clinical context needed for actionability; and 7- and 30-day follow-up, adverse-event, utilization, and mortality ascertainment. `hosp/services`, `transfers`, and `icustays` cannot substitute for any of these fields.

## Bridge population, chronology, and finite workload

The bridge begins only after the retrospective candidate board has produced a signed allow-list. Its population is the first consecutive eligible prospective encounter/admission for a patient that maps to an allow-listed signature during a fixed 12-week enrollment window at the participating site. The encounter must have an actual discharge/departure timestamp `D*`; all bridge clocks use actual site timestamps, not MIMIC-shifted dates. Follow-up is through `D*+7 days` for the primary workflow/outcome window and `D*+30 days` for the secondary outcome window.

Enrollment is outcome-blind and route-blind. Screening uses only the presealed signature manifest and the contemporaneous artifact fields. If more than 300 distinct admissions satisfy the manifest, select exactly the first 300 by the presealed hash rank of `(bridge_protocol_hash || site_case_key)`, within each atom after applying the presealed atom order; no route, actionability, workflow, or outcome field is available to the selector. If an atom has fewer than 30 enrolled cases, it may be described but cannot be claimable. There are no replacements, top-ups, or post-label enrichment. A case that later proves unmapped, duplicate, or outside the frozen chronology is retained in the screening ledger and excluded only under the presealed rule, with reason recorded.

The retrospective <=900-admission and <=300-challenge ledger is unchanged. The bridge has a separate hard operational cap of 300 distinct admissions, 1,200 professional-hours, and 30,000 packet/access-review minutes; it cannot be used to purchase additional retrospective labels. The bridge ledger charges every enrolled case for retrieval and workflow abstraction (45 minutes), documentation review (30 minutes), independent actionability panel (45 minutes), and outcome verification (30 minutes), plus a fixed 60-hour setup/closeout allowance. Maximum at 300 cases is `60 + 300*(0.75+0.50+0.75+0.50) = 810` professional-hours, leaving a 390-hour contingency that may be used only for prespecified missing-event retrieval and adjudication, never for extra cases. Actual minutes and every retrieval attempt are recorded. Exceeding 1,200 hours, 30,000 minutes, 300 cases, or a sealed activity maximum is fail-closed `BRIDGE_INCONCLUSIVE`.

## Two independent blinded streams

### Stream D: documentation reproducibility

A documentation panel receives the prospective analogue of the MIMIC artifact packet: the exact radiology report chain and permitted discharge artifact versions available under the frozen pre-departure rule, their `charttime`/`storetime` or site equivalents, explicit missingness, and the permitted structured departure fields. It does not receive the atom code, retrospective route, parent labels, service/workflow proxy, workflow audit events, order/referral status, outcomes, or actionability panel output.

Two roster-disjoint documentation reviewers, using separately hashed codebooks `DB-D1` and `DB-D2`, independently code the same finite fields as the inherited route predicate: unit identity/target cluster, action/modality, due interval, polarity, recipient, responsibility, replacement, conflict, departure state, availability, lag, eventual text state, and missingness. They emit atomic tuples, not free-text route votes. The route is computed by the inherited pure predicate only after both outputs are sealed. A third senior documentation reviewer receives only the packet and the sealed atomic outputs after append-only sealing; it is an additional measurement system, not a truth oracle. The inherited compatible-set algorithm, including shared error, adverse unknown handling, and exact joint ratio optimization, applies unchanged.

The documentation estimand for atom `g` and route `r` is the design-weighted finite-population proportion of bridge cases whose sealed documentation outputs yield the same route-defining state as the retrospective signature under the inherited route predicate. Report `D_g,r` as a compatible interval, not as clinical correctness. Also report field-level missingness, unit-level disagreement, and `P(D=pass, A=not-ready)` jointly; do not report only a favorable route match.

### Stream A: actionability and feasibility

An independent actionability panel has a disjoint roster and never sees the documentation panel output, generated route, retrospective route, atom code, or workflow result. It receives the candidate recommendation unit in a standardized packet consisting of (i) the original route-relevant text span with provenance, (ii) the normalized target/action/due/recipient/responsibility fields produced by a separate sealed extraction service, and (iii) complete contemporaneous clinical context permitted by local governance, including current status, contraindications, patient preference, feasibility, and available alternatives. The normalized fields are shown so that actionability is a judgment about the actual proposed plan rather than a test of whether a reviewer can infer its topic. The extraction service cannot expose a route or favorable/adverse category.

Each of two independent clinicians records exactly one actionability state:

* `ACTIONABLE_NOW`: a responsible clinician/team could execute or communicate the plan at the specified time using the available information;
* `ACTIONABLE_AFTER_CLARIFICATION`: potentially useful, but a named clarification, missing result, responsible recipient, or timing decision is required before execution;
* `NOT_ACTIONABLE`: the plan is infeasible, contradictory, clinically inappropriate for the documented context, or lacks a viable action pathway;
* `INSUFFICIENT_CONTEXT`: the required clinical context is absent or cannot be verified.

The panel also records the blocking dimension(s), each binary: missing recipient/responsibility, missing timing, contradictory plan, contraindication/feasibility, patient preference, unavailable resource, missing result, and other prespecified reason. Reviewers must not infer that `AUTO` means actionable or that `DEFER` means harmful. A senior clinical adjudicator resolves only coding disagreements using the sealed context and records the disagreement rather than deleting it; adjudication cannot see the generated route until all actionability labels are sealed.

The primary actionability estimand is the weighted proportion `A_ready = ACTIONABLE_NOW`; a secondary permissive estimand is `A_possible = ACTIONABLE_NOW or ACTIONABLE_AFTER_CLARIFICATION`. The key bridge estimand is the actionability mismatch

`M_g,r = P(ACTIONABLE_AFTER_CLARIFICATION or NOT_ACTIONABLE or INSUFFICIENT_CONTEXT | documentation stream is route-compatible with r)`,

with numerator and denominator states optimized jointly over the compatible sets. `M` is a documentation-to-actionability discordance, not clinical harm. Report the full 4-category distribution and reason-specific components; no composite may conceal `INSUFFICIENT_CONTEXT`.

### Stream W: actual workflow delivery

A workflow abstractor, blinded to all routes, documentation labels, and actionability labels, extracts only contemporaneous system evidence. Required binary/time fields are: artifact available before `D*`; actual view/access by the responsible team before the relevant due time; finalization/signature/version; responsible person/team identifiable; acknowledgement or communication; order/referral created if the plan requires one; scheduling or handoff status; completion/cancellation/no-show; and outside-plan status. Each positive field requires a source-system event identifier and timestamp. A self-report without an event identifier is `UNVERIFIED`; absence of an event is `NOT_OBSERVED`, not `NO` unless the source system has complete event coverage for that field.

Define `W_complete=1` only when artifact availability, responsible-team identity, and the route-relevant delivery action are all observed with valid timestamps; define `W_ack=1` only when an acknowledgement/communication event is observed; and define `W_exec=1` only when a required order/referral or handoff has a recorded status. If a plan requires no order/referral, `W_exec` is `NOT_APPLICABLE`, never favorable missingness. The primary workflow estimand is the weighted proportion with `W_complete=1`; report coverage and each component separately. The bridge cannot certify an action as delivered merely because it was documented or clinically judged actionable.

### Stream O: outcome evidence

Outcome abstractors, blinded to routes, documentation labels, actionability labels, and workflow results, ascertain a fixed 7-day record and a fixed 30-day record. The minimum outcome fields are: death, ED visit/readmission, urgent contact for the target problem, completion of the planned test/referral/order, documented adverse event plausibly related to delay or noncompletion, and outcome-source availability. Each event has source, timestamp, and adjudication status. Two clinicians independently adjudicate whether a recorded adverse event is temporally compatible with the candidate plan and whether attribution is `RELATED`, `POSSIBLY_RELATED`, `UNRELATED`, or `UNDETERMINED`; attribution is descriptive and cannot be inferred from timing alone.

The primary outcome endpoint is not a benefit endpoint. It is **7-day outcome ascertainment completeness**, `O7_complete`, requiring a verified status for death, ED/readmission, target-related urgent contact, and plan completion or a documented reason that the field is not applicable. `O30_complete` is secondary. Event rates and completion rates are descriptive, jointly stratified by documentation and actionability states, with finite-population or exact binomial intervals as appropriate. No comparison of actionability groups is interpreted causally, and no adjustment model may convert this silent cohort into an effect estimate.

## Prespecified gates and interpretation

All bounds use the bridge's fixed sampling weights, exact finite-population inversion where applicable, and one simultaneous 95% max-statistic family. Unknown, unavailable, corrupted, unverified, and `INSUFFICIENT_CONTEXT` states are retained and adverse-compatible; there is no complete-case substitution. The following are nomination gates for a later study, not clinical harm thresholds.

1. **Documentation gate:** for a claimable atom, the lower simultaneous compatible bound for documentation reproducibility must meet the inherited route gate (`AUTO` 0.95; `RECON` 0.90; `TIMING` and `DEFER` use the inherited route-specific requirement). At least 30 enrolled cases per claimed route/atom are required.
2. **Actionability separation gate:** for an `AUTO` atom, the upper simultaneous bound for `M_g,AUTO` is <=0.10 and the upper bound for `NOT_ACTIONABLE` is <=0.05. For `RECON`, `M_g,RECON` <=0.20 is allowed because clarification is part of the intended route; `NOT_ACTIONABLE` remains <=0.10. `INSUFFICIENT_CONTEXT` is reported separately and has an upper bound <=0.05 for any claimed atom.
3. **Workflow evidence gate:** the lower simultaneous bound for `W_complete` is >=0.90 and the upper bound for unverified/missing workflow evidence is <=0.05. A passing actionability result cannot rescue workflow failure.
4. **Outcome evidence gate:** `O7_complete` lower bound is >=0.95 and `O30_complete` lower bound is >=0.90. These gates require evidence capture, not a favorable event rate. A high event rate is adverse information for study planning; a low event rate does not establish safety.
5. **Cross-stream accounting:** every atom reports the weighted 4-by-4 table of documentation pass/fail by actionability state, plus workflow and outcome completeness. If the actionability panel cannot judge a plan, the case is not moved into `ACTIONABLE_AFTER_CLARIFICATION` to preserve the denominator.
6. **Finite workload and seal gate:** no atom is claimable if its bridge packet time, adjudication burden, missing-event retrieval, or protocol seal exceeds the separate bridge cap. Any roster overlap, route leakage, post-label control construction, or revealed route before all streams seal makes the affected atom `BRIDGE_INCONCLUSIVE`.

A supportive bridge result means only that an exact allow-listed observable signature has (a) reproducible documentation, (b) independently judged actionability with a bounded mismatch, and (c) measurable workflow and outcome evidence sufficient to plan a separately governed study. An adverse result is anatomically interpretable: documentation failure blocks the signature; actionability mismatch blocks the route even if documentation passes; workflow failure means delivery is unknown; outcome evidence failure means the silent bridge did not establish the needed follow-up infrastructure. An inconclusive result includes too few cases, unmapped signatures, wide compatible bounds, missing event coverage, unverified workflow, nonresponse, broken seals, or zero denominators. Inconclusive is not evidence of safety or danger.

No result permits a retrospective automation claim, a live alert, a clinical-safety claim, a causal effect estimate, a benefit claim, a claim of guideline appropriateness, or temporal/external transport. Those require additional expert review and a prospective design with actual intervention governance. In particular, MIMIC's stored discharge and radiology text, `services.curr_service`, `transfers`, and ICU exposure do not supply workflow or outcome evidence; they only define and stratify the frozen retrospective signatures.

## Required bridge fixtures and falsification tests

Before enrolling a real bridge case, the implementation must pass synthetic fixtures with no clinical records:

* a documentation-perfect but actionability-`INSUFFICIENT_CONTEXT` case must pass neither the actionability nor workflow gate;
* a clinically actionable plan with no responsible-team/view event must have `A_ready=1` but `W_complete=0`, proving the streams are not conflated;
* a documented view without an executed order/referral must not count as `W_exec`;
* a route-compatible documentation panel with a route-incompatible independent actionability judgment must widen `M` and block `AUTO` at the stated bound;
* a route-irrelevant formatting change must not change documentation route or actionability category;
* a one-field replacement or timing change must alter only the inherited route as dictated by the locked truth table, while actionability remains independently adjudicated;
* a missing workflow log must remain `UNVERIFIED`/adverse-compatible rather than being treated as no action or successful action;
* a 7-day follow-up record with an event but no adjudication must not count as complete outcome evidence;
* a shared-wrong documentation panel must remain compatible with an adverse state even when actionability reviewers agree; and
* revealing a route to any reviewer before all labels and workflow/outcome extracts are sealed must invalidate the affected atom.

This repair changes the decision relevance of the next study without changing the parent scientific schema: it turns the prospective-silent bridge from a documentation-only handoff into a pre-specified, route-blinded measurement of documentation, actionability, delivery, and ascertainment, while explicitly refusing to call missing workflow or outcomes evidence clinical safety.
