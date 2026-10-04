> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

title: "Can a sparse CBC trajectory identify colorectal cancer early enough to improve fixed-capacity diagnostic prioritisation?"

parent_and_advance:
  dataset: "UK Biobank snapshot [source checksum]"
  parent: "[prior hypothesis]"
  advance: >-
    Retains the parent's directly feasible 1–5-year landmark question and conservative four-CBC
    event evidence, but makes the clinical decision explicit without claiming benefit: at a fixed
    diagnostic capacity, does within-person change improve concentration of registry CRC events
    beyond what a clinician already knows at the landmark? The primary estimand is a prespecified
    incremental association/prediction contrast, while sensitivity, PPV and event yield at 1%, 2%
    and 5% capacity are descriptive operating characteristics. Registry coverage, death and
    missingness become executable gates rather than post-hoc caveats. Three CBC slopes are the
    primary biological hypothesis; RDW is retained as a locked secondary extension so event
    feasibility is not purchased by data-driven selection.

clinical_question:
  question: >-
    Among cancer-free UK Biobank repeat-assessment participants aged 40–75 at a protocolized
    landmark, does annualized change in haemoglobin, MCV and platelet count between assessments
    0 and 1 add useful 1–5-year CRC risk information beyond age, sex and current CBC values,
    and does it concentrate CRC events more than incident non-CRC cancer at the same fixed
    diagnostic capacity?
  clinical_importance: >-
    A positive finding would justify external validation of a low-cost trigger for FIT or other
    diagnostic assessment, whereas a null or nonspecific finding would discourage burden from
    acting on sparse CBC trends. The configured data cannot test whether referral, FIT, colonoscopy,
    stage, treatment, mortality, harms or cost improves; this is a prognostic prioritisation study,
    not an impact or screening trial.
  strongest_evidence_supported: >-
    The inspected full text of BLOODTRACC (Virdee et al., BMC Cancer 2026, PMCID PMC13295383) supports
    prediction from clinically ordered longitudinal haemoglobin, MCV and platelet histories in a
    large primary-care population. The inspected cancer demonstration supplement reports longitudinal
    routine-laboratory cancer prediction, but its unavailable main article and STAR Methods are not
    claimed as read. Neither source establishes incremental value of two sparse protocolized UKB
    repeats, CRC specificity, fixed-capacity yield, or clinical benefit.
  unresolved_hypothesis: >-
    In sparse protocolized repeats, the prespecified forward CBC changes have incremental prognostic
    information for registry C18–C20 diagnoses during days 366–1825 after the landmark, beyond
    landmark CBC levels and age/sex; the signal should be stronger for CRC than for incident
    non-CRC malignant cancer. The competing hypothesis is no incremental information or a signal
    no more CRC-specific than general cancer/frailty.
  estimand: >-
    Primary: conditional cause-specific association of the three direction-coded annualized slopes
    and an incremental prediction contrast (trajectory model minus locked current-value model) for
    5-year CRC risk, with death treated as a competing event and non-CRC cancer retained in the risk
    set. Secondary: two-year and three-year landmark contrasts, cumulative incidence, and event yield
    among the highest 1%, 2% and 5% predicted-risk capacities. These are prognostic estimands, not
    causal effects or net benefit claims.

exact_data_bindings:
  join_key: "eid; one-to-one joins only; overlapping eid fields must agree"
  source_snapshot: "[source checksum]"
  archive_members: "All required sources are ordinary CSV files; no archive member is used."
  assessment:
    path: "[internal dataset path]"
    table: "assessment"
    catalog_schema: "[internal dataset path]"
    sha256: "[source checksum]"
    columns:
      - "eid"
      - "53-0.0: instance-0 assessment-centre date"
      - "53-1.0: instance-1 assessment-centre date and landmark/index date"
  biological_samples:
    path: "[internal dataset path]"
    table: "biological_samples"
    catalog_schema: "[internal dataset path]"
    sha256: "[source checksum]"
    columns:
      - "30020-0.0 and 30020-1.0: haemoglobin"
      - "30040-0.0 and 30040-1.0: mean corpuscular volume"
      - "30080-0.0 and 30080-1.0: platelet count"
      - "30070-0.0 and 30070-1.0: RDW, locked secondary only"
  population:
    path: "[internal dataset path]"
    table: "population"
    catalog_schema: "[internal dataset path]"
    sha256: "[source checksum]"
    columns:
      - "31-0.0: sex; authoritative coding 0 Female, 1 Male"
      - "34-0.0 and 52-0.0: birth year and month"
      - "21022-0.0: age at recruitment in years, sensitivity check only"
  health_outcomes:
    path: "[internal dataset path]"
    table: "health_outcomes"
    catalog_schema: "[internal dataset path]"
    sha256: "[source checksum]"
    columns:
      - "40006-0.0 through 40006-21.0: cancer registry ICD-10 codes"
      - "40005-0.0 through 40005-21.0: diagnosis dates paired by identical suffix to 40006"
      - "40000-0.0 and 40000-1.0: death dates"
      - "40001-0.0/1.0 and 40002 arrays: death causes, audit only; never predictors"
  metadata_and_provenance:
    catalog: "[internal dataset path]"
    known_limit: >-
      The catalog provides authoritative local metadata only for field 31/coding9 and field 21022;
      units, missing semantics, assay ranges and temporal annotations for CBC and registry fields are
      absent. Before analysis, freeze per-field UKB Showcase metadata for 53, 30020, 30040, 30070,
      30080, 40000, 40005 and 40006, recording URL, retrieval time and hashes. Retain raw values
      until this check; do not globally recode negative numbers or invent ranges. If identity,
      units, or missing-value semantics cannot be verified, stop inference and report infeasibility.

population_and_time:
  inclusion:
    - "Both 53-0.0 and 53-1.0 parse as valid dates, with instance 1 strictly later than instance 0."
    - "Elapsed interval is 1.0–8.0 years; report interval distribution and a 2–6-year sensitivity."
    - "All three primary CBC markers are paired numeric values at both instances; the conservative executable subset additionally requires paired RDW."
    - "Age calculated from 34-0.0/52-0.0 and 53-1.0 is 40–75 years inclusive; compare with 21022-0.0 plus elapsed time."
  exclusion:
    - "Any suffix-paired C00–C97 registry diagnosis on or before 53-1.0."
    - "Any C18–C20 diagnosis during days 0–365 after 53-1.0; retain counts by 0–90, 91–180, 181–365 as reverse-causation diagnostics."
    - "Impossible dates, duplicate or discordant eid joins, or values outside verified field-specific ranges."
  index: "53-1.0; no predictor may be measured or derived after this date."
  primary_window: "day 366 through day 1825 after index, exact dates and leap years handled with calendar-day differences"
  secondary_windows:
    - "day 366–1095 (1–3 years), preserving the parent's observed feasibility count of 40 as a descriptive check"
    - "day 366–730 (1–2 years), only if coverage-valid events support reporting"
    - "day 0–1825 and day 91–1825 as washout sensitivities, never replacements for the primary window"
  endpoint: >-
    First suffix-paired registry C18, C19 or C20 diagnosis date in the window. If a diagnosis date
    follows a recorded death, flag it as a data-quality inconsistency and do not count it as an
    observable event; report the audit count. Non-CRC C00–C97 diagnoses are not censoring for the
    CRC estimand and are a secondary specificity outcome.
  competing_death: >-
    Earliest valid 40000 date before CRC is a competing event. Cause-specific Cox censors at death
    for its mathematical risk-set construction but is labelled cause-specific; report Aalen–Johansen
    CRC cumulative incidence with death competing and a Fine–Gray sensitivity. Do not treat non-CRC
    cancer as censoring.
  registry_coverage_gate: >-
    Before modeling, use the frozen snapshot provenance and authoritative registry documentation to
    identify a defensible cancer ascertainment end date (and nation-specific rule if relevant). Never
    infer coverage from the last observed diagnosis. If a documented endpoint exists, include only
    horizons covered through that date or administratively censor at it using risk-set methods and
    report the fraction with complete nominal horizons. If no trustworthy endpoint can be established,
    report flow and raw event audits only and classify the prognostic result inconclusive.

feasibility_and_sampling:
  sampling: >-
    Full-row scans, not a sample, are required. Read only the named columns from the four read-only
    CSVs, join one row per eid, and emit a manifest containing source hashes, row counts, selected
    columns, parsing failures and all exclusion counts. No clinical record or row is sent to public
    search.
  known_parent_scan: >-
    A succeeded managed full-source feasibility artifact reports 20,343 participants with an
    instance-1 date, 18,379 with complete paired four-marker CBC, 1,801 prior malignant cancers,
    16,578 preliminarily cancer-free landmarks, 81 first CRCs in days 366–1825, and 40 in days
    366–1095. These establish feasibility only; final counts must be recomputed after field metadata,
    age, date, death, post-death and coverage checks. The three-marker-expanded cohort and competing
    event counts are not fabricated and must be reported by execution.
  event_rules:
    - "If coverage-valid primary CRC events are >=60, fit the locked primary association and prediction analyses."
    - "If 30–59 events, retain the locked low-dimensional association and descriptive capacity yields; do not fit flexible prediction models."
    - "If <30 events, report cumulative incidence, event audits and at most the prespecified simplest penalized association; prediction updating is inconclusive."
    - "If metadata or registry coverage fails, do not rescue the analysis by changing the window or selecting a different marker."

predictors_and_comparators:
  primary_slopes: >-
    For each m in haemoglobin, MCV and platelets, delta_m_per_year = (m_1 - m_0) /
    ((date_1-date_0)/365.2425). Direction-code as adverse = -haemoglobin slope, -MCV slope,
    +platelet slope. Standardize using controls in each training resample only. Enter the three
    continuous slopes as separate one-degree-of-freedom terms; no observed-outcome marker selection.
  current_value_comparator: >-
    Locked baseline model: age at landmark (restricted linear term only if event count allows,
    otherwise linear), sex, and the three instance-1 CBC values. This is the clinically available
    comparator. The trajectory model adds only the three locked slopes. Age/sex-only is descriptive.
  secondary_rdw: >-
    Current RDW and annualized RDW slope are a locked exploratory extension, reported only if the
    four-marker complete subset is used; never add RDW because it improves observed performance.
  pattern_summary: >-
    Secondary descriptive pattern: count of adverse-direction slopes (0–3), defined by sign only;
    do not call it iron deficiency or assign clinical thresholds without ferritin, transferrin
    saturation, symptoms, bleeding source and adjudication. Report marker-specific estimates and
    pattern counts without replacing continuous primary terms.
  specificity: >-
    Fit the same locked construction for first incident non-CRC C00–C97 cancer in the same window,
    excluding C18–C20. Similar or larger changes imply general occult illness, inflammation, frailty
    or cancer susceptibility rather than CRC specificity. Subsite C18–C19 versus C20 is descriptive
    and explicitly underpowered.

analysis:
  descriptive:
    - "Participant flow, duplicate/discordant joins, missingness by field and instance, date/range failures and visit interval."
    - "Included repeat attenders versus participants with valid instance-0 data but no instance-1 visit; no causal correction is claimed."
    - "CRC, non-CRC cancer, death-before-CRC, other censoring, post-death inconsistencies and coverage-valid horizon counts."
    - "Aalen–Johansen cumulative incidence at 2, 3 and 5 years with death competing."
  association: >-
    Fit a ridge-penalized cause-specific Cox model from day 366 with the locked baseline terms and
    trajectory terms. Report HR per training-set SD, the joint 3-df incremental test and bootstrap
    participant-level 95% intervals. Check proportional hazards. Fine–Gray is sensitivity only; do
    not switch the estimand because it gives a different result. Use Firth only if software is
    validated and label it sensitivity.
  prediction: >-
    If the event rule permits, use repeated nested participant-level 5-fold cross-validation with
    identical splits for baseline and trajectory models; otherwise bootstrap optimism correction or
    leave-one-event-out as predeclared. All standardization, missing covariate imputation and penalty
    selection occur inside training resamples. Report paired changes in Uno C-index, time-dependent
    AUC at 2, 3 and 5 years, integrated Brier score, calibration intercept and slope, and calibration
    plots with uncertainty. The primary incremental prediction contrast is the paired change in
    5-year time-dependent AUC, interpreted jointly with calibration and Brier score rather than a
    fixed arbitrary cutoff.
  capacity_operating_characteristics: >-
    At locked top 1%, 2% and 5% predicted-risk capacities, report number flagged, sensitivity,
    specificity, PPV, CRC events per 1,000 flagged, and proportion of all CRCs captured, all from
    held-out predictions and with bootstrap intervals. These describe prioritisation yield only;
    decision curves may be shown as exploratory net-benefit curves but must not be called clinical
    benefit or a referral threshold.
  missingness: >-
    Paired CBC missingness defines the primary cohort; do not impute missing historical CBC values.
    For optional covariates, impute only within training resamples and show complete-case sensitivity.
    Report missingness as a potential selection mechanism; do not use missingness to select a model.
  sensitivity:
    - "180-day and 730-day washouts, plus 1–3-year and 1–5-year horizons, with no post hoc best-window selection."
    - "2–6-year versus 1–8-year visit intervals."
    - "Raw change, annualized change and regression-to-the-mean residualized change, all prespecified."
    - "Exclude reviewed hospital code lists for anaemia, bleeding and inflammatory disease in the year before landmark only if exact code lists and metadata are frozen; this is a sensitivity, not a predictor."
    - "Sex-stratified and C18–C19 versus C20 descriptive analyses, labelled low precision."

falsification_and_interpretation:
  pipeline_falsification:
    - "Permute outcome labels within sex and 5-year age bands and rerun the full resampling pipeline; non-null incremental performance indicates leakage or implementation error."
    - "Use CRC dates before the landmark as an intentionally impossible temporal outcome; incremental performance indicates cohort construction or date leakage."
    - "Audit suffix pairing, dates after death, duplicate eids and all coverage truncation decisions."
    - "Do not reverse visit order as a negative control: it mechanically reverses slope directions and is not independent evidence."
  supportive: >-
    Support requires directionally coherent prespecified slope effects, a held-out incremental signal
    beyond current values that is not offset by worse calibration or Brier error, and capacity yields
    that are stable across resamples and materially more CRC-concentrated than the non-CRC comparator.
    Exact magnitude thresholds are not declared as truth because 81 preliminary events imply low
    precision. The strongest conclusion is incremental prognostic information in selected repeat
    attenders, sufficient to justify external validation with clinically timed CBCs; it is not a
    recommendation for screening or referral.
  adverse: >-
    Precise null or opposite-direction slopes, no held-out improvement, worse calibration/error, or
    similar-or-greater association for non-CRC cancer is adverse evidence against prioritising this
    sparse trajectory for CRC. It does not refute longitudinal prediction in indication-driven
    primary-care records.
  inconclusive: >-
    Unresolved field semantics, no defensible registry coverage endpoint, fewer than 30 coverage-valid
    events, broad intervals compatible with consequential benefit and no incremental value, unstable
    resamples, or discordance between discrimination and calibration is inconclusive. Report all
    computed bounds and stop rather than escalating model flexibility or changing the estimand.
  claim_limits: >-
    Computation can establish source integrity, cohort flow, temporal ordering, endpoint coding,
    event counts, associations, held-out performance and whether the result follows this framework.
    It cannot establish biological onset, symptoms, occult bleeding, iron deficiency, stage shift,
    treatment effect, mortality benefit, cost-effectiveness, acceptable colonoscopy burden, or which
    individual should receive FIT/colonoscopy. Those require clinical adjudication, external data,
    external calibration and a prospective impact study.

references_and_provenance:
  ambition_readme: "[internal dataset path]"
  inspected_literature:
    - "Virdee et al., BLOODTRACC, PMCID PMC13295383; full text was inspected by predecessor work."
    - "BLOTTED protocol, PMCID PMC9830700; full text was inspected by predecessor work."
    - "Cancer demonstration supplement and publisher metadata only; main article and STAR Methods unavailable and not claimed as inspected."
  feasibility_artifact: "[internal dataset path]"
  limitations: >-
    Healthy-volunteer and repeat-attender selection, conditioning on survival to instance 1, sparse
    two-point trajectories, regression to the mean, assay changes, and incomplete clinical context
    limit transportability. Reserved catalog partitions are not an independent validation set.
