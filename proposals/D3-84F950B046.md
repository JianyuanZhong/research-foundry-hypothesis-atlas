> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Directional macrophage-to-fibroblast communication in OA-like cocultures

Seed: D3-M2
Domain: Disease Mechanisms & Pathway Hypotheses
Status: hypothesis-stage proposal; no confirmatory analysis has been executed.

## Question and clinical importance

In osteoarthritis-like tissue, macrophages and fibroblast-like synoviocytes (FLS) can reinforce one another through paracrine signaling. The consequential unresolved question is whether a measured FLS response is better explained by directional macrophage-to-FLS communication or by an alternative, including endothelial-cell input, donor-specific baseline state, or simply changes in measured cell composition.

Resolving this matters because it changes the next mechanistic experiment and could inform whether anti-inflammatory strategies should target macrophage signaling, FLS intrinsic state, or tissue composition. It is not a treatment recommendation.

## Evidence opening

The seed points to paired coculture and inhibitor conditions in E-MTAB-8316 and E-MTAB-8873, plus GSE95588 coculture data. The available source catalog lists condition-specific RSEC matrices and design metadata, including macrophage-positive/negative and inhibitor conditions.

## Hypothesis

In osteoarthritis-like coculture systems, a measured fibroblast-like synoviocyte (FLS) response is better explained by directional macrophage-to-FLS communication than by endothelial-cell input, donor-specific baseline state, or measured cell-composition changes.

## Competing explanations

1. **Endothelial-cell input**: The observed FLS response may reflect paracrine signaling from endothelial cells present in the coculture, not macrophage-to-FLS communication.
2. **Donor-specific baseline state**: The FLS response may reflect a pre-existing donor-specific state rather than a coculture-induced change.
3. **Cell-composition changes**: The measured signal may reflect changes in the proportion of measured cell types rather than a within-cell response.
4. **Assay limitation**: E-MTAB-8873 is a targeted assay measuring only 445 features; unmeasured genes are unavailable and may be relevant.

## Falsifiable test

A donor-aware paired comparison of FLS gene expression between macrophage-positive and macrophage-negative coculture conditions, with inhibitor perturbation, should show a reproducible directional signal that is attenuated by the inhibitor. If the signal disappears or reverses with inhibitor, or is fully explained by donor baseline or composition, the hypothesis is falsified.

**Supportive outcome**: A reproducible directional FLS signal in macrophage-positive conditions that is attenuated by inhibitor, after accounting for donor baseline and composition.

**Adverse outcome**: No reproducible directional signal, or a signal that is fully explained by donor baseline or composition.

**Inconclusive outcome**: A signal that is present but not reproducible across donors, or an inhibitor effect that is inconsistent.

## Data bindings

- **E-MTAB-8316**: [internal dataset path]; metadata E-MTAB-8316.design.json. Four FLS donor clusters, six nested monocyte donors, twelve condition samples.
- **E-MTAB-8873**: [internal dataset path]; metadata E-MTAB-8873.design.json. Targeted assay; 445 measured feature columns.
- **GSE95588**: [internal dataset path]; metadata GSE95588_coculture_htseq_counts.design.json. Coculture r1/r2 includes earlier GSE57723 data and cannot count as independent validation.

## Method comparison

- **Baseline**: Donor-aware paired t-test or linear model on pseudobulk expression, with donor as a fixed effect.
- **Alternative**: A donor-aware mixed model with donor as a random effect, to account for nested donor structure.
- **Selection**: The mixed model is preferred for the nested donor structure, but the baseline is retained for transparency and comparison.

## Key references

- [K1] Directional macrophage-to-FLS communication in OA-like cocultures (seed D3-M2)
- [K2] E-MTAB-8316/8873 coculture and inhibitor conditions (data source)
- [K3] GSE95588 coculture data (data source)

## Limitations

- The assay registry reconciliation and inhibitor cleanliness require verification before causal claims.
- The targeted assay in E-MTAB-8873 measures only 445 features; unmeasured genes are unavailable.
- The coculture r1/r2 includes earlier GSE57723 data and cannot count as independent validation.
- No wet-lab validation has been performed.
