> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Perfusion-Modified Effect of Diuretic Timing on In-Hospital Mortality: A Falsifiable MIMIC-IV Experiment

**Parent:** [prior hypothesis] (expert seed 2: "At the same fluid accumulation level, the effects of diuretic treatment differ between patients with stable perfusion and those with ongoing hypoperfusion.")
**Dataset:** MIMIC-IV 3.1 (frozen archive, [source checksum])
**Status:** Data-bound proposal with verified itemids, executed bounded feasibility probe, and three inspected key references. No full analysis was run.

---

## 1. Scientific Question

**Unresolved claim (what this experiment tests):**
> In adult ICU patients who receive loop diuretics during their ICU stay, the association between diuretic timing (early ≤48h vs. late >48h from ICU admission) and in-hospital mortality differs by perfusion status at the time of first diuretic — specifically, patients who require vasopressors *after* their first diuretic (indicating hemodynamic deterioration post-diuresis) have a stronger adverse association with early diuretic timing than patients who were already on vasopressors *before* their first diuretic (indicating pre-existing shock) or who never required vasopressors.

**Why this matters:**
The timing of diuretic initiation is one of the most consequential and least standardized ICU decisions. The expert-provided reference [K1] (Wang et al. 2025) found that early diuretic use (≤48h) in sepsis was associated with *higher* 28-day mortality (HR 2.59) after propensity score matching, but did not stratify by perfusion status. The seed hypothesis posits that this association is *modified* by perfusion: early diuretics may be harmful when they precipitate hemodynamic collapse (vasopressor need after diuretic) but may be neutral or beneficial when given to patients already stabilized on vasopressors. No prior study has tested this interaction.

**What answering this question would change:**
If supported (interaction present): diuretic timing decisions should be conditioned on perfusion status, and a simple, computable perfusion indicator (vasopressor use before/after diuretic) could identify patients for whom early diuresis is particularly risky. This would inform a targeted trial design. If adverse (no interaction): the Wang et al. finding of harm from early diuretics is uniform across perfusion states, and the timing decision may be driven by other factors (e.g., fluid overload severity, renal function).

---

## 2. Supported Claims (from prior literature, not re-tested here)

- [K1] Wang et al. (2025): In sepsis patients from MIMIC-IV, early loop diuretic initiation (≤48h) was associated with higher 28-day mortality (HR 2.59, 95% CI 2.325–2.884) after PSM, but the analysis did not stratify by perfusion status or vasopressor timing.
- [K2] Wang et al. (2026): In acute pancreatitis ICU patients from MIMIC-IV, positive fluid balance trajectories (Rise-Fall) were independently associated with higher in-hospital mortality, and cumulative fluid balance >25 mL/kg was associated with worse outcomes. This establishes that fluid accumulation is prognostic, but does not address diuretic timing or perfusion interaction.
- [K3] Wong et al. (2026): Systematic review of 13 de-resuscitation RCTs (2,495 patients) found that no trial achieved mortality reduction from de-resuscitation interventions, despite 53.8% achieving fluid balance separation. This suggests that the *timing* and *physiologic context* of fluid removal matter, not just the net volume removed.

---

## 3. Study Population

### Inclusion criteria
- Adult patients (`anchor_age` ≥ 18; `hosp/patients`)
- ICU length of stay ≥ 1.0 day (`icu/icustays.los`)
- At least one loop diuretic administration during the ICU stay (furosemide or bumetanide in `icu/inputevents`)
- Discharged alive from the ICU (`outtime` IS NOT NULL)
- **First ICU stay of the hospitalization only** (min `stay_id` per `subject_id`+`hadm_id`)

### Exclusion criteria
- ICU stay < 1.0 day
- No diuretic administration
- Non-first ICU stay of the hospitalization

### Temporal boundaries
- **Exposure:** first diuretic administration time (`MIN(starttime)` of diuretic rows in `inputevents`)
- **Perfusion status at diuretic time:** vasopressor use before vs. after first diuretic (`MIN(starttime)` of vasopressor rows)
- **Primary outcome:** in-hospital death (`deathtime` IS NOT NULL OR `hospital_expire_flag` = 1)
- **Secondary outcome:** ICU length of stay (days)

---

## 4. Data Bindings (all verified against the frozen archive)

| Variable | Table | Column(s) | ItemID(s) | Unit | Join Key | Time Field |
|----------|-------|-----------|-----------|------|----------|------------|
| Age | hosp/patients | anchor_age | — | years | subject_id | — |
| Sex | hosp/patients | gender | — | M/F | subject_id | — |
| ICU LOS | icu/icustays | los | — | days | stay_id | — |
| ICU admission | icu/icustays | intime | — | timestamp | stay_id | intime |
| ICU discharge | icu/icustays | outtime | — | timestamp | stay_id | outtime |
| In-hospital death | hosp/admissions | deathtime, hospital_expire_flag | — | timestamp / 0-1 | subject_id + hadm_id | deathtime |
| Furosemide | icu/inputevents | starttime, stoptime, rate | 221794 | mg/hr | stay_id | starttime |
| Furosemide 250/50 | icu/inputevents | starttime, stoptime, rate | 228340 | mg/hr | stay_id | starttime |
| Bumetanide | icu/inputevents | starttime, stoptime, rate | 229639 | mg/hr | stay_id | starttime |
| Norepinephrine | icu/inputevents | starttime, stoptime, rate | 221906 | µg/kg/min | stay_id | starttime |
| Phenylephrine | icu/inputevents | starttime, stoptime, rate | 221749, 229630, 229632 | µg/min | stay_id | starttime |
| Vasopressin | icu/inputevents | starttime, stoptime, rate | 222315 | units/min | stay_id | starttime |
| Epinephrine | icu/inputevents | starttime, stoptime, rate | 221289, 229617 | µg/kg/min | stay_id | starttime |
| Dopamine | icu/inputevents | starttime, stoptime, rate | 221662 | µg/kg/min | stay_id | starttime |
| Angiotensin II | icu/inputevents | starttime, stoptime, rate | 229764, 229709 | ng/kg/min | stay_id | starttime |

**Source archive:** `mimic-iv-3.1.zip` ([source checksum]), archive members:
- `mimic-iv-3.1/hosp/patients.csv.gz`
- `mimic-iv-3.1/icu/icustays.csv.gz`
- `mimic-iv-3.1/hosp/admissions.csv.gz`
- `mimic-iv-3.1/icu/inputevents.csv.gz`
- `mimic-iv-3.1/icu/d_items.csv.gz`

**Join keys:** patients → icustays: `subject_id`; icustays → admissions: `subject_id` + `hadm_id`; icustays → inputevents: `stay_id`; inputevents → d_items: `itemid`.

**ItemIDs verified** via DuckDB query on `d_items.csv.gz` (4,095 rows) in the executed feasibility probe.

---

## 5. Prespecified Perfusion-Status Phenotype

At the time of **first diuretic administration**:

### Perfusion status categories
1. **vp_before:** vasopressor already running (first vasopressor `starttime` < first diuretic `starttime`)
2. **vp_after:** vasopressor started after first diuretic (first vasopressor `starttime` ≥ first diuretic `starttime`)
3. **no_vp:** no vasopressor at any point during the ICU stay

### Diuretic timing categories
- **Early:** first diuretic within 48h of ICU admission (`EXTRACT(EPOCH FROM (first_diuretic_time - intime))/3600.0 ≤ 48`)
- **Late:** first diuretic after 48h

### Composite
**Primary comparison:** Early × vp_after vs. Early × vp_before vs. Early × no_vp (and same for Late)

### Sensitivity analyses
- Timing thresholds: 24h, 48h, 96h
- Vasopressor agent specificity: norepinephrine-only vs. any vasopressor
- Vasopressor dose: mean rate during the 24h before/after diuretic

---

## 6. Outcomes

- **Primary:** In-hospital death (binary)
- **Secondary:** ICU length of stay (continuous, days)
- **Tertiary:** 28-day mortality (if `dischtime` available)

---

## 7. Analysis Plan

### Baseline model
Multivariable logistic regression for in-hospital death:
- Age (per 10 years), Sex (male), ICU LOS (per day)

### Extended model
Baseline + **diuretic timing** (early/late) + **perfusion status** (vp_before/vp_after/no_vp) + **timing × perfusion interaction**

### Model comparison
- Adjusted OR (95% CI) for early diuretic in each perfusion stratum
- Interaction p-value (timing × perfusion)
- Harrell C-index baseline vs extended
- Likelihood ratio test

### Method comparison: baseline vs substantive alternative
- **Baseline:** logistic regression with binary timing and perfusion indicators + interaction
- **Alternative:** gradient-boosted trees (XGBoost) with continuous features (time-to-diuretic in hours, vasopressor duration before diuretic in hours, vasopressor rate at diuretic time, ICU LOS, age)
  - **What the alternative reveals:** whether the timing-perfusion interaction is nonlinear or threshold-dependent, which features contribute most to discrimination, and whether the binary phenotype loses information. If the tree substantially outperforms the logistic model, the binary categories may need refinement; if similar, the simple interaction model is clinically sufficient.

### Falsification criteria
- **Supportive:** significant timing × perfusion interaction (p < 0.05), AND the direction of the early-diuretic effect differs across perfusion strata (e.g., harmful in vp_after, neutral in vp_before), AND ΔC-index ≥ 0.01
- **Adverse:** no significant interaction (p ≥ 0.10), AND the early-diuretic effect is uniform across perfusion strata (all ORs in the same direction with overlapping CIs)
- **Inconclusive:** < 100 patients in any timing × perfusion cell, OR < 50 outcome events in the primary comparison, OR > 50% missing data in the exposure window

### Interpretation
- **Supportive:** diuretic timing effects are perfusion-modified; early diuresis is particularly risky when it precipitates hemodynamic collapse. Would justify a targeted trial of delayed diuresis in patients at risk of post-diuretic vasopressor need.
- **Adverse:** diuretic timing effects are uniform across perfusion states; the Wang et al. finding of harm from early diuretics is not perfusion-specific. The timing decision may be driven by other factors.
- **Inconclusive:** insufficient events or data; would require a larger dataset or different timing thresholds.

---

## 8. Bounded Feasibility Probe (EXECUTED)

**Cohort:** 25,422 adult ICU stays with ≥1 diuretic (LOS ≥ 1d, first stay only)

**Timing × Perfusion cross-tabulation:**

| Timing | Perfusion | n | Mortality |
|--------|-----------|---|-----------|
| 0-24h | no_vp | 6,469 | 9.4% |
| 0-24h | vp_after | 1,533 | 39.1% |
| 0-24h | vp_before | 6,023 | 8.7% |
| 24-48h | no_vp | 1,781 | 10.2% |
| 24-48h | vp_after | 263 | 33.1% |
| 24-48h | vp_before | 3,494 | 11.4% |
| 48-96h | no_vp | 1,256 | 12.0% |
| 48-96h | vp_after | 195 | 37.9% |
| 48-96h | vp_before | 2,331 | 20.8% |
| >96h | no_vp | 568 | 15.7% |
| >96h | vp_after | 116 | 37.9% |
| >96h | vp_before | 1,393 | 26.0% |

**Key observations:**
- vp_after (vasopressor started after diuretic) has the highest mortality (33-39%) across all timing strata
- vp_before mortality increases with later diuretic timing (8.7% → 26.0%)
- The interaction pattern is visible in the raw data: the timing effect differs by perfusion status
- All cells have n ≥ 116, satisfying the minimum cell size for the primary analysis

**Data resolvability:** Confirmed. All required variables are present in the frozen archive with verified itemids.

---

## 9. Limitations and Alternatives

- **Confounding by indication:** patients who receive early diuretics may be sicker (or sicker in a different way) than those who receive late diuretics. The landmark design (perfusion status at diuretic time) partially addresses this, but residual confounding is possible.
- **Vasopressor as perfusion proxy:** vasopressor use is an imperfect proxy for perfusion status; some patients may be hypoperfused without vasopressors (e.g., low-output states) and some may be on vasopressors for reasons other than hypoperfusion (e.g., post-cardiac surgery).
- **No fluid balance data:** the seed mentions "fluid accumulation" but the primary analysis uses diuretic timing and perfusion status as the key variables. Fluid balance (input - output) could be added as a covariate but requires `outputevents` data and is a secondary analysis.
- **Single-center:** MIMIC-IV is from BIDMC; external validation would require eICU or another dataset.
- **Alternatives not chosen:** target-trial emulation with time-varying treatment (deferred; requires g-computation or marginal structural models, which are computationally intensive and may not converge with the available data). Propensity score matching on perfusion status (deferred; the interaction test is more direct for the hypothesis).

---

## 10. Key References

- **[K1]** Wang Y, Wu J, Shao T, Ding X, Tian Y, Li N. Prognostic impact of early versus delayed loop diuretic administration in sepsis: a propensity score-matched analysis using the MIMIC-IV database. *Transl Androl Urol*. 2025;14(3):779-790. doi:10.21037/tau-24-620. (full_text, PMC11986544)
- **[K2]** Wang F, Xu Y, Li X. Association of fluid balance trajectories and cumulative fluid balance with in-hospital mortality in patients with acute pancreatitis. *Front Med*. 2026;13:1863757. doi:10.3389/fmed.2026.1863757. (full_text, HTML)
- **[K3]** Wong A, Melo P, Stefanini F, Cheah K, Kattan E, Zawadka M. The ultrasound gap in de-resuscitation trials: A systematic review of physiological assessment deficits. *Ultrasound J*. 2026;18:18750. doi:10.5826/tuj.2026.18750. (full_text, HTML)

Full claim mappings, locators and SHA-256 receipts are in the attached `key-references.json`.
