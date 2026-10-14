> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Research Proposal: Discordant Organ Recovery After Critical Illness

## Scientific Question

**Primary Hypothesis:** After circulatory stabilization in critically ill patients, discordant organ recovery patterns (rapid kidney recovery without concurrent respiratory or cardiovascular improvement, or vice versa) are independently associated with higher risk of subsequent deterioration and mortality, beyond what is captured by any single organ function measure.

**Unresolved Question:** Can we identify patients at high risk of deterioration based on the temporal discordance between organ-specific recovery trajectories, and does this risk stratification outperform traditional single-organ metrics (e.g., SOFA score, creatinine alone)?

## Clinical Importance

1. **Current Limitations:** Current critical care practice relies heavily on aggregate measures like SOFA scores or single-organ metrics (e.g., creatinine for kidney function). These aggregate measures may mask important discordances between organ systems that signal impending deterioration.

2. **Risk of Harm:** Patients with discordant recovery patterns may receive inappropriate treatment intensification or de-escalation. For example, a patient whose kidney function is recovering rapidly but whose respiratory status is deteriorating may be inappropriately weaned from respiratory support.

3. **Treatment Optimization:** Identifying patients with discordant recovery could enable more precise timing of interventions, such as when to escalate or de-escalate organ support, potentially improving outcomes and reducing unnecessary ICU stays.

## Substantive Advance Over Existing Knowledge

**Closest Prior Work:** [Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations](https://www.nature.com/articles/s41467-022-32222-2)

**Limitation of Prior Work:** The referenced study identifies co-regulatory WBC-PLT dynamics as a marker of inflammatory recovery but focuses primarily on inflammatory markers and does not directly address multi-organ recovery discordance in the context of treatment decisions.

**Substantive Advance:** This proposal extends the mechanistic insight from the inflammatory recovery paper to multi-organ recovery patterns. While the original paper identifies a universal WBC-PLT recovery trajectory, we propose that similar discordance principles apply across different organ systems. The hypothesis that multi-organ recovery discordance predicts deterioration represents a mechanistic refinement: organs may recover independently due to different pathophysiologic processes, and failure to achieve coordinated recovery signals ongoing systemic instability.

## Hypothesis Refinement

**Original Seed Hypothesis:** "After circulatory stabilization, patients whose kidney or respiratory function remains impaired are more likely to deteriorate again."

**Refined Hypothesis:** After circulatory stabilization in critically ill patients, those exhibiting discordant organ recovery patterns (e.g., rapid creatinine improvement without concurrent improvement in respiratory mechanics or oxygenation) have significantly higher odds of 28-day mortality or ICU readmission compared to patients with concordant organ recovery, even after adjusting for baseline severity and confounders.

**Quantifiable Prediction:** The odds ratio for adverse outcomes comparing discordant vs. concordant recovery patterns will be >1.5 (p<0.05) in a propensity score-matched analysis.

## Study Population

**Inclusion Criteria:**
- ICU patients aged 18+
- Diagnosed with sepsis, septic shock, or other critical illness requiring organ support
- Survived initial circulatory stabilization (defined as SOFA score improvement in at least one organ system)
- Had at least 3 organ-specific measurements during ICU stay (kidney: creatinine/BUN; respiratory: PaO2/FiO2, PEEP; cardiovascular: MAP, lactate)
- Followed for 28 days from stabilization point

**Exclusion Criteria:**
- Active major bleeding (ICD-10 D65, D66, or diagnosis_icd_10 containing "bleeding")
- Pre-existing end-stage renal disease (ESRD) at ICU admission
- Patients without adequate organ-specific measurements
- Transfers to other facilities during study period

**Temporal Boundaries:**
- Study period: MIMIC-IV ICU stays from 2018-01-01 to 2020-12-31
- Index time: First ICU day after circulatory stabilization (defined as MAP ≥65 mmHg for 2 hours with lactate trending down)
- Follow-up: 28 days from index time

## Main Data and Table Bindings

**Source:** MIMIC-IV v3.1, stored in `[internal dataset path]`

**Primary Tables:**

1. **icu/icustays**
   - `stay_id`: Unique ICU stay identifier (join key)
   - `hadm_id`: Hospital admission identifier
   - `intime`: ICU admission datetime
   - `outtime`: ICU discharge datetime
   - `los`: Length of stay in days

2. **icu/chartevents**
   - `stay_id`: Join key
   - `item_id`: Item identifier (join with icu/d_items)
   - `concept_name`: Description of the event
   - `datetime`: Event timestamp
   - `value_num`: Numeric value (for vitals)
   - `value_str`: String value (for diagnoses)

3. **icu/d_items**
   - `item_id`: Item identifier
   - `concept_name`: Item description
   - `domain_id`: Domain identifier

4. **icu/outputevents**
   - `stay_id`: Join key
   - `datetime`: Output timestamp
   - `output_type`: Type of output
   - `amount`: Amount output
   - `unit`: Unit of measurement

5. **icu/inputevents**
   - `stay_id`: Join key
   - `datetime`: Input timestamp
   - `input_type`: Type of input
   - `amount`: Amount input
   - `unit`: Unit of measurement

6. **hosp/pharmacy**
   - `patient_id`: Patient identifier
   - `stay_id`: ICU stay identifier
   - `drug_id`: Drug identifier
   - `drug_name`: Drug name
   - `dose_amount`: Dose amount
   - `dose_unit`: Dose unit
   - `admin_datetime`: Administration time

7. **hosp/labevents**
   - `patient_id`: Patient identifier
   - `stay_id`: ICU stay identifier
   - `lab_id`: Lab test identifier
   - `datetime`: Lab result time
   - `value_num`: Numeric value
   - `value_str`: String value
   - `labitem_id`: Lab item identifier (join with hosp/d_labitems)

8. **hosp/d_labitems**
   - `labitem_id`: Lab item identifier
   - `name`: Lab test name
   - `category`: Test category
   - `unit`: Unit of measurement

9. **hosp/patients**
   - `subject_id`: Patient identifier
   - `age`: Patient age
   - `gender`: Patient gender
   - `race`: Patient race
   - `ethnicity`: Patient ethnicity

10. **hosp/d_icd_diagnoses**
    - `patient_id`: Patient identifier
    - `stay_id`: ICU stay identifier
    - `icd10_code`: ICD-10 diagnosis code
    - `icd10_version`: ICD-10 version
    - `dt_start`: Start date of diagnosis
    - `dt_end`: End date of diagnosis

**Key Variables for Analysis:**

**Organ Recovery Metrics:**

**Kidney Recovery:**
- Creatinine trajectory (hourly measurements)
- BUN trajectory
- Urine output (from outputevents)
- Recovery defined as creatinine decreasing by >20% from peak or reaching baseline

**Respiratory Recovery:**
- PaO2/FiO2 ratio trajectory (from blood gases)
- PEEP requirements (from ventilator settings in chartevents)
- Oxygen saturation trajectory
- Recovery defined as PaO2/FiO2 improving by >20% or decreasing PEEP by 2 cmH2O

**Cardiovascular Recovery:**
- MAP trajectory
- Lactate trajectory
- Vasopressor requirements (from pharmacy/emar)
- Recovery defined as MAP ≥65 mmHg for 2 hours with lactate trending down

**Discordance Classification:**
- **Concordant recovery:** All three organ systems showing improvement simultaneously (within 24 hours)
- **Discordant recovery:** At least one organ system showing deterioration while others improve
  - Kidney-only recovery (kidney improves, respiratory/cardiovascular worsen)
  - Respiratory-only recovery (respiratory improves, kidney/cardiovascular worsen)
  - Cardiovascular-only recovery (cardiovascular improves, kidney/respiratory worsen)
  - Mixed discordance (any combination of two-way discordance)

**Outcomes:**
- **Primary:** 28-day mortality
- **Secondary:**
  - ICU readmission within 30 days
  - Hospital readmission within 30 days
  - Renal replacement therapy (RRT) initiation
  - Length of ICU stay
  - Length of hospital stay
  - Any adverse event (composite of death, RRT, or readmission)

## Baseline vs. Alternative Models

### Baseline Model: Single-Organ or Aggregate Recovery

**Model:** Logistic regression or Cox proportional hazards comparing outcomes based on single-organ recovery or aggregate SOFA score change.

**Equation:** logit(P(mortality)) = β₀ + β₁(kidney_recovery) + β₂(respiratory_recovery) + β₃(SOFA_improvement) + β₄(confounders)

**Expected Output:** Odds ratios for mortality comparing recovered vs. non-recovered patients based on single metrics.

### Alternative Model: Multi-Organ Discordance Analysis

**Model:** Logistic regression with discordance interaction terms.

**Equation:** logit(P(mortality)) = β₀ + β₁(kidney_recovery) + β₂(respiratory_recovery) + β₃(cardiovascular_recovery) + β₄(kidney×respiratory) + β₅(kidney×cardio) + β₆(respiratory×cardio) + β₇(any_discordance) + β₈(confounders)

**Expected Output:**
- Main effects of individual organ recovery
- **Interaction terms:** Test for discordance effects
- **Discordance indicator:** Odds ratio for any discordance vs. concordance

### Information Revealed by Alternative

The alternative model reveals **discordance patterns** that single-organ metrics cannot detect. This is clinically crucial because:
1. It identifies patients whose recovery is "one-sided" and may mask ongoing systemic instability
2. It suggests personalized monitoring based on which organ systems are discordant
3. It provides a more nuanced risk stratification than aggregate scores

## Analysis Plan

### Step 1: Phenotype Construction

1. **Identify ICU stays:** Match icustays to patients with critical illness
2. **Identify stabilization point:** Define circulatory stabilization (MAP ≥65 mmHg for 2 hours, lactate trending down)
3. **Calculate organ trajectories:**
   - Extract hourly creatinine, BUN, PaO2/FiO2, PEEP, MAP, lactate from chartevents/labevents
   - Fit piecewise linear models to identify improvement/deterioration phases
4. **Classify recovery patterns:**
   - Determine recovery status for each organ system at 24, 48, 72 hours post-stabilization
   - Classify as concordant (all improving) or discordant (any worsening)
5. **Define discordance subtypes:**
   - Kidney-only discordance
   - Respiratory-only discordance
   - Cardiovascular-only discordance
   - Mixed discordance

### Step 2: Propensity Score Matching

1. **Propensity model:** Multivariate logistic regression predicting discordant recovery
   - Covariates: Age, sex, comorbidities, baseline severity, organ support intensity, diagnosis type
2. **Matching:** 1:1 nearest neighbor matching with caliper = 0.2 SD of logit
3. **Balance check:** Standardized mean differences < 0.1 for all covariates

### Step 3: Outcome Analysis

1. **Primary analysis:** Cox proportional hazards or logistic regression comparing outcomes between matched groups
2. **Interaction analysis:** Test for discordance-by-outcome interactions
3. **Sensitivity analyses:**
   - Different definitions of discordance (time windows, thresholds)
   - Different follow-up periods (7, 14, 28, 30 days)
   - Subgroup analyses by diagnosis type (sepsis vs. cardiac vs. trauma)
   - Time-varying discordance (discordance at different time points)

### Step 4: Falsification Criteria

**Supportive Evidence:**
- Significant positive interaction (p<0.05): Discordant recovery increases risk of adverse outcomes
- Hazard ratio for mortality in discordant group > 1.5
- Discordance predicts outcomes better than concordance or single-organ metrics

**Adverse Evidence:**
- No significant interaction (p>0.05): Discordance does not affect outcomes
- Hazard ratios are similar in concordant and discordant groups

**Inconclusive Evidence:**
- Interaction p-value between 0.01 and 0.10 (borderline)
- Small sample size in discordant group
- High confounding despite adjustment

## Compute Requirements

**CPU:** 8 cores, 32 GB memory
**GPU:** 0 (tabular analysis on CPU)
**Time:** 1800 seconds (30 minutes)

**Output Files:**
- `phenotypes.json`: Constructed phenotype definitions and counts
- `propensity_scores.csv`: Matching results with balance statistics
- `outcome_analysis.csv`: Primary and secondary outcome results
- `discordance_analysis.json`: Discordance classification and interaction tests
- `analysis_log.txt`: Execution log with timestamps

## Limitations

1. **Unmeasured Confounding:** Despite propensity matching, unmeasured confounders may bias results
2. **Measurement Gaps:** Not all organ-specific measurements are captured in MIMIC-IV
3. **Discordance Definition:** The temporal definition of discordance (24 vs. 48 vs. 72 hours) may affect results
4. **Treatment Effects:** Discordance may be both a cause and consequence of treatment decisions
5. **Selection Bias:** Patients with severe discordance may receive different treatments, creating healthy user bias
6. **Temporal Resolution:** Hourly measurements may miss rapid changes

## Clinical Implications

If the hypothesis is supported:
1. **Treatment Guidelines:** Clinicians should monitor for discordant recovery patterns, not just aggregate scores
2. **Monitoring:** Real-time alerts for discordance between organ systems could trigger earlier intervention
3. **Risk Stratification:** Discordance could identify high-risk patients for closer monitoring or earlier escalation
4. **Clinical Decision Support:** Algorithms could flag patients with discordant recovery for review
5. **Research Direction:** Further investigation into the pathophysiologic mechanisms underlying discordant recovery

## Key References

[K1] Foy BH, Sundt TM, Carlson JCT, et al. Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations. Nat Commun. 2022;13(1):4705. PMID: 35995789

[K2] Kumar V, Roberts D, Wood KE, et al. Duration of hypotension initiating shock, a predictor for patient outcome. Crit Care Med. 2006;34(4):887-894. PMID: 16539545

[K3] Unspecified. Prognostic impact of early versus delayed loop diuretic administration in sepsis: a propensity score-matched analysis using the MIMIC-IV database. PMC: PMC11986544

## Data Availability

The MIMIC-IV dataset is available at:
- Source: `[internal dataset path]`
- Schema: See `[internal dataset path]`

All table metadata files are available in the MIMIC dataset catalog.

## Next Steps

1. Validate phenotype definitions with a small sample
2. Check data completeness for key variables (especially blood gas and ventilator data)
3. Run exploratory analysis to verify discordance patterns
4. Execute full propensity score matching and outcome analysis
5. Perform sensitivity analyses and robustness checks
6. Prepare manuscript with clear clinical recommendations
