# UKB 20: 肺功能下降与右心改变的先后关系

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

肺功能较差者中，右心结构或功能异常与未来心衰的关联强于单纯肺功能异常。

## 研究对象及主要数据

有肺功能和心脏MRI者；重复测量子集、呼吸病与心衰随访。

## 基本做法

对齐肺功能与影像时间，区分先前肺功能和同期肺功能，比较右心、左心指标及后续结局。

## 研究意义

识别肺循环负荷与全身心肺共病的不同线索。

## 主要难点

没有右心导管压力不能诊断肺动脉高压；重复测量时间不一定支持先后推断。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41467-026-74715-4；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=20150；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=20151；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=24106

## 生命科学方向

跨器官代谢与疾病分叉

## 竞争解释

吸烟、肥胖或左心疾病同时影响肺功能和右心。

## 最小验证与否定条件

先检查肺功能是否确实早于MRI；若仅同期数据可用，则只报告联合表型。

## 字典字段依据

20150 Forced expiratory volume in 1-second (FEV1), Best measure；20151 Forced vital capacity (FVC), Best measure；24106 RV end diastolic volume；24107 RV end systolic volume；24109 RV ejection fraction；24103 LV ejection fraction；24105 LV myocardial mass；20116 Smoking status；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.20.
