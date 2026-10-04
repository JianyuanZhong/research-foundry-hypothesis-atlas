{
  "title": "Early systemic treatment versus a third TACE after repeated TACE in HCC: a landmark emulation of hepatic-reserve preservation",
  "dataset": "hcc",
  "hypothesis": "Among adults with recorded hepatocellular carcinoma who have undergone two qualifying TACE episodes 14-180 days apart and have no recorded systemic HCC therapy through the second TACE, assignment to medication-defined systemic targeted or immune therapy within 90 days after the second TACE, rather than proceeding to a third TACE, is associated with better subsequent hepatic-reserve preservation without a higher risk of incident advanced-disease or hepatic-decompensation diagnoses.",
  "clinical_question": {
    "importance": "After repeated TACE, continuing locoregional treatment can expose patients to cumulative hepatic injury, while switching to systemic therapy may preserve liver function but can be constrained by toxicity, access, and treatment selection. The decision is consequential because preserved hepatic reserve affects eligibility for later cancer therapy and transplant-oriented care.",
    "strongest_existing_claim": "Public clinical literature supports that TACE is standard for selected intermediate-stage HCC and that repeated TACE may be inappropriate when response is inadequate or liver function is threatened; early systemic switching in TACE-refractory disease is an active, debated treatment paradigm. This evidence does not establish that an early switch preserves hepatic reserve or improves outcomes for this institution's patients.",
    "unresolved_claim_tested": "Within the observed institutional treatment pathway, whether early medication-defined systemic treatment after the second TACE is associated with a clinically meaningful difference in hepatic-reserve change and subsequent incident progression/decompensation compared with a third TACE.",
    "substantive_advance": "The design targets a specific post-second-TACE decision and uses a fixed assignment window plus a day-90 landmark, rather than treating the entire longitudinal record as an undifferentiated treatment association. It jointly evaluates liver preservation and disease-control signals and makes treatment-channeling, overlap, missingness, and unobserved radiographic response explicit."
  },
  "estimand": {
    "primary": "Among eligible patients who initiate either strategy within the 90-day assignment window, the adjusted intention-to-treat-like association of early systemic strategy versus third-TACE strategy with the difference in change in hepatic reserve from the pre-second-TACE baseline to the first eligible post-landmark measurement during days 91-270.",
    "secondary": "The corresponding 365-day risk difference or hazard ratio for first incident diagnosis-based hepatic decompensation and first incident diagnosis-based advanced disease after the day-90 landmark, among patients free of that endpoint at the landmark.",
    "interpretation": "Because treatment assignment is nonrandom and outside care, death, transplant status, performance status, radiographic response, and complete treatment intent are incompletely observed, estimates are associations under the recorded care pathway, not causal effects or treatment recommendations."
  },
  "population_and_time": {
    "eligibility": [
      "Age at the second qualifying TACE is at least 18 years when age is available; report the amount missing and run an all-ages sensitivity analysis if necessary.",
      "An HCC diagnosis name containing the exact observed term 肝细胞癌 is recorded on an encounter dated on or before the second TACE.",
      "The first qualifying pair is two distinct calendar-day TACE episodes for the patient, with the second 14-180 days after the first. Multiple same-day procedure rows are collapsed to one episode.",
      "No recorded medication-defined systemic HCC treatment starts before or on the second TACE. Procedure-level systemic-treatment labels are retained for a sensitivity definition.",
      "The second TACE has a valid start date and the patient has sufficient institutional observation to reach the day-90 landmark, unless death or loss of observation can be reliably ascertained in a sensitivity analysis."
    ],
    "time_zero": "The calendar day of the second qualifying TACE.",
    "assignment_window": "Days 1-90 after time zero. The final analysis uses exact day arithmetic on parsed local timestamps; exact dates are not released.",
    "strategies": {
      "early_systemic": "First medication-defined targeted or immune HCC systemic treatment starts on days 1-90 after the second TACE and before the first qualifying third TACE, or before a same-window competing TACE. Medication names are identified by a prespecified ontology including lenvatinib, sorafenib, regorafenib, sintilimab, tislelizumab, bevacizumab, camrelizumab, atezolizumab, pembrolizumab, donafenib, apatinib, and nivolumab; the execution log must record every matched generic/product string and exclude clearly non-HCC indications where documentation permits.",
      "third_tace": "First qualifying third TACE starts on days 1-90 after the second TACE and before the first medication-defined systemic treatment.",
      "ties_and_neither": "Exclude same-day ties and patients receiving neither mutually exclusive strategy from the primary contrast; retain them for a descriptive pathway table and an exploratory multinomial/sensitivity analysis."
    },
    "landmark": "Day 90 after the second TACE; outcomes and post-treatment covariates begin after this landmark to avoid immortal-time bias.",
    "follow_up": "From the day-90 landmark through 365 days for diagnosis outcomes, and through day 270 for the primary laboratory outcome, censoring at the last observed institutional encounter only in analyses that explicitly address informative observation."
  },
  "exposure_ascertainment": {
    "primary_table": "medications",
    "primary_fields": ["患者主索引", "就诊号", "用药", "开始时间", "结束时间", "用药方式", "药品类型"],
    "primary_time": "开始时间",
    "sensitivity_table": "procedures",
    "sensitivity_fields": ["患者主索引", "就诊号", "手术", "开始时间", "结束时间", "手术来源"],
    "sensitivity_time": "开始时间",
    "episode_rule": "Deduplicate by 患者主索引 and local calendar day after parsing 开始时间; preserve the raw row count and matched labels for audit. The exact first qualifying TACE pair is selected by scanning chronological episode days and taking the earliest pair with an interval of 14-180 days, not simply the first three raw rows."
  },
  "covariates_and_confounding": {
    "core": [
      "Age, sex, calendar year of time zero, and treating department/site proxy from encounters.",
      "Interval in days between TACE 1 and TACE 2 and recorded prior hepatic surgery, ablation, or transplantation procedures where ascertainable.",
      "Baseline laboratory values closest to the second TACE within the window from 30 days before through 7 days after: albumin 白蛋白, total bilirubin 总胆红素, INR 国际标准化比值, platelets 血小板计数, AFP 甲胎蛋白, and, if the assay and units are validated, creatinine and sodium.",
      "Pre-time-zero diagnoses joined to encounter timing: cirrhosis, portal hypertension, ascites, hepatic encephalopathy, variceal bleeding, liver dysfunction, diabetes, hypertension, viral hepatitis, portal-vein tumor thrombus, and extrahepatic metastasis.",
      "Recent treatment intensity and encounter frequency before time zero, derived only from records dated before time zero."
    ],
    "tumor_burden_and_response": "Use examinations joined by 患者主索引 and 就诊号, with 检查, 检查所见, 检查诊断, 开始时间, and 检查号. A prespecified lexical screen for lesion size/number, enhancement or washout, residual blood supply after TACE, portal-vein tumor thrombus, and ascites may define a sensitivity subset. It is not a validated mRECIST/RECIST extractor; clinician adjudication is required before using it as a definitive response endpoint or relying on it to remove confounding by indication.",
    "confounding_controls": [
      "Estimate propensity scores for strategy using only pre-time-zero variables, inspect standardized mean differences and positivity, and use overlap-restricted inverse-probability or stabilized weighting.",
      "Use doubly robust outcome regression for the primary continuous endpoint and weighted cumulative-incidence/risk-difference models for binary/time-to-event endpoints.",
      "Restrict or stratify by calendar era because systemic agents became available over time; repeat with procedure-defined exposure and medication-defined exposure.",
      "Report missingness by arm and use a prespecified missing-indicator/multiple-imputation sensitivity analysis only for clinically interpretable variables; do not impute absent imaging evidence as no disease."
    ]
  },
  "outcomes": {
    "primary": "Change in ALBI score from the baseline laboratory pair nearest the second TACE to the first post-landmark laboratory pair in days 91-270, if albumin and bilirubin assay units/scales are validated within the source. If units cannot be validated, replace ALBI with separately reported within-assay changes in albumin and total bilirubin and do not pool incompatible scales.",
    "secondary": [
      "First incident diagnosis of hepatic decompensation after the landmark: 腹腔积液 or 腹水, 肝性脑病, variceal bleeding terms, or 肝功能不全, with the same term absent before or at the landmark.",
      "First incident diagnosis of advanced disease after the landmark: portal-vein tumor thrombus terms or prespecified extrahepatic metastasis terms, with baseline presence excluded.",
      "Change in AFP using uncensored, assay-compatible quantitative values; censored results such as >60500 are not treated as ordinary numeric values and are analyzed separately or with censoring-aware methods.",
      "Subsequent treatment escalation and recorded encounter/hospitalization burden as exploratory utilization outcomes, recognizing that outside care and death are not fully observed."
    ],
    "endpoint_timing": "Diagnosis timing is inherited from encounters using 入院时间, falling back to 就诊时间, because diagnoses has no timestamp. Laboratory timing uses 检验时间; examination timing uses 开始时间; medication/procedure timing uses 开始时间."
  },
  "analysis_plan": {
    "descriptive": "Create a patient-level flow diagram with exact raw and deduplicated counts, strategy counts, availability of each covariate/outcome, and balance/overlap diagnostics. Do not release identifiers or exact dates.",
    "primary_model": "Weighted doubly robust regression for the continuous change outcome, with robust patient-level uncertainty intervals; report the adjusted mean difference with a prespecified clinically meaningful threshold chosen before viewing arm-specific outcomes.",
    "event_models": "For incident diagnosis endpoints, report weighted risks at 365 days and risk differences with confidence intervals; use competing-risk or censoring sensitivity analyses only if death/observation status is sufficiently ascertainable.",
    "uncertainty": "Use bootstrap resampling at the patient level or influence-function based intervals, and report effective sample sizes. Do not interpret statistical significance as proof of clinical benefit.",
    "sensitivity": [
      "90-day versus 60-, 120-, and 180-day assignment windows.",
      "Medication-defined versus procedure-label-defined systemic treatment.",
      "Alternative baseline and follow-up laboratory windows and complete-case versus missingness-adjusted analyses.",
      "Exclusion of patients with baseline portal-vein tumor thrombus, extrahepatic metastasis, transplant history, or major resection when the estimand is intended to represent liver-confined/intermediate-stage disease.",
      "Imaging-adjudicated subset and negative-control analyses using pre-landmark diagnoses that should not plausibly be changed by post-landmark strategy."
    ]
  },
  "falsification_and_interpretation": {
    "supportive": "After adjustment and overlap restriction, early systemic strategy shows a prespecified clinically meaningful favorable difference in hepatic-reserve change, with no clear increase in incident advanced disease or decompensation, and the direction is reasonably stable across exposure, era, and missingness sensitivities.",
    "adverse": "Early systemic strategy is associated with worse hepatic-reserve change and/or materially higher incident decompensation or advanced-disease risk, or apparent benefit disappears after accounting for baseline response/tumor-burden proxies. This would argue against assuming that switching is liver-sparing in this pathway, not prove that systemic therapy causes harm.",
    "falsifying": "The confidence interval excludes the prespecified clinically meaningful hepatic-reserve benefit and favors no benefit or harm, or a nominal benefit is contradicted by robustly higher progression/decompensation in the same estimand population. A null result is informative about this observed decision pathway even if it cannot exclude residual confounding.",
    "inconclusive": "Poor propensity overlap, insufficient paired laboratory observations, sparse incident events, unstable effective sample size, major disagreement between medication and procedure exposure definitions, or material sensitivity to unvalidated imaging extraction prevents a defensible conclusion.",
    "stronger_claims_not_supported": "This snapshot alone cannot establish mortality benefit, causal superiority, efficacy of any particular drug, validated radiographic response, safety toxicity rates without complete medication exposure/adjudication, or generalizability outside the institution. These require vital-status/out-of-system data, clinician-adjudicated imaging and toxicity, prospective measurement of performance status and treatment intent, or another comparative study."
  },
  "exact_data_binding": {
    "readme": "[internal dataset path]",
    "metadata": "[internal dataset path]",
    "tables": {
      "encounters": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": ["入院时间", "就诊时间", "出院时间"]},
      "procedures": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": ["开始时间", "结束时间"], "archive_member": "ordinary file"},
      "medications": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": ["开始时间", "结束时间"], "archive_member": "ordinary file"},
      "diagnoses": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": [], "archive_member": "ordinary file"},
      "labs": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": ["检验时间"]},
      "examinations": {"schema": "[internal dataset path]", "source": "[internal dataset path]", "keys": ["患者主索引", "就诊号"], "time_fields": ["开始时间"], "archive_member": "ordinary file"}
    },
    "additional_context_tables": {
      "clinical_documents": "[internal dataset path]",
      "pathology": "[internal dataset path]",
      "orders": "[internal dataset path]"
    },
    "join_rule": "Join every encounter-linked table to encounters on the composite key 患者主索引 + 就诊号; derive patient-level longitudinal intervals using within-patient timestamps only."
  },
  "feasibility_evidence": {
    "catalog": "[internal dataset path]",
    "medication_screen": "[internal dataset path]",
    "procedure_screen": "[internal dataset path]",
    "lab_screen": "[internal dataset path]",
    "observed_counts": "The bounded medication screen found 4,040 eligible patients after two TACE episodes with no prior medication-defined systemic treatment, 564 early-switch patients, 1,030 third-TACE patients, and 2,468 neither/other patients under the preliminary 90-day algorithm. These are feasibility counts, not final analytic counts; the executable analysis must apply the exact earliest 14-180-day pair rule, validate drug ontology and units, and recompute all endpoint availability under the final cohort. The procedure-label screen found 356 and 1,326 in the corresponding arms, demonstrating exposure-definition sensitivity."
  },
  "limitations": [
    "No explicit laboratory unit column; ALBI is conditional on assay-scale validation.",
    "No images; CSV examination reports are narrative and lexical extraction is unvalidated.",
    "Diagnosis rows have no timestamp and may reflect coding rather than disease onset; encounter date is only a proxy.",
    "No reliable complete vital-status, outside-care, performance-status, Child-Pugh, treatment-intent, or clinician-adjudicated toxicity fields were identified.",
    "Medication records may include starts, orders, discontinuations, or indications that require ontology and chart-context review.",
    "Residual confounding by tumor burden, radiographic response, frailty, access, and clinician preference remains likely."
  ],
  "provenance": {
    "snapshot_id": "[source checksum]",
    "source_data_read_only": true,
    "analysis_artifacts": "All feasibility outputs are derived workspace files; no source rows were modified or published."
  }
}
