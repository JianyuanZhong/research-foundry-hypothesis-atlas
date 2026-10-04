> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Patient-balanced coverage frontier with non-overlapping decision outcomes for documentary-M2 review

## Clinical question and falsifiable hypothesis

Among adults undergoing a first source-documented HCC liver resection, can semantic information in routine preoperative CT/MRI report bodies improve allocation of a fixed number of retrospective review positions for pathology-documented high-grade microvascular invasion (M2), and is that improvement robust to plausible report visibility?

The action represented is allocation of a scarce review position. It is not a recommendation about resection extent, transplantation, neoadjuvant/adjuvant treatment, locoregional/systemic treatment, surveillance, or any other care.

The latest valid parent used a patient-balanced effective-visibility threshold of 0.80. This successor preserves that clinically interpretable denominator but repairs two linked weaknesses. First, a mean patient coverage can hide a completely unserved subgroup: 80% of patients may be fully visible while 20% have no usable report. Second, the parent's “one-hot” result list allowed an accession-only artifact, semantic-only evidence, quota-policy-only evidence, and visibility brittleness to overlap. Those are diagnostics, not mutually exclusive conclusions.

The primary estimand is therefore a coverage frontier, with a prespecified policy point:
- For patient i, let p_i(r,omega) be the fraction of that patient's eligible nonblank CT/MRI accession units whose exact whole report input is visible under mask r in source world omega; patients with no eligible unit have p_i=0.
- Let C_mean=(1/N)sum_i p_i.
- Let C_tail(q) be the mean of the lowest qN patient visibility values, with q=.20 as a prespecified lower-tail diagnostic. It is reported in every world and mask; it is not silently substituted for C_mean.
- Define F_c as all full-roster masks with C_mean>=c. The primary policy point is c=.80, with locked sensitivity points .60,.70,.90, and 1.00. A mask must use identical bits for all model arms and all coupled outcomes in its world.
- The hypothesis is: in each locked test year (2020 and 2021), for every admissible source/pathology/reader world and every r in F_.80, all three semantic-content margins—G versus independently optimized acquisition-only B, G versus independently optimized nonsemantic surface comparator R, and G versus its same-fitted semantic mask Gmask—exceed 5 documentary-M2 captures per 100 fixed review positions, both before deletion and after restricting the same mask to survivors after deletion of any one whole test patient.
- Equality to 5 fails. If F_.80 is empty in any required world, the hypothesis is falsified as “coverage infeasible,” not passed. The frontier c* is the smallest grid point at which the conjunction holds for all higher attainable grid points; it is undefined if the conjunction never holds or later fails.

The C_tail curve prevents a supportive mean-coverage result from being described as equitable or patient-complete. It does not create an ungrounded fairness claim: age/sex are available but no social, site, socioeconomic, or protected-group sampling frame is available.

## Evidence boundary and substantive advance

The strongest available evidence is data availability, not clinical validity. The HCC snapshot contains patient/encounter-linked procedures, acquisition-like CT/MRI examination times, accession-like identifiers, eventual report narratives, and same-encounter pathology narratives. The full examination audit read all 419,996 rows and found 392,854 nonblank accession groups, 16,534 multirow groups, 66,534 patient-encounters with multiple accessions, and 39,610 patients with multiple accessions; duplicate components and accession multiplicity make an accession-weighted denominator clinically misleading. Direct source inspection shows no radiology authored/final/release/view time or immutable version, no pathology time/specimen/slide/block identifier or sampling protocol, no raw images/slides, no MDT capacity ledger, no clinician action, recurrence, survival, treatment response, harm, cost, or benefit.

Current literature supports the importance of MVI and the need for external validation but not this hypothesis. The inherited inspection of Feng, Qu, and Han (2026, DOI 10.2196/82000, PMCID PMC12954728) reports promising but heterogeneous imaging studies and lower performance in external than internal validation; its abstract/opening discussion call for prospective multicentre work. Current Europe PMC records also describe recent retrospective HCC MVI models with independent validation and explicitly retain prospective validation/recalibration as necessary. These sources do not validate the local documentary-M2 terminal, report semantics, 0.80 policy threshold, fixed K, or any clinical benefit.

The advance is a decision-aligned stress test between discrimination and operational feasibility: it asks whether a fixed-capacity semantic gain survives adversarial but patient-balanced loss of report availability, and whether the result is an all-patient coverage property or an artifact of many scans from a small number of patients. It produces a report-release/data-access acquisition target (c*) without pretending that the snapshot measures report release.

## Population, chronology, and outcomes

Use the parent’s frozen high-sensitivity hepatobiliary procedure dictionary. For each cutoff offset d, retain at most one state-specific episode per patient:
1. age >=18 at the index encounter;
2. earliest eligible source-documented liver resection;
3. same-encounter indivisible pathology composite supporting the HCC frame;
4. no recorded prior qualifying HCC resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in [t_op-365 days,t_op).

The primary cutoff is c_d=t_op-24 hours; 12, 48, and 72 hours are locked diagnostics. A CT/MRI accession is eligible only when its acquisition interval is wholly in [c_d-90 days,c_d). Acquisition is not report release or clinician view. Treatment absence means no recorded treatment, not biological treatment-naivety.

Reconstruct exact-deduplicated procedure candidates on all six source fields and retain raw ordinals. Use a validated non-midnight anesthesia-system start as a point; an unvalidated midnight/date-like case-record start is [date,date+24 hours). Missing/competing clocks, episode identity, calendar role, imaging membership, and prior-treatment membership remain coherent outer-envelope alternatives. Quarantine by possibility before inspecting outcomes: 2015–2018 development, 2019 lock/tuning, and separate 2020 and 2021 tests; 2022 onward is audit-only. The 80:20 catalog split is not external validation.

Radiology book pairs are the complete corpus-wide R1/R2/RA and P1/P2/PA reader books, exactly nine global pairs. Radiology forms encode predeclared lesion burden, capsule, margins, enhancement/washout, peritumoral features, satellites, venous tumor thrombus, cirrhosis, ascites, uncertain, not-mentioned, and source-unavailable terminals. Pathology terminals are OUT, IN0-A, IN1-A, IN0-U, IN1-U; IN1 is the encounter-documentary M2 terminal. All reader books, forms, pathology composites, and source alternatives are coupled; no item-, patient-, year-, arm-, or mask-specific reader switching is allowed.

## Information sets, models, and fixed-capacity outcome

Keep the parent’s locked additive logistic family, outcome-blind patient-balanced preprocessing, certified penalty grid, and minimax fit over all coherent source/terminal states and nine global book pairs:
- B(Z): independently optimized acquisition-only comparator;
- R_clean(Z,S,Q): independently optimized nonsemantic report-surface/availability comparator;
- G_clean(Z,S,Q,X_clean): independently optimized full semantic model;
- Gmask: the same fitted G with every semantic block replaced by its training-defined unavailable value, with no refit, recalibration, or threshold change.

Z contains only age, sex, CT/MRI acquisition, eligible-unit count/recency, component/accession ambiguity, and development-grouped machine. S contains raw/canonical/markup surface quantities. Q is reason-free whole-block source availability. X_clean contains only the frozen radiology meanings. Labs, unrestricted tokens, identifiers, hashes, reader agreement, annotation times, outcomes, pathology, state-width and test-derived features are excluded from predictors.

Set N_ref to the minimum eligible test-reference size over 2015–2019 development/lock states, four offsets, and admissible worlds. Use K_rho=floor(rho*N_ref), rho=.05,.10,.20; K_.10 is confirmatory. Require N_ref>=500, K_.05>=25, K_.10>=50, K_.20>=100. Each test world requires N>=K+1, anchored-grade fraction >=.85, and >=50 Y=1 events. K is a retrospective quota, not observed service capacity.

For model M in year a and world omega, T_M=100/K times the sum of Y among the exact frozen top K scores with hash-defined ties. The six confirmatory coordinates are Delta_B=T_G-T_B, Delta_R=T_G-T_R, and Delta_mask=T_G-T_Gmask in 2020 and 2021. Compute sharp lower/upper endpoints under the same world and the same r for both arms.

## Version-faithful visibility and patient-balanced frontier

For each temporally eligible nonblank accession u=(Patient master index,Encounter number,Examination number), preserve every exact-deduplicated component row in original order with raw-byte/field backpointers. Define
H_HCC(u)=SHA256(schema_version || parser_version || length-delimited ordered tuples(source_row_ordinal, field_name, exact raw bytes, V/A/E lineage)).
The bit r_u=1 exposes the complete eventual report input only in an external audit state where the exact version was finalized, retrievable pre-cutoff, uniquely crosswalked, and byte-identical to H_HCC(u). In the Harbor corpus, report version/release/view is unknown; r is a hypothetical mask for a stored-content robustness experiment. Preliminary/amended/retracted/unmatched/nonidentical versions are not visible. Source-unavailable or blank-accession units remain denominator units with forced r=0.

For each world, E_i is all eligible nonblank CT/MRI units for patient i and n_i=|E_i|. Let p_i=0 if n_i=0, otherwise p_i=(1/n_i)sum_{u in E_i}r_u. C_mean=N^-1 sum_i p_i. A patient with ten accessions therefore contributes one patient’s total mass, not ten patients’ mass. Compute C_tail(.20) from the ordered p_i values and report the full empirical distribution, minimum, 10th/20th/50th percentiles, and number with p_i=0. These are diagnostics of concentration; no “equity,” fairness, or service guarantee may be claimed.

For c in the locked grid, F_c(omega)={r:C_mean(r,omega)>=c}. Empty families fail closed. For every c, compute the minimum of each of the six margins over the same coherent omega and r. Recompute the old accession-weighted criterion only as a diagnostic; it cannot support the primary claim. Report CT-only, MRI-only, and dual-modality visibility descriptively, with modality event/roster gates.

Deletion is anchored: remove a whole test patient and all of that patient’s states, outcomes, and units; keep survivor bits, features, models, books, K, N_ref, c, and weights byte-identical. Do not reapply a quota or replace a deleted accession. Require N_after>=K; inability to define fixed K is inconclusive. Report every singleton witness and the exact multi-patient deletion radius only as a secondary non-monotone diagnostic.

## Exact computation

Compile patient domains carrying all source-world membership, year, Y, Z/S/Q/X, accession sets, p_i/C_mean/C_tail rational weights, score/tie hashes, book/terminal hashes, and raw backpointers. Use exact MIP or a certified equivalent to select one coherent state per patient and one full-roster mask. Encode C_mean with exact rational scaling, rank exactly K with complete inversion constraints, and use the same world/mask in every contrast. Preserve all tied maximizers.

Require zero integer gap, residual <=1e-8, complete rank replay, raw/quotient replay, exhaustive equality with brute force on fixtures through 12 patients and real shards through 20, and deletion mask invariance. No sampled masks, state caps, favorable incumbents, time-limited bounds, or unexplained branches may decide the hypothesis. Bootstrap is diagnostic only and cannot create population confidence intervals.

## Mutually exclusive conclusion protocol

First assign exactly one primary status after all gates:
1. **Inconclusive**: any source, schema, chronology, roster, annotation, leakage, event/N/K, fit, exact-weight, solver, replay, or mask-invariance gate fails.
2. **Coverage-infeasible**: gates pass but some required world has max C_mean<.80, so F_.80 is empty.
3. **All-content-adverse-or-heterogeneous**: F_.80 is nonempty but at least one all-content (r=1) coordinate is <=5 or its sharp interval crosses the margin without resolving universally; report whether the universal claim is adverse or heterogeneous.
4. **Visibility-brittle**: all six all-content lower endpoints are >5, but a feasible r with C_mean>=.80 makes at least one required undeleted or singleton lower endpoint <=5.
5. **Visibility-robust-supportive**: all gates pass, every required world has F_.80 nonempty, every all-content and every F_.80 undeleted/singleton lower endpoint is strictly >5, and the attained maximum-coverage failing mask is <.80 (equivalently no qualifying failing mask exists).

The first applicable status is the only primary conclusion. “Adverse” is reserved for a coordinate whose upper endpoint is <=5; threshold-crossing coordinates are heterogeneous/inconclusive within the prescribed finite-corpus logic and must not be called adverse. If multiple coordinate patterns exist, preserve them as secondary structured fields, never additional top-level labels.

After assigning the primary status, attach non-overlapping diagnostic flags:
- accession-only artifact: accession-weighted .80 passes while patient-balanced .80 does not;
- semantic-evidence-only: Delta_R and Delta_mask pass but Delta_B does not;
- quota-policy-only: Delta_B passes but a semantic contrast does not;
- concentration-risk: primary passes but C_tail(.20) or zero-visibility-patient audit shows concentration, without changing the primary status;
- singleton-fragile: undeleted primary passes but a singleton lower endpoint fails;
- frontier c* and all sensitivity-grid endpoints.

These flags are not alternative conclusions. A supportive status always means only a finite-corpus, eventual-report, documentary-M2 ranking property. A coverage-infeasible status does not prove reports were late; brittle does not prove semantics are useless; a negative semantic contrast does not establish no clinical utility outside this feature set.

## Exact HCC bindings

Controlling catalog: [internal dataset path], [source checksum]. HCC snapshot: [source checksum]. All HCC sources are read-only ordinary CSVs; archive member is none.

- encounters: [internal dataset path]; table datasets/hcc/table-b743286cb1249287.json. Join (patient master index, encounter number); required age, sex, encounter time, admission time, discharge time.
- procedures: [internal dataset path]; table datasets/hcc/table-d5eae16f8f8093d9.json. Join keys plus Surgery,start time,end time,surgery source.
- examinations: [internal dataset path]; table datasets/hcc/table-fd016d2731b9d6c6.json. Join keys plus Examination Number; required Examination, Examination Findings, Examination Diagnosis, Start Time, Machine Model, Examination Number.
- pathology: [internal dataset path]; table datasets/hcc/table-0a4ee86a446c605c.json. Join keys; required Pathology,Examination Findings,Examination Diagnosis,Machine Model. No pathology time/specimen/accession field exists.
- medications: [internal dataset path]; table datasets/hcc/table-4f6ecaeb6e8f69c2.json. Join keys; required Medication,Drug Type,Start Time,End Time.
- orders: [internal dataset path](non-medication)_2062526727266216118.csv; table datasets/hcc/table-6b93dcf0ea823702.json. Join keys; required Medical order (non-medication),Order time,Start time,End time,Order status.
- diagnoses: [internal dataset path]; table datasets/hcc/table-12710723c3df0c99.json. Join keys; diagnosis name, diagnosis type; untimed corroboration only.
- labs: [internal dataset path]; table datasets/hcc/table-38aad8c54471332f.json. Join keys; test, qualitative result, quantitative result, specimen type, test time. Excluded from predictors and used only for a zero-lab lineage audit.
- clinical_documents: [internal dataset path]; table datasets/hcc/table-66afca58512c2fca.json. Duplicate Admission Diagnosis header; narratives audit-only and no reliable document time.
- vitals: [internal dataset path]; table datasets/hcc/table-8436de9cba74b8ca.json. Identifier-only.
- transfers: [internal dataset path]; table datasets/hcc/table-320c20f732e71789.json. Identifier-only.
- front_page: [internal dataset path]; table datasets/hcc/table-38b3224239acc33f.json. Header-only (30 bytes) and identifiers only.

Same-encounter joins are exact on (patient master index,visit number); examination grouping adds examination number; prior-treatment searches join patient-wide on patient master index before interval filtering. Never coerce blank keys, normalize identifiers, or join direct identifiers. Preserve source ordinal, raw bytes/hashes, and backpointers.

MIMIC, eICU, and UKB remain directly accessible read-only under datasets/{mimic,eicu,ukb}/README.md and their catalogued files, but there is no crosswalk or compatible endpoint/estimand, so they are not pooled. This is a scientific exclusion, not an access limitation.

## Verification, limitations, and required stronger evidence

Verifier recomputes source/hash/schema agreement, complete rosters/forms/books, parser V/A/E, chronology, outer quarantine, model identities, masks, exact rational coverage, ranks, extrema, deletion integrity, c* and all primary/diagnostic labels. Fixtures must include: overlapping labels that now resolve by priority; empty F_.80; exact equality at 5; later-grid failure; one patient with ten accessions versus ten with one; 20% zero-visibility patients with C_mean=.80; changed survivor bits after deletion; omitted N<K world; all-content failure; semantic-only and quota-only diagnostics; and correct supportive, brittle, adverse/heterogeneous, and inconclusive prose.

Automatic verification can establish only finite-corpus computation and conclusion linkage. It cannot establish Chinese semantic correctness, reader qualifications or independence, renderer fidelity, operation completion, pathology specimen linkage/sampling adequacy, biological M2, pre-cutoff report release/view, actual capacity or clinician response, treatment effect, recurrence/survival, harm, cost, fairness, transportability, or patient benefit. Biological M2 requires timed specimen-linked pathology and sampling adjudication. Real-time utility requires accession-linked finalized/version/release/view logs and validated operative clocks. Deployment needs an unseen-reader/site and prospective silent-mode study; benefit needs a controlled clinical outcomes study.

All source rows/notes remain read-only. Sampling/filtering is none for source audit; the analysis uses exact-deduplication, the prespecified population/clock/pathology/parser rules, temporal quarantine, locked masks and fixed top-K ranking. Derived artifacts are ordinary workspace files only.
