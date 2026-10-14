> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# First-line vasopressor choice and escalation order in shock: independent prognostic signal, or hospital practice and confounding? A bounded eICU-CRD 2.0 study

**Dataset:** eICU-CRD 2.0 (local snapshot 896e1fb7) · **Parent seed:** `[prior hypothesis]` ([starting question])
**Status:** complete, bounded, falsifiable study proposal with verified data bindings (measured counts from jobs `job-ce296ea8`, `job-b18692fc`, and shell probes; outputs `work/ep6-measure.json`, `work/ep6-mortality.json`).

---

## 1. Unresolved question and why it matters clinically

**Question.** In ICU patients receiving a vasopressor in the first 24 h, does the **first-line vasopressor agent** (norepinephrine, dopamine, phenylephrine, epinephrine, vasopressin) and the **escalation order** (which second agent is added first, and how soon) carry independent prognostic information for in-hospital mortality beyond shock type, severity and hospital, and is the residual between-hospital variation in first-line choice and escalation practice associated with outcomes?

**Why it matters.** First-line vasopressor selection is one of the most common real-time treatment decisions in shock, yet randomized evidence is narrow: SOAP II (K2) found no 28-day mortality difference between dopamine and norepinephrine overall (OR 1.17, 95% CI 0.97–1.42) but a dopamine mortality signal in cardiogenic shock, and VANCS II (K3) found no difference between vasopressin and norepinephrine in a small cancer septic-shock cohort. Guidelines therefore leave first-line choice to clinician judgment, and practice varies widely between hospitals. If real-world first-line choice and escalation order are prognostic *after* conditioning on shock type, severity and hospital, that would (a) identify a modifiable process variable for quality improvement, and (b) explain why treatment findings may not transport across hospitals (the seed's stated significance). If they are not prognostic after conditioning, that would support the interpretation that observed agent differences are confounding/practice artifacts rather than treatment effects — a consequential negative result for practice variation programs.

**Rival explanations with different observable predictions:**
- **R1 (agent effect).** The agent or escalation order itself affects mortality (e.g., dopamine arrhythmogenicity per K2). Prediction: agent/escalation terms remain significant after conditioning on shock type, APACHE, age, sex and hospital; effects consistent across hospitals.
- **R2 (confounding by severity/shock type).** Sicker or cardiogenic patients are preferentially given certain agents (e.g., vasopressin in severe septic shock; dopamine in cardiogenic). Prediction: crude differences (measured: vasopressin-first mortality 41.1% vs dopamine-first 22.8%) shrink to null after conditioning; agent terms become non-significant.
- **R3 (hospital practice artifact).** Between-hospital differences in first-line choice reflect local habit, and residual outcome differences track hospital, not agent. Prediction: hospital random effects absorb most of the agent contrast; leave-one-hospital-out estimates unstable; escalation-order signal driven by a few hospitals.

## 2. Verified data bindings (measured)

Source files (read-only), snapshot 896e1fb7:
- `treatment.csv.gz` (SHA `115ce152...`): columns `treatmentid, patientunitstayid, treatmentoffset, treatmentstring, activeupondischarge`. Shock rows: `treatmentstring` starting `cardiovascular|shock` — 112,206 rows, 24,290 stays.
- `patient.csv.gz` (SHA `2acf25f7...`): `patientunitstayid, hospitalid, gender, age, hospitaldischargestatus, ...`
- `apachePatientResult.csv.gz` (SHA `f9870a5a...`): `patientunitstayid, apachescore, ...`
- `admissionDx.csv.gz` (SHA `f0018aa3...`): `patientunitstayid, admitdxname`
- Join key: `patientunitstayid`; time field: `treatmentoffset` (seconds from unit start).

Measured (jobs `job-ce296ea8`, `job-b18692fc`, shell probes):
- Population: 18,360 stays with a first vasopressor agent (norepi/vaso/dopa/phenyleph/epi) documented in 0–24 h, across 182 hospitals (min 1 stay/hospital; analysis will require ≥10 stays/hospital, expected ~120–150 hospitals).
- First-line agent: norepi 11,322 (61.7%), phenyleph 2,936 (16.0%), dopa 2,120 (11.5%), epi 997 (5.4%), vaso 985 (5.4%).
- Crude in-hospital mortality (hospitaldischargestatus='Expired'): overall 27.5%; by first agent: norepi 28.3%, epi 24.4%, phenyleph 23.8%, dopa 22.8%, vaso 41.1% — large crude spread, motivating the confounding test.
- Sepsis admission-dx rate by first agent: norepi 40.9%, vaso 34.4%, dopa 18.5%, phenyleph 16.0%, epi 8.8% — strong shock-type confounding visible in raw data.
- Mean APACHE by first agent: norepi 79.6, vaso 90.2, dopa 71.5, phenyleph 70.4, epi 76.0 (note: apachescore field range 0–211 in eICU; treat as continuous severity marker, document range).
- Escalation: 4,433 stays (24.1%) received a second *different* agent within 24 h; median delay to second agent 0.12–0.22 h. Most common transitions: norepi→vaso 1,128; phenyleph→norepi 377; dopa→norepi 326; norepi→phenyleph 493; norepi→epi 324; epi→norepi 251.
- Hospital practice: 160/182 hospitals have norepinephrine as dominant first agent; 0 hospitals dominant-vasopressin; hospital-level share of stays with any vasopressin in 24 h: median 13.8%, p90 26.4% — measurable between-hospital variation in escalation practice.

## 3. Estimand and analysis plan

**Primary estimand.** In the 0–24 h shock population, the association of (a) first-line agent and (b) escalation order (second agent identity and delay) with in-hospital mortality, adjusted for shock type (sepsis dx, cardiogenic proxy), severity (APACHE), age, sex, and hospital.

**Models (hospital-clustered logistic GLMM, random intercept for hospitalid):**
- M1 (baseline): age, sex, APACHE (continuous, winsorized 1st–99th), sepsis-dx indicator, hospital random intercept.
- M2 (agent): M1 + first-line agent (categorical, norepi reference).
- M3 (escalation): M2 + second-agent indicator, second-agent identity (among those with a second agent), delay-to-second-agent (h, log).
- R3 test: hospital-level first-agent mix and vasopressin-usage rate as hospital covariates; leave-one-hospital-out refit (hospitals ≥10 stays) for agent-term stability; report the share of hospital folds where the sign of the vasopressin-first contrast flips.

**Sensitivity (learned alternative).** Gradient-boosted trees (CPU) on the same features to detect nonlinearity/higher-order interaction (agent × shock type × APACHE) that the parametric GLMM would miss; compare the agent main effect and agent×shock-type interaction against M3. This is the substantive learned alternative: it can reveal whether the agent effect is concentrated in a severity/shock-type stratum (e.g., dopamine harm in non-septic shock, echoing K2's cardiogenic subgroup) rather than a main effect.

**Deferred alternatives (with revisit criteria):**
- Instrumental-variable / hospital-preference analysis: deferred because the seed itself cautions hospital preference cannot automatically serve as an IV; revisit only if a valid instrument (e.g., hospital-level formulary policy) becomes identifiable.
- Time-to-event (ICU mortality, vent-free days): deferred because the primary question is agent contrast, not timing; revisit if mortality censoring (1.1% missing status) materially changes estimates.
- GPU/sequence methods: not scientifically warranted for this tabular contrast; no GPU quota claimed.

## 4. Falsification criteria (pre-specified)

- **Supportive of R1 (agent/escalation signal):** in M2/M3, at least one non-norepinephrine first agent has a mortality OR with 95% CI excluding 1.0 after full adjustment, the same contrast keeps its sign in ≥80% of leave-one-hospital-out folds, and the GBM agent×shock-type interaction is significant.
- **Supportive of R2 (confounding):** crude agent contrasts (e.g., vaso vs norepi ≈ 1.9) shrink by ≥50% in M2 and become non-significant (CI includes 1.0); GBM adds <1% AUC over M1.
- **Supportive of R3 (practice artifact):** agent terms non-significant after hospital random effects; ≥50% of hospital folds flip the sign of the largest agent contrast; hospital-level vasopressin-usage covariate is significant while agent terms are not.
- **Inconclusive:** agent terms significant in <80% of folds with wide CIs straddling 1.0, or escalation-order terms unstable; report as such and state that the question needs richer dose/timing data (infusionDrug) or another dataset.

## 5. What results would and would not establish

- A supportive R1 result establishes an *association* of first-line choice/escalation with mortality in this population; it does not establish causality (residual confounding by unmeasured shock physiology, no randomization). Causal claims require an RCT or a valid instrument.
- A supportive R2/R3 result would support deprioritizing agent-choice audits as a mortality lever and refocusing on severity-adapted selection; it would not prove agents are equivalent (absence of evidence in a confounded design).
- Clinical adjudication needed: shock-type labels (sepsis dx string, cardiogenic proxy) are imperfect; a final interpretation should be reviewed against infusionDrug dose data and clinical context.

## 6. Key references

- [K1] eICU-CRD 2.0 documentation (full text inspected; SHA-256 `124eb8c9...`) — data binding.
- [K2] SOAP II, De Backer et al., NEJM 2010, PMID 20200382 (abstract only) — bounds the dopamine/norepinephrine first-line contrast; cardiogenic-shock mortality signal.
- [K3] VANCS II, Hajjar et al., Crit Care Med 2019, PMID 31609774 (abstract only) — bounds the vasopressin/norepinephrine first-line contrast (null).

See `work/key-references.json` and attached source snapshots in `work/sources/`.
