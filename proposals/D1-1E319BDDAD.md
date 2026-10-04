> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Threshold-calibrated patient-sufficiency test for documentary-M2 review

## Targeted successor and unresolved clinical question

This Episode-67 successor evolves assessed-valid `[prior hypothesis]`. It preserves that candidate's mature, source-bound HCC design: the adult first eligible source-documented liver-resection population; coherent procedure-clock alternatives; the 24-hour preoperative cutoff with locked 12/48/72-hour diagnostics; 90-day acquisition and 365-day recorded-prior-treatment windows; possibility-based temporal quarantine; the encounter-documentary M2 endpoint; whole accession report units; nine global radiology/pathology reader pairs; locked patient-balanced B/R/G/same-fit-Gmask models; fixed retrospective quotas; strict greater-than-five capture margins; exact patient-level 80/80 stored-content masks; and anchored whole-patient deletion.

The clinical question is whether routine preoperative CT/MRI report semantics can identify a sufficiently large and sufficiently distributed set of adults whose resection pathology will document M2 to justify scarce multidisciplinary review. The unresolved claim is not merely whether a score ranks more documentary-M2 cases at a fixed quota. It is whether calibrated predicted documentary-M2 risk yields a reproducible review threshold with positive incremental decision-analytic value over acquisition-only and nonsemantic report-surface baselines, while the result remains valid when report content is distributed incompletely across patients.

The primary hypothesis is:

> A single threshold t* selected and frozen using 2019 alone from the prespecified grid {0.05, 0.10, 0.20} will, in each 2020 and 2021 test year, improve documentary review net benefit for the locked semantic model G over independently fitted B and R in every coherent source/pathology/reader world, every whole-unit stored-content mask satisfying the patient-sufficiency condition (at least 80% of the complete roster each have at least 80% of their own eligible CT/MRI units exposed), and the anchored deletion of any one test patient; the strictly greater-than-five-per-100 fixed-quota capture margin remains the primary confirmation.

The threshold values are design scenarios: a threshold of t treats a false-positive review as costing t/(1-t) documentary-M2 opportunities relative to a true-positive review. They are not measured patient utilities, validated clinical cutoffs, or claims that review changes outcomes. The primary estimand remains fixed-quota capture because actual review capacity and consequence-of-review are absent.

The experiment can support only a historical stored-content statement: whether the fitted semantic scoring rule identifies more source-documented M2 cases and has positive net benefit under declared hypothetical review-cost ratios. It cannot show that reports were visible before surgery, that M2 is biologically correct, that a clinician would act, that review improves surgery or systemic treatment, or that patients benefit.

## Existing evidence, strongest supported claim, and substantive advance

The inspected public literature supports the clinical importance of the problem but not this hypothesis. The full-text XML of Feng, Qu and Han's 2026 systematic review/meta-analysis (DOI 10.2196/82000; frozen source ID `[source checksum]`) reports 52 imaging deep-learning studies involving 19,531 patients, pooled sensitivity about 0.80, specificity about 0.82 and SROC about 0.88, with worse performance in external than internal validation. This supports a need for disciplined external/temporal validation and decision-focused analysis; it does not validate this HCC corpus, its report semantics, its documentary M2 endpoint, or any threshold. Current search evidence on HCC prognosis supports MVI as associated with recurrence and poor outcomes, but does not establish this model's predictive utility or a treatment effect. The supplied research-ambition README was inspected: the natural-history and Bayesian demonstration files include full article material, while the Cell cancer main article and full STAR Methods are unavailable; no unavailable text is used as evidence here.

Direct inspection of the HCC catalog, metadata, schemas and headers establishes that this snapshot contains patient/encounter-linked procedures, acquisition-timed examination rows with report-like narrative fields, and same-encounter pathology narratives. It lacks report finalization/release/view/version history, raw images, pathology time/specimen/slide/block/sampling fields, recurrence, survival, treatment response, actual review capacity/workload, clinician decisions and benefit/harm/cost. The strongest supported claim before this experiment is therefore structural: an eventual stored CT/MRI narrative can be linked to an encounter and acquisition interval, and an untimed same-encounter pathology composite can be linked to a procedure encounter. No stronger claim about availability or biological MVI is supported.

The substantive advance is a decision-relevant bridge between two often conflated claims. Fixed-quota capture measures what a scarce review service could recover at a specified capacity; threshold net benefit measures how a calibrated policy behaves across explicit review-cost scenarios. The new patient-sufficiency condition tests distributed missingness rather than accession-weighted average coverage. Reporting both prevents a favorable AUC or a concentrated set of complete patient packets from being mistaken for a deployable review policy.

## Population, chronology and coherent source states

For each cutoff offset d in {12, 24, 48, 72} hours, construct at most one state-specific first eligible episode per patient:

1. age >=18 at the index encounter;
2. earliest eligible source-documented liver resection under a frozen high-sensitivity hepatobiliary procedure dictionary;
3. same-encounter indivisible pathology composite supporting the HCC frame under the selected pathology book and terminal;
4. no recorded prior HCC resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in [t_op-365 days, t_op), using the source-reconciled procedures, medications and orders.

The primary cutoff is c=t_op-24 hours. A CT/MRI unit is eligible only when its acquisition interval lies wholly within [c-90 days,c). Acquisition time is not report release, service readability or clinician view. A case-record midnight/date-like procedure start is represented as [date,date+24 hours); a validated nonmidnight anesthesia-system start may be a point clock. Missing or competing clocks, procedure identity, year, imaging-window membership and prior-treatment membership remain coherent outer-state branches, proved impossibilities or explicitly adjudication-only exclusions. Patient-wide treatment history is assembled before interval filtering. Recorded absence is not biological treatment-naivety.

Before reading outcomes, reader forms, scores or test counts, quarantine any patient eligible in any possible 2020/2021 state into the test union; quarantine possible 2019 patients from development; among the remainder quarantine possible 2015-2018 patients from later use. Fit on 2015-2018, tune/calibrate on 2019, and evaluate 2020 and 2021 separately. Rows from 2022 onward are audit-only. The other configured datasets remain directly accessible but are not pooled: MIMIC, eICU and UKB have no crosswalk and cannot define this HCC first-resection/eventual-report/documentary-M2 estimand.

## Reports, readers and outcome

A report unit is the complete exact-deduplicated examination group u=(Patient Master Index,Encounter Number,Examination Number), retaining every component row in original order, immutable raw ordinals, exact bytes and backpointers. Group by this three-field key before modality assignment. A blank Examination Number row is a forced-zero pseudo-unit keyed by its raw ordinal for the patient-sufficiency denominator; it cannot supply report semantics or be text-merged. No component may be selectively deleted. A reversible parser separates visible bytes, markup/attributes and parse errors. Nonreversible, contaminated or unresolved units are source-unavailable and forced to the masked state.

Before outcomes or scores are exposed, two qualified Chinese-reading abdominal radiologists and one adjudicator read the complete radiology roster, and two qualified hepatobiliary pathologists and one adjudicator read the complete pathology roster. Freeze three radiology books and three pathology books, yielding exactly nine corpus-wide global pairs. No patient-, year-, outcome-, mask-, model- or deletion-specific reader switching is allowed. Radiology concepts are lesion burden, capsule, margin, enhancement/washout, peritumoral features, satellites, venous tumor thrombus, cirrhosis and ascites, with present/absent/uncertain/not-mentioned/source-unavailable terminals. Pathology terminals are OUT, IN0-A, IN1-A, IN0-U and IN1-U; IN1 is encounter-documentary M2. Untimed pathology and missing specimen/sampling data make this documentary, not biological, M2.

## Information sets, models and primary comparator

Use the inherited information sets:

- B(Z): independently fitted acquisition-only comparator;
- R(Z,S,Q): independently fitted nonsemantic report-surface/availability comparator;
- G(Z,S,Q,X): independently fitted report-semantic model;
- Gmask: the same fitted G with every semantic block replaced by its training-defined unavailable value, without refitting, recalibration or threshold change.

Z includes age, sex, modality, eligible-unit count/recency, component/accession ambiguity and development-grouped machine. S includes only raw/canonical/markup surface quantities; Q is the reason-free whole-block availability state; X contains frozen reader concepts. Labs, diagnoses, clinical documents, unrestricted tokens, pathology/outcome fields, identifiers, annotation metadata, post-cutoff content and uncertainty-width features are forbidden predictors. Laboratory rows are audited for lineage but never enter any primary feature, cohort, state or endpoint path.

Fit one minimax coefficient vector per information set over all coherent source/terminal states and nine reader pairs, using the inherited additive logistic family, outcome-blind preprocessing and certified penalty grid. Tune each independently on 2019 worst-state fixed-quota performance, then seal 2020/2021. Calibration is also frozen at this stage: use an outcome-blind model family chosen before test inspection, with 2019-only calibration and an explicitly declared monotone calibrator or intercept-only recalibration. Select one t* from the fixed grid in 2019 by maximizing the minimum of INB_G-B and INB_G-R over all 2019 states and qualifying masks, subject to a flagged fraction no greater than K_.10/N in every state; break ties toward the larger threshold and then freeze t*. If no threshold is feasible, threshold status is prospectively inconclusive and no test-year threshold is selected. If calibration cannot be certified across the outer states, threshold results are inconclusive, but primary quota results are not silently relabeled.

Set N_ref to the minimum state-specific roster size over 2015-2019, all four offsets and admissible worlds. Set K_rho=floor(rho N_ref) for rho in {0.05,0.10,0.20}; K_.10 is confirmatory, with inherited requirements N_ref>=500, K_.05>=25, K_.10>=50 and K_.20>=100. Every test world must have N>=K+1, at least 85% anchored-grade sufficiency and at least 50 Y=1 events. K is a retrospective quota, not an observed service capacity.

For model M, the primary capture yield is T_M=100/K times the number of documentary-M2 outcomes among exact top-K scores. Confirmatory contrasts are Delta_R=T_G-T_R, Delta_B=T_G-T_B and Delta_mask=T_G-T_Gmask in each test year. Every required lower simultaneous endpoint must be strictly greater than 5 at K_.10, before and after anchored removal of any one test patient.

## Patient-sufficiency mask and threshold decision analysis

For each eligible patient i, let E_i be all temporally eligible whole units, n_i=|E_i|, and let r_u indicate exposure of that exact stored unit. For n_i>0 set k_i=ceil(4n_i/5), m_i=sum(r_u), and s_i=1 iff m_i>=k_i. Zero-unit patients remain in the denominator with s_i=0. A mask qualifies iff 5 sum_i s_i >=4N. Search every qualifying mask jointly with every coherent source/pathology/reader world; do not sample masks or requalify after deletion. Require the qualifying family to be nonempty in every required world. Report C_80, C_any, mean C_frac, C_all and accession-weighted C_A as diagnostics, with exact ordering checks and counterexamples; none replaces C_80.

For threshold t in {0.05,0.10,0.20}, define a review policy for model M as a positive flag p_i^M(t)=1(score_i^M >= t), with ties resolved by the frozen patient-ID hash. Compute TP, FP, FN and TN only against the documentary endpoint within each complete state/world; unknown outcomes are not imputed and are handled by the inherited outer endpoint envelope. Define documentary net benefit:

NB_M(t)=TP_M/N - FP_M/N * t/(1-t).

Define incremental net benefits INB_G-B(t)=NB_G(t)-NB_B(t) and INB_G-R(t)=NB_G(t)-NB_R(t). Compare each also with review-none (NB=0) and review-all (NB=prevalence - (1-prevalence)t/(1-t)). These are transparent hypothetical review-value scales. They are not patient-benefit net benefit because no consequence of review, harm, cost, treatment or survival is observed.

Thresholded review must also be capacity-audited. Report the exact flagged fraction and whether it is <= each K_rho/N. If it exceeds a quota, do not truncate the threshold policy and call it a threshold result; report it as capacity-infeasible. The top-K policy remains the capacity-constrained primary. Conversely, a policy can have favorable net benefit at a threshold yet fail the primary quota margin; this is a prespecified mixed result, not a reason to select whichever endpoint is favorable.

The threshold hypothesis is supported only if the single 2019-selected t* has simultaneous lower confidence bounds for both INB_G-B(t*) and INB_G-R(t*) above 0 in every required 2020/2021 world/mask/deletion, its policy is capacity-feasible at K_.10, calibration and outcome-state gates pass, and the primary Delta_B and Delta_R lower bounds remain >5. The other two grid values are locked diagnostics and cannot rescue t*. The stronger claim that t* is clinically appropriate is not identifiable and requires prospective workflow/cost/action adjudication.

## Exact analysis, uncertainty and falsification

Compile finite ledgers for patient states, unit hashes, reader books, outcome terminals, model lineage, frozen scores, calibration maps and ties. For every year, offset, world, global book pair, qualifying mask, contrast, threshold and anchored deletion, use exact state-expanded optimization or a certified equivalent. The comparator arms share the same state, mask and endpoint completion. Return every attained extremum and a raw-row witness.

Use one joint simultaneous family for the primary capture coordinates and secondary threshold net-benefit coordinates, including both years, all required worlds/books/masks/deletions, K_.10, the locked quota sensitivities, three threshold values, both comparators and review-all/none contrasts. Do not report separate unadjusted intervals as confirmatory. Patient-level outer bootstrap may summarize uncertainty but cannot replace exact extrema or change labels. If the full family is too large for certified computation, Q is false and the result is inconclusive.

The null/falsification checks are outcome-blind semantic-block permutations within frozen year, modality, report-surface and report-cardinality strata; G must not retain a positive incremental net benefit or primary capture advantage under the prespecified null envelope. A semantic-mask fixture must produce identical G and Gmask scores, ranks, threshold flags and quota queues, with Delta_mask=0 and INB_G-Gmask=0 exactly. Exact fixtures must cover zero-unit/blank/source-unavailable patients, high average completeness with low patient sufficiency, 80/80 pass with complete-packet failure, threshold capacity excess, review-all dominating at low t, review-none dominating at high t, tied thresholds, unknown outcomes, anchored deletion, and adverse/inconclusive logic.

Define Q as source/hash/header, chronology, roster, outcome, reader, leakage, model-fit, calibration, mask-invariance, exact-solver, bootstrap-family, null, and predicate-consistency gates all passing. Define A as the 80/80 mask family nonempty in every required world. Define F_cap if any qualifying world/mask/deletion has a required primary capture margin <=5; define F_NB if the frozen t* has any required INB lower endpoint <=0 or is capacity-infeasible in any required test state; define F_max if primary capture or t* superiority fails under the unique all-exposable stored-content mask. Timeout, sampled masks, omitted states, favorable-incumbent optimization, incomplete witnesses, changed survivor features, failed replay, invalid calibration, or failed parser/reader adjudication makes Q false.

Emit one primary stored-content label:

1. `inconclusive`: Q fails;
2. `patient-sufficiency infeasible`: Q passes but A fails;
3. `robustly supportive`: Q and A pass, no F_cap, and the primary capture plus threshold conditions pass;
4. `maximum-content non-supportive`: Q and A pass and F_max holds;
5. `visibility-brittle`: Q and A pass, all-content passes, but an allowed 80/80 mask fails.

If primary capture passes but threshold analysis fails, emit `capture-supportive threshold-inconclusive`; if threshold passes but the primary >5 margin fails, emit `threshold-supportive capture-adverse`. These are prespecified secondary-mixed flags attached to the one primary label, not evidence for deployment. If calibration fails, threshold status is inconclusive even if discrimination or capture is favorable. A favorable threshold at one year, capacity or threshold only is localized, not robust support.

Supportive means the historical source reconstruction shows both a fixed-quota documentary capture advantage and a robust, capacity-feasible threshold policy under the declared hypothetical review-cost scenarios. Adverse means a required margin or threshold net-benefit condition fails even with all exposable stored content, or the semantic null is not exceeded. Visibility-brittle means the all-content policy passes but distributed missing content creates a failure. Infeasible means the 80/80 mask contract has no admissible mask. Inconclusive means computation, calibration, parser/reader validation, endpoint adjudication or source-state completeness cannot certify the claim. None proves semantics useless or harmful generally.

## Exact HCC bindings and required data

Controlling catalog: `[internal dataset path]`, [source checksum]. HCC snapshot: `[source checksum]`. All HCC sources are ordinary read-only CSVs; there are no archive members.

- `encounters`: `[internal dataset path]`; table schema `datasets/hcc/table-b743286cb1249287.json`; columns Patient Master Index, Visit Number, Age, Sex, Visit Time, Admission Time, Discharge Time. Join key (Patient Master Index,Visit Number); age/sex predictors and encounter times/audit.
- `procedures`: `[internal dataset path]`; schema `table-d5eae16f8f8093d9.json`; Procedure, Start Time, End Time, Procedure Source. Same encounter key; source-reconciled episode clocks and prior procedures.
- `examinations`: `[internal dataset path]`; schema `table-fd016d2731b9d6c6.json`; Examination, Examination findings, Examination diagnosis, Start time, Machine model, Examination number. Group key adds Examination number; acquisition window, report surface and frozen semantic concepts.
- `pathology`: `[internal dataset path]`; schema `table-0a4ee86a446c605c.json`; Pathology, Examination findings, Examination diagnosis, Machine model. Same encounter key; all rows form an indivisible untimed documentary endpoint composite.
- `medications`: `[internal dataset path]`; schema `table-4f6ecaeb6e8f69c2.json`; Medication, Drug type, Start time, End time plus dose/frequency fields. Patient-wide source-reconciled recorded-prior-treatment history.
- `orders`: `[internal dataset path]`; schema `table-6b93dcf0ea823702.json`; Non-drug orders, Order time, Start time, End time, Order status, Frequency. Patient-wide recorded local/radiotherapy treatment history.
- `diagnoses`: `[internal dataset path]`; schema `table-12710723c3df0c99.json`; Diagnosis Name, Diagnosis Type. Untimed corroboration only, never a predictor or time filter.
- `labs`: `[internal dataset path]`; schema `table-38aad8c54471332f.json`; Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time. Descriptive/lineage audit only: no unit column and forbidden from cohort, features, masks, model, endpoints and inference.
- `clinical_documents`: `[internal dataset path]`; schema `table-66afca58512c2fca.json`; all listed narrative fields including Chief Complaint, History of Present Illness, Past History, Admission Diagnosis, Admission Status, Course of Diagnosis and Treatment, Discharge Status, and Surgical Procedure. Untimed leakage audit only; never a predictor.
- `vitals`: `[internal dataset path]`; schema `table-8436de9cba74b8ca.json`; identifier-only (patient master index, visit number), not usable payload.
- `transfers`: `[internal dataset path]`; schema `table-320c20f732e71789.json`; identifier-only, no transfer timestamps.
- `front_page`: `[internal dataset path]`; schema `table-38b3224239acc33f.json`; 30-byte identifier-only/header-only source.

Verify all source hashes against the guide/metadata and retain raw row ordinals, exact field bytes and table schema hashes. Same-encounter joins are exact on (patient master index, encounter number); examinations additionally group on examination number; longitudinal treatment joins use patient plus valid source times before interval restriction. Do not pool the other three datasets. The full no-sampling audit previously inspected 419,996 examination rows, finding 419,986 exact-unique rows and 392,854 nonblank patient-encounter-accession units among 42,205 patients, with 39,610 patients having multiple units and maximum 205; these counts establish why patient-distributed missingness is nontrivial, not cohort event counts.

## Required artifacts, verification and external evidence

Publish source/filter manifest with actual counts and every exclusion; patient-state and report-unit ledgers with reachability, clocks, n_i/k_i and exact hashes; frozen reader books; preprocessing/calibration maps; fit hashes, scores, ranks, thresholds and ties; exact quota and net-benefit extrema with witnesses; mask/deletion invariance audit; one-hot requirement/label JSON; and a fail-closed operational bridge certificate.

The automatic verifier can check source hashes and headers, exact joins, chronology windows, no-overlap quarantine, whole-unit masks, state reachability, reader coupling, forbidden-feature lineage, fit/calibration hashes, top-K and threshold arithmetic, capacity checks, exact extrema, simultaneous-family construction, permutation nulls, fixture behavior and conclusion-to-output linkage. It must reject correct computation followed by claims of report timeliness, biological MVI, pathological sampling adequacy, real review capacity, clinically appropriate thresholds, deployment, clinician action, treatment effect, recurrence, survival, safety, fairness, transportability or patient benefit.

Clinical experts must adjudicate the hepatobiliary procedure dictionary, operation identity, Chinese radiology/pathology semantic books, specimen linkage and sampling adequacy. An external source-system audit is required for final/release/view times, version identity, pipeline-input hashes and historical visibility. Workflow stakeholders must supply actual review capacity, burden, review duration, action and costs. A prospective or external cohort is required for biological MVI validation, calibration transport, clinician action, treatment effect, recurrence, survival, harm, cost and patient benefit. If any such evidence is absent, label the corresponding claim not estimable rather than adverse.

A bounded feasibility run (job `[research job]`, output [source checksum]) checked all 12 live CSV headers against the catalog schemas, exhaustively replayed 50,625 small-packet C80 masks without an ordering violation, and passed net-benefit and capacity-overflow fixtures. This establishes source/header and arithmetic feasibility only; it does not establish cohort size, event prevalence, model performance or clinical validity.

The automatic experiment therefore tests an important falsifiable stored-content hypothesis and its decision-analytic robustness, while keeping clinical utility, deployment and causal benefit as explicit next-study questions.
