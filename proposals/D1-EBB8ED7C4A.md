> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Individual documentary-M2 comparator-loss frontier for a report-robust HCC queue

## 1. Successor, unresolved question, and substantive advance

This is a targeted successor of assessed-valid [prior hypothesis] (q_M2), with assessed-valid [prior hypothesis] (q_safe) as the second parent.

The parents establish complementary guarantees:

- q_M2 tests whether every documentary-M2 patient in the same-world maximum-stored-content G queue remains in the incomplete-bundle G queue.
- q_safe tests aggregate documentary-M2 non-loss against B, R, Gmask, and exact uniform-random capture in four recorded age-by-sex cells, while retaining q_dec queue identity.

A remaining individual-patient defect is not covered by either guarantee. A patient can be offered by B, R, or Gmask and be dropped by G while another documentary-M2 patient replaces that patient. The replacement can preserve aggregate capture within every q_safe cell, and the dropped patient can be absent from the maximum-content G queue so that q_M2 and q_dec both pass. Thus the existing design does not ask whether G withdraws an identifiable documentary-M2 review opportunity that an already-defined deterministic comparator would have offered.

The new estimand is q_IP, an exact patient-level comparator-loss frontier. At every coupled state and anchored patient-deletion state, it counts documentary-M2 patients in each comparator's fixed-K queue who are not in G's fixed-K queue. The primary individual safety contract is zero such losses for each deterministic comparator C in {B,R,Gmask}. It is a no-loss/regret contract, not a utility model and not a claim that every comparator-offered patient truly has biological MVI.

This is nonredundant:

1. q_M2 compares incomplete G with maximum-content G and protects only maximum-content G documentary positives.
2. q_safe compares counts, including subgroup counts, and does not protect identities.
3. q_IP compares identities of documentary positives offered by each locked comparator and detects a one-for-one individual loss hidden by q_safe.

No model, feature, threshold, capacity, workload, clinical action, or report-timing assumption is added.

## 2. Evidence-supported claim versus hypothesis

### Strongest claim supported before execution

Direct inspection of the frozen HCC catalog, table schemas, and raw headers establishes that the snapshot contains encounter-linked age/recorded-sex fields, procedure start/end fields, whole-accession CT/MRI-like examinations with acquisition-like start times and stored narrative fields, same-encounter pathology narrative, and dated medication/order rows. The inherited audits read all rows of encounters, procedures, examinations, and pathology and retained raw ordinals. These facts establish that the proposed patient and queue joins are source-feasible; they do not establish the clinical procedure dictionary, M2 semantics, report availability, model validity, or patient benefit.

The public literature is motivation, not validation of this experiment. Li et al. studied the prognostic association of graded microvascular invasion after HCC resection (DOI 10.1186/s12957-026-04229-2; frozen full-text source ID [source checksum], [source checksum]). Kocak et al. reviewed bias and fairness across the healthcare-AI lifecycle (DOI 10.4274/balkanmedj.galenos.2026.2026-6-3; frozen full-text source ID [source checksum], [source checksum]). Neither addresses whether report-bundle missingness removes individual patients from a fixed HCC review queue. Neither supplies report-release timing, queue utility, or an answer to q_IP.

### Untested hypothesis

At rho=0.10 and d=24 hours, in both the 2020 and 2021 independent tests, q_IP is below 1 after all inherited maximum-content, overall, queue-identity, subgroup, random, and deletion conditions pass:

1. maximum stored content passes every inherited strict G-versus-B, G-versus-R, G-versus-Gmask, and capacity-matched-random gate;
2. q_req < 1, q_M2 < 1, q_dec < 1, and q_safe < 1; and
3. q_IP < 1, where q_IP is the smallest exact patient-complete conditional bundle-coverage threshold at which no documentary-M2 patient offered by B, R, or Gmask is absent from G in any allowed same-world state or anchored deletion.

This is a stronger individual decision-safety claim than either parent. It remains retrospective and documentary: a positive is a same-encounter pathology-book classification, not biological MVI. It does not test actual report release, clinician review, treatment, recurrence, survival, or harm.

## 3. Population, time boundaries, and endpoint

Preserve the parent population exactly in every coherent source/operation world:

- adults with age >=18 in encounters Age, at the earliest source-documented eligible hepatobiliary resection under a preregistered procedure dictionary reviewed by a hepatobiliary surgeon;
- same-(Patient Master Index, Encounter Number) pathology narrative sufficient for the documentary endpoint under at least one complete pathology book;
- no earlier qualifying resection and no recorded transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in [t_op-365 days, t_op), using procedures, medications, and non-medication orders;
- ambiguous treatment membership remains a separate outer state and is never resolved in favor of eligibility.

Use only clinically supported operation times. A point time is used when justified by the anaesthesia-system procedure record. A date-only or midnight-like case value is the interval [date,date+24 hours). Missing, contradictory, non-reversible, or clinically ambiguous times remain unavailable/alternative source states. Encounter admission, discharge, or visit time never substitutes for operation time.

For primary d=24 hours, an eligible CT/MRI accession must have its acquisition interval wholly within [t_op-90 days, t_op-24 hours). The 12-, 48-, and 72-hour analyses are locked sensitivities and cannot rescue or veto the 24-hour conclusion. Exposure onset is coupled across cutoffs: O=0 eligible by 72 hours, O=1 first eligible in (72,48] hours, O=2 in (48,24] hours, O=3 in (24,12] hours, and O=4 later/never. The monotone exposure vectors are retained in 72/48/24/12 order. Exposure means hypothetical inclusion of eventual stored report content, not authored, finalized, released, retrieved, read, or viewed content.

Use patient-disjoint temporal roles: 2015-2018 development; 2019 preprocessing, hyperparameter, feature/tie/K lock; separate 2020 and 2021 tests; 2022 onward audit only. Any possible membership in a later role quarantines the patient from every earlier role.

The unit is one patient at the first eligible episode. The policy unit is one fixed queue position. The endpoint is encounter-documentary M2 from same-encounter pathology, never a claim of specimen-linked or biological MVI.

## 4. Exact read-only HCC bindings

All twelve HCC sources are ordinary CSV files. There are no HCC archive members. Use catalog [internal dataset path], catalog [source checksum], and HCC snapshot [source checksum].

| Table | Exact source path | Join key | Required columns and role |
|---|---|---|---|
| encounters | [internal dataset path] | (Patient master index, encounter number) | age, sex, encounter time, admission time, discharge time; index demographics and audit clocks |
| procedures | [internal dataset path] | encounter key | Surgery, start time, end time, surgery source; eligible operation and prior-operation clocks |
| examinations | [internal dataset path] | encounter key plus whole accession (Patient master index,Encounter number,Examination number) | Examination,Examination findings,Examination diagnosis,Start time,Machine model,Examination number; accession identity, acquisition-like time, report surface/content |
| pathology | [internal dataset path] | encounter key only | Pathology,Examination Findings,Examination Diagnosis,Machine Model; documentary endpoint; no pathology time/specimen/accession |
| medications | [internal dataset path] | patient-wide temporal join, then episode restriction | Medication,Drug Type,Start Time,End Time; prior-treatment exclusion |
| orders | [internal dataset path](Non-Drug)_2062526727266216118.csv | patient-wide temporal join | Non-Drug Order,Order Placement Time,Start Time,End Time,Order Status; prior-treatment exclusion |
| diagnoses | [internal dataset path] | encounter key | Diagnosis Name, Diagnosis Type; untimed corroboration only |
| clinical_documents | [internal dataset path] | encounter key | all narrative columns, including chief complaint, present illness, past history, personal history, menstrual history, marriage and childbearing history, family history, admission diagnosis, admission condition, admission diagnosis__duplicate_2, course of diagnosis and treatment, discharge diagnosis, surgery name, surgery procedure; leakage audit only |
| labs | [internal dataset path] | encounter key | test, qualitative result, quantitative result, specimen type, test time; leakage audit only; no unsafe unit harmonization |
| vitals | [internal dataset path] | encounter key | identifiers only; no usable payload/time |
| transfers | [internal dataset path] | encounter key | identifiers only; no usable payload/time |
| front_page | [internal dataset path] | encounter key | identifiers only; no usable payload/time |

Group examinations at the complete nonblank whole-accession key (patient master index,encounter number,examination number). Preserve every raw row in ordinal order and every examination, examination findings, and examination diagnosis boundary; never choose a representative row, deduplicate repeated text, or mix fields across accessions. A blank accession, component disagreement, ambiguous modality, or non-reversible time parse makes that entire accession unavailable in that source state.

MIMIC, eICU, and UKB remain directly accessible read-only but are not pooled. MIMIC includes [internal dataset path] with archive members such as mimic-iv-3.1/hosp/admissions.csv.gz and radiology-note members; eICU consists of ordinary *.csv.gz under [internal dataset path] 2.0 data/; UKB consists of ordinary files under [internal dataset path] No cross-dataset patient identity, compatible first-resection frame, or documentary-M2 endpoint is established.

## 5. Frozen books, models, queues, and inherited frontiers

Retain three complete immutable radiology books made by two qualified Chinese-reading abdominal radiologists plus an adjudicator, and three complete immutable pathology books made by two qualified Chinese-reading hepatobiliary pathologists plus an adjudicator. Use the nine fixed global radiology-by-pathology book pairs across all patients, years, cutoffs, source/operation worlds, onset states, models, thresholds, and deletions. No row-level or field-level favorable reader mixing is allowed. Unresolved pathology alternatives remain outer states with terminals OUT, IN0-A, IN1-A, IN0-U, and IN1-U.

Retain the outcome-blind, patient-balanced frozen pipelines:

- B(Z): acquisition-only structured information;
- R(Z,S,Q): the same structured block plus report surface/availability;
- G(Z,S,Q,X): structured, surface, and blinded-reader semantic content;
- Gmask: the same fitted G object with semantic blocks replaced by its training-defined unavailable block, with no refitting.

Use age and recorded sex only as already-locked model inputs and index descriptors. Z includes acquisition facts, eligible accession count/recency, modality/ambiguity, age, recorded sex, and development-grouped machine. S/Q contain report length, component count, field presence, and availability/surface features. X contains only frozen reader-book clinical-content fields. IDs, pathology, endpoint labels, reader identity, labs, untimed notes, future rows, and test-derived dictionaries are forbidden from predictors.

Freeze preprocessing, feature order, coefficients, regularization, score bytes, tie serialization, tie keys, and K_rho=floor(rho*N_ref) from 2019. Retain N_ref>=500, K_.05>=25, K_.10>=50, K_.20>=100; each primary test state requires N>=K_.10 and at least 50 documentary-positive events. Build fixed-K queues with no backfill.

For each complete state z=(omega,O,year,radiology/pathology pair,deletion), let S_m(z) be the non-EMPTY patient identities in model m's fixed-K queue, for m in {G,B,R,Gmask}. Let Y_i(z) be the documentary-M2 endpoint in the same pathology state. The all-content G queue S_max(z) uses the same fitted G object, same-world patients, reader pair, pathology state, year, K, tie rule, and deletion, with all source-clean eligible accessions exposed. It is an oracle for stored content, not truth or deployable report availability.

Retain exact inherited strict gates for G against B, R, Gmask, and capacity-matched uniform random: 100*(H_G-H_C)/K > 5 for deterministic C, with exact integer cross-products for random. Retain all inherited exact threshold set R, PASS(q), q_req, q_M2, q_dec, q_safe, lower-threshold witnesses, queue hashes, ordered-slot diagnostics, and anchored whole-patient deletion. The parent invariants must verify:
q_req <= q_M2 <= q_dec <= q_safe (with q_dec <= q_safe; q_M2 <= q_dec).

A state at conditional coverage q is eligible for frontier evaluation only when its patient-complete 24-hour coverage Q(z)>=q, using the fixed eligible-accession denominator n_A. If n_A=0, it is feasibility-inconclusive, never Q=0 or Q=1. Do not replace N or n_A with archive-derived denominators.

## 6. New patient-level loss/regret estimand

For each active, non-deleted patient i in state z and each deterministic comparator C in {B,R,Gmask}, define:

loss_C,i(z) = 1{i in S_C(z)} * 1{i not in S_G(z)} * Y_i(z).

Define the patient-level comparator loss count:

L_C(z) = sum_i loss_C,i(z),

and the worst comparator loss:

L_IP(z) = max_C L_C(z).

The primary contract is L_IP(z)=0 in every complete eligible state. The report must also emit the individual protected sets
D_C(z) = {i: i in S_C(z) and i not in S_G(z) and Y_i(z)=1},
their protected hashes, queue positions, Y_i, cell, year, source/operation world, onset state, reader/pathology pair, deletion state, and exact raw boundary witnesses. Patient identities must be SHA-256 protected in derived outputs; no private rows go to public search.

This is deliberately an identity contract, not a count-only contract:

- If one comparator-positive patient is dropped and another positive patient is added, q_safe may pass but L_C>0 fails.
- If G drops only comparator-negative patients, L_C=0 can pass even when q_dec fails; q_IP cannot rescue q_dec and the q_dec/q_safe requirements remain mandatory.
- The random baseline has no fixed patient identities. Its inherited exact expected capture K*Y/N remains a count non-harm gate, but q_IP makes no invalid identity comparison to a random draw.

Anchored deletion follows the parent exactly: remove every source record for one patient, do not refit, rerank, backfill, requota, or change K. A deleted patient is not counted as a loss in the post-deletion active set; an originally offered deleted slot remains EMPTY. All non-deleted patients and all inherited deletion effects remain in the state ledger. This makes the leave-one-patient stress test deterministic without inventing a utility or workload model.

For every exact rational q in inherited R, define:

IP_PASS(q)=1 iff:

1. inherited SAFE_PASS(q)=1 in every eligible 2020 and 2021 coupled state;
2. L_IP(z)=0 in every one of those same states and anchored deletion states; and
3. all inherited source, state, demographic, model, queue, fixed-K, and boundary-witness checks pass.

Define q_IP = min {q in R : IP_PASS(q)=1}, only if maximum-content feasibility and all inherited frontiers are defined.

The exact nesting invariant is:
q_IP >= q_safe >= q_dec >= q_M2 >= q_req.

Because q_safe already includes q_dec and q_M2's parent endpoint, q_IP is a genuine additional layer rather than a relabeling of q_M2 or q_safe. Report exact rational values and gaps q_IP-q_safe, q_safe-q_dec, q_dec-q_M2, and q_M2-q_req.

The confirmatory estimand is zero worst-comparator documentary-positive loss, not a relative risk or a clinical utility score. No arbitrary loss weight, substitution tolerance, capacity fraction, or probability model is introduced.

## 7. Analysis plan and exact baselines

Enumerate the full compatible state space: all non-favorable source/operation alternatives, five coupled onset states, both primary test years, all nine global reader-book pairs, and every permitted anchored patient deletion. Do not sample rows, accessions, patients, states, readers, pathology books, or deletions.

For each state:

1. Replay the raw-ordinal source ledger and whole-accession grouping.
2. Construct the first eligible episode, operation interval, prior-treatment window, 90-day acquisition set, 24-hour deadline, patient-complete Q, and coupled exposure vector.
3. Assign endpoint Y from each complete pathology book without using pathology in predictors.
4. Replay locked B/R/G/Gmask scores, binary64 serialization, exact ties, fixed K, and no-backfill queues.
5. Construct same-world S_max, S_G, S_B, S_R, and S_Gmask; calculate inherited H counts/gates/frontiers and D_C, L_C, L_IP.
6. Assign the four inherited cells F18_64, F65P, M18_64, and M65P from the index encounter's recorded Sex and Age: female/male and age 18-64/65+. Age exactly 65 belongs to the 65+ cell. Never infer sex or age from names, notes, diagnoses, dates, or treatment. Blank, nonnumeric, nonbinary, duplicate-discordant, or world-discordant demographic values remain resolution-inconclusive under q_safe.
7. Evaluate exact threshold monotonicity, all boundary witnesses, protected-set hashes, and the full frontier invariant.

Baselines are fixed and interpreted separately:

- B is the acquisition-only deterministic queue.
- R is the acquisition-plus-surface deterministic queue.
- Gmask is the same G model with its semantic content masked, not a refitted comparator.
- Uniform random is an exact expected-count baseline only: compare N*H_G-K*Y and inherited subgroup cross-products as integers. Never simulate random queues or claim patient-level random protection.
- S_max is the same-world maximum stored-content oracle, not an operational baseline.

The primary estimand is evaluated only at rho=.10 and d=24 hours. Report 12/48/72-hour and rho=.05/.20 results as locked non-rescuing sensitivities/diagnostics. Do not pool years, average readers, select a favorable source state, or use a favorable deletion to override a primary failure.

## 8. One-hot outcome labels and falsification

Apply exactly one primary label in this order:

1. computationally_inconclusive: any source/hash/schema replay, BOM or raw-ordinal retention, whole-accession grouping, operation interval, temporal quarantine, coupled-state generation, complete reader/pathology book, score/tie replay, fixed-K queue, deletion, demographic join, threshold search, exact arithmetic, protected-set witness, or invariant check fails.
2. feasibility_inconclusive: inherited N/K/event/n_A or structural-entry requirements fail; n_A=0 is not a zero-coverage result.
3. demographic_or_subgroup_feasibility_inconclusive: an included patient cannot be assigned to exactly one inherited age-by-recorded-sex cell in a complete state, or any required cell has Y_g=0. This is not individual-loss evidence.
4. maximum_content_signal_adverse: maximum stored content fails an inherited overall comparator, random, year, reader, source-world, or deletion gate.
5. maximum_content_group_adverse: maximum stored content passes inherited overall gates but fails an inherited q_safe cell comparator/random non-harm gate.
6. aggregate_capture_adverse: q_req is undefined or equals 1 after maximum-content gates pass.
7. documentary_M2_retention_adverse: q_req<1 but q_M2 is undefined or equals 1.
8. group_safety_adverse: q_M2/q_dec conditions pass but q_safe is undefined or equals 1, or a required inherited subgroup gate fails at the relevant maximum/conditional state.
9. individual_comparator_loss_adverse: q_safe<1 but q_IP is undefined or equals 1, or a state with q>=q_IP fails L_IP=0. The witness must identify at least one non-deleted documentary-M2 patient in D_B, D_R, or D_Gmask; an aggregate count loss alone is not sufficient for this label.
10. individual_documentary_loss_supportive_bridge_pending: all inherited frontiers pass, q_IP<1, exact lower-boundary minimality and all protected loss-set witnesses verify. This supports the finite-corpus individual comparator no-loss contract only.
11. external_clinical_bridge_pending: a separate mandatory evidence-status field attached to label 10 (and any narrower supported parent label); it records that HCC lacks the evidence needed for clinical deployment or clinical benefit.

A primary label is never upgraded or downgraded by a favorable sensitivity. Equality at q=1 is adverse for that frontier because the confirmatory claim requires a threshold below one. A zero documentary-positive event in an inherited cell is inconclusive, not safe or adverse. A failed computation is computationally inconclusive, not scientific adverse evidence. A valid adverse patient witness is not reclassified as inconclusive.

Supportive means that under every required frozen HCC source/operation/onset/reader/pathology/year/deletion state, the fixed G queue has no documentary-M2 patient-level loss relative to B, R, or Gmask once all inherited layers pass. Adverse means the corresponding stronger contract is falsified in at least one allowed state; it does not erase narrower q_req, q_M2, or q_safe results. Inconclusive means the data or computation cannot evaluate the contract.

The external bridge status must remain nonclinical. A supportive computation does not establish actual preoperative report availability, authored/final/release/retrieval/read/view timing, image truth, biological MVI, pathology sampling adequacy, clinician action, treatment selection, benefit, recurrence, survival, harm, cost, fairness, calibration, transportability, or patient utility. It cannot justify a treatment or surveillance recommendation.

## 9. Required derived outputs and verifier contract

Write only workspace-derived files; all listed source files remain read-only. Required new artifacts are:

- derived/q_ip_frontier.parquet: exact rational q_req, q_M2, q_dec, q_safe, q_IP, gaps, role and state counts;
- derived/patient_comparator_loss.parquet: one row per state/comparator/loss patient with protected patient hash, queue position, Y, cell, and witness references;
- derived/q_ip_gate_tensor.parquet: exact L_C, L_IP, inherited gates, q, and pass bits for every state/deletion;
- derived/q_ip_boundary_witnesses.parquet: immediately lower q and q_IP witnesses, hashes, comparator, queue positions, and raw source/accession ordinal references;
- derived/q_ip_interpretation.json: one-hot label, external bridge status, computed values, and bounded prose;
- derived/source_manifest_and_raw_ordinal_ledger.parquet, derived/whole_accession_interval_clock_ledger.parquet, derived/coupled_state_registry.parquet, derived/locked_model_score_and_tie_manifest.parquet, derived/anchored_deletion_results.parquet, and the inherited qreq/qM2/qdec, demographic, subgroup, and q_safe artifacts.

The verifier must independently check:

- all HCC source and catalog hashes, exact schemas, BOM handling, raw ordinals, and no source writes;
- all stated encounter/procedure/examination/pathology joins and complete whole-accession preservation;
- exact first-episode, temporal-window, operation-interval, prior-treatment, and coupled-onset construction;
- complete reader books, nine fixed pairings, pathology alternatives, frozen predictors, score bytes, ties, fixed K, and no-backfill deletion;
- inherited PASS, q_req, q_M2, q_dec, SAFE_PASS, q_safe, and all boundary minimality witnesses;
- exact patient identities in S_G, S_B, S_R, S_Gmask, endpoint Y, D_C, L_C, and L_IP;
- no random identity inference, no subgroup pooling, no cross-world comparator stitching, exact q-chain q_IP>=q_safe>=q_dec>=q_M2>=q_req, and label/prose consistency.

Mandatory synthetic fixtures include:

- equal overall G and B capture with one B-positive patient lost and a different positive patient gained: q_safe can pass but q_IP must fail;
- q_M2/q_dec pass while B offers a documentary-positive patient absent from G: q_IP must fail;
- a loss to R only and a loss to Gmask only;
- all comparator-positive identities retained while comparator-negative substitutions occur: q_IP passes but q_dec may fail;
- exact random cross-product equality, which must not create an identity claim;
- one female/older cell loss hidden by aggregate gain; zero-event cell; age exactly 65; duplicate-discordant demographics;
- O=2/O=3 transition, blank/multirow accession, duplicate text rows, missing/date-only/competing clocks, score ties, N=K, n_A=0, and deleted selected patient;
- lower q failure followed by q_IP equality, with exact immediate-lower boundary witness;
- correct q_IP<1 paired with claims of biological MVI, actual report timing, clinical benefit, fairness, safe substitution, or deployment readiness: verifier rejects;
- computational failure described as adverse, valid adverse described as inconclusive, and appropriately bounded supportive/adverse/inconclusive outputs.

Reference execution establishes computational feasibility and correct linkage of prose to outputs, not scientific truth. The verifier can establish source replay, state construction, endpoint-book counts, queue identity, gate arithmetic, q frontiers, and interpretation linkage. Clinical adjudication is still required for the eligible-operation dictionary, radiology/pathology books, and appropriateness of recorded demographic cells. Missing report-version/timing, specimen linkage, actual clinician action, utility, outcomes, fairness, and transportability require external evidence, expert review, prospective silent-mode/workflow study, linked outcomes, or another decision-appropriate study.

## 10. Exact evidence still required for a clinical decision

Before any clinical deployment claim, obtain for every HCC accession a one-to-one (Patient Master Index, Visit Number, Examination Number) crosswalk and immutable report-version/amendment/retraction lineage; authored, final, release, ingestion, retrieval, parse-readability, and clinician-view events with timezone/clock provenance; exact as-of-deadline payload hashes; all nonresponders; and patient-level simultaneous bounds on no-accession/incomplete/complete states. HCC has none of these report-event fields. Therefore M=1 remains hypothetical stored-content exposure and cannot be called a real 24-hour availability guarantee.

A biological MVI claim additionally needs specimen/accession/time linkage, sampling adequacy, blocks/slides or validated structured pathology, and blinded clinical adjudication. An individual clinical-safety or benefit claim needs clinician action, patient utilities, harms, treatment/surveillance outcomes, competing workload, and prospective or interventional evidence. No such conclusion is permitted from q_IP.

The substantive advance is narrow and falsifiable: it upgrades aggregate/subgroup non-loss and oracle-positive retention into a predeclared individual documentary-positive no-loss contract against each deterministic baseline. Negative findings remain valuable because a single protected-patient witness identifies where a seemingly robust queue would withdraw a documented high-risk review opportunity.
