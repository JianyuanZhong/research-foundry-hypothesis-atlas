> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 35: Bone mass and fat gain are asynchronous after menopause

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## Hypotheses to Be Tested

Among postmenopausal women with similar body weight, those with increased visceral fat and decreased bone mass have a higher subsequent risk of both fracture and diabetes than those with only one of these changes.

## Study population and key data

Postmenopausal women with repeat DXA or body MRI and biochemical measurements.

## Basic Approach

Starting at the second joint assessment, compare changes in bone density and fat over time, analyzing two outcomes: fracture and diabetes.

## Significance of the Research

Study bone and energy-storage allocation after reproductive aging.

## Main Challenges

The overlap between repeated images may be small; age differences between different subjects cannot substitute for individual change.

## References

Relevant background or data description, not proof of hypothesis validity or novelty: https://www.nature.com/articles/s41467-026-74715-4; field definitions: https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=2724; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3581; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=23204

## Life Sciences

Sex, hormones, and metabolic redistribution

## Competing Explanations

HRT, changes in activity, or weight loss may affect bone and fat first.

## Minimal validation and falsification criteria

First audit the overlap of repeated DXA and MRI measurements in the same individuals; if insufficient, retain only cross-sectional descriptions of bone mass and concurrent fat.

## Basis for Dictionary Fields

2724 Had menopause；3581 Age at menopause (last menstrual period)；23204 L1-L4 BMD (bone mineral density)；23208 Femur neck BMD (bone mineral density) (right)；21085 Visceral fat volume；21002 Weight；30750 Glycated haemoglobin (HbA1c)；3536 Age started hormone-replacement therapy (HRT)；3546 Age last used hormone-replacement therapy (HRT)；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.

Blood instances 0/1 and imaging instances 2/3 are not contemporaneous. Do not infer a time-matched phenotype from column presence.

Exact field map: see source-schema-audit.json, seeds.35.
