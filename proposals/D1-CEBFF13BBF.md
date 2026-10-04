# Certified two-part report-coverage contract for patient-complete documentary-M2 allocation

## 1. Successor, audit finding, and substantive repair

This is a targeted child of \`[prior hypothesis]\`. It preserves the parent’s frozen adult first-eligible-resection population, documentary-M2 endpoint, coupled source/operation/identity/onset/reader/pathology uncertainty, whole-accession units, locked B/R/G/Gmask pipelines, fixed-\(K\) comparator/random/anchored-deletion gates, exact patient-complete coverage frontier, 24-hour confirmatory result, and explicit limits on clinical inference.

The unresolved defect is the operational meaning of \`q_req\`. The parent correctly defines a finite-corpus worst-case threshold, but its scalar name can still be read as an overall service coverage target. That is not justified when the HCC cohort contains patients with no technically eligible CT/MRI accession and when \(n_A\) changes across coupled source/operation worlds. A report-archive audit that supplies only “percent of reports available” or an estimated patient percentage cannot establish the parent’s contract, even if the percentage numerically exceeds q_req.

The repair is to make q_req a conditional threshold with a separately certified structural denominator. The primary output is now the auditable contract

\[
\mathcal C_{\omega,a}=(N_{\omega,a},n_{A,\omega,a},e_{\omega,a},q_{\rm req}),
\qquad e_{\omega,a}=n_{A,\omega,a}/N_{\omega,a}.
\]

Here \(e\) is the fraction of all eligible first-resection patients with at least one source-clean, acquisition-eligible 24-hour CT/MRI accession, and q_req is the required fraction of those patients whose entire eligible accession bundle is exposed. Neither is an observed HCC report-availability estimate. The bridge must certify both components and retain the three patient strata:

1. \(I=0\): no eligible accession in the frozen HCC world;
2. \(I=1\), incomplete: at least one eligible accession but not all are exposed;
3. \(I=1\), complete: every eligible accession is exposed.

The scalar q_req is reported only with its \((N,n_A,e)\) certificate and is never labelled “coverage of all patients,” “fraction of reports released,” “capacity,” “viewing,” or “clinical utility.” If a future service is intended for all first-resection patients, \(e\) is a separate structural feasibility issue; if it is intended only after an eligible acquisition exists, q_req is explicitly conditional on that entry population. This distinction repairs auditability without changing the frozen documentary estimand.

## 2. Clinical question and falsifiable hypothesis

The clinically relevant unresolved question is:

> In a fixed-capacity retrospective documentary review service offered 24 hours before first eligible HCC resection, what patient-level report-bundle exposure contract is sufficient to preserve the locked semantic model’s documentary-M2 capture advantage under the worst compatible source, identity, onset, reader, pathology, and deletion worlds?

This matters because a model can appear useful in stored text while its required reports are not technically available as a complete patient bundle. Conversely, an accession-level availability percentage can overstate readiness when one patient has multiple eligible accessions and a missing component changes the semantic input. The advance is an auditable handoff requirement for a future archive/workflow study, not a claim that HCC contains a deployable service.

The strongest HCC-supported claim is limited to source structure: the snapshot contains patient/encounter-linked procedures; examination rows with nonblank whole-accession identifiers, an acquisition-like time, machine labels, and narrative fields; same-encounter pathology narratives; and temporally labelled medication and non-medication order records. It does not contain authored, finalized, released, ingested, retrievable, readable, viewed, amended, or retracted timestamps for examination reports, nor service capacity, clinician actions, costs, harms, treatment changes, recurrence, survival, or patient utility.

The untested claim is whether the frozen ranking has a strictly positive reserve against adversarial missing report bundles at 24 hours, after conditioning that statement on a certified HCC patient/accession denominator.

The confirmatory hypothesis is:

> At \(\rho=.10\) and \(d=24\) hours, maximum stored content passes every inherited comparator, random, and anchored singleton-deletion gate separately in 2020 and 2021, and the certified conditional threshold \(q_{\rm req}<1\), where q_req is the smallest exact patient-complete bundle-coverage lower bound for which all inherited gates pass in every compatible coupled world with the HCC-derived \(N\) and \(A\) denominators.

A q_req below one means only that some nonzero amount of conditional missing-bundle exposure can be tolerated in this finite corpus under the prespecified adversarial contract. It does not mean that a hospital can achieve that threshold, that all patients are covered, or that clinical outcomes improve.

## 3. Available evidence and clinical evidence limits

The proposal is motivated by the clinical problem of preoperative information about HCC heterogeneity and microvascular invasion, but the HCC endpoint remains documentary rather than biological. Pathology narratives are available by encounter, but HCC has no specimen, block, slide, accession, or pathology time field to establish specimen-level linkage or adequate sampling. The experiment therefore tests capture of a prespecified documentary-M2 label, not pathological MVI validity, recurrence risk, margin selection, transplantation, ablation, systemic therapy, surveillance, or survival benefit.

The three demonstrations in \`references/research-ambition/README.md\` were treated as demonstrations of rigor, not as evidence that HCC contains their modalities or endpoints. In particular, the cancer demonstration’s main article and full STAR Methods are unavailable according to that README and are not claimed as inspected. The local HCC data are the binding evidence for this proposal; any public literature can motivate the question but cannot repair absent report-release, pathology-linkage, workflow, or outcome fields.

## 4. Population, temporal boundaries, and frozen estimand

Use HCC snapshot \`[source checksum]\) and catalog \`[internal dataset path]`, catalog SHA-256 \`[source checksum]\`.

For each coupled source world, include adults at their earliest source-documented eligible hepatobiliary resection under a preregistered clinician-adjudicated procedure dictionary, requiring same-\((患者主索引,就诊号)\) pathology support for the documentary frame. Exclude a patient if that world records an earlier qualifying resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in \([t_{\rm op}-365\text{ d},t_{\rm op})\). Candidate CT/MRI acquisition intervals must lie wholly within \([t_{\rm op}-90\text{ d},t_{\rm op}-d)\), with \(d\in\{72,48,24,12\}\) hours.

Use validated operation times. Date-only or midnight-like operation values are intervals \([{\rm date},{\rm date}+24\text{ h})\), and interval logic must be declared before outcomes or scores are inspected. Competing operation, episode, calendar-year, treatment, modality, imaging-window, and source interpretations remain coupled worlds. Possible 2020/2021 cases cannot enter development or 2019 lock, and possible 2019 cases cannot enter testing. Roles remain patient-disjoint: 2015–2018 development, 2019 preprocessing/hyperparameter/K lock, separate 2020 and 2021 tests, and 2022 onward audit-only.

The endpoint is same-encounter documentary M2. Two qualified Chinese-reading hepatobiliary pathologists plus an adjudicator create three complete pathology books with OUT, IN0-A, IN1-A, IN0-U, and IN1-U states, preserving every row, raw order, and field boundary. Two qualified Chinese-reading abdominal radiologists plus an adjudicator create three complete radiology books. The nine global radiology/pathology book pairs are fixed across patients, years, cutoffs, source worlds, onset states, models, and deletions. No row- or field-level reader mixing is permitted. Unresolved cases remain outer states.

## 5. Exact source bindings and availability

All HCC sources are ordinary CSV files; there are no HCC archive members. The complete configured non-HCC datasets remain read-only and directly accessible, but they are not pooled because no compatible first-resection documentary-M2 endpoint or patient crosswalk is established.

The bound HCC files and required fields are:

- \`encounters\`: \`[internal dataset path]`; key \((患者主索引,就诊号)\); \`年龄\`, \`性别\`, \`就诊时间\`, \`入院时间\`, \`出院时间\`.
- \`procedures\`: \`[internal dataset path]`; key \((患者主索引,就诊号)\); \`手术\`, \`开始时间\`, \`结束时间\`, \`手术来源\`.
- \`examinations\`: \`[internal dataset path]`; encounter key \((患者主索引,就诊号)\), whole-accession key \((患者主索引,就诊号,检查号)\); \`检查\`, \`检查所见\`, \`检查诊断\`, \`开始时间\`, \`机器型号\`, \`检查号\`. The only temporal column is the acquisition-like \`开始时间\`.
- \`pathology\`: \`[internal dataset path]`; key \((患者主索引,就诊号)\); \`病理\`, \`检查所见\`, \`检查诊断\`, \`机器型号\`; no specimen, slide, accession, or time field.
- \`medications\`: \`[internal dataset path]`; patient-wide temporal join before episode restriction; \`用药\`, \`药品类型\`, \`开始时间\`, \`结束时间\`.
- \`orders\`: \`[internal dataset path]`; patient-wide temporal join; \`医嘱(非药品)\`, \`开立时间\`, \`开始时间\`, \`结束时间\`, \`医嘱状态\`.
- \`diagnoses\`: \`[internal dataset path]`; encounter key; untimed corroboration only.
- \`clinical_documents\`: \`[internal dataset path]`; audit-only because it has no usable preoperative exposure time.
- \`labs\`: \`[internal dataset path]`; leakage audit only because the catalog documents no safe common assay-unit harmonization.
- \`vitals\`: \`[internal dataset path]`; identifier-only for this design.
- \`transfers\`: \`[internal dataset path]`; identifier-only for this design.
- \`front_page\`: \`[internal dataset path]`; identifier-only for this design.

The BOM-aware raw-header audit confirms the examination header is exactly \((患者主索引,就诊号,检查,检查所见,检查诊断,开始时间,机器型号,检查号)\), procedures contain \((患者主索引,就诊号,手术,开始时间,结束时间,手术来源)\), pathology contains \((患者主索引,就诊号,病理,检查所见,检查诊断,机器型号)\), and encounters contain the stated demographic and encounter-time columns. Read all rows of each bound HCC file; retain source SHA-256, schema hash, parser version, BOM handling, raw ordinal, raw bytes, reversible backpointer, and every deterministic inclusion/exclusion reason. Source files remain read-only.

For completeness, retain direct access and provenance for:

- MIMIC: \`[internal dataset path]`, with archive members such as \`mimic-iv-3.1/hosp/admissions.csv.gz\` and the separate ordinary \`note/radiology.csv.gz\` and \`note/radiology_detail.csv.gz\` files. No HCC crosswalk or compatible endpoint is available.
- eICU: \`[internal dataset path]`, including \`patient.csv.gz\`, \`diagnosis.csv.gz\`, \`treatment.csv.gz\`, and \`note.csv.gz\`. No compatible first-resection documentary-M2 crosswalk is available.
- UKB: ordinary files under \`[internal dataset path]`, including \`ukb672073.csv\`, \`ukb672073_Health_Related_Outcomes.csv\`, and the other catalogued tables. No HCC crosswalk or compatible documentary endpoint is available.

These datasets are not silently treated as negative evidence; they are retained as accessible but out of scope.

## 6. Coupled whole-accession onset and exposure

For patient \(i\), source/operation world \(\omega\), cutoff \(d\), and nonblank whole accession \(u\), define \(E_{i\omega d u}=1\) only when operation state, accession identity, CT/MRI membership, and the acquisition interval from examinations.\`开始时间\` are all valid and the interval lies wholly in \([t_{i\omega}-90\text{ d},t_{i\omega}-d)\). Blank identifiers, component disagreement, ambiguous modality/context, nonreversible parsing, treatment/pathology/MVI leakage, unresolved identity, or invalid hashes make the entire accession unavailable.

Assign one onset category to each source-clean eligible accession version:

- \(O=0\): eligible by 72 hours;
- \(O=1\): first eligible in \((72,48]\) hours;
- \(O=2\): first eligible in \((48,24]\) hours;
- \(O=3\): first eligible in \((24,12]\) hours;
- \(O=4\): not eligible by 12 hours or only later/never.

The visibility vector in 72/48/24/12 order is
\[
V(O)=(1\{O=0\},1\{O\le1\},1\{O\le2\},1\{O\le3\}),
\]
and \(M_{i\omega d u}=E_{i\omega d u}V_d(O_{i\omega u})\). HCC does not observe authored or release onset. The state set is therefore the complete set of compatible hypothetical content-onset states, not an imputed timestamp distribution. Coupling is retained: source, operation, identity, onset, reader, pathology, year, deletion, and model inputs are not selected independently to improve a result.

## 7. Locked models, K, endpoint gates, and uncertainty

Fit four additive logistic pipelines independently with patient-balanced, outcome-blind preprocessing:

- \(B(Z)\): acquisition-only;
- \(R(Z,S,Q)\): acquisition plus report surface/availability;
- \(G(Z,S,Q,X)\): semantic model;
- \(Gmask\): the same fitted \(G\), with report-derived semantic blocks replaced by the training-defined unavailable block and no refit.

\(Z\) includes age, sex, acquisition facts, eligible-accession count/recency, accession ambiguity, and development-grouped machine. \(S/Q\) are report-surface and availability blocks; \(X\) is clean-reader semantics. Exclude pathology, endpoints, IDs, reader identity, labs, untimed narratives, and test-derived features. Freeze the regularization grid and all preprocessing after the independent 2019 lock, over all nine global reader/pathology books.

Let \(N_{\rm ref}\) be the minimum eligible N over 2015–2019, all four cutoffs, and every admissible source world. Freeze \(K_\rho=\lfloor\rho N_{\rm ref}\rfloor\), \(\rho\in\{.05,.10,.20\}\), requiring \(N_{\rm ref}\ge500\), \(K_{.05}\ge25\), \(K_{.10}\ge50\), and \(K_{.20}\ge100\). The confirmatory analysis is \(\rho=.10,d=24\), with separate 2020 and 2021 results; each primary year/world requires \(N\ge K_{.10}\) and at least 50 documentary-positive events.

Serialize score and tie keys using exact binary64 bits, a specified correctly rounded evaluation order, and protected SHA-256 patient keys for exact ties. For anchored singleton deletion, freeze original K positions, models, scores, onset ledger, books, and tie order; remove all records for the deleted patient without backfill or requota. A deleted selected patient leaves an empty offered position.

For complete state \(z=(\omega,O,a,d,\text{reader/pathology pair},\text{deletion})\), let \(H_M(z)\) be documentary-M2 captures. For \(C\in\{B,R,Gmask\}\),
\[
D_{G,C}(z)=100[H_G(z)-H_C(z)]/K,\quad
D_{G,rand}(z)=100H_G(z)/K-100Y(z)/N(z).
\]
Each inherited gate requires \(D>5\) by exact integer cross-products; equality fails. All margins use the same complete coupled state. No maxima and minima from different worlds may be stitched.

## 8. Repaired two-part coverage estimand

For each year \(a\) and source/operation world \(\omega\), define the frozen 24-hour eligible bundle
\[
A_{i\omega}=\{u:E_{i\omega,24,u}=1\},\quad
I_{i\omega}=1\{|A_{i\omega}|>0\}.
\]

The full analysis population is
\[
N_{\omega,a}=\sum_{i\in a}1,
\]
including \(I=0\) patients. The structural entry fraction is
\[
e_{\omega,a}=n_{A,\omega,a}/N_{\omega,a},\qquad
n_{A,\omega,a}=\sum_{i\in a}I_{i\omega}.
\]
This is not report availability. It records how often the frozen acquisition rule produces a report-bundle opportunity.

For onset state \(O\), define patient-complete bundle exposure
\[
C_{i\omega}(O)=1\{I_{i\omega}=1\ \land\
\sum_{u\in A_{i\omega}}M_{i\omega,24,u}=|A_{i\omega}|\}.
\]
A patient with no eligible accession is not silently treated as an incomplete report bundle; it is recorded in the structural \(I=0\) stratum. A patient with one or more eligible accessions and any missing accession is incomplete. Whole accessions remain indivisible.

The conditional coverage is
\[
Q_{\omega,a}(O)=
\frac{\sum_{i\in a}C_{i\omega}(O)}{n_{A,\omega,a}},
\quad n_{A,\omega,a}>0.
\]
If \(n_A=0\), the state is feasibility-inconclusive, not \(Q=0\) and not \(Q=1\).

Define the exact contract record for every state as
\[
T_{\omega,a,O}=(N_{\omega,a},n_{A,\omega,a},N_{\omega,a}-n_{A,\omega,a},
n_{\rm partial},n_{\rm complete},Q_{\omega,a},\text{patient hashes}).
\]
The record must include patient-level membership in all three strata, accession count per patient, all eligible accession hashes, and the source-world identifier. This is the operational audit object.

For q in the exact finite set \(R\) of all rational values \(k/n_{A,\omega,a}\) over retained primary year/world denominators, including 0 and 1, let \(Z_{\rm cert}(q)\) contain every complete coupled state satisfying \(Q_{\omega,2020}\ge q\) and \(Q_{\omega,2021}\ge q\), with its independently retained structural \(e_{\omega,a}\). Define \(\operatorname{PASS}(q)=1\) only when every comparator, random, and anchored-deletion gate passes in every state in \(Z_{\rm cert}(q)\). Since \(Z_{\rm cert}(q_2)\subseteq Z_{\rm cert}(q_1)\) for \(q_2>q_1\), PASS is monotone.

If maximum stored content fails, q_req is undefined. Otherwise
\[
q_{\rm req}=\min\{q\in R:\operatorname{PASS}(q)=1\}.
\]
Also emit \(q_{\rm prev}\), the immediately lower failing threshold when one exists, and the complete boundary witnesses. Report the entire \(e\)-range and the worst structural entry fraction alongside q_req; do not collapse them into a fabricated “overall coverage requirement.” This is a conditional finite-corpus threshold, not a population or service estimate.

The 12/48/72-hour analyses use the same onset assignments and emit the same \((N,n_A,e,n_{\rm partial},n_{\rm complete})\) trajectory. They are non-vetoing sensitivity analyses and cannot rescue or veto the 24-hour confirmatory result.

## 9. External audit bridge made exact

A future report-archive audit may establish the conditional contract only if it is linked to the frozen HCC world. It must provide, for every audited HCC patient and every HCC-derived eligible accession:

- exact \((患者主索引,就诊号,检查号)\) crosswalk, source row ordinals, hashes, and complete-version hashes;
- immutable report version and predecessor/amendment/retraction identifiers;
- authored, finalized, released, ingested, retrievable, readable, and retracted timestamps with timezone and clock provenance;
- operation-clock validation and the locked scoring-pipeline input hash;
- a patient-level disposition for \(I=0\), incomplete, or complete;
- an explicit statement that archive access did not redefine \(N\), \(A\), modality, operation, or pathology eligibility.

Technical readability means that the locked pipeline can retrieve and parse the complete report bundle. It does not mean a clinician viewed it or acted on it.

A census reports exact stratum counts and \(Q\) for each compatible world. A probability audit samples only from the fixed HCC-derived patient/accession frame and retains nonresponders. For each year/world it must produce a simultaneous design-based lower bound \(L_{\rm complete}\) on the number of complete patients in the fixed \(A\) denominator and report
\[
q_L=L_{\rm complete}/n_A.
\]
The denominator is not estimated from an aggregate archive percentage. If the archive audit cannot certify the HCC-derived \(A\) frame, it is archive-inconclusive. A valid \(q_L\ge q_{\rm req}\), with matching source/version/hash and structural strata, establishes the conditional coverage contract; it says nothing about patients in \(I=0\).

The external bridge has one-hot labels:

1. \`archive_inconclusive\`: crosswalk, version, clock, denominator, sampling, simultaneous-bound, or readability validation fails.
2. \`structural_entry_not_certified\`: the audit cannot certify the HCC-derived \(N\) and \(A\) strata.
3. \`conditional_coverage_contract_not_established\`: a valid audit has \(q_L<q_{\rm req}\).
4. \`audited_documentary_adverse\`: a census or exact compatible audit state directly fails a primary fixed-K gate.
5. \`externally_conditional_documentary_supportive\`: a valid census passes directly, or a valid \(q_L\ge q_{\rm req}\) places every compatible state in the passing set.

The last label is still not clinical-action support. A separate prospective silent-mode workflow study must measure actual report availability to intended users, viewing, action, queueing, staffing, competing workload, failures, downstream decisions, harms, costs, and patient outcomes. If a proposed service includes \(I=0\) patients, it must also specify how they are handled; q_req cannot be used to waive that structural problem. Set \`clinical_action_status=not_identified\` until those data and stakeholder-defined utilities exist.

## 10. Primary interpretation and falsification

Use mutually exclusive one-hot interpretation:

1. \`computationally_inconclusive\`: source replay, state generation, exact ranking, contract certificate, quotient replay, boundary witness, or verification fails.
2. \`feasibility_inconclusive\`: any locked N, K, event, \(n_A>0\), or structural-denominator gate fails.
3. \`maximum_content_signal_adverse\`: maximum stored content fails any 24-hour comparator, random, or deletion gate in 2020 or 2021.
4. \`conditional_bundle_robustness_adverse\`: maximum content passes but q_req is undefined or q_req=1; no positive conditional missing-bundle reserve is certified.
5. \`hcc_conditional_robustness_supportive_bridge_pending\`: maximum content passes, q_req<1, q_prev fails when it exists, all exact witnesses verify, and the \((N,n_A,e)\) certificates are complete. This supports only the finite-corpus conditional documentary reserve.
6. \`structural_entry_or_archive_bridge_pending\`: the HCC computation is valid but an external denominator/crosswalk/readability bridge is absent; this is not adverse evidence about the model.

A favorable sensitivity cutoff cannot alter the primary label. Report q_req, \(1-q_{\rm req}\) as a mathematical conditional reserve only, every structural \(e\), \(N\), \(n_A\), stratum count, \(H_G\), \(K-H_G\), all comparator/random margins, and raw worst witnesses. Variation across source, operation, identity, onset, reader, pathology, and deletion worlds is uncertainty for the frozen corpus; no superpopulation interval or causal effect is claimed.

## 11. Computation, outputs, and verification

Create workspace-only:

- \`derived/source_and_filter_manifest.json\`;
- \`derived/patient_operation_accession_ledger.parquet\`;
- \`derived/pathology_reader_ledger.parquet\`;
- \`derived/monotone_onset_exposure_ledger.parquet\`;
- \`derived/frozen_models_K_ties.json\`;
- \`derived/patient_complete_contract_strata.parquet\`;
- \`derived/q_requirement_witnesses.parquet\`;
- \`derived/interpretation.json\`;
- source/hash/replay, exact-ranking, deletion, boundary-oracle, and contract-audit logs.

Required checks are lossless raw-to-ledger replay; source/schema hash agreement; complete coupled worlds; exact score/tie replay; exact q-threshold certificate; structural \((N,n_A,e)\) certificate replay; raw boundary witnesses; transformed-loss residual \(\le10^{-8}\); synthetic brute force through 12 patients; source-backed shards through 20; and regression to the parent’s source/accession and maximum-content outputs.

Fixtures must include blank and multirow accessions, acquisition after cutoff, O=2/O=3 transition, same conditional q with different structural e, same e with different patient identities, partial bundles, zero-accession patients, exact ties, \(N=K\), \(n_A=0\), sparse events, deleted selected patients, and q equality. Any sampling, state cap, timeout, heuristic gap, unresolved incumbent, floating-only threshold, quotient collision, missing stratum witness, denominator substitution, or coordinatewise world stitching is computationally inconclusive.

The verifier may establish source lineage, exact arithmetic, onset monotonicity, bundle predicates, fixed-K gates, the conditional q_req, the structural denominator certificate, and whether the conclusion follows from computed outputs. It must reject a scalar q_req presented without \(N,n_A,e\) and patient-level strata, and reject supportive prose attached to adverse or incomplete outputs. It may accept correctly bounded adverse or inconclusive interpretations. It cannot establish actual report release, readability outside the tested archive, viewing, workflow capacity, stakeholder preference, biological MVI, treatment effect, safety, recurrence, survival, transportability, or patient benefit.

## 12. What changed and what remains uncertain

Changed from the parent: q_req is explicitly conditional; \(I=0\) patients remain in the model population but are separated into a structural entry stratum; \(n_A=0\) is infeasible rather than assigned a coverage value; every q result carries a fixed \((N,n_A,e)\) and three-stratum certificate; external probability audits use a lower bound over the fixed HCC-derived \(A\) denominator rather than an unqualified ratio; and deployment interpretation requires both denominator certification and conditional bundle coverage. The q frontier, patient-complete unit, fixed-K gates, coupled uncertainty, first-resection frame, and clinical evidence limits are unchanged.

Remaining uncertainty is substantive: the HCC archive does not reveal release or viewing times; examination-to-report version identity and pathology-to-specimen validity require expert adjudication; the procedure and treatment dictionaries require clinical review; and no configured dataset supplies workflow capacity, utilities, treatment decisions, recurrence, survival, or patient benefit. Therefore the experiment can falsify a finite-corpus conditional documentary robustness claim and can specify the next archive/workflow evidence requirement, but it cannot recommend a clinical service or treatment decision.
