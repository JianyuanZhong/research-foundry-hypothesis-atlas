> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Documentary-M2 patient-priority preservation under incomplete preoperative report bundles

## 1. Targeted repair and clinical question

This is a targeted child of assessed-valid \`[prior hypothesis]\` (documentary-M2 patient retention, \`q_M2\`) and \`[prior hypothesis]\` (recorded age-by-sex subgroup non-loss, \`q_safe\`). It preserves their HCC population, 24-hour decision boundary, coupled uncertainty, reader/pathology books, fixed pipelines and K, strict aggregate gates, oracle-positive retention, subgroup contract, exact queue identity, anchored deletion, and nonclinical limits.

The single remaining defect is within the individual-patient decision claim. \`q_M2\` requires that every documentary-M2 patient in the maximum-stored-content queue remains selected, but is silent about that patient's ordered queue position. \`q_safe\` protects subgroup capture and inherits \`DEC_PASS\`, but \`DEC_PASS\` compares selected patient sets, not their order. Thus an incomplete-report queue can retain every oracle-positive patient and the exact same selected set while demoting one documentary-M2 patient below another patient; the existing aggregate, \`q_M2\`, and \`q_safe\` gates can all pass. The inherited logs mention ordered-slot disagreement, but do not make patient-specific demotion a falsifiable safety endpoint.

The repair adds a predeclared patient-level ordinal-regret contract: every maximum-content-queued documentary-M2 patient must have an incomplete-report G rank no worse than its same-world maximum-content rank. This is a policy-priority contract, not a claim about waiting time, staffing, report release, clinician attention, treatment, or outcome. It adds no workload or capacity assumption and no unavailable report-timing evidence. It is clinically consequential only to the extent that a deployment consumes the fixed queue in order; that operational meaning requires expert review and is withheld here.

The unresolved question is therefore: at the 24-hour preoperative boundary, can incomplete exposure of stored CT/MRI report bundles preserve not only aggregate documentary-M2 capture, oracle-positive patient membership, and recorded age/sex non-loss, but also the priority position of every retained oracle-positive patient, across every compatible source, onset, reader, pathology, calendar-year, and anchored-deletion state?

## 2. Evidence-supported and untested claims

The strongest available dataset claim is source feasibility. The HCC snapshot \`[source checksum]\` provides encounter-linked age/recorded sex and timestamps, source-labelled procedures with start/end fields, CT/MRI-like examination accessions with acquisition-like \`Start time\` and stored narrative fields, same-encounter pathology narrative, and dated medication/order rows. The catalog, HCC README, table metadata, BOM-preserving header checks, and inherited full scans document the columns and joins. This supports construction of the proposed retrospective documentary experiment, not correct procedure semantics, report availability, biological MVI, actual queue use, or clinical benefit.

The inspected Li et al. full-text XML (DOI \`10.1186/s12957-026-04229-2\`, frozen source \`[source checksum]\`, SHA-256 \`[source checksum]\`) reports prognostic associations for graded microvascular invasion after resection; it does not establish that a report-based queue improves care. The inspected systematic-review XML (DOI \`10.3390/cancers18132028\`, frozen source \`[source checksum]\`, SHA-256 \`[source checksum]\`) describes predominantly retrospective, heterogeneous early-recurrence AI studies and limited independent validation. Those sources motivate rigorous patient-level evaluation but do not answer this report-bundle priority question. The three expert-selected demonstration files were inspected as specified in the research-ambition README; the cancer main article and full STAR Methods remain unavailable, so no claim is based on reading them.

The tested claim is strictly computational: under the frozen HCC corpus and complete coupled uncertainty envelope, a threshold below one exists at which the inherited aggregate gates, \`q_M2\`, \`q_safe\`, and zero patient-level demotion all hold. Support would establish a finite-corpus documentary priority-preservation reserve for a frozen score under hypothetical stored-content masks. It would not establish biological MVI, recurrence risk, fairness, report release/view timing, treatment benefit, safety, utility, or deployment readiness.

## 3. Population and temporal boundaries

For each coupled source/operation world \`omega\`:

- Include adults with age >=18 in \`encounters.Age\` at their earliest source-documented eligible hepatobiliary resection, using a preregistered procedure dictionary reviewed by a hepatobiliary surgeon.
- Require a same-\`(patient master index, encounter number)\` pathology narrative sufficient to assign the encounter to the documentary target frame under at least one complete pathology book.
- Exclude an earlier qualifying resection and any recorded transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in \`[t_op-365 days,t_op)\`, using procedures, medications, and non-medication orders. Ambiguous membership remains a separate outer source state.
- Treat a clinically supported anaesthesia-system procedure timestamp as a point. Treat date-like midnight values as \`[date,date+24h)\`. Missing, contradictory, non-reversible, or clinically ambiguous operation times remain unavailable/alternative states. Never substitute admission or discharge time.
- Set \`t_dec=t_op-24h\`. Candidate CT/MRI acquisition intervals must lie wholly in \`[t_op-90d,t_dec)\`. The inherited 12-, 48-, and 72-hour analyses remain non-rescuing sensitivities.
- Use patient-disjoint roles: 2015–2018 development, 2019 preprocessing/hyperparameter/K lock, separate 2020 and 2021 tests, and 2022 onward audit only. A patient possibly belonging to a later role is quarantined from earlier roles.

The analysis unit is one patient at the first eligible episode. The policy unit is one fixed ordered queue position. The endpoint is encounter-documentary M2, not specimen-linked or biological MVI.

## 4. Exact source bindings and availability

All 12 HCC inputs are ordinary read-only CSVs; HCC has no archive members. The exact HCC source paths, catalog source IDs, snapshot hashes, and schema hashes must be copied into the run manifest and independently replayed:

| Table | Exact source path | Join key | Required columns and role |
|---|---|---|---|
| \`encounters\` | \`[internal dataset path]` | \`(patient master index, encounter number)\` | \`age, sex, encounter time, admission time, discharge time\`; age/recorded-sex cells and audit clocks |
| \`procedures\` | \`[internal dataset path]` | encounter key | \`Surgery,Start Time,End Time,Surgery Source\`; operation identity and interval clock |
| \`examinations\` | \`[internal dataset path]` | \`(patient master index,encounter number,examination number)\` | \`examination,examination findings,examination diagnosis,start time,machine model,examination number\`; whole-accession modality/time/report |
| \`pathology\` | \`[internal dataset path]` | encounter key only | \`Pathology,Examination Findings,Examination Diagnosis,Machine Model\`; complete documentary endpoint book |
| \`medications\` | \`[internal dataset path]` | patient-wide temporal join, then episode restriction | \`Medication, Medication type, Start time, End time\`; prior-treatment exclusion |
| \`orders\` | \`[internal dataset path]` | patient-wide temporal join | \`Orders (non-drug), order time, start time, end time, order status\`; prior-treatment exclusion |
| \`diagnoses\` | \`[internal dataset path]` | encounter key | \`Diagnosis Name,Diagnosis Type\`; untimed corroboration only |
| \`clinical_documents\` | \`[internal dataset path]` | encounter key | \`Chief complaint,History of present illness,Past medical history,Admission diagnosis,Clinical course,Discharge diagnosis,Procedure name,Procedure details\`; leakage/audit only |
| \`labs\` | \`[internal dataset path]` | encounter key | \`Test,Qualitative Result,Quantitative Result,Specimen Type,Test Time\`; leakage audit only |
| \`vitals\` | \`[internal dataset path]` | encounter key | identifiers only; no usable payload/time |
| \`transfers\` | \`[internal dataset path]` | encounter key | identifiers only; no usable payload/time |
| \`front_page\` | \`[internal dataset path]` | encounter key | identifiers only; no usable payload/time |

The HCC catalog metadata gives table-specific schema hashes: encounters \`8ff49f3a...\`, procedures \`e86f7a74...\`, examinations \`6963fe9f...\`, pathology \`a8e2aa9e...\`, medications \`39d1de89...\`, and orders \`e902f54d...\`; the verifier must use the complete JSON values and raw source hashes from \`datasets/hcc/README.md\` and \`datasets/hcc/metadata.json\`, not these abbreviated labels.

Examinations are grouped at the complete nonblank whole-accession grain \`(patient master index, encounter number, examination number)\). Preserve every raw row in original ordinal order and all \`Examination\`, \`Examination Findings\`, and \`Examination Diagnosis\` boundaries; never select a representative row or deduplicate repeated text. Blank accession, component disagreement, ambiguous modality, or non-reversible parsing makes the whole accession unavailable in that state. The inherited audit found 72 blank accession IDs, 392,854 distinct nonblank whole-accession keys, 16,534 multirow keys, and at most 12 rows/key; these values must be replayed, not assumed.

MIMIC, eICU, and UKB remain accessible read-only through their catalogued paths and archive members, but are not pooled: no compatible first-resection frame, patient crosswalk, or documentary-M2 endpoint is established. MIMIC includes the archive \`[internal dataset path]`, eICU uses the ordinary gzipped files under \`[internal dataset path]`, and UKB uses ordinary files under \`[internal dataset path]`. No non-HCC rows enter this experiment.

## 5. Frozen books, models, and inherited safeguards

Two qualified Chinese-reading abdominal radiologists plus an adjudicator create three complete immutable radiology books. Two qualified Chinese-reading hepatobiliary pathologists plus an adjudicator create three complete immutable pathology books. The nine radiology-by-pathology book pairs are fixed across patients, years, cutoffs, source/onset worlds, models, thresholds, and deletions. Pathology terminals remain \`OUT\`, \`IN0-A\`, \`IN1-A\`, \`IN0-U\`, and \`IN1-U\`; each same-encounter pathology row is indivisible. No pathology value enters a predictor.

Reuse the parent's patient-balanced, additive, outcome-blind pipelines without refitting:

- \`B(Z)\): acquisition-only structured information.
- \`R(Z,S,Q)\): structured information plus report surface/availability.
- \`G(Z,S,Q,X)\): structured, surface, and blinded-reader semantic content.
- \`Gmask\): the fitted G object with semantic blocks replaced by the training-defined unavailable block, without refitting.
- Capacity-matched random K: exact expected documentary-M2 capture \`K*Y/N\`, represented by integer cross-products.

Z may contain age, recorded sex, eligible acquisition count/recency, modality/ambiguity, and development-grouped machine. S/Q may contain only report length, component count, field presence, and availability/surface. X may contain only frozen radiologist-book clinical-content fields. IDs, test labels, reader identity, pathology, labs, untimed notes, future rows, and test-derived dictionaries are forbidden. Freeze preprocessing, feature order, coefficients, regularization, score bytes, tie keys, and \`K_rho=floor(rho*N_ref)\` from 2019. Retain \`N_ref>=500\`, \`K_.05>=25\`, \`K_.10>=50\`, \`K_.20>=100\`; each test state requires \`N>=K_.10\) and at least 50 documentary-positive events.

For each state, retain inherited strict gates in both 2020 and 2021 and every allowed deletion: \`100*(H_G-H_C)/K>5\` for \`C in {B,R,Gmask}\`, and the exact random-K cross-product equivalent to \`100*H_G/K-100*Y/N>5\`. Preserve exact rational threshold enumeration, \`q_req\), immediate-lower-threshold witnesses, queue hashes, set differences, ordered-slot disagreement logs, and anchored whole-patient deletion: deleting a patient removes all their records, with no refit, reranking, backfill, or requota.

## 6. Coupled exposure states and inherited frontiers

For patient i, source world \`omega\), cutoff d, and whole accession u, define \`E_iomega,d,u=1\` only when operation membership/time, accession identity, CT/MRI modality, and acquisition-like \`start time\` are valid and the acquisition interval lies wholly in \`[t_op-90d,t_dec)\`.

Each source-clean eligible accession receives one coupled monotone onset state: O=0 eligible by 72h; O=1 first eligible in (72,48]h; O=2 in (48,24]h; O=3 in (24,12]h; O=4 later/never. In 72/48/24/12 order, \`V(O)=(1[O=0],1[O<=1],1[O<=2],1[O<=3])\` and \`M=E*V\). M is a hypothetical exposure of eventual stored content, never an authored/finalized/released/retrieved/viewed event.

Retain target N, n_A, structural entry fraction e, and zero-acquisition/incomplete/complete-bundle dispositions in every state. If n_A=0, the result is feasibility-inconclusive. Define Q using the fixed n_A denominator. Archive evidence cannot redefine N, n_A, or the eligible accession set.

For state z, let S_G(z) be the non-EMPTY fixed-K queue from incomplete content and S_max(z) the same fitted G queue with every source-clean eligible accession exposed, in the identical source, reader, pathology, year, and deletion state. S_max is an eventual-stored-content oracle, not truth or deployable information. Let \`Y_i(z)\` be the binary documentary-M2 endpoint and \`P_max(z)={i:i in S_max(z),Y_i(z)=1}\`.

Inherited frontiers are preserved exactly:

- \`q_req\`: smallest exact threshold where all overall gates pass in every state with Q>=q.
- \`q_M2\`: smallest threshold where inherited gates pass and \`P_max(z) subseteq S_G(z)\` in every state with Q>=q.
- \`q_dec\`: smallest threshold additionally requiring \`S_G(z)=S_max(z)\`.
- \`q_safe\`: smallest threshold satisfying \`DEC_PASS(q)\) plus all four fixed age-by-recorded-sex cells (18–64/65+ by recorded \`Sex\`) having resolved positive events and all inherited non-harm comparator/random inequalities, in every state with Q>=q.

Retain exact invariants \`q_req <= q_M2 <= q_dec\` and \`q_safe >= q_dec\`; do not alter K, denominators, cells, or state coupling. Recorded \`sex\` is an administrative field, not gender identity.

## 7. New patient-level ordinal-regret contract

The new endpoint is evaluated only after a state satisfies the inherited feasibility conditions, overall PASS, q_M2 patient membership, and q_safe subgroup contract at threshold q. This makes it a refinement of the selected decision claim rather than a replacement for any mature safeguard.

Serialize each queue's occupied positions exactly as the inherited fixed-K score/tie ordering, with rank 1 the highest-priority non-EMPTY position. For every \`i in P_max(z)\`, define:

\`r_max,i(z)=position of i in S_max(z)\`,
\`r_G,i(z)=position of i in S_G(z)\`,
\`D_i(z)=max(0,r_G,i(z)-r_max,i(z))\`.

Under q_M2, both ranks exist. A positive D is patient-specific demotion; D=0 preserves or improves the oracle priority. The primary safety contract is:

\`NO_DEMOTION(z)=1 iff D_i(z)=0 for every i in P_max(z)\`.

For every exact rational threshold q in the inherited threshold set R, define:

\`PRIO_PASS(q)=1\` iff:

1. inherited aggregate \`PASS(q)\` holds in every eligible 2020/2021 state with Q>=q;
2. \`J_M2(z)=1\) for every such state;
3. \`SAFE_PASS(q)\) holds in every such state; and
4. \`NO_DEMOTION(z)=1\) in every such state.

If maximum-content feasibility holds, define:

\`q_prio=min{q in R: PRIO_PASS(q)=1}\`.

The confirmatory hypothesis is that at rho=0.10 and d=24h, maximum stored content passes all inherited gates and there is a threshold q_prio<1. Report \`q_req,q_M2,q_dec,q_safe,q_prio\`, gaps \`q_M2-q_req\`, \`q_dec-q_M2\`, \`q_safe-q_dec\`, and \`q_prio-q_safe\`, and verify \`q_prio>=q_safe>=q_dec>=q_M2>=q_req\` whenever all frontiers are defined. The immediate lower q witness must include every demoted patient hash, its \`r_max\`, \`r_G\`, \`D_i\`, slot occupant in both queues, endpoint Y, subgroup cell, source/onset/reader/pathology/year/deletion state, Q, and responsible missing whole-accession bundles. Also emit descriptive per-patient maximum D, median/mean D, promoted-patient counts, and all queue order disagreements; descriptive summaries never rescue a failed zero-demotion contract.

This is not redundant with q_M2: q_M2 tests membership only. It is not redundant with q_safe: q_safe tests subgroup capture/non-harm and inherits selected-set identity, but permits an order swap within the same set. It is not redundant with q_dec: q_dec tests set equality, while \`q_prio\` tests the directional patient-level priority consequence of an ordered queue. Zero demotion is deliberately exact rather than a chosen percentage or rank tolerance, so it introduces no workload, capacity, utility, or service-time assumption. If ordered position has no prespecified operational meaning in a future deployment, the computational result remains reportable but its clinical interpretation requires expert review.

## 8. One-hot outcomes and falsification

Use this precedence-ordered primary label:

1. \`computationally_inconclusive\`: any source/hash/schema/BOM replay, lossless raw-ordinal audit, accession grouping, operation clock, temporal quarantine, reader/pathology completeness, fixed score/tie replay, deletion, state coupling, threshold enumeration, rank calculation, boundary witness, or invariant check fails.
2. \`feasibility_inconclusive\`: any N/K/event/n_A/structural denominator requirement fails.
3. \`demographic_or_subgroup_feasibility_inconclusive\`: a state cannot assign every included patient to exactly one predeclared cell, or any cell has no resolved positive event.
4. \`maximum_content_signal_adverse\`: maximum stored content fails an inherited comparator, random, year, reader, source-world, or deletion gate.
5. \`aggregate_capture_reserve_adverse\`: q_req is undefined or equals 1.
6. \`patient_retention_adverse\`: q_req<1 but q_M2 is undefined or equals 1; at least one allowed nontrivial-coverage state loses an oracle-positive documentary-M2 patient.
7. \`subgroup_nonloss_adverse\`: q_M2<1 but q_safe is undefined or equals 1; a fixed cell loses documentary-M2 capture under a comparator/random gate or the demographic contract is otherwise not met.
8. \`patient_priority_adverse\`: q_safe<1 is false but q_prio is undefined or equals 1; all earlier membership/set/subgroup conditions can pass while at least one oracle-positive patient is demoted in an admissible state. This is the falsification target of the new repair.
9. \`documentary_M2_priority_supportive\`: q_prio<1, maximum content passes, the immediate lower threshold fails when one exists, all exact witnesses and invariants verify, and all structural certificates are complete.
10. \`external_clinical_bridge_pending\`: mandatory evidence-status field accompanying label 9, never upgrading it. It records that report-version/access, workflow, biological, treatment, harm, utility, and deployment evidence is absent.

An adverse result at the new layer does not erase narrower aggregate, q_M2, or q_safe findings. An inconclusive result is not adverse evidence. Favorable 12/48/72-hour sensitivities cannot rescue the 24-hour primary label, and adverse sensitivities cannot veto it. Supportive means only finite-corpus documentary priority preservation under hypothetical masks and coupled uncertainty. It does not support fairness, biological MVI validity, clinical benefit, safety, or deployment.

## 9. Executable Harbor experiment and verification

The compiler must replay all inherited source manifests and generate only workspace-derived files. Add:

- \`derived/patient_priority_ledger.parquet\` with state ID, patient hash, Y, q, \`r_max\`, \`r_G\`, D, cell, source/onset/reader/pathology/year/deletion;
- \`derived/q_prio_frontier.parquet\`;
- \`derived/q_prio_witnesses.parquet\`;
- \`derived/interpretation.json\` with one-hot label and external bridge status;
- \`derived/priority_order_log.parquet\`, plus inherited source/header/hash, raw ordinal, join, accession, operation-clock, temporal-role, score/tie, deletion, state-coupling, queue-oracle, threshold, subgroup, and conclusion logs.

The verifier independently checks all 12 HCC source hashes, schemas, BOM handling and lossless raw-to-ledger replay; exact encounter joins; age-65 behavior; no demographic inference; whole-accession grouping; operation intervals; all inherited score/tie, fixed-K, deletion, state, pathology, comparator, random, q_req, q_M2, q_dec and q_safe computations; and exact integer/rational frontier arithmetic. It then recomputes each protected patient hash, both ranks, D, \`NO_DEMOTION\`, \`q_prio\`, all gaps and the frontier invariant. It must reject:

- a correct q_M2/q_safe result described as patient-priority safety when a retained oracle-positive patient is demoted;
- q_prio<1 described as fairness, biological MVI validation, treatment benefit, clinical safety, or deployment readiness;
- omission of a state, subgroup, deletion, lower-threshold witness, or coordinatewise world stitching;
- rank calculated from score values without frozen tie serialization;
- any rank interpreted as time-to-review;
- altered K, backfill, refitting, denominator substitution, demographic imputation, report-row sampling, report-version substitution, or use of inaccessible report timing.

Synthetic fixtures must include: identical selected sets with an order swap that demotes a documentary-M2 patient; a demoted M2 patient with q_M2 and q_safe otherwise passing; a promoted M2 patient with no demotion; an omitted M2 patient that is caught by q_M2 before rank evaluation; exact ties with frozen tie keys; anchored deletion of a selected patient; age exactly 65; duplicate-discordant demographics; zero-event cells; multirow and blank accessions; O=2/O=3 transitions; lower-threshold demotion followed by zero demotion at q_prio; and adverse/inconclusive/supportive conclusion-adversarial prose.

Computationally checkable claims are source replay, cohort/state construction, endpoint assignment within complete books, queue membership/order, patient ranks, all gates/frontiers, and whether conclusion text follows from output. Procedure dictionary review, radiology/pathology book validity, and the clinical meaning of ordered queue positions require expert adjudication. Actual report authored/final/released/ingested/retrievable/readable/retracted times require an external archive bridge with immutable report-version identity and simultaneous uncertainty; HCC has no such timing fields. Biological MVI requires specimen/block/slide linkage and blinded pathology review. Actual clinician action, treatment change, harms, recurrence, survival, utility, fairness, transportability, staffing, and deployment require another study.

## 10. Substantive advance and limits

Compared with the two assessed-valid parents, this child adds exactly one decision-relevant layer: a directional, per-patient ordinal-regret contract for every oracle-positive documentary-M2 patient. It does not add a model, feature, threshold, outcome, dataset, report-timing variable, workload assumption, capacity model, clinical action, or subgroup category. It retains all mature safeguards and makes the previously descriptive ordered-slot disagreement a falsifiable patient-level endpoint.

The advance is clinically meaningful only as protection against priority demotion in an ordered review policy. Because no configured source contains reliable report-release/view timestamps, staffing, actual review completion, treatment, outcome, or patient utility, the experiment cannot claim that demotion delayed care or harmed a patient. A supportive computation is a finite-corpus priority-preservation certificate under hypothetical stored-content exposure; an adverse computation identifies an exact patient-level policy instability; an inconclusive computation identifies failure to establish the certificate. No result authorizes treatment or surveillance recommendations.
