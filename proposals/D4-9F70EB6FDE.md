> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-05: Bone-muscle discordance and incident fracture risk

## Unresolved clinical question
Current fracture risk assessment (FRAX, DXA-based) relies primarily on bone
mineral density (BMD). If grip strength — a simple, low-cost bedside measure —
adds independent predictive information beyond BMD, this would identify a
practical tool to augment DXA-based risk stratification and suggest that bone
strength and fall susceptibility are two distinct pathways to fracture with
different modifiable targets. The unresolved claim: do participants with low
BMD AND low grip strength have higher incident fracture risk than low BMD
alone, and is this excess partly mediated by falls?

## Leading claim vs strongest rival
- **Leading claim**: Low BMD + low grip → higher fracture risk than low BMD
  alone, with part of the excess mediated by falls (two-pathway model: bone
  fragility + fall susceptibility).
- **Strongest rival**: Frailty confounding — a general state of vulnerability
  that affects BMD, grip, and falls simultaneously. If correct, the
  BMD×Grip interaction should attenuate to null after adjusting for age, BMI,
  comorbidities, and physical activity.

## Discriminating observation
If the leading claim is correct, the BMD×Grip interaction should be
significant and attenuated (but not eliminated) after adjusting for falls.
If the rival is correct, the interaction should attenuate to null after
adjusting for frailty covariates.

## Clinical importance
- Identifies a simple bedside test (handgrip dynamometry) that could augment
  DXA-based risk stratification [K3].
- Suggests two distinct pathways to fracture with different modifiable targets.
- Informs clinical decisions about who to refer for additional fracture
  prevention interventions.
- Missed opportunities for osteoporosis treatment before hip fracture are
  common; better risk stratification could reduce this gap [K3].

## Data bindings (verified, ukb672073 namespace)

**Assessment_Center** ([UKB data file], 502,370 rows, id=eid):
- 23208-2.0/3.0: Femur neck BMD (g/cm2) — best = max of 2.0/3.0
- 23204-2.0/3.0: L1-L4 BMD (g/cm2) — sensitivity analysis
- 46-0.0..3.0: Grip left (kg); 47-0.0..3.0: Grip right (kg)
- 2296-0.0..3.0: Falls in last year (0/1)
- 53-0.0..3.0: AC date (baseline time)
- 21001-0.0: BMI; 924-0.0: Walking pace

**Health_Related_Outcomes** ([UKB data file], 502,370 rows, id=eid):
- 41270-0.0..258: ICD10 diagnoses
- 41280-0.0..258: Diagnosis dates
- 40000-0.0/1.0: Death date
- Fracture S-codes: S72 (hip), S52 (arm), S42 (shoulder), S22 (rib),
  S32 (spine), S82 (leg), S92 (ankle/foot), S62 (hand)

**Population_Characteristics** ([UKB data file]):
- 31-0.0: Sex; 34-0.0: Ethnicity; 21022-0.0: Date of birth

**Verified overlap** ([research job]):
- 46,706 participants with femur BMD + grip + falls + AC date
- 2,198 with ≥1 fracture S-code; 793 with fracture after AC date
- 2×2 fracture-after-AC: lowBMD+lowGrip=181 (n=5,125), lowBMD+highGrip=73
  (n=2,689), highBMD+lowGrip=245 (n=13,292), highBMD+highGrip=294 (n=25,600)

## Analysis plan
1. **Baseline**: Cox PH for incident fracture (after AC date), with BMD × Grip
   interaction term, adjusted for age, sex, BMI, walking pace, falls.
   Low BMD: femur < 0.80 g/cm2. Low grip: bottom tertile (≤30 kg).
2. **Mediation**: Proportion of BMD×Grip interaction explained by falls.
3. **Site-specific**: Hip (S72) vs non-hip fractures.
4. **Sensitivity**: Exclude fractures within 2 years of AC date; use lumbar
   BMD instead of femur; adjust for smoking (20016).
5. **Learned alternative**: LightGBM + SHAP for non-linear interaction
   detection. What it reveals: whether the BMD-grip relationship is linear
   (baseline) or has threshold/non-linear structure.
   Resource: Both fit on CPU in minutes (~47k rows). No GPU needed.

## Falsification criteria
- **Supportive**: BMD×Grip interaction significant (p<0.05), attenuated but
  not eliminated after falls adjustment. Low-BMD+low-grip cell has highest
  hazard ratio.
- **Adverse**: No significant interaction, or interaction fully explained by
  falls/frailty covariates.
- **Inconclusive**: Borderline interaction (0.05<p<0.10), or insufficient
  fracture events in the low-BMD+low-grip cell.

## Key references

[K1] Fan et al. 2026 (Nat Commun) — Pan-organ imaging proteomics in UKB,
     including muscle composition IDPs. Establishes the UKB imaging
     infrastructure and the framework for integrating body composition
     measures with clinical outcomes.
     DOI: 10.1038/s41467-026-74715-4
     source_id: [source checksum]
     Inspection: full HTML text (939,719 bytes)

[K2] Yue et al. 2026 (Front Med) — Dementia → muscle-bone fragility in UKB.
     Demonstrates that grip strength and fracture are linked in UKB, with
     time-updated Cox analysis and proteomic mediation. Provides the
     methodological template for our interaction analysis.
     DOI: 10.3389/fmed.2026.1883046
     source_id: [source checksum]
     Inspection: full-text XML (PMC13597354, 192,902 bytes)

[K3] Arcidiacono et al. 2026 (Calcif Tissue Int) — Missed opportunities for
     osteoporosis treatment before hip fracture. Documents the clinical gap
     that better fracture risk stratification could address. Supports the
     clinical importance of adding a simple bedside measure to DXA-based
     assessment.
     DOI: 10.1007/s00223-026-01594-8
     source_id: [source checksum]
     Inspection: full-text XML (PMC13525934, 122,290 bytes)

## Method comparison
- **Baseline**: Cox PH with prespecified covariates and BMD×Grip interaction.
- **Learned alternative**: LightGBM + SHAP for non-linear interaction detection.
- **What the alternative reveals**: Whether the BMD-grip relationship is
  linear (baseline) or has threshold/non-linear structure (learned).
- **Resource**: Both fit on CPU in minutes (~47k rows). No GPU.
- **Selection reason**: The scientific question is whether the interaction
  exists and is mediated by falls. The baseline answers this directly. The
  learned alternative adds value by detecting non-linear structure that the
  linear interaction term would miss.

## Unresolved issues
1. Clinical adjudication of fracture codes required (ICD10 S-codes may
   include non-fragility fractures).
2. Temporal ordering: AC date (53) should precede fracture date (41280).
   Verified: 793 fractures after AC date, median 900 days.
3. Falls (2296) is a single timepoint; cannot model fall trajectory.
4. BMD threshold (0.80 g/cm2) is a rough approximation of T-score -2.5;
   sensitivity analysis with lumbar BMD and continuous BMD planned.
