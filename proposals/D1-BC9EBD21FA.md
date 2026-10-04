> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 19 method exploration: decision-profile repair

Parent anchor: [prior hypothesis]. This note records the alternative comparison and the substantive repair; it does not report a fitted result.

## Scientific question and deliverable

The decision-relevant descriptive question is whether the last 12 hours before a first ICU discharge identify different early-failure profiles: a later ICU-return-compatible escalation signal versus in-hospital death, while alive discharge is retained as a competing event and the observation/discharge processes are made explicit.

The future solver must newly construct the cohort and exposure ledger, estimate 6/24/48-hour cumulative-incidence risk profiles and bound-aware contrasts, fit two matched models, and return locked test estimates with uncertainty. Completion is established by:
- run_manifest.json with source/catalog hashes, archive members, schema/item checks, temporal rules and software versions;
- cohort_audit.parquet, hourly_features.parquet, support_observation_audit.parquet, and transfer_outcome_audit.parquet;
- risk_profile.parquet containing L/U ICU-return-compatible CIFs, death CIF, alive-discharge CIF, total early-failure burden, and return-minus-death balance for every exposure, horizon, q scenario and topology rule;
- locked baseline and alternative predictions, calibration/IPCW Brier, bootstrap intervals, split stability, and model-comparison files;
- falsification_outputs.parquet and interpretation_map.parquet linking every statement to an output, event count, interval/bound width and evidence limitation.

No discovery or readiness result is a clinical conclusion.

## Binding and population

Use the read-only MIMIC-IV 3.1 ZIP named in datasets/mimic/README.md: [internal dataset path], [source checksum]; catalog [internal dataset path], [source checksum]. Archive members are under mimic-iv-3.1/. The path spelling must be taken literally from the dataset guide at execution time.

Select one earliest valid ICU stay per subject across all admissions, tie-breaking by smallest stay_id. Require patients.anchor_age >= 18, valid subject_id,hadm_id, icustays.intime < icustays.outtime < admissions.dischtime, non-null dischtime, no deathtime <= outtime, and a complete 12-hour window after ICU intime. Retain age 91 as top-coded. Patient-level 70/15/15 train/validation/test splits use fixed seeds 17, 29 and 43.

The landmark is icustays.outtime. Predictors are only in [outtime-12h,outtime): chartevents.charttime for observations; inputevents.starttime,endtime and procedureevents.starttime,endtime for intervals; storetime is never clinical time. Admission context is pre-landmark. Do not use dod, discharge location, post-landmark text, or any outcome field as predictors.

## Mutually exclusive exposure ledger

Create two six-hour halves, [outtime-12h,outtime-6h) and [outtime-6h,outtime). Record each domain/hour as positive, observed non-positive, uninformative absence, contradiction, or invalid. Respiratory positive evidence is O2 flow >2 L/min, FiO2 >0.21, PEEP >0, or corroborating intubation/extubation/NIV procedure evidence. Vasoactive positive evidence is overlap of a listed vasoactive input interval.

For the primary adequately observed subset, define mutually exclusive classes:
1. recorded-off reference: no positive respiratory or vasoactive evidence in either half;
2. respiratory-only recent withdrawal: respiratory positive in the preceding half and not positive in the final half, with no vasoactive withdrawal;
3. vasoactive-only recent cessation: vasoactive positive in the preceding half and not positive in the final half, with no respiratory withdrawal;
4. joint recent withdrawal: both domain withdrawal definitions;
5. other/discordant/persistent-support or inadequate-transition states, retained for audit and secondary descriptive estimates, not silently used as the reference.

A domain withdrawal is not assigned from absence alone. Require at least two respiratory and two MAP observation bins per half for the primary well-observed subset. Verified item IDs, to be checked against icu/d_items, are HR 220045, arterial MAP 220052, NIBP MAP 220181, RR 220210, SpO2 220277, O2 flow 223834, FiO2 223835, PEEP 220339, temperature 223761/223762, vasoactive inputs 221906, 221289/229617, 221662, 221749/229630/229631/229632 and 222315, and procedures 224385, 227194, 225794. These are feature definitions, not claims that a procedure is continuous support.

Observation is part of the design. The primary well-observed estimand is reported separately from the all-eligible estimand. For the latter, apply the locked q sensitivity grid {0,.10,.25,.50,.75,1.00}: only uninformative absence may be recoded as positive, observed non-positive and contradictions are never recoded. Use a fixed hash-based assignment or explicitly seeded multiple imputation and report the full q frontier, not a selected q. Standardize results to all eligible discharges as a descriptive transport estimate; this is not causal missing-data correction. Preserve inadequate, active and discordant strata and report their sizes/positivity.

## Outcomes and decision-profile estimand

Follow [outtime, min(outtime+48h, dischtime)). Each person has one first event: documented-bridge ICU return L, non-bridge ICU return (so L plus non-bridge equals any return U), in-hospital death before return, or alive hospital discharge. Death wins a one-minute tie; a non-discharge event wins a discharge tie; repeat with 0- and 5-minute tolerances.

For a later ICU stay, search all valid hosp/transfers rows with non-null careunit, intime < outtime, start no earlier than index outtime minus five minutes and end no later than later ICU intime plus five minutes. Clip to the index-outtime/later-intime interval; require 30 minutes; require careunit differs from the later stay's first_careunit and last_careunit. Any qualifying row supports L; any later ICU stay supports U. Keep every candidate and audit the 0/5-minute endpoint, 0/15/30/60-minute bridge-duration, careunit-only versus interval, discharge-exclusion and ICU-unit matching variants.

The clinically useful output is a risk profile, not a treatment effect:
- L_g(h) and U_g(h), the lower and upper CIFs of a return-compatible transition;
- D_g(h), death CIF before return;
- A_g(h), alive-discharge CIF;
- B_g(h)=return CIF + D_g(h), total observed early-failure burden;
- S_g(h)=return CIF - D_g(h), the return-versus-death balance relevant to whether a record signal is more rescue/escalation-like or mortality-dominant.

For each exposure contrast, preserve partial identification. If T is the latent return-compatible transition CIF, only L <= T <= U is claimed. Report the compatible interval for a return contrast [L_A-U_B, U_A-L_B], and for the profile balance contrast [(L_A-D_A)-(U_B-D_B), (U_A-D_A)-(L_B-D_B)]. Never report a midpoint as identified. Discharge is a competing event, not censoring; a discharge-censored sensitivity is secondary only.

The prespecified hypothesis is: compared with recorded-off, respiratory-only withdrawal has a larger return-compatible contrast than vasoactive-only withdrawal; vasoactive-only has a larger death contrast than respiratory-only; and joint withdrawal has the largest B. A supportive result requires these directions in the worst-case intervals at 24 and 48 hours and not contradictory at 6 hours, adequate overlap/events, and agreement of baseline and alternative. This supports only retrospective, record-compatible risk stratification. Adverse evidence is reversal, collapse after q/observation adjustment, an association only for U but not L, dependence on one bridge rule/channel, or persistence under transfer permutation. Inconclusive evidence is wide intervals, sparse cells, poor positivity, q/topology direction changes, high latent entropy, or unstable calibration.

## Baseline versus scientifically meaningful alternative

Both methods use the identical ledger, q scenarios, covariates, outcome definitions and patient splits.

Transparent baseline: pooled one-hour cause-specific discrete-time hazards/multinomial risk model for documented-bridge return, non-bridge return, death and alive discharge. Inputs are the four primary exposure classes plus explicitly named other state, final/preceding physiology summaries, support indicators, masks and row counts, admission type/location, age, gender, anchor-year group and ICU LOS, with prespecified domain interactions. Fit on train, select regularization on validation, lock on test. Derive CIFs, L/U, B and S by standardization; report calibration intercept/slope, IPCW Brier, event counts, overlap and subject-bootstrap 95% intervals.

Alternative: an observation-aware factorized two-domain hidden semi-Markov model with respiratory/hemodynamic duration states and constrained persistence/withdrawal transitions, emissions from the same physiology/support ledger, and an observation model for masks, row counts and source channels. Fit latent state/duration/regularization by observed-cause likelihood plus observation-mask likelihood on train, select on validation, and evaluate locked test predictions and latent state/duration summaries. Vary transfer-capture/false-bridge sensitivity and reject any latent transition output outside [L,U]. Its scientific value is to reveal ordered duration and respiratory/hemodynamic discordance that one-hour summary coefficients lose; it does not identify the latent transition as truth.

The baseline is the primary inferential report because it is auditable. The HSMM is selected as a sensitivity/structure-revealing alternative, not because it is more complex or predictive. A flexible GRU/TCN is deferred: it would add sequence capacity without resolving the missing transfer-path semantics. Causal discharge-policy, treatment-limitation, validated intent/readiness, ward-monitoring, waveform/image, external-validation and renal-ground-truth analyses are deferred because the configured data do not provide those dependencies.

## Uncertainty, falsification and limits

Use subject bootstrap intervals, fixed split repetitions/seeds 17/29/43, q and topology frontiers, calibration, IPCW Brier, event counts, overlap, effective sample size and bound width. Run timestamp/leakage audits; within-window time shuffling; storetime negative control; mask/support/physiology/process ablations; procedure removal; channel-specific analyses; +6-hour transfer shift; pre-landmark pseudo-return negative control; discharge-as-censoring sensitivity; first-careunit/admission-type/anchor-year/transfer-density strata; and latent-state stability. Transfer-careunit permutation should erase a true topology-linked signal; persistence under it is adverse.

MIMIC timestamps are deidentified with within-subject intervals preserved and cross-subject calendar alignment invalid. The files contain no validated discharge readiness or clinician intent, treatment limitation, ward monitoring, preventability, exact transfer intent, external cohort, waveform or image evidence. Discharge notes and discharge-detail fields are available only as documentation-availability/audit sources; note text is excluded from validated predictors. Clinical adjudication is required to determine true deterioration, planned versus unplanned return, appropriateness, or actionable monitoring policy. Automatic verification can check data joins, time ordering, computed CIFs/bounds, model outputs, uncertainty and whether conclusions match those outputs; it cannot establish those clinical claims.

## Evidence and compute

The parent’s prior feasibility audit reported 52,591 eligible first outtimes, 2,661 later ICU returns within 48 hours, 2,060 with a qualifying bridge and 601 without; 294 returns had multiple bridge candidates. Those are feasibility/topology facts, not exposure associations, and no new association is claimed here. Demonstration papers were used only as methodological context: the local methods summary supports bounded dated-sequence and latent-trajectory adaptations; the cancer main article/full STAR Methods remain unavailable, and missing images/genetic/external data prevent reproduction claims. The MIMIC-10 residual-instability seed is a motivation, not validation.

Measured: source/catalog/schema availability, parent topology audit, and configured limits. Future solver envelope: 16 CPUs, 262,144 MiB RAM, up to 8 allocated GPUs, 28,800 seconds; this discovery episode allows 7,200 science seconds. Unverified planning estimate: 10–30 minutes streaming extraction, 30–60 minutes baseline/bounds/bootstrap, and 1–4 hours for repeated HSMM/q/topology fits. Use CPU for extraction/baseline; request one A100 only if a bounded profile shows repeated HSMM optimization benefits, using cuda:0 inside the allocation. No discovery estimate is a computed result.
