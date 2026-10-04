> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB 15: Breast cancer genetic risk and the postmenopausal hormonal background

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## Hypotheses to Be Tested

Among postmenopausal women, the association between breast cancer PRS and disease risk is stronger in those with low SHBG and high adiposity.

## Study population and key data

Postmenopausal women without breast cancer; standard BC PRS, SHBG, sex hormones, body fat, HRT history, and cancer registry.

## Basic Approach

Prespecify a small number of interactions between PRS and SHBG and fat, follow up from the blood draw date, and stratify by natural menopause and HRT use.

## Significance of the Research

Test whether genetic susceptibility is expressed differently in different endocrine contexts.

## Main Challenges

Hormones were measured only once, and low values may be affected by the detection limit; HRT effects or receptor subtypes cannot be inferred.

## References

Relevant background or data description, not evidence that the hypothesis is valid or novel: https://www.nature.com/articles/s41467-025-60058-z; field definitions: https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26200; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26220; https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22009

## Life Sciences

Genetic Risk and Protective Phenotypes

## Competing Explanations

BMI, HRT selection, and screening frequency may jointly explain the association.

## Minimal validation and falsification criteria

First audit menopausal status, detection limits, and HRT; if the continuous interaction is unstable in an independent subset, this does not support an amplification effect.

## Basis for Dictionary Fields

26200 In UK Biobank PRS Release Testing subgroup；26220 Standard PRS for breast cancer (BC)；22009 Genetic principal components；2724 Had menopause；3581 Age at menopause (last menstrual period)；30830 SHBG；30800 Oestradiol；23099 Body fat percentage；3536 Age started hormone-replacement therapy (HRT)；3546 Age last used hormone-replacement therapy (HRT)；40005 Date of cancer diagnosis；40006 Type of cancer: ICD10

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.15.
