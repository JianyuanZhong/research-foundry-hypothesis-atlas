> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# D3-M2 repair: directional macrophage–fibroblast communication in inflammatory synovial coculture

## Seed and question

Seed D3-M2 asks which competing macrophage–fibroblast or endothelial–fibroblast mechanism is distinguishable by perturbation. This repair preserves that question but makes the testable claim directional and donor-aware. The primary hypothesis is about macrophage-to-fibroblast signaling; endothelial–fibroblast communication is retained only as a secondary, non-primary comparison because the bound matrices do not provide a verified endothelial-cell component.

## Evidence-supported claim versus untested hypothesis

The inspected literature supports a broader claim: active rheumatoid synovium contains reciprocal stromal–myeloid communication, and a failed-resolution framework can explain persistence of inflammation [K1]. Fibroblast-derived IGFBP5 reduction has also been associated with pathogenic fibroblast states and altered macrophage polarization [K2]. A cross-tissue transcriptomic analysis supports shared myeloid-inflammatory programs but does not establish directionality in an RA coculture [K3].

The unresolved, falsifiable claim is narrower: in matched-donor inflammatory coculture, macrophage-derived ligand expression precedes or is associated with a reciprocal fibroblast receptor-response signature, more strongly than the reverse fibroblast-to-macrophage direction. This is a directional association/perturbation hypothesis, not a claim that co-expression proves causality.

## Data bindings

### E-MTAB-8873 (primary donor-aware coculture)

- Counts: `[internal dataset path]`
- Design: `[internal dataset path]`
- Use: targeted assay with 445 measured feature columns. Preserve transcript identifiers. Summarize each recorded FLS/coculture sample as pseudobulk.
- Required columns: transcript identifiers, sample identifiers, FLS/coculture condition labels, donor identifiers or contributing-donor mapping, and any recorded time/condition fields in the design JSON.
- Join key: sample identifier in counts to sample identifier in design; donor grouping must come from the design record, not from an inferred ID match.
- Limits: targeted panel only; unmeasured genes are unavailable. Multiple contributing or reused donors require explicit dependence modeling; ordinary donor t-tests are disabled.

### E-MTAB-8316 (paired inflammatory context)

- Counts: `[internal dataset path]`
- Design: `[internal dataset path]`
- Use: four FLS donor clusters, six nested monocyte donors, twelve condition samples. Average repeated context measurements within each donor/condition before paired exploratory inference.
- Required columns: gene/transcript identifiers, sample identifiers, FLS donor cluster, monocyte donor, condition, and time or replicate fields if present.
- Join key: sample identifier to design; donor nesting is explicit in the design.
- Limits: not twelve independent donors. Metadata cell-type labels and experimental readout must be reconciled with protocol before cell-specific claims.

### GSE95588 (coculture and time-series cross-check)

- Counts: `[internal dataset path]`
- Counts (time series): `[internal dataset path]`
- Designs: `[internal dataset path]` and `[internal dataset path]`
- Use: expression exploration and donor-aware inferential comparisons only after verified column-to-GSM/donor mapping. Resolve duplicate and date-like gene labels using feature-map records before naming targets; do not merge counts or guess corrections.
- Required columns: gene identifiers, GSM/sample identifiers, donor identifiers, coculture versus control labels, and time points d1–d4 in the time-series matrix.
- Join key: sample/GSM identifier in counts to design; donor grouping from design.
- Limits: coculture r1/r2 includes earlier GSE57723 data and cannot count as independent validation of that study.

## Hypothesis and competing explanations

Primary hypothesis: inflammatory macrophage–fibroblast coculture shows a directional signal from macrophage ligand expression to fibroblast receptor-response expression, with the macrophage-to-fibroblast direction stronger than the reverse.

Competing explanations:

1. Reverse direction: fibroblast-derived signals drive macrophage activation, so the observed association is fibroblast-to-macrophage.
2. Composition artifact: differences reflect cell-state composition or donor-specific baseline expression rather than directional communication.
3. Measurement artifact: targeted-panel coverage, duplicate labels, or pseudobulk aggregation obscures true ligand/receptor expression.
4. Selection artifact: donors or conditions selected for disease severity create a non-representative signal.
5. Timing artifact: without verified time ordering, expression differences cannot be interpreted as precedence.

## Donor-aware methods

1. Inspect each design JSON and assay registry before selecting contrasts. Do not claim independent donors unless the design supports it.
2. Build pseudobulk by sample and donor/condition, averaging repeated context measurements within each donor/condition where the design permits.
3. Model donor as a random effect or use donor-level paired contrasts; do not use ordinary donor t-tests.
4. For E-MTAB-8316, respect the four FLS donor clusters and six nested monocyte donors; pair within donor where possible.
5. For E-MTAB-8873, account for reused/contributing donors explicitly; if donor mapping is incomplete, restrict to exploratory description.
6. For GSE95588, verify column-to-GSM/donor mapping before inferential comparison; use time points only if the design records them.
7. Define ligand/receptor pairs from the measured 445-feature panel only; do not infer unmeasured genes.
8. Use a simple directional association baseline (paired donor-level correlation or difference in expression changes) and a donor-aware mixed model as the learned alternative. The mixed model can reveal donor-specific heterogeneity that the simple baseline loses.
9. Evaluate with donor-level bootstrap or permutation respecting donor dependence; report uncertainty intervals.
10. Compare the macrophage-to-fibroblast direction against the reverse direction using the same donors, features, and time/condition structure.

## Falsification criteria

Supportive: the macrophage-to-fibroblast directional association is consistently stronger than the reverse direction across donors and datasets, with donor-aware uncertainty intervals excluding the null and the effect not explained by composition or timing controls.

Adverse: the reverse fibroblast-to-macrophage direction is stronger, or the directional difference disappears after donor-aware adjustment, indicating the hypothesis is not supported.

Inconclusive: donor mapping is incomplete, the targeted panel lacks required ligand/receptor genes, or uncertainty intervals are too wide to distinguish directions. This would require additional data or a different assay, not a claim of refutation.

## Key references

[K1] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026. PMC13591627. Supports the broader claim of reciprocal stromal–myeloid crosstalk in RA synovium; does not establish directionality in a donor-matched coculture.

[K2] Bao L, Wang D, Wang P, et al. Reduced fibroblast-derived IGFBP5 is associated with pathogenic synovial fibroblast states and altered macrophage polarization in rheumatoid arthritis. Front Immunol. 2026. PMC13553944. Supports fibroblast–macrophage communication in RA; does not test directional precedence in a perturbation experiment.

[K3] Wei W, Pan B, Li R, et al. Cross-Tissue Transcriptomic Convergence Identifies a Leuko-Cyte-Shared, Myeloid-Enriched Inflammatory Program in Frailty and Osteoarthritis. Int J Mol Sci. 2026. PMC13467158. Supports shared myeloid-inflammatory programs across tissues; does not establish directional cell communication in RA coculture.

## What the experiment would establish

A supportive result would establish a donor-aware directional association in the bound coculture data, motivating a perturbation experiment (e.g., blocking a specific macrophage ligand) to test causality. It would not by itself prove a mechanism. An adverse result would redirect attention to fibroblast-to-macrophage signaling or composition artifacts. An inconclusive result would identify the missing donor mapping or panel coverage needed for a future study.

## Alternatives not chosen

- Endothelial–fibroblast comparison: deferred because the bound matrices do not provide a verified endothelial-cell component.
- Whole-tissue or spatial analysis: not available in the bound data; would require additional evidence acquisition.
- Wet-lab perturbation: not executed in this run; proposed as a next step if the computational directional association is supportive.
