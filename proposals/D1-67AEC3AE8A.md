# Provisional hypothesis: discordant AKI recovery after an ICU landmark

Status: provisional draft for registration; no computed results are claimed.

## Proposed relationship

Among adult MIMIC-IV ICU patients with an acute kidney injury episode and a creatinine measurement at or near a prespecified 48-hour landmark, patients whose creatinine has improved but whose urine output remains low, or whose cumulative fluid balance remains positive, will have higher subsequent in-hospital death or persistent/worsening kidney dysfunction than patients with concordant creatinine and urine-output recovery. The comparison will adjust for pre-landmark illness severity and treatment.

The clinically useful claim is narrower than “creatinine is wrong.” Discordance may represent delayed clearance, ongoing tubular injury, fluid overload, or differences in measurement and monitoring. The experiment tests whether the discordant phenotype adds prognostic information beyond a creatinine-only recovery phenotype.

## Evidence and opening

This is a development of the expert seed “Asynchronous organ recovery” ([prior hypothesis]), which proposes that after circulatory stabilization, persistent impairment in one organ may predict later deterioration. A prior provisional child ([prior hypothesis]) narrowed that idea to discordant AKI recovery and identified the need for a leakage-safe landmark. The seed is expert-proposed and untested; it is not evidence that the hypothesis is true.

The available MIMIC-IV source is the read-only archive at
[internal dataset path]
([source checksum]), with archive members including:
- mimic-iv-3.1/hosp/admissions.csv.gz
- mimic-iv-3.1/hosp/patients.csv.gz
- mimic-iv-3.1/hosp/labevents.csv.gz
- mimic-iv-3.1/hosp/d_labitems.csv.gz
- mimic-iv-3.1/icu/icustays.csv.gz
- mimic-iv-3.1/icu/outputevents.csv.gz
- mimic-iv-3.1/icu/inputevents.csv.gz
- mimic-iv-3.1/icu/d_items.csv.gz
- mimic-iv-3.1/icu/chartevents.csv.gz

The catalog identifies these as MIMIC-IV tables hosp/admissions, hosp/patients, hosp/labevents, hosp/d_labitems, icu/icustays, icu/outputevents, icu/inputevents, icu/d_items, and icu/chartevents. The exact creatinine item IDs/units, output-event item IDs, fluid-balance construction, and row coverage must be verified against the table JSON headers and source rows before execution.

## Population, time and variables (to verify)

- Population: adults with a qualifying ICU stay and an AKI episode, restricted to stays with enough pre- and post-landmark observation; exact age and AKI criteria to be fixed from available fields.
- Landmark: 48 hours after the prespecified AKI onset/entry definition, with no post-landmark variable used to define exposure.
- Exposure: discordant recovery phenotype based on pre-landmark creatinine trajectory and urine-output/fluid-balance trajectory, versus concordant recovery.
- Outcomes: subsequent in-hospital death and persistent/worsening kidney dysfunction, with a prespecified follow-up window and censoring rules.
- Baseline adjustment: pre-landmark severity, demographics, admission context, renal support, vasopressor/fluid treatment, and measurement density where available.
- Join keys: patient_id and hospital/ICU stay identifiers as documented in the MIMIC table metadata; do not join across datasets.

## Falsifiable test and interpretation

Compare the discordant and concordant groups using a prespecified multivariable model and, if feasible, a landmarked survival analysis. Report effect estimates and uncertainty, not only significance.

- Supportive: discordant recovery has a reproducible adverse association beyond the creatinine-only baseline, with consistent direction in a held-out or temporal split and adequate event/coverage counts.
- Adverse: no clinically meaningful difference, or the association disappears after measurement-density and severity adjustment, weakening the proposed incremental prognostic claim.
- Inconclusive: sparse events, missing/irregular measurements, unstable item definitions, or wide intervals that do not exclude a meaningful effect.

A supportive result would establish prognostic association, not mechanism or causal benefit from changing fluid management. Mechanistic claims about tubular injury, delayed clearance, or fluid overload require additional clinical adjudication and/or another study.

## Method alternatives

Baseline: a prespecified creatinine-only recovery model with the same landmark, covariates, outcomes, split, and uncertainty evaluation.

Substantive alternative: a time-aware model using the pre-landmark sequence of creatinine, urine output, fluid balance, and treatment intensity (for example, a regularized survival model or a small sequence model), with the same patient split and held-out outcome evaluation. This can reveal whether timing and trajectory shape add information that a single landmark summary loses, while allowing calibration and uncertainty assessment. It is deferred until the exact item definitions and coverage are verified; no result is claimed.

## Missing evidence and next deliverable

The draft lacks verified exact item IDs/units, bounded cohort/event coverage, a complete inspected three-work bibliography, and computed results. The next deliverable is a bounded schema/coverage check and evidence acquisition for exactly three inspected works, followed by a substantive child only if the data support the proposed estimand.
