> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: a capture-calibrated reassessment boundary after TACE

## Episode, parent, and actual scientific deliverable

This is a substantive child of assessed candidate `[prior hypothesis]`. It preserves that parent’s HCC cohort, frozen TACE vocabulary, day-45 landmark, paired laboratory trajectory, competing recorded-care outcomes, observation-process audit, censoring sensitivity, and evidence limits.

The remaining repair is a clinical decision-boundary repair. The parent estimates whether an observed trajectory is associated with a later recorded action, but does not predefine when that association would be strong enough to justify a prospective reassessment trigger or how much alert burden such a trigger would impose. The solver must therefore newly estimate a day-45, 320-day probability of a first recorded liver-directed action and select a burden-constrained operating threshold on the tuning split.

The actual deliverable is a locked-test comparison of:

1. B0, a transparent capture-adjusted competing-risk model without the post-index biomarker trajectory;
2. B2, the matched transparent model adding the prespecified AFP/hepatic trajectory and its missingness indicators; and
3. M3, a substantive irregular-time latent observation model using the same target and patient-level splits.

For each model, the solver must produce a threshold selected without locked-test outcomes, trigger rate, sensitivity, positive predictive value, false-alert rate, number flagged per observed liver-directed action, calibration, and uncertainty. The primary boundary is the smallest predicted-risk threshold attaining at least 90% sensitivity for a later liver-directed action in the 2023 tuning set, using training-only censoring weights. Secondary boundaries target 80% and 95% sensitivity. This is an operational research boundary for recorded care, not an established clinical cutoff.

## Unresolved question and hypothesis

The strongest supported claim from the inspected local evidence is that the HCC snapshot contains dated encounters, diagnoses, procedures, laboratory rows and examination rows that can be linked by patient and encounter identifiers. A prior all-row audit read 105,044 encounter rows and 338,040 procedure rows and found 19,496 patients with a first TACE-like index, 15,605 with another procedure during days 0–45, 1,468 with a first repeat-TACE-like procedure and 1,491 with a first alternate liver-directed procedure during days 46–365, and 4,524 with a joined encounter at least 365 days after index. These counts establish feasibility and ascertainment constraints only. They do not establish response, recurrence, treatment failure, benefit, survival, or a useful trigger.

Primary unresolved hypothesis H1 is:

> Among adults with a structured HCC diagnosis and a first TACE-like recorded procedure who remain free of a liver-directed procedure through day 45, adding the prespecified early AFP/hepatic trajectory to a capture-adjusted transparent model will produce a more specific reassessment boundary than the capture-adjusted no-trajectory baseline: at a prespecified 90% sensitivity for first recorded liver-directed action during days 46–365, it will reduce the alert fraction by at least 10 absolute percentage points on the locked test, with a 95% interval excluding no reduction, and the reduction will not be reproduced for first non-liver procedures or the pre-index placebo trajectory.

H1 is a prognostic prediction hypothesis about recorded local care. It is not a claim that the trajectory measures viable tumour, that a recorded action means progression or treatment failure, or that alerting or treating a flagged patient improves outcomes.

A secondary model-information hypothesis asks whether M3’s asynchronous latent states and informative-observation process yield a further substantive boundary improvement over B2. M3 is considered informative only if it lowers alert fraction by at least 5 absolute percentage points versus B2 at the same 90% sensitivity, with calibrated locked-test predictions and an interval excluding no reduction. If it does not meet that margin, its latent state and measurement-process estimates are still reported as mechanistic/measurement diagnostics rather than promoted for use.

## Population, index, landmark, and outcomes

Use one index per patient. A TACE-like procedure is a procedure name matching case-insensitive `TACE`, containing `transarterial chemoembolization`, or containing both `hepatic artery` and `embolization`. Collapse qualifying rows within 24 hours and anchor the earliest `start time`. Require age >=18 and nonmissing `sex` in the joined encounter. Require a diagnosis name containing the literal `hepatocellular carcinoma` in a joined encounter from 180 days before through 7 days after index. Include indices through 2025-01-01 so that a full 365-day horizon is possible.

The day-45 landmark cohort excludes a procedure after index + 24 hours through day 45 if its name is repeat-TACE-like or alternate liver-directed. Report those early procedures separately; they are not non-events or evidence of response. Alternate liver-directed names contain `resection`, `ablation`, `radiofrequency`, or `microwave`, excluding TACE-like procedures.

From index day 46 through day 365, define the first recorded competing outcome as:

- repeat TACE-like procedure;
- alternate liver-directed procedure;
- first non-liver procedure, used as a capture-control outcome.

Also report combined liver-directed action and cumulative incidence functions. A non-liver procedure is not treated as a competing biological outcome; it is a control for general local-care capture. A patient with no recorded action is not called successfully treated or disease-free.

If liver-directed and non-liver procedures have exactly the same first timestamp, label the observation a same-time competing tie and exclude it from the primary ordered-category contrast; report sensitivity analyses assigning the tie to liver-directed and non-liver first, respectively. This prevents an arbitrary timestamp tie from creating a clinical interpretation.

## Prespecified trajectory and observation process

For AFP, use the last parseable numeric value in days -30 through -1 and the first in days 7 through 45. Define z = log1p(AFP), AFP improvement as z_post <= 0.5*z_pre, and retain continuous change, assay/qualitative flags and missingness. For albumin, total bilirubin, prothrombin time ratio, and platelets, use the last pre-index and first early-post value. Non-deterioration means early >= pre for albumin/platelets and early <= pre for bilirubin/coagulation ratio. Do not call the coagulation measure INR, pool assays, compute ALBI or MELD, or use cross-assay units: the local lab schema has no separate unit column.

The primary trajectory category is AFP improvement plus non-deterioration in at least two hepatic proxies. Continuous changes and each component are secondary outputs. The solver must retain a complete paired-trajectory indicator rather than imputing an absent post-index biological response.

Observation features known by day 45 include number and timing of joined encounters, laboratory row/day counts, assay availability, examination row counts and timing, non-liver procedure counts, and (optionally, in a declared sensitivity) dated order counts from `Order Time`, `Start Time`, and `End Time`. An order is not completion. Examination narrative text is excluded from the primary model; its use as an unvalidated lexical sensitivity must be separately audited and cannot be interpreted as radiology adjudication.

Define local observation time as the latest dated joined encounter among `visit time`, `admission time`, and `discharge time`. Censor at the first day after the last observed local contact or day 365, whichever comes first, unless an outcome occurs first. Fit censoring weights on training data only and report overlap, truncation and calibration. Repeat the boundary analysis in a stable-ascertainment subset with an encounter on or after day 365. No death or outside-care event is imputed.

The paired estimand is the boundary and risk contrast among complete paired-trajectory, eligible day-45 landmark patients. The full-index estimand reports trajectory availability/missingness and observation opportunity for every eligible index patient reaching day 45; it does not call an availability contrast a transported response effect. A full-index stabilized inverse-probability sensitivity is reported only if positivity, weight overlap and calibration pass.

## Exact HCC data bindings

All source data are read-only, HCC snapshot `[source checksum]`; every listed source is an ordinary CSV with no archive member.

- `encounters`: `datasets/hcc/table-b743286cb1249287.json`; source `[internal dataset path]`; [source checksum]; schema [source checksum]. Required columns: `Patient Master Index`, `Encounter Number`, `Age`, `Sex`, `Encounter Time`, `Admission Time`, `Discharge Time`, `Encounter Department`.
- `procedures`: `datasets/hcc/table-d5eae16f8f8093d9.json`; source `[internal dataset path]`; [source checksum]; schema [source checksum]. Required columns: `Patient Master Index`, `Encounter Number`, `Surgery`, `Start Time`, `End Time`, `Surgery Source`.
- `diagnoses`: `datasets/hcc/table-12710723c3df0c99.json`; source `[internal dataset path]`; [source checksum]; schema [source checksum]. Required columns: `Patient Master Index`, `Encounter Number`, `Diagnosis Name`, `Diagnosis Type`; diagnosis time comes only from the joined encounter.
- `labs`: `datasets/hcc/table-38aad8c54471332f.json`; source `[internal dataset path]`; [source checksum]; schema [source checksum]. Required columns: `patient master index`, `encounter number`, `test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`.
- `examinations`: `datasets/hcc/table-fd016d2731b9d6c6.json`; source `[internal dataset path]`; [source checksum]; schema [source checksum]. Required columns for primary use: `patient master index`, `encounter number`, `start time`, `examination`, `examination number`; `examination findings` and `examination diagnosis` are narrative and excluded from the primary model.
- Optional `orders`: `datasets/hcc/table-6b93dcf0ea823702.json`; source `[internal dataset path]`; required columns `patient master index`, `encounter number`, `order time`, `start time`, `end time`; use only dated capture features.

Join every child table to encounters on (`patient master index`, `visit number`), verify duplicate behavior before aggregation, and preserve raw procedure/lab vocabulary audits. The diagnosis is not independently timed. Clinical documents and pathology are excluded from dated prediction because their schemas have no temporal columns. Vitals, transfers and front_page are identifier-only in the catalog and add no payload. Medication rows are not needed for the primary question.

The catalog is `[internal dataset path]` ([source checksum]). The catalog's participant hash partition is not an external validation set; any reserved inaccessible buckets must not be described as independent validation.

## Matched baseline and learned/mechanistic alternative

All models use identical population, outcome, censoring, split and locked-test rules.

B0 is a regularized discrete-time cause-specific hazard model with age, sex, encounter department, pre-index diagnosis/procedure-family counts, pre-index assay summaries and missingness, and day-45 capture features. It outputs cause-specific hazards, liver-directed CIF, non-liver CIF and calibrated 320-day risk. B0 is deliberately transparent and establishes whether a trajectory adds information beyond clinical history and observation opportunity.

B2 adds the frozen AFP/hepatic trajectory category, continuous component changes, component missingness and paired-trajectory availability. It uses no post-day-45 information. The primary incremental boundary comparison is B2 versus B0.

M3 is an irregular-time low-rank state-space model. It has AFP-informed latent activity and hepatic-function states, patient random intercepts/slopes, assay-specific informative-observation submodels, observation intensity, and competing action hazards. It estimates the day-45 state from measurements available through day 45 and outputs posterior state/slope uncertainty. On the paired population, M3 uses actual observed trajectories; on the full-index analysis, a missing-data category is explicit and no absent post-index response is imputed. M3 can reveal asynchronous shape, discordance and timing/measurement intensity that a thresholded phenotype loses. It cannot recover unmeasured tumour burden, treatment intent, access, outside care or a biological response label.

The method comparison tests a scientific uncertainty about whether a prespecified trajectory provides a stable, action-specific alert boundary and whether any additional information is in longitudinal shape rather than in care capture. It does not chase a small generic predictive improvement. A transformer adaptation is deferred because the single-site recorded-action endpoint makes observation-process identification and vocabulary audit more informative than extra sequence capacity. The inspected methods summary supports dated sequence learning and latent longitudinal modeling as possible adaptations, but the demonstration cohorts, external validations and original data are not available locally; no reproduction claim is made. The cancer demonstration's main article and full STAR Methods were unavailable in the supplied bundle, and image files are absent. The Bayesian demonstration's genetic inputs are unavailable, so no genetic analysis is proposed.

## Splits, threshold selection, uncertainty, and falsification

The primary split is by index date: 2010–2022 fit, 2023 tuning, and 2024–2025-01-01 locked test, with no patient crossing splits. If date support fails, use the catalog's deterministic participant-hash buckets and record the fallback; this is still not external validation. Freeze vocabulary, parsing, feature construction, imputation, model settings and censoring models before locked-test evaluation.

For each model, select the 90% boundary on the 2023 tuning set as the smallest threshold with IPCW sensitivity >=90%, breaking ties toward the higher threshold only when sensitivity remains >=90%. Never select thresholds on locked-test data. Report the same predeclared threshold procedure at 80% and 95% sensitivity. On the locked test, report cause-specific sensitivity, cumulative-incidence-sensitive performance, alert fraction, PPV, false-alert fraction, number flagged per liver-directed event, calibration-in-the-large, calibration slope, Brier/log score, and bootstrap intervals clustered by patient. The primary absolute alert-burden contrast is B2 minus B0 at 90% sensitivity; the learned-model contrast is B2 minus M3. Bootstrap threshold selection is repeated within each resample or a nested fixed-threshold sensitivity is shown, so threshold uncertainty is not hidden.

Support for H1 requires all of the following: (a) B2 achieves the locked-test target sensitivity within the prespecified uncertainty convention; (b) B2 reduces alert fraction versus B0 by >=10 percentage points and its 95% interval excludes zero; (c) the reduction is stable in the complete-follow-up subset and literal-vocabulary sensitivity; and (d) neither the non-liver control nor the pre-index placebo shows a comparable trajectory-specific boundary gain. A result meeting only predictive calibration or log-score improvement is not H1 support.

Support for the secondary M3 hypothesis requires a >=5 percentage-point lower alert fraction than B2 at the same 90% sensitivity, calibrated locked-test risk, stable convergence and no worsening of the non-liver/placebo specificity checks. A smaller gain is reported as an exploratory model difference, not a clinically meaningful boundary advance.

Adverse evidence is null or reversed boundary gain, attenuation after adding capture features, comparable non-liver or placebo gain, unstable operating points, failed positivity/weight diagnostics, substantial complete-follow-up reversal, M3 nonconvergence, or calibration failure. If trajectory availability alone predicts action while the paired trajectory does not, that supports measurement/care capture rather than a trajectory-specific signal. Inconclusive evidence includes too few eligible paired patients or events, high loss-to-local-follow-up, sparse or incomparable assays, unresolved raw-name ambiguity, same-time tie prevalence, or unstable intervals.

## Interpretation and unavailable evidence

A supportive result establishes only that a local EHR-derived rule can reproducibly stratify the probability of a later recorded liver-directed action, with a quantified alert burden, in this source and time split. It could justify a prospective silent reassessment study or clinician adjudication study. It does not establish response, recurrence, viable tumour, treatment failure, treatment benefit, survival, clinical utility, cost-effectiveness, or a recommendation to repeat TACE.

The dataset has no image files, validated radiology response labels, explicit treatment intent, reliable tumour burden/number/size, death linkage for this analysis, outside-care capture, access/eligibility reasons, external institution, or separate laboratory unit column. Examination report text is present but is an unvalidated narrative source and is not a substitute for expert imaging review. Exact calendar dates are not released, so only within-patient intervals are used. Expert radiology/pathology adjudication, treatment-intent review, validated units, mortality/outside-care linkage, external validation, and a prospective impact study are required for stronger clinical conclusions. A clinical decision threshold would additionally require expert-selected harms/benefits and an impact evaluation; the 90% boundary here is not that threshold.

## Required artifacts and compute

The solver must write: `index_manifest.csv`, `landmark_manifest.csv`, `split_manifest.csv`, `predictions.parquet`, `metrics.json`, `bootstrap_intervals.json`, `decision_boundary.csv`, `operating_curves.csv`, `threshold_selection.json`, `procedure_vocabulary_audit.csv`, `early_pathway.csv`, `availability_selection.csv`, `examination_proxy_audit.csv`, `negative_control.csv`, `weight_diagnostics.json`, `model_parameters.json`, `interpretation.json`, and `limitations.csv`. Outputs must carry snapshot/schema hashes, filtering counts, split definitions and the interpretation-to-output map.

Completion requires newly fitted B0/B2 coefficients and M3 latent/observation parameters, locked-test individual CIF predictions, thresholds selected on tuning only, operating-point contrasts with patient-level uncertainty, calibration/log-score intervals, early-action and censoring diagnostics, negative-control results, and a conclusion that is explicitly linked to those outputs. Computation can establish these artifacts and numeric contrasts; it cannot adjudicate clinical response, intent, benefit, utility or external validity.

The prior all-row encounter/procedure audit is measured at 3.27 seconds using 8 CPUs and 32 GiB and is only a feasibility diagnostic. Current discovery compute is limited to 7,200 science seconds. The proposed future solver envelope is up to 16 CPUs, 262,144 MiB and 28,800 seconds as recorded in the assessed parent’s planning note; the full preprocessing, M3 convergence and bootstrap duration remain unverified. B0/B2 should fit on CPU. M3 should first use sparse CPU fitting; one allocated A100 may be used only if repeated optimization materially benefits, with `cuda:0` inside the allocation. GPU use is optional and no proposer/solver weights are trained.
