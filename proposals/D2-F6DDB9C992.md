> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Evolution: MerTK-inhibitor perturbation selectivity in E-MTAB-8873

## 1. Scientific question and claim scope

**Unresolved question.** In the three recorded MerTK/CD206-positive rheumatoid arthritis (RA) synovial coculture units, does pre-treating macrophages with a MerTK inhibitor reduce a harmful fibroblast inflammatory/destructive program relative to the typical non-program panel background, while preserving fibroblast matrix/TGF-beta repair and macrophage repair-linked identity?

The experiment tests **perturbation-response selectivity** in one bounded ex vivo assay. It does not test MerTK target causality, fibroblast-intrinsic mechanism, off-target effects, patient benefit, clinical safety, or generalizability to other donors, tissues, doses, or timings. Because the prepared matrix is pseudobulk, the three named programs are coculture-level programs, not cell-type-resolved programs.

**Clinical motivation.** RA synovial fibroblasts can drive inflammatory and destructive pathology, while macrophage-fibroblast repair circuits can support resolution. A perturbation that suppresses the harmful fibroblast program while erasing repair-linked identity or matrix/TGF-beta programs could be biologically counterproductive. Conversely, a null or adverse result can reduce premature enthusiasm for MerTK blockade in this cell state. Prior work supports harmful fibroblast transitions [K1], macrophage-fibroblast repair circuitry [K2], and pathogenic fibroblasts as therapeutic targets [K3], but none establishes the effect of MerTK inhibition in E-MTAB-8873.

**Existing evidence versus new claim.** The repository evidence associates MerTK/CD206-negative macrophages with an inflammatory fibroblast cluster and MerTK/CD206-positive macrophages with collagen/TGF-beta repair responses. It does not report MerTK-inhibitor effects. The new, falsifiable claim is that MerTK inhibition changes the harmful program selectively relative to a non-program panel background and the two prespecified repair-linked interpretive outcomes. A mere negative raw harmful score is insufficient because it could reflect global expression suppression.

## 2. Exact source binding and verified population

### Inputs

- Prepared expression matrix: `[internal dataset path]`
  - [source checksum]
- Prepared design: `[internal dataset path]`
  - [source checksum]
- Repository provenance: `[internal dataset path]`
  - [source checksum]

The expression file is a feature-by-sample gzip TSV with a `feature` key column and **33 sample columns**. It contains **445 unique feature labels**. The design JSON contains **33 objects**, one per sample, with fields including `sample_id`, `donor_id`, `age`, `sex`, `condition`, `treatment`, `source_metadata`, and `cells`. The required join is:

`design.sample_id == expression column name`

The 33 sample identifiers match exactly between the two files. No archive member is needed for the primary analysis because the prepared matrix and design are direct frozen inputs. The temporal boundary is the repository-described 48-hour ex vivo coculture; `R1`, `R2`, and `R5` are experimental runs, not longitudinal disease time points.

### Primary matched units

The primary population is the three recorded MerTK/CD206-positive coculture units with an exact untreated/inhibitor pair, matched within run on FLS donor, macrophage donor, cell state, and treatment sequence.

| Unit | Untreated | Inhibitor | FLS donor | Macrophage donor | Age | Cells |
|---|---|---|---|---|---|---|
| R1 | `R1_SA256A_FLS_SA259A_Mpos` | `R1_SA256A_FLS_SA259A_Mpos_Inhibitor` | SA256A | SA259A | 53 | 368 / 283 |
| R2 | `R2_SA257A_FLS_SA266A_Mpos` | `R2_SA257A_FLS_SA266A_Mpos_preInhibitor` | SA257A | SA266A | 50 | 383 / 394 |
| R5 | `R5_SA266A_FLS_SA277A_Mpos` | `R5_SA266A_FLS_SA277A_Mpos_preInhibitor` | SA266A | SA277A | 69 | 1060 / 1032 |

The single exploratory negative-state unit is:

| Unit | Untreated | Inhibitor | FLS donor | Macrophage donor | Age | Cells |
|---|---|---|---|---|---|---|
| R1 Mneg | `R1_SA256A_FLS_SA259A_Mneg` | `R1_SA256A_FLS_SA259A_Mneg_Inhibitor` | SA256A | SA259A | 53 | 491 / 432 |

This negative-state unit is not a fourth primary replicate. It shares the R1 donor pair and differs in macrophage state, so it is reported only as a directional specificity check.

### Donor/run overlap

The three primary units have distinct FLS-macrophage donor pairs, but donor `SA266A` crosses roles: it is the macrophage donor in R2 and the FLS donor in R5. Therefore the primary sample size is three matched coculture units, not six independent donors. Unit-level paired differences are the inference units. Donor identifiers must not be used to enlarge the effective sample size.

## 3. Exact prespecified program features

All 28 labels below are present in the 445-feature matrix. Exact labels must be used because the panel contains both `COL1A1|NM_000088.3|Reference_end` and `COL1A1|NM_000088.3|PolyA_1`; only the `Reference_end` row is in the repair score.

### Harmful fibroblast inflammatory/destructive program (10)

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

### Fibroblast matrix/TGF-beta repair program (9)

- `COL1A1|NM_000088.3|Reference_end`
- `COL1A2|NM_000089.3|PolyA_1`
- `COL3A1|NM_000090.3|PolyA_1`
- `TGFB1|NM_000660.5|PolyA_1`
- `TGFB3|NM_003239.3|Reference_end`
- `TGFBI|NM_000358.2|Reference_end`
- `TGFBR1|NM_004612.3|PolyA_1`
- `TGFBR2|NM_003242.5|PolyA_1`
- `CMKLR1|NM_004072.2|Reference_end`

### Macrophage repair-linked identity program (9)

- `MERTK|NM_006343.2|Reference_end`
- `MRC1|NM_002438.3|Reference_end`
- `CD163|NM_004244.5|PolyA_1`
- `FOLR2|NM_000803.4|Reference_end`
- `APOE|NM_000041.3|Reference_end`
- `TREM2|NM_018965.3|Reference_end`
- `C1QA|NM_015991.2|Reference_end`
- `C1QB|NM_000491.3|Reference_end`
- `ARG1|NM_000045.3|Reference_end`

The remaining **417 panel features** are the non-program background set. Genes outside the 445-feature panel are unavailable and must not be imputed or described as measured.

## 4. Primary estimand, co-primary interpretive outcomes, and controls

For matched unit \(i\) and feature \(f\), define the paired log2 change

\[
d_{if}=\log_2(y^{\text{inhibitor}}_{if}+1)-\log_2(y^{\text{untreated}}_{if}+1).
\]

Let \(H\), \(R\), and \(M\) be the 10 harmful, 9 fibroblast repair, and 9 macrophage identity feature sets. Raw program scores are

\[
h_i=\frac{1}{10}\sum_{f\in H}d_{if},\quad
r_i=\frac{1}{9}\sum_{f\in R}d_{if},\quad
m_i=\frac{1}{9}\sum_{f\in M}d_{if}.
\]

Let \(B\) be the 417 non-program features. The unit-specific **non-program background shift** is

\[
g_i=\operatorname{median}_{f\in B}d_{if},
\]

and the unit-specific **panel-wide perturbation magnitude** is

\[
q_i=\operatorname{median}_{f\in B}|d_{if}|.
\]

The **panel-normalized program change** is the program score minus the non-program background shift:

\[
t_{iP}=p_i-g_i,\quad p_i\in\{h_i,r_i,m_i\}.
\]

The **single primary estimand** is

\[
\theta_H=\operatorname{median}_{i\in\{R1,R2,R5\}}(h_i-g_i).
\]

Interpretation:

- \(\theta_H<0\): the harmful program falls more than the typical non-program feature.
- \(\theta_H=0\): the harmful program moves with the panel-wide background; selectivity is not established.
- \(\theta_H>0\): the harmful program does not fall relative to background.

The fibroblast repair and macrophage identity changes

\[
\theta_R=\operatorname{median}(r_i-g_i),\quad
\theta_M=\operatorname{median}(m_i-g_i)
\]

are prespecified **co-primary interpretive outcomes**. They are not independent confirmatory tests. They determine whether a harmful-program reduction is selective or accompanied by loss of repair-linked programs.

This background subtraction is the **global-suppression control**. If MerTK inhibition broadly lowers expression, \(g_i\) becomes negative and a raw negative \(h_i\) no longer demonstrates selectivity; \(h_i-g_i\) approaches zero when the harmful program merely follows the global shift. The scale \(q_i\) is reported for every unit and summarizes the typical size of non-program perturbation. It is a scale descriptor and a check on whether the experiment produced a detectable panel perturbation, not a second significance test.

## 5. Exact uncertainty and donor/run sensitivity

### Primary exact sign-flip procedure

Under the null of no systematic direction, the signs of the three matched unit-level normalized differences are exchangeable. Enumerate all \(2^3=8\) assignments of signs to

\[
t_{R1,H},\ t_{R2,H},\ t_{R5,H}.
\]

For each assignment \(s\), compute

\[
T_s=\operatorname{median}(s_1t_{R1,H},s_2t_{R2,H},s_3t_{R5,H}).
\]

Let \(T_{\text{obs}}=\theta_H\). The exact two-sided p-value is

\[
p_H=\frac{\#\{s:|T_s|\ge |T_{\text{obs}}|\}}{8},
\]

counting the observed assignment and ties. The solver must print all eight flip statistics, not sample them randomly. The same exact procedure is applied separately to \(t_{i,R}\) and \(t_{i,M}\), with the corresponding 8-flip null distributions. No normal approximation, three-unit t-test, or asymptotic confidence interval is permitted. With three units, the minimum exact two-sided p-value is 0.25; results are therefore mechanistic/exploratory evidence, not proof.

### Donor/run overlap sensitivity

The primary analysis remains at matched-unit level. Because SA266A connects R2 and R5 across roles, the solver must also report:

1. **Leave-one-unit-out medians.** For each unit left out, report the median of the two remaining \(t_{i,H}\), \(t_{i,R}\), and \(t_{i,M}\) values.
2. **Overlap-conservative cluster sensitivity.** Treat R1 as cluster A and {R2,R5} as overlap-linked cluster B. Define cluster scores \(a=t_{R1,P}\) and \(b=\operatorname{median}(t_{R2,P},t_{R5,P})\). Enumerate all \(2^2=4\) sign assignments and report an exact two-sided p-value for the median of the two cluster scores. This is a conservative sensitivity analysis, not the primary test.
3. **Role-overlap check.** Report whether dropping R2, dropping R5, or using the two-cluster analysis changes the sign of the harmful, repair, or macrophage normalized estimates. A sign change labels that outcome fragile and prevents a supportive interpretation.

The single Mneg unit is reported only as a unit-level directional comparison. It receives no p-value and cannot rescue or overturn the primary result.

## 6. Baseline, feature-level alternative, and computational plan

### Simple program-score baseline

The baseline is the panel-normalized score above. It is the primary analysis because the gene sets are prespecified, the scientific claim is program-level selectivity, and the effective sample size is three matched units. The fit target is the paired inhibitor-minus-untreated log2 change at unit level after non-program background subtraction. There is no training split; the exact 8-flip null distribution is the uncertainty evaluation. Outputs are three unit-level \(t_{i,H}\), \(t_{i,R}\), and \(t_{i,M}\) values; their medians; exact p-values; per-unit \(g_i\) and \(q_i\); and leave-one-unit and cluster sensitivities.

### Substantive multivariate feature-level alternative

A mean score can conceal whether one extreme gene drives the result or whether multiple harmful genes move coherently. The alternative therefore analyzes all normalized feature-level changes

\[
e_{if}=d_{if}-g_i,\quad f\in P,\ i\in\{R1,R2,R5\}.
\]

For each program \(P\):

1. Rank \(|e_{if}|\) among program features within each unit.
2. Compute the unit-level signed-rank vector \(w_{if}=\operatorname{sign}(e_{if})\operatorname{rank}(|e_{if}|)\).
3. Compute the program statistic as the mean signed rank across all features and units.
4. Generate the exact null distribution by independently flipping the signs of entire unit vectors, preserving within-unit feature correlations and the donor/run structure. There are 8 sign assignments.
5. Report the exact two-sided p-value, the median normalized change for each feature across units, each feature's rank contribution, and the change in the statistic after leaving out the highest-contribution feature.

This is a multivariate profile test, not a supervised predictive model. Its fit target is the paired normalized feature-level response; its uncertainty is exact unit-vector sign-flipping; and its outcome is whether the harmful program's shift is coordinated rather than driven by one gene. It is compared with the baseline on the same three units and exact null structure. The solver must not use the result to retune the primary score or gene set.

A sparse PLS, elastic-net, or neural model is explicitly deferred. Three matched units cannot support stable feature selection, hyperparameter tuning, or honest held-out validation, and any small predictive gain would not answer the program-selectivity question. If more independent matched units become available, revisit a prespecified sparse multivariate model with leave-one-unit-out evaluation and held-out program-score prediction. Approximate resources for the entire CPU-only baseline and feature-level analysis are 2–4 CPU cores, at most 4 GB RAM, and under one minute; this is an estimate based on the verified 445-by-33 matrix, not a completed solver run. No GPU is needed.

## 7. Computational and clinical adjudication boundaries

### Computationally checkable

- Source hashes and file dimensions.
- Exact `sample_id` joins.
- Presence and uniqueness of all 28 program labels and the two distinct COL1A1 rows.
- Matched untreated/inhibitor unit construction.
- \(d_{if}\), \(h_i\), \(r_i\), \(m_i\), \(g_i\), \(q_i\), and normalized estimates.
- Exact sign-flip p-values and donor/run sensitivities.
- Feature-level rank statistics, feature contributions, and outcome classification.

### Not computationally adjudicable from these data

- Whether the three gene sets fully capture the intended biological programs.
- Whether coculture-level transcript origin is fibroblast or macrophage.
- Whether a decrease in a measured program would improve a patient's clinical state.
- Whether the inhibitor effect is on-target or off-target.
- Whether a perturbation is safe, durable, dose-appropriate, or clinically actionable.
- Generalization beyond these donors, cell states, runs, and the 48-hour assay.

Essential missing evidence for stronger claims includes vehicle and genetic MerTK perturbation, cell-type-resolved or sorted measurements, additional independent matched donor units, protein and functional readouts, and prospective clinical validation. Expert clinical/biological review is required to judge whether the prespecified programs are adequate surrogates for the intended repair and destructive phenotypes; a verifier cannot establish that by recomputation alone.

## 8. Supportive, adverse, and inconclusive outcomes

### Supportive bounded outcome

The result is **supportive** only if all three conditions hold:

1. \(\theta_H<0\), with \(t_{i,H}<0\) in all three primary units and exact \(p_H\le0.25\).
2. The normalized repair and macrophage identity outcomes are not similarly negative: at least two of three units have \(t_{i,R}\ge0\) and at least two of three have \(t_{i,M}\ge0\), and their medians are not below zero.
3. The harmful result is not a global-suppression artifact: the non-program background shift does not dominate the harmful shift, and the feature-level signed-rank alternative agrees in direction without being driven solely by one feature after leave-one-out.

This supports only a bounded claim of harmful-program selectivity in the recorded MerTK/CD206-positive cocultures. It does not establish target causality, clinical benefit, or a treatment recommendation.

### Adverse outcome

The result is **adverse** if the harmful program is not reduced relative to background (\(\theta_H\ge0\)), or if the harmful program falls but both repair-linked interpretive outcomes also fall coherently relative to background. The latter suggests broad loss of protective programs rather than selective suppression. An adverse finding challenges MerTK blockade in this context and favors different targets, timing, or cell states, but it does not prove that the drug would harm patients.

### Inconclusive outcome

The result is **inconclusive** if:

- \(t_{i,H}\) signs are discordant across units;
- exact \(p_H>0.25\) or the overlap-conservative cluster sensitivity reverses the harmful direction;
- the harmful and non-program background shifts are both broadly negative, so selectivity cannot be distinguished from global suppression;
- panel-wide perturbation magnitude \(q_i\) is negligible while the program shift is small;
- the mean-score and feature-level signed-rank methods disagree, or one feature drives the multivariate result;
- the exploratory Mneg unit contradicts the primary direction but cannot adjudicate it because it has one unit.

Inconclusive means the design lacks power or coherence to support a directional claim. It is not evidence of therapeutic failure.

## 9. Scientific deliverable

The future solver must produce:

1. A binding verification report: hashes, dimensions, sample/design join, 445 unique labels, 417 background features, and 28/28 program labels present.
2. Three unit-level raw and normalized harmful, repair, and macrophage scores.
3. Three unit-level background shifts \(g_i\) and perturbation magnitudes \(q_i\).
4. Exact 8-flip p-values for all three normalized program outcomes.
5. Leave-one-unit and overlap-conservative cluster sensitivity results.
6. Feature-level normalized medians, signed-rank contributions, leave-one-feature-out influence, and exact 8-flip p-values.
7. The exploratory Mneg directional comparison.
8. A single classification as supportive, adverse, or inconclusive, with explicit reasons and no unsupported clinical or causal language.

## Bibliography

- [K1] Zou AE, Kongthong S, Watts GFM, Murphy CL, Fairfield ML, Mueller AA, Brenner MB. ARID5B drives an inflammatory-to-destructive shift in pathologic fibroblast behavior. bioRxiv preprint, 2026. DOI 10.64898/2026.08.04.742822.
- [K2] Mosallanejad K, Hubeau C, Schwartz Sterman A, Tan Y. Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies. Cells. 2026;15(15):1412. DOI 10.3390/cells15151412.
- [K3] Xenophontos M, Progatzky F, Buckley CD. Targeting fibroblasts in immune mediated inflammatory diseases: a cellular basis for cure? Rheumatology (Oxford). 2026;65(6):keag249. DOI 10.1093/rheumatology/keag249.
