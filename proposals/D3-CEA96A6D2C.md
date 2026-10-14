> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: macrophage-conditioned FLS response in E-MTAB-8873

## Proposed relationship

In the available E-MTAB-8873 targeted expression experiment, synovial fibroblast-like cell (FLS) exposure to macrophages may induce a reproducible, condition-specific transcriptional response that is distinguishable from FLS-only and macrophage-negative controls after accounting for donor and repeated context. This is a hypothesis, not a computed result.

## Grounding and exact data opening

The domain guide binds the primary source to:

- matrix: [internal dataset path]
- design: [internal dataset path]

The guide states that this is a targeted assay with 445 measured feature columns, that the source identifiers must be preserved, and that pseudobulk summaries and reused or multiple donors require explicit dependence handling. It also warns that unmeasured genes are unavailable and ordinary donor t-tests are disabled. No numerical result, donor mapping, or feature-level conclusion has been computed in this provisional draft.

## Unresolved claim and falsifiable test

The unresolved claim is whether the macrophage-positive versus FLS-only contrast contains a donor-aware, condition-specific FLS response rather than a generic donor, batch, or cell-composition effect. A first discriminating analysis should:

1. verify the design JSON fields, sample/condition labels, donor identifiers, and matrix join key;
2. define the macrophage-positive, FLS-only, and macrophage-negative contrasts without treating pseudobulk rows as independent;
3. compare a simple donor-aware paired/clustered contrast or permutation test with a mechanistically motivated alternative that models condition-by-donor interaction and repeated context;
4. report effect direction, uncertainty, and feature-level reproducibility, with a prespecified threshold for biological interpretability.

Supportive evidence would be a reproducible condition-specific contrast with uncertainty that excludes the prespecified null and is not explained by the negative control or donor structure. Adverse evidence would be no reproducible contrast, a contrast confined to the negative control, or evidence that the apparent signal is dominated by donor/batch structure. Inconclusive evidence would include too few independent donor units, unresolved metadata, or wide uncertainty; it would motivate metadata reconciliation or a new assay rather than a causal claim.

## Missing evidence and limits

The provisional draft does not yet establish the exact donor-to-sample mapping, whether the 445 features support a stable contrast, or whether any observed signal is direct macrophage-to-FLS signaling. It also cannot establish ligand-receptor causality, whole-tissue composition, clinical response, or treatment benefit. These require verified metadata and, ultimately, perturbation or clinical validation.

## Method comparison

The simple baseline is a donor-aware paired/clustered contrast with permutation uncertainty. The substantive alternative is a condition-by-donor interaction model that can reveal whether the response is shared across donors or driven by a subset and whether repeated context changes the apparent contrast. The alternative loses interpretability if overfit to the small number of independent donors; therefore its result must be compared against the baseline and held out or permuted within donor where feasible. No GPU is required for this hypothesis-stage design.
