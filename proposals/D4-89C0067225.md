> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-05: Bone-Muscle Discordance and Fracture Risk — A UK Biobank Cohort Study

## Unresolved Question

Low bone mineral density (BMD) and low muscle strength (grip) are each independently associated with fracture risk. However, it remains unclear whether their combination produces a synergistic (multiplicative) or merely additive increase in fracture risk, and whether the excess risk in the dual-low group is mediated by increased fall susceptibility or represents an independent bone-strength pathway. This distinction has direct clinical implications: if the excess risk is fall-mediated, fall-prevention interventions may be sufficient; if it is bone-strength-mediated, dual anti-resorptive + resistance-exercise strategies are needed.

## Hypothesis

In a UK Biobank cohort with DXA-measured BMD and handgrip strength, participants with both low BMD and low grip strength have a significantly higher hazard ratio for incident fracture than predicted by the additive combination of their individual risks, and this excess risk is partially (but not fully) mediated by increased fall occurrence.

## Clinical Importance

Osteosarcopenia (co-occurrence of osteoporosis and sarcopenia) is a recognized clinical entity, but the conventional definition has produced mixed results for fracture prediction [K3]. If the BMD×grip interaction is synergistic and partially fall-mediated, this would:
1. Justify dual-targeted interventions (anti-resorptive + resistance exercise) over single-target approaches
2. Identify a high-risk subgroup (dual-low) that may be missed by BMD-only screening
3. Inform fall-prevention strategies for the fall-mediated component

## Data and Feasibility (Verified)

**Source**: [UKB data file] (ukb671626 namespace, 502,371 participants)
- BMD: 23204-2.0/3.0 (L1-L4, g/cm2), 23208-2.0/3.0 (femur neck, g/cm2) — DXA subcohort, visits 2-3
- Grip: 46-0..3 / 47-0..3 (handgrip L/R, kg) — visits 0-3
- Falls: 2296-0..3 (falls in last year, binary) — visits 0-3
- Fracture: 41270-0..258 (ICD10 diagnoses) + 41280-0..258 (first in-patient date)
- Demographics: 31 (sex), 34 (date of birth), 21001 (BMI), 924 (ethnicity)
- AC dates: 53-0..3 (assessment centre visit dates)

**Verified counts** (this episode):
- BMD non-missing: 46,009
- Grip non-missing: 63,687
- BMD+grip overlap: 45,008
- Fracture events after BMD visit: 3,288
- 4-group: low BMD+low grip n=277 (43 fractures), low BMD+norm grip n=347 (39), norm BMD+low grip n=8,359 (578), norm+norm n=36,025 (1,405)

**BMD threshold**: <0.8 g/cm2 (approximates T-score ≤ -2.5 for lumbar spine in this age range)
**Grip threshold**: <20 kg (approximates <5th percentile for men, <10th for women)

## Design

### Population
UK Biobank participants with non-missing BMD (23204 at visit 2 or 3) AND grip strength (46/47 at visit 2 or 3), no prior fracture before the BMD visit date, age ≥50 at BMD visit.

### Exposure
- BMD: continuous (per SD) and binary (low <0.8 g/cm2 vs normal)
- Grip: continuous (per SD) and binary (low <20 kg vs normal)
- Interaction: BMD × grip (continuous and binary)

### Outcome
- Primary: incident fracture (any ICD10 S00-S99, T17, M80/M81) after BMD visit date
- Secondary: hip fracture (S72), vertebral fracture (S22/S32), fall occurrence (2296 at subsequent visits)

### Temporal boundaries
- Baseline: BMD visit date (53-2.0 or 53-3.0)
- Follow-up: from BMD visit to first fracture, death, or end of follow-up
- Exclude: fracture before BMD visit, death before BMD visit

### Analysis
1. **Cox PH model 1**: BMD (continuous) + grip (continuous) + BMD×grip interaction, adjusted for age, sex, BMI, ethnicity
2. **Cox PH model 2**: 4-group comparison (low BMD+low grip vs reference), same adjustments
3. **Mediation analysis**: BMD+grip → falls (2296) → fracture, using causal mediation framework
4. **Sensitivity**: sex-stratified, BMD site-specific (lumbar vs femoral), grip threshold sensitivity

### Falsification
- If BMD×grip interaction is not significant (p > 0.05) and 4-group HRs are flat, the synergistic hypothesis is not supported
- If the excess risk in the dual-low group is fully explained by falls (mediation proportion > 80%), the bone-strength pathway is not independently supported
- If the interaction is significant but the mediation proportion is < 20%, the fall-susceptibility pathway is not the primary mechanism

### Baseline vs Alternative
- **Baseline**: Cox PH with BMD + grip + interaction (additive model)
- **Alternative**: Mediation analysis adding falls as a mediator, revealing whether the excess risk is fall-mediated or bone-strength-mediated. This reveals information the baseline loses: the mechanism of the interaction.

## Key References

[K1] Yue J, et al. "Candidate proteomic indirect-effect signals linking dementia to probable muscle-bone fragility: a UK Biobank cohort study." Front Med (Lausanne). 2026;13:1883046. DOI: 10.3389/fmed.2026.1883046.
- Supports: UK Biobank framework for bone-muscle fragility analysis; grip strength as functional marker; time-updated Cox methodology
- Limitation: Focus on dementia, not BMD×grip interaction; no mediation analysis for fracture

[K2] Xu S, et al. "Bidirectional Relationship and Shared Mechanisms Between Sarcopenia and Osteoporosis: An Observational Study Integrating Genomic, Proteomic, and Metabolomic Data." Aging Cell. 2026;25(7):e70617. DOI: 10.1111/acel.70617.
- Supports: Bidirectional sarcopenia-osteoporosis relationship; grip strength HR for osteoporosis (0.544); genetic correlation r=0.25
- Limitation: UK Biobank heel BMD (not DXA); no fracture outcome; no mediation analysis

[K3] Lu AZ, et al. "Improving Hip Fracture Prediction by Using Sarcopenia-Specific Cut-Offs of T-Scores for Osteosarcopenia: A Prospective Cohort Study." J Cachexia Sarcopenia Muscle. 2026;17(4):e70348. DOI: 10.1002/jcsm.70348.
- Supports: Osteosarcopenia improves hip fracture prediction; sex- and sarcopenia-specific BMD cut-offs; conventional definition has mixed results
- Limitation: Small cohort (n=4000); hip fracture only; no mediation analysis; no interaction term

## What this proposal adds
1. First UK Biobank analysis of BMD×grip interaction for fracture (not just osteoporosis)
2. Mediation analysis through falls (not done in K1-K3)
3. Large sample (n=45,008; 3,288 fractures) vs K3 (n=4,000; 132 fractures)
4. DXA BMD (not heel) vs K2

## Limitations
- BMD threshold <0.8 g/cm2 is an approximation of T-score ≤ -2.5; T-score not directly available in this subset
- Grip threshold <20 kg is a rough cutoff; sex-specific percentiles would be more precise
- Falls (2296) are self-reported and binary; not a continuous measure of fall risk
- In-patient fracture codes may miss outpatient fractures
- No adjustment for physical activity, medication use, or comorbidities (available in 20003 but complex to code)

## Solver Task
Fit the Cox PH models and mediation analysis as specified. Report:
1. BMD×grip interaction coefficient, HR, 95% CI, p-value
2. 4-group HRs with 95% CIs
3. Mediation proportion (falls-mediated vs direct)
4. Sex-stratified results
5. Sensitivity analyses
