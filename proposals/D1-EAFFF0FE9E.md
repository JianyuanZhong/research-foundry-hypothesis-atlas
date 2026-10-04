# A deterministic source-identity anchor audit for pulmonary discharge handoff

## Successor purpose and preserved scientific contract

This is a substantive child of `[prior hypothesis]` and `[prior hypothesis]`. The parents established a clinically useful but still potentially permissive documentary-anchor construct: a reader could call a discharge phrase “source-linked” when a generic descriptor, a copied phrase, an inferred pronoun, or an ambiguous field relationship merely co-occurred with an exact recommendation. They also left implementation choices about document containers, descriptor uniqueness, and source-span permutations to compilation. This successor makes the actionability proxy stricter and reproducible without turning it into a workflow or clinical-truth claim.

The inherited protocol is frozen and unchanged: the first-eligible adult admission per subject, one admission per subject, all pre-discharge radiology opportunities, reciprocal report/addendum chronology, `D=admissions.dischtime`, exactly one canonical pre-D discharge summary, the exact target atom/route `g=(E, terminal curr_service, W)`, route-concealed panels, all-unit adverse precedence, label-independent matched controls, sealed two-phase whole-admission positive-probability sampling, finite-population HT/Hájek inference, the additive distinct-admission ledger, and the silent-validation-only conclusion ceiling. This child adds only a pre-label source-identity/actionability audit and stricter support gate. It cannot change population, chronology, target atom, route, inherited primary estimand, unitization, sample, or allocation after any label.

The falsifiable question is:

> On a pre-specified, source-unique pulmonary recommendation unit, is the exact atom-preserving instruction in the canonical discharge document accompanied by the same source-unique finding descriptor in the same bounded document container more often for the pulmonary target than for a within-admission non-target recommendation matched exactly on modality and due interval, while source-descriptor and discharge-container permutations destroy the apparent relationship?

“Source-unique” and “same bounded container” are deliberately stronger than lexical co-occurrence. A supportive result means only that a particular stored radiology-to-discharge text relation is reproducible and more specific for the target than its matched control. It does not show delivery, viewing, responsibility, ordering, scheduling, completion, appropriateness, safety, benefit, or causality. MIMIC’s shifted timestamps support within-subject chronology only; they cannot support cross-subject calendar comparisons.

## Exact read-only MIMIC bindings

Use snapshot `[source checksum]` and only these source members/files. The ZIP is `[internal dataset path]`, [source checksum].

- `mimic-iv-3.1/hosp/admissions.csv.gz`, `datasets/mimic/table-e8ec3e6e2b58015d91d1d4` is not a catalog identifier; the authoritative local artifact is `datasets/mimic/table-685b6b74d0d7c547.json`, table `hosp/admissions`; use `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; join on `(subject_id,hadm_id)`, with `D=dischtime`.
- `mimic-iv-3.1/hosp/patients.csv.gz`, `datasets/mimic/table-9154f8c46cade9af.json`, table `hosp/patients`; use `subject_id,anchor_age,anchor_year,anchor_year_group`; join on `subject_id` for adult/first-admission eligibility only.
- `mimic-iv-3.1/hosp/services.csv.gz`, `datasets/mimic/table-491b3c713229062a.json`, table `hosp/services`; use `subject_id,hadm_id,transfertime,prev_service,curr_service`; join on `(subject_id,hadm_id)` and derive terminal service only by the inherited pre-D deterministic rule.
- `mimic-iv-3.1/icu/icustays.csv.gz`, `datasets/mimic/table-7d5c8feb0fb0dbd4.json`, table `icu/icustays`; use `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los` only for the inherited ICU proxy.
- `mimic-iv-3.1/hosp/transfers.csv.gz`, `datasets/mimic/table-685b6b74d0d7c547.json`, table `hosp/transfers`; use `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime` for diagnostics only, never as departure, responsibility, action, or completion.
- `[internal dataset path]`, `datasets/mimic/table-1ffcd77c4cbdaeda.json`, table `note/radiology`; use `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`.
- `[internal dataset path]`, `datasets/mimic/table-2972dbfe5cb661c0.json`, table `note/radiology_detail`; use `note_id,subject_id,field_name,field_value,field_ordinal`.
- `[internal dataset path]`, `datasets/mimic/table-69be322e2b58015b.json`, table `note/discharge`; use `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`.
- `[internal dataset path]`, `datasets/mimic/table-18d43f38e33d1fd2.json`, table `note/discharge_detail`; use `note_id,subject_id,field_name,field_value,field_ordinal`.

The apparent malformed path-like token in the second bullet is explicitly not a source or schema identifier; only `table-9154f8c46cade9af.json` is used. This explicit correction prevents a compiler from silently inventing a schema artifact.

Join note/detail rows only on `(subject_id,note_id)` and notes/admissions only on `(subject_id,hadm_id)`. A missing radiology `hadm_id` is never relinked by subject. Parse all timestamps with one strict timezone-naive ISO parser, retaining original and parsed strings. Require non-null keys and both `charttime < D` and `storetime < D` for all radiology and canonical DS rows. Apply the inherited exact reciprocal report/addendum predicates and unique canonical-DS key `(storetime,charttime,note_seq,note_id)`; ties with different text are `UNKNOWN`, not file-order choices. No source is modified.

Before target or label exposure, emit a manifest containing the snapshot/source/schema hashes, exact ZIP member names, parser version, UTF-8/CSV delimiter/quote/NA policy, all null/malformed/duplicate/quarantine counts, unmatched-link counts, dictionary hash, random seeds, and every derived identity. Any eligible identity duplicate, malformed required time, unresolved required link, post-D row, or changed parser/dictionary/seed fails closed.

## Frozen source-only descriptor and document-container grammar

### Immutable normalization and descriptor dictionary

The dictionary is a finite versioned file sealed at `FRAME_SUPPORT_SEALED`, with SHA-256 recorded before labels. It contains Unicode NFKC, lowercase, whitespace collapse, punctuation and sentence-boundary rules; exact modality and due-interval IDs; inherited recommendation/negation/uncertainty/historical/hypothetical/conditional/no-follow-up rules; cluster lexicons; and a descriptor lexicon whose entries are explicitly enumerated from the supplied radiology vocabulary. Descriptor classes are `ANATOMY`, `LATERALITY`, `SIZE`, `COUNT`, and `FINDING_QUALIFIER`. Generic tokens (`finding`, `abnormality`, `lesion`, `nodule`, `opacity`, `follow-up`, `imaging`) are not descriptors. No spelling correction, lemma, embedding, language model, clinical synonym, or post-label edit is permitted.

Normalization is deterministic: NFKC, lowercase, replace non-alphanumeric separators by one space except date/decimal punctuation required by the fixed grammar, collapse whitespace, and retain a map from normalized tokens to original character offsets. Longest exact dictionary phrase wins; equal-length ties use dictionary row order. Incompatible modality, interval, polarity, or descriptor parses make a unit ineligible rather than selecting one by reader preference.

### Source-identity eligibility `Q_S`

For every inherited recommendation unit, construct `Q_S` without DS text, H labels, K labels, route labels, observed times, or post-D information.

1. The unit must be an inherited positive, patient-specific recommendation unit in a reciprocal pre-D radiology report/addendum chain and must yield one exact atom `(E,M,W)` under the inherited parser. It must be affirmative, non-conditional, non-historical, non-hypothetical, non-screening, non-surveillance, non-staging, and not explicit no-follow-up.
2. The source identity span is one contiguous span in one radiology text/detail container. It contains the frozen cluster span for `E` plus exactly one or more descriptor tokens from at least one non-generic descriptor class. The descriptor sequence must be within the same recommendation clause, with no semicolon/newline clause boundary and no negation or uncertainty scope.
3. Define `sigma(u)` as the normalized ordered sequence of the cluster ID plus all descriptor dictionary IDs in that source span, preserving class and token order. Do not include modality or interval in `sigma`; those are separately matched atom fields. A unit with two incompatible descriptor parses, two distinct finding objects in one inseparable span, or an unresolved scope is `Q_S=0` with reason `SOURCE_AMBIGUOUS`.
4. `sigma(u)` must be unique among all inherited recommendation units in the same admission after exact source-span overlap suppression. If the same signature occurs in two units, both are `Q_S=0` with reason `SOURCE_NONUNIQUE`; no “closest” unit is chosen. Uniqueness is computed before any labels and is not a clinical assertion that the finding itself is unique.
5. The source identity key is `(subject_id,hadm_id,note_id,field_ordinal,unit_ordinal,source_start,source_end,sigma_id)`. Report/addendum representations of one inherited unit collapse to one unit under the inherited canonical relation; detail duplicates do not create units. If an identity key duplicates with nonidentical text or span, the eligible frame fails closed.

`Q_S` is a feasibility property, not an H or K outcome. The selected target cell is eligible only if every target unit in every paired-support admission and the deterministic control unit in every paired-support admission has `Q_S=1`. Thus a target with no source-identity support returns `NO_SELECTION`; it is not rescued by a favorable DS phrase. This is a pre-label restriction and leaves the inherited population and primary route untouched.

### Canonical DS containers and exact `Q_D`

To eliminate hidden concatenation, canonical DS evidence is searched in two separately indexed container types only: (a) the canonical `note/discharge.text` row as one `TEXT` container, and (b) each linked `note/discharge_detail` row `(note_id,field_ordinal)` as one `DETAIL` container. `field_name` is retained literally but has no section or ownership semantics. Text and detail rows are never concatenated, sorted into a synthetic note, or deduplicated by equal content. A positive primary anchor must occur inside one container; adjacent fields cannot be combined. An empty/null container is readable absence only if the other container rules permit review; it is never silently imputed.

Within a container, sentence boundaries are the fixed parser's punctuation/newline boundaries, with decimal/date exceptions. A candidate instruction must occupy one sentence, one non-semicolon clause, and at most 48 normalized tokens. It must contain the exact packet atom `(E,M,W)` under the inherited positive H grammar and a contiguous occurrence of the exact normalized `sigma` descriptor sequence. The descriptor and all atom components must be in the same bounded instruction span. Generic descriptor words, pronouns, “the above,” “this lesion,” clinical synonyms, inferred coreference, a descriptor in another sentence, a modality or interval in another instruction, or a field-name interpretation do not satisfy `Q_D`.

The H readers retain the parents’ exact H+/H-/H_U definitions and independent spans. The added anchor reader/panel receives the frozen source span, atom dictionary row, one DS container, and fixed codebook, blinded to target/control role, route, phase-1 labels, other outcomes, and the fact that `Q_S` is a support requirement. `Q_D` is a deterministic navigation flag only; it never overrules a reader. A reader must mark the original source span, the DS instruction span, the exact `sigma` token sequence, the atom components, and container identity.

## Anchor outcomes and estimands

Use two independent anchor readers, roster-disjoint from phase 1, H, C/S, codebook authors, and allocation staff. Each assigns exactly one status.

- `K+`: both readers assign inherited H+ with valid attributable spans, and both independently verify `Q_S=1`, exact same `sigma` IDs, exact `(E,M,W)`, affirmative scope, same single DS container, and `Q_D=1`.
- `K-`: the source and DS are readable and linked, `Q_S=1`, but the required exact source-identity relation is absent, conflicting, negated, conditional, or in a different container. This is a documentation-construct negative, not a clinical failure.
- `K_U`: source/DS truncation or unreadability, unresolved linkage or chronology, malformed/missing required key, incompatible parse, descriptor ambiguity, missing attributable span, reader nonresponse, or any reader disagreement. `Q_S=0` is not reclassified as K-; it is structural `ANCHOR_OPPORTUNITY_UNAVAILABLE` and triggers the pre-label support gate/DEFER if encountered.

No majority vote turns disagreement into K+. A third reader can characterize disagreement only if its roster and time are pre-registered; it cannot rescue the primary status. `K_P` records literal `field_name` and `field_ordinal` availability separately. Missing detail rows or null field names are `PLACEMENT_UNAVAILABLE`, never evidence of non-delivery, poor care, or a K-.

Let `S_TC^A` be the frozen full-frame paired domain of admissions with the selected target, its deterministic matched control, and `Q_S=1` for every required target/control unit. `S_TC^A` is source-only and fixed before labels. The added estimands are finite-population rates on this domain:

`theta_KT = |S_TC^A|^-1 sum_i K+_Ti`, `theta_KC = |S_TC^A|^-1 sum_i K+_Ci`, and `Delta_K = theta_KT-theta_KC`.

Report separately the inherited `theta_HT`, `theta_HC`, `Delta_H`, source-support counts, K+ / K- / K_U / nonresponse counts, placement availability, and the joint `(H,K)` table. For an admission with multiple target units, the target admission is K-positive only when every required target unit is jointly H+ and K+; one K- is adverse to the exact construct and one K_U is uncertainty under all-unit precedence. Controls remain specificity comparators, never clinical negative controls. No complete-case deletion is allowed.

Use the inherited sequential inclusion probabilities `pi1_i`, conditional `q_i`, and path weights. Report paired HT/Hájek estimates and design uncertainty with the inherited nested finite-population procedure and at least 20,000 deterministic replicates. A zero/undefined support probability or pair probability produces an undefined quantity and `DEFER`; conditional factors are not called unconditional probabilities.

## Pre-label support, workload, and state machine

The state machine is immutable: `FRAME_SUPPORT_SEALED` -> `TARGET_SEALED` -> `CONTROL_UNIVERSE_SEALED` -> `ANCHOR_SUPPORT_SEALED` -> `PHASE1_LABELS_SEALED` -> `ALLOCATION_SEALED` -> `ACCESS_COMMITTED`. Target/control membership, `Q_S`, `sigma`, document-container indexing, negative-control pools, and all cost constants are sealed before labels.

At `ANCHOR_SUPPORT_SEALED`, compute from the complete inherited frame:

- `N_TC^A`, paired admissions with target and deterministic control and all required `Q_S=1`;
- `N_TC,h^A` in every inherited phase-1 stratum and `N_TC,master^A` in the outcome-blind phase-1 master;
- count of each structural reason (`SOURCE_AMBIGUOUS`, `SOURCE_NONUNIQUE`, missing container, malformed key, and no valid permutation pool);
- positive first-stage and every allowed conditional second-stage support indicator; and
- the full finite workload certificate.

Select the first inherited target cell only if the parents’ floors and all of the following hold: `N_TC^A >= 120`, `N_TC,master^A >= 60`, representation in at least two inherited strata, every target/control unit has positive first- and conditional-phase support under every allowed post-label band partition, both negative-control constructions have a valid pre-label pool, and every allowed partition satisfies the workload ledger. Otherwise set `NO_SELECTION`; never choose a later cell or relax the descriptor rule.

The workload certificate enumerates every finite post-label phase-1 band partition allowed by the inherited state machine, every possible occupied role subcell, and every potential target/control/negative-control packet. It records `T`, target/control/K packet counts, two-reader active minutes, fixed calibration/duplicate/roster charges, reviewer-hours, weekly minutes, roster counts, and 32-week deadline. Use worst-case componentwise maxima; use integer ceiling for each packet conversion and exactly `reserve_minutes=ceil(0.15*(phase2_reading_minutes+fixed_controls_minutes))`. Require `120 <= T <= 300`, target quota at most 180, reviewer-hours at most 1,400, and `charged_minutes <= 84,000`, plus every inherited ceiling. `t2_max_minutes_per_unit` must come from a synthetic-only rehearsal using generated text with known statuses; it cannot use MIMIC text, labels, observed reader times, or a target-dependent expected value. A failed rehearsal, absent bound, or any partition failure yields `NO_SELECTION`.

## Deterministic falsification controls

All controls are constructed before labels with a committed cryptographic seed and are marked non-clinical.

1. **Source-descriptor derangement.** Within each admission, permute `sigma` among the complete eligible `Q_S=1` source-unit pool by a deterministic derangement, excluding identity and incompatible descriptor class/length. Keep the original target/control atom, radiology provenance, DS text, and container metadata. If no valid derangement exists, that negative-control estimand is undefined and the added result is `DEFER`; do not borrow another admission.
2. **DS-container derangement.** Within each admission, permute the complete canonical-DS container (TEXT or DETAIL identity and content) among eligible packets while retaining the frozen source atom and provenance. Do not concatenate or cross-admission match. Require a nonidentity derangement and exclude a container containing the packet’s exact atom/`sigma` by source-only lexical screening. If no valid pool exists, report undefined/`DEFER`.
3. **Atom-preserving lexical decoy.** For a fixed subset of eligible packets whose source `sigma` is unique, replace the presented source descriptor with another same-class dictionary sequence of the same token count from the same admission, while retaining atom metadata and marking it non-clinical. A K+ decoy is a false traceability signal. The decoy pool and replacement are frozen before labels.

The negative-control expected-positive ceiling is strict: each permutation/decoy K+ rate’s simultaneous one-sided 95% upper bound must be at most 0.05. If a control is invalid or its denominator has no positive support, the result is inconclusive, not silently omitted. The verifier must test that every negative-control transformation is independent of H/K outcomes, reader preference, observed time, route, and post-D information.

## Fixed gates and interpretation

The finite family of one-sided tests and max-statistic multiplicity adjustment are frozen before labels and include inherited H outcomes, `Delta_H`, `Delta_K`, target K-failure, both permutation rates, and the decoy rate.

Supportive documentary evidence requires all inherited primary gates; target H-failure upper simultaneous 95% bound `<=0.10`; positive source-support and probability certificates; lower simultaneous 95% bound `Delta_H >= 0.20` and `Delta_K >= 0.20`; target K-failure upper bound `<=0.10`; K_U/nonresponse rates within the pre-registered `0.10`/`0.05` operating limits; each falsifier upper bound `<=0.05`; intact seals, blind rosters, valid spans, finite intervals, and a passing ledger. It supports only a target-cell-specific nomination for a separately approved prospective silent validation.

Adverse documentary evidence is a sufficiently supported exact cell with target K- or H- under the all-unit rule, target no better than its matched control, a simultaneous lower bound below zero, or a valid falsifier above its ceiling. This falsifies the stored-text specificity/anchor claim for that exact cell and blocks bridge priority; it does not imply unsafe care or clinical inappropriateness. K_U, nonresponse, missing placement, structural source nonuniqueness, invalid permutation, undefined interval, insufficient support, failed calibration, or any seal/probability/workload defect is `DEFER`, not adverse clinical evidence. A positive point estimate without the required lower bound is not supportive.

A target with high H+ but low K+ is explicitly reported as “atom reproduced without source-identity anchor.” A high K+ rate with a high permutation rate is “lexical or container confounding,” not actionability. No subgroup, adjacent atom, later target, pooled service, neighboring interval, or control replacement may rescue a failed exact cell.

## Clinical evidence ceiling and required next study

MIMIC contains linked note text/detail and within-admission storage/chart times but no report delivery/view audit, named accountable recipient, order/referral/scheduling/completion, result review, outside-care linkage, patient preference/refusal, UI presentation/edit/override, images, completed follow-up, independent clinical appropriateness adjudication, safety adjudication, or patient-level benefit outcome. `services`, `transfers`, ICU fields, discharge location, death, and hospital-expire fields cannot fill those gaps. The source-identity anchor is not proof that the finding is real, that the recommendation was appropriate, that a responsible clinician saw it, or that any care occurred.

Only a supportive exact cell can nominate a separately governed prospective silent study. Before exposure, that study must collect actual-calendar report availability/delivery/view logs with role and timestamp; accountable clinician/service; target-linked orders, referrals, scheduling, completion and result-review; patient preference; outside care/loss to follow-up; UI display/edit/copy/override; and independent adjudication of finding identity, appropriateness, timing, safety and outcomes. It must suppress alerts, orders, referrals, copied text and patient communication. It must define separate availability, delivery/view, action, completion, safety and clinical-outcome estimands with right-censoring and explicit unknown categories. Missing responsibility, delivery/view, outside care or adjudication maps to `DEFER`. A later contemporaneous comparative intervention study is required for utility, safety, equity, or causal benefit.

## Verification contract and substantive advance

The verifier independently replays source hashes, joins, chronology, first-admission ordering, reciprocal chain, canonical DS, inherited target/control freeze, `Q_S` and `sigma` uniqueness, document-container indexing, exact H/K spans and scope, all-unit adverse precedence, inclusion probabilities, HT/Hájek weights, simultaneous intervals, derangements, decoy pools, and the complete worst-case ledger. It permutes phase-1 labels and confirms that target, controls, `Q_S`, `sigma`, support counts, negative-control pools, and all cost constants are invariant. Fixtures must include copied-but-unanchored text, duplicate source signatures, generic descriptors, pronoun-only references, conflicting intervals, negation/conditional/history, text/detail duplicate content, missing field names, unreadable containers, reader disagreement/nonresponse, no valid derangement, and zero-support paths.

Fixtures establish computation only. Computationally checkable claims are source integrity, deterministic parser behavior, uniqueness, chronology, container boundaries, blinding, support, weights, falsifier construction, margins, and workload. Claims about clinical truth, delivery, viewing, responsibility, action, completion, appropriateness, safety, benefit, equity, and causality require the unavailable prospective evidence and expert adjudication.

The substantive advance over both parents is an actionability proxy that cannot be satisfied by generic co-occurrence, inferred coreference, cross-field concatenation, or a duplicated/nonunique source phrase. It requires a finite source-unique identity signature, an exact atom-and-signature match in one canonical DS container, independently marked attributable spans, and pre-label source-only support for the entire paired domain. It adds deterministic container and descriptor permutation falsifiers, a same-class decoy, structural-versus-outcome unknown handling, and a complete finite workload certificate. It preserves the inherited scientific question and all noncausal limits; even a fully supportive result remains only evidence for a target-specific prospective silent validation, never evidence of delivery, action, safety, benefit, or causality.
