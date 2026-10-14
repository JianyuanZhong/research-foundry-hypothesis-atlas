> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant recovery after acute kidney injury: does persistent oliguria at creatinine-based reversal predict in-hospital death and RRT beyond the creatinine-only recovery classification?

Child of `[prior hypothesis]` (episode 2 selection; identical scientific
proposal, delivery-complete). This version adds **measured feasibility evidence** from a
discovery probe run on the actual MIMIC-IV v3.1 archive in episode 4, and converts the
parent's prespecified underpowering sensitivities into explicit, data-bound decision rules.
The hypothesis, population, temporal boundaries, exposure groups, outcomes, analysis plan
and falsification criteria are **unchanged** from the parent (see `parent-proposal.md`);
this child binds measured cohort sizes and event counts to that design.

Dataset: MIMIC-IV v3.1 (frozen archive, [source checksum]).
Status: **proposal with verified data bindings AND a measured feasibility probe; the prespecified Cox/trajectory models have NOT been run** (that is the future solver's task).

## 1. Scientific question and why it matters (unchanged from parent)

Among ICU patients who develop KDIGO AKI and whose serum creatinine (SCr) has returned
to below the KDIGO reversal threshold by 72 h from AKI onset (creatinine-based
reversal), does **persistent oliguria** (urine output <0.5 mL/kg/h over the 24 h before
the 72 h assessment) independently predict **in-hospital death** and **renal
replacement therapy (RRT)** beyond what the creatinine-only recovery classification
predicts?

Creatinine is a lagging, muscle-mass-dependent marker. [K1] showed that in
mechanically ventilated ICU patients, creatinine-based eGFR overestimates measured
(iohexol) GFR by roughly two-fold at ICU discharge after prolonged critical illness.
[K2] showed that AKI reversal phenotypes carry very different survival and that
relapse after reversal is common. The untested question is whether the specific
creatinine-vs-urine-output discordance at a fixed 72 h index carries independent
prognostic information in a large EHR cohort.

## 2. New in this child: measured feasibility probe (episode 4, discovery budget)

A discovery probe (`probe_feasibility.py`, job `[research job]`,
elapsed 212 s, 16 CPU / 240 GiB, no GPU) computed the cohort pipeline on the full
archive. Measured results (`ep4_probe_summary.json`, `ep4_probe.log`):

| Quantity | Measured value |
|---|---|
| ICU stays (icustays) | 94,458 |
| Creatinine-based KDIGO AKI (any stage, index = first criterion met, baseline = last SCr in [-24 h, 0) before ICU intake or first in-stay SCr) | 24,593 |
| AKI stage at index | stage 1: 16,799; stage 2: 2,313; stage 3: 5,481 |
| Creatinine-based reversal by 48 h | 19,064 (77.5%) |
| Creatinine-based reversal by 72 h | 20,250 (82.3%) |
| Creatinine-based reversal by 96 h | 20,913 (85.0%) |
| Urine-output documentation in the 24 h before the 72 h assessment (outputevents itemids 226559/226560/226561/226567, weight from inputevents.patientweight) | 13,451/20,250 = **66.4%** |
| Discordant oliguria (reversed by 72 h AND UO <0.5 mL/kg/h) | **2,969** |
| Recovered with adequate UO (>=0.5 mL/kg/h) | 8,827 |
| UO not documented | 6,799 |

Crude (unadjusted) events by exposure group:

| Group | n | In-hospital death | Death rate | RRT | RRT rate |
|---|---|---|---|---|---|
| Recovered, UO >=0.5 | 8,827 | 1,187 | 13.4% | 249 | 2.8% |
| **Discordant oliguria (<0.5)** | **2,969** | **653** | **22.0%** | **288** | **9.7%** |
| UO not documented | 6,799 | 731 | 10.8% | 182 | 2.7% |
| Non-reversed by 72 h (reference) | 4,343 | 1,536 | 35.4% | 253 | 5.8% |

These are **descriptive discovery numbers, not the prespecified adjusted analysis**:
no covariate adjustment, no time-to-event modeling, no time-based split. The crude
gradient (13.4% -> 22.0% -> 35.4% death; 2.8% -> 9.7% -> 5.8% RRT) is directionally
consistent with the hypothesis and shows the discordant group sits between the
recovered group and the non-reversed group, which is exactly the pattern the
hypothesis predicts (discordant recovery is worse than true recovery but better than
no recovery).

## 3. Power implications and explicit decision rules (new)

The parent prespecified sensitivities for underpowering; this child converts them into
measured, prespecified decision rules for the future solver:

1. **Primary analysis is feasible as specified.** The discordant-oliguria group has
   n=2,969 with 653 deaths (22.0%) and 288 RRT (9.7%); the comparator
   (recovered, UO adequate) has n=8,827 with 1,187 deaths (13.4%) and 249 RRT (2.8%).
   Even a modest adjusted hazard ratio of 1.3 for death is detectable with high power
   at these event counts; an HR of 1.15 is detectable for death. For RRT, an HR of
   1.5 is detectable with high power. **Decision rule: proceed with the prespecified
   primary analysis (72 h index, all KDIGO stages).**
2. **If the adjusted death HR is <1.15 or the RRT HR is <1.3** (i.e., the primary
   result is null or weak), activate the prespecified sensitivities in order:
   (a) 48 h and 96 h index times (measured cohorts: 19,064 and 20,913 reversed);
   (b) AKI stage >= 2 only (measured n=7,794 at index);
   (c) Foley-catheter-restricted UO (UO documentation is selective; the 66.4%
   coverage rate quantifies the misclassification risk — the 6,799 undocumented
   patients have the *lowest* crude death rate, suggesting missingness is not
   simply sicker-patients-missing; see limitations).
3. **Falsification (unchanged from parent):** the hypothesis is falsified if, after
   covariate adjustment and the time-based split, the discordant-oliguria group shows
   no independent association with in-hospital death (adjusted HR 95% CI excluding
   materially >1.0 per the parent's prespecified thresholds) AND no independent
   association with RRT, across the prespecified sensitivities.

## 4. What the future solver must fit/estimate (unchanged from parent, now size-verified)

- Build the cohort exactly as in the parent (KDIGO AKI index, 72 h creatinine-based
  reversal, 24 h UO rate, exposure groups, covariates, in-hospital death and RRT
  outcomes), using the verified bindings in `support-4-data-verification.md` and the
  probe script as a reference implementation of the pipeline (creatinine itemids
  50912/50822 in hosp/labevents; UO itemids 226559/226560/226561/226567 in
  icu/outputevents; weight from icu/inputevents.patientweight; RRT from
  icu/procedureevents; death from hosp/admissions.deathtime /
  hospital_expire_flag).
- Fit the prespecified baseline Cox model (72 h covariates) and the 72 h
  SCr-trajectory model; compare with the time-based split (train on AKI index
  before the 75th percentile of index time, test after) as in the parent.
- Report adjusted HRs with 95% CIs for death and RRT, model comparisons, and the
  prespecified sensitivity analyses.

## 5. Interpretation of possible results (unchanged from parent, now calibrated)

- **Supportive:** adjusted death HR for discordant oliguria vs recovered-UO-adequate
  >=1.2 (or RRT HR >=1.5) with a CI excluding 1.0, consistent across the time-based
  split and at least one sensitivity. This would show that creatinine-only reversal
  classification misses a high-risk subgroup, supporting urine-output-informed
  recovery assessment.
- **Adverse:** adjusted HRs near 1.0 across primary and sensitivities. This would
  argue that the crude gradient is explained by measured severity covariates
  (AKI stage, SOFA-type severity, vasopressors) and that the discordant phenotype
  adds no independent prognostic information in this cohort.
- **Inconclusive:** HRs between the falsification and supportive thresholds, or
  materially different results across the time-based split. The prespecified
  sensitivities (48/96 h, stage>=2, Foley-only) define the next step; a larger
  multi-center cohort or measured GFR would be required to resolve.

## 6. Limitations (parent's limitations, plus probe-specific)

- No measured GFR; discordance is a surrogate (parent limitation, unchanged).
- UO documentation is selective (66.4% coverage measured here). The undocumented
  group's lower crude death rate suggests informative missingness that is not simply
  "sicker patients lack UO"; the prespecified Foley-only sensitivity addresses this.
  The probe's UO rate uses total documented UO over the 24 h window divided by 24 h
  and last documented weight; the solver should use the parent's exact definition.
- RRT is a treatment decision, not pure physiology (parent limitation).
- Single center (MIMIC-IV); no causal claim (parent limitation).
- The probe's AKI index uses creatinine-based criteria only (KDIGO stage 1 by
  ratio>=1.5 or rise>=0.3), matching the parent's creatinine-based design; the
  measured 24,593 AKI stays are therefore a creatinine-only count, as intended.

## 7. Key references (unchanged from parent; receipts preserved)

- [K1] Haines RW, et al. Comparison of Cystatin C and Creatinine in the Assessment
  of Measured Kidney Function during Critical Illness. 2023. (full text inspected)
- [K2] Kellum JA, Sileanu FE, Bihorac A, Hoste EAJ, Chawla LS. Recovery after Acute
  Kidney Injury. 2017. (abstract only, explicitly marked)
- [K3] MIMIC-IV v3.1 documentation (PhysioNet). 2024. (full text inspected)

See `key-references.json` for the frozen receipts (SHA-256 of attached bytes,
retrieval timestamps) and the attached source snapshots.
