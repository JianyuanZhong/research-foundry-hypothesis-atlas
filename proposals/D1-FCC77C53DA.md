> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repair: discordant AKI recovery in MIMIC-IV

Status: provisional child of [prior hypothesis]. No cohort counts, model results, or clinical conclusions are claimed.

## Hypothesis

Among adults in their first MIMIC-IV ICU stay who have a documented AKI episode and survive/remain under observation through a prespecified 48-hour landmark, a creatinine-improved but urine-output-impaired phenotype will have worse subsequent in-hospital death and/or persistent or worsening kidney dysfunction than a concordant creatinine-and-urine-output recovery phenotype. The comparison is prognostic, not causal.

The strongest rival explanation is that discordance is not a biological recovery phenotype but a measurement/monitoring artifact: creatinine is sampled at clinician-selected times, urine output is recorded only when a catheter or bedside urine collection is present, and fluid balance is a treatment/monitoring summary rather than a direct organ state. A second rival is residual illness severity and treatment selection: sicker patients may have more invasive monitoring, diuresis, renal replacement therapy, or fluid administration, producing apparent discordance. The experiment must therefore distinguish incremental prognostic information from a monitoring-intensity proxy and must not infer tubular injury or fluid-overload mechanism from association.

## Evidence inspected

- Tang et al., 2026, “An interpretable machine learning model for early prediction of subsequent observed CRRT initiation in patients with sepsis-associated acute kidney injury,” DOI 10.1007/s10238-026-02305-1, PMCID PMC13627203. Full-text XML was acquired and inspected at source ID [source checksum]. Its abstract and introduction support that serum creatinine, AKI stage, urine output, fluid status, severity, and other evolving measures are used in real-world CRRT assessment, while CRRT initiation is a treatment decision rather than an objective necessity. It also demonstrates a strict 24-hour landmark design and warns against interpreting prediction as treatment indication or benefit. This supports the clinical plausibility and temporal framing, not the proposed discordant-recovery association.
- Yu et al., 2026, “STARDaki: a consensus-based STARD extension for standardized reporting of diagnostic accuracy in acute kidney injury,” DOI 10.1007/s00134-026-08549-5, PMCID PMC13433398. Full-text XML was acquired and inspected at source ID [source checksum]. It is relevant to standardized AKI diagnostic reporting and the need to avoid unsupported diagnostic claims; it does not establish the proposed prognostic discordance.
- A third required inspected work was not completed because the checkpoint paused acquisition. Search results for a MIMIC-IV 48-hour AKI landmark study were observed, but they are not treated as inspected evidence or as a substitute for a frozen receipt.

The required key-references.json and three frozen source snapshots are therefore incomplete for this provisional registration. The two inspected sources are available in the frozen evidence store; no unavailable full text is claimed.

## Proposed data-bound experiment

Source archive: `[internal dataset path]`.

Required MIMIC-IV members, to be verified against the catalog and source headers before execution:
- `mimic-iv-3.1/icu/icustays.csv.gz`: ICU stay identifiers, admission/discharge times, adult age, and ICU timing.
- `mimic-iv-3.1/hosp/admissions.csv.gz`: hospital admission identifier, admission/discharge times, death and in-hospital outcome fields.
- `mimic-iv-3.1/hosp/labevents.csv.gz`: creatinine measurements, item identifiers, result units, and timestamps.
- `mimic-iv-3.1/icu/outputevents.csv.gz`: urine-output event identifiers, quantities, units, and timestamps.
- `mimic-iv-3.1/icu/inputevents.csv.gz`: fluid/input event identifiers, quantities, units, and timestamps for cumulative fluid balance.

Join keys must be verified in the catalog/source headers, expected to be the documented MIMIC-IV `stay_id`/`had_id` relationships; no incompatible identifier namespaces may be joined. The exact admissions table identifier, creatinine item ID(s), urine-output item ID(s), and input/output unit conventions remain to be verified. A bounded feasibility audit must count adult first ICU stays, AKI-eligible stays, 48-hour landmark survivors, and post-landmark outcome coverage before choosing thresholds.

Time origin is ICU admission. The primary landmark is 48 hours after ICU admission, with a prespecified tolerance only if it is fixed before outcome analysis. Exposure uses only data before the landmark: baseline/landmark creatinine trajectory, urine output over a fixed pre-landmark window, and cumulative fluid balance. The primary comparison is creatinine-improved/urine-output-impaired versus concordant recovery; fluid balance is a prespecified secondary/stratified exposure, not silently substituted for urine output.

Outcomes are in-hospital death and a prespecified post-landmark kidney outcome, such as persistent/worsening creatinine or renal replacement therapy, with follow-up through hospital discharge or a fixed 7-day window and explicit competing-risk handling. The exact outcome definition must be fixed after schema inspection and before model fitting.

## Baseline versus substantive alternative

Simple baseline: a prespecified logistic or cause-specific Cox model for the post-landmark outcome using age, sex, admission type, pre-landmark severity, creatinine value/trajectory, urine-output category, fluid-balance category, and monitoring intensity. It estimates an interpretable association and is the primary test of whether discordance adds information beyond creatinine recovery.

Substantive alternative: a time-aware landmark model using ordered pre-landmark creatinine, urine-output, and fluid-balance trajectories (for example, a discrete-time survival model or a regularized recurrent/functional model), with the same patient split, outcome, and calibration/uncertainty evaluation. The alternative can reveal whether the sequence and slope of recovery matter, rather than a single landmark category; it cannot establish mechanism. Compare incremental discrimination, calibration, and uncertainty against the baseline, with a held-out temporal or patient split and bootstrap confidence intervals. A small CPU fit is appropriate for the baseline; the time-aware model may use CPU or one allocated GPU if trajectory fitting is materially slower, but no GPU is required by the scientific question.

Supportive results require a prespecified incremental association for discordance with uncertainty, persistence after monitoring-intensity adjustment, and no material reversal in the fixed sensitivity analysis. Adverse results include no incremental association, disappearance after monitoring adjustment, or reversal. An imprecise null is inconclusive. Clinical adjudication of AKI, true recovery, fluid overload, and treatment indication is unavailable and would be required for stronger mechanistic or management claims.

## Missing evidence and next steps

1. Verify exact catalog table identifiers, source headers, item IDs, units, join keys, and bounded cohort/event counts.
2. Complete the third inspected key reference with a frozen receipt and attach exactly three sources plus key-references.json before selection.
3. Fix thresholds and outcome definitions before any exploratory outcome peeking.
4. Run the feasibility audit, then the baseline and time-aware comparison with uncertainty and falsification checks.
