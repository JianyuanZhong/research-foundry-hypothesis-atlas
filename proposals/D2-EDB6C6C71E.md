> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# D2-T1: Intervention-associated transcript response in macrophage–fibroblast context

## Question
Does the intervention-associated transcript response in synovial fibroblasts depend on the presence and phenotype of co-cultured macrophages?

## Hypothesis
The intervention-associated transcript response in synovial fibroblasts is context-dependent: it differs when fibroblasts are co-cultured with macrophages versus cultured alone, and the magnitude and direction vary by macrophage phenotype.

## Scientific value
If intervention responses are context-dependent, single-cell-type screening may miss effects that depend on the microenvironment. This would affect prioritization of fibroblast versus macrophage targets and the interpretation of drug response in RA synovium.

## Evidence and closest inspected work
The available GSE95588 and E-MTAB-8316 sources contain macrophage–fibroblast coculture and fibroblast condition measurements, but they are not independent donor-level validation sets. The closest inspected works establish that macrophage–fibroblast crosstalk is relevant to synovial disease and fibrotic remodeling, while leaving open whether an intervention-associated transcript response is context-dependent in the available assay.

[K1] A 2026 Frontiers in Immunology review frames persistent rheumatoid arthritis as a failed-resolution niche in which pathogenic fibroblast and macrophage states form a self-sustaining stromal–myeloid circuit. It supports the biological relevance of reciprocal fibroblast–macrophage signaling and motivates resolution-restoring or crosstalk-directed interventions. It does not establish that a specific intervention-associated fibroblast transcript response depends on macrophage phenotype in the available assay.

[K2] A 2026 Frontiers in Immunology study reports reduced fibroblast-derived IGFBP5 in pathogenic synovial fibroblast states and shows that IGFBP5 overexpression attenuates aggressive fibroblast features and alters macrophage polarization in a Transwell coculture system. It supports fibroblast-to-macrophage communication and a possible therapeutic node, but it does not test whether an intervention-associated fibroblast transcript response is context-dependent across macrophage phenotypes.

[K3] A 2026 Signal Transduction and Targeted Therapy study demonstrates that BCL9 inhibition reprograms macrophage–fibroblast crosstalk in pulmonary fibrosis, suppressing M2 polarization through a MerTK–ERK–SPP1 axis and promoting a myogenic-to-lipogenic fibroblast switch. It supports the principle that macrophage state can determine fibroblast phenotype after intervention, but it is a different disease and cell system and does not establish the proposed context-dependence in RA synovial fibroblasts.

## Unresolved claim
The exact mechanism by which an intervention-associated transcript response in synovial fibroblasts depends on the presence and phenotype of co-cultured macrophages is not yet established.

## Falsifiable test
If the intervention-associated transcript response is context-dependent, then fibroblast transcriptomic changes under the intervention will differ significantly between coculture and fibroblast-alone conditions, and the direction or magnitude will vary with macrophage phenotype. A null result with no difference between coculture and fibroblast-alone conditions, or no phenotype-specific pattern, would be adverse to the hypothesis. Inconclusive results would include insufficient donor-level replication, unresolvable donor/condition mapping, or failure to separate technical from biological variation.

## Data and assay bindings
- GSE95588 coculture and fibroblast condition matrices: [internal dataset path] and [internal dataset path]
- E-MTAB-8316 matrix and design: [internal dataset path] and [internal dataset path]
- Required columns: gene identifiers, sample identifiers, donor identifiers, condition labels, and cell-type labels. Join keys are sample-to-donor and sample-to-condition mappings in the design files. Time fields are condition labels where present.
- Limits: Four FLS donor clusters, six nested monocyte donors, and twelve condition samples in E-MTAB-8316. Average repeated context measurements within each donor/condition before paired exploratory inference. No twelve-independent-donor claim. Metadata cell-type labels and experimental readout must be reconciled with protocol before cell-specific claims.

## Competing explanations
- The observed difference may reflect donor composition rather than macrophage phenotype.
- The observed difference may reflect technical variation in coculture versus fibroblast-alone preparation.
- The observed difference may reflect a general stress response to coculture rather than a specific intervention-associated effect.
- The observed difference may reflect an off-target effect of the intervention rather than a direct target action.

## Method alternatives
- Baseline: donor-aware paired comparison of fibroblast-alone versus coculture conditions, with vehicle/unstimulated controls where actually present.
- Learned alternative: a donor-aware linear mixed model or regularized regression that includes macrophage phenotype as a covariate, to estimate context-specific intervention effects. This could reveal whether the intervention effect is modified by macrophage phenotype, which the baseline paired comparison cannot estimate directly.
- Selection: the baseline is sufficient for the initial exploratory test. The learned alternative is deferred until donor-level replication and condition mapping are verified.

## Experiment card
See experiment-card.json for the life-science-experiment-card-v1 record.

## Key references
- [K1] Frontiers in Immunology, 2026. Failed-resolution framework for persistent rheumatoid arthritis.
- [K2] Frontiers in Immunology, 2026. Reduced fibroblast-derived IGFBP5 and macrophage polarization in RA.
- [K3] Signal Transduction and Targeted Therapy, 2026. BCL9 inhibition and macrophage–fibroblast crosstalk in pulmonary fibrosis.
