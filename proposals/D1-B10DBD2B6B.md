> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional successor hypothesis: does hypotension duration add information beyond nadir for subsequent AKI?

## Proposed relationship

Among adults in a qualifying eICU ICU stay with at least one valid systolic blood-pressure measurement below 65 mmHg during ICU time 0–24 hours, greater cumulative time below 65 mmHg is associated with higher risk of new or worsening acute kidney injury during the subsequent 24–72 hours, after accounting for baseline illness severity, prior vasopressor exposure, and hospital. The duration signal is expected to add reproducible information beyond the admission nadir alone.

This is an association hypothesis, not a causal claim that lowering blood pressure causes AKI or that 65 mmHg is a treatment target.

## Unresolved question and clinical importance

A single nadir can be transient or artifact-prone, whereas sustained hypotension may represent a different exposure burden. The unresolved claim is whether duration and trajectory add clinically meaningful information about subsequent AKI beyond the nadir, rather than merely reflecting severity, treatment response, or measurement intensity. Resolving this could inform whether early AKI risk assessment should use duration/trajectory rather than a single minimum.

The closest inspected work supports the clinical relevance of hypotension and AKI in critical illness and the need for standardized AKI measurement, but does not establish that duration adds information beyond nadir in this eICU population or that the association is causal. Existing evidence is therefore a rationale, not a result.

## Exact data and computable design

Use only the eICU dataset. The source catalog and eICU README identify the read-only source files and table schemas; the proposal must bind to the patient/stay identifier, ICU time fields, blood-pressure measurements, creatinine measurements, urine-output measurements, vasopressor administration, and hospital identifier available in the eICU tables. The exact table names, columns, joins, and archive members must be verified from the catalog/source headers before execution; no cross-dataset join is permitted.

Population: adults with a qualifying ICU stay, at least one valid SBP measurement below 65 mmHg in ICU hours 0–24, and sufficient creatinine/urine-output observations to classify the outcome. Temporal exposure window: ICU hours 0–24. Outcome window: ICU hours 24–72. Define new or worsening AKI using a KDIGO-compatible creatinine and/or urine-output rule, with a prespecified baseline creatinine and time-zero convention. Exclude or sensitivity-test measurements that cannot be temporally ordered, invalid physiologic values, and stays lacking the required outcome observations.

Primary analysis: compare cumulative SBP<65 duration and admission nadir, adjusting for baseline severity, prior vasopressor exposure, and hospital. A simple baseline model uses nadir plus prespecified covariates; a time-aware alternative uses duration, slope/trajectory, and time-varying measurement intensity. Evaluate discrimination, calibration, and uncertainty with a prespecified split or hospital-level validation, bootstrap confidence intervals, and sensitivity analyses for measurement frequency, vasopressor timing, missingness, and alternative AKI definitions.

Falsification and interpretation: the hypothesis is supported if duration adds reproducible information beyond nadir with a clinically meaningful, uncertainty-qualified improvement and a directionally consistent association under artifact controls. It is adverse if duration adds no information, is attenuated after measurement-intensity adjustment, or is unstable across hospitals/AKI definitions. It is inconclusive if the cohort is too small, outcome ascertainment is too sparse, uncertainty is wide, or the estimand is dominated by missingness. A positive association would not establish causality, a treatment threshold, or clinical utility; those require additional clinical adjudication, treatment-policy data, and prospective or causal validation.

## Alternatives and method choice

The simple baseline is a prespecified logistic or survival model using nadir and baseline covariates. The substantive alternative is a time-aware model using duration, trajectory, and measurement intensity; it can reveal whether the information is in exposure burden or observation practice, which the baseline loses. If the time-aware model is not feasible, retain the baseline and report the dependency rather than changing the scientific question. No full study result is claimed here.

## Evidence status and missing evidence

The exact source bindings, full schema/header verification, and the three inspected key works must be completed before final selection. No computed effect, causal conclusion, or clinical recommendation is asserted in this provisional draft.
