> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant Organ Recovery Predicts ICU Deterioration

## Hypothesis

In critically ill patients, the presence of discordant organ recovery (one organ function improving while another continues to decline) after initial circulatory stabilization predicts subsequent deterioration more strongly than either organ's recovery alone.

## Scientific Rationale

Current ICU practice relies on aggregate severity scores (SOFA, qSOFA) that measure organ dysfunction at discrete time points, potentially masking discordant organ trajectories. Patients whose kidney and respiratory functions diverge in their recovery patterns may require fundamentally different management strategies than those with uniform recovery or no recovery. Understanding these discordant patterns could improve risk stratification and guide targeted organ support.

This hypothesis builds on insights from recent literature:
- **ALADYNOULLI** (Nature 2026) demonstrates that latent disease signatures can be identified from longitudinal EHR data, revealing biological subtypes within diagnostic categories
- **Delphi-2M** (Nature 2025) shows that multi-disease progression can be modeled with continuous-time prediction
- **Inflammatory recovery** (Nat Comm 2022) defines universal WBC-PLT co-regulatory dynamics as a recovery trajectory

However, none of these studies:
1. Explicitly test temporal discordance between organ systems in ICU populations
2. Use ICU chart events for real-time organ recovery monitoring
3. Define and quantify "discordant recovery" as a distinct clinical phenotype

## Study Population and Data

**Population:** ICU patients in MIMIC-IV who:
- Admitted with infection (ICD-9/10 codes for sepsis, pneumonia, UTI, etc.) or shock (ICD codes for hypovolemic, cardiogenic shock)
- Require at least one form of organ support (ventilator, vasopressors, CRRT/dialysis)
- Have at least 72 hours of ICU stay

**Primary Data Tables:**
- `icu/icustays`: ICU admission and discharge details
  - Columns: subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los
- `icu/chartevents`: Real-time chart events (vital signs, measurements)
  - Columns: subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valuenum, valueuom
- `icu/inputevents`: ICU inputs (ventilators, vasopressors, dialysis)
  - Columns: subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom
- `icu/outputevents`: ICU outputs (urine, drainage)
  - Columns: subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom
- `hosp/labevents`: Laboratory measurements
  - Columns: labevent_id, subject_id, hadm_id, specimen_id, itemid, order_provider_id, charttime, storetime, value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag, priority, comments
- `hosp/admissions`: Admission and discharge details
  - Columns: subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, etc.

## Temporal Boundaries

**Study period:** ICU stay from first_careunit admission to discharge/death

**Phenotype definition:**
1. **Hemodynamic stabilization:** Time to first 24-hour period without vasopressor requirement (from inputevents)
2. **Recovery assessment window:** 48 hours after hemodynamic stabilization
3. **Follow-up:** 24 and 7 days from hemodynamic stabilization for outcomes

## Key Variables

### Primary Exposure: Discordant Organ Recovery

At 48 hours post-stabilization, define organ status for each system:

**Renal function (from labevents, itemid for creatinine):**
- Status: improving (creatinine decreasing from stabilization to 48h), stable, or worsening
- Metric: % change in creatinine from stabilization to 48h

**Respiratory function (from chartevents, itemid for pO2, FiO2, SpO2):**
- Status: improving, stable, or worsening
- Metric: pO2/FiO2 ratio change from stabilization to 48h

**Hemodynamic stability (from inputevents, vasopressors):**
- Status: stabilized (no vasopressors for 24h), or unstable (continuous vasopressor use)

**Discordance categories:**
1. **Concordant recovery:** Both renal and respiratory improving
2. **Concordant deterioration:** Both worsening
3. **Discordant A→B:** Renal improving, respiratory worsening
4. **Discordant B→A:** Renal worsening, respiratory improving
5. **Mixed:** One improving, one stable

### Outcomes

**Primary outcome:** 24-hour ICU mortality
**Secondary outcomes:**
- 7-day ICU mortality
- Need for escalation of organ support (additional ventilator days, dialysis initiation)
- ICU length of stay

### Covariates

**Baseline characteristics:**
- Age, sex (from hosp/patients)
- Admission SOFA score (computed from chartevents/labevents)
- Initial vasopressor requirement
- Initial organ support (ventilator, CRRT)
- Comorbidities (from labevents, chartevents at admission)

**Temporal confounders:**
- Day of week (seasonality in ICU care)
- Time of day (circadian variation in measurements)
- ICU admission type (emergency vs planned)

## Analysis Plan

### Baseline Method

**Traditional approach:**
1. Compute single-organ recovery trajectories (renal and respiratory separately)
2. Use SOFA score at stabilization and 48h
3. Compare outcomes between organ recovery categories using logistic regression

### Substantive Alternative

**Discordance Index:**
1. Quantify the rate and direction of change for each organ system
2. Compute a discordance score based on:
   - Directional conflict (opposite trends)
   - Magnitude of discordance (difference in recovery rates)
   - Temporal persistence (how long discordance lasts)
3. Test whether discordance index predicts outcomes better than:
   - Single-organ recovery metrics
   - Aggregate SOFA scores
   - Composite "organ recovery score"

**Model specification:**
```
P(outcome | discordance_index, covariates) = logistic(β₀ + β₁·discordance_index + β₂·covariates)
```

Compare with:
```
P(outcome | renal_recovery, respiratory_recovery, covariates)
P(outcome | SOFA_stabilization, SOFA_48h, covariates)
```

## Falsification Criteria

**Hypothesis would be falsified if:**
1. Discordant recovery does not predict worse outcomes after adjusting for:
   - Initial severity (SOFA at stabilization)
   - Demographics (age, sex)
   - Comorbidities
2. The discordance index performs no better than the best single-organ recovery metric
3. Discordance is only predictive in patients with initial severity above a certain threshold (suggesting initial severity drives outcomes, not discordance)

**Hypothesis would be supported if:**
1. Discordant recovery is associated with higher mortality and organ escalation after adjustment
2. Discordance index outperforms single-organ metrics and traditional scores (AUC improvement ≥0.05)
3. Discordance persists in multivariate models and is independent of initial severity

## Clinical Significance

**If supported:**
- Discordant recovery should be identified as a distinct high-risk phenotype
- Clinicians should monitor patients for discordant organ trajectories
- Interventions targeting discordant recovery (e.g., renal support for patients with worsening respiratory function) may improve outcomes

**If not supported:**
- Current aggregate scoring approaches may be sufficient
- Resources could be redirected to other aspects of ICU care
- Further research on discordance may not be warranted

## Missing Evidence and Limitations

**Data limitations:**
1. **Causality:** Observational design cannot establish that discordance causes deterioration
2. **Measurement:** ICU chart events are intermittently recorded, not continuous
3. **Confounding:** Unmeasured confounders (e.g., specific pathogen, treatment decisions) may drive both discordance and outcomes
4. **Generalizability:** MIMIC-IV represents a single US ICU; results may not generalize to other settings

**Clinical adjudication required:**
1. Causal interpretation requires interventional studies
2. External validation in other ICU populations
3. Prospective trials testing interventions for discordant recovery

**Next steps if hypothesis is falsified:**
- Consider exploring discordance in specific subgroups (e.g., sepsis only, shock only)
- Test alternative definitions of discordance (e.g., different time windows, additional organ systems)
- Revisit the temporal boundaries or stabilization criteria

## Key References

**Inspected works:**
1. **ALADYNOULLI** (Nature 2026) - DOI: 10.1038/s41586-026-10780-5
   - Shows that Bayesian generative frameworks can identify latent disease signatures from longitudinal EHR
   - Demonstrates that disease-level predictions complement code-level foundation models
   - Limitation: Uses UK Biobank, not ICU data; doesn't test temporal discordance

2. **Delphi-2M** (Nature 2025) - DOI: 10.1038/s41586-025-09529-3
   - Models multi-disease progression with GPT transformers on continuous time axis
   - Shows sustained vs regressive effects of different diseases on mortality
   - Limitation: Uses UK Biobank, not ICU; focuses on disease occurrence, not organ recovery trajectories

3. **Inflammatory recovery** (Nat Comm 2022) - DOI: 10.1038/s41467-022-32222-2
   - Defines universal WBC-PLT co-regulatory dynamics as acute inflammatory recovery
   - Shows that recovery trajectories can predict adverse outcomes
   - Limitation: Focuses on hematologic markers, not multi-organ discordance; uses hospital data, not ICU

---

*This proposal has not been validated for data feasibility. The Lead must verify that all required columns and temporal relationships exist in the MIMIC-IV dataset before implementation.*
