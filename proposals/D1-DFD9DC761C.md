# Report-state-robust, laboratory-independent M2 triage before first HCC resection

## Clinical question, current evidence, and the unresolved claims

The decision question is deliberately narrow: 24 hours before an adult patient's first eligible liver resection, can a frozen, interpretable strategy use only decision-safe demographics, imaging-acquisition facts, and possibly available routine CT/MRI report content to flag a patient in this institution's retrospectively pathology-confirmed HCC resection frame for multidisciplinary review because the resection specimen may show pathology-defined high-grade microvascular invasion (M2)?

The output is a historical weighted classification flag. It is not a recommendation for a wider margin, neoadjuvant or adjuvant therapy, surveillance, transplantation, or any other treatment.

**Strongest claim the available evidence supports now.** Direct inspection of the HCC catalog, metadata, and source headers establishes that operation start times and CT/MRI acquisition start times exist, while the examination table has no report-authored, finalization, release, or clinician-view timestamp. Its exact header is `患者主索引,就诊号,检查,检查所见,检查诊断,开始时间,机器型号,检查号`. The pathology table contains same-encounter untimed text but no specimen identifier, block count, sampling protocol, slide, or pathology time. The laboratory table has only `患者主索引,就诊号,检验,定性结果,定量结果,标本类型,检验时间`; it has no collection, result-entry, verification, finalization, release, clinician-view, panel/accession, or unit field. These observations establish computability of acquisition-bounded, pathology-text-defined research and the absence of evidence for report or laboratory visibility. They do not establish prevalence, performance, clinical utility, or benefit.

The inspected full XML of Li et al. (2025; DOI `10.1111/jcmm.70746`, PMCID `PMC12309289`, frozen source `[source checksum]`, [source checksum]) supports the pathological MVI-TTG definition—M2 is more than five proximal foci within 1 cm and/or any focus beyond 1 cm—and the prognostic relevance and ascertainment limitations of MVI. The inspected full HTML of Huang et al. (2026; DOI `10.3389/fonc.2026.1821034`, frozen source `[source checksum]`, [source checksum]) reports a retrospective multicenter complete-data model for binary MVI using CT margin irregularity and AFP positivity (487 development and 256 external-validation patients; AUC 0.740 and 0.781) with exploratory decision-curve analysis and explicit pathology slide/sampling review. It does not validate M2, routine report semantics, historical report/result visibility, this dataset, or treatment benefit.

**Unresolved clinical-value hypothesis C.** In the locked 2020–2021 whole target frame, does the laboratory-independent, report-state-robust semantic strategy `S` add at least 0.01 net-benefit units over the identically fitted laboratory-independent structured baseline `B` at threshold 0.30, uniformly over every patient-wise radiology-report availability state and pathology-grade state allowed by the data? Support also requires a positive increment at every threshold from 0.25 through 0.35 and superiority to flag-all and flag-none. At 0.30, the false-positive weight is `0.30/0.70=0.4286`; the 0.01 margin is one net true-positive equivalent per 100 target-frame patients under that exchange rate. Neither the threshold nor that exchange rate has been clinically elicited.

**Unresolved attribution hypothesis A.** Does the identical radiology-semantic block add positive net benefit after measured radiology workflow/provenance variables are present, comparing nested `A=W+C_R` with `W`, under the same report and pathology uncertainty and the same report-state-robust fitting rule? This can support incremental modeled information beyond measured workflow; it cannot establish semantic causality or eliminate unmeasured documentation-process confounding.

`S-B` is the primary deployable clinical-value estimand. `A-W` is the separate nested attribution estimand. Non-nested `S-W` is descriptive only. Attribution failure cannot erase a supported S-B contrast, and attribution support without S-B support does not establish deployable value.

## Substantive successor repair: remove an invented training-state distribution

The parent correctly bounds test evaluation over shared latent report states, but it fits, tunes, and recalibrates models by giving every feasible state equal weight. For one report this invents 50% availability; for two reports it invents a uniform distribution over four CT/MRI combinations and implicitly treats those combinations symmetrically. No source field supports those probabilities. Exact test extrema conditional on a fitted model cannot repair coefficients, penalties, and calibration selected under an unsupported pseudo-distribution.

This child replaces equal-weight state augmentation in every primary fit with an exact patient-wise least-favorable loss over the same state set. It therefore makes the fitted policy itself robust to unknown report availability. This is a changed analysis, not a wording repair. Population, clocks, endpoint, information sets, primary contrasts, thresholds, test-state bounds, and falsification criteria remain unchanged.

The advance over current knowledge is a falsifiable estimate of whether routine radiology-report semantics can add historically material M2 triage value when neither development nor test fitting/evaluation assumes a report-availability probability. Existing complete-data MVI models and the parent’s equal-state training do not answer that question.

## Frozen population, index, and temporal boundaries

The unit is one patient (`患者主索引`) and one first eligible index resection. All sources are read-only; row-level derivatives stay private in the workspace.

1. In `procedures`, select the earliest valid `开始时间` whose normalized exact `手术` is in a frozen, clinically reviewed dictionary of partial, segmental, hemihepatic, or liver-tumor resections. Exclude transplant, biopsy, puncture, ablation-only, gallbladder-only, metastatic-organ surgery, and explicit repeat/recurrence operations. Break exact-time ties by `就诊号` and normalized `手术`. Before outcome access, emit included and excluded raw operation values and frequencies, invalid times, ties, and a one-index-per-patient assertion.
2. Require age at least 18 and same-encounter pathology text explicitly identifying HCC in the index surgical encounter. This defines a retrospectively resected, pathology-confirmed institutional frame; it does not prove preoperative diagnostic certainty, resectability, curative intent, or biological treatment-naivety. Do not require an observed MVI grade or secure specimen linkage for inclusion.
3. Define `t_dec=procedures.开始时间-24 hours`. No record at or after `t_dec` predicts. The inherited 12-, 48-, and 72-hour-buffer analyses are required sensitivities and never replace the primary.
4. A liver CT/MRI row is acquisition-eligible only with valid `examinations.开始时间` in `[t_dec-90 days,t_dec)`. After exact-row deduplication, bundle by `(患者主索引,就诊号,检查号,开始时间)`; a missing `检查号` creates a row-level bundle. Freeze CT/MRI dictionaries from exact `检查`. Select at most the latest CT and latest MRI bundle by `开始时间`, then `检查号` and normalized `检查` for ties. Require at least one eligible CT/MRI. Emit multiplicity, ties, and discarded bundles. Acquisition time never establishes report availability.
5. Laboratories remain diagnostic only. A laboratory row is timestamp-eligible for audits when valid `检验时间` lies in `[t_dec-30 days,t_dec)`; retain exact `(检验,标本类型)`, last-row, and source-order tie audits. No laboratory field or derivative—including row existence, assay/specimen, value, count, missingness, or time—may enter B/S/W/A/U, fitting strata, recalibration, thresholds, or primary gates.
6. The primary no-recorded-prior-treatment cohort excludes recorded HCC resection, transplant, TACE, ablation, radiotherapy, targeted therapy, or immunotherapy found in procedures, medications, or non-drug orders during `[t_dec-365 days,t_dec)`, using frozen reviewed dictionaries and valid source times. Report exclusions by source and invalid time. Previously treated patients are a separately labeled sensitivity cohort.
7. Development fitting is 2015–2018; penalty selection and logistic recalibration use 2019 only; 2020–2021 is untouched test. Assign by index operation date and keep every row from a patient in one period. Exclude 2013–2014. A frozen pipeline may score 2022 through snapshot end 2025-11-11 only for predictor, extraction, and template drift plus endpoint identifiability; no contemporary performance claim is permitted.
8. Freeze population dictionaries, tie/bundle rules, text masks, semantic rules, pathology rules, preprocessing constants, robust objectives, alpha/penalty grid, recalibration, thresholds, bootstrap family, permutation strata, and gates before test outcomes are read.

Harbor must report actual counts for every filter, invalid or missing clock, exact duplicate, join multiplicity, dictionary value, exclusion, selected/discarded bundle, report state, and endpoint state, and prove zero laboratory lineage in every primary artifact.

## Pathology-only endpoint and ascertainment boundary

`Y=1` only for pathology-defined M2; `Y=0` for M0 or M1. `V=1` means a trustworthy documentary assignment to the index resection specimen under the frozen position-aware parser and blinded adjudication; missing grade, positive-ungraded MVI, conflict, or uncertain specimen linkage is `V=0`, never an exclusion.

Assign grade only from the immediate selected value after an anchored field such as `MVI提示风险分级[:：]`, stopping before definitions, explanatory bullets, historical clauses, or a new specimen section, or from a frozen synonymous selected-value construction accepted in blinded development review. Handle negation, `未见`, multiple specimens, and discordance. Unanchored M2, binary `微脉管侵犯：有/无`, positive-ungraded MVI, blank vessel-number/distance fields, absent MVI language, definitions, and conflicts cannot assign M0/M1/M2. Pathology never predicts.

Two independently implemented parsers must agree on locked test records. Two qualified Chinese-reading pathologists, blinded to predictors and scores, independently review every parsed M2, every conflict, at least 150 parsed M0 and 150 parsed M1 sampled by year/template, and every test `V=0`; a third resolves disagreements. Require class-specific PPV at least 0.98, sensitivity at least 0.95, Cohen kappa at least 0.90, and parser disagreement no more than 5%. Reviewers may derive grade only from explicit number/distance language under the frozen definition. Inadequate text, ambiguous specimen linkage, or inadequate documented sampling remains `V=0`.

Raw slides, specimen identifiers, block counts, vessel-distance measurements, and sampling protocol are unavailable. Thus the endpoint is the documented index-specimen pathology grade, not latent biological M2. Text adjudication cannot prove that tissue sampling did not miss MVI. Any claim about biological M2 requires slide/specimen review and another study.

## Shared radiology report-availability states

For patient `i`, let `q_i` be the number (0, 1, or 2) of selected CT/MRI bundles with nonempty eventual report text and let `Omega_i^R={0,1}^{q_i}`. A one means the stored report is treated as finalized and visible at `t_dec`; a zero means unavailable. Empty stored text has state zero only. No probability, independence, temporal monotonicity, or relation to outcome is imposed.

At state zero, mask every report-body-derived item from that bundle: size, lesion count, macrovascular thrombus, report length/sections/template, all semantic findings, and unrestricted text. Acquisition facts remain: valid acquisition time, modality from `检查`, bundle count, distinct-`检查号` count without exposing the identifier, and development-frequency machine-availability category. At state one, stored report variables are exposed.

The same patient state `r` must be used for every compared model when computing a contrast. Choosing different states for S and B or A and W is forbidden. The same state definitions and bit ordering are used in development, 2019, test evaluation, bootstrap replicates, and permutations. State zero is not ordinary missingness and must not generate a hidden availability proxy beyond the explicitly represented report state.

## Frozen laboratory-independent information sets

All primary models remain interpretable elastic-net logistic regressions. Their only change from the parent is the fitting objective below.

**B — deployable structured/basic-report baseline**

- age and sex;
- CT/MRI indicators and development-frequency machine-availability category, never a raw identifier;
- only in report-available states, frozen extractions for maximum lesion diameter, lesion count (1, 2, at least 3), and explicit macrovascular tumor thrombus, each with unknown indicators.

B contains no laboratory lineage, semantic `C_R` feature, report formatting, year, diagnosis, procedure text, pathology, raw identifier, or post-cutoff content.

**S — deployable radiology-semantic strategy**

Exactly B plus `C_R`, exposed only in report-available states: frozen present/absent/unknown extractions from `检查所见` and `检查诊断` for complete/interrupted/absent capsule, irregular or non-smooth margin, satellite/peritumoral lesion or enhancement, arterial hyperenhancement, washout, and peritumoral hypointensity.

S contains no examination/report code, raw machine identifier, formatting/template family, accession number, year, laboratory field, procedure/diagnosis/pathology term, unrestricted n-gram, or post-cutoff content.

**W — workflow/provenance negative control**

Exactly B plus acquisition count and time since last acquisition; reviewed non-semantic protocol category from exact `检查`; development-frequency machine category; and, only in report-available states, character/line/section counts and outcome-blind formatting family. Construct formatting family in 2015–2018 after masking clinical words, numbers, dates, identifiers, and values, using punctuation, line breaks, section order, and repeated boilerplate. Unseen formats map to “unseen.” W has no `C_R` or laboratory field and is not deployable.

**A — process-adjusted semantic model**

Exactly `W+C_R`, with `C_R` bit-for-bit identical to S's added block. Thus A-W is nested and asks whether the same semantic block adds modeled information beyond measured workflow/provenance. It is not a causal estimand and A is not the proposed deployment strategy.

**U — diagnostic unrestricted-text ceiling**

A plus report-available, development-fitted character 3–5-gram TF-IDF after removing identifiers, dates, accession strings, pathology/MVI terms, and postoperative text. Audit the 100 largest absolute coefficients before test outcomes. U has no laboratory lineage and cannot rescue either claim.

Two blinded radiologists review at least 200 reports for B's size/count/thrombus extraction and, separately in each test year and CT/MRI provenance, at least 150 reports enriched for each `C_R` feature and parser-negative examples. Require size agreement within 5 mm or 10% in at least 90%, count-category agreement at least 90% with kappa at least 0.80, and per-year/per-modality PPV and sensitivity at least 0.85 for every binary `C_R` feature. This validates interpretation of stored text, not its visibility at `t_dec`.

## Primary patient-wise report-state-robust fitting

For model `M`, patient `i`, state `r`, binary outcome `y_i`, and linear predictor `eta_Mi(r;theta)=theta_0+x_Mi(r)'theta`, define logistic loss

`ell_iM(r;theta)=log(1+exp(eta_Mi(r;theta)))-y_i*eta_Mi(r;theta)`.

For every alpha/penalty pair in the frozen grid, fit on `V=1` 2015–2018 patients by

`theta_hat_M = argmin_theta { n_dev^-1 sum_i max_{r in Omega_i^R} ell_iM(r;theta) + lambda[alpha||theta||_1 +(1-alpha)||theta||_2^2/2] }`.

The maximum is patient-wise: it permits report availability to be associated with outcome and covariates and equals the worst loss over the full Cartesian product of allowed patient states. It assigns no state probability. Because a maximum of convex logistic losses plus an elastic-net penalty is convex, fit it exactly with one epigraph variable `z_i` and constraints `z_i >= ell_iM(r;theta)` for every feasible state. Use deterministic solver tolerances, fixed seeds only where needed, and a declared tie rule. Verify the solution against brute-force state-loss evaluation and primal feasibility.

Patient-level preprocessing is development-only and state-invariant. Age is scaled once per patient. Frozen report numeric parsing and units are applied before masking; report-derived scaling constants may use eventual 2015–2018 stored reports without outcome but may not expose content at state zero. Categorical levels and formatting families are development-frozen. No test distribution changes preprocessing.

For each candidate penalty, compute 2019 patient-wise worst-state log loss `n_2019^-1 sum_i max_r ell_iM(r;theta_hat)`. Choose the simplest penalty within one patient-bootstrap standard error of the minimum, using the inherited frozen simplicity/tie rule. Then estimate a single recalibration intercept `a` and slope `b>=0` on 2019 by minimizing `sum_i max_r ell(y_i,a+b*eta_hat_i(r))`. Do not refit features in 2019. A zero slope is permitted computationally but will generally fail discrimination/calibration gates.

Every model must score every test patient in every state. Every one of the 2,000 bootstrap replicates resamples patients, rebuilds state vectors, refits preprocessing, robust elastic-net models, tuning, and robust recalibration, then recomputes test bounds.

The parent's equal-weight state-augmentation fit is retained as a named diagnostic `E`, along with all-report and no-report fits. These can quantify training-state fragility but cannot support, rescue, refute, or narrow C or A. Calling equal weighting an estimated availability distribution is forbidden.

## Exact joint test estimands

For threshold `p`, let `w=p/(1-p)`, `I_Mi(r,p)=1[score_Mi(r)>=p]`, and for contrast `k=(M_1,M_0)` define

`d_i^k(y,r,p)=[y-w(1-y)]*[I_M1i(r,p)-I_M0i(r,p)]`.

For `V_i=1`,

`L_k(p)=N^-1 sum_i min_{r in Omega_i^R} d_i^k(Y_i,r,p)`

and

`U_k(p)=N^-1 sum_i max_{r in Omega_i^R} d_i^k(Y_i,r,p)`.

For `V_i=0`, each minimum and maximum additionally ranges over `y in {0,1}`. `N` is the entire 2020–2021 target frame. With at most four report states and two endpoint states, enumerate every state exactly. No patient is dropped or imputed.

Compute bounds for S-B (C), A-W (A), descriptive S-W and S-U, and every model versus flag-none and flag-all. For one model's net benefit, flag-none has action zero and flag-all action one; uncertain Y is enumerated identically.

The intervals are coordinatewise sharp because patient states and missing outcomes are otherwise unrestricted. Endpoints from different contrasts or thresholds may require different latent assignments and must not be described as one joint world. The lower endpoint is a conservative guarantee over allowed states, not an estimate of an actual visibility distribution.

Primary `p=0.30`; evaluate `p=0.20,0.21,...,0.40`; the 0.25–0.35 plateau is a robustness range, not an elicited preference. Report flags and incremental flags by state. At 0.30 decompose interval width into pathology ambiguity with all reports exposed, report ambiguity among `V=1`, and full joint ambiguity; report the fraction of patients whose action changes across states.

## Inference, falsification, and diagnostics

Use 2,000 patient bootstraps, resampling patients within calendar period and retaining all rows/states. The simultaneous family contains L and U endpoints for S-B, A-W, S-W, and S versus both defaults at all 21 thresholds. Use the 95th percentile of the maximum absolute centered bootstrap deviation on the net-benefit scale for one two-sided 95% simultaneous band; report pointwise percentile intervals separately. Do not studentize zero-variance coordinates. More than 2.5% failed robust fits or bootstrap replicates fails inference.

Run 1,000 process-matched semantic-null repetitions for A. Within each development/tuning period, permute the entire `C_R` block between patients within frozen year, CT/MRI acquisition provenance, report-state cardinality, and formatting-family availability, with prespecified coarsening when a cell has fewer than 20 patients. Keep B/W variables, Y/V, patient grouping, and state masks fixed; robustly refit and recalibrate A. Observed `L_A-W(0.30)` must exceed the 97.5th percentile. Full-patient C_R shuffle and label permutation must yield intervals compatible with zero. Post-cutoff models are leakage demonstrations only.

Required sensitivities are 12/48/72-hour buffers and the previously treated cohort. At 0.30 report bounds by test year, sex, age below/at least 65, and CT-only/MRI-only/dual acquisition; for attribution also report the four largest test formatting families and pool the rest. Suppress inferential claims below 100 patients or 20 `V=1` M2 events. Among `V=1`, report paired AUPRC, AUROC, Brier, calibration intercept/slope, sensitivity, specificity, PPV, and NPV in all-report and no-report scenarios, labeled selection-sensitive. A model for V using pre-`t_dec` B, year, and template availability is descriptive only; inverse weighting does not identify missing grades or report states.

Laboratory audits remain segregated: describe eligible exact assay/specimen rows, invalid clocks, ties, and distance to `t_dec`; optionally reproduce eventual-record lab models under all-record and lag masks, all labeled “visibility unverified.” Before any oracle state analysis emit selected lab-row count `m_i` and `2^(m_i+q_i)`; any per-row state must mask the entire row-derived vector and be shared across compared oracle models. No lab analysis can support, rescue, refute, or narrow C/A.

## Feasibility, validity, and reliability gates

Global interpretation requires:

- test N at least 1,000, at least 75 adjudicated `V=1` M2 outcomes, `V=1` at least 85%, and review of every test V=0;
- both pathology parsers and pathology/radiology reliability thresholds above;
- identical patients and shared state bit ordering/masking across models;
- exact masking of every report-derived variable at state zero and absence of forbidden/post-cutoff features;
- machine-checkable zero-column and zero-lineage intersection between every primary matrix/pipeline/stratum and every labs field or derivative;
- all-report nonempty text in at least 80% of the frame and B size/count jointly extractable in at least 70%;
- no required primary variable's missingness shifting more than 15 percentage points from 2019 to either test year; report unseen template and machine-category drift;
- in both all-report and no-report V=1 diagnostics, S recalibration slope 0.80–1.20, intercept -0.10–0.10, sensitivity at least 0.70, and PPV at least 0.50 at 0.30;
- at least 100 patients and 20 V=1 M2 in each estimable CT-only and MRI-only analysis; failure limits modality-specific generality and a harmful stratum forbids cross-modality robustness;
- robust objective convergence, epigraph feasibility, deterministic repeated-fit agreement, brute-force loss checks, complete bootstrap output, and exact bound unit tests.

C uses global, endpoint, extraction, calibration, robust-fit, and bootstrap gates. A additionally requires valid workflow masks, at least 20 patients in terminal permutation blocks after coarsening, and estimable null repetitions. An A-only gate failure makes A inconclusive, not C. Equal-weight diagnostic disagreement is reported but does not invalidate a converged robust primary estimate.

## Prespecified supportive, adverse, and inconclusive zones

**C supportive:** every C gate passes; the simultaneous lower confidence limit for `L_S-B(0.30)` exceeds 0.01; the simultaneous lower limit for `L_S-B(p)` exceeds zero at every p from 0.25 through 0.35; S's lower-bound net benefit simultaneously exceeds flag-all and flag-none throughout that plateau; and neither test year's point lower bound is negative. The strongest allowed conclusion is: “The laboratory-independent, report-state-robust S policy had a material, threshold-robust historical weighted M2 classification increment over identically fitted B in the 2020–2021 institutional first-resection frame under the declared report/pathology uncertainty.”

**C adverse:** with gates passed, the simultaneous upper confidence limit for `U_S-B(0.30)` is below 0.01, ruling out the prespecified material increment; an upper limit below zero supports classification harm. Failure to beat a default is adverse at that threshold. Better AUPRC, equal-weight/all-report success, or oracle-lab success cannot rescue an adverse primary result.

**C inconclusive:** a gate fails or the simultaneous band spans 0.01. A positive point estimate with an interval spanning no material increment is inconclusive. Name whether robust-fit instability, report/pathology width, extraction reliability, event count, calibration, or sampling uncertainty dominates.

**A supportive:** every A gate passes; the simultaneous lower confidence limit for `L_A-W(p)` is above zero at every p from 0.25 through 0.35; and observed 0.30 exceeds the matched-null 97.5th percentile. The strongest allowed conclusion is incremental modeled radiology-semantic information beyond measured workflow/provenance—not causality.

**A adverse:** with gates passed, the simultaneous upper limit for `U_A-W` is at or below zero at any required plateau threshold, or the observed statistic fails to exceed the matched null. This falsifies robust attribution even if C is positive.

**A inconclusive:** reliability, overlap, robust-fit, permutation, or inference gates fail, or simultaneous bands span zero. This does not alter C.

Joint interpretation is mandatory: dual support permits both bounded statements; C support with A adverse/inconclusive forbids characterizing the deployable increment as semantic rather than workflow-related; A support with C adverse/inconclusive establishes no material deployable increment; adverse results falsify only their prespecified historical classification hypotheses; inconclusive results must not be relabeled absence of association.

Even dual support cannot establish acceptable clinical thresholds, changed clinician decisions, improved treatment selection, recurrence, survival, quality of life, harms, capacity effects, or cost-effectiveness. Those claims require report finalization/view timestamps, stakeholder threshold elicitation, prospective workflow capture, treatment and follow-up outcomes, and another study. External or contemporary transport requires independent hospitals and prospectively verified predictor availability.

## Exact HCC source bindings

Snapshot `[source checksum]`. Every source is an ordinary read-only CSV; archive member is none. Direct headers and the catalog were inspected.

| Table; exact source path | Required columns and role |
|---|---|
| `encounters`; `[internal dataset path]` | `患者主索引,就诊号` join; `年龄,性别` predictors; `就诊时间,入院时间,出院时间` chronology. Names and direct identifiers excluded. |
| `procedures`; `[internal dataset path]` | keys; `手术,手术来源,开始时间,结束时间` for first index, t_dec, tie audit, and prior-treatment exclusion. |
| `examinations`; `[internal dataset path]` | keys; `检查,检查所见,检查诊断,开始时间,机器型号,检查号` for acquisition eligibility, bundling, state masks, B/C_R extraction, and W provenance. No report finalization/view time or images. |
| `labs`; `[internal dataset path]`; [source checksum] | keys; `检验,定性结果,定量结果,标本类型,检验时间` for non-primary audit/oracle diagnostics only. No unit, collection, result-entry, verification, release, view, panel, or accession. Zero primary lineage. |
| `pathology`; `[internal dataset path]` | keys; `病理,检查所见,检查诊断` for HCC frame, specimen-link review, grade/conflict, Y/V; `机器型号` dedup audit only. No time, specimen ID, slide, block count, or sampling field; never predicts. |
| `medications`; `[internal dataset path]` | keys; `用药,药品类型,开始时间,结束时间` for prior systemic-treatment exclusion only. |
| `orders`; `[internal dataset path]` | keys; `医嘱(非药品),开立时间,开始时间,结束时间,医嘱状态` for prior local/radiotherapy exclusion only. |
| `diagnoses`; `[internal dataset path]` | keys; `诊断名称,诊断类型` for untimed HCC corroboration only; never predicts. |

After exact-row deduplication, same-encounter links use `(患者主索引,就诊号)` and must not multiply rows silently. Longitudinal imaging, procedures, medications, orders, and diagnostic-only labs link on `患者主索引` plus valid source times and frozen windows. Untimed documents/diagnoses, identifier-only vitals/transfers/front page, direct identifiers, post-`t_dec` content, and all laboratory-derived data are excluded from predictors.

The configured MIMIC, eICU, and UKB datasets remain directly accessible under `datasets/mimic`, `datasets/eicu`, and `datasets/ukb`, but cannot identify this frozen institutional HCC estimand and are not pooled.

## Compiler and verifier contract

The compiler must preserve the first-resection frame, no-recorded-treatment cohort, t_dec, 90/30/365-day windows, bundle selection, 2015–2018/2019/2020–2021 split, pathology-only Y/V endpoint, whole-frame denominator, shared report states, B/S/W/A nesting, radiology-only C_R, S-B and A-W estimands, descriptive S-W, thresholds, exact extrema, simultaneous family, gates, and result zones. It must implement the patient-wise maximum-loss fitting/tuning/recalibration objective. Replacing it with equal-state weighting, imputation, observed-text-only fitting, or a probability model is a scientific change requiring a Lead-approved child.

Required artifacts are source hashes/headers; raw dictionary frequencies; attrition and join tables; one index/t_dec per patient; selected/discarded bundles; every state and masked vector; Y/V provenance; preprocessing constants; for every fit, per-patient per-state losses, maximizing-state indices, epigraph residuals, objective and convergence trace; selected penalty and 2019 worst-state loss; robust recalibration; state-specific scores/actions; per-patient bound contributions; width decomposition; bootstrap bands; permutation outputs; diagnostic-fit labels; zero-lab lineage proof; and machine-readable conclusion-to-output links.

Computationally checkable claims include source/header agreement, dictionary use, dedup/joins, period disjointness, windows, one index, state construction/masking, same state in each contrast, absence of forbidden/post-cutoff/lab features, B subset S, B subset W, W subset A, identical C_R in S/A, robust epigraph inequalities and objective arithmetic, held-out worst-state tuning, nonnegative recalibration slope, full-pipeline bootstrap refitting, anchored pathology fixtures including selected M0 followed by M2 boilerplate remaining M0, V=0 enumeration, whole-frame N, exact bounds, simultaneous maximum-deviation critical value, permutation blocking, suppression rules, and conclusion links.

Verifier fixtures must include:

- a tiny analytically solvable data set where equal-weight and robust fits differ, and fail any submission using equal weights as primary;
- one- and two-report patients proving `max_r loss` is evaluated over 2 and 4 states, with state masks shared across models;
- correct supportive outputs with only the bounded historical wording;
- adverse outputs including best-case upper limits below 0.01 or below zero, requiring adverse interpretation;
- inconclusive outputs with positive points but simultaneous bands crossing 0.01/zero, requiring inconclusive interpretation;
- numerically correct results followed by unsupported treatment, recurrence, survival, patient-benefit, causal, threshold-acceptable, contemporary, or external-transport conclusions, which fail;
- all-report, equal-weight, or oracle-lab success presented as primary support, which fails;
- any lab value, row presence/missingness, assay/specimen, count, or time derivative in a primary matrix, stratum, or serialized pipeline, which fails;
- different report states across compared models, complete-case analysis, V=0 as M0, coordinatewise extrema called one latent world, pointwise intervals called simultaneous, threshold cherry-picking, S-W used as a gate, A-W called causal, or W/A called deployable, all of which fail.

Not automatically checkable are Chinese clinical semantics, reviewer qualifications, actual report finalization/visibility, actual laboratory visibility, specimen linkage, tissue sampling adequacy, biological M2, threshold acceptability, clinician response, patient benefit, or transportability. These require qualified pathology/radiology review, source-system timestamps, raw specimen/slide evidence, stakeholder elicitation, prospective workflow/outcome data, and/or another study. Reference execution establishes computational feasibility and whether conclusions follow from outputs; it does not establish scientific truth or clinical benefit.
