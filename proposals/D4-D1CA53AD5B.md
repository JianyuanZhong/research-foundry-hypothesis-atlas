> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 04 seed assessment (working draft)

## Question
Among people with similar pre-illness lung function, does preserved systemic reserve (grip strength and biochemical markers) identify lower short-term mortality after infection-related hospitalization?

## Why it matters
Respiratory impairment and general frailty are often conflated. Separating them could identify patients who need respiratory support versus broader post-infection monitoring.

## Available evidence and bindings (to verify)
- FEV1/FVC: UKB fields 20150/20151.
- Grip strength: fields 46/47.
- Albumin/CRP: fields 30600/30710.
- Hospitalization, diagnosis and death: 41270, 41280, 40000.
- Assessment date: field 53.

## Competing explanation
Reserve indicators may proxy prior disease burden or healthcare access rather than acute physiological reserve.

## Falsification
If reserve does not predict post-infection mortality after adjustment for timing, age, sex, smoking and prior hospitalization, or if the association is identical for non-infection hospitalizations, the infection-specific reserve claim is not supported.

## Status
Seed-level design only. Exact Parquet paths, infection definitions, temporal windows, event counts and three inspected key works are unresolved.
