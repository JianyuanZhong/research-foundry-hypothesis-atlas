> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Macrophage metabolic reprogramming distinguishes treatment-resistant from remission rheumatoid arthritis

## Seed
D3-M3 (Persistence versus remission)

## Domain
Disease Mechanisms & Pathway Hypotheses

## Question
In rheumatoid arthritis synovial macrophages, is the persistent pro-inflammatory state in treatment-resistant disease driven by a specific metabolic reprogramming program (glycolytic shift, HIF-1α activation, oxidative phosphorylation suppression) that is quantitatively distinct from the metabolic state in remission, beyond what can be explained by simple inflammatory activation?

## Hypothesis
Treatment-resistant RA macrophages exhibit a distinct glycolytic/HIF-1α metabolic program that is not simply a scaled version of the inflammatory state in remission or naive RA. Specifically:
1. Resistant RA macrophages show upregulation of glycolytic genes (HK2, LDHA, PKM, PFKL, GPI) and HIF-1α target genes (VEGFA, PDK1, ENO1) relative to remission RA macrophages.
2. This metabolic signature is independent of the inflammatory cytokine signature (IL6, TNF, IL1B, CCL2, CXCL8): the metabolic and inflammatory programs are partially separable.
3. Remission RA macrophages show a relative shift toward oxidative phosphorylation (MT-ND genes, SUCLA2, UQCRH) and fatty acid oxidation (CPT1A, ACADL) compared to resistant RA.

The key discriminative test: if the metabolic program in resistant RA is merely proportional to inflammatory activation (i.e., resistant = more of the same), then the metabolic/inflammatory ratio should be similar across groups. If resistant RA has a distinct metabolic program, the ratio will differ.

## Clinical importance
Approximately 30% of RA patients fail to achieve remission on current DMARDs and biologics [K1]. The "difficult-to-treat" phenotype is defined by the EULAR, and understanding its mechanism is critical for developing new therapeutic strategies [K1]. Macrophage metabolic reprogramming has been identified as a key driver of RA pathogenesis, with glycolytic shift and HIF-1α activation promoting IL-1β production and sustained inflammation [K2, K3]. If treatment-resistant RA macrophages have a distinct metabolic program, this would:
1. Identify a mechanistic target for converting resistant to remission (e.g., metabolic inhibitors)
2. Provide a biomarker for predicting treatment response
3. Explain why anti-inflammatory therapies alone fail in resistant disease (the metabolic program is self-sustaining)

## Data
- **E-MTAB-8322** (macrophage pseudobulk, 27 samples, 33694 genes):
  - Remission RA: 7 donors (RemSA132, RemSA160, RemSA161, RemSA174, SA159, SA168, SA225)
  - Resistant RA: 6 donors (ResistantSA144, ResistantSA145, ResistantSA151, ResistantSA166, SA222, SA227)
  - Naive RA: 6 donors (SA131, SA138, SA146, SA172, SA139, SA220)
  - Healthy control: 4 donors (HC0547, HC0572, HC0701, HC0732)
  - Undifferentiated arthritis: 4 donors (SA149P, SA154, UPASA149, UPASA153)
  - All macrophages from synovial membrane
  - SA149/SA149P relatedness unresolved; excluded from independent-donor screens

## Methods

### Baseline: Pathway-level comparison (donor-aware)
1. For each gene, compute the log2 fold change between resistant and remission RA (donor-level)
2. Define gene sets:
   - Glycolysis: HK2, LDHA, PKM, PFKL, GPI, ALDOA, ENO1, PDK1, VEGFA, HIF1A
   - Oxidative phosphorylation: MT-ND1-6, MT-CO1-3, SUCLA2, UQCRH, NDUFA1, COX7A2
   - Fatty acid oxidation: CPT1A, ACADL, ACADM, ACADVL, HADHA, HADHB
   - Inflammatory: IL6, TNF, IL1B, CCL2, CXCL8, IL10, TGFB1
   - HIF-1α targets: VEGFA, PDK1, ENO1, ALDOC, LDHA, MMP9, CA9
3. For each pathway, compute the mean expression in resistant vs remission (donor-level)
4. Test the difference using Wilcoxon rank-sum test (donor-level, n=6 vs n=7)
5. Compute the metabolic/inflammatory ratio: (mean glycolysis score) / (mean inflammatory score) for each donor
6. Compare the ratio between resistant and remission

### Alternative: Machine learning classifier
1. Fit a regularized logistic regression (L1 penalty) to classify resistant vs remission
2. Features: all 33694 genes (log-normalized)
3. Cross-validation: leave-one-donor-out (13 donors total)
4. Evaluate: AUC, accuracy, and feature importance
5. Compare with a baseline classifier using only inflammatory genes
6. If the full model outperforms the inflammatory-only model, the metabolic program adds discriminative information

### Key comparisons
- Resistant vs Remission (primary)
- Resistant vs Naive (secondary: is resistance a distinct state or just more disease?)
- Remission vs Healthy (tertiary: does remission normalize?)
- Metabolic/inflammatory ratio across groups

## Falsification criteria
- **Supportive**: Resistant RA shows significantly higher glycolytic/HIF-1α program than remission, and the metabolic/inflammatory ratio differs between groups. The ML classifier using all genes outperforms the inflammatory-only classifier.
- **Adverse**: No significant metabolic difference between resistant and remission, or the metabolic difference is fully explained by the inflammatory difference (ratio is similar). The ML classifier shows no improvement over inflammatory-only.
- **Inconclusive**: Small sample size (n=6-7) leads to wide confidence intervals, or the metabolic and inflammatory programs are too correlated to separate.

## Limitations
- Cross-sectional design: cannot establish longitudinal transitions from resistant to remission
- Pseudobulk macrophage data: not single-cell, so cell-type composition effects are not separated
- Small sample size: 6 resistant + 7 remission donors
- No treatment history data: don't know which specific drugs each patient received
- No clinical outcome data: don't know if "resistant" patients eventually achieved remission
- SA149/SA149P relatedness: excluded from analysis

## Next steps
1. Perform the baseline pathway-level comparison
2. Fit the ML classifier with leave-one-donor-out CV
3. Identify genes that are specifically associated with the metabolic program
4. Propose a follow-up experiment with single-cell RNA-seq and more donors
5. Test whether metabolic inhibitors (e.g., 2-DG, metformin) can convert resistant macrophage phenotype in vitro

## Key references
- [K1] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026;17:1935792. doi:10.3389/fimmu.2026.1935792
- [K2] Liu X, Wang J, Lou T, Tang Q, Fang Z, Zhang W, Hu Y. Immunometabolism in rheumatoid arthritis: mechanisms, biomarkers, and the path to precision medicine. Front Immunol. 2026;17:1691946. doi:10.3389/fimmu.2026.1691946
- [K3] Jia Y, Li R, Huang L, Wu X, Zhao L, Yang H, You X, Fei Y. The Glycolysis-HIF-1α axis induces IL-1β of macrophages in rheumatoid arthritis. Arthritis Res Ther. 2025;27:180. doi:10.1186/s13075-025-03647-z
