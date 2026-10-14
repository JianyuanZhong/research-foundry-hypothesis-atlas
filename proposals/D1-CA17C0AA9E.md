> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# gen-ep28 child proposal — informativeness-bounded R5 test (eICU 2.0)

Proposed child of true parent `[prior hypothesis]` (episode 27, valid, delivery-complete
leader; seed origin `[starting question]`). Operation: evolve. This child **freezes the parent's
population / exposure / outcome / hour-24 landmark / severity adjustment / within-vs-between
decomposition / E-value rule / LOHO transport unchanged** and adds **one computable output**: a
pre-specified, executed **MDE / informativeness rule** classifying the R5 hospital-stratum test as
informative or inconclusive. Evidence: `work/gen-ep28/probe.md`, `work/gen-ep28/feasibility.md`.

## 1. Unresolved question and what is added

The parent's remaining opening is the anticipation rival **R5** (clinicians stop drawing labs because they
already judge the patient will deteriorate/die), bounded via a hospital-stratified contrast: β_W must
stay clearly negative in the **112 zero-EOL hospitals** where documented-EOL anticipation is structurally
impossible. The parent recorded that **the zero-EOL stratum's informativeness was not asserted**. This
child supplies the missing computable bound: **is that stratum large enough for the R5 falsification test
to be informative?**

- **Already supported (not re-claimed):** lab order presence/timing carry survival signal independent of
  value ([K1] Agniel 2018); documented EOL is hospital-clustered (96/208 hospitals; 112 zero) as the
  parent's probe showed.
- **Unresolved claim this experiment tests:** that the R5 stratum test is **informative** (a null β_W in
  zero-EOL hospitals would genuinely falsify R5), *and* the parent's substantive claim that β_W is an
  unmet-need signal not explained by documented comfort-care transitions.

## 2. Added computable output (EXECUTED this episode)

Source: `work/gen-ep28/probe_fast.py` (shell, 9.4 s) + `work/gen-ep28/probe_lab.py` (managed compute
`[research job]`, 68.6 s, succeeded).

- zero-EOL stratum: **47,901** eligible stays, **112** hospitals, **2,200** escalation events (4.593%).
- Whole eligible cohort: 128,140 stays, 208 hospitals, 6,794 events (5.302%).
- MDE(single standardized logistic coefficient, α=0.05 two-sided, 80% power):
  **zero-EOL MDE OR = 1.063** (naive) → **1.335** (ICC=0.05 design effect) → **1.498** (ICC=0.10);
  whole-cohort MDE OR = 1.036.
- **Verdict: INFORMATIVE** (MDE ≤ parent's targeted OR ≈ 2.0 and even ≤ 1.5 under worst-case clustering).

## 3. Hypothesis vs. the exact data required

- **Leading H1:** β_W < 0 (within-hospital draw-rate drop → later escalation), high within-hospital
  variance share S_W, E-value ≥ 2.0, stable LOHO transport, **and β_W materially unchanged after
  documented-EOL censoring, in both EOL-coding and non-EOL-coding hospitals**.
- **R5 (rival, tested):** the association is EOL anticipation; therefore β_W in **zero-EOL hospitals**
  should be ≈ 0 or materially attenuated. With 47,901 stays / 2,200 events the test can detect OR ≤ 1.5,
  so a clean null there is genuine adverse evidence against R5.
- **Other rivals preserved:** R2 between-hospital fingerprint; R4 reverse ordering (hour-12 placebo
  landmark, washout); residual severity (hour-24 APACHE-IVa + trajectory).

**Supportive / adverse / inconclusive (pre-specified):**
- *Supportive H1:* β_W(zero-EOL) < 0 with CI excluding 0 and E-value ≥ 2.0, and it attenuates toward 0 in
  EOL-coding hospitals after censoring.
- *Adverse to H1 / supportive R5:* β_W(zero-EOL) CI includes 0 while β_W(EOL-coding) is clearly negative.
- *Inconclusive:* CI is wide (would occur only if MDE were ≥ target — **not the executed case**), or
  severity/LODO diagnostics fail, or the draw-drop exposure has near-zero within-hospital variance in the
  zero-EOL stratum (unexecuted here).

## 4. Binding to source (exact tables / columns / keys; eICU 2.0; offsets in MINUTES)

Source root (read-only): `[internal dataset path]`.
Join key everywhere: `patientunitstayid`.

| table | columns used | role |
|---|---|---|
| `patient.csv.gz` | `patientunitstayid, hospitalid, unittype, unitdischargeoffset, unitdischargestatus, hospitaldischargestatus, age` | population, hospital id, landmark, decedent def |
| `carePlanEOL.csv.gz` | `patientunitstayid, cpleolsaveoffset, cpleoldiscussionoffset` | EOL stratum (de-duplicate on stay: 1,433 rows / 1,230 stays) |
| `lab.csv.gz` | `patientunitstayid, labname, labresultoffset` | panel draw-rate exposure |
| `infusionDrug.csv.gz` | `patientunitstayid, infusionoffset, drugname` | escalation proxy (vasoactive) |
| `respiratoryCare.csv.gz` | `patientunitstayid, ventstartoffset` | escalation proxy (ventilation) |
| `apachePatientResult.csv.gz` | `patientunitstayid, apacheversion, predictedicumortality` | severity adjustment |
| `hospital.csv.gz` | `hospitalid, numbedscategory, teachingstatus, region` | hospital covariates |

- **Population:** adult (`age` ≥ 16), `unitdischargeoffset` ≥ 1440, decisive `unitdischargestatus` ∈
  {Alive, Expired} → **128,140** stays / 208 hospitals. Zero-EOL stratum: stays in the 112 hospitals
  with no `carePlanEOL` row → **47,901** stays.
- **Exposure:** within-hospital standardized panel draw-rate drop, using exact labname strings present in
  `lab.csv.gz` (`creatinine, sodium, potassium, chloride, bicarbonate, bun, glucose, calcium`; note
  substring variants `urinary creatinine, urinary sodium, glucose - csf, ionized calcium, bedside
  glucose` to be pre-specified in/out). Distinct draws 0–24 h: 749,154 (cohort) / 269,506 (zero-EOL).
- **Outcome (proxy):** escalation after 24 h = any vasoactive `infusionDrug` start with
  `min(infusionoffset) > 1440` **or** any `ventstartoffset > 1440`. Events: 6,794 cohort / 2,200 zero-EOL.
- **Analysis:** multilevel logistic with hospital random intercept, within-vs-between decomposition
  (β_W, β_B), RCS main effect; E-value (≥ 2.0 target); LOHO transport; pre-specified informativeness gate
  using §2's MDE.

## 5. Honest limits / what remains unexecuted

- **Unexecuted (one line):** the multilevel β_W/β_B fit, E-value, LOHO transport, and the actual
  within-hospital draw-drop variance are **not** computed here — this child adds a power/informativeness
  bound, not a solved result; the discovery probe covers only cohort sizes, EOL distribution, draw counts
  and an escalation proxy.
- EOL is under-coded (documented transitions only, 2.98% of decedents); the escalation outcome is a
  proxy, not adjudicated rescue; ICC used for the clustering bound is **assumed**, not estimated.
- Causal / "unmet need" / policy claims require stewardship/quality-registry data, the randomized
  WICH-ICU result, or expert adjudication — outside the computable experiment.
- **[K1]/[K2]/[K3] are inherited placeholders** bonded to the parent's inspected works
  (Agniel 2018; WICH-ICU 2026 protocol; VanderWeele & Ding 2017) and are not re-litigated here.
