> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: donor-aware macrophage-to-FLS communication in E-MTAB-8873

## Proposed relationship
In the E-MTAB-8873 synovial coculture experiment, macrophage exposure may induce a reproducible, condition-specific transcriptional response in synovial fibroblast-like cells (FLS) that is distinguishable from FLS-only and macrophage-negative controls after accounting for donor and repeated measurements. This is a hypothesis, not a computed result.

## Evidence and exact data opening
The dataset guide identifies E-MTAB-8873 as a targeted 445-feature assay with 12 condition samples, including FLS-only, macrophage-positive, macrophage-negative, pre-LPS, and inhibitor-associated conditions, with repeated context measurements and reused/multiple donors. The exact source is the E-MTAB-8873 prepared count matrices and design JSON listed in datasets/disease_mechanisms/README.md. The guide warns that pseudobulk does not make samples independent, that the panel is targeted, and that ordinary donor t-tests are disabled. No numerical result has been computed here.

## Unresolved claim and falsifiable test
Test whether the macrophage-positive versus FLS-only contrast, and the macrophage-positive versus macrophage-negative contrast, show a prespecified, donor-aware, condition-specific response rather than a generic donor, batch, or assay artifact.

1. Reconcile feature identifiers, sample names, condition labels, donor identifiers, and repeated-measurement context from the E-MTAB-8873 design JSON and source headers before naming any gene.
2. Use the verified sample-to-donor mapping and repeated-measurement structure. If no reliable donor key is present, stop the causal/donor-aware claim and report the mapping as unavailable.
3. Estimate the condition contrast in log-expression space, with donor as a nuisance/random effect or a donor-stratified permutation null; do not treat replicate samples as independent biological replicates.
4. Prespecify a direction and effect-size threshold, and require consistency across donors and a negative-control condition/feature comparison. Pre-LPS and inhibitor conditions are mechanistic context, not independent causal proof.

Supportive evidence: a reproducible condition-specific signature with donor-aware uncertainty and separation from controls. Adverse evidence: no separation, reversal, or failure to survive donor/condition permutations. Inconclusive evidence: unresolved mapping, low detectability, or uncertainty too large to distinguish communication from technical/composition artifacts.

## Baseline versus substantive alternative
Baseline: a donor-aware paired/stratified contrast for each prespecified feature, with donor-level uncertainty and permutation inference.

Substantive alternative: a hierarchical/regularized model across the 445 measured features that borrows information across features while retaining donor and condition effects. It could reveal coordinated pathway-level structure that single-feature contrasts lose, but it cannot establish direct ligand-receptor action or causality. Defer the alternative unless the baseline establishes metadata integrity and adequate feature-level signal.

## Missing evidence and limits
No result has been computed. The targeted panel cannot measure unlisted genes. Expression association cannot establish direct target action, ligand-receptor causality, or clinical transition. Reused donors and repeated samples require dependence-aware analysis. Clinical phenotype, treatment history, age, and independent external validation are not assumed available. Causal interpretation requires perturbation or independent experimental evidence.

## Next deliverable
Inspect the exact source headers/design JSON and verify feature/sample/donor mappings; then publish a child only if the mappings support the prespecified donor-aware test.
