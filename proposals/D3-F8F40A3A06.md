> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Directional macrophage-to-fibroblast communication in rheumatoid arthritis

## Question

Does macrophage-derived inflammatory signaling causally drive fibroblast activation in rheumatoid arthritis, or is the observed macrophage–fibroblast co-expression pattern better explained by a shared disease state, donor-specific biology, or fibroblast-autonomous activation?

## Clinical importance

Fibroblast activation is central to rheumatoid arthritis (RA) pathogenesis, driving synovial inflammation, cartilage destruction, and bone erosion. Macrophages and fibroblasts communicate bidirectionally in the synovial microenvironment. If a macrophage-conditioned state has a robust, donor-aware fibroblast response, it supports a testable intervention point for macrophage-fibroblast crosstalk. If the signal is donor-specific or absent after paired comparison, it argues against treating observed macrophage-fibroblast co-expression as a directional mechanism.

The clinical consequence is significant: if macrophage-derived inflammatory signaling is a primary driver of fibroblast activation, then targeting macrophage-fibroblast communication could provide a new therapeutic strategy for RA, particularly for the difficult-to-treat subset that fails to respond to conventional DMARDs and biologics.

## Evidence and unresolved claim

The available data can establish whether fibroblast activation markers change after exposure to macrophage-derived inflammatory signals, and whether that response is reproducible across independent donors. The data cannot establish that any single ligand–receptor pair is the sole causal mechanism, because the assays are transcriptomic and do not directly measure ligand secretion, receptor binding, or in vivo cell-cell contact.

The unresolved claim is directional: macrophage-conditioned exposure changes fibroblast state beyond donor and composition effects. Co-expression or a whole-tissue contrast cannot establish this.

## Data bindings (verified from dataset README)

### E-MTAB-8873 (primary donor-aware coculture dataset)
- Source files: `[internal dataset path]`
- Assay: RSEC (RNA-seq on sorted cells), MolsPerCell normalization
- Donors (from file names): SA256A, SA257A, SA258R, SA259A, SA260R, SA263R, SA266A, SA267R, SA277A, SA278R
- Key contrasts (from file names):
  - FLS-only vs FLS+Mpos (macrophage-positive coculture): e.g., R1_SA256A_FLS_only vs R1_SA256A_FLS_SA260R_Mpos
  - FLS+Mpos vs FLS+Mneg (macrophage-negative control): e.g., R1_SA256A_FLS_SA259A_Mpos vs R1_SA256A_FLS_SA259A_Mneg
  - Pre-LPS vs post-LPS macrophage: e.g., R1_SA256A_FLS_SA259A_Mpos_preLPS vs R1_SA256A_FLS_SA259A_Mpos
  - Inhibitor treatment: e.g., R1_SA256A_FLS_SA259A_Mpos_Inhibitor vs R1_SA256A_FLS_SA259A_Mpos
- Donor structure: Each donor (SA256A, SA257A, etc.) has multiple experimental conditions, so donors are nested within conditions. The same donor appears in FLS-only, FLS+Mpos, FLS+Mneg, and inhibitor conditions.
- Design metadata: `E-MTAB-8873.sdrf.txt` (74719 bytes) and `E-MTAB-8873.idf.txt` (9976 bytes)

### E-MTAB-8316 (bulk RNA-seq, rheumatoid arthritis)
- Source files: `[internal dataset path]`
- Assay: MK (microarray), readcountMatrix
- Design metadata: `E-MTAB-8316.sdrf.txt` (18139 bytes) and `E-MTAB-8316.idf.txt` (5464 bytes)
- Use: Context for whole-tissue macrophage–fibroblast co-expression patterns

### GSE95588 (coculture time-course)
- Source files: `[internal dataset path]`
- Assay: HTSeq counts
- Files: `GSE95588_d1d2d3d4_counts.txt.gz` (time-course d1-d4), `GSE95588_coculture_htseq_counts.txt.gz` (coculture)
- Design metadata: `prepared/GSE95588_d1d2d3d4_counts.design.json`, `prepared/GSE95588_coculture_htseq_counts.design.json`
- Use: Temporal dynamics of macrophage–fibroblast communication

## Hypothesis (falsifiable)

**H1 (directional communication):** Macrophage-derived inflammatory signaling (LPS-activated macrophages) causally drives fibroblast activation, as evidenced by a reproducible, donor-independent upregulation of fibroblast activation markers (e.g., COL1A1, COL1A2, FN1, MMP13, IL6) in FLS+Mpos vs FLS-only and FLS+Mneg comparisons across independent donors.

**H2 (shared disease state / donor-specific):** The observed macrophage–fibroblast co-expression pattern is driven by donor-specific biology or a shared disease state, not by directional macrophage-to-fibroblast signaling. This would be supported if the fibroblast response is inconsistent across donors, or if the response is equally strong in FLS+Mneg (macrophage-negative control) as in FLS+Mpos.

**H3 (fibroblast-autonomous activation):** Fibroblast activation is autonomous and not dependent on macrophage signaling. This would be supported if fibroblast activation markers are already elevated in FLS-only samples from RA patients, and the macrophage coculture does not further activate them.

## Donor-aware discriminating test

1. **Primary analysis (E-MTAB-8873):**
   - For each donor, compute the log2 fold-change (FLS+Mpos vs FLS-only) for a predefined set of fibroblast activation markers.
   - Use a donor-aware mixed model: `~ condition + (1|donor)` to account for nested donors.
   - Test whether the condition effect (Mpos vs only) is significant after accounting for donor variability.
   - Compare FLS+Mpos vs FLS+Mneg to isolate the macrophage-specific effect from general coculture effects.

2. **Replication (GSE95588):**
   - Check whether the same fibroblast activation markers show a time-dependent increase in the coculture time-course (d1→d4).
   - This provides an independent dataset for replication.

3. **Context (E-MTAB-8316):**
   - Check whether the same fibroblast activation markers are elevated in RA whole-tissue samples vs healthy controls.
   - This provides disease context but cannot establish directionality.

## Falsification criteria

- **Supportive of H1:** Reproducible upregulation of fibroblast activation markers in FLS+Mpos vs FLS-only and FLS+Mneg across ≥5 independent donors, with a significant condition effect in the donor-aware mixed model.
- **Adverse to H1 (supports H2 or H3):** No reproducible upregulation across donors, or equal response in FLS+Mneg as in FLS+Mpos, or no further activation in FLS+Mpos beyond FLS-only levels.
- **Inconclusive:** Inconsistent results across donors, or insufficient power to detect a condition effect after accounting for donor variability.

## Competing explanations

1. **Donor-specific biology:** Different donors may have different baseline fibroblast activation states, which could confound the condition effect.
2. **Shared disease state:** RA patients may have a shared inflammatory state that drives both macrophage activation and fibroblast activation independently.
3. **Fibroblast-autonomous activation:** Fibroblasts may be activated by factors other than macrophage signaling (e.g., mechanical stress, other cytokines).
4. **Technical artifacts:** Differences in cell sorting efficiency, RNA quality, or normalization could create spurious condition effects.

## Method comparison

- **Simple baseline:** Compare mean expression of fibroblast activation markers in FLS+Mpos vs FLS-only without accounting for donor variability. This is confounded by donor-specific effects and is not a valid test of directional communication.
- **Donor-aware mixed model (selected):** Use a mixed model `~ condition + (1|donor)` to account for nested donors. This is the most appropriate method for this question because it accounts for the nested donor structure and tests the directional hypothesis directly.
- **Learned alternative:** Train a classifier to predict fibroblast activation from macrophage expression profiles. This could reveal which macrophage features are most predictive of fibroblast activation, but it does not test the directional hypothesis and is prone to overfitting with small sample sizes.
- **Mechanistic alternative:** Perturb specific ligand–receptor pairs (e.g., TNF/TNFR, IL-6/IL-6R) and measure fibroblast activation. This would be the strongest test of directional communication, but it requires wet-lab experiments that are not feasible in this computational study.

## Resource estimate

- CPU: 4 cores, 8 GB RAM
- Time: ~2 hours for data loading, preprocessing, and mixed model fitting
- No GPU required

## Key references

### [K1] Bao et al. (2026)
- **Title:** Reduced fibroblast-derived IGFBP5 is associated with pathogenic synovial fibroblast states and altered macrophage polarization in rheumatoid arthritis
- **Authors:** Bao et al.
- **Year:** 2026
- **Work ID:** doi:10.3389/fimmu.2026.1873778
- **Claim:** IGFBP5 expression is reduced in RA synovial fibroblasts, particularly in inflammatory and fibrotic subclusters. IGFBP5 overexpression in vitro attenuated aggressive features of RA synovial fibroblasts and altered macrophage phenotypic and cytokine profiles in coculture.
- **Contribution:** This proposal tests the directional macrophage-to-fibroblast communication hypothesis using a donor-aware mixed model on E-MTAB-8873, which is a more direct test of the directional hypothesis than the in vitro coculture experiments in Bao et al.
- **Limitation:** Bao et al. used in vitro coculture experiments and single-cell RNA sequencing, which cannot establish the donor-aware directional hypothesis in a controlled experimental setting.
- **Locator:** Abstract
- **Inspection:** abstract_only

### [K2] Wei & Xu (2026)
- **Title:** Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal-myeloid crosstalk in the synovium and emerging resolution-restoring therapies
- **Authors:** Wei W, Xu J
- **Year:** 2026
- **Work ID:** doi:10.3389/fimmu.2026.1935792
- **Claim:** Refractory RA is better understood as an active failure of the program meant to end inflammation. Pathological fibroblasts and a macrophage compartment stripped of its pro-resolving, efferocytic subsets both work against resolution. Their reciprocal, largely feed-forward signaling assembles a self-sustaining stromal-myeloid circuit.
- **Contribution:** This proposal provides a concrete, donor-aware test of the directional macrophage-to-fibroblast communication hypothesis, which is a key component of the stromal-myeloid circuit described by Wei & Xu.
- **Limitation:** Wei & Xu is a review article that proposes a framework but does not provide a concrete experimental test of the directional hypothesis.
- **Locator:** Abstract
- **Inspection:** abstract_only

### [K3] Luo et al. (2026)
- **Title:** Extracellular vesicle-mediated immune crosstalk in rheumatoid arthritis synovium: mechanistic insights and translational challenges
- **Authors:** Luo F, Yuan X, Zhou H, Wang Q, Chen C, Ling Y, Zheng J, Yao X, Ma W
- **Year:** 2026
- **Work ID:** doi:10.3389/fimmu.2026.1891984
- **Claim:** Extracellular vesicles (EVs) may contribute to residual disease activity in RA by carrying signals that are not captured by soluble cytokine measurements alone. FLS-derived sEVs promote macrophage migration, and macrophage-derived sEVs drive RA-FLS proliferation and inflammatory responses through transfer of miRNA cargo.
- **Contribution:** This proposal tests the directional macrophage-to-fibroblast communication hypothesis using a donor-aware mixed model on E-MTAB-8873, which is a more direct test of the directional hypothesis than the EV-mediated communication described by Luo et al.
- **Limitation:** Luo et al. is a mini-review that examines EV-mediated communication in RA, but it does not provide a concrete experimental test of the directional hypothesis.
- **Locator:** Abstract
- **Inspection:** abstract_only
