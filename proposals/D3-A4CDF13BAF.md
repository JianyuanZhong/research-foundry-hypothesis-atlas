> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: donor-aware macrophage-to-FLS response in E-MTAB-8873

## Proposed relationship

In the frozen E-MTAB-8873 targeted expression experiment, co-culture of RA type B synovial cells (FLS) with MerTK/CD206-positive macrophages may induce a reproducible, condition-specific transcriptional response that is distinguishable from FLS-only and MerTK/CD206-negative macrophage co-culture after accounting for contributing donors and repeated context measurements.

This is a hypothesis, not an executed result. The available evidence motivates reciprocal macrophage–FLS communication and MerTK-associated resolution in RA synovium, but does not establish a response in this targeted assay, direct ligand-receptor action, causality, or clinical benefit.

## Evidence opening and exact data binding

The primary source is the frozen prepared matrix:

- `[internal dataset path]`
- `[internal dataset path]`

The matrix is reported in the inherited candidate record to contain a feature column plus 33 sample columns and 445 targeted features. The design JSON is reported to contain 33 records joined to matrix columns by `sample_id`. Feature identifiers are source identifiers of the form `gene|transcript|Reference_end`; they must not be merged without a verified feature map. The design is reported to include condition, treatment, donor/context and repeated-measurement fields, but exact donor mapping and feature identity still require direct verification.

The proposed primary contrast is positive-macrophage co-culture versus FLS-only and negative-macrophage co-culture within treatment=none, with donor-paired or donor-aware contrasts and a permutation/uncertainty analysis that respects repeated contexts. A secondary exploratory contrast may examine treatment-associated changes only if treatment and donor structure are verified; it is not a causal treatment claim.

## Falsifiable test

Fit a prespecified donor-aware model to the 445 features, using the 33 condition samples as the unit of observation and the matrix feature column as the measurement. Compare the positive-macrophage condition with both controls, with uncertainty from donor/context-aware permutations or a prespecified mixed model. The hypothesis is supported only if the positive contrast is directionally and reproducibly distinct from both controls, survives the prespecified donor/context adjustment, and is not explained by a small number of features, batch, or donor imbalance. It is adverse if the positive condition is indistinguishable from controls, is driven by a single donor or feature, or shows the opposite pattern. It is inconclusive if donor/context metadata, feature identity, replicate structure, or variance cannot support the prespecified inference.

## Missing evidence and limits

No numerical expression contrast, significance test, model fit, or validation has been executed in this episode. Direct source inspection and exact schema verification are still required. The targeted panel does not measure absent genes. The assay cannot establish direct ligand-receptor mechanism, cell-cell causality, clinical efficacy, or generalization to patients. Donor identity conflicts, treatment exposure, batch, composition, and assay artifacts are competing explanations. A complete experiment card, three inspected key-reference receipts, and an independent critique remain required for selection.

## Method comparison

The simple baseline is a donor-paired condition contrast with permutation uncertainty. A substantive alternative is a donor-aware mixed-effect model or hierarchical feature model that borrows information across features while preserving donor and context dependence. The alternative could reveal whether the signal is coherent across a pathway rather than a few outlier features, but it loses nothing scientifically if it cannot be identified because the 33-condition structure is too sparse. No neural model is justified at this stage; the scientific uncertainty is mechanism/condition specificity, not predictive performance.

## Disposition of demonstrations and seed context

The inherited E-MTAB-8873 direction is retained as a concrete adaptation because it has exact local source files and a paired condition structure. The EHR multimodal demonstration is not pursued here because the configured source is molecular expression and the missing imaging/longitudinal EHR dependency would change the question. The proteomic aging-clock demonstration is not pursued because no verified local aging-clock inputs are bound to this hypothesis. These are dispositions, not claims that the demonstrations were reproduced.
