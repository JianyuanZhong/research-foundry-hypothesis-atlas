> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Pre-admission local-care trajectories and the next 72-hour recorded transition after an HCC-coded admission

## Decision, scientific deliverable, and substantive advance

This is a substantive child of `[prior hypothesis]`. The parent established a semantics-independent, exhaustive admission-anchored recorded-procedure transition endpoint, with an early [0,12) laboratory-to-[24,72) outcome buffer. This child keeps that endpoint and asks a clinically distinct unresolved question:

> Among all eligible adult first-observed HCC-coded inpatient admissions, does the patient's **pre-admission local-care and assay trajectory** add calibrated information about the complete recorded transition through 72 hours beyond admission context and the first 12 hours of current-admission laboratories?

The target is coordination and risk stratification of recorded care, not treatment selection. No result may be called treatment intent, treatment benefit, causal utility, active HCC, or external validation.

The future solver must newly produce:

1. a frozen all-admission cohort, patient-level partition, pre-admission history window, source/time audit, and unchanged parent endpoint;
2. locked predictions from four nested information sets on the same split:
   - A: admission context only;
   - L: A plus the first 12 hours of current-admission assay history (the incumbent information set);
   - H: L plus a transparent, source-separated summary of the prior 730 days;
   - S: L plus an irregular learned state-space representation of those same prior-730-day events;
3. the primary held-out incremental comparison H versus L, with S versus H as a secondary representation comparison;
4. patient-clustered uncertainty, calibration, history-availability strata, exact competing-state probabilities, process-only diagnostics and prespecified falsifications; and
5. a claim-to-output table separating computable recorded-care associations from claims requiring clinical adjudication, linkage or another study.

A null history increment is a scientifically meaningful completion outcome. The study is complete when the cohort/time audit, exhaustive labels, locked predictions, proper-score/calibration intervals, sensitivity analyses and interpretation gates are reported; it is not necessary to confirm the hypothesis.

## What is supported and what remains unresolved

The verified HCC snapshot contains encounter dates, assay-specific native laboratory timestamps, native procedure timestamps, and timestamped order/medication records. The parent’s source audit reported 42,692 provisional first-patient admissions, 146,703 linked procedure rows, 86,025 midnight procedure starts, 9,077 missing/unparseable procedure starts, 25,527 valid starts in [0,24), and 51,332 valid starts in [24,72). Those are feasibility figures, not locked endpoint results; the solver must recompute them after the rules below. Direct inspection of the ordinary CSV headers and rows confirms the required Chinese fields (rendered in English here) and timestamp formats, including `Admission Time`, `Discharge Time`, `Test Time`, `Surgery`, `Start Time`, `Order Time`, and medication `Start Time`.

The strongest supported claim is only that this local snapshot can record prior encounters, assays and care-process rows before an admission, and can record subsequent procedures and discharge. Diagnoses have no native diagnosis time. The source has no laboratory unit/reference-range column, no images or raw waveforms, no validated clinical concept extraction, and no reliable evidence of outside-hospital care, indication, scheduling, consent, receipt, completion, response, toxicity, mortality or treatment intent.

The unresolved claim is the incremental-information hypothesis above. It is falsified, for this snapshot and endpoint, if adding the pre-admission trajectory does not improve held-out calibrated prediction, if any apparent improvement is reproduced by documentation-intensity-only variables, or if the improvement survives history-label/time permutation that should destroy temporal content.

## Population, anchor and temporal boundaries

Use HCC snapshot `[source checksum]), catalog [source checksum], and all source files as read-only ordinary files.

Normalize Unicode and whitespace in keys and diagnosis text. Join `diagnoses` to `encounters` on the exact pair (`Patient Master Index`, `Visit Number`). The cohort diagnosis rule is frozen as normalized `hepatocellular carcinoma` or case-insensitive substring `hepatocellular carcinoma` in `Diagnosis Name`; print the regex, all matched strings, diagnosis-type overlap, duplicate keys and unmatched keys before prediction. This identifies a record-coded cohort, not active HCC.

Require age >=18, parseable native `admission time` and `discharge time`, nonnegative length of stay, and the parent’s calendar boundary [2011-01-01, 2026-01-01). Retain the earliest eligible HCC-coded encounter per `patient master index`, ordered by native `admission time` and then `encounter number`; do not replace an invalid earliest record with a later record. Set (t_0) to `admission time`. Exclude direct identifiers (`name`, `national ID number`, `mobile phone number`, `medical insurance/visit card number`, `hospitalization number`) from all features. Keep every eligible anchor admission in the primary estimand, including early discharge, early procedure and unresolved-time states.

Use half-open elapsed-time intervals in hours. The pre-admission history window is exactly [(t_0-730) days, (t_0)); current-admission labs are exactly [(t_0,t_0+12) h); the parent outcome windows remain [(t_0,t_0+24) h) and [(t_0+24,t_0+72) h). A history row is eligible only when its native event/documentation time is strictly less than (t_0); this strict rule applies even if the row is linked to the anchor encounter. For the primary history cohort, preferentially require a linked prior encounter with native `Admission time` < (t_0), and audit any row linked to the anchor encounter that nevertheless has a pre-anchor timestamp rather than silently using it. A left-truncation indicator records whether any encounter begins before (t_0-730) days.

History timestamps are:
- prior encounter timing: `encounters.admission time` and `discharge time`; 
- prior assay timing: `labs.test time`;
- prior procedure timing: `procedures.start time` (with `end time` retained for audit);
- prior non-drug order documentation timing: `orders.Order Date` as the primary process timestamp, with `Start Time`/ `End Time` retained only for sensitivity;
- prior medication documentation timing: `medications.start time`, with `end time` retained for audit.

Unparseable times are excluded from the primary history features but counted by source, encounter, patient and time-window; they are not coded as absence. The solver must print source row counts, linked-key multiplicity, invalid-time counts, prior-window counts, current-window counts, boundary/tie counts and patients with no prior record.

## Unchanged primary endpoint

Copy the parent’s label construction exactly and make no history variable available to it.

For every eligible admission, use procedure presence and native `procedures.Start Time` only:

- `P0`: a valid procedure start in [0,24) before `discharge time`;
- `D0`: discharge at or before 24 hours before any valid early procedure;
- `U0`: a missing/invalid procedure time whose unknown position could change procedure-versus-discharge or boundary ordering;
- `R24`: no established `P0`, `D0` or `U0`.

Among `R24):

- `P1`: first valid procedure start in [24,72) before discharge;
- `D1`: discharge in [24,72) before any valid later procedure;
- `U1`: unresolved procedure timing that could change later ordering;
- `N72`: no established `P1`, `D1` or `U1) by 72 hours.

The primary all-admission estimand is the mean terminal probability vector at (t_0) over `P0,D0,U0,P1,D1,U1,N72). Fit/estimate the early distribution for every admission, the later conditional distribution among `R24), and marginalize to the complete vector. Report the `R24)-conditional distribution only as a secondary diagnostic. The primary tie rule is D0/D1 (discharge wins); procedure-wins is a sensitivity. Audit before-admission procedures, after-discharge rows, multiple rows at the same time, invalid dates, midnight starts, missing times, and all exact-boundary ties. Missing timing must never become no procedure.

The endpoint means a locally recorded procedural transition. It does not mean a liver-directed treatment, clinical decision, appropriate care, treatment receipt/completion, benefit, or causal effect. Procedure-string route families may be printed after primary labels and locked predictions as a descriptive secondary characterization only; they cannot define the primary endpoint.

## Exact information sets and pre-admission variables

All four models use the same eligible admissions, labels, patient split, preprocessing rules, regularization selection, and output target.

A (admission context) includes age, sex, admitting department (`Encounter Department`), calendar era, admission time-of-day, and missingness indicators. It does not use current or prior diagnosis text, procedure text, orders, medications, documents, pathology or examinations.

L (incumbent early-lab comparator) adds current-admission [0,12) assay-specific observations using `Test`, `Qualitative result`, `Quantitative result`, `Specimen type`, and `Test time`. Numeric and qualitative assays remain separate because units are absent. For each assay, use first/last valid numeric value, change, elapsed time, count, density/missingness and a slope only with at least two distinct native timestamps; nonnumeric results stay assay-specific categorical indicators. No [12,24) row is allowed. L is the prespecified comparator for the primary history question, even if the parent’s original pre-admission summary is also rerun as a sensitivity.

H (transparent history summary) adds only documented data in [(t_0-730) days,(t_0)):

- encounter process: number of prior encounters, number of prior inpatient days, days since last prior admission and discharge, number of distinct prior departments, and a left-truncation indicator;
- assay-specific labs: counts, distinct prior encounters, first/last numeric value, change, last-observation recency, elapsed span, supported slope, and qualitative-result/missingness indicators. Each `test` assay remains its own feature block; no cross-assay pooling or clinical score is allowed;
- procedures as recorded occurrence: count, distinct prior encounters, recency and inter-event gaps, without using `Surgery` text to infer indication or treatment family;
- orders and medications as documentation process variables only: row counts, distinct linked prior encounters, recency, gap/density and time-missingness. Do not use drug/order names, dose, frequency, route or status to claim treatment or intent. A prespecified source-ablation table will compare encounter+lab+procedure history with and without order/medication process blocks.

All count/recency features are computed within the fixed 730-day window and have explicit “no observation” indicators. Numeric transformation parameters, assay inclusion thresholds, clipping and imputation are fit on buckets 0–59 only and selected on 60–69. The solver must save a feature manifest with each Chinese column, time rule and source block.

S (irregular learned alternative) uses exactly the same prior-window rows as H, not a richer outcome or later data. Represent each prior record as an event with source/type, native time relative to (t_0), and payload permitted above: assay identity plus numeric value or qualitative token; generic encounter/procedure/order/medication process tokens; and missingness. It excludes diagnosis text, clinical-document text, pathology text, examination findings, direct identifiers and current/post-anchor records. Assay values are standardized within assay using fit-only parameters, never across assays.

Fit a low-dimensional continuous-time latent state-space model. Between irregular events, latent state (z) evolves with elapsed-time decay; at an event, an assay-specific emission/update uses the event type and observation mask. Learn assay-specific offsets/noise, time-decay and shrinkage parameters, and a coupled competing-state head for the unchanged early/later target. The primary fitting objective is supervised negative log likelihood of the complete terminal-state construction, with an optional masked-event reconstruction term fixed before selection and tuned only on bucket 60–69. Use no more than two latent coordinates unless selection demonstrates a reproducible need; call them latent coordinates, never validated “liver reserve” or “renal reserve” scores. S can expose order-sensitive recency, nonlinear multivariate trajectory patterns and uncertainty from irregular observation timing that H’s first/last/count summaries lose. A process-only sequence variant using source/time/count tokens but no assay values is mandatory to determine whether that gain is merely recording intensity.

## Split, estimand, evaluation and uncertainty

Assign each patient with SHA-256 of normalized `Patient Master Index` modulo 100: buckets 0–59 fit; 60–69 preprocessing, hyperparameter and regularization selection; 70–79 locked evaluation; 80–99 inaccessible and not external validation. Every encounter and row for a patient follows the same partition. Freeze cohort, windows, label/tie/missing rules, assay vocabulary, history payload, dimensions, hyperparameters and calibration procedure before reading locked test labels for model selection.

Fit sequential competing-state heads for the early and later distributions, then marginalize each model’s predictions to the same seven-state terminal vector. Primary outcomes are, on all eligible admissions:

1. paired change in held-out multiclass log loss and multiclass Brier score for H minus L;
2. calibration intercept/slope, reliability curves and observed-versus-predicted probability for every terminal state;
3. the same metrics for S minus H and S minus L.

Use at least 1,000 patient-clustered paired bootstrap resamples of locked predictions, preserving all admissions from each patient; report 95% intervals. A 500-resample fallback is allowed only if documented by the solver’s time budget. Use fit-only calibration (for example, multinomial temperature/Platt calibration selected on 60–69); never calibrate on bucket 70–79. Report state-specific probability contrasts, especially marginal `P1), only as secondary quantities. Report by patient buckets 0–59, 60–69, 70–79 and 80–99 exactly as configured: the first three are fit/selection/test partitions and the 80–99 bucket is inaccessible, not a result or validation set. Also report pre-admission availability strata (none, 1–2 prior encounters, >=3; and lab-observed versus process-only) as heterogeneity diagnostics, not subgroup causal effects.

The primary scientific deliverable is a calibrated, all-admission estimate of whether H adds information over L. It is not a threshold policy, net-benefit claim or clinical decision rule.

## Falsification and robustness

Freeze the following analyses before locked evaluation:

1. Shuffle pre-admission event times within patient and assay/source while preserving values and counts. A trajectory/order contribution should attenuate, while a pure count contribution may remain.
2. Shuffle complete pre-admission histories across patients within fit/selection/test partitions, preserving history length; H/S gains should disappear. Persistence suggests leakage or a split/label bug.
3. Fit the process-only history model. If it reproduces the full H or S increment, interpret the result as documentation/observation intensity, not patient physiology or care need.
4. Reverse pre-admission chronological order and compare S; an order-sensitive gain should attenuate. H should be unchanged except for explicitly order-dependent recency checks.
5. Verify no row linked to the current encounter with native time >= (t_0), no [12,24) lab, no post-discharge row, and no outcome-derived feature enters H/S. Run a forbidden-window sentinel using current [12,24) data to predict the already-started [0,24) endpoint; any gain indicates leakage and invalidates the affected result.
6. Recompute under 30-, 180- and 730-day history windows, and report left truncation. A result dependent only on the source’s observation start is not a stable long-history claim.
7. Repeat exact-boundary, discharge/procedure tie, midnight-start exclusion and conservative/optimistic unresolved-time rules inherited from the parent. Material reversals make the transition analysis inconclusive.
8. Permute labels within calendar era and department. Any persistent performance indicates leakage, duplicate patients across split, or a label artifact.
9. Run the parent’s original comparator with pre-admission nearest/count/recency summaries. This sensitivity distinguishes “any prior data” from the proposed richer local-care trajectory; it does not replace the prespecified H-versus-L estimand.
10. Report by admitting department and history availability. These are local heterogeneity/transport diagnostics, never external validation.

Supportive evidence requires H to improve held-out full-vector log loss and/or Brier score over L with a 95% paired patient-cluster interval excluding zero, without material calibration deterioration; the result should not be confined to one fit/test hash bucket or a single availability stratum; shuffled histories and reversed order should attenuate the relevant gain; and process-only features should not explain it all. S is supportive as a substantive representation only if it adds over H beyond uncertainty and remains calibrated, stable across seeds and timing sensitivities.

Adverse evidence is no H-versus-L improvement, worse calibration, a gain fully reproduced by process-only variables, persistence after cross-patient history shuffling, or a forbidden-window/split artifact. That rejects the incremental longitudinal-information explanation while leaving the endpoint and local recorded-care description valid.

Inconclusive evidence includes dominant `U0/U1` states, too few `R24` or `P1` observations, wide intervals, severe timestamp dependence, substantial left truncation without stable sensitivity, unstable calibration, or a result that cannot distinguish assay information from documentation intensity. Inconclusive is not confirmation.

## Exact HCC bindings and availability

Every usable clinical row is joined to the selected encounter by normalized (`patient master index`, `encounter number`), with duplicate, multiplicity and unmatched-key audits. Each listed archive member is the ordinary file itself; no archive member is used.

| Table and schema | Exact read-only source | Required columns and native time/role |
|---|---|---|
| `encounters` / `datasets/hcc/table-b743286cb1249287.json` | `[internal dataset path]` | `patient master index`, `encounter number`, `age`, `sex`, `encounter time`, `admission time`, `discharge time`, `encounter department`; anchor and prior-encounter times |
| `diagnoses` / `datasets/hcc/table-12710723c3df0c99.json` | `[internal dataset path]` | keys, `Diagnosis Name`, `Diagnosis Type`; HCC-coded cohort only, no native time |
| `labs` / `datasets/hcc/table-38aad8c54471332f.json` | `[internal dataset path]` | keys, `Test`, `Qualitative result`, `Quantitative result`, `Specimen type`, `Test time`; pre-admission and [0,12) assay trajectories |
| `procedures` / `datasets/hcc/table-d5eae16f8f8093d9.json` | `[internal dataset path]` | keys, `Surgery`, `Start Time`, `End Time`, `Surgery Source`; unchanged endpoint and prior generic occurrence history |
| `orders` / `datasets/hcc/table-6b93dcf0ea823702.json` | `[internal dataset path]` | keys, `non-drug medical order`, `order time`, `start time`, `end time`, `order duration`, `order status`, `frequency`; timestamped process counts only |
| `medications` / `datasets/hcc/table-4f6ecaeb6e8f69c2.json` | `[internal dataset path]` | keys, `Medication`, `Single Dose Amount`, `Single Dose Amount Unit`, `Frequency`, `Start Time`, `End Time`, `Administration Method`, `Drug Type`; timestamped process counts only, no treatment interpretation |
| `examinations` / `datasets/hcc/table-fd016d2731b9d6c6.json` | `[internal dataset path]` | keys, `examination`, `examination findings`, `examination diagnosis`, `start time`, `machine model`, `examination number`; audit/possible future descriptive extension, not primary history because narrative scope and units are unvalidated |
| `clinical_documents` / `datasets/hcc/table-66afca58512c2fca.json` | `[internal dataset path]` | keys, `Chief Complaint`, `History of Present Illness`, `Past Medical History`, `Personal History`, `Menstrual History`, `Marital and Childbearing History`, `Family History`, `Admission Diagnosis`, `Admission Status`, `Admission Diagnosis__duplicate_2`, `Diagnosis and Treatment Course`, `Discharge Status`, `Discharge Diagnosis`, `Surgery Name`, `Surgical Procedure`; no native time, not primary history |
| `pathology` / `datasets/hcc/table-0a4ee86a446c605c.json` | `[internal dataset path]` | keys, `Pathology`, `Findings`, `Diagnostic impression`, `Machine model`; no native time, no primary history |
| `vitals` / `datasets/hcc/table-8436de9cba74b8ca.json` | `[internal dataset path]` | keys only; identifier-only, no payload or time |
| `transfers` / `datasets/hcc/table-320c20f732e71789.json` | `[internal dataset path]` | keys only; identifier-only, no payload or time |
| `front_page` / `datasets/hcc/table-38b3224239acc33f.json` | `[internal dataset path]` | keys only; nominal/identifier-only, no primary history |

No archive member is applicable beyond “ordinary file.” These bindings are checked against `datasets/hcc/README.md`, `metadata.json`, the twelve schema JSON files and source headers. The HCC metadata states that all clinical tables are many-to-one to encounters only after duplicate verification, that lab numeric results have no separate units, and that text extraction is not a validated diagnosis extractor.

## Compute plan and feasibility limits

The discovery audit used managed CPU work because the lab, order and medication sources are multi-gigabyte files; it did not fit a reliable short shell read and no solver fit was run. A future solver may use the planning envelope in `inputs.json`: at most 16 CPUs, 262,144 MiB memory, 8 GPUs and 28,800 seconds. Discovery’s 7,200-second science budget is not the solver budget.

B0/A and L/H summary models, feature aggregation and locked-prediction bootstrap are CPU-first. Use chunked CSV scans and compact patient-level matrices; measured source sizes are approximately 2.2 GB labs, 2.19 GB orders, 491 MB medications, 113 MB examinations, 89 MB diagnoses, 35 MB procedures and 18.6 MB encounters. Expected future resources (unverified): 8–16 CPUs, 64–192 GiB RAM, 1–4 hours for source aggregation and summary fits, and 1–4 hours for 1,000 locked-prediction bootstrap resamples depending on state sparsity and implementation.

S is not excluded because it is learned. Its low-dimensional state-space fit is unverified on this snapshot. Plan one CPU run within 16 CPUs/192 GiB first; if convergence or repeated-seed fitting materially requires acceleration, request one allocated A100 (80 GB) using the cached `ehr-campaign-gpu:20260908` image, set model and tensors to `cuda:0`, and do not infer GPU absence from an ordinary shell. A bounded future feasibility probe may measure one epoch and memory, but must not be reported as the study result. Expected unverified S budget is 1 GPU, 4–8 CPUs, up to 64 GiB and 2–8 hours, plus CPU bootstrap. No GPU is mandatory.

The method choice is scientific: H is interpretable and directly tests whether clinically recognizable prior observation/trajectory summaries add information; S can reveal order-sensitive, nonlinear, irregularly sampled patterns and posterior state uncertainty that H loses. A large transformer is deferred because no measured need or validated benefit is established, not because neural models or GPUs are categorically disallowed. Reconsider it only if S has stable incremental value and the question specifically becomes whether long-range event order, rather than latent-state sufficiency, is responsible.

## Demonstration and seed dispositions

The three research demonstrations are methodological context, not topic or method mandates:

- Natural-history/Delphi: the local methods summary reports learned dated disease histories and a modified GPT-2; this proposal adapts only the scientific idea of comparing structured summaries with irregular sequence information. It does not reproduce the paper, UK Biobank cohort, code, genetics or reported performance.
- Bayesian longitudinal discovery: the local methods summary reports an irregular latent longitudinal model and CPU/GPU alternatives. This proposal uses an explicitly changed, HCC-only state-space adaptation with no genetic claim and no reproduction of its paper.
- Cancer/Oncoformer: the local README says the main article and full STAR Methods remain unavailable; only the supplement/metadata were available, and this HCC snapshot has no images. No claim about the inaccessible main text or a multimodal reproduction is made, and no image model is proposed.

The 30 expert seeds (10 UK Biobank, 10 MIMIC-IV, 10 eICU) contain no HCC problem. Their source fields, populations and limitations are dataset-mismatched; none is imported as a parent or treated as evidence for this HCC hypothesis. The HCC parent is selected from the assessed HCC population as assigned. No expert seed supplies active-HCC labels, local-care history or an HCC outcome here.

## Evidence limits and interpretation

Computationally checkable outputs are exact source/key/time audits, cohort and bucket counts, history feature manifests, endpoint states, locked predictions, log loss/Brier scores, calibration, state probabilities, bootstrap intervals, source-ablation results and falsification outputs. These can establish whether pre-admission local recorded history adds predictive information for this locally recorded transition distribution.

Clinical adjudication, additional linkage or another study is required for active HCC confirmation, diagnosis timing, tumor burden/stage/resectability, indication, scheduling, consent, intent, receipt, completion, appropriateness, treatment response, toxicity, mortality, causal benefit, bedside utility, outside-care completeness and transportability. The missing lab units prevent cross-assay physiologic scores. Any route-family analysis requires a prespecified clinician-blinded dictionary/adjudication protocol and remains secondary. A prospective clinical decision study would additionally need time-linked imaging/pathology, outcomes, calibration and net-benefit evaluation.

The substantive advance over the parent is therefore precise: it tests whether a temporally prior, source-separated local-care/assay trajectory adds calibrated information beyond admission context and the first 12 hours of current labs, while preserving the parent’s exhaustive all-admission recorded-transition endpoint and refusing stronger clinical or causal interpretations.
