> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 30: Nighttime noise and sleep vulnerability jointly point to atrial fibrillation

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## Hypotheses to Be Tested

The association between nighttime noise and subsequent atrial fibrillation is stronger among people with insomnia or irregular sleep and cannot be fully explained by air pollution.

## Study population and key data

Individuals with residential noise data, sleep questionnaires or accelerometry, and atrial fibrillation follow-up.

## Basic Approach

Use the point when joint exposure can be determined as the starting point, prespecify noise–sleep interaction, jointly adjust for air pollution, and conduct a residential-move sensitivity analysis.

## Significance of the Research

Clues that distinguish nighttime environmental interference from general traffic exposure.

## Main Challenges

Exposure years must be consistent; a single sleep measurement cannot represent a long-term mechanism.

## References

Relevant background or data description, not proof that the hypothesis is valid or novel: https://www.nature.com/articles/s41591-024-03483-9; field definitions: https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=24022; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=24006; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=1200

## Life Sciences

Environment, behavior, and biological susceptibility

## Competing Explanations

Traffic pollution, socioeconomic status, or healthcare utilization may explain the association.

## Minimal validation and falsification criteria

First assess collinearity between noise and pollution and whether there is support for independent variation; if they cannot be disentangled, report only the joint exposure.

## Basis for Dictionary Fields

24022 Average night-time sound level of noise pollution；24006 Particulate matter air pollution (pm2.5); 2010；1200 Sleeplessness / insomnia；1160 Sleep duration；90001 Acceleration data - cwa format；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre。Sleep regularity and activity segments need to be derived from the raw acceleration data.

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.

Questionnaire insomnia is available; accelerometer sleep irregularity is blocked without its bulk payload. Any narrower formulation must be labeled.

Exact field map: see source-schema-audit.json, seeds.30.
