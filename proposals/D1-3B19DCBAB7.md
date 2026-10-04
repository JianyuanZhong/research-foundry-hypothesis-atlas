> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

Title: Observation-bounded test of whether the frozen early albumin/bilirubin separation remains recorded later in the repeat-TACE encounter

Two-parent advance

This child combines the executed persistence analysis of [prior hypothesis] with the observation-process separation of [prior hypothesis]. It preserves the exact 131 early-landmark episodes, independently selected repeat-TACE event, strict assay parser, duplicate rule, early common-panel selector, and strict early-signal inequalities. It changes neither the cohort nor the event. It replaces the invalid P-overlapping placebo with an all-episode observation estimand and audits every post-landmark albumin and total-bilirubin row before making a numeric claim. The no-sampling audit finds that assay-specific analysis does not rescue support: in this snapshot albumin and bilirubin are always recorded together at the same timestamp after the landmark, and only 41/131 episodes have a qualifying post-landmark panel before the patient-specific horizon. Thus the clinically important advance is a falsifiable negative feasibility result plus a bounded conditional numeric test, rather than an overgeneralized persistence claim.

Question, evidence boundary, and hypothesis

Supported before this child: the frozen EHR construction contains 34 systemic-pathway and 97 comparator early landmarks; 23 and 63 respectively satisfy early_signal=1. The inherited exact-panel analysis selected 41 late panels and produced expected-direction coefficients but bootstrap intervals spanning zero for albumin and bilirubin. Its 22-panel pre-event placebo is structurally invalid because all 22 timestamps equal both assay-specific P timestamps. The complementary parent showed that earlier panel observation is strongly associated with prior measurement history, establishing that recording cannot safely be treated as incidental.

Unresolved biological/clinical claim: whether the early recorded changes represent persistent liver injury, toxicity, hepatic failure, decompensation, recovery, treatment effect, safety, or prognosis. These data do not adjudicate any of those claims.

Computable hypothesis: within the frozen 131 episodes, early_signal=1 is associated with (a) a different probability of a later assay record and (b), conditional on a later record, lower albumin and higher total bilirubin at the last recorded post-landmark panel, after adjustment for the corresponding early and pre-event assay value and pathway arm. The joint persistence hypothesis requires both conditional assay contrasts to be in the prespecified direction with arm-stratified bootstrap 95% intervals excluding zero, stable to leave-one-out and locked timing analyses. It is a hypothesis about persistent recorded assay separation, not biology or causality.

Sources and exact bindings

HCC snapshot [source checksum]. These are ordinary CSV files, not archive members.

1. Encounters table `encounters`: `[internal dataset path]` ([source checksum]). Required columns: `patient master index`, `encounter number`, `age`, `sex`, `encounter time`, `admission time`, `discharge time`, `encounter department`. Join the already frozen event encounter on (`patient master index`,`encounter number`); `discharge time` bounds recorded encounter opportunity but is not an outcome.
2. Diagnoses table `diagnoses`: `[internal dataset path]` ([source checksum]). Required: `patient master index`, `encounter number`, `diagnosis name`, `diagnosis type`. It is used only by the frozen pathway reconstruction; there is no native diagnosis timestamp.
3. Procedures table `procedures`: `[internal dataset path]` ([source checksum]). Required: `Patient Master Index`, `Encounter Number`, `Procedure`, `Start Time`, `End Time`, `Procedure Source`. Parsed `Start Time` supplies the independently selected repeat-TACE event clock; `End Time` does not replace it.
4. Medications table `medications`: `[internal dataset path]` ([source checksum]). Required: `Patient Master Index`, `Encounter Number`, `Medication`, `Single-dose medication amount`, `Single-dose medication amount unit`, `Frequency`, `Start Time`, `End Time`, `Route of administration`, `Drug type`; used only by the frozen pathway assignment.
5. Labs table `labs`: `[internal dataset path]` ([source checksum]). Required: `Patient master index`, `Encounter number`, `Test`, `Quantitative result`, `Test time` (with `Qualitative result` and `Specimen type` retained for audit only). Exact assay labels are `Albumin` and `Total bilirubin`; event-encounter matching uses both keys; time is parsed from `Test time`. There is no unit or reference-range column, so no unit-dependent clinical threshold is used.

Frozen reconstruction gates

Run the colocated frozen reconstruction unchanged. It must reproduce 319 systemic and 1,491 comparator pathways; 159 and 526 selected repeat events; 34 and 97 early landmarks; 23 and 63 early-signal-positive episodes; and 476,813 valid deduplicated target-assay rows. Failure of any gate is reconstruction falsification and stops inference.

Preserve strict parsing of `quantitative result` as optional whitespace plus an optional inequality marker and a signed decimal/scientific number. Exclude inequality-censored, nonnumeric, or invalid-time rows. Preserve source order `_src`; for duplicate (`patient master index`,`encounter number`,`test`,`test time`) groups, fail if numeric values disagree and otherwise retain the final source row. The snapshot contains seven duplicate assay timestamps and no discordant groups before final filtering.

Preserve the parent assay-specific B and P clocks and the early common panel. The early panel must contain both exact assay labels at one same-event-encounter timestamp in inclusive [12h,36h] relative to the independently selected repeat-TACE `event_time`; choose minimum absolute distance from +24h, earlier timestamp on ties, and final `_src` only after timestamp choice. Define `early_signal=1` iff selected early albumin is strictly below its assay-specific P value AND selected early total bilirubin is strictly above its assay-specific P value. Equality is negative.

Observation horizon and value-blind selection

For each frozen episode set H_i = min(event_time+120h, parsed `Discharge time` of the already selected event encounter). The primary post-landmark risk interval is `(y_time,H_i]`; all 131 have positive opportunity and documented discharge in this snapshot. The 120-hour cap is a five-day same-encounter peri-procedural boundary inherited from the earlier locked sensitivity, while discharge prevents counting time after documented encounter opportunity. Never attach a different encounter to extend follow-up. Report missing discharge, nonpositive opportunity, opportunity-time quartiles, and assay rows after discharge. A sensitivity reports fixed event-time caps of 48, 72, 96, 120, and 168 hours without changing the primary patient-specific horizon.

For each assay separately define O_A and O_B as at least one valid row in `(y_time,H_i]`. Define O_both and O_common (both assays at any time and at one exact common timestamp). Before inspecting values report all four indicators overall, by arm, by early-signal status, and in all arm-by-signal cells; report distinct-timestamp counts and first/last timing. Select the final row separately for each assay by maximum `Test time`, with the preserved duplicate rule. This selector uses only timing, never values. If assay clocks differ, retain assay-specific values and times rather than manufacturing a common panel.

Estimands and analyses

Part O, all 131 episodes: for each O, estimate the arm-standardized risk difference E_arm[P(O=1|early_signal=1,arm)-P(O=1|early_signal=0,arm)], standardized to the observed arm mix. Use 5,000 episode bootstraps within arm-by-signal cells and percentile 95% intervals. This describes differential recording only; an interval spanning zero does not prove nondifferential observation, MAR, or exchangeability.

Part V, recorded subsets only: separately fit

last_albumin = intercept + beta_A*early_signal + gamma_A*early_albumin + eta_A*P_albumin + theta_A*arm_systemic
last_bilirubin = intercept + beta_B*early_signal + gamma_B*early_bilirubin + eta_B*P_bilirubin + theta_B*arm_systemic.

The albumin persistence direction is beta_A<0 and bilirubin direction is beta_B>0. Report n, rank, coefficients, ordinary 95% intervals, 5,000 episode bootstraps within arm-by-signal cells with fixed seeds 20261011 and 20261111, and leave-one-out coefficient ranges/sign. Also report value-free coverage and descriptive counts still beyond P and moving farther than the early value, explicitly conditional on recording. Do not impute values, use inverse-probability weights, or claim to recover the 90 unrecorded episodes.

Locked baselines and sensitivities

The inherited exact common-panel model in `(36h,96h]`, nearest +80h with earlier timestamp winning ties, remains a locked timing sensitivity and must be reported, including its negative/inconclusive results. The patient-horizon final-record model is the primary observation-bounded selector. Report the fixed 120h and 168h availability audit but do not enlarge the numeric horizon after seeing values. The invalid [-96h,-36h) placebo is retired as a support gate: preserve the finding that 22/22 selected panels reused both P timestamps and do not reinterpret it as independent trajectory evidence. A valid computation-level falsification is to permute early-signal labels within arm 1,000 times and verify the implementation returns the observed coefficient’s randomization tail area; this checks linkage/code behavior only and cannot validate biology or the missingness assumptions.

Decision and falsification rules

1. Cohort-wide persistent recorded separation is supported only if each assay is recorded in at least 50% of all 131 episodes, both beta_A and beta_B have the prespecified signs with bootstrap 95% intervals excluding zero, the signs persist in the inherited 96h selector, and every leave-one-out coefficient has the same sign. Coverage is a support condition, not a missing-data correction.
2. Conditional persistent recorded separation is supported only for the actually recorded subsets if both beta intervals exclude zero in the expected directions and timing/leave-one-out gates pass. It must never be generalized to unrecorded episodes.
3. Adverse evidence is a stable interval excluding zero in the opposite direction for either assay, or a direction reversal across locked timing analyses.
4. Inconclusive/mixed evidence is any expected-direction interval spanning zero, conflicting assays, or sensitivity instability.
5. Cohort-wide persistence is unsupported/falsified as an estimable claim if either assay coverage is below 50%, even if a conditional coefficient is nonzero. This does not establish transience or recovery.
6. Reconstruction failure, discordant duplicates, selected rows outside the event encounter/horizon, or failure to reproduce frozen gates is computational falsification and stops all substantive interpretation.

Executed no-sampling audit

Every deduplicated target-assay row was scanned. The frozen gates reproduced exactly. All 131 had documented discharge and positive post-landmark opportunity; opportunity quartiles were 24.868, 27.864, and 51.337 hours. Two target-assay rows fell after documented discharge and were excluded.

At fixed event-time horizons without discharge censoring, assay-specific/both/common support was identical: 0 at 48h, 1 at 72h, 41 at 96h, 42 at 120h, and 44 at 168h. Under the primary patient-specific horizon, albumin, bilirubin, both-any-time, and exact-common observation were each 41/131 (14/34 systemic; 27/97 comparator). Every observed assay had one distinct post-landmark timestamp; clocks were identical. Therefore relaxing the exact common-panel requirement yields no additional episode in this snapshot. Observation was 25/86 among early-signal-positive and 16/45 among negative episodes. The arm-standardized observation risk difference was -0.0679, with bootstrap intervals spanning zero (for O_both, -0.2347 to 0.0917). This does not establish nondifferential observation.

The primary conditional final-record models used 41 episodes. Albumin beta_A=-1.8276; ordinary 95% CI -4.1820 to 0.5267 and bootstrap CI -3.5910 to 0.1918; all leave-one-out estimates were negative. Bilirubin beta_B=7.2914; ordinary CI 0.1597 to 14.4230 and bootstrap CI 0.1377 to 14.1725; all leave-one-out estimates were positive. This differs from the inherited nearest-80h analysis, where both bootstrap intervals span zero, demonstrating selector sensitivity. The joint conditional rule fails because albumin remains imprecise, and the cohort-wide rule fails because coverage is only 31.3%. The strongest warranted conclusion is therefore that cohort-wide persistence is unsupported and the recorded-subset result is mixed/inconclusive; the data do not show transience, recovery, injury, or clinical harm.

Supportive, adverse, inconclusive, and next-data interpretations

A supportive result would establish only durable EHR-recorded separation over this bounded encounter among adequately observed episodes. An adverse result would undermine that recorded-separation hypothesis, not prove recovery. The executed mixed result is inconclusive for numeric persistence and falsifies adequate support for a cohort-wide estimand. To make a stronger clinical claim requires units/reference ranges, structured liver-function context (including INR and clinical signs), reasons and protocols for repeat testing, complete longitudinal encounters, treatment details, and expert chart adjudication; causal effects require a separate design with defensible treatment/exchangeability assumptions. An automatic verifier can check reconstruction, timing, joins, parsing, counts, models, intervals, and whether reported conclusions follow these rules. It cannot adjudicate toxicity, hepatic failure, decompensation, recovery, causality, or clinical benefit.
