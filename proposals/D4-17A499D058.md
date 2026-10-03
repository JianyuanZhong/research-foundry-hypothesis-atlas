# UKB 30: 夜间噪声与睡眠脆弱性共同指向房颤

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

夜间噪声与后续房颤的关联在失眠或睡眠不规律者中更强，且不能完全由空气污染解释。

## 研究对象及主要数据

有居住地噪声、睡眠问卷或加速度计及房颤随访者。

## 基本做法

以联合暴露可确定时为起点，预设噪声与睡眠交互，联合调整空气污染并进行搬迁敏感性分析。

## 研究意义

区分夜间环境干扰与一般交通暴露的线索。

## 主要难点

暴露年份需一致；不能用一次睡眠测量代表长期机制。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41591-024-03483-9；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=24022；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=24006；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=1200

## 生命科学方向

环境、行为与生物学易感性

## 竞争解释

交通污染、社会经济状况或就医频率解释关联。

## 最小验证与否定条件

先检查噪声与污染的共线性及独立变化支持；无法分开时只报告联合暴露。

## 字典字段依据

24022 Average night-time sound level of noise pollution；24006 Particulate matter air pollution (pm2.5); 2010；1200 Sleeplessness / insomnia；1160 Sleep duration；90001 Acceleration data - cwa format；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre。睡眠规律及活动片段需从原始加速度推导

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.

Questionnaire insomnia is available; accelerometer sleep irregularity is blocked without its bulk payload. Any narrower formulation must be labeled.

Exact field map: see source-schema-audit.json, seeds.30.
