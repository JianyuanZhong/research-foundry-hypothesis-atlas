# UKB 15: 乳腺癌遗传风险与绝经后激素背景

Admission: feasibility_required. Verify participant overlap, measurement dates, missingness and event support before committing this design.

## 待检验假说

绝经后女性中，乳腺癌PRS与发病风险的关联在低SHBG和高脂肪负荷者中更强。

## 研究对象及主要数据

无乳腺癌的绝经后女性；标准BC PRS、SHBG、性激素、体脂、HRT史及癌症登记。

## 基本做法

预设PRS与SHBG及脂肪的少数交互，从采血日随访，按自然绝经和HRT使用分层。

## 研究意义

检验遗传易感是否在不同内分泌背景下表达不同。

## 主要难点

激素单次测量且低值可能受检测限影响；不能推断HRT效果或受体亚型。

## 参考资料

相关背景或数据说明，非假说成立或新颖性证明：https://www.nature.com/articles/s41467-025-60058-z；字段定义：https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26200；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=26220；https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=22009

## 生命科学方向

遗传风险与保护性表型

## 竞争解释

BMI、HRT选择及筛查频率共同解释关联。

## 最小验证与否定条件

先审计绝经状态、检测限和HRT；若连续交互在独立子集中不稳定，不支持放大效应。

## 字典字段依据

26200 In UK Biobank PRS Release Testing subgroup；26220 Standard PRS for breast cancer (BC)；22009 Genetic principal components；2724 Had menopause；3581 Age at menopause (last menstrual period)；30830 SHBG；30800 Oestradiol；23099 Body fat percentage；3536 Age started hormone-replacement therapy (HRT)；3546 Age last used hormone-replacement therapy (HRT)；40005 Date of cancer diagnosis；40006 Type of cancer: ICD10

## Bound source groups

The clinical fields map to the UKB/ukb672073 split tables of the completed subset. Use the dataset catalog and Parquet convenience tables for exact paths. Olink/dta and ukb671626 have separate ID namespaces. Header presence does not establish nonmissing overlap.


Exact field map: see source-schema-audit.json, seeds.15.
