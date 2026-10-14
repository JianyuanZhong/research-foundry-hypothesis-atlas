> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Candidate Proposal: Vasopressor Washout Periods and Hemodynamic Recovery

## Candidate ID
candidate-vasopressor-washout-new

## Scientific Hypothesis

**Primary Question**: In critically ill patients receiving vasopressors, does the duration of the vasopressor-free interval (washout period) after cessation predict mortality, independent of baseline severity and cumulative vasopressor exposure?

**Hypothesis Statement**: After stopping vasopressor therapy, the length of the vasopressor-free interval (washout period) before achieving sustained normotension (>90th percentile systolic BP for 2 consecutive hours) is associated with subsequent mortality, independent of baseline severity and cumulative vasopressor exposure.

**Rival Hypothesis**: Mortality is predicted by baseline severity and cumulative vasopressor exposure, but not by the duration of the washout period after cessation.

## Clinical Importance

1. **De-escalation Protocols**: Current vasopressor protocols focus on achieving target blood pressure while minimizing duration of exposure, but the specific hemodynamic dynamics during the "washout" period after stopping vasopressors have not been systematically characterized.

2. **Rebound Hypotension Risk**: Understanding whether there is a critical threshold of vasopressor-free time needed for true hemodynamic recovery could help identify patients at risk of rebound hypotension who may need continued monitoring or prophylactic measures.

3. **Personalized Dosing**: The relationship between washout duration and outcomes could guide personalized dosing strategies based on cumulative exposure.

4. **Transportability**: This study could inform whether treatment effects are consistent across different hospitals and patient populations.

## Study Population

- **Dataset**: eICU-CRD 2.0
- **Population**: Adult patients (≥18 years) in ICU who received vasopressor therapy
- **Inclusion Criteria**:
  - Age ≥ 18 years at admission
  - Received vasopressor(s) for at least 12 hours
  - Had at least one vasopressor discontinuation event
  - Followed for 72 hours after final vasopressor dose
- **Exclusion Criteria**:
  - Missing vital sign data for ≥ 50% of ICU stay
  - Missing lab data for organ function assessment
  - Patients with documented pre-existing end-stage organ failure

## Main Data and Variables

### Primary Exposure: Washout Duration
- **Definition**: Time from last vasopressor infusion to first observation of sustained normotension (>90th percentile systolic BP for 2 consecutive hours)
- **Table**: `infusionDrug` and `vitalPeriodic`
- **Columns**: `patientunitstayid`, `infusionoffset`, `systemicsystolic`, `observationoffset`
- **Temporal Boundary**: From last vasopressor dose to 72 hours after or death/discharge

### Primary Outcome: Mortality
- **Definition**: Death within 72 hours of washout_end or death during ICU stay
- **Table**: `patient` (via `deathtime` and `hospitaldischargestatus`)

### Key Covariates

#### Patient-level (from `patient` table)
- `gender`: Sex at admission
- `age`: Age at admission
- `ethnicity`: Race/ethnicity

#### Baseline Severity (from `lab` and `diagnosis` tables)
- SOFA score at ICU admission
- APACHE II components at ICU admission
- Baseline organ dysfunction (from lab values at earliest labresultoffset)

#### Treatment-related
- **Cumulative Vasopressor Dose**: Sum of (infusionDrug.drugrate * duration of infusion) during exposure
- **Vasopressor Type**: norepinephrine, epinephrine, vasopressin, dopamine
- **Hospital Effects**: From `hospital` table (teachingstatus, region)

## Analysis Plan

### Baseline Model (Univariate)
- Compare mortality between patients who achieve normotension within 2 hours vs. >4 hours after stopping vasopressors
- Adjust only for baseline severity (SOFA score, APACHE II components)

### Primary Analysis (Multivariable)
- Cox proportional hazards model with:
  - Time-varying exposure to vasopressor-free intervals (categorical: <1h, 1-2h, 2-4h, >4h)
  - Time-varying covariates for cumulative vasopressor dose during exposure (continuous)
  - Interaction terms between washout duration and cumulative dose
  - Interaction terms between washout duration and baseline severity
  - Hospital-level random effects (mixed-effects Cox model)
  - Non-linear terms for washout duration (splines)

### Falsification Criteria
1. No association found after adjusting for baseline severity and hospital effects
2. All effect estimates mediated through baseline organ dysfunction
3. Linear relationship with no clinically meaningful threshold
4. Hazard ratio per hour of washout < 1.05 after adjustment

## Data Bindings

### Required Tables
- `infusionDrug` (table-18e1a8caaa91eb44.json): Vasopressor infusion data
- `vitalPeriodic` (table-a22c6d6981a32279.json): Blood pressure measurements
- `lab` (table-79bdb33275339b1a.json): Organ function markers
- `patient` (table-ab037c09d7df9a3c.json): Patient demographics and discharge/death status
- `hospital` (table-811df7b2ef435e12.json): Hospital characteristics
- `diagnosis` (table-5d5ab99e8c359037.json): Admission diagnoses for severity scoring

### Join Keys
- Primary key: `patientunitstayid` across all tables

### Time Fields
- Vasopressor timestamps: `infusionoffset` in `infusionDrug`
- BP timestamps: `observationoffset` in `vitalPeriodic` (minutes from ICU admission)

## Key References

1. **K1**: Suganuma et al. (2025) - Recent evidence showing no difference in hypotension rates based on discontinuation order
2. **K2**: Messina et al. (2025) - Framework for de-escalation phases
3. **K3**: Bauer et al. (2010) - Early evidence suggesting vasopressor-specific risks

## Scientific Value

High - addresses an important gap in understanding the temporal dynamics of vasopressor washout, with clear operationalization, comprehensive analysis plan, and strong clinical relevance.
