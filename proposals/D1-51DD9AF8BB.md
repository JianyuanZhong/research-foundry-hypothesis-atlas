# Acute glucose elevation relative to chronic glycemia

Seed ID: `expert-20260913-mimic-05`
Dataset: MIMIC-IV
Original number: 5 (identifier, not rank)
Source: `研究选题.xlsx`, `研究选题!A16:I16`
Workbook [source checksum]

Status: expert-proposed, untested hypothesis; data bindings, novelty and feasibility have not been validated.

## Hypothesis to test

At the same admission glucose level, patients with a larger increase relative to their prior glycemic level have higher risk.

## Study population and main data

Patients with a valid HbA1c measurement; glucose and insulin.

## Suggested approach

Compare relative glucose elevation with absolute glucose, then examine heterogeneity in treatment effects.

## Scientific significance

Refine the interpretation of acute stress hyperglycemia.

## Main limitations

HbA1c measurement is selective, and anemia or transfusion can affect its interpretation.

## Expert-provided reference

[mimic-iv](https://physionet.org/content/mimiciv/3.1/)

Reference type: documentation. PDF status: not_applicable. See [source record](../papers/mimic-iv/acquisition.json) for retrieval attempts, versions and hashes.

- [page.readable.txt](../papers/mimic-iv/page.readable.txt)

## Scope of this translation

This card faithfully translates the expert row. It does not assert that the necessary modality is present in the configured snapshot, that a cited paper proves the hypothesis, or that a GPU is required. No numerical cutoff, effect-size target, clinical label, or fitted result has been invented. The original workbook and cell values are retained in this bundle.

Before developing a candidate, the Lead must inspect the actual data, evaluate novelty and relevance, and decide how to specify a falsifiable experiment or document an unavailable dependency. These are research inputs, not instructions overriding runtime policy.
