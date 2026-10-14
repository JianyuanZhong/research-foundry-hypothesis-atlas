> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repaired hypothesis: discordant AKI recovery

## Proposed relationship
Among adult ICU patients with a creatinine-defined AKI episode, a 48-hour recovery pattern in which creatinine has improved but urine output has not will identify a higher risk of subsequent renal deterioration or death than a creatinine-only recovery label, after accounting for the same 48-hour severity and treatment state.

This is provisional and untested. It is a predictive/explanatory hypothesis about whether discordance adds clinically useful information; it is not a causal claim about fluid status or renal physiology.

## Concrete opening and unresolved claim
The expert seed observes that creatinine and urine output can recover discordantly and that creatinine-only recovery may miss persistent renal vulnerability. The unresolved claim is whether the discordant pattern is informative beyond the patient's current severity, rather than merely a marker of illness severity, measurement timing, or treatment intensity. A creatinine-only label loses the trajectory and the contemporaneous urine-output signal; a trajectory-based comparison can test whether the pattern contains incremental information.

## Data-bound study design
Dataset: MIMIC-IV core 3.1, snapshot `[source checksum]`, from the configured read-only archive `[internal dataset path]` ([source checksum]).

Population: adults (`hosp/patients.anchor_age >= 18`) in a first eligible ICU stay with an AKI episode defined from `hosp/labevents` creatinine values, joined by `subject_id` and `hadm_id`; retain one episode per patient using the earliest qualifying stay. The exact creatinine item ID, baseline/reference window, AKI threshold, and minimum observation requirement must be frozen from `hosp/d_labitems` and the source rows before analysis.

Landmark: 48 hours after the AKI onset/anchor, using only measurements and events with timestamps at or before that landmark. Require sufficient pre-landmark urine-output coverage and a post-landmark follow-up window. Do not use discharge, death, later labs, or later treatment as predictors. The landmark cohort is explicitly a selected, observed-recovery cohort; results are not generalizable to all AKI patients without a separate comparison.

Exposure: at the landmark, classify creatinine recovery versus no recovery using only pre-landmark creatinine, and urine-output recovery versus no recovery using pre-landmark urine output. Discordant recovery is creatinine improvement without urine-output improvement. A secondary continuous trajectory analysis will use the pre-landmark sequence of creatinine and urine output rather than a single cutoff.

Outcomes: subsequent renal deterioration (a prespecified creatinine/urine-output worsening or dialysis/renal replacement procedure, if the available procedure tables support it) and hospital death, measured after the landmark and before discharge/death. The exact outcome item IDs and timing rules are not yet frozen and must be verified from the source dictionaries and procedure tables.

Baseline: a simple landmark logistic or Cox model using current creatinine, pre-landmark urine output, age, sex, comorbidity proxies, and available severity/treatment covariates. Alternative: a trajectory-based model (for example, a regularized sequence model or prespecified trajectory features such as slopes, nadir, and persistence) using the same pre-landmark inputs and outcomes. Both models use identical patient splits, leakage-safe time windows, calibration and discrimination uncertainty, and a held-out validation set. The alternative is scientifically useful only if it reveals whether the pattern/persistence of discordance matters beyond the current values; a small predictive gain alone is not sufficient.

Falsification and interpretation: supportive evidence requires reproducible incremental calibration/discrimination and a prespecified directionally consistent association in held-out data, with uncertainty reported. Adverse evidence is no incremental information, reversal, or instability after severity adjustment. Inconclusive evidence includes insufficient discordant cases, sparse urine-output coverage, or wide confidence intervals. None establishes mechanism or treatment benefit. Cystatin C, measured GFR, reliable fluid balance, and clinical adjudication of AKI/recovery are unavailable or not yet verified and limit interpretation.

## Evidence status and next checks
The expert seed and its cited creatinine-versus-cystatin-C paper are not yet inspected here as hypothesis-specific evidence. Exact item IDs, outcome definitions, cohort counts, and feasibility have not been computed. The next bounded checks are dictionary/header inspection, a small cohort count/coverage diagnostic, and acquisition/inspection of three relevant public works. No numerical result is claimed.
