> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Strictly available assay content beyond capture intensity for the all-admission HCC recorded transition

## Scientific deliverable and substantive advance

This is a substantive child of [prior hypothesis]. It preserves the parent’s assay-content-versus-capture-intensity question and its exhaustive admission-anchored endpoint, while repairing a specific temporal-validity threat: a row attached to an anchor encounter, or a row timestamped before admission, does not prove that the row was available before the prediction time. The primary design therefore uses a conservative, auditable strict-prior history.

The falsifiable hypothesis is:

> Among all eligible adult first-observed HCC-coded inpatient admissions, assay-specific prior laboratory content (identity, qualitative/numeric result and dated within-assay trajectory) from completed encounters that ended before admission improves held-out calibrated prediction of the complete seven-state recorded procedure/discharge transition over the same strictly available capture/process history without assay payload.

This is an information hypothesis about locally recorded care. It does not claim active HCC, liver reserve, stage, burden, treatment indication, intent, receipt, completion, response, benefit or causality.

The actual solver deliverable is newly fitted/estimated, not a literature reproduction:

1. a frozen all-admission cohort, strict-history eligibility ledger, patient partition, duplicate/key/time audit and exhaustive terminal labels;
2. locked predictions for admission-only A, strict capture-only Q, strict assay-content E, the parent-comparable transparent history summary H, and a continuous-time learned model S;
3. the primary paired E-Q change in complete seven-state log loss and Brier score, with calibration and patient-clustered uncertainty;
4. S-E and mandatory assay-free process control S_Q-Q contrasts on exactly the same admissions, labels and split;
5. strict-availability, anchor-linked, timestamp-only and calendar-era sensitivities, plus locked predictions, permutation falsifications and a claim-to-evidence table.

No model has been fitted here and no empirical conclusion is claimed.

## What is supported and what remains unresolved

The inspected HCC snapshot and catalog support that encounters have native admission/discharge timestamps; labs, procedures, orders and medications have native time fields and payload fields; and the sources join through (patient master index, visit number). The inspected headers confirm:

- encounters: age, sex, encounter time, admission time, discharge time, clinical department;
- diagnoses: diagnosis name, diagnosis type;
- labs: test, qualitative result, quantitative result, specimen type, test time;
- procedures: surgery, start time, end time, surgery source;
- orders: non-drug orders, order entry time, start time, end time, order duration, order status, frequency;
- medications: Medication, Single-Dose Medication Amount, Single-Dose Medication Amount Unit, Frequency, Start Time, End Time, Route of Administration, Medication Type.

These are availability facts. They do not establish diagnosis timing, assay units, clinical availability logs, stage, burden, intent or outcome adjudication.

The strongest evidence-supported statement is that strictly dated source rows can be used to describe prior recorded laboratory/care history and later recorded transitions. The unresolved statement is whether prior assay payload adds information beyond a matched strict capture process. It is falsified for this snapshot and endpoint if E does not improve locked calibrated prediction over Q, if the increment disappears when assay payload is removed, or if it is reproduced by process-only controls.

## Cohort and temporal policy

Use HCC snapshot [source checksum] and catalog [source checksum]. Each listed source is an ordinary file; no archive member is used. Source files remain read-only. All four configured datasets remain directly accessible, but this HCC study uses only HCC sources.

Normalize Unicode/whitespace in keys and diagnosis text. Join diagnoses to encounters exactly on (patient master index, encounter number). Define record-coded HCC as normalized hepatocellular carcinoma or case-insensitive substring hepatocellular carcinoma in diagnosis name; print the regex, every matched string, diagnosis-type overlap, duplicate keys and unmatched keys. This is not an active-disease label.

Require age >=18, parseable native admission time and discharge time, nonnegative stay, and anchor encounter date in [2011-01-01, 2026-01-01). Retain the earliest eligible HCC-coded encounter per patient master index, ordered by native admission time then encounter number; do not replace an invalid earliest record with a later one. Let t0 = admission time. Keep every eligible anchor, including early discharge, early procedure and no-history cases. Exclude direct identifiers from features: name, national ID number, mobile phone number, health insurance/encounter card number, inpatient number.

Primary windows are half-open:

- strict prior history: [t0 - 730 days, t0);
- early endpoint: [t0, t0 + 24 hours);
- later endpoint: [t0 + 24 hours, t0 + 72 hours).

A prior source row is eligible in the primary analysis only if all of the following hold:

1. its normalized key matches an encounter for the same patient;
2. that linked encounter is not the anchor encounter;
3. the linked encounter has parseable native admission time and discharge time, with discharge time < t0 (and therefore its admission is also before t0);
4. the source-specific availability time is parseable, lies in [t0 - 730 days, t0), and is not a future or anchor-time row.

Use source-specific availability time: labs test time; procedures start time; orders order placement time (not future start time); medications start time. For prior encounter summaries, use the linked encounter’s admission time/discharge time. For orders and medications, use start/end only as secondary duration descriptors after their strict availability criterion; never let a later start/end move a row into the history. Missing or unparseable availability excludes the row from primary content/count features but is counted by source and linked encounter; it is never silently treated as absence. Rows linked to the anchor encounter are excluded from primary history even when their native event time is before t0. Record the number of excluded anchor-linked, open/overlapping, missing-discharge and missing-event-time rows.

This policy is conservative rather than proof of a true EHR availability timestamp: the files lack audit-log/order-entry and result-release times. The primary estimand is thus “strictly attributable to a completed prior encounter,” not “proven visible to a clinician.” Timestamp-only history (event time <t0 regardless of encounter discharge) and anchor-linked pre-t0 history are prespecified sensitivities, never silently pooled with the primary.

## Exact all-admission endpoint

For every anchor admission, use only procedures.surgery and native procedures.start time for procedure timing, plus native encounters.discharge time; do not use orders as an endpoint or intent proxy. Apply one frozen precedence rule: sort valid procedure starts and discharge by elapsed time, with discharge winning exact ties. Keep invalid/missing procedure timing unresolved when it could change state, never as no procedure.

Define:

- P0: a valid procedure start in [0,24 hours) and before discharge;
- D0: discharge at or before 24 hours before any qualifying early procedure;
- U0: missing/invalid procedure time that could change early ordering/window assignment;
- R24: none of P0/D0/U0 established;
- among R24, P1: first valid procedure start in [24,72 hours) and before discharge;
- D1: discharge in [24,72 hours) before any qualifying later procedure;
- U1: unresolved procedure timing that could change the later state;
- N72: no P1/D1/U1 by 72 hours.

The primary estimand is the mean terminal probability vector over all admissions for P0,D0,U0,P1,D1,U1,N72. Fit early and later distributions for every admission, then marginalize to this complete vector. Report the R24-conditional distribution only secondarily. Audit procedures before admission, after discharge, exact boundaries, midnight starts, multiple rows, missing times and alternate procedure/discharge tie precedence. The endpoint is a locally recorded procedure/discharge transition, not a validated treatment or clinical decision.

Create a secondary deterministic lexical audit over procedures.surgery (never replacing the primary endpoint): TACE/embolization (TACE, embolization, chemoembolization), resection/transplant (resection, transplantation), ablation (ablation, radiofrequency, microwave, absolute alcohol), systemic/infusion (chemotherapy, targeted therapy, immunotherapy, infusion), diagnostic/access (angiography, puncture, biopsy, drainage, catheter placement), otherwise other. Preserve multi-match, blank and ambiguous strings and report nested P0/P1/source summaries. This requires clinical review before any treatment or decision interpretation.

## Strict nested information sets

All primary models use the same admissions, exhaustive labels, strict-history ledger, patient split, fit-only preprocessing and target.

- A: age, sex, department, calendar era, admission time-of-day and admission missingness.
- Q: A plus strict prior capture/process only: prior completed-encounter count and duration, active days, time since last completed encounter, source-specific row counts and distinct linked-encounter counts for labs/procedures/orders/medications, observed source-type count, strict excluded/missing-time counts, left-truncation, no-history and source-availability indicators. Q contains no assay identity/value/result and no procedure/order/medication names, doses, routes, frequency or status.
- E: Q plus strict prior lab content from labs: assay identity Test, assay-specific Qualitative Result, assay-specific valid Quantitative Result, Specimen Type, recency, span, count, missingness and within-assay change/slope only when at least two distinct valid Test Time values exist. No cross-assay pooling or physiologic score is allowed because the catalog has no lab unit column.
- H: the parent-comparable transparent strict-history summary, rerun with Q-like process features, assay-specific lab summaries, and prior procedure/order/medication type occurrence/recency/gap summaries. Names are descriptive tokens only; no treatment meaning is assigned.
- S: a two-coordinate continuous-time latent event model using exactly the strict prior rows used by E/H: source/type, relative availability time, payload mask, assay identity and only assay-specific lab payload. Process events are type/time tokens, not treatment concepts. Between events, latent coordinates decay with elapsed time; assay-specific emissions and noise model lab payload; a supervised head predicts the same early/later competing-state target. Fit terminal-state negative log likelihood on fit patients. Fix latent dimension, decay family, regularization, masking term and seed count before locked evaluation; tune only in selection data. Call coordinates latent coordinates, never reserve or disease states.
- S_Q: the identical S architecture and rows with all assay identity, qualitative and numeric payload removed, retaining process/source/time/masks. It tests whether S’s apparent gain is only capture intensity.

The primary simple baseline comparison is E versus Q using the same regularized sequential multinomial-logistic heads for the early and R24-conditional later distributions, then marginalization to seven states. A is the admission floor and H is a transparent all-history sensitivity. The learned alternative is S versus E, with S_Q versus Q as the process control. Both alternatives consume the identical strict event ledger and target; the alternative can reveal irregular timing, nonlinear assay interactions, gaps and representation uncertainty that first/last/count summaries discard. It is retained only for a stable calibrated increment, not a small predictive gain.

The parent’s current-lab [0,12-hour) comparison is not part of the primary all-admission score: a P0 procedure can occur before 12 hours, making later current labs post-outcome. A secondary landmark analysis may use labs with test time in [t0,t0+12h) only among admissions with no P0/D0/U0 by t0+12h, and must define a new post-landmark label from the unchanged endpoint ledger. It cannot be reported as evidence for the primary E-Q estimand.

## Split, analysis and falsification

Use the frozen patient-level split SHA-256(normalized patient master index) modulo 100: 0–59 fit, 60–69 preprocessing/hyperparameter/fit-only calibration selection, 70–79 locked evaluation, 80–99 inaccessible. All rows for a patient follow the same bucket. Freeze cohort, strict-availability ledger, endpoint rules, feature manifest, model dimensions and calibration before reading locked labels.

Primary outcomes are paired patient-clustered changes in held-out complete-vector multiclass log loss and Brier score, defined as score(E)-score(Q), lower better. Also report Q-A, H-A, S-E and S_Q-Q, calibration intercept/slope, reliability, observed/predicted probability and each-state probability contrasts. Use >=1,000 patient-clustered paired bootstrap resamples of locked predictions, preserving all admissions per sampled patient. Report no-history, strict-prior-count and fit-derived Q-intensity strata, 30/180/730-day windows, and a later-era descriptive holdout if each era has support; these are heterogeneity/transport diagnostics, not external validation.

Freeze and execute:

1. shuffle complete strict histories across patients within each partition, preserving Q features; any E-Q gain should disappear;
2. permute assay payload within assay and partition, preserving identity, times and counts; content increment should attenuate;
3. permute assay identity while preserving values/times; assay-specific signal should attenuate;
4. shuffle event times within patient/source while preserving payload/counts; time-order increment should attenuate;
5. reverse event order for S; Q/H should be unchanged except recency summaries;
6. compare strict primary history with timestamp-only and anchor-linked sensitivities; a large reversal makes the availability claim inconclusive;
7. fit S_Q and Q and test whether process-only controls reproduce E-Q or S-E;
8. test sentinels for any row at/after t0, anchor-linked row, post-discharge row, current [0,12) lab in primary features, duplicate-patient split leakage or outcome-derived feature;
9. repeat endpoint tie, missing-time and midnight rules; material endpoint reversals are inconclusive;
10. permute labels within calendar era and department; persistent performance suggests leakage or label artifact.

Supportive evidence requires a negative (better) 95% patient-clustered interval for E-Q log loss and/or Brier without material calibration deterioration, attenuation under payload/history permutations, no primary future-window sentinel, and no complete reproduction by Q/S_Q. It supports incremental information in strictly attributable prior recorded assay content for this local recorded-transition distribution.

Adverse evidence is no E-Q improvement, worse calibration, process-only reproduction, persistence after payload permutation, a strict-to-timestamp reversal that invalidates availability interpretation, or any leakage/split failure. Inconclusive evidence includes dominant U states, sparse assays, wide intervals, substantial strict-history exclusion/left truncation, unstable era/timing behavior, missing/uninterpretable procedure times, or insufficient family support. Supportive/adverse/inconclusive results do not establish clinical utility.

## Exact bindings and archive status

All sources are read-only ordinary files; every join requires duplicate-key, multiplicity, unmatched-key and row-inflation audits.

| table / schema | exact source path | required columns and use | archive member |
|---|---|---|---|
| encounters / datasets/hcc/table-b743286cb1249287.json | [internal dataset path] | patient master index, encounter number, age, sex, encounter time, admission time, discharge time, encounter department; anchor, completed-prior gate, split and endpoint | ordinary file |
| diagnoses /datasets/hcc/table-12710723c3df0c99.json | [internal dataset path] | patient master index, encounter number, diagnosis name, diagnosis type; record-coded cohort, no diagnosis time | ordinary file |
| labs / datasets/hcc/table-38aad8c54471332f.json | [internal dataset path] | keys; Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time; E/S payload and strict availability | ordinary file |
| procedures / datasets/hcc/table-d5eae16f8f8093d9.json | [internal dataset path] | keys; Surgery, Start time, End time, Surgery source; endpoint, Q/H process and lexical audit | ordinary file |
| orders / datasets/hcc/table-6b93dcf0ea823702.json | [internal dataset path](non-drug)_2062526727266216118.csv | keys; non-drug order, order time, start time, end time, order duration, order status, frequency; strict Q/H process, availability=order time | ordinary file |
| medications / datasets/hcc/table-4f6ecaeb6e8f69c2.json | [internal dataset path] | keys; medication, single-dose medication amount, single-dose medication amount unit, frequency, start time, end time, route of administration, drug type; strict Q/H process, availability=start time | ordinary file |
| examinations / datasets/hcc/table-fd016d2731b9d6c6.json | [internal dataset path] | keys; Examination, Examination Findings, Examination Diagnosis, Start Time, Examination Number; availability audit only, no primary history | ordinary file |
| clinical_documents / datasets/hcc/table-66afca58512c2fca.json | [internal dataset path] | keys plus narrative fields; no native time and unvalidated extraction, excluded from primary | ordinary file |
| pathology / datasets/hcc/table-0a4ee86a446c605c.json | [internal dataset path] | keys plus Pathology, Examination Findings, Examination Diagnosis, Machine Model Number; no native time, excluded from primary | ordinary file |
| vitals / datasets/hcc/table-8436de9cba74b8ca.json | [internal dataset path] | keys only; identifier-only, availability audit | ordinary file |
| transfers / datasets/hcc/table-320c20f732e71789.json | [internal dataset path] | keys only; identifier-only, availability audit | ordinary file |
| front_page / datasets/hcc/table-38b3224239acc33f.json | [internal dataset path] | keys only; nominal identifier-only, excluded | ordinary file |

The catalog and all twelve HCC schema JSON files were inspected, as were headers and sample rows of the six sources used for cohort/features/endpoint. The other configured MIMIC, eICU and UKB datasets remain available but are not an HCC external validation cohort.

## Method alternatives, compute and evidence limits

The transparent nested summaries are the adequacy floor. The learned alternative is the matched continuous-time S/S_Q adaptation motivated by the inspected methods guide’s dated-history and longitudinal latent-structure examples; it is not a reproduction. The cancer demonstration’s main article and complete STAR Methods are unavailable locally, its supplement does not establish an HCC method, and HCC has no images, so no multimodal reproduction is claimed. A mechanistic ALBI/MELD-like branch is deferred because lab units, validated reference ranges, stage and clinically adjudicated outcomes are absent. Raw document/pathology/examination modeling is deferred because these sources lack native time or validated semantic/temporal extraction. Revisit only if timestamp/audit logs, unit/reference metadata or expert adjudication become available.

Measured discovery work in this episode: source catalog/schema inspection, direct header/sample inspection, and the parent’s prior verified procedure scan were available; no cohort fit, endpoint prevalence, locked prediction or GPU probe was run. The full future solver envelope is inherited as an unverified planning estimate: at most 16 CPUs, 262,144 MiB RAM, 8 allocated GPUs and 28,800 seconds. Chunked scans/strict-ledger construction and transparent fits are expected (unverified) to require 1–4 hours and 64–192 GiB; the continuous-time model 2–8 CPU hours; >=1,000 clustered bootstrap calculations 1–4 hours. Start CPU-first because the primary matrices are compact after aggregation. If a bounded allocated probe shows S benefits materially from GPU, request one A100 using ehr-campaign-gpu:20260908, explicitly place model and tensors on cuda:0, and report the probe separately. Ordinary-shell CUDA absence is not evidence of unavailable hardware.

Computationally checkable claims are schema/path/key/time audits, strict eligibility, leakage tests, cohort/endpoint counts, feature nesting, split, predictions, proper scores, calibration, bootstrap intervals and permutation behavior. Clinical adjudication, audit-log linkage, laboratory units, stage/burden data, treatment intent/receipt/completion, outcomes beyond this recorded transition, external validation and another study are required for biologic mechanism, treatment decisions, benefit, safety, clinical utility or transportability.
