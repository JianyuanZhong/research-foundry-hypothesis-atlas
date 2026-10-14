> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal (episode 12): Is the macrophage->FLS program MerTK-signalling-dependent and reproducible, or FLS-donor/composition identity?

Domain: disease_mechanisms. Operation: evolve. Parent: [prior hypothesis]
(valid, gen 3; the board leader at mu 31.6, itself an evolution of [prior hypothesis]).
Seeds engaged: D3-M2 (directional crosstalk), benchmarked by D3-M1 (composition vs within-cell state)
and D3-M3 (persistence vs remission).
Status: hypothesis-stage, data-bound, with an EXECUTED exploratory screening (below). No causal or
clinical claim is asserted as established.

## 1. Unresolved question
The parent branch asks whether the FLS response attributed to the MerTK+CD206+ (Mpos) macrophage state
is reproducible (state-shaping) or donor/composition-driven. The parent recorded two unresolved
limitations that block a decisive test:
(a) the 445-feature E-MTAB-8873 targeted panel does not measure the ligand/receptor side
    (GAS6/PROS1/TYRO3 absent), and
(b) the exact MerTK-inhibitor identity and dose were unverified, so the "inhibitor-reversal" arm was
    a plan, not a bound contrast.
Both limitations are RESOLVED this episode by E-MTAB-8316 (verified below). The sharpened, falsifiable
question:
**Does pharmacological blockade of macrophage MerTK (UNC106238) produce a reproducible, donor-consistent
change in the co-cultured FLS transcriptome (a directional MerTK-dependent program, H1), or is the FLS
co-culture transcriptome dominated by FLS/monocyte-donor identity and generic LPS with no donor-consistent
inhibitor effect (composition/context rival, H0)?**

## 2. Clinical importance
If the MerTK axis is a functional driver of the FLS state, MERTK-directed modulation (or the resolution
program it indexes) is a candidate mechanism for restoring a non-activated FLS state, and MerTK+ macrophage
frequency is an actionable pharmacodynamic readout. If instead the FLS response is donor/context identity,
then MerTK+ macrophage markers are a disease-activity correlate rather than an intervention node, and
MERTK-targeted strategies would be mis-specified. The distinction changes the next experiment, not a
correlation plot.

## 3. Leading claim vs strongest rival and the discriminating observation
- H1 (MerTK-dependent crosstalk): the UNC106238-vs-none FLS effect vector is positively concordant across
  independent co-culture experiments and exceeds a sign-flip/donor-shuffle null; the effect is a coherent,
  axis-relevant program (not one outlier gene), and ligand/receptor genes respond consistently.
- H0 (composition/context): the reproducible axis is FLS-donor identity (and LPS-driven generic inflammation),
  the inhibitor effect vector is near-orthogonal across experiments, and donor terms dominate a variance
  decomposition. [K2]
- Discriminating observation: across-experiment concordance (Pearson/Spearman r) of the paired
  UNC106238-vs-none FLS effect vectors, benchmarked against (i) a sign-flip null, and (ii) a donor-aware
  variance decomposition (variance in condition vs FLS_donor vs monocyte_donor) and a low-rank factor model.
  [K3]

## 4. Verified data bindings (executed this episode)
Primary matrix: [internal dataset path]
Design: .../prepared/E-MTAB-8316.design.json ; Protocol (read-only, authoritative): ...[internal dataset path]
- Verified: counts are 58303 rows x 13 columns = `feature` + 12 samples MK3,MK4,MK7,MK8,MK11,MK12,MK15,MK16,MK19,MK20,MK23,MK24.
  set(header) == set(design.sample_id) == True; join key = `sample_id`.
- Verified conditions: `condition`/`treatment` none = {MK3,MK7,MK11,MK15,MK19,MK23}; UNC106238 = {MK4,MK8,MK12,MK16,MK20,MK24}; 6 paired experiments.
- Verified donors: FLS donor (`donor_id`) in {SA049,SA051,SA104,SA114}; monocyte donor (`other_donor_id`) in {1462,1463,1533,1534,1601,1602}. SA049 and SA114 are each used with two monocyte donors; SA051 and SA104 with one.
- Verified readout identity (Lead marker probe): PTPRC/LYZ/CD68/MRC1 ≈ 0 and COL1A1/COL1A2/DCN/PDGFRA high => the matrix is the
  FLS (fibroblast) readout, NOT the monocyte label in design.cell_type. This reconciles the assay-registry warning; a cell-specific claim must use the FLS readout.
- Verified inhibitor (protocol text): UNC106238 (Aobious), MerTK-specific, 250 uM added for the last 2 h of a 4 h LPS (1 ng/mL) pre-treatment of healthy-donor
  monocyte-derived macrophages, then 48 h transwell co-culture; FLS lysed for RNA. This RESOLVES the parent's unverified inhibitor identity/dose.
- Verified ligand-side observability: genome-wide Ensembl panel contains MERTK (ENSG00000153208), AXL (ENSG00000167601),
  TYRO3 (ENSG00000092445), PROS1 (ENSG00000184500). GAS6 (ENSG00000183083) is NOT present in this matrix by that ID. This RESOLVES the parent's ligand-side limitation (with the GAS6 caveat).

Clinical/context anchor (read-only, NOT external validation): E-MTAB-8322 (.../prepared/E-MTAB-8322.counts.tsv.gz + .design.json),
macrophage pseudobulk remission/resistant/naive/healthy (27 samples; donor_status requires a contributing-donor model for 2 samples).
Domain limits retained: no cross-dataset patient joins; GSE95588 coculture r1/r2 reuses earlier GSE57723 and cannot count as independent validation.

## 5. EXECUTED screening (this episode; exploratory, NOT confirmatory)
Script: work/lead/screen_8316.py ; log: work/lead/screen_8316.out
Method: log2(CPM+1) per sample (27055 genes with total count >= 12 kept); effect vector = log2CPM(UNC106238) - log2CPM(none)
paired within each of the 6 experiments (same FLS donor + same monocyte donor).
- Across-experiment effect-vector concordance: mean pairwise Pearson r = +0.284 (min -0.052, max +0.616);
  mean Spearman rho = +0.158. Sign-flip permutation null (2000 draws) mean r = -0.004, sd = 0.093, p(|r| >= 0.284) = 0.029.
- Coherent direction: top |mean effect| features are inflammatory/NF-kB program genes, mostly INCREASED with MerTK
  blockade, e.g. IL1B (ENSG00000125538, mean logFC +2.47, sd 1.33), CXCL8 (ENSG00000169429 +2.34), CCL20 (ENSG00000115009 +2.19),
  PTGS2 (ENSG00000073756 +2.31), IL23A (ENSG00000110944 +3.02), CSF3 (ENSG00000108342 +2.96), MMP3 (ENSG00000149968 +2.86),
  CXCL5 (ENSG00000163735 +2.78).
- Axis genes: MERTK +0.57 (sd 0.33), TYRO3 +0.18, AXL -0.11, PROS1 -0.39.
Interpretation: an exploratory, weak-to-moderate, direction-coherent signal that MerTK blockade raises a shared inflammatory
FLS program (consistent with blocking a resolution/efferocytosis receptor -> Alivernini's Mpos=resolution biology [K1]).
This is a nominal concordance (mean r=0.28; one of six pairs negative; no independent replicate ceiling), so it does NOT
establish a validated MerTK-dependent program and does NOT separate H1 from a shared batch/global shift.

## 6. Methods: baseline and substantive alternative (same question)
- Baseline: paired UNC106238-vs-none log2CPM effect vectors, across-experiment Pearson/Spearman concordance, sign-flip null.
- Substantive alternative (kept distinct): (i) donor-aware variance decomposition per gene, e.g.
  expression ~ condition + FLS_donor + monocyte_donor (+ library size), reporting the reproducible variance share of
  `condition` vs donor terms; and (ii) a low-rank factor model (PCA on the 12-sample x G log2CPM matrix) with each factor
  scored/regressed against condition vs FLS_donor vs monocyte_donor to see whether the dominant reproducible axis is the
  inhibitor condition or the FLS donor. [K3] The alternative reveals HOW MUCH reproducible variance is condition vs
  composition, and whether a single latent factor carries the perturbation signal — information the concordance baseline
  alone cannot provide. It is the natural rival discriminator (H0), not complexity for its own sake.
- Resource budget: 12 samples x ~58k features is a small CPU fit; baseline + variance decomposition + PCA is seconds-to-minutes
  on CPU (my screening ran in <10 s on 4 CPUs). No GPU required; a GPU is available if a larger permutation/bootstrap is wanted.

## 7. Falsification criterion
H1 is falsified as stated if the across-experiment concordance of the UNC106238 effect vector is not distinguishable from the
sign-flip/donor-shuffle null (e.g. p >= 0.05) AND the donor-aware variance decomposition attributes the dominant reproducible
axis to FLS_donor (or monocyte_donor) rather than `condition`. H0 is falsified if the condition effect is concordant beyond the
null AND condition explains a larger reproducible variance share than donor identity, with the effect carried by a coherent
axis program rather than isolated genes.

## 8. Supportive / adverse / inconclusive outcomes
- Supportive (for a MerTK-dependent FLS program): across-experiment effect-vector concordance exceeds the null
  (p < 0.05) with a positive mean r that survives leave-one-donor-out, and the condition term explains a materially larger
  reproducible variance share than donor identity; axis genes behave consistently across experiments. Meaning: proceed to a
  donor-balanced, pre-registered replication and a ligand (GAS6/PROS1) side test; this justifies a MerTK-axis intervention study.
- Adverse (composition/context): effect vectors are near-orthogonal (r ~ 0) and donor-identity terms dominate; the exploratory
  r=0.28 signal disappears under leave-one-donor-out or is carried by one pair. Meaning: the FLS co-culture readout is a donor/
  composition correlate; MERTK-directed strategies are mis-specified on this evidence, and the branch should be revised toward
  composition/state-covariate modeling, not an inhibitor target.
- Inconclusive: concordance is nominally positive but small (as in the current screening) with a wide interval and no independent
  replicate ceiling, or the design cannot separate condition from global/batch shift with only 6 pairs. Meaning: do not
  over-claim; the result is consistent with a weak shared effect or a technical/batch shift, and a larger, independently
  generated co-culture series (or GAS6/PROS1 perturbation) is required.

## 9. What each outcome does / does not establish
A supportive result establishes a reproducible, donor-consistent transcriptional consequence of MerTK blockade in this
co-culture system; it does NOT by itself prove direct MERTK engagement (UNC106238 selectivity is taken from the protocol),
nor a causal in-vivo mechanism, nor that MerTK+ macrophage abundance is causal in disease. An adverse result bounds the
parent's state-shaping claim and argues the reproducible axis is composition; it does not exclude a MerTK effect that this
6-pair design is underpowered to detect. GAS6 dependence cannot be tested in this matrix (GAS6 absent by the checked ID).

## 10. Key references (inspected; abstract-level)
[K1] Alivernini 2020 (doi:10.1038/s41591-020-0939-8) supports the clinical salience of the MerTK+CD206+ macrophage-remission
association but is cross-sectional and provides no FLS perturbation or directionality. [K2] Culemann 2019
(doi:10.1038/s41586-019-1471-1) supplies the leading composition/ontogeny rival. [K3] Squair 2021
(doi:10.1038/s41467-021-25960-2) bounds the inference: replicate-blind contrasts over-report DE, motivating the permutation
null and the inconclusive zone. Inspection was abstract_only; publisher full text and supplementary methods were NOT inspected.
Receipts are hashed to the attached excerpt bytes (K1 021d6f20..., K2 db21b401..., K3 fe7a4940...).

## 11. Expert-adjudicated / out of scope
Clinical interpretation, UNC106238 selectivity/dose translation, donor disease-state modeling and any in-vivo mechanism require
expert review and are not established here. The GSE95588 coculture arm reuses GSE57723 and is not independent validation.
