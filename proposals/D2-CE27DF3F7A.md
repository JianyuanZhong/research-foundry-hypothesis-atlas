> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: intervention-specific separation of protective and harmful states

## Proposed relationship

In the available macrophage–fibroblast intervention data, UNC106238-associated transcriptional changes will show a context-dependent pattern: a reduction of a fibroblast-linked harmful program while preserving or strengthening a macrophage-linked protective/resolving state. The primary test is a donor-aware, condition-verified context-by-intervention interaction, not a generic expression increase or decrease.

This is a hypothesis, not an observed result. The expert seed D2-T2 motivates the clinically consequential question, but no dataset-specific effect has been computed in this episode.

## Evidence and unresolved claim

The inspected evidence supports only that macrophage–stromal interactions and MerTK-associated resolving phenotypes are plausible contexts for rheumatoid arthritis therapy [K1][K2][K3]. It does not establish that UNC106238 acts directly on MerTK, that the response is causal, that a protective state is preserved, or that any in-vitro pattern transfers to patients.

The unresolved claim is whether the intervention produces a reproducible separation between the two functional readouts after accounting for donor, timing, condition, composition, and measurement artifacts. A simple mean-expression or single-cell-type contrast would lose this distinction; the substantive comparison is whether the intervention changes the balance between the two programs differently across verified contexts.

## Concrete data-bound test

The primary planned source is the prepared E-MTAB-8873 assay:
- counts table: `[internal dataset path]`;
- design table: `[internal dataset path]`;
- join key: `sample_id` in the design joined to the corresponding column in the counts matrix;
- required design fields: `sample_id`, `donor_id`, `other_donor_id`, `donor_status`, `condition`, `treatment`, `cell_type`, `age`, `sex`, `tissue`, and `source_metadata`;
- observed design rows include FLS-only controls, MerTK/CD206neg and MerTK/CD206pos co-cultures, LPS controls, and MerTK-inhibitor variants; the assay registry records 33 samples and 445 targeted features.

The counts matrix has a `feature` column and one column per `sample_id`. The experiment must preserve source feature identifiers and reconcile duplicate/date-like labels before naming targets. It must average repeated context measurements within each verified donor/condition before paired exploratory inference; it must not treat the 33 samples as 33 independent donors. The design explicitly marks mixed/reused donors as `requires_contributing_donor_model`, so donor dependence must be modeled or the contrast must be narrowed to verified single-donor comparisons.

For each verified donor and condition, compute a paired log-ratio contrast between intervention and control. Compare macrophage-linked and fibroblast-linked program scores, using donor-clustered permutation or a prespecified interaction model. The primary estimand is the interaction: the difference in intervention-associated change between macrophage and fibroblast contexts, not the marginal expression difference.

A robust, directionally consistent interaction with adequate independent donor units is supportive of context specificity. A null interaction, reversal, or loss after donor/timing adjustment is adverse to the proposed specificity. Missing controls, insufficient independent units, unstable donor estimates, or inability to verify the assay contrast is inconclusive and should narrow the claim to exploratory description.

## Missing evidence and limitations

- The exact source paths, table/archive members, columns, join keys, and timestamps still require an audit against the catalog and assay registry.
- Expression response is not direct target action, causality, protection, or clinical benefit.
- Donor reuse, mixed populations, treatment timing, batch, composition, and absent independent biological replicates may invalidate inferential claims.
- Three inspected key works and the prior candidate’s evidence bundle are inherited as motivation; their claim mappings must be rechecked after any scientific revision.
- No full study, model fit, or clinical adjudication has been executed.

## Method comparison

The simple baseline is a donor-aware paired log-ratio contrast between treatment and control, averaged within each verified donor/condition and tested by permutation. A substantive alternative is a mechanistic context-by-intervention model estimating separate macrophage-linked and fibroblast-linked program scores and their interaction, with donor-clustered uncertainty. The alternative can reveal whether the intervention changes a coordinated state rather than only a mean expression shift; it is deferred if the feature map or independent donor units cannot support the program definition. Both methods use the same inputs and outcomes.

## Falsifiable decision rule

Continue toward a developed candidate only if the registry supports an interpretable intervention contrast and at least one context-specific gene program with adequate independent donor units. Otherwise, record the dependency as blocked and narrow the claim to exploratory description.

## Bibliography

[K1] Wang et al., 2026, doi:10.7150/thno.132172.
[K2] Wei and Xu, 2026, doi:10.3389/fimmu.2026.1935792.
[K3] Mosallanejad et al., 2026, doi:10.3390/cells15151412.
