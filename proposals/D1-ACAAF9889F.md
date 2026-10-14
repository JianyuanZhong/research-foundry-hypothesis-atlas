> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional HCC research hypothesis

## Proposed relationship
Among adults with a documented HCC diagnosis in this HCC hospital dataset, a temporally defined pattern of clinical deterioration during the index admission may be associated with a clinically important subsequent outcome (for example, readmission, escalation of care, or death), beyond baseline severity and treatment. The direction and magnitude are not assumed.

This is provisional because the exact outcome, diagnosis field, time zero, and cohort filters have not yet been verified against the HCC table schemas and source rows. The hypothesis must be narrowed after those bindings are inspected.

## What is currently supported
The available HCC dataset is a multi-table hospital record collection with source files for encounters, diagnoses, laboratory results, medications, procedures, examinations, vitals, transfers, orders, pathology, and clinical documents. The HCC README identifies 12 source files and corresponding table metadata. This supports the possibility of a longitudinal, data-bound study; it does not establish that any proposed variable or outcome exists, is complete, or is clinically interpretable.

No effect estimate, subgroup result, or causal conclusion is claimed.

## Unresolved question and clinical importance
The unresolved question is whether an early, measurable deterioration signal identifies patients whose subsequent clinical course is materially worse than patients with similar baseline severity. If supported, this could inform monitoring intensity or escalation decisions. If adverse or null, it would caution against treating a simple deterioration pattern as sufficient for risk stratification.

The strongest rival explanations are current severity, treatment intensity, documentation intensity, admission selection, and delayed or missing follow-up. These must be tested rather than interpreted away by adjustment alone.

## Falsifiable test to define next
A future computable experiment should define:
- a cohort from the HCC encounters/diagnoses tables with an explicit HCC diagnosis and index admission time;
- a prespecified observation window after time zero and an outcome window;
- baseline severity and treatment variables available before the outcome;
- a deterioration measure constructed only from time-stamped observations;
- patient-level splitting and leakage control;
- a simple baseline (for example, logistic regression or a prespecified severity score) and a substantive alternative that can reveal whether ordering, persistence, or multimodal interaction matters;
- supportive, adverse, and inconclusive criteria based on held-out discrimination/calibration, uncertainty intervals, and sensitivity to missingness and documentation intensity.

A null result would be informative if the cohort and outcome are adequately supported; it would not prove that deterioration is clinically irrelevant.

## Missing evidence and immediate limitations
- The HCC table JSON schemas, exact columns, join keys, timestamp conventions, and row-level availability have not been inspected because the episode checkpoint paused analysis.
- The exact HCC diagnosis code, discharge/readmission/death fields, and follow-up completeness are unverified.
- No public literature has been inspected or frozen for this draft.
- No model has been fitted and no dataset observation has been used to select the hypothesis.
- Clinical adjudication of outcome validity, treatment indication, and missingness mechanisms is unavailable from an automatic analysis alone.

## Next deliverable
Inspect the HCC metadata and exact source headers, verify the diagnosis/time/outcome bindings, and replace this provisional statement with a concrete population, estimand, variables, baseline, alternative method, falsification criteria, and three inspected key references.
