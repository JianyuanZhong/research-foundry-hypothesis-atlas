> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: assay-verified context-dependent intervention response

## Proposed relationship

In the available macrophage–fibroblast intervention data, the intervention-associated transcriptional response will differ between macrophage and fibroblast cellular contexts. The primary unresolved claim is a donor-aware, condition-verified context-by-intervention interaction, not a generic mean-expression change.

This is a hypothesis, not an observed result. No dataset-specific effect has been computed in this episode. The proposed test is whether the intervention changes a coordinated macrophage-linked versus fibroblast-linked state after accounting for donor, timing, composition, and measurement artifacts.

## Evidence and claim boundary

The inspected evidence supports that MerTK-positive synovial tissue macrophage subsets are associated with remission and can induce repair responses in synovial fibroblasts [K1]. It also supports that macrophage–fibroblast crosstalk and active resolution programs are context-dependent and can become maladaptive in chronic inflammatory disease [K2][K3]. These observations make context-dependent MerTK modulation a plausible therapeutic question.

The strongest evidence does not establish that UNC106238 acts directly on MerTK, that an in-vitro transcriptional response is causal, that a protective state is preserved, or that any pattern transfers to patients. The unresolved claim is whether the intervention produces a reproducible separation between a macrophage-linked resolving/protective state and a fibroblast-linked harmful program under verified conditions.

## Concrete falsifiable test

1. Verify the therapeutic-target assay registry and source catalog for the exact E-MTAB-8873 intervention, vehicle/unstimulated, timing, donor, and cell-context fields.
2. Restrict analysis to samples with verified treatment, control, temporal, and context labels; join expression and design by sample_id and retain source-specific identities without cross-dataset identity joins.
3. Estimate a donor-aware context-by-intervention interaction for prespecified macrophage-linked and fibroblast-linked programs, with uncertainty clustered or permuted at the independent donor level.
4. Compare a simple additive baseline (main effects only) with a substantive interaction model; use the interaction contrast, not a small predictive gain, as the scientific test.
5. Treat a reproducible, donor-stable interaction as supportive; a null or reversed interaction as adverse to the proposed specificity; unstable donor estimates, missing controls, insufficient independent units, or context ambiguity as inconclusive.

## Exact data bindings and limitations

Primary source: E-MTAB-8873.
- Counts table: `[internal dataset path]` (gzip TSV; observed header `feature` plus 33 sample columns; 445 feature rows).
- Design table: `[internal dataset path]` (JSON list; 33 rows).
- Join key: design `sample_id` to the matching counts column name. Required design fields are `sample_id`, `donor_id`, `other_donor_id`, `donor_status`, `condition`, `treatment`, `cell_type`, `age`, `sex`, `tissue`, and `source_metadata`.
- The observed conditions include FLS-only, MerTK/CD206-positive and -negative co-culture, mixed macrophage co-culture, LPS controls, and MerTK-inhibitor variants. All 33 design rows are marked `requires_contributing_donor_model`; donors are mixed or reused, so samples are not independent and a donor-level model or narrowed verified single-donor contrasts are required.
- Preserve source feature identifiers and do not merge duplicate/date-like labels. No cross-dataset identity join is permitted.

Essential unavailable evidence includes direct target occupancy or perturbation of MerTK, patient clinical outcomes, and independent external validation. A drug-associated expression response cannot be interpreted as proof of direct target action. Clinical interpretation requires expert adjudication and a separate study.

## Method comparison

Baseline: additive intervention and context effects with donor-aware uncertainty. Alternative: an interaction model for the same question, potentially with a mechanistically informed macrophage-versus-fibroblast program contrast. The alternative can reveal whether the intervention changes the relationship between cell context and state rather than merely shifting overall expression. It is retained because it tests the substantive unresolved specificity claim; it is not selected for predictive performance.

## Deliverable and next step

The solver must newly estimate the interaction contrast and uncertainty from the verified source files, report the baseline comparison, and classify the result as supportive, adverse, or inconclusive under prespecified criteria. The next step is to inspect the three frozen key works, complete the experiment card, and assess feasibility without claiming a completed result.


## Compact bibliography

[K1] Alivernini S et al. “Distinct synovial tissue macrophage subsets regulate inflammation and remission in rheumatoid arthritis.” Nature Medicine 26:1295–1306, 2020. doi:10.1038/s41591-020-0939-8. Inspected abstract/full-text metadata; supports MerTK-positive STM remission signatures and in-vitro fibroblast repair induction, not direct drug-target causality.

[K2] Wang MQ et al. “Targeted phagocytosis of TNF-α by CAR macrophages restores immune homeostasis in arthritis.” Theranostics 16:9007–9029, 2026. doi:10.7150/thno.132172. Inspected full-text XML abstract and methods/results; supports MerTK-positive resolving macrophage function and therapeutic reprogramming, not UNC106238 direct action.

[K3] Mosallanejad K et al. “Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies.” Cells 15:1412, 2026. doi:10.3390/cells15151412. Inspected full-text XML abstract and introduction; supports context-dependent myeloid–stromal repair and maladaptive remodeling, not a drug-specific interaction.
