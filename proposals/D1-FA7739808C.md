> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Context-Dependent Lactate Clearance in Sepsis: A MIMIC-IV Cohort Study

**Seed / lineage.** Expert seed `[starting question]` ("Different meanings of persistent hyperlactatemia"), parent candidate `[prior hypothesis]` (valid expert-seed import; no data bindings, outcomes or analysis specified). This proposal is a full, data-bound development of that seed.

**Dataset.** MIMIC-IV 3.1, archive `mimic-iv-3.1.zip` at `[internal dataset path]` ([source checksum]), archive root `mimic-iv-3.1/`. Source data is read-only; all derived files live under `work/`.

**Status.** Complete experiment specification with measured feasibility anchors (all probe counts below were computed on this snapshot in this episode; see `work/probes/`). No scientific result has been computed yet; the analysis plan is prespecified and falsifiable.

---

## 1. Scientific question, why it matters, and rival explanations

**Question.** In adult ICU patients with sepsis or septic shock who are receiving vasopressors, does a >=30% fall in serum lactate over 2-12 hours ("lactate clearance") identify patients at lower risk of in-hospital death and new vasopressor escalation than patients with persistent hyperlactatemia (lactate remaining >=70% of baseline), after severity adjustment?

**Why this matters.** Lactate clearance is a widely used resuscitation target in sepsis guidelines (Surviving Sepsis Campaign). However, lactate is not specific to hypoperfusion: it can be elevated by hepatic dysfunction, thiamine deficiency, beta-agonist use, or tumor metabolism. Weinberger et al. [K1] note that "hyperlactatemia does not always reflect fluid-responsive hypoperfusion" and that "titrating resuscitation to lactate clearance can also lead to unnecessary fluid and volume overload." Kataria et al. [K2] showed that hyperlactatemia in a hypoperfusion context vs non-hypoperfusion context had similar 28-day mortality (24% vs 15%, P=0.234), suggesting that the prognostic value of lactate depends on the underlying pathophysiology. The unresolved question is whether lactate clearance (a dynamic measure, not just a single level) has different prognostic value depending on whether the patient is in a perfusion-compromised state (vasopressor-dependent) vs a non-perfusion state. If lactate clearance only predicts mortality in vasopressor-dependent patients, this would support a context-dependent interpretation of lactate trends and argue against using lactate clearance as a universal resuscitation target.

**Rival explanations.**
- R1 (severity confounding): Patients with persistent lactate may simply be sicker (higher APACHE/SOFA), and the mortality difference is entirely explained by baseline severity. Design feature: unadjusted vs severity-adjusted logistic regression; the gap between unadjusted and adjusted ORs is the readout.
- R2 (lactate as a marker of hepatic dysfunction): In non-vasopressor patients, persistent lactate may reflect impaired hepatic clearance rather than hypoperfusion, and the mortality difference may be driven by liver failure rather than sepsis severity. Design feature: the primary analysis is restricted to vasopressor-dependent patients (perfusion context); a secondary analysis in non-vasopressor patients tests whether the effect disappears.
- R3 (immortal time bias): Patients who survive long enough to have a second lactate measured may differ from those who die before the second measurement. Design feature: the analysis is conditional on having both lactate measurements (t1 and t2); this is a selection bias that is acknowledged but not eliminated.

## 2. Population and data bindings

**Inclusion criteria** (all measured this episode):
1. Adult (anchor_age >= 18) ICU stay in MIMIC-IV 3.1.
2. Sepsis or septic shock diagnosis: ICD-10 code in {A419, A4159, A4151, A4152, A4153, A4154, A4155, A4156, A4157, A4158, A410, A418, A4191, A4192, R6520, R6521, R6510, R650, R658, R651, R652, A4181, A4189, A4190} in `hosp/diagnoses_icd.csv.gz` (icd_code, icd_version=10).
3. At least one vasopressor infusion in `icu/inputevents.csv.gz` (itemid in {221289, 221662, 221749, 221906, 222315, 229617, 229630, 229631, 229632, 229770, 229764}) within 24 hours before t1.
4. At least two serum lactate measurements (itemid 50813 in `hosp/labevents.csv.gz`, valuenum IS NOT NULL) with a gap of 2-12 hours, where the first measurement (t1) has lactate >= 4.0 mmol/L.

**Measured feasibility anchors** (computed this episode, probes p4-p28):
- Sepsis/shock ICD-10 admissions with ICU stay: 7,951 (p4).
- Adult sepsis ICU stays: 7,951 (p7; all sepsis stays are adult in this snapshot).
- Sepsis stays with >=1 lactate: 7,425 (p5).
- Sepsis stays with >=1 vasopressor: 4,433 (p5).
- Sepsis stays with both lactate and vasopressor: 4,264 (p5).
- Sepsis stays with a valid lactate pair (gap 2-12h, l1>=4): 5,906 (p8).
- Cohort (sepsis + adult + vasopressor within 24h of t1 + valid pair): 334 hadm_id (p23, p28).
- In-hospital death in cohort: persistent 172/238 (72.3%), cleared 46/96 (47.9%) (p28).
- New vasopressor agent escalation (2-72h after t2): persistent 56/245 (22.9%), cleared 17/89 (19.1%) (p27).

**Note on hadm_id vs stay_id.** The cohort is defined at the hadm_id level. Some hadm_id values appear in multiple icustays (transfers between ICUs within the same admission). The analysis uses the first ICU stay per hadm_id (by icustays.intime) to avoid double-counting.

**Exclusion criteria:**
- Lactate t1 < 4.0 mmol/L (not hyperlactatemic).
- Gap between t1 and t2 < 2 hours or > 12 hours.
- No vasopressor within 24 hours before t1 (non-perfusion context; secondary analysis).
- anchor_age < 18.

## 3. Phenotype definition

**Lactate clearance (cleared group):** l2 <= 0.7 * l1 (>=30% fall from t1 to t2).
**Persistent hyperlactatemia (persistent group):** l2 > 0.7 * l1 (less than 30% fall).

Where l1 = first lactate value (>=4.0) and l2 = second lactate value (2-12h later).

**Perfusion context (primary):** Vasopressor infusion (any of the 11 itemids) within 24 hours before t1.
**Non-perfusion context (secondary):** No vasopressor within 24 hours before t1.

## 4. Outcomes

**Primary outcome:** In-hospital death (`hosp/admissions.csv.gz`, deathtime IS NOT NULL).
**Secondary outcome 1:** New vasopressor agent escalation within 72 hours after t2 (a vasopressor itemid not used in the 24h before t1 through t2+2h, started in the window t2+2h to t2+72h).
**Secondary outcome 2:** In-ICU mortality (icustays.outtime < deathtime, or deathtime within ICU stay).

## 5. Analysis plan

**Primary analysis (perfusion context, n=334):**
1. Baseline table: age, gender, APACHE II proxy (computed from available variables), lactate t1, lactate t2, gap (t2-t1), number of vasopressor agents, ICU LOS, hospital LOS.
2. Unadjusted comparison: in-hospital death rate and new vasopressor escalation rate in cleared vs persistent groups, with 95% CIs (Wald).
3. Adjusted logistic regression: outcome ~ group + age + gender + lactate_t1 + gap + n_vasopressor_agents + icu_los. Report adjusted OR with 95% CI.
4. Unadjusted-vs-adjusted gap: the difference between the unadjusted and adjusted ORs, interpreted as the extent of severity confounding.

**Secondary analyses:**
- S1: Non-perfusion context (no vasopressor within 24h of t1): same analysis, testing whether the effect disappears.
- S2: Lactate threshold sensitivity: l1 >= 2.0 instead of 4.0.
- S3: Gap window sensitivity: 4-8h instead of 2-12h.
- S4: Clearance threshold sensitivity: l2 <= 0.5*l1 (>=50% fall) instead of 0.7*l1.
- S5: In-ICU mortality instead of in-hospital death.

**Falsification criteria:**
- F1: If the adjusted OR for death in the persistent group is < 1.0 (95% CI excludes 1.0), the hypothesis is falsified (persistent lactate is protective, not harmful).
- F2: If the adjusted OR for death in the persistent group is between 0.8 and 1.2 (95% CI includes 1.0), the result is inconclusive.
- F3: If the unadjusted OR is > 1.5 but the adjusted OR is < 1.2, the effect is explained by severity confounding (R1).
- F4: If the effect is present in the perfusion context (S0) but absent in the non-perfusion context (S1), this supports the context-dependent interpretation.

**Supportive result:** Adjusted OR for death in the persistent group > 1.5 (95% CI excludes 1.0), with a smaller but still significant effect in the non-perfusion context (S1) or no effect in S1.
**Adverse result:** Adjusted OR < 1.0 (F1) or the effect is entirely explained by severity confounding (F3).
**Inconclusive result:** Adjusted OR between 0.8 and 1.2 (F2), or the cohort is too small to detect a clinically meaningful difference.

## 6. Method alternatives record

**Baseline (unadjusted comparison):** Simple rate comparison with 95% CIs. This is the minimum analysis; it does not adjust for confounding.
**Learned/mechanistic alternative (adjusted logistic regression):** Adjusts for age, gender, lactate_t1, gap, n_vasopressor_agents, icu_los. This is the primary analysis. The adjusted model can reveal whether the unadjusted association is driven by severity confounding (R1).
**Deferred alternatives:**
- Machine learning (random forest, gradient boosting): Deferred because the cohort is small (n=334) and the primary question is a causal/prognostic comparison, not a prediction task. ML would add complexity without addressing the scientific question.
- Fine-Gray subdistribution hazard model: Deferred because the primary outcome is in-hospital death (binary), not a time-to-event with competing risks.
- Propensity score matching: Deferred because the cohort is small and the groups are not well-balanced (238 vs 96). Logistic regression with covariate adjustment is more efficient at this sample size.

## 7. Resource and time budget

**Discovery (this episode):** CPU-only, 8 CPUs, 24 GB RAM. Probes p4-p28 completed in ~55-110 seconds each. Total discovery time: ~1 hour.
**Solver (future):** CPU-only, 16 CPUs, 256 GB RAM, 28,800 seconds. Estimated solver time: 2-4 hours (cohort construction, phenotype assignment, outcome computation, logistic regression, sensitivities). No GPU required.

## 8. What the solver must compute

1. Cohort table: hadm_id, subject_id, t1, t2, l1, l2, gap, group (cleared/persistent), perfusion_context (yes/no).
2. Baseline table: age, gender, lactate_t1, lactate_t2, gap, n_vasopressor_agents, icu_los, hospital_los, by group.
3. Unadjusted rates: in-hospital death, new vasopressor escalation, by group, with 95% CIs.
4. Adjusted logistic regression: outcome ~ group + covariates, with adjusted OR and 95% CI.
5. Unadjusted-vs-adjusted gap.
6. Sensitivities S1-S5.
7. Written verdict against F1-F4.

## 9. Key references

See `work/support-lactate/key-references.json` for the three key references with complete receipts.

- K1: Weinberger J, Klompas M, Rhee C. "What Is the Utility of Measuring Lactate Levels in Patients with Sepsis and Septic Shock?" Semin Respir Crit Care Med. 2021;42(5):650-661. DOI: 10.1055/s-0041-1733915. Abstract only.
- K2: Kataria S, Singh O, Juneja D, et al. "Hypoperfusion context as a predictor of 28-d all-cause mortality in septic shock patients." World J Clin Cases. 2023;11(16):3765-3779. DOI: 10.12998/wjcc.v11.i16.3765. Abstract only; full text at PMC10294150 not inspected.
- K3: MIMIC-IV 3.1 documentation. PhysioNet. 2024. Full text.
