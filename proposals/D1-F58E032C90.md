> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Working proposal: temporal discordance between liver tests and albumin after decompensation

## Question and clinical importance

For adults with a liver cirrhosis diagnosis who experience a first inpatient decompensation event, does a worsening discordance between the trajectory of liver-specific tests (AST, ALT, ALP, bilirubin) and the trajectory of albumin predict a subsequent clinically meaningful deterioration, beyond what the current severity at the index event already predicts?

The clinical problem is that cirrhosis is heterogeneous. A patient may have relatively preserved synthetic function (albumin) while showing hepatocellular or cholestatic injury, or the reverse. This discordance may indicate different pathophysiologic states, treatment needs, or risk of progression. If it carries prognostic information beyond the index event, it could inform follow-up intensity and the need for hepatology review.

## Evidence and closest work

Routine laboratory trajectories are known to predict mortality and hospitalization in cirrhosis, and dynamic biomarkers are used in prognostic models. However, most existing work either treats laboratory values as contemporaneous predictors or focuses on aggregate severity scores. The unresolved question is whether the *directional mismatch* between two complementary laboratory domains over a defined post-event window is itself prognostic, or whether it merely reflects the level of illness at the index event, measurement timing, or treatment changes.

The three demonstration papers are not direct HCC-specific prior work. The natural-history transformer study demonstrates longitudinal modeling of disease progression; the cancer longitudinal EHR study illustrates routine-data prognostic modeling; and the Bayesian longitudinal EHR study illustrates joint modeling of longitudinal outcomes. None of them establishes the specific discordance question in cirrhosis. The closest relevant evidence is general prognostic modeling with longitudinal biomarkers; the remaining gap is the explicit discordance estimand and its comparison with current-severity baselines.

## Hypothesis

In the HCC cohort, among patients with a cirrhosis diagnosis and a first inpatient decompensation event, a post-index worsening discordance between liver-specific laboratory trajectories and albumin trajectory is associated with a higher risk of subsequent clinical deterioration (new decompensation, ICU admission, or death within 180 days), after adjustment for age, sex, index event severity, and baseline laboratory levels.

## Data bindings

All data are from the HCC snapshot ([source checksum]).

- `encounters` table from `HCC/data_基本信息_2500296761891079109.csv`: patient identifier, encounter identifier, admission/discharge times, and encounter-level fields.
- `diagnoses` table from `HCC/data_诊断_7504718184492840569.csv`: patient/encounter identifiers, diagnosis codes/text, and diagnosis time. Used to identify cirrhosis and decompensation events.
- `labs` table from `HCC/data_检验_609065997844652188.csv`: patient/encounter identifiers, test name/code, result value, unit, and collection time. Used for AST, ALT, ALP, bilirubin, and albumin trajectories.
- `vitals` table from `HCC/data_体征数据_3824052911997097911.csv`: patient/encounter identifiers and vital sign measurements with times, for severity context.
- `transfers` table from `HCC/data_出入转_7369490831683459252.csv`: patient/encounter identifiers and location/time, for ICU admission and discharge/death context.
- `medications` table from `HCC/data_用药_5693407050835159466.csv`: patient/encounter identifiers, medication name, dose, and time, for treatment context and sensitivity analysis.
- `clinical_documents` table from `HCC/data_病历文书_8434587325530196878.csv`: patient/encounter identifiers and document text/time, for adjudicating decompensation events where diagnosis codes are ambiguous.

The exact join keys and time fields must be verified against the table schemas and source headers before the experiment is run. The catalog metadata is authoritative for field names; missing labels are not a restriction on access.

## Population and temporal boundaries

1. Include adults (age >= 18) with at least one cirrhosis diagnosis in the diagnoses table.
2. Identify the first inpatient decompensation event: an encounter with a diagnosis or clinical-document indicator of ascites, hepatic encephalopathy, variceal bleeding, or acute-on-chronic liver failure, occurring after the cirrhosis diagnosis.
3. Index time is the admission time of that encounter.
4. Require at least one valid albumin and one valid liver-specific test (AST, ALT, ALP, or bilirubin) in the 30 days before index and at least one in the 30–90 days after index.
5. Exclude encounters with missing or non-standard units that cannot be reconciled, and exclude patients with no follow-up encounter or death record within 180 days after index.

## Variables and estimand

- Baseline covariates: age, sex, index event type, index encounter severity (ICU admission, vital signs, laboratory values at index).
- Laboratory trajectories: for each of AST, ALT, ALP, bilirubin, and albumin, compute the slope or change from the pre-index 30-day mean to the post-index 30–90-day mean, using available measurements.
- Discordance measure: the difference between the standardized change in a composite liver-specific score (mean of standardized AST, ALT, ALP, bilirubin changes) and the standardized change in albumin. A positive value indicates liver-specific tests worsening while albumin is stable/improving, or albumin worsening less than liver-specific tests.
- Outcome: a binary indicator of subsequent clinical deterioration within 180 days: new decompensation event, ICU admission, or death. Death is inferred from discharge/death fields or the absence of subsequent encounters with a death indicator; this must be adjudicated from the available fields.
- Primary estimand: the adjusted association between a one-standard-deviation increase in discordance and the 180-day risk of deterioration, expressed as a risk difference or hazard ratio with 95% confidence interval.

## Baseline and learned alternative

- Baseline: a Cox proportional hazards model or logistic regression with baseline covariates and index-event severity, no post-index trajectory information. This establishes the prognostic value of current severity.
- Substantive alternative: a flexible longitudinal model (e.g., a gradient-boosted tree model or a Bayesian joint model) that uses the sequence of post-index laboratory measurements and captures nonlinear or time-varying relationships. This could reveal whether the simple discordance summary is sufficient or whether the full trajectory carries additional information.
- Comparison: both models are trained on the same population and evaluated on the same 180-day outcome using time-based train/validation/test splits. The learned model is not required to outperform the baseline; its value is to test whether the discordance summary captures the relevant information or whether a more complex trajectory representation is needed.
- Resources: CPU-only, with a bounded pilot on a subset of patients to estimate runtime. The full analysis is expected to fit within the solver envelope of 16 CPUs, 256 GB memory, and 28800 seconds.

## Falsification and interpretation

- Supportive result: discordance is significantly associated with the outcome after adjustment, and the association is stable across sensitivity analyses (different discordance definitions, exclusion of early post-index measurements, adjustment for treatment changes).
- Adverse result: discordance is not associated with the outcome after adjustment, or the association is explained by index-event severity or measurement timing. This would suggest that the discordance is not an independent prognostic signal and that current severity is sufficient.
- Inconclusive result: the association is present but unstable across sensitivity analyses, or the confidence interval is wide. This would suggest that the question requires a larger cohort, better adjudication, or a different discordance definition.
- A positive result would not establish a causal mechanism; it would support a prognostic association and motivate further work on the pathophysiologic interpretation.

## Key references

[K1] Wei H, Zhang J, Yu S, Zhang C, Weng Y, Shao M. Association Between Lactate Trajectories and Clinical Outcomes in Critically Ill Patients with Sepsis-Associated Liver Injury. J Clin Med. 2026;15(17):6837. doi:10.3390/jcm15176837. This work demonstrates that dynamic lactate trajectories in liver injury are prognostic for mortality, supporting the general principle that laboratory trajectories carry prognostic information. It does not address the specific discordance between liver-specific tests and albumin in cirrhosis.

[K2] Liu J, Cai H, Feng J. In-hospital inflammatory-nutritional-renal trajectory phenotypes and 90-day readmission or mortality in patients with acute decompensated heart failure: a retrospective cohort study. Front Cardiovasc Med. 2026;13:1900715. doi:10.3389/fcvm.2026.1900715. This work demonstrates that trajectory phenotypes of inflammatory, nutritional, and renal biomarkers are associated with post-discharge outcomes, supporting the use of trajectory-based prognostic modeling. It does not address the specific discordance between liver-specific tests and albumin in cirrhosis.

[K3] Wiggers T, Skovgaard ET, Karsdal M, Holst JJ, Christiansen F, de Zawadzki A, Leeming DJ, Patel K. Endotrophin Measured by PRO-C6 as a Prognostic Biomarker for Liver-Related Events in Patients With Advanced Chronic Liver Disease. Liver Int. 2026;46(9):e70824. doi:10.1111/liv.70824. This work demonstrates that a baseline biomarker (PRO-C6) is an independent prognostic marker for liver-related events in cirrhosis, supporting the prognostic value of liver-specific biomarkers. It does not address the temporal discordance between liver-specific tests and albumin.

## Unresolved issues

- The exact diagnosis codes and clinical-document indicators for cirrhosis and decompensation events must be verified from the source data.
- The definition of death and the availability of follow-up encounters must be confirmed.
- The units and standardization of laboratory values must be checked.
