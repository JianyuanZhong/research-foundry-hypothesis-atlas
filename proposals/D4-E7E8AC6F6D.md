# UKB CBC cancer-type contrast: same-table ascertainment bridge and selection stress test

Status: proposed substantive child of [prior hypothesis]. No full solver or hypothesis test has been executed.

## What changed and why

The parent already made the delayed first-CBC CRC-versus-haematologic contrast primary and made repeat observation conditional. The remaining consequential rival is narrower: a registry date/code may be delayed or differently captured by cancer type, while the repeat-CBC population may be selected by clinical need that is not measured in UKB.

I audited the exact UKB guide, catalog, binding template and table JSON. The catalog contains Health Related Outcomes, Online Follow-up and Assessment Center derivatives, but those are namespace `ukb672073`; the CBC/registry source is namespace `ukb671626`. The catalog metadata explicitly disallows cross-namespace participant joins without a documented crosswalk. The Online Follow-up Parquet contains only `eid` and `20191-0.0`, and therefore cannot provide a valid laboratory indication or date bridge for this proposal. I reject those joins and do not change the primary population, temporal boundaries, estimand, outcome families or parent falsification logic.

The substantive repair is a same-table ascertainment bridge. In addition to the unchanged primary registry analysis, fit a prespecified outcome-source sensitivity using paired inpatient diagnosis/date arrays already present in the same `ukb671626` table: `41270-k.0` ICD-10 code with the same-index `41280-k.0` first-inpatient-diagnosis date, k=0,...,258. Compare registry and inpatient source estimates and, where both sources have a valid same-class event, describe their date displacement. This can expose source-specific timing or severity capture. It is not adjudication and cannot establish that either source is correct.

## Scientific opening and claim boundary

[K1] Hamilton et al. show clinically meaningful haemoglobin/anaemia associations with CRC in electronic primary-care records, but their matched CRC-versus-control case-control design does not test CRC specificity against haematologic cancer or registry timing. [K2] Sala et al. report pre-diagnostic longitudinal CBC trajectories in CRC patients, while calling the retrospective proof-of-concept investigational and requiring independent prospective validation. [K3] Hampton et al. find that colorectal risk models can discriminate but that calibration and external validation are often limited. These works support CBC–CRC associations and the value of timing/validation checks; they do not establish this UKB cancer-type contrast or resolve registry/clinical-selection artifacts.

The strongest evidence-supported claim is therefore only that haemoglobin and some longitudinal CBC summaries can associate with CRC-related outcomes in selected populations. The unresolved claim is:

> In adults without a registered cancer at a complete first UKB CBC, the prespecified higher-platelet/lower-haemoglobin phenotype is relatively more associated with CRC than with haematologic cancer in the delayed 2–5-year window, and this cancer-type contrast is not created by repeat-observation selection or by registry-specific timing/ascertainment.

This is descriptive/predictive, not causal, mechanistic, diagnostic, or a clinical-utility claim. A supportive result would justify an externally adjudicated validation study; a source-discordant or near-diagnostic result would redirect the question toward ascertainment and timing rather than a serial-CBC clinical rule.

## Exact source binding and audit

Read-only source and lineage:

- Dataset snapshot: `ukb-completed-subset-20261002`; catalog [source checksum].
- Catalog/guide: `datasets/README.md`, `datasets/ukb/README.md`, and `datasets/ukb/table-5d49a6760e7ffdbd.json`; table name `ukb671626.csv (Parquet)`; source ID `[UKB data file]`; 502,371 rows; ordinary file (no archive member); key `eid`; identifier namespace `ukb671626`.
- Bound Parquet: `[internal dataset path]`; [source checksum].
- Original lineage: `[internal dataset path]`; [source checksum].
- Binding target: `[internal dataset path]`; same Parquet SHA-256.

Required fields, all in that one table:

- Landmark dates `53-0.0`, `53-1.0`, `53-2.0`; T0, T1 and T2 are parsed as ISO dates. T1/T2 are research assessment dates, not clinical blood-draw order dates.
- CBC: `30000-{0,1,2}.0` WBC, `30020-{0,1,2}.0` haemoglobin, `30070-{0,1,2}.0` RDW, `30080-{0,1,2}.0` platelets.
- Baseline covariates: `31-0.0` sex, `21003-0.0` age, `21001-0.0` BMI, `20116-0.0` smoking, `30710-0.0` CRP, calendar year derived from T0.
- Primary registry outcomes: pair `40005-j.0` cancer date only with same-index `40006-j.0` ICD-10 code, j=0,...,21. Retain only valid date/code pairs and take the earliest qualifying event. Classes: CRC C18/C19/C20; haematologic C81–C96; other primary malignant C00–C97 excluding those families and secondary C77–C79.
- Same-table ascertainment sensitivity: pair `41270-k.0` ICD-10 code only with same-index `41280-k.0` first-inpatient-diagnosis date, k=0,...,258. Use the same cancer classes and earliest valid paired event. Never cross array indices, and never pool registry and inpatient records into one “gold-standard” date.
- Death: `40000-0.0`; retain `40001-0.0` only for an audit. Death is a competing event, not a cancer-type proxy.

The table JSON contains the 41270/41280 arrays as well as the parent’s 40005/40006 arrays. A bounded schema audit observed that the source columns are physically present; the planned solver must recompute all nonmissingness, pair completeness, invalid-date, duplicate-eid, impossible-date-order and code-class denominators rather than importing audit counts. Parent source audit counts (478,033 complete first CBCs; 19,409 complete second CBCs; 5,862 complete third CBCs; 18,377 valid first/second pairs; 439,735 first-CBC eligible after prior-cancer exclusion; 750 CRC and 525 haematologic 0–2-year events) remain availability diagnostics, not fitted results.

The source has no symptoms, reason for testing, laboratory order date/source, primary-care contacts, ferritin/iron, reticulocytes, FIT, smear, marrow/pathology adjudication, stage, treatment, imaging, transfusion context, healthcare utilisation, or expert cancer adjudication.

## Primary population, time and estimands (unchanged)

Primary first-CBC population: nonmissing `eid`, parseable T0 and complete instance-0 WBC, haemoglobin, RDW and platelets; exclude any valid qualifying registry cancer on or before T0; do not require T1/T2.

Follow from T0 to first CRC, haematologic cancer, other primary cancer, death, administrative censoring at 2022-12-31, or window boundary. The primary estimand is unchanged:

`D0,2–5 = (beta_platelet,CRC - beta_Hb,CRC) - (beta_platelet,HEME - beta_Hb,HEME)`

from separate cause-specific models in the risk set at T0+2 years, with other cancer and death competing. Positive D means the platelet/Hb contrast is relatively more CRC-associated. It is conditional delayed-risk association, not a causal effect or population risk ratio.

Report the unchanged secondary `D0,0–2`, 2-year and 5-year cumulative incidence, and 2–5-year increment. A 0–2-only signal does not support a delayed phenotype.

Repeat-CBC stress population: complete T1 strictly after T0 with all four instance-1 CBC values, main gap 2–8 years, no qualifying cancer or death on/before T1. Repeat features are baseline CBC, four changes z(j,1)-z(j,0), gap and baseline covariates. Estimate unchanged `DDelta,0–2` from T1 and `DDelta,2–5` as delayed sensitivity; T2 remains sensitivity-only. This cohort is explicitly conditional on survival, cancer-free status, return for a research assessment and measurement completeness.

## Ascertainment and clinical-selection tests

Retain every parent check: R=1 versus R=0 first-CBC contrast, measured baseline repeat-observation weighting, fixed gap strata, repeat-era strata, T0 calendar-era interaction, two-year near-diagnostic displacement, other-cancer specificity, cancer-type permutation, and sparse-event stop rules. R is defined without future outcomes. Weighting is a selection stress test, not a causal correction.

Add the following prespecified same-table bridge without changing the primary estimand:

1. Derive the primary registry event series from paired 40005/40006. Independently derive an inpatient event series from paired 41270/41280. Run the same first-CBC population, T0 windows, competing events, predictors, standardisation and D contrasts under each source. The inpatient series is a secondary ascertainment proxy, not an alternative primary outcome.
2. Among participants with valid events in both sources, report same-class date displacement (inpatient date minus registry date), class-specific median/IQR and the proportion whose source order changes the 0–2 versus 2–5 window. Do not use this descriptive overlap to alter cohort eligibility or reassign events.
3. Repeat the R=1/R=0, gap/era, two-year displacement, other-cancer and cancer-type permutation checks under the inpatient source. Keep registry and inpatient outputs side by side; do not average them.
4. Classify registry-versus-inpatient disagreement as ascertainment-sensitive if the D direction reverses, the delayed contrast loses its prespecified precision, the contrast changes by >0.20 log-hazard units, or a source-specific calendar interaction appears. Concordance is only compatibility with robustness because both sources may share errors.
5. A registry-positive/inpatient-negative pattern is adverse to registry-robustness, not proof of no cancer biology. A concordant delayed positive pattern is supportive of a timing-robust descriptive association but still cannot establish indication, stage or mechanism. If paired event counts or date displacement are too sparse, report inconclusive rather than choosing the favorable source.

No HRO, Online Follow-up or Assessment Center field is added to the analysis. The catalog bindings are: HRO Parquet source `[UKB data file]`, table `UKB/ukb672073_Health_Related_Outcomes.csv (Parquet)`, 502,370 rows, `eid`, namespace `ukb672073`, source [source checksum]; Online Follow-up source `[UKB data file]`, table `UKB/ukb672073_Online_Follow_up.csv (Parquet)`, `eid` and `20191-0.0` only, namespace `ukb672073`, [source checksum]; Assessment Center source `[UKB data file]`, table `UKB/ukb672073_Assessment_Center.csv (Parquet)`, namespace `ukb672073`, [source checksum]. Their source archive members are ordinary files. The exact catalog metadata states that ukb671626 and ukb672073 are separate namespaces and no cross-namespace join is authorized without documented mapping. Using same-looking `eid` values would be an invalid join. These derivatives therefore cannot validly improve follow-up, indication, or selection in this child.

## Methods, comparison, split and uncertainty

A. Primary transparent model: separate cause-specific Cox models for CRC and haematologic cancer with four standardised instance-0 CBC variables, age, sex, BMI, smoking, CRP and T0 calendar year; other cancer and death are competing causes. Repeat models add baseline CBC, four changes, gap and the same covariates. Use robust intervals, time-varying diagnostics and Aalen–Johansen cumulative incidence. Penalize only for documented separation/convergence failure.

B. Same-input learned alternative: CPU gradient-boosted discrete-time multi-task competing-risk model with yearly intervals and hazards for CRC, haematologic cancer, other cancer and death. It uses exactly the same people, predictors, landmarks, paired outcome source, windows and competing-risk definitions as A; only the functional form changes. It can expose nonlinear Hb/platelet ranges, interactions and time-varying type-specific hazards hidden by additive Cox coefficients. It cannot identify mechanism or indication. Fit the bridge under both sources, but never let source choice be tuned on final test performance.

Sort by landmark date: earliest 70% development, latest 30% final temporal holdout; participants remain intact. All standardisation, missingness/imputation decisions, weighting, tuning and calibration are development-only. Compare A and B on target-specific calibration intercept/slope, calibration plots, 2- and 5-year cumulative-incidence Brier and log scores, with AUC/Uno C-index secondary. Use 500 participant-bootstrap replicates for predictions, weighted estimates, source differences and date displacement, preserving failures. If a primary comparison has fewer than 50 held-out haematologic events, label that learned comparison inconclusive rather than changing the split or endpoint.

Future solver envelope: up to 16 CPUs, 262,144 MiB, 8 GPUs and 28,800 seconds. Planned workload is 8–16 CPU cores, 32–64 GiB, approximately 2–4 hours for selected-column parsing, Cox/boosted fits and bootstrap; unmeasured estimate. GPU is not required. No full solver is run in this discovery branch.

## Interpretation and falsification

Supportive requires: positive and useful-precision D0,2–5 under the primary registry source; delayed direction not confined to R=1, one era or one gap; compatible R-weighted/unweighted repeat contrast; no near-diagnostic-only explanation; CRC specificity versus other cancer; cancer-type permutation collapse; and no adverse registry/inpatient source reversal or >0.20 log-hazard source discrepancy. The learned alternative must add stable held-out calibration or time-varying information, not merely AUC.

Adverse includes a precise reversal, a large weighted/unweighted shift, era/gap dependence, disappearance after two years, other-cancer similarity, permutation failure, registry/inpatient reversal or source-specific timing, or a learned result that only discriminates without calibration. These weaken stable cancer-type interpretation but do not refute generic CBC–cancer association.

Inconclusive includes fewer than 50 held-out haematologic events, sparse paired source overlap/date displacement, wide delayed intervals, weight positivity failure, unstable pairing/date parsing, nonconvergence, or a wide null. A wide null is not refutation.

A supportive result establishes only a temporally ordered descriptive association in selected volunteers and cross-source compatibility. It cannot establish diagnostic accuracy in symptomatic patients, clinical utility, referral thresholds, causality, mechanism, stage or treatment benefit. Expert adjudication of cancer dates/codes, symptoms and laboratory indication, pathology/stage/treatment, healthcare utilisation, and prospective decision-linked external validation remain required.

## Alternatives and decision rule

The parent Cox plus same-input boosted comparator remains selected because it directly tests the estimand and nonlinear/time-varying information with auditable outputs. A state-space/GP trajectory model is deferred because only two broadly complete CBC repeats exist and repeat haematologic events are sparse; it cannot identify clinical indication and adds assumptions without resolving the source/timing rival. A transformer is likewise deferred. A model using future R as a first-CBC predictor is rejected as leakage. Cross-namespace joins to ukb672073, HCC, MIMIC or EICU are rejected.

The independent exact-data UKB alternative retained for comparison is [prior hypothesis]: baseline HbA1c/weight metabolic mismatch versus inpatient pancreatic cancer using the same ukb671626 source and 41270/41280 fields. Its audit found 23 total pancreatic events, zero in both repeat windows and one later repeat-landmark event, so its central longitudinal question and learned validation are likely inconclusive. It is clinically important but does not resolve the CBC cancer-type ascertainment question as efficiently; it remains deferred, not refuted.

## Scientific deliverable

The solver must newly fit and emit: exact registry and inpatient paired-event audits; cohort/exclusion tables; source-overlap/date-displacement table; R and gap/era tables; split manifest; fitted A and B artifacts for both outcome sources; D0 and DDelta contrasts with uncertainty; cumulative incidence; weighted selection diagnostics; held-out calibration/Brier/log scores; other-cancer and cancer-type permutation controls; and a conclusion labelled supportive, adverse or inconclusive. These outputs, not readiness or planned results, establish completion.

## Key references

Exactly three distinct inspected works are attached in `key-references.json` with UTF-8 evidence excerpts: Hamilton [K1], Sala [K2], and Hampton [K3]. Their claims are bounded to the inspected passages; no inaccessible supplement or unavailable original evidence is asserted.
