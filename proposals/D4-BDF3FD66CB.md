> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Multisystem Organ Dysfunction Trajectories in UK Biobank

## Hypothesis

Among patients hospitalized for acute illness, the temporal pattern of multiple organ dysfunction (MODD) - rather than single organ failure - predicts mortality better than the trajectory of individual organ failures, and the rate of organ system convergence (different organs failing in sequence) differs by pre-illness frailty.

## Unresolved Question

Current critical care research predominantly focuses on single-organ failure trajectories (e.g., "does acute kidney injury predict mortality?"). However, in real-world critical illness, multiple organ systems often fail in a coordinated, sequential manner. The key unresolved question is:

> **Does the temporal pattern of MULTIPLE organ system involvement (rather than the presence of individual organ failures) provide superior prognostic information, and does pre-illness frailty modify this relationship?**

## Clinical Importance

1. **Risk Stratification**: Current tools (SOFA, APACHE) score individual organs but don't capture the *temporal convergence* of organ failures. Understanding MODD trajectories could improve early risk prediction.

2. **Targeted Interventions**: If organ system convergence is driven by pre-illness frailty rather than acute insult severity, interventions could be prioritized for frail patients before organ failures become apparent.

3. **Prognostic Refinement**: The hypothesis is testable with UKB data on repeated hospitalizations and longitudinal outcomes.

## Substantive Advance Over Existing Knowledge

**Existing Research**:
- Studies single organ trajectories (e.g., AKI, ARDS)
- Uses static baseline measures (age, comorbidities)
- Doesn't examine temporal convergence of multiple organ failures

**This Proposal Advances By**:
- Examining *multisystem* rather than single-system organ trajectories
- Using *temporal convergence* (rate at which different organs fail in sequence) as the key variable
- Testing *frailty-modification* of the MODD-mortality relationship
- Leveraging UKB's repeated hospitalization data for natural experiments

## Key References

### K1: Wang et al. 2026 - "Organ-specific proteomic aging clocks predict disease and longevity across diverse populations" (Nature Aging)
**Claim**: Accelerated organ-specific aging (brain, artery, etc.) predicts disease onset, progression and mortality beyond clinical and genetic risk factors.
**Contribution**: Provides mechanistic framework for understanding organ-specific vulnerability to disease; supports hypothesis that multisystem dysfunction may be driven by underlying organ aging processes.
**Limitation**: Study uses proteomic aging clocks from UK Biobank; does not examine temporal trajectories of organ dysfunction during acute illness; clocks measure cumulative aging rather than acute decompensation.

### K2: Qiu et al. 2021 - "Dynamic changes in human single-cell transcriptional signatures during fatal sepsis" (J Leukoc Biol)
**Claim**: Temporal dynamics of immune cell populations and transcriptional signatures differ between surviving and fatal sepsis; platelet and erythroid precursor responses drive fatal outcomes.
**Contribution**: Demonstrates that temporal patterns of organ dysfunction (immune-mediated) matter for prognosis; supports hypothesis that tracking organ system trajectories may improve prediction.
**Limitation**: Single-cell transcriptomic study of peripheral blood; does not examine multiple organ systems; focuses on immune cell dynamics rather than multi-organ failure trajectories.

### K3: Liu et al. 2025 - "Phenotypes of Functional Decline or Recovery in Sepsis ICU Survivors" (Crit Care Med)
**Claim**: Functional decline phenotypes (including grip strength-based frailty) predict post-sepsis mortality and recovery trajectories; severe functional decline has poor outcomes.
**Contribution**: Demonstrates that pre-illness functional status (grip strength) predicts post-illness outcomes; supports hypothesis that frailty modifies organ failure trajectories.
**Limitation**: ICU survivors only; does not examine pre-illness frailty predicting organ failure trajectories in community-dwelling populations; focuses on recovery rather than progression.

## Data Bindings (UK Biobank Dataset)

### Population
UK Biobank participants with ≥1 hospitalization (health_outcomes table)

### Key Tables

1. **health_outcomes** (table-3cfae45e0905b0e3.json)
   - Source: `baidu_downloads/UKB/UKB/ukb672073_Health_Related_Outcomes.csv`
   - Columns: `eid`, ICD-10 codes (27980-0.0 for sepsis, 40000-0.0 for cardiovascular, etc.)
   - Join key: `eid`

2. **population** (table-38565c9e35e7cb6c.json)
   - Source: `baidu_downloads/UKB/UKB/ukb672073_Population_Characteristics.csv`
   - Columns: `eid`, `21022-0.0` (age at recruitment), `31-0.0` (sex)
   - Join key: `eid`

3. **additional_exposures** (table-099f610bfb23a632.json)
   - Source: `baidu_downloads/UKB/UKB/ukb672073_Additional_Exposures.csv`
   - Columns: `eid`, `24500-0.0` (likely grip strength), `24501-0.0` (likely waist circumference)
   - Join key: `eid`

### Temporal Boundaries
- Start: First hospitalization for acute illness (ICD-10 in infection [A00-B99] or organ failure categories)
- End: Death or 5 years from index hospitalization
- Follow-up: Repeated hospitalizations during follow-up

### Variables

**Exposure**: Temporal pattern of organ system involvement
- Organ systems: Sepsis (A00-B99), Cardiovascular (I00-I99), Respiratory (J00-J99), Renal (N00-N99), Neurological (G00-G99)
- Metric: Time from first organ failure to second organ failure (convergence rate)

**Outcome**: Mortality (ICD-10 codes starting with S00-T98 for death)

**Effect Modifier**: Pre-illness frailty (grip strength, age, comorbidity count)

### Baseline
- Compare MODD trajectories in low-frailty vs high-frailty participants
- Compare single-organ vs multi-organ failure trajectories

### Analysis
- Cox proportional hazards with time-varying exposure (organ system involvement)
- Test interaction between MODD convergence rate and frailty
- Baseline: Univariate hazard ratios for single organ failures
- Alternative: Multivariable model with MODD convergence as primary predictor

### Falsification Criteria
- **Adverse**: MODD convergence rate predicts mortality independently of single-organ trajectories, and this effect is stronger in high-frailty patients
- **Supportive**: Single-organ trajectories predict mortality equally well or better than MODD convergence
- **Inconclusive**: No independent predictive value for MODD convergence, or effect only in low-frailty patients

## Missing Evidence / Clinical Adjudication Required

1. **ICD-10 to Organ System Mapping**: Need to verify which ICD-10 codes in health_outcomes map to specific organ systems
2. **Frailty Definition**: Grip strength alone may not capture full frailty; need expert validation of the frailty definition
3. **Confounding**: Need to adjust for illness severity at index hospitalization (which may be partially captured by initial organ failures)

## Next Steps

1. Inspect ICD-10 to organ system mapping in health_outcomes
2. Verify additional_exposures fields for grip strength and frailty measures
3. Review expert seeds for related work (ukb-01, ukb-03, ukb-09)
4. Develop concrete analysis plan with Python/SQL queries
5. Prepare for reference inspection (3 key works)

## Related Expert Seeds

- **ukb-01**: Infection onset versus progression to severe disease - related focus on infection and organ damage
- **ukb-03**: Discordant kidney-function estimates and pre-illness reserve - uses grip strength and kidney function
- **ukb-09**: Metabolic deterioration and multimorbidity - examines changes in metabolic measures predicting multimorbidity
- **ukb-05**: Sleep regularity and progression to metabolic disease - uses longitudinal data approach (but requires accelerometry)
