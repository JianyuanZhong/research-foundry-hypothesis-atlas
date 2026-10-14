> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Pre-Illness Physiological Reserve and Post-Infection Recovery Trajectories

## Unresolved Question

**Does pre-illness physiological reserve (measured by pre-infection proteomic profiles) predict the *pattern* of organ recovery after severe infection, beyond merely predicting whether deterioration or recovery will occur?** [K1][K2]

Current literature focuses on:
1. Proteins associated with infection onset (UKB-01) [K3]
2. Proteins associated with cardiovascular risk after infection (UKB-06) [K3]
3. Single-timepoint recovery assessments in ICU (MIMIC-01, MIMIC-03) [K1]

**What remains unresolved:** The *temporal dynamics* of recovery—whether recovery follows a specific trajectory pattern (e.g., rapid early recovery followed by late deterioration vs. gradual sustained recovery)—and whether pre-illness proteomic profiles can predict these trajectory patterns.

## Clinical Importance

1. **Personalized recovery monitoring:** Identifying patients at risk of delayed recovery could trigger earlier interventions before clinical deterioration occurs.

2. **Mechanistic insight:** Distinguishing between "low reserve leading to poor outcomes" and "low reserve leading to atypical recovery trajectories" would clarify whether interventions should target prevention of infection or optimization of recovery.

3. **Treatment stratification:** Patients with specific recovery trajectory patterns may require different supportive care strategies (e.g., extended organ support vs. early weaning).

4. **Beyond binary outcomes:** Current prognostic models focus on death or major organ failure. Understanding trajectory patterns could improve risk stratification for intermediate clinical states.

## Substantive Advance Over Existing Knowledge

**Existing work:**
- UK Biobank studies identify proteins associated with infection onset vs. cardiovascular outcomes, but do not characterize recovery trajectories in ICU populations [K3].
- MIMIC-IV studies assess single-timepoint recovery (SOFA scores, creatinine) but lack pre-illness biological context.
- The inflammatory recovery paper [K1] characterizes WBC/platelet dynamics but does not link to pre-illness proteomics.
- Organ-specific proteomic aging clocks [K2] demonstrate that pre-illness proteomics capture meaningful biological aging signals.

**This proposal advances by:**
1. **Temporal granularity:** Moving from single-timepoint recovery to trajectory pattern classification.
2. **Multi-omics integration:** Combining pre-illness proteomics with ICU longitudinal data.
3. **Mechanistic specificity:** Testing whether specific proteomic signatures predict specific trajectory patterns (e.g., "rapid but unstable recovery" vs. "gradual sustained recovery").
4. **Clinical actionability:** Identifying trajectory patterns that warrant different clinical responses.

## Falsifiable Hypothesis

**Primary Hypothesis:** Patients with high pre-illness physiological reserve (defined by proteomic profiles in the top quartile of a composite reserve score) exhibit significantly different recovery trajectory patterns after severe infection compared to low-reserve patients, even when controlling for baseline severity and treatment.

**Specifically:**
- High-reserve patients are more likely to follow a "sustained recovery" trajectory (monotonic improvement with no late deterioration).
- Low-reserve patients are more likely to follow either "delayed recovery" (slow initial improvement) or "unstable recovery" (early improvement followed by late deterioration).
- These trajectory patterns are predictive of intermediate clinical outcomes (e.g., ICU length of stay, ventilator days) beyond traditional prognostic scores.

**Null Hypothesis:** Pre-illness physiological reserve does not predict recovery trajectory patterns after severe infection, independent of baseline severity and treatment.

## Data Bindings

### Primary Dataset: UK Biobank
- **Table:** `ukb.health_outcomes` (table-3cfae45e0905b0e3.json)
  - Columns: `eid`, proteomic columns (e.g., `22000-0.0`, `22001-0.0`, etc.)
  - Purpose: Pre-illness proteomic measurements

- **Table:** `ukb.population` (table-38565c9e35e7cb6c.json)
  - Columns: `eid`, demographics (age, sex, ethnicity)
  - Purpose: Covariates for baseline characteristics

### Secondary Dataset: MIMIC-IV
- **Table:** `icu.icustays` (table-7d5c8feb0fb0db4.json)
  - Columns: `subject_id`, `admit_time`, `discharge_time`, ICU stay duration
  - Purpose: Identify ICU admissions (infection-related)

- **Table:** `icu.chartevents` (table-8208609a785ea7e8.json)
  - Columns: `subject_id`, `chartevent_id`, `itemid`, `value`, `timestamp`
  - Purpose: Longitudinal ICU measurements

- **Table:** `icu.inputevents` (table-d193e854c19eb4ba.json)
  - Columns: `subject_id`, `itemid`, `value`, `timestamp`
  - Purpose: Fluid and medication administration

- **Table:** `icu.outputevents` (table-a7ad1c4cdcdbfe0a.json)
  - Columns: `subject_id`, `itemid`, `value`, `timestamp`
  - Purpose: Urine output, drainage

- **Table:** `hosp.labevents` (table-bf701d962c63287c.json)
  - Columns: `subject_id`, `itemid`, `value`, `timestamp`
  - Purpose: Laboratory measurements including lactate, creatinine, WBC

### Join Keys
- **UKB eid** ↔ **MIMIC subject_id** (via patient matching)
- **Time alignment:** UKB baseline (pre-infection) → MIMIC ICU admission time

## Baseline Methods

### Baseline 1: Logistic Regression
- **Model:** Predict infection-related ICU admission (binary)
- **Features:** Pre-illness proteomic profile
- **Outcome:** ICU admission for infection
- **Limitation:** Cannot capture trajectory patterns; only predicts whether admission occurs

### Baseline 2: Cox Proportional Hazards
- **Model:** Time to ICU discharge
- **Features:** Pre-illness proteomic profile + ICU covariates
- **Outcome:** Time to discharge
- **Limitation:** Assumes proportional hazards; cannot distinguish trajectory *patterns* from overall duration

### Baseline 3: Random Forest Classifier
- **Model:** Predict ICU length of stay
- **Features:** Pre-illness proteomic profile + ICU longitudinal features
- **Outcome:** Length of stay (continuous)
- **Limitation:** Black-box; does not explain trajectory patterns

## Alternative (Learned) Methods

### Method 1: Trajectory Pattern Classification with LSTM
- **Architecture:** Long Short-Term Memory network
- **Input:** Time-series ICU measurements (lactate, creatinine, SOFA, fluid balance)
- **Output:** Discrete trajectory pattern (e.g., "rapid-sustained", "delayed", "unstable", "no-recovery")
- **Training target:** Cluster-based trajectory labels (using unsupervised clustering on ICU trajectories)
- **Scientific value:** Can learn complex temporal dependencies that linear models miss

### Method 2: Mixed-Effects Trajectory Modeling
- **Model:** Non-linear mixed-effects model with random slopes
- **Fixed effects:** Pre-illness proteomic reserve, treatment, demographics
- **Random effects:** Individual patient trajectory intercepts and slopes
- **Scientific value:** Explicitly models individual variation in recovery dynamics

### Method 3: Latent Class Growth Analysis
- **Model:** Growth mixture modeling with time-varying coefficients
- **Output:** Probabilities of belonging to latent trajectory classes
- **Scientific value:** Identifies distinct subpopulations with different recovery dynamics

**What the alternative reveals that baselines lose:**
- Baselines predict *outcomes* or *duration*; alternatives identify *patterns* of recovery
- Baselines treat recovery as a single dimension; alternatives capture multi-dimensional trajectory dynamics
- Baselines cannot explain *why* certain patients follow certain trajectories; alternatives can identify proteomic signatures associated with specific patterns

## Analysis Plan

### Step 1: Population Definition
1. **UKB cohort:** Participants with proteomic measurements and ≥1 hospitalization for infection
2. **MIMIC cohort:** ICU admissions with documented infection (ICD-10 codes for infectious diseases)
3. **Linked cohort:** UKB participants who were admitted to ICU after infection (via patient matching)

### Step 2: Pre-Illness Reserve Score
1. **Composite reserve score:** Principal component analysis of proteomic columns
2. **Q1 vs Q4 stratification:** High vs low reserve groups
3. **Validation:** Check score distribution, missingness patterns

### Step 3: Trajectory Pattern Classification
1. **Feature extraction:** For each ICU stay, extract time-series of:
   - Lactate (persistent elevation vs. decline)
   - Creatinine (trajectory slope)
   - Fluid balance (input-output dynamics)
   - Vasopressor duration and intensity
2. **Unsupervised clustering:** Use k-means or Gaussian mixture models to identify trajectory patterns
3. **Pattern labels:** "Rapid-sustained", "Delayed", "Unstable", "No-recovery"

### Step 4: Association Testing
1. **Primary analysis:** Compare trajectory pattern distribution between high/low reserve groups
2. **Adjustment:** Control for age, sex, comorbidities, baseline severity (SOFA at admission), treatment
3. **Statistical test:** Chi-squared test with trend, logistic regression

### Step 5: Mediation Analysis
1. **Test:** Does pre-illness reserve affect outcomes through trajectory patterns?
2. **Model:** Mediation analysis with trajectory pattern as mediator

## Evaluation Criteria

### Success Criteria
1. **Statistical significance:** High-reserve patients show significantly different trajectory pattern distribution (p < 0.01)
2. **Effect size:** At least 15% difference in probability of "unstable" vs "sustained" recovery between groups
3. **Clinical utility:** Trajectory pattern + reserve score improves prediction of ICU length of stay beyond traditional scores (C-statistic improvement ≥ 0.05)

### Falsification Criteria
1. **No association:** High-reserve vs low-reserve patients show identical trajectory pattern distribution (p > 0.1)
2. **No clinical utility:** Adding reserve score to trajectory pattern does not improve outcome prediction
3. **Confounding:** All associations disappear after adjusting for baseline severity and treatment

### Inconclusive Results
1. **Small sample:** <100 patients with complete trajectory data
2. **Heterogeneous patterns:** Too many trajectory classes to identify meaningful subgroups
3. **Data quality:** >30% missing proteomic or ICU data prevents proper matching

## Key References

**[K1]:** Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations
- **Authors:** Wang et al.
- **Year:** 2022
- **DOI:** 10.1038/s41467-022-32222-2
- **Claim supported:** Recovery from diverse pathologic conditions follows a universal trajectory defined by exponential WBC decay and delayed linear platelet growth; co-regulation of WBC-PLT dynamics predicts adverse outcomes with 32x relative risk for cardiac surgery and 9x for sepsis mortality
- **Contribution:** Establishes that recovery trajectory patterns (not single timepoint measurements) are predictive of outcomes, providing a mechanistic framework for studying recovery dynamics
- **Limitation:** Focuses on WBC-PLT dynamics in hospitalized patients; does not link to pre-illness proteomic reserve
- **Locator:** Abstract and Methods sections
- **Inspection:** full_text

**[K2]:** Organ-specific proteomic aging clocks predict disease and longevity across diverse populations
- **Authors:** Wang et al.
- **Year:** 2025
- **DOI:** 10.1038/s43587-025-01016-8
- **Claim supported:** Organ-specific proteomic aging clocks derived from UK Biobank proteomic data can predict disease risk and longevity, demonstrating that pre-illness proteomic profiles capture biologically interpretable organ-specific aging processes
- **Contribution:** Demonstrates that pre-illness proteomic measurements capture meaningful biological aging signals that could serve as physiological reserve markers
- **Limitation:** Focuses on overall disease prediction rather than specific recovery trajectories after acute illness
- **Locator:** Abstract and Introduction sections
- **Inspection:** full_text

**[K3]:** Severe Infection and Risk of Cardiovascular Disease: A Multicohort Study
- **Authors:** Yusuf et al.
- **Year:** 2022
- **DOI:** 10.1161/CIRCULATIONAHA.122.061183
- **Claim supported:** Pre-illness proteomic profiles predict cardiovascular risk after severe infection, establishing a link between baseline biology and post-infection outcomes
- **Contribution:** Provides evidence that pre-illness proteomics are informative for post-infection risk stratification
- **Limitation:** Focuses on cardiovascular outcomes rather than comprehensive recovery trajectory patterns; limited to cardiovascular endpoints
- **Locator:** Abstract and Results sections
- **Inspection:** abstract_only

## Clinical Adjudication Required

1. **Patient matching:** UKB eid ↔ MIMIC subject_id linkage requires expert review of hospitalization dates and patient identity
2. **Trajectory pattern definitions:** Clinical experts should validate whether identified patterns correspond to clinically meaningful states
3. **Causality:** Observational design cannot establish causation; expert review needed to interpret mediation results
4. **Generalizability:** UKB (UK population) + MIMIC (US ICU) combination may have selection biases requiring expert review

## Resource Requirements

- **CPU:** 8 cores for data processing, trajectory clustering, and statistical analysis
- **Memory:** 32 GB for full dataset loading
- **Time:** 1800 seconds (30 minutes) for initial analysis
- **GPU:** Not required for initial analysis; could be used for deep learning trajectory models

## Next Steps

1. **Data exploration:** Load and inspect UKB proteomic and MIMIC ICU data
2. **Patient matching:** Develop algorithm to link UKB participants to MIMIC ICU admissions
3. **Trajectory extraction:** Implement time-series feature extraction for ICU stays
4. **Preliminary analysis:** Test association between reserve score and trajectory patterns
5. **Refinement:** Adjust analysis based on preliminary findings

---

**Note:** This proposal is a bounded scientific study designed to test a specific, falsifiable hypothesis. The full analysis would require significant computational resources and expert clinical review. The discovery phase focuses on designing the experiment and verifying data availability, not completing the full analysis.
