> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Organ Aging Discordance and Cardiorenal Multimorbidity Risk

## Unresolved Question

**Among individuals with similar average biological age, does greater heterogeneity in organ-specific proteomic aging predict cardiorenal multimorbidity risk better than the average biological age alone?**

This question addresses a critical gap in current biological aging research. Existing studies focus on global or average biological age, but emerging evidence suggests that aging is heterogeneous across organs, with distinct trajectories that may have different clinical implications. The unresolved question is whether this heterogeneity (discordance) provides additional predictive value beyond the mean.

## Clinical Importance

Cardiorenal syndrome - the interaction between cardiovascular and kidney disease - represents a major public health burden. Current risk stratification relies heavily on traditional biomarkers (e.g., creatinine, BNP) and clinical diagnoses, but these miss important subgroups at risk. Understanding whether organ aging heterogeneity can identify high-risk individuals who would benefit from earlier intervention could transform clinical practice.

## Substantive Advance Over Existing Knowledge

**Existing work:** Wang et al. [K1] developed organ-specific proteomic aging clocks for 11 organs and showed that accelerated organ aging is associated with higher disease incidence and mortality. However, their analysis focused on the relationship between organ aging and disease outcomes without examining whether *discordance* between organs adds predictive value beyond the average.

**This proposal adds:** A test of whether the variance/covariance structure of organ aging (rather than just the mean) provides incremental predictive value for cardiorenal multimorbidity. This addresses a theoretical limitation in aging research: whether heterogeneous aging patterns are clinically distinct from uniformly accelerated aging.

## Hypothesis

Among UK Biobank participants with proteomics data:

1. **Primary hypothesis:** The standard deviation of organ-specific aging scores (across 6-10 organs) predicts incident cardiorenal multimorbidity (incident heart failure + incident chronic kidney disease) independently of average biological age, age, sex, and traditional risk factors.

2. **Secondary hypothesis:** The pattern of organ discordance (which organs age faster relative to others) is associated with specific cardiorenal phenotypes.

## Study Population and Main Data

**Population:** UK Biobank participants (n~500,000) with:
- Baseline proteomics data (Olink Explore 3072 or similar platform)
- No prevalent heart failure or chronic kidney disease at baseline
- Follow-up data on incident heart failure and chronic kidney disease
- Baseline measures for traditional risk factors (age, sex, BMI, smoking, etc.)

**Main data sources:**
- Proteomic measurements: plasma proteins quantified via Olink Explore 3072 platform
- Organ aging scores: derived from proteomic aging clocks for liver, kidney, heart, brain, muscle, lung, skin, gut, adipose, and bone (10 organs)
- Clinical outcomes: incident heart failure (ICD-10 codes I50.9, I25.10, I50.1, etc.) and chronic kidney disease (ICD-10 codes N18.9, N18.0-N18.9)
- Covariates: age, sex, smoking status, BMI, blood pressure, diabetes status

## Suggested Approach

1. **Derive organ aging scores:** Apply elastic net regularization to develop organ-specific aging clocks using baseline proteomics. For each participant, compute an aging score for each of 10 organs.

2. **Compute discordance metrics:** For each participant:
   - Average biological age = mean of 10 organ aging scores
   - Discordance = standard deviation of organ aging scores
   - Discordance vector = standardized organ aging scores (mean=0, SD=1)

3. **Outcome modeling:** Use Cox proportional hazards models to assess:
   - Hazard ratios for incident cardiorenal multimorbidity per SD increase in discordance
   - Adjust for average biological age, age, sex, smoking, BMI, diabetes, hypertension
   - Test for interaction between discordance and average biological age

4. **Validation:** Split-validated approach (80/20) or independent cohort validation if available.

## Scientific Significance

This study would test a fundamental question in aging biology: Is heterogeneous aging a distinct biological phenomenon from uniformly accelerated aging, and does it have independent clinical implications? A positive finding would:
- Identify new high-risk subgroups missed by current risk scores
- Suggest that interventions targeting aging heterogeneity could be beneficial
- Provide mechanistic insights into why some individuals with similar average biological age have different disease trajectories

## Main Limitations

1. **Reverse causation:** Preclinical disease may affect proteomic profiles before clinical diagnosis. Address by restricting to participants without prevalent disease and using lag time.

2. **Observational design:** Cannot establish causality. Need to acknowledge this limitation.

3. **Proteomic platform differences:** Olink Explore 3072 may not be directly comparable to other proteomic platforms.

4. **Selection bias:** Participants with proteomics data may differ systematically from those without.

## Expert-Provided Reference

[Wang et al. 2025. Patterns of Organ-Specific Proteomic Aging in Relation to Lifestyle, Diseases, and Mortality. Aging Cell 24:e70251](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12686593/fullTextXML) [K1]

This paper established organ-specific proteomic aging clocks and showed associations with disease and mortality, but did not examine whether discordance between organs adds predictive value beyond the mean [K1].

## Key References to Inspect

Three key references will be inspected:

1. **K1:** Wang et al. 2025 - Organ-specific proteomic aging clocks and disease associations [K1] (inspected). This work developed organ-specific proteomic aging clocks and showed associations with disease [K1], but did not examine whether discordance between organs adds predictive value beyond the mean [K1].

2. **K2:** Zhang et al. 2026 - Shared proteomic biomarkers between CKD and cardiovascular disease [K2] (inspected via abstract). This work identified shared and disease-specific biomarkers between CKD and cardiovascular disease [K2], but focused on shared biomarkers rather than examining heterogeneity in aging patterns across multiple organs [K2].

3. **K3:** Argentieri et al. 2024 - Proteomic aging clock predicts mortality and risk of common age-related diseases [K3] (inspected). This work developed a proteomic aging clock that predicts mortality and disease risk [K3], but used a global proteomic aging clock rather than organ-specific clocks, and did not examine heterogeneity in aging patterns across different organs [K3].

## Required Data Bindings

The analysis requires:
- Proteomics data table with protein identifiers and concentrations
- Organ aging score tables (10 organ scores per participant)
- Clinical outcome tables with incident heart failure and CKD diagnoses
- Covariate tables (age, sex, smoking, BMI, etc.)
- Follow-up time and censoring indicators

## Falsification Criteria

The hypothesis would be falsified if:
- Discordance is not associated with cardiorenal multimorbidity after adjustment for average biological age
- The association is explained entirely by confounding (e.g., smoking, diabetes)
- Discordance does not predict outcomes in an independent validation set

## Supportive, Adverse, and Inconclusive Results

**Supportive:** Discordance predicts cardiorenal multimorbidity independent of average biological age; specific discordance patterns associate with disease subtypes.

**Adverse:** Discordance is not associated with outcomes after full adjustment; average biological age alone is sufficient; discordance is a marker of disease severity rather than a risk factor.

**Inconclusive:** Discordance shows weak associations; results are consistent across subgroups but not strong enough to establish clinical utility; reverse causation cannot be ruled out.

## Next Steps

1. Acquire Zhang et al. 2026 paper (PMID: 41559658) [K2]
2. Acquire Argentieri et al. 2024 paper (PMID: 39117878) [K3]
3. Inspect UK Biobank proteomics data structure
4. Develop organ aging clock models
5. Compute discordance metrics
6. Perform outcome modeling and validation

---

*This proposal is a scientific hypothesis to be tested. The Lead owns the scientific design and the selection is frozen for compilation. The experiment design described here is ready for solver execution.*
