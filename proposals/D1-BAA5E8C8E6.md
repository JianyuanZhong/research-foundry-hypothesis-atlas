> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Dynamic hepatic reserve after first TACE and 90-day coded decompensation

## Scientific question and hypothesis

For adults with hepatocellular carcinoma receiving a first recorded transarterial chemoembolization (TACE), does the direction and rate of early liver-function change after TACE identify patients at higher risk of subsequent hepatic decompensation beyond their current pre-treatment laboratory levels?

The falsifiable hypothesis is: among patients with no coded hepatic decompensation in the preceding 180 days, a worsening early trajectory (falling albumin, rising total bilirubin and/or INR, with platelet and creatinine context) from the pre-TACE window to days 1–7 after TACE is associated with a higher probability of a new coded hepatic-decompensation encounter on days 8–90, and a model using that trajectory is better calibrated and has higher clinically relevant net benefit than a model using only pre-TACE levels and history.

This is a prognostic/decision-support hypothesis, not a causal claim that TACE causes decompensation and not a claim that an algorithm establishes true liver failure.

## What is established versus unresolved

The strongest available external evidence I inspected is a 2026 retrospective TACE cohort (DOI 10.3389/fonc.2026.1794553; frozen source [source checksum]). It reports that baseline tumor burden, portal-vein tumor thrombosis, Child–Pugh class, INR and AFP predict overall survival, with internal validation. Its cohort had standardized imaging, procedure details, clinical adjudication and follow-up that are not present in this HCC snapshot.

That supports the narrower premise that baseline hepatic reserve and tumor biology matter after TACE. It does not establish that within-person peri-TACE laboratory change adds prognostic information, nor that a local coded decompensation endpoint can reproduce radiographic response, Child–Pugh status, procedural selectivity or survival. The unresolved question is whether the available routine longitudinal measurements contain an early, reproducible reserve signal that could identify who needs closer post-procedure monitoring. The substantive advance over a single baseline score is an explicit test of recovery versus worsening, with patient-level uncertainty and a direct comparison against a current-level baseline.

## Population and temporal design

Use only the discovery partition specified by the catalog: participant-level SHA-256 partition sha256("ehr-hypothesis-discovery-v1" + NUL + "hcc" + NUL + Patient master index) mod 100, buckets 0–79. Do not access the reserved buckets 80–99. All splits below are by Patient master index, never by row or encounter.

1. Candidate population: encounters for adults (age plausibly 18 or older after a value audit) with a diagnosis name containing hepatocellular carcinoma or liver cancer in diagnoses, and a procedure row whose Surgery is exactly TACE case-insensitively or contains chemoembolization.
2. Index: for each patient, the earliest qualifying TACE start time in the discovery partition. If multiple procedure rows describe the same encounter, retain the earliest timestamp and deduplicate to one patient index. Require an index encounter in encounters and retain its visit number.
3. Exclude patients with a coded hepatic decompensation term (ascites, liver failure, hepatic failure, decompensation, hepatic encephalopathy or hepatic coma) on an encounter whose admission time is in days -180 through -1. Also exclude a concurrent liver resection or ablation procedure in days -7 through +7, because the estimand is the post-TACE trajectory rather than a mixed-treatment episode.
4. Baseline window: laboratory observations with test time from days -14 through -1 relative to index TACE. Early window: days +1 through +7. The primary model must not use any data after day +7.
5. Primary analytic cohort: at least one valid numeric observation in the prespecified primary assays in each window, plus a computable outcome observation window. The exact complete-case count, assay coverage and missingness will be reported by the compiled audit rather than guessed here.
6. Primary outcome: a new coded hepatic-decompensation encounter on days +8 through +90 after index, where diagnosis name contains one of the decompensation terms above and the associated encounter admission time lies in that interval. To avoid treating a chronic label as a new event, require no matching term in the -180 to -1 history window. The primary outcome is deliberately called coded because diagnosis rows have no diagnosis-time field and lexical context is imperfect.
7. Secondary outcomes: coded decompensation in days 0–7 (descriptive safety outcome, not used as a predictor target), coded ascites alone, coded hepatic encephalopathy alone, coded bleeding/infection, and coded recurrence/progression through day 365. These are exploratory and are not substitutes for adjudicated clinical events.
8. Follow-up: report the number with a later encounter at least 90 days after index and a sensitivity analysis among those with such evidence. Patients are not assumed event-free when no later record exists; censoring/observation limitations will be shown.

Use only relative intervals. Do not interpret local dates as a released calendar or assume complete death capture.

## Variables and exact source binding

All joins use the catalog relationship key patient master index, encounter number; one-to-many tables are aggregated before joining to the patient index.

- encounters: [internal dataset path], table encounters. Use Patient Master Index, Visit Number, Age, Sex, Visit Time, Admission Time, Discharge Time, Department. Names, identity numbers, phone numbers and insurance/card identifiers are not analysis variables and must be dropped from derived files.
- procedures: [internal dataset path], table procedures. Use patient master index, encounter number, surgery, start time, end time, surgery source to define TACE and exclude mixed-treatment index episodes. The full scan found 78,067 rows matching explicit TACE/chemoembolization text, 39,886 encounters and 19,675 patients before discovery-partition and cohort filters.
- diagnoses: [internal dataset path], table diagnoses. Use patient master index, encounter number, diagnosis name, diagnosis type; attach encounters.admission time as the available event-time proxy. Preserve the distinction between admission diagnosis, attending physician diagnosis, discharge diagnosis, death diagnosis and unknown in sensitivity analyses; do not claim this is adjudicated outcome timing.
- labs: [internal dataset path], table labs. Use Patient Master Index, Encounter Number, Test, Quantitative Result, Qualitative Result, Specimen Type, Test Time. Primary assay-name whitelist is exact: albumin, total bilirubin, international normalized ratio, platelet count; secondary context assays are exact creatinine, sodium, alpha-fetoprotein, plus explicitly listed (urgent) variants in a sensitivity analysis. Parse numeric Quantitative Result only. Because the guide states that lab numeric results have no separate unit column, never pool unlike assay names, infer units, or compute a cross-assay score requiring an unverified conversion.
- medications: [internal dataset path], table medications. Use only as pre-index context (for example, documented supportive or antineoplastic medication exposure) after exact-name audit, with Start Time and End Time; do not infer administered dose from the free-text product name.
- examinations: [internal dataset path], table examinations, and pathology: [internal dataset path], table pathology. Use structured procedure/context counts and exact diagnosis fields only in sensitivity/descriptive analyses. Their narrative fields can support later expert adjudication, but no unvalidated NLP-derived stage, tumor size, radiologic response or metastasis label is a primary covariate.
- clinical_documents: [internal dataset path], table clinical_documents. Use only for a blinded manual adjudication sample if authorized/available, or as a sensitivity audit. It has no temporal columns; do not use post-index document text as if it were a dated lab or outcome.

The nominal vitals, transfers and front_page sources are identifier-only and contribute no clinical measurements. There are no images or raw waveforms. The local snapshot has no institutional release manifest, and exact dates are not released for external interpretation.

## Feature construction

For each assay and time window, retain the median numeric value and number of observations. For the primary analysis, standardize each exact assay name using the training-fold median and IQR only; retain raw-within-assay values for interpretability. Define trajectory features as early minus baseline robust-standardized values, the number of days between window medians, and an indicator for worsening direction (albumin down; bilirubin/INR up). Platelets, creatinine, sodium and AFP are contextual covariates, not components of an invented liver score. Include age, sex, prior 180-day encounter count, prior cirrhosis/portal-hypertension diagnosis flags, and index-year-free relative timing features only if their availability is clear. Missingness and test-count features are reported and evaluated as possible care-process signals, not silently imputed as normal.

## Prespecified baseline and substantive alternative

Baseline model: penalized logistic regression for the primary coded outcome using pre-TACE assay medians, age, sex, prior coded liver disease/decompensation history, encounter count and index treatment-context indicators. Use multiple imputation or a missingness category fitted within each training fold, with a complete-case analysis as sensitivity. This is a clinically recognizable current level plus history benchmark.

Dynamic alternative: a Bayesian assay-specific latent-reserve state-space model. Each exact assay is an observation stream with its own robust scale and measurement-error term; a shared latent reserve state has a pre-TACE level and a post-TACE transition, with separate assay loadings, irregular observation times and an explicit recovery/worsening slope. Fit the transition and outcome link on the training patients only; use the posterior mean and 95% interval of the day-7 latent change to predict the day 8–90 coded outcome. The alternative answers a scientific question the baseline loses: whether the within-person response pattern (including rate, discordance and uncertainty) carries information beyond the current lab level. It is not justified by complexity or a small score gain.

Use a patient-level 60/20/20 train/tune/test split within the discovery partition, generated deterministically from a second documented hash fold. Tune only on the tune set. The test set is touched once for final comparison. If the dynamic model is unstable, retain the baseline result and report the alternative as inconclusive; do not replace the scientific question with a simpler endpoint.

## Estimands and uncertainty

Primary estimand 1 is the adjusted odds ratio and 95% bootstrap confidence interval for a prespecified IQR increase in the latent worsening trajectory (and, separately, each assay trajectory) for day 8–90 coded decompensation. Primary estimand 2 is paired test-set change in log loss and Brier score for dynamic versus baseline predictions. Report AUROC and AUPRC, calibration intercept/slope and reliability plots, and decision-curve net benefit at thresholds chosen before looking at test outcomes (5%, 10% and 20% are reporting thresholds, not treatment targets). Use patient bootstrap resampling for intervals; do not treat repeated lab rows as independent observations.

## Falsification and interpretation

- Supportive: the worsening trajectory has a directionally adverse adjusted association with a reasonably precise interval, the dynamic model improves held-out log loss/Brier with uncertainty excluding no improvement, calibration is not worse, and net benefit improves at a clinically plausible monitoring threshold. This supports incremental prognostic information for the coded endpoint only.
- Adverse/falsifying: the trajectory association is null or reversed with a sufficiently precise interval, or the dynamic model performs no better/worse than baseline on held-out proper scoring and calibration, especially if apparent gains disappear when test-frequency/missingness features are removed. This would refute the claim that the early trajectory adds reliable information in this snapshot; it would not show that liver reserve is biologically irrelevant.
- Inconclusive: few complete trajectories/events, unstable assay harmonization, wide intervals, inadequate 90-day observation, or materially different results by diagnosis type/history exclusion. Report this as a data/support limitation, not as support for the hypothesis.
- Prespecified negative controls: use a pre-index-only model, a shuffled post-index lab-time permutation within patient, and a model using test-count/missingness only. A large apparent trajectory effect that survives only in the missingness model or disappears under time permutation is evidence of leakage/care-process bias.
- The verifier can check joins, windows, fitting, held-out predictions, estimates, intervals, scoring and the relation of conclusions to those outputs. It cannot determine whether a diagnosis label represents clinically adjudicated decompensation, whether TACE caused it, or whether a monitoring policy benefits patients.

## Required deliverable

The scientific deliverable is a newly fitted patient-level baseline model and a newly fitted latent-trajectory model, not merely an input audit. Completion requires: (1) cohort flow and actual sampling/filtering counts, (2) assay coverage and outcome counts, (3) frozen train/tune/test membership hashes, (4) fitted model parameters and posterior trajectory summaries, (5) held-out predictions, (6) bootstrap uncertainty, (7) calibration/scoring/net-benefit comparison, (8) negative-control/falsification outputs, and (9) a conclusion classified as supportive, adverse or inconclusive with no stronger clinical claim than the data permit. Clinical adjudication of coded decompensation and any treatment recommendation require expert review and an additional validated cohort.
