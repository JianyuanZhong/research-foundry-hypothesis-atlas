> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Strictly prior-encounter assay content for the complete recorded transition after an HCC-coded admission

## Successor decision and scientific deliverable

This is a substantive child of `[prior hypothesis]`. It preserves the incumbent's primary scientific question—whether assay content adds information beyond capture intensity, measured by the held-out E-minus-Q contrast—and preserves its exhaustive all-admission seven-state recorded-transition estimand. The repair is a provenance restriction that changes the primary exposure definition, not a cosmetic sensitivity analysis:

> Among all eligible adult first-observed HCC-coded inpatient admissions, does strictly pre-admission assay content (assay identity, value/result and dated trajectory from rows linked to an encounter whose native admission predates the index admission) improve calibrated prediction of the complete recorded procedure/discharge transition beyond admission context, first-12-hour current labs and strictly prior capture intensity?

The incumbent admits a row linked to the anchor encounter when its event timestamp is earlier than admission, while a timestamp alone cannot establish that the result was available before the index admission; it may represent retrospective entry, registration or peri-admission workflow. The successor therefore excludes every anchor-linked row from primary pre-admission history, even if its native event time is earlier than t0. It retains those rows only in an explicitly labelled sensitivity analysis. This is a clinically consequential validity repair because a purported prior-assay signal should not use information whose availability before the admission is uncertain.

The primary target remains local recorded care, not active HCC, liver reserve, treatment intent or benefit. The incumbent's secondary order-before-procedure layer is retained, but remains gated and noncausal. It asks whether the E-minus-Q signal transfers to a temporally resolvable two-source record of a documented care sequence; it cannot establish a clinician decision.

Completion requires a frozen cohort and row-level provenance audit; unchanged primary labels; matched A/L/Q/E/H predictions; matched continuous-time S/S_Q predictions; locked E-minus-Q log-loss and Brier contrasts; calibration and clustered uncertainty; strict-history and anchor-linked sensitivity; concordance gate/results; falsification outputs; and a claim-to-evidence table. A positive result is not required.

## Evidence-supported versus untested

The verified HCC snapshot and catalog support native encounter admission/discharge times, native lab/procedure/order/medication time and payload fields, and many-to-one source-to-encounter joins on (Patient Master Index, Encounter Number), subject to duplicate and multiplicity audits. Direct header inspection confirms the exact columns below. The strongest supported statement is only that this local snapshot can describe recorded assays, local capture processes, and recorded procedure/discharge transitions.

Diagnoses have no diagnosis-time field. No available field establishes active HCC, stage, tumor burden, resectability, indication, scheduling, consent, intent, receipt, completion, response, toxicity, mortality, outside-care completeness or treatment benefit. The unresolved claim is the strict prior E-minus-Q predictive increment and, conditionally, its relation to an order-before-procedure recorded sequence. No model result is claimed.

## Population and temporal boundaries

Use HCC snapshot [source checksum] and catalog [source checksum]. All 12 HCC sources are ordinary read-only CSV files; no archive member is used.

Normalize Unicode/whitespace in keys and diagnosis text. Join diagnoses to encounters exactly on (Patient master index, Visit number). Define an HCC-coded encounter as normalized diagnosis name equal to hepatocellular carcinoma or containing the case-insensitive phrase hepatocellular carcinoma. Print every matched diagnosis string and Diagnosis type, duplicate keys, unmatched diagnosis keys and multiplicity. This is an operational record-code definition, not disease adjudication.

Require age >=18, parseable native Admission Time and Discharge Time, nonnegative stay, and Encounter Time in [2011-01-01, 2026-01-01). Retain the earliest eligible HCC-coded encounter per patient, ordered by native Admission Time then Encounter Number; do not substitute a later encounter when the earliest candidate has invalid time. Set t0 to Admission Time. Keep early discharges, early procedures and unresolved-time admissions.

Use half-open windows:

- strict prior history: [t0 - 730 days, t0);
- current-admission context: [t0, t0 + 12 hours);
- early primary transition: [t0, t0 + 24 hours);
- later primary transition: [t0 + 24 hours, t0 + 72 hours).

### Strict availability rule

A lab, procedure, order or medication row enters primary prior history only when it joins an encounters row on the two keys, that linked encounter has parseable Admission time strictly earlier than t0, its native event time is valid and lies in [t0 - 730 days, t0), and it is not linked to the index encounter. Source event times are: labs Test time; procedures Start time; orders Order time; medications Start time. Orders with invalid Order time may use Start time only in a separately reported low-confidence tier, never silently in the primary tier.

For encounter capture counts, require linked encounter admission strictly before t0 and use that admission time. Invalid time is unresolved, not absence. Audit anchor-linked pre-t0 rows, invalid timestamps, event/encounter disagreements, left truncation, exact boundaries, duplicates, unmatched keys and rows after discharge.

The current-admission L component may use index-encounter labs in [t0,t0+12h), because it is identical in Q and E. It is not called pre-admission assay content. A delayed-outcome timing analysis is secondary and cannot replace the primary estimand.

## Complete all-admission primary endpoint

Using only anchor admission/discharge times and procedure rows joined on (patient master index, encounter number), create an exhaustive, mutually exclusive label for every eligible admission:

- P0: valid procedure start in [0,24h) and before discharge;
- D0: discharge at or before 24h before any valid qualifying early procedure;
- U0: missing/invalid procedure timing whose possible placement could alter early procedure/discharge ordering or boundary status;
- R24: neither P0, D0 nor U0 is established;
- among R24, P1, D1 or U1 are assigned analogously in [24h,72h);
- N72: no established transition by 72h.

Preserve the incumbent tie policy, procedure wins an exact procedure/discharge tie, and report the opposite policy as sensitivity. Audit pre-admission and post-discharge rows, multiple rows, midnight starts, exact 24h/72h boundaries and missing starts. Missing procedure time is never no procedure. Report the all-admission terminal probability vector (P0,D0,U0,P1,D1,U1,N72); R24 is routing state, never a primary inclusion filter.

The primary estimand is unchanged in form:
E-minus-Q = score(E) - score(Q)
for held-out multiclass log loss and Brier, where lower is better. Only the strict-history provenance rule changes.

## Gated decision-relevance layer

Freeze a deterministic lexical map before locked evaluation, with normalized case/Unicode but no inferred synonyms:

- embolization/TACE: TACE, embolization, chemoembolization;
- resection/transplant: resection, transplant;
- ablation: ablation, radiofrequency, microwave, absolute alcohol;
- systemic/infusion: chemotherapy, targeted therapy, immunotherapy, infusion;
- diagnostic/access: contrast imaging, puncture, biopsy, drainage, catheter placement;
- otherwise other.

Preserve blank, ambiguous and multi-match strings. For each procedure in P0/P1, search orders with the same two-key join. A primary-tier qualifying order has nonblank Non-drug Order, valid Order Time strictly less than procedure Start Time, and a shared deterministic family match. Start Time is a separately reported fallback; ties, missing or conflicting times are not concordant. No outcome row enters predictors.

Run the family layer only if pre-locked counts meet: at least 100 timed procedure admissions with uniquely assigned family and valid pre-procedure order time; >=80% of timed procedure admissions have nonblank procedure text and exactly one family; >=70% of candidate orders have resolvable order time; no family exceeds 90% of concordant events; and <=25% of concordant candidates depend on fallback or unresolved/midnight timing. If it fails, report inconclusive and run generic any-order-before-any-procedure only if >=100 resolvable events; otherwise retain only the primary endpoint.

The gated labels are C (same-family order preceding procedure), Ponly, Oonly, D, U, and R/N for no established event, separately for the early and later windows. The generic fallback replaces same-family with any non-drug order and any procedure. This is a recorded order-procedure sequence, not a decision, treatment plan, intent, administration, completion or benefit.

## Information sets and alternatives

All models use identical cohort, endpoint, patient split, fit-only preprocessing and scores.

- A: age, sex, admitting department Encounter Department, calendar era, admission time-of-day and admission missingness.
- L: A plus index labs in [t0,t0+12h), using Lab Test, Qualitative Result, Quantitative Result, Specimen Type and Lab Time. Use assay-specific first/last valid numeric values, change, elapsed time, count, density/missingness and slope only with two distinct times; retain qualitative results by assay. No cross-assay numeric pooling because units are absent.
- Q: L plus strict-prior capture/process intensity: prior encounter count/duration/days active; time since last valid prior event; source-specific row and distinct-encounter counts for labs, procedures, orders and medications; source-type count; missing-time, left-truncation and no-history flags. Q contains no assay identity/value/result and no names, dose, route, frequency or status.
- E: Q plus strict-prior assay identity, numeric/qualitative result and dated trajectory, with fit-only within-assay scaling, recency, span, count, missingness and supported change/slope. No unverified physiologic score.
- H: transparent strict-prior summary of Q-like capture features, assay-specific lab summaries and source/process recency/gaps. Names are not interpreted.
- S: supervised irregular continuous-time latent state over the same strict-prior rows as E/H; each event has source/type, elapsed time, payload mask and only labs carry assay-specific content. A supervised competing-state head predicts the identical seven-state endpoint and, only after the gate, the concordance endpoint.
- S_Q: identical S with assay values/results removed, retaining source/type/time and capture information.

Fit A/L/Q/E/H with the same regularized sequential multinomial-logistic heads and marginalize early/later probabilities to the seven-state target. Fit S/S_Q with supervised terminal-state negative log likelihood; latent dimension, decay, masking/reconstruction term and shrinkage are fixed before locked evaluation and tuned only in selection. S can reveal irregular spacing, order-sensitive trajectory shape, nonlinear assay interactions and uncertainty that first/last/count summaries lose. S_Q tests whether any apparent gain is only capture-process structure. Primary contrast is E-Q; secondary contrasts are Q-L, E-L, H-L, S-E and S_Q-Q. The anchor-linked analysis is a provenance sensitivity, not a replacement.

A large transformer is deferred because no evidence establishes a long-context need. Documents, pathology and examination text are deferred because they lack native time and/or validated extraction. Causal treatment-effect, bedside utility and cross-site validation are unavailable from this snapshot.

## Split, uncertainty and falsification

Assign patients using SHA-256(normalized Patient Master Index) modulo 100: 0-59 fit, 60-69 selection/preprocessing/calibration, 70-79 locked evaluation, 80-99 inaccessible holdout. Every row follows its patient bucket. Freeze dictionaries, features, scaling, dimensions, hyperparameters, gate and calibration before locked outcomes.

Report paired held-out multiclass log loss and Brier for the complete seven-state vector, state calibration intercept/slope, reliability, observed-versus-predicted probabilities and probability contrasts. Use >=1,000 patient-clustered paired bootstrap resamples for 95% intervals, retaining all admissions per patient. Report no-prior-lab, one/two and >=3 prior-occasion strata and encounter-count strata without causal subgroup claims.

Predeclared falsifications:

1. Permute prior assay identity/results within row-count and capture strata, preserving times and counts; a content increment should attenuate while Q remains stable.
2. Compare S_Q with Q and test whether Q reproduces E's gain.
3. Reverse prior-row times and forcibly exclude all [t0,t0+72h) rows; future dependence invalidates interpretation.
4. Among patients with no strict-prior assay opportunity, E and Q must agree apart from missingness bookkeeping.
5. Reintroduce anchor-linked pre-t0 rows only as a labelled sensitivity; material divergence flags provenance dependence.
6. Rerun endpoint under conservative/optimistic missing-time handling and both tie policies; sign reversal or dominant U is inconclusive.
7. Scramble order times within encounter and compare order time with start time tiers; survival after scrambling is adverse for decision-relevance.

Supportive evidence requires the locked E-Q interval below zero for log loss and/or Brier, no material calibration deterioration, stability across opportunity/capture strata and 30/180/730-day windows, attenuation under content permutation, no future/split artifact, and no reproduction by Q/S_Q. The secondary requires its gate, adequate state support, tier robustness and attenuation under order-time scrambling.

Adverse evidence is no E-Q improvement, worse calibration, Q reproducing it, persistence after permutation, future dependence, leakage, or a concordance result surviving time scrambling or dominated by unresolved/low-confidence rows. Inconclusive evidence includes wide intervals, severe left truncation, sparse assays, dominant U states, substantial anchor-linked dependence, coarse timestamps, failed gate, ambiguous strings, source reversal or fallback-only results. Inconclusive is not confirmation.

## Exact HCC source bindings

Every source is an ordinary read-only CSV; archive member is ordinary file. Joins and multiplicity audits use (patient master index, encounter number).

| table / schema | exact source path | required columns and use |
|---|---|---|
| encounters / datasets/hcc/table-b743286cb1249287.json | [internal dataset path] | Patient Master Index, Encounter Number, Age, Sex, Encounter Time, Admission Time, Discharge Time, Department; cohort, time, A and capture |
| diagnoses / datasets/hcc/table-12710723c3df0c99.json | [internal dataset path] | Patient Master Index, Encounter Number, Diagnosis Name, Diagnosis Type; cohort coding, no time |
| labs / datasets/hcc/table-38aad8c54471332f.json | [internal dataset path] | Patient Master Index, Encounter Number, Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time; L/Q/E/S |
| procedures / datasets/hcc/table-d5eae16f8f8093d9.json | [internal dataset path] | patient master index, encounter number, surgery, start time, end time, surgery source; endpoint and gate |
| orders / datasets/hcc/table-6b93dcf0ea823702.json | [internal dataset path](Non-drug)_2062526727266216118.csv | Patient Master Index, Encounter Number, Non-drug Order, Order Time, Start Time, End Time, Order Duration, Order Status, Frequency; Q/H and concordance |
| medications / datasets/hcc/table-4f6ecaeb6e8f69c2.json | [internal dataset path] | keys, Medication, Single-dose Medication Amount, Single-dose Medication Amount Unit, Frequency, Start Time, End Time, Route of Administration, Drug Type; Q/H/S process |
| examinations / datasets/hcc/table-fd016d2731b9d6c6.json | [internal dataset path] | keys, examination, examination findings, examination diagnosis, start time, machine model, examination number; availability audit only |
| clinical_documents / datasets/hcc/table-66afca58512c2fca.json | [internal dataset path] | keys plus narrative fields including chief complaint, present illness, past history, admission diagnosis, course of diagnosis and treatment, discharge diagnosis, surgery procedure; no native time, excluded |
| pathology / datasets/hcc/table-0a4ee86a446c605c.json | [internal dataset path] | keys, pathology, examination findings, examination diagnosis, machine model; no native time, excluded |
| vitals / datasets/hcc/table-8436de9cba74b8ca.json | [internal dataset path] | keys only; identifier-only |
| transfers / datasets/hcc/table-320c20f732e71789.json | [internal dataset path] | keys only; identifier-only |
| front_page / datasets/hcc/table-38b3224239acc33f.json | [internal dataset path] | keys only; identifier-only |

Metadata confirms absent lab units, unvalidated narrative extraction, identifier-only vitals/transfers/front_page, no downloaded images or waveforms, and no native diagnosis time. The other configured datasets are accessible but are not HCC cohorts and are not external validation.

## Compute and clinical-evidence limits

Future solver planning is separate from discovery: chunked scans of the 2.2 GB labs and 2.19 GB orders plus smaller sources, compact patient matrices, 8-16 CPUs and 64-192 GiB RAM; expected but unverified 1-4 hours for aggregation/fits and 1-4 hours for bootstrap. S is CPU-first; an allocated A100 is optional only if a bounded measurement shows benefit, using cached ehr-campaign-gpu:20260908 and cuda:0. The planning envelope is at most 16 CPUs, 262144 MiB, 8 GPUs and 28800 seconds. These are estimates, not measured study results; no solver fit has been run. Discovery's 7200-second science budget is not substituted for future solver capacity.

Computationally checkable outputs are source/header/schema/key/time audits, cohort and endpoint counts, provenance exclusions, gate status, locked probabilities, scores, calibration, bootstrap intervals, permutations and sensitivities. Clinical adjudication or another study is required for active HCC, diagnosis timing, stage, burden, resectability, order meaning, intent, indication, scheduling, receipt, completion, appropriateness, response, toxicity, mortality, causal effects, bedside utility and transportability.

The actual deliverable is a newly fitted, locked strict-history E-versus-Q test on the unchanged complete all-admission endpoint, plus matched S/S_Q, provenance falsifications and gated order-procedure sensitivity. Revisit anchor-linked rows as primary only if expert review establishes pre-admission availability; revisit richer sequence models only if S adds stable information beyond E/H and S_Q does not reproduce it.
