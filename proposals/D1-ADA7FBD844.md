> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Structural-weight uncertainty grid for HCC documentary-M2 allocation

Parent anchors: `[prior hypothesis]` (accession/raw-row/text burden envelope) and `[prior hypothesis]` (semantic feature attribution and no-refit shadow).

## 1. Exactly one residual defect

The residual defect is point-ledger fragility. The structural parent tests three computable costs: one per accession \(U\), one per raw examination row \(R\), and raw rows plus 512-byte narrative chunks \(T\). Those corners do not establish actual review burden, and they do not test intermediate relative weights of extra components and narrative volume. Because the patient queue uses a longest-prefix capacity rule, its membership is discontinuous: all three named ledgers can pass while an intermediate source-computable weighting fails. Calling a three-corner pass “workflow-burden robustness” is therefore stronger than the computation supports.

This child repairs only that defect. It retains the exact same raw examination units and adds a finite, prelocked structural-weight uncertainty grid containing \(U,R,T\) as exact corners. It does not attempt to infer report lifecycle, minutes, or clinical action from HCC. Those remain external evidence requirements.

The complete read-only examination source contains 419,996 rows and 392,854 nonblank \((patient primary index,encounter number,examination number)\) accessions. A direct all-row audit found 16,534 multirow accessions; raw rows per accession had median 1, 90th percentile 1, 99th percentile 3, and maximum 12. The UTF-8 narrative term defined below had median 2, 90th percentile 22, 99th percentile 50, and maximum 154 512-byte chunks. These are whole-source structural counts, not cohort prevalence, reports, image series, or reader time.

## 2. Repair and falsifiable hypothesis

For each eligible nonblank whole accession \(u=(patient master index,visit number,examination number)\), preserve every raw examination row, including byte-identical duplicates and conflicting components. Define:

\[
n_u=\text{number of raw examination rows in }u,
\]

\[
b_u=\sum_{j\in u}\sum_{x\in\{\text{Examination},\text{Examination Findings},\text{Examination Diagnosis}\}}
\operatorname{len}(\operatorname{UTF8}(x_j)),
\]

and

\[
x_u=\begin{cases}
\lceil b_u/512\rceil,& b_u>0,\\
0,& b_u=0.
\end{cases}
\]

For \(a,b\in\{0,1,2,3,4\}\), define 25 prelocked rational ledgers:

\[
w^{a,b}_u=1+\frac{a}{4}(n_u-1)+\frac{b}{4}x_u.
\]

The grid contains the inherited ledgers exactly:

- \(w^{0,0}=w^U=1\);
- \(w^{4,0}=w^R=n_u\);
- \(w^{4,4}=w^T=n_u+x_u\).

The other 22 ledgers interpolate predeclared quarter-weight surcharges for extra rows and text chunks. They are not claims that actual burden lies on this grid. They answer a narrower, computable question: does the allocation result depend on the three chosen corner weights?

The falsifiable hypothesis is:

> At the inherited frozen threshold \(q^*\), the report-semantic queue \(G\)'s documentary-M2 advantage over acquisition-only \(B\), report-surface \(R\), and masked-semantic \(G_{\rm mask}\) remains strictly greater than 5 percentage points under every one of the 25 structural-weight ledgers, in every required coupled source/onset/reader/pathology state in the 2020 lock-set replay and untouched 2021 temporal confirmation.

The 25-ledger grid, byte encoding, field list, divisor, duplicate rule, coefficient grid, capacity arithmetic, and output order are frozen in 2019. The new grid is evaluated only after the parent’s \(q^*\) is frozen; it cannot select or alter \(q^*\). The substantive advance is a direct test of whether the documentary-M2 allocation property survives uncertainty in the relative structural weights already implicit in the parent, without relabeling source size as clinical work.

## 3. Supported evidence, unresolved claim, and strict limits

Available evidence supports these claims before Harbor execution:

- HCC snapshot is `[source checksum]`.
- The examination source is an ordinary read-only CSV with the exact header `Patient Master Index`, `Encounter Number`, `Examination`, `Examination Findings`, `Examination Diagnosis`, `Start Time`, `Machine Model`, `Examination Number`.
- The source supports exact whole-accession keys, raw row multiplicity, field-bounded UTF-8 byte lengths, source ordinals, acquisition-like dates, and deterministic replay of all 25 structural costs.
- The source has heterogeneous row and text structure as quantified above.
- Examinations have only `start time` as a temporal field. There is no finalization, release, ingestion, retrieval, view, author, report-status, or review-duration field.
- Pathology has narrative payload but no time, specimen, block, slide, or examination-accession key.
- No HCC image files are available.

The strongest pre-execution claim is that a fixed 25-ledger source-structure sensitivity analysis is computable. The unresolved claim tested is whether the frozen semantic queue’s finite-census documentary-M2 advantage survives every predeclared intermediate weighting, all inherited uncertainty worlds, and untouched temporal replay.

The experiment can establish source lineage, exact cost/capacity and queue arithmetic, semantic feature provenance, patient-disjoint chronology, finite-corpus robustness, and whether conclusions follow from witnesses. It cannot establish report lifecycle, actual reader minutes, image-series or prior-comparison burden, clinical semantic correctness, pathology specimen linkage, biological microvascular invasion, clinician action, recurrence, survival, safety, fairness, transportability, causality, cost-effectiveness, benefit, or deployment readiness.

For the external bridge, I inspected Brady, “Measuring Consultant Radiologist workload: method and results from a national survey,” *Insights into Imaging* 2011, DOI `10.1007/s13244-011-0094-3`, PMCID `PMC3259371`. The acquired Europe PMC full-text XML has source ID `[source checksum]` and [source checksum]. Its methods/abstract describe relative-value weighting for countable studies and separate measurement of non-countable activities. It does not validate an HCC coefficient, cost, endpoint, or threshold. The three demonstrations listed in `references/research-ambition/README.md` are not used as evidence for this HCC claim; specifically, the cancer demonstration’s main article and full STAR Methods remain unavailable and are not claimed as inspected.

## 4. Population, temporal boundaries, and quarantine

Use the first eligible source-documented hepatobiliary resection episode per patient. Include age \(\ge18\) and a procedure matching a hepatobiliary-resection dictionary frozen after independent hepatobiliary-surgeon review. Exclude an earlier qualifying resection and recorded transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in \([t_{\rm op}-365\text{ days},t_{\rm op})\). The episode join is \((patient master index,encounter number)\); patient-wide medication and order scans retain their original encounter keys.

Take \(t_{\rm op}\) from the selected procedure/anesthesia `start time` and define \(t_{\rm dec}=t_{\rm op}-24\) hours. Date-like values are intervals \([date,date+24\text{ h})\), never invented clock times. An examination accession is eligible only when every raw component’s `start time` interval is wholly inside \([t_{\rm op}-90\text{ days},t_{\rm dec})\). The inherited 12-, 48-, and 72-hour onset states are monotone descriptive sensitivities; 24 hours is confirmatory.

Patient-disjoint roles remain:

- 2015–2018: development;
- 2019: cohort and treatment dictionaries, parsing, feature order, models/books, protected ties, random seeds, \(K\), all 25 ledgers and capacities, and the rational threshold grid;
- 2020: inherited threshold selection only, followed by a frozen-\(q^*\) grid replay;
- 2021: one untouched temporal confirmation;
- 2022 onward: audit only.

No 2020/2021 endpoint, ledger result, queue, failure pattern, or clinical interpretation may change a 2019 artifact or \(q^*\). Cross-role patient or clock identity is quarantined.

## 5. Exact HCC source bindings

The full catalog is `[internal dataset path]`, [source checksum]. All HCC sources are ordinary read-only CSVs; no archive member is used.

| table | exact source path | keys | required columns and role |
|---|---|---|---|
| `encounters` | `[internal dataset path]` | \((patient master index,encounter number)\) | `age`, `sex`; `encounter time`, `admission time`, `discharge time` for episode/year clocks; `name`, `national ID number`, `mobile phone number`, `medical insurance/encounter card number` for inherited identity audit only |
| `procedures` | `[internal dataset path]` | \((Patient Master Index,Encounter Number)\) | `Surgery`, `Surgery Source`, `Start Time`, `End Time` for first eligible resection and \(t_{\rm op}\) |
| `examinations` | `[internal dataset path]` | episode on first two; accession on \((Patient Master Index,Visit Number,Examination Number)\) | `Examination`, `Examination Findings`, `Examination Diagnosis`, `Start Time`, `Machine Model`, `Examination Number`; all eight fields, raw boundaries and ordinals for eligibility, onset, feature provenance, \(n_u,b_u,x_u,w^{a,b}_u\) |
| `pathology` | `[internal dataset path]` | \((patient master index, visit number)\) | `pathology`, `examination findings`, `examination diagnosis`, `machine model` for fixed documentary-M2 books only; no time/specimen/accession linkage assumed |
| `medications` | `[internal dataset path]` | patient-wide `Patient Master Index`, retain `Encounter Number` | `Medication`, `Drug Type`, `Start Time`, `End Time` for prior-treatment exclusion |
| `orders` | `[internal dataset path]` | patient-wide `Patient Master Index`, retain `Encounter Number` | `Non-drug Orders`, `Order Status`, `Order Time`, `Start Time`, `End Time` for prior-treatment exclusion/audit |
| `diagnoses` | `[internal dataset path]` | \((Patient Master Index, Encounter Number)\) | `Diagnosis Name`, `Diagnosis Type`; untimed corroboration/audit only |
| `clinical_documents` | `[internal dataset path]` | \((Patient Master Index,Encounter Number)\) | all narrative fields, including `Admission Diagnosis__duplicate_2`; leakage audit only because no usable document time exists |
| `labs` | `[internal dataset path]` | \((patient master index, encounter number)\) | `laboratory test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`; leakage audit only, no unsafe unit pooling |
| `vitals` | `[internal dataset path]` | \((Patient Master Index,Encounter Number)\) | identifier-only; no predictor, semantic source, time, or cost |
| `transfers` | `[internal dataset path]` | \((patient master index, encounter number)\) | identifier-only; no predictor, semantic source, time, or cost |
| `front_page` | `[internal dataset path]` | \((Patient Master Index,Encounter Number)\) | identifier-only; no predictor, semantic source, time, or cost |

Required schema hashes are encounters `[source checksum]`, procedures `[source checksum]`, examinations `[source checksum]`, pathology `[source checksum]`, medications `[source checksum]`, orders `[source checksum]`, diagnoses `[source checksum]`, clinical documents `[source checksum]`, and labs `[source checksum]`.

MIMIC, eICU, and UKB remain directly accessible and read-only but are not pooled. MIMIC is `[internal dataset path]` with `mimic-iv-3.1/hosp/*.csv.gz`, `icu/*.csv.gz`, and note members; eICU uses the catalogued `EICU 2.0 data/*.csv.gz` members; UKB uses the catalogued `ukb672073*.csv` files. They have no HCC crosswalk, compatible first-resection documentary-M2 endpoint, or complete Chinese reader/pathology mapping. Their rows and notes remain available but are not inputs.

## 6. Coupled uncertainty, endpoint, models, and comparators

For every world, construct episode, operation clock, CT/MRI window, whole-accession identity, raw row/text costs, treatment exclusion, source-clean status, and all 25 ledger capacities together. Blank `Examination Number`, cross-patient \((Encounter Number,Examination Number)\) collision, component disagreement, ambiguous modality/context, and nonreversible parse remain explicit outer states; no representative row is selected.

Retain inherited onset categories \(O=0\) readable by 72 hours, \(O=1\) first readable in (72,48] hours, \(O=2\) first readable in (48,24] hours, \(O=3\) first readable in (24,12] hours, and \(O=4\) not readable by 12 hours, later/never, or unresolved. They are reader-book/onset states, not report-release evidence.

Use three fixed radiology and three fixed pathology books: two independent qualified Chinese readers and an adjudicator for each modality. Preserve all disagreements and pathology labels \(\{OUT,IN0\text{-}A,IN1\text{-}A,IN0\text{-}U,IN1\text{-}U\}\); evaluate all nine radiology-by-pathology pairs. Documentary-M2 remains a fixed documentary endpoint, not biological MVI.

Retain frozen additive logistic arms:

- \(B\): acquisition-only;
- \(R\): acquisition plus report-surface;
- \(G\): acquisition, report-surface, and clean-reader semantics;
- \(G_{\rm mask}\): byte-identical \(G\) coefficients with report blocks replaced by the training-defined unavailable block;
- \(G_{\rm SA}\): the attribution parent’s no-refit shadow.

Every \(G\) semantic feature must retain the parent’s exact source table/field, accession, raw-byte digest, ordinal set, normalization/parser digest, and aggregation provenance. Missing or ambiguous provenance masks the complete semantic block in \(G_{\rm SA}\), without refitting. Identifiers, pathology, untimed notes, future rows, reader identity, and test-derived dictionaries are forbidden predictors. Feature order, coefficients, model hashes, score bytes, unavailable block, and protected tie keys are frozen in 2019.

Use the inherited 256 hash-random rankings, anchored patient deletion with EMPTY positions, and all inherited source identity/content and patientwise worst-state attribution gates. No state, reader, pathology label, identity choice, cost coefficient, or future row crosses worlds.

## 7. Capacities, queue, and estimand

Let the exact scaled integer cost be

\[
\widetilde w^{a,b}_u=4+a(n_u-1)+b x_u=4w^{a,b}_u.
\]

For each \((a,b)\), let \(\widetilde W^{a,b}_{\rm ref}\) be the minimum total scaled cost across all required 2015–2019 development/lock states. Freeze the base-unit capacity and its scaled equivalent:

\[
C_{a,b}=\left\lfloor\frac{\widetilde W^{a,b}_{\rm ref}}{40}\right\rfloor,\qquad
\widetilde C_{a,b}=4C_{a,b}.
\]

This exactly reproduces the inherited capacities at \((0,0),(4,0),(4,4)\): \(C_U,C_R,C_T\). Require \(N_{\rm ref}\ge500\), \(K=\lfloor0.10N_{\rm ref}\rfloor\ge50\), every \(C_{a,b}\ge50\), at least 50 documentary-M2 events in every required primary year/world, and nonempty eligible/event support in every grid cell. The 5% and 20% capacity fractions remain descriptive only.

For method \(M\), world \(\omega\), and frozen threshold \(q\), use the same ranked patient list \(\pi_M(\omega,q)\) for every ledger. Define the longest-prefix queue

\[
S_{M,a,b}^{K,C}=
\{\pi_M(1),\ldots,\pi_M(m)\},\quad
m=\max\left\{j:j\le K,\ 
\sum_{r=1}^j\sum_{u\in i_r}\widetilde w^{a,b}_u
\le\widetilde C_{a,b}\right\}.
\]

Stop when the next patient exceeds capacity; do not skip, backfill, rerank, or spend unused capacity. Charge all eligible accessions whether report content is observed, masked, or lifecycle-unknown. Zero-accession patients remain in the denominator with zero cost. Preserve identical/conflicting rows in every grid cost.

For each coupled cell \(z=(\omega,O,y,d,r,\delta)\), let \(H_{M,a,b}(z)\) be documentary-M2 patients captured, \(m_{M,a,b}(z)\) offered patients, and \(\widetilde U_{M,a,b}(z)\) used scaled cost. Define

\[
D_{G,C,a,b}(z)=
100[H_{G,a,b}(z)-H_{C,a,b}(z)]/K,
\quad C\in\{B,R,G_{\rm mask}\},
\]

with exact integer cross-products; equality with 5 fails. Report \(H,m,\widetilde U,\widetilde U/\widetilde C\), unused capacity, EMPTY positions, patient/accession witnesses, \(n_u,b_u,x_u\), and coefficients.

The new estimand is

\[
\Delta_{\rm grid}(q)=
\min_{a,b\in\{0,\ldots,4\}}
\min_{z\in{\cal Z}_{20}\cup{\cal Z}_{21}}
\min_{C\in\{B,R,G_{\rm mask}\}}
D_{G,C,a,b}(z).
\]

The grid gate is \(\Delta_{\rm grid}(q^*)>5\), together with every inherited comparator, random, deletion, identity/content, semantic-attribution, temporal, and nonvacuity gate. \(H/U\), the number of selected patients, queue symmetric differences, and coefficient-wise frontiers are descriptive only.

## 8. Selection, falsification, and outcome meaning

Select the inherited
\[
q^*=\min\{q\in{\cal R}:q<1,\ G^{\rm parent}_{20}(q)=1\}
\]
using only the parent’s complete 2020 \(U/R/T\) gate. Freeze all rejected lower thresholds and witnesses. The 22 intermediate ledgers do not participate in selection and cannot rescue or change \(q^*\). Replay all 25 cells at frozen \(q^*\) in 2020, then once in untouched 2021 with the same coefficients, capacities, patient set, books, scores, ties, and queue rule.

Outcome precedence:

1. `computationally_inconclusive`: any catalog/source/schema hash, raw ordinal/field boundary, join, date interval, ledger/capacity, feature provenance, frozen model/score/tie, fixed-\(K\), longest-prefix/EMPTY, patientwise-max, no-refit, output-linkage, or \(q^*\)-freeze check fails.
2. `feasibility_inconclusive`: required \(N,K,C_{a,b}\), events, books, label-stable patients, or grid-cell support is insufficient.
3. `selection_adverse_no_subcomplete_threshold`: no parent \(q<1\) passes, or \(q^*=1\).
4. `inherited_gate_adverse`: any inherited \(U/R/T\), comparator, random, deletion, source/content, attribution, or temporal gate fails.
5. `structural_weight_adverse`: inherited gates pass, but at least one computable intermediate grid cell has \(D_{G,C,a,b}\le5\) in a required 2020/2021 world.
6. `structural_weight_supportive`: every inherited and all 25 grid gates pass in both 2020 and untouched 2021 with exact witnesses.
7. Append `lifecycle_actual_burden_and_action_evidence_inconclusive` to every status because those fields are unavailable.

The hypothesis is falsified by any required intermediate-weight margin \(\le5\), not by a descriptive queue change alone. Supportive means only that the finite HCC queue property is insensitive to the stated structural-weight grid. Adverse means the property depends on the chosen relative row/text weights; it does not show that semantic imaging is useless. Inconclusive means computation or feasibility prevents the source-only test. A grid pass does not identify actual costs, report availability, clinician behavior, or benefit.

## 9. Harbor outputs, verifier tests, and external bridge

Read every configured HCC source row read-only and record actual filtering: only the first-resection frame, prior-treatment window, CT/MRI window, role years, and explicit ambiguity quarantine; no unreported sampling. Write derived files only in the workspace:

- `derived/source_manifest_raw_ordinals.parquet`;
- `derived/cohort_clock_and_quarantine.parquet`;
- `derived/whole_accession_onset_states.parquet`;
- `derived/accession_payload_digest_registry.parquet`;
- `derived/accession_structural_costs.parquet`, containing \(n_u,b_u,x_u\) and all 25 scaled costs;
- `derived/ledger_capacity_manifest_2019.json`;
- `derived/semantic_feature_provenance_registry.parquet`;
- `derived/frozen_model_queue_manifest.json`;
- `derived/state_registry_2020.parquet` and `derived/state_registry_2021.parquet`;
- `derived/threshold_selection_2020.json`;
- `derived/grid_frontiers_2020.parquet` and `derived/grid_frontiers_2021.parquet`;
- inherited patientwise identity/content and semantic-attribution loss files;
- `derived/temporal_confirmation_2021.json`;
- `derived/operational_metadata_status.json`;
- `derived/interpretation.json`.

The verifier must evaluate computation and conclusion discipline:

- prove the \((0,0),(4,0),(4,4)\) grid cells reproduce inherited \(U,R,T\) accession costs, capacities, queues, and outputs byte-for-byte;
- recompute all 25 scaled integer costs and capacities from exact examination fields and raw ordinals;
- use an adversarial fixture where all three corners pass but an intermediate cell fails, and require `structural_weight_adverse` rather than a corner-based supportive claim;
- alter one coefficient, 512-byte divisor, field boundary, duplicate row, or accession component and require the exact affected cost/queue witness to change; a source/hash/parser mismatch is computationally inconclusive;
- ensure no intermediate coefficient is chosen or removed using 2020/2021 outcomes and no failed cell is averaged away;
- make one semantic feature unattributed and require the parent’s complete-block no-refit masking and patientwise worst-state witness;
- perturb only a 2021 row/world and verify no 2019 artifact, \(q^*\), or 2020 selection changes;
- verify the same score bytes, tie key, \(K\), patient set, and longest-prefix/EMPTY rule are used in every ledger;
- test conclusion templates against supportive, adverse, feasibility-inconclusive, and computationally-inconclusive outputs;
- reject prose describing finite-census margins as future-patient probabilities, actual minutes, report release/viewing, causal effects, clinical benefit, staffing requirements, or deployment readiness.

Automatic verification can establish deterministic source lineage, all 25 structural calculations, queue arithmetic, temporal freeze/replay, feature masking, and whether the written conclusion is linked to computed outputs. It cannot establish which coefficient pair approximates human work, whether a report was available or reviewed, whether text is clinically correct, whether pathology is specimen-linked, or whether a clinician would act.

Before any workflow interpretation, the external bridge must obtain accession-level RIS/PACS audit trails with acquisition, report creation, finalization, release, ingestion, retrieval, and view times; image-series and prior-comparison metadata; and a blinded timed-reader study recording task, reader qualification, report/image content, interruptions, and duration. Link those data to the same accession/resection frame under governance review. Use them to calibrate or replace the structural weights in a separate patient-disjoint study; do not back-fit the 25-grid result, \(q^*\), or documentary endpoint. Clinical action or patient benefit additionally requires linked treatment/outcome data and a decision-appropriate silent-mode or interventional study with expert adjudication.
