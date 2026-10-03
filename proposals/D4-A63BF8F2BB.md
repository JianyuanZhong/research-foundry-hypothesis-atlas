# CBC cancer-type contrast under source-dependent ascertainment

Status: binding-corrected child of [prior hypothesis]. No hypothesis fit has been run here. This revision addresses the parent's strongest remaining rival: registry/inpatient disagreement may reflect severity-dependent capture and healthcare-use selection, not clinical timing.

## Scientific opening and bounded claim

Prior evidence supports an association between blood abnormalities and cancer-related outcomes, and a CRC-only retrospective study reports CBC trajectory differences up to 24 months before CRC diagnosis [K2]. A symptom-defined primary-care study shows that the tested population and a short diagnostic window materially shape cancer prediction [K1]. A review finds that discrimination is often reported without adequate calibration or external validation [K3]. None establishes that a UKB platelet/haemoglobin contrast is CRC-specific, persists after the near-diagnostic period, or is robust to two ascertainment processes.

The strongest evidence-supported claim is descriptive: CBC measurements or trajectories can be associated with later CRC-related outcomes in selected clinical cohorts. The unresolved claim is narrower and falsifiable:

> In UKB adults with a complete first CBC and no source-observed cancer at baseline, the prespecified higher-platelet/lower-haemoglobin phenotype has a delayed CRC-versus-haematologic absolute-risk contrast that is not explained by a generic cancer ascertainment signal, by the inpatient source's severity-dependent capture, by the first 90 days after assessment, or by future repeat-assessment selection.

This is a temporally ordered association. It is not a causal, mechanistic, diagnostic-accuracy, screening, stage, treatment, referral-threshold or clinical-utility claim. Inpatient-versus-registry date differences are treated as ascertainment disagreement; UKB field 53 dates are research-assessment dates, not laboratory order dates.

The clinical advance would be to determine whether the parent CBC contrast remains cancer-type-specific after separating (i) the contrast between cancer classes, (ii) a shared all-cancer/source-capture component, and (iii) the temporal and repeat-attendance patterns that can mimic an early-warning signal. A supportive result would justify an indication-rich external validation; an adverse result would redirect interpretation toward general illness or capture; an inconclusive result would identify missing evidence rather than support action.

## Exact UKB binding and verified availability

Use only the single same-namespace UKB table recorded in the catalog/schema audit:

- Snapshot: `ukb-completed-subset-20261002`; catalog [source checksum].
- Catalog/guide records: `datasets/README.md`, `datasets/ukb/README.md`, and `datasets/ukb/table-5d49a6760e7ffdbd.json`.
- Table: `ukb671626.csv (Parquet)`, source ID `[UKB data file]`, 502,371 rows, unique key `eid`, identifier namespace `ukb671626`, ordinary file with no archive member.
- Read-only source: `[internal dataset path]`, [source checksum].
- Binding target for the future solver: `[internal dataset path]`, with the same Parquet hash. The original CSV lineage file is provenance only and is not an analysis input.

No participant join is permitted. `eid` is the only key. Do not use `ukb672073`, Olink, HCC, MIMIC, EICU or any cross-namespace field.

Required fields, all in the audited table:

- Key/landmarks: `eid`; `53-0.0` T0, `53-1.0` T1, `53-2.0` T2.
- Instance-0 CBC: `30000-0.0` WBC, `30020-0.0` haemoglobin, `30070-0.0` RDW, `30080-0.0` platelets.
- Instance-0 baseline adjustment: `31-0.0` sex, `21003-0.0` age, `21001-0.0` BMI, `20116-0.0` smoking, `30710-0.0` CRP; derive T0 calendar year from `53-0.0`.
- Registry arrays: pair same-index `40005-j.0` cancer date with `40006-j.0` ICD-10 code for j=0,...,21. Keep only valid paired date/code observations and take the earliest qualifying event.
- Inpatient arrays: pair same-index `41270-0.k` inpatient ICD-10 code with `41280-0.k` first-inpatient-diagnosis date for k=0,...,258. This is an ascertainment proxy, not a gold standard. Never cross indices.
- Death: `40000-0.0`; `40001-0.0` is audit-only. Death is a competing event.

Schema-only availability audit (not participant-level nonmissingness, cohort counts, or fitted results): the complete `columns` array in `datasets/ukb/table-5d49a6760e7ffdbd.json` was inspected. It has 1,160 column names, 502,371 rows, id column `eid`, namespace `ukb671626`, and contains every field required above. Exact presence is: `eid`; `53-0.0`, `53-1.0`, `53-2.0`; instance-0 CBC `30000-0.0`, `30020-0.0`, `30070-0.0`, `30080-0.0`; baseline `31-0.0`, `21003-0.0`, `21001-0.0`, `20116-0.0`, `30710-0.0`; registry `40005-j.0` and `40006-j.0` for every j=0..21; inpatient `41270-0.k` and `41280-0.k` for every k=0..258; death `40000-0.0` and `40001-0.0`; and repeat fields `30000-1.0`, `30020-1.0`, `30070-1.0`, `30080-1.0`. The corresponding observed inpatient column-name sets are exactly `41270-0.0` through `41270-0.258` and `41280-0.0` through `41280-0.258` (259 each). `41270-k.0` is not the binding and is not a column-name pattern in this table. The attached `schema-availability-audit.json` records the exact generated sets and zero missing expected names. Values and participant-level availability must be recomputed by the solver.

Classify CRC as ICD-10 C18-C20, haematologic cancer as C81-C96, and other primary malignant cancer as C00-C97 excluding those families and secondary C77-C79. Report invalid dates, missing pair members, duplicate `eid`, date ties, impossible date ordering and code-family denominators. The parent audit's counts are not analysis results: the solver must recompute all denominators.

Unavailable evidence is essential to the clinical interpretation: symptoms, reason for CBC, laboratory order date and source, primary-care contacts, ferritin/iron, reticulocytes, FIT, smear, marrow/pathology, stage, treatment, imaging, transfusion context, healthcare utilisation and expert cancer adjudication. The source cannot determine whether a CBC was ordered because of symptoms or whether an inpatient diagnosis represents first biological diagnosis.

## Population and temporal boundaries

Construct one common source-clean cohort so source comparisons are not confounded by different baseline prevalent-cancer exclusions.

1. Include one row per nonmissing unique `eid`, parseable T0, and complete instance-0 WBC, haemoglobin, RDW and platelets.
2. Require no valid qualifying registry or inpatient cancer event on or before T0, and no death on or before T0. Report the separate registry-only, inpatient-only and intersection exclusions.
3. Do not require T1 or T2 for the primary population.
4. For the common delayed risk set, additionally require alive and free of qualifying cancer in both source series through T0+2 years. This is a conditional T0+2-to-T0+5 estimand; events before T0+2 are reported as exclusions, never converted into delayed events.
5. Follow to the earliest source-specific CRC, haematologic cancer, other primary cancer, death, administrative censoring at 2022-12-31, or the window boundary. A source can be missing an event that the other source records; that discordance is itself reported.

Primary windows are (T0,T0+2 years], (T0+2 years,T0+5 years]. A timing falsification additionally reports (T0,T0+90 days] and (T0+90 days,T0+2 years]. Use exact calendar dates and state the day-boundary convention in the solver output.

Define future repeat observation `R=1` as T1 strictly after T0 and within 2-8 years, with all four instance-1 fields `30000-1.0`, `30020-1.0`, `30070-1.0`, `30080-1.0` observed; otherwise R=0. R is a future-attendance sensitivity stratum, never a baseline predictor. A repeat-change analysis is secondary only and requires no qualifying source cancer or death on/before T1; it uses the four baseline-to-T1 changes and the T0-T1 gap. T2 is sensitivity-only.

## Source-stratified estimands

For source s in {R=registry, I=inpatient}, fit the same competing-risk analysis on the common source-clean risk set and report CRC, haematologic, other-primary and death event counts separately. Let Δ_s,c(w) be the model-standardized cumulative-incidence difference for cancer class c in window w between two fixed baseline CBC profiles:

- g_CRC: platelets +1 development-standard deviation, haemoglobin -1 SD, WBC and RDW at development means.
- g_HEME: platelets -1 SD, haemoglobin +1 SD, WBC and RDW at development means.

Keep observed age, sex, BMI, smoking, CRP and T0 year for each person; replace only platelet and haemoglobin with the profile; standardize over the same holdout risk set. Report each component risk and difference in percentage points.

The cancer-type estimand is:
`T_s(w) = Δ_s,CRC(w) - Δ_s,HEME(w)`.

The preserved parent absolute-risk estimand is:
`A_s(w) = [P_s(CRC,g_CRC,w)-P_s(CRC,g_HEME,w)] - [P_s(HEME,g_CRC,w)-P_s(HEME,g_HEME,w)]`.
Thus `A_s=T_s` when the profile and risk definitions match, but both notation and all four component risks must be reported.

To expose a generic cancer-ascertainment component, define:
`G_s(w) = mean[Δ_s,CRC(w), Δ_s,HEME(w), Δ_s,OTHER(w)]`,
and the CRC-specific residual:
`S_s(w) = Δ_s,CRC(w) - mean[Δ_s,HEME(w), Δ_s,OTHER(w)]`.
`G_s` is not a severity score and `S_s` is not a causal effect. A large `G_I` with small `S_I`, or similar Δ for CRC and other cancer, is evidence against a CRC-specific interpretation even if inpatient prediction is strong.

For transparency also fit separate cause-specific models and report the parent's relative contrast:
`D_s(w) = (beta_platelet,CRC - beta_Hb,CRC) - (beta_platelet,HEME - beta_Hb,HEME)`.
Positive D/T/A means the fixed CBC ordering shifts observed risk more toward CRC than haematologic cancer. These are descriptive source-specific contrasts, not hazard ratios, causal effects or individual diagnostic probabilities.

The primary scientific comparison is delayed `T_R(2-5)` versus `T_I(2-5)`, with `A_R` and `A_I` as the decision-scale presentation. Use a descriptive absolute boundary Δ=1 percentage point; it is not a referral threshold.

## Source/capture bridge and falsifications

1. Run all estimates separately for R and I on the same source-clean population; never pool dates or choose the more favorable source.
2. Among same-class events observed in both sources, report inpatient date minus registry date by class: n, median, IQR, 5th/95th percentiles, and fractions crossing 90 days, 2 years and 5 years. If fewer than 50 same-class paired events exist, source-displacement conclusions for that class are inconclusive. A crossing is an ascertainment discrepancy, not proof of diagnostic delay.
3. For each registry event in a window, report whether a same-class inpatient event occurs in the same participant within the available follow-up and whether the inpatient date is before/after the registry date. Conversely report registry capture among inpatient events. Stratify these capture fractions by development-defined deciles of the CBC profile score and by WBC/CRP severity strata. This tests whether source agreement is severity-dependent; it does not identify which source is correct.
4. Near-diagnostic falsification: report 0-90 days, 90 days-2 years and 2-5 years. A signal confined to 0-90 days, or materially attenuated after excluding that band, supports proximity/ascertainment rather than a stable delayed association. A delayed signal with no early-only concentration is compatible with, but does not prove, a non-near-diagnostic association.
5. General-ascertainment falsification: compare Δ for CRC, haematologic and other cancer. If Δ_I,OTHER is comparable to Δ_I,CRC or if `S_I` is near zero while `G_I` is large, the inpatient result is interpreted as general cancer/hospital capture, not CRC specificity.
6. Repeat-selection falsification: estimate T/A separately for R=1 and R=0, with fixed T0+2-to-T0+5 follow-up and fixed gap strata; fit a baseline-only R-observation model using T0 CBC and listed baseline covariates, then use stabilized inverse-probability weights only as a stress test. Report overlap and weighted/unweighted estimates. A large stratum or weighted shift is adverse to generalising a repeat-CBC signal; poor positivity is inconclusive, not a reason to trim until favorable.
7. CRC-versus-haematologic label permutation preserves event dates/censoring and is run in development only; the type contrast should collapse toward zero. Other-cancer and permutation checks test specificity/implementation, not mechanism.
8. Report T0 calendar-era interactions and paired-array integrity. Concordance across R and I is only compatibility with robustness because both sources can share coding error.

## Transparent baseline versus learned alternative

A. Transparent baseline, selected for auditability: source-specific cause-specific Cox models for CRC, haematologic cancer, other cancer and death, with standardized WBC, haemoglobin, RDW and platelets plus age, sex, BMI, smoking, CRP and T0 year. Use Aalen-Johansen/model-standardized cumulative incidence for the fixed profiles. Complete-case model covariates are required after the CBC cohort screen; missingness denominators are reported and no missing value is silently treated as normal. Use robust intervals and proportional-hazard diagnostics.

B. Scientifically substantive same-input alternative: a CPU gradient-boosted discrete-time multi-task competing-risk model with yearly intervals (and a separate first-90-day interval for the timing falsification) and hazards for CRC, haematologic cancer, other cancer and death, fit independently for registry and inpatient sources. It uses exactly the same people, fields, source-clean exclusions, dates, profiles and competing risks as A. It can reveal nonlinear CBC ranges, interactions and time-varying source/class hazards that additive Cox can lose; it cannot reveal symptoms, indication, pathology or mechanism. A secondary same-input logistic model/classifier for cross-source capture is allowed only as a bridge output, not as a clinical predictor.

Split by T0: earliest 70% for development and latest 30% for a locked temporal holdout; one `eid` stays in one split. Fit standardization, covariate completeness decisions, tuning, weighting and calibration in development only. On the holdout report target-specific calibration intercept/slope and plots, 2- and 5-year cumulative-incidence Brier and log scores, the four profile risks, T/A/G/S, D, source differences and 500 participant-bootstrap intervals. AUC/Uno C-index is secondary. If the holdout has fewer than 50 haematologic events, learned type-specific comparison is inconclusive; do not replace the split or endpoint.

The learned model is retained because it tests a substantive uncertainty—whether nonlinear/time-varying CBC information is being lost by the transparent additive model—not because of a small ranking gain. A state-space/GP or transformer trajectory model is deferred: only two broadly complete repeat CBC assessments are available, and extra latent-state assumptions cannot identify source correctness or clinical indication. Future R is rejected as a baseline predictor because it is leakage.

Approximate future solver budget: 8-16 CPU cores, 32-64 GiB RAM, 2-4 hours including selected-column parsing, two source-stratified fits, capture bridge and 500-bootstrap outputs; unmeasured estimate. Configured planning envelope: up to 16 CPUs, 262,144 MiB and 28,800 seconds. GPU is not required for this tabular workload; the available A100 hardware does not add scientific value unless a measured implementation shows otherwise.

## Interpretation rules and completion

Supportive, source-robust type-specific evidence requires all of: (a) delayed T_R and T_I share the positive direction, with 95% intervals excluding zero and, for the absolute presentation, lower bounds above +1 percentage point when event/overlap thresholds are met; (b) no source reversal or prespecified large source discrepancy (|D_R-D_I| >0.20 log-hazard units or |A_R-A_I| >1 percentage point); (c) CRC residual S is positive and other-cancer Δ is materially smaller in both sources; (d) the result is not confined to 0-90 days, R=1, one era or one gap stratum; (e) weighted/unweighted selection stress tests agree within their uncertainty and have adequate positivity; and (f) permutation collapses. This supports external validation only.

Adverse evidence is a precise delayed reversal, source reversal, large source discrepancy, inpatient signal with large G and small S, comparable other-cancer contrast, early-only signal, R=1 confinement, large selection-weight shift, or learned-only ranking gain without calibrated absolute risk. These weaken stable CRC specificity but do not refute generic CBC-cancer association.

Inconclusive evidence is sparse source-overlap (<50 same-class paired events), fewer than 50 held-out haematologic events, broad intervals crossing the null or ±1 percentage-point boundary, poor positivity, invalid pairing/date parsing, nonconvergence, or a wide null unable to distinguish no meaningful contrast from the prespecified boundary. An imprecise null is not refutation.

Computationally checkable outputs are the source-pair audit, cohort/exclusion counts, temporal event bands, T/A/G/S/D estimates, profile risks, calibration/Brier/log scores, source-displacement and capture tables, selection diagnostics, permutation behavior and adherence of conclusions to these rules. Clinical adjudication or another study is required for symptoms, test indication, laboratory timing, pathology, cancer date validity, stage, treatment, healthcare utilisation, clinical usefulness and causal/mechanistic claims. A prospective, indication-rich external cohort with adjudicated cancer onset and decision-impact evaluation is required before clinical deployment.

## Actual scientific deliverable and deferred branches

Completion requires newly fitted source-specific baseline and learned models and emits: data-quality audit; common source-clean population and split manifest; event counts by source/class/window; D/T/A/G/S and four profile risks with bootstrap uncertainty; source displacement and cross-source capture tables; early-band, other-cancer, permutation, era and repeat-selection falsifications; holdout calibration/Brier/log outputs; and a supportive/adverse/inconclusive conclusion tied to those files. Readiness or a source audit alone is not completion.

The parent absolute-risk estimand is retained but its interpretation is sharpened by G/S and common source-clean entry. The bounded ApoB/albumin liver direction and sparse pancreatic metabolic direction remain deferred, not refuted: they do not adjudicate the CBC source/timing rival, and the pancreatic branch has only 23 total inpatient pancreatic events with zero in the planned repeat windows in the inherited audit. Revisit them only for a distinct question or new outcome evidence.

Exactly three inspected works are attached in `key-references.json`, with UTF-8 excerpts:
- [K1] Nicholson et al., BMJ 2024: symptom-defined diagnostic timing and clinical-feature context.
- [K2] Sala et al., Translational Oncology 2026: CRC-only retrospective CBC trajectories up to 24 months, explicitly investigational.
- [K3] Hampton et al., eClinicalMedicine 2023: calibration/validation limitations in symptomatic CRC prediction.

This proposal contains no fitted result and makes no claim that the three works establish the UKB hypothesis.
