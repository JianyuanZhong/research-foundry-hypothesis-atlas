# UKB 11: 高糖尿病遗传风险下的异位脂肪差异

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

糖尿病PRS高且BMI相近者，肝脏和胰腺脂肪较低的人未来糖尿病发生较少。

## 研究对象及主要数据

影像时无糖尿病者；标准PRS、腹部MRI、HbA1c、代谢组。

## 基本做法

从影像日随访，连续检验PRS与器官脂肪的交互，比较绝对风险并在保留样本复核。

## 研究意义

定位高遗传风险未转化为疾病的候选表型。

## 主要难点

需核对PRS训练重叠、祖源和用药；未发病不等于终身受保护。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41588-022-01199-5；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26200；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26285；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22009

## 生命科学方向

遗传风险与保护性表型

## 竞争解释

影像健康选择或已经改变生活方式的人群造成表面保护。

## 最小验证与否定条件

先检查高PRS低脂肪交集与事件数；若只有短随访差异，不能称为稳定保护。

## 字典字段依据

26200 In UK Biobank PRS Release Testing subgroup；26285 Standard PRS for type 2 diabetes (T2D)；22009 Genetic principal components；21088 Liver PDFF (fat fraction)；21090 Pancreas PDFF (fat fraction)；21001 Body mass index (BMI)；30750 Glycated haemoglobin (HbA1c)；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.11.
