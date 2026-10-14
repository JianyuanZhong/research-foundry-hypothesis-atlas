> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Full-Transcriptome MerTK Inhibitor Analysis in FLS-Macrophage Co-culture: Executed Null Result

## Seed
D3-M2 (Directional cell communication) — execution of [prior hypothesis]

## Domain
Disease Mechanisms & Pathway Hypotheses

## Question
Does UNC106238 (MerTK inhibitor, 250 μM) suppress the LPS-induced inflammatory transcriptional program in the FLS-macrophage co-culture system, and is the effect donor-consistent? Does the full transcriptome (58,302 genes) reveal effects invisible to the 445-gene targeted panel (E-MTAB-8873)?

## Scientific opening
The parent candidate ([prior hypothesis]) proposed that MerTK-positive macrophages activate FLS through a MerTK-dependent pathway [K1]. The full-transcriptome dataset (E-MTAB-8316, 58,302 genes, 12 samples) from the same experimental system was PLANNED but never executed (candidate-5111ae26). This analysis executes that planned experiment, providing the first full-transcriptome test of the MerTK inhibitor hypothesis in this co-culture system.

The unresolved question: does the MerTK inhibitor have ANY detectable transcriptomic effect in the full transcriptome, given that the targeted panel showed null results for the Mpos effect (ep12/ep13/ep14)?

## Hypothesis (as planned, now tested)
UNC106238 reduces FLS activation in a MerTK-dependent manner [K1][K3], with:
1. Concordant core response between assays
2. Novel pathway effects invisible to the 445-gene panel
3. Donor consistency (≥4/6 pairs)

## EXECUTED RESULTS ([research job])

### Primary analysis: Paired Wilcoxon signed-rank test (6 pairs, 58,302 genes)
- **0 genes with BH FDR < 0.05**
- **0 genes with BH FDR < 0.10**
- Mean log2FC across all genes: **-0.0103** (essentially zero)
- Median log2FC: 0.0000
- 7,813 genes with |mean log2FC| > 0.5 (13.4% of transcriptome)
- 1,629 genes with |mean log2FC| > 1.0; 116 genes with |mean log2FC| > 2.0

### Donor consistency
- 601 genes: all 6/6 pairs up; 945 genes: all 6/6 pairs down
- 5,518 genes: 5/6 pairs same direction
- 4,252 genes: consistent across all 4 FLS donors
- **None statistically significant after BH correction**

### Key genes (5/33 verified in matrix)
- IL6: mean log2FC = +1.04 (up), not significant
- AXL: mean log2FC = -0.08 (slight down), not significant
- GAPDH: mean log2FC = -0.23 (down), p=0.078 (housekeeping)

### Pathway analysis
- No pathway-level effects detected (limited by gene set coverage)
- Housekeeping: mean log2FC = -0.19, p = 0.078 (marginal)

### Cross-assay comparison (E-MTAB-8316 vs E-MTAB-8873)
- 2 paired Mpos vs Mpos_Inhibitor comparisons in E-MTAB-8873
- **IL6: DISCORDANT** (8316: +1.04 up vs 8873: -1.34 down)
- AXL, GAPDH: concordant (both slightly down)
- Discordance likely driven by different donors and co-culture conditions

## Interpretation

### NULL result for the primary hypothesis
The full transcriptome shows **no statistically significant effect** of UNC106238 on the transcriptional program. The mean effect across 58,302 genes is essentially zero. No gene passes multiple-testing correction.

### What this means
1. The MerTK inhibitor does not produce a detectable transcriptomic effect in this system (healthy monocyte-derived macrophages, transwell, LPS-stimulated, 48h) [K2]
2. Consistent with targeted panel null results (ep12/ep13/ep14)
3. The full transcriptome does NOT reveal hidden effects — because there are no significant effects in either assay
4. The null is consistent with the complexity of MerTK biology as a resolution receptor [K3]

### Competing explanations for the null
1. **Healthy monocyte donors** (not RA synovial macrophages) may not engage MerTK-dependent signaling [K2]
2. **Transwell co-culture** excludes contact-dependent MerTK interactions [K2]
3. **LPS pre-stimulation timing** (4h) and **UNC106238 duration** (last 2h of 48h) may be insufficient
4. **Small sample size** (6 pairs) limits power
5. **RNA-seq measures FLS transcriptome**, not macrophage; indirect effects may be diluted
6. **Different donors between assays** confound cross-assay comparison

## Falsification criteria
- **Supportive**: ≥70% concordance; ≥3 novel pathways; ≥4/6 pairs consistent → **NOT MET**
- **Adverse**: <50% concordance; OR no significant effect; OR no novel pathways → **PARTIALLY MET** (no significant effect, no novel pathways)
- **Inconclusive**: Insufficient power; conflicting donors; different donors → **PARTIALLY MET** (small n, different donors)

**Verdict: Most consistent with ADVERSE (no significant effect) with elements of INCONCLUSIVE.**

## What would change the next decision
- **If null confirmed** with RA synovial macrophages and direct co-culture: MerTK-dependent FLS activation hypothesis not supported; consider alternative mechanisms
- **If positive** with RA macrophages: healthy donor limitation is key confound
- **If null persists** across all systems: inhibitor may not be effective at tested dose/duration

## Limitations
1. Small sample size: 6 pairs, 4 FLS donors, 6 monocyte donors
2. Healthy monocyte donors (not RA synovial macrophages) [K2]
3. Transwell co-culture (no direct contact) [K2]
4. Single compound, single dose (UNC106238 250 μM)
5. Different FLS donors between assays
6. No FLS-only control
7. ENSG ID mapping: only 5/33 key genes verified
8. Cross-sectional (48h single time point)
9. Cell type ambiguity (FLS vs macrophage) unresolved [K2]

## Key references
- [K1] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026;17:1935792. doi:10.3389/fimmu.2026.1935792
- [K2] BioStudies E-MTAB-8316: Sequencing of synovial tissue fibroblasts from Rheumatoid Arthritis patients that were co-cultured with inflammatory macrophages. ArrayExpress. 2020. https://www.ebi.ac.uk/biostudies/studies/E-MTAB-8316
- [K3] Mosallanejad K, Hubeau C, Schwartz Sterman A, Tan Y. Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies. Cells. 2026;15(15):1412. doi:10.3390/cells15151412
