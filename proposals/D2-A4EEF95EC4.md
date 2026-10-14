> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Intervention-specific protective-versus-pathogenic target selectivity

Seed: D2-T2. Parent: [prior hypothesis].

## Question and clinical importance

Does an intervention-associated transcript pattern selectively reduce a pathogenic fibroblast program while preserving a protective macrophage-linked state, in a way that is not explained by donor composition or stimulation? This matters because a target prioritized from an averaged intervention-associated signal may be misleading if the apparent selectivity is driven by donor-specific baseline differences, differential cell composition, or a general stimulation response. Resolving the question would change whether a target is pursued as context-specific, requires a cell-type-resolved intervention, or is deprioritized.

## Strongest currently supported claim

The strongest claim supported by the available evidence is that the configured sources contain macrophage/fibroblast-related conditions and intervention-associated transcript changes. The datasets are available as prepared counts and design metadata. This is descriptive evidence, not evidence that a specific transcriptomic signature is protective or pathogenic.

## Unresolved claim

Whether the proposed selectivity is an intervention-specific signal or a consequence of donor composition or stimulation.

## Data bindings

The four configured sources are GSE95588 coculture and d1d2d3d4 counts, E-MTAB-8316, E-MTAB-8873, and E-MTAB-8322. These are available as prepared counts and design metadata. The assay registry and source files must be inspected before claiming an enabled contrast. Mixed/reused donors require appropriate modeling; no universal age restriction. The targeted assay may not measure absent genes. The datasets are not a complete transcriptome.

## Design

A donor-aware linear mixed model with donor random effects and condition fixed effects, testing whether the intervention-associated pattern separates protective and pathogenic states. A negative-control gene set and a stimulation control are used to test for composition and stimulation artifacts.

## Competing explanations

The apparent selectivity may be driven by donor-specific baseline differences, differential cell composition, or a general stimulation response. The targeted assay may not measure absent genes. The datasets are not a complete transcriptome.

## Method comparison

The baseline is a donor-aware linear mixed model. A substantive alternative is a mechanistic model of macrophage-fibroblast interaction, which could reveal the direction and magnitude of the intervention effect on each cell type. The baseline loses information about the mechanism of the intervention effect. The alternative is deferred because it requires additional data and is not necessary for the current question.

## Falsification criteria

The hypothesis is falsified if the intervention-associated pattern does not separate protective and pathogenic states, or if the negative-control gene set or stimulation control shows that the apparent selectivity is driven by donor composition or stimulation.

## Supportive, adverse, and inconclusive outcomes

Supportive: the intervention-associated pattern separates protective and pathogenic states, and the negative-control gene set and stimulation control do not show that the apparent selectivity is driven by donor composition or stimulation. Adverse: the intervention-associated pattern does not separate protective and pathogenic states, or the negative-control gene set or stimulation control shows that the apparent selectivity is driven by donor composition or stimulation. Inconclusive: the intervention-associated pattern separates protective and pathogenic states, but the negative-control gene set or stimulation control is inconclusive.

## Key references

[K1] The first key reference supports the claim that macrophage and fibroblast programs can have opposing roles in fibrotic or inflammatory disease.

[K2] The second key reference supports the claim that a target prioritized from an averaged intervention-associated signal may be misleading if the apparent selectivity is driven by donor-specific baseline differences, differential cell composition, or a general stimulation response.

[K3] The third key reference supports the claim that a donor-aware linear mixed model with donor random effects and condition fixed effects can test whether the intervention-associated pattern separates protective and pathogenic states.

## Limitations

The targeted assay may not measure absent genes. The datasets are not a complete transcriptome. The hypothesis is not a proof of direct target action. The datasets are not a complete transcriptome. The hypothesis is not a proof of direct target action.
