> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# MerTK-inhibitor selectivity in matched RA synovial cocultures

## Scientific question

**Unresolved hypothesis.** In rheumatoid arthritis (RA), MerTK/CD206-positive synovial tissue macrophages (STMs) are associated with a reparative rather than inflammatory state. Does pre-treating those macrophages with a MerTK inhibitor selectively reduce a harmful fibroblast inflammatory/destructive program while preserving macrophage repair-linked identity and a fibroblast matrix/TGF-beta repair program?

This experiment tests **perturbation-response selectivity**, not target causality, fibroblast-intrinsic mechanism, patient benefit, or clinical safety. Prior repository evidence shows that MerTK/CD206-negative STMs induce an inflammatory fibroblast cluster and MerTK/CD206-positive STMs induce collagen/TGF-beta repair responses; it does **not** report MerTK-inhibitor effects [K1][K2][K3].

## Exact data binding

- Matrix: `[internal dataset path]`
  [source checksum]
- Design: `[internal dataset path]`
  [source checksum]
- Repository provenance: `[internal dataset path]`
  [source checksum]

The matrix has a `feature` key column plus **33 sample columns**. It contains **445 unique feature labels**. The design has 33 objects, one per sample. The join key is:

`design.sample_id == expression column name`

No archive member is needed; the two prepared files are direct gzip TSV and JSON inputs. The repository describes a **48-hour ex vivo coculture protocol**, so R1/R2/R5 are experimental runs, not a longitudinal disease timeline.

### Verified matched contrasts

| Unit | Untreated sample | Inhibitor sample | FLS donor | Macrophage donor | Age | Cells |
|---|---|---|---|---|---|---|
| R1 | `R1_SA256A_FLS_SA259A_Mpos` | `R1_SA256A_FLS_SA259A_Mpos_Inhibitor` | SA256A | SA259A | 53 | 368 / 283 |
| R2 | `R2_SA257A_FLS_SA266A_Mpos` | `R2_SA257A_FLS_SA266A_Mpos_preInhibitor` | SA257A | SA266A | 50 | 383 / 394 |
| R5 | `R5_SA266A_FLS_SA277A_Mpos` | `R5_SA266A_FLS_SA277A_Mpos_preInhibitor` | SA266A | SA277A | 69 | 1060 / 1032 |

The one available negative-state specificity check is:

| Unit | Untreated sample | Inhibitor sample | FLS donor | Macrophage donor | Age | Cells |
|---|---|---|---|---|---|---|
| R1 Mneg | `R1_SA256A_FLS_SA259A_Mneg` | `R1_SA256A_FLS_SA259A_Mneg_Inhibitor` | SA256A | SA259A | 53 | 491 / 432 |

### Run and donor structure

The three primary units have distinct FLS donors and distinct macrophage donors, but **SA266A crosses roles**: it is the macrophage donor in R2 and the FLS donor in R5. Therefore the experiment has three matched run/donor-pair units, not six independent donor observations. All primary inference must use the matched unit, not the individual donor label.

## Population

Human RA synovial membrane cocultures from female donors aged 50–70 in E-MTAB-8873. The primary population is the three recorded MerTK/CD206-positive samples with an exact untreated/inhibitor pair. The single R1 MerTK/CD206-negative pair is an exploratory specificity check, not an independent inference unit.

## Prespecified program features

All labels below are verified exactly in the 445-feature panel. The matrix is pseudobulk, so these are coculture-level programs, not cell-type-resolved expression.

### Harmful fibroblast inflammatory/destructive program

- `IL6|NM_000600.4|Reference_end`
- `IL1B|NM_000576.2|Reference_end`
- `TNF|NM_000594.3|Reference_end`
- `CXCL8|NM_000584.3|Reference_end`
- `CCL2|NM_002982.3|Reference_end`
- `CCL3|NM_002983.2|Reference_end`
- `MMP1|NM_002421.3|Reference_end`
- `MMP3|NM_002422.4|Reference_end`
- `MMP9|NM_004994.2|Reference_end`
- `MMP13|NM_002427.3|Reference_end`

### Fibroblast matrix/TGF-beta repair program

- `COL1A1|NM_000088.3|Reference_end`
- `COL1A2|NM_000089.3|PolyA_1`
- `COL3A1|NM_000090.3|PolyA_1`
- `TGFB1|NM_000660.5|PolyA_1`
- `TGFB3|NM_003239.3|Reference_end`
- `TGFBI|NM_000358.2|Reference_end`
- `TGFBR1|NM_004612.3|PolyA_1`
- `TGFBR2|NM_003242.5|PolyA_1`
- `CMKLR1|NM_004072.2|Reference_end`

`COL1A1|NM_000088.3|PolyA_1` also exists in the panel, but the prespecified score uses the `Reference_end` label above.

### Macrophage repair-linked identity program

- `MERTK|NM_006343.2|Reference_end`
- `MRC1|NM_002438.3|Reference_end`
- `CD163|NM_004244.5|PolyA_1`
- `FOLR2|NM_000803.4|Reference_end`
- `APOE|NM_000041.3|Reference_end`
- `TREM2|NM_018965.3|Reference_end`
- `C1QA|NM_015991.2|Reference_end`
- `C1QB|NM_000491.3|Reference_end`
- `ARG1|NM_000045.3|Reference_end`

No prespecified program feature is missing. Genes outside the 445 feature labels are unmeasured and unavailable; they must not be imputed or discussed as measured.

## Primary estimand and run/donor-aware uncertainty

For program \(P\) in matched unit \(u\), transform each count as \(g=\log_2(\text{count}+1)\), average the exact feature labels, and compute:

\[
D_{u,P}=\overline{g}_{P,\text{inhibitor}}-\overline{g}_{P,\text{untreated}}
\]

The primary point estimate is:

\[
\hat{\Delta}_P=\operatorname{median}_{u}D_{u,P}
\]

across the three run/donor-matched MerTK/CD206-positive units.

Inference is an **exact restricted sign-flip randomization test** over the three matched units, preserving the within-pair matching and donor-pair/run structure. This yields eight possible sign assignments. Report:

1. The three paired differences.
2. The median.
3. An exact sign-flip confidence interval obtained by inverting the test.
4. A leave-one-unit-out range as a run/donor sensitivity check.

Do not use an ordinary three-donor t-test, mixed model, or claim that repeated donor labels create independent replicates. With three units, conventional \(p<0.05\) support is not the criterion; the scientific criterion is directional consistency plus the panel-referenced selectivity rule below.

## Prespecified panel-wide perturbation control

For each unit \(u\) and each of the 445 features \(j\), compute:

\[
d_{u,j}=g_{u,j,\text{inhibitor}}-g_{u,j,\text{untreated}}
\]

Define two panel-wide controls:

- Signed panel shift:
  \[
  S_u=\operatorname{median}_{j=1}^{445}d_{u,j}
  \]
- Panel perturbation magnitude:
  \[
  M_u=\operatorname{median}_{j=1}^{445}|d_{u,j}|
  \]

For each program, compute the panel-referenced residual:

\[
R_{u,P}=D_{u,P}-S_u
\]

This control separates a program-specific shift from a global panel-wide suppression. A harmful program is considered selectively reduced only if its residual falls below the negative magnitude threshold \(R_{u,H}<-M_u\). A repair or macrophage program is considered not broadly erased when \(R_{u,P}\ge -M_u\).

## Analysis and alternatives

1. Join the design to the expression matrix by `sample_id`.
2. Compute \(g\), program scores, and \(D_{u,P}\) for the three matched units.
3. Compute exact sign-flip inference for each program score.
4. Compute \(S_u\), \(M_u\), and \(R_{u,P}\) for every unit.
5. Report the single R1 MerTK/CD206-negative pair using the same scores, explicitly as an exploratory specificity check with no inferential claim.
6. Perform two sensitivity analyses: rank-based program scores and leave-one-unit-out median.
7. Report per-gene paired differences for prespecified program genes, labeled exploratory.

A simple mean-score baseline is scientifically adequate because the feature sets are prespecified and the effective sample size is three. A rank-based multivariate profile alternative can reveal whether a program moves coherently or is driven by one gene; it does not replace the primary program-score estimand. Sparse PLS or neural models are deferred because three units cannot support stable tuning or honest held-out validation. Estimated solver cost is CPU only, under one minute and 4 GB for this 33-sample by 445-feature matrix; no GPU is needed.

## Supportive, adverse, and inconclusive rules

- **Supportive.** All three MerTK/CD206-positive units have \(D_{u,H}<0\); all three have \(R_{u,H}<-M_u\); the matrix/TGF-beta and macrophage repair programs each have \(R_{u,P}\ge -M_u\) in at least two of three units; and the exact sign-flip interval for the harmful program does not cross zero. This supports bounded perturbation-response selectivity in this assay.
- **Adverse.** The harmful program is not reduced in at least two units, or both repair programs have \(R_{u,P}<-M_u\) in all three units. This indicates either no harmful-program reduction or broad suppression of repair-linked programs.
- **Inconclusive.** Any other pattern, including discordant directions, harmful reduction without a panel-referenced selective signal, repair scores falling in some but not all units, sensitivity analyses disagreeing, or the exact sign-flip interval crossing zero. Inconclusive means uncertainty, not therapeutic failure.
- **Negative-state check.** A similar harmful reduction in the single R1 Mneg pair would weaken cell-state specificity; absence of such a reduction would support, but not prove, specificity. Because this is one exploratory unit, it cannot establish an independent claim.

## Stronger claims requiring more evidence

Target causality, fibroblast-intrinsic mechanism, clinical benefit, safety, or generalization beyond these cocultures require additional vehicle controls, genetic MerTK perturbation, cell-type-resolved measurement, independent donor-matched units, and prospective validation. None are computationally checkable from this assay.

## Scientific deliverable

The solver must produce:

1. Verified count and feature-label audit.
2. Three matched program-score differences.
3. Exact sign-flip medians, intervals, and leave-one-unit-out sensitivity.
4. Panel-wide signed shift, magnitude, and residuals.
5. Exploratory negative-state comparison.
6. A single supportive/adverse/inconclusive classification using the rules above.

No claim of target causality or clinical benefit is warranted.

## Bibliography

- [K1] Zou AE, Kongthong S, Watts GFM, Murphy CL, Fairfield ML, Mueller AA, Brenner MB. ARID5B drives an inflammatory-to-destructive shift in pathologic fibroblast behavior. bioRxiv preprint, 2026. DOI 10.64898/2026.08.04.742822.
- [K2] Mosallanejad K, Hubeau C, Schwartz Sterman A, Tan Y. Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies. Cells. 2026;15(15):1412. DOI 10.3390/cells15151412.
- [K3] Xenophontos M, Progatzky F, Buckley CD. Targeting fibroblasts in immune mediated inflammatory diseases: a cellular basis for cure? Rheumatology (Oxford). 2026;65(6):keag249. DOI 10.1093/rheumatology/keag249.
