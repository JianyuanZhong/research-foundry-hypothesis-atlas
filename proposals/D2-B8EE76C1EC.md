> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# D2-T1: Intervention-associated transcript response in macrophage–fibroblast context

## Question
Does the intervention-associated transcript response in synovial fibroblasts depend on the presence and phenotype of co-cultured macrophages?

## Hypothesis
The intervention-associated transcript response in synovial fibroblasts is context-dependent: it differs when fibroblasts are co-cultured with macrophages versus cultured alone, and the magnitude and direction vary by macrophage phenotype.

## Scientific value
If intervention responses are context-dependent, single-cell-type screening may miss effects that depend on the microenvironment. This would affect prioritization of fibroblast versus macrophage targets and the interpretation of drug response in RA synovium.

## Evidence and closest inspected work
The available GSE95588 and E-MTAB-8316 sources contain macrophage–fibroblast coculture and fibroblast condition measurements, but they are not independent donor-level validation sets. The closest inspected works establish that macrophage–fibroblast crosstalk is relevant to synovial disease and fibrotic remodeling, while leaving open whether an intervention-associated transcript response is context-dependent.

[K1] Macrophage-fibroblast crosstalk in rheumatoid arthritis synovium: evidence for context-dependent transcriptomic responses.
[K2] Fibroblast activation and macrophage phenotype in fibrotic remodeling: implications for therapeutic target prioritization.
[K3] Intervention-associated transcriptomic responses in synovial fibroblasts: donor-aware design and assay considerations.

## Unresolved claim
The exact mechanism by which the intervention-associated transcript response depends on the cellular context is not yet established.

## Falsifiable test
If the intervention-associated transcript response is context-dependent, then the transcriptomic effects of the intervention on synovial fibroblasts will differ significantly when fibroblasts are co-cultured with macrophages versus when they are cultured alone, and the magnitude and direction of the response will vary by macrophage phenotype (e.g., MerTK/CD206-positive vs. negative, LPS-stimulated vs. unstimulated).

## Data bindings
- GSE95588: macrophage–fibroblast coculture measurements
- E-MTAB-8316: fibroblast condition measurements
- Assay registry: verified contrasts for macrophage phenotype and fibroblast condition

## Method alternatives
- Baseline: donor-aware matched contrasts with vehicle/unstimulated controls
- Learned alternative: context-aware model that predicts fibroblast transcriptomic response from macrophage phenotype and intervention

## Competing explanations
- The observed context-dependence may reflect differences in cell number, viability, or culture conditions rather than true biological crosstalk.
- The intervention-associated response may be driven by a subset of fibroblasts that are not representative of the bulk population.

## Supportive, adverse, and inconclusive outcomes
- Supportive: significant context-dependent transcriptomic response with consistent direction across donors.
- Adverse: no significant difference in transcriptomic response between coculture and single-cell conditions.
- Inconclusive: insufficient donor-level replication or assay variability to resolve the question.

## Expert questions
1. What is the minimal macrophage phenotype that drives context-dependent fibroblast responses?
2. Can the context-dependent response be reproduced in an independent donor-level validation set?
3. What is the clinical relevance of the context-dependent transcriptomic response for therapeutic target prioritization?
