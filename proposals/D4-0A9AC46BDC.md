> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Source-concordant absolute CBC cancer-type contrast

Status: planned Harbor experiment; no hypothesis fit or participant-level result has been executed in this branch.
Parent: [prior hypothesis].
Scientific change: make a first-CBC, fixed-profile source-concordance estimand primary, using separate paired registry and inpatient outcome series and a prespecified absolute-risk boundary. The parent repeated-CBC trajectory question is retained only as a conditional secondary analysis with a corrected, non-collinear parameterization.

## Opening, supported claim, unresolved claim, and clinical advance

The parent establishes a useful opening: repeated haemoglobin/RDW/platelet/WBC changes may differ between later colorectal cancer (CRC) and haematologic cancer, but a repeat assessment is selected by survival, cancer-free status, return attendance and observation practices. Its primary model also risks non-identifiability if baseline CBC, second CBC and their change are entered together, because second value = baseline value + change. The strongest evidence supports only a descriptive association between CBC measurements or trajectories and later coded cancer outcomes in selected cohorts [K1], including a CRC-only retrospective longitudinal signal [K2]. Reviews show that discrimination without calibration, external validation, and a clinically appropriate population does not establish clinical utility [K3]. None establishes that a CBC contrast is cancer-type-specific, persists after the near-diagnostic period, or survives a different ascertainment process.

The unresolved hypothesis is:

> Among adults with a complete first CBC and no registry- or inpatient-coded malignant cancer at the first assessment, the prespecified high-platelet/low-haemoglobin profile has a positive, clinically material CRC-over-haematologic absolute cumulative-incidence contrast during years 2–5 after assessment, and that contrast is concordant between the paired registry and inpatient outcome series.

This is a new observable implication. Biology or a durable site-related association predicts a similar delayed CRC-over-haematologic contrast under two outcome-capture processes, while proximity or ascertainment predicts an early-only signal, source reversal/displacement, or a shared contrast for other cancers. Agreement is compatibility with robustness, not proof of biology: both sources may share coding error, and indication, symptoms, test ordering and pathology are unavailable.

The clinical advance is a bounded interpretation decision. If the contrast is above a prespecified +1 percentage-point boundary in both sources and source-discordance is small, the CBC pattern merits indication-rich external validation as a cancer-type-specific association. If it is large only in the registry, only in inpatient data, confined to 0–90 days, or shared by other cancers, the result argues against treating a research-assessment CBC as a stable CRC-specific signal. This does not create a referral threshold or establish diagnostic accuracy.

## Exact source, table, namespace and columns

Use one read-only UKB source and no participant joins:

- Snapshot: `ukb-completed-subset-20261002`; catalog [source checksum].
- Catalog table: `datasets/ukb/table-5d49a6760e7ffdbd.json`; table `ukb671626.csv (Parquet)`; 502,371 rows; id column `eid`; identifier namespace `ukb671626`.
- Analysis input: `[internal dataset path]`; source ID `[UKB data file]`; [source checksum].
- Original lineage, not an analysis input: `[internal dataset path]`; source ID `[UKB data file]`; [source checksum]. It is an ordinary file, not an archive member.
- The catalog schema audit has 1,160 columns and confirms all required fields below, including 22 registry code/date pairs and 259 inpatient code/date pairs. The corresponding assessment-centre table is `ukb672073`; its fields must not be joined because no documented crosswalk is available.

Required fields and exact roles:

- Key and landmark: `eid`; `53-0.0` (date of attending assessment centre), parsed as T0.
- Baseline CBC exposure: `30000-0.0` WBC, `30020-0.0` haemoglobin, `30070-0.0` RDW, `30080-0.0` platelets. No imputation for these four fields.
- Baseline adjustment: `31-0.0` sex, `34-0.0` year of birth, `21001-0.0` BMI, `20116-0.0` smoking status, `30710-0.0` CRP. Derive age at T0 from T0 and `34-0.0); do not use a field from another namespace.
- Registry outcome pairs: for j=0,...,21, pair `40006-j.0` (ICD-10 cancer type) only with `40005-j.0` (date of cancer diagnosis). A valid record requires both a parseable date and code at the same j.
- Inpatient outcome pairs: for k=0,...,258, pair `41270-0.k` (diagnosis ICD-10) only with `41280-0.k` (date of first in-patient diagnosis ICD-10). A valid record requires both at the same k. These are a second ascertainment series, not a gold standard and never pooled with registry dates.
- Death competing event: `40000-0.0` (date of death). `40001-0.0` is audit-only.
- Secondary repeat-selection stress test only: `53-1.0`, `30000-1.0`, `30020-1.0`, `30070-1.0`, `30080-1.0`. No future repeat variable enters the primary model.

Normalize codes only by trimming, uppercasing and removing punctuation; retain original strings for the audit. CRC is C18–C20 inclusive, haematologic cancer is C81–C96 inclusive. Other primary malignant cancer is C00–C97 excluding C77–C79 and excluding the two target families. Codes outside these definitions are not assigned to a target. Report missing pair members, invalid dates, duplicate eids, ties and class denominators.

## Population and temporal boundaries

The primary population includes one row per unique eid with a parseable T0 and complete baseline CBC. Exclude any valid CRC, haematologic or other-primary cancer event in either source on or before T0, and exclude death on or before T0. Report registry-only, inpatient-only and intersection exclusions; this source-clean entry is needed so source comparisons do not use different prevalent-cancer populations.

Follow separately in each outcome source from T0 to the first source-specific CRC, haematologic cancer, other primary cancer, death, or the fixed administrative boundary T_admin=2022-06-01, whichever comes first. The parent source audit observed 2022-06-01 as the maximum non-missing primary registry date; the solver must recompute that checksum and flag any valid date beyond it rather than silently extending follow-up. A same-day cancer-class tie is a separate multi-class event and is not forced into a CRC-versus-haematologic contrast. A same-day cancer/death tie follows the prespecified cancer-first convention and is counted.

The primary delayed estimand uses participants who are alive and free of a source-specific target/other cancer through T0+2 years, with follow-up in (T0+2,T0+5]. This is explicitly conditional survivor risk, not an unconditional natural-history effect. The 0–90 day, 90-day–2-year, and full 0–5 windows are timing falsifications/context; the 0–2 window is not silently combined with the delayed primary. If a participant is source-clean at T0 but not at T0+2, they contribute to the earlier window and are excluded from the delayed risk set.

The secondary repeat analysis defines R=1 as a strictly later parseable `53-1.0` with all four instance-1 CBC values observed; R=0 otherwise. It is conditional on repeat attendance, survival and source-clean status at T1. It is not a baseline predictor and cannot overturn the first-CBC primary result. For selection stress testing, fit a baseline-only R model using age, sex, BMI, smoking, CRP, baseline CBC and T0 year; compare unweighted and stabilized inverse-probability-of-repeat weighted estimates with fixed 1st/99th percentile trimming, balance and positivity reports. Treat this as measured-selection sensitivity, not causal adjustment.

## Fixed-profile estimand and outcome bridge

Standardize the four baseline CBC measures using development-partition means and SDs. Define two fixed profiles, applied only at prediction time:

- g_CRC: platelet +1 SD, haemoglobin −1 SD, WBC and RDW at their development means.
- g_HEME: platelet −1 SD, haemoglobin +1 SD, WBC and RDW at their development means.

For source s in {registry, inpatient} and cancer class c, let P_s(c,g,w) be the model-standardized cumulative incidence by the end of window w, averaging over each held-out participant's observed age, sex, BMI, smoking, CRP and T0 calendar year while replacing only the four CBCs by g. Define:

- Δ_s,c(w) = P_s(c,g_CRC,w) − P_s(c,g_HEME,w)
- T_s(w) = Δ_s,CRC(w) − Δ_s,HEME(w), the CRC-over-haematologic absolute contrast
- G_s(w) = mean[Δ_s,CRC(w), Δ_s,HEME(w), Δ_s,OTHER(w)], a shared cancer-burden component
- S_s(w) = Δ_s,CRC(w) − mean[Δ_s,HEME(w), Δ_s,OTHER(w)], a CRC-specific residual

The primary estimand is T_registry(2–5) and T_inpatient(2–5), with their difference and bootstrap interval. The clinically consequential descriptive boundary is T_s(2–5) > +0.01 (one percentage point) in each source, with |T_registry−T_inpatient| ≤ 0.01. This is a study interpretation boundary, not an individual diagnostic or referral threshold. Also report all component risks, Δ, G and S; a large G with small S means a generic cancer/ascertainment signal, even if prediction is strong.

For same-class events observed in both sources, pair the earliest post-T0 event per participant and class and report n, median inpatient-minus-registry date, IQR, 5th/95th percentiles, and fractions crossing 90 days, 2 years and 5 years. This is a source-displacement audit, not a claim about true biological onset. If fewer than 50 paired events exist for a class, that class's source-displacement conclusion is inconclusive.

## Baseline versus learned alternative

The selected transparent baseline fits separate cause-specific Cox models for CRC, haematologic cancer, other primary cancer and death, separately for registry and inpatient outcomes. Inputs are the four baseline CBC z-scores, age, sex, BMI, smoking, CRP, T0 calendar year, and a fixed 0–2/2–5 interval indicator. No baseline, second-visit and change terms are simultaneously entered. Compute T, G, S and component cumulative incidences with Aalen–Johansen/model-standardized predictions, robust participant-level intervals, proportional-hazard diagnostics and convergence records.

The substantive learned alternative is a CPU gradient-boosted discrete-time multi-task competing-risk model with the same participants, same source-specific outcomes, same covariates, same fixed profiles, same windows and the same temporal split. Use one early 0–90-day interval, subsequent yearly intervals, and separate hazards for CRC, haematologic cancer, other primary cancer and death. The learned model can reveal nonlinear CBC ranges, interactions, and time-varying source/class contrasts that an additive Cox average loses. It cannot reveal symptoms, clinical indication, pathology or mechanism and is not justified by a small AUC gain alone.

Sort by T0 then eid and hold out the latest 30% of eligible participants; the earliest 70% is development. Keep each eid in one split. Fit scaling, missingness rules, tuning, calibration and profiles in development only. On the locked holdout report T/G/S/component risks, 95% participant-bootstrap intervals (500 replicates), target-specific calibration intercept/slope and plots, cumulative-incidence Brier and log scores at 2 and 5 years, and time-dependent discrimination secondarily. If the holdout contains fewer than 50 haematologic events in either source, source-specific learned type contrasts are inconclusive regardless of point estimate; do not replace the temporal holdout with a random split.

The baseline is selected because its contrast is visible and directly auditable. The learned model is retained for a substantive uncertainty—nonlinear and time-varying CBC/source interactions—not for complexity or ranking. A neural sequence, GP or transformer model is deferred: the primary question uses one CBC visit, and extra latent-state capacity cannot recover indication or source correctness. Revisit only with richer dated clinical measurements and adequate repeat target events.

## Falsification and interpretation

Supportive evidence requires:

1. Both source-specific delayed T_s(2–5) estimates are positive, their 95% intervals exclude zero and their point estimates exceed +1 percentage point, with the predeclared source difference within ±1 percentage point.
2. S_registry and S_inpatient are positive and the other-cancer Δ is materially smaller than CRC Δ in both sources; a broad G component alone is not supportive.
3. The learned model reproduces the direction and fixed-profile source contrast on the temporal holdout with acceptable calibration and Brier/log performance; a ranking gain without the prespecified contrast is not supportive.
4. The contrast is not confined to 0–90 days, one calendar era, one gap/selection stratum, or R=1 repeat attendees.
5. Registry/inpatient date pairing and class support meet the predeclared thresholds; type-label permutation in development collapses T toward zero.

Adverse evidence is a precise delayed reversal, source reversal, a source difference above +1 percentage point, comparable other-cancer contrast, a large G with small S, early-only concentration, or a learned-only ranking gain. These weaken stable CRC specificity but do not refute a generic CBC–cancer association.

Inconclusive evidence includes fewer than 50 held-out haematologic events, fewer than 50 same-class source-paired events for the displacement claim, intervals spanning both zero and +1 percentage point, poor calibration, nonconvergence, invalid pair/date support, poor repeat-weight positivity, or a wide null. An imprecise null is not mechanistic refutation.

Computationally checkable claims are cohort flow, paired-field integrity, source-specific event timing, T/G/S contrasts, absolute boundary, source displacement, temporal/era/other-cancer/permutation checks, holdout calibration and uncertainty. Essential unavailable evidence includes symptoms, reason and order date for the CBC, primary-care contacts, ferritin/iron, reticulocytes, FIT, smear, marrow/pathology, stage, treatment, imaging, transfusion context, healthcare utilization and expert cancer adjudication. Even source-concordant association cannot establish biology, causality, diagnostic accuracy or clinical utility; those require indication-linked external data and prospective decision-impact evaluation.

## Actual scientific deliverable and alternatives not chosen

Completion requires newly fitted source-specific transparent and learned models and these outputs: locked cohort/exclusion and pair-integrity audit; split manifest; event counts by source/class/window; T/G/S and component risks with 500-bootstrap intervals; source date-displacement and capture tables; early-band, other-cancer, calendar-era, repeat-selection and type-permutation falsifications; holdout calibration/Brier/log outputs; and a conclusion explicitly classified supportive, adverse or inconclusive and linked to those files. A readiness probe or fit alone is not completion.

The parent is not discarded as evidence. Its repeated CBC trajectory contrast becomes a secondary conditional analysis only after reparameterizing it: either baseline CBC plus changes (not second CBC) or baseline plus second CBC (not changes), with the same outcome/source rules. This prevents the parent's linear dependence from producing an uninterpretable primary coefficient. The secondary may be abandoned if the repeated landmark has fewer than 50 held-out haematologic events, as the parent audit already suggests sparse support.

A static threshold-only analysis was not selected because it discards continuous information and makes cutoffs look clinical. The first-CBC fixed-profile analysis is selected over a repeat-only design because it removes future attendance from the primary estimand. The source bridge is selected over an assessment-centre join because the catalog documents ukb672073 as a distinct namespace without a crosswalk. A causal model, mechanism label, clinical referral threshold, or diagnostic net-benefit analysis is deferred because required indication, adjudication and decision data are absent.

Discovery resource facts are measured: the catalog/schema audit confirmed 1,160 columns, 502,371 rows, the exact field sets and namespace; the parent's bounded Parquet audit found 478,033 complete first CBCs and 18,377 complete first/second CBC pairs, but those are feasibility audits, not this child's results. Future fitting is unverified and budgeted at 8–16 CPU cores, 32–64 GiB RAM, approximately 2–4 hours including source-stratified fits, person-period expansion and 500 bootstrap replicates. No GPU is requested; the available A100 hardware does not add scientific value for this tabular workload. The configured future solver planning envelope is up to 16 CPUs, 262,144 MiB and 28,800 seconds; this discovery branch does not launch the solver.

## Three inspected works

[K1] Virdee et al. systematically review blood-test trends and report heterogeneous, limited evidence across test/cancer combinations, including limited evidence for haematologic cancer. This supports the opening and the need for a bounded comparison; it does not establish the UKB source-concordant hypothesis.

[K2] Sala et al. report retrospective longitudinal CBC deviations up to 24 months before CRC and explicitly describe the result as investigational pending independent validation. This motivates the delayed timing test; it does not establish cancer-type specificity or registry/inpatient robustness.

[K3] Hampton et al. review symptomatic CRC prediction models and emphasize calibration, bias, heterogeneity and limited external validation. This motivates the locked temporal holdout and calibration; symptomatic-population results cannot be transferred to an unindicated UKB research-assessment CBC.

Exactly three distinct works are attached locally: `key-references.json`, `K1-virdee-abstract-excerpt.txt`, `K2-sala-abstract-excerpt.txt`, and `K3-hampton-abstract-excerpt.txt`. Each excerpt is an explicitly labeled abstract/provider-response inspection with a hash over the attached UTF-8 bytes; no unavailable paper text or supplementary methods are claimed here.
