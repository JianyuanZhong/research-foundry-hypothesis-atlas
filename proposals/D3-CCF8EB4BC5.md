> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: donor-aware macrophage-to-FLS communication in E-MTAB-8873

## Proposed relationship

In the available E-MTAB-8873 synovial experiment, exposure of fibroblast-like synoviocytes (FLS) to macrophages may induce a reproducible, condition-specific transcriptional response that is distinguishable from FLS-only and macrophage-negative controls after accounting for donor/context and repeated measurements. This is a hypothesis, not a computed result.

## Evidence and exact data opening

The inherited candidate and dataset guide identify E-MTAB-8873 as a targeted 445-feature assay with 33 recorded condition samples, including FLS-only, macrophage-positive, macrophage-negative, pre-LPS, and inhibitor-associated conditions, with repeated context measurements and reused or multiple donors. The exact frozen inputs are:

- [internal dataset path]
- [internal dataset path]

The matrix is reported to have a feature column plus 33 sample columns; design records are joined by sample_id to matrix columns. Feature identifiers are source identifiers of the form gene|transcript|Reference_end and must be preserved unless a verified feature map is available. The design is reported to contain sample_id, donor_id, donor_status, condition, treatment, age, sex, tissue, cell_type, cells, and source_metadata. These inherited bindings still require direct re-verification in this episode; no numerical expression result has been computed here.

The closest inherited literature context is macrophage–FLS communication and MerTK-associated resolution in RA synovium, but those works motivate the question and do not establish this targeted assay's response or direct ligand-receptor causality. Three claim-linked inspected references and receipts are available from the parent candidate; they are not being treated as newly inspected or as evidence of a result.

## Unresolved claim and falsifiable test

Test whether the macrophage-positive versus FLS-only contrast, and macrophage-positive versus macrophage-negative contrast, yield a reproducible feature-level signature in the 33 condition records. Use a donor-aware paired/stratified contrast or contributing-donor random-effects model, with the contributing donor/context rather than cells as the uncertainty unit. Preserve condition and donor structure in permutation inference. Pre-LPS and inhibitor conditions are mechanistic context, not independent causal replicates.

Supportive evidence would be a condition-specific signature with donor-aware uncertainty, separation from both controls, and no comparable signal in the negative-control contrast. Adverse evidence would be no separation, reversal, or failure under donor/condition-preserving permutations. Inconclusive evidence includes unresolved donor mapping, insufficient independent donor contexts, low detectability, or uncertainty too large to distinguish communication from composition or technical artifacts.

## Baseline, alternative, and deliverable

The simple baseline is a donor-aware paired/stratified feature contrast with donor-level uncertainty and condition-preserving permutation. A substantive alternative is a hierarchical/regularized model across the 445 measured features that borrows information across features and can reveal coordinated pathway-level structure lost by single-feature contrasts. It cannot establish direct ligand-receptor action or causality. The alternative is deferred unless the baseline establishes metadata integrity and adequate feature-level signal. Both use the same inputs, contrasts, donor-stratified split/permutation, outcome, and uncertainty evaluation.

The scientific deliverable is a fitted donor-aware contrast table and prespecified condition-specific signature test, with effect estimates, uncertainty, permutation results, negative-control behavior, and an explicit supportive/adverse/inconclusive interpretation. No full study result is claimed.

## Missing evidence and limits

Direct re-verification of the matrix header, design records, sample_id join, feature identifiers, donor mapping, and condition/treatment values is pending. The assay is targeted and cannot support claims about unmeasured genes. Repeated context measurements and reused donors do not make cells independent biological replicates. Treatment, macrophage composition/ratio, batch, age/sex, cell count, and targeted-panel measurement are competing explanations. Expression association cannot establish direct target action, ligand-receptor causality, clinical transition, or treatment benefit; those require perturbation, independent experimental evidence, or another study.

## Alternatives and seed disposition

The D3-M2 directional communication question is pursued because paired FLS-only and macrophage-negative controls are available. D3-M1 composition versus within-cell regulation is deferred because this targeted FLS assay does not resolve whole-tissue composition. D3-M3 persistence/remission is deferred because cross-sectional condition states do not establish longitudinal transitions. The learned alternative is retained as a substantive comparison, not selected merely for complexity.
