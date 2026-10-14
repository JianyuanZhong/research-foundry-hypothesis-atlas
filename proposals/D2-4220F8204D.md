> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 18 working proposal: within-assay context-by-intervention repair

## Scientific question
Does the intervention-associated transcriptional response of primary macrophages differ when macrophages are exposed to synovial fibroblasts, and is that difference reproducible after accounting for the available sample-context structure? This is clinically important because reciprocal stromal–myeloid signaling can sustain rheumatoid arthritis inflammation and may explain why a drug response observed in isolated macrophages differs in a synovial microenvironment. The proposed claim is observational: it concerns intervention-associated transcription in the measured context, not direct target action, causal mediation, clinical efficacy, or an in vivo mechanism.

## Evidence boundary and substantive repair
The mature parent established a context-by-intervention question and exact E-MTAB-8316/GSE95588 bindings. A later source audit found zero exact feature-ID overlap between E-MTAB-8316 ENSG feature rows and GSE95588 source gene labels, with no admitted crosswalk. Therefore this repair removes any claim that an E-MTAB-8316-derived feature program can be applied to GSE95588. E-MTAB-8316 remains contextual evidence about FLS readout and the rationale for testing context; it is not used as a cross-assay feature map. The computable core is restricted to within-GSE95588 context contrasts.

## Exact available inputs
Primary matrix: `[internal dataset path]`, [source checksum]; header is `feature` plus 70 sample columns. Feature map: `[internal dataset path]`, [source checksum]; retain distinct source rows and do not merge ambiguous/date-like labels. Design: `[internal dataset path]`, [source checksum]; donor IDs are unresolved. GSM metadata: `[internal dataset path]`, [source checksum]; use accession/title/treatment/characteristics only where verified.

The primary computable population is the 13 GSE95588 columns with exact unique GSM-title matches identified from the design/GSM metadata; the remaining 57 columns are excluded from inferential claims because column-to-GSM/donor assignment is unresolved. The analysis must report the exact retained column list and matching rule before fitting. If fewer than two matched MT/MTF intervention pairs remain after this rule, the result is inconclusive rather than negative.

## Estimand and analysis
For each retained intervention with a verified matched macrophage-only/transwell (`MT`) and macrophage+transwell+fibroblast (`MTF`) pair, define response as log2 fold-change from the corresponding control/unstimulated condition, using the same source feature rows. The primary estimand is the context-by-intervention difference in response (MTF minus MT), summarized over the retained matched contrasts. Use a donor/condition-aware permutation or paired analysis where the verified metadata support it; otherwise treat the 13-column result as exploratory and use condition-blocked uncertainty, never 70 independent samples.

Simple baseline: estimate MT and MTF responses separately for each intervention and compare their difference with a paired/permutation test. This is transparent and directly tests whether context changes the observed response.

Substantive alternative: fit a hierarchical intervention-by-context model with shrinkage across interventions and a context-by-intervention interaction, using condition blocks and the verified repeated-measurement structure. It can reveal a shared context-dependent response versus intervention-specific reversal, information the baseline loses. Evaluate the interaction estimate and uncertainty, and held-out context contrasts using condition-blocked splits; do not select the alternative solely for a small predictive gain.

## Outcomes and falsification
Supportive: reproducible context-by-intervention heterogeneity with uncertainty excluding the prespecified null, consistent direction across retained matched contrasts, and no explanation by feature ambiguity, sample assignment, or batch/condition artifacts. This supports a context-dependent transcriptional association and motivates a donor-resolved perturbation study.

Adverse: no reproducible heterogeneity, or disappearance after feature-identity and condition checks. This weakens the context-dependence claim but does not prove absence of in vivo context effects.

Inconclusive: fewer than two matched pairs, unresolved column-to-GSM/donor mapping, high uncertainty, contradictory retained results, or inability to distinguish context from batch. This requires metadata repair or a new experiment, not a biological negative.

## Method comparison and compute
The baseline and hierarchical alternative answer the same scientific question on the same retained inputs. The baseline is CPU-sufficient; the alternative is a small tabular hierarchical fit, also CPU-sufficient within the future solver envelope. No GPU is required. The actual deliverable is the fitted baseline and alternative, retained-column audit, interaction estimate with uncertainty, condition-blocked held-out evaluation, and an interpretation tied to supportive/adverse/inconclusive criteria.

## Demonstration dispositions
The natural-history transformer demonstration is not pursued because the configured data lack its longitudinal patient histories and the question is a molecular intervention-context contrast. The cancer multimodal demonstration is not pursued because chest images and the main article are unavailable; a lab-only adaptation would not answer this question. The Bayesian longitudinal demonstration is not pursued because genetics and longitudinal trajectories are unavailable; its latent-trajectory idea is not needed for the paired assay comparison.

## References
[K1] Wei W, Xu J. Failed resolution as a mechanistic basis of difficult-to-treat rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging resolution-restoring therapies. Front Immunol. 2026;17:1935792. doi:10.3389/fimmu.2026.1935792. PMCID:PMC13591627. Abstract/Introduction inspected; supports reciprocal stromal–myeloid signaling and unresolved therapeutic implications, not this dataset's contrast.
[K2] Bao L, Wang D, Wang P, et al. Reduced fibroblast-derived IGFBP5 is associated with pathogenic synovial fibroblast states and altered macrophage polarization in rheumatoid arthritis. Front Immunol. 2026;17:1873778. doi:10.3389/fimmu.2026.1873778. PMCID:PMC13553944. Abstract and methods/results passages inspected; supports context-dependent macrophage profiles, not a general intervention-response rule.
[K3] Philippon EML, van Rooijen LJE, Jongejan A, et al. Targeting inflammatory and angiogenic responses by small-molecule kinase inhibitors in a 3D macrophage-containing spheroid model of rheumatoid arthritis synovial tissue. Arthritis Res Ther. 2026;28:163. doi:10.1186/s13075-026-03849-z. PMCID:PMC13543596. Abstract and results inspected; supports context-aware therapeutic testing, not validation of the present datasets.
