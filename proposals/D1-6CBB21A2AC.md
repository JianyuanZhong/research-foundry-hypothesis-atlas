> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Audit-compatible whole-accession visibility frontier for documentary-M2 review

## 1. Targeted repair and preserved design

This is a targeted successor to assessed-valid `[prior hypothesis]`. It preserves without modification the parent's:

- adult, source-defined first-eligible HCC-resection population and at most one state-specific episode per patient;
- coherent operative-clock alternatives, primary `c_24=t_op-24h` cutoff, diagnostic `d={12,48,72}` cutoffs, 90-day CT/MRI acquisition window, and 365-day recorded-prior-treatment window;
- possibility-based `U_D/U_V/U_T` temporal quarantine, 2015-2018 development, 2019 locking, and separate 2020 and 2021 tests;
- encounter-documentary HCC/M2 endpoint, indivisible same-encounter pathology composites and `OUT, IN0-A, IN1-A, IN0-U, IN1-U` terminals;
- reversible `V/A/E` report lineage, whole-accession source-unavailability, six complete corpus-wide reader books, and nine globally fixed radiology-by-pathology pairs;
- frozen `B, R_clean, G_clean, Gclean_mask` pipelines, independent fitting where specified, no-refit semantic mask, fixed historical `K_.10`, comparator-closed contrasts, strict margin greater than five documentary-M2 captures per 100 positions, exact attained world extrema, and whole-patient singleton deletion;
- parent all-content prerequisite, exact optimization, fail-closed gates, and non-causal/nondeployment claim limits.

The parent's whole-accession release frontier is computationally coherent, but its external decision bridge is not yet audit-identifiable. It says a later audit should compare a lower report-coverage bound with `c*`, without freezing the denominator that must be reconstructed across population/clock worlds, distinguishing accession from patient availability, handling within-patient multi-accession dependence, or proving that a pre-cutoff report version is the same body the locked model scored.

The exact HCC source demonstrates that this matters. A full read of all 419,996 examination rows found 392,854 nonblank `(patient master index,encounter number,examination number)` units, 16,534 multirow units, 66,534 multi-accession encounters, and 39,610 multi-accession patients. A coarse CT/MR lexical scan, not a cohort count, still found 7,647 patients with multiple candidate units. Thus patient, accession, and component denominators are not interchangeable.

This child repairs one issue: it freezes an audit-compatible denominator and version/time mapping for the computed frontier. It does not add unavailable timestamps or relax the parent's robustness claim.

## 2. Evidence-supported claim and unresolved hypothesis

The strongest evidence currently supported is limited to source structure. HCC examinations contains patient and encounter keys, an explicit `Examination Number`, modality text, eventual `Examination Findings/Examination Diagnosis` bodies, acquisition-like `Start Time`, and `Machine Model`. It has no report-author, version, signature, finalization, release, amendment, or clinician-view field. One accession can contain multiple rows and one patient can contain multiple accessions. Pathology remains untimed and lacks specimen/accession/slide/block/sampling linkage. These facts support computing a finite stored-content missing-report stress test, not historical decision-time availability.

The unresolved Harbor hypothesis remains:

> Conditional on every parent all-content gate passing at `K_.10` and `c_24`, there is a sharp sufficient accession-release fraction `c_A* <= 0.80` such that all six comparator-closed undeleted lower margins and all six whole-patient singleton lower margins remain strictly greater than five in every declared source/pathology/reader world and every whole-accession release pattern meeting that fraction.

Equality of a margin to five fails. Equality `c_A*=0.80` passes only when every required margin is strictly greater than five. The 0.80 bound is a preregistered operational stress criterion, not measured hospital capacity.

The additional falsifiable bridge claim is:

> The value `c_A*` is audit-mappable only if a later audit reconstructs the exact eligible accession denominator for every admissible primary-cutoff world, assigns whole-unit pre-cutoff final/release/view states to matching report versions, and establishes a simultaneous lower accession-coverage bound at least `c_A*`. Patient coverage, pooled coverage, acquisition counts, or unmatched eventual text cannot substitute.

Harbor computes and can falsify the first claim and the internal audit-mapping contract. Harbor cannot establish that an external audit will meet the contract or that reports were historically visible.

## 3. Frozen audit denominator

For each test year `a`, admissible world `omega`, primary cutoff `c_24`, and singleton deletion state `j` (including undeleted `j=none`), define:

- `E_{a,omega,j}`: all eligible patients after the frozen parent population logic and, when applicable, deletion of patient `j`.
- `U_{p,a,omega,j}`: every nonblank, source-eligible CT/MRI examination unit on `u=(patient master index,encounter number,examination number)` that the locked pipeline is permitted to read for patient `p`, whose entire acquisition interval is in `[c_24-90d,c_24)`. All exact-deduplicated source rows sharing the key are one unit.
- `A_{a,omega,j}`: units in the union of `U_p` that pass the parent's reversible clean-source/releasable gate. Blank `Examination Number`, non-CT/MRI units, out-of-window units, corrupt/nonreversible/contaminated units, and units never consumed by the locked pipeline are not denominator members. They remain on the ledger with exclusion reason; they may not inflate coverage.
- `n_p=|A_p|`: the number of releasable units per eligible patient.
- `P^0={p in E:n_p=0}`: eligible patients with no releasable clean unit.
- `P^+={p in E:n_p>0}`: eligible patients represented in the accession denominator.

For an operational pattern `r`, accession coverage is
`C_A(r)=sum_{u in A} r_u/|A|` when `|A|>0`.
Patient-at-least-one coverage and patient-complete coverage are reported diagnostics:
`C_Pany=|{p in E:sum_{u in A_p}r_u>0}|/|E|` and
`C_Pall=|{p in E:n_p>0 and sum r_u=n_p}|/|E|`.
Patients in `P^0` remain in the patient denominator and can never count as covered. Neither patient metric may be substituted for `C_A` in the confirmatory hypothesis.

If `|A|=0` in any required world, the frontier is undefined and the experiment is inconclusive. The external audit denominator is the exact hashed `A_{a,omega,j}`, not all radiology records, all hospital reports, one accession per patient, or the intersection of convenient worlds.

The primary release family remains
`sum_{u in A} r_u >= ceil(c |A|)`.
The same `r_u` applies to all four arms, all three contrasts, the globally selected reader-book pair, and paired undeleted/deleted computations. Whole-accession `r_u=0` replaces every body-derived `S,Q,X_clean` block by its training-defined operational-unavailable block in `R_clean` and `G_clean` and applies the identical surface/availability mask to `Gclean_mask`; `B` and acquisition-only facts are unchanged.

This clarification does not weaken the parent: the attained bounds still range over every admissible placement of unavailable accessions, without independence, exchangeability, missing-at-random, or favorable patient-distribution assumptions.

## 4. Frontier computation, singleton stability, and uncertainty families

Let `C` be the sorted union of exact breakpoints `m/|A_{a,omega,j}|` across both test years, all admissible worlds, undeleted and every singleton-deleted ledger, plus zero and one. For each `c`, year, contrast and deletion state, compute exact attained lower and upper capture-margin endpoints over:

1. one coherent source/population/clock state per patient;
2. one corpus-wide radiology book and one corpus-wide pathology book from the fixed nine pairs;
3. one indivisible pathology membership/grade terminal per patient;
4. every whole-accession release vector satisfying the denominator constraint.

These are distinct finite uncertainty families. Release bits do not become report-time evidence and receive no probabilities. Books cannot switch by patient, year, release pattern, arm, capacity, or deletion. The population/clock world determines the denominator before release optimization. Outcome nonmembership is never recoded as `Y=0`.

After deleting patient `j`, remove that whole patient, all of their units, and all of their outcomes from both years and all arms. Do not refit, retune, recalibrate, rebuild temporal roles, change books, change `N_ref`, or lower `K`. Recompute only the explicitly defined denominator `A_{a,omega,j}` and `ceil(c|A|)`; require the parent's sharp post-deletion `N>=K` gate.

Define `c_A*` exactly as in the parent: the smallest breakpoint for which every undeleted and singleton lower endpoint for all three contrasts in both 2020 and 2021 is strictly greater than five. All-content failure prohibits reporting a rescuing `c_A*`. Emit all attaining witnesses and the last failing breakpoint. The 12/48/72-hour and `K_.05/K_.20` analyses are diagnostics only.

Computational gates remain zero integer gap, numerical feasibility and transformed-loss residual at most `1e-8`, no violated ranking inversion, raw/quotient replay, all tied maximizers, brute-force agreement on synthetic fixtures through 12 patients and real-data shards through 20, and no state cap or sampled release pattern.

## 5. Exact external finalization/release/view mapping

A later audit must be accession-linked and version-linked. For every frozen denominator unit it must supply, at minimum:

- exact source-system accession key crosswalk to `(Patient Master Index,Encounter Number,Examination Number)`, with audited collision/orphan rates;
- modality and component roster;
- every report version identifier and immutable report-body hash;
- authored, signed/finalized, released, amended, and preferably authenticated clinician-view timestamps, with timezone and timestamp semantics;
- the source system and event type generating each timestamp;
- whether the body available at the event exactly matches the frozen whole-accession body consumed by the locked model.

At cutoff `c_d`, define separate bits:

- `r_u^F=1` only if the complete matching whole-accession version was finalized no later than `c_d`;
- `r_u^R=1` only if it was released into the clinically relevant system no later than `c_d`;
- `r_u^V=1` only if an eligible clinical viewer event occurred no later than `c_d`.

Missing, impossible, or ambiguous event semantics map to zero in the lower-bound analysis. Acquisition `start time` never substitutes. If source rows/components for one accession do not all map to the same complete pre-cutoff version, its whole-unit bit is zero. If the pre-cutoff body differs from the eventual frozen body, the parent score cannot be credited: the different body must be frozen, parsed, independently read under the same form protocol, and rescored as a new prespecified audit study.

The audit must reproduce `A_{a,omega,none}` separately for every admissible 2020 and 2021 primary-cutoff world and report the minimum coverage over worlds. It must also report exact numerator/denominator counts by year and modality, `|P^0|`, `n_p` distribution, `C_Pany`, and `C_Pall`. Pooled years, pooled modalities, or patient percentages do not satisfy an accession threshold.

A census of the frozen ledgers yields exact finite-corpus coverage. If only a sample is audited, it must have a defined sampling frame and inclusion probabilities, treat the patient as the dependence cluster, and provide a prespecified simultaneous one-sided lower confidence bound over years, modalities, event types `F/R/V`, and all admissible primary worlds. An accession-binomial interval that assumes independent accessions is invalid. Exact clustering/inference requires external statistical review because no audit sampling frame exists in Harbor.

The stored-content frontier can support report-finalization potential only if the simultaneous `F` bound clears `c_A*`; a release-to-worklist claim requires `R`; actual clinician-access language requires `V`. Finalization cannot stand in for release or view. Even a clearing audit supports only prospective silent-mode consideration after clinical capacity review, not deployment or patient benefit.

## 6. Outcomes and falsification

The one-hot parent result labels are retained, with an added audit-bridge status:

1. **inconclusive**: any source/header/hash, roster/form/book, chronology, leakage, population, `N/K`, event/anchoring, fit, replay, denominator-ledger, or exact-optimization gate fails.
2. **visibility-robust comparator-closed supportive**: all parent all-content and singleton gates pass, `c_A*` exists, and `c_A*<=0.80`.
3. **all-content supportive but visibility-brittle**: all-content gates pass but `c_A*>0.80` or is undefined because a permitted release pattern fails.
4. **semantic-evidence-only**, **policy-only**, or **falsified-localized**: exactly the parent's comparator-localized rules.
5. **external audit unmappable**: reserved for a later audit that lacks the exact world-specific accession denominator, matching report versions, valid whole-unit event bits, or dependence-aware uncertainty. It is not evidence against stored-content value.
6. **external operational criterion cleared**: reserved for a later audit whose simultaneous accession-level lower bound for the claimed event type meets `c_A*` in every primary world. This still is not a benefit or deployment conclusion.

Support means only that the frozen eventual-report ranking retained the strict documentary-M2 capture margin under all declared worlds and all whole-accession unavailability placements once the stated accession fraction was exposed. Brittle/adverse results do not prove imaging semantics are useless or reports are late. Inconclusive and unmappable audits are not adverse evidence.

The verifier must reject: patient denominators substituted for accession denominators; denominator restriction to patients with visible reports; non-CT/MRI or never-consumed accessions used to inflate coverage; one row counted as one report; one accession sampled per patient; independent-accession confidence intervals; pooled years/worlds/modalities; finalization called view; acquisition called release; unmatched later report versions credited before cutoff; partial accession components exposed; a different `r` across arms; denominator changes after seeing outcomes; sensitivity-cutoff rescue; partial-release rescue after all-content failure; equality at five; and correct arithmetic followed by unsupported deployment, biological-M2, treatment, recurrence, survival, harm, cost, or benefit claims.

## 7. Exact data bindings

All source files are read-only ordinary CSV files, archive member none. Controlling catalog:
`[internal dataset path]`;
[source checksum].
HCC snapshot:
`[source checksum]`.

The parent's full exact binding table is inherited. The fields central to this repair are:

| Table | Source path | Required columns / role |
|---|---|---|
| examinations | `[internal dataset path]` | `Patient Master Index,Encounter Number,Examination Number` unit and join; `Examination` frozen CT/MRI classification; `Examination Findings,Examination Diagnosis` complete body; `Start Time` acquisition only; `Machine Model` provenance. No report final/release/view/version field exists. |
| procedures | `[internal dataset path]` | keys; `surgery,start time,end time,surgery source` episode and cutoff states. |
| encounters | `[internal dataset path]` | keys; `Age,Sex`; `Encounter Time,Admission Time,Discharge Time` chronology audit. |
| pathology | `[internal dataset path]` | keys; `Pathology, Examination Findings, Examination Diagnosis, Machine Model`; no time, specimen, or accession. |
| medications | `[internal dataset path]` | keys; `Medication,Drug Type,Start Time,End Time` prior recorded systemic treatment. |
| orders | `[internal dataset path]` | keys; `orders (non-drug), order time, start time, end time, order status` prior local/radiotherapy evidence. |
| diagnoses | `[internal dataset path]` | keys; `diagnosis name,diagnosis type` untimed corroboration only. |
| labs | `[internal dataset path]` | keys; `test,qualitative result,quantitative result,specimen type,test time` forbidden-predictor lineage audit only. |
| clinical_documents | `[internal dataset path]` | keys and narratives audit only; duplicate raw `admission diagnosis` header and no document time. |
| vitals / transfers / front_page | exact paths in parent and HCC README | identifier-only, no predictor or report-audit role. |

Same-encounter joins are exact on `(patient master index,encounter number)`; report grouping adds nonblank `examination number`. Patient-wide prior-treatment retrieval joins on `patient master index` before interval filtering. Preserve raw ordinal, exact bytes, hashes, and backpointers. Never use direct identifiers as predictors or export clinical rows.

Required new artifacts:

- `derived/audit_denominator_ledger.parquet`: year, cutoff, world, deletion hash, patient hash, accession hash, modality, component hashes/backpointers, inclusion/exclusion reason, source-clean/releasable status, and `n_p/P0/P+` tags.
- `derived/audit_denominator_summary.parquet`: every world/year/deletion denominator, patient/accession/component counts, multi-accession distribution, and modality counts.
- `derived/audit_bridge_contract.json`: `c_A*`, exact required ledger hashes, event-bit definitions, external columns, multiplicity family, and permitted conclusion strings.
- the parent's release ledger, frontier, witnesses, requirement JSON, models, rosters, forms, books, states, ranks, singleton witnesses, and certificates.

## 8. Claim boundary and clinical importance

The advance is a valid decision bridge, not a new predictor. It makes the result actionable as an evidence-acquisition target: a hospital can know exactly which accession/version/timestamp audit would warrant a prospective silent-mode study and which commonly reported coverage numbers cannot do so.

Computationally checkable now: exact HCC bindings, whole-accession grouping, source-clean denominator membership, patient/accession/component counts, world/cutoff/deletion ledgers, release masks, fixed models and K, rank replay, exact extrema, singleton stability, `c_A*`, and conclusion-output links.

Not checkable now: actual finalization/release/view timestamps, pre-cutoff report versions, audit crosswalk completeness, Chinese semantic truth, reader qualifications beyond records, operative completion, specimen linkage/sampling and biological M2, actual capacity, clinician action, future/site/unseen-reader transport, treatment effect, recurrence, survival, harms, costs, fairness, or patient benefit.

Biological M2 requires timed specimen/accession/slide/block linkage and sampling review. Operational availability requires the external version/final/release/view audit above. Capacity requires prospective flow and workload evidence. Patient benefit requires a controlled outcome study.

The research-ambition README was inspected. It states that the natural-history and Bayesian demonstrations have full local articles and supplements, while the Cell cancer main article and full STAR Methods remain unavailable. This targeted repair did not rely on or claim inspection of any unavailable paper text.
