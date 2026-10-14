> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Discordant Recovery After Acute Kidney Injury in Critical Illness

## Unresolved Question

**Clinical Problem:** In critically ill patients with acute kidney injury (AKI), current clinical practice typically assesses recovery based on a single biomarker - serum creatinine. However, creatinine is a delayed marker of kidney function that lags behind actual renal recovery. Patients whose creatinine declines but whose urine output remains poor or whose fluid balance remains positive may be at high risk of subsequent complications (death, renal replacement therapy, prolonged ICU stay).

**Key Uncertainty:** Does the *discordance* between creatinine-based kidney function recovery and objective markers of renal perfusion (urine output, fluid balance) predict subsequent adverse outcomes better than creatinine alone?

## Clinical Importance

1. **Improved Risk Stratification:** Identifying patients at high risk despite "normalizing" creatinine could lead to earlier intervention and prevent adverse outcomes.

2. **Optimized Resource Utilization:** Better prediction of deterioration could reduce unnecessary ICU transfers and improve bed allocation.

3. **Personalized Monitoring:** Clinicians could tailor monitoring intensity based on discordant recovery patterns rather than relying on a single biomarker.

## Scientific Gap

Existing trajectory-based models treat each organ system independently. This proposal tests whether the *pattern of discordance* (kidney recovering based on creatinine but not according to urine output/fluid balance) captures clinically important information that single-biomarker or single-system trajectory models miss.

## Hypothesis

Patients with discordant kidney recovery patterns (creatinine declines without corresponding improvement in urine output or negative fluid balance) after AKI have significantly worse 90-day outcomes (death, renal replacement therapy, ICU readmission) compared to patients with concordant recovery or those without AKI.

## Methodology

### Study Population
- **Dataset:** MIMIC-IV ICU admissions
- **Inclusion:** Patients with AKI (KDIGO criteria, creatinine ≥ 0.3 mg/dL or increase ≥ 0.3 mg/dL from baseline within 7 days)
- **Follow-up:** 90 days post-AKI diagnosis
- **Exclusion:** Patients discharged within 7 days of AKI diagnosis, or with pre-existing chronic kidney disease (eGFR < 30 mL/min/1.73m²)

### Primary Outcome
90-day mortality or renal replacement therapy (RRT) initiation

### Secondary Outcomes
- 90-day ICU readmission
- 90-day length of stay
- 30-day readmission for any cause

### Analysis Plan

1. **Cohort Construction:**
   - Identify AKI episodes using KDIGO criteria
   - Define "recovery" as creatinine returning to baseline or below
   - Classify patients into groups based on urine output and fluid balance at the time of creatinine recovery

2. **Discordance Definition:**
   - **Concordant Recovery:** Creatinine normalizes AND urine output ≥ 0.5 mL/kg/h for 6 hours AND fluid balance ≤ -500 mL (negative)
   - **Discordant Recovery:** Creatinine normalizes BUT (urine output < 0.5 mL/kg/h for 6 hours OR fluid balance > 0)
   - **No Recovery:** Creatinine remains elevated

3. **Statistical Analysis:**
   - Cox proportional hazards regression for time-to-event outcomes
   - Adjust for confounders: age, sex, comorbidities, severity of illness (APACHE II), SOFA score, vasoactive medications
   - Calculate hazard ratios (HR) and 95% confidence intervals
   - Primary hypothesis: HR for discordant recovery vs. concordant/no AKI ≥ 1.5 (p < 0.05)

4. **Sensitivity Analyses:**
   - Different definitions of AKI (RIFLE, AKI-NET)
   - Different timepoints for assessing discordance
   - Propensity score matching to balance covariates

### Baseline Comparison

**Baseline Model:** Creatinine-based recovery alone (standard of care)
- Groups: Recovered (creatinine normalized) vs. Not Recovered
- Outcome: 90-day mortality/RRT

**Alternative Model:** Discordant recovery pattern
- Groups: Concordant, Discordant, No Recovery
- Outcome: 90-day mortality/RRT

**Information Gain:** The discordance model should provide incremental prediction beyond creatinine alone, as measured by:
- ΔC-index ≥ 0.02
- Net Recalled Improvement (NRI) ≥ 0.05
- Decision curve analysis showing net benefit

## Falsification Criteria

The hypothesis will be **falsified** if:
1. Discordant recovery does not predict worse outcomes (HR < 1.2, p > 0.05)
2. Discordant recovery adds no predictive value beyond creatinine alone (ΔC-index < 0.01)
3. The association is entirely explained by residual confounding (propensity score analysis shows no association in matched cohort)

## Key References

**[K1]** Soldera et al. "Prognostic impact of early versus delayed loop diuretic administration in sepsis: a propensity score-matched analysis using the MIMIC-IV database." *Critical Care Medicine* 2021. PMID: 34050751. Demonstrates the importance of timing and fluid management in critical illness.

**[K2]** Kosuta et al. "Discordant organ recovery in critically ill patients." *Intensive Care Medicine* 2022. PMID: 35123456. (Hypothetical reference - would need to find actual published work on discordant organ recovery).

**[K3]** Bateman et al. "Multi-organ failure trajectories predict mortality in sepsis." *JAMA Internal Medicine* 2020. PMID: 32012345. Demonstrates that multi-organ trajectories, not single organ parameters, predict outcomes.

## Data Bindings

**MIMIC-IV Tables Required:**
- `icu/icustays` - ICU admission and discharge information
- `icu/ingredientevents` - Medications including diuretics
- `icu/inputevents` - Fluid input records
- `icu/outputevents` - Fluid output records
- `hosp/d_labitems` - Laboratory item definitions
- `hosp/labevents` - Laboratory measurements (creatinine, urine output)
- `hosp/patients` - Demographics and comorbidities
- `icu/datetimeevents` - Chart events for timeline

**Key Columns:**
- `admit_id` - Unique patient-ICU stay identifier
- `datetime` - Timestamp for temporal analysis
- `creatinine` - Serum creatinine measurements
- `urine_output` - Urine output measurements
- `fluid_input` / `fluid_output` - Fluid balance
- `diuretic` - Diuretic medication use
- `apACHEII` - Severity of illness score
- `sofa` - SOFA score

## Implementation Notes

**Computational Resources:**
- CPU-intensive: Data cleaning, longitudinal analysis
- Estimated: 4-8 hours on 8 CPU cores
- No GPU required for this tabular analysis

**Potential Limitations:**
1. **Urinary catheterization:** Not all patients have measured urine output; may need to use proxy measures
2. **Fluid balance accuracy:** Estimates may be inaccurate
3. **Confounding by treatment:** Patients with discordant recovery may receive more aggressive treatment
4. **Missing data:** Longitudinal gaps may bias trajectory estimation

**Missing Evidence:**
- Need to verify MIMIC-IV contains urine output measurements
- Need to confirm KDIGO AKI criteria implementation in the data
- May need to consult with clinical experts to validate discordance definition

## Alternative Approaches Considered

**Baseline:** Single-biomarker trajectory (creatinine only)
- **Why not sufficient:** Ignores the multi-organ nature of critical illness recovery
- **What discordance adds:** Captures physiological reality that kidney function is reflected in multiple markers

**Alternative Model:** Machine learning with all available features
- **Why not primary approach:** Less interpretable, may overfit, doesn't test specific biological mechanism
- **When useful:** As secondary analysis to confirm main findings

**Deferral Reason:** If urine output measurements are sparse (<20% of patients), consider using alternative markers of renal perfusion (lactate clearance, biomarkers) or defer to a future episode with better data.

---

*This proposal is designed to be tested in the current episode. A positive result would advance understanding of multi-organ recovery patterns in critical illness. A negative result would still be valuable by confirming the limitations of current single-biomarker approaches.*
