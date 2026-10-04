# Pre-illness kidney-function discordance, grip strength, and incident hospitalized AKI

## Claim and opening

Existing evidence shows that eGFRcys−eGFRcr discordance is common and reflects both filtration and non-GFR determinants [K1], predicts broad adverse outcomes [K2], and can arise when acute muscle loss makes creatinine eGFR overestimate measured GFR [K3]. It does not establish prospective AKI risk in ambulatory adults.

Hypothesis: among UK Biobank participants with baseline eGFRcr >=60 and no prior hospitalized AKI, lower eGFRcys than eGFRcr predicts higher 10-year incidence of hospitalized N17* AKI beyond both current eGFR values, and the association is stronger with lower sex-specific grip strength.

Resolution matters because a supportive, calibrated result could target cystatin-C testing/risk review before nephrotoxic exposures; an adverse result would argue against interpreting discordance plus weakness as hidden renal vulnerability.

## Harbor experiment

Population: age 40-80, valid baseline 53-0.0, sex 31-0.0, creatinine 30700-0.0, cystatin C 30720-0.0, grip 46/47-0.0, eGFRcr >=60; exclude prior N17* and 30-day washout events. Follow day 31 through first paired 41270-0.* N17* / 41280-0.* date, death 40000-0.*, 10 years, or administrative end.

Sources: main ukb672073.csv; biological_samples ukb672073_Biological_Samples.csv; health_outcomes ukb672073_Health_Related_Outcomes.csv. Join one-to-one on eid. Full exact paths, covariate fields, snapshot and unit readiness checks are in work/kidney-evidence.md. Outcome is coded hospitalized AKI, not KDIGO/severe AKI.

Exposure: 2021 CKD-EPI race-free eGFRcr and 2012 CKD-EPI eGFRcys after unit verification; eGFRdiff=eGFRcys−eGFRcr, continuous spline, categories <−15/[−15,15)/>=15 descriptive. Modifier: sex-specific z score of maximum valid grip.

Primary analysis: cause-specific Cox B0 eGFRcr+covariates; B1 +eGFRcys; B2 +discordance+grip; B3 +interaction. Report HRs, bootstrap CIs, Aalen-Johansen standardized 10-year risk differences and competing death. Adjust for demographics, smoking, adiposity, CRP, albumin, urea, glycemia, ACR and only exactly verified comorbidities/medications. Combined-eGFR/residualized-discordance, complete-case, early-event and negative-control sensitivities.

Learned alternative: discrete-time competing-risk boosted trees on identical inputs/target, 64/16/20 train/validation/untouched holdout; full versus discordance/grip ablation; time-AUC, integrated Brier, calibration and decision curves with bootstrap uncertainty. This can reveal nonlinear/high-order vulnerability patterns lost by Cox, but not mechanism. CPU plan <2 hours/16 CPUs/<64 GiB after projection (unverified estimate).

Completion requires newly fitted B0-B3 and learned/ablated models, cohort/event flow, effect/interaction/risk estimates, calibration/discrimination/decision outputs, and uncertainty.

Supportive: higher AKI risk with lower discordance, low-grip amplification, robust sensitivities, and held-out incremental information. Adverse: precise null/reversal, attenuation by inflammation/adiposity, nonspecific hospitalization association, or no learned incremental utility. Inconclusive: sparse events, wide intervals, collinearity, poor overlap, unstable missingness, or inadequate dates/follow-up.

No result proves muscle mechanism, renal reserve, causal screening benefit, or severe AKI. Those require measured GFR/body composition, serial markers, medication/acute-exposure data, hospital labs, adjudication, external validation, and another study.

## Key references

[K1] Chen DC et al. Kidney Medicine. 2024;6:100796. doi:10.1016/j.xkme.2024.100796.
[K2] Potok OA et al. AJKD. 2020;76:765-774. doi:10.1053/j.ajkd.2020.05.017.
[K3] Haines RW et al. CJASN. 2023;18:997-1005. doi:10.2215/CJN.0000000000000203.

Detailed claim mappings, rivals, data bindings, alternatives, falsification criteria, and inspected limitations: work/kidney-evidence.md.
