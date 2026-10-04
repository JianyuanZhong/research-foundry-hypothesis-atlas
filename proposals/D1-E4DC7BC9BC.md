> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Cutoff-anchored archive and operational replay bridge for the HCC q_dec queue

## 1. Targeted successor and unresolved question

This is a targeted successor of `[prior hypothesis]` and preserves the patient-level q_dec experiment from `[prior hypothesis]`. It changes only the remaining external decision-validity weakness: the prior archive bridge could count a report that was eventually stored and hash-matched without proving that the same complete accession/version was available at the preoperative deadline or that an operational queue used that as-of-deadline state.

The clinical decision under study is narrow: allocation of a fixed number of scarce documentary-review offers among adults approaching an eligible HCC resection. It is not a recommendation about resection, transplantation, surveillance, systemic/local treatment, biological microvascular invasion (MVI), or patient benefit.

The unresolved question is:

> In the frozen HCC-derived patient/accession frame, does a version-faithful, complete report archive provide enough content by the 24-hour preoperative deadline to preserve the same fixed-K patient set as the same-world maximum-stored-content q_dec oracle, and can an operational queue reproduce that as-of-deadline state without using later text?

The advance is a jointly falsifiable bridge. Archive coverage and operational replay must pass together. Eventual presence of text in HCC is audit evidence only; it never establishes pre-deadline availability.

## 2. Evidence boundary and hypothesis

The strongest supported claim is structural. The HCC snapshot contains encounter-linked procedure rows, acquisition-like examination timestamps, whole-accession multirow narrative fields, and same-encounter pathology narratives. The inherited experiment can test a finite-corpus documentary-M2 queue predicate under coupled source, interval-clock, accession, onset, reader, pathology, year and deletion states.

The unresolved claim is weaker than clinical effectiveness and is testable:

> At rho=0.10 and d=24 hours, after all inherited comparator/random/deletion gates and q_dec patient-set equality pass, the frozen HCC-derived eligible patient frame has a simultaneous lower bound q_cut,L >= q_dec for complete, version-faithful, technically retrievable and readable report packets available by the deadline; and a deterministic queue service can reproduce the locked queue from only those cutoff packets and frozen unavailable blocks.

Here q_dec is the inherited smallest exact patient-complete coverage threshold at which the semantic fixed-K queue equals the same-world maximum-stored-content queue in every compatible HCC state. q_cut,L is an externally audited lower bound on *cutoff-valid* patient-complete coverage, not a hospital coverage rate and not an archive-defined denominator.

This hypothesis does not assert that a clinician viewed a report, acted on it, changed treatment, improved outcome, or that documentary M2 is biological MVI.

## 3. Frozen population, time, endpoint and inherited analysis

Use HCC snapshot `[source checksum]` and catalog `[internal dataset path]`, catalog [source checksum].

Within every coupled source/operation world, include adults (age >=18 in the frozen encounter row) at the earliest source-documented eligible hepatobiliary resection under a pre-analysis clinician-adjudicated procedure dictionary. Require same-(Patient ID, Encounter ID) pathology support. Exclude a prior qualifying resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in [t_op-365 days,t_op). CT/MRI accessions must lie wholly in [t_op-90 days,t_op-d), with d in {72,48,24,12} hours; d=24 is confirmatory and the others are non-vetoing sensitivities.

An exact operation timestamp is used as an instant. A date-only or midnight-like operation value is the interval [date,date+24 hours), never an inferred hour. Missing, contradictory, invalid or ambiguous operation clocks remain compatible unavailable states. A cutoff claim is valid only for every compatible operation time; equivalently, the packet must be valid by the earliest possible deadline t_op^- - 24h. Source, operation, identity, onset, archive, reader, pathology, year and deletion alternatives remain coupled.

Use patient-disjoint 2015–2018 development, 2019 preprocessing/hyperparameter/K lock, separate 2020 and 2021 tests, and 2022 onward audit-only. The endpoint is same-encounter documentary M2. Two qualified Chinese-reading hepatobiliary pathologists plus an adjudicator produce complete pathology books with OUT, IN0-A, IN1-A, IN0-U and IN1-U terminals; two qualified Chinese-reading abdominal radiologists plus an adjudicator produce complete radiology books. Use nine global reader/pathology pairs fixed across all years, cutoffs, worlds, models and deletions. Unresolved labels remain outer states.

Retain the inherited patient-balanced, outcome-blind pipelines:

- B(Z): acquisition-only;
- R(Z,S,Q): acquisition plus report surface/availability;
- G(Z,S,Q,X): semantic model;
- Gmask: the same fitted G with semantic blocks replaced by the training-defined unavailable block, with no refit.

Z includes age, sex, acquisition facts, eligible-accession count/recency, accession ambiguity and development-grouped machine. Exclude pathology, endpoint labels, IDs, reader identity, labs, untimed narratives and test-derived features. Freeze preprocessing, regularization, parameters, exact binary64 score serialization, tie keys and K after the independent 2019 lock.

Use N_ref and K_rho=floor(rho N_ref), rho in {0.05,0.10,0.20}; require N_ref>=500, K_.05>=25, K_.10>=50 and K_.20>=100. Each primary test year requires N>=K_.10 and at least 50 documentary-positive events. Preserve fixed original K positions and anchored singleton deletion: deletion removes all patient records without backfill or requota.

The inherited internal gates, q_req, q_dec, q_dec>=q_req check, whole-accession identity, interval-safe clocks, patient-set equality, ordered-slot diagnostic, exact threshold frontier, comparator/random margins and uncertainty procedure are unchanged. The maximum-content oracle is a same-world oracle, not biological truth and not an archive observation.

## 4. Exact HCC source bindings

All HCC sources are ordinary files with no archive members. Sources remain read-only. Retain catalog SHA-256/schema hash, BOM handling, raw ordinal, reversible raw-byte pointer and deterministic inclusion/exclusion reason.

| table | exact source path | join key | required columns and role |
|---|---|---|---|
| encounters | `[internal dataset path]` | (patient master index, encounter number) | age, sex, encounter time, admission time, discharge time; demographics and chronology |
| procedures | `[internal dataset path]` | (patient master index, encounter number) | surgery, start time, end time, surgical source; index operation, clock and prior-treatment exclusions |
| examinations | `[internal dataset path]` | whole accession (Patient Master Index, Encounter Number, Examination Number), with encounter prefix | Examination, Examination Findings, Examination Diagnosis, Start Time, Machine Model, Examination Number; CT/MRI eligibility and complete report bundle |
| pathology | `[internal dataset path]` | (Patient Master Index, encounter number) | pathology, examination findings, examination diagnosis, machine model; documentary endpoint adjudication only |
| medications | `[internal dataset path]` | patient-wide temporal join then episode restriction | Medication, Drug Type, Start Time, End Time; prior systemic-treatment exclusion |
| orders | `[internal dataset path]` | patient-wide temporal join | non-medication order, order time, start time, end time, order status; prior local/radiotherapy exclusion |
| diagnoses | `[internal dataset path]` | (patient master index, encounter number) | diagnosis name, diagnosis type; untimed HCC corroboration only |
| clinical_documents | `[internal dataset path]` | (Patient master index, encounter number) | all narrative fields; audit-only because no safe preoperative exposure clock |
| labs | `[internal dataset path]` | (Patient Master Index, encounter number) | test, qualitative result, quantitative result, specimen type, test time; leakage audit only, no primary lineage |
| vitals | `[internal dataset path]` | (Patient master index, encounter number) | identifiers only; no usable payload/time |
| transfers | `[internal dataset path]` | (patient master index, encounter number) | identifiers only; no usable payload/time |
| front_page | `[internal dataset path]` | (patient master index, visit number) | identifiers only; no usable payload/time |

Group every examination row by the complete nonblank accession key in raw ordinal order. Never choose a representative row or deduplicate repeated text. The source audit reports 419,996 examination rows, 72 blank examination-number rows, 392,854 distinct nonblank keys, 16,534 multirow keys and at most 12 rows/key. Any blank key, component disagreement, ambiguous modality or non-reversible parse makes that whole accession unavailable. The procedure file has 338,040 rows and 42,117 missing start/end cells; retain exact/date-interval/missing/invalid categories.

The other configured datasets remain directly accessible and read-only but are not pooled: MIMIC ordinary files plus archive `[internal dataset path]`, including member `mimic-iv-3.1/hosp/admissions.csv.gz`, and ordinary `note/radiology.csv.gz` and `note/radiology_detail.csv.gz`; eICU ordinary `*.csv.gz` under `[internal dataset path]`, including `patient.csv.gz`, `diagnosis.csv.gz`, `treatment.csv.gz` and `note.csv.gz`; UKB ordinary files under `[internal dataset path]`, including `ukb672073.csv` and `ukb672073_Health_Related_Outcomes.csv`. No compatible HCC crosswalk or documentary-M2 endpoint exists for pooling, so no cross-dataset estimate is made.

## 5. Whole-accession stored-content and q_dec computation

For each patient i, source world omega, cutoff d and accession u, define E_iomega d u=1 only when operation state, accession identity, CT/MRI membership and examination start time are valid and the acquisition interval is wholly in the preregistered window. The unit is the indivisible complete accession.

Assign each clean eligible accession coupled onset O=0 if eligible by 72h, O=1 if first eligible in (72,48], O=2 if first eligible in (48,24], O=3 if first eligible in (24,12], and O=4 if not eligible by 12h or only later/never. Use V(O)=(1{O=0},1{O<=1},1{O<=2},1{O<=3}) in 72/48/24/12 order. M=E*V is a hypothetical stored-content exposure state, never an imputed release or viewing time.

For d=24, retain N, n_A, e=n_A/N, I=0, incomplete and complete patient strata. Q_omega,a(O) is the complete-bundle proportion among the fixed n_A denominator. If n_A=0, label feasibility-inconclusive, never Q=0 or 1. Construct the exact rational threshold set from retained k/n_A values. q_req is the smallest threshold passing inherited gates in every compatible state; q_dec is the smallest threshold passing those gates plus exact fixed-K patient-set equality between G and its same-world all-stored-content oracle. Report q_req, q_dec, q_dec-q_req, exact boundary witnesses, set differences, ordered-slot disagreement and all denominators.

## 6. New cutoff-anchored archive bridge

The external archive must audit the frozen HCC-derived frame; it may not redefine N, A, modality, operation eligibility, pathology eligibility or the patient denominator.

For each frozen eligible accession u, the archive supplies an append-only availability packet with:

1. HCC identity: patient hash, encounter key, whole accession key, every HCC raw row ordinal, raw-row SHA-256 and the frozen source-manifest/schema hash.
2. Complete component identity: one record for every HCC examination component, archive component ID, immutable report-version ID, predecessor/successor/amendment/retraction IDs, component order and component-complete canonical payload hash.
3. Point-in-time status: authored, finalized, released, ingested, technically retrievable, parse-readable and retracted timestamps, each with timezone, clock source, clock uncertainty and correction history. A status is valid only if it is supported by an immutable event/audit log, not by the current value of a mutable status field.
4. Cutoff verdict: for every compatible operation time and therefore every compatible deadline, a signed `available_complete_at_cutoff` bit, with the exact version IDs and hashes that were available then. Missing, ambiguous, unresolved, post-deadline or later-amended components are 0, not recovered from eventual text.
5. Later evidence quarantine: any payload/version first found or supplied after the deadline is retained only in a `post_cutoff_audit` field. It cannot alter the primary availability bit, q_cut,L, packet replay or queue.
6. Clock and integrity anchors: archive timezone database/version, synchronized clock source, event-log sequence/monotonic ID, packet creation time, input-bundle hash and signer/key ID.

The whole accession is cutoff-valid only when every component maps one-to-one, all canonical hashes match the frozen HCC component ledger, one immutable version was complete and non-retracted by the deadline, and the complete payload was technically retrievable and parse-readable by the deadline. A later report with identical text is still invalid for that deadline if its version or availability event is later. A changed or amended version is a new version; it cannot silently replace the earlier packet.

For patient i, cutoff completeness C_i=1 only if every accession in the frozen A_i,omega is cutoff-valid. The denominator remains n_A patients with at least one HCC-derived eligible accession. Retain I=0 patients, every sampled patient with incomplete coverage, all nonresponders and all archive ambiguity. Estimate year-specific design-based simultaneous lower bounds L_2020 and L_2021 from a prespecified probability sample of the fixed HCC patient frame, sampling patients and enumerating every accession in each sampled A_i. Define q_cut,L=min(L_2020,L_2021). A census may replace sampling but must retain the same frame and fields. The archive bridge passes only if q_cut,L>=q_dec; q_cut,L>=q_req supports aggregate capture only.

A coverage percentage over archive rows, an eventual nonempty text count, a pooled-year bound, or a bound that discards nonresponders cannot pass this bridge.

## 7. Joint operational replay predicate

Operational interpretation is deliberately technical: “the locked documentary queue can be generated at the deadline from point-in-time archive packets.” It is not “a clinician received/viewed/acted on the queue.”

For each test-year patient and each compatible deadline, the service must emit an immutable queue-generation record containing:

- packet ID and frozen HCC frame hash;
- deadline interval and chosen conservative boundary;
- exact report-version/component IDs, payload hashes and unavailable mask used;
- locked model/preprocessing/book-pair hash, rho, K, score bits and tie key;
- protected patient hashes in original fixed K positions, including EMPTY;
- generation timestamp, synchronized clock evidence and service identity;
- feature/input digest, queue digest, and a no-post-deadline-input attestation;
- correction, retry, amendment and deletion logs.

The operational replay predicate O_PASS is true only if an independent verifier, using the packet’s as-of-deadline bytes and the training-defined unavailable block for missing components, reproduces the exact locked scores, tie order, queue hash and fixed K positions. It must also reproduce the same patient-set comparison with the same-world maximum-content oracle where that oracle is applicable. No later HCC text, later archive version, post-deadline retrieval, mutable current status or hidden backfill may enter the packet.

The joint bridge predicate is:

`BRIDGE_PASS = (q_cut,L >= q_dec) AND O_PASS`

evaluated separately for 2020 and 2021 and then under the inherited simultaneous worst-case rule. Archive coverage without replay is not operational support; replay without cutoff-valid coverage is not an archive bridge. A service may output an unavailable queue, but it may not label a later-completed report as available at the earlier deadline.

## 8. Falsification, interpretation and uncertainty

Use one mutually exclusive primary interpretation:

- `computationally_inconclusive`: lossless source replay, full-accession grouping, interval-clock logic, coupled-state enumeration, exact ranking, q_req/q_dec frontier, witness, deletion, archive event provenance or independent verifier fails.
- `feasibility_inconclusive`: N/K/event/n_A or structural denominator requirements fail.
- `maximum_content_signal_adverse`: the inherited maximum-content comparator, random or deletion gate fails.
- `conditional_coverage_adverse`: q_req is undefined or equals 1.
- `mixed_capture_supportive_queue_adverse`: q_req<1 but q_dec is undefined or equals 1; aggregate capture survives but patient-set identity does not.
- `documentary_decision_supportive_bridge_pending`: internal q_dec support is valid, but no cutoff-valid archive or operational packet is available. This is not adverse evidence.
- `archive_cutoff_bridge_adverse`: internal support is valid and the archive is auditable, but q_cut,L<q_dec, or a known fraction is available only after the deadline/version boundary.
- `operational_replay_adverse`: q_cut,L>=q_dec, but O_PASS fails, including use of post-deadline text, wrong version/component hash, changed patient set, changed K positions, or hidden backfill.
- `mixed_archive_supportive_operation_adverse`: cutoff archive coverage meets q_dec but the operational implementation fails; the archive bridge is supported, deployment reproducibility is not.
- `cutoff_bridge_and_technical_replay_supported`: internal gates, q_dec minimality, q_cut,L>=q_dec, packet identity/version conditions, simultaneous uncertainty, and O_PASS all pass.

The supportive label means only finite-corpus documentary queue validity plus a technical cutoff replay bridge. It does not establish viewing, clinician action, biological MVI, treatment benefit, recurrence, survival, harms, costs, fairness, transportability or utility. Those require clinical adjudication, source-system evidence or a prospective/silent-mode workflow and outcome study.

Adverse archive coverage is falsification of the proposed cutoff bridge, not falsification of the internal q_dec result. An inconclusive archive caused by missing fields, nonresponse accounting, unresolved clock provenance or competing versions cannot be converted to support by assuming the favorable state. Mixed results must report both components.

## 9. Required outputs and independent verification

Write only workspace-derived files; all source files remain read-only:

- `derived/source_manifest_and_raw_ordinal_ledger.parquet`;
- `derived/whole_accession_and_interval_clock_ledger.parquet`;
- `derived/patient_complete_qreq_qdec_witnesses.parquet`;
- `derived/fixed_k_queue_signatures_and_set_differences.parquet`;
- `derived/archive_cutoff_packet_ledger.parquet`;
- `derived/archive_coverage_strata_and_qcut_lower_bounds.parquet`;
- `derived/operational_replay_ledger.parquet`;
- `derived/interpretation.json`;
- `derived/archive_bridge_audit.json`;
- exact source/schema/hash, reader/pathology, coupled-state, threshold, deletion, packet-integrity and replay logs.

The verifier independently checks all 12 HCC source hashes and schemas; BOM/raw ordinals; whole-accession component retention; interval-valued operation clocks; fixed HCC-derived N/A and n_A denominators; coupled worlds; exact score/tie serialization; no-backfill deletion; inherited gates; q_dec>=q_req; archive one-to-one version/component/hash mapping; immutable as-of-cutoff event evidence; retained nonresponders; simultaneous lower bounds; packet-to-queue byte/hash replay; no-post-deadline attestation; and conclusion-to-output links.

Fixtures must include: multirow accessions; duplicate text with distinct rows; blank accession; midnight and missing operation clocks; compatible boundary times; O=2/O=3 transitions; zero-accession patient; partial bundle; exact ties; N=K; n_A=0; deleted selected patient; same aggregate capture with different patient sets; later-arriving identical text; later amendment; retraction; timezone ambiguity; archive row/hash mismatch; one-year lower-bound failure; queue generated with eventual text; and a packet that reproduces scores but not the fixed patient set.

The verifier can establish computation, provenance, exact documentary q_dec validity, cutoff packet integrity and whether the operational prose follows from outputs. It cannot establish Chinese semantic correctness, report viewing, clinician action, biological truth, treatment effect, patient outcome or utility. Those claims require expert review or another study.

## 10. Substantive change and remaining unavailable evidence

This successor adds a single decision-validity repair: it binds archive evidence and operational interpretation to the same immutable as-of-deadline packet. It preserves the exact HCC denominator, whole-accession identity, interval-safe operation clocks, coupled pathology/reader uncertainty, same-world maximum-content oracle, patient-set equality, fixed-K comparator/random/deletion gates and fail-closed limits.

HCC itself lacks report-version, finalization/release/retrieval/readability/amendment/retraction/view timestamps; raw images; specimen/block/slide/accession linkage; pathology time; and clinical action, outcome, harm, cost or utility fields. The HCC archive bridge will therefore normally be `documentary_decision_supportive_bridge_pending` unless an external archive supplies the specified frozen-frame packet. Eventual stored HCC text is never treated as evidence of pre-deadline service availability.
