> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: post-TACE biomarker trajectories with time-aligned examination proxies

## Scientific question, evidence boundary, and hypothesis

After TACE for HCC, clinicians must decide whether a patient can enter routine surveillance or should be reassessed for additional liver-directed treatment. AFP may fall while hepatic function recovers, remain high, or change in the opposite direction. A repeat TACE is clinically consequential, but it is also a clinician action affected by eligibility, access, local practice, and whether the patient returns. The unresolved question is whether the early joint AFP/hepatic-marker trajectory identifies a subsequent treatment action because it carries a reproducible residual-disease signal, or whether its apparent value is mainly an artifact of who is measured and who receives care.

The strongest claim supported by the already inspected evidence is narrower: AFP and hepatic-function measures are clinically used but heterogeneous; dated examination reports exist in this HCC source and include relevant upper-abdominal/liver study names, but their narrative labels are not a validated radiologic-response ontology. The local data do not establish true residual tumor, progression, treatment intent, or clinical benefit.

The primary prespecified hypothesis is:

> Among adults with structured HCC and a first recorded TACE-like procedure who have numeric pre-TACE and early post-TACE AFP, an early-response phenotype—at least a 50% fall in log1p AFP from days -30 to -1 to days 7 to 45, with no deterioration in at least two of albumin, total bilirubin, INR, and platelet count—will be associated with lower odds of a repeat recorded TACE-like procedure during days 46 to 365.

The repair adds a secondary, independent proxy hypothesis:

> The same favorable phenotype will be associated with lower probability of a conservative, date-aligned “concerning examination wording” proxy during days 46 to 180, after accounting for whether an eligible examination was obtained; the direction will be concordant with the repeat-TACE association.

These are prognostic associations, not causal effects. A concerning wording flag is not called radiologic progression, and a repeat TACE is not called recurrence. The substantive advance over the parent is a prespecified attempt to test the biological interpretation against a different, time-aligned evidence stream while explicitly modeling examination availability as an observation process.

## Actual scientific deliverable

The solver must newly construct the frozen index cohort, fit a transparent baseline and the joint longitudinal/observation model, and estimate two linked post-landmark associations:

1. the association of the day-45 biomarker phenotype with recorded repeat TACE; and
2. the association of the same phenotype with the examination proxy, with examination availability reported and handled as missing-not-negative.

Completion requires locked-test predictions, calibrated uncertainty, the action/proxy concordance table, the observation-process analysis, and an analysis manifest that permits a machine checker to reproduce filters, dates, joins, flags, split membership hashes, and all reported metrics. The result is a locally testable prognostic/evidence-coherence study, not a validated clinical decision rule.

## Population and temporal boundaries

Use one index per patient: the earliest procedure episode satisfying the TACE-like rule, with the procedure’s Start Time. Collapse same-patient procedure rows within 24 hours into one episode, retain all original Surgery names, and do not select the index using any future outcome.

Require:

- age >=18 and nonmissing sex at the index encounter;
- a structured diagnosis name containing the literal Hepatocellular Carcinoma on an encounter from 180 days before through 7 days after index;
- a usable index procedure time and an exact procedure-to-encounter join;
- index date on or before 2025-01-01, allowing a nominal 365-day window within the local snapshot.

A TACE-like procedure name is selected before outcome inspection if surgery contains TACE, transarterial chemoembolization, or both hepatic artery and embolization. The primary action outcome is any later TACE-like episode with 45 < days after index <=365. A secondary action outcome is any later liver-directed procedure whose surgery contains resection, ablation, radiofrequency, microwave, or the TACE rule.

The landmark is day 45. No laboratory or examination information after day 45 enters a predictive feature. The primary biomarker estimand is the complete-pair population with a parseable numeric AFP in both days -30 to -1 and 7 to 45. An all-eligible analysis with explicit missingness indicators is secondary and must not treat absent testing as a biologic response.

For the primary examination proxy, use only records dated 46 to 180 days after index; use 46 to 365 days as a prespecified window sensitivity. The examination record is not used as an exposure. An absent eligible examination is missing proxy evidence, not evidence of response or stability.

## Exact HCC data bindings

The source is read-only HCC snapshot [source checksum]; the full catalog is [internal dataset path] All joins use the exact identity pair patient master index, encounter number.

- encounters, schema datasets/hcc/table-b743286cb1249287.json, source [internal dataset path] Use age, sex, and admission time; fall back to encounter time only when admission time is missing. Discharge time is descriptive follow-up only. Do not use names, identity-card numbers, phone numbers, insurance numbers, or other direct identifiers.
- procedures, schema datasets/hcc/table-d5eae16f8f8093d9.json, source [internal dataset path] Use procedure, start time, end time, and procedure source; index and outcome time are start time joined by the same two keys. A fallback to encounter time is permitted only when a procedure start is absent and must be counted separately; the primary analysis requires a usable procedure start.
- labs, schema datasets/hcc/table-38aad8c54471332f.json, source [internal dataset path] Use test, qualitative result, quantitative result, specimen type, and test time; window on test time. Exact assay names are alpha-fetoprotein, albumin, total bilirubin, international normalized ratio, and platelet count. Parse numeric quantitative result, preserve qualitative result inequalities as flags/censored values, and never pool values across assays. There is no lab unit column, so do not compute ALBI, MELD, or cross-assay ratios.
- diagnoses, schema datasets/hcc/table-12710723c3df0c99.json, source [internal dataset path] Use Diagnosis Name and Diagnosis Type; bind to encounters by the same two keys and use the joined encounter admission time for the +/-180-to-+7 diagnosis window. The literal substring rule is a reproducible structured-label rule, not NLP.
- examinations, schema datasets/hcc/table-fd016d2731b9d6c6.json, source [internal dataset path] Use Examination, Examination Findings, Examination Diagnosis, Start Time, Machine Model, and Examination Number; window on Start Time, join/provenance by the same two keys. Examination Findings and Examination Diagnosis are narrative text and may contain HTML/template duplication.
- clinical_documents, schema datasets/hcc/table-66afca58512c2fca.json, source [internal dataset path], is not a primary source: it has no document time field and its lexical detector is not validated for comprehensive diagnosis extraction. It may be used only for a separately labeled clinician-review sample, if expert review is actually supplied.

The HCC catalog also confirms that images and raw waveforms are unavailable; vitals, transfers, and front_page are identifier-only for this purpose. The other configured dataset islands remain directly accessible, but this child intentionally uses only HCC and does not import MIMIC, eICU, or UKB variables.

## Examination proxy and observation-process design

A bounded read-only scan of all 419,996 examination rows found nonempty payload and, in the exact adult-HCC/first-TACE feasibility cohort, 36,615 post-day-45 examination rows from 5,905 patients. Relevant names included upper-abdominal plain-plus-enhanced DWI/MRCP, liver ultrasound contrast, liver elastography, liver/portal-vein studies, and PET/CT. The same scan showed many unrelated chest, cardiac, pathology, and other records. Therefore the broad examination table is not itself a radiologic endpoint.

Freeze the following transparent proxy rule before fitting and report every matched name and original text hash:

1. An eligible name contains one of liver, abdomen, abdominal cavity, upper abdomen, hepatobiliary, or PET/CT.
2. Exclude names containing pathology, specimen, tissue, heart, echocardiogram, chest, pulmonary function, bone, lower limb, gastroscopy, adrenal gland, or puncture.
3. Strip HTML only for matching; retain the raw fields. A row is “concerning wording” only if the combined examination diagnosis plus examination findings contains at least one lesion/tumor term (lesion, space-occupying lesion, mass, nodule, tumor, cancer, metastasis, recurrence, residual, enhancement, or necrosis) and at least one concerning term (recurrence, residual, progression, metastasis, new onset, active, active lesion, worsening, suspicious for malignancy, or abnormal enhancement).
4. Separately flag explicit response/stability wording if it contains shrinkage, resolution, disappearance, stable, no abnormal enhancement seen, no obvious enhancement seen, necrosis, or not seen after treatment. These categories are descriptive and may overlap; no flag is treated as a validated label. Rows with only generic findings, unrelated anatomy, or no eligible name are other/not classified.
5. Deduplicate exact repeated patient/examination number/time/text rows. If reports are repeated under several names on the same patient and date, retain a report hash and row count, and use patient-level any concern only once.

Because negation, historical comparison, copied-forward reports, and anatomic scope are not reliably resolved by this lexical rule, the primary term is concerning examination wording proxy. The solver must not call it progression, response, viable tumor, or radiologic adjudication. If a clinical reviewer later labels a stratified report sample, that adjudication is a separate sensitivity analysis and must report reviewer count and agreement; it cannot be fabricated by the solver.

Create separate indicators for:

- any eligible examination in days 7 to 45 (early measurement availability);
- any eligible examination in days 46 to 180 and 46 to 365 (follow-up availability);
- concerning, response/stable, and other classified wording among available eligible reports;
- number and timing of eligible examinations, report duplication, and examination name family.

Model follow-up examination availability as its own post-landmark observation outcome using only day-45-available features. For the wording association, report the complete observed-report analysis and an inverse-probability-of-observation sensitivity model fit without future outcomes. Never code no examination as no concern.

## Features and preprocessing

The transparent baseline is regularized logistic regression, separately for repeat TACE and the examination proxy:

- age, sex, index year, and index procedure-name family;
- prior 180-day structured diagnosis indicators/counts for Liver Cirrhosis, Portal Vein, Intrahepatic Metastasis, Lung Metastasis, Bone Metastasis, and Ascites;
- prior liver-directed procedure count and prior TACE/resection/ablation indicator;
- last pre-index-window AFP, albumin, total bilirubin, INR, platelet count, plus assay missingness;
- for the day-45 prediction comparison, no post-landmark outcome or report text; an early-examination-presence indicator is added only in a prespecified observation-process sensitivity.

The primary phenotype is fixed before fitting: >=50% reduction in log1p AFP from the last pre-window value to the first post-window value, and no deterioration in at least two of the four hepatic markers relative to their corresponding window summaries. The solver must define marker-direction conventions before seeing outcomes, use within-assay training-set median/IQR standardization, preserve inequality/censor flags, and report the exact window value chosen. No units, ALBI, MELD, treatment intent, or imputed disease stage may be introduced.

The substantive alternative is a joint longitudinal-state/discrete-time hazard model with an observation component. It estimates an AFP-dominant latent activity proxy and a hepatic-marker latent-function proxy from irregular dated measurements in days -30 to 45, with patient random intercepts/slopes or an equivalent prespecified state-space formulation. Separate discrete-time hazards then estimate repeat TACE and eligible-examination occurrence; conditional on observed eligible reports, a second component estimates concerning versus response/other wording. Include baseline covariates, measurement timing/missingness, and procedure-name family. This model can reveal whether trajectory direction, timing, and AFP/hepatic discordance carry information beyond a pre-index snapshot and whether apparent action prediction is concentrated in the measurement process. It does not recover true tumor burden, true liver reserve, or causal treatment response.

## Split, estimand, analysis, and uncertainty

Use a temporal patient-level split restricted to index records with complete 365-day ascertainment: 2010–2022 for fitting, 2023 for tuning and threshold choices, and 2024 through 2025-01-01 as a locked test period. No patient contributes more than one index; still verify leakage by patient and by report hash. A grouped/random split is a secondary stability check only.

The primary estimands are:

- the adjusted odds ratio for the favorable phenotype versus repeat recorded TACE from days 46–365;
- the adjusted association of the same phenotype with a concerning wording proxy in days 46–180 among observed eligible reports, with an observation-weighted sensitivity;
- incremental locked-test predictive performance of the joint alternative versus the baseline for action and proxy outcomes.

Report AUROC, PR-AUC, Brier score, calibration intercept/slope, and mean log score for each outcome where prevalence permits; report event counts rather than suppressing sparse outcomes. Use patient bootstrap or robust sandwich intervals, with bootstrap resampling preserving all records from each patient. For the phenotype association, use a 95% interval and prespecified direction; for model comparison, define a practically negligible improvement as 0.01 nats per patient in mean log score and report whether the uncertainty interval excludes that margin. Thresholds are selected on 2023 only. Any decision curve is validation-only and is not a treatment recommendation.

The action/proxy artifact check is a prespecified four-cell table among patients with an eligible follow-up examination: repeat TACE yes/no by concerning wording yes/no, accompanied by the same table stratified by examination availability and early AFP measurement. Compare the trajectory’s direction and uncertainty across the action model, proxy model, and observation model. A post-day-45 exam is an outcome/evidence stream, not a covariate in the primary action prediction.

## Falsification and interpretation

Supportive evidence requires all of the following:

- the favorable phenotype has an adjusted association below the null with repeat TACE, its 95% interval excludes 1, and the direction is stable under literal TACE/arterial chemoembolization naming and 90-/180-day action windows;
- the same phenotype is directionally associated with fewer concerning-wording proxy reports, with the complete-report and observation-weighted analyses not materially contradictory;
- the joint model improves locked-test log score by more than 0.01 nats/patient over the baseline for at least one prespecified outcome, with uncertainty excluding that negligible margin, without a calibration deterioration;
- the action association does not disappear after adjustment/stratification for prior examination utilization, early measurement presence, procedure-name family, index year, and index encounter department where available.

This would support a local, evidence-coherent prognostic association and justify prospective evaluation with adjudicated imaging. It would not support recurrence, residual viable tumor, a causal treatment strategy, clinical utility, or transportability.

Adverse evidence is a null/reversed phenotype association, a proxy association in the opposite direction, poor or worsened calibration, instability under conservative name/lexical definitions, or an apparent action gain that disappears after observation-process handling. Action prediction with no corresponding proxy association is specifically adverse to the claim that the result reflects residual disease; it may instead reflect clinician selection, eligibility, access, or measurement behavior. A concerning proxy without repeat TACE indicates discordance, not proof that treatment was withheld or inappropriate.

Inconclusive evidence includes too few paired AFP records, too few eligible reports or concerning events in the locked test period, intervals crossing clinically meaningful effects, heavy report duplication, units/censoring ambiguity, extreme observation weights, calendar/site changes, or inability to determine whether wording is current versus copied-forward. If the conservative examination rule is too sparse or cannot be separated from unrelated/negated text, declare the examination dependency unusable and retain the original biomarker-to-recorded-action question as the only computable result. Do not redefine the proxy after seeing outcomes.

Clinical adjudication or another study is required for radiologic response/progression, viable tumor, Barcelona stage, treatment intent, appropriateness of repeat TACE, hepatic decompensation, death, recurrence, outside-care capture, and clinical utility. The local files contain no image files, no validated NLP, no reliable treatment-intent field, no death endpoint, no complete claims/outside-care ascertainment, and no assay units. Expert review of dated reports and an external or prospective cohort would be needed for those stronger claims.

## Machine-checkable solver deliverable

The solver must write an analysis directory containing:

- analysis_manifest.json with source paths, table IDs, schema hashes, snapshot ID, input file hashes, exact regexes, assay parser/censor rules, window endpoints, fallback counts, row counts after every filter, duplicate-collapse counts, report hashes, split membership hashes, random seeds, feature lists, model configurations, and missingness/weight diagnostics;
- cohort-flow, index-year, procedure-name, examination-name, report-duplication, assay availability, censoring, and outcome tables;
- baseline and joint-model parameter/state summaries, observation-model estimates, locked-test patient predictions, calibration/discrimination/log-score tables, and patient-bootstrap intervals;
- phenotype association tables for repeat TACE and examination wording, the four-cell action/proxy table, complete-report and observation-weighted sensitivities, literal-name and 90-/180-day window sensitivities, and a no-examination-is-negative guard;
- a machine-readable conclusion.json whose classification is exactly supportive, adverse, or inconclusive, with every criterion linked to computed output paths and uncertainty intervals;
- a limitations table separating computationally checkable claims from claims requiring clinical adjudication, unavailable evidence, or another cohort.

Readiness checks may verify imports, private paths, schemas, deterministic fixtures, exact filters, no post-day-45 leakage, split integrity, and declared metrics. Readiness cannot establish clinical truth or validate the examination proxy.
