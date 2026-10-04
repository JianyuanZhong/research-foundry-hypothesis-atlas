> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Patient-sufficiency 80/80 stress test for documentary-M2 review

## Targeted successor and the unresolved clinical question

This two-parent successor evolves assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It preserves their mature HCC design: the adult first-eligible source-documented resection frame; coherent operation-clock, imaging-window and prior-treatment source worlds; possibility-based temporal quarantine; encounter-documentary M2 rather than biological MVI; whole-accession radiology units and indivisible same-encounter pathology composites; six frozen reader books and nine global radiology-by-pathology pairs; locked patient-balanced B/R/G/same-fit-Gmask models; fixed absolute K; three comparator-closed contrasts; a strict margin of more than five additional documentary-M2 captures per 100 review positions; exact attained extrema; and anchored whole-patient singleton deletion.

The remaining problem is clinically substantive. The primary parent's equal-threshold patient-reach gate is redundant because mean within-patient report completeness can never exceed any-report reach. Its mean-completeness rule can also pass when availability is concentrated in a clinically awkward pattern. The second parent's complete-packet rule fixes concentration but requires every eligible report unit for four fifths of patients, even though the locked model explicitly has an unavailable-input state and may remain robust with a small amount of missing content. These rules answer different questions and can drive opposite evidence-investment decisions.

The replacement is a literal patient-sufficiency contract:

> In each of 2020 and 2021, in every coherent source/pathology/reader world and under every version-faithful stored-content mask for which at least 80% of the complete eligible patient roster has at least 80% of its eligible CT/MRI report units exposed, do all G-versus-B, G-versus-R and G-versus-same-fit-Gmask fixed-K documentary-M2 capture margins remain strictly greater than five, both before deletion and after anchored removal of any one test patient?

For a patient with `n_i` eligible units, “80% sufficient” means at least `ceil(0.8 n_i)` whole units. Thus one to four units must all be present; four of five are sufficient. No report fragment is exposed. A margin equal to five fails. An empty 80/80 mask family does not pass.

This is an exact counterfactual stored-corpus stress test. It asks whether a modest, explicitly distributed degree of missing report content can overturn a fixed-capacity documentary-ranking result. It does not assert that any report was finalized, readable or viewed before surgery; recommend treatment; or test recurrence, survival, safety, workload or patient benefit.

## What evidence supports now, what remains unresolved, and why it matters

The strongest currently supported claim is structural. I inspected `inputs.json`, the research-ambition availability README, the HCC guide and metadata, the relevant table schemas, and the actual headers of all 12 HCC CSVs. Snapshot `[source checksum]` contains patient/encounter-linked procedure rows, CT/MRI examination rows with an acquisition-like start, accession-like `examination number`, eventual narrative fields, and untimed same-encounter pathology narrative. It does not contain radiology report authorship, version, finalization, release, amendment, retraction, ingestion, service-readability or view time; raw images; pathology time, specimen identity, slides, blocks or sampling adequacy; real multidisciplinary-review capacity; recurrence; survival; response; harm; cost; or benefit.

The episode-66 no-sampling audit (job `[research job]`; output [source checksum]) read all 419,996 examination rows, found 419,986 exact-unique rows and 392,854 nonblank patient-encounter-accession units among 42,205 patients, with 39,610 patients having multiple units and a maximum of 205. Its broad text-bearing CT/MR lexical screen is explicitly unvalidated and will not define modality, population or eligibility. The verified source-grain counts establish that the distribution of report units across patients is not a theoretical detail: accession-weighted, mean-fraction, patient-sufficiency and complete-packet availability can differ.

Feng, Qu and Han's 2026 systematic review and meta-analysis (DOI `10.2196/82000`, PMCID `PMC12954728`) was inspected from full-text XML source `[source checksum]`, [source checksum]. It included 52 imaging deep-learning studies and 19,531 patients; reported pooled sensitivity 0.80, specificity 0.82 and SROC 0.88; and found lower SROC in external than internal validation (0.85 versus 0.90), motivating prospective multicenter evaluation. Neves and Soares' 2026 review (DOI `10.3390/cancers18132028`, PMCID `PMC13360217`) was inspected from full-text XML source `[source checksum]`, [source checksum]. It found 35 of 36 studies retrospective, 27 of 36 single-center, only 6 externally validated, with inconsistent calibration and clinical-utility evaluation. These reviews support the importance of disciplined preoperative study and the weakness of discrimination-only evidence. They do not validate this dataset's documentary-M2 label, semantics, 80/80 criterion, fixed K or any clinical benefit.

The unresolved claim is whether report semantics retain a clinically material fixed-quota documentary-capture advantage when missingness is constrained at the patient level rather than averaged across accessions or forced to complete packets. The substantive advance is a distribution-sensitive availability estimand: it prevents a few complete patients from compensating for many poorly supplied patients, yet does not declare a patient unusable after one missing unit when the model may be robust to that omission. A supportive HCC result would justify the next, cheaper evidence step—acquiring the report-version/readability census—before considering a prospective silent-mode workflow study. It would not justify deployment.

## Population, temporal boundaries and source uncertainty

For each cutoff offset d, retain at most one state-specific episode per patient:

1. age at least 18 at the index encounter;
2. earliest eligible source-documented liver resection under the frozen high-sensitivity hepatobiliary procedure dictionary;
3. same-encounter indivisible pathology composite supporting the HCC frame under the selected pathology book and terminal;
4. no recorded qualifying prior HCC resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in `[c_d-365d,c_d)`.

The primary analytical cutoff is `c_d=t_op-24h`; d=12, 48 and 72 hours are locked diagnostics. A CT/MRI accession is eligible only when its acquisition interval lies wholly in `[c_d-90d,c_d)`. Acquisition is not report availability or view. “No recorded prior treatment” is not biological treatment-naivety.

Exact-deduplicate procedure rows on all six source fields while retaining raw ordinal. Link provisional same-patient, same-encounter, same-calendar-day candidates. A validated nonmidnight anesthesia-system start may be a point clock; an unvalidated midnight/date-like case-record start remains `[date,date+24h)`. Missing or competing operation clocks, episode identity, year, imaging-window membership and prior-treatment membership remain coherent finite branches, proved impossibilities or adjudication-only exclusions retained in the outer universe. Retrieve treatment history patient-wide before interval filtering. Nonmembership is never recoded as Y=0.

Before outcomes, reader forms, fitting or test inspection, possibility-quarantine any patient eligible in any 2020/2021 state into `U_T`; among the remainder, any possible 2019 patient into `U_V`; among the remainder, any possible 2015–2018 patient into `U_D`. Develop in 2015–2018, tune and seal in 2019, and test 2020 and 2021 separately. Rows from 2022 onward are audit-only. The inaccessible catalog-reserved partition is not external validation.

## Whole source objects, readers and documentary outcome

A nonblank radiology unit is `u=(Patient Master Index,Encounter Number,Examination Number)` and contains every exact-deduplicated component row in original order with immutable byte, field and raw-row backpointers. A reversible parser separates visible text, markup/attributes and parse errors. Semantic spans may arise only from reversible visible bytes. Nonreversibility, treatment/pathology/specimen/MVI-grade contamination or unresolved context makes the whole unit semantic-source-unavailable; no phrase is selectively removed and no patient is dropped.

For the sufficiency denominator only, each eligible exact-deduplicated CT/MRI row with blank `examination number` becomes a forced-zero pseudo-unit `u0=(patient master index,encounter number,raw_ordinal)`. It supplies no semantics and cannot be merged by text similarity. This prevents an additional uncrosswalkable report row from disappearing from a patient's denominator.

A pathology object serializes every exact-deduplicated same-encounter `Pathology/Examination Findings/Examination Diagnosis` field in row and field order. It remains one indivisible documentary composite because the source has no pathology time or specimen identifier.

Before outcomes or scores are exposed, two qualified Chinese-reading abdominal radiologists plus one complete adjudicator read the complete radiology roster, and two qualified Chinese-reading hepatobiliary pathologists plus one complete adjudicator read the complete pathology roster. Freeze radiology books R1/R2/RA and pathology books P1/P2/PA. Exactly nine global book pairs apply corpus-wide; patient-, item-, year-, model-, outcome-, mask- or deletion-specific reader switching is forbidden.

Radiology forms retain the inherited lesion burden, capsule, margin, enhancement/washout, peritumoral features, satellites, venous tumor thrombus, cirrhosis and ascites concepts with uncertain, not-mentioned and source-unavailable terminals. Pathology terminals remain `OUT, IN0-A, IN1-A, IN0-U, IN1-U`; IN1 is encounter-documentary M2 and OUT has no outcome. Computation cannot establish dictionary validity, reader qualification, Chinese semantic truth, operation identity, specimen linkage, sampling adequacy or biological MVI.

## Locked models, baselines, K and outcome

Preserve the four information sets:

- `B(Z)`: independently optimized acquisition-only comparator;
- `R_clean(Z,S,Q)`: independently optimized nonsemantic report-surface/availability comparator;
- `G_clean(Z,S,Q,X_clean)`: independently optimized full semantic model;
- `Gclean_mask`: the same fitted G with every semantic block replaced by its training-defined unavailable value, without refitting, recalibration or threshold change.

Z contains only age, sex, acquisition modality, eligible-unit count and recency, component/accession ambiguity and development-grouped machine. S contains raw/canonical/markup surface quantities, Q reason-free whole-block availability, and X_clean only frozen-reader semantic concepts. Outcomes, pathology, reader identity or agreement, unrestricted text/tokens, identifiers/hashes, annotation times, uncertainty width, labs, interactions, splines and test-derived features are forbidden.

Use the inherited additive logistic family, unpenalized intercept, one patient-balanced outcome-blind preprocessing map over the complete outer development ledger, byte-identical shared columns and certified penalty grids. Fit one minimax coefficient vector per information set over all coherent source/terminal states and nine reader pairs. Tune each model independently on 2019 worst-state fixed-K performance, then seal all test outcomes.

Let `N_ref=min N_a(omega,d)` over 2015–2019, all four offsets and admissible worlds. Set `K_rho=floor(rho*N_ref)` for rho=.05,.10,.20; K_.10 is confirmatory. Require N_ref>=500, K_.05>=25, K_.10>=50 and K_.20>=100. Every test world requires N>=K+1, anchored-grade fraction >=.85 and at least 50 Y=1 events. K is a frozen retrospective quota, not observed service capacity.

For model M, year a and world omega,
`T_M=100/K * sum_i(Y_i * 1[i is in exact top-K_M])`.
The six confirmatory coordinates are `Delta_R=T_G-T_R`, `Delta_B=T_G-T_B` and `Delta_mask=T_G-T_Gmask` in each test year. Every required lower endpoint must be strictly greater than five.

## Exact patient-sufficiency availability

For every eligible nonblank accession, freeze

`H_HCC(u)=SHA256(schema_version || parser_version || length-delimited ordered tuples(source_row_ordinal,field_name,exact_raw_bytes,V/A/E_lineage))`

over all exact-deduplicated `Examination Findings` and `Examination Diagnosis` components. This commits to component count and order, field and empty boundaries, parser lineage and exact bytes. Similar wording, impression-only equality, edit distance, equal score or reader judgment cannot substitute.

For the HCC-computable stored-content experiment, binary `r_u=1` exposes that exact whole eventual report input; `r_u=0` replaces every body-derived S/Q/X block in R, G and Gmask by its development-defined unavailable block. B and acquisition-only Z stay fixed. Blank, nonreversible, contaminated and adjudicated source-unavailable units have `r_u=0` forced. Other r bits are counterfactual stress-test choices, not observations of historical availability.

For a full test-year world omega, let I be the complete eligible patient roster, N its size, E_i all temporally eligible CT/MRI units before semantic filtering, and n_i=|E_i|. Zero-unit patients remain in N.

Let `m_i=sum_{u in E_i} r_u`, `k_i=ceil(4 n_i/5)`, and

`s_i(r)=1` iff `n_i>0` and `m_i>=k_i`.

Primary patient-sufficiency coverage is
`C_80(r,omega)=sum_i s_i/N`.

The confirmatory family is
`R_80/80(omega)={r: 5*sum_i s_i >= 4N}`.

Thus at least four fifths of all eligible patients—not report-bearing patients—must each have at least four fifths of their own whole report units. Patients with no unit or insufficient units contribute zero. If the family is empty in any required world, structural 80/80 sufficiency is infeasible and cannot pass vacuously.

Mandatory diagnostics on the identical worlds and masks are:

- `C_any`: fraction of all patients with at least one exposed unit;
- `C_frac`: mean within-patient exposed fraction over the complete roster;
- `C_all`: fraction with every eligible unit exposed;
- `C_A`: legacy accession-weighted exposure.

Always verify `C_all<=C_80<=C_any`; no fixed ordering is asserted between C_80 and C_frac. Report counterexamples in both directions. None of these diagnostics may replace the primary estimand.

For whole-patient deletion j, remove j and all its states, outcomes and units, then restrict the same qualifying full-roster mask to survivors. Do not requalify the mask, recompute n_i or K, expose a replacement report, refit, recalibrate, alter books/worlds/ties or change any survivor's bit or feature hash. Require N-1>=K. Survivor-denominator coverage is descriptive only.

## Exact analysis, uncertainty and falsification

Compile finite patient domains carrying membership, year, Y, Z/S/Q/X, unit sets and hashes, source/form/terminal hashes, locked scores, ties and raw backpointers. For n_i>0 encode the sufficiency indicator exactly with `k_i=ceil(4n_i/5)`:

- `m_i >= k_i*s_i`;
- `m_i <= (k_i-1)+n_i*s_i`.

Set s_i=0 when n_i=0. The roster gate is exact integer arithmetic `5 sum_i s_i >= 4N`.

For each year, world, global reader pair, contrast and deletion, exact MIP or certified equivalent must search all coherent states and all masks in R_80/80. Comparator arms share the same world and mask. A failure witness satisfies
`20*(captures_G-captures_comparator)<=K`.
Return attained raw-row witnesses for every extremum.

Define Q as all source/header/hash, chronology, roster, event/K, reader-record, leakage, fit, mask-invariance, exact-solver, replay and predicate-consistency gates passing. Define A as R_80/80 nonempty in every required world; F as any attained qualifying undeleted or anchored-deletion witness with a required margin <=5; and Fmax as such a failure under the unique all-exposable-content mask. Under A, Fmax must imply F or Q is false.

Emit exactly one primary label:

1. `inconclusive` if not Q;
2. `patient-sufficiency infeasible` if Q and not A;
3. `patient-sufficiency robust supportive` if Q and A and not F;
4. `maximum-content non-supportive` if Q and A and F and Fmax;
5. `patient-sufficiency visibility-brittle` if Q and A and F and not Fmax.

These labels are exhaustive and disjoint. Compute `b_80=max C_80` over every attained failing witness, or NONE if no failure; when Q and A, support must agree with `b_80<.80` or NONE. Also report which year, comparator, reader pair, source world, patient deletion and exact mask first fail. Comparator-specific patterns and whether C_frac or C_all would change the decision are secondary, intentionally nonexclusive flags.

Require zero integer gap, exact rational replay, numerical residual <=1e-8, complete rank-inversion constraints, all tied maximizers, forward/reverse raw-state reachability, lossless quotient replay and brute-force agreement on synthetic fixtures through 12 patients and real shards through 20. Timeout, state cap, sampled masks, favorable incumbent, omitted world/book/deletion, missing witness, changed survivor feature, rational-scaling loss or failed replay makes Q false.

The uncertainty statement is exact and bounded: source ambiguity, global reader variation, every qualifying missing-content placement and every one-patient deletion are propagated jointly. The result describes this frozen finite corpus. It is not a confidence statement about a target population. Bootstrap summaries, if reported, are diagnostics and cannot alter the exact label.

Falsification occurs if the 80/80 family is structurally unattainable, if any qualifying mask/world/book/deletion has a margin <=5, or if exact computation fails to certify the universal claim. “Maximum-content non-supportive” is the strongest adverse result: a required margin fails even when every exposable stored unit is present. “Visibility-brittle” means maximum content passes but allowed distributed missingness creates a failure. Neither proves radiology semantics useless or harmful generally.

## Exact source bindings and required data

Controlling catalog: `[internal dataset path]`, [source checksum]. All HCC sources are read-only ordinary CSVs; archive member is none.

| Table | Exact source path | Required columns and role |
|---|---|---|
| encounters | `[internal dataset path]` | `patient master index,encounter number` joins; `age,sex` Z; `encounter time,admission time,discharge time` audit |
| procedures | `[internal dataset path]` | keys; `surgery, start time, end time, surgery source` episode, clock and prior-operation evidence |
| examinations | `[internal dataset path]` | keys; `examination number` accession and blank-unit audit; `examination` modality; `examination findings, examination diagnosis` S/Q/X and exact hash; `start time` acquisition only; `machine model` Z/provenance |
| pathology | `[internal dataset path]` | keys; `pathology, examination findings, examination diagnosis` HCC frame/documentary-M2 composite; `machine model` provenance; no time/specimen |
| medications | `[internal dataset path]` | keys; `Medication,Drug Type,Start Time,End Time` prior systemic-treatment evidence |
| orders | `[internal dataset path]` | keys; `Orders (non-drug), order time, start time, end time, order status` prior local/radiotherapy evidence |
| diagnoses | `[internal dataset path]` | keys; `Diagnosis Name, Diagnosis Type` untimed corroboration only |
| labs | `[internal dataset path]` | keys; `test,qualitative result,quantitative result,specimen type,test time` forbidden-predictor audit only |
| clinical_documents | `[internal dataset path]` | keys and narratives for leakage audit only; no usable document time |
| vitals | `[internal dataset path]` | identifier-only keys |
| transfers | `[internal dataset path]` | identifier-only keys |
| front_page | `[internal dataset path]` | 30-byte identifier-only header |

Same-encounter joins are exact on `(Patient Master Index,Encounter Number)`; examination grouping adds `Examination Number`. Patient-wide history joins on `Patient Master Index` before time filtering. Preserve raw ordinal, exact bytes/hash and backpointer. Direct identifiers, post-cutoff content, laboratory values, untimed diagnoses/documents and identifier-only tables are forbidden predictors.

MIMIC, eICU and UKB remain directly readable through their configured guides and catalog paths. They are not pooled because there is no patient crosswalk or compatible first-resection, eventual-Chinese-report, untimed-pathology documentary-M2 frame.

## Missing evidence and operational bridge

The automatic HCC experiment can test stored-content robustness because each free r bit exposes an exact eventual source object. It cannot determine historical or deployable availability. Any operational bridge requires a complete same-snapshot accession/version census with protected `Examination ID` crosswalk; all version IDs and predecessors; exact full pipeline-input hashes; authored, final, release, amendment, retraction and ingestion times; intended-service readability; validated operation clocks; and the same complete patient/accession denominator. Clinician-view timestamps are additionally required to claim that a clinician saw content.

The bridge must classify every unit as exact-precutoff-readable, proven absent, or unresolved and replay the observed mask. Missing archive evidence is unknown, not zero. Until census completeness and hash crosswalk pass, emit `operational_80_80_status=not_estimable_from_HCC`; do not relabel this as structural infeasibility. Actual review slots, reviewer-hours, duration, abandonment, completion, clinician action, treatment, recurrence, survival, harms, cost and benefit require workflow data, expert/stakeholder review, an external cohort or another study.

## Outputs and verifier contract

Publish:

- `derived/source_and_filter_manifest.json`: source hashes, headers, all filters and actual counts by exclusion/state;
- `derived/patient_state_ledger.parquet`: raw branches, reachability, chronology and role;
- `derived/report_unit_ledger.parquet`: patient/encounter/accession or blank pseudo-unit, n_i, k_i, forced-zero reason, exact hash and backpointers;
- frozen reader books, preprocessing maps, fit hashes, K, scores, ranks and ties;
- `derived/patient_sufficiency_extrema.parquet`: every year/contrast/world/book/deletion endpoint, C_80/C_any/C_frac/C_all/C_A, witness and solver certificate;
- `derived/patient_sufficiency_requirement.json`: Q/A/F/Fmax, b_80, exact one-hot label and permitted conclusion;
- `derived/mask_invariance_audit.parquet`: each survivor's original/deleted bit and feature hash;
- `derived/operational_bridge_certificate.json`: required external fields, census/hash checks and fail-closed status.

Fixtures must include: all patients at 80% but none complete; 80% complete and 20% empty; high mean completeness with fewer than 80% patient-sufficient; patient-sufficiency pass with complete-packet failure; zero-unit, blank and source-unavailable patients retained; a full-roster qualifying mask that would qualify only after forbidden deletion reweighting; and correct supportive, maximum-content non-supportive, visibility-brittle, infeasible and inconclusive outputs.

The automatic verifier can check hashes/headers, joins, clocks/windows, state reachability, reader coupling, forbidden-feature absence, fits/K/ties, whole-unit masks, exact ceil thresholds, full-roster qualification, deletion invariance, extrema arithmetic, b_80 agreement, one-hot logic and conclusion-to-output linkage. It must accept appropriate supportive, adverse and inconclusive interpretations, and reject correct arithmetic followed by claims of report timeliness, biological MVI, real capacity, deployment, treatment effect, recurrence, survival, safety, fairness, transportability or benefit.

No automatic verifier can establish clinical dictionaries, reader qualifications, Chinese semantics, specimen linkage/sampling, biological MVI, archive completeness, actual report release/readability/view, workflow acceptability, clinician action, treatment effects or patient benefit. Reference execution establishes computational feasibility and whether conclusions follow from computed outputs, not scientific truth.

The research-ambition README was inspected. It reports full article material for the natural-history and Bayesian demonstrations but not the Cell cancer main article or full STAR Methods. No demonstration paper is used as evidence here, and no unavailable paper text is claimed inspected.
