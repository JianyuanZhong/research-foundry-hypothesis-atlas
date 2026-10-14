> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Condition-Level Regulation Dominates Macrophage Inflammatory Gene Expression Variance in RA Coculture: Executed Variance Partitioning on GSE95588

## Seed
D3-M1 (Composition versus within-cell regulation)

## Domain
Disease Mechanisms & Pathway Hypotheses

## Parent
[prior hypothesis] (PLANNED, mu 29.40, valid, refs complete)

## Question
In the GSE95588 macrophage-fibroblast coculture drug screen (4 patients × M/MT/MTF × ~13 drugs, 70 samples, 23,710 genes), is patient-level composition (donor effect) the dominant source of variance in macrophage inflammatory gene expression, or is condition/drug-level (within-cell, shared) regulation dominant?

## Hypothesis (from parent, now tested)
The parent hypothesized that patient-level composition (donor effect) explains a larger fraction of variance than condition-specific drug responses for the core inflammatory gene set. **This hypothesis is NOT supported by the executed analysis.**

## EXECUTED RESULTS

### Analysis performed
- **Job**: [research job] (succeeded, 12.6s, 8 CPUs, 64 GiB)
- **Data**: GSE95588_d1d2d3d4 (70 samples, 23,710 genes → 14,207 after filtering)
- **Normalization**: log1p(raw counts)
- **Gene filter**: count > 10 in ≥ 4 samples
- **Methods**: One-way ANOVA (patient factor, condition factor), set-level permutation test for patient × drug interaction (N=1000), sensitivity analyses

### Primary result: Condition-level regulation dominates

| Metric | Genome-wide (14,207) | Core inflammatory (63) |
|--------|---------------------|----------------------|
| η²_patient (mean) | 0.1282 | 0.1296 |
| η²_condition (mean) | 0.1391 | **0.2495** |
| Patient > Condition | 48.9% | **33.3%** |
| η²_patient (median) | 0.0949 | 0.0967 |
| η²_condition (median) | 0.0998 | **0.2072** |

**Key finding**: For the core inflammatory gene set, condition-level regulation explains ~2× more variance than patient-level composition (η²_condition = 0.2495 vs η²_patient = 0.1296). Only 33.3% of core inflammatory genes show patient > condition variance, well below the 60% threshold for supportive evidence.

### Per-pathway breakdown (core inflammatory genes)

| Pathway | n | η²_patient | η²_condition | P>C % |
|---------|---|-----------|-------------|-------|
| NF-κB | 8 | 0.098 | **0.339** | 12.5% |
| Chemokines | 10 | 0.091 | **0.324** | 10% |
| TNF pathway | 5 | 0.125 | **0.260** | 40% |
| IL-6 pathway | 5 | 0.118 | **0.249** | 40% |
| Interferon | 10 | 0.095 | **0.228** | 20% |
| Proinflammatory cytokines | 7 | 0.140 | 0.221 | 57.1% |
| Macrophage activation | 10 | 0.144 | 0.160 | 50% |
| Antigen presentation | 8 | **0.237** | 0.225 | 50% |

**Pattern**: Condition-level regulation dominates in all canonical inflammatory signaling pathways (NF-κB, chemokines, TNF, IL-6, IFN). Patient-level variance is relatively higher in antigen presentation (HLA genes) and macrophage activation markers, consistent with the idea that these reflect baseline cellular identity rather than drug-responsive signaling.

### Patient × drug interaction (permutation test, N=1000)

10 drugs tested (shared across ≥2 patients). **1/10 significant** at p<0.05:

| Drug | Patients | n | F | p_perm | Sig |
|------|----------|---|---|--------|-----|
| Triple (MTX+HCQ+SSZ) | P1,P2,P3 | 6 | 121.3 | **0.041** | ✓ |
| A77 (TNFi) | P1,P2,P3 | 6 | 19.9 | 0.063 | |
| Nap (NSAID) | P1,P2,P3 | 5 | 49.3 | 0.068 | |
| Aur (Auranofin) | P1,P2,P3 | 6 | 35.2 | 0.181 | |
| GW (TGFβRII) | P1,P2,P3 | 6 | 3.8 | 0.275 | |
| aIL6 (anti-IL6) | P1,P2 | 4 | 21.3 | 0.296 | |
| Hy (HCQ) | P1,P2 | 4 | 5.7 | 0.324 | |
| Dic (NSAID) | P1,P2 | 4 | 3.1 | 0.313 | |
| AG (Abatacept) | P2,P3 | 4 | 11.4 | 0.345 | |
| Dex (Dex) | P1,P2 | 4 | 69.4 | 0.352 | |

**Interpretation**: Drug responses are largely consistent across patients. The one significant interaction (Triple therapy) shows P2 responding negatively (mean response = -0.57) while P1 and P3 respond positively, suggesting a specific patient-drug incompatibility for combination DMARDs. A77 (TNF inhibitor) and Naproxen show borderline interactions (p≈0.06-0.07), suggesting modest patient-specificity for these agents but insufficient power to confirm.

### Sensitivity analyses

- **Exclude P4** (no drugs, n=3): Core η²_patient = 0.1084, η²_condition = 0.2197. Direction unchanged; condition still dominates.
- **Leave-one-patient-out** (core genes): η²_patient ranges 0.0995 (excl. P1) to 0.1312 (excl. P3). No single patient drives the result.
- **Genome-wide (no P4, 500-gene sample)**: η²_patient = 0.1092, η²_condition = 0.1234. At the genome-wide level, patient and condition effects are comparable, but the core inflammatory set shows the condition effect more clearly.

### Mixed-effects model
The linear mixed-effects model (patient random + condition fixed) failed to converge for all genes due to singular random effects covariance (expected with only 4 patients and no technical replicates). The ANOVA-based η² estimates are the primary evidence. The ICC could not be estimated, which limits the strength of the patient-effect conclusion.

## Falsification Assessment

### Verdict: ADVERSE to patient-composition-dominates hypothesis

The parent's hypothesis predicted:
- η²_patient > η²_condition for >60% of core inflammatory genes → **Observed: 33.3%** (ADVERSE)
- ICC > 0.4 → **Not estimable** (model convergence failure)
- Significant patient × drug interaction → **1/10 significant** (weak, borderline)

The observed pattern is consistent with **condition/drug-level regulation dominating** macrophage inflammatory gene expression variance:
- Condition η² is ~2× patient η² for core inflammatory genes
- The dominance is consistent across all canonical inflammatory pathways
- Drug responses are largely consistent across patients (low interaction)
- The result is stable to exclusion of any single patient

### What this means
1. **Drug-target pathway regulation is the dominant source of variance** in macrophage inflammatory gene expression in this coculture system. The same drug produces similar transcriptional effects across different patients' macrophages.
2. **Patient-level composition contributes modestly** (~13% of variance) and is more prominent in antigen presentation (HLA) and macrophage activation markers, suggesting these reflect baseline cellular identity rather than drug-responsive signaling.
3. **Clinical implication**: A "one-size-fits-all" drug selection strategy based on target pathway may be more effective than patient-state-based personalization for the core inflammatory response. However, the one significant interaction (Triple therapy) and borderline results for A77/Nap suggest that some patients may have specific drug incompatibilities.
4. **Limitation**: This is a stimulated system (all conditions include TNF 20 ng/mL). The variance partitioning reflects drug effects on top of TNF stimulation, not resting-state differences. The 4-patient design limits statistical power for interaction tests.

## Data Binding (verified)

### Primary dataset
- **Counts**: `[internal dataset path]`
  - [source checksum]
  - Format: TSV, 23,710 genes × 70 samples, HTSeq raw counts
- **Design**: `[internal dataset path]`
  - [source checksum]
  - 70 entries, patient labels P1-P4 (25/27/15/3 samples)
- **Feature map**: `[internal dataset path]`
  - 23,710 entries, gene symbols preserved

### Sample structure
| Patient | M | MT | MTF | MTF drugs | MT drugs | Total |
|---------|---|----|----|-----------|----------|-------|
| P1 | 1 | 1 | 1 | 11 | 11 | 25 |
| P2 | 1 | 1 | 1 | 12 | 12 | 27 |
| P3 | 1 | 1 | 1 | 6 | 6 | 15 |
| P4 | 1 | 1 | 1 | 0 | 0 | 3 |

Drug abbreviations: 3=Triple(MTX+HCQ+SSZ), A77=A77 1726 (TNFi), AG=Abatacept, Aur=Auranofin, Dex=Dexamethasone, Dic=Diclofenac, GW=GW9662 (TGFβRII), Hy=Hydroxychloroquine, Meth=Methotrexate, Nap=Naproxen, Sul=Sulfasalazine, Tof=Tofacitinib (JAK1/3i), aIL6=anti-IL6

## Competing Explanations

1. **Within-cell regulation dominates** (SUPPORTED): Consistent drug-responsive pathways across patients. Observed: high condition η², low patient×drug interaction. ✓
2. **Patient-drug interaction**: Specific patient-drug combinations drive variance. Partially supported: 1/10 significant (Triple), 2 borderline (A77, Nap). Not the dominant pattern.
3. **Technical/batch confounding**: Library preparation or sequencing batch effects confound patient effects. Not directly testable without batch information, but the leave-one-patient-out stability argues against a single outlier driving the result.
4. **FLS cell line differences**: FLS from different patients have different activation potential. The MTF vs MT difference could vary by patient. However, the condition factor includes both MT and MTF, so FLS effects are partially captured in the condition variance. The M (macrophage-only) baseline (n=4) cannot be used to separate FLS from macrophage effects.
5. **TNF stimulation confound**: All conditions include TNF 20 ng/mL. The variance partitioning reflects drug effects on top of TNF stimulation. If resting-state variance were measured, the patient vs condition balance might differ.

## Limitations

1. **Small n (4 patients)**: No technical replicates. Statistical power for interaction tests is very limited (2-6 samples per drug). ICC not estimable (mixed model convergence failure).
2. **Unresolved donor identity**: design.json has donor_status="unresolved". Patient labels (P1-P4) are used as the unit, but cannot verify that P1 macrophages and P1 FLS are from the same patient.
3. **FLS are cell lines**: Not primary FLS. Cell line behavior may differ from primary tissue.
4. **All conditions include TNF**: Stimulated system. Variance partitioning reflects drug effects on top of TNF stimulation.
5. **No independent validation**: GSE95588 coculture r1/r2 includes earlier GSE57723 data.
6. **Cross-sectional**: No longitudinal data.
7. **Core gene set is predefined**: Not derived from the data. May miss important inflammatory genes not in the predefined list.

## Method Exploration

- **Baseline**: Per-gene one-way ANOVA (patient/condition as factor) → η². Simple, interpretable, no distributional assumptions beyond ANOVA.
- **Alternative**: Linear mixed-effects model with patient as random effect → ICC. Properly accounts for nested design. **Failed** due to convergence (4 patients, singular covariance).
- **What the alternative would have revealed**: A direct ICC estimate with confidence intervals. The ANOVA η² is a reasonable proxy but does not separate patient variance from residual in the same way.
- **Interaction test**: Permutation test (N=1000) on set-level drug response. Appropriate for small n. Limited power with 2-6 samples per drug.

## Key References

### [K1] Kuo D, Ding J, Cohn IS, et al. (2019)
**HBEGF+ macrophages in rheumatoid arthritis induce fibroblast invasiveness.**
Sci Transl Med 11(491):eaau8587. DOI: 10.1126/scitranslmed.aau8587. PMID: 31068444.
- **Claim supported**: Macrophage-fibroblast coculture in RA shows that different drugs redirect macrophages into different states; most RA medications target HBEGF+ inflammatory macrophages, but in some cases redirect them into unexpected states. Patient-level heterogeneity in drug response is observed but not quantified.
- **Contribution of this work**: This proposal performs variance partitioning to quantify the relative contribution of patient vs. drug effects, which Kuo et al. described qualitatively but did not decompose statistically. The executed analysis shows that condition/drug-level regulation dominates, consistent with Kuo et al.'s observation that drugs produce consistent macrophage state changes.
- **Limitation**: Kuo et al. used single-cell RNA-seq on synovial tissue; this proposal uses bulk RNA-seq on coculture. The patient-level variance structure may differ between these systems.
- **Inspection**: Abstract only (Europe PMC metadata). Full text not accessed.

### [K2] Chatterjee P, Stevens HY, Kippner LE, et al. (2026)
**Single-cell transcriptomics of multi-site cell therapy in osteoarthritis: Tissue-specific treatment correlations.**
Mol Ther Nucleic Acids 37(1):102839. DOI: 10.1016/j.omtn.2026.102839. PMID: 41717289.
- **Claim supported**: Variance partitioning in a cell therapy context revealed that patient heterogeneity can mask treatment effects; site-specific variability was significant in BMAC but not SVF.
- **Contribution of this work**: This proposal applies the same variance partitioning framework to bulk RNA-seq in RA macrophage-fibroblast coculture, a different disease and assay system. The finding that condition-level regulation dominates (opposite to the "patient heterogeneity masks treatment" narrative) suggests that the balance between patient and treatment effects is system-specific.
- **Limitation**: Chatterjee et al. used single-cell RNA-seq with tensor decomposition in osteoarthritis; this proposal uses bulk RNA-seq with ANOVA in RA. The variance structure may differ between single-cell and bulk data.
- **Inspection**: Abstract only (Europe PMC metadata). Full text not accessed.

### [K3] Meng S, Xing F, Luo Y, et al. (2026)
**Signaling Pathway-Biomarker Coupling for Precision Therapy in Rheumatoid Arthritis: Mechanistic Insights, Translational Bottlenecks, and Emerging Strategies.**
ACR Open Rheumatol 8(8):e90136. DOI: 10.1002/acr2.90136. PMID: 42634942.
- **Claim supported**: RA is heterogeneous; failure of biomarker-driven trials stems from treating RA as a single entity rather than a spectrum of pathway-dominant endotypes. JAK/STAT, MAPK, and other pathways show direct coupling to specific biomarkers.
- **Contribution of this work**: This proposal provides quantitative evidence that, in a controlled coculture system, pathway-level drug regulation dominates over patient-level composition for core inflammatory genes. This supports the pathway-guided treatment framework but suggests that patient-state-based personalization may be less important than target-pathway matching for the core inflammatory response.
- **Limitation**: Meng et al. is a review, not an experimental study. It does not provide direct evidence for the variance partitioning hypothesis.
- **Inspection**: Abstract only (Europe PMC metadata). Full text not accessed.

## Bibliography
1. Kuo D, et al. HBEGF+ macrophages in rheumatoid arthritis induce fibroblast invasiveness. Sci Transl Med. 2019;11(491):eaau8587.
2. Chatterjee P, et al. Single-cell transcriptomics of multi-site cell therapy in osteoarthritis. Mol Ther Nucleic Acids. 2026;37(1):102839.
3. Meng S, et al. Signaling Pathway-Biomarker Coupling for Precision Therapy in Rheumatoid Arthritis. ACR Open Rheumatol. 2026;8(8):e90136.

## Expert Questions
1. Is the patient label (P1-P4) a reliable proxy for donor identity, given that donor_status is "unresolved"?
2. Should the variance partitioning be restricted to the MTF (coculture) conditions only, or include all conditions? (This analysis included all conditions.)
3. Is the core inflammatory gene set appropriate, or should it be defined differently (e.g., based on Kuo et al.'s HBEGF+ macrophage signature)?
4. Given the small n (4 patients), what is the minimum detectable ICC with 80% power? (Not estimable in this analysis.)
5. Does the finding that condition-level regulation dominates in bulk RNA-seq coculture extend to single-cell RNA-seq in primary synovial tissue?

## What Would Strengthen the Result
1. **More patients** (n≥10): Would enable ICC estimation and increase power for interaction tests.
2. **Technical replicates**: Would separate biological from technical variance.
3. **Resting-state samples** (no TNF): Would separate drug effects from TNF-stimulation effects.
4. **Primary FLS** (not cell lines): Would test whether FLS cell line differences drive the condition effect.
5. **Independent validation** in a second RA cohort: Would confirm that the condition-dominance pattern is generalizable.
