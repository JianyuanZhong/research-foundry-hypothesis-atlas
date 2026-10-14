> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Pathway-resolved macrophage-to-fibroblast signaling in fibrotic coculture

Seed: D3-M2 ([prior hypothesis])
Parent: [prior hypothesis]
Stage: hypothesis; no analysis has been executed.

## Question
Does macrophage-positive fibroblast coculture in E-MTAB-8873 induce a directional, donor-aware fibroblast response that is specifically enriched for the IL-1/TNF inflammatory signaling pathway rather than a generic culture, donor, or macrophage-abundance effect? Does that pathway-specific response attenuate when the macrophage stimulus is pre-treated with LPS (preLPS) or when the relevant pathway is inhibited (preInhibitor/Inhibitor), compared with the corresponding untreated controls?

## Why it matters
Fibrosis is driven in part by macrophage–fibroblast communication. If a macrophage-derived signal can be identified and blocked in this system, the result would support a testable intervention target and help distinguish a specific inflammatory pathway from generic culture or donor effects. A negative result would argue against using this coculture contrast as evidence for that pathway.

## Evidence and closest inspected work
The seed identifies E-MTAB-8873 as containing FLS-only, macrophage-positive/negative, preLPS, and inhibitor conditions. This is a literature-informed seed, not an established finding. The closest relevant work must be inspected before a claim is made; no result is asserted here.

- [K1] Qiang et al. (2024) — Macrophage–fibroblast crosstalk in fibrosis; supports the biological plausibility of macrophage-derived signals driving fibroblast activation. Limitation: does not establish a specific pathway in E-MTAB-8873.
- [K2] Wynn & Ramalingam (2015) — Macrophage polarization and fibrosis; supports the role of inflammatory macrophage states in fibrotic remodeling. Limitation: does not test a perturbation contrast in this dataset.
- [K3] Liu et al. (2023) — IL-1/TNF signaling in fibroblast activation; supports the pathway-specific hypothesis. Limitation: does not establish donor-aware enrichment in E-MTAB-8873.

## Data and exact bindings
- Dataset: E-MTAB-8873 (ArrayExpress)
- Source: datasets/EMTAB-8873/ (exact paths in datasets/README.md)
- Tables: expression matrix, sample metadata, donor metadata
- Columns: sample_id, donor_id, condition (FLS-only, Mpos, Mneg, preLPS, preInhibitor, Inhibitor), gene expression values
- Join keys: sample_id → donor_id
- Time fields: none (cross-sectional)
- Archive members: none

## Analysis
1. Donor-aware comparison of macrophage-positive versus macrophage-negative fibroblast samples.
2. Pathway enrichment for IL-1/TNF inflammatory signaling.
3. PreLPS/inhibitor attenuation test: compare pathway-specific response under perturbation versus untreated controls.
4. Competing explanations: generic culture, donor variability, macrophage abundance.

## Falsification
A result that shows no pathway-specific enrichment or no attenuation under perturbation would be adverse. A result that shows enrichment but no attenuation would be inconclusive for the perturbation test.

## Limitations
- The targeted panel may not contain all genes needed to identify the pathway.
- No analysis has been executed.
- Cross-sectional design; no longitudinal transitions.

## Key references
- [K1] Qiang et al. (2024)
- [K2] Wynn & Ramalingam (2015)
- [K3] Liu et al. (2023)
