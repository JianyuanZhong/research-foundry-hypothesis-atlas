> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Hyperoxia Exposure and Pulmonary Status: A Falsifiable eICU Study

## Unresolved Question and Clinical Importance

The unresolved question is whether sustained hyperoxemia (arterial PaO2 above a prespecified threshold) in patients with already adequate oxygenation is associated with different subsequent outcomes according to pulmonary disease status. This matters because oxygen therapy is common in ICUs and oxygen targets are not uniformly established. A result could inform whether oxygenation targets should be stratified by pulmonary status or whether a uniform conservative target is reasonable.

The closest relevant prior work inspected includes:
- [K1] Nadeau et al. (2026) "Bench evidence, bedside uncertainty: hyperoxia, mechanical ventilation and lung injury." This review synthesizes evidence on how hyperoxia primes the adult lung for increased susceptibility to lung injury during mechanical ventilation. It notes that while the injurious role of hyperoxia in animal models is highly consistent, clinical trials have been less consistent in directly linking hyperoxia exposure to increased patient mortality. The review underscores the importance of judicious oxygen titration to mitigate iatrogenic lung injury.
- [K2] Ruaysungnoen et al. (2026) "Hyperoxia reflects poor native cardiac function and demonstrates cardiac index-dependent associations with mortality in VA-ECMO patients." This study found that the association between early hyperoxia and mortality in VA-ECMO is primarily driven by underlying cardiac failure rather than direct oxygen toxicity. After adjusting for native cardiac index, the association between hyperoxia and mortality became insignificant. This highlights the importance of accounting for underlying pathology when evaluating hyperoxia.
- [K3] AlSejari et al. (2026) "Perioperative hyperoxia versus normoxia during cardiopulmonary bypass in adult cardiac surgery: a systematic review and meta-analysis of randomized controlled trials." This meta-analysis of 12 RCTs involving 2,732 patients found no significant difference between hyperoxia and normoxia in short-term mortality, long-term mortality, or AKI. The evidence remains uncertain, warranting further research.

The strongest claim currently supported is that the question is clinically relevant and that SpO2 is insufficient to quantify hyperoxemia. The unresolved claim is that the association between sustained hyperoxemia and subsequent outcomes differs by pulmonary status.

## Proposed eICU Experiment

### Population
- Adult ICU patients in the eICU dataset with at least one arterial blood-gas measurement and at least one FiO2 record during the ICU stay.
- Exclude patients with no usable blood-gas or FiO2 records, and exclude the first 24 hours after ICU admission to reduce admission-related confounding.

### Exposure
- Define a hyperoxemia episode as a period during which PaO2 is above a prespecified threshold (e.g., 300 mmHg) for at least 6 consecutive hours, while FiO2 is at least 0.4.
- Define adequate oxygenation as PaO2 at least 80 mmHg or SpO2 at least 92% at the start of the episode.
- Use arterial PaO2, not SpO2, to quantify hyperoxemia, consistent with the seed limitation.

### Pulmonary Status
- Stratify by pulmonary disease using admission and in-hospital diagnosis codes (e.g., pneumonia, ARDS, COPD, asthma) and respiratory support (mechanical ventilation, non-invasive ventilation, supplemental oxygen).
- Compare patients with pulmonary disease versus those without, and within pulmonary disease, compare different diagnoses where feasible.

### Outcome
- Primary outcome: 7-day ICU mortality.
- Secondary outcomes: 28-day mortality, new organ failure, and liberation from mechanical ventilation.

### Analysis
- Primary analysis: a prespecified interaction test between hyperoxemia exposure and pulmonary status for 7-day ICU mortality, using a multivariable model adjusted for age, sex, APACHE II score, and hospital.
- Baseline: a simple adjusted logistic regression with hyperoxemia exposure and pulmonary status as main effects.
- Learned/mechanistic alternative: a flexible model (e.g., gradient-boosted trees or a mechanistic time-to-event model) that can capture nonlinear and time-varying relationships between hyperoxemia exposure, pulmonary status, and outcomes. This alternative could reveal whether the association is driven by specific exposure durations or by interactions with respiratory support that the baseline logistic model would miss.
- Validation: whole-hospital holdout validation to assess transportability.

### Falsification
- If the interaction between hyperoxemia exposure and pulmonary status is null after adjustment for severity and hospital, the hypothesis is not supported.
- If the association is driven by admission severity or hospital practice rather than by pulmonary status, the hypothesis is not supported.
- If the association is present but not consistent across hospitals, the result is inconclusive for a generalizable clinical effect.

## Method Comparison

- Baseline: adjusted logistic regression with prespecified hyperoxemia exposure and pulmonary status. This is simple, interpretable, and directly tests the prespecified interaction.
- Learned alternative: gradient-boosted trees or a mechanistic time-to-event model. This could reveal nonlinear exposure-duration effects and interactions with respiratory support that the baseline would miss. It is more complex and less interpretable, but it could provide a more nuanced understanding of the exposure-outcome relationship.
- Selection: the baseline is the primary analysis because it directly tests the prespecified hypothesis. The learned alternative is a secondary analysis to explore whether the association is driven by specific exposure patterns. If the learned alternative reveals a strong nonlinear effect that the baseline misses, this would justify a follow-up study with a more detailed exposure characterization.

## Data Bindings

- eICU blood-gas data: `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/lab.csv.gz` (PaO2, FiO2).
- eICU diagnosis data: `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/admissionDx.csv.gz` and `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/diagnosis.csv.gz`.
- eICU patient data: `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/patient.csv.gz` (age, sex, APACHE II score).
- eICU hospital data: `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/hospital.csv.gz`.

## Key References

- [K1] Nadeau EE, Schwingshackl A, Sturgill JL, Waters CM. "Bench evidence, bedside uncertainty: hyperoxia, mechanical ventilation and lung injury." Eur Respir Rev. 2026;35(181):260058. DOI: 10.1183/16000617.0058-2026. PMID: 42386311.
- [K2] Ruaysungnoen RK, et al. "Hyperoxia reflects poor native cardiac function and demonstrates cardiac index-dependent associations with mortality in VA-ECMO patients." Eur Heart J Acute Cardiovasc Care. 2026. DOI: 10.1093/ehjacc/zuag082. PMID: 42400098.
- [K3] AlSejari NY, et al. "Perioperative hyperoxia versus normoxia during cardiopulmonary bypass in adult cardiac surgery: a systematic review and meta-analysis of randomized controlled trials." J Cardiothorac Surg. 2026;21(1):572. DOI: 10.1186/s13019-026-04344-x. PMID: 42271504.
