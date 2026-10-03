# Pre-diagnosis physiologic reserve and competing mortality after colorectal cancer

Status: independent delivery-ready branch from expert seed 36 and parent `[prior hypothesis]`. This is a planned Harbor experiment; no participant-level hypothesis fit or result is claimed.

## Scientific opening and clinical importance

The strongest inspected evidence supports a narrower claim than the seed's mechanistic language. In a diagnosed, treated CRC cohort, tumor factors were associated with CRC mortality while age, anemia and poor functional status were associated with non-CRC mortality under competing-risk analysis [K1]. In older stage I-III survivors who had already received definitive surgery and survived five recurrence-free years, other-cause mortality exceeded cancer-specific mortality and stage predicted late recurrence [K2]. Preoperative handgrip strength and frailty were associated with postoperative loss of independence in a small CRC surgical cohort, but that study did not establish long-term cause-specific mortality [K3].

The unresolved clinical question is whether a physiologic-reserve signal measured before CRC diagnosis can identify patients whose post-diagnosis mortality is more likely to be non-cancer than CRC mortality. That could change survivorship planning: a signal that is specific to non-cancer mortality would support external validation of intensified cardiovascular, renal, nutritional or functional assessment alongside oncology follow-up. It would not by itself justify a referral or treatment rule.

The strongest rival is diagnosis-related and treatment-selection bias: low reserve may be a marker of occult, proximally symptomatic CRC, advanced stage, emergency presentation, or later treatment intolerance. The configured data do not contain stage, grade, metastasis, treatment, symptoms, indication, pathology, recurrence, performance status, or chemotherapy tolerance. A remote measurement and a two-year washout can test diagnosis proximity, but cannot eliminate stage/treatment selection. A second rival is ordinary frailty: a low reserve score may simply summarize age, comorbidity and low function rather than a CRC-specific process.

## Falsifiable hypothesis and estimand

Primary hypothesis H1: among UKB participants with a first registry-recorded CRC diagnosis at least 730 days and at most 3,650 days after the baseline assessment, lower pre-diagnosis reserve is associated with a larger 5-year cumulative incidence of non-cancer death after CRC diagnosis than of CRC death. Formally, for the prespecified low-versus-high reserve contrast,

`D = [CIF_non-cancer(5y | low) - CIF_non-cancer(5y | high)] -
    [CIF_CRC(5y | low) - CIF_CRC(5y | high)]`.

The primary claim is that `D > 0`, not that reserve causes death, identifies a mechanism, or improves treatment decisions. The same contrast is estimated at 1 and 3 years and in the near-diagnosis rival window (0-730 days). Other primary-cancer deaths are a third competing event, not silently merged with either endpoint.

Supportive evidence requires a positive 95% bootstrap interval for `D`, a low-to-high non-cancer absolute-risk difference of at least 2 percentage points at 5 years, and the same direction in the delayed window and temporal holdout. Adverse evidence is a non-positive delayed-window contrast with an upper 95% interval below zero, or a CRC contrast at least as large as the non-cancer contrast with an upper interval below zero. Inconclusive evidence is an interval crossing zero, fewer than 50 CRC deaths or fewer than 50 non-cancer deaths in the primary risk set, or failure of the outcome/date audit. A near-window-only association supports the diagnosis-proximity rival rather than H1.

These criteria are deliberately about a descriptive/prognostic competing-risk association. Support would not establish a physiologic mechanism, treatment tolerance, causal effect of reserve, or clinical utility. An adverse result would argue against this reserve contrast for the proposed survivorship use, not against frailty as a general prognostic construct. A stage/treatment explanation remains unresolved without linked cancer registry or oncology records.

## Exact population, timing and outcomes

Use one read-only source and no participant join:

- Source path: `[internal dataset path]`.
- Source ID: `[UKB data file]`; [source checksum]; 502,371 rows; identifier namespace `ukb671626`.
- Catalog table: `datasets/ukb/table-5d49a6760e7ffdbd.json` (schema file [source checksum]), table name/lineage `ukb671626.csv (Parquet)`, id key `eid`, ordinary-file archive member. The catalog's UKB source entry is `[UKB data file]` with the corresponding read-only CSV path and source hash `[source checksum]`; the Parquet derivative is the execution input.
- Baseline assessment date is `53-0.0`. Use baseline sex `31-0.0`, birth year `34-0.0`, age `21003-0.0`, BMI `21001-0.0`, smoking `20116-0.0`, and assessment date/year for prespecified adjustment and selection reporting.
- Reserve inputs, all at instance 0, are left/right hand grip `46-0.0`, `47-0.0`; albumin `30600-0.0`; creatinine `30700-0.0`; cystatin C `30720-0.0`; and haemoglobin `30020-0.0` if present in the schema. The readiness check must verify `30020-0.0` before including it; if absent, the primary score uses the five verified seed fields and reports the change. No later assessment or post-diagnosis measurement is used in H1.
- Registry cancer diagnosis date/code pairs are `40005-j.0` and `40006-j.0`, `j=0,ldots,20`. Normalize code strings to uppercase and identify CRC by ICD-10 prefix C18, C19 or C20. For each participant, `T_CRC` is the earliest paired date whose code matches. Do not pair a date from one array member with another code member.
- The primary cohort requires nonmissing `53-0.0`, a valid first `T_CRC`, `730 <= T_CRC - 53-0.0 <= 3650` days, and a valid baseline reserve vector. The measurement is therefore pre-diagnosis by at least two years. Preserve the 0-730-day cohort as a prespecified proximity-rival analysis, not as an after-the-fact exclusion.
- Death date and underlying cause are `40000-0.0` and `40001-0.0`. Define CRC death as cause C18-C20; non-cancer death as a nonmissing cause outside C00-C97; other cancer death as C00-C97 excluding C18-C20. Treat other cancer death, unknown cause and censoring as competing/uncertain categories according to the frozen outcome table; do not classify an unknown cause as non-cancer. Set administrative censoring deterministically to the maximum valid `40000-0.0` date in the frozen source, recorded before modeling, and censor any follow-up beyond it.
- For source-robustness only, inspect paired inpatient diagnosis/date members `41270-0.k` and `41280-0.k`, `k=0,ldots,258`, in the same namespace. If both fields are sufficiently populated, derive an alternate first CRC date using the same C18-C20 rule and repeat the primary analysis. If the paired source is sparse or code semantics cannot be verified, report it as unavailable rather than replacing the registry outcome.

The readiness output must include participant flow, valid date ranges, missingness and overlap for every reserve component, event counts by cause, and the number of primary-cohort participants with each outcome. These are checks, not hypothesis results.

## Exposure construction and baseline

Within the eligible assessment population, estimate component means and standard deviations using assessment data only, with all choices frozen before inspecting death outcomes. Residualize each continuous reserve component for baseline age and sex using a prespecified linear fit in the eligible non-CRC assessment population, standardize, reverse the signs for creatinine and cystatin C, and average available components when at least four of the five verified seed components are present. The primary low/high contrast is the bottom versus top quartile of this composite, with the cutpoints computed in the development population and applied unchanged to the temporal holdout. Report the complete-case sensitivity requiring all five components and a no-residualization sensitivity. If haemoglobin is verified and included, it is an added sensitivity component, not a silent primary change.

The interpretable baseline is a cause-specific Cox model for CRC death, non-cancer death and other-cancer death with the reserve score, baseline age, sex, BMI, smoking, assessment year, and diagnosis-gap category. The reserve score has one prespecified coefficient per cause and one reserve-by-cause contrast; cumulative incidence is obtained through Aalen-Johansen standardization. Report hazard ratios only as secondary summaries. Use 1,000 participant bootstrap resamples stratified by event category for confidence intervals, with the bootstrap unit always `eid`.

## Substantive learned alternative

Fit a same-input, competing-risk discrete-time gradient-boosted hazard model (one cause-specific hazard head per event) using the six raw reserve measurements, age, sex, BMI, smoking, assessment year and diagnosis gap. The target is the one-year interval event indicator from CRC diagnosis through the frozen administrative end date; a person contributes only while event-free. Use the earliest 70% of distinct CRC diagnosis years for development and the remaining 30% for temporal holdout, with the split determined from diagnosis years before model fitting and shared by both methods. No inpatient labels, post-diagnosis values, stage surrogates or death-derived predictors may enter the feature matrix.

This learned model is scientifically substantive because it can reveal nonlinear reserve thresholds, grip/renal/albumin interactions, and whether the equal-weight score hides opposing dimensions for non-cancer versus CRC death. Compare it with the linear baseline on 1-, 3- and 5-year cause-specific calibration, cause-specific Brier score, integrated Brier score, log loss and population-standardized CIF contrasts. Use permutation ablation by reserve component and reliability plots; predictive improvement alone is not evidence of a mechanism or clinical value.

Method-selection record: retain both methods in the experiment. The baseline is preferred for the primary scientific contrast because its cause-specific coefficients and standardized absolute risks are auditable. The learned model is retained as an alternative explanation probe, not as a replacement chosen for a small performance gain. If the learned model only improves discrimination without stable calibration or a reproducible reserve interaction in the temporal holdout, defer it and report the baseline result. If the baseline and learned model disagree materially, treat that as model uncertainty requiring expert review, not as evidence favoring the hypothesis.

Approximate future envelope: CPU, four cores and 16 GiB RAM; one Parquet scan plus preprocessing, bootstrap baseline fits and a modest boosted model should be budgeted for at most about two hours, with a checkpoint after cohort construction and before bootstrap. This estimate is provisional because the discovery scan is a packaging/availability audit, not a full fit. No GPU is required for this tabular experiment; the deployment hardware guidance says allocated CUDA is available but does not make GPU use scientifically necessary.

## Falsification, robustness and interpretation

1. Proximity: repeat 0-730 days and 730-3650 days. H1 should persist in the delayed band; disappearance after the washout supports occult-disease/diagnostic activity.
2. Timing direction: within the delayed band, compare 730-1825 versus 1826-3650 days. A steep monotone increase toward diagnosis is adverse to a durable reserve interpretation.
3. Cancer specificity: repeat with other-cancer death as the target and CRC death/non-cancer death as competitors. A uniform association with every cancer cause suggests generic illness or selection rather than the stated cause contrast.
4. Source ascertainment: compare registry-only and paired inpatient-derived diagnosis entry when available. Large divergence suggests capture/healthcare-use selection.
5. Label permutation: permute cause labels within diagnosis-year strata while preserving event time and censoring. Any apparent reserve-by-cause contrast under permutation indicates an analysis bug or instability.
6. Measurement permutation: permute reserve vectors within sex and assessment-year strata. The primary contrast should disappear; persistence indicates leakage or coding error.
7. Missingness and repeat-observation selection: report complete-case, inverse-probability-of-observation weighted, and available-component analyses. If the result changes sign, it is inconclusive.
8. Calendar and age: report age-stratified and assessment-era estimates; do not claim effect modification unless interaction uncertainty is reported.
9. Treatment/stage boundary: do not adjust for unavailable stage or treatment and do not interpret residual association as treatment tolerance. A delivery conclusion must state that linked cancer registry, pathology, treatment, symptoms and clinical frailty adjudication are needed to resolve this rival.

## Actual scientific deliverable

Completion requires newly estimated, not merely packaged, outputs: (i) frozen cohort flow and reserve missingness audit; (ii) pre-specified reserve cutpoints and a dated competing-risk analysis dataset; (iii) cause-specific baseline coefficients and 1/3/5-year standardized CIFs with bootstrap uncertainty; (iv) temporal-holdout learned-model calibration and Brier/log-loss outputs; (v) the low-versus-high reserve `D` contrast with supportive/adverse/inconclusive classification; and (vi) the listed falsification and source-sensitivity results. No conclusion is complete unless its direction, uncertainty and exact computed output are reported.

## Three key references

[K1] García-Aranda et al., 2026, DOI 10.3390/jcm15114389. Prospective CRC competing-risk evidence for tumor versus vulnerability factors; abstract-level inspection only.

[K2] Yasin et al., 2026, DOI 10.1093/jncics/pkag002. Long-term survivor evidence that stage and other-cause mortality matter; abstract-level inspection only.

[K3] Zhao et al., 2026, DOI 10.3389/fonc.2026.1878444. Handgrip/frailty evidence bounded to early postoperative function; abstract-level inspection only.

The attached evidence excerpts and receipts are in `work/evidence-K1.txt`, `work/evidence-K2.txt`, `work/evidence-K3.txt`, and `work/key-references.json`.
