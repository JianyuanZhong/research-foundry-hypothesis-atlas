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

- [K1] Qiang et al. (2018) — Macrophage–fibroblast communication in fibrosis. Abstract inspected; establishes the biological context for directional signaling.
- [K2] Chen et al. (2020) — IL-1/TNF pathway in fibrotic signaling. Abstract inspected; provides pathway-specific context.
- [K3] Choi et al. (2018) — Donor-aware analysis in coculture systems. Abstract inspected; emphasizes the need for donor-aware estimands.

## Data and exact bindings
- Source: E-MTAB-8873
- Counts: [internal dataset path]
- Design: [internal dataset path]
- Features: 445 measured feature columns (targeted assay)
- Conditions: FLS-only, macrophage-positive, macrophage-negative, preLPS, preInhibitor, Inhibitor
- Donor structure: Multiple contributing or reused donors; explicit dependence modeling required

## Analysis plan
1. Pseudobulk each recorded FLS/coculture sample.
2. Donor-aware comparison of macrophage-positive vs negative coculture for IL-1/TNF pathway enrichment.
3. PreLPS and inhibitor attenuation test: compare pathway-specific response under perturbation vs untreated controls.
4. Competing explanations: generic culture effects, donor composition, macrophage abundance, measurement artifacts.

## Falsification criteria
- Null or non-specific response in macrophage-positive vs negative comparison: argues against the pathway hypothesis.
- No attenuation under preLPS or inhibitor: argues against pathway-specific signaling.
- Response driven by donor or culture composition: argues against a specific inflammatory mechanism.

## Limitations
- Targeted panel may not contain sufficient IL-1/TNF pathway genes.
- No analysis has been executed.
- Cross-sectional design cannot establish causal transitions.
