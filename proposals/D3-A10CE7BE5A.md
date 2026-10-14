> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Contamination-Controlled Re-analysis of Directional Macrophage→FLS Communication in RA: A Useful Negative Result

Parent: [prior hypothesis] (ep1 selection, valid, mu=29.40). Domain: disease_mechanisms.
Claim stage: observational (contamination-controlled re-analysis of an executed probe).
Screening: executed (bounded CPU probe, [research job]).

## Unresolved question (from parent)

The ep1 selection identified a 41-gene (reproducible: 26-gene) Mneg-dominant FLS transcriptional response (permutation p=0.021) in E-MTAB-8873 coculture data, but confirmed macrophage contamination of FLS-only baselines as the dominant unresolved confound. The pre-specified next test was: **does the Mneg-specific FLS signature survive after controlling for differential macrophage contamination?**

## What was done (this episode)

A contamination-controlled re-analysis was executed ([research job], succeeded, 1.5s):

1. **Contamination score**: For each of the 33 samples, the mean log2(x+1) expression of 58 macrophage-enriched marker genes (CD14, CD163, ITGAX, FCN1, CD33, CD48, CD86, PTPRC, LILRB4, MRC1, VSIG4, CD200, CD274, CD38, CD70, CD1A, CD1B, FCER2, FCGR3A, TNFSF8, C1QA, C1QB, CD80, CD209, CD37, CD22, CD300A, CD40, ITGAM, ITGB2, LY86, MME, TLR2, TLR9, FCER1G, CLEC4E, CLEC10A, BIN2, FYB, IRF8, IRF4, RUNX3, BACH2, PRDM1, STAT5A, MERTK, KLRK1, GIMAP2, GIMAP5, CCR2, CCR5, CXCR4, CXCR5, S100A9, S100A12, MS4A1, CD68, CD36, CD44) was computed.

2. **Differential contamination confirmed**: Mneg coculture samples have ~4× more macrophage RNA than Mpos samples (mean contamination score 6.89 vs 5.57; FLS-only baseline 4.01). Differential contamination (coculture − FLS-only): Mneg +2.88 vs Mpos +1.68 log2 units (mean).

3. **Regression**: For each gene, per-donor paired contrast (log2 coculture/FLS-only) was regressed on the differential contamination score. Mean R² = 0.35 (Mneg), 0.36 (Mpos) — contamination explains ~35% of per-gene contrast variance.

4. **Signature re-derivation**: After contamination adjustment, **ZERO genes** meet the Mneg-specific criterion (≥4/5 donors up, ≤1/5 Mpos up). The original 26-gene signature is entirely explained by contamination.

5. **Gene classification**: 92% (24/26) of the original Mneg-specific genes are macrophage-derived (surface markers, chemokines, cytokine receptors, immune transcription factors). 0% are FLS-identity genes.

6. **Directional asymmetry eliminated**: Original 26:0 (Mneg:Mpos) → Adjusted 0:1 (CXCL13).

## Result

**The apparent Mneg-specific FLS transcriptional response in E-MTAB-8873 is a contamination artifact, not a genuine macrophage-state imprint.** This is a useful negative result that:
- Refutes the parent's primary claim as stated (macrophage STATE imprints a reproducible directional FLS response)
- Identifies the specific limitation (440-gene panel resolution, not biology)
- Points toward cell-type-resolved assays (snRNA-seq, FACS-sorted FLS) as the necessary next step

## What this does NOT establish
- It does NOT prove that macrophage state has no effect on FLS biology
- It does NOT exclude a genuine FLS response that is smaller than the contamination signal
- It does NOT address the NOTCH3 fibroblast-intrinsic program (absent from panel)
- It does NOT address in vivo relevance

## Clinical importance

This result has direct implications for how coculture-based transcriptomic studies in RA (and other diseases) should be interpreted. The apparent "macrophage-state-specific FLS response" in E-MTAB-8873 is a composition artifact that would mislead researchers into pursuing a non-existent mechanism. The contamination-controlled analysis provides a methodological template for distinguishing genuine cell-type-specific responses from composition artifacts in bulk/coculture transcriptomic data.

## Data bindings (exact, verified)

- E-MTAB-8873.counts.tsv.gz: 440 targeted genes × 33 samples (MolsPerCell pseudobulk); SHA d218d3c4…
- E-MTAB-8873.design.json: 33 records; 5 FLS donors (SA256A, SA257A, SA258R, SA263R, SA266A) × {FLS-only, Mpos, Mneg} arms
- 58 macrophage-enriched marker genes verified present in the 440-gene panel
- Job: [research job] (succeeded, 1.5s, CPU 8, 64GB)

## Falsification (exact)

- Supportive: ≥5 genes with consistent within-donor direction (≥4/5 donors, |mean log2FC| ≥ 0.25) survive contamination control AND concordant direction in ≥1 external dataset.
- Adverse: no such gene set survives contamination control; the state-specific signature is fully explained by macrophage contamination. **This is the observed result.**
- Inconclusive: <3 donors with a paired arm; external concordance only on unresolved donor columns; contamination not excludable with available data.

Current status: **ADVERSE** — the Mneg-specific signature is fully explained by contamination. The parent's primary claim is refuted for the E-MTAB-8873 440-gene panel.

## Next test (computable, bounded)

1. Cell-type-resolved data: snRNA-seq or FACS-sorted FLS from the same coculture system would eliminate contamination entirely. This requires new data acquisition (not computable with bound data).
2. Larger gene panel: whole-transcriptome RNA-seq of the same coculture system would provide the resolution to separate FLS from macrophage expression. This requires new data acquisition.
3. External validation: GSE95588 (bulk RNA-seq of cocultures) could test whether the top genes show the same pattern, but it has the same contamination limitation and unresolved donor mapping.
4. Mechanistic perturbation: MerTK inhibitor or macrophage depletion experiments with FLS-only readout. This requires wet-lab.

## Key references

- [K1] Kuo D et al. HBEGF+ macrophages in rheumatoid arthritis induce fibroblast invasiveness. Sci Transl Med 2019. doi:10.1126/scitranslmed.aau8587 (abstract_only). Supports: directional, state-specific macrophage→fibroblast communication (HBEGF/EGFR).
- [K2] Alivernini S et al. Distinct synovial tissue macrophage subsets regulate inflammation and remission in rheumatoid arthritis. Nat Med 2020. doi:10.1038/s41591-020-0939-8 (abstract_only). Bounds: MerTK-defined macrophage states are biologically meaningful across RA clinical states.
- [K3] Wei K et al. Notch signalling drives synovial fibroblast identity and arthritis pathology. Nature 2020. doi:10.1038/s41586-020-2222-z (abstract_only). Rival: fibroblast-intrinsic NOTCH3 program; known finding, not novel here; NOTCH3 genes absent from the bound 440-gene panel.

## What each outcome would and would not establish

- Supportive: would establish state-specific directionality in the bound coculture system; would NOT establish the ligand (HBEGF vs others) or in vivo relevance without cell-type-resolved data and wet-lab validation.
- Adverse: **observed** — would argue against a macrophage-state-driven FLS imprint on this panel and shift weight to composition-based mechanisms or fibroblast-intrinsic [K3]; would NOT refute macrophage effects measured by other assays.
- Inconclusive: underpowered or confounded; next tests above are the decision rule.

## Alternatives preserved

- D3-M1 (composition vs within-cell): parked — E-MTAB-8322 is macrophage-only pseudobulk; no whole-tissue component in bound data to decompose.
- D3-M3 (persistence vs remission): parked — cross-sectional Rem/Resistant/Naive groups; no longitudinal transitions in bound data.
- NOTCH3 extension: conditional on a dataset/assay that measures the NOTCH3 program (absent from the 440-gene panel).
- Cell-type-resolved re-analysis: requires new data acquisition (snRNA-seq or FACS-sorted FLS); not computable with bound data.
