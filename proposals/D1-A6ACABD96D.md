# Preoperative HCC microvascular-invasion signal in longitudinal routine care

Status: new restart proposal with no scientific parent. The postoperative biomarker-surveillance branch is transition context only. Two bounded source audits were executed; no hypothesis model has been fitted and no predictive claim is yet supported.

## Question, evidence boundary, and advance

The clinical question is whether the ordering and co-evolution of preoperative laboratory measurements contains reproducible information about histologic microvascular invasion (MVI) beyond an ordinary last-value clinical snapshot in adults undergoing first recorded HCC resection. This matters before resection because suspected MVI may affect discussion of anatomic versus nonanatomic resection, margin strategy, neoadjuvant-study eligibility, and postoperative risk counseling. Prediction here is not proof that changing surgery or giving treatment improves outcomes.

The strongest evidence-supported claim is that a static score using AFP, tumor size, and tumor margin achieved C-statistics near 0.81 in two Chinese validation cohorts, while MVI itself is confirmed pathologically [K1]. Three-tier pathology grading defines M0 as no MVI, M1 as 1–5 foci within 1 cm, and M2 as more extensive or distant MVI; one retrospective series associated M2 with recurrence and mortality [K2]. Routine observation times can themselves encode clinician behavior and severity; methodology distinguishes value summaries, observation-process predictors, and latent structures, and warns that prediction is not explanation [K3].

The unresolved claim tested here is:

> Among adults with first recorded, pathology-confirmed HCC resection and at least two distinct preoperative numeric-laboratory days, a patient-level time-aware model of the same day −90 through −1 event history will improve temporally held-out prediction of M1/M2 versus M0 over a transparent latest-snapshot model, and that gain will remain when measurement-process information is ablated and after adjustment for tumor burden, liver reserve, treatment selection, and era.

The leading scientific explanation is that coordinated change in tumor-marker, liver-injury, synthetic-function, coagulation, and inflammatory measurements reflects invasive tumor biology not captured by one late snapshot. The strongest rivals are: (1) larger/multifocal tumors and poorer liver reserve cause both abnormal trajectories and MVI; (2) patients selected for repeated work-up are sicker or diagnostically uncertain, so measurement timing rather than values drives performance; (3) preoperative treatment changes values and selection; (4) tests drawn near admission or surgery encode timing and perioperative workflow; and (5) pathology template/sampling changes create label drift. The matched ablations and temporal tests separate predictive contributions but cannot identify a biological mechanism.

The substantive advance over inspected work is not another static nomogram. It is a falsifiable test of whether temporal order adds stable information beyond a transparent snapshot, with explicit measurement-process separation and temporal transport. A negative result would be clinically useful: it would favor the simpler score and discourage deployment of a fragile trajectory model.

## Observed feasibility evidence

The audit scripts and aggregate JSON are attached. Observed results, not model results:

- The pathology table has 46,395 rows. The parser found 12,350 HCC rows with an explicit first grade following `MVI提示风险分级:`; after encounter aggregation there were 12,193 nonconflicting explicit-grade encounters and 38 grade-conflict encounters.
- Linking explicit-grade encounters to a dated liver resection and retaining the earliest linked event per adult produced 10,808 patients in the broad audit: 6,940 M0, 2,400 M1, and 1,468 M2. A later check showed 455 had an earlier recorded qualifying resection, motivating the first-recorded-resection primary rule.
- In the broad cohort, 10,768 had at least one strict numeric laboratory result in days −90 through −1; 5,839 had values on at least two distinct days. Of the latter, 2,060 were M1/M2. The final strict calendar-day rerun, after requiring the first recorded qualifying resection and excluding recorded HCC-directed treatment in days −180 through −1, yielded 10,171 adults overall and 5,204 with at least two preoperative measurement days, including 1,950 M1/M2.
- Static measurement support is high: AFP was observed in 10,219 broad-cohort patients, PIVKA-II in 8,266, platelets in 9,565, albumin and bilirubin in about 7,830. There were 1,025,415 strict numeric preoperative rows.
- Preoperative examination reports existed in 10,706 patients; bounded lexical support was 10,311 for a size expression, 9,072 for margin/capsule language, and 4,876 for multiplicity/satellite language. These are extraction opportunities, not validated tumor features.
- The audit found strong calendar drift. In the corrected strict cohort, serial support was train 2014–2018: 2,210 (935 M1/M2); validation 2019: 992 (463); test 2020–2021: 1,365 (510); 2022–2023: 5 (1); stress 2024–2025: 632 (41). The late prevalence shift is a mandatory label/reporting stress test, not an extra random test set.
- The full-source audit completed in 57 seconds on 4 CPUs/32 GiB; this is measured preprocessing feasibility. No baseline or learned model has been fit.

These counts establish usable outcomes and event density. They do not validate the label parser, prove representativeness, or support the hypothesis.

## Population, clocks, and outcomes

Index time is the earliest recorded qualifying liver resection start timestamp per patient that is in the same `(患者主索引, 就诊号)` encounter as pathology text explicitly stating HCC and exactly one parseable MVI grade. A qualifying resection name contains liver and resection, excluding transplant/donor, biopsy/puncture, drainage, abscess/cyst, and isolated cholecystectomy terms. Duplicate procedure rows are collapsed before choosing the index.

Include age ≥18 and index years 2014–2021 for primary development/evaluation. Exclude missing procedure timestamp; encounter-level conflicting grades; no explicit MVI grade; any earlier recorded qualifying liver resection; and recorded embolization/intervention, ablation/radiofrequency/microwave, infusion/chemotherapy/radiotherapy, or targeted systemic treatment during calendar days −180 through −1. “No recorded prior treatment” is limited to these institutional files and is not lifetime treatment-naïve. Sensitivities exclude any such treatment at any prior recorded time and restrict to patients with no treatment language in blinded clinical review.

Prediction cutoff is the start of calendar day −1. Inputs are restricted to event timestamps in calendar days −90 through −1; same-day surgery measurements are prohibited. Require numeric measurements on at least two distinct calendar days. Collapse exact duplicate rows; for same-label/same-timestamp duplicates use the median only if all are strict numeric, otherwise mark ambiguous and do not convert inequalities. Labels are never pooled by value across different test names because units/platform/reference ranges are absent. Training-era rank/robust scaling is by exact label and calendar year, then frozen.

Primary outcome is MVI presence: M1 or M2 versus M0. Secondary outcome is the ordered M0/M1/M2 grade. M2 versus M0/M1 is exploratory because treatment relevance and sampling differ. The outcome is postoperative pathology and cannot be used in feature construction. MVI is not recurrence, survival, or treatment benefit.

Development split is temporal and frozen before fitting: 2014–2018 training; 2019 validation/model selection; 2020–2021 locked primary test. The near-empty 2022–2023 period is reported but not modeled. 2024–2025 is a reporting-drift stress set only; its low positive count prevents a strong discrimination conclusion. Within training, patient-level five-fold cross-fitting tunes models. No patient crosses sets.

## Inputs and matched methods

All models use the identical eligible patients, raw day −90:−1 event table, static demographics, and preoperative report-derived variables. No model may use pathology, postoperative events, procedure duration, intraoperative variables, or future encounter information.

### Transparent baseline B

Fit penalized logistic regression with training-only preprocessing. Inputs are age, sex, calendar year, service, latest strict numeric value for each training-supported exact lab label (minimum 100 training patients), days since that value, missing indicator, number of distinct measurement days, and prespecified interpretable features: AFP, PIVKA-II, platelets, albumin, bilirubin, ALT, AST, INR/PT, GGT, ALP, WBC, hemoglobin, creatinine, plus rule-extracted maximum lesion size, multiplicity, margin irregularity/capsule, and modality from the last eligible preoperative examination report. Continuous terms use restricted cubic splines for the prespecified clinical variables; other labels enter through elastic-net regularization. Publish a reduced three-feature AFP/size/margin benchmark where all three are available, but do not substitute it for B.

B is transparent and deployable. It loses the direction, synchrony, irregular spacing, transient peaks, and order of measurements.

### Learned temporal alternative T

Fit a modest time-aware masked transformer to the same events. Each token contains exact lab-label ID, robustly scaled numeric value, days-to-index, time since previous event, panel/day ID, and missing/ambiguous status. Static demographics and the same report-derived variables enter only after pooled temporal encoding. Use ≤4 layers, hidden width ≤128, ≤8 heads, dropout, class-weighted binary cross-entropy, early stopping on validation log loss, and five fixed seeds. Vocabulary, scaling, rare-label threshold, and truncation are training-frozen. Cap at 512 tokens with deterministic day-stratified retention that always retains the last value and preserves earlier days; report the fraction truncated.

Fit two locked ablations on the same cohort and architecture:

- `T-value`: values, label identity, and event order, but observation gaps/panel counts are masked to constants.
- `T-full`: adds timing, panel co-measurement, and observation intensity.

`T-value − B` tests whether learned temporal value structure adds information that hand summaries lose. `T-full − T-value` estimates predictive information in the observation process; it must never be called tumor biology. Attention weights or embeddings are descriptive only, not mechanistic explanations.

A Gaussian-process joint latent trajectory model was considered. It would estimate smooth shared liver-injury/synthetic/tumor-marker factors and be more mechanistically legible, but exact-label sparsity and irregular panels make multivariate fitting less robust at this scale. Revisit it if T shows stable gain and factor recovery in simulation; do not add it merely for complexity.

## Evaluation, falsification, and decision rules

Evaluate B, T-value, and T-full on the same locked test patients. Report AUROC, AUPRC, log loss, Brier score, calibration intercept/slope, calibration-in-the-large, and decision-curve net benefit at prespecified predicted-risk thresholds 0.20, 0.30, 0.40, and 0.50. Use 2,000 patient bootstrap replicates for paired 95% intervals. Report sensitivity, specificity, PPV, and NPV at one validation-selected threshold corresponding to 80% sensitivity; do not optimize on test. Report subgroup calibration by sex, age <65/≥65, tumor size ≤5/>5 cm, service, and year where n and events permit; suppress cells <20.

Primary supportive evidence requires all of: test `T-value − B` AUROC ≥0.02 with a paired 95% interval excluding 0; Brier improvement ≥0.01 with interval excluding 0; calibration slope 0.8–1.2 after validation-frozen recalibration; positive net benefit over B at at least two adjacent thresholds without material harm at others; and no direction reversal in 2019 versus 2020–2021. The 2024–2025 stress set can only corroborate calibration/drift, never rescue a failed primary test. T-full improvement alone is not biological support.

Mandatory falsifications are:

1. Randomly permute preoperative event order within patient while preserving values and observation counts. A genuine temporal-order gain should materially attenuate; persistence suggests static severity or leakage.
2. Shift the cutoff to day −7 and repeat. Collapse to latest-day-only. If the gain exists only immediately before surgery, perioperative timing/workflow is favored.
3. Compare T-value and T-full. Gain only in T-full favors measurement/selection behavior.
4. Exclude any prior recorded directed treatment at any time; stratify by recorded prior treatment and service. A reversal favors treatment selection.
5. Fit report-only, labs-only, and demographics/observation-only controls. A trajectory claim requires value-sequence gain beyond report-defined tumor burden and measurement intensity.
6. Leave-one-year-out training analyses; report prevalence and calibration by year. Failure under ordinary 2019–2021 transport favors era/platform drift.
7. Repeat after same-day panel collapse and exact-label restriction; perform outcome-label permutation and feature-time leakage tests.
8. Before model fitting, a hepatopathologist blinded to predictors reviews a stratified random 200 pathology encounters (50 each M0/M1/M2 plus 50 conflicts/era-shift cases) against the parser. Require ≥95% grade accuracy overall and ≥90% in each era/grade stratum. A radiologist/hepatobiliary clinician reviews 200 report extractions for size, multiplicity, and margin/capsule. These are clinical adjudication gates, not automatic checks.

Adverse evidence is a precise test result excluding the prespecified material gain, T-value matching B while T-full gains, order permutation failing to reduce gain, or stable B performance with temporal-model miscalibration. This favors a static severity snapshot and/or observation process over added temporal value structure.

Inconclusive evidence includes broad paired intervals, failed label/report adjudication, marked year-specific reversal, severe calibration failure, insufficient subgroup events, dependency/training instability, or an apparent gain confined to day −1 workflow. An imprecise null does not refute temporal biology; it means this snapshot cannot distinguish it.

Support would establish internally and temporally held-out predictive utility of the available preoperative sequence. It would not establish that trajectories cause MVI, identify a mechanism, generalize outside this institution, or prove that changing surgery/treatment improves outcomes. Those claims require external prospective validation, standardized assays and imaging, pathology review, and a decision-impact or treatment study.

## Exact source bindings

Sources are read-only ordinary CSVs under snapshot `[source checksum]`. Join within encounter on `(患者主索引, 就诊号)`; link longitudinally on `患者主索引`; prefer native event timestamps. Derived files go only to the workspace.

- `pathology`: `[internal dataset path]`; columns `患者主索引, 就诊号, 病理, 检查所见, 检查诊断, 机器型号`. No native time. Supplies only same-encounter HCC confirmation and explicit first MVI grade after `MVI提示风险分级:`; it is never an input.
- `procedures`: `[internal dataset path]`; `患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源`. Supplies index, prior resection, and recorded locoregional treatment.
- `encounters`: `[internal dataset path]`; `患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室`. Supplies age, sex, service; names and direct identifiers are prohibited.
- `labs`: `[internal dataset path]`; `患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间`. Supplies exact-label sequence. No unit/platform/reference-range column exists.
- `examinations`: `[internal dataset path]`; `患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 机器型号, 检查号`. Supplies only pre-cutoff report-derived tumor burden/margin/modality; raw images are unavailable.
- `medications`: `[internal dataset path]`; `患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型`. Adds systemic-treatment exclusion/sensitivity; indication is unavailable.
- `diagnoses`: `[internal dataset path]`; `患者主索引, 就诊号, 诊断名称, 诊断类型`. No native time; audit only, never temporal input.
- `clinical_documents`: `[internal dataset path]`; encounter keys plus complaint/history/admission/course/discharge/procedure text. Used only for blinded treatment/selection review, not automatic truth.

Mortality, recurrence, outside treatment, complete treatment intent, assay units/platform, raw images, pathology block count, and specimen sampling protocol are unavailable. The nominal vitals, transfers, and front-page tables have no usable payload for this question. All four configured datasets remain directly accessible and read-only through `datasets/README.md`; only HCC is analyzed.

## Solver-computable deliverable and resources

The solver must newly produce: immutable cohort and exclusion flow; parser/adjudication sample manifest; year/grade/event-support tables; frozen preprocessing dictionaries; B, reduced benchmark, T-value, and T-full fits with five seeds; validation tuning records; locked-test predictions; paired uncertainty and calibration/decision outputs; all falsification results; and a machine-readable conclusion mapped to supportive/adverse/inconclusive rules. Completion is established by those files, not by confirming the hypothesis.

Measured discovery cost was 57 seconds on 4 CPU/32 GiB for a full-source audit. Planned full run: preprocessing and baseline on 8–16 CPUs, ≤64 GiB, approximately 1–2 hours; five-seed transformer/ablations on one allocated A100 80 GiB plus 8 CPUs/64 GiB, approximately 3–6 hours; bootstrap/evaluation on 16 CPUs, approximately 1–2 hours. These training estimates are unverified but fit the solver envelope (16 CPUs, 8 GPUs, 256 GiB, 8 hours). Request one GPU; use `cuda:0` inside the allocation. Cached `ehr-campaign-gpu:20260908` should be probed for Python, pandas, pyarrow, scikit-learn, statsmodels, and PyTorch; install only missing declared dependencies. No discovery GPU pilot is scientifically necessary.

An automatic verifier can check hashes, schema/columns, joins, timestamps, exclusion flow, parser regex, no post-cutoff or pathology leakage, split isolation, preprocessing fit only on training, model/seed completion, metric arithmetic, paired bootstrap, thresholds, falsification execution, and whether the submitted interpretation follows the computed rule. It must test a correct computation paired with an unsupported causal/treatment conclusion and appropriate interpretations of supportive, adverse, and inconclusive fixtures. It cannot establish pathology sampling adequacy, clinical meaning of report phrases, outside treatment, assay equivalence, mechanism, transportability, or benefit of a changed clinical decision.

## Alternatives and revisit triggers

- Static AFP/size/margin benchmark: retained as an inspected-work comparator, not sufficient as the sole baseline.
- Transparent latest-snapshot B: selected because it is auditable and directly tests whether sequence information is needed.
- T-value: selected substantive alternative; reveals ordering, synchrony, spacing, and transient dynamics lost by B.
- T-full: selected measurement-process ablation; predictive only, never biological.
- Multivariate GP latent-factor model: deferred until sequence gain and factor recoverability are shown.
- Report-text transformer/radiomics: deferred. Raw images are absent and unvalidated report embeddings would confound the central temporal-lab question.
- Postoperative recurrence/survival: not available reliably; not used as a surrogate endpoint.
- 2024–2025 fitting: prohibited as primary confirmation because of label/prevalence drift; retained only as stress evidence.

## Compact bibliography

[K1] Xu J, Zhang YL, Yang M, et al. Preoperative Prediction of Microvascular Invasion in Hepatocellular Carcinoma: A Chinese Retrospective Multicenter Study Based on Global Meta-Analysis. *Cancer Medicine*. 2026;15:e71749. doi:10.1002/cam4.71749.

[K2] Li Z, Xu L, Liu X, et al. Comparisons of clinical patterns, short- and long-term prognostic outcomes in patients stratified by the severity of microvascular invasion after curative resection for hepatocellular carcinoma. *World Journal of Surgical Oncology*. 2026;24:132. doi:10.1186/s12957-026-04229-2.

[K3] Sisk R, Lin L, Sperrin M, et al. Informative presence and observation in routine health data: A review of methodology for clinical risk prediction. *Journal of the American Medical Informatics Association*. 2021;28:155–166. doi:10.1093/jamia/ocaa242.
