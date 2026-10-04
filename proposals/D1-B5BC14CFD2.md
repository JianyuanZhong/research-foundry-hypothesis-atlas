> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repair draft: discordant AKI recovery

Status: provisional child of [prior hypothesis]. This is a hypothesis and design checkpoint, not a completed analysis or selection.

## Proposed relationship

Among adults in their first MIMIC-IV ICU stay with a documented AKI episode who remain observable at a prespecified 48-hour landmark, creatinine improvement accompanied by impaired urine output will have worse subsequent in-hospital death and/or persistent or worsening kidney dysfunction than concordant creatinine-and-urine-output recovery. The estimand is prognostic, not causal.

The leading rival is measurement and monitoring artifact: creatinine sampling is clinician-selected, urine output is observed mainly when catheterized or actively collected, and fluid balance is a treatment/monitoring summary. A second rival is residual illness severity and treatment selection. The experiment must test incremental prognostic information beyond monitoring intensity and must not infer tubular injury, fluid-overload mechanism, or treatment benefit from association.

## What is supported and what remains untested

The inherited candidate contains two inspected works supporting the clinical plausibility of using evolving creatinine, urine output, fluid status, and severity in AKI assessment, and the need for standardized diagnostic reporting. It does not establish the discordant-recovery association. The third required inspected key reference and its frozen receipt remain incomplete at this checkpoint. Exact MIMIC-IV table identifiers, item IDs, units, joins, and bounded cohort/event counts also remain to be verified. No cohort counts, model outputs, or clinical conclusions are claimed.

## Data-bound experiment

Source archive: [internal dataset path]

Expected members, subject to catalog/header verification:
- icu/icustays.csv.gz: stay/admission identifiers, adult age, ICU admission/discharge timing.
- hosp/admissions.csv.gz: hospital identifiers, admission/discharge timing, death and in-hospital outcomes.
- hosp/labevents.csv.gz: creatinine result, item identifier, units, and timestamp.
- icu/outputevents.csv.gz: urine-output event identifier, quantity, units, and timestamp.
- icu/inputevents.csv.gz: input event identifier, quantity, units, and timestamp for fluid balance.

The exact documented stay_id/had_id relationships, creatinine item ID(s), urine-output item ID(s), unit conventions, and outcome fields must be verified before execution. No incompatible identifier namespaces may be joined. A bounded audit must count adult first ICU stays, AKI-eligible stays, 48-hour landmark survivors, and post-landmark outcome coverage before thresholds are fixed.

Time origin is ICU admission. Exposure uses only pre-landmark data: creatinine trajectory, fixed-window urine output, and cumulative fluid balance. The primary comparison is creatinine-improved/urine-output-impaired versus concordant recovery; fluid balance is secondary/stratified. Outcomes are in-hospital death and a prespecified post-landmark kidney outcome, with follow-up through discharge or a fixed 7-day window and explicit competing-risk handling.

## Baseline versus substantive alternative

Baseline: prespecified logistic or cause-specific Cox model using age, sex, admission type, pre-landmark severity, creatinine value/trajectory, urine-output category, fluid-balance category, and monitoring intensity. This is the interpretable primary test of incremental discordance information.

Alternative: a time-aware landmark model using ordered pre-landmark creatinine, urine-output, and fluid-balance trajectories (for example discrete-time survival or regularized recurrent/functional modeling), with the same patient split, outcome, calibration, and uncertainty evaluation. It can reveal whether sequence and slope matter beyond a single landmark category; it cannot establish mechanism. Compare discrimination, calibration, and bootstrap uncertainty on held-out data. CPU is appropriate for the baseline; GPU is optional only if trajectory fitting is materially slower.

Supportive results require a prespecified incremental association with uncertainty, persistence after monitoring-intensity adjustment, and no material reversal in fixed sensitivity analyses. Adverse results include no incremental association, disappearance after monitoring adjustment, or reversal. An imprecise null is inconclusive. Clinical adjudication of AKI, true recovery, fluid overload, and treatment indication is unavailable and is required for stronger mechanistic or management claims.

## Missing evidence and next step

1. Verify exact catalog/source headers, joins, item IDs, units, and bounded cohort/event coverage.
2. Complete the third inspected key reference with an exact frozen receipt and attach exactly three inspected sources plus key-references.json before selection.
3. Fix thresholds and outcomes before exploratory outcome analysis, then run the baseline and time-aware comparison with uncertainty and falsification checks.
