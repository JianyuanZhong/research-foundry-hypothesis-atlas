# Value-aware temporal ventilation-state audit across airway lookbacks

## Substantive repair and clinical advance

This is a substantive child of `[prior hypothesis]`. The parent established an important measurement warning: a broad respiratory-chart marker appeared in approximately 99.4–99.7% of unbounded-only, 24-hour-retained, and 6-hour-retained rows, while treatment and note markers were sparse. That result could not distinguish active ventilation from repeated device-oriented documentation. This child replaces the near-universal label-presence endpoint with an explicit, value-aware temporal state machine. It retains the parent’s target-independent denominator, strict physiology and exclusions, variant-specific first-stay freezing, landmarks, and post-freeze care-plan receipt classification; no target is used to define ventilation evidence.

The clinical question is whether an old airway status carried forward to a landmark is supported by contemporaneous, value-bearing evidence of an invasive ventilation state. This matters because a falsely qualified ventilation denominator can distort estimates of daily evaluation, SBT documentation, and downstream care-plan receipt. The proposed advance is not a claim that structured proxies recover bedside truth. It is an auditable way to identify positive, negative, ambiguous, and conflicting evidence and to expose where the denominator is not clinically adjudicable.

## Evidence-supported versus untested claims

The available parent computation supports only that the broad structured-chart label is nearly ubiquitous and that future composite coverage is lower than contemporaneous coverage. It does not support active invasive ventilation, SBT delivery, quality, causality, or benefit. The unresolved, falsifiable claim is that unbounded-only rows have a lower fraction of high-specificity positive ventilation states, and a higher fraction of ambiguous/negative states, than rows retained by a 24-hour or 6-hour airway lookback. The converse result would weaken the stale-airway interpretation but still would not validate true continuous ventilation.

## Frozen population, time, and estimands

The exact inherited membership artifact is `[internal dataset path]`. It contains the parent’s `exact_unbounded`, `exact_airway_24h`, and `exact_airway_6h` memberships and their overlap groups. The parent denominator remains unchanged: adult eICU stays from `patient.csv.gz`, first-stay freezing, unit-discharge and landmark eligibility, strict pre-landmark physiologic windows and exclusions, and landmarks L = 1,440, 2,880, 4,320, 5,760, and 7,200 minutes. Care-plan receipt is attached only after population selection and remains descriptive.

The inherited artifact has 5,518 distinct `(patientunitstayid, landmark)` keys across all three membership definitions. The mutually exclusive overlap classes audited here contain 3,788 distinct keys: `unbounded_only` 1,148, `retained_24h_only` 1,462, and `retained_6h` 1,178. The 24-hour-only class is membership in 24-hour but not 6-hour; the 6-hour class is membership in 6-hour; first-stay and variant rules are not recomputed or changed.

For each row and each lookback, the primary estimands are proportions classified positive, negative, ambiguous, or conflicting in `[L-360,L)`, plus risk differences and bootstrap confidence intervals clustered by stay (and sensitivity clustered by hospital). Secondary estimands are the same proportions in 24-hour and 6-hour windows, hospital- and landmark-stratified distributions, and future/placebo evidence in `[L,L+360)`.

## Explicit temporal state machine

Evidence is evaluated only by event offset relative to L; no chart entry time is substituted for clinical event time.

1. **Airway state.** From `respiratoryCare.csv.gz`, take the last pre-L `airwaytype` as the carried state, while separately counting values in the prior 6-hour window. `oral ett`, `nasal ett`, `tracheostomy`, `double-lumen tube`, and `cricothyrotomy` are invasive-airway-positive lexical states; `no artificial airway` and `none` are negative; null/other values are ambiguous. `ventstartoffset` and `ventendoffset` are used as an explicit interval: a pre-L row with non-null start and null or post-L end is active at L. The `priorventstartoffset`/`priorventendoffset` fields are retained for a sensitivity analysis, not silently treated as current state.

2. **RT Vent On/Off state.** From `respiratoryCharting.csv.gz`, `RT Vent On/Off` values are value-aware: `continued` and `start` are positive; `off` is negative; `suspended` and any unrecognized value are ambiguous. A positive state is not inferred from label presence alone.

3. **Ventilator setting/mode state.** Value-bearing rows for mechanical ventilator mode, ventilator support mode, ventilator population, pressure support/control, tidal-volume set/observed, mean airway pressure, exhaled minute/ tidal volume, Adult Con setting and patient/ventilator output labels, and ventilator checks are retained as high-specificity device-oriented evidence only when `respchartvalue` is nonempty and not `none`, `null`, `na`, or blank. Their presence alone is not sufficient for invasive ventilation because it may be a stale or device-dependent trace.

4. **Treatment corroboration.** From `treatment.csv.gz`, a contemporaneous `mechanical ventilation` treatment string excluding `non-invasive ventilation` is invasive-treatment corroboration. NIV is retained as a separate negative/alternative modality signal and never counted as invasive evidence.

5. **Note corroboration.** `note.csv.gz` `Intubation` and `Extubation` note types are timestamped corroboration. Note text is not exported or sent to public search. These note types are not independently treated as continuous state.

6. **Mutually exclusive row classification.** Positive means an explicit active ventilation interval at L, or a positive RT/mode/setting value plus invasive mechanical-ventilation treatment, or an invasive airway plus value-bearing ventilator evidence. Negative means an explicit `RT Vent On/Off=off` or latest `no artificial airway` state when no positive rule fires. Conflicting means positive and negative evidence coexist in the same prior-6-hour/L state window. Ambiguous means neither rule fires, including missing, unrecognized, or isolated label-only evidence. In the primary implementation, conflicting takes precedence over positive/negative; a sensitivity reports component-level discordance rather than collapsing it.

This ordering prevents an old airway label from automatically winning against current off/no-airway evidence and prevents a ubiquitous label from being counted as a positive state.

## Exact source bindings

The source snapshot is eICU 2.0 `[source checksum]`, catalog [source checksum].

* `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/respiratoryCare.csv.gz`, archive member ordinary file, table `respiratoryCare`; columns `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
* `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/respiratoryCharting.csv.gz`, archive member ordinary file, table `respiratoryCharting`; columns `patientunitstayid`, `respchartoffset`, `respchartvaluelabel`, `respchartvalue`, with `respchartentryoffset` retained for provenance but not used as clinical time.
* `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/treatment.csv.gz`, archive member ordinary file, table `treatment`; columns `patientunitstayid`, `treatmentoffset`, `treatmentstring`.
* `baidu_downloads/eicu_mimic/eicu数据库/EICU 2.0数据/note.csv.gz`, archive member ordinary file, table `note`; columns `patientunitstayid`, `noteoffset`, `notetype`; note text is not required for the primary state machine and is not exported.
* Parent denominator bindings remain those documented in the parent proposal, including `patient.csv.gz` (`patientunitstayid`, `uniquepid`, `hospitalid`, `age`, `unitvisitnumber`, `unitdischargeoffset`) and the inherited parent artifact. No private clinical record is queried publicly.

All source files are read-only. Full-file scans used DuckDB `read_csv_auto(..., strict_mode=false, ignore_errors=true)` because malformed rows are known in these frozen CSVs; malformed-row counts must be quantified in a production adjudication. The computation used the full respiratoryCare, respiratoryCharting, and treatment sources, rather than a row sample.

## Executed audit

The executed state audit output is `[internal dataset path]` (job `[research job]`). It scanned 3,788 overlap-class keys in `[L-360,L)`. Results were:

* `unbounded_only`: positive 579/1,148 (50.44%), negative 0/1,148, ambiguous 569/1,148 (49.56%), conflicting 0.
* `retained_24h_only`: positive 913/1,462 (62.45%), negative 4/1,462 (0.27%), ambiguous 545/1,462 (37.28%), conflicting 0.
* `retained_6h`: positive 961/1,178 (81.58%), negative 7/1,178 (0.59%), ambiguous 210/1,178 (17.83%), conflicting 0.

Thus, under this conservative state machine, unbounded-only rows have 31.14 percentage points less positive evidence than 6-hour-retained rows and 31.73 percentage points more ambiguous evidence; the positive difference versus 24-hour-only rows is 12.01 percentage points. Explicit negatives were rare, and no row was conflicting under the operational rule. The absence of conflicts is not evidence of agreement: it reflects the conservative positive/negative definitions and should be stress-tested with component-level discordance.

Hospital and landmark cross-tabs were written to `[internal dataset path]` and `[internal dataset path]`. They must be shown with denominators and sparse cells, not pooled into a claim of transportability. The row-level audit is `[internal dataset path]`.

The parent’s future/placebo computation remains required: compare positive and composite marker coverage in `[L,L+360)` with present coverage, separately by hospital and landmark. The prior parent results showed future composite coverage lower than present (91.03% versus 99.56% unbounded-only; 90.08% versus 99.73% 24-hour-only; 91.09% versus 99.41% 6-hour-retained), but those broad-label results cannot override the value-aware state audit. A proper future state audit should repeat the same state machine post-L as a placebo and report transitions (positive-to-negative, ambiguous-to-positive, and future-only evidence).

## Interpretation and falsification gates

Support for stale carry-forward is a materially lower positive-state proportion and materially higher ambiguity in unbounded-only rows, replicated across landmarks and not explained solely by hospital documentation intensity. The executed result is directionally supportive of the stale-carry-forward concern, unlike the parent’s broad label-presence result. It is not evidence that 6-hour rows represent true ventilation; it only shows that they more often meet the operational high-specificity proxy.

Evidence against stale carry-forward would be similar positive-state proportions after value-aware classification, frequent explicit active intervals in unbounded-only rows, low ambiguity, and stable hospital/landmark effects. A finding dominated by one hospital, one landmark, or one marker family is inconclusive. Explicit off/no-airway evidence, especially when temporally adjacent to positive evidence, would be adverse to a simple carried-forward state and should be reported as conflict rather than discarded.

Results are inconclusive if confidence intervals are wide, hospital/landmark heterogeneity dominates the pooled contrast, parser rejection is substantial or differential, or expert review shows that the positive rules mostly capture documentation rather than active invasive ventilation. Sensitivity analyses must vary the positive rule (interval-only; interval plus RT state; requiring two independent families), airway lexical mapping, and windows (6 versus 24 hours), while preserving the inherited denominator.

## What the computation cannot establish

This audit cannot establish actual ventilation, continuous duration, invasive versus NIV status for every row, delivery of an SBT, quality of daily evaluation, clinician intent, causality, benefit, or transportability. It cannot adjudicate whether a `continued` value was entered prospectively, copied forward, or recorded after an event. Definitive interpretation requires expert review against respiratory flowsheets, tube/device placement and removal, ventilator settings, event semantics, and a clinically adjudicated ventilation episode gold standard. Any claim about care-plan action or patient benefit requires a separate outcome study with confounding control and clinical adjudication.

## Change from parent and remaining uncertainty

Changed: broad label presence is no longer the principal ventilation endpoint; airwaytype, interval fields, RT values, setting values, treatment, and note markers are ordered into explicit state classes; negative and conflicting evidence are retained; hospital/landmark tables and future/placebo state transitions are required. The executed result materially changes the measurement conclusion toward stale-carry-forward concern.

Unchanged: exact parent population and target-independent denominator, strict physiology/exclusions, first-stay freezing, landmarks, post-freeze receipt classification, and the noncausal interpretation. Remaining uncertainty is semantic validity of source values, missingness and malformed rows, residual documentation persistence, sparse note/treatment corroboration, and lack of expert episode adjudication.
