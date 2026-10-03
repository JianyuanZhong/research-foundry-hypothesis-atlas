# UKB 13: 房颤遗传风险与左房结构的不同组合

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

房颤PRS高但左房容积和功能保留者，其未来房颤风险低于同PRS且左房异常者，但仍高于低PRS结构正常者。

## 研究对象及主要数据

影像时无房颤者；标准AF PRS、心脏MRI和血压。

## 基本做法

从心脏MRI起随访，比较PRS与左房指标的交互，控制体型与血压，并在重复影像子集核对稳定性。

## 研究意义

区分电生理易感性与结构性负荷的组合。

## 主要难点

不能把左房正常视为保护机制；未诊断房颤也可能已改变左房。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41467-026-74715-4；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26200；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26212；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22009

## 生命科学方向

遗传风险与保护性表型

## 竞争解释

隐匿房颤或血压累积暴露产生结构差异。

## 最小验证与否定条件

排除影像后早期房颤后复核；若差异只集中于近期，不支持稳定的前驱分层。

## 字典字段依据

26200 In UK Biobank PRS Release Testing subgroup；26212 Standard PRS for atrial fibrillation (AF)；22009 Genetic principal components；24110 LA maximum volume；24111 LA minimum volume；24113 LA ejection fraction；4080 Systolic blood pressure, automated reading；4079 Diastolic blood pressure, automated reading；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.13.
