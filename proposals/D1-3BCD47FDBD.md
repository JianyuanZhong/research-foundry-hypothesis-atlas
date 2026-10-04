> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional HCC hypothesis: post-hepatectomy laboratory trajectory and 30-day deterioration

Status: provisional checkpoint for episode 10. This is a proposed relationship and experiment, not a completed analysis or clinical conclusion.

## Proposed relationship

Among adults with a recorded liver resection in the HCC snapshot, the early post-operative trajectory of liver-related laboratory abnormalities will be associated with a clinically important deterioration signal during the subsequent 30 days, beyond baseline disease severity and operative context. The unresolved claim is whether a reproducible trajectory, rather than a single post-operative value, identifies a distinct recovery/deterioration pattern that could inform surveillance or escalation research.

This is not established. The inspected HCC dataset README and catalog establish that the snapshot contains longitudinal procedure, laboratory, encounter, transfer, diagnosis, medication, examination, pathology, and clinical-document data. They do not establish the proposed association, a causal mechanism, or clinical utility.

## Clinical importance and substantive advance

A positive result would distinguish an early warning pattern that merits prospective validation from the simpler explanation that a single baseline or early laboratory value is sufficient. A null result would be informative: it would argue against prioritizing trajectory-based surveillance in this dataset, while not proving that trajectories are clinically useless. The substantive advance is a data-bound comparison of a low-dimensional trajectory representation against a clinically interpretable baseline, rather than an uninterpreted expression plot or a prediction-only benchmark.

## Exact data binding (verified at catalog/README level)

Primary source snapshot: HCC snapshot `[source checksum]`.

- Procedures: `[internal dataset path]`, table `procedures`, schema `datasets/hcc/table-d5eae16f8f8093d9.json`. Use procedure labels and available procedure timestamps to define the liver-resection cohort and index date.
- Laboratory results: `[internal dataset path]`, table `labs`, schema `datasets/hcc/table-38aad8c54471332f.json`. Use dated liver-related assays (for example bilirubin, INR, ALT, albumin where labels and units are verified) to construct pre-index baseline and post-index trajectory features.
- Encounters: `[internal dataset path]`, table `encounters`, schema `datasets/hcc/table-b743286cb1249287.json`. Use encounter identifiers and dates to link the index procedure and subsequent observations.
- Transfers: `[internal dataset path]`, table `transfers`, schema `datasets/hcc/table-320c20f732e71789.json`. Use dated transfer/admission signals as an exploratory deterioration outcome and to assess observation intensity.
- Diagnoses: `[internal dataset path]`, table `diagnoses`, schema `datasets/hcc/table-12710723c3df0c99.json`. Use dated diagnosis records for prespecified post-index clinical deterioration and severity adjustment, subject to label validation.

The joins must use the documented HCC identifiers and time fields in the table schemas; no cross-dataset patient join is permitted. Source files are read-only. The exact procedure-label cohort, assay labels/units, missing-time handling, and operational outcome rule must be frozen after direct schema/row inspection.

## Planned Harbor experiment

Population: adults with a verified liver-resection procedure record and a valid index timestamp, restricted to the HCC source namespace. Temporal boundary: baseline laboratory measurements before the index procedure; trajectory measurements from post-index day 0 through day 7; outcome window from day 0 through day 30. Exclude patients without enough dated information for the prespecified comparison, and report exclusions.

Baseline comparison: a parsimonious model using pre-index baseline laboratory values, age/sex and available operative/encounter context. Alternative: a low-dimensional trajectory model using the same baseline covariates plus post-index day 0–7 assay slopes/changes (or a prespecified latent trajectory summary). Fit and evaluate with patient-level temporal splitting, no future leakage, and uncertainty intervals. The trajectory model is scientifically substantive because it tests whether direction and timing of recovery contain information lost by a single value; it is not justified merely by model complexity.

Outcome: a prespecified deterioration endpoint composed of dated transfer/admission and diagnosis signals, with the exact rule frozen before fitting. If the available labels cannot support a clinically interpretable endpoint, report an exploratory observation-intensity analysis only and do not call it clinical deterioration.

Supportive result: the trajectory model improves held-out discrimination/calibration for the prespecified endpoint with stable uncertainty, and the improvement is not explained by measurement frequency or baseline severity alone. Adverse result: no reproducible improvement, or improvement disappears after frequency/missingness adjustment, would weaken the trajectory claim. Inconclusive result: sparse assay coverage, unstable endpoint labels, or wide uncertainty would motivate endpoint adjudication or a larger/external cohort rather than a positive or negative clinical conclusion.

## Missing evidence and limits

The current checkpoint does not have fresh direct schema/row verification of every required column, verified assay units, a validated deterioration endpoint, or exactly three inspected key-reference receipts/source snapshots. The prior board recorded substantial procedure and laboratory row counts, but those counts are not treated as newly observed results here. Clinical adjudication, missing outcome definitions, and external validation are required before any treatment or surveillance claim.

## Alternatives and method choice

A simple baseline is required and is scientifically interpretable. The low-dimensional trajectory alternative is retained because it directly tests the unresolved information-in-timing question. A richer neural sequence model is deferred: it would add capacity without resolving the endpoint and assay-validity uncertainty, and the configured discovery budget is better spent on bounded schema/row diagnostics and the baseline-versus-trajectory comparison. Revisit a learned sequence model only if trajectory coverage, outcome support, and endpoint validity are established and the low-dimensional comparison remains scientifically ambiguous.

## Deliverable

The future solver must newly fit both models on the frozen HCC cohort, estimate held-out discrimination/calibration and uncertainty, quantify trajectory-feature contribution, and report supportive/adverse/inconclusive interpretations linked to computed outputs. Completion is not a claim of causality or clinical utility.
