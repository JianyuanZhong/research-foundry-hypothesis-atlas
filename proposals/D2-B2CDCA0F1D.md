> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Evidence-complete hypothesis: context-specific MerTK-inhibitor response in E-MTAB-8873

## Status

This is a planned, evidence-bounded research task for episode 16. No E-MTAB-8873 effect estimate has been computed. This is not a claim of direct MerTK action, causality, protection, clinical efficacy, or patient benefit.

## Proposed relationship and clinical importance

In the available E-MTAB-8873 RA macrophage–fibroblast coculture assay, the MerTK-inhibitor-associated transcriptional response differs between MerTK/CD206-positive and MerTK/CD206-negative macrophage contexts. The primary estimand is a donor-aware, condition-verified context-by-inhibitor interaction, not a generic mean-expression change. A secondary descriptive question is whether the interaction separates a macrophage-linked resolving/repair-associated program from a fibroblast-linked inflammatory or harmful program.

Resolving this matters because a context-specific response would justify targeted mechanistic follow-up, whereas a generic response would redirect attention to treatment, donor, composition, or assay artifacts. The inspected literature supports biological plausibility but not this assay-specific effect: MerTK-positive synovial macrophage subsets have remission-associated signatures and can induce repair responses in synovial fibroblasts [K1]; macrophage reprogramming can alter inflammatory homeostasis in arthritis [K2]; and macrophage–fibroblast repair circuits are context-dependent and can become maladaptive [K3]. These works do not establish that UNC106238 acts directly on MerTK, that the response is causal, or that any pattern transfers to patients.

## Exact data binding and verified availability

Use read-only prepared files:
- Counts: [internal dataset path]
- Design: [internal dataset path]

The design is a JSON list of 33 records. Verified fields are sample_id, donor_id, donor_status, other_donor_id, age, sex, tissue, cell_type, condition, treatment, source_metadata, and cells. The counts TSV has a feature column plus 33 sample columns, for 445 measured feature rows; the first feature is ADAM17|NM_003183.5|Reference_end and source identifiers must be retained. Join counts to design on sample_id. The source catalog records the original E-MTAB-8873 repository, idf, sdrf, and R1/R2/R5 matrix files and hashes.

The design contains repeated and mixed donor identities and donor_status values requiring a contributing-donor model. Therefore the 33 samples are not independent replicates; do not use an ordinary donor t-test. The assay is targeted and pseudobulk; unmeasured genes are unavailable. No verified temporal field exists, so do not invent a time scale or claim a time-resolved effect.

## Falsifiable test

1. Audit exact contrasts using verified condition, treatment, macrophage-context, and available pre/post labels. Retain source feature identifiers and do not merge duplicate or date-like labels.
2. Define macrophage-linked and fibroblast-linked programs only from the 445 measured features, with a prespecified feature-definition audit and sensitivity analysis.
3. Fit a donor-aware additive baseline for condition, treatment, age, sex, tissue, cell_type, cells, and contributing-donor structure. Compare it with the prespecified context-by-inhibitor interaction model. Use donor-clustered or permutation uncertainty that respects repeated/mixed donors.
4. Add a composition negative control: standardize or stratify by cell_type and contributing-donor composition where the design permits, and compare with the unadjusted interaction. A composition-sensitive interaction that disappears under this control is evidence against specificity.
5. Add a within-context treatment negative control: compare inhibitor-associated changes with verified untreated/control contrasts in the same context and donor strata. A similar generic treatment effect across contexts weakens the specificity claim.
6. Report sample-level and program-level estimates, independent-donor support, missing/mixed-donor flags, and uncertainty. Do not select a favorable subgroup after seeing results.

Supportive evidence requires a reproducible prespecified interaction that remains directionally consistent after composition and treatment controls, with uncertainty adequate for the prespecified null. Adverse evidence is a null/reversed interaction, disappearance after composition adjustment, or a generic treatment effect indistinguishable across contexts. Inconclusive evidence includes unstable contrasts, missing controls, insufficient independent donor information, ambiguous feature definitions, or imprecise estimates. Supportive results justify a follow-up mechanistic study; they do not establish direct target action or clinical benefit.

## Baseline, substantive alternative, and resource plan

The simple baseline is the donor-aware additive model. The substantive alternative adds the context-by-inhibitor interaction and the two negative-control comparisons. It can reveal a context-specific response that the additive baseline averages away, while exposing whether an apparent effect is donor, composition, or generic-treatment structure. Both use the same inputs, target, split, and uncertainty evaluation. A mechanistically constrained program model may be used only if it is prespecified and evaluated on the same features; it is not justified by predictive gain alone.

CPU is adequate for this tabular analysis. The future solver must newly fit both models, estimate the interaction and uncertainty, and produce program-level and sample-level outputs. No full study result is claimed here.

## Missing evidence and claim boundaries

The assay lacks whole-tissue or cell-state-resolved measurements, an independent clinical cohort, temporal labels, and patient outcomes. Drug-associated expression does not identify direct target action. Direct-target, mechanistic, causal, and therapeutic claims require perturbation/mechanistic evidence, expert review, and independent validation.

## Alternatives not chosen

A generic predictive model is deferred because it would not distinguish context-specific biology from donor or treatment composition. A full neural sequence model is deferred because no verified longitudinal patient trajectory or temporal outcome is available; this is a dependency decision, not a blanket rejection of learned methods. Revisit if verified temporal or independent-unit data become available.

## Key references

[K1] Alivernini et al., “Distinct synovial tissue macrophage subsets regulate inflammation and remission in rheumatoid arthritis,” Nature Medicine 26:1295–1306 (2020), doi:10.1038/s41591-020-0939-8.
[K2] Wang et al., “Targeted phagocytosis of TNF-α by CAR macrophages restores immune homeostasis in arthritis,” Theranostics 16:9007–9029 (2026), doi:10.7150/thno.132172.
[K3] Mosallanejad et al., “Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies,” Cells 15:1412 (2026), doi:10.3390/cells15151412.
