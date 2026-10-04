> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Negative feasibility: the fixed early post-repeat-TACE albumin-down/bilirubin-up signal cannot be tested against a high-specificity 30-day decompensation endpoint in this HCC snapshot

## Clinical question and decision relevance

The parent freezes a leakage-safe, patient-specific early panel after a selected repeat TACE. Its recorded signal is albumin lower than the contemporaneous pre-event value and total bilirubin higher than that pre-event value at the common exact-timestamp panel selected nearest +24 hours in inclusive `[12h,36h]`. That laboratory transition is frequent (86/131 landmark episodes), but it is not itself hepatic failure or a clinical complication.

The clinically consequential unresolved hypothesis was:

> Among the 131 frozen landmark episodes, does the early albumin-down/total-bilirubin-up transition predict a new, temporally later, high-specificity recorded hepatic decompensation or major care-escalation event within 30 days?

If estimable, this question could distinguish a routine post-embolization laboratory pattern from an early warning marker that might justify closer clinical review. The complete-source audit instead shows that the available snapshot contains no qualifying high-specificity recorded decompensation events after the landmark and only one nonspecific critical-care-order match. The hypothesis therefore cannot be estimated or falsified as a prognostic association in these data. This child records that negative endpoint-feasibility result and preserves the laboratory-only parent as the preferable computable experiment.

## Strongest evidence supported, unresolved claim, and exact evidence still required

### Supported by the complete-source audit

Using HCC snapshot `[source checksum]`, the audit read source files without sampling or modification and reproduced the frozen parent:

- 319 systemic-record and 1,491 comparator pathway patients;
- 159 and 526 independently selected repeat-TACE events;
- 34 and 97 fixed early-panel landmark episodes;
- 23/34 and 63/97 early signal-positive episodes, or 86/131 pooled;
- 28,159,928 laboratory rows, 476,846 exact target-assay rows, 476,820 valid uncensored numeric-time rows, seven duplicate assay timestamps, and no discordant duplicate groups.

After follow-up began strictly after each episode's selected early-panel timestamp and all rows from the repeat-TACE encounter were excluded:

- no patient had a distinct later encounter starting within 7 days;
- 11/131 had a distinct later encounter starting within 30 days: 8/86 signal-positive and 3/45 signal-negative;
- 10/11 later encounters were in departments lexically consistent with routine oncology/interventional/chemotherapy/outpatient care, so later encounter occurrence is not a credible escalation endpoint;
- the first later encounter among these 11 occurred at 20.142, 27.087, and 28.158 days at the 25th, 50th, and 75th percentiles;
- 0/131 had any high-specificity diagnosis-family match in a distinct later encounter, whether or not incident-family exclusion was applied;
- 0/131 had a matching high-specificity concept in the later encounter's clinical document;
- 0/131 had artificial-liver/plasma-exchange, dialysis/CRRT, or ventilation order matches; 0/131 had paracentesis/drainage order matches; and 0/131 had terlipressin/somatostatin/octreotide medication matches;
- one patient had a broad critical-care-order lexical match, in the signal-negative group; this isolated unadjudicated order cannot support modeling or establish escalation;
- medication records sometimes used as weak contextual proxies were sparse and nonspecific: hepatic-encephalopathy-directed medication 2/131, albumin 3/131, diuretic 2/131, and selected antibiotic 3/131;
- later total bilirubin was recorded in a distinct encounter for 7/131, and none had a within-assay value at least twice the selected early-panel value;
- 104/131 had some institutional encounter timestamp at least 30 days after the landmark (69/86 signal-positive and 35/45 signal-negative), but this only documents later institutional data presence and cannot prove continuous or outside-hospital outcome capture.

These are endpoint-support and recording-process facts. They do not establish that no clinical decompensation occurred.

### Unsupported and still unresolved

The data do not answer whether the early laboratory transition predicts true post-TACE hepatic decompensation, hepatic failure, emergency readmission, ICU transfer, organ support, death, or a management benefit from intensified monitoring. Zero recorded qualifying events is not evidence of biological safety or a precise clinical null because outcome capture is incomplete and the candidate records lack adjudication.

A valid test of the clinical hypothesis requires, at minimum, native event timestamps and reliable capture for new ascites requiring treatment or drainage, hepatic encephalopathy, variceal hemorrhage, spontaneous bacterial peritonitis, hepatorenal syndrome, clinically diagnosed hepatic failure, emergency or unplanned readmission, ICU transfer, organ support, and death. It also requires distinction of incident from pre-existing decompensation; verification of order execution and medication administration; outside-hospital linkage; laboratory units/reference ranges; and clinician adjudication of temporal attribution to repeat TACE. Preferably it would also include Child-Pugh/MELD components, baseline decompensation state, tumor burden, TACE technique and extent, infection/bleeding, fluids, albumin infusion, transfusion, and systemic-treatment administration.

## Frozen population, event, predictor, and landmark

No population, pathway, event, assay parser, observation selector, or signal definition is changed from `[prior hypothesis]`.

1. Qualify a procedure only when `procedure` contains literal case-insensitive `TACE` or literal `chemoembolization` and `start time` parses. Collapse qualifying rows to the earliest deterministic row per patient-calendar-day. Select the earliest adjacent pair 14–180 calendar days apart; the second is TACE2 and its earliest exact `start time` is `tace2_time`.
2. Preserve the parent's adult HCC, calendar, institutional-observation, systemic-record/comparator medication ontology, and prior-record/placebo/bevacizumab-only/generic-treatment ambiguity exclusions exactly.
3. Independently select the first strict repeat-TACE patient-day on TACE2 days 15–90; its earliest valid procedure start is `event_time` and its `visit number` is `event_encounter`.
4. Preserve the strict laboratory parser, exact-timestamp duplicate rule, `B`, `P`, and leakage-safe intermediate-history clocks. Require both albumin and total bilirubin at `B` and `P` and at one common exact timestamp in `event_encounter` in inclusive `[12h,36h]`; select the timestamp nearest +24 hours, with the earlier timestamp winning a tie.
5. Define `landmark` as that selected panel timestamp, not repeat-TACE time. Define `signal=1` only if selected albumin is strictly below `P` albumin and selected total bilirubin is strictly above `P` bilirubin. Equality is signal-negative.

Reconstruction must reproduce 319/1,491 pathways, 159/526 selected events, 34/97 landmarks, and 23/63 signal-positive episodes before any endpoint audit. Any unexplained mismatch stops interpretation.

## Locked later-outcome audit and temporal safeguards

The fixed horizon is `(landmark, landmark+30 days]`; `(landmark, landmark+7 days]` is descriptive only. A record at or before the patient-specific landmark cannot be an outcome. A record carrying `event_encounter` cannot be an outcome even if its native timestamp is later than the landmark. These rules prevent use of the same peri-procedural episode to define both predictor and outcome and prevent immortal-time assignment from repeat-TACE time to the later selected panel.

A later encounter is a different `visit number` whose start is `admission time`, otherwise `visit time`, otherwise the encounter key's available time, strictly after landmark and no later than 30 days. Later-encounter occurrence is audit-only because scheduled cancer care contaminates it.

The intended high-specificity recorded diagnosis endpoint is a new family-level match on a different later encounter, absent on every exact-key-linked encounter at or before landmark:

- hepatic failure: `hepatic function failure|liver failure|acute hepatic insufficiency`;
- hepatic encephalopathy: `hepatic encephalopathy|hepatic coma`;
- decompensated cirrhosis: `decompensated cirrhosis|cirrhosis decompensation`;
- specific variceal hemorrhage: an esophageal/gastric-variceal phrase with rupture or bleeding, or `variceal rupture and bleeding`;
- spontaneous bacterial peritonitis: `spontaneous` within four characters of `peritonitis`;
- hepatorenal syndrome: `hepatorenal syndrome`.

`Acute liver injury`, generic `liver insufficiency/abnormality`, isolated ascites, and generic gastrointestinal bleeding are excluded from the high-specificity endpoint. The audit deliberately removed `acute liver injury` from the primary hepatic-failure expression because it is not equivalent to clinical hepatic failure. Diagnosis rows have no native date: they inherit only the start of an exact (`patient master index`,`encounter number`) encounter match. Unmatched diagnosis rows are never dated or used.

Clinical-document matches use the same concept families only in a distinct later encounter. They are corroboration, not outcomes, because documents lack native timestamps and lexical matching cannot resolve negation, history, or diagnostic uncertainty.

Major escalation audits use native `Start Time`, otherwise `Order Time`, and require a different encounter plus a time in the locked horizon. They separately search critical-care/ICU/`critical condition`/resuscitation, artificial liver/plasma exchange, CRRT/dialysis, ventilation/intubation, and paracentesis/ascites drainage. Medication audits use native `Start Time` and separately search vasopressin/somatostatin-class bleeding rescue, encephalopathy-directed drugs, albumin, diuretics, and antibiotics. Orders are not proof of execution and medication rows are not proof of administration; broad critical-care phrases and supportive drugs cannot be promoted to a hepatic-decompensation endpoint without record adjudication.

## Exact source bindings and actual filtering

All sources are read-only ordinary CSV files, not archive members. Catalog SHA-256 is `[source checksum]`; HCC snapshot is as stated above. Rows are linked on the composite (`patient master index`,`encounter number`) unless attaching the already frozen patient-level event/landmark map to longitudinal rows.

- `encounters`: `[internal dataset path]`, [source checksum], table `encounters`, schema `[internal dataset path]`. Audit read 105,044 rows. Required columns are `Patient Master Index`,`Encounter Number`,`Age`,`Sex`,`Encounter Time`,`Admission Time`,`Discharge Time`,`Encounter Department`.
- `diagnoses`: `[internal dataset path]`, [source checksum], table `diagnoses`, schema `[internal dataset path]`. Audit read all 1,810,646 rows, retained the 131 landmark patients for matching, and used `Patient Master Index`,`Visit Number`,`Diagnosis Name`,`Diagnosis Type`. There is no native diagnosis time.
- `procedures`: `[internal dataset path]`, [source checksum], table `procedures`, schema `[internal dataset path]`. Use `Patient Master Index`,`Encounter Number`,`Procedure`,`Start Time`,`End Time`,`Procedure Source`; only parsed `Start Time` defines procedure clocks.
- `labs`: `[internal dataset path]`, [source checksum], table `labs`, schema `[internal dataset path]`. Use `Patient Master Index`,`Encounter Number`,`Test`,`Quantitative Result`,`Qualitative Result`,`Specimen Type`,`Test Time`; exact assays are `Albumin`,`Total Bilirubin`. The frozen target-assay frame had 476,813 rows after duplicate resolution, from the 476,820 valid numeric-time source rows.
- `clinical_documents`: `[internal dataset path]`, [source checksum], table `clinical_documents`, schema `[internal dataset path]`. Audit read all 105,044 rows and used `Patient Master Index`,`Encounter Number`,`Chief Complaint`,`History of Present Illness`,`Past Medical History`,`Admission Diagnosis`, the second physical `Admission Diagnosis` column read by pandas as `Admission Diagnosis.1` (catalogued as `Admission Diagnosis__duplicate_2`),`Admission Status`,`Clinical Course`,`Discharge Status`,`Discharge Diagnosis`,`Surgery Name`,`Surgical Procedure`. The source has no document timestamp.
- `orders`: `[internal dataset path]`, [source checksum], table `orders`, schema `[internal dataset path]`. Audit streamed all 16,730,319 rows and used `patient master index`,`encounter number`,`order (non-medication)`,`order time`,`start time`,`end time`,`order status`.
- `medications`: `[internal dataset path]`, [source checksum], table `medications`, schema `[internal dataset path]`. Audit streamed all 4,097,517 rows and used `Patient master index`,`Visit number`,`Medication`,`Start time`,`End time`,`Route of administration`,`Drug type`.
- `transfers`: `[internal dataset path]`, [source checksum], table `transfers`, schema `[internal dataset path]`. Its complete schema contains only `Patient Master Index`,`Encounter Number`; it has no transfer time, origin, destination, unit, or disposition and therefore cannot define ICU transfer or escalation. No outcome rows can legitimately be derived from it.

The implementation and aggregate output are `[internal dataset path]` (executed [source checksum]) and `[internal dataset path]` ([source checksum]). Resource-managed job `[research job]` completed successfully. Only aggregate counts and timing quantiles were written; no identifiers or dates were released.

## Why no prognostic model is valid

The primary endpoint is constant at zero. Logistic regression, time-to-event modeling, discrimination, calibration, risk ratios, arm interactions, and adjusted association estimates are therefore undefined or scientifically meaningless. Combining the one broad critical-order match with supportive medications to manufacture events would violate the high-specificity requirement, create a heterogeneous endpoint, and still leave inadequate support. Treating all 11 later visits as escalation would be especially misleading because 10 were routine-oncology-coded and none occurred within seven days.

The signal and nonsignal groups also differ only weakly in the descriptive presence of any 30-day institutional encounter timestamp (69/86 versus 35/45). This does not repair endpoint absence or establish equal capture. No window widening, same-encounter inclusion, broad-diagnosis substitution, outcome-composite expansion, or follow-up weighting is permitted after seeing these counts.

## Locked interpretation and falsification branches

This audit is governed by the following branches, in order:

1. **Reconstruction failure.** If source hashes/schemas or frozen counts, parser facts, landmark construction, composite joins, or temporal exclusions do not reproduce, stop without an endpoint conclusion.
2. **Endpoint falsified / negative feasibility.** If the high-specificity endpoint has fewer than 10 total events, either signal stratum has fewer than five events, or routine-care contamination exceeds 50% of a proposed encounter-based proxy, do not fit a prognostic model. Conclude only that this snapshot cannot test the hypothesis. The observed result triggers this branch with 0 high-specificity events and 10/11 routine-coded later visits.
3. **Supportive prognostic result, applicable only in a future adequately captured dataset.** If feasibility gates pass, compare the 30-day event risk for signal-positive versus signal-negative episodes with a prespecified pooled model adjusted only for arm, age, sex, TACE2-to-repeat interval, and pre-panel albumin and bilirubin values; use penalized logistic regression and patient bootstrap uncertainty. Support would require a positive adjusted signal coefficient, lower 95% confidence bound above zero on the log-odds scale, and stable direction under an arm-stratified descriptive analysis and a complete-follow-up subset. Such a result would support prognosis for the recorded proxy only, not causation, hepatic-failure adjudication, or monitoring benefit.
4. **Adverse result.** With adequate endpoint support, a confidence interval wholly below zero would indicate that the prespecified early transition predicts fewer recorded events under the locked model; it would challenge the proposed risk-marker direction but not establish protection.
5. **Precise null.** With adequate endpoint support and a prespecified clinically meaningful association margin, an interval entirely inside that null region would rule out that design-sized recorded-event association in the analyzed population, not rule out pathophysiology or effects on unrecorded outcomes.
6. **Inconclusive.** If event support is adequate but uncertainty spans adverse, null, and clinically meaningful positive associations; follow-up capture differs materially by signal; model convergence fails; or record adjudication shows low positive predictive value, report the estimate without a prognostic conclusion.

The current zero-event finding is not a precise-null association result. It is endpoint falsification for this dataset.

## Clinical and verifier boundaries

A verifier can check source identities, complete scans, required columns, frozen cohort/event/panel reconstruction, strict post-landmark and different-encounter conditions, incident-family logic, lexical concept membership, aggregate counts, routine-care contamination, and correct activation of the no-model branch. It can also reject any conclusion that interprets the 11 later visits, two encephalopathy-directed medication records, or one critical-order match as adjudicated decompensation.

An automatic verifier cannot determine whether an absent record means an absent clinical event, resolve negation/history in narrative text, verify that an order was carried out or a medication administered, adjudicate hepatic failure, infer attribution to TACE, establish complete outside follow-up, or justify a clinical monitoring policy. Those require clinical review and additional linked or prospectively collected evidence.

## Substantive advance over the parent and final conclusion

The parent established an observation-aware laboratory forecasting question. This child tested whether that signal could be promoted to a more consequential downstream endpoint without relaxing its safeguards. It could not: the conservative explicit-decompensation endpoint has no events, major escalation proxies are absent or isolated, and nearly every later encounter is compatible with routine cancer care. This is a useful negative result because it prevents outcome broadening and prevents a common post-procedural laboratory direction from being mislabeled as clinically validated hepatic decompensation.

The strongest defensible conclusion is therefore:

> In this frozen 131-episode observed-panel cohort, a high-specificity, temporally distinct 30-day recorded hepatic-decompensation endpoint is not computably supported. The early albumin-down/bilirubin-up signal remains a laboratory-only construct; its relationship to adjudicated decompensation is unresolved, and the existing laboratory-only parent remains preferable for execution on this snapshot.
