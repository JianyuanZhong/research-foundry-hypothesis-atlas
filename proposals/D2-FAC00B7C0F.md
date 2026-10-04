# Provisional hypothesis: macrophage–fibroblast context modifies the intervention-associated fibroblast transcript response

Seed: D2-T1
Status: provisional, evidence-bound draft; no inferential result has been computed yet.

## Proposed relationship

Among rheumatoid-arthritis fibroblast-like synoviocytes (FLS) exposed to the interventions represented in the available E-MTAB-8316 assay, the direction and magnitude of the intervention-associated transcript response will depend on the macrophage context (monocyte/macrophage phenotype or coculture condition), rather than being a context-independent FLS response. Operationally, a context-dependent effect is a reproducible interaction between intervention and macrophage context after accounting for donor pairing and repeated context measurements.

This is a hypothesis about an intervention-associated expression pattern, not a claim that any drug acts directly on a specific target or that the expression change is causal.

## Clinical importance and substantive advance

Target prioritization is consequential when an intervention appears effective in one inflammatory microenvironment but ineffective or potentially harmful in another. A context-dependent response would change which target/pathway is prioritized and would motivate stratified or combination strategies; a context-independent response would support a simpler target-level interpretation. The proposed advance is an explicit, donor-aware test of whether the apparent intervention response is stable across macrophage contexts, rather than treating a single assay contrast as target evidence.

## Existing evidence and unresolved claim

The prior episode design ([prior hypothesis] and its successors) identified E-MTAB-8316 as the available molecular assay and GSE95588 as a related source context, with donor/condition structure to be verified against the assay registry. The strongest supported claim at this checkpoint is only that these datasets contain the relevant intervention and macrophage-context variables for a planned comparison; no interaction estimate, biological validation, or clinical outcome has been computed. The unresolved claim is whether the intervention-by-macrophage-context interaction is reproducible and clinically informative.

## Exact data and planned experiment

Use the read-only therapeutic-targets source files and the exact E-MTAB-8316 assay members identified in datasets/therapeutic_targets/README.md and the assay registry. Required fields are the assay's sample identifiers, donor identifiers, intervention labels, macrophage/coculture context labels, condition/time fields, and gene expression matrix; joins must use the documented keys and preserve source-specific identities. Verify the registry before analysis; do not join datasets merely by matching IDs.

The primary comparison is an additive donor-aware model for intervention and macrophage context versus a model adding their interaction, with repeated measurements handled according to the verified design. A simple baseline is a donor-paired contrast summary with additive intervention and context effects; the substantive alternative is the interaction model. The alternative can reveal whether target prioritization changes by microenvironment, information the additive baseline necessarily loses. A prespecified held-out donor split, uncertainty intervals, and a negative control using context labels permuted within donor will test reproducibility and guard against donor/technical artifacts.

Supportive results require a reproducible interaction effect with uncertainty excluding the prespecified null, stable across the held-out donor split, and not explained by the negative control. Adverse results are a robust null interaction or a context-independent response, which would favor the simpler target interpretation. Inconclusive results include insufficient donors, unstable estimates, failed registry verification, or a result driven by one condition/technical batch; these require assay review or a larger independent cohort, not a favorable reinterpretation.

## Missing evidence and limits

The following are not yet established: exact registry-verified contrasts and column availability; the computed interaction estimate and uncertainty; whether expression changes map to direct target action; clinical efficacy or patient outcomes; independent biological validation; and whether macrophage context is measured at the same temporal resolution as intervention exposure. Clinical adjudication and perturbation/experimental follow-up would be required for causal or mechanistic conclusions. The three key inspected works and frozen receipts from the prior episode remain the literature basis; they are not being re-cited here as newly inspected evidence.
