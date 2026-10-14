> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Scientific Proposal: Metabolic-Organ Discordance Predicts Acute Hospitalization Outcomes

## Unresolved Question

Current critical care practice relies heavily on single-point organ dysfunction scores (SOFA, APACHE) to assess risk after acute illness. However, these scores capture only the current state of organ function, not the dynamic interplay between complementary physiological systems. A critical blind spot exists: patients whose metabolic recovery (glucose regulation) remains impaired while renal function improves (or vice versa) may be at elevated risk of subsequent deterioration, yet this discordant recovery pattern is not captured by traditional monitoring.

## Clinical Importance

This question has direct clinical importance because:

1. **Current practice limitation**: Single-point assessments at admission or discharge do not capture the dynamic, discordant nature of physiological recovery
2. **Patient safety**: Patients with discordant metabolic-renal recovery may receive inappropriate de-escalation of care or be at risk of delayed deterioration
3. **Resource allocation**: Identifying high-risk patients with discordant recovery could inform extended monitoring and escalation strategies
4. **Mechanistic insight**: Understanding which system's recovery lags provides insight into the pathophysiology of post-acute illness vulnerability

## Substantive Advance Over Existing Knowledge

Existing work ([prior hypothesis], [prior hypothesis]) focuses on:
- Multi-organ impairment duration after circulatory stabilization
- Temporal discordance between kidney function and inflammatory recovery

This proposal advances by:
1. **Different physiological axis**: Focuses on metabolic-renal discordance rather than multi-organ or inflammatory-renal discordance
2. **Different clinical context**: Addresses general hospitalization (HCC dataset) rather than ICU-specific stabilization
3. **Different measurement**: Uses glucose (metabolic) and creatinine (renal) rather than SOFA scores or inflammatory markers
4. **Novel prediction**: Tests whether metabolic-renal discordance predicts outcomes independent of traditional risk factors

## Data Bindings

### Population
- Patients with acute hospitalization in HCC dataset
- With at least 2 glucose measurements and 2 creatinine measurements
- With complete demographic and encounter information
- Excluding patients with known pre-existing diabetes (to focus on acute metabolic dysfunction)

### Tables and Columns
- **encounters**: 患者主索引 (patient_id), 就诊号 (encounter_id), 入院时间 (admission_time), 出院时间 (discharge_time), 年龄 (age), 性别 (gender)
- **labs**: 患者主索引 (patient_id), 就诊号 (encounter_id), 检测 (exam_type), 定量结果 (quantitative_result), 检测时间 (exam_time)
  - Filter: exam_type contains "glucose" or "血糖"
  - Filter: exam_type contains "creatinine" or "肌酐"
- **diagnoses**: 患者主索引 (patient_id), 就诊号 (encounter_id), 诊断名称 (diagnosis_name)

### Join Keys
- 患者主索引 (patient_id) across all tables
- 就诊号 (encounter_id) for encounter-level joins

### Time Fields
- admission_time from encounters
- exam_time from labs
- Discharge defined as first encounter where discharge_time is not null

## Hypothesis

Patients with discordant metabolic-renal recovery (glucose improving while creatinine worsens, or vice versa) after acute hospitalization have worse outcomes (mortality, readmission, length of stay) compared to patients with concordant recovery or stable recovery, independent of traditional risk factors (age, comorbidities, admission SOFA-equivalent scores).

## Baseline Comparisons

1. **Concordant recovery**: Both glucose and creatinine improve (or both worsen)
2. **Discordant recovery**: Glucose improves while creatinine worsens, OR glucose worsens while creatinine improves
3. **Stable recovery**: Both glucose and creatinine remain stable

## Outcomes

1. **Primary outcome**: In-hospital mortality
2. **Secondary outcomes**:
   - 30-day readmission
   - Length of hospital stay
   - ICU admission during index hospitalization

## Falsification Criteria

The hypothesis will be falsified if:
1. Discordant recovery is NOT associated with worse outcomes (adjusted HR < 1.0, p > 0.05)
2. Discordant recovery adds no incremental predictive value beyond traditional risk factors (NRI < 5%, C-index improvement < 0.02)
3. The discordance effect is only present in specific subgroups (e.g., only in patients with pre-existing conditions), not across the general population

## Method Comparison

### Baseline Method: Single-Point Risk Scores
- Uses admission SOFA-equivalent score
- Static assessment at one time point
- Does not capture recovery dynamics

### Learned/Mechanical Alternative: Temporal Discordance Modeling
- Uses longitudinal glucose and creatinine trajectories
- Identifies discordant vs concordant recovery patterns
- Can capture timing and rate of discordance
- Reveals what single-point scores miss: the *direction* of recovery mismatch

### Information Revealed by Alternative
- **Threshold effects**: Discordance at specific glucose-creatinine thresholds may have different risks
- **Multi-system coordination**: Discordance may indicate broader pathophysiological dysfunction
- **Recovery rates**: Rate of discordant recovery may predict outcomes better than absolute levels

## Resource Budget

- **CPU**: ~4 cores for data processing and statistical analysis
- **Memory**: ~16 GB for in-memory data processing
- **GPU**: Not required (tabular statistical analysis)
- **Time**: ~2-4 hours for data extraction, cleaning, and analysis

## Key References (to be acquired and inspected)

Three key references will support the hypothesis:
1. Paper on metabolic dysfunction and acute illness outcomes
2. Paper on renal recovery dynamics after acute illness
3. Paper on recovery discordance predicting outcomes

## Limitations

1. **Data availability**: HCC dataset may not have sufficient glucose/creatinine measurements
2. **Confounding**: Pre-existing metabolic/renal conditions may confound results
3. **Causality**: Observational study cannot establish causality
4. **Clinical validation**: Requires external validation before clinical implementation

## Next Steps

1. Acquire and inspect three key references
2. Extract and clean HCC data (glucose, creatinine, demographics)
3. Define recovery trajectories and discordance patterns
4. Perform statistical analysis comparing concordant vs discordant recovery groups
5. Evaluate incremental predictive value beyond traditional risk factors
6. Document results and submit candidate for assessment
