> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Reduced Testing and Subsequent Deterioration in eICU

## Scientific Question

Among eICU patients who remain clinically unstable after initial ICU stabilization, does an abrupt reduction in laboratory testing predict subsequent acute kidney injury (AKI) and organ deterioration? Is this association hospital-specific?

## Clinical Importance

Laboratory testing intensity in the ICU is a proxy for clinical attention. If reduced testing during instability predicts deterioration, it identifies a modifiable process-of-care signal for quality improvement. If the association is absent or explained by de-escalation/discharge, it prevents overinterpretation of testing frequency as a marker of patient need.

## Hypothesis

An abrupt reduction in laboratory testing while a patient remains clinically unstable is associated with higher subsequent AKI and organ-deterioration risk, with meaningful between-hospital variation.

## Study Population

- eICU-CRD patients with >=24h ICU stay
- At least one laboratory panel in the first 24h
- Excluded: patients with discharge/de-escalation flags in the 24h window preceding the test-interval analysis
- Excluded: patients with end-of-life treatment limitations (if identifiable in eICU)

## Key Variables

| Variable | Source | Definition |
|----------|--------|------------|
| Test count | eICU laboratory timestamps | Number of distinct lab tests ordered per 24h window |
| Clinical instability | eICU vitals/labs | MAP < 65 mmHg OR new organ dysfunction (SOFA component) |
| AKI | eICU creatinine | KDIGO stage 1-3 within 48h |
| Organ deterioration | eICU SOFA components | Increase in SOFA score within 48h |
| Hospital | eICU hospital_id | For stratification and random effects |

## Estimand

The association between an "abrupt reduction" (>=50% decrease in lab-test count over a 24h window compared to the prior 24h) and 48h AKI incidence, adjusted for:
- Current clinical state (MAP, SOFA, time since admission)
- Hospital (random effect or stratification)
- Time since ICU admission

## Analysis Plan

1. **Descriptive**: Distribution of test counts, instability prevalence, hospital variation
2. **Primary**: Cox regression or logistic regression for 48h AKI, with abrupt-reduction as time-varying exposure
3. **Sensitivity**:
   - Restrict to patients without discharge/de-escalation flags
   - Alternative reduction thresholds (30%, 70%)
   - Hospital-stratified analysis
4. **Competing explanations**:
   - De-escalation: test whether association persists after excluding patients with discharge orders
   - Confounding by indication: adjust for clinical instability at the time of reduced testing
   - Data gaps: sensitivity analysis excluding patients with >6h gaps in vital signs

## Falsification Criteria

- Null or reversed association after adjustment for clinical state and hospital
- Association confined to patients with discharge/de-escalation flags
- No hospital-specific variation in the association

## Interpretation

- **Supportive**: Association persists after adjustment, with hospital-specific effects → monitoring intensity may be a modifiable quality signal
- **Adverse**: Association absent or explained by de-escalation → testing frequency is not a reliable marker of patient need
- **Inconclusive**: Weak association with wide CIs, or association only in specific hospital subgroups

## Limitations

- eICU does not capture all reasons for reduced testing (e.g., clinician judgment, resource constraints)
- AKI definition relies on creatinine, which may be affected by fluid status
- Hospital-level confounding cannot be fully addressed
- No causal inference; association only

## Data Bindings

- Source: eICU-CRD (eicu-crd 2.0)
- Tables: patient, stay, lab, vitals, medication
- Join keys: patient_id, stay_id
- Time fields: timestamp (lab), admission_time (stay)
