> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Ventilatory Burden Beyond Tidal Volume: Does Mechanics-Adjusted Ventilatory Load Predict Liberation Failure in a Multi-Hospital eICU Cohort?

## Parent
- Expert seed `[starting question]` ([prior hypothesis], assessed valid this episode)
- New scientific direction (evolve from seed; restart in context of the two already-selected branches: hypotension→AKI [prior hypothesis], nighttime discharge [prior hypothesis])

## Unresolved Question

Among mechanically ventilated ICU patients, do ventilatory-burden measures adjusted for respiratory mechanics (driving pressure, mechanical power proxy) carry incremental information about liberation failure beyond tidal volume alone, after adjustment for illness severity?

**Leading claim:** Ventilatory load per unit of lung mechanics (driving pressure = plateau pressure − PEEP; mechanical power proxy from TV, RR, peak/plateau pressure, PEEP) predicts prolonged ventilation / liberation failure beyond what tidal volume alone captures, because the same tidal volume is harmful in a stiff lung and tolerable in a compliant one.

**Strongest rival:** Tidal volume (and its surrogate, minute ventilation) already captures the clinically relevant signal; mechanics-adjusted burden measures are redundant proxies, and apparent incremental value is driven by confounding (sicker patients receive higher pressures) or by center practice variation rather than by patient-level ventilatory mechanics.

**What would distinguish them:** A model adding driving pressure / mechanical-power proxy to a tidal-volume-only baseline should improve discrimination for prolonged ventilation (e.g., vent days ≥ 3) in held-out hospitals. If the burden model adds no meaningful incremental discrimination (ΔC-index < 0.005 and non-significant likelihood-ratio test) in held-out hospitals, the rival is favored.

## Clinical Importance

1. **Liberation failure is a major, costly, modifiable ICU event.** Prolonged mechanical ventilation drives ICU length of stay, ventilator-associated complications, diaphragm weakness, and mortality (vent stays in this cohort: hospital mortality 18.3% vs 4.7% in non-vent stays).
2. **Ventilatory settings are a bedside decision.** If mechanics-adjusted burden (not just tidal volume) identifies high-risk patients, this supports lung-protective weaning strategies and individualized SBT timing.
3. **Practice variation is large.** 188 hospitals with ≥1 vent stay (median 124, max 2030); a consistent multi-hospital finding would support system-level guidance, while hospital-level heterogeneity would point to practice effects.

## Evidence and Novelty

### Closest prior work (inspected)

**[K1] Nakama et al. 2026** (Acute Crit Care 41(3):550-563, DOI 10.4266/acc.000338, PMC13575377)
- Single-center Japanese cohort (n=160 tracheostomized patients) of ventilator liberation after T-tube trials.
- MPCdyn (mechanical power normalized by dynamic compliance) ≤ 454.72 J/min and albumin > 2.3 g/dl independently associated with liberation success; replacing MPCdyn with driving pressure gave similar findings. Competing-risk analysis with in-hospital death as competing event.
- **Limitation:** Single center, tracheostomy/T-tube population, small n; MPCdyn requires dynamic compliance.
- **What this proposal adds:** Multi-hospital eICU intubated cohort (188 hospitals), competing-risks model of time to liberation, direct comparison of tidal-volume-only baseline vs mechanics-adjusted burden with held-out hospital validation.

**[K2] Zhang et al. 2026** (J Intensive Care 14:95, DOI 10.1186/s40560-026-00935-x, PMC13536708)
- Prospective single-arm trial of a standardized weaning protocol in tracheostomized PMV patients (n=250, Beijing rehabilitation hospital). 60-day weaning success 75.6% vs historical benchmark 65%; 30-day reconnection 2.1%; 6-month mortality 14.4% (9.0% weaned vs 31.1% not). LASSO-Poisson weaning score with monotonic gradient (T1 44.0% / T2 84.3% / T3 98.8%).
- **Limitation:** Single-arm, single-center, tracheostomy PMV population; historical benchmark not randomized; confounding and limited events preclude causal inference.
- **What this proposal adds:** Multi-center observational cohort; tests whether ventilatory-burden measures (not just clinical scores) add incremental information beyond tidal volume for liberation failure, with hospital-level validation.

**[K3] Adam et al. 2026** (Crit Care 30:405, DOI 10.1186/s13054-026-06234-z, PMC13449835)
- Secondary analysis of the ERIC trial (10 ICU clusters, Berlin, stepped-wedge cluster RCT): a telemedicine intervention increased SBT frequency (51% vs 27% of patient days, p<0.001) but did not improve weaning outcomes. Weaning is commonly not performed according to guideline recommendations.
- **Limitation:** Telemedicine intervention, not a ventilatory-burden measure; single metropolitan area; no direct comparison of tidal volume vs mechanical power.
- **What this proposal adds:** Directly tests the rival that center practice / patient factors dominate weaning outcomes: if burden measures add no incremental signal beyond tidal volume in held-out hospitals, the K3 rival is supported.

### Novelty
No inspected study has compared tidal-volume-only vs mechanics-adjusted ventilatory-burden models for liberation failure in a multi-hospital cohort with held-out hospital validation. The incremental-discrimination test (burden model vs TV-only baseline) is the specific scientific contribution.

## Study Design

### Population
- eICU-CRD ICU stays with mechanical ventilation: apachePatientResult.actualventdays > 0 (max over multiple records per stay).
- Feasibility-confirmed (probes [research job], [research job], [research job]): 49,911 vent stays across 188 hospitals (median 124, max 2030); hospital mortality 18.3% (vent) vs 4.7% (non-vent); 43,514 vent stays with Alive unit discharge.
- Require: ≥1 respiratoryCharting row with a key ventilatory label (Plateau Pressure, PEEP, Tidal Volume (set), Total RR/Vent Rate) — estimated ~18-20% of vent stays based on 4M-row sample (8,871/49,911 ≈ 17.8% with any key label; TV set 16.6%, PEEP 17.0%, plateau 12.6%, RR 13.3%).
- Estimated eligible: ~8,000-10,000 vent stays (conservative), across ~150+ hospitals.

### Exposure (the key comparison)
- **Tidal volume (baseline):** mean/median "Tidal Volume (set)" (respFlowSettings) and "Exhaled TV (machine)" (respFlowPtVentData) during the first 48h of ventilation (or entire stay if <48h).
- **Ventilatory burden (alternative):**
  - **Driving pressure** = "Plateau Pressure" − "PEEP" (respFlowPtVentData / respFlowSettings), mean over the window.
  - **Mechanical power proxy** = (0.091 × TV_L × RR × (Ppeak + 0.49 × Pmean_airway) + 0.591 × TV_L × (Ppeak − PEEP)² / (2 × Compliance)) simplified to a computable proxy: TV_L × RR × (Ppeak − PEEP) / 1000 (J/min order-of-magnitude), using "Peak Insp. Pressure", "Mean Airway Pressure", "Compliance" where available.
  - **Minute ventilation** = "Exhaled MV" or TV × RR.
- All burden measures computed per stay from respiratoryCharting rows with respchartoffset within the ventilation window (respiratoryCare.ventstartoffset to ventendoffset, or first 48h).

### Outcome
- **Primary:** Prolonged ventilation — actualventdays ≥ 3 (binary; ~30% of vent stays based on vent-day distribution: 1d 31%, 2d 26.5%, ≥3d 42.5%).
- **Secondary:** (a) actualventdays as continuous (log-transformed); (b) hospital mortality (actualhospitalmortality = 'EXPIRED'); (c) ICU mortality (actualicumortality).

### Covariates
- APACHE score (apachePatientResult.apachescore), age, gender (patient), ICU LOS (patient.unitdischargeoffset), airway type (respiratoryCare.airwaytype: Oral ETT vs Tracheostomy vs other), sedative exposure (medication: midazolam, propofol, fentanyl, morphine, dexmedetomidine, ketamine — any use in first 48h), hospital (random effect).

### Analysis
1. **Descriptive:** Compare baseline characteristics (APACHE, age, airway type, sedatives) between short (<3d) and prolonged (≥3d) ventilation, overall and by hospital.
2. **Baseline model:** Multivariable logistic regression (or Cox with hospital random effect) for prolonged ventilation with TV-only + covariates.
3. **Burden model:** Same model + driving pressure + mechanical power proxy + minute ventilation.
4. **Primary estimand:** Incremental discrimination — ΔC-index (burden model vs TV-only model) in **held-out hospitals** (20% of hospitals held out, stratified by vent-stay count). Likelihood-ratio test for nested models.
5. **Sensitivity analyses:**
   - Restrict to stays with ≥3 respiratoryCharting rows in the window (reduce measurement noise).
   - Use 24h and 72h windows instead of 48h.
   - Restrict to Oral ETT (exclude tracheostomy, matching the liberation-failure question).
   - Hospital-level clustering (GEE or mixed model).
   - Competing-risks model (death before liberation) using actualhospitalmortality.

### Falsification Criteria
- **Supportive:** Burden model ΔC-index ≥ 0.005 in held-out hospitals with significant likelihood-ratio test (p < 0.05), and driving pressure or mechanical power proxy is independently associated with prolonged ventilation (OR > 1.2 per 5 cmH2O or per 5 J/min, 95% CI excluding 1).
- **Adverse:** No significant incremental discrimination (ΔC-index < 0.005, LRT p > 0.10), or burden measures are not independently associated after TV adjustment.
- **Inconclusive:** Incremental discrimination is significant but ΔC-index < 0.002 (clinically trivial), or the eligible population is < 3,000 stays, or hospital-level heterogeneity (I² > 75%) precludes a consistent multi-hospital conclusion.

### Method Comparison
- **Baseline:** TV-only logistic regression with covariates (simple, interpretable, the clinical standard).
- **Primary model:** Burden model (TV + driving pressure + mechanical power proxy + minute ventilation) with hospital random effect.
- **Alternative:** Gradient-boosted trees with hospital as a feature, to check if the incremental signal is robust to non-linear effects.
- **Rationale for regression as primary:** The incremental-discrimination question is directly answered by nested model comparison; the sample size is large; the effect is expected to be modest. Trees are a robustness check.

### Data Bindings (exact)
| Variable | Source Table | Column(s) | Join Key |
|----------|-------------|-----------|----------|
| Vent days | apachePatientResult | actualventdays | patientunitstayid |
| Hospital mortality | apachePatientResult | actualhospitalmortality | patientunitstayid |
| ICU mortality | apachePatientResult | actualicumortality | patientunitstayid |
| APACHE score | apachePatientResult | apachescore | patientunitstayid |
| Age, gender | patient | age, gender | patientunitstayid |
| Hospital | patient | hospitalid | patientunitstayid |
| ICU LOS | patient | unitdischargeoffset | patientunitstayid |
| Discharge status | patient | unitdischargestatus | patientunitstayid |
| Vent window | respiratoryCare | ventstartoffset, ventendoffset, airwaytype | patientunitstayid |
| Tidal volume | respiratoryCharting | respchartvaluelabel='Tidal Volume (set)' or 'Exhaled TV (machine)', respchartvalue, respchartoffset | patientunitstayid |
| Plateau pressure | respiratoryCharting | respchartvaluelabel='Plateau Pressure', respchartvalue | patientunitstayid |
| PEEP | respiratoryCharting | respchartvaluelabel='PEEP', respchartvalue | patientunitstayid |
| Peak pressure | respiratoryCharting | respchartvaluelabel='Peak Insp. Pressure', respchartvalue | patientunitstayid |
| Mean airway pressure | respiratoryCharting | respchartvaluelabel='Mean Airway Pressure', respchartvalue | patientunitstayid |
| Compliance | respiratoryCharting | respchartvaluelabel='Compliance', respchartvalue | patientunitstayid |
| Respiratory rate | respiratoryCharting | respchartvaluelabel='Total RR' or 'Vent Rate', respchartvalue | patientunitstayid |
| Minute ventilation | respiratoryCharting | respchartvaluelabel='Exhaled MV', respchartvalue | patientunitstayid |
| Sedatives | medication | drugname, drugstartoffset, drugstopoffset | patientunitstayid |

### Feasibility (from probes)
- 49,911 vent stays, 188 hospitals (median 124 vent stays/hospital, max 2030).
- Hospital mortality: 18.3% (vent) vs 4.7% (non-vent) — strong outcome signal.
- respiratoryCharting label coverage in 4M-row sample of vent stays: TV set 16.6%, PEEP 17.0%, plateau 12.6%, RR 13.3%, peak pressure 8.7%, mean airway pressure 8.2%, compliance 6.6%, Exhaled TV (machine) 0.5%, Exhaled MV 7.5%.
- Estimated eligible with ≥1 key label: ~8,000-10,000 stays (conservative).
- Vent-day distribution: 1d 31%, 2d 26.5%, ≥3d 42.5% — primary outcome (≥3d) has adequate event rate.

### Limitations
1. **Charting sparsity:** Only ~18% of vent stays have any key respiratoryCharting label in the 4M-row sample. Mitigation: require ≥3 rows for primary analysis; use 24h/72h windows; sensitivity analysis.
2. **Mechanical power proxy is approximate:** Full mechanical power requires dynamic compliance and precise pressure-volume data; the proxy (TV × RR × (Ppeak − PEEP)) is an order-of-magnitude estimate. Driving pressure (plateau − PEEP) is more reliable.
3. **Tracheostomy vs intubated:** K1/K2/K3 all study tracheostomy/PMV populations; eICU includes both. Mitigation: restrict to Oral ETT in sensitivity analysis.
4. **Retrospective design:** Cannot establish causality. The incremental-discrimination test is an association, not a causal effect.
5. **No SBT data:** eICU does not have explicit spontaneous breathing trial records; liberation failure is proxied by prolonged ventilation (≥3d).
6. **Center practice:** No staffing or protocol data; hospital random effect absorbs center-level variation but cannot distinguish practice from patient mix.

### What Would Require Additional Data
- Explicit SBT / extubation attempt records (not in eICU)
- Continuous pressure-volume loop data (not in eICU)
- Staffing and protocol adherence data (not in eICU)
- Clinical adjudication of "appropriate" vs "inappropriate" liberation timing

## Compute Budget
- CPU only (no GPU needed)
- Estimated: 30-60 min for full analysis (49,911 vent stays, 20M respiratoryCharting rows)
- Memory: 16 GB (respiratoryCharting is 198 MB compressed)
- Solver envelope: 16 CPUs, 256 GB, 28,800 s (per inputs.json solver_planning_limits)
