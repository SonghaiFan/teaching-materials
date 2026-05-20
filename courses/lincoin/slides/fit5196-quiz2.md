---
theme: apple-basic
title: FIT5196 Quiz 2 Week 6-11 练习与解析
layout: intro
---

# FIT5196 Quiz 2

Week 6-11 练习与解析

---
layout: default
---

# 这份题库怎么来

- 参考了 `2025_5196_S1_Quiz2 2.pdf` 的真题题型与高频考点
- 按 `week6-11` 的 lecture + applied session 重新组织
- 每周保留 10 题，重点考察概念区分、方法选择、边界条件、常见误区
- 每题都带 `参考答案` 和 `解析`，适合课堂讲解和课后复习

---
layout: default
---

# Quiz 2 真题信号

- 从 PDF 中识别出 `3` 套并行卷，每套 `50` 题，共 `150` 个 question markers
- 高频主题 1：`data structures`，尤其是 graph / BST / hash / heap / DFS
- 高频主题 2：`data quality & anomalies`，尤其是 duplicate / consistency / anomaly type
- 高频主题 3：`missing & outliers`，尤其是 MAR / missing-data handling / outlier detection
- 高频主题 4：`transformation`，尤其是 log transformation / categorical transformation
- 高频主题 5：`integration & enrichment`，尤其是 use cases / benefits / schema-related ideas
- 高频主题 6：`validation`，尤其是 schema validation / consistency checks / expected format
- 真题最常考的不是死记定义，而是场景判断
- 真题也很爱考方法适用边界和易混概念辨析

---
layout: section
---

# Week 6

Data Structuring

---

### Week 6 (10 题)

- 范围：primitive / non-primitive data structures, graph, BST, B-tree, hash table, heap
- 目标：看到场景就能判断该选什么结构，而不是只背定义

## Question 1

**What is the primary purpose of data structuring?**

- a. To visualise data trends only
- b. To organise data into formats that support efficient retrieval and processing
- c. To remove all missing values
- d. To convert all data into text

<v-click>

参考答案： `b`

解析：Week 6 的核心不是“把数据变漂亮”，而是让 retrieval、update、processing、management 更高效。

</v-click>

---

## Question 2

**Which of the following is a primitive data type?**

- a. Queue
- b. Graph
- c. Boolean
- d. Dictionary

<v-click>

参考答案： `c`

解析：primitive type 是最基础、固定表示的数据类型，`boolean` 属于这一类。

</v-click>

---

## Question 3

**Which scenario most strongly favours using an array over a linked list?**

- a. Frequent insertion and deletion in the middle
- b. Fast indexed access to same-type elements
- c. Priority-based removal
- d. Key-value lookup by hash

<v-click>

参考答案： `b`

解析：array 的优势是 contiguous storage 带来的快速 indexed access；频繁中间插删并不是它的强项。

</v-click>

---

## Question 4

**Which data structure is the best match for a first-in, first-out scheduling task?**

- a. Stack
- b. Queue
- c. Heap
- d. Tree

<v-click>

参考答案： `b`

解析：FIFO 对应 queue，这是 week6 里最基础但也很常考的匹配题。

</v-click>

---

## Question 5

**A data wrangler needs to model friendships in a social network. Which structure is most appropriate?**

- a. Graph
- b. Heap
- c. Array
- d. Stack

<v-click>

参考答案： `a`

解析：friendship 本质上是 entity + relationship，所以 graph 最自然。

</v-click>

---

## Question 6

**In which data structures is depth-first search (DFS) typically used? (Select all that apply)**

- a. Stack
- b. Tree
- c. Graph
- d. Array

<v-click>

参考答案： `a, b, c`

解析：DFS 是一种 traversal/search strategy，常用于 tree 和 graph；实现时通常依赖 stack 或 recursion。

</v-click>

---

## Question 7

**Which statement correctly describes the Binary Search Tree (BST) rule?**

- a. Left subtree keys are always greater than the parent key
- b. Both subtrees can contain any values in any order
- c. Left subtree keys are smaller and right subtree keys are larger than the parent key
- d. Every node must have exactly two children

<v-click>

参考答案： `c`

解析：BST 的核心 invariant 就是 left smaller, right larger；这也是它支持 ordered search 的基础。

</v-click>

---

## Question 8

**Which traversal of a BST returns keys in sorted order?**

- a. Inorder
- b. Preorder
- c. Postorder
- d. Level-order only

<v-click>

参考答案： `a`

解析：inorder 会按 left, node, right 的顺序访问，因此 BST 上会得到 sorted output。

</v-click>

---

## Question 9

**Why are B-trees widely used in storage systems and database indexing?**

- a. They always keep exactly two children per node
- b. They avoid storing keys in internal nodes
- c. They support good block/page efficiency with multiple children per node
- d. They guarantee O(1) lookup

<v-click>

参考答案： `c`

解析：B-tree 的优势在于面向 storage blocks / pages 的高扇出结构，不是 O(1) 查找。

</v-click>

---

## Question 10

**Which structure is most appropriate when you repeatedly need to extract the smallest current value?**

- a. Min-heap
- b. Directed graph
- c. Linked list
- d. Character array

<v-click>

参考答案： `a`

解析：heap 的使用场景不是“排序一切”，而是 repeated priority extraction，这点很容易在选择题里考。

</v-click>

---
layout: section
---

# Week 7

Data Quality & Anomalies

---

### Week 7 (10 题)

- 范围：data quality dimensions, measures, anomaly types, auditing, governance
- 目标：分清 dimension / measure / anomaly / inconsistency / governance

## Question 1

**Which of the following best describes a data quality dimension?**

- a. A specific cleaning script used to repair errors
- b. A broad criterion used to evaluate data quality
- c. A storage format for processed datasets
- d. A machine learning model for anomaly detection

<v-click>

参考答案： `b`

解析：dimension 是“从什么角度评价质量”，例如 accuracy、completeness；不是具体工具。

</v-click>

---

## Question 2

**Which of the following is a data quality measure rather than a data quality dimension?**

- a. Timeliness
- b. Consistency
- c. Duplicate rate
- d. Relevance

<v-click>

参考答案： `c`

解析：`duplicate rate` 是可量化指标；其余是更高层的 quality dimensions。

</v-click>

---

## Question 3

**A company makes poor strategic decisions because customer records are incomplete and outdated. This is primarily an example of:**

- a. Improved operational efficiency
- b. The positive effect of data enrichment
- c. An impact of poor data quality
- d. A benefit of data silos

<v-click>

参考答案： `c`

解析：Week 7 反复强调 poor data quality 会直接伤害 decision-making，这题就是典型场景题。

</v-click>

---

## Question 4

**Which scenario is the best example of a point anomaly?**

- a. A customer spends slightly more during holiday season than usual
- b. One staff record shows `Work_Hour = 500` while others are in single digits
- c. A sequence of individually normal transactions forms a suspicious pattern
- d. Electricity use is high at 7pm but normal for that time of day

<v-click>

参考答案： `b`

解析：single record 明显偏离整体，就是 point anomaly。

</v-click>

---

## Question 5

**A temperature reading of 35°C is considered abnormal only because it occurs at 3am in winter. This is best classified as a:**

- a. Point anomaly
- b. Contextual anomaly
- c. Coverage anomaly
- d. Referential integrity violation

<v-click>

参考答案： `b`

解析：contextual anomaly 的关键是“值本身不一定异常，但在特定 context 下异常”。

</v-click>

---

## Question 6

**Several individually reasonable credit card transactions together form a suspicious pattern of fraud. This is best classified as a:**

- a. Collective anomaly
- b. Lexical anomaly
- c. Coverage anomaly
- d. Domain format error

<v-click>

参考答案： `a`

解析：collective anomaly 看的是 group pattern，不是单个 record。

</v-click>

---

## Question 7

**In the Titanic auditing exercise, values like `Cherborg`, `Cherbourge`, and `Southamtpon` are best treated as:**

- a. Semantic anomalies
- b. Coverage anomalies
- c. Syntactic anomalies
- d. Referential integrity violations

<v-click>

参考答案： `c`

解析：这些首先是 spelling / formatting 问题，所以归到 syntactic anomalies。

</v-click>

---

## Question 8

**In the Titanic data, a passenger labeled `who = man` with `age = 16` is best treated as:**

- a. A lexical error
- b. A semantic anomaly involving an integrity constraint
- c. A coverage anomaly
- d. A multi-source schema mismatch

<v-click>

参考答案： `b`

解析：这里的问题不是拼写，而是 cross-field contradiction，因此更接近 semantic anomaly。

</v-click>

---

## Question 9

**Why is `pd.crosstab(embark_town, embarked)` useful in the Titanic auditing exercise?**

- a. It imputes missing values automatically
- b. It validates expected correspondence between redundant categorical fields
- c. It normalizes the values into a standard scale
- d. It removes duplicate observations

<v-click>

参考答案： `b`

解析：这类 cross-tab 很适合检查两个冗余字段是否真的一致，是 applied session 的重点思路。

</v-click>

---

## Question 10

**Which statement best reflects the role of data governance in data quality management?**

- a. Governance is optional if enough data scientists are available
- b. Governance mainly matters only after machine learning deployment
- c. Governance provides standards, responsibilities, and processes for sustained quality
- d. Governance is equivalent to removing duplicates from one table

<v-click>

参考答案： `c`

解析：data quality 不是一次性 cleaning，必须靠 governance 持续维护。

</v-click>

---
layout: section
---

# Week 8

Data Cleansing

---

### Week 8 (10 题)

- 范围：cleansing workflow, missing data, deletion, imputation, outliers
- 目标：知道什么时候删、什么时候补、什么时候先调查

## Question 1

**Which sequence best matches the data cleansing workflow presented in class?**

- a. Backup → Audit → Clean → Document → Review
- b. Audit → Define goals → Plan → Backup → Clean → Verify → Document → Review
- c. Clean → Audit → Verify → Backup → Review
- d. Define goals → Review → Clean → Backup → Audit

<v-click>

参考答案： `b`

解析：week8 很强调 cleansing 不是随手修几列，而是一整套 audit-to-review 的 workflow。

</v-click>

---

## Question 2

**What is the main purpose of a data audit?**

- a. To automatically impute all missing values
- b. To systematically identify quality issues and assess data health
- c. To train a predictive model
- d. To remove all outliers immediately

<v-click>

参考答案： `b`

解析：audit 是诊断阶段，先看问题分布和严重程度，再决定 cleansing strategy。

</v-click>

---

## Question 3

**Which example is the best illustration of `MCAR`?**

- a. High-income people are less likely to report income
- b. Younger respondents are more likely to skip an income question
- c. Several questionnaire pages were lost randomly in transit
- d. Patients with more severe symptoms are more likely to drop out

<v-click>

参考答案： `c`

解析：MCAR 的关键词是 completely random，与 observed 和 unobserved values 都无关。

</v-click>

---

## Question 4

**Which scenario is the best example of `MAR`?**

- a. A value is missing because the value itself is unusually high
- b. Females have a different missing-age rate than males
- c. A sensor fails for completely random reasons
- d. A respondent hides income because it is very low

<v-click>

参考答案： `b`

解析：MAR 依赖其他已观测变量，而不直接依赖缺失值本身。

</v-click>

---

## Question 5

**A key limitation of `listwise deletion` is that it:**

- a. Creates fake variability
- b. Requires multiple complete datasets
- c. Reduces sample size by discarding any row with a missing value
- d. Can only be used for numeric data

<v-click>

参考答案： `c`

解析：listwise deletion 简单，但代价通常是 sample size 大幅下降。

</v-click>

---

## Question 6

**What is the main risk of `pairwise deletion`?**

- a. It always produces smaller samples than listwise deletion
- b. It can distort estimates if the MCAR assumption does not hold
- c. It always increases variance too much
- d. It cannot be used for correlation analysis

<v-click>

参考答案： `b`

解析：pairwise 看起来“利用了更多数据”，但不同统计量基于不同子样本时会带来偏差和不稳定。

</v-click>

---

## Question 7

**What is the main problem with `mean imputation`?**

- a. It increases variability too much
- b. It reduces variability and can distort distributions
- c. It can only be used on categorical variables
- d. It always improves model accuracy

<v-click>

参考答案： `b`

解析：mean imputation 会把值往中心拉，低估 variability，也可能削弱变量间关系。

</v-click>

---

## Question 8

**Compared with plain regression imputation, why might `stochastic regression imputation` be preferred?**

- a. It avoids fitting any model
- b. It adds random residual variation back into the imputed values
- c. It guarantees unbiased estimates in all settings
- d. It only uses the target variable

<v-click>

参考答案： `b`

解析：plain regression imputation 太“平滑”；stochastic regression 会把 residual variability 补回来。

</v-click>

---

## Question 9

**In the Titanic example, why is imputing age by `Title` usually better than using one global mean age?**

- a. It guarantees perfect ages
- b. It uses group structure such as `Mr`, `Mrs`, and `Master`, which better reflects likely age differences
- c. It removes all missing values without assumptions
- d. It works only because age is categorical

<v-click>

参考答案： `b`

解析：Title 提供了有信息量的 subgroup structure，因此 group-wise imputation 通常优于 one global mean。

</v-click>

---

## Question 10

**A fare of `512.3292` appears as an outlier in the Titanic data. What is the best response?**

- a. Delete it immediately because all outliers are errors
- b. Replace it with the mean fare
- c. Investigate it with domain knowledge and keep it if it is a valid extreme value
- d. Ignore it because boxplots are unreliable

<v-click>

参考答案： `c`

解析：week8 的关键原则之一就是 statistical outlier 不等于 data error，先调查再决定。

</v-click>

---
layout: section
---

# Week 9

Data Transformation

---

### Week 9 (10 题)

- 范围：scaling, power transformation, discretisation, feature construction, sampling
- 目标：按场景选方法，而不是只记公式

## Question 1

**Which of the following best explains why scaling was needed for the wine dataset features `Alcohol` and `Malic acid`?**

- a. Scaling removes class labels that may bias the model
- b. Scaling prevents the larger-scale feature from disproportionately influencing analysis
- c. Scaling guarantees all features become normally distributed
- d. Scaling converts continuous variables into categorical variables

<v-click>

参考答案： `b`

解析：scaling 的第一性原理是让不同量纲的变量可比较，而不是“把一切变正态”。

</v-click>

---

## Question 2

**A dataset contains a few extremely expensive houses among otherwise typical prices. Which scaling method is the best choice according to the week 9 materials?**

- a. Min-Max Scaling
- b. Z-score Standardisation
- c. Robust Scaling
- d. Decimal Scaling

<v-click>

参考答案： `c`

解析：当 outlier 明显存在时，median + IQR 的 robust scaling 更稳。

</v-click>

---

## Question 3

**After applying Z-score standardisation to a feature, which statement should be true?**

- a. All values lie between 0 and 1
- b. The feature mean is about 0 and the standard deviation is about 1
- c. The feature becomes categorical
- d. The feature will no longer contain outliers

<v-click>

参考答案： `b`

解析：Z-score 改变 location 和 spread，不保证 bounded range，也不自动消除 outliers。

</v-click>

---

## Question 4

**Which property is preserved by both Z-score standardisation and Min-Max scaling?**

- a. The exact minimum and maximum values
- b. The number of categories in the feature
- c. The relative ordering and shape of the data
- d. The feature mean in the original units

<v-click>

参考答案： `c`

解析：这两类方法本质上都是 linear transformations，会保留 ordering 和 overall shape。

</v-click>

---

## Question 5

**Which scaling method is most appropriate when you want to preserve sign and scale values into approximately `[-1, 1]`?**

- a. MaxAbs Scaling
- b. Min-Max Scaling
- c. Robust Scaling
- d. Decimal Scaling

<v-click>

参考答案： `a`

解析：MaxAbs scaling 按最大绝对值缩放，保留正负号。

</v-click>

---

## Question 6

**The BMR example in the applied session is positively skewed. Which transformation gave the best result in the materials?**

- a. Square transformation
- b. Log transformation
- c. Cubic transformation
- d. No transformation

<v-click>

参考答案： `b`

解析：对 right-skewed data，往 Tukey ladder 的 downward direction 走，`log` 往往能压缩大值、改善线性关系。

</v-click>

---

## Question 7

**In the basic Box-Cox transformation, what does the case `λ = 0` correspond to?**

- a. No transformation
- b. Square-root transformation
- c. Log transformation
- d. Reciprocal transformation

<v-click>

参考答案： `c`

解析：这是 Box-Cox 最经典的边界条件题，`λ = 0` 对应 `log(x)`。

</v-click>

---

## Question 8

**Which statement about Box-Cox is correct?**

- a. The basic version can handle any negative input directly
- b. The basic version requires strictly positive input
- c. Box-Cox is only used for categorical variables
- d. Box-Cox always maps data to `[0,1]`

<v-click>

参考答案： `b`

解析：标准版 Box-Cox 的输入条件是 `x > 0`，这类边界条件很适合出选择题。

</v-click>

---

## Question 9

**Which option best distinguishes `pd.cut()` from `pd.qcut()`?**

- a. `cut()` creates equal-frequency bins, while `qcut()` creates equal-width bins
- b. `cut()` creates equal-width bins, while `qcut()` creates bins based on sample quantiles
- c. `cut()` is only for integers, while `qcut()` is only for floats
- d. `cut()` preserves outliers, while `qcut()` removes them

<v-click>

参考答案： `b`

解析：equal-width vs equal-depth / quantile-based binning 是 week9 的核心辨析点。

</v-click>

---

## Question 10

**What is the main advantage of stratified sampling over simple random sampling in the wine quality example?**

- a. It guarantees more total records
- b. It preserves the original class proportions across samples
- c. It removes noise from numeric features
- d. It transforms labels into continuous values

<v-click>

参考答案： `b`

解析：当 label 分布不平衡时，stratified sampling 更能保住原始 class mix。

</v-click>

---
layout: section
---

# Week 10

Data Integration & Enrichment

---

### Week 10 (10 题)

- 范围：integration vs enrichment, schema integration, data-level integration, matching, pandas merge/join/concat
- 目标：看到 source conflict 和 use case，就知道在考哪一层 integration

## Question 1

**Which option best describes the main purpose of data enrichment?**

- a. To remove duplicate records across multiple tables
- b. To append relevant external information that adds context and value
- c. To standardize all source schemas into a mediated schema
- d. To reduce the number of attributes before modeling

<v-click>

参考答案： `b`

解析：enrichment 是“补上下文”，integration 是“合成统一视图”，两者不能混。

</v-click>

---

## Question 2

**Which statement best distinguishes data integration from data enrichment?**

- a. Integration increases value, while enrichment ensures schema consistency
- b. Enrichment combines multiple sources, while integration only cleans one dataset
- c. Integration creates a unified dataset from multiple sources, while enrichment adds useful detail to existing records
- d. There is no practical difference between them

<v-click>

参考答案： `c`

解析：这是 week10 第一组最核心的概念区分题。

</v-click>

---

## Question 3

**Which of the following is the best example of an incompatible taxonomy problem in data integration?**

- a. One source stores dates as strings and another as timestamps
- b. One source defines `customer` as an individual, while another defines it as an account holder group
- c. One source has missing values in a postcode field
- d. One source contains duplicate rows caused by manual entry

<v-click>

参考答案： `b`

解析：taxonomy conflict 是 conceptual definition 不一致，不只是 format 不同。

</v-click>

---

## Question 4

**In schema integration, `Customer ID` and `Client ID` referring to the same concept is an example of:**

- a. Homonyms
- b. Synonyms
- c. Structural conflict
- d. Abstraction conflict

<v-click>

参考答案： `b`

解析：different names, same meaning 属于 synonym；反过来 same name, different meaning 才是 homonym。

</v-click>

---

## Question 5

**A mediated schema is mainly used to:**

- a. Remove all null values before analysis
- b. Provide a unified representation across multiple heterogeneous source schemas
- c. Replace machine learning with manual rules
- d. Convert categorical data into numeric form

<v-click>

参考答案： `b`

解析：mediated schema 是 schema integration 的中心对象，不是 cleaning 工具。

</v-click>

---

## Question 6

**Which option is an example of a one-to-many schema mapping?**

- a. `Movies.title` maps to `Items.name`
- b. `Movies.year` maps to `Items.year`
- c. `Items.price` maps to `Products.basePrice × (1 + Locations.taxRate)`
- d. `Customer ID` maps to `Customer ID`

<v-click>

参考答案： `c`

解析：一个 target value 由多个 source attributes 推导出来，就是 one-to-many mapping。

</v-click>

---

## Question 7

**Which pairing is correct for data-level integration categories?**

- a. Attribute-level: duplicate tuples; Tuple-level: correlated variables
- b. Attribute-level: redundancy and correlation; Tuple-level: duplication and inconsistency
- c. Attribute-level: schema mapping; Tuple-level: naming conflicts
- d. Attribute-level: enrichment; Tuple-level: normalization

<v-click>

参考答案： `b`

解析：attribute-level 看变量关系；tuple-level 看 records 本身是否重复或冲突。

</v-click>

---

## Question 8

**In a chi-square test for two categorical variables, if the computed statistic is greater than the critical value at the chosen significance level, what should you conclude?**

- a. Accept the null hypothesis that the variables are independent
- b. Reject the null hypothesis and conclude the variables are associated
- c. Conclude the sample size is too small to analyze
- d. Conclude the variables have a perfect linear relationship

<v-click>

参考答案： `b`

解析：超过 critical value 就 reject independence，这是 attribute-level integration 的经典题型。

</v-click>

---

## Question 9

**Which set contains all three basic edit-distance operations discussed in Week 10?**

- a. Insert, delete, substitute
- b. Sort, merge, split
- c. Trim, lowercase, tokenize
- d. Encode, hash, compare

<v-click>

参考答案： `a`

解析：edit distance 的三种基本操作非常适合出 definitions / methods 题。

</v-click>

---

## Question 10

**In the applied pandas materials, which statement is correct?**

- a. `merge` is mainly for stacking DataFrames row-wise without keys
- b. `join` is especially convenient for combining DataFrames on their index
- c. `concat` automatically resolves entity duplicates using similarity matching
- d. The default `merge` type is full outer join

<v-click>

参考答案： `b`

解析：`join` 偏 index-based，`merge` 偏 key-based，`concat` 只是拼接，不会自动做 semantic matching。

</v-click>

---
layout: section
---

# Week 11

Data Validation

---

### Week 11 (10 题)

- 范围：structural / content / logical validation, error handling, healthcare applied session
- 目标：知道“哪种 validation 在检查什么”，也知道 notebook 里实际查了什么

## Question 1

**Which type of validation checks whether `Age` is stored as an integer and whether a date field follows the expected format?**

- a. Structural validation
- b. Content validation
- c. Logical validation
- d. Error handling

<v-click>

参考答案： `a`

解析：data type、format、schema 都属于 structural validation。

</v-click>

---

## Question 2

**A hospital record has a negative `Billing Amount`. What is the best immediate response?**

- a. Delete the row because billing must always be positive
- b. Convert the value to its absolute value
- c. Investigate the business context because refunds or overpayments may explain it
- d. Treat it as a missing value

<v-click>

参考答案： `c`

解析：negative billing amount 很可能 unusual，但未必 wrong；这里考的是 validation 里的 business reasoning。

</v-click>

---

## Question 3

**Which check is the best fit for validating a `Blood Type` column?**

- a. Ensure values are in an allowed set such as `A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`
- b. Ensure the column has no whitespace in its header
- c. Ensure the file size is below a threshold
- d. Ensure the dataset has more than 100 rows

<v-click>

参考答案： `a`

解析：allowed set / list validation 是 content validation 的典型任务。

</v-click>

---

## Question 4

**The notebook found `0` missing values in every column. What is the most justified conclusion?**

- a. The dataset is fully clean and needs no further checks
- b. Missingness is not the main issue, but other data quality problems may still exist
- c. Structural validation is complete, so logical validation is unnecessary
- d. Duplicate detection can be skipped

<v-click>

参考答案： `b`

解析：没有 missing values 不代表没有 duplicates、inconsistencies 或 invalid content。

</v-click>

---

## Question 5

**The dataset had 55,500 rows and 534 exact duplicate rows. How many rows remain after removing duplicates?**

- a. 54,866
- b. 54,946
- c. 54,966
- d. 55,034

<v-click>

参考答案： `c`

解析：这是 applied session 里的直接结果题，`55,500 - 534 = 54,966`。

</v-click>

---

## Question 6

**Two rows have the same patient name, admission date, doctor, hospital, billing amount, and discharge date, but different `Age` values. What is the best interpretation?**

- a. They must be two separate valid visits
- b. They are harmless duplicates and both should be kept
- c. At least one field is inconsistent and should be investigated
- d. The age field is missing

<v-click>

参考答案： `c`

解析：这提醒我们“重复样子”背后可能是 content inconsistency，不是只会机械去重。

</v-click>

---

## Question 7

**In the applied session, checking whether `Date of Admission` is later than `Discharge Date` is treated as an example of:**

- a. Structural validation
- b. Content validation
- c. Logical validation
- d. File type validation

<v-click>

参考答案： `c`

解析：这类时间先后关系检查属于 business / temporal logic。

</v-click>

---

## Question 8

**What is the main risk of comparing dates as strings instead of converting them to `datetime` values first?**

- a. Duplicate rows cannot be detected
- b. The comparison may be wrong when date formats are inconsistent
- c. Missing values will become duplicates
- d. Numeric columns will be converted to strings

<v-click>

参考答案： `b`

解析：string comparison 只有在格式完全标准化时才可靠，格式一混就可能出错。

</v-click>

---

## Question 9

**In the lecture example, which validation method would best catch an email like `adam_1@wrongformat`?**

- a. Required field check
- b. Pattern matching
- c. Duplicate removal
- d. File size validation

<v-click>

参考答案： `b`

解析：pattern matching，通常配合 regex，是 content validation 的典型做法。

</v-click>

---

## Question 10

**A validation issue keeps reappearing every week even after analysts manually fix the affected rows. Which error-handling action best addresses the real problem?**

- a. Hide the error from users
- b. Focus only on reporting the latest failure
- c. Perform root cause analysis and add preventive measures
- d. Ignore the issue if the dataset is large

<v-click>

参考答案： `c`

解析：error handling 不只是修当前错误，更重要的是防止同类错误反复出现。

</v-click>

---
layout: default
---

# 最后怎么用这套题

- 先按 week 做：每周先自己答，再点开解析
- 再按主题复盘：`dimension vs measure`
- 再按主题复盘：`MCAR vs MAR`
- 再按主题复盘：`integration vs enrichment`
- 再按主题复盘：`structural vs content vs logical validation`
- 最后回头看 Quiz 2 真题信号：真题特别爱考“场景判断”
- 最后回头看 Quiz 2 真题信号：applied session 细节也会变成选择题

---
layout: end
---

# End

Week 6-11 quiz bank ready
