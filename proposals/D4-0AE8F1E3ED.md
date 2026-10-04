> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Absolute-risk CBC cancer-type contrast under generic burden and source ascertainment

Status: substantive child of `[prior hypothesis]`. This is a planned Harbor experiment; no hypothesis fit or participant-level result has been run here.

## Scientific opening, evidence, and unresolved claim

The parent established a useful but decision-incomplete question: whether a prespecified platelet/haemoglobin CBC ordering is more associated with later colorectal cancer (CRC; ICD-10 C18–C20) than with haematologic cancer (C81–C96), after timing, registry/inpatient source disagreement, generic cancer and repeat-observation concerns. The remaining clinical uncertainty is the scale and specificity of the contrast. A relative coefficient or a ratio can look impressive while corresponding to a negligible absolute risk difference, or while reflecting a shared tendency to be observed with cancer.

The three inspected works bound, but do not answer, this opening. Virdee et al. [K1] reviewed blood-test trends and found heterogeneous, limited evidence across cancer types, including no reported association for combined haematological cancer in the reviewed trend literature; it does not compare fixed CBC profiles in an unselected cancer-free population or establish source robustness. Sala et al. [K2] reported retrospective, CRC-only longitudinal CBC trajectories up to 24 months before diagnosis, with an explicit investigational/external-validation limitation; it cannot show CRC specificity against haematologic or other cancers. Hampton et al. [K3] found that symptomatic CRC prediction studies often report discrimination without calibration and have limited internal/external validation; it does not establish that an assessment-centre CBC contrast is clinically usable or decision-effective.

The strongest supported claim is therefore descriptive: abnormal or changing blood measurements can be associated with later cancer outcomes in selected clinical cohorts. The unresolved claim to test is:

> In UKB adults with a complete first CBC and no source-observed qualifying cancer or death at baseline, two fixed, prespecified CBC profiles produce a clinically meaningful, population-standardized absolute competing-risk difference for delayed CRC versus delayed haematologic cancer that persists after adjustment for generic all-cancer burden, an explicit other-primary-cancer comparator, registry/inpatient ascertainment, calendar era, and future repeat-observation selection.

This is an observational, source-specific risk contrast. It is not a causal effect of changing haemoglobin or platelets, a biological mechanism, a diagnostic probability, a screening threshold, a stage/treatment claim, or a claim that either source date is disease onset. The substantive advance over the parent is decision-facing: it requires all four profile-specific component risks, their absolute differences in percentage points, and a generic burden comparator before calling the delayed CRC-versus-haematologic contrast clinically meaningful.

## Clinical estimand and competing outcomes

Let (g_C) be the fixed “CRC-like” profile: platelet count set to development-set mean + 1 development SD and haemoglobin to development-set mean − 1 SD; WBC and RDW remain at their development-set means. Let (g_H) be the fixed “haematologic-like” profile: platelet mean − 1 SD and haemoglobin mean + 1 SD; WBC and RDW remain at their development-set means. These are prespecified contrasts, not treatment assignments or clinical phenotypes. Development means/SDs are frozen before holdout scoring and the solver must report them.

For source (sin{R,I}), where (R) is registry and (I) is inpatient, and cancer class (cin{CRC,H,Other}), define (F_{s,c}(g,wmidmathcal P)) as the model-standardized cumulative incidence of the first source-observed event of class (c) by window end (w), over the same target population (mathcal P), with death and the other cancer classes as competing events. The primary delayed target population is the common T0 cohort that is alive and free of qualifying cancer in both source series through T0+2 years; its risk clock starts at T0+2 and ends at the earliest event, death, administrative censoring or T0+5. Events in the first two years are reported and excluded from this conditional delayed risk set, never relabeled as delayed events.

For each class:
[
Delta_{s,c}^{2-5}=F_{s,c}(g_C,2!-!5)-F_{s,c}(g_H,2!-!5).
]

The decision-facing cancer-type contrast is:
[
T_s^{2-5}=Delta_{s,CRC}^{2-5}-Delta_{s,H}^{2-5}.
]
Report the four component risks (F_{s,CRC}(g_C)), (F_{s,CRC}(g_H)), (F_{s,H}(g_C)), and (F_{s,H}(g_H)), as well as both (Delta) values and (T), all in percentage points with 95% uncertainty intervals. The same calculation is repeated for 0–90 days, 90 days–2 years, and the delayed 2–5-year window.

Generic cancer burden is not inferred from the CRC-versus-haematologic contrast. Define (All=CRC+H+Other) and:
[
B_s^{2-5}=F_{s,All}(g_C)-F_{s,All}(g_H)
]
and report (Delta_{s,Other}). Define a residual specificity display:
[
S_s^{2-5}=Delta_{s,CRC}^{2-5}-	frac12(Delta_{s,H}^{2-5}+Delta_{s,Other}^{2-5}).
]
(B) is the profile contrast in total observed primary-cancer burden; it is not severity, causality or a clinical utility measure. (S) is a descriptive residual, not a mechanism. A positive (T) with small (S), or an other-cancer contrast comparable to CRC, is not evidence of CRC specificity.

For completeness, report the parent’s cause-specific relative summary:
[
D_s=(eta_{platelet,CRC}-eta_{Hb,CRC})-(eta_{platelet,H}-eta_{Hb,H}),
]
but do not use (D) as the primary clinical decision estimand. A descriptive absolute boundary of +1 percentage point for the lower 95% interval is prespecified as a scale marker, not a referral threshold or minimum clinically important difference.

## Population, dates, and exact source binding

Use one row per unique, nonmissing `eid` in the exact same-namespace source:

- Snapshot: `ukb-completed-subset-20261002`; catalog [source checksum].
- Catalog guide: `datasets/README.md`, `datasets/ukb/README.md`; table record: `datasets/ukb/table-5d49a6760e7ffdbd.json`.
- Table: `ukb671626.csv (Parquet)`, source ID `[UKB data file]`, table identifier `table-5d49a6760e7ffdbd`, 502,371 rows, id column `eid`, namespace `ukb671626`, ordinary file with no archive member.
- Read-only source path: `[internal dataset path]`; [source checksum].
- Future solver binding target: `[internal dataset path]`, same source hash. The 37.8-GB CSV lineage file is provenance only, not an analysis input.

No joins are permitted. `eid` is the only key. Do not use `ukb672073`, Assessment Center, Olink, HCC, MIMIC, EICU, or any cross-namespace field. All configured sources remain read-only; the other configured datasets are intentionally unused because their namespaces do not supply required paired cancer arrays and joining them would alter the estimand.

Required fields and roles are:

- Baseline and time: `eid`; T0 `53-0.0`; T1 `53-1.0`; T2 `53-2.0`. T0 year is derived from `53-0.0); UKB assessment dates are landmarks, not laboratory order dates.
- Complete instance-0 CBC: WBC `30000-0.0`, haemoglobin `30020-0.0`, RDW `30070-0.0`, platelets `30080-0.0`.
- Baseline covariates: sex `31-0.0`, age `21003-0.0`, BMI `21001-0.0`, smoking `20116-0.0`, CRP `30710-0.0`.
- Registry arrays: pair same-index cancer date `40005-j.0` with ICD-10 code `40006-j.0`, for (j=0,ldots,21). Retain only valid paired date/code observations and use the earliest qualifying event.
- Inpatient arrays: pair same-index ICD-10 code `41270-0.k` with first-inpatient-diagnosis date `41280-0.k`, for (k=0,ldots,258). This exact paired schema correction is preserved from the parent. The non-existent/incorrect pattern `41270-k.0) must not be substituted. Inpatient dates are an ascertainment proxy, not a gold standard.
- Death: `40000-0.0`; `40001-0.0` is audit-only, not a second death endpoint.
- Future observation sensitivity: `30000-1.0`, `30020-1.0`, `30070-1.0`, `30080-1.0`; T2 CBC fields are sensitivity-only.

The inspected complete table schema contains 1,160 names and all required sets, including exactly 259 columns each for `41270-0.0)–`41270-0.258) and `41280-0.0)–`41280-0.258). This is a schema-availability observation, not participant-level nonmissingness or an event-count result. The attached `schema-availability-audit.json` records the generated expectations and source provenance; the solver must rerun it and report duplicate `eid`, parse failures, missing pair members, invalid dates, date ties, impossible orderings, and denominators before fitting.

Classify CRC as C18–C20, haematologic cancer as C81–C96, and other primary malignant cancer as C00–C97 excluding those families and secondary C77–C79. Codes outside these families are not qualifying cancer outcomes. Keep source-specific first event dates; do not merge registry and inpatient dates into a “true” onset date.

Population construction:

1. Exclude duplicated `eid`, missing/unparseable T0, incomplete instance-0 CBC, and death on or before T0.
2. Exclude any valid qualifying registry or inpatient cancer on or before T0. Report registry-only, inpatient-only, intersection and total exclusions.
3. Do not require T1/T2 for the primary cohort.
4. For the delayed risk set, additionally exclude participants with a qualifying cancer or death in either source on or before T0+2. The solver must report how many events were removed in each source and intersection.
5. Follow each source separately to its first CRC, haematologic, other-primary, death, administrative censoring at 2022-12-31, or window boundary. A discordant source record is retained as discordance, not resolved by preference.

The primary split is temporal by T0: earliest 70% of eligible T0 dates for development and latest 30% for a locked temporal holdout; ties at the split date stay in one split according to an explicit deterministic rule. One `eid` cannot occur in both splits. All profile means/SDs, missingness decisions, tuning, calibration, weighting and thresholds are development-only.

Define future repeat observation (R=1) only if T1 is strictly after T0, within 2–8 years, and all four instance-1 CBC fields are observed; otherwise R=0. R is a post-baseline selection stratum, never a baseline predictor. A repeat-change analysis is secondary and requires no qualifying source cancer or death on/before T1; it is not part of the primary absolute-risk estimand.

## Baseline and learned same-input alternative

The transparent baseline is four source-specific cause-specific Cox models (CRC, H, Other, death), using standardized instance-0 WBC, haemoglobin, RDW, platelets, age, sex, BMI, smoking, CRP and T0 calendar year. After the CBC cohort screen, model complete cases are reported explicitly; no missing value is silently treated as normal. Use robust variance and inspect proportional-hazard diagnostics. Convert fitted cause-specific hazards to model-standardized cumulative incidence under competing risks for the two fixed CBC profiles. Aalen–Johansen estimates are a non-model descriptive check on observed event incidence, not a replacement for profile standardization.

The substantive learned alternative uses exactly the same people, source-specific outcomes, exclusions, dates, covariates and profiles: a CPU gradient-boosted discrete-time multi-task competing-risk model with a first 90-day interval and yearly intervals thereafter, with separate hazards for CRC, H, Other and death. It can reveal nonlinear CBC ranges, interactions and time-varying class/source hazards that an additive Cox model may miss; it cannot recover symptoms, test indication, pathology, stage, healthcare utilisation or biological onset. Fit registry and inpatient models independently. Do not permit future R, T1/T2 results or post-T0 outcomes as predictors.

On the locked holdout report four profile-specific component risks, (Delta), (T), (B), (S), (D), source differences, target-specific calibration intercept/slope, calibration plots, 2-year and 5-year cumulative-incidence Brier and log scores, and 500 participant-bootstrap intervals. AUC/Uno C-index is secondary. Bootstrap resampling must preserve the temporal split and source strata. If the holdout has fewer than 50 haematologic events, learned type-specific comparisons are inconclusive and the solver must not replace the split or endpoint.

The transparent model is selected as the primary presentation because it makes the absolute-risk decomposition auditable. The boosted alternative is retained because its nonlinear/time-varying predictions test a substantive information-loss uncertainty, not because a small predictive gain is clinically valuable. A sequence transformer, GP/state-space model or causal mediation model is deferred: only two broadly available repeat CBC assessments exist, and unavailable indication/pathology/treatment evidence would not be identified by extra latent structure. GPU is not required for this tabular experiment; hardware guidance confirms A100 capacity is not a scientific requirement. Future solver estimate: 8–16 CPU cores, 32–64 GiB RAM, 2–4 hours including selected-column parsing, two source fits, bridge analyses and 500 bootstraps; unmeasured estimate. Configured envelope is up to 16 CPUs, 262,144 MiB and 28,800 seconds. This is distinct from the bounded discovery episode and does not authorize solver execution here.

## Falsification and source/selection checks

All checks are prespecified and run on the development data for design diagnostics and on the locked holdout for reported confirmation where estimands permit:

1. Timing: report 0–90 days, 90 days–2 years and 2–5 years. An effect confined to 0–90 days, or lost after removing that band, supports proximity/ascertainment rather than stable delayed association.
2. Generic burden: compare CRC, H and Other (Delta) values and total burden (B). If (Delta_{Other}) is comparable to (Delta_{CRC}), or (B) is large while (S) is near zero, the apparent signal is interpreted as generic cancer burden/capture, not CRC specificity.
3. Source ascertainment: fit identical analyses on the common source-clean population for registry and inpatient dates. For same-class paired events, report n, median, IQR, 5th/95th percentiles of inpatient minus registry date and fractions crossing 90 days, 2 years and 5 years. If fewer than 50 paired events exist for a class, source-displacement interpretation is inconclusive. Report reciprocal same-class capture and stratify capture by development CBC-score deciles and WBC/CRP strata; this tests severity-dependent capture, not which source is correct.
4. Calendar era: report T0-year interactions and estimates by prespecified eras (solver must state bins before holdout scoring). A contrast present in one era only is adverse to temporal robustness.
5. Repeat-observation selection: estimate the primary T/A/B/S in R=1 and R=0 with the same delayed risk definition and report overlap. Fit a development-only baseline R model using only T0 CBC and baseline covariates, then stabilized inverse-probability weights as a stress test; report weight tails, positivity, and weighted/unweighted estimates. Poor positivity is inconclusive and is not repaired by favorable trimming.
6. Label permutation: within development only, permute CRC and H labels while preserving event times, censoring and source; the type contrast should collapse toward zero. This checks implementation/specificity, not biology.
7. Pair integrity: rerun with invalid/missing date-code pairs excluded and report all integrity denominators. Never cross array indices.
8. Relative/absolute consistency: compare (D) direction with (T) and the four component risks. A ranking or coefficient gain without calibrated absolute-risk separation is adverse to a decision-facing interpretation.

## Interpretation, uncertainty, and claims

Supportive evidence for the intended claim requires: (i) both registry and inpatient delayed (T_s) have the same positive direction with 95% intervals excluding zero; (ii) both source-specific CRC-versus-haematologic absolute contrasts have lower 95% bounds above +1 percentage point when event, paired-source and positivity thresholds are met; (iii) CRC (Delta) is materially larger than (Delta_{Other}) and (S) is positive in both sources; (iv) the result is not confined to 0–90 days, one calendar era or R=1; (v) weighted and unweighted estimates agree within uncertainty with adequate overlap; (vi) the label permutation collapses; and (vii) the learned model does not overturn calibrated absolute-risk interpretation. This supports an external, indication-rich validation study only.

Adverse evidence is a precise delayed reversal, source reversal, large prespecified source discrepancy (for example (|A_R-A_I|>1) percentage point), comparable other-cancer contrast, large (B) with small (S), early-only signal, era confinement, repeat-stratum confinement, or a learned-only ranking improvement without meaningful calibrated absolute separation. These weaken a stable CRC-specific interpretation but do not refute a generic CBC/cancer association.

Inconclusive evidence includes fewer than 50 held-out haematologic events, fewer than 50 same-class paired source events for a bridge claim, broad intervals spanning both zero and the +1-point boundary, poor positivity, invalid pairing/date parsing, nonconvergence, or a wide null that cannot distinguish no meaningful contrast from the prespecified boundary. A wide null is not refutation.

Computationally checkable claims are exact binding/schema integrity, cohort flow, event counts, date windows, profile values, profile-specific cumulative risks, (T/B/S/D), calibration/Brier/log metrics, source-displacement/capture, era and repeat-selection diagnostics, permutation behavior, bootstrap intervals and whether a conclusion obeys these rules. Clinical adjudication or another study is required for symptoms, reason for CBC, laboratory order/source and timing, expert cancer onset/date validity, ferritin/iron, reticulocytes, FIT, smear, marrow/pathology, stage, treatment, transfusion context, healthcare utilisation, causal mechanism, transportability, clinical utility, and intervention/referral decisions. A prospective, indication-rich cohort with adjudicated cancer onset and decision-impact evaluation is required before deployment.

## Actual scientific deliverable and deferred alternatives

Completion requires newly fitted source-specific transparent and learned models and the following outputs: `data_quality.json`; `cohort_flow.json`; `split_manifest.json`; `event_counts.json`; `profile_risks.json`; `estimands_absolute.json`; `source_bridge.json`; `falsifications.json`; `holdout_metrics.json`; `bootstrap_intervals.json`; and `conclusion.json`. The conclusion must cite computed file names and distinguish supportive, adverse and inconclusive outcomes. A schema audit, readiness probe or synthetic fixture is not completion and no result is claimed in this proposal.

Alternatives not chosen are recorded explicitly. A Cox/Aalen–Johansen presentation plus the same-input boosted model is scientifically adequate for the fixed-profile absolute-risk question. A trajectory model is deferred because only T0/T1/T2 CBC landmarks are available and adding latent dynamics would not identify source correctness or clinical indication. A causal mediation/mechanistic analysis is deferred because all essential mediators and adjudication data are unavailable. Revisit these branches only with an indication-rich cohort, reliable laboratory dates, pathology/stage and a validated cancer-onset reference. This child changes the clinical estimand and comparator, not the parent’s exact source binding or paired schema.

## Key references

Exactly three distinct inspected full-text works are attached as UTF-8 excerpts and linked by hash in `key-references.json`:

- [K1] Virdee et al., *Cancers* 2024: systematic review of blood-test trends and undiagnosed cancer; supports heterogeneity and limited evidence across cancer types.
- [K2] Sala et al., *Translational Oncology* 2026: retrospective CRC-only longitudinal CBC trajectory study; bounds the evidence and its explicit investigational status.
- [K3] Hampton et al., *eClinicalMedicine* 2023: systematic review of symptomatic CRC prediction models; supports calibration/validation caution.

No paper establishes the UKB hypothesis, and no unavailable supplement, clinical note or original paper beyond the attached inspected excerpts is claimed.
