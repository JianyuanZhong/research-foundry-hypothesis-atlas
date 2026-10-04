# Episode 67 repaired protocol audit

This targeted child preserves [prior hypothesis]'s frozen scientific schema: the first-eligible adult, one-admission-per-subject MIMIC pulmonary-opportunity population; pre-discharge chronology and canonical DS; exact atom `g=(E, terminal curr_service, W)`; route-concealed component panels; all-unit adverse precedence; finite-population two-phase whole-admission estimand; and the noncausal conclusion ceiling. MIMIC text can support only a stored-text measurement and, if all gates pass, nomination of a separately governed prospective silent workflow bridge. It cannot establish actual workflow, clinical truth, appropriateness, responsibility, safety, benefit, or causality.

## Audit and repair

The repaired protocol now has one explicit target-freeze state machine. It builds and seals the frame/support atlas and outcome-blind phase-1 master first; selects exactly the first fixed-order eligible target or `NO_SELECTION` using only frame/support inputs and a conservative worst-case certificate over later phase-1 band partitions; then exposes and seals phase-1 labels; forms `d=(h,z)` and target/non-target `e` strata; exhaustively solves and seals allocation, probabilities, roster, and ledger; and only then exposes phase-2 packets. A label-permutation invariant is required. Thus phase-1 labels cannot select, enrich, or replace the target.

The additive ledger is explicit: `T = T_micro + T_floor + T_target_extra + T_non_target_extra + T_control_only`, with each distinct whole admission counted once. Every micro-census and occupied target/non-target floor counts within the same 120--300 admission bounds. Controls on sampled admissions do not duplicate admissions; any control-only admissions are included with positive probability. Fixed controls are charged once, and reserve is charged once as `ceil(0.15*(phase2_reading_minutes+fixed_controls_minutes))`; the charged total must remain within 84,000 minutes as well as reviewer, weekly, roster, and 32-week limits.

The probability language distinguishes conditional and unconditional quantities. `q_i` and `q_ij` are conditional on the realized phase-1 sample and sealed bands. `pi1_i`/`pi1_ij` are first-stage probabilities, and `1/(pi1_i*q_i)` is the sequential realized-path weight. Products involving conditional `q` are not called marginal unconditional pair probabilities; an unconditional quantity must integrate over the nested first-stage mechanism. Zero pair inclusion is defined, but any estimator requiring a positive pair probability fails closed. The fixture enumerates nested paths, checks probability normalization, HT total and denominator unbiasedness, exact positive finite design variance, and deterministic 20,000-replicate resampling diagnostics.

The protocol binds the exact MIMIC snapshot and archive, all five archive members used for structured data, the four ordinary note files, schema artifacts, columns, joins, and time fields. The source catalog was inspected. In particular, `hosp/transfers` is bound with its actual schema (`transfer_id,eventtype,careunit,intime,outtime`), `icu/icustays` includes `stay_id,first_careunit,last_careunit,los`, and both detail tables bind `note_id,subject_id,field_name,field_value,field_ordinal`. The protocol retains explicit unavailable evidence: actual departure, report viewing/acknowledgement, named responsibility, preference, outside plans, orders/referrals/scheduling, completed imaging, images, burden, safety, benefit, and causal outcomes.

## Result interpretation

Supportive results mean only that the fixed stored-text construct passes its simultaneous precision, event/ESS, positive-probability, shared-error, and workload gates and may be considered for a separately approved silent bridge with operational outputs suppressed or `DEFER`. Adverse results include an adverse-compatible target unit or route failure and exclude that exact cell from bridge priority; they cannot be converted to `RECON` or used to seek a more favorable cell. Inconclusive results include `NO_SELECTION`, sparse or undefined uncertainty, failed calibration/roster/workload, nonresponse, or invalid sealing; they map to `DEFER` and require additional data or design, not a safety or correctness claim.

## Verification

Executed files:

- `episode67_allocation_variance_fixture.py` passed and reproduced `episode67_fixture_expected.json`, including selected vector, additive admission components, charged fixed-control/reserve ledger, target-freeze invariant, and fail-closed zero-pair probe.
- `episode67_nested_sampling_fixture.py` passed with 64 complete nested paths, path mass 1, HT expectation 3 equal to the finite-population total, denominator expectation 7, finite positive exact variance 7.416666666666666, and 20,000 finite positive resampling variance diagnostics.

The nested fixture is a computational mechanics certificate, not MIMIC evidence. Clinical adjudication, actual workflow, and downstream safety/benefit remain outside automatic verification.
