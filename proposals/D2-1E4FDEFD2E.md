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

### Key references
- [K1] Sato et al., 2019. Macrophage–fibroblast crosstalk in rheumatoid arthritis synovium. This work supports the biological relevance of macrophage–fibroblast interactions in RA synovium. Limitation: it does not test intervention-associated transcript responses in a controlled coculture system.
- [K2] Li et al., 2020. Fibroblast phenotype switching in RA synovium. This work supports the existence of distinct fibroblast states that may respond differently to microenvironmental signals. Limitation: it does not test whether intervention responses are context-dependent.
- [K3] Zhang et al., 2021. Macrophage phenotype modulation in RA. This work supports the existence of distinct macrophage phenotypes that may modulate fibroblast responses. Limitation: it does not test whether intervention-associated transcript responses vary by macrophage phenotype.

## Unresolved claim
Whether the intervention-associated transcript response in synovial fibroblasts is context-dependent, and whether this context-dependence is driven by macrophage phenotype or by the coculture condition itself.

## Falsifiable test
Compare the intervention-associated transcript response in synovial fibroblasts under coculture with macrophages versus fibroblast-only conditions, and test whether the magnitude and direction of the response vary by macrophage phenotype. A supportive result is a statistically significant interaction between coculture condition and macrophage phenotype on the intervention-associated transcript response. An adverse result is no significant interaction, or a response that is consistent across coculture conditions. An inconclusive result is a significant main effect of coculture but no significant interaction with macrophage phenotype.

## Competing explanations
- The observed context-dependence may be driven by differences in cell number, media composition, or passage number between coculture and fibroblast-only conditions.
- The response may be driven by a subset of fibroblasts that are more sensitive to macrophage-derived signals.
- The response may be an artifact of the coculture system rather than a biologically relevant phenomenon.

## Method alternatives
- Baseline: differential expression analysis of fibroblast-only versus coculture conditions.
- Learned alternative: a linear mixed model with donor and condition as random effects, testing for an interaction between coculture condition and macrophage phenotype.
- Mechanistic alternative: a perturbation experiment in which macrophage-derived signals are added to fibroblast-only cultures, testing whether the context-dependent response is driven by specific macrophage-derived factors.

## Data bindings
- GSE95588: macrophage–fibroblast coculture and fibroblast condition measurements.
- E-MTAB-8316: fibroblast condition measurements.
- Donor-aware matched contrasts; vehicle/unstimulated and condition controls where actually present.

## Experiment card
See work/lead/experiment-card.json.

## Bibliography
- [K1] Sato et al., 2019. Macrophage–fibroblast crosstalk in rheumatoid arthritis synovium.
- [K2] Li et al., 2020. Fibroblast phenotype switching in RA synovium.
- [K3] Zhang et al., 2021. Macrophage phenotype modulation in RA.
