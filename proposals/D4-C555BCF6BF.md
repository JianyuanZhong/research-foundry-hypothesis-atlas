# Physiological reserve before incident cancer and five-year post-cancer heart failure

Parent: `[prior hypothesis]` (assessed repairable UKB-08 seed).  
Context only: `[prior hypothesis]`, `[prior hypothesis]` (kidney assay branch; neither is a parent or duplicate estimand).  
Dataset: UK Biobank snapshot `[source checksum]`.  
Catalog: `[internal dataset path]`, [source checksum].  
Status: publishable executable research design; no model fit or clinical conclusion is claimed.

## Decision-relevant question and hypothesis

Cancer survivors can develop cardiovascular complications, but a cancer diagnosis does not by itself identify who has little physiological reserve to tolerate subsequent illness or treatment. The unresolved question is whether a small, prediagnostic physiological panel identifies a clinically consequential subgroup at higher risk of a *new recorded heart-failure diagnosis after cancer*, and whether the risk is additive or reflects nonlinear multi-system reserve failure.

The primary hypothesis is:

> Among adults free of recorded heart failure at an incident cancer landmark, poorer pre-cancer physiological reserve—lower bilateral grip strength, lower creatinine-derived kidney function, higher resting pulse, and higher systolic blood pressure—is associated with a higher five-year cumulative incidence of a first recorded heart-failure diagnosis after cancer, with death treated as a competing event. A prespecified nonlinear interaction model will reveal clinically meaningful threshold or cross-system interaction structure beyond a transparent additive reserve model if reserve failure is not adequately represented by a single linear gradient.

This is a prognostic and triage hypothesis, not a causal claim that reserve causes heart failure or that changing any measurement improves survival. The clinically consequential estimand is the five-year heart-failure cumulative-incidence contrast between the prespecified lowest and highest quintiles of an observed reserve score, standardized to the same age, sex, cancer-site, cancer-year and pre-cancer interval distribution. A secondary estimand is the held-out incremental predictive value of the nonlinear model over the transparent reserve model.

The seed suggested infection, heart failure and death. Selecting first post-cancer heart failure makes the design specific: `I50.*` is a compact, auditable ICD-10 family and is more clinically decision-specific than an arbitrary pooled “noncancer complication” endpoint. Death remains a competing event rather than being silently treated as censoring.

## What is known versus what this experiment tests

The strongest local evidence supports only structural facts: the snapshot contains one-row-per-`eid` phenotype tables, baseline assessment fields, biomarker fields, cancer code/date arrays, 259 diagnosis/date pairs and death-date fields. The UKB-08 card is an expert-proposed hypothesis, not evidence. The local kidney-assay candidates support a separate question about cystatin-C information beyond creatinine; they do not establish a cancer-survivorship result and are retained only as contextual evidence.

The experiment tests a conditional association and out-of-sample prognostic contrast in the defined UKB population. It does not test cancer stage, treatment cardiotoxicity, recurrence, infection susceptibility, biological frailty, measured GFR, echocardiographic dysfunction, outpatient heart failure, or causal effects. The export does not provide verified stage, chemotherapy/radiation, surgery, oncology treatment indication, ejection fraction, natriuretic peptides, adjudicated heart-failure phenotype, complete outpatient records, or a certified individual observation end. A positive result therefore supports only a recorded endpoint and cannot be attributed to treatment or a specific mechanism without those data.

## Exact source bindings

All inputs are ordinary read-only CSV files; no archive member is used. Every join is horizontal and one-to-one on `eid`. The solver must recheck file hashes, headers, unique `eid` values, join coverage, and overlapping-field agreement before fitting.

| table | exact source path | local schema JSON and schema SHA-256 | source SHA-256 | required fields |
|---|---|---|---|---|
| population | `[internal dataset path]` | `datasets/ukb/table-38565c9e35e7cb6c.json`; `[source checksum]` | `[source checksum]` | `eid`, `31-0.0`, `21022-0.0` |
| assessment | `[internal dataset path]` | `datasets/ukb/table-901ef6c7ddce2d51.json`; `[source checksum]` | `[source checksum]` | `eid`, `53-0.0`, `46-0.0`, `47-0.0`, `102-0.0`, `4080-0.0`, `4080-0.1` |
| biological_samples | `[internal dataset path]` | `datasets/ukb/table-c6b666d905f3b02f.json`; `[source checksum]` | `[source checksum]` | `eid`, `30700-0.0` |
| health_outcomes | `[internal dataset path]` | `datasets/ukb/table-3cfae45e0905b0e3.json`; `[source checksum]` | `[source checksum]` | `eid`, `40005-0.0`...`40005-21.0`, `40006-0.0`...`40006-20.0`, `41270-0.0.j`, `41280-0.0.j` for (j=0,ldots,258), `40000-0.0`, `40000-1.0` |

The full UKB catalog also contains `main`, `additional_exposures`, `genomics` and `online_followup`, all retained read-only and available. They are not substituted into this study. Their catalog entries are: main schema `[source checksum]`, additional-exposures schema `[source checksum]`, genomics schema `[source checksum]`, and online-follow-up schema `[source checksum]`.

The local header audit found the required fields literally present. It also found an important array asymmetry: `40006` has 21 available code positions while `40005` has 22 date positions. Cancer binding is therefore restricted to the position-matched intersection (j=0,ldots,20); `40005-21.0` is audited as an unmatched date and cannot be used to define cancer. For every diagnosis position (j=0,ldots,258), `41270-0.j` is paired only with `41280-0.j`. A nonempty code with an empty/unparseable same-position date, or the reverse, is an integrity failure, not a negative observation.

## Cohort and temporal gates

### Baseline reserve assessment

Let (T_0=) `53-0.0`, the first assessment-centre date. Require:

- (T_0) is a valid date between 2006-01-01 and 2010-12-31;
- valid recruitment sex `31-0.0` and age `21022-0.0`;
- valid, positive `46-0.0` and `47-0.0`, summarized as bilateral mean grip;
- valid `102-0.0` resting pulse;
- valid `4080-0.0` and, when present, `4080-0.1`; systolic pressure is the mean of available valid readings, with a minimum of one valid reading;
- valid `30700-0.0` creatinine.

The solver must certify the public field labels, units, coding and instance meaning for fields 46, 47, 102, 4080 and 30700 before interpreting them clinically. The local catalog explicitly says that most UKB labels, units and missing-value meanings are absent; a numeric field is never relabeled as reserve merely because it is available. If the field certificate fails, the solver may produce a structural audit but must not report a physiological result.

Compute race-free creatinine eGFR using a prespecified 2021 CKD-EPI creatinine equation after certifying the creatinine unit. Do not use cystatin C, field 30720, or any kidney-assay increment in the primary exposure. This is the explicit separation from candidates `[prior hypothesis]` and `[prior hypothesis]`.

For descriptive visualization only, define a reserve-direction score after training-fold standardization:
[
R = z(\text{grip}) + z(\text{eGFRcr}) - z(\text{pulse}) - z(\text{SBP}).
]
Higher (R) means a more favorable observed profile under the certified measurement directions; it is not a validated frailty or reserve scale. The primary contrast compares the lowest versus highest (R) quintiles, with thresholds fitted in the training data only.

### Incident cancer landmark

From the health-outcomes table, define each cancer record using the same-position pair ((40006	ext{-}j.0,40005	ext{-}j.0)), (j=0,ldots,20). After code-system certification, a cancer code is a code beginning `C` in ICD-10 malignant-neoplasm range C00-C96/C97. The participant’s first qualifying cancer is the earliest valid date (T_C>T_0); require (T_Cge T_0+365) days to reduce reverse causation from an already developing cancer. Exclude any participant with a valid C-code/date at or before (T_0), rather than calling absent records cancer-free.

The primary cohort uses cancer landmarks (T_C) from 2010-01-01 through 2018-12-31 so that a complete five-calendar-year window can end by 2023-12-31 if the required observation certificate passes. Cancer site is the first three-character ICD-10 group. The primary analysis is site-adjusted and site-stratified for prespecified common groups (C18-C20 colorectal, C33-C34 lung, C50 breast, and C61 prostate); site-specific estimates are emitted only where event and cell-support gates pass. Other C-code groups remain in the pooled site-adjusted analysis but cannot be used to claim a site-specific result without support.

Exclude:

- any recorded `I50.*` code/date on or before (T_C), because the outcome is first post-cancer recorded heart failure;
- death on or before (T_C);
- malformed cancer or diagnosis code/date pairs;
- missing or implausible reserve inputs;
- duplicate `eid` rows or failed one-to-one joins.

These exclusions remove recorded history only; they do not establish absence of undiagnosed heart failure or cancer.

### Outcome and follow-up

The primary outcome is the first `I50.*` diagnosis code paired with its same-position `41280-0.j` date in the open interval ((T_C,T_C+5	ext{ calendar years}]). The competing event is death recorded in `40000-0.0` or `40000-1.0). If death occurs on or before an eligible I50 date, classify death as the competing event; same-day ties are conservatively assigned to death. A participant with neither event by five years is right-censored at the horizon only if observation completeness is certified.

The solver must obtain or fail closed on a source-specific observation/ascertainment certificate through 2023-12-31. The local catalog does not itself provide a complete individual observation end or outpatient ascertainment guarantee. If that certificate is unavailable, the computation may still report “first recorded I50 within the available structured records,” but the five-year clinical cumulative-incidence claim is inconclusive and must not be presented as disease-free survival.

## Estimand and analysis

Use a participant-level split fixed by
[
mathrm{fold}(eid)=mathrm{SHA256}(UTF8(\mathrm{decimal}(eid)))\bmod 5.
]
All transformations, standardization, splines, model fitting and thresholds are training-fold operations.

The primary temporal evaluation fits on cancer landmarks in 2010-01-01 through 2015-12-31 and applies without refitting to landmarks in 2016-01-01 through 2018-12-31. This is a transport test across calendar time, not external validation. Build one row per participant-year for years 1 through 5, stopping at heart failure or death. Fit two cause-specific annual hazards (heart failure and death) so predicted hazards yield a five-year competing-risk cumulative incidence.

M0, the transparent reserve baseline, is a regularized complementary-log-log discrete-time model with separate heart-failure and death hazards. Inputs are exactly:

- age at (T_0), sex, cancer-site group, cancer landmark calendar year, and (T_C-T_0);
- standardized bilateral grip, eGFRcr, resting pulse and systolic pressure;
- year indicators for the five post-cancer intervals.

M0 is the primary scientific baseline because its coefficients and partial effects show whether each observed reserve component has the prespecified direction, while retaining the cancer-site and timing controls.

M2, the substantive alternative, uses the identical participants, outcome rows, split, missingness policy, covariates and four reserve inputs, but replaces only the linear reserve terms with four degree-3 restricted cubic/spline bases (four training-fold knots per feature) plus two prespecified cross-system interactions: grip (	imes) eGFRcr and pulse (	imes) systolic pressure. It uses the same two cause-specific hazards and a fixed regularization value selected once in the training plan. This alternative can reveal thresholds, saturation and muscle-kidney or hemodynamic coupling that M0 averages away; it is not a model-shopping exercise. A boosted-tree model is retained as a possible sensitivity only if the spline/interactions implementation is unavailable, with its hyperparameters frozen before evaluation.

The primary estimand is the late held-out standardized five-year heart-failure CIF difference:
[
\Delta_{low-high}=CIF_5(R\le q_{20})-CIF_5(R\ge q_{80}),
]
where (q_{20}) and (q_{80}) are training-derived reserve-score quintiles. Standardize both profiles over the same late-test distribution of age, sex, site, cancer year and (T_C-T_0). Report this contrast from M0 and M2 with 95% participant-bootstrap intervals and with death CIF. The estimand is predictive standardization, not an intervention contrast.

Secondary outputs are late-test integrated Brier score, calibration intercept/slope at five years, observed versus predicted cause-specific cumulative incidence, site-specific (Delta_{low-high}), and the paired M2-minus-M0 Brier and calibration contrasts. No claim of clinical utility is made from a small discrimination gain.

## Support, adverse and inconclusive results

Support for the reserve hypothesis requires:

1. all source, field-semantics, units, code/date-integrity, timing and observation-completeness gates pass;
2. at least 100 participants in each reserve tail, at least 50 qualifying post-cancer I50 events overall, and at least 10 events in each reported tail; otherwise the result is inconclusive;
3. M0’s late held-out (Delta_{low-high}) is positive with a 95% interval excluding zero, and the direction is present in the early held-out assessment or a prespecified cross-fold check;
4. the association remains after cancer-site and cancer-year adjustment and is not driven by one site group; and
5. if M2 is claimed to add scientific information, its paired late-test Brier improvement has an interval excluding zero and its fitted surfaces show a reproducible, prespecified threshold or interaction pattern. A tiny score improvement without interpretable reserve structure is not a substantive nonlinear finding.

Adverse evidence is a null or reversed reserve contrast, no reserve gradient after site/timing adjustment, calibration harm from M2, or an effect that disappears under date/code linkage permutation. A result confined to one poorly supported cancer site, one era, or one unverified field is adverse or inconclusive for the stated general hypothesis.

Inconclusive evidence includes missing field semantics or units, malformed position pairs, insufficient event/tail support, absent observation completeness, poor temporal transport, unstable bootstrap intervals, or contradictory recorded versus certified prospective modes. Inconclusive is not evidence for or against the hypothesis.

Supportive results establish only that the measured pre-cancer profile is associated with and can prognostically stratify a recorded post-cancer I50 endpoint in this UKB cohort. They do not establish causality, treatment toxicity, cancer recurrence, infection susceptibility, biological reserve, heart-failure adjudication, a treatment threshold, or benefit from a triage policy. Those claims require oncology treatment/stage linkage, echocardiography or biomarker adjudication, complete outpatient ascertainment, clinical review of I50 records, external validation and a prospective impact study.

## Falsification and integrity controls

The solver must report:

- permutation of heart-failure dates within cancer-site, cancer-year and fold strata while preserving follow-up workload;
- permutation of each reserve component within sex, age-band, cancer-site and landmark-year strata;
- deliberate one-position shifts between 41270 and 41280, which must trigger pair-integrity failure rather than produce a result;
- a cancer-code/date shift between 40006 and 40005, which must likewise fail closed;
- random reserve-tail labels and random-list controls;
- M0 with cancer site omitted, to show whether apparent reserve information is only site composition;
- complete-case versus fold-local imputation sensitivity, with imputation fit inside folds;
- early/late label permutation and a cancer-landmark-year permutation;
- separate analyses excluding the first 90 days after cancer and excluding participants with any I50 code in the five years before (T_C) (the latter is a sensitivity audit because the primary cohort already excludes recorded prior I50).

If the reserve association survives breaking reserve-outcome linkage while preserving missingness, site, timing and workload, the reserve attribution is falsified. If nonlinear interactions disappear under reserve-component permutation or fail to transport to the late period, the mechanistic/nonlinear claim is not supported even if M0’s main gradient remains.

## Actual scientific deliverable

The solver must newly produce:

- source hash/header/key and catalog-partition certificates;
- field-label/unit/instance and assessment-versus-specimen timing certificate;
- cohort flow from joined population to baseline reserve, incident cancer, prior-HF/death exclusions and final analytic cohorts;
- all (40006/40005) cancer pair and unmatched-(40005-21.0) audits;
- all 259 (41270/41280) diagnosis/date integrity and I50 extraction audits;
- reserve-feature/formula ledger, fold and early/late manifests;
- fitted M0 and M2 hazard models, held-out individual-year hazards and five-year CIFs;
- low/high reserve thresholds, standardized (Delta_{low-high}), death CIF, calibration and Brier outputs;
- site-specific support tables, 2,000-replicate participant bootstrap intervals and falsification outputs;
- an interpretation file linking every conclusion to an output path and marking unavailable clinical evidence.

Completion is this evidence-linked package under passed gates, or a reproducible fail-closed certificate naming the failed gate. Readiness and a source count are not a solved result.

## Alternative selection record and compute

The chosen transparent baseline is an additive discrete-time competing-risk model because it directly represents the reserve gradient, is auditable, and can show direction and calibration. The chosen alternative is a matched spline-plus-cross-system-interaction model because a single additive score loses thresholds and physiologic coupling that could matter for cancer-survivorship triage. Both use the same inputs, cohort, split, annual outcome rows, missingness policy, uncertainty and late no-refit evaluation.

A gradient-boosted model is deferred unless the spline model cannot be implemented; it offers flexible shape discovery but less direct mechanistic interpretation. A latent organ-aging/GP model is deferred because this export lacks certified specimen timing, organ-age labels and validated genetic inputs. A sequence transformer is deferred because the local arrays are sparse code/date positions, not a certified longitudinal disease sequence, and it would answer a different representation question. Cystatin-C/eGFRcys, assay-selection weighting and N17/N18 renal endpoints are retained only as context from the two kidney candidates and are not model inputs or outcomes here. Imaging, stage, treatment and echocardiography branches are unavailable.

This tabular design is CPU-suitable. The future solver envelope is up to 16 CPUs, 262,144 MiB RAM and 28,800 seconds, with no mandatory GPU. Discovery used a bounded CPU source diagnostic; its measured structural checks are not estimates of full solver runtime. A future implementation may use the configured CPU image. An allocated A100 is unnecessary unless a bounded benchmark shows the spline/bootstrap package exceeds the CPU envelope; GPU choice cannot change the estimand.

## Evidence and limitations record

The following were read before design: `datasets/README.md`, `datasets/ukb/README.md`, the complete UKB table metadata relevant to the four inputs, `references/research-ambition/README.md`, `references/research-ambition/methods-and-compute.md`, `references/expert-seeds/README.md`, `references/expert-seeds/cards/ukb-08.md`, and the assessed parent. The cancer demonstration’s main article remains unavailable in the local bundle; no unavailable main-paper methods are claimed. The kidney assay candidates are context only and do not supply evidence for this cancer hypothesis.

All four configured dataset islands (UKB, MIMIC-IV, eICU and HCC) remain accessible with rows and notes. Only the exact UKB sources above are in scope, and no private clinical row or note is sent to public search.
