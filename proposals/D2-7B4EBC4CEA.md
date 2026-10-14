> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# D2-T1 proposal: context-dependent intervention response

## Question and clinical importance
Does the intervention-associated transcript response of primary macrophages depend on whether they are exposed to synovial fibroblasts? This matters because reciprocal macrophage–fibroblast signaling can sustain rheumatoid arthritis inflammation and may explain why a drug that appears effective in isolated macrophages behaves differently in the synovial microenvironment [K1]. Resolving the question would inform whether therapeutic screening must include fibroblast-containing context and whether apparent drug resistance is context-dependent rather than purely target-mediated.

The hypothesis is observational: intervention-associated transcription differs between macrophage-only and macrophage–fibroblast context. The data do not establish direct target action, clinical efficacy, or causality.

## Exact data bindings

### E-MTAB-8316 (FLS readout)
- Raw matrix: `[internal dataset path]`, [source checksum].
- Prepared matrix: `[internal dataset path]`, [source checksum].
- Design: `[internal dataset path]`, [source checksum]; fields are `sample_id`, `donor_id`, `other_donor_id`, `condition`, `treatment`, `cell_type`, `age`, `sex`, `source_metadata`.
- Original metadata: `[internal dataset path]` and `E-MTAB-8316.sdrf.txt`; SDRF fields include `Source Name`, `Characteristics[individual]`, `Characteristics[specimen]`, `Factor Value[compound]`, `Factor Value[dose]`, and `Factor Value[specimen]`.
- Population and units: 12 samples from four verified FLS donor clusters (SA049, SA051, SA104, SA114) and six nested healthy monocyte donors. The readout is FLS transcript abundance after macrophage pretreatment. Paired intervention contrast is `condition=none` versus `condition=UNC106238` (250 µM), both under LPS; repeated context measurements are averaged within donor/condition before exploratory inference. Donors are not independent.

### GSE95588 (macrophage readout)
- Raw matrix: `[internal dataset path]`, [source checksum].
- Prepared matrix: `[internal dataset path]`, [source checksum].
- Feature map: `[internal dataset path]`, [source checksum]; 23,710 rows, with 28 date-like labels marked `ambiguous_do_not_assign_target`.
- Design: `[internal dataset path]`, [source checksum]; all donor IDs are unresolved.
- GSM metadata: `[internal dataset path]`, [source checksum]; original `samples.soft` is also bound. It provides accession, title, treatment, characteristics, BioSample and SRA links.
- Population and units: 70 macrophage samples, with columns encoding P1–P4, macrophage-only (`M`), macrophage+transwell (`MT`), and macrophage+transwell+fibroblast (`MTF`) contexts and drug suffixes. The planned primary contrast is the intervention-associated response in matched `MT` versus `MTF` columns; `M` is an unstimulated/context control. This is exploratory until column-to-GSM and donor mapping is verified. The r1/r2 coculture subset includes earlier GSE57723 data and is not independent validation.

## Estimand and analysis
For each intervention with a verified matched MT and MTF pair, define the response as the log2 fold-change from the corresponding unstimulated/control condition. The primary estimand is the context-by-intervention difference in response (MTF minus MT), summarized over donors/conditions with donor-aware uncertainty. Use a prespecified permutation or mixed-effects analysis that treats donor/condition as the dependence unit; do not treat 12 or 70 samples as independent donors.

Simple baseline: estimate each intervention’s MT and MTF response separately, then compare their difference using a donor-aware paired test or permutation. This directly answers whether context changes the observed response and is transparent.

Substantive alternative: fit a joint hierarchical model of intervention response across context, donor/condition, and gene, with a context-by-intervention interaction and shrinkage across interventions/genes. It can reveal a shared context-dependent program or intervention-specific reversal that the baseline loses, while borrowing information across repeated measurements. Evaluate with donor-blocked cross-validation and uncertainty intervals; compare the interaction estimate and held-out prediction of context contrast, not merely overall predictive accuracy.

## Interpretation and falsification
- Supportive: a reproducible context-by-intervention heterogeneity estimate with uncertainty excluding the prespecified null, consistent direction across available donors/conditions, and no evidence that it is explained by feature-map or batch artifacts.
- Adverse: no reproducible heterogeneity, or disappearance after donor/condition and feature-identity checks. This weakens the context-dependence claim; it does not prove drugs have no context effects in vivo.
- Inconclusive: unresolved donor mapping, insufficient matched contrasts, high uncertainty, or contradictory assay-specific results. This motivates metadata repair or a new study rather than a negative biological conclusion.

## Limitations and next evidence
E-MTAB-8316 is FLS readout after macrophage pretreatment, whereas GSE95588 is macrophage readout; cross-dataset claims must remain assay/context-specific. GSE95588 donor identity is unresolved, so donor-aware inference is gated on verified GSM-to-column mapping. The feature map must retain distinct source rows and must not merge ambiguous labels. No wet-lab target validation, clinical outcome, or direct mechanistic perturbation is available. A supportive result would justify a new donor-resolved experiment with direct target perturbation and clinical readouts; an adverse result would redirect screening toward isolated macrophage effects or other mechanisms.

## References
[K1] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026;17:1935792. doi:10.3389/fimmu.2026.1935792. PMCID:PMC13591627. Inspected full text supports the importance of reciprocal stromal–myeloid signaling and unresolved therapeutic implications.
[K2] Bao L, Wang D, Wang P, et al. Reduced fibroblast-derived IGFBP5 is associated with pathogenic synovial fibroblast states and altered macrophage polarization in rheumatoid arthritis. Front Immunol. 2026;17:1873778. doi:10.3389/fimmu.2026.1873778. PMCID:PMC13553944. Inspected full text supports a transwell fibroblast–macrophage coculture context and altered macrophage profiles, not a general intervention-response rule.
[K3] Philippon EML, van Rooijen LJE, Jongejan A, et al. Targeting inflammatory and angiogenic responses by small-molecule kinase inhibitors in a 3D macrophage-containing spheroid model of rheumatoid arthritis synovial tissue. Arthritis Res Ther. 2026;28:163. doi:10.1186/s13075-026-03849-z. PMCID:PMC13543596. Inspected full text supports context-aware therapeutic testing in a multicellular model, not validation of the present datasets.
