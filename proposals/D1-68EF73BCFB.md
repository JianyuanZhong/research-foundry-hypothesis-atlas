> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Comparator-closed, capacity-localized whole-panel stability of clean report semantics for documentary-M2 capture

## 1. Assigned successor and the unresolved decision flaw

This is a substantive child of assessed-valid `[prior hypothesis]`. It preserves that candidate's first-eligible resection population, preoperative clocks and windows, documentary-M2 boundary, six immutable corpus-wide reader books and nine globally fixed radiology×pathology book pairs, coupled source states, frozen 2015–2018/2019/2020/2021 split, additive fixed-capacity models, strict 5-per-100 margin, and exact leave-one-whole-patient-out analysis.

The parent's remaining consequential flaw is comparator closure. Its universal support rule requires `G_clean` to beat independently fitted `R_clean` and same-fit `Gclean_mask`, but `B` is only diagnostic. Because `B`, `R_clean`, and `G_clean` are fitted independently, added information and minimax training do not guarantee test-year performance monotonicity. The parent can therefore declare stable universal support even if `G_clean` captures fewer documentary-M2 events than the simpler acquisition-only `B` ranking in 2020 or 2021. Such a result supports a semantic contrast but not the fixed-capacity strategy that a silent-mode study would evaluate.

Historical-minimum `K` and temporal drift are secondary interpretation threats, not reasons to replace the estimand. `K` is retained as a frozen absolute retrospective benchmark, but is not called observed MDT capacity. All three already locked absolute budgets are computed, their historical argmin and test-year workload fractions are exposed, and no sensitivity can rescue the confirmatory 10% benchmark. Separate-year results remain primary; an exact cross-year finite-corpus shift interval localizes calendar dependence without becoming population drift inference.

The decisions informed are staged:

1. whether stored report meanings show enough robust incremental and within-model reliance to make acquisition of accession-linked report version/final/release/view times a rational next evidence step; and
2. whether the locked full ranking strategy also dominates the simpler acquisition-only capacity policy strongly enough to justify consideration of a prospective silent-mode MDT study.

Neither computation authorizes funding, deployment, review, treatment, or a clinical recommendation. Cost, staffing, capacity, prospective availability, benefit and harm still require external review and new data.

## 2. Evidence-supported claim, untested hypothesis, and advance

### Strongest claim supported before computation

Direct inspection of `datasets/README.md`, the complete HCC catalog/schema, live CSV headers, and source rows supports only that HCC snapshot `[source checksum]` contains patient/encounter-linkable encounters, procedure rows, CT/MRI examination rows with `examination number`, acquisition-like `start time`, eventual `examination findings/examination diagnosis`, and untimed same-encounter pathology narratives. The pathology table has no time, specimen/accession, slide, block, section, sampling-site, distance or adequacy field. Radiology has no report author, version, finalization, release or view time. No configured HCC table measures MDT roster, slot capacity, review duration, clinician action, recurrence, survival, treatment response, harm or cost.

The inherited full pathology audit read 46,395/46,395 rows: 32,386 patient-encounters, 8,932 with multiple rows, maximum 14 rows per encounter, 16 exact duplicates after the first, and all 32,386 with at least one nonblank `Pathology/Examination Findings/Examination Diagnosis` field. These are source-availability facts, not an eligible-cohort size, prevalence estimate, or validated HCC/M2 count.

The full frozen XML of Yim et al. (PMID 27570686; PMCID PMC5001784; source `[source checksum]`, [source checksum]) was inspected. It reports 101 annotated HCC radiology reports, partial-match interannotator F1 0.93 for entities and 0.90 for relations, and describes piecemeal mentions, anaphora, split antecedents, prior measurements and uncertainty. It motivates whole-report interpretation; it does not validate this Chinese annotation rubric or any reader as biologically correct.

The full frozen XML of Cong et al. (DOI 10.3748/wjg.v22.i42.9279; PMCID PMC5107692; source `[source checksum]`, [source checksum]) was inspected. It describes a seven-point baseline gross-sampling protocol, including four tumor–liver junction samples and adjacent/distant peritumoral samples used to observe MVI. HCC source text cannot show that protocol was followed or link words to a specimen. The outcome therefore remains encounter-documentary M2.

### Unresolved hypothesis

At confirmatory `K=K_.10`:

> Among adults in the frozen first-eligible source-documented HCC-resection frame, one locked `G_clean` model using only source-byte-traceable, context-quarantined meanings from eventual stored whole-accession CT/MRI text improves encounter-documentary M2 capture by strictly more than 5 per 100 fixed review positions over (i) independently fitted `R_clean`, (ii) independently fitted acquisition-only `B`, and (iii) same-fit `Gclean_mask`, in every admissible coupled source state, pathology-terminal completion and predeclared whole radiology×pathology reader-book pair, separately in 2020 and 2021; every one of these six universal lower-margin claims remains strictly above 5 after deletion of any one whole frozen test patient.

One attained world, year, comparator or whole-patient deletion at or below 5 falsifies the corresponding universal claim once all mandatory gates pass. Equality to 5 fails. An all-world upper endpoint at or below 5 is stronger adverse evidence. Gate failure is inconclusive.

The substantive advance is not another model. It prevents semantic attribution from being mistaken for superiority of the proposed queue, while preserving exact finite-corpus uncertainty. It also gives the two contemplated evidence investments different computable predicates: `G-R` plus `G-Gmask` address semantic increment/reliance; adding `G-B` closes the fixed-capacity policy comparison.

## 3. Frozen population, clocks and source states

For each cutoff offset `d`, retain at most one state-specific episode per patient:

- age at least 18;
- earliest eligible source-documented liver resection under the frozen hepatobiliary procedure dictionary;
- same-encounter pathology composite supports documentary HCC-frame membership under the selected indivisible pathology book/form and allowed terminal;
- no recorded prior qualifying HCC resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in `[c_d-365d,c_d)`.

The primary analytical cutoff is `c_d=t_op-24h`; locked sensitivities are `d∈{12,48,72}`. CT/MRI acquisitions must lie wholly in `[c_d-90d,c_d)`. Acquisition is not report availability; no recorded treatment is not biological treatment-naivety.

Source reconstruction is unchanged: exact-deduplicate all six procedure fields while retaining raw ordinal; provisionally link same-patient/same-encounter/same-calendar-day procedures; use point clocks only for validated nonmidnight anesthesia-system starts; represent date-like or unvalidated-midnight case-record starts as `[date,date+24h)`; and partition competing/missing clocks, episode, year, imaging-window and prior-treatment membership. Prior treatment is retrieved patient-wide before interval filtering. Every ambiguity must emit a finite coherent state, a machine-checkable impossibility, or an adjudication-only exclusion retained in the outer universe. Nonmembership is never `Y=0`.

Possibility-based quarantine is over all nine reader-book pairs and all source/pathology terminals. `U_T` contains every patient eligible in any 2020 or 2021 world; among the remainder `U_V` contains anyone eligible in any 2019 world; among the remainder `U_D` contains anyone eligible in any 2015–2018 world. Development is 2015–2018, 2019 locks preprocessing and hyperparameters, 2020 and 2021 are separate untouched tests, and 2022 onward is audit-only.

## 4. Whole source objects and corpus-wide reader books

Radiology unit `u=(Patient Master Index,Encounter Number,Examination Number)` contains all exact-deduplicated components in raw order with immutable field/source-byte boundaries. Blank `Examination Number` cannot supply primary semantics. The reversible parser emits canonical-text nodes `V`, markup/attribute nodes `A`, and parse-error lineage `E`; semantic spans originate only from reversible `V` bytes. Parse-disagreeing, nonreversible, treatment/pathology/specimen/MVI-grade-contaminated or unresolved-context units receive one whole-unit unavailable block. No phrase is selectively removed and no patient is dropped.

Pathology object `v=(Patient Master Index,Encounter Number,composite_hash)` exact-deduplicates all six fields while retaining raw ordinals and serializes every `Pathology/Examination Findings/Examination Diagnosis` field in raw-row/field order with byte offsets. All pathology rows in the encounter are one indivisible documentary composite; none is assigned to a resection specimen.

Before outcome, score, split role or top-K status is exposed, freeze every reachable usable radiology unit and reachable nonempty pathology composite without HCC/grade filtering. The same two qualified Chinese-reading abdominal radiologists plus one complete adjudicator read every radiology item; the same two qualified Chinese-reading hepatobiliary pathologists plus one complete adjudicator read every pathology item. Missing expected forms, corrupt provenance or unresolved qualifications make the primary experiment globally inconclusive and cannot shrink the cohort.

Each radiology form is one indivisible concept-and-span vector for modality-specific maximum lesion diameter, lesion count, capsule, margin, arterial hyperenhancement, washout, peritumoral enhancement/hypointensity, satellite lesion, portal/hepatic-vein tumor thrombus, cirrhosis and ascites, with uncertain/not-mentioned/source-unavailable levels. Each pathology form indivisibly contains HCC-frame judgment, conditional grade judgment, spans/context and terminals from only `OUT, IN0-A, IN1-A, IN0-U, IN1-U`. `OUT` has no Y; no HCC call or grade is borrowed across forms.

Freeze three complete radiology books `B^R_R1,B^R_R2,B^R_RA` and three complete pathology books `B^P_P1,B^P_P2,B^P_PA`. The primary panel is exactly `G={R1,R2,RA}×{P1,P2,PA}`. One pair applies across all items, patients, years, cutoffs, fitting stages, models, capacities and deletions. No itemwise, patientwise, conceptwise, modelwise, capacitywise or post-deletion reader switching is allowed. `(RA,PA)` is secondary adjudicated-only and cannot rescue a nine-pair failure.

A world is `ω=(g,{s_i},{τ_i})`. The same coherent world supplies membership, year, predictors, outcomes, denominators and ties for every arm of a contrast. This is the inherited finite `Omega_book+`.

## 5. Models and fixed capacities

Information sets remain:

- `B(Z)`: independently optimized acquisition-only comparator;
- `R_clean(Z,S,Q)`: independently optimized reduced comparator with the full nonsemantic surface and availability information;
- `G_clean(Z,S,Q,X_clean)`: independently optimized full semantic model;
- `Gclean_mask`: locked `G_clean` with every complete semantic block replaced by its training-defined unavailable block, preserving byte-identical `Z,S,Q`, with no refit, recalibration or threshold change.

`Z` includes age, sex, CT/MRI/unit availability, eligible-unit count, recency, component/accession ambiguity and development-grouped `Machine Model`. `S` contains only raw/canonical/markup surface quantities. `Q` is reason-free whole-block availability. `X_clean` comes from the selected complete radiology book. Pathology, Y, reader identity/agreement, identifiers, hashes, form time, ambiguity width, unrestricted tokens, labs, interactions, splines and test-derived features are forbidden.

Use the inherited additive logistic model with unpenalized intercept, one patient-balanced outcome-blind preprocessing map over the outer development ledger, byte-identical common columns, and one robustly certified zero-slope threshold `A_M` per model. Elastic-net `alpha∈{.25,.5,.75,1}` uses 100 log-spaced lambdas from `A_M/alpha` to `10^-4 A_M/alpha`; ridge uses 100 finite values from `A_M` to `10^-4 A_M`. Fit one coefficient vector per information set by normalized minimax development loss over all nine book pairs/source/terminal states with exact cutting-plane/Dinkelbach certificates. Tune each model independently on 2019 worst-state fixed-K performance. Test outcomes/forms remain sealed until preprocessing, hyperparameters, coefficients, `N_ref` and all K values are frozen.

Compute exactly
`N_ref=min_{a=2015,...,2019; d∈{12,24,48,72}; ω∈Omega_book+} N_a(ω,d)`
and `K_ρ=floor(ρ N_ref)` for `ρ∈{.05,.10,.20}`. Confirmatory `K=K_.10`; require `N_ref≥500` and `K_.05≥25,K_.10≥50,K_.20≥100`. These are three absolute slot counts, not percentages of a test roster and not observed service capacity.

For every `K_ρ`, emit all attaining `N_ref` argmins and, for each test year/world, `f_{a,ω,ρ}=K_ρ/N_a(ω)`. Confirmatory adequacy requires every world to have at least `K_.10+1` patients, sharp anchored-grade fraction at least 0.85, and at least 50 eligible Y=1 events. Each sensitivity has its own `K_ρ+1`, anchored-grade and 50-event gate; a failed sensitivity is sensitivity-inconclusive and does not alter the 10% result. No observed or hypothetical capacity may be selected after outcomes.

## 6. Comparator-closed endpoints and singleton deletion

For locked model `M`, year `a`, capacity `k` and world `ω`,
`T_M(a,k,ω)=100/k sum_{i∈Topk_M(a,k,ω)}Y_i(ω)`,
selecting exactly `k` whole patients by locked score, SHA-256 patient tie key and raw episode backpointer.

Compute three paired contrasts using the identical world:

- `Delta_R=T_Gclean-T_Rclean` (increment beyond independently optimized nonsemantic surface);
- `Delta_B=T_Gclean-T_B` (full strategy versus simpler acquisition-only capacity policy);
- `Delta_mask=T_Gclean-T_Gclean_mask` (within-model reliance on the semantic block, not a causal attribution).

For `e=(a,k,c)`, compute attained `I_e^0=[L_e^0,U_e^0]=[min_ω Delta_c,max_ω Delta_c]`.

Freeze `U_T` before test results. For every `j∈U_T`, delete all of j's rows, states, forms, membership/outcome terminals and ranking possibilities from every model arm and both test years. Books, preprocessing, models, calibration, `N_ref` and all K values remain frozen. Define
`L_{e,j}^{-1}=min_ω Delta_c(a,k,ω\{j})`,
`U_{e,j}^{-1}=max_ω Delta_c(a,k,ω\{j})`,
`L_e^{-1}=min_j L_{e,j}^{-1}`, and `U_e^{-1}=max_j U_{e,j}^{-1}`.

Replay `min_{ω,j}N_a(ω\{j})≥k`, anchored-grade fraction ≥0.85 and at least 50 eligible Y=1 events for each evaluated capacity. Gate failure is inconclusive, never fragility or adverse evidence. Every minimizing deletion emits a protected patient hash, panel pair, source/pathology terminals, before/after top-K hashes, occupancy/replacement status, scores/ranks/outcomes and raw/form backpointers. Singleton endpoints are exact finite-corpus stress tests, not influence probabilities or sampling distributions.

## 7. Capacity and calendar localization without rescue

The 5% and 20% fixed-slot results repeat all three contrasts, nine books, adequacy gates and singleton deletions. Define `capacity-range-supportive` only if all three contrast families are stable-supportive in both years at all three K values. Otherwise emit every failed capacity/comparator/year witness as `capacity-localized`, `comparator-localized`, `calendar-localized`, or combinations. Sensitivity support cannot rescue failure at `K_.10`; sensitivity failure cannot falsify the explicitly 10% hypothesis.

For each comparator and capacity, compute the attained paired calendar-shift interval
`D_{c,k}=[min_ω{Delta_c(2021,k,ω)-Delta_c(2020,k,ω)}, max_ω{...}]`
under one global reader-book pair and coherent source/pathology choices across both years. `U(D)<0` is an invariant adverse shift within these two corpus years; `L(D)>0` is invariant favorable shift; otherwise direction is unresolved. This is descriptive finite-corpus calendar dependence, not secular-trend, transportability or future-population inference, and it never rescues a year-specific margin failure.

## 8. Exact falsification and decision-linked interpretation

For each confirmatory year×contrast coordinate after all gates:

- `stable-supportive` iff `L_e^0>5` and `L_e^{-1}>5`;
- `singleton-fragile` iff `L_e^0>5` and `L_e^{-1}≤5`;
- `world-heterogeneous` iff `L_e^0≤5<U_e^0`;
- `all-world-adverse` iff `U_e^0≤5`.

Equality to 5 fails. All extrema must be attained. The confirmatory result is one-hot:

1. `inconclusive` if any mandatory annotation, source, adequacy, fit or exact-solver gate fails;
2. `joint-comparator-closed-supportive` if all six coordinates are stable-supportive;
3. `semantic-evidence-only` if all four `Delta_R/Delta_mask` coordinates are stable-supportive but either `Delta_B` year is not;
4. `capacity-policy-only` if both `Delta_B` years are stable-supportive but the four semantic coordinates are not all stable-supportive;
5. `falsified-localized` otherwise, with exact world/calendar/comparator/deletion labels and attained witnesses.

Within categories 2–5, separately emit `all-world-adverse` only for coordinates whose upper endpoint is ≤5; do not call a heterogeneous or fragile coordinate all-world adverse.

Category 2 supports only this statement: in the frozen eventual-report corpus at the frozen `K_.10`, the full locked model added >5 documentary-M2 captures per 100 positions over both independently fitted nonsemantic policies and its same-fit semantic mask under every declared world in each test year, and no singleton deletion reversed any margin. It provides the strongest retrospective evidence for considering both accession-linked timing acquisition and a silent-mode study, subject to noncomputable operational/clinical review.

Category 3 supports robust semantic increment/reliance at the benchmark but falsifies superiority over the simpler acquisition-only queue in at least one coordinate. It can motivate resolving report timing or model redevelopment, but this experiment alone does not support advancing the current `G_clean` queue to silent mode.

Category 4 supports a better full ranking than `B` but does not establish that clean meanings, rather than fitting/surface behavior, account for the gain. It does not specifically justify accession-linked report-timing acquisition for semantic deployment.

Category 5 falsifies at least one required universal claim and identifies where. A fragile result does not mean the deleted patient is erroneous. Heterogeneity identifies dependency, not the correct reader or source state. All-world adverse excludes the strict >5 margin only for that coordinate; it does not prove reports or semantics useless. Inconclusive is not adverse evidence.

No output is a p value, confidence interval, causal effect, biological-M2 result, report-availability result, future-population guarantee, unseen-reader guarantee, treatment effect, cost-effectiveness finding, service-capacity measurement or deployment authorization.

## 9. Exact computation and certification

Enumerate all nine global book pairs exactly. Conditional on a pair, patient source/terminal domains remain finite. Robust fitting retains exact patient-domain separation inside normalized Dinkelbach/cutting-plane optimization and maximizes over all nine global books. One coefficient vector per information set is reported.

After scores freeze, solve every undeleted/deletion/comparator/capacity endpoint with the inherited state-expanded exact top-K MILP. Select one coherent state per retained patient and exactly K patients per arm; enforce total order `(linear predictor,SHA-256 tie key,raw episode backpointer)` with lazy rank-inversion constraints until no violation remains. Enumerating every j and using a shared one-deletion selector must agree. Calendar-shift extrema couple both years through one book pair.

Certification requires zero unresolved integer gap, numerical feasibility gap ≤`1e-8`, raw-state and quotient replay, order invariance, all tied maximizers, complete source/form/book/capacity/deletion backpointers, exhaustive equality on synthetic fixtures through 12 patients, and exhaustive/raw agreement on real-data shards through 20 patients. No cap, sampled state, beam, favorable incumbent, approximate bound or timeout may support or falsify a claim.

## 10. Exact HCC data bindings

Controlling catalog: `[internal dataset path]`, [source checksum]. Every HCC source is a read-only ordinary CSV; archive member is null.

| Table | Exact source path | Required columns and role |
|---|---|---|
| encounters | `[internal dataset path]` | `Patient master index, encounter number` join; `age, sex` Z; `encounter time, admission time, discharge time` audit |
| procedures | `[internal dataset path]` | keys; `surgery,start time,end time,surgery source` episode, clocks and prior procedure states |
| examinations | `[internal dataset path]` | keys+`Examination ID` whole accession; `Examination` modality; `Findings, Diagnosis` V/A/E, surface and concepts; `Start time` acquisition; `Machine model` Z |
| pathology | `[internal dataset path]` | keys; `pathology, examination findings, examination diagnosis` whole encounter composite/HCC frame/Y; `machine model` provenance; no time/specimen/accession |
| medications | `[internal dataset path]` | keys; `medication,drug type,start time,end time` prior systemic treatment |
| orders | `[internal dataset path]` | keys; `Orders (non-drug), order time, start time, end time, order status` prior local/radiotherapy evidence |
| diagnoses | `[internal dataset path]` | keys; `Diagnosis Name, Diagnosis Type` untimed corroboration only |
| labs | `[internal dataset path]` | keys; `Test,Qualitative Result,Quantitative Result,Specimen Type,Test Time` zero-predictor-lineage audit only |
| clinical_documents | `[internal dataset path]` | keys and narratives audit-only; no reliable version/release/view time |
| vitals | `[internal dataset path]` | identifier-only; forbidden predictor |
| transfers | `[internal dataset path]` | identifier-only; forbidden predictor |
| front_page | `[internal dataset path]` | header-only identifiers; forbidden predictor |

Same-encounter joins are exactly `(patient master index,encounter number)`; examination grouping adds `examination number`; prior-treatment retrieval joins patient-wide on `patient master index` before temporal filtering. Retain raw ordinal/source backpointer throughout. Direct identifiers, post-cutoff acquisitions, labs, untimed diagnoses/documents and identifier-only tables are forbidden predictors.

The complete catalog and dataset guides confirm direct access to HCC 12/12, MIMIC 5/5, eICU 31/31 and UKB 8/8 source files. MIMIC includes `[internal dataset path]` (for example member `mimic-iv-3.1/hosp/admissions.csv.gz`) plus ordinary note files; eICU uses ordinary gzipped CSVs; UKB includes eight ordinary CSVs such as `[internal dataset path]`. No cross-dataset patient linkage or equivalent Chinese HCC resection/eventual-report/untimed-pathology estimand exists, so they are not pooled. That is a scientific exclusion, not an access limitation.

## 11. Outputs and verifier boundary

Required derived outputs add comparator and localization fields to the parent package:

- `derived/annotation_roster.parquet`, complete radiology/pathology forms, immutable reader books and panel worlds;
- `derived/source_panel_states.parquet` and `chronology_partitions.parquet` with source/terminal/predictor hashes and raw backpointers;
- `derived/capacity_registry.parquet` with `N_ref`, every argmin, K values, adequacy gates and every test-world workload fraction;
- preprocessing, coefficients and exact robust-fit certificates for B, R and G;
- `derived/endpoint_extrema.parquet` keyed by year, capacity and comparator with all 3×3 matrices;
- `derived/loo_patient_endpoints.parquet` and `loo_witnesses.parquet` for all models/capacities;
- `derived/calendar_shift_extrema.parquet`; and
- a machine-readable one-hot conclusion object linked to all required output hashes.

The verifier checks source/header hashes, joins, clocks, V/A/E reversibility, whole-unit quarantine, complete form coverage, indivisible books/terminals, chronology quarantine, predictor exclusions, fixed preprocessing/models/K, B-comparator inclusion, exact ranking/ties, singleton coupling, endpoint and shift arithmetic, solver certificates, and conclusion linkage. Adversarial fixtures must include a parent-like output where G beats R and Gmask but loses to B; choosing the best K after results; treating K as observed capacity; pooling years; allowing a sensitivity or adjudicated-only pair to rescue failure; reader switching by model/capacity/deletion; recomputing K or refitting after deletion; equality at 5; gate failure called adverse; and numerically correct outputs paired with unsupported biological, availability, population, benefit or deployment prose.

Automatic verification can establish correct finite-corpus construction, computation, frozen comparisons and whether the submitted conclusion follows. It cannot establish Chinese semantic correctness, reader qualifications, dictionary completeness, renderer fidelity, operation completion, pathology specimen identity/sampling, biological M2, report final/release/view timing, actual MDT capacity, feasibility, benefit, harms, fairness, cost or transportability.

## 12. Evidence required for stronger conclusions

Biological M2 requires pathology time plus specimen/accession/slide/block links and sampling-site/extent adjudication. Real-time semantics require accession-linked authored/version/final/release/view logs and validated operation clocks. Actual capacity requires a prospective candidate stream, staffing, review duration, queue abandonment and completion measurements. A silent-mode study must preregister its actual offered and completed slots, timing, missingness and workflow comparator; retrospective K values cannot substitute. Clinical benefit requires external validation and then a controlled outcomes study. Population inference requires a defined target population, consecutive ascertainment or known inclusion probabilities, site/calendar coverage and a prespecified inferential method appropriate to the nonsmooth robust top-K estimand.

The research-ambition README was inspected. It documents full article/supplement availability for the natural-history and Bayesian demonstrations and unavailable main-article/full-STAR-Methods text for the Cell cancer demonstration. No unavailable demonstration text is claimed inspected, and none dictated this topic or method.
