> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 40 adaptation: glycemic worsening with weight loss as an early pancreatic-cancer signal

## Scientific opening

The UKB 40 seed asks whether similar HbA1c worsening accompanied by weight loss predicts later pancreatic cancer more strongly than weight gain. This is clinically important because pancreatic cancer is often diagnosed late, and a reproducible pre-diagnostic metabolic pattern could justify earlier imaging or specialist review. However, the seed's claim is not yet identifiable: weight loss may reflect intentional dieting, diabetes treatment, another malignancy, or early pancreatic cancer itself. The unresolved question is whether the excess risk is concentrated in a prespecified short window and persists after accounting for medication and pre-existing cancer, rather than merely describing people who were already ill.

## Hypothesis and strongest rival

**Hypothesis:** Among UKB participants with valid HbA1c and weight at two assessment visits and no prior pancreatic cancer, a prespecified increase in HbA1c accompanied by weight loss (rather than weight gain) is associated with a higher hazard of pancreatic cancer diagnosed within 2 years after the second visit, compared with similar HbA1c worsening accompanied by weight gain.

**Strongest rival:** The association is driven by pre-existing pancreatic cancer or another serious illness causing weight loss before diagnosis, or by diabetes treatment and lifestyle changes rather than an early pancreatic-cancer signal.

## Data bindings

Use the UKB/ukb672073 split tables of the completed subset:

- Field 30750: Glycated haemoglobin (HbA1c) — repeated measurements
- Field 30740: Glucose — repeated measurements
- Field 21002: Weight — repeated measurements
- Field 21001: Body mass index (BMI) — repeated measurements
- Field 20003: Treatment/medication code — diabetes medication
- Field 40005: Date of cancer diagnosis
- Field 40006: Type of cancer: ICD10 — pancreatic cancer
- Field 41270: Diagnoses - ICD10 — pre-existing cancer
- Field 41280: Date of first in-patient diagnosis - ICD10
- Field 53: Date of attending assessment centre

Join key: participant ID (UKB-specific namespace; never join incompatible namespaces).

## Population and temporal boundaries

- Participants with valid HbA1c and weight at two assessment visits
- No prior pancreatic cancer (exclude if diagnosed before the second visit)
- Second visit within 2 years of the first (to ensure a meaningful interval)
- Follow-up starts at the second visit
- Primary outcome: pancreatic cancer diagnosed within 2 years after the second visit
- Sensitivity: exclude diagnoses within 90 days of the second visit (reverse causation)

## Analysis

1. **Primary:** Cox proportional hazards model with baseline HbA1c, weight change, and a prespecified HbA1c-worsening-by-weight-loss interaction.
2. **Sensitivity:** Gradient-boosted survival model to capture nonlinear HbA1c/weight trajectories and medication patterns.
3. **Adjustment:** Diabetes medication, pre-existing cancer, assessment interval.

## Falsification criteria

The hypothesis is falsified if:
- The prespecified HbA1c-worsening-by-weight-loss interaction is null or reversed after restricting to participants with two valid measurements within 2 years, excluding prior pancreatic cancer, and adjusting for diabetes medication, pre-existing cancer and assessment interval.
- The association disappears in a sensitivity analysis excluding diagnoses within 90 days of the second visit.

## Interpretation

- **Supportive:** A significant interaction with a hazard ratio >1 for weight loss vs. weight gain, persisting after adjustment and reverse-cause sensitivity analysis.
- **Adverse:** A null or reversed interaction, or disappearance after adjustment.
- **Inconclusive:** Insufficient event support (e.g., <30 pancreatic cancer cases in the 2-year window) or high missingness.

## Limitations

- Cannot establish causality or identify pancreatic cancer as the cause of weight loss without additional data.
- Association surviving adjustment does not by itself identify a mechanism.
- The study cannot distinguish intentional dieting from illness-related weight loss without additional data.

## Key references

- [K1] UKB 40 seed: glycemic worsening with weight loss as a pancreatic cancer signal
- [K2] UKB field definitions: HbA1c, weight, cancer diagnosis
- [K3] Cox proportional hazards model for survival analysis
