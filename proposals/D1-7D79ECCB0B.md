> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Provisional HCC hypothesis (episode 2)

## Proposed relationship
Among HCC encounters with a documented liver-cell-carcinoma diagnosis, a time-stamped deterioration pattern in liver function, coagulation, renal function, or tumor-marker measurements during the first 7 days of admission is associated with a subsequent clinically consequential deterioration event, beyond a baseline laboratory snapshot and demographics. The direction and magnitude are not assumed.

## What is supported now
The HCC README and table metadata identify a multi-table hospital record collection. Detail tables are intended to join to encounters using the documented patient/admission identifiers. The encounters source is HCC/data_基本信息_2500296761891079109.csv (table encounters), with admission/discharge and demographic fields; diagnoses is HCC/data_诊断_7504718184492840569.csv (table diagnoses), with diagnosis name/type; labs is HCC/data_检验_609065997844652188.csv (table labs). These bindings support a longitudinal study design but do not establish an effect.

## Unresolved evidence
The exact index-cohort rule, outcome definition and event support, laboratory units and modality mapping, treatment/documentation adjustment variables, and clinical validity of any deterioration proxy require direct schema and row inspection. No model has been fitted and no result is claimed.

## Falsifiable test
Compare a time-aware 7-day trajectory representation with a baseline snapshot model on a patient-level, time-respecting split. The trajectory representation should improve prespecified discrimination/calibration for the outcome, with uncertainty intervals and negative-control timing checks. Support requires a reproducible improvement beyond the snapshot; no improvement or degradation is adverse to the hypothesis; sparse events, unstable units, or imprecise intervals are inconclusive.

## Missing evidence and next work
Inspect exact HCC table schemas and representative rows, verify temporal fields and joins, quantify event support and lab modality/unit coverage, then bind the final cohort and outcome before any fitting. Literature and clinical adjudication limits remain to be resolved.
