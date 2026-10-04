# Decision-thresholded patient-sufficiency stress test for documentary-M2 review

## 1. Targeted successor, audit finding, and clinical question

This child evolves assessed-valid [prior hypothesis] and changes one scientific element only: it makes the fixed-quota review contrast decision-interpretable through a prespecified threshold and capacity-constrained decision-curve analysis. It preserves the parent's adult first-eligible source-documented resection frame; operation-clock, imaging-window and prior-treatment source worlds; possibility quarantine; encounter-documentary M2 outcome; whole-accession radiology objects; indivisible same-encounter pathology composites; six frozen reader books and nine global reader pairs; patient-balanced locked B/R/G/same-fit-Gmask models; fixed absolute K; comparator-closed masks; exact extrema; patient-disjoint temporal roles; and anchored whole-patient singleton deletion.

The most important remaining weakness is scientific, not computational. The parent asks whether G captures strictly more than five additional documentary-M2 cases per 100 review positions than B, R, and same-fit Gmask, but never states how many non-M2 reviews are acceptable for one documentary-M2 review. Two fixed-K rules can differ by the required five captures while both have negative value under a plausible review preference. The parent therefore establishes a ranking contrast but not whether using the K slots is preferable to leaving them unused or allocating them without ranking.

The repaired question is:

> At a prespecified documentary-review threshold of 20%, does the locked semantic G top-K policy, in each 2020 and 2021 test year and every admissible 80/80 stored-content, source, pathology, reader and singleton-deletion world, both retain the parent's strict capture advantages and have positive net benefit versus no review and capacity-matched random review?

The action is record prioritization for a review slot. The outcome remains pathology-encounter documentary M2. “Benefit” in the net-benefit arithmetic means correctly prioritizing a record whose linked pathology composite is read as documentary M2; it does not mean biological MVI was correctly identified, a clinician saw a report, care changed, treatment worked, or a patient benefited.

## 2. Evidence-supported claim, unresolved claim, and advance

The strongest claim supported before this experiment is about source structure and the evidence gap. I inspected datasets/README.md, the HCC README and metadata, every HCC table schema, and the actual first-line header of all 12 ordinary CSV sources. HCC snapshot [source checksum] contains patient/encounter-linked procedure rows, CT/MRI examination rows with 开始时间, accession-like 检查号, eventual narrative fields, and untimed same-encounter pathology narrative. It lacks radiology authorship, report-version, finalization, release, amendment, retraction, ingestion, service-readability and view times; pathology time and specimen/slide/block identity; raw images and slides; real review capacity, completion and burden; clinician action; treatment; recurrence; survival; harm; cost; and patient benefit. No clinical rows were sampled for this successor. The inherited no-sampling audit read all 419,996 examination rows and found 392,854 nonblank patient-encounter-accession units in 42,205 patients; it is retained only as source-grain feasibility evidence, not a cohort count or modality validation.

Feng, Qu and Han's 2026 systematic review/meta-analysis (DOI 10.2196/82000, PMCID PMC12954728) was inspected from full-text XML source [source checksum], [source checksum]. It included 52 imaging deep-learning studies and 19,531 patients and reported pooled sensitivity 0.80, specificity 0.82 and SROC 0.88, with lower SROC in external than internal validation (0.85 versus 0.90). Neves and Soares' 2026 HCC review (DOI 10.3390/cancers18132028, PMCID PMC13360217) was inspected from full-text XML source [source checksum], [source checksum]; 35/36 studies were retrospective, 27/36 single-center, only 6/36 externally validated, and calibration and decision-curve analysis were inconsistently reported. These reviews motivate utility-focused evaluation but do not validate HCC report semantics, documentary-M2 labels, the 80/80 rule, K, or a clinical threshold.

Vickers, van Calster and Steyerberg's decision-curve guide (DOI 10.1186/s41512-019-0064-7, PMCID PMC6777022) was inspected from full-text XML source [source checksum], [source checksum]. It defines threshold probability as the minimum disease probability at which action is warranted and net benefit as true-positive benefit minus false-positive burden weighted by threshold odds. This supports the arithmetic, not the substantive choice of 20% in this setting.

The unresolved claim is conditional and falsifiable: whether G's top-K documentary ranking remains worth using when one documentary-M2 prioritization is valued against four non-M2 reviews, under every retained source and stored-content uncertainty. The advance over the parent is an absolute action criterion against no review and random K, not a relabeling of the capture contrast. Because every arm uses the same K, G-versus-comparator net-benefit differences are algebraic rescalings of capture differences; they are not counted as independent evidence.

## 3. Prespecified preference threshold and exact primary estimand

Freeze the primary threshold before any 2020/2021 outcome or score is exposed:

p_t*=1/5=0.20, with false-positive weight w*=p_t*/(1-p_t*)=1/4.

Interpretation: for this documentary review action only, one correctly prioritized documentary-M2 record offsets the burden of four reviewed records without documentary M2. Thus a K-slot policy must capture strictly more than K/5 documentary-M2 records to beat no review. Equality fails. This threshold is a transparent design preference, not an empirical estimate or endorsed clinical standard. Deployment requires prospective hepatobiliary-radiology, pathology, workflow and patient/stakeholder review of the action and threshold.

For model/policy M, let h_M be documentary-M2 cases among its exact top K, f_M=K-h_M, N the binary-outcome eligible roster, and E its total documentary-M2 count in the same world. Define standard net benefit per patient at rational threshold p=a/b:

NB_M(a/b) = h_M/N - f_M/N * a/(b-a) = (b*h_M-a*K)/((b-a)*N).

Baselines on the identical roster are:

- no review: NB_none=0;
- review all: NB_all=(b*E-a*N)/((b-a)*N), reported as a conventional but capacity-infeasible reference because N>=K+1;
- capacity-matched random review of exactly K patients: expected NB_randK=K*(b*E-a*N)/((b-a)*N^2);
- oracle K: h_oracle=min(K,E), an unattainable upper benchmark.

The random baseline is an exact finite-roster expectation, not a random simulation. At p_t*=1/5, G beats no review iff 5*h_G>K, and beats random K iff N*h_G>K*E. Both are strict integer predicates.

Retain the parent's capture measure T_M=100*h_M/K. For each C in {B,R,Gmask}, define Delta_C=T_G-T_C. Equal K implies:

NB_G(a/b)-NB_C(a/b)=b*(h_G-h_C)/((b-a)*N).

At 20%, strict Delta_C>5 is exactly a gain of more than 6.25 net-benefit units per 100 review positions. It remains a comparator contrast, while NB_G>max(NB_none,NB_randK) is the new absolute decision test.

For test years y in {2020,2021}, all admissible worlds omega, global reader pairs, full-roster qualifying masks r, and anchored deletions j in {none} union I, define the sharp universal vector:

- theta_C = min Delta_C for C=B,R,Gmask;
- theta_none = min NB_G(1/5);
- theta_rand = min [NB_G(1/5)-NB_randK(1/5)].

The primary hypothesis is theta_B>5, theta_R>5, theta_Gmask>5, theta_none>0, and theta_rand>0 separately in both years. A single attained counterexample falsifies it.

## 4. Population, clocks, temporal roles, and outcome

For each cutoff offset d, retain at most one state-specific episode per patient: age at least 18; earliest eligible source-documented liver resection under the frozen high-sensitivity hepatobiliary procedure dictionary; same-encounter indivisible pathology composite supporting the HCC frame under the selected pathology book and terminal; and no recorded qualifying prior HCC resection, transplant, TACE/embolization, ablation, radiotherapy, targeted therapy or immunotherapy in [c_d-365d,c_d).

The primary analytical cutoff is c_d=t_op-24h; d=12, 48 and 72 hours are locked diagnostics. A CT/MRI accession is eligible only if its acquisition interval is wholly in [c_d-90d,c_d). Acquisition is not report availability or viewing. “No recorded prior treatment” is not biological treatment-naivety.

Exact-deduplicate procedure rows on all six source fields while retaining raw ordinal. Link provisional same-patient, same-encounter, same-calendar-day candidates. A validated nonmidnight anesthesia-system start may be a point clock. An unvalidated midnight/date-like case-record start remains [date,date+24h). Missing or competing operation clocks, episode identity, year, imaging-window membership and prior-treatment membership remain coherent finite alternatives, proved impossibilities, or adjudication-only exclusions in the outer universe. Retrieve treatment history patient-wide before interval filtering; nonmembership is never Y=0.

Before outcomes, reader forms, fitting or test inspection, possibility-quarantine any patient eligible in any 2020/2021 state into U_T; among the remainder any possible 2019 patient into U_V; among the remainder any possible 2015-2018 patient into U_D. Develop in 2015-2018, tune/seal in 2019, test 2020 and 2021 separately, and leave 2022 onward audit-only. Patients are disjoint across roles under every state. The catalog-reserved partition is not external validation.

Pathology terminals remain OUT, IN0-A, IN1-A, IN0-U, IN1-U. IN1 is encounter-documentary M2; IN0 is encounter-documentary non-M2. OUT is a nonmember/no-outcome state and is never recoded as a negative. Every admitted test roster member is binary IN0/IN1 in that world. Require the inherited anchored-grade fraction at least .85 and at least 50 Y=1 events in every test world. Computation cannot establish biological MVI, specimen linkage or sampling adequacy.

## 5. Whole source units and frozen readers

A nonblank radiology unit is u=(患者主索引,就诊号,检查号) and includes every exact-deduplicated component row in original order with immutable byte, field and raw-row backpointers. A reversible parser separates visible text, markup/attributes and parse errors. Semantic spans may arise only from reversible visible bytes. Nonreversibility, treatment/pathology/specimen/MVI-grade contamination, or unresolved context makes the whole unit semantic-source-unavailable; phrases are not selectively removed and patients are not dropped.

For the sufficiency denominator, each eligible exact-deduplicated CT/MRI row with blank 检查号 is a forced-zero pseudo-unit (患者主索引,就诊号,raw_ordinal). It supplies no semantics and cannot be text-merged. A pathology object serializes all exact-deduplicated same-encounter 病理/检查所见/检查诊断 fields in row and field order and remains indivisible because pathology has no time or specimen identifier.

Before outcomes or scores are exposed, two qualified Chinese-reading abdominal radiologists plus one complete adjudicator read the complete radiology roster, and two qualified Chinese-reading hepatobiliary pathologists plus one complete adjudicator read the complete pathology roster. Freeze R1/R2/RA and P1/P2/PA; exactly nine global book pairs apply corpus-wide. Patient-, item-, year-, model-, outcome-, mask- or deletion-specific reader switching is forbidden. Reader qualification, Chinese semantic truth, dictionary validity and pathology sampling remain clinical adjudication, not automatic outputs.

## 6. Locked models, quota, and comparator closure

Preserve four information sets:

- B(Z): independently optimized acquisition-only comparator;
- R_clean(Z,S,Q): independently optimized report-surface/availability comparator;
- G_clean(Z,S,Q,X_clean): independently optimized semantic model;
- Gclean_mask: the identical fitted G with every semantic block replaced by its training-defined unavailable value, without refit, recalibration or threshold change.

Z is limited to age, sex, modality, eligible-unit count and recency, component/accession ambiguity, and development-grouped machine. S is raw/canonical/markup surface quantity; Q is reason-free whole-block availability; X contains only frozen-reader concepts. Outcomes, pathology, reader identity/agreement, unrestricted text/tokens, identifiers/hashes, annotation times, uncertainty width, labs, interactions, splines and test-derived features are forbidden.

Use the inherited additive logistic family, unpenalized intercept, one patient-balanced outcome-blind preprocessing map over the complete outer development ledger, byte-identical shared columns and certified penalty grids. Fit one minimax coefficient vector per information set across all development source/terminal states and nine reader pairs. Tune each model independently on 2019 worst-state fixed-K performance, then seal models, preprocessing, ties and all test outcomes. Scores need not be calibrated probabilities: p_t is the decision preference used to evaluate the binary top-K policy, not a cutoff applied to the score. No per-world thresholding or slot abandonment is introduced.

Let N_ref=min N_y(omega,d) over 2015-2019, four offsets and admissible worlds. Freeze K_rho=floor(rho*N_ref) for rho=.05,.10,.20; K_.10 is confirmatory and K_.05/K_.20 are diagnostics. Require N_ref>=500, K_.05>=25, K_.10>=50, K_.20>=100, and every test/deletion roster N_j>=K+1. K is a retrospective quota, not observed service capacity.

## 7. Exact 80/80 stored-content experiment and deletion

For each eligible accession freeze the parent's version-faithful hash over schema/parser version and length-delimited ordered tuples of raw row ordinal, field, exact raw bytes and parser lineage for all 检查所见 and 检查诊断 components. Binary r_u=1 exposes that exact whole eventual report object; r_u=0 replaces all body-derived S/Q/X blocks in R, G and Gmask by their development-defined unavailable block. B and acquisition-only Z remain fixed. Blank, nonreversible, contaminated and adjudicated source-unavailable units are forced zero. Free bits are counterfactual stored-corpus interventions, not observed historical availability.

For complete test-world roster I, eligible unit set E_i and n_i=|E_i|, set m_i=sum r_u, k_i=ceil(4*n_i/5), and s_i=1 iff n_i>0 and m_i>=k_i. A mask qualifies iff 5*sum_i s_i>=4*N. Zero-unit patients remain in N with s_i=0. The qualifying family must be nonempty in every required world. Diagnostics C_any,C_frac,C_all,C_A are retained, with C_all<=C_80<=C_any; none substitutes for C_80.

For deletion j, first qualify r on the full roster, then remove j and all its states, outcomes and units. Keep K, books, models, calibration state, tie rule and every survivor's bit, feature hash and score unchanged; rerank survivors to exact K if the deleted patient occupied a slot. Do not requalify the mask, recompute survivor n_i, expose a replacement report, or modify a survivor. This is the parent's anchored whole-patient singleton deletion.

## 8. Decision curve, exact analysis, and falsification

Compute exact capacity-constrained decision-curve points for every locked policy and baseline at P={1/10,3/20,1/5,1/4,3/10}. The 20% point alone is confirmatory; the other points display preference sensitivity and cannot rescue failure. Report standard NB per 100 patients and slot-standardized 100/K*[h_M-w(K-h_M)]. Curves connect displayed points only for visualization; no uncomputed interpolation claim is allowed.

Compile finite patient domains carrying membership, year, Y, Z/S/Q/X, unit sets and hashes, source/form/terminal hashes, scores, ties and raw backpointers. Encode the 80/80 iff constraints exactly as in the parent. For every year, world, reader pair, contrast, deletion and qualifying mask, exact MIP or certified equivalent must search for these integer failure witnesses:

- comparator failure for C: 20*(h_G-h_C)<=K;
- no-review failure at 20%: 5*h_G<=K;
- random-K failure at 20%: N*h_G<=K*E.

Comparator arms share the same world, mask, roster and deletion. Return attained raw-row witnesses and exact rational NB arithmetic for every extremum. For each DCA grid point a/b, store (N,E,K,h_M) so the verifier recomputes all policies and baselines without floating-point dependence.

Define Q as all source/header/hash, chronology, population, role-disjointness, outcome, reader, leakage, fit, K, tie, whole-mask, mask-invariance, exact-solver, replay and conclusion gates passing. Define A as the 80/80 family nonempty in every required world. Let Fcmp be any comparator witness, Fdec any no-review or random-K witness, and Fmax either type under the unique all-exposable-content mask.

Emit exactly one primary label:

1. computationally inconclusive if not Q;
2. patient-sufficiency infeasible if Q and not A;
3. decision-robust supportive if Q and A and neither Fcmp nor Fdec;
4. maximum-content adverse if Q and A and Fmax;
5. patient-sufficiency visibility-brittle adverse if Q and A and (Fcmp or Fdec) and not Fmax.

These labels are exhaustive and disjoint. Report separate reason bits for B, R, Gmask, no review and random K; year, reader pair, source world, deletion and mask; and whether failure is comparative, absolute-threshold, or both. Retain the parent's b_80=max C_80 over failing witnesses and its consistency check. Maximum-content adversity means failure even when every exposable stored unit is supplied. Visibility-brittle adversity means maximum stored content passes but an allowed distributed omission defeats the contract. Neither establishes that report semantics are generally useless or harmful.

Require zero integer gap, exact rational replay, numeric residual <=1e-8, complete rank-inversion constraints, all tied maximizers, forward/reverse raw-state reachability, lossless quotient replay and brute-force agreement on synthetic fixtures through 12 patients and real shards through 20. Timeout, state cap, mask sampling, favorable incumbent, omitted world/book/deletion, missing witness, changed survivor feature, rational-scaling loss or failed replay makes Q false.

The exact uncertainty envelope covers the finite frozen corpus, source ambiguity, global reader variation, every qualifying missing-content placement and every singleton deletion. It is not a confidence interval for a target population. Bootstrap summaries may be descriptive only.

## 9. Interpretation of results

Supportive: the locked G rule exceeds each comparator by >5 documentary-M2 captures per 100 slots and beats no review and expected random K at the 20% preference in every required state. This supports acquiring the operational report-version/readability census and conducting a prospective silent workflow study. It does not support deployment, treatment, or patient benefit.

Adverse: a maximum-content failure says the fixed G rule or its assumed review preference is not supported even with all exposable stored content. A visibility-brittle failure says its apparent usefulness depends on a missing-content pattern stronger than the 80/80 contract. A no-review-only failure means the semantic ranking may beat comparators yet the K-slot action still captures too few documentary-M2 cases at the stated preference. A random-only failure means use of G does not improve expected utility over allocating the same K slots at random. These findings do not prove absence of biological signal.

Inconclusive: failed computation, unresolved leakage, invalid readers/dictionaries, insufficient events/roster, nonreplayable states, or unavailable binary outcomes prevents the universal claim. Structural 80/80 infeasibility is reported separately and never treated as support. If clinical stakeholders do not endorse 20% as reasonable, the arithmetic remains a valid conditional sensitivity analysis but no clinical action conclusion follows.

## 10. Exact HCC source bindings

Controlling catalog: [internal dataset path], [source checksum]. All sources are read-only ordinary CSVs; archive member is none.

| table | exact path | required columns and role |
|---|---|---|
| encounters | [internal dataset path] | 患者主索引,就诊号 joins; 年龄,性别 Z; 就诊时间,入院时间,出院时间 audit |
| procedures | [internal dataset path] | keys; 手术,开始时间,结束时间,手术来源 episode, clock, prior operation |
| examinations | [internal dataset path] | keys; 检查号 accession; 检查 modality; 检查所见,检查诊断 S/Q/X/hash; 开始时间 acquisition; 机器型号 Z/provenance |
| pathology | [internal dataset path] | keys; 病理,检查所见,检查诊断 frame and documentary-M2 composite; 机器型号 provenance; no time/specimen |
| medications | [internal dataset path] | keys; 用药,药品类型,开始时间,结束时间 prior systemic-treatment evidence |
| orders | [internal dataset path](非药品)_2062526727266216118.csv | keys; 医嘱(非药品),开立时间,开始时间,结束时间,医嘱状态 prior local/radiotherapy evidence |
| diagnoses | [internal dataset path] | keys; 诊断名称,诊断类型 untimed corroboration only |
| labs | [internal dataset path] | keys; 检验,定性结果,定量结果,标本类型,检验时间 forbidden-predictor audit only |
| clinical_documents | [internal dataset path] | keys and all narrative columns for leakage audit only; no usable document time |
| vitals | [internal dataset path] | identifier-only 患者主索引,就诊号 |
| transfers | [internal dataset path] | identifier-only keys |
| front_page | [internal dataset path] | identifier-only keys, 30-byte file |

Same-encounter joins are exact on (患者主索引,就诊号); examination grouping adds 检查号; patient-wide history joins on 患者主索引 before time filtering. Preserve BOM-aware exact headers, raw ordinal, raw bytes/hash and backpointer. Direct identifiers, post-cutoff content, lab values, untimed diagnoses/documents and identifier-only tables are forbidden predictors. MIMIC, eICU and UKB remain directly accessible through their guides but are not pooled because there is no crosswalk or compatible first-resection/eventual-Chinese-report/untimed-pathology documentary-M2 frame.

## 11. Required derived outputs and operational bridge

Write analyses only in the workspace:

- derived/source_and_filter_manifest.json: source/schema hashes, exact filters, no-sampling declaration and actual counts by exclusion/state;
- derived/patient_state_ledger.parquet and derived/report_unit_ledger.parquet: roles, branches, outcomes, n_i/k_i, hashes and raw backpointers;
- frozen reader books, preprocessing maps, model hashes, K, scores, ranks and ties;
- derived/decision_extrema.parquet: every year/world/book/mask/deletion/model N,E,K,h,f, capture contrast, exact NB and witness;
- derived/decision_curve.parquet: all five rational thresholds and none/random/all/oracle baselines;
- derived/decision_requirement.json: Q/A/F predicates, sharp theta vector, one-hot label and permitted conclusion;
- derived/mask_invariance_audit.parquet and derived/operational_bridge_certificate.json.

Fixtures must include threshold equality (5*h_G=K), positive versus none but not random, comparator margin pass with absolute-NB failure, absolute-NB pass with comparator failure, supportive/adverse/visibility-brittle/infeasible/inconclusive labels, zero-unit and forced-zero patients, deletion without mask requalification, and exact DCA replay at every rational grid point.

HCC can compute only counterfactual eventual stored-content robustness. An operational bridge requires a complete same-snapshot accession/version census keyed by protected 检查号; all predecessor/version IDs and exact input hashes; authored, final, release, amendment, retraction and ingestion times; service-readability; validated operation clocks; and the complete patient/accession denominator. Clinician-view timestamps are additionally required to claim viewing. Missing archive evidence is unknown, never zero. Until the census/hash crosswalk passes, emit operational_80_80_status=not_estimable_from_HCC.

Actual slots, reviewer-hours, turnaround, completion, abandonment, clinician actions, treatments, recurrence, survival, harms, costs and patient-reported outcomes require workflow data, expert review, an external cohort or another study. An automatic verifier can check source hashes/headers, joins, temporal logic, roles, forbidden features, fixed K, top-K/ties, whole-unit masks, 80/80 qualification, deletion invariance, integer failures, exact NB, labels and conclusion linkage. It cannot establish dictionaries, reader qualification, Chinese semantics, specimen linkage/sampling, biological MVI, archive completeness, report visibility/viewing, the clinical acceptability of 20%, workflow feasibility, treatment effect or patient benefit. Correct computation with any such unsupported conclusion must fail verification; appropriate supportive, adverse and inconclusive interpretations must pass.

The research-ambition README was inspected. It states that full natural-history and Bayesian article materials are available, while the Cell cancer main article and full STAR Methods are unavailable. No demonstration paper is used as substantive evidence here, and no unavailable text is claimed inspected.
