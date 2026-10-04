> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Assay content beyond documentation intensity for the next 72-hour recorded transition after an HCC-coded admission

## Decision and scientific deliverable

This is a substantive child of `[prior hypothesis]`. It preserves the incumbent’s exact HCC files, all-admission estimand, temporal exclusions, transparent baseline and learned state-space alternative, while repairing the main validity problem: a pre-admission history gain can be a proxy for how intensely the hospital observed and documented a patient.

The falsifiable hypothesis is:

> Among all eligible adult first-observed HCC-coded inpatient admissions, prior assay content—assay-specific values/results and their dated trajectory—improves calibrated prediction of the complete recorded procedure/discharge transition beyond admission context, first-12-hour current labs, and a prespecified measure of prior source-capture intensity.

This is an information hypothesis about the local recorded-care distribution. It is not a claim about active HCC, liver reserve, treatment indication, treatment benefit or causality.

The future solver must newly produce:

1. a frozen cohort, patient partition, time/key audit and the unchanged exhaustive terminal labels;
2. locked predictions for A, L, Q, E, H and S:
   - A: admission context;
   - L: A plus current [0,12) assay history;
   - Q: L plus prior source-capture/process intensity with no clinical payload;
   - E: Q plus prior assay content and dated assay trajectory;
   - H: the incumbent’s transparent all-history summary;
   - S: an irregular learned state-space model of the same prior history;
3. the prespecified primary E-versus-Q proper-score/calibration contrast, plus Q-versus-L and incumbent H-versus-L;
4. process-only S_Q, assay/value/time permutations, capture-intensity strata, exact boundary tests and endpoint-family audit;
5. clustered uncertainty, calibration, missing-history diagnostics, locked predictions and a claim-to-evidence table.

Completion is the audit, labels, locked estimates, uncertainty, robustness and interpretation—not confirmation of the hypothesis. No solver result is available yet and no empirical model conclusion is claimed here.

## Evidence-supported and unresolved claims

The verified HCC snapshot supports only that encounters have native admission/discharge times; labs, procedures, orders and medications have native timestamps and payload fields; and rows can be joined by the pair (`patient master index`, `encounter number`). Diagnoses can define a record-coded cohort but have no diagnosis time. A direct read-only scan of the procedure source verified 338,040 rows, 7,781 distinct procedure strings, 179 blank procedure names and two source values; representative rows include TACE and the sources `medical records surgery` and `anesthesia information system`. These are source-availability facts, not cohort prevalence or prediction results.

The parent’s provisional counts—42,692 provisional first-patient admissions, 146,703 linked procedure rows, 86,025 midnight starts, 9,077 missing/unparseable starts, 25,527 valid starts in [0,24) and 51,332 in [24,72)—remain provisional and must be recomputed. They are not evidence of the hypothesis.

The strongest supported clinical statement is that the files can describe locally recorded prior assays/care and later recorded procedures or discharge. They cannot establish active disease, diagnosis timing, stage, tumor burden, resectability, indication, scheduling, consent, intent, receipt, completion, response, toxicity, mortality, outside-care completeness or treatment benefit.

The unresolved statement is the assay-content increment above Q. It is falsified for this snapshot/endpoint if E does not improve held-out calibrated prediction over Q, if Q reproduces the apparent H-versus-L gain, or if assay-content gains persist after permutations that destroy assay values or within-patient timing.

## Population, anchor and temporal boundaries

Use HCC snapshot `[source checksum]`, catalog [source checksum]. All source files are ordinary read-only files; no archive member is used.

Normalize Unicode and whitespace in keys and diagnosis text. Join `diagnoses` to `encounters` on exactly (`Patient master index`, `Encounter number`). Define HCC-coded as normalized `Hepatocellular carcinoma` or a case-insensitive substring `hepatocellular carcinoma` in `Diagnosis name`; print the regex, every matched string, diagnosis-type overlap, duplicate keys and unmatched keys before fitting. This is not an active-HCC label.

Require age >=18, parseable native `Admission Time` and `Discharge Time`, nonnegative stay, and encounter date in [2011-01-01, 2026-01-01). Retain the earliest eligible HCC-coded encounter per `Patient Master Index`, ordered by native `Admission Time` then `Encounter Number`; do not substitute a later record for an invalid earliest record. Let `t_0 = Admission Time`. Keep every eligible anchor admission, including early discharge, early procedure and unresolved-time cases. Exclude direct identifiers (`Name`, `National ID Number`, `Mobile Phone Number`, `Medical Insurance/Encounter Card Number`, `Inpatient Number`) from features.

Use half-open elapsed-time intervals:

- prior history: [(t_0 - 730 days), t_0);
- current labs: [t_0, t_0 + 12 hours);
- early outcome: [t_0, t_0 + 24 hours);
- later outcome: [t_0 + 24 hours, t_0 + 72 hours).

A history row is eligible only when its native event time is strictly less than t_0, even if linked to the anchor encounter. Prefer prior rows linked to an encounter whose native `admission time < t_0`; audit, rather than silently use, any anchor-linked row with a pre-anchor timestamp. Count left truncation when an encounter begins before t_0 - 730 days. Unparseable timestamps are counted by source/window and excluded from primary features, never treated as absence. Print row counts, duplicate/multiplicity and unmatched-key audits, invalid-time counts, boundary/tie counts, prior/current counts and patients with no prior record.

## Unchanged all-admission endpoint

The primary endpoint is copied from the incumbent and uses only procedure presence and native `procedures.Start Time` for label timing. Discharge wins exact ties.

For every anchor admission:

- `P0`: valid procedure start in [0,24) and before discharge;
- `D0`: discharge at or before 24 hours before any valid early procedure;
- `U0`: missing/invalid procedure time whose possible position could change procedure/discharge or boundary ordering;
- `R24`: no established P0, D0 or U0.

Among R24:

- `P1`: first valid procedure start in [24,72) and before discharge;
- `D1`: discharge in [24,72) before any valid later procedure;
- `U1`: unresolved procedure timing that could change later ordering;
- `N72`: no established P1, D1 or U1 by 72 hours.

The primary all-admission estimand is the mean terminal probability vector over `P0,D0,U0,P1,D1,U1,N72`. Fit early and later distributions for every admission, then marginalize to this complete seven-state vector. Report the R24-conditional distribution only secondarily. Procedure-wins ties, midnight-start handling, unresolved-time optimistic/conservative rules, before-admission procedures, after-discharge rows, multiple rows and exact boundaries are audited sensitivities. Missing timing never becomes no procedure.

The endpoint means a locally recorded procedural transition. It does not mean a liver-directed treatment, clinically intended decision, appropriate care, receipt/completion, benefit or causal effect.

### Procedure-family interpretability audit

To make the recorded endpoint more clinically legible without replacing it, label each eligible timed procedure row using a frozen, deterministic multi-label map over `surgery`: 

- arterial embolization/TACE: `TACE`, `embolization`, `chemoembolization`;
- resection/transplant: `resection`, `transplant`;
- ablation: `ablation`, `radiofrequency`, `microwave`, `absolute ethanol`;
- systemic/infusion-coded: `chemotherapy`, `targeted therapy`, `immunotherapy`, `perfusion`;
- diagnostic/access-coded: `angiography`, `puncture`, `biopsy`, `drainage`, `catheter placement`;
- otherwise `other`; preserve multiple matches and unmatched/ambiguous strings.

Report family flags nested within P0/P1 and by `procedure source`, including `medical-record surgery` and `anesthesia system` where present. This is a lexical description of recorded names, not a validated procedure adjudication. Family outputs are secondary; D/N/U admissions remain in the primary seven-state estimand.

## Information sets and observation-intensity repair

All models use the same admissions, labels, patient split, fit-only preprocessing and target. Fit A/L/Q/E/H with the same regularized sequential multinomial-logistic heads for the early distribution and the R24-conditional later distribution, then marginalize to the complete seven-state vector; an additive generalized-linear sensitivity may be reported but cannot replace this transparent baseline.

A includes age, sex, admitting department `visiting department`, calendar era, admission time-of-day and missingness indicators.

L adds current-admission labs in [0,12) using `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time`. For each assay, use first/last valid numeric value, change, elapsed time, count, density/missingness, and slope only with at least two distinct native timestamps; qualitative values remain assay-specific categorical indicators. No [12,24) lab is permitted.

Q is the documentation/capture comparator. It adds only pre-admission [(t_0-730 days),t_0) event-source/time features: number and duration of prior encounters, days active, days since last event/encounter, row counts and distinct linked encounters separately for labs, procedures, orders and medications, observed source-type count, missing-time counts, left truncation and no-history indicators. It does not use any assay identity/value/result, procedure/order/medication name, dose, route, frequency, status or text. These variables are not a causal adjustment and cannot prove complete capture.

E adds to Q the prior laboratory content and trajectory from `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time`: assay-specific identity, numeric/qualitative observations, first/last value, within-assay change/slope where supported, recency, span, count and missingness. Units are absent, so do not pool numeric values across assays or create physiologic scores.

H is the incumbent transparent history summary rerun exactly: Q-like encounter/source features, assay-specific prior laboratory summaries, prior procedure occurrence counts/recency/gaps, and order/medication process counts/recency/gaps. Procedure/order/medication names are not interpreted as treatment or intent. The prespecified source-ablation table removes orders/medications and then procedures from H.

The primary contrast is E versus Q: whether dated assay content adds information after recorded intensity. Secondary contrasts are Q versus L, E versus L and H versus L. A null Q-versus-L but positive E-versus-Q result is still interpretable only as recorded assay-content information, not physiology.

Use a feature manifest containing each Chinese column, table, source path, native timestamp, window, transformation, missingness rule and whether it belongs to Q or E/H. Fit clipping, standardization, assay vocabulary, imputation and regularization only on buckets 0–59; select on 60–69.

## Learned/mechanistic alternative

S uses exactly the same prior-window rows available to H/E, excluding diagnosis text, clinical-document text, pathology text, examination findings, direct identifiers and current/post-anchor rows. Each event has source/type, native time relative to t_0, payload mask and, only for labs, assay-specific numeric or qualitative content. Generic order/medication/procedure records are process/type tokens; names are not interpreted as treatment.

Fit a two-coordinate continuous-time latent state model. Between events, z evolves with elapsed-time decay; assay observations have assay-specific emission/update, noise and mask parameters; process events feed an observation/capture component and a supervised competing-state head for the unchanged early/later endpoint. Fit supervised terminal-state negative log likelihood on 0–59. Any masked-event reconstruction term, dimensions, decay form and shrinkage are fixed before locked evaluation and tuned only on 60–69. Numeric values are standardized within assay using fit-only parameters. Call coordinates latent coordinates, never liver reserve, renal reserve or validated disease states.

Fit `S_Q` with assay values/results removed but source/type/time and capture features retained. S can reveal irregular gaps, order, nonlinear assay interactions and posterior uncertainty that transparent summaries lose. S is not selected for complexity or a small score gain: it is supportive only if calibrated held-out performance adds over E/H, remains stable across seeds and timing windows, and its assay-containing gain is not reproduced by S_Q.

## Split, analysis and uncertainty

Assign every patient by SHA-256 of normalized `Patient Master Index` modulo 100:

- 0–59: fit;
- 60–69: preprocessing, hyperparameter, regularization and fit-only calibration selection;
- 70–79: locked evaluation;
- 80–99: inaccessible, not an external validation set.

All rows and encounters for a patient follow that partition. Freeze the cohort, feature manifest, windows, endpoint rules, family map, model dimensions, hyperparameters and calibration before locked evaluation labels are used.

The prespecified primary outcome on all eligible admissions is the paired E-minus-Q change in held-out multiclass log loss and multiclass Brier score for the complete seven-state vector. Also report Q minus L, E minus L, H minus L, S minus E and S_Q minus Q. Report calibration intercept/slope, reliability, observed-versus-predicted probability and probability contrasts for every state; marginal P1 is secondary.

Use at least 1,000 patient-clustered paired bootstrap resamples of locked predictions, preserving all admissions from each patient, for 95% intervals. Report overall results and availability/intensity strata (no prior record, 1–2 prior encounters, >=3; and fit-only-defined Q capture-intensity bins). These are heterogeneity diagnostics, not causal subgroups or external validation. Calibration is fit-only; never calibrate on buckets 70–79.

## Falsification and robustness

Freeze these before locked evaluation:

1. Shuffle complete pre-admission histories across patients within each fit/selection/test partition, preserving history length and Q features. E/Q and H/L gains should disappear; persistence suggests leakage or split/label error.
2. Permute prior assay values/results within assay and partition while preserving assay identity, timestamps and counts. The E-minus-Q content increment should attenuate.
3. Shuffle pre-admission event times within patient and source/assay while preserving values, counts and source. Time/order gains should attenuate; Q’s pure count component may remain.
4. Reverse pre-admission chronological order for S. An order-sensitive increment should attenuate; Q and order-insensitive H summaries should be unchanged except recency features.
5. Fit Q alone and report whether it reproduces H/L or E/L. If it does, classify the apparent gain as documentation/capture intensity rather than assay content.
6. Stratify or coarsened-match on fit-derived Q intensity and repeat E-versus-Q. A result only in one capture stratum is not a general history claim.
7. Source-ablate orders/medications and procedures, and report `Procedure Source` strata. This tests whether one documentation subsystem drives the result.
8. Enforce no native row at or after t_0 in history, no current [12,24) assay, no post-discharge row and no outcome-derived feature. A forbidden-window sentinel using current [12,24) labs to predict an already-started [0,24) endpoint must not improve; any gain invalidates the affected result.
9. Repeat 30-, 180- and 730-day histories and report left truncation. A result dependent on observation-start artifacts is unstable.
10. Repeat exact-boundary, discharge/procedure tie, midnight-start and unresolved-time rules. Material reversals make the transition analysis inconclusive.
11. Permute labels within calendar era and department. Persistent performance indicates leakage, duplicate-patient partitioning or a label artifact.
12. Report procedure-family and source-specific descriptive outputs without making them primary labels or clinical adjudications.

## Interpretation gates

Define each proper-score contrast as score(E) minus score(Q), so lower is better. Supportive evidence requires the 95% paired patient-cluster interval for log loss and/or Brier to lie below zero, without material calibration deterioration; the improvement should be reasonably stable across Q availability/intensity strata and timing windows; assay-value/time permutations should attenuate the increment; and Q alone should not reproduce it. This supports incremental information in prior recorded assay content for the local recorded-transition distribution.

A positive H/L or Q/L result with no E/Q result supports only documentation/capture association. A positive E/Q result does not establish physiology, active disease, treatment need or clinical utility. S is supportive only if it adds over E/H, remains calibrated and stable, and S_Q does not explain it.

Adverse evidence is no E/Q improvement, worse calibration, complete reproduction by Q, persistence after assay/history permutation, reversed-order failure inconsistent with the claimed mechanism, or any forbidden-window/split artifact. This rejects the incremental assay-content explanation while leaving a descriptive association between local records and local recorded transitions.

Inconclusive evidence includes dominant U0/U1 states, too few procedure-family observations, wide cluster intervals, severe timestamp dependence, substantial left truncation, unstable calibration, sparse assay coverage, failure to distinguish assay content from Q, or ambiguous/missing procedure names. Inconclusive is not confirmation.

## Exact HCC bindings, source paths and availability

All usable rows join to the selected encounter by normalized (`patient master index`, `encounter number`) with duplicate, multiplicity and unmatched audits. Each source is an ordinary file; archive member is `ordinary file`.

| Table / schema | Exact read-only source | Required columns and role |
|---|---|---|
| encounters / `datasets/hcc/table-b743286cb1249287.json` | `[internal dataset path]` | keys; `age`, `sex`, `visit time`, `admission time`, `discharge time`, `visit department`; anchor/context/prior times |
| diagnoses / `datasets/hcc/table-12710723c3df0c99.json` | `[internal dataset path]` | keys; `Diagnosis Name`, `Diagnosis Type`; HCC-coded cohort only, no native time |
| labs / `datasets/hcc/table-38aad8c54471332f.json` | `[internal dataset path]` | keys; `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time`; current/prior assay content |
| procedures / `datasets/hcc/table-d5eae16f8f8093d9.json` | `[internal dataset path]` | keys; `Surgery`, `Start time`, `End time`, `Surgery source`; primary endpoint, prior process and secondary family map |
| orders / `datasets/hcc/table-6b93dcf0ea823702.json` | `[internal dataset path]` | keys; `Orders (non-drug)`, `Order time`, `Start time`, `End time`, `Order duration`, `Order status`, `Frequency`; Q/H process timing/counts only |
| medications / `datasets/hcc/table-4f6ecaeb6e8f69c2.json` | `[internal dataset path]` | keys; `Medication`, dose/unit, `Frequency`, `Start time`, `End time`, `Medication administration method`, `Medication type`; Q/H process timing/counts only |
| examinations / `datasets/hcc/table-fd016d2731b9d6c6.json` | `[internal dataset path]` | keys; `Examination`, `Examination Findings`, `Examination Diagnosis`, `Start Time`, `Examination Number`; auditable availability only, not primary history |
| clinical_documents / `datasets/hcc/table-66afca58512c2fca.json` | `[internal dataset path]` | keys; narrative columns including `Chief Complaint`, `History of Present Illness`, `Past Medical History`, `Admission Diagnosis`, `Clinical Course`, `Discharge Diagnosis`, `Operative Course`; no native time, excluded from primary history |
| pathology / `datasets/hcc/table-0a4ee86a446c605c.json` | `[internal dataset path]` | keys; `Pathology`, `Examination Findings`, `Examination Diagnosis`, `Machine Model`; no native time, excluded from primary history |
| vitals / `datasets/hcc/table-8436de9cba74b8ca.json` | `[internal dataset path]` | keys only; identifier-only, no payload/time |
| transfers / `datasets/hcc/table-320c20f732e71789.json` | `[internal dataset path]` | keys only; identifier-only, no payload/time |
| front_page / `datasets/hcc/table-38b3224239acc33f.json` | `[internal dataset path]` | keys only; nominal/identifier-only, no primary history |

The twelve schema files, `datasets/hcc/metadata.json` and `datasets/hcc/README.md` were inspected. Metadata confirms many-to-one relationships only after duplicate verification, absent laboratory units, and unvalidated narrative extraction. The workspace retains direct read-only access to all four configured dataset directories (HCC, MIMIC, eICU and UKB); this HCC proposal uses only HCC. No expert seed is a parent or evidence source because the imported seeds are UKB/MIMIC/eICU and dataset-mismatched.

## Method provenance and alternatives

The local research-ambition README and methods/compute guide were inspected. The dated-history demonstration motivates only the comparison between summaries and irregular event ordering; this study does not reproduce its UK Biobank cohort or transformer. The Bayesian demonstration motivates only a changed EHR-only latent-state adaptation; genetics and its original cohort are absent. For the cancer demonstration, the main article and complete STAR Methods remain unavailable, only supplement/metadata are locally available, and this HCC source has no images; no inaccessible text or multimodal reproduction is claimed. A large transformer remains deferred unless S establishes a stable unresolved long-order signal beyond Q/E/H. Raw document/pathology/examination text is deferred because temporal attribution and extraction validity are inadequate for this pre-admission question.

## Compute plan and future evidence limits

No solver fit was run. Discovery’s 7,200-second science budget is separate from the future solver planning envelope of at most 16 CPUs, 262,144 MiB memory, 8 GPUs and 28,800 seconds. Source sizes are approximately 2.2 GB labs, 2.19 GB orders, 491 MB medications, 1.14 GB examinations, 89 MB diagnoses, 35 MB procedures and 18.6 MB encounters. Use chunked CSV scans and compact patient-level matrices; do not load the large sources naively.

A/L/Q/E/H aggregation and transparent fits are CPU-first: expected, unverified 8–16 CPUs, 64–192 GiB and 1–4 hours for aggregation/fits, with another 1–4 hours for 1,000 locked-prediction bootstrap resamples. S is first attempted on CPU within the same envelope. If a bounded feasibility measurement shows material need, request one allocated A100 using `ehr-campaign-gpu:20260908`, explicitly place model/tensors on `cuda:0`, and report the measurement separately from study results. No GPU is mandatory; ordinary shell CUDA absence is not evidence of hardware absence.

Computationally checkable claims include source/header/schema availability, key/time audits, cohort counts, endpoint states, family-string coverage, feature manifests, locked predictions, proper scores, calibration, bootstrap intervals, ablations and permutation behavior. Clinical adjudication, additional linkage or another study is required for active HCC, diagnosis timing, stage, burden, resectability, indication, scheduling, consent, intent, receipt, completion, appropriateness, response, toxicity, mortality, outside-care completeness, causal effects, bedside utility and transportability. Missing lab units prevent cross-assay physiologic scores. The family map cannot establish that a procedure was clinically indicated, completed or beneficial.

The substantive advance over the incumbent is thus narrow and testable: it retains the exhaustive recorded-transition question while asking whether prior assay content contributes beyond an explicit local observation-intensity signature, and it reports a clinically recognizable but explicitly non-adjudicated procedure-family characterization so that any predictive result is not mislabeled as treatment evidence.
