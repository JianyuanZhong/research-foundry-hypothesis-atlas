# Five-year renal-vulnerability interaction after an audited UKB provenance repair

## Episode decision and unresolved claim

Parent: `[prior hypothesis]`. This is a targeted scientific repair of the UK Biobank creatinine–cystatin C discordance question, not a new topic.

Haines et al. (CJASN 2023), which I read locally at `references/expert-seeds/papers/kidney-function/article.readable.txt`, studied 38 mechanically ventilated ICU patients with serial creatinine, cystatin C, measured GFR by iohexol clearance and muscle ultrasound. It supports a critical-illness physiological concern that creatinine-based eGFR can overestimate filtration during muscle loss. It does not establish a community UKB association, a grip interaction, renal-event specificity, or benefit from cystatin-C testing.

The unresolved, falsifiable claim is:

> Among UKB participants with valid initial creatinine, cystatin C and bilateral grip, without a previously recorded paired N17/N18 hospital diagnosis, lower standardized (D=eGFR_{cys}-eGFR_{cr}) has a positive interaction with lower standardized grip for the five-year cumulative incidence of a first subsequently recorded paired N17 diagnosis, conditional on eGFRcr, age, sex and BMI.

This is a prognostic association with a recorded hospital-code endpoint. It is not a claim about true filtration, muscle mass, AKI stage, causality, treatment benefit, or clinical utility. If supported, it would justify prospective validation of selective cystatin-C measurement or kidney surveillance in a functionally vulnerable subgroup; if null, it would weaken the case that this discordance pattern adds renal prognostic information in this selected population.

## Exact data binding and audited availability

Use UKB snapshot `[source checksum]`, catalog [source checksum], and read-only ordinary CSV sources:

- `population`, `datasets/ukb/table-38565c9e35e7cb6c.json`: `[internal dataset path]`; `eid`, `31-0.0` (sex), `21022-0.0` (age at recruitment).
- `assessment`, `datasets/ukb/table-901ef6c7ddce2d51.json`: `[internal dataset path]`; `eid`, `53-0.0` (assessment/index date), `21001-0.0` (BMI), `46-0.0`, `47-0.0` (initial left/right grip).
- `biological_samples`, `datasets/ukb/table-c6b666d905f3b02f.json`: `[internal dataset path]`; `eid`, `30700-0.0` (creatinine), `30720-0.0` (cystatin C). Repeat `30700-1.0`/`30720-1.0` are sensitivity-only, never assumed to be dated longitudinal measures.
- `health_outcomes`, `datasets/ukb/table-3cfae45e0905b0e3.json`: `[internal dataset path]`; `eid`, all `41270-0.0` through `41270-0.258`, paired only with the equal-suffix `41280-0.0` through `41280-0.258`, and `40000-0.0`, `40000-1.0` death dates. The live header has 259 code columns and 259 date columns; the terminal fields are `41270-0.258` and `41280-0.258`.

A successful read-only lexical audit is preserved at `work/episode7_event_audit.json` (job `[research job]`, [source checksum]). It reports 502,370 rows, 502,370 unique eids and no duplicate eids; 6,888,112 nonempty codes, 6,888,028 nonempty dates and valid code/date pairs, 84 code-without-date cases, no date-without-code cases and no malformed dates. Lexically there are 25,794 N17-prefixed and 32,764 N18-prefixed code/date pairs; these are not called verified events until code semantics are established. Death fields contain 44,499 and 60 nonempty values, with observed death dates 2006-05-10 to 2022-12-19. The audit does not establish that either death field is complete or that the maximum date is an administrative cutoff.

Before fitting, produce a versioned manifest that verifies field units/ranges and missing-value handling, sex and age meanings, the exact N17/N18 code representation and code set, `41280` paired-date/linkage semantics, death-field compatibility, biomarker/index compatibility, and the common administrative end date. The local metadata freezes age and sex coding but explicitly says most units, code dictionaries and exact date semantics are absent. Failure of any required verification is an inconclusive provenance result; do not substitute prefix matching, inferred units, a maximum observed date or an inferred cutoff.

## Population, time and outcomes

After one-to-one horizontal joins by `eid`, require finite, metadata-valid age 40–69, sex, BMI, both initial grip fields, both biomarkers and a valid `53-0.0` date. Use mean left/right grip in kg. Exclude death on/before index, ambiguous index dates, and any valid paired N17/N18 code/date on/before index; an index-date diagnosis is temporally ambiguous. This absence criterion covers only these linked hospital arrays, not outpatient or unlinked disease.

Only equal-suffix pairs are valid. After the verified dictionary permits the exact frozen codes, a first paired N17 date strictly after index is the primary endpoint; N18 is secondary. A same-day N17/death is death-first in the primary analysis and N17-first in a sensitivity. Follow to first N17, death, verified administrative end or five years. Death is a competing event, not ordinary censoring. The analysis cannot infer KDIGO AKI, CKD chronicity, outpatient disease, complete follow-up or clinical adjudication.

Support gates are prerequisites: at least 100 verified post-index N17 events and at least 20 in each four-sign D/grip quadrant for the transparent interaction; for the learned alternative, at least 200 N17 events, 100 competing deaths and adequate support at every grid cell. If provenance or the transparent gate fails, report the audit/cohort only as inconclusive. If only the learned gate fails, fit the transparent analysis and defer the learned alternative.

## Exposure and primary estimand

After unit verification, convert creatinine from micromol/L to mg/dL and retain cystatin C in mg/L. Freeze the race-free CKD-EPI 2021 creatinine equation and standalone cystatin-C equation before outcome fitting:

[
eGFR_{cr}=142,min(S_{cr}/k,1)^alpha max(S_{cr}/k,1)^{-1.200}0.9938^{Age}1.012^{Female},
]
with female (k=.7,alpha=-.241), male (k=.9,alpha=-.302), and
[
eGFR_{cys}=133,min(S_{cys}/.8,1)^{-.499}max(S_{cys}/.8,1)^{-1.328}.996^{Age}.932^{Female}.
]
Define (D=eGFR_{cys}-eGFR_{cr}). Standardize eGFRcr, D and grip using training parameters; lower D is the prespecified direction but is not interpreted as filtration error.

The primary clinical estimand is the five-year competing-risk risk-scale interaction:
[
I_5=CIF^{N17}_5(-1,-1)-CIF^{N17}_5(+1,-1)-CIF^{N17}_5(-1,+1)+CIF^{N17}_5(+1,+1),
]
where coordinates are standardized D and grip at ±1 SD and risks are standardized over observed age, sex, BMI and eGFRcr. Report all four risks, component contrasts, (I_5), 95% participant-bootstrap intervals and a descriptive 1-percentage-point meaningfulness flag, not a clinical threshold.

The transparent nested cause-specific Cox baseline uses the same eligible population and participant split: B0 = eGFRcr, grip, age, sex, BMI; B1 adds D; B2 adds D×grip and is primary. Estimate N17 CIF with fitted N17/death hazards and Aalen–Johansen/model-based competing-risk integration; the Cox coefficient is secondary. Report robust eid-level uncertainty, proportional-hazards and risk-support diagnostics.

## Same-question learned alternative

Fit a shallow one-year discrete-time competing-risk model with separate N17 and death hazards using exactly the six baseline inputs (eGFRcr, D, grip, age, sex, BMI), the same index/exclusions/outcomes and the same competing-risk process. Use a frozen eid-level 60/20/20 train/validation/test split; estimate transformations, imputation, tuning and censoring weights in training only; use depth 2–3, fixed leaf size/regularization and validation-selected iterations. Report test (I_5), four grid CIFs, IPCW Brier/integrated Brier, time-dependent discrimination, N17/death calibration and participant-bootstrap intervals.

This alternative can reveal a stable threshold or curved D-by-grip risk region lost by B2’s single log-linear interaction. It is not selected for a small AUC gain: it must be stable, calibrated, supported and alter an interpretable risk contrast. CPU-only fitting is adequate (at most 4 CPUs, 8 GiB RAM, approximately two hours plus bounded bootstrap); no GPU is needed or rewarded. A raw-biomarker or restricted-spline analysis is a sensitivity, not a new scientific claim.

## Falsification and interpretation

Preserve source-to-analysis flow, missingness, joins, overlap disagreements, baseline selection, value ranges, event support and all transformations. Run:

- strict code/date and same-day death-ordering sensitivities;
- N17-only versus N17/N18 baseline exclusion;
- a two-year survivor/landmark analysis, explicitly noting its changed population;
- raw-biomarker sensitivity and repeat-biomarker sensitivity only if timing is verified;
- within-sex-by-age-stratum permutation of D with a frozen seed; persistence indicates leakage or implementation error;
- a preselected K35 nonrenal control only after exact semantics and support are verified. A comparable K35 interaction weakens renal specificity but does not prove confounding; failure to support K35 leaves specificity unresolved.

Supportive evidence requires all provenance/support gates, positive (I_5) with a 95% interval excluding zero, persistence under strict timing and landmarking, and no comparable supported K35 interaction. It supports only a selected-cohort association with prospectively recorded hospital codes. Adverse evidence is a precise null/opposite, no increment from B1/B2, loss after timing/landmark controls, a comparable K35 result, or an unstable/poorly calibrated learned surface. Inconclusive evidence includes missing semantics, units, timing or cutoff, inadequate events/quadrants, unpaired dates, unsupported cells or failed calibration. No result establishes measured filtration, muscle mediation, AKI stage, causality or clinical utility.

## Demonstration and alternative dispositions

Delphi’s read structured disease histories support a possible UKB sequence adaptation, but this question is an index-time biomarker/function interaction; outcome semantics and precise timing remain the limiting dependency, so sequence learning is deferred. ALADYNOULLI’s read article supports latent longitudinal EHR/genetic modeling, but verified repeat specimen timing and the paper’s genetic inputs are unavailable; an EHR-only latent model would change the question and is deferred. Oncoformer’s supplement was read, but its main article/STAR Methods remain unavailable and raw chest images are absent; a lab-only variant would not resolve a distinct uncertainty here and is deferred. The UKB seeds on organ aging, sleep regularity, protective factors, infection/CVD, CHIP and cancer reserve remain repairable provenance branches because required derived aging/PRS/proteomic/timing/code definitions are not frozen. Revisit only when those dependencies are verified.

## New scientific deliverable and limits

Completion requires newly computed provenance/join/event audits, eligible flow and missingness, exposure distributions, exact support counts, fitted B0/B1/B2 (I_5) and uncertainty, four CIFs and component contrasts, N18 secondary, timing/landmark/K35/permutation diagnostics, and—only if gated—the held-out learned competing-risk surface and calibration/uncertainty. Conclusions must cite these outputs; the lexical audit is not a clinical result.

Expert clinical review, adjudicated longitudinal creatinine/urine-output AKI, measured GFR, inflammation/body-composition data, treatment context, independent validation and prospective decision-impact evaluation are required for stronger claims. Repeat trajectories, inverse-probability selection weighting, causal treatment analyses and latent disease sequences are retained as deferred alternatives with those explicit dependencies.
