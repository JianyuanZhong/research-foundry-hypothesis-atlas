> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional HCC trajectory-versus-care-process hypothesis (episode 12)

## Proposed relationship

Among adults with an exact documented hepatocellular carcinoma diagnosis and an inpatient encounter with a valid admission time, an ordered 7-day within-assay laboratory trajectory may add held-out predictive information about a subsequent inpatient procedure-based escalation proxy beyond an admission snapshot, treatment/procedure indicators, and documentation intensity.

The primary unresolved claim is whether temporal laboratory information persists after accounting for routine HCC treatment and care-process intensity. The procedure endpoint is a computable proxy for escalation of care, not a validated measure of death, ICU admission, clinical harm, or causal treatment effect.

## What is supported now

The inherited HCC source audit supports feasibility of a bounded test: the local HCC snapshot is bound to encounter, diagnosis, laboratory, and procedure files; joins are by patient/admission identifiers within HCC only. Prior direct scans reported 105,044 encounter rows, 101,457 valid admission times, 104,554 exact HCC patient/admission keys, 338,040 procedure rows, 321,207 timed HCC procedure rows, 15,774 untimed HCC procedure rows, and 20,052 HCC procedure rows after day 7 and before discharge (6,779 keys). These are availability and ascertainment counts, not fitted results or validated clinical outcomes.

The strongest currently supported claim is therefore only that the HCC tables contain enough timed, joinable records to test whether a prespecified temporal representation predicts a procedure-derived proxy. It does not establish that procedures represent deterioration, that the trajectory is biological, or that the proxy is clinically consequential.

## Falsifiable test

The solver must freeze a cohort and endpoint dictionary before fitting. The primary comparison is a snapshot model using admission demographics, admission laboratory values, admission department, treatment/procedure indicators, and documentation intensity against a time-aware model using ordered within-assay summaries over days 0–7 (liver, coagulation, renal, and tumor-marker assays where available). Because the available laboratory schema has no verified unit column, primary features must be within-assay summaries and must not combine incompatible units.

Use a patient-level split with no leakage across the same patient, a prespecified temporal window, and held-out evaluation of the incremental prediction contrast with uncertainty intervals. Compare the primary non-routine post-window procedure endpoint with a routine-treatment procedure endpoint and a timing-shifted negative-control endpoint. The test is supportive only if the temporal model improves held-out prediction for the prespecified non-routine endpoint beyond the snapshot by a prespecified non-trivial margin, with uncertainty excluding that margin, and the improvement is smaller for routine procedures and absent in the negative control. A null or adverse result is informative: it would favor care-process/documentation explanations or show no incremental temporal signal. Wide intervals, inadequate event support, or unstable endpoint definitions are inconclusive and require a revised endpoint or additional data.

## Exact data binding and missing evidence

Use only the HCC source files identified in the local catalog, with the HCC encounter table joined to diagnosis, laboratory, and procedure tables on the documented patient/admission keys. The encounter fields include patient/admission identifiers, age, sex, admission/visit/discharge times and department; diagnosis fields include diagnosis name/type; laboratory fields include assay/measurement and timestamped values; procedure fields include procedure name and timestamp. The solver must verify the exact source paths, table names, columns, archive members, and row counts from the catalog and source files before execution.

Missing or unresolved evidence includes: a clinically adjudicated escalation/death/ICU outcome; a frozen routine-versus-non-routine procedure dictionary; verified laboratory units and assay mappings; event counts after all temporal and cohort rules; and external validation. Clinical interpretation of the procedure proxy requires expert adjudication. No cross-database joins are permitted.

## Method comparison and selection

The simple baseline is a regularized logistic/gradient-boosted snapshot model with the same covariates available at admission. The substantive alternative is a time-aware model using ordered within-assay summaries, persistence, and change features over days 0–7, with the same patient split and outcome. The alternative can reveal whether the timing and persistence of measurements contain information that a static snapshot loses; it does not establish mechanism. A mechanistic or causal model is deferred because treatment assignment, indication, and clinical adjudication are not sufficiently available to identify them. CPU is adequate for the proposed tabular fits; GPU use is not scientifically necessary at this stage.

## Deliverable and interpretation limits

The future solver must newly fit both models, estimate the held-out incremental contrast and uncertainty, report endpoint/event counts, and produce supportive, adverse, or inconclusive conclusions linked to computed outputs. A positive predictive result would justify expert review of the proxy and a prospective validation study; it would not justify treatment claims. A negative result would challenge the usefulness of temporal monitoring for this proxy. An inconclusive result would identify the missing endpoint or measurement evidence needed next.
