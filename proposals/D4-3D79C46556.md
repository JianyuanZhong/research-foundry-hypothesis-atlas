# UKB 32: 早绝经与心脏重构是否独立于血压负荷

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

相同年龄和血压下，较早自然绝经者更可能出现左心室质量或左房功能异常。

## 研究对象及主要数据

自然绝经女性；生殖史、心脏MRI、血压及心血管随访。

## 基本做法

排除手术绝经并处理HRT，比较绝经年龄与心脏表型，检验随后心衰或房颤关联。

## 研究意义

寻找生殖衰老与心脏结构之间的连接。

## 主要难点

单次血压不足以表示累积负荷；不能解释为激素补充治疗获益。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41467-026-74715-4；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3581；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=2724；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=3536

## 生命科学方向

性别、激素与代谢重分布

## 竞争解释

共同的遗传、吸烟和社会因素造成生殖与心血管衰老同步。

## 最小验证与否定条件

先比较重复血压可用子集；若只在粗略血压调整下出现，优先解释为残余负荷。

## 字典字段依据

3581 Age at menopause (last menstrual period)；2724 Had menopause；3536 Age started hormone-replacement therapy (HRT)；3546 Age last used hormone-replacement therapy (HRT)；24105 LV myocardial mass；24110 LA maximum volume；24113 LA ejection fraction；4080 Systolic blood pressure, automated reading；4079 Diastolic blood pressure, automated reading；41270 Diagnoses - ICD10；41280 Date of first in-patient diagnosis - ICD10；53 Date of attending assessment centre

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.32.
