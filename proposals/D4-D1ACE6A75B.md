> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 04: Systemic reserve and infection-related mortality

## Question
Among adults with similar pre-illness lung function, does preserved systemic reserve identify lower short-term mortality after infection-related hospitalization?

## Clinical importance
Lung function alone may not capture the physiologic reserve that determines recovery from infection. If grip strength and biochemical reserve add prognostic information, post-discharge monitoring, rehabilitation and escalation decisions could be better targeted.

## Evidence opening
The closest inspected work supports that frailty and muscle strength are associated with adverse outcomes, while infection studies show that baseline physiologic state matters for recovery. The unresolved claim is whether systemic reserve adds information beyond pre-illness lung function and measured illness severity.

## Population and temporal design
Use UKB 04 participants with a pre-illness lung function measurement, an infection-related hospitalization, and available systemic reserve measurements. Lung function and reserve must precede the index hospitalization. Exclude measurements taken during or after the index event. Define the index date from the hospitalization record and assess mortality within 30 days. Preserve source-specific identity and do not join incompatible namespaces.

## Variables
- Outcome: 30-day mortality after the index infection-related hospitalization.
- Exposure: systemic reserve, represented by grip strength and biochemical markers available in the UKB 04 catalog.
- Conditioning: pre-illness lung function, age, sex and measured illness severity where available.
- Missingness: report measurement availability and use a prespecified multiple-imputation or complete-case sensitivity analysis; do not treat missing reserve as normal.

## Estimand and analysis
The primary estimand is the adjusted association between a prespecified reserve index and 30-day mortality within a pre-illness lung-function stratum. Fit a simple adjusted logistic regression baseline. Fit a regularized or ensemble alternative on the same inputs to test nonlinear reserve interactions and robustness. Compare calibration, discrimination and held-out performance; do not claim causality from adjustment alone.

## Falsification and interpretation
The claim is falsified if reserve has no meaningful or stable association after adjustment, or if the association disappears in held-out validation. Supportive results would justify a prospective prognostic study, not immediate treatment. Adverse results would weaken the reserve hypothesis. Inconclusive results require larger cohorts or better severity measurement.

## Method comparison
The simple adjusted model is interpretable and establishes the primary association. The learned alternative can reveal nonlinear reserve interactions and missingness patterns that a linear baseline loses. Both use the same inputs, split and outcome; the alternative is selected only if it resolves a substantive uncertainty rather than a small predictive gain.

## Key works
[K1], [K2] and [K3] are inspected works supporting the relevance of reserve/frailty, infection prognosis and measurement limits. See key-references.json for exact claim mappings and limitations.
