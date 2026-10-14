> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal (Lead) — MIMIC-IV island, episode 28 (evolution)

Parent: `[prior hypothesis]` (board top, valid, refs complete). Operation: evolve.
Origin: expert seed `[starting question]` (acute glucose elevation relative to chronic glycemia).
Status: design frozen; NO cohort rows modelled in discovery this episode. No clinical truth claimed.

## 1. Unresolved question
At the same absolute admission glucose and illness severity, does the RELATIVE (acute-on-chronic)
glycemia component add incremental 28-day-mortality information — and is any increment separable
from the fact that HbA1c is drawn in a SELECTED subgroup of admissions? [K1] reports SHR is
prognostic in MIMIC-IV pneumonia, but analyses only patients who already have an HbA1c and does not
model the measurement process. [K3] shows competing HbA1c-derived indices target the same outcome.
[K2] shows glucose–mortality signal is population-specific, so it must be re-established here.

## 2. Why it matters
If the relative component carries no information beyond absolute glucose and severity, clinicians
should not defer to "relative hyperglycemia" triage. If its apparent value disappears once the
HbA1c-measurement process is modelled, the SHR signal is partly a selection artifact — changing how
these markers are used and reported.

## 3. Strongest rival
Measurement/selection artifact: sicker or more-monitored patients are likelier to have HbA1c drawn;
the derived chronic baseline is therefore informative-of-severity rather than a genuine trait.

## 4. Data bindings (verified this episode against the frozen archive)
Source: `[internal dataset path]`
([source checksum]; 34 members).
Members: `mimic-iv-3.1/hosp/labevents.csv.gz` (2,592,909,134 B uncompressed),
`hosp/admissions.csv.gz`, `hosp/patients.csv.gz`, `icu/icustays.csv.gz`, `hosp/d_labitems.csv.gz`, `icu/d_items.csv.gz`.
CORRECT reader (ep-26/27 defect): inner members are gzip streams inside the zip →
`gzip.GzipFile(fileobj=zip.open(member))`, NOT `pd.read_csv(zip.open(member))`.
Keys: `subject_id` / `hadm_id` / `stay_id`.
Itemids to CONFIRM in `hosp/d_labitems.csv.gz`: glucose 50931/50809/52027/52569; HbA1c 50852/50854.
Outcome: 28-day death from `hosp/patients.dod` vs `hosp/admissions.dischtime`.

## 5. Design
Population: first ICU stay per `subject_id` with sepsis; admission `[t0, t0+24h]` glucose window.
Exposure: G_adm (absolute admission glucose), Gc (chronic level from HbA1c), log-ratio term.
Models: M0 = severity + G_adm; M1 = M0 + relative term; M2 = M1 + HbA1c-measurement-process
(selection-aware alternative). Negative control: availability-only indicator (no value).
Supportive: ΔAUROC(M1 vs M0) ≥ 0.02 with 95% CI excluding 0 AND M2-vs-M1 not fully attenuated.
Adverse: ΔAUROC(M1 vs M0) ≤ 0.005 within ±0.01 equivalence margin, or attenuation under M2.
Inconclusive: cohort/power gate fails; CI spans margin. Permutation control for AUROC.
Split: single locked temporal 70/30 by `icustays.intime`.

## 6. Power/cohort gate (NOT computed this episode — honest limit)
The real cohort/HbA1c-measured-fraction/death counts are NOT established. Prior episodes produced a
defective zero-count join (ep-26) and a cancelled recompute (ep-27). This is the branch's single
biggest blocking uncertainty and is the delegated deliverable for this episode.

## 7. Key references
[K1] Chen 2026 SHR/GI vs absolute glucose, MIMIC-IV pneumonia (abstract+intro excerpt). [K2] Yang 2026
glucose trajectories in ICH (abstract excerpt). [K3] Zhang 2026 HGI in sepsis with external
validation (METADATA ONLY — abstract/full text not read). See `work/key-references.json`.

## 8. Limits
Single-centre retrospective; no causal claim; HbA1c validity under anemia/transfusion not adjudicated;
K3 inspection severely limited; power unresolved.
