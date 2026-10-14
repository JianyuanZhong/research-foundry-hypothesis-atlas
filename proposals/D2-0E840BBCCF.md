> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: context-specific MerTK-inhibitor response in E-MTAB-8873

## Status

Provisional draft for episode 8. This is not an executed result, a selected candidate, or a claim of clinical benefit.

## Proposed relationship

In the available E-MTAB-8873 RA macrophage–fibroblast assay, a MerTK-inhibitor-associated transcriptional response will differ by the macrophage context (MerTK/CD206-positive versus MerTK/CD206-negative macrophages). The primary estimand is a donor-aware, condition-verified context-by-inhibitor interaction, not a generic mean-expression change. A secondary descriptive question is whether the interaction separates a fibroblast-linked harmful program from a macrophage-linked resolving/protective program.

## Evidence and unresolved claim

The inspected evidence supports that MerTK-positive synovial macrophage subsets are associated with remission and can induce repair responses in synovial fibroblasts [K1], that macrophage functional reprogramming can alter inflammatory mediator production in arthritis [K2], and that macrophage–fibroblast repair circuits are context-, timing-, and niche-dependent [K3]. These observations make context-dependent MerTK modulation a plausible therapeutic question.

The strongest claim the available evidence supports is only that this targeted assay can measure intervention-associated expression patterns under defined macrophage-coculture conditions while preserving the documented dependence structure. The unresolved claim is whether the inhibitor-associated pattern is context-specific after accounting for donor, condition, timing, composition, and measurement artifacts. No dataset-specific effect has been computed in this episode.

The available evidence does not establish that UNC106238 acts directly on MerTK, that the response is causal, that a “protective” program is preserved, or that any in-vitro pattern transfers to patients. Those claims require perturbation/mechanistic evidence, clinical adjudication, and independent validation.

## Concrete data binding

Use the read-only prepared E-MTAB-8873 files:
- counts: [internal dataset path]
- design: [internal dataset path]

The design has 33 records and the targeted counts have 445 measured feature columns. Join on sample_id. Required design fields are sample_id, donor_id, donor_status, condition, treatment, age, sex, tissue, cell_type, and source_metadata; retain cells and contributing-donor information. The source catalog records the original E-MTAB-8873 repository, idf, sdrf, and R1/R2/R5 matrix files and hashes in datasets/therapeutic_targets/README.md and binding-template.json. Do not infer independent replicates from the 33 samples: donor_id is repeated and mixed, and donor_status marks contributing-donor uncertainty.

## Falsifiable test

1. Audit exact counts/design and retain only contrasts with verified inhibitor, control, macrophage-context, and temporal labels.
2. Define macrophage-linked and fibroblast-linked programs from the 445 measured features without using unmeasured genes; retain source feature identifiers.
3. Fit a donor-aware additive baseline and compare it with a substantive context-by-inhibitor interaction model, using donor-clustered/permutation uncertainty or another dependence-aware method.
4. Treat a reproducible interaction with the prespecified direction as supportive; a null or reversed interaction as adverse to context specificity; unstable contrasts, missing controls, insufficient independent donor information, or feature-definition ambiguity as inconclusive.

## Method comparison and resource plan

The simple baseline is a donor-aware additive model for condition, treatment, and measured program expression. The substantive alternative adds the interaction and tests whether the inhibitor changes the macrophage-context contrast. This alternative can reveal a context-specific response that the additive baseline averages away, while also exposing whether an apparent effect is merely donor or composition structure. Both use the same inputs, target, split, and uncertainty evaluation. CPU is adequate for the planned tabular interaction analysis; no GPU is required. The future solver must newly fit both models, estimate the interaction and uncertainty, and produce the prespecified program-level and sample-level outputs. No full study result is claimed here.

## Outcomes and limits

Supportive results would justify a follow-up mechanistic study of the identified context-specific program. Adverse results would weaken the proposed specificity and favor a generic intervention, donor, or composition explanation. Inconclusive results would identify missing controls, inadequate independent units, or unstable feature definitions. Expression response is not direct target action, causality, protection, clinical efficacy, or patient benefit.

## References

[K1] Alivernini et al., “Distinct synovial tissue macrophage subsets regulate inflammation and remission in rheumatoid arthritis,” Nature Medicine 26:1295–1306 (2020), doi:10.1038/s41591-020-0939-8.
[K2] Wang et al., “Targeted phagocytosis of TNF-α by CAR macrophages restores immune homeostasis in arthritis,” Theranostics 16:9007–9029 (2026), doi:10.7150/thno.132172.
[K3] Mosallanejad et al., “Macrophages and the Tissue Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic Strategies,” Cells 15:1412 (2026), doi:10.3390/cells15151412.
