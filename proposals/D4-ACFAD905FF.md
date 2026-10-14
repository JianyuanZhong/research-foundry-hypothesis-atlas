> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 04: Systemic reserve and infection-related mortality

## Question
Among adults with similar pre-illness lung function, does preserved systemic reserve identify lower short-term mortality after infection-related hospitalization?

## Clinical importance
Lung function alone may not capture the physiologic reserve that determines recovery from infection. If grip strength and biochemical reserve add prognostic information, post-discharge monitoring, rehabilitation and escalation decisions could be better targeted.

## Evidence opening
The closest inspected work supports that frailty and muscle strength are associated with adverse outcomes, while infection studies show that baseline physiologic state matters for recovery. The unresolved claim is whether systemic reserve adds information beyond pre-illness lung function and measured illness severity.

## Population and temporal design
Use UKB 04 participants with a pre-illness lung function measurement, an infection-related hospitalization, and available systemic reserve measurements. Lung function and reserve must precede the index hospitalization. Exclude measurements taken during or after the index event. Define the index date from the first infection-related hospitalization. Follow for 30-day mortality.

## Variables
- Exposure: pre-illness systemic reserve (grip strength, biochemical reserve)
- Covariates: age, sex, pre-illness lung function, measured illness severity
- Outcome: 30-day mortality after infection-related hospitalization

## Competing explanation
Illness severity may drive both lower systemic reserve and higher mortality. If the association disappears after adjustment for illness severity, the hypothesis is not independently supported.

## Estimand
The adjusted hazard ratio for 30-day mortality per unit increase in pre-illness systemic reserve, conditional on pre-illness lung function and measured illness severity.

## Method comparison
- Baseline: adjusted Cox proportional hazards model with pre-illness systemic reserve, lung function, illness severity, age, and sex.
- Learned alternative: penalized Cox model with structured shrinkage to test whether reserve is a stable independent signal or only a sparse/overfit pattern.
- The learned alternative can reveal whether the association is robust to regularization and whether it is driven by a small number of reserve components.

## Interpretation criteria
- Supportive: significant incremental association in both models, stable after adjustment.
- Adverse: no association after adjustment for illness severity.
- Inconclusive: association present in one model but not the other, or insufficient event count.

## Falsification
If the adjusted and penalized Cox models show no significant incremental association between pre-illness systemic reserve and 30-day mortality after infection-related hospitalization, after controlling for age, sex, illness severity, and pre-illness lung function, the hypothesis is not supported.

## Data bindings
- Source: UKB 04 (ukb672073 split tables)
- Lung function: FEV1, FVC (pre-illness)
- Systemic reserve: grip strength (left/right), biochemical reserve markers
- Infection-related hospitalization: ICD10 codes for infection
- Mortality: date of death
- Illness severity: APACHE or equivalent severity score if available

## Key references
[K1] Frailty and muscle strength associated with adverse outcomes (inspected)
[K2] Baseline physiologic state matters for recovery from infection (inspected)
[K3] UKB 04 data dictionary and field definitions (inspected)
