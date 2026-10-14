> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# JAK inhibitor context-dependent transcript response: managed execution reveals the discovery-level signal does not survive FDR correction

## Seed
D2-T1 (Context-specific intervention response)

## Domain
Therapeutic Target Prioritization

## Parent
[prior hypothesis] (Fibroblast presence modulates JAK inhibitor transcript response in synovial macrophage cocultures)

## Type
new_evidence child of [prior hypothesis]. This child EXECUTES the parent's analysis plan as a managed compute job and reports the results. The parent was a discovery-level candidate; this child converts it into an evidence-bearing result.

## Question (unchanged from parent)
Does the transcript response to the JAK inhibitor A77 in synovial tissue cocultures depend on the presence of fibroblast-like synoviocytes (FLS), as measured by the difference in drug response between macrophage+T cell (MT) and macrophage+T cell+FLS (MTF) contexts? Specifically, do JAK/STAT pathway genes show attenuated drug response in the presence of fibroblasts?

## What this execution found (EXECUTED this episode)

### Classification: INCONCLUSIVE
The pre-specified falsification criteria are evaluated as follows:
- **0 JAK/STAT core genes** (JAK1, JAK2, JAK3, TYK2, STAT1-5B, SOCS1, SOCS3) reach FDR<0.1
- **1 broad JAK-STAT gene** (EPO) reaches FDR<0.1, but this is a data artifact (Infinity t-stat from zero-variance counts)
- **3 direction-consistent genes** (JAK1, STAT1, STAT4) show the same sign across all 3 donors, but none reach FDR<0.1
- **E-MTAB-8316 validation**: 0 overlap between top-50 GSE95588 context-dependent genes and the E-MTAB-8316 panel (58,302 features)

### Key results
1. **Genome-wide context effect is real**: All 3 donors show highly significant positive mean attenuation (P1: 0.086, p=1.8e-78; P2: 0.182, p=3.2e-75; P3: 0.447, p<1e-300). The MTF context does produce a different transcript response than MT for A77.
2. **But the effect is NOT JAK/STAT-specific**: The parent's discovery-level evidence (JAK1 p=0.007, TYK2 p=0.014, STAT5A p=0.014) was computed without FDR correction. Under BH FDR correction across 23,710 genes, NO JAK/STAT core gene reaches FDR<0.1. JAK1 p=0.196, TYK2 p=0.282, STAT5A p=0.495.
3. **Direction consistency is limited**: JAK1 is positive in all 3 donors (0.61, 0.04, 1.10), STAT1 is positive in all 3 (0.15, 0.14, 0.32), STAT4 is negative in all 3 (-1.35, -0.08, -1.59). But TYK2 is mixed (0.33, -0.02, 0.98) and STAT5A is mixed (0.19, -0.23, 0.69).
4. **Top context-dependent genes are NOT JAK/STAT**: A2ML1 (t=6.89, p=0.02), AFG3L1P (t=5.83), ABCB6 (t=4.60) - all FDR=1.0. These are not JAK/STAT pathway genes.
5. **E-MTAB-8316 validation is empty**: The 445-gene targeted panel (actually 58,302 features in the prepared data) has 0 overlap with the top-50 GSE95588 context-dependent genes. Cross-dataset validation is not possible.

### Comparison with parent's discovery-level evidence
The parent reported JAK1 (p=0.007), TYK2 (p=0.014), STAT5A (p=0.014) as "significantly attenuated in MTF." These p-values were from uncorrected per-gene t-tests. Under proper BH FDR correction across 23,710 genes, none of these survive. This is consistent with the auranofin correction ([prior hypothesis]), which showed that the auranofin-specific MTF-context attenuation was also not reproducible. The pattern is: bulk context effects are real (genome-wide) but not pathway-specific.

## Clinical importance
JAK inhibitors (tofacitinib, baricitinib, upadacitinib) are approved for RA but ~40% of patients respond inadequately. The hypothesis that fibroblast presence attenuates JAK inhibitor response at the transcriptional level would provide a mechanistic explanation for this resistance and suggest combination therapies targeting both macrophage and fibroblast arms. The INCONCLUSIVE result means this specific mechanistic claim (JAK/STAT pathway-specific attenuation) is NOT supported by the available data. The broader context effect (genome-wide) is real but does not nominate a specific therapeutic target.

## Data Bindings
- **Primary dataset**: GSE95588_d1d2d3d4_counts
  - Path: `[internal dataset path]` ([source checksum])
  - Design: `[internal dataset path]` ([source checksum])
  - Feature map: `[internal dataset path]` ([source checksum])
  - 23,710 genes x 70 samples, 3 donors with A77 data (P1, P2, P3)
  - A77 samples: P1_MT_A77, P1_MTF_A77, P2_MT_A77, P2_MTF_A77, P3_MT_A77, P3_MTF_A77
  - Vehicle controls: P1_MT_3, P1_MTF_3, P2_MT_3, P2_MTF_3, P3_MT_3, P3_MTF_3

- **Validation dataset**: E-MTAB-8316
  - Path: `[internal dataset path]` ([source checksum])
  - Design: `[internal dataset path]` ([source checksum])
  - 58,302 features x 12 samples, 4 FLS donors
  - 0 overlap with top-50 GSE95588 context-dependent genes

## Analysis (executed)
1. Load GSE95588_d1d2d3d4 counts (23,710 genes x 70 samples)
2. Identify A77 drug samples and vehicle controls for P1, P2, P3
3. Per-gene log2FC: log2((drug+1)/(vehicle+1)) for MTF and MT contexts
4. Context-dependent attenuation = MTF_log2FC - MT_log2FC
5. Per-donor one-sample t-test on attenuation vs 0
6. Pooled per-gene paired t-test (n=3 donors), BH FDR correction
7. JAK/STAT core (12 genes) and broad (35+ genes) pathway analysis
8. E-MTAB-8316 cross-dataset validation (0 overlap)

## Falsification Criteria (pre-specified, unchanged from parent)
- **Supportive**: >=5 JAK/STAT core genes FDR<0.1 AND direction-consistent across all 3 donors
- **Adverse**: No JAK/STAT pathway genes FDR<0.1
- **Inconclusive**: <2 donors OR FDR eliminates all significance

**Result: INCONCLUSIVE** (0 JAK/STAT core FDR<0.1, 1 broad FDR<0.1 [artifact], 3 direction-consistent but none FDR<0.1)

## Limitations
1. Donor identity unresolved (column labels P1-P3 used, not verified from GSM metadata)
2. Bulk RNA-seq: cannot separate cell-type-specific effects
3. n=3 donors: low power for per-gene inference (FDR correction across 23,710 genes is very stringent)
4. Vehicle control is unstimulated (not stimulated+vehicle)
5. P4 has no drug treatments (excluded)
6. E-MTAB-8316 has 0 overlap with top GSE95588 genes (validation not possible)
7. The EPO "significant" result is a data artifact (zero variance in counts)

## Residual open question
The genome-wide context effect is real (p<1e-75) but not JAK/STAT-specific. The next test would be: (1) single-cell RNA-seq of the same coculture system to separate macrophage vs fibroblast transcriptional responses, or (2) a larger donor cohort (n>=10) to increase power for per-gene FDR. The current data cannot distinguish between "fibroblasts broadly buffer drug response" (genome-wide effect) and "fibroblasts specifically compensate for JAK inhibition" (pathway-specific effect).

## Key References
- [K1] Kuo D, et al. HBEGF+ macrophages in rheumatoid arthritis induce fibroblast invasiveness. Sci Transl Med. 2019;11(491):eaau8587. DOI: 10.1126/scitranslmed.aau8587. (Source of GSE95588; shows drug responses depend on cellular context)
- [K2] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal-myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026;17:1935792. DOI: 10.3389/fimmu.2026.1935792. (Proposes stromal-myeloid circuit as basis for therapeutic resistance)
- [K3] Pascual-García S, et al. Fibroblast-like Synoviocytes as Therapeutic Targets in Rheumatoid Arthritis: Current Evidence on DMARD-Mediated Modulation. Biomedicines. 2026;14(8):1784. DOI: 10.3390/biomedicines14081784. (Reviews JAK inhibitor effects on FLS; shows fibroblasts are active participants in drug response)
