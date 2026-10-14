> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 4 (MIMIC-IV 3.1) — Lead working design, recovery attempt

Markers: **[OBSERVED]** computed in this workspace (script named), **[PRIOR]** measured in an
earlier attempt/episode of this campaign with hash-verified outputs, **[PLANNED]** for the
future solver, **[UNRESOLVED]** open.

## 0. Recovery status

This attempt recovers an interrupted attempt of the same episode (`recovery-checkpoint.json`,
source attempt `[internal run]`). No candidate had been published before the
interruption. I verified the recovered derived files against the checkpoint hashes
(`cohortG.csv` e8b2798f…, `windows.tsv` 7f68be44…, `scanG1.json` 3449fa5b…, `cascade.json`
e2217dbe…) and the frozen source size (10,551,747,784 bytes), so the earlier measurements are
reusable rather than needing a re-scan. The prior Lead's branch structure (L = seed mimic-04,
G = seed mimic-10) is kept; the registered work for this attempt is
`choose_work seq=2`, repair of `[prior hypothesis]` (seed mimic-10).

## 1. The question (branch G, primary)

Seed mimic-10 asserts that residual oxygen requirement / vital-sign fluctuation before ICU
discharge predicts ICU readmission or in-hospital death, and itself cautions: "account for
treatment limitations, discharge destination, and the competing risk of death."

The **strongest claim existing evidence already supports** is the bare association: pre-discharge
physiologic abnormality is associated with ICU readmission and post-ICU death. That is published
many times over and is not an available contribution.

The **unresolved claim** is which process generates it:

- **H_det (deterioration):** residual instability marks impending, *escalatable* physiologic
  deterioration — a triage/monitoring failure that post-ICU surveillance could act on.
- **H_noesc (documented non-escalation + capacity):** residual instability largely marks patients
  in whom a decision not to escalate has already been documented, or who are moved out under bed
  pressure/after hours, so the "events" are expected ward deaths and planned non-returns rather
  than preventable deterioration.

These are not nested nuisance-adjustment variants; they imply different clinical actions. Under
H_det, post-ICU early-warning monitoring and delayed discharge are candidate interventions and
existing readmission scores are measuring something actionable. Under H_noesc, the same scores are
substantially re-identifying goals-of-care documentation, so monitoring-based interventions will
not move the events, and published discrimination statistics for "ICU readmission or death" are
optimistic for the actionable fraction.

### Discriminating predictions
H_det predicts the instability signal concentrates in **ICU readmission followed by escalation**
(reintubation, new vasopressor, new RRT) and survives restriction to documented-full-code, daytime,
low-occupancy discharges. H_noesc predicts the signal concentrates in **in-hospital death without
ICU return** and in hospice disposition, among patients with a limitation documented *before* ICU
discharge, and attenuates strongly in the full-code/low-occupancy stratum.

## 2. Lead's own bounded diagnostic this attempt — the design is separable and the direction is non-trivial

Job `[research job]` (succeeded, 329.8 s, 4 CPU/24 GiB) did one streaming pass over
`mimic-iv-3.1/icu/chartevents.csv.gz` restricted to the 8 h pre-ICU-discharge window of the 87,087
cohort stays, plus all Code Status (223758) rows; `work/lead/poe_codestatus.sh` then extracted the
timed `hosp/poe_detail` "Code status" orders (my first version had a column-index bug — field_name
is column 4, not 3 — which returned 0 rows and is recorded here rather than hidden).
Analysis scripts: `work/lead/leadcheck.py` → `work/lead/out/leadcheck.json`, and the union
computation logged in `work/lead/out/union_goc.txt`.

**[OBSERVED] goals-of-care coverage is far better than the chartevents item alone suggested.**
Union of chartevents 223758 and timed poe code-status orders before ICU discharge covers
**60,438 / 87,087 stays (69.4%)** (last status sourced from chartevents in 32,794 and from poe in
27,644), of which **9,860 stays carry a documented limitation before ICU discharge**. The poe
channel alone covers 41,918 stays; chartevents alone was 44% of all ICU stays [PRIOR].

**[OBSERVED] the outcome mix differs sharply by documented status** (87,087 stays; "readmit72" =
ICU readmission ≤72 h, "death_no_return" = in-hospital death after ICU discharge with no ICU
readmission recorded, "hospice" = discharge location HOSPICE without those events):

| last documented status before ICU discharge | n | readmit ≤72 h | death without ICU return | hospice |
|---|---|---|---|---|
| limitation | 9,860 | 532 (5.4%) | 1,684 (17.1%) | 1,459 (14.8%) |
| full code | 50,578 | 3,411 (6.7%) | 1,051 (2.1%) | 665 (1.3%) |
| undocumented | 26,649 | 1,560 (5.9%) | 299 (1.1%) | 180 (0.7%) |

**[OBSERVED] 2,106 of the 3,977 post-ICU in-hospital deaths (53.0%) occur with no ICU readmission
at all.** The composite endpoint used by the seed and by the published literature therefore merges
two populations with opposite clinical implications.

**[OBSERVED] a crude pre-discharge instability flag separates them further.** Using the late
(−4 h → 0) window only, ≥2 of {HR ≥110 or ≤50; RR ≥24; SpO2 ≤92; FiO2 ≥40%; mean BP ≤60}: 15,926 of
85,477 stays with any late-window vital are "unstable". Cross-classified:
unstable|limitation (n=1,001): 74 readmit72 (7.4%) vs 222 death-without-return (22.2%);
unstable|full-code (n=6,416): 623 readmit72 (9.7%) vs 225 death-without-return (3.5%).
So instability raises readmission within the full-code stratum (6.7%→9.7%) *and* raises
death-without-return much more steeply within the limitation stratum — neither explanation is
trivially correct, which is what makes the test informative. (These are the Lead's crude flags for
feasibility only; the solver's exposure definition is the branch's business.)

**[OBSERVED] the measurement-intensity rival is weak for this exposure.** Median total chartevents
rows in the 8 h window: 265 (unstable) vs 257 (stable). Charting intensity does not explain the
contrast, though it must still be conditioned on.

**[OBSERVED] vital coverage in the late window** (stays): HR 84,489; RR 83,307; SpO2 82,642; NIBP
mean 79,984; arterial BP mean 6,693; FiO2 only 3,385. **FiO2 is sparse**, so the seed's "persistently
high oxygen requirement" axis must be carried by O2 device (226732) and O2 flow (223834) plus SpO2,
not by FiO2 — a binding constraint the published proposal must state.

**[OBSERVED, capacity axis]** 32.9% of cohort discharges are after hours (19:00–07:00) and 39.8%
occur above the unit's median concurrent census [PRIOR, `scanG1.json`].

## 3. What remains unidentified, honestly

- **Informative missingness.** 30.6% of stays have no documented code status before ICU discharge,
  and the undocumented stratum has the *lowest* death-without-return rate (1.1%), consistent with
  documentation being triggered by illness/goals discussion. The decomposition is therefore a
  **bounded** one: the solver must report tipping-point/extreme-case bounds over the undocumented
  stratum, not a point identification.
- **Reverse direction.** A limitation may be documented *because* the patient is unstable and being
  transferred out; conditioning on it is post-treatment relative to the discharge decision for some
  patients. Timing (limitation documented ≥24 h before ICU discharge vs within the discharge window)
  partially separates this and must be reported separately.
- **Severity confounding** and **unobserved ward escalation capability** remain; no observational
  contrast here establishes that delayed ICU discharge would have prevented an event.
- ICD Z66/Z51.5 are hospitalisation-level with no timing (8,880 / 4,265 cohort admissions [PRIOR]);
  they can support but not time a limitation.
- Structured adjudication of goals-of-care language in `note/discharge.csv.gz` is available in the
  snapshot but is a separate NLP study with its own validation burden; named as the main missing
  evidence, not assumed.

## 4. Branch L (secondary, seed mimic-04)

Persistent hyperlactatemia with restored vs non-restored peripheral perfusion, and what follows
clinically. Kept as a complementary branch with a distinct failure mode. Its blocking defect from
the interrupted attempt — the fluid-exposure extraction returned 0 rows while vasopressor extraction
worked [PRIOR, `cascade.json`] — is assigned as a required repair, because the seed's hypothesis is
about *response to fluid*. Novelty boundary passed to the branch: lactate/CRT discordance is
established background (hemodynamic incoherence) and MIMIC-IV lactate-trajectory→mortality is
already published, so only what *follows* inside the discordant phenotype, or a measurement-validity
claim, survives.

## 5. Disposition of the three expert research demonstrations (this attempt)

- **Delphi / generative transformer of disease natural history** — defensible *alternative*, not the
  primary design, for both branches: a next-token/sequence model over pre-discharge ICU events would
  improve prediction of the composite without separating H_det from H_noesc, which is the whole
  question. Structural mismatch also recorded [PRIOR]: MIMIC-IV is admission-level with shifted
  dates, so lifetime ordering is absent. Each branch must cost it explicitly as its learned
  alternative and justify selection or deferral.
- **Oncoformer / longitudinal routine clinical data in cancer** — missing dependency, unchanged: no
  images in this snapshot (radiology *report text* only) and the main text/STAR Methods returned
  403/401 in an earlier episode. Not pursued.
- **ALADYNOULLI / Bayesian longitudinal latent dynamics** — genetic inputs absent, so its genetic
  analysis is blocked; its *stance* (latent continuous-time state with explicit uncertainty) is the
  most defensible learned alternative here: for branch G a latent "discharge-readiness vs
  decision-state" model that generates both the physiologic stream and the discharge/limitation
  decisions; for branch L a latent perfusion/clearance state generating both lactate and charted
  refill.

## 6. Compute facts (measured)

`compute_concurrency=1`, `gpu_slots=2`, `science_seconds=9000`. The chartevents 8 h-window pass over
all 87,087 stays plus all 223758 rows cost **329.8 s on 4 CPUs** [OBSERVED]; the poe_detail+poe pass
ran locally in a few minutes. No GPU was needed in discovery. The solver envelope (16 CPU / 8 GPU /
256 GiB / 28,800 s) is a ceiling, not a target; the baseline analysis for branch G is CPU-only, and
a GPU is only in question for the learned alternative.

## 7. Adapter limitation

This native adapter exposes no `worker_start(role="progress")`, no message channel to a running
worker and no `episode_status`; marginal-progress review was unavailable and was **not** simulated
through Generation or Critique. Lead→worker information after launch is left in files under
`work/lead/`.
