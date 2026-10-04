> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional discordant AKI recovery hypothesis

Status: provisional, evidence repair checkpoint. This preserves the assigned question and does not claim cohort results, clinical conclusions, or completion of the reference contract.

## Proposed relationship

Among adults in their first MIMIC-IV ICU stay with a documented AKI episode who remain under observation at a prespecified 48-hour landmark, a creatinine-improved but urine-output-impaired phenotype is hypothesized to have worse subsequent in-hospital death and/or persistent or worsening kidney dysfunction than a concordant creatinine-and-urine-output recovery phenotype. This is a prognostic association, not a causal or mechanistic claim.

The leading rival is measurement and monitoring artifact: creatinine is sampled at clinician-selected times, urine output is recorded only when collection is available, and fluid balance is a treatment/monitoring summary. Residual illness severity, diuresis, renal replacement therapy, and fluid administration may also produce apparent discordance. The experiment must test incremental prognostic information beyond creatinine recovery and monitoring intensity, without interpreting an association as tubular injury or fluid-overload mechanism.

## Evidence currently supporting the framing

The inherited provisional candidate reports inspection of two accessible works: Tang et al. (2026, DOI 10.1007/s10238-026-02305-1, PMCID PMC13627203), supporting the clinical plausibility of evolving creatinine, urine output, fluid status, severity, and a strict landmark design while treating CRRT initiation as a treatment decision; and Yu et al. (2026, DOI 10.1007/s00134-026-08549-5, PMCID PMC13433398), relevant to standardized AKI diagnostic reporting and avoiding unsupported diagnostic claims. These are inherited source claims, not newly inspected here. They do not establish the proposed discordant-recovery association.

A third distinct inspected work on AKI recovery discordance, measurement/monitoring artifacts, or prognostic time-aware modeling is not yet available in this checkpoint. No inaccessible full text is claimed.

## Falsifiable test

Use only pre-landmark data to define exposure: creatinine trajectory, fixed-window urine output, and cumulative fluid balance. Compare discordant recovery with concordant recovery for post-landmark in-hospital death and a prespecified kidney outcome, with follow-up to discharge or a fixed 7-day window and explicit competing-risk handling. A simple adjusted model is the baseline; a time-aware trajectory model is the substantive alternative. Support requires incremental association with uncertainty, persistence after monitoring-intensity adjustment, and no material reversal in a fixed sensitivity analysis. Disappearance after adjustment, no incremental association, or reversal is adverse; an imprecise null is inconclusive.

## Exact data binding still required

The source archive is `[internal dataset path]`. The required members are expected to be `mimic-iv-3.1/icu/icustays.csv.gz`, `mimic-iv-3.1/hosp/admissions.csv.gz`, `mimic-iv-3.1/hosp/labevents.csv.gz`, `mimic-iv-3.1/icu/outputevents.csv.gz`, and `mimic-iv-3.1/icu/inputevents.csv.gz`. Their exact headers, table identifiers, join keys, creatinine item IDs, urine-output item IDs, units, and bounded cohort/outcome coverage must be verified against the catalog and source files before execution. No incompatible identifier namespaces may be joined.

## Missing evidence and next step

Complete acquisition and reading of at least one additional distinct accessible work, preserve exact source excerpts/receipts, and write key-references.json only if all three required works and receipts are complete. Then verify the exact MIMIC-IV schema/item/unit bindings and perform the bounded feasibility audit. No selection should occur while these dependencies remain unresolved.
