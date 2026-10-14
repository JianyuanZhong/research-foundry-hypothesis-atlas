> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# When the feed stops and the insulin does not: how much of the glucose fall after enteral-feed interruption is insulin-attributable, and how much is the deterioration that stopped the feed?

A multicentre negative-control-exposure study with an insulin dose–response, in eICU-CRD v2.0

> **Design history, stated up front.** This study was drafted as a binary target-trial emulation of
> the insulin-hold decision (outcome: glucose < 54 mg/dL within 12 h). A measured feasibility probe
> run before the plan was frozen found **26 such outcome events** in the entire eligible population
> (§2.3). The binary emulation is therefore not deliverable in eICU and is **not** what is proposed.
> The proposed study keeps the same scientific question and the same discriminating logic, but moves
> the primary estimand to the continuous glucose trajectory, which the same data measure well, and
> reports the rare-event incidence as an explicit measured bound rather than as an estimate.

Dataset island: **eICU** (eICU Collaborative Research Database v2.0 snapshot
`[source checksum]`).
Scientific parent: expert seed `[starting question]` (board id `[prior hypothesis]`,
assessed **repairable** in episode 1). This is a declared targeted repair that substantially reframes
the seed; the reframing and the reason for it are stated in §1.3.

---

## 1. The question

### 1.1 What the seed asked, and why it is not yet a testable scientific question

Seed eicu-09 states: *"At the same insulin intensity, patients with worsening kidney function and
interrupted nutrition are more likely to develop hypoglycemia."* Episode 1 assessed it **repairable**
for two specific reasons that I accept and act on here:

1. As a *risk-factor interaction* it is close to established clinical teaching. Renal impairment
   prolongs insulin clearance and interrupted nutrition removes exogenous glucose; that these raise
   hypoglycaemia risk is in every ICU insulin protocol. Confirming it would add little.
2. The seed's own caution — *"missing nutrition records must not be treated as cessation of
   nutrition"* — is an exposure-misclassification threat that must be resolved by a measured audit
   before any inferential claim. It had not been.

### 1.2 The strongest claim the existing evidence already supports

- Moderate and severe hypoglycaemia in critically ill adults is associated with increased mortality,
  with a dose–response by depth of hypoglycaemia [K1].
- That association is **not uniform by cause**: hypoglycaemia occurring without insulin exposure
  ("spontaneous") carries at least as strong, and in several cohorts a stronger, association with
  death than insulin-associated hypoglycaemia [K1][K2].
- Removing exogenous glucose while insulin action continues lowers blood glucose. This is
  pharmacology, not a hypothesis.
- **The closest inspected prior work on this exact exposure is a risk-factor association, not a
  decision-level estimate** [K3]: in one academic ICU (2,272 patients, 156 events of glucose
  < 45 mg/dL), a length-of-stay-matched case–control analysis reported *"a decrease of nutrition
  without adjustment for insulin infusion"* with OR 6.6 (95 % CI 1.9–23) alongside insulin use
  (OR 5.3, 2.8–11). What makes [K3] the *opening* rather than the answer is that the **same model**
  also associated deterioration markers with hypoglycaemia — sepsis OR 2.2 (1.2–4.1), inotropic
  support OR 1.8 (1.1–2.9) — while gastric residual without insulin adjustment and reduced GFR were
  not. Both rival explanations sit in one cohort, estimated side by side, and the design cannot
  separate them: exposures were scored by chart review *around the moment of hypoglycaemia*, so
  ascertainment is outcome-anchored, with no time origin, no strategy comparator and no estimand.
  All three key works were inspected **abstract-only** (publisher full text not retrievable here;
  acquisition failures are listed in `work/branch-lit/novelty-and-opening.md`), so claims drawn from
  them are limited to abstract-level statements and their covariate lists and operational exposure
  definitions were *not* read.

### 1.3 The unresolved claim this experiment tests

None of the above tells a clinician or a hospital **what fraction of post-interruption hypoglycaemia
is prevented by the obvious counter-action**, nor whether the hypoglycaemia that follows a feed
interruption is caused by the unmodified insulin at all. Two explanations predict the same marginal
association and are routinely conflated:

- **H_iatrogenic (leading claim).** When enteral feeding stops and insulin is *not* reduced, the
  continuing insulin action causes a material part of the subsequent glucose fall. Operationally:
  the fall is substantially larger when insulin is on board than when it is not, it scales with the
  insulin rate left running, and it is accompanied by the potassium shift that continuing insulin
  action produces. If so, the event is in principle preventable by reducing insulin or supplying
  dextrose.
- **H_marker (strongest rival).** Feeds are stopped *because something happened* — septic shock,
  hepatic failure, a procedure, intubation/extubation, vomiting, vasopressor escalation. That same
  event independently causes the glucose fall (impaired gluconeogenesis, hepatic hypoperfusion,
  reduced counter-regulation). The insulin response is then largely irrelevant, and any apparent
  benefit of reducing insulin is confounding by indication reversed.
- **H_measurement (third rival, often ignored).** After a feed stops, glucose is simply checked more
  often, and the recorded nadir of a more densely sampled series is lower. Part or all of the
  apparent fall is then an artefact of monitoring behaviour. This is not a nuisance to be adjusted
  away in a sentence: the probe in §2.3 measured a median of 6 post-interruption glucose values in
  the insulin group versus 3 without insulin, so the artefact is present and of the right sign to
  mimic H_iatrogenic. §3.4 gives three pre-specified handles and one pre-committed discard rule.

These rivals make **different observable predictions** (§4). Resolving them determines:

- whether an automatable EHR rule ("feed stopped + insulin running → hold/reduce insulin or start
  10% dextrose") is worth building and auditing; and
- whether ICU hypoglycaemia rate is a defensible *preventability-based* quality metric, or whether
  hospitals are substantially being scored on their patients' illness.

A null or small effect is scientifically and operationally valuable: it would redirect quality-
improvement effort away from a widely assumed, intuitively obvious target.

**The inspected evidence actively conflicts on this axis, which is why the question is open and not
merely unstudied.** [K1] (6,026 randomised patients) found the mortality association *strongest where
the event looks least iatrogenic* — severe hypoglycaemia in the absence of insulin treatment, HR 3.84
(2.37–6.23), with the gradient steepest for death from distributive shock — which argues that
H_marker dominates and that an insulin-hold rule has little headroom. [K2] (642 patients classified
prospectively-defined as medication-induced vs spontaneous by agent-specific pharmacokinetic windows)
found **no** difference in adjusted hospital mortality by aetiology (OR 1.22, 0.77–1.93), which both
undercuts the usual "iatrogenic events are the lethal ones" justification for preventability-based
hypoglycaemia quality metrics *and* implies that preventing the drug-attributable subset still has
value. Both condition on the hypoglycaemic event rather than on the clinical decision, and neither
measures nutrition at all — [K2]'s "spontaneous" label is a residual category ("no identifiable
cause") that therefore *absorbs* feed interruption. **The strongest counter-argument to this proposal
is that [K3] already settled the mechanistic part** (OR 6.6, which clinicians accept as causal) so
that only implementation remains; the honest rebuttal is that OR 6.6 rests on 156 single-centre
events from 2002–2004 strict-glycaemic-control-era practice with a CI spanning an order of magnitude
and an outcome-anchored exposure, and that it provides no estimate of the fraction attributable to
the omission. Conflicting evidence plus an untested decision-level estimand is the opening. This is
**not** an exhaustive novelty search: see `work/branch-lit/novelty-and-opening.md` §(d) for the
named literatures not searched (EPaNIC/PermiT/TARGET/NUTRIREA nutrition-trial secondary analyses,
computerised insulin titration, the MIMIC glycaemic-control literature), any of which could contain
a closer match.

### 1.4 What this study is not

It is not a test of whether hypoglycaemia causes death (not identifiable here, and [K1] already
bounds what observational data can say). It is not a glycaemic-target trial. It does not claim a
mechanism for hypoglycaemia in any individual patient.

---

## 2. Data bindings (measured in this episode, not assumed)

All paths are read-only sources listed in `datasets/eicu/README.md`; the base directory is
`[internal dataset path]`.
Every table below is an ordinary gzip CSV file (archive member: *ordinary file*).

| Role | Source file (sha256) | Columns used | Join key / time field |
|---|---|---|---|
| Cohort, hospital, censoring | `patient.csv.gz` (`2acf25f7…dc392b`) | `patientunitstayid`, `hospitalid`, `age`, `gender`, `unitdischargeoffset`, `unitdischargestatus`, `hospitaldischargestatus`, `unittype`, `admissionweight` | `patientunitstayid`; offsets in minutes from unit admission |
| Enteral nutrition (exposure) | `intakeOutput.csv.gz` (`f809b425…9baa5121`) | `patientunitstayid`, `intakeoutputoffset`, `cellpath`, `celllabel`, `cellvaluenumeric` | `patientunitstayid` / `intakeoutputoffset` |
| IV insulin (treatment) | `infusionDrug.csv.gz` (`f1c958b9…beefc9fc3b`) | `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `patientweight` | `patientunitstayid` / `infusionoffset` |
| SC / other insulin | `medication.csv.gz` (`3d504b48…9810ebc5`) | `patientunitstayid`, `drugstartoffset`, `drugstopoffset`, `drugname`, `dosage`, `routeadmin`, `frequency`, `drugordercancelled` | `patientunitstayid` / `drugstartoffset` |
| Outcome + confounders | `lab.csv.gz` (`91b55ed3…20d93bc7a`) | `patientunitstayid`, `labresultoffset`, `labname`, `labresult` | `patientunitstayid` / `labresultoffset` |
| Severity at admission | `apacheApsVar.csv.gz` (`4dfa6d3d…cbfc41b4`), `apachePatientResult.csv.gz` (`f9870a5a…bb7a070a`) | APS components, `apachescore`, `predictedhospitalmortality` | `patientunitstayid` |
| Ventilation / procedure context | `respiratoryCare.csv.gz` (`67b63bd7…4ee55da`), `treatment.csv.gz` (`115ce152…3fca4bd6`) | `ventstartoffset`, `treatmentoffset`, `treatmentstring` | `patientunitstayid` |
| Care limitation (sensitivity) | `carePlanGeneral.csv.gz` (`6bc1b695…b5f6d33aa6`) | `cplitemoffset`, `cplgroup`, `cplitemvalue` | `patientunitstayid` |

**Identity rule.** All analysis is inside the eICU island. No join to MIMIC, HCC or UKB.

### 2.1 Measured coverage (job receipts in §8)

MEASURED, [research job] (141 s CPU):
- `lab.csv.gz`: 39,132,531 rows. `bedside glucose` 3,175,835 rows and `glucose` 1,319,496 rows
  across **192,798 stays**. Per-stay glucose count: median 10, p75 29, p90 57, p99 167.
  Glucose <70 mg/dL: 86,228 results in 29,624 stays; <54: 25,555 in 11,480 stays; <40: 8,044 in 4,482.
- `infusionDrug.csv.gz`: 4,803,719 rows; **14,312 stays** have an insulin infusion. Dominant
  `drugname` strings: `Insulin (units/hr)` 252,838; `Insulin (ml/hr)` 128,016; `Insulin ()` 14,139;
  `Insulin 250 Units Sodium Chloride 0.9% 250 ml (units/hr)` 12,810. `drugrate` carries the rate.
- `medication.csv.gz`: 7,301,853 rows; **66,120 stays** with an insulin order (NOVOLOG, lispro,
  aspart, regular, glargine, …).

MEASURED, [research job] (90 s CPU) — this is the audit the seed demanded:
- Enteral **formula volume** charting (regex on `celllabel`, restricted to `cellpath` containing
  `Intake`, excluding flush/water/residual/medication labels) exists for **8,920 stays** in
  **74 of 208 hospitals**; 5,294 stays have ≥10 feed rows, 3,722 have ≥24.
- **Median within-stay feed charting interval = 60 min** (deciles 60,60,60,60,60,60,300,480,690),
  i.e. in the majority of these stays the flowsheet is charted hourly — fine enough to time an
  interruption to the hour.
- Overlap of feed-charting stays with insulin-infusion stays = **1,626**; 1,250 with ≥10 feed rows.
- Candidate interruption events (a charted feed volume > 0 at time t, no positive feed row in
  (t, t+180 min], **the flowsheet still active** — at least one other I/O row charted in that
  window — and an insulin infusion running at rate > 0 in [t−240, t]): **2,069 events in 790 stays**.

**This directly resolves the seed's stated threat.** Absence of a feed row is only read as
interruption when the I/O flowsheet is demonstrably still being charted for that stay in the same
window. Hospitals and stays without active hourly I/O charting are *excluded*, not imputed.

### 2.2 Honest limitation created by that audit

Enteral nutrition is charted usably in **74/208 hospitals (8,920/200,859 stays, 4.4 %)**. The study
population is therefore *not* a representative sample of eICU. It is a population of tube-fed ICU
patients in hospitals with hourly I/O flowsheet charting. Hospital-level generalisation is explicitly
out of scope, and the hospital set must be reported.

---

## 2.3 Measured power facts that CHANGED the design ([research job], [research job])

I drafted this study as a binary target trial (12-h risk of glucose < 54 mg/dL). A measured probe
refuted that design's feasibility before it was frozen, and the honest consequence is recorded here
rather than absorbed silently.

Applying the event definition of §3.1 (≥180-min feed gap, flowsheet active, ≥1 glucose before and
after, ≥12 h of remaining unit stay):

| | events | stays | hospitals | nadir < 54 | nadir < 70 | mean ΔG (nadir − baseline) | SD of ΔG |
|---|---|---|---|---|---|---|---|
| insulin active at t | **2,328** | 983 | 39 | **26 (1.12 %)** | 132 (5.67 %) | **−38.1 mg/dL** | 48.5 |
| no insulin at t (negative control) | **15,854** | 3,784 | 53 | 130 (0.82 %) | 430 (2.71 %) | **−19.3 mg/dL** | 40.7 |

IV insulin infusion rate at t among 1,662 infusion events: quartiles 2.0 / 4.0 / 6.0 units/h.
Paired potassium (one value in [t−360,t] and one in (t,t+720]): **432 events**.
Relaxing the gap to 120 min gives 2,495 / 15,185 events — essentially the same, so the result is
not an artefact of the 180-min threshold.

**Consequence 1 — the binary endpoint is not deliverable.** 26 outcome events cannot support a
clone–censor–weight risk-difference estimate. No weighting scheme recovers power from 26 events.
I am not shrinking the scientific question to fit; I am changing the *endpoint* to the one the data
can measure, and stating the limit on the one it cannot.

**Consequence 2 — the continuous endpoint is strongly powered.** Every event carries a glucose
trajectory. With SD ≈ 48 mg/dL and n = 2,328 insulin events (983 stays), the standard error of a
mean ΔG contrast is ≈ 1.1 mg/dL before clustering and ≈ 2 mg/dL with a conservative stay-level
design effect. For the dose–response slope on insulin rate (SD of rate ≈ 3 U/h, n = 1,662 infusion
events) the standard error is ≈ 0.4–0.6 mg/dL per U/h, so a slope of 1.7 mg/dL per U/h is
detectable at 80 % power. These are adequate for the scientific question.

**Consequence 3 — a measured bound on the clinical headroom.** Whatever the causal truth, the 12-h
incidence of glucose < 54 mg/dL after a feed interruption during insulin therapy in this population
is of order 1 %. A perfect prevention rule could therefore avert at most about one severe episode
per ~90 interruptions. Reporting that bound is itself decision-relevant and is a pre-specified
deliverable.

**Consequence 4 — a measurement threat the probe exposed.** The nadir is a minimum statistic and
therefore depends on how often glucose was sampled; the insulin group has a median of 6
post-interruption glucose measurements versus 3 in the no-insulin group. A raw nadir comparison
between those groups is partly a sampling artefact. This is handled in §3.4 and is the strongest
single argument for the trajectory-model alternative in §5.2.

Exploratory crude arm-level numbers I saw during this probe are recorded, with their
interpretation and their non-confirmatory status, in `work/diagnostic-evidence.md`.

---

## 3. Design

### 3.1 Unit of analysis and time zero

**Event (time zero, t):** a *feed interruption* — the last charted positive enteral-formula volume
before a ≥180-minute gap with no positive feed row, with the intakeOutput flowsheet demonstrably
still active for that stay in (t, t+180] (at least one other I/O row charted). A stay may contribute
several events; all inference clusters on `patientunitstayid`.

**Eligibility at t:** adult stay (`patient.age`; ">89" recoded to 90); hospital passes the charting
audit (hourly I/O flowsheet, enteral formula volume charted); ≥1 glucose in [t−240, t];
≥1 glucose in (t, t+720]; `unitdischargeoffset` ≥ t+720.

**Exposure groups:**
- **Insulin-exposed**: IV insulin infusion rate > 0 in [t−180, t] (`infusionDrug.drugrate`, names
  matching insulin with a units/h rate), or an SC insulin administration in [t−360, t]
  (`medication.drugstartoffset`, not cancelled).
- **Negative control (no insulin)**: neither of the above in the same windows.

### 3.2 Primary estimand (revised to the powered endpoint)

Let ΔG = (glucose nadir in (t, t+720]) − (last glucose in [t−240, t]), and let R = IV insulin
infusion rate at t (units/h; secondarily units/kg/h using `patient.admissionweight`).

**Primary (A): the insulin-attributable component of the post-interruption glucose fall.**
E[ΔG | insulin-exposed, standardised] − E[ΔG | no insulin, standardised], standardising the
no-insulin group to the insulin group's joint distribution of baseline glucose, diabetes history
(`pastHistory`/`diagnosis`), severity, vasopressor use, renal function, feed rate withdrawn, and
**post-interruption glucose-measurement count** (§3.4). Reported in mg/dL.

**Primary (B): the dose–response.** The slope dE[ΔG]/dR within the insulin-infusion group,
estimated with a flexible (natural-spline) function of R and the same adjustment set, plus the
counter-action indicator. Reported in mg/dL per unit/h.

**Secondary (C): the measurement-independent composite event.** `glucose < 54 mg/dL in (t, t+720]`
**OR** a non-cancelled rescue order for 50 % dextrose or glucagon with `drugstartoffset` in
(t, t+720] (`medication.csv.gz`, `drugname` matching dextrose 50 %/D50/D50W/glucagon,
`drugordercancelled != 'Yes'`). Measured in `[research job]`: rescue orders exist in
58,086 stays; within the eligible event set the composite gives **106 / 2,328 (4.55 %)** events in
the insulin-exposed group and **487 / 15,854 (3.07 %)** in the no-insulin group, versus 26 and 130
for glucose < 54 alone. **Rescue orders outnumber documented glucose < 54 by roughly 3:1 (83 vs 26
in the insulin group)**, which is itself a measurement result: glucose-only ascertainment of
hypoglycaemia in eICU misses most clinically recognised events. The composite is therefore the
*primary binary* endpoint and the glucose-only count is reported alongside it as the
ascertainment-limited version. Caveat bound in §8.1: these are **orders with a start offset, not
verified administrations**.

**Other secondary:** 12-h incidence of glucose < 54 and < 70 mg/dL alone (26 and 132 events in the
insulin group — descriptive only); composite at the < 70 threshold (204 vs 763); the derived "number
of insulin holds per severe episode averted" under the fitted dose–response; the glucose trajectory
in 2-h bins; the paired potassium change (n = 432 events).

### 3.3 Why this is not just a regression on an association

ΔG after a feed interruption has two sources: the withdrawn exogenous glucose acting on a patient
with *some* insulin on board, and whatever clinical event stopped the feed. The negative-control
exposure gives a direct measurement of the second source in the *same* kind of event, in the *same*
hospitals, with the *same* flowsheet behaviour. The difference, standardised, is the quantity a
clinician actually needs: *how many mg/dL of the fall is the insulin responsible for, and how does
that scale with the rate I leave running?*

### 3.4 Confounders, and the sampling-density problem

Time-varying covariates at t, each with its source: glucose level and 6-h slope, creatinine, BUN,
lactate, albumin, total bilirubin, potassium, bicarbonate (`lab.csv.gz`); insulin rate and
vasopressor rate (`infusionDrug.csv.gz`); SC insulin dose and corticosteroid exposure
(`medication.csv.gz`); mechanical ventilation (`respiratoryCare.csv.gz`); diabetes and hepatic
disease (`pastHistory.csv.gz`, `diagnosis.csv.gz`); admission severity (`apacheApsVar.csv.gz`,
`apachePatientResult.csv.gz`); age, sex, weight, unit type, hospital (`patient.csv.gz`); feed rate
in the preceding 6 h and total intake (`intakeOutput.csv.gz`).

**Sampling density is a first-class variable, not a nuisance.** The nadir of a sampled series falls
as the number of samples rises, and sampling is itself a response to clinical concern. Three
pre-specified handles, in increasing strength:
1. The post-interruption glucose-measurement count enters the adjustment set and the
   standardisation.
2. A **matched-sampling** sensitivity analysis restricted to events with exactly 3–6
   post-interruption measurements in both groups.
3. A **fixed-time** endpoint that does not depend on sampling count: glucose at the measurement
   nearest to t+240 min and to t+480 min (with the realised offset as a covariate). If the
   fixed-time and nadir analyses disagree in sign, the nadir result is discarded as a sampling
   artefact. This is a pre-committed rule, not a post-hoc choice.

---

## 4. The discriminating tests (this is what separates H_iatrogenic from H_marker)

Pre-specified. Each has a direction predicted by one hypothesis and not the other.

**D1 — Negative-control exposure (primary A).** H_iatrogenic predicts a substantially larger
standardised fall when insulin is on board. H_marker predicts the two standardised falls converge,
because the event that stopped the feed is common to both. Pre-committed materiality threshold:
a standardised difference of ≥ 10 mg/dL is taken as a material insulin-attributable component;
a 95 % CI contained in (−5, +5) mg/dL is taken as evidence against a material component.

**D2 — Dose–response (primary B).** H_iatrogenic predicts a monotone, positive slope of fall on
insulin rate. H_marker predicts a flat slope after adjustment. Pre-committed: slope CI excluding 0
and ≥ 2 mg/dL per U/h supports H_iatrogenic; a CI contained in (−1, +1) mg/dL per U/h is adverse.

**D3 — Potassium corroborant (pharmacologically specific, n = 432 paired events).** Continuing
insulin action drives potassium intracellularly; shock, acute kidney injury and tissue injury push
potassium *up*. H_iatrogenic predicts a larger fall in serum potassium in the insulin-exposed group
that tracks the insulin rate. This endpoint is **underpowered by design** (432 events) and is
reported as corroborative only, with its CI; it cannot refute D1/D2 on its own.

**D4 — Interruption-reason strata.** From data available at t, classify the interruption as
(a) **routine/nursing** — tube care or gastric residual charted, no new organ-support change in
[t−180, t+180]; (b) **procedural** — intubation/extubation (`respiratoryCare.ventstartoffset`),
dialysis or procedure (`treatment.treatmentstring`); (c) **deterioration** — new or escalating
vasopressor, new intubation, new lactate > 4 mmol/L in [t−180, t+180]. Stratum (a) is the primary
discriminating stratum: there the interruption is closest to being unrelated to systemic illness,
so H_marker predicts little excess fall while H_iatrogenic predicts the insulin effect persists.

**Measured, and this is a partial binding failure ([research job]).** Of the 2,328
insulin-exposed events, a vasopressor infusion was running in [t−180, t+180] for **511 (21.9 %)**
(2,302 / 15,854 = 14.5 % in the negative-control group), so stratum (c) is assignable. But a
**gastric-residual row in `intakeOutput.celllabel` was found for 0 events**: residual volumes are
not charted in the `intakeOutput` table in this snapshot. Stratum (a) as drafted is therefore
**not bindable from `intakeOutput` alone**. Two candidate rebindings, both *unverified*:
`nurseCharting.csv.gz` (`nursingchartcelltypevallabel`, 1.73 GB gz — the largest unexamined table)
and `treatment.csv.gz` / `careplangeneral.csv.gz` for NPO / procedure-hold strings.
**Pre-committed reading, unchanged in spirit and now quantified:** if, after attempting those two
rebindings, stratum assignment into (a)/(b)/(c) fails for > 50 % of events, the primary
discriminating stratum is lost; the study then reports the overall estimate plus the
vasopressor-stratified contrast only, with H_marker explicitly **not** excluded. On the measured
numbers this failure is more likely than not, and the proposal says so rather than assuming the
stratum will materialise.

**D5 — Timing shape.** Estimate mean glucose by 2-h bin in each group. Insulin pharmacodynamics
predict a fall concentrated in the first 2–6 h then a plateau or rebound once insulin is adjusted;
an illness process predicts a sustained decline tracking the illness.

**D6 — Renal-function modification (the seed's original claim, retained as secondary).**
Pre-specified interaction of the dose–response with ΔCreatinine over the preceding 24 h and with
eGFR category at t. Reported with its CI whatever the direction; explicitly *not* the primary test,
and explicitly underpowered relative to D1/D2.

**D7 — Counter-action, reported honestly as an associational contrast.** The "insulin reduced ≥50 %
or dextrose started within 150 min" vs "continued" contrast is retained, estimated with
inverse-probability-of-treatment weights on the §3.4 covariate set, but is reported as
**confounded by indication in a known direction** (clinicians reduce insulin precisely when they
foresee a fall) and is *not* used to support a prevention claim on its own. Its role is to test
whether the dose–response of D2 is attenuated after the counter-action — a coherence check.

**D8 — Ascertainment-independence test (new, from `[research job]`).** Run the binary
analysis twice: on glucose < 54 alone and on the measurement-independent composite of §3.2(C).
H_measurement (the artefact rival) predicts that the insulin-vs-no-insulin contrast shrinks or
reverses when the outcome no longer depends on how often glucose was measured, because the insulin
group is measured twice as often (median 6 vs 3 post-interruption values). H_iatrogenic predicts the
contrast *persists* under the composite. **Pre-committed:** if the two endpoints give risk
differences of opposite sign, the metric rather than the intervention is driving the result and no
directional claim is made (this is the same rule as the fixed-time handle in §3.4, applied to the
binary endpoint). Crude, exploratory anchor already seen and recorded in
`work/diagnostic-evidence.md`: 4.55 % vs 3.07 % composite, unadjusted and confounded — not a result.

**D9 — Replication of the dose–response in a second, deliberately *worse-identified* trigger.**
The method branch measured a much larger trigger set: **85,084 insulin-rate-decrease episodes in
12,755 stays**, 90 % with ≥ 3 glucose values in the next 12 h, 12-h nadir < 54 in 1.67 %
(≈ 1,421 events) (`[research job]`, 67.5 s, in
`work/branch-method/sampling_probe.json`). This cohort is **not** the primary population — see §7
for the Lead's reason — but the D2 dose–response slope is re-estimated in it as a pre-specified
replication. Its scientific value is the *direction of the discrepancy*: in the rate-decrease
cohort the insulin decision is made in response to the glucose trajectory itself, so confounding by
indication is maximal and the estimated insulin effect should be *biased toward protection*. If the
feed-interruption slope and the rate-decrease slope agree, the feed-interruption estimate is
unlikely to be an artefact of the interruption-specific selection; if the rate-decrease cohort shows
a much stronger apparent insulin effect, that difference quantifies how much the endogenous trigger
inflates it. Either way it is reported as a bias probe, never as the headline estimate.

---

## 5. Analysis

### 5.1 Baseline method (what the solver must fit)

1. Build the event table from the bound sources (§2); emit the event count, stay count and hospital
   count, and a CONSORT-style attrition table from all feed-charting stays to eligible events.
2. Estimate propensity/standardisation models: for D1, a model for insulin exposure at t given the
   §3.4 covariates, used for inverse-probability-of-treatment weighting *and* for g-computation
   standardisation; report both, and report overlap diagnostics (propensity distribution, weight
   truncation at 1st/99th percentile, standardised mean differences before and after).
3. Fit the ΔG outcome model: generalised linear model with a natural-spline function of insulin
   rate, the adjustment set, hospital random intercept, and the sampling-density terms of §3.4.
4. Uncertainty by **stay-level cluster bootstrap** (1,000 replicates, re-fitting weights inside each
   replicate). Not event-level: stays contribute a median of ~2 events.
5. Repeat for the fixed-time endpoints, the matched-sampling subset, and each D4 stratum. Fit the
   binary composite endpoint of §3.2(C) with the same weights and standardisation (106 / 2,328 vs
   487 / 15,854 measured events), and the glucose-only endpoint beside it, as **D8**. Report the
   effective per-arm event count *before* interpreting; **< 50 events in the smaller arm is reported
   as inconclusive, explicitly not as a null**.
6. **Held-out confirmation: leave-one-hospital-out refitting** across the 39 (insulin) / 53
   (negative control) hospitals; report the distribution of the estimate and whether the sign is
   stable. Any quantity whose sign flips across hospitals is reported as unstable.

### 5.2 Substantive alternative on the same question

A mechanistic **glucose–insulin state-space model**: latent plasma glucose evolving under a
patient-specific insulin sensitivity S_i, endogenous glucose production, and an exogenous
glucose-appearance term driven by the *charted feed rate* (which is observed, and which drops to
zero at t), observed through irregularly sampled bedside glucose; fitted hierarchically across
events with partial pooling across patients and hospitals.

What it recovers that the baseline loses:
- **A sampling-invariant trajectory.** The baseline's nadir depends on how often glucose was
  measured (§2.3 Consequence 4, §3.4). A latent-trajectory model estimates the continuous curve and
  its true minimum, which is exactly the quantity the baseline can only approximate.
- **Per-patient insulin sensitivity**, identified from that patient's own glucose response to
  earlier insulin-rate changes before t. This separates "insulin kept acting" from "glucose supply
  fell" *within* a patient rather than across covariate-matched patients.
- **Transfer of information from the dense continuous signal to the rare binary event.** The binary
  endpoint has 26 events; a fitted trajectory model can simulate the probability of crossing
  54 mg/dL under counterfactual insulin rates for every one of the 2,328 events, converting a
  well-measured continuous signal into a calibrated statement about a rare outcome that the
  baseline cannot estimate at all.
- **A falsifiable out-of-sample prediction**: the observed glucose trajectory in held-out hospitals.
  A marginal risk model makes no such prediction.

Where it can fail, and how that is detected: unmeasured IV dextrose boluses and oral intake break
the glucose-appearance term (detect by posterior-predictive misfit concentrated in events with
charted dextrose); S_i is weakly identified when fewer than ~4 glucose values are available
(report identifiability by posterior shrinkage toward the prior and restrict the counterfactual
claims to events with ≥4 values); model misspecification of the insulin-action delay (compare
fixed versus estimated effect-site delay). Full specification, priors, fitting algorithm,
identifiability analysis, evaluation plan and measured/unverified resource estimates are in
`work/branch-method/method-comparison.md`, which is attached as supporting evidence.

### 5.3 Pre-specification and exploratory peeks

The feasibility probes were run **before** this plan was written. They are motivating and power
evidence, not confirmatory results, and the crude arm-level numbers I saw are written down in
`work/diagnostic-evidence.md` with their non-confirmatory status. Because I have seen the crude
arm contrast, the confirmatory quantities are D1–D6 as written, with leave-one-hospital-out
refitting as held-out confirmation. Single look; no repeated peeking.

---

## 6. Falsification criteria

**Supportive of H_iatrogenic (insulin-attributable, preventable component is material):** D1
standardised difference ≤ −10 mg/dL with the 95 % CI excluding −5 mg/dL, **and** D2 slope ≥
2 mg/dL per U/h with CI excluding 0, **and** the effect persisting in the routine/nursing stratum
D4(a), **and** sign stability under leave-one-hospital-out.

**Adverse — H_marker favoured (the fall is mainly the event, not the insulin):** the D1 95 % CI
contained in (−5, +5) mg/dL, **or** the D2 slope CI contained in (−1, +1) mg/dL per U/h, with the
glucose fall in the no-insulin negative-control group of similar magnitude after standardisation
and concentrated in the deterioration stratum D4(c). Under this pattern the correct report is that
post-interruption hypoglycaemia in eICU is largely not insulin-attributable, that an automated
insulin-hold rule has little headroom, and that hypoglycaemia rate is a poor preventability metric.

**Adverse — measurement failure (H_measurement):** the fixed-time endpoint (§3.4 handle 3) disagrees
in sign with the nadir endpoint, **or** the D8 composite and glucose-only risk differences have
opposite signs, **or** D4 strata cannot be assigned for > 50 % of events after both attempted
rebindings. Then no directional claim may be made and the reportable output is the attrition table,
the event counts, the descriptive trajectories, the measured 3:1 excess of rescue orders over
documented glucose < 54, and the explicit statement of which quantity failed. Note that the third of
these conditions is, on the measured numbers (§4 D4), more likely than not to fire; the proposal is
written so that this outcome is still an informative, reportable result about eICU's charting rather
than a failed study.

**Inconclusive:** D1 CI wider than ±15 mg/dL, or D1/D2/D3 disagree, or the leave-one-hospital-out
sign is unstable. Report as inconclusive; do not convert a wide CI into a direction. An imprecise
null does not refute H_iatrogenic.

**Always reported regardless of direction:** the measured 12-h incidence of glucose < 54 mg/dL after
feed interruption on insulin, with its exact numerator and denominator, as the bound on the maximum
preventable burden; and the attrition from 8,920 feed-charting stays to the analysed events.

---

## 7. Method-exploration record (baseline vs alternative)

Full 834-line specification: `work/branch-method/method-comparison.md` (attached). Summary and the
**Lead decisions**, including the two recommendations I did *not* adopt.

### 7.1 The two methods, matched on the same question

| | **Baseline (selected as primary)** | **Alternative (pre-specified secondary)** |
|---|---|---|
| form | IPTW / clone–censor–weight pooled logistic + g-computation standardisation for the continuous ΔG estimand | hierarchical glucose–insulin state-space model: 2 latent states (plasma glucose, insulin effect), patient-specific sensitivity `S_i`, exogenous-appearance input from the charted feed/dextrose rate |
| exact inputs | §2 bindings + §3.4 covariate set, all column-level verified | same event table, plus the full within-event glucose series and insulin-rate series |
| fitting target | E[ΔG] and the dose–response slope; composite 12-h risk | one-step-ahead predictive likelihood of each observed bedside glucose (exact 2-state Kalman likelihood — insulin, feed and dextrose are *observed inputs*, so the model is linear-Gaussian given inputs and needs no particle filter) |
| split | leave-one-hospital-out over the 39 insulin / 53 negative-control hospitals; stay-level cluster bootstrap (1,000) | same LOHO folds; restricted to hospitals with ≥ 300 eligible episodes (measured feed-charting leaders hold 893/832/660/603/490 stays, so ~8–15 folds — must be reported with its audited size) |
| uncertainty / evaluation | bootstrap CIs, SMD and weight-truncation diagnostics, positivity check | CRPS and 50 %/90 % interval coverage of held-out glucose at 1/2/4/8/12 h against a **persistence + linear-slope comparator with calibrated variance**; integrated calibration index for P(nadir<54); posterior-predictive check of the nadir distribution |
| resource budget | **CPU only**, 16 CPUs / 64 GB / UNVERIFIED 1.0–1.5 h wall. Dominated by 1,000 small GLM refits on an ~8 M × 45 float32 matrix: memory-bandwidth and process-parallel bound, not matmul bound; a GPU would idle between tiny fits | **1 GPU** (not 8), ≤ 8 GB device memory, UNVERIFIED 20–40 min, because the parallelism is across ~10⁴ independent 96-step sequences with 10³–10⁴ repeated passes (restarts, empirical-Bayes rounds, τ_X × σ_U sensitivity grid, HMC check) — batched small-tensor work. **CPU-only fallback exists** (per-episode MAP ≈ 2–3 h on 16 CPUs, then a weighted regression of log `S_i` on covariates instead of the EB outer loop), so the GPU buys the full hierarchical fit and the sensitivity grid, not the study's feasibility |
| only measured compute fact | — | `[research job]`: 2 CPUs, 67.5 s, return code 0, full streaming pass over `infusionDrug.csv.gz` (4.80 M rows) **and** `lab.csv.gz` (39.13 M rows). Every other number in this table is explicitly UNVERIFIED projection |

### 7.2 What the alternative could reveal that the baseline loses
(1) a *decomposition*: how much of each episode's fall the insulin-disposal term can account for, episode by episode, rather than inferred from a negative control; (2) an *individualised* counterfactual `δ_i` estimated from that patient's own response to earlier insulin-rate changes (measured median 6 rate-change points per stay), i.e. each patient as their own control — information that "exchangeable given measured L" discards; (3) a *sampling-invariant* latent nadir, which is the exact quantity the baseline's observed nadir only approximates (§3.4); (4) a falsifiable out-of-sample trajectory prediction — the marginal model stakes nothing on trajectory shape and cannot be refuted by it; (5) `S_i` as a reusable physiological phenotype regressable on creatinine, steroid dose and vasopressor, which is how D6 (the seed's renal claim) could become mechanistic rather than an interaction term.

### 7.3 Selection and deferral
**Primary = baseline.** It is the only one of the two carrying a pre-registrable causal estimand with
explicit identification assumptions whose failure modes (weights, SMDs, event counts, negative
controls) a verifier can check without adjudicating physiology.

**Deferred, but run as a pre-specified secondary with its own falsification criteria** (A1–A5 in
`method-comparison.md` §2.9/§3): the state-space model. Deferral reasons: its Bergman-type functional
form has not, to this branch's knowledge, been validated in a multicentre *retrospective* ICU cohort
with q1–2h point-of-care glucose and **order-level rather than administration-level** dextrose; the
measured identifiability margin is thin for a substantial minority (p25 = 2 insulin-rate change
points, p25 = 13 glucose values per infusion span); τ_X and σ_U are fixed by prior, not identified,
so the headline contrast would inherit an untestable choice; and it needs the baseline's positivity
assumption **plus** a structural one.

**Exact evidence that would justify promoting it to primary** (a child proposal to the Lead, not a
compiler repair): (1) LOHO 4-h-ahead CRPS ≥ 10 % better than persistence **and** 90 % interval
coverage inside [0.85, 0.95]; (2) split-half within-stay ICC of log `S_i` ≥ 0.5 with median posterior
SD(log `S_i`) ≤ 0.35; (3) ≥ 80 % of upward glucose excursions > 50 mg/dL per 30 min matched to a
recorded D50/D10/glucagon order within ±60 min; (4) the baseline's estimand proves non-estimable
(persisting SMD > 0.10, or > 1 % of stabilised weights > 20, or truncation moving the estimate by
> 50 % of its magnitude); (5) IPTW effect modification by `δ_i` tertile monotone with interaction
p < 0.01. **Promotion rule: any two of (1)–(3) plus either (4) or (5).**
**Abandon it entirely if** residual lag-1 autocorrelation > 0.2, or split-half ICC < 0.3, or < 50 %
of large upward excursions match a dextrose order, or the sign of its contrast reverses across
τ_X ∈ {15, 30, 60} min or across three σ_U prior scales — each a reportable negative methodological
finding about what this data source can support.

**Joint failure mode, stated in advance.** If insulin titration is near-deterministic given glucose
in a hospital's protocol, positivity fails for the baseline *and* the mechanistic counterfactual
becomes extrapolation beyond any observed input variation. Both then produce confident meaningless
numbers. Detection, required *before* any pooled estimate: the per-hospital distribution of the
fitted deviation hazard and the measured within-stay insulin-rate variation.

**Neural models: considered concretely, not banned.** A time-aware sequence encoder (GRU-D / mTAN
over the irregular glucose–insulin–feed–dextrose–vasopressor–lab sequence; ~0.3 M parameters,
UNVERIFIED 2–4 min per LOHO fold on one A100, ≤ 4 GB) is adopted in **two diagnostic roles**: a
predictive ceiling (if its held-out AUPRC for the composite substantially exceeds the mechanistic
model's, the 6-parameter balance model is leaving real signal on the table and attribution names the
missing mechanism; if it does not, that is positive evidence the structural assumptions are cheap),
and a flexible nuisance model for the censoring/deviation hazard, where interpretability is not
required. It is **not** eligible as the primary because a conditional hazard fitted on observed
behaviour has no interventional semantics for the insulin input: setting insulin to a counterfactual
value and re-predicting would largely reproduce the clinician's policy — the very confounding under
test. A neural ODE with insulin as a control input *does* have an interventional reading but has far
more flexibility than a median of 21 glucose values and 6 rate changes per stay can constrain;
its recommended role is a learned residual on the fixed mechanistic skeleton, promoted only if the
residual checks fire with *structured* rather than random error.

### 7.4 Two method-branch recommendations the Lead did NOT adopt, and why

**(a) Rejected: moving the primary trigger to the union of feed interruption and rapid glucose fall /
insulin-rate decrease, with feed interruption demoted to a subgroup.** The branch recommended this on
measured power (85,084 rate-decrease episodes vs ~2,069 interruption events; ~1,421 vs 26 events at
glucose < 54). I decline, for three reasons that are scientific rather than conservative:
1. **The power objection was specific to the binary endpoint, and I have already answered it another
   way.** §2.3 and §3.2 moved the primary estimand to the continuous ΔG, for which all 2,328 +
   15,854 events contribute a measured trajectory (ΔG SD ≈ 48.5 and 40.7 mg/dL), and §3.2(C)
   quadrupled the binary numerator with the composite outcome (106 insulin-group events). Broadening
   the trigger is not the only remedy, and it is the costly one.
2. **The rate-decrease trigger destroys the identification that makes the question answerable.** A
   feed interruption is timed by gastrointestinal tolerance, procedures and nursing routine — not by
   the glucose value — which is why it admits a *no-insulin negative-control exposure* (D1). An
   insulin-rate decrease is by construction a response to the glucose trajectory: treatment
   assignment is a near-deterministic function of the outcome's own recent history, so confounding by
   indication is maximal, positivity is weakest, and the negative control is undefined (there is no
   "rate decrease" without insulin). Trading a quasi-exogenous shock for a 40× larger endogenous one
   buys precision about a quantity that is not the one in question.
3. **It would silently replace the seed's scientific question.** Expert seed eicu-09 is about feed
   interruption during insulin therapy. Retargeting to any insulin-rate change would be exactly the
   "replace the question with an easier task" move the brief warns against.
*What I did adopt instead:* the rate-decrease cohort is retained as **D9**, a pre-specified bias
probe whose expected direction is known in advance. *Evidence that would reverse this decision:* if
the coverage audit (§2.1) admits hospitals holding ≥ 3,000 feed-interruption events with a
spurious-fire rate < 10 % the primary population simply grows and no union is needed; conversely, if
the D1 standardised contrast has a CI wider than ±15 mg/dL (the §6 inconclusive rule) *and* the
negative control behaves as designed, then a union-trigger child proposal with an explicit
instrumental or protocol-variation strategy for the endogenous trigger becomes the right next
episode — not a compiler repair.

**(b) Adopted with a change of status: the measurement-independent composite outcome.** The branch
proposed it as a robustness check. I measured it in the actual eligible event set
(`[research job]`) and **promoted it to the primary binary endpoint** (§3.2 C) and to
a discriminating test in its own right (**D8**), because rescue orders outnumber documented
glucose < 54 by ~3:1 — which makes ascertainment a substantive finding, not a sensitivity analysis.

**(c) Not developed, recorded for a future episode:** an instrumental-variable / protocol-variation
design exploiting between-hospital differences in response-to-trigger propensity. It attacks the
unmeasured-prognosis problem from a different angle and is the natural next methodological question
if the joint failure mode of §7.3 fires. It requires evidence of strong between-hospital variation in
the response propensity conditional on patient state, partially checkable from the deviation-hazard
model; not checked in this episode.

## 8. Job receipts (all executed by me this episode; CPU only, no GPU requested)

| job | wall s | what it measured | output sha256 |
|---|---|---|---|
| `[research job]` | 141 | insulin in `infusionDrug`/`medication`; `intakeOutput` celllabel inventory; `lab` glucose density and hypoglycaemia counts | `[source checksum]` |
| `[research job]` | 90 | enteral-feed charting audit (stays, hospitals, within-stay interval), insulin overlap, candidate interruption events | `[source checksum]` |
| `[research job]` | 186 | event construction with eligibility; outcome counts; negative-control arm; crude counter-action split (exploratory, see `work/diagnostic-evidence.md`) | `[source checksum]` |
| `[research job]` | 192 | ΔG mean/SD in both groups, insulin-rate quartiles, paired-potassium availability, 120 vs 180 min gap sensitivity | `[source checksum]` |
| `[research job]` | 195 | rescue-order inventory (58,086 stays); composite endpoint counts in the eligible event set; vasopressor and gastric-residual availability for the D4 strata | `[source checksum]` |
| `[research job]` (method branch) | 67.5 | glucose inter-measurement intervals (median 67 min; 77.5 % of 455,323 gaps ≤ 2 h), insulin-rate change points per stay (median 6, p25 = 2), 85,084 rate-decrease episodes in 12,755 stays, continuous-dextrose scarcity in `infusionDrug` | `[source checksum]` |

Scripts: `work/probe_all.py`, `work/probe_feed.py`, `work/probe_power.py`, `work/probe_var.py`,
`work/probe_rescue.py`, `work/branch-method/sampling_probe.py`.
Total measured discovery compute: 872 s CPU across 6 jobs. **No GPU was requested during discovery**
— not as a ban, but because every discovery question was a single streaming pass over compressed CSV
(I/O bound); the solver-stage GPU request and its workload reason are in §7.1.

### 8.1 Bindings that FAILED or are weak, reported rather than worked around

- **Enteral nutrition charting covers only 74/208 hospitals and 8,920/200,859 stays (4.4 %).**
  This is the single largest limitation and it is a property of eICU, not of the design.
- After applying the full eligibility rule the insulin-exposed event set shrinks to **39 hospitals**
  and the negative-control set to **53 hospitals**. Leave-one-hospital-out is therefore a check on
  39 units, not 208.
- **Paired potassium exists for only 432 events**, so D3 is corroborative and underpowered by
  construction. Declared in advance, not discovered later.
- `infusionDrug.drugname` mixes units: 128,016 rows are `Insulin (ml/hr)` and 14,139 are
  `Insulin ()`, where the numeric `drugrate` is not interpretable as units/h without the bag
  concentration. Restricting to units/h-labelled names leaves **6,761 stays** (of 14,312 with any
  insulin infusion). The dose–response (D2) is therefore estimated only on units/h-labelled events;
  ml/h events are kept for the binary "insulin on board" exposure but excluded from D2. This is a
  measured, not assumed, restriction.
- IV dextrose given as a bedside push may be charted inconsistently; under-ascertainment of rescue
  dextrose biases D7 toward the null in a known direction. **Measured bound
  (`[research job]`, and the method branch):** rescue dextrose/glucagon appears as a
  *medication order* in 58,086 stays (`DEXTROSE 50%`, `D50`, `GLUCAGON …`), but continuous dextrose
  infusions are nearly absent from `infusionDrug` (`D5W (ml/hr)` 235 stays, `D10` 106). So the
  composite endpoint of §3.2(C) rests on **order records with `drugstartoffset`, not verified
  administrations**: an ordered-but-not-given dose inflates it, and a push given from a code cart
  without an order is missed. Required reporting, not optional: the fraction of composite events
  contributed by rescue-order-only, and the fraction of upward glucose excursions > 50 mg/dL in
  ≤ 30 min matched to an order within ±60 min (the latter is also failure criterion A4 for the
  mechanistic secondary, §7.3).
- **Gastric-residual volumes are not in `intakeOutput` in this snapshot: 0 of 2,328 insulin-exposed
  events had a residual row** (`[research job]`). The D4(a) "routine/nursing" stratum —
  the primary discriminating stratum — is therefore unbound pending an unverified rebinding to
  `nurseCharting.csv.gz` or `treatment.csv.gz`. A vasopressor infusion in [t−180, t+180] *is*
  bindable and present for 21.9 % of insulin-exposed events, so the deterioration stratum survives.
  This is the most consequential open binding in the proposal and it is stated as such, with its
  pre-committed consequence, rather than assumed away.
- eICU-CRD has no calendar date; no weekday, season or staffing explanation can be tested. A
  previous candidate on this island established by measurement that the reconstructible time-of-day
  field is not hospital-local clock time, so no time-of-day covariate is used here.

## 9. Disposition of the three expert research demonstrations

1. **"Learning the natural history of human disease with generative transformers"** — NOT adopted.
   Missing dependency: that work models disease trajectories over calendar years of registry
   follow-up. eICU-CRD has no calendar time and no post-discharge follow-up; the longest axis here
   is a single ICU stay in offset minutes. A generative trajectory model has no time axis to
   generate along at the relevant scale. Recorded as a dependency limit, not a judgement on the
   method.
2. **"A Bayesian framework for longitudinal EHR and genetic discovery"** — PARTIALLY adapted in
   spirit, not reproduced. Its latent-state-over-time structure is the direct ancestor of the
   hierarchical latent-trajectory model in §5.2: partial pooling across patients and sites, latent
   state observed through sparse irregular measurements. Its genetic component has no analogue —
   eICU has no genotypes — so this is an adaptation with a different scientific target, and is
   labelled as such rather than cited as a reproduction.
3. **"Advancing cancer detection and treatment using longitudinal routine clinical data"** — NOT
   adopted. Missing dependency: no imaging and no oncology longitudinal follow-up in this island.
   The reference README also states the main article text is unavailable (publisher 403/401), so I
   have not inspected its methods and make no claim about them.

## 10. What this study cannot establish

- That hypoglycaemia causes death. Not identifiable here.
- That the hospitals studied are representative: 74/208 hospitals, 4.4 % of stays.
- The true reason a feed was stopped. D4 uses proxies; chart review would be needed, and is not
  available in this snapshot.
- Calendar time, season, weekday and staffing are absent from eICU-CRD, so no temporal or
  workload-based explanation can be tested.
- Dextrose given as an IV push at the bedside may be charted inconsistently; under-ascertainment of
  rescue dextrose biases the counter-act arm toward the null and is stated as a direction-known bias.
- Whether a rescue order was actually administered. The composite endpoint uses order records; this
  requires administration-level data (an eMAR) that eICU-CRD does not contain.
- **Which claims need clinical adjudication rather than computation.** Computationally checkable:
  every count, the attrition table, the weights/SMD/positivity diagnostics, the standardised
  contrasts and their CIs, LOHO sign stability, the trajectory calibration metrics, and every
  pre-committed threshold in §4/§6/§7.3. **Not** computationally checkable, and therefore never to be
  certified by an automatic verifier: whether a given interruption was clinically "routine" rather
  than an early sign of deterioration; whether a rescue order reflects true hypoglycaemia; and
  whether an estimated insulin-attributable decrement is large enough to justify an alert. Those
  require chart adjudication by intensivists or a prospective study.

---

## 11. Scientific deliverable (what must be newly fitted/estimated, and what marks completion)

Newly estimated, none of which exists today: (i) the standardised insulin-attributable component of
the post-interruption glucose decrement, in mg/dL, with a stay-clustered bootstrap CI (D1);
(ii) the dose–response slope of that decrement on the insulin rate left running, mg/dL per U/h, over
units/h-labelled events (D2); (iii) the risk difference for the measurement-independent composite
endpoint, beside the ascertainment-limited glucose-only version (D8); (iv) the audited coverage and
spurious-fire characterisation of feed-interruption ascertainment across 74 hospitals; (v) a fitted
hierarchical glucose–insulin state-space model with per-episode insulin sensitivity, its held-out
trajectory calibration against a persistence comparator, and the pass/fail status of A1–A5.
**Completion is marked by** those five artefacts plus the CONSORT-style attrition table, the LOHO
estimate distribution, and an explicit mapping of the realised pattern onto one of the four labelled
outcomes in §6 — including the adverse and inconclusive ones. A result that fires the §6
measurement-failure rule is a completed deliverable, not a failed one.

## 12. Key references (three inspected works; see `work/branch-lit/key-references.json`)

- **[K1]** NICE-SUGAR Study Investigators; Finfer S, Liu B, Chittock DR, et al. Hypoglycemia and risk
  of death in critically ill patients. *N Engl J Med* 2012;367(12):1108–18.
  doi:10.1056/NEJMoa1204942. **Inspected abstract only** (publisher full text returned HTTP 403).
- **[K2]** Saliba L, Cook CH, Dungan KM, Porter K, Murphy CV. Medication-induced and spontaneous
  hypoglycemia carry the same risk for hospital mortality in critically ill patients. *J Crit Care*
  2016;36:13–17. doi:10.1016/j.jcrc.2016.06.010. **Inspected abstract only** (not open access).
- **[K3]** Vriesendorp TM, van Santen S, DeVries JH, de Jonge E, Rosendaal FR, Schultz MJ, Hoekstra
  JBL. Predisposing factors for hypoglycemia in the intensive care unit. *Crit Care Med*
  2006;34(1):96–101. doi:10.1097/01.CCM.0000194536.89694.06. **Inspected abstract only** (not open
  access).

Frozen Europe PMC provider responses and the labelled excerpts actually inspected are attached, with
SHA-256 of the attached bytes recorded in `key-references.json`. Three citations are a delivery
requirement and are not offered as proof of novelty (§1.3).
