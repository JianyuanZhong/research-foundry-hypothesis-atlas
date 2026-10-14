> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: discordant AKI recovery beyond current severity

Status: provisional and untested. This is a research task, not a completed analysis; no cohort count, prevalence, or effect estimate is claimed.

## Proposed relationship

Among adults with an ICU stay and a prespecified creatinine-defined AKI episode who survive to a fixed 48-hour landmark, persistent creatinine improvement without concurrent urine-output improvement will be associated with higher subsequent risk of renal deterioration or in-hospital death than concordant recovery, after adjustment for the same landmark severity, treatment state, and observation intensity. The test is incremental prognostic information, not a causal mechanism, treatment effect, or proof of true renal recovery.

## Why this matters and what is unresolved

Creatinine and urine output can recover discordantly because they measure different dimensions of renal function and are affected by body composition, illness severity, fluid balance, and treatment. A creatinine-only recovery label could misclassify vulnerable patients. The unresolved claim is whether the discordant trajectory adds information beyond the patient's current state and measurement density. The strongest available evidence supports the measurement concern, not the proposed association.

## Falsifiable test and data boundary

The future Harbor experiment should construct a leakage-safe landmark cohort from the assigned read-only MIMIC-IV source, using the documented patient/encounter joins and time fields. It should define AKI, the 48-hour landmark, concordant versus discordant recovery, and subsequent renal deterioration/death from prespecified creatinine and urine-output measurements. A simple current-state baseline (landmark severity, treatment, and observation intensity) should be compared with a persistent-trajectory alternative using the pre-landmark sequence. Held-out evaluation, uncertainty, and sensitivity to measurement density are required.

Supportive results would show reproducible incremental discrimination/calibration for discordance beyond the matched current-state baseline, with uncertainty excluding a clinically negligible effect. Adverse results would show no incremental information, instability, or attenuation after measurement-density adjustment. Inconclusive results would include sparse outcomes/events, unstable estimates, or inability to define a reliable trajectory. None would establish causality or fluid status.

## Missing evidence and limitations

The exact MIMIC-IV archive members, table names, item IDs, joins, time fields, cohort counts, and outcome definitions still require verification from the read-only catalog/source files. No cohort or effect has been computed. Measured GFR/cystatin C, fluid-status adjudication, and treatment intent are unavailable or not yet verified and would be needed for stronger mechanistic or causal claims. Three inspected key works and a complete experiment card are not yet assembled for this provisional registration.
