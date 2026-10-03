# UKB 38: 长端粒相关的肿瘤与血管风险权衡

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

在相同年龄和炎症水平下，较长白细胞端粒可能对应较低动脉事件风险，却不对应较低的部分癌症风险。

## 研究对象及主要数据

有端粒、生化和随访者；预先限定肺癌、结直肠癌及冠心病。

## 基本做法

比较端粒对不同结局的非线性关联，调整细胞组成并检查滞后；有合适工具时用遗传分析作补充。

## 研究意义

检验细胞复制潜能与不同疾病之间的潜在权衡。

## 主要难点

已有文献涉及该方向，增量需落在癌种和细胞组成；遗传分析受多效性限制。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s43587-025-01016-8；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22191；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22192；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=30000

## 生命科学方向

肿瘤发生、宿主储备与造血

## 竞争解释

吸烟、细胞组成及潜在肿瘤解释方向差异。

## 最小验证与否定条件

先比较细胞组成校正前后及近期事件排除结果；若方向不稳，不支持权衡解释。

## 字典字段依据

22191 Adjusted T/S ratio；22192 Z-adjusted T/S log；30000 White blood cell (leukocyte) count；30120 Lymphocyte count；30140 Neutrophill count；30710 C-reactive protein；20116 Smoking status；40005 Date of cancer diagnosis；40006 Type of cancer: ICD10；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.38.
