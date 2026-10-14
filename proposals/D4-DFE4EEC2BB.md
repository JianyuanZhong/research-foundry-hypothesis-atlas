> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: body-fat distribution separates metabolic from functional/fall risk trajectories

## Status

This is a provisional, data-bound research hypothesis, not an observed result. No association, model performance, or clinical conclusion has been computed in this episode. The proposal is registered before the full schema and literature checks are completed.

## Proposed relationship

Among UK Biobank participants with baseline body-composition MRI and subsequent follow-up, at similar total adiposity, higher visceral fat may be more specifically associated with subsequent metabolic disease, whereas higher posterior-thigh muscle fat infiltration (MFI) may be more specifically associated with subsequent functional decline or falls. The substantive question is whether fat distribution identifies distinct downstream trajectories rather than merely predicting a generic health-risk score.

This matters clinically because a positive result could justify targeted body-composition assessment and separate risk pathways, while a null result would argue against treating visceral fat and muscle-fat infiltration as clinically interchangeable. The design does not establish mechanism or treatment benefit.

## Grounding and evidence boundary

The opening is grounded in the expert seed [prior hypothesis] ([starting question]), which proposes this divergence and identifies candidate UKB fields including 21085, 23355/23356, 22403/22404, 23099, 46/47, 2296, 30750, and diagnosis fields 41270/41280. The seed is source material, not evidence that the hypothesis is true. Its cited background has not been independently inspected yet, and no full-text or supplementary method is being claimed as read.

The exact source paths, archive members, table names, columns, joins, and temporal fields still require verification against datasets/README.md, the population_multiomics guide, and the complete catalog. The prior board contains related UKB body-composition candidates, but this draft does not treat their feasibility counts or references as results.

## Planned computable experiment

The future Harbor experiment will use only the UKB namespace and documented same-namespace joins on participant ID (eid). The baseline index will be the first available assessment with the required body-composition measurements; outcomes will be first recorded events after that index within a prespecified follow-up window. The population will require complete exposure measurements or a prespecified missingness rule, and will exclude events already present at baseline.

The primary comparison will be a simple total-adiposity model versus a prespecified body-composition model adding visceral fat and posterior-thigh MFI. Outcomes will include a metabolic composite (for example, incident diabetes/metabolic disease fields) and a functional/fall composite, with exact field definitions frozen after catalog inspection. The analysis will report estimates with uncertainty, calibration/discrimination or trajectory summaries, overlap/missingness counts, and sensitivity analyses for measurement timing and selection into MRI. A falsification check will test whether the proposed divergence disappears after conditioning on baseline severity and whether the direction is stable in a held-out split.

Supportive evidence would be a reproducible, uncertainty-qualified divergence in held-out or temporally ordered analyses, with the composition model explaining outcome-specific associations beyond total adiposity. Adverse evidence would be no outcome-specific divergence, reversal, or instability across prespecified sensitivity analyses. Inconclusive evidence would be insufficient event support, poor overlap, or uncertainty compatible with both the proposed and rival explanations.

## Strongest rival and limits

The strongest rival is that apparent divergence reflects baseline severity, selection into MRI, ascertainment of outcomes, or the timing of measurements rather than distinct biological pathways. Available data may not distinguish biological mechanism from these artifacts. Clinical adjudication, treatment data, and external validation would be required for stronger clinical or causal claims.

## Method comparison

The simple baseline is an adjusted model using total adiposity and key demographics/timing variables. The substantive alternative is a prespecified composition model adding visceral fat and MFI, with outcome-specific estimates and uncertainty. This alternative can reveal whether fat distribution carries information lost by total adiposity, rather than merely improving prediction. A more flexible learned or mechanistic model is deferred unless the bounded comparison supports it; no GPU or complex model is required for this provisional question.

## Actual deliverable

The future solver must newly fit the baseline and composition models, produce cohort/overlap/event counts, estimates with uncertainty, held-out or temporally ordered evaluation, and classify the conclusion as supportive, adverse, or inconclusive. Completion is established by those computed outputs and a conclusion linked to them, not by readiness or a planned analysis.
