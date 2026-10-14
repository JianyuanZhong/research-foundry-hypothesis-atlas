> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Asynchronous Organ Recovery

## Hypothesis

After circulatory stabilization in critically ill patients, patients whose kidney or respiratory function remains impaired are more likely to deteriorate again.

## Study Population and Main Data

Patients with infection or shock; organ support, laboratory measurements, and vital signs.

## Suggested Approach

Prespecify recovery criteria and analyze recovery intervals in relation to subsequent escalation of support and death.

## Scientific Significance

Capture recovery information not represented by a single SOFA assessment.

## Main Limitations

Begin follow-up when the phenotype can be determined, avoiding future information.

## Expert-Provided Reference

[Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations](https://www.nature.com/articles/s41467-022-32222-2)

## Refined Hypothesis

This hypothesis has been refined to specify which recovery patterns are most predictive of subsequent deterioration. The refined hypothesis focuses on:

1. **Temporal recovery trajectories**: Analyzing the time to recovery of kidney and respiratory function after circulatory stabilization
2. **Discordant patterns**: Identifying patients where one organ recovers while another remains impaired
3. **Phenotype stratification**: Examining whether recovery patterns differ by underlying clinical phenotype (sepsis vs. shock vs. cardiac)
4. **Treatment escalation outcomes**: Focusing on subsequent treatment escalation as an actionable outcome rather than just mortality

## Data Bindings

### Primary Dataset: MIMIC-IV

Tables used:
- `icu/icustays` - ICU admission and discharge times, care units
- `icu/chartevents` - ICU vital signs and measurements
- `icu/d_items` - ICU item definitions
- `icu/inputevents` - Fluid and medication inputs
- `icu/outputevents` - Urine output and other outputs
- `hosp/pharmacy` - Pharmacy medications
- `hosp/admissions` - Admission and discharge information
- `icu/ingredientevents` - Detailed medication administration

### Key Variables:
1. Circulatory Stabilization Timepoint: Time when vasoactive support is discontinued or reduced below a threshold
2. Kidney Function Recovery: Time to creatinine normalization, time to urine output recovery
3. Respiratory Function Recovery: Time to SpO2 ≥92% on room air, time to ventilator discontinuation
4. Outcomes: 30-day mortality, ICU mortality, hospital mortality, re-escalation of organ support

## Scientific Approach

### Baseline Approach
- Use single-timepoint SOFA scores at admission or stabilization
- Compare outcomes between high vs. low SOFA groups

### Dynamic Approach (Proposed)
- Model time-to-recovery for each organ function
- Classify patients into recovery patterns (rapid, delayed, discordant)
- Build dynamic risk prediction models incorporating recovery trajectory features

## Falsification Criteria

The hypothesis will be falsified if:
1. Recovery trajectory metrics do not independently predict outcomes after adjusting for baseline severity
2. Single-timepoint SOFA scores perform as well as or better than recovery trajectory metrics
3. No specific recovery patterns show consistent prognostic value

## Key References

Three key references have been inspected:
1. **K1**: Nature Communications 2022 - Demonstrates that temporal inflammatory recovery dynamics predict outcomes
2. **K2**: MIMIC-IV documentation - Confirms data availability for temporal analysis
3. **K3**: Translational Andrology and Urology 2025 - Demonstrates temporal treatment analysis can identify prognostic patterns
