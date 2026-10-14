> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: discordant renal recovery after acute kidney injury

## Proposed relationship
Among adults with an acute kidney injury (AKI) episode in MIMIC-IV, patients whose creatinine has returned toward baseline but whose urine output and/or fluid balance remain abnormal at a prespecified 48-hour assessment will have a higher risk of subsequent in-hospital death or persistent/recurrent kidney dysfunction than patients with concordant creatinine and urine-output recovery, after accounting for baseline illness severity and treatment context.

This is a hypothesis, not an observed result. The clinical opening is that creatinine-based recovery may be a misleading surrogate: creatinine can fall because of dilution, altered production, or recovery while residual tubular dysfunction or fluid overload persists. Resolving this would clarify whether a single creatinine criterion is sufficient for judging renal recovery and for deciding whether continued monitoring or renal-risk assessment is warranted.

## Concrete supporting observations and source locations
- The expert seed `[starting question]` (candidate `[prior hypothesis]`) explicitly proposes that creatinine falling without improvement in urine output or fluid status leaves patients at high risk, and identifies the limitation that measured kidney function is unavailable.
- The seed points to the comparison of cystatin C and creatinine during critical illness (PMID 37256861) as a measurement reference; this supports the premise that creatinine alone may not represent kidney function, but it does not establish the proposed outcome association.
- The MIMIC-IV dataset is the assigned source and is expected to contain longitudinal laboratory, urine-output, fluid-balance, vital-sign, medication, and outcome data; exact table/column bindings still require catalog inspection before the final experiment card.

## Uncertainties and missing evidence
- AKI onset, baseline creatinine, recovery timing, and “persistent urine-output/fluid abnormality” must be operationalized without future information.
- Creatinine and urine output are imperfect and selectively measured; fluid balance is affected by treatment and documentation.
- The available data may not contain measured GFR, cystatin C, dialysis details sufficient for adjudication, or reliable reasons for discharge/ICU transfer.
- Severity, nephrotoxic drugs, vasopressors, diuretics, dialysis, and fluid management can confound or mediate the association; a retrospective design cannot by itself identify a causal mechanism.
- The literature claim and exact MIMIC tables/columns have not yet been fully inspected in this provisional checkpoint.

## Falsifiable test
Use a fixed landmark at 48 hours after an operational AKI onset (or the first qualifying AKI assessment), with outcomes assessed only after that landmark: in-hospital death and a prespecified persistent/recurrent kidney endpoint. Compare discordant recovery with concordant recovery using a prespecified multivariable baseline/landmark model and a competing-risk or time-to-event analysis. Report effect estimates and uncertainty, calibration, and sensitivity analyses for missingness, treatment, and alternative AKI definitions.

Support would be a reproducible adjusted association with clinically meaningful uncertainty and robustness to measurement/timing sensitivity analyses. Adverse evidence would be no association, reversal, or instability under prespecified sensitivity analyses, arguing against using this discordance as a risk marker. Inconclusive evidence would be insufficient event support, excessive missingness, or wide intervals that cannot distinguish a clinically important effect.

## Required next evidence
Inspect the complete MIMIC catalog and relevant table schemas; acquire and read the cited measurement work plus two additional closest works; define exact joins, time fields, cohort filters, and outcome windows; and compare a simple landmark baseline with a substantive longitudinal learned or mechanistic alternative before selecting the final method.
