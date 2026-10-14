> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Proposal: Preoperative laboratory prediction of early (≤1-year) HCC recurrence after hepatic resection in a large Chinese liver-cancer cohort (HCC dataset)

## 1. Clinical question and why it matters
After curative-intent hepatic resection for hepatocellular carcinoma (HCC), roughly a quarter to
half of patients recur within one year. Early recurrence drives consequential decisions:
intensified surveillance, adjuvant/systemic therapy (lenvatinib, IO combinations), and transplant
listing. Published recurrence models (nomograms [K1], MERP [K2]) rely on variables that are NOT
available as structured data in this EHR: microvascular invasion (MVI), tumor size/number,
resection margin, histologic grade, and imaging features. The unresolved question is whether
**routinely drawn preoperative laboratory values alone** — the only variables with dense,
time-stamped availability in this cohort — carry enough independent prognostic signal to stratify
1-year recurrence risk, and whether a simple, deployable lab-only rule can approach the
discrimination reported for richer models (C-index ~0.68–0.74 [K1,K2]).

A validated lab-only score would be computable at the preoperative lab draw in any hospital,
whereas MVI is only known after surgery and imaging-feature models require radiology pipelines.

## 2. Evidence inspected (closest prior work; abstract-level, see key-references.json)
- [K1] Zeng et al. 2020 (PMID 33145280, Ann Transl Med): inflammation-based nomograms for OS/RFS
  after radical resection (n=3,071); RFS C-index 0.71/0.74 (train/val). Uses AFP, ALBI, PLR,
  NrLR, GPR, tumor size/number, MVI, margin, grade — most unavailable here. Bounds the
  discrimination achievable with "accessible clinical parameters" in a comparable Chinese cohort.
- [K2] Wei et al. 2026 (PMID 42323021, J Hepatol): MERP MRI-based 1-year RFS prediction in 1,811
  single BCLC 0/A resections; C-index 0.685–0.790 vs staging systems 0.524–0.682. State of the
  art for 1-year recurrence prediction; requires imaging features + MVI unavailable here.
- [K3] Chen et al. 2024 (PMID 39336451, Medicina): preoperative nomogram for MVI before
  hepatectomy (n=489) using AFP, platelets, GOT/GPT ratio, AAR, ALBI, GNRI — evidence that
  preop labs partially capture the biology (MVI) that dominates recurrence risk. This is the
  strongest rival explanation: any lab signal may proxy MVI rather than independent biology.

## 3. Hypothesis (falsifiable)
H1: A model using only preoperative (0–30 d before index resection) laboratory values predicts
1-year recurrence after hepatic resection with discrimination meaningfully above a clinical
baseline (age, sex, calendar year): held-out C-index ≥ 0.62, and top-vs-bottom tercile 1-year
recurrence rates differing by ≥ 10 percentage points.
Falsification: if the best lab-only model's held-out C-index ≤ 0.58 or the tercile risk gap is
≤ 5 pp, routine labs alone are not supported for early-recurrence triage in this cohort.

## 4. Cohort and data bindings (verified in source files; all measured this episode)
Source: local HCC snapshot [source checksum]
(datasets/hcc/README.md; absolute paths under [internal dataset path]).

- Index event: first hepatic resection per patient, 2013-01-01 to 2018-12-31.
  Table: data_手术_8024330590283626027.csv (procedures); columns 患者主索引, 就诊号, 手术, 开始时间.
  Rule (documented, lexical): 手术 contains one of 肝叶切除/肝部分切除/部分肝切除/肝段切除/半肝切除/
  肝肿瘤切除/肝(肿瘤)切除/肝（肿瘤）切除, excluding rows containing 移植 or 活检.
  Measured: 36,885 rows, 19,203 patients; first-resection 2013–2018 cohort n=7,689
  (2013:1481, 2014:1334, 2015:1339, 2016:1138, 2017:971, 2018:1426).
- Demographics: data_基本信息_2500296761891079109.csv (encounters); 患者主索引, 就诊号, 年龄, 性别,
  就诊时间, 入院时间, 出院时间, 就诊科室. Join key (患者主索引, 就诊号).
- Outcome: any HCC diagnosis in an encounter strictly after the index resection date.
  data_诊断_7504718184492840569.csv: 患者主索引, 就诊号, 诊断名称, 诊断类型; 诊断名称 contains
  肝细胞癌 or 原发性肝癌; encounter date from encounters.就诊时间.
  Measured: 3,424/7,689 (44.5%) ever recur; 1-y RFS 67.5% (1,475/2,186 with ≥1y follow-up);
  3-y RFS 55.7% (826/1,484 with ≥3y follow-up).
- Follow-up/censoring: last encounter date per patient (encounters.就诊时间). No encounter ≥365 d
  after resection ⇒ censored <1y, excluded from primary 1-year analysis (n=2,186 at risk).
  No mortality table exists; death is unobserved (limitation).
- Preoperative labs (0–30 d before index resection; nearest pre-surgery value per analyte):
  data_检验_609065997844652188.csv: 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间.
  Measured cohort availability (rows in window): 白蛋白 6,890; 总胆红素 6,895; 直接胆红素 6,894;
  总蛋白 6,892; 球蛋白 6,891; γ-谷氨酰转移酶 7,025; 肌酐 6,385; 白细胞计数 12,817; 血红蛋白 7,976;
  血小板计数 7,767; 癌胚抗原 6,236; 甲胎蛋白 6,346; 糖类抗原19-9 6,229; 葡萄糖 10,977;
  淋巴细胞数 367,586 (dataset-wide, dense); 中性粒细胞数 327,533 (dataset-wide).
  甲胎蛋白异质体 (AFP-L3): 0 rows for the 2013–2018 cohort (all 82,592 rows are 2019–2025) → excluded.
  Lab names are free text; a fixed name dictionary (above) is part of the protocol. Numeric values
  parsed from 定量结果; 定性结果 used for non-numeric items.
- MVI (secondary endpoint only, NOT in the primary model): data_病理_3292603985559017792.csv
  (pathology), 检查所见/检查诊断 free text; lexical rule: positive if 微血管侵犯/脉管内癌栓/脉管癌栓/
  血管侵犯/门静脉癌栓 present without a negation pattern (未见微血管侵犯/未见脉管/未见癌栓/…);
  measured in 29,240 HCC pathology rows: 5,604 positive, 585 explicitly negative, 173 ambiguous,
  remainder silent. MVI is postoperative; used only to test mediation of the lab signal.

## 5. Design
Primary analysis (1-year recurrence):
- Population: 7,689 patients, first resection 2013–2018, ≥365 d follow-up (n≈2,186).
- Features (all preoperative, 0–30 d window, nearest pre-surgery value):
  AFP, ALB, TBIL, DBIL, TP, GLB, GGT, CREA, WBC, HGB, PLT, CEA, CA199, GLU,
  淋巴细胞数, 中性粒细胞数; derived: ALBI score/grade (ALB, TBIL), PLR (PLT/lymphocyte),
  NLR (neutrophil/lymphocyte), GNRI (GLU, ALB, lymphocyte). Plus age, sex, resection year.
- Baseline B0: logistic regression on age, sex, year only.
- Main model B1: penalized logistic regression (L1/L2, 5-fold CV) on the lab feature set.
- Learned alternative B2: gradient-boosted trees (e.g., LightGBM) on the same features — tests
  whether non-linear interactions (AFP×ALBI, GGT×PLT) add information the linear model loses.
  B2 is the substantive learned alternative; B1 the simple baseline. A Delphi-style sequence
  model is not scientifically justified at n≈2,000 with ~20 features.
- Split: temporal — train 2013–2016, test 2017–2018 (no patient overlap; guards assay drift).
  Secondary: 5-fold CV within 2013–2018.
- Outcome: recurrence within 365 d (event) vs no recurrence by 365 d (non-event); patients
  censored <365 d excluded (primary); sensitivity analysis with all comers and censoring flag.
- Metrics: C-index with DeLong CI, calibration (Hosmer-Lemeshow / slope), AUC at 1 y,
  NRI and IDI of B1/B2 vs B0, tercile risk gap.
- Secondary: (a) 3-year recurrence among ≥3y FU (n≈1,484); (b) MVI mediation — add adjudicated
  MVI to the lab model and measure attenuation; (c) AFP-L3 exploratory 2019–2025 sub-cohort
  (shorter FU; descriptive only).

## 6. Interpretation plan
- Supportive: B1 or B2 held-out C-index ≥ 0.62 and tercile gap ≥ 10 pp → routine labs carry
  actionable early-recurrence signal; next steps: external validation (not available here) and
  decision-curve analysis.
- Adverse: C-index ≤ 0.58 or gap ≤ 5 pp → lab-only triage not supported; record as a negative
  result; the field should rely on postoperative MVI/imaging.
- Inconclusive: 0.58 < C-index < 0.62 → weak signal; report with CIs; do not claim utility.
- NOT established by this study: causality, external validity (single center), or that the lab
  signal is not a proxy for unmeasured MVI/tumor burden (partially addressed by MVI mediation;
  definitive mediation requires adjudicated MVI in the full cohort).

## 7. Compute and feasibility (measured this episode)
- Labs 2.2 GB CSV; single-pass Python ≈ 80–100 s per full scan (measured, 4 CPU).
- Cohort assembly + model fitting < 1 h on 4–16 CPU, 32 GB RAM. No GPU needed (tabular,
  n≈2,000–8,000). Fits the solver envelope (16 CPU, 256 GB, 8 h) with large margin.
- Solver deliverables: cohort table (features, outcome, follow-up), B0/B1/B2 models, held-out
  metrics with CIs, calibration, tercile table, MVI mediation table. Completion = all metrics
  computed and reported; clinical truth is NOT established by this experiment.

## 8. Limitations and essential adjudication
- Outcome is a diagnosis-text proxy (unstructured 诊断名称; 诊断类型 often blank), not
  imaging/pathology-confirmed recurrence. Clinical adjudication would require chart review
  (not computable here).
- ~55% of the 2013–2018 cohort has no later encounter in this EHR (loss to facility); the
  primary analysis conditions on ≥1y follow-up (possible selection bias; sensitivity analysis).
- No death data → recurrence-free survival conflates recurrence with survival; the estimand is
  1-year recurrence, not OS.
- MVI is sparsely and textually recorded; the mediation analysis is underpowered for precision.
- Single center; no external validation cohort in the configured datasets.
- Assay drift 2013–2018 handled by temporal split + year covariate.

## 9. Alternatives considered (recorded, with deferral reasons)
- MVI-prediction model (as in K3): deferred as primary — MVI labels sparse (5,604 pos / 585 neg /
  rest silent) and text-adjudicated; kept as secondary mediation analysis.
- Imaging-text tumor size extraction (~60% of enhanced-MRI rows contain mm measurements):
  deferred — adds a second unvalidated NLP extraction layer; revisit if the lab-only signal is
  weak and size is the suspected missing variable.
- AFP-L3% model: assay unavailable for the primary cohort (introduced 2019); kept as a
  2019–2025 exploratory sub-cohort.
- Neural/sequence models (Delphi-style): not justified at n≈2,000 with ~20 features;
  gradient boosting is the appropriate learned alternative.
- Systemic-therapy timing questions (lenvatinib/IO era): deferred — treatment-course timestamps
  unreliable (median course duration 0 d) and heavily confounded by era.
