> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 86: joint patientwise documentary certification and uncertainty reserve

## Successor, unresolved question, and advance

This is a substantive successor of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It preserves their mature first eligible resection/documentary-M2 experiment: patient-disjoint calendar roles, coherent operation and report-onset states, whole-accession report units, complete global radiology and pathology books, crossed-book label-stable set (P_LS), locked (B/R/G/Gmask) models, fixed capacity queues, comparator/random gates, anchored deletion, and exact (q_req,q_LS,q_M2,q_dec) frontiers.

The two parents answer different questions. (q_LS) asks whether incomplete stored content retains every current-book maximum-content patient who is documentary-positive under every pathology book. (q_LS_U05) asks whether the observed patient-level loss is small enough, under a declared exchangeability target, for an exact one-sided reserve. (q_DOC) asks whether every protected patient's own eligible accession bundle is complete and all fixed queue positions are source-content-certified. Passing either parent alone is insufficient: zero observed loss can be weak evidence when the protected set is small, while an uncertainty reserve does not certify that the protected patients' own packets are complete.

The new, nonredundant hypothesis is that a single predeclared stored-content threshold can satisfy both requirements simultaneously. Define (q_J) as the smallest allowed aggregate exposure threshold at which, in every required state and anchored deletion, (i) all inherited comparator and documentary retention gates pass, (ii) all required (P_LS) patients have every eligible accession exposed and remain in (S_G), (iii) all (K) ordered queue positions are source-content-certified, and (iv) the family-wise exact upper bound on the protected-patient loss proportion is at most (delta=0.05), conditional on the declared exchangeability model. The experiment asks whether (q_J<1), not whether a real archive or clinician could attain that threshold.

This is a decision-relevant advance over the parents: it supplies one fail-closed evidence-strength contract for deciding whether to fund a prospective archive/version census and silent-mode queue replay. It does not turn an aggregate coverage fraction into report availability, and it makes no claim about biological MVI, clinician action, treatment, safety, benefit, or transportability.

## Evidence and limits

The strongest supported claim before execution is structural: the frozen HCC catalog contains encounter-linked procedure rows, CT/MRI examination acquisition starts and eventual narrative fields, same-encounter pathology narratives, and timed medication/order rows. Full scans inherited from the parents report 105,044 encounter rows, 338,040 procedure rows, 419,996 examination rows, 46,395 pathology rows, 4,097,517 medication rows and 16,730,319 order rows; 392,854 nonblank whole-accession keys, 16,534 multirow accessions (maximum 12 rows), and 8,932 multirow pathology encounters (maximum 14 rows). These establish computability only.

HCC has no report authored/final/release/retrieval/parse-readable/view timestamps, report-version lineage, timezone provenance, pathology time, specimen/accession identifier, slides/blocks, sampling protocol, raw images, clinician action, review capacity audit, recurrence, survival, treatment response, safety, or utility. The eventual report body must therefore be treated as hypothetical stored content, not as content available at (t_dec). The operational gate is `unavailable` for this snapshot even if (q_J<1).

The local natural-history demonstration was inspected and supports temporal development and longitudinal testing; the local Bayesian demonstration was inspected and supports explicit likelihood/selection-bias accounting. The cancer demonstration's main paper and STAR Methods remain unavailable; only its supplement was inspected. A current Europe PMC search was frozen as source `[source checksum]`; its results motivate, but do not validate, external pathology and imaging evidence. No external paper supplies an HCC endpoint or replaces missing HCC metadata.

## Population and time

The unit is one adult patient and the first eligible source-documented hepatobiliary resection. A surgeon-locked procedure dictionary identifies resection in `procedures.surgery`; earlier qualifying resection and recorded transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in ([t_op-365d,t_op)) exclude the episode using patient-wide timed procedures, medications and orders. Ambiguous dictionary membership is an outer coherent state. Age and recorded sex are descriptive only.

Join encounter-level tables on ((Patient master index,Encounter number)). An explicitly supported exact procedure clock is a point; a date-like case-record clock is ([d,d+24h)); missing, contradictory and competing clocks remain coherent alternatives. Never use admission/discharge as an operation substitute. Set (t_dec=t_op-24h). An acquisition is eligible only if its interval is wholly inside ([t_op-90d,t_dec)). Report onset states are monotone: available by 72h, first in (72,48]h, (48,24]h, (24,12]h, or later/never; 24h is confirmatory and other cutoffs are sensitivities.

Use patient-disjoint 2015–2018 development, 2019 preprocessing/hyperparameter/capacity lock, separate 2020 and 2021 tests, and 2022+ audit only. Quarantine any patient that could cross calendar roles.

## Predictors, endpoint, and states

The locked models are:

- (B): age, recorded sex, eligible acquisition count/recency, modality/ambiguity and development-grouped machine;
- (R): (B) plus nonsemantic surface/availability fields;
- (G): (B/R) plus frozen radiology-book content features;
- (Gmask): the identical fitted (G) with semantic blocks replaced by the training-defined unavailable block, with no refit;
- exact capacity-matched uniform random capture.

Patient IDs, pathology, labs, untimed notes, future rows, reader identity and test-derived dictionaries are forbidden predictors. Fit preprocessing, coefficients, penalty, score bytes, ties and (K_
ho=lfloor
ho N_ref
floor) in 2019; use (
ho=.10) primary and .05/.20 sensitivities, requiring (N_refge500,K_.05ge25,K_.10ge50,K_.20ge100), (Nge K_.10), and at least 50 documentary-positive events in each primary test state.

Three globally fixed Chinese-reading radiology books and three globally fixed pathology books are created before analysis. No row-wise book mixing is allowed. Pathology terminals remain OUT, IN0-A, IN1-A, IN0-U, IN1-U; every state maps its terminal to documentary (Y_i(a,b)), never a predictor.

An examination unit is the indivisible whole accession ((patient master index, encounter number, examination number)), with every component row retained in raw ordinal order. Blank accession, component disagreement, ambiguous modality or irreversible parsing makes the unit unavailable. A source-clean unit has monotone exposure (M) according to the onset state; (M) is not a claim of finalization or viewing. (S_G(s,q)) is the incomplete-content fixed-(K) queue and (S_max(s)) is the same frozen model with all source-clean eligible units exposed. Anchored deletion removes all records of one patient without refit, reranking, backfill or requota; the deleted offered slot remains EMPTY.

For each nonpathology state (a), (U_LS(a)={i:Y_i(a,b)=1 orall b}). For current pathology book (b), (P_LS(a,b)=S_max(a,b)cap U_LS(a)), (P_M2(a,b)=S_max(a,b)cap{i:Y_i(a,b)=1}), and (P_common(a)=cap_b P_M2(a,b)). Preserve (P_commonsubseteq P_LSsubseteq P_M2subseteq S_max) when nonempty.

## Estimands and analysis

Retain the inherited strict margins (100(H_G-H_C)/K>5) for (Cin{B,R,Gmask}), random-K cross-product margin, separate-year/source/reader/pathology/deletion gates, and exact rational threshold lattice (mathcal R). Retain exact (q_req,q_LS,q_M2,q_dec), immediate lower-threshold witnesses, and all score/queue hashes.

For each state (s), threshold (q), and patient (i), let (A_i(s,q)=1) iff every eligible nonblank accession for (i) is exposed. Patients with no eligible accession never receive (A_i=1). Let (J_DOC(s,q)=1[P_LS(a,b)subseteq{i:A_i=1}]land[P_LS(a,b)subseteq S_G(s,q)]), and let (K_cert(s,q)=|S_G(s,q)cap{i:A_i=1}|). A documentary certificate requires (J_DOC=1) and (K_cert=K) in every required state.

For each required state (c=(a,b)), let (m_c(q)=|P_LS(c)|), (x_c(q)=|P_LS(c)setminus S_G(c,q)|). Empty (P_LS) is nonvacuous failure. After freezing the complete state registry and threshold lattice, use (M=|mathcal R|max_q|C(q)|), (alpha=.05/M), and the exact one-sided Clopper–Pearson upper bound (U_c(q)=Beta^{-1}(1-alpha;x_c+1,m_c-x_c)), retaining integer counts, library/version and decimal output. No normal approximation or downsampling is allowed. A reserve passes only if every required (U_c(q)le.05), with exchangeability explicitly declared; under fixed-census interpretation the bound is descriptive and the reserve claim is inconclusive.

Define:
[
q_J=min{qinmathcal R:
  PASS(q)=1, q	ext{ has all required nonempty }P_LS, 
  J_DOC(s,q)=1, K_cert(s,q)=K, 
  U_c(q)le.05 orall c}.
]
Evaluate every (q) directly; do not assume monotonicity of (U_c). Report (q_J), all component frontiers, lower-bound witnesses, protected/unprotected patient hashes, accession exposure counts, reserve gaps, (N,Y,K,n_A,e,Q), EMPTY slots, queue rank changes, and exact model/score hashes. Require and verify the diagnostic nesting (q_reqle q_LSle q_J); do not assert an order involving (q_M2) or (q_dec) because patientwise certification and exact queue equality are different requirements.

## Falsification and interpretation

Use one-hot precedence:

1. `computationally_inconclusive`: any source/header/schema/hash, raw ordinal, accession grain, clock, state, book completeness, score/tie, deletion, threshold, exact-bound, set/hash, witness or invariant check fails.
2. `feasibility_inconclusive`: fixed-frame, (N/K/event/n_A) requirements fail.
3. `maximum_content_signal_adverse`: any inherited comparator, random, year, reader, source or deletion gate fails.
4. `aggregate_capture_reserve_adverse`: (q_req) undefined/equal 1.
5. `label_stability_attribution_inconclusive`: required (P_LS) empty.
6. `book_specific_retention_adverse`: (q_LS) undefined/equal 1.
7. `patientwise_documentary_certificate_adverse`: (q_J) undefined/equal 1 because at least one protected patient lacks a complete bundle or (K_cert<K).
8. `uncertainty_reserve_inconclusive`: exchangeability is not declared, or an exact reserve is undefined; report q_LS/q_DOC descriptively.
9. `joint_documentary_reserve_adverse`: q_DOC/q_LS_U05 component claims pass but q_J fails; identify the state, patient, slot, or exact upper bound.
10. `joint_documentary_reserve_supportive_bridge_pending`: q_J<1, all witnesses and gates pass, and the operational metadata gate remains unavailable.

Supportive means only that a finite, retrospective, hypothetical stored-content contract passed. Adverse means the named documentary contract was falsified in a required state. Inconclusive means computation, nonvacuity, feasibility, or the inferential target prevented the claim. No result means reports were actually available, clinical review occurred, biological MVI was present, treatment changed, or patients benefited.

## Exact source bindings

All are read-only ordinary CSVs; no archive members beyond ordinary files. Use the live catalog schema hashes and preserve raw headers/ordinals.

- `encounters`, `table-b743286cb1249287.json`, source `[internal dataset path]`; join ((patient master index,encounter number)); `age,sex,encounter time,admission time,discharge time`.
- `procedures`, `table-d5eae16f8f8093d9.json`, source `[internal dataset path]`; encounter join; `Surgery,Start time,End time,Surgery source`.
- `examinations`, `table-fd016d2731b9d6c6.json`, source `[internal dataset path]`; encounter plus `examination number`; `examination,examination findings,examination diagnosis,start time,machine model,examination number`.
- `pathology`, `table-0a4ee86a446c605c.json`, source `[internal dataset path]`; encounter join only; `pathology, examination findings, examination diagnosis, machine model`; no time/specimen/accession.
- `medications`, `table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`; patient-wide time join; `Medication,Drug Type,Start Time,End Time`.
- `orders`, `table-6b93dcf0ea823702.json`, source `[internal dataset path]`; patient-wide time join; `Non-drug Orders,Order Time,Start Time,End Time,Order Status`.
- `diagnoses`, `table-12710723c3df0c99.json`, source `[internal dataset path]`; encounter join; `Diagnosis Name,Diagnosis Type`, untimed corroboration only.
- `clinical_documents`, `table-66afca58512c2fca.json`, source `[internal dataset path]`; encounter join; `chief complaint, history of present illness, past medical history, personal history, menstrual history, marital and childbearing history, family history, admission diagnosis, admission status, admission diagnosis__duplicate_2, treatment course, discharge status, discharge diagnosis, surgery name, surgical procedure`; leakage audit only.
- `labs`, `table-38aad8c54471332f.json`, source `[internal dataset path]`; encounter join; `Test,Qualitative Result,Quantitative Result,Specimen Type,Test Time`; audit only, never primary predictors because units/timing are unsafe.
- `vitals`, `table-8436de9cba74b8ca.json`; source `[internal dataset path]`; encounter identifiers only.
- `transfers`, `table-320c20f732e71789.json`; source `[internal dataset path]`; encounter identifiers only.
- `front_page`, `table-38b3224239acc33f.json`; source `[internal dataset path]`; encounter identifiers only.

MIMIC, eICU and UKB remain directly accessible but are not pooled: no patient crosswalk, compatible first-resection frame, Chinese reader books or documentary-M2 endpoint exists.

## Required evidence, artifacts, and verifier limits

Derive only workspace files: source manifest/raw ordinal ledger; whole-accession interval-clock ledger; coupled state registry; locked model/score/tie manifest; all q-frontiers including q_J; patientwise certificate and reserve witnesses; anchored-deletion results; operational_metadata_status; interpretation; and a no-sampling source audit. Keep source files read-only.

A verifier can check source/schema/header/hash/ordinal replay, joins, clocks, temporal quarantine, forbidden predictors, global book pairing, state coupling, exact queues, deletion, exact CP arithmetic, q frontiers, nonvacuity, q_J minimality, nested inequalities, witnesses, one-hot labels, and prose-output linkage. It cannot establish radiology/pathology semantic validity, procedure dictionary correctness, pathology sampling adequacy, biological MVI, actual report lifecycle/viewing, clinical action, utility, safety, causality, benefit, fairness, transportability, recurrence, survival, or patient outcomes. Those require expert adjudication, versioned archive telemetry, linked outcomes, and prospective silent-mode or decision-appropriate interventional study.

Adversarial fixtures must include high aggregate Q with one protected patient unexposed; q_LS<q_DOC; K_cert=K-1; exact loss with q_LS_U05 failing; q_DOC passing but q_J failing due reserve; all components passing; empty P_LS; score ties; anchored deletion; N=K; q_J=1 paired with supportive prose; fixed-census exchangeability omitted; and supportive prose making unavailable operational or biological claims.
