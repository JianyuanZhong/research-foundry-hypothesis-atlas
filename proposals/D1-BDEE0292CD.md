> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Vasopressor Washout Periods and Hemodynamic Recovery

## Hypothesis to test

After stopping vasopressor therapy, the length of the vasopressor-free interval (washout period) before achieving sustained normotension (>90th percentile systolic BP for 2 consecutive hours) is associated with subsequent mortality, independent of baseline severity and cumulative vasopressor exposure.

## Study population and main data

**Population:** Patients in eICU with:
- Continuous vasopressor infusion records (infusionDrug table)
- Frequent blood pressure monitoring (vitalPeriodic table)
- ICU stay duration sufficient to observe post-cessation outcomes

**Inclusion criteria:**
- Received vasopressor(s) for at least 12 hours
- Had at least one vasopressor discontinuation event
- Followed for 72 hours after final vasopressor dose

**Key tables and joins:**
```
infusionDrug.patientunitstayid → vitalPeriodic.patientunitstayid → lab.patientunitstayid → patient.patientunitstayid → hospital.hospitalid
```

**Variables:**
- `vasopressor_start`: timestamp of first infusionDrug.infusionoffset
- `vasopressor_end`: timestamp of last infusionDrug.infusionoffset
- `cumulative_dose`: sum of (infusionDrug.drugrate * duration of infusion) in units
- `washout_start`: timestamp of last infusionDrug.infusionoffset
- `washout_end`: timestamp when BP >90th percentile systolic for 2 consecutive hours
- `washout_duration`: washout_end - washout_start (in hours)
- `outcome`: mortality within 72h of washout_end OR death during ICU stay
- `baseline_severity`: SOFA score or APACHE II at ICU admission (from diagnosis/lab at admission)
- `vasopressor_type`: norepinephrine, epinephrine, vasopressin, dopamine
- `hospital_id`: hospital-level characteristics (teachingstatus, region)

## Scientific significance

Current vasopressor protocols focus on achieving target blood pressure while minimizing duration of exposure, but the specific hemodynamic dynamics during the "washout" period after stopping vasopressors have not been systematically characterized. Understanding whether there is a critical threshold of vasopressor-free time needed for true hemodynamic recovery could:

1. Inform de-escalation protocols in shock - when to stop and when to continue
2. Predict which patients require continued vasopressor support
3. Identify patients at risk of rebound hypotension who may need continued monitoring or prophylactic measures
4. Guide personalized dosing strategies based on cumulative exposure

## Baseline comparison

**Baseline approach:** Compare mortality between patients who achieve normotension within 2 hours vs. >4 hours after stopping vasopressors, adjusting only for baseline severity (SOFA score, APACHE II components).

This baseline tests whether a simple threshold-based analysis shows an association, but fails to:
- Account for the cumulative vasopressor burden during exposure
- Model the interaction between exposure intensity and washout duration
- Control for hospital-level practice differences
- Examine non-linear relationships (e.g., U-shaped risk)

**Expected baseline result:** May show weak or no association due to confounding by baseline severity and hospital practices.

## Substantive learned/mechanistic alternative

**Alternative model:** A Cox proportional hazards model with:
- Time-varying exposure to vasopressor-free intervals (categorical: <1h, 1-2h, 2-4h, >4h)
- Time-varying covariates for cumulative vasopressor dose during exposure (continuous)
- Interaction terms between washout duration and cumulative dose
- Interaction terms between washout duration and baseline severity
- Hospital-level random effects (mixed-effects Cox model)
- Non-linear terms for washout duration (splines)

**What this could reveal that baseline loses:**
1. **Non-linear relationship:** Whether risk increases monotonically, peaks at intermediate durations, or has a threshold effect
2. **Exposure-washout interaction:** Whether patients with higher cumulative exposure need longer washout periods
3. **Hospital-level effects:** Whether practice differences explain residual variation
4. **Clinical utility:** Whether the relationship is strong enough to inform clinical decision-making

## Data bindings (concrete paths and columns)

```python
# Required data sources
# eicu/admissionDrug.csv.gz - patient demographics at admission
# eicu/patient.csv.gz - patient-level identifiers
# eicu/hospital.csv.gz - hospital characteristics
# eicu/vitalPeriodic.csv.gz - blood pressure measurements (systemicsystolic, systemicdiastolic, systemicmean)
# eicu/infusionDrug.csv.gz - vasopressor infusions (drugname, drugrate, infusionoffset)
# eicu/lab.csv.gz - organ function markers (creatinine, lactate, base deficit)
# eicu/diagnosis.csv.gz - admission diagnoses for severity scoring

# Key transformations
# 1. Identify vasopressor drugs: norepinephrine, epinephrine, vasopressin, dopamine
# 2. For each patient-unit-stay, find:
#    - First infusion timestamp (vasopressor_start)
#    - Last infusion timestamp (vasopressor_end)
#    - Cumulative dose during exposure
#    - Washout start (last infusion timestamp)
#    - Washout end (first time BP >90th percentile for 2 consecutive hours)
#    - Washout duration in hours
# 3. Outcome: death within 72h of washout_end or death during ICU stay
# 4. Baseline severity: SOFA score at ICU admission (from lab values at earliest labresultoffset)
# 5. Hospital effects: join hospital.hospitalid to patientunitstayid
```

## Falsification criteria

The hypothesis will be falsified if:
1. **No association found:** After adjusting for baseline severity and hospital effects, washout duration shows no significant association with mortality (p > 0.05 for primary outcome)
2. **Mediated entirely by baseline severity:** All effect estimates are mediated through baseline organ dysfunction (indirect effect accounts for >90% of total effect)
3. **Purely linear with no threshold:** The relationship is linear across all washout durations with no clinically meaningful threshold
4. **Effect size too small:** The hazard ratio per hour of washout is <1.05 after adjustment (clinically uninformative)

## Clinical decision relevance

If the hypothesis is supported, clinicians could:
1. Use washout duration as a decision rule for continuing vs. discontinuing vasopressors
2. Set personalized thresholds based on cumulative exposure (higher exposure → longer washout)
3. Identify patients at high risk of rebound hypotension who may need continued monitoring
4. Develop de-escalation protocols with specific washout duration targets

## Key references (three inspected works)

1. **K1:** Suganuma et al. (2025) - Recent evidence showing no difference in hypotension rates based on discontinuation order, but does not address washout duration
2. **K2:** Messina et al. (2025) - Framework for de-escalation phases, but lacks specific metrics
3. **K3:** Bauer et al. (2010) - Early evidence suggesting vasopressor-specific risks, providing historical context

## Limitations and unresolved questions

1. **Definition of sustained normotension:** The 90th percentile threshold may not be appropriate for all patient populations
2. **Rebound vasopressor use:** Patients who restart vasopressors within 72 hours should be treated as continuation or new exposure
3. **Shock etiology:** The relationship may differ by shock type (sepsis vs. cardiogenic vs. hemorrhagic)
4. **Causality:** The observed association may be confounded by unmeasured factors (e.g., severity of underlying disease, response to treatment)
5. **Clinical applicability:** Whether the relationship is strong enough to change practice remains to be determined

## Resource requirements

- **Compute:** CPU-only sufficient for data processing and statistical analysis
- **Time:** ~2-4 hours for data extraction, cleaning, and analysis
- **Data:** Full eICU dataset (~2GB compressed, ~5GB uncompressed)

## Next steps

1. Extract vasopressor infusion records and identify patients with discontinuation events
2. Calculate cumulative dose and washout duration for each patient
3. Determine outcome (mortality within 72h)
4. Fit baseline model (simple threshold comparison)
5. Fit alternative model (Cox with interactions and hospital random effects)
6. Test for non-linearity using splines
7. Assess clinical utility (decision curve analysis)
8. Interpret results and prepare for clinical adjudication
