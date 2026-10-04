> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional successor hypothesis: macrophage context changes FLS state beyond donor composition

## Proposed relationship
In the frozen E-MTAB-8873 targeted human synovial type B synovial cell (FLS) assay, FLS cells co-cultured with MerTK/CD206-positive macrophages have a reproducible, donor-set-aware difference in measured transcript state from FLS cells co-cultured with MerTK/CD206-negative macrophages, beyond recorded cell count and the complete set of contributing donors. This is a context-associated hypothesis, not a causal macrophage-mechanism claim. No expression contrast or model has been computed in this episode.

## Grounded evidence and exact bindings
The persistent candidate board records a verified assay binding to:
- Design: `[internal dataset path]`, with 33 records and fields `sample_id`, `donor_id`, `donor_status`, `condition`, `treatment`, `cells`, `age`, `sex`, `tissue`, `cell_type`, and `source_metadata`; the join key is `sample_id`.
- Matrix: `[internal dataset path]`, with row key `feature` and 33 sample columns matching the design records.

The prior board records that the matrix contains 445 feature-instance keys and that the primary comparison should use the five none-treatment Mpos/Mneg pairs, treating complete contributing-donor sets as the analysis unit and excluding the malformed donor record from the primary set. These are inherited design facts, not newly executed results in this episode.

## Unresolved question and falsification test
The unresolved claim is whether the macrophage-context contrast is reproducible within donor sets after accounting for the recorded donor composition and cell count. The planned test is a donor-aware paired contrast of the five none-treatment Mpos/Mneg pairs, with a simple baseline of donor-centered mean differences and a substantive alternative that models feature-level effects with donor-set and cell-count structure. The alternative can reveal whether a coherent pathway/state signal is retained after donor composition is accounted for, information lost by a single aggregate difference.

Supportive evidence would be a reproducible, directionally consistent contrast across donor sets with uncertainty that excludes a prespecified negligible effect and a structured alternative that is not explained by the baseline. Adverse evidence would be no reproducible contrast, a contrast confined to the malformed/excluded donor, or a result that disappears after donor-set accounting. Inconclusive evidence would include too few usable donor sets, unstable feature-instance mapping, or uncertainty spanning both meaningful and negligible effects. None of these outcomes establishes a direct macrophage mechanism.

## Missing evidence and limitations
No expression result, model fit, or literature receipt was computed or inspected in this episode. The exact raw assay metadata and full source catalog were not independently re-read after the checkpoint. The required three inspected key works with frozen receipts are not attached. The complete life-science experiment card is not yet finalized. A targeted panel does not measure absent genes, and the assay cannot by itself establish whole-tissue composition, cell-cell signaling, or causality.

## Method comparison and deliverable
The simple baseline is a donor-centered paired difference with uncertainty from the available donor sets. The substantive alternative is a hierarchical feature/donor-set model, fitted only if the feature-instance map and missingness are reconciled; it tests whether the signal is structured across features rather than a single aggregate shift. This is a CPU-feasible planned analysis for 33 samples and 445 features; no GPU is required. The actual scientific deliverable is the newly fitted/estimated contrast and uncertainty, not a readiness check. The three earlier demonstrations are not being reproduced: their missing cohort/modalities or full methods do not define this targeted assay adaptation.
