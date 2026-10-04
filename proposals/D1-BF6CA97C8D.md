# Deterministic route-blinded documentation-to-actionability bridge

## Status, parent, and unchanged scientific schema

This is a targeted repair of `[prior hypothesis]`. It preserves the inherited first-eligible adult, one-admission-per-subject, all-opportunity pulmonary-opportunity population; reciprocal pre-departure radiology chronology; one exact canonical discharge (`DS`) artifact; unit-specific clocks and exhaustive `Y,V,H,Z`; the exact atom

`g = (possible-calendar class, terminal curr_service, workflow class)`;

all-unit adverse routing; `AUTO > RECON > TIMING > DEFER > NOACTION` precedence; support-atlas construction; positive-probability stratified sampling, inclusion probabilities, and hash-rank challenge selection; compatible-set inference; no rescue, switching, borrowing, pooling, or post-label reallocation; the inherited ceilings `A <= 900`, `C <= 300`, displayed worst-case physician hours `<= 2,370`, and packet minutes `<= 84,000`; and the prospective-silent-only conclusion ceiling.

No population, admission or recommendation-unit definition, route, atom, time boundary, baseline, primary estimand, sampling probability, workload ceiling, or causal estimand is changed. The bridge is a pre-label, route-blinded secondary diagnostic inside the already budgeted holistic challenge and packet-review rows. It adds no admission, panel, review pass, top-up, adaptive enrichment, or post-label control.

The repair makes four operational contracts exact:

1. H1/H2 must emit the same deterministic canonical unit inventory and assertion serialization before `D_REPRO` can be true.
2. H3 has a separately specified source-inventory/assertion reproduction scope and must be byte-identical under row reordering, input chunking, and permitted archive extraction order; H3 is not silently folded into the H1/H2 documentation-reproducibility estimand.
3. A predeclared source-availability audit distinguishes a fact that cannot occur in any configured source (`NOT_PRESENT_IN_AVAILABLE_SOURCES`) from a fact that could be represented but is not established for this record (`UNKNOWN`).
4. A mutually exclusive eligibility/actionability state machine explicitly handles zero-unit admissions, `NOACTION`, route `DEFER`, structural ineligibility, adverse findings, and inconclusive results, with an additive workload reconciliation rather than an expanded budget.

## Clinical question, evidence-supported claim, and unresolved claim

The strongest claim these local files can support is that a first-eligible admission frame and a reproducible admission-linked text packet can be constructed from pre-departure radiology records, a canonical discharge summary, structured admission/service/transfer/ICU fields, and their available timestamps. They can support an audit of storage-to-storage text consistency and explicit textual fields.

They cannot establish that a clinician viewed a report before physical departure, that a note was finalized or signed, that a recommendation was communicated, that an order or referral was placed or executed, that a responsible team accepted ownership, that a handoff or appointment was scheduled, that a patient or caregiver could or wished to follow a plan, that follow-up occurred, or that a clinical outcome resulted. `storetime`, service, care unit, discharge location, death, and note wording are not substitutes for those facts.

The falsifiable unresolved claim is narrower: among the frozen atoms and routes, can independent route-blinded readers reproduce the same recommendation-unit documentation and separately identify whether the supplied text explicitly specifies a next action without inventing a target, modality/action, interval, recipient or responsibility, replacement rule, or conflict resolution? The prespecified hypothesis is that at least some parent-supported signatures are documentation-reproducible but not text-actionability-ready. The size and composition of that gap would identify which prospective workflow fields are needed before any silent validation.

`D_REPRO` and `A_TEXT_COMPLETE` are observable properties of sealed artifacts, not clinical truth labels. A passing retrospective bridge supports only a better specified prospective silent data-collection protocol. It does not support clinical appropriateness, communication, safety, completion, benefit, causal effect, or deployment.

## Frozen packet, roles, and label timing

For each already selected challenge admission, make one immutable packet from the inherited extraction. It contains only the permitted reciprocal pre-`D` radiology chain, permitted admission/death/disposition fields, the canonical exact DS artifact and permitted DS-detail artifact, and the source-availability manifest. It excludes parent component labels, route, route-defining atom, stratum, inclusion weight, challenge status, all post-`D` text, POE/POE-detail, later outcome summaries, and any route or atom summary.

The existing disjoint H1/H2/H3 holistic roster and its three existing 10-minute challenge rows are retained. New bridge fields are appended to those rows; they do not create additional time. A reviewer who cannot complete a field within its existing row maximum records `NONRESPONSE` and `BRIDGE_INFEASIBLE`; the record enters the inherited adverse-compatible state and the sample is not extended.

* H1, documentation lane, independently inventories canonical distinct recommendation units and atomic assertions: target cluster, action/modality, due interval, polarity, recipient/responsibility, replacement, conflict, source-artifact span, and explicit/absent/contradictory/unreadable status. H1 sees no route or atom output.
* H2, text-actionability lane, independently performs the same unit inventory under separately worded codebook `CB-ACT`, without seeing H1 output, and then answers whether a receiving clinician could identify a concrete next action from the artifact without adding any unstated target, action, interval, recipient/responsibility, replacement rule, or conflict resolution. This is a textual sufficiency property only.
* H3, evidence-boundary lane, runs the source inventory/assertion reproduction contract below after H1/H2 outputs are sealed. H3 does not adjudicate clinical workflow from proxies and does not alter `D_REPRO`.

H1, H2, and H3 codebooks, rosters, pseudonyms, packet ordering, source manifests, and append-only seal order are independent. No reviewer sees route, atom, stratum, weight, parent label, or another lane's output before sealing. Synthetic fixtures, not real records, are used for examples and tuning.

## H1/H2 deterministic canonical unit and assertion contract

### Canonical source unit identity

The inherited unit list `U_i` is first constructed by the frozen reciprocal-restatement algorithm. It is not reconstructed by either panel. For each retained source recommendation, define a source key

`S = (subject_id, hadm_id, note_id, note_seq, charttime, storetime, normalized_span_start, normalized_span_end, reciprocal_role)`.

`normalized_span_start/end` are UTF-8 code-point offsets in the exact stored note text after only the inherited normalization (Unicode normalization form NFC, CRLF/CR converted to LF, and no whitespace collapse or semantic rewriting). `reciprocal_role` is the inherited report/addendum role. Missing values are represented by the literal typed token `NULL`, never by an empty string or the string `"null"`.

A candidate unit has a typed assertion record

`(target_class, action_class, modality_class, due_class, polarity_class, recipient_class, replacement_class, conflict_class, source_key, span_start, span_end, explicitness_class)`.

Each category is from the frozen codebook vocabulary. Free text is retained only as a separately escaped evidence span; it is never used as an implicit sort key or as a reviewer-selected identity. H1 and H2 may mark an assertion `UNKNOWN`, `ABSENT`, `CONTRADICTED`, or `UNREADABLE`, but may not create a new category after labels are sealed.

### Total matching algorithm

The matcher is total and deterministic.

1. Parse both lane outputs against the versioned schema. Reject malformed types, duplicate assertion IDs, out-of-range spans, illegal category strings, non-UTF-8 bytes, or references to a packet object not present in the immutable packet. Such a lane is `INVALID_OUTPUT`, not a favorable or adverse clinical label.
2. Normalize every assertion to the typed tuple above and sort assertions within each lane by the bytewise key
   `K = (target_class, action_class, modality_class, due_class, polarity_class, recipient_class, replacement_class, conflict_class, source_note_id, source_note_seq, source_charttime, source_storetime, span_start, span_end, explicitness_class, escaped_evidence_span)`.
   Each scalar is serialized as a length-prefixed UTF-8 field, with `NULL` distinct from empty string. Numeric fields use canonical base-10 with no leading zero except `0`; timestamps use UTC ISO-8601 with six fractional digits where present.
3. Match H1 and H2 units by exact equality of the inherited source-unit identity after the typed normalization. A unit with the same semantic text but a different source key is a distinct unit. A duplicated key, an unmatched key, or an assertion that maps to more than one source unit produces `AMBIGUOUS_MATCH`; it is not resolved by similarity, reviewer majority, or route knowledge.
4. Within a matched source unit, match assertions by exact equality of the complete identity fields through `conflict_class` and the normalized span. If one lane has an omitted assertion and the other has an assertion, retain an explicit unmatched assertion in the joint manifest. If both lanes assert the same field but disagree on its value, retain the disagreement as a paired assertion; do not choose the more favorable value.
5. A reciprocal restatement is the same unit only when the inherited parent algorithm has already assigned the same canonical reciprocal unit ID. A distinct recommendation in a later or addendum text remains distinct unless that frozen algorithm explicitly marks it as a restatement. Similar wording is never sufficient.
6. Emit a complete manifest containing every inherited unit, every H1 assertion, every H2 assertion, all unmatched and ambiguous states, and packet-validity flags. The manifest is sorted by `(admission_key, canonical_unit_id, K, lane)` and is hashed before any aggregate is read.

The fixed lexicographic serialization is RFC-8785-style canonical JSON with these additional locked rules: UTF-8 bytes; object keys sorted by Unicode code point; arrays in the specified manifest order; no insignificant whitespace; integers in decimal; finite decimals rendered with the shortest round-trippable decimal representation and no exponent; timestamps as the canonical strings above; and `NULL` as JSON `null`. The exact byte stream, not a pretty-printed equivalent, is the object of the SHA-256 hash. The implementation must publish serializer version, schema version, code hash, source hashes, packet hash, row count, and byte length in a sidecar manifest.

### H1/H2 reproducibility functional

`D_REPRO_i = 1` if and only if both H1 and H2 outputs are valid, the complete canonical source-unit inventories agree one-to-one with no duplicate, unmatched, ambiguous, or unresolved reciprocal-restatement identity, and every non-unknown route-defining assertion in the required field set `F_i` agrees after the exact matcher. `D_REPRO_i = 0` for a valid packet with a resolvable adverse disagreement. `D_REPRO_i = UNKNOWN` for `INVALID_OUTPUT`, `NONRESPONSE`, packet corruption, unreadable source identity, or any unresolved missingness under the inherited compatible-set rules.

H3 is **not** included in the H1/H2 `D_REPRO` functional. H3 is an independent reproduction and evidence-boundary audit. This separation prevents an unavailable workflow fact from being misrepresented as a disagreement in stored-text documentation and prevents H3 agreement from rescuing an H1/H2 mismatch.

For a valid empty inventory, both lanes must emit the same explicit zero-unit record; this is a structural inventory result, not a positive actionability result. It maps to `NOACTION` as specified below and never to `A_TEXT_COMPLETE`.

## H3 inventory/assertion reproduction scope and byte-identity contract

H3 has two separately reported outputs.

### Source-inventory reproduction

H3 consumes the frozen source availability manifest and independently regenerates the list of source objects, rows, fields, note-detail ordinals, and source-level capability assertions used by the packet. Its inventory scope is exactly:

* one admission row from `hosp/admissions`;
* the joined patient row from `hosp/patients`;
* all pre-`D` service rows from `hosp/services`;
* all admission-linked transfer rows used by the inherited workflow diagnostic from `hosp/transfers`;
* all admission-linked ICU rows with inherited pre-`D` eligibility from `icu/icustays`;
* every inherited reciprocal radiology row from `note/radiology` and every joined detail row from `note/radiology_detail`;
* the canonical exact-DS row from `note/discharge` and every joined row from `note/discharge_detail`.

No other tables, note streams, derived outcomes, or POE fields are in H3 scope. The inventory includes source table ID, source/archive member, schema hash, source row key, field name, ordinal where available, typed value-presence state, and the inherited time predicate. It does not include raw clinical text in a public query or publication; local sealed packets may retain it as permitted.

### Assertion reproduction

H3 independently parses the sealed inventory and emits one typed assertion per one of the eight bridge facts. Each assertion has `(admission_key, fact_code, source_capability_state, record_observation_state, evidence_locator, provenance_hash)`. H3 may assert `OBSERVED` only when a permitted source contains an explicit fact meeting the fact-specific rule below. H3 may assert `CONTRADICTED` only when a permitted source explicitly contradicts the fact. Absence in a source that can represent the fact is `UNKNOWN`; absence of the capability itself is `NOT_PRESENT_IN_AVAILABLE_SOURCES`.

H3 reruns the same manifest and assertions under all of these equivalent input conditions: original row order; reverse row order; a fixed pseudorandom permutation seeded by the protocol hash; every legal chunk partition (including singleton and one-chunk input) in lexicographically ordered chunk IDs; and archive-member extraction order permuted before the final sort. The emitted canonical bytes and SHA-256 hash must be identical across all runs. Reordering or chunking may not change a row key, assertion, availability state, or aggregate.

The H3 reproduction result is `H3_BYTE_IDENTICAL=1` only if every permitted rerun has identical manifest bytes, assertion bytes, row count, and hash. A mismatch is a computational failure and yields `INCONCLUSIVE` for H3; it does not get averaged away, repaired by majority, or folded into `D_REPRO`. A source extraction failure, unavailable field, or record-level unknown is a substantive state in the manifest, not a byte-identity failure.

The H3 result is reported as `(inventory_scope_hash, assertion_scope_hash, rerun_hash_set, byte_identity, fact-state vector)`. H3 cannot establish that an unrecorded workflow event did not occur.

## Predeclared eight-fact source-availability audit

The audit is fixed before labels. Source capability is assessed from the full catalog, exact schema JSONs, source headers where necessary, and the read-only source paths. It is not learned from the observed prevalence of a fact. The following distinction is mandatory.

* `NOT_PRESENT_IN_AVAILABLE_SOURCES` means the configured sources have no field or source modality capable of observing the specified fact under its definition. It is a source-level limitation and is assigned uniformly as a capability state; it is never converted to `NO`, `ABSENT`, or a patient-level adverse outcome.
* `UNKNOWN` means a configured source could represent the fact, but this record has no qualifying assertion, has missing/ambiguous evidence, or the packet cannot resolve it. It is a record-level uncertainty and remains in the inherited compatible set.
* `OBSERVED` and `CONTRADICTED` require explicit admissible evidence. A timestamp, location, service, discharge disposition, death, or recommendation phrase is not enough unless the fact rule explicitly permits it.

The eight fact rules are:

| Fact code | Required claim | Predeclared source audit and record rule |
|---|---|---|
| `VIEWED_BEFORE_DEPARTURE` | A person viewed the relevant report before `D` | No configured source has a view/audit-log event. Source capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES` for every record. `storetime`, `charttime`, transfer, and note text cannot be upgraded to viewed. |
| `FINALIZED_SIGNED` | The report/plan was finalized or signed | No signer, signature event, or finalization-status field is available in the bound sources. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`. `storetime` is storage provenance only. |
| `COMMUNICATED` | Recommendation was communicated to a recipient | No communication/event/audit field or recipient-confirmation stream exists. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`; a named recipient in prose is only a textual assertion, not communication. |
| `ORDER_OR_REFERRAL_EXECUTED` | An order/referral was placed and executed | POE/POE-detail are explicitly excluded and no permitted source provides execution status. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`; recommendation text and discharge location are not execution. |
| `RESPONSIBLE_TEAM_ACCEPTED` | A team/person accepted responsibility | Provider/service/care-unit fields can describe assignment-like context but not acceptance. For the fact as defined, capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`. `curr_service`, `careunit`, and author-like detail fields cannot prove acceptance. |
| `SCHEDULED_OR_HANDOFF_CONFIRMED` | Appointment or handoff was scheduled/confirmed | No scheduling, handoff confirmation, or appointment-execution stream is available. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`; due intervals and discharge disposition are not scheduling. |
| `PATIENT_OR_CAREGIVER_CAPACITY_PREFERENCE` | Patient/caregiver capacity, preference, or feasibility was assessed | No structured capacity/preference/teach-back/acceptance field is available in the permitted sources. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`; demographics, language, insurance, or note prose cannot prove this fact. |
| `POST_DISCHARGE_FOLLOWUP_OR_OUTCOME` | Follow-up occurred or a post-discharge clinical outcome was observed | The configured episode data provide no complete post-discharge follow-up/outcome stream for this definition. Capability is `NOT_PRESENT_IN_AVAILABLE_SOURCES`; subsequent absence, death, discharge location, or a later stored note cannot be relabeled as non-follow-up or harm. |

This table is a source-availability assertion, not a claim that none of these events occurred. If a future compiler identifies a permitted field that can genuinely represent one fact, the protocol version must be stopped and amended before labels; it may not silently convert prior `NOT_PRESENT...` values to record-level `UNKNOWN`.

For the current snapshot, H3 still emits an eight-element vector for every valid packet. Each element contains both `source_capability_state` and `record_observation_state`; for the eight facts above, the former is `NOT_PRESENT_IN_AVAILABLE_SOURCES`, and the latter is `NOT_APPLICABLE_TO_CURRENT_SNAPSHOT` rather than a clinical negative. If a synthetic fixture supplies a source capable of representing a fact, it may test `UNKNOWN`, `OBSERVED`, and `CONTRADICTED` semantics without changing the real-source capability claim.

## Complete eligibility and actionability state machine

Eligibility is determined from sealed packet structure before any actionability label. The following states are mutually exclusive at the stated level; raw reasons are retained in a separate nonexclusive reason vector. A state may not be changed by a route, a favorable panel, an atom aggregate, or a compatible-set optimization.

| Priority | `ELIGIBILITY_STATE` / `ACTIONABILITY_STATE` | Exact condition | Estimand treatment |
|---:|---|---|---|
| 1 | `NA_NOT_ELIGIBLE` | Required canonical packet, source identity, or inherited reciprocal chronology is absent/corrupt; admission is outside the frozen eligible frame; or the bridge packet fails structural validation before labels | Structural NA. Excluded from the actionability numerator/denominator; retained in census, failure ledger, and compatible-set audit. Never recoded as adverse text. |
| 2 | `NA_NO_TARGET` | Packet is valid and eligible but no retained pulmonary target unit exists after the frozen unitization algorithm | Structural NA for target-level actionability. Retain zero-unit inventory and reason. It is not a favorable actionability observation. |
| 3 | `NA_NO_ACTION` / `NOACTION` | Valid eligible packet has an explicit empty recommendation/action inventory under the inherited `NOACTION` state; no unit can have required action fields | NA for actionability fields by definition. `D_REPRO=1` only when H1/H2 independently emit identical valid empty inventories. `A_TEXT_COMPLETE=NA`, not 1. |
| 4 | `NA_ROUTE_DEFER` / `DEFER` | A retained unit exists, but inherited route precedence assigns `DEFER` because the route-defining evidence is unresolved, unsupported, or otherwise deferred | Route-conditioned actionability contrast is NA for the deferred route cell. The unconditioned text fields may still be labeled if the unit is structurally eligible; those labels cannot upgrade the inherited route. |
| 5 | `ELIGIBLE_COMPLETE` | At least one retained unit is structurally eligible, all required text fields for that unit are explicit and internally nonconflicting, and no field is inferred from a proxy | Favorable textual state, `A_TEXT_COMPLETE=1`; does not prove workflow or appropriateness. |
| 6 | `ADVERSE_PARTIAL` | Eligible unit has one or more required fields absent while at least one required field is explicit; no complete explicit plan can be recovered | Adverse-compatible; `A_TEXT_COMPLETE=0`, `A_TEXT_GAP=1`. |
| 7 | `ADVERSE_REPLACEMENT` | Eligible unit is explicitly replaced, superseded, or conflicts with another plan and the frozen text does not resolve which action governs | Adverse-compatible; retain both assertions and conflict. No reviewer may select a preferred plan. |
| 8 | `ADVERSE_CONTRADICTION` | H1/H2 disagree on a required assertion or the artifact contains internally contradictory required fields | Adverse-compatible for the affected unit; `D_REPRO=0` when valid and resolvable, otherwise `UNKNOWN`. |
| 9 | `ADVERSE_TIMING` | Target and action are explicit but due interval/timing is absent, contradictory, or not anchored by the frozen interval vocabulary | Adverse-compatible text gap. A calendar proxy or storage timestamp cannot fill timing. |
| 10 | `ADVERSE_UNREADABLE` | Required source text or field is unreadable, malformed, or cannot be interpreted under the locked codebook | Adverse-compatible when the packet is otherwise valid; `UNKNOWN` if the defect prevents validity of the entire packet. |
| 11 | `ADVERSE_NONRESPONSE` | A lane does not return a valid field within the existing row maximum, including `BRIDGE_INFEASIBLE` | `UNKNOWN` in the record and adverse-compatible in bounds; no extra review is permitted. |
| 12 | `INCONCLUSIVE_AMBIGUITY` | Unit identity, reciprocal-restatement status, or field mapping remains ambiguous after the total matcher | Inconclusive, retained in compatible states; it cannot be collapsed to complete or partial. |
| 13 | `INCONCLUSIVE_SOURCE_UNKNOWN` | A configured source could represent a needed record fact but this record lacks a resolvable assertion | Inconclusive/unknown, not `NOT_PRESENT...` and not a clinical negative. |
| 14 | `INCONCLUSIVE_SEAL_OR_COMPUTE` | Hash/seal mismatch, H3 byte-identity failure, invalid reference execution, or incompatible joint ratio state | Inconclusive and fail closed; no atom nomination or rescue. |

For a multi-unit admission, the inherited all-unit adverse rule remains controlling: one adverse, unresolved, or incompatible unit prevents a favorable admission-level route result. `A_TEXT_COMPLETE_i=1` requires every retained target unit to be `ELIGIBLE_COMPLETE`. `A_TEXT_GAP_i=1` is defined only among records with `D_REPRO_i=1` and at least one structurally eligible target unit; it is false/NA, not favorable, for zero-unit and `NOACTION` records. Route `DEFER` is not changed by actionability labels. H3 workflow gaps are reported alongside these states and never converted into adverse clinical outcomes.

The bridge reports the joint weighted table `(D_REPRO, A_TEXT_COMPLETE, A_TEXT_GAP, eligibility/actionability state, eight-fact vector, H3 byte identity)` by frozen atom and inherited route. It retains numerator and denominator jointly in every compatible state. No complete-case deletion, favorable-consensus rule, imputation, marginal-extrema combination, or pooled atom rescue is allowed.

## Estimands and uncertainty

The inherited primary route and all primary route estimands remain unchanged. Secondary bridge quantities are descriptive finite-population quantities using the inherited inclusion probabilities and compatible-set machinery. Challenge-only estimates are explicitly conditional on challenge inclusion.

The principal secondary contrast is

`G_text = P_w(A_TEXT_GAP = 1 | D_REPRO = 1, structurally eligible target, g, inherited route)`,

with the complete numerator/denominator pair retained across compatible states. A second table reports the prevalence and exact reason vector of the eight source-availability limitations among text-complete records. It is interpreted as evidence about observability, not workflow failure.

All H1/H2/H3 missingness and shared-error states remain admissible in the parent compatible set. A unanimous pair does not remove the shared-wrong state. Joint ratio bounds are optimized jointly, not by combining independently favorable marginal extrema. Report finite-population design-weighted point summaries and simultaneous intervals under the inherited estimator and state rules; no new statistical model is introduced.

## Exact local MIMIC bindings

Use only dataset snapshot `[source checksum]`. Read-only source paths, archive members, schema JSON paths, columns, keys, and time predicates are as follows.

* Archive `[internal dataset path]`, [source checksum].
  * `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema `[internal dataset path]`, schema [source checksum]. Use `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; key `(subject_id,hadm_id)`; `D=dischtime`.
  * `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema `table-9154f8c46cade9af.json`, schema [source checksum]. Use `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; join on `subject_id`; use only the inherited widened possible-calendar class, never shifted raw years as actual calendar dates.
  * `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema `table-491b3c713229062a.json`, schema [source checksum]. Use `subject_id, hadm_id, transfertime, prev_service, curr_service`; join `(subject_id,hadm_id)`; retain `transfertime < D`; terminal `curr_service` and inherited workflow class remain atom inputs.
  * `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema `table-685b6b74d0d7c547.json`, schema [source checksum]. Use `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; join `(subject_id,hadm_id)`; use only inherited pre-`D` `intime/outtime` diagnostic predicates; never reinterpret `careunit` as responsibility.
  * `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema `table-7d5c8feb0fb0dbd4.json`, schema [source checksum]. Use `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; join `(subject_id,hadm_id)`; inherited ICU exposure uses `intime < D`; it is not an actionability label.

* `[internal dataset path]`, [source checksum], table `note/radiology`, schema `table-1ffcd77c4cbdaeda.json`, schema [source checksum]. Columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; join `(subject_id,hadm_id)` and identify notes `(subject_id,note_id)`; use only the inherited reciprocal pre-`D` chain and `R_store` chronology.
* `[internal dataset path]`, [source checksum]b`, table `note/radiology_detail`, schema `[internal dataset path]`, schema [source checksum]3`. Columns are exactly `note_id, subject_id, field_name, field_value, field_ordinal`; join `(subject_id,note_id)`; retain every ordinal. This schema contains no `parent_note_id` or `addendum_note_id` column; reciprocal linkage comes only from the inherited radiology extraction/text rules, not an invented detail field.
* `[internal dataset path]`, [source checksum], table `note/discharge`, schema `[internal dataset path]`, schema [source checksum]. Columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; join `(subject_id,hadm_id)`; require exact `note_type == DS`; retain the inherited canonical `(subject_id,hadm_id)` DS artifact and `DS_store`.
* `[internal dataset path]`, [source checksum], table `note/discharge_detail`, schema `[internal dataset path]`, schema [source checksum]3`. Columns `note_id, subject_id, field_name, field_value, field_ordinal`; join `(subject_id,note_id)`; retain fields and ordinals; do not use an author-like field as a responsibility ontology.

The compiler must stop on any source or schema hash mismatch rather than guessing through it. The exact local README and schema JSONs are authoritative.

POE and POE-detail are excluded from all primary packets, bridge labels, routes, estimands, and gates. The exact source catalog and all complete schema JSONs are authoritative; any mismatch between this proposal and the catalog stops execution rather than being guessed through.

## Pre-label execution, fixtures, and verification

1. Verify the MIMIC snapshot, every source hash, archive member, schema JSON hash, read-only status, and the exact columns/keys/time fields above.
2. Extract the inherited population, `D`, reciprocal radiology chain, `R_store`, canonical `DS_store`, pre-`D` service/transfer/ICU records, and packet artifacts before opening any labels. Write source, extraction, serializer, and packet hashes.
3. Build the same frozen atlas, strata, positive-probability sample, challenge reservation, atom reservations, and weights as the parent. Seal these before route or bridge labels.
4. Seal independent `CB-DOC`, `CB-ACT`, and `CB-GAP` versions, ordered vocabularies, synthetic examples only, rosters, and append-only seal order.
5. Run fixtures before real packets: identical explicit plan; missing recipient; one lane missing due interval; zero-unit valid inventory; valid `NOACTION`; route `DEFER` with a retained unresolved unit; explicit text with every workflow fact source-unavailable; record-level unknown in a synthetic capable source; contradictory replacement; post-departure order-like language; route-irrelevant formatting perturbation; decisive one-field perturbation; reordered rows; all chunk partitions; and shared-wrong reviewer agreement.
6. Run H1/H2 matching and H3 source/assertion reproduction, then recompute all results with an independent reference interpreter. Check that H3 cannot change `D_REPRO`, route, atom, sample, primary estimand, or compatible-set rules.
7. Publish the full joint state table, hashes, byte lengths, eligibility counts, fact availability vector, and workload ledger. A failure is not repaired by rerunning until favorable; any deterministic mismatch is an inconclusive/fail-closed result.

## Additive workload compatibility

The bridge uses the inherited challenge rows and packet-review activities. It does not create a second budget. Nonetheless every bridge field has a recorded charge so that an apparently free appended field cannot conceal an overflow.

For each admission `i`, record the parent charge `P_i` and bridge incremental charge `B_i` in physician minutes and packet minutes, with activity IDs. If a single read is used by both parent and bridge, the physical read is charged once to the union ledger, while the incremental bridge coding time is charged separately. The ledger contains: selected admissions, distinct-admission union, challenge union, overlap, parent-only activities, bridge-only activities, shared activities, planned charges, actual charges, unresponsive/infeasible charges, and cap headroom. It must satisfy

`sum_i (parent_union_minutes_i + bridge_increment_minutes_i) <= 2,370 physician-hours`

and

`sum_i (parent_union_packet_minutes_i + bridge_increment_packet_minutes_i) <= 84,000 packet-minutes`,

as well as `A <= 900` and `C <= 300`. The inherited displayed worst-case accounting convention is retained; no alternate denominator or hidden discount is allowed. If bridge fields make the additive total exceed any ceiling, the protocol fails closed before labels. It may not reduce the parent sample, select easier admissions, top up, or reallocate after seeing bridge labels. A ledger/hash mismatch makes the bridge `INCONCLUSIVE` while leaving the inherited primary analysis unchanged.

## Supportive, adverse, and inconclusive results

Supportive evidence is a reproducible, atom-level pattern with valid byte-identical H3 runs, a narrow compatible-set estimate of `D_REPRO`, a finite and reported `G_text`, and a stable explicit list of unavailable workflow facts. This supports only a prospective silent-study specification that captures the eight missing workflow/outcome fields. It does not support clinical actionability, safety, appropriateness, benefit, completion, or transport.

Adverse evidence is a large or wide documentation-to-text-actionability gap, route-invariant changes under the locked controls, unresolved canonical units, or an affected atom whose actionability state remains adverse-compatible. That atom is not nominated for a silent bridge without adding the missing field to a future collection protocol. If the only adverse-looking result is that MIMIC lacks workflow/outcome sources, report evidence limitation, not care failure, and do not alter the inherited route.

Inconclusive evidence includes insufficient challenge cases, nonresponse, malformed packets, broken seals, H3 reorder/chunk byte mismatch, unresolved timestamps or reciprocal identity, infeasible controls, wide compatible-set intervals, additive ledger overflow, or inability to distinguish source-level unavailability from record-level unknown. Inconclusive is neither evidence of safety nor evidence of non-actionability.

Falsification occurs if any lane sees route/atom/weight information before sealing; if H1/H2 matching depends on input order, reviewer order, or noncanonical serialization; if H3 bytes change under permitted reordering/chunking; if H3 is used to inflate `D_REPRO`; if a missing source capability is called a patient-level negative; if zero-unit/`NOACTION` is counted as complete; if `DEFER` is upgraded by text completeness; if a route-invariant perturbation changes the prescribed state; if a decisive one-field perturbation has no prescribed state change; if joint bounds use incompatible marginal extrema; if additive caps are exceeded or hidden by overlap accounting; or if any report calls text completeness communication, workflow completion, clinical appropriateness, safety, benefit, or causality.

## Prospective evidence required and conclusion ceiling

A passing retrospective bridge is a gate to study design, not deployment. A separately governed prospective silent study must collect provenance and timestamps for viewing/availability, finalization/signature, communication, responsible-team acceptance, order/referral execution, scheduling/handoff, patient/caregiver preference or capacity, outside-plan visibility, and follow-up/outcomes. It must retain the frozen atom/route mapping and predeclare that missing workflow evidence routes to `DEFER`.

Expert clinical adjudication is required for appropriateness and safety. A prospective outcome study is required for harm, utility, benefit, or causal effects. No conclusion from this MIMIC experiment may claim live trigger validity, successful care delivery, follow-up completion, external validity, temporal transport, patient benefit, or a causal effect.

## What changed and what remains uncertain

Relative to `[prior hypothesis]`, this version adds a total typed H1/H2 matcher, canonical fixed lexicographic byte serialization, explicit separation of H3 from `D_REPRO`, a closed H3 inventory/assertion scope with reorder/chunk byte-identity tests, a predeclared eight-fact source-capability audit, the full mutually exclusive actionability eligibility table including zero-unit/`NOACTION`/`DEFER`, and an additive no-budget-expansion ledger. It also corrects the detail-schema binding by using only the columns present in the exact local JSON rather than inventing parent/addendum columns.

Uncertainty remains substantive and intentional: source text may be incomplete; independent readers may share errors; the eligible target set may be sparse; workflow and outcome modalities are absent; stored text is not a record of communication or care; and prospective silent validation is still required. These limitations are preserved rather than resolved by a more elaborate retrospective computation.
