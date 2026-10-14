> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Directional cell communication: macrophage-to-fibroblast versus fibroblast-to-macrophage signaling in RA

Seed: D3-M2
Domain: Disease Mechanisms & Pathway Hypotheses

## Unresolved question

In rheumatoid arthritis (RA), do macrophages drive fibroblast activation (macrophage-to-fibroblast direction), or do fibroblasts drive macrophage polarization (fibroblast-to-macrophage direction), or both? This question is consequential because the dominant signaling direction determines whether therapeutic intervention should target the immune compartment or the stromal compartment.

## Evidence for the opening

- E-MTAB-8316 contains four FLS donor clusters with six nested monocyte donors and twelve condition samples. The nested design allows donor-aware paired comparisons of FLS and monocyte/macrophone expression under the same donor context.
- E-MTAB-8873 provides a targeted assay (445 measured features) with FLS/coculture pseudobulk samples, enabling measurement of specific ligand/receptor pairs in the same experimental system.
- GSE95588 coculture data provide additional paired condition comparisons, though r1/r2 includes earlier GSE57723 data and cannot count as independent validation.

## Hypothesis

H1 (macrophage-driven): In RA, macrophage-derived inflammatory signals (e.g., TNF, IL-1, IL-6) are the primary drivers of fibroblast activation, and fibroblast expression of activation markers (e.g., MMP1, MMP3, COL1A1 downregulation) increases in response to macrophage contact.

H2 (fibroblast-driven): In RA, fibroblast-derived signals (e.g., HB-EGF, NOTCH ligands, chemokines) are the primary drivers of macrophage polarization, and macrophage expression of inflammatory markers (e.g., CD80, CD86, IL-6) increases in response to fibroblast contact.

H3 (bidirectional): Both directions are active, and the dominant direction depends on the disease state or donor.

## Competing explanations

1. **Transient response**: The observed expression changes are transient and do not persist beyond the initial stimulus.
2. **Disease-driven persistence**: The expression changes are driven by the underlying disease state, not by cell-cell communication.
3. **Treatment artifact**: The expression changes are an artifact of the treatment or experimental conditions.
4. **Composition effect**: The observed changes reflect differences in cell composition rather than within-cell regulation.

## Data bindings

- **E-MTAB-8316**: [internal dataset path]; metadata [internal dataset path]
- **E-MTAB-8873**: [internal dataset path]; metadata [internal dataset path]
- **GSE95588**: [internal dataset path]; metadata [internal dataset path]

## Experimental design

1. **Donor-aware paired analysis**: Use the nested design in E-MTAB-8316 to compare FLS and monocyte/macrophone expression under the same donor context.
2. **Ligand/receptor pairing**: Identify ligand/receptor pairs that are co-expressed in the same experimental system (E-MTAB-8873).
3. **Perturbation test**: Use the coculture data (GSE95588) to test whether the expression changes persist beyond the initial stimulus.
4. **Competing explanations**: Explicitly test for transient response, disease-driven persistence, treatment artifact, and composition effect.

## Falsification criteria

- If the expression changes are transient and do not persist beyond the initial stimulus, H1 and H2 are falsified.
- If the expression changes are driven by the underlying disease state, not by cell-cell communication, H1 and H2 are falsified.
- If the expression changes are an artifact of the treatment or experimental conditions, H1 and H2 are falsified.
- If the observed changes reflect differences in cell composition rather than within-cell regulation, H1 and H2 are falsified.

## Key references

[K1] Wang et al. (2026) describe how RA develops through continuous interaction between systemic autoimmunity and local synovial lesion formation. The transition to persistent clinical synovitis requires establishment and stabilization of a local synovial immune niche. However, the review does not test whether the macrophage inflammatory state within this niche is persistent or transient upon stimulus removal.

[K2] Yi et al. (2026) describe how M1/M2 polarization imbalance drives RA progression. M1 macrophages maintain the inflammatory state, while M2 macrophages promote resolution. The review does not test whether the polarization is driven by macrophage-to-fibroblast or fibroblast-to-macrophage signaling.

[K3] Zhang et al. (2025) describe how fibroblast-derived HB-EGF drives macrophage polarization in RA. The study provides evidence for the fibroblast-to-macrophage direction, but does not test whether the macrophage-to-fibroblast direction is also active.
