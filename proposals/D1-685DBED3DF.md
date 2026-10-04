> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Forward-time validation of affine persistence versus inherited M1

## Design and data bindings

Targeted child of `[prior hypothesis]`. This preserves its HCC snapshot, frozen repeat-TACE cohort, event and laboratory clocks, denominators, inherited M1 feature/model definition, and noncausal limits. The new validation is outcome-blind: the calendar cutoff was selected from event counts before reading any Y-based result. Complete-source reconstruction scans every row of the five frozen ordinary CSV bindings: encounters (`patient master index`,`visit number`,`age`,`sex`,`visit time`,`admission time`,`discharge time`), diagnoses (`patient master index`,`visit number`,`diagnosis name`,`diagnosis type`), procedures (`patient master index`,`visit number`,`procedure`,`start time`,`end time`,`procedure source`), medications (`patient master index`,`visit number`,`medication`,`start time`), and labs (`patient master index`,`visit number`,`test`,`qualitative result`,`quantitative result`,`specimen type`,`test time`). Patient identity and encounter keys remain `patient master index` and (`patient master index`,`visit number`); diagnosis time remains encounter-linked. No sampling or public clinical-record query is used.

The assay triplet remains B = latest valid assay value on TACE2 days -30:-1; P = latest valid value in the same repeat encounter from event-72h through but excluding event; Y = valid same-encounter value after event through +72h nearest +24h, with the inherited tie rules and strict B_time < P_time < event_time < Y_time. The event is the first later TACE on TACE2 days 15-90. The training period is event_day < 2023-01-01 and the test period is event_day >= 2023-01-01. This was chosen solely from the outcome-blind event-date counts: 212 events before the cutoff and 106 after across 147 unique dates (2018-09-04 through 2025-02-25); the split gives calendar eras rather than random folds and was fixed before test outcomes were inspected. The assay-specific complete-triplet counts are reported by the execution below.

## Hypothesis and estimand

The untested claim is that an affine persistence forecast, `Yhat = a + bP` learned only on earlier-calendar episodes, transports to later episodes and retains its error/calibration advantage over raw `Yhat=P`; additionally, inherited M1 should add reproducible value over that transparent affine forecast. The estimand is descriptive prognostic transport in the selected complete-triplet population, not a treatment effect or causal effect. Affine parameters and M1 preprocessing/regularization are learned only from the earlier period; no later Y is used for fitting or tuning. M1 uses the inherited B, P, arm, age, sex, event timing, and P-lead features and inherited ridge alpha search on the training period only.

Primary test-period outputs are RMSE, MAE, mean prediction bias, calibration intercept/slope, and paired RMSE differences. Uncertainty is a within-arm patient-frequency bootstrap of the fixed test predictions, reported as percentile 95% intervals; because the temporal split has only 106 total events and sparse arms, these intervals quantify sampling variability conditional on the fitted forecasts, not universal transport uncertainty.

## Results and interpretation

Managed execution is linked to `temporal_validation_results.json`. The exact computed counts and metrics are in that file. The key decision rule is prespecified: supportive M1 added value requires positive M1-minus-affine RMSE gain with uncertainty excluding zero and acceptable calibration in the later period; affine transport is supportive when affine beats raw persistence with stable calibration and error, adverse when it loses or materially drifts, and inconclusive when intervals are broad or calibration/units prevent a clinical margin.

A supportive result would justify only replication of the prognostic transport pattern in this later calendar era. An adverse result would indicate temporal drift or failure of the benchmark, not mechanism or treatment harm. An inconclusive result would motivate a larger external/temporal cohort, assay-unit harmonization, and prespecified clinical margins. No result can establish bedside utility, toxicity, treatment response, benefit, or causality because the HCC data lack validated assay units/reference ranges, adjudicated hepatic outcomes, imaging/tumor burden, reliable outside-care capture, and an action threshold or clinical loss function.

## Reproducibility and limits

Runner: `[internal dataset path]` ([source checksum]). Temporal count audit: `[internal dataset path]`; count script: `[internal dataset path]`. Parent reconstruction support is retained at `[internal dataset path]`; parent benchmark output is at `[internal dataset path]`. 

The result must not be treated as an exact replication of the parent unless all frozen denominator gates pass. It is a forward-time validation, not an external validation: both periods come from one institution/snapshot, cohort selection is highly selected, repeated patient episodes are reduced to one event under the inherited construction, and temporal nonexchangeability remains possible. Clinical adjudication, units, and an independent cohort are required for stronger claims.
