> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: selection-aware transport of post-TACE trajectory information

## Parent and substantive repair

This episode-13 child evolves assessed valid parent `[prior hypothesis]`. It preserves the parent’s one-index HCC cohort, 24-hour procedure episodes, day-45 landmark, days 46–365 competing recorded-care states, reassessment-anchored versus unanchored TACE split, administrative end-of-local-observation state, patient-level temporal split, capture-adjusted baseline, and irregular-time alternative.

The remaining clinically consequential uncertainty is transport through measurement selection. A post-TACE AFP/hepatic trajectory exists only when the local system obtains the relevant tests. A missing trajectory can mean stable care, outside care, access/capture loss, clinician choice, or simple missingness; the available HCC snapshot cannot distinguish these. A model that predicts recorded TACE among the measured subgroup may therefore not answer whether this information could support surveillance for the full day-45-eligible population. The parent includes missingness features, but this child makes the conditional-versus-full-population estimands and an observation-only comparator explicit.

This is not a claim that testing is random, that weighting identifies a causal effect, or that the trajectory measures viable tumor or response.

## Evidence-supported and unresolved claims

The strongest supported claim is operational: the frozen HCC snapshot has linkable dated encounters, procedures, labs, and examinations. The parent’s audit found 105,044 encounter rows, 338,040 procedure rows, 1,810,646 diagnosis rows, 106,963 TACE-lexicon procedure rows, and exact source/schema bindings. Those are availability and coding facts, not evidence of intent, indication, response, mortality, or benefit. The source has no validated outcome adjudication, no released images or waveforms, no separate laboratory-unit column, and no time field in clinical_documents or pathology.

The unresolved claim is:

> Among adults with HCC and a first recorded TACE-like episode who are free of a liver-directed therapeutic episode through day 45, does an early AFP/hepatic trajectory add reproducible information about a later reassessment-anchored TACE-containing recorded pathway in the full eligible local cohort, beyond information about who gets measured and remains observable?

The primary falsifiable hypothesis is that, on a locked temporal test, adding the prespecified trajectory and its missingness pattern to an observation-aware baseline will reduce the alert fraction at 90% sensitivity for first reassessment-anchored TACE by at least 10 percentage points, with a patient-bootstrap 95% interval excluding zero, after standardizing/transport-weighting the measured trajectory to the full day-45-eligible cohort. The reduction must exceed the corresponding gain for TACE without a prior local reassessment opportunity by at least 5 points and must not be reproduced for a non-liver capture control or pre-index placebo. A separate observation-only model must not explain nearly all of the gain. These margins are operating criteria for reproducible local recorded-care information, not clinical utility or treatment recommendations.

## Population, time, outcomes and selection estimands

Use one index per patient.

- Join child tables to `encounters` only after aggregating each child table to (`Patient Master Index`, `Encounter Number`); never form many-to-many joins.
- Group procedure rows whose parsed `start time` values are within 24 hours into episodes, retaining raw names, source, start/end times, encounter key, row count, family hits, missing-time flags and composite status. Missing `start time` rows cannot define event time and are reported.
- Index = earliest episode containing literal `TACE`, a name containing `transarterial chemoembolization`, or both `hepatic artery` and `embolization`.
- Require age >=18 and nonmissing `sex` on the index encounter.
- Require a diagnosis name containing `hepatocellular carcinoma` on a joined encounter from 180 days before through 7 days after index; diagnosis has no time field and inherits the encounter time only for this cohort criterion.
- Include index dates through 2025-01-01, giving a nominal one-year local horizon.
- Exclude/report any post-index liver-directed therapeutic episode after the first 24 hours through day 45 from the primary day-45 risk set; report these early pathways separately.
- Stop all predictors at day 45. Follow-up is days 46–365.

The population estimand is first-event cumulative incidence through day 365 with mutually exclusive states: `reassessment_anchored_TACE`, `TACE_without_prior_reassessment`, `alternate_liver_directed`, `mixed_liver_therapeutic`, `non_liver_procedure`, and `end_of_local_observation`; no-state patients remain `observed_no_action` under the declared local-contact rule. The parent’s unqualified first TACE-containing endpoint remains a secondary sensitivity.

Define a strict prior-local-reassessment flag for each future therapeutic episode using only records strictly before that episode and excluding its encounter: a dated liver-relevant lab, or a dated liver/abdominal examination, in the preceding 30 days. Use the parent’s frozen assay and examination-name screens. Encounter-only and 14-day/30-day windows are sensitivities. This is a dated documentation opportunity, not adjudicated tumor reassessment.

Define trajectory availability `A=1` before modeling as at least one parseable numeric AFP in days -30 to -1 and days 7–45, plus at least one of albumin, total bilirubin, the observed coagulation-ratio assay, or platelets in each window. Preserve partial-observation patterns rather than silently complete-casing. The complete-pair estimand is the association among A=1 patients; the full-index estimand standardizes it to all day-45-eligible patients using an observation model fitted only on the training split. The observation model predicts A from index history and variables known by day 45: age, sex, year, department, procedure/composite history, encounter/contact intensity, assay availability, examination opportunities, non-liver/unclassified procedure counts and missingness. Report overlap and positivity; do not weight outside unsupported regions.

Use the parent’s end-of-local-observation definition based on the maximum valid encounter, admission or discharge timestamp after day 45, with encounter-time-only sensitivity. Treat this as an administrative recorded state, never death or outside-care cessation. Report capture-inclusive and continued-local-observation analyses.

## Variables and exact information boundary

The trajectory uses last parseable pre-index and first early-post values for AFP, albumin, total bilirubin, the observed coagulation-ratio assay and platelets; log1p AFP, continuous changes, frozen direction indicators, exact assay identity, availability and missingness are retained. No cross-assay pooling, unit inference, ALBI/MELD construction or unit-dependent threshold is permitted because `labs` has no separate unit column.

Baseline history contains age, sex, index year, department, procedure family/composite status, pre-index procedure and diagnosis-history counts, assay summaries/missingness and day-45-known capture features. Clinical-document and examination report text are excluded from primary inference. Orders are a sensitivity-only opportunity/capture feature and are never treated as completed treatment. No future reassessment context, post-day-45 record, future test, or future procedure is a predictor.

## Baseline and substantive learned alternative

Fit all models on the same cohort, event ontology, split and uncertainty procedure.

1. **B0**, regularized discrete-time cause-specific competing-risk hazards using pre-index history and day-45 capture features, without laboratory values.
2. **Bobs**, B0 plus trajectory-availability and measurement-pattern variables but no laboratory values. This is the selection-only comparator.
3. **B2**, Bobs plus AFP/hepatic values and changes, with all-index missingness features. Report both the all-index fit and the A=1 complete-pair fit standardized to the full eligible cohort by training-only observation weights.
4. **M3**, a low-rank irregular-time joint state-space model with separate latent activity and hepatic-function trajectories, assay-specific observation models, observation intensity, and the same competing recorded-care hazards. It must predict the same context-stratified outcomes and cannot smooth the day-45 state with future data.

The central scientific contrasts are B2 versus Bobs (trajectory information beyond selection), complete-pair versus observation-weighted full-index estimates (transport), and reassessment-anchored versus unanchored TACE gains. M3 could reveal asynchronous biomarker shape, discordance and informative observation timing that B2’s paired summaries lose; it cannot recover intent, eligibility, tumor burden, radiologic response, mortality, outside care or benefit. A transformer is deferred because endpoint/context validity and selection—not sequence capacity—is the limiting uncertainty. Causal treatment-effect, radiology/image, and report-text models are deferred for absent validated treatment intent, outcome adjudication, images, reliable temporal text semantics and external linkage.

The future solver must newly construct the selection model, fit/estimate B0/Bobs/B2 and, if feasible, M3, and produce locked predictions, observed/full-index standardized risks, uncertainty, overlap diagnostics and context/pathway falsification. Completion is demonstrated by fitted parameters, predictions and interpretation files—not by readiness and not by a presumed positive result.

## Split, uncertainty and falsification

Use patient-level temporal splits: 2010–2022 fit, 2023 tuning, and 2024–2025-01-01 locked test. If calendar support fails, use deterministic patient hashing and label it internal. No patient crosses splits. Choose thresholds only on fit/tuning data, including training-only observation weights; report fixed-threshold and patient-clustered bootstrap intervals.

Required locked outputs include cause-specific and competing-risk sensitivity, alert fraction, PPV, calibration, Brier/log score, cumulative incidence, B2–Bobs gain, B0–B2 gain, complete-pair versus full-index estimates, anchored/unanchored gain difference, observation-model overlap/positivity, weight truncation, context rates, and event counts. Include procedure vocabulary/mixed/unclassified/tie/missing-time audits, last-contact and context-window sensitivities, a non-liver capture control, and a pre-index trajectory placebo.

Supportive evidence requires the prespecified 10-point anchored alert reduction with an interval excluding zero after transport, stability under observation and context sensitivities, at least a 5-point anchored-over-unanchored gain difference with uncertainty excluding zero, a smaller/no comparable gain for Bobs alone, non-liver control and placebo, acceptable overlap/calibration, and converged M3 if attempted. Adverse evidence includes Bobs explaining nearly all gain, conditional gain disappearing after weighting, stronger gain for unanchored/non-liver/placebo, gain confined to high-contact strata, unstable context definitions, poor overlap, calibration failure, or M3 nonconvergence. Inconclusive evidence includes sparse A=1 events, positivity failure, too few anchored events, wide intervals spanning margins, unresolved ties/missing times, inadequate follow-up or insufficient calendar support. Never relax rules after locked outcomes.

## Exact HCC source bindings

All sources are ordinary unarchived CSV files in HCC snapshot `[source checksum]`. Full catalog is `[internal dataset path]`, [source checksum]. Every solver output must record source and schema hashes.

- `encounters`, schema `datasets/hcc/table-b743286cb1249287.json`, source `[internal dataset path]`, [source checksum]; keys `Patient Master Index, Visit Number`; fields `Age, Sex, Visit Time, Admission Time, Discharge Time, Visit Department`.
- `procedures`, schema `datasets/hcc/table-d5eae16f8f8093d9.json`, source `[internal dataset path]`, [source checksum]; fields `surgery, start time, end time, surgery source`.
- `diagnoses), schema `datasets/hcc/table-12710723c3df0c99.json`, source `[internal dataset path]`, [source checksum]; fields `diagnosis name, diagnosis type`; no diagnosis timestamp.
- `labs`, schema `datasets/hcc/table-38aad8c54471332f.json`, source `[internal dataset path]`, [source checksum]; fields `Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time`; no unit column.
- `examinations`, schema `datasets/hcc/table-fd016d2731b9d6c6.json`, source `[internal dataset path]`, [source checksum]; fields `examination, examination findings, examination diagnosis, start time, model, examination number`; use only `start time` for dated opportunities.
- `orders`, schema `datasets/hcc/table-6b93dcf0ea823702.json`, source `[internal dataset path]`, [source checksum]; fields `Orders (non-drug), Order time, Start time, End time, Order status, Frequency`; sensitivity only.
- `medications`, schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`, [source checksum]; fields `Medication, Single Dose, Single Dose Unit, Frequency, Start Time, End Time, Route of Administration, Medication Type`; may be descriptive only because regimen semantics are unverified.
- `clinical_documents), schema `datasets/hcc/table-66afca58512c2fca.json`, source `[internal dataset path]`; no usable temporal column, so excluded from time-valid prediction.
- `pathology), schema `datasets/hcc/table-0a4ee86a446c605c.json`, source `[internal dataset path]`; no usable temporal column, so excluded from time-valid prediction.
- `vitals`, `transfers), and `front_page` are identifier-only under their catalog schemas; HCC contains no image or waveform files.

All joins use only the two stated keys after child aggregation. Source files are read-only; derived manifests and analyses are written in the workspace. MIMIC, eICU and UKB remain directly accessible configured datasets but are not joined into this HCC estimand.

## Availability limits, demonstration dispositions and compute

The natural-history/Delphi demonstration motivates dated-history representations, but its cohort/code/external validation is not reproduced. The Bayesian longitudinal demonstration motivates M3, but its genetic analysis is not imported because this HCC island has no genetic inputs. The cancer/Oncoformer main paper and full STAR Methods remain unavailable; only the accessible supplement limitations are respected, and HCC has no images. These are adaptations, not reproductions.

B0/Bobs/B2, weighting, bootstrap and audits are expected to fit within the future solver planning envelope (up to 16 CPUs, 262,144 MiB, 28,800 seconds); exact fit time is unverified. M3 begins with sparse CPU fitting and checkpoints. If a bounded probe shows repeated state-space optimization materially benefits from acceleration, request one allocated A100 and use `cuda:0`; ordinary-shell CUDA visibility is not evidence of absence. No GPU or proposer/solver weight training is required. Discovery has used no full solver fit.

Clinical adjudication or additional data are essential for claims about TACE indication, planned versus reactive intent, eligibility, radiologic response, viable tumor, treatment failure/benefit, mortality, outside care, appropriateness, clinical utility, or external validity. Computational results can establish only reproducible local recorded-care associations, selection/transport stability, and whether the prespecified falsifications hold.
