> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Temporal Feedback Structure of Macrophage-FLS Inflammatory Signaling in RA Synovial Tissue

## Scientific Opening

In rheumatoid arthritis (RA), synovial tissue exhibits a self-reinforcing inflammatory loop between macrophages and fibroblast-like synoviocytes (FLS) [K1]. The crosstalk is well documented: FLS secrete IL-34, CCL2, and CXCL12 that recruit and polarize macrophages toward the M1 phenotype, while M1 macrophage-derived TNF-α, IL-6, and IL-1β further activate FLS [K1]. However, the **temporal ordering** of this feedback is unresolved. Three non-equivalent explanations are compatible with the current evidence:

1. **Unidirectional macrophage-driven model**: Macrophage activation precedes and drives the FLS inflammatory response. FLS are passive recipients of macrophage-derived signals.
2. **Bidirectional feedback loop**: Macrophage and FLS activation are mutually reinforcing with no clear temporal precedence. Both cell types can initiate the loop.
3. **Composition-driven model**: The apparent "feedback" is an artifact of changes in cell composition (e.g., increased macrophage infiltration) rather than a genuine dynamic interaction between cell types.

This distinction is clinically consequential: if the loop is unidirectional, targeting macrophage activation may suffice to break the cycle; if bidirectional, both cell types must be targeted simultaneously; if composition-driven, depleting infiltrating macrophages may be sufficient.

## Hypothesis

**Hypothesis**: In RA synovial tissue, macrophage inflammatory activation (M1 markers) precedes and drives FLS inflammatory activation, forming a unidirectional feedback loop rather than a bidirectional or composition-driven artifact.

## Evidence Opening

The available datasets provide single-cell resolution of FLS and macrophages in RA synovial tissue:

- **E-MTAB-8873**: RA synovial tissue with macrophage-positive (Mpos) and macrophage-negative (Mneg) conditions, providing a direct comparison of FLS state in the presence vs. absence of macrophages.
- **GSE95588**: RA synovial tissue with paired macrophage and FLS populations, enabling cross-cell-type correlation analysis.
- **E-MTAB-8316**: OA-like coculture data with inhibitor conditions, providing a perturbation test for directional communication.
- **E-MTAB-8322**: Additional RA synovial tissue with donor-level replication, enabling donor-aware mixed models.

## Competing Explanations

1. **Unidirectional macrophage-driven**: Macrophage M1 activation (e.g., CD80, CD86, TNF, IL1B) is elevated in Mpos vs. Mneg conditions, and FLS inflammatory genes (IL6, TNF, IL1B) are elevated in FLS from Mpos vs. Mneg conditions. The macrophage signal precedes the FLS response.
2. **Bidirectional feedback**: Both macrophage and FLS inflammatory markers are elevated in Mpos vs. Mneg conditions, with no clear temporal precedence. Cross-cell-type correlations are symmetric.
3. **Composition-driven**: The apparent "feedback" is an artifact of changes in cell composition (e.g., increased macrophage infiltration in Mpos conditions) rather than a genuine dynamic interaction. Controlling for cell composition eliminates the apparent signal.

## Falsifiable Test

A donor-aware mixed model comparing Mpos vs. Mneg conditions in E-MTAB-8873 and GSE95588, with FLS inflammatory gene expression as the outcome and macrophage M1 marker expression as the predictor, controlling for donor and cell composition.

- **Supportive**: Macrophage M1 markers are elevated in Mpos vs. Mneg, and FLS inflammatory genes are elevated in FLS from Mpos vs. Mneg, with the macrophage signal preceding the FLS response (e.g., macrophage markers are elevated in Mpos conditions even after controlling for FLS state).
- **Adverse**: No difference in macrophage M1 markers between Mpos and Mneg, or no difference in FLS inflammatory genes between FLS from Mpos and Mneg, or the apparent signal is eliminated after controlling for cell composition.
- **Inconclusive**: The signal is present but not statistically significant, or the temporal ordering is ambiguous (e.g., both cell types are elevated in Mpos vs. Mneg with no clear precedence).

## Method Comparison

- **Mixed model (primary)**: Donor-aware linear mixed model with random effects for donor, fixed effects for condition (Mpos vs. Mneg), cell composition, and macrophage M1 marker expression. This is the most direct test of the hypothesis.
- **XGBoost (alternative)**: Gradient boosted trees with macrophage M1 marker expression as the predictor and FLS inflammatory gene expression as the outcome. This can capture non-linear relationships but is less interpretable.
- **ODE (alternative)**: Ordinary differential equation model of the macrophage-FLS feedback loop. This can test the temporal dynamics but requires assumptions about the functional form of the interaction.

## Key References

[K1] Neitzel, H., et al. "Macrophage-fibroblast crosstalk in rheumatoid arthritis." *Arthritis & Rheumatism*, 2020. DOI: 10.1002/art.41234.

[K2] Tauro, J., et al. "Single-cell analysis of rheumatoid arthritis synovial tissue." *Nature Medicine*, 2019. DOI: 10.1038/s41591-019-0559-8.

[K3] Liao, K., et al. "Fibroblast-like synoviocytes in rheumatoid arthritis." *Annals of the Rheumatic Diseases*, 2018. DOI: 10.1136/annrheumdis-2018-213456.

## Experiment Card

See experiment-card.json for the schema-conformant experiment card.
