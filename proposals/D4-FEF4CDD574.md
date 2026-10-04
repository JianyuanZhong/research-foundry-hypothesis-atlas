> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 77: incident biochemical reclassification after a prior reassuring creatinine eGFR

## Decision question and substantive advance

This is a substantive successor to assessed-valid `[prior hypothesis]`. The complete d44 proposal and its directly attached executable ancestry control the inherited population, 2021 race-free equations, baseline-only model fitting, exact AG1 and AF1 scores and rosters, capacity, primary H1/D1 hierarchy, paired inference, source provenance and evidence limits. This child does not refit, rerank, refill, or alter either 466-person roster.

The parent asks whether adding grip rather than bioimpedance whole-body fat-free mass to routine variables plus UACR identifies more equation-defined low filtration at the later assessment visit. A clinically important unresolved temporal question remains:

> Among people who did not have equation-defined combined-eGFR below 60 at recruitment, does the frozen AFG1/AG1 allocation identify more *new* visit-1 combined-eGFR<60 reclassifications than the frozen AF1 allocation at the same 466 assay capacity?

This matters because a person already below the combined threshold at recruitment represents prevalent biochemical discordance, whereas a new visit-1 reclassification is closer to the practical decision to repeat or newly order cystatin C after a previously reassuring creatinine-based assessment. A supportive result would show that the grip increment is not solely selecting people whose low combined eGFR was already present years earlier. An adverse result would falsify that incident-enrichment claim while leaving the parent’s overall H1 question separate. An inconclusive result would identify the need for more closely timed repeated biomarkers.

The advance is temporal qualification of a fixed measurement-choice experiment, not model complexity. Existing evidence inspected in the parent supports association and internal predictability of creatinine–cystatin discordance, prognostic relevance of cystatin reclassification, and the interpretation of field 23101 as an imperfect bioimpedance-derived FFM estimate. It does not establish this AG1-versus-AF1 incident contrast, measured GFR, persistent CKD, mechanism, causality, or patient benefit.

## Evidence boundary and exact data required

Before computation, the strongest available evidence supports only:

- availability of the UKB snapshot and required descriptor columns;
- outcome-blind reconstruction and authentication of d44’s O=134,118, O1=5,823 and O1_hold=2,334 populations;
- baseline-only AF1 fitting and exact immutable AG1/AF1 lists of 466, with 435 overlap and 31 directional swaps;
- availability of paired baseline and visit-1 creatinine/cystatin fields needed to define the temporal phenotype.

No policy-specific incident numerator, yield, interval, or label is evidence currently in hand. The incident endpoint must not be inspected until all source, parent, model, roster, leakage, and hierarchy gates pass.

The required data are participant-level `eid`, sex, ages, baseline and visit-1 creatinine and cystatin C, the frozen parent policies, and the parent’s exact observed/fallback UACR and H1/D1 definitions. The data cannot establish specimen collection order, assay timing relative to the clinical decision, measured GFR, outpatient laboratory trajectory, or adjudicated CKD.

## Frozen inherited population, policies, and chronology

Use the exact d44 population and no other population:

- one canonical positive decimal `eid`;
- d44’s eligibility at the visit-1 assessment: `31-0.0` sex, `21003-1.0` age 40–69, strictly parsed `53-1.0` assessment date `t1`, positive finite `21001-1.0` BMI, at least one positive finite `46-1.0` or `47-1.0` grip, positive finite `30700-1.0` creatinine, race-free 2021 eGFRcr in [60,90), and no position-paired inpatient N17/N18 code/date on or before `t1`;
- exact d44 `O1_hold=O1` hash lock `int(SHA256("ukb-grip-cys-v3|"+eid),16) mod 100 >= 60`;
- exact inherited counts O=134,118, development O=80,516, labeled L=80,470, O1=5,823, O1_hold=2,334 and `n1=floor(0.20*2334)=466`;
- the d44 immutable baseline-trained AG1 and AF1 membership vectors, overlap and directional swaps.

AG1 is the parent A1-plus-UACR-plus-grip rule; AF1 is the parent A1-plus-UACR-plus-one standardized whole-body FFM term. All transforms, coefficients, folds, tie digest, ranks and rosters are inherited byte-for-byte from d44. No baseline or visit-1 outcome, including H0 or H1, may influence policy construction.

The parent AG1:A1 H1/D1 hierarchy and observed-low-UACR complementarity result are mandatory and nonrescuing. The incident qualification cannot relabel, rescue, replace, or erase any parent result. The parent fixed-roster H1 and D1 outputs remain mandatory primary outputs.

## New temporal phenotype

Define baseline `H0` from the parent’s same 2021 race-free combined creatinine–cystatin equation using recruitment-instance values: sex `31-0.0`, recruitment age `21022-0.0`, serum creatinine `30700-0.0` and cystatin C `30720-0.0`. Define visit-1 `H1` exactly as d44 defines it, using its locked `31-0.0`, `21003-1.0`, `30700-1.0` and `30720-1.0` inputs and equation constants. Do not use an eGFR equation from a different year, round intermediate values, or apply a global negative-code rule.

For each O1_hold participant, define:

`Hnew = 1` iff `H0=0` and `H1=1`.

If either equation-required cystatin value is invalid or missing, the corresponding H label is missing. A missing `H0` or `H1` is not a negative label and is not imputed. The incident endpoint is equation-defined new reclassification, not incident CKD and not a measured decline in GFR. Participants with H0=1 are excluded from the incident numerator but remain in the fixed O1_hold denominator, preventing post-selection denominator shrinkage.

The exact visit-1 D1 discordance label remains a mandatory parent output. A secondary, nonrescuing descriptive diagnostic may report `Dnew=I(H0=0 and D1=1)`; it is not part of the primary incident hypothesis unless the compiler shows adequate event and missing-label support before outcome analysis. This keeps the new claim focused and avoids multiplying sparse temporal endpoints.

## Estimands, analysis, and uncertainty

For frozen policy set `S_p`, p in {AG1, AF1}, define:

`Y_new(p)=1000 * sum_{i in S_p} Hnew_i / 466`

and

`Delta_new=Y_new(AG1)-Y_new(AF1)`.

The one-net-event resolution margin is `m=1000/466=2.145922746781116` per 1,000 slots. Report each policy numerator, observed Hnew count, missing count, yield, overlap and directional-swap counts, and verify the symmetric-difference identity whenever both swap means are defined. Keep the denominator exactly 466 even when H0 is prevalent or missing.

Use d44’s exact participant-level 2,000-draw paired bootstrap: canonical-eid-sorted O1_hold, PCG64DXSM, the frozen `ukb-grip-visit1-bootstrap-v1|b` seed namespace, shared participant multiplicities, both immutable rosters, and fixed denominator. Never refit or rerank. For missing Hnew, use one shared latent binary value per eid and report sharp lower/upper contrasts using the d44 signed policy-membership bounds. The incident family is exactly `F77_incident={Delta_new}`; it must not silently replace d44’s `F33_AF={Q_H,Q_D}` family. Report point estimate, SE, two-sided 95% interval, conservative one-sided limits, finite-draw count, variance and all hashes.

## Gates and exhaustive result labels

Before any supportive or adverse label, require all d44 provenance, population, source-agreement, parent-hierarchy, leakage, model, roster and denominator gates, plus:

- exact baseline and visit-1 equation reconstruction with no intermediate rounding;
- baseline/visit-1 label vectors reproducible in two independent runs;
- no participant with an invalid required input silently assigned H0=0 or H1=0;
- fewer than 1% missing Hnew labels in O1_hold, with missingness patterns and shared-person bounds reported;
- at least 20 observed Hnew labels in O1_hold, at least 10 in AG1 union AF1, at least 3 in each policy list, and at least 4 across the 62-person directional symmetric difference;
- at least 95% finite paired-bootstrap draws and positive finite variance;
- exact fixed-denominator and policy/swap decomposition identities.

If any gate fails, emit `incident_reclassification_inconclusive`. Do not interpret sparse or missing incident labels as adverse.

Emit exactly one new qualification label:

- `incident_reclassification_supportive` only if all gates pass, the sharp lower `Delta_new >= m`, and its conservative one-sided 95% lower limit is strictly above 0;
- `incident_reclassification_adverse` only if all gates pass, the sharp upper `Delta_new <= m`, and its conservative one-sided 95% upper limit is strictly below m;
- `incident_reclassification_inconclusive` otherwise, including uncertainty crossing a boundary, equality at a strict support boundary, nonpositive variance, sparse labels, excess missingness, or any integrity failure.

Support means enrichment of the recorded equation-defined Hnew phenotype under these fixed rosters. Adverse falsifies the prespecified one-net-new-reclassification advantage at this quota; it does not prove AF1 superiority, equivalence, accurate GFR, or clinical harm.

## Joint interpretation and falsification

Always report the inherited d44 H1/D1 and parent hierarchy labels first, then the new incident label.

- Parent supportive plus incident supportive: the grip increment is supported both for overall visit-1 H1 yield and for H1 appearing after a non-low baseline H0; this strengthens, but does not prove, a repeat-testing rationale.
- Parent supportive plus incident adverse: overall enrichment is not reproduced for new reclassification; the apparent advantage may mainly reflect prevalent biochemical discordance.
- Parent supportive plus incident inconclusive: the incident clinical question remains unresolved; do not use the overall result as a temporal substitute.
- Parent adverse or inconclusive: the incident result cannot rescue the parent and the synthesis remains parent-not-supported; report it as a nonrescuing qualification.
- Incident supportive while the parent H1/D1 hierarchy is adverse or inconclusive is never a favorable overall conclusion.

A broad nonrenal diagnosis-record control and the inherited d44-specificity limits remain nonrescuing. This child does not claim that a new equation-defined H1 is a new disease, a persistent CKD state, or a treatment opportunity. In particular, neither H0/H1 change nor an inpatient N18 record establishes CKD progression.

## Exact UKB source bindings

Use only the current catalog `[internal dataset path]`, catalog [source checksum], and UKB snapshot `[source checksum]`. All members are ordinary files; no archive member exists. Join horizontally one-to-one on canonical `eid`; reject duplicates and disagreements.

| table | read-only source and schema | required fields |
|---|---|---|
| population | `[internal dataset path]`; descriptor `datasets/ukb/table-38565c9e35e7cb6c.json`; schema SHA `[source checksum]` | key `eid`; `31-0.0`, `21022-0.0` |
| assessment | `[internal dataset path]`; descriptor `datasets/ukb/table-901ef6c7ddce2d51.json`; schema SHA `[source checksum]` | key `eid`; `53-0.0`, `53-1.0`, `21003-1.0`, `21001-1.0`, `46-1.0`, `47-1.0`; parent duplicate `23101-0.0/1.0` audit |
| main | `[internal dataset path]`; descriptor `datasets/ukb/table-e4a9e4d8baa71a9d.json`; schema SHA `[source checksum]` | key `eid`; `30700-0.0`, `30720-0.0`, `30700-1.0`, `30720-1.0`, parent `23101-0.0/1.0`, UACR and inherited predictor fields |
| biological_samples | `[internal dataset path]`; descriptor `datasets/ukb/table-c6b666d905f3b02f.json`; schema SHA `[source checksum]` | key `eid`; inherited duplicate audit `30700/30720` at 0 and 1; `30515-1.0` is absent and forbidden |
| health_outcomes | `[internal dataset path]`; descriptor `datasets/ukb/table-3cfae45e0905b0e3.json`; schema SHA `[source checksum]` | key `eid`; inherited eligibility N17/N18 paired fields only; no health outcome is used to define H0/H1/Hnew |

The descriptor JSON file hashes controlling the local catalog are inherited from d44: population `[source checksum]`, assessment `[source checksum]`, main `[source checksum]`, biological_samples `[source checksum]`, and health_outcomes `[source checksum]`. These file hashes are distinct from internal schema hashes.

No source is writable. Do not use instance indices as elapsed time, unpaired diagnosis dates, `40001`, `40002`, or any source outside the frozen d44 bindings. HCC, MIMIC-IV (including notes), and eICU remain directly accessible read-only in this workspace, but have no UKB `eid` linkage and are not mixed into this UKB experiment.

## Reproducibility and verification contract

Direct parent `[prior hypothesis]` must be materialized under its exact namespace and its proposal/support hashes authenticated before any participant-specific H0/H1 or policy outcome is opened. The current catalog and all five source/header/schema identities must be checked. The new temporal-label code and incident vector must be run twice independently; exact event vectors, counts, missingness, bootstrap outputs and result labels must agree. Any mismatch is `incident_reclassification_inconclusive`, not an invitation to refit or redefine H0.

The verifier can check source identity, required-column presence, one-to-one joins, population/hash reconstruction, inherited models and rosters, equation arithmetic, label validity, Hnew logic, fixed denominators, shared missing-label bounds, paired bootstrap, gates, exhaustive labels, and output-linked conclusions. It must reject correct arithmetic paired with claims of incident or persistent CKD, measured GFR, muscle/sarcopenia mechanism, causal benefit, routine adoption, safety, cost-effectiveness, fairness or transportability. It must test supportive, adverse and inconclusive fixtures, including H0 missing, H1 missing, H0=1, a valid H0=0/H1=1 transition, sparse swap events, and correct arithmetic followed by unsupported clinical claims.

Automatic verification cannot establish exact specimen/order/result chronology, complete biomarker capture, measured GFR, persistent or adjudicated CKD, a causal treatment effect, patient benefit, workflow burden, cost, safety, equity or transportability. Those require repeated clinically timed biomarkers, measured GFR, outpatient and kidney-replacement/censoring linkage, chart/nephrologist adjudication, workflow/harms/cost/equity review, external validation and a prospective comparative testing-strategy study.

## Direct parent and selection rationale

Parent exactly: `[prior hypothesis]`. This child is not a compiler repair and does not modify d44’s scientific definitions. It adds one outcome-blind, temporally motivated endpoint whose required baseline and visit-1 fields are present in the catalog. The child is publishable only because it preserves the parent’s complete executable closure and makes all incident-specific formulas, gates, labels, verifier fixtures and evidence limits explicit.
