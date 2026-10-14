> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repaired hypothesis: donor-aware macrophage-to-FLS response in E-MTAB-8873

## Proposed relationship

In the frozen E-MTAB-8873 targeted expression experiment, co-culture of RA type B synovial cells (FLS) with MerTK/CD206-positive macrophages may produce a reproducible, condition-specific transcriptional response that is distinguishable from FLS-only and MerTK/CD206-negative macrophage co-culture after accounting for contributing donors and repeated context measurements. This is a hypothesis; no expression contrast or significance result has been computed in this episode.

## Evidence opening and exact verified bindings

The available evidence is an inherited, already inspected literature context on macrophage–FLS communication and MerTK-associated resolution in RA synovium. It motivates the question but does not establish a response in this targeted assay, direct ligand-receptor action, or causality. The three inherited inspected references and frozen receipts are scientifically unchanged and will be reattached; no new literature inspection is claimed.

Direct read-only inspection of the frozen source files found:

- Counts: `[internal dataset path]`
- Design: `[internal dataset path]`

The counts file is a gzip-compressed TSV with 34 columns: a `feature` column followed by 33 sample columns. It contains 445 feature rows and 445 unique feature identifiers. The feature field is a source identifier; 444 rows are three-part identifiers of the form `gene|transcript|assay_feature` (for example `ADAM17|NM_003183.5|Reference_end`), with assay-feature suffixes `Reference_end`, `PolyA_1`, or `PolyA_2`. One row is the anomalous one-part identifier `TNFRSF11B`; it must be retained as an observed source identifier, not silently renamed or dropped. All 33 sample columns are numeric in the inspected rows.

The design file is a JSON list with 33 records. Its records contain `sample_id`, `donor_id`, `donor_status`, `other_donor_id`, `age`, `sex`, `tissue`, `cell_type`, `condition`, `treatment`, `cells`, and `source_metadata`. The 33 `sample_id` values exactly match the 33 non-feature counts columns (no missing or extra IDs). Every record has `donor_status="requires_contributing_donor_model"`; `other_donor_id` is empty in all inspected records. The condition values are 13 MerTK/CD206-positive macrophage co-cultures, 11 MerTK/CD206-negative co-cultures, 6 not-co-cultured controls, and 3 mixed MerTK/CD206-negative/positive co-cultures. Treatment values are 23 `none`, 5 MerTK-inhibitor pre-treatments, and 5 LPS pre-treatments. One record, `R1_SA256A_FLS_SA260R_Mpos`, has an explicit `_metadata_conflicts` entry in `source_metadata` and an ambiguous `donor_id` (`SA256A | SA256A, SA260R`); its donor contribution must be resolved or excluded by a prespecified rule before inference.

## Unresolved claim and falsifiable test

The unresolved claim is whether the macrophage-positive versus FLS-only contrast, and macrophage-positive versus macrophage-negative contrast, reveal a reproducible feature-level signature with donor-aware uncertainty. The exact primary comparisons are:

1. `condition = co-cultured with MerTK/CD206pos macrophages` versus `condition = not co-cultured`, restricted to `treatment = none`.
2. `condition = co-cultured with MerTK/CD206pos macrophages` versus `condition = co-cultured with MerTK/CD206neg macrophages`, restricted to `treatment = none`.

The analysis must use the 445 source feature rows, join only on exact `sample_id`, preserve the observed feature identifiers, and treat contributing donor/context—not each cell—as the uncertainty unit. A donor-aware paired/stratified contrast or contributing-donor random-effects model is the prespecified baseline, with condition/donor-preserving permutation inference. The ambiguous donor record is not silently assigned to a single donor; its handling is a readiness/interpretation decision. Pre-LPS and inhibitor records are mechanistic context, not independent causal replicates.

Supportive results would require a condition-specific signature with donor-aware uncertainty, separation from both controls, and no comparable signal in the negative-control contrast. Adverse results include no separation, reversal, or failure under donor/condition-preserving permutations. Inconclusive results include unresolved donor mapping, insufficient independent donor contexts, low detectability, or uncertainty too large to distinguish communication from composition or technical artifacts.

## Baseline, alternative, and deliverable

The simple baseline is a donor-aware paired/stratified feature contrast with donor-level uncertainty and condition-preserving permutation. The substantive alternative is a hierarchical/regularized model across the 445 measured features that borrows information across features and can reveal coordinated pathway-level structure lost by single-feature contrasts. It cannot establish direct ligand-receptor action or causality. The alternative is deferred unless the baseline establishes metadata integrity and adequate feature-level signal. Both use the same inputs, contrasts, donor-stratified split/permutation, outcome, and uncertainty evaluation.

The scientific deliverable is a fitted donor-aware contrast table and prespecified condition-specific signature test, with effect estimates, uncertainty, permutation results, negative-control behavior, and an explicit supportive/adverse/inconclusive interpretation. No result is claimed here.

## Missing evidence and limits

The assay is targeted and cannot support claims about unmeasured genes. Repeated context measurements and reused donors do not make cells independent biological replicates. Treatment, macrophage composition/ratio, batch, age/sex, cell count, and targeted-panel measurement are competing explanations. Expression association cannot establish direct target action, ligand-receptor causality, clinical transition, or treatment benefit; those require perturbation, independent experimental evidence, or another study. The one anomalous feature identifier and one explicit donor-metadata conflict are concrete limitations, not evidence of a biological result.

## Alternatives and seed disposition

The D3-M2 directional communication question is pursued because paired FLS-only and macrophage-negative controls are available. D3-M1 composition versus within-cell regulation is deferred because this targeted FLS assay does not resolve whole-tissue composition. D3-M3 persistence/remission is deferred because cross-sectional condition states do not establish longitudinal transitions. The learned alternative is retained as a substantive comparison, not selected merely for complexity.
