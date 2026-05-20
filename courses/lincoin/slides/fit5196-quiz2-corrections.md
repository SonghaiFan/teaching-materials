---
theme: apple-basic
title: FIT5196 Quiz 2 总纠错讲解版
layout: intro
---

# FIT5196 Quiz 2

总纠错讲解版


---
layout: default
---

# 这份总讲解版怎么用

- 内容来源：`2025_5196_S1_Quiz2 2.pdf` 的三套真题
- 结构：按 `Set 1 -> Set 2 -> Set 3` 保持原卷顺序
- 每题都给出复核后的 `参考答案` 和简洁解析
- 目标不是背答案，而是看清每道题在考哪个知识点


---
layout: default
---

# 这次我重点修正了什么

- Set 1：明确修正 `Q16`、`Q45`
- Set 2：明确修正 `Q6`、`Q8`、`Q9`、`Q27`
- Set 3：明确修正 `Q8`、`Q13`、`Q49`
- 另外保留了少数歧义题的说明，例如某些结构题和 transformation 题


---
layout: section
---

# Set 1

Quiz 2 corrected walkthrough


---
layout: default
---

# Set 1 讲解重点

- 这一套保持原卷顺序，方便你按真实做题节奏复盘
- 重点关注我修正或特别说明的题：`Q16、Q45`
- 遇到多选题时，先判断题目在考定义、场景还是方法边界


## Question 1

**You are applying a log transformation with base 10 to the data set[10, 100, 1000]**

- a. [2, 3, 4]
- b. [0, 1, 2]
- c. [1, 2, 3]
- d. [10, 100, 1000]

<v-click>

参考答案： `c`

解析：`log10(10)=1`，`log10(100)=2`，`log10(1000)=3`。

</v-click>

---

## Question 2

**What are the best practices for documenting the data cleaning process? (Select all that apply)**

- a. Version control for datasets
- b. Recording the reasons for excluding data
- c. Detailed logging of all transformations
- d. Independent audits of the cleaning process

<v-click>

参考答案： `a, b, c, d`

解析：前 3 项直接提升可追溯性，`d` 更偏治理与质量保证，但仍属于良好的 documentation / review practice。

</v-click>

---

## Question 3

**What are the key benefits of data integration?**

- a. Enhanced decision-making
- b. Better data accessibility
- c. Increased data storage
- d. Improved data consistency
- e. Reduced IT costs

<v-click>

参考答案： `a, b, d, e`

解析：integration 的核心收益是统一视图、提升可访问性和一致性；`c` 不是 benefit，`e` 可视为减少重复系统和维护成本的常见 side effect。

</v-click>

---

## Question 4

**What challenges might be encountered in data integration projects?**

- a. Data quality issues
- b. Limited storage capacity
- c. Different data update cycles
- d. Data security concerns
- e. Incompatible data formats

<v-click>

参考答案： `a, b, c, d, e`

解析：这些都可能成为实际 integration project 的阻碍，其中课程最强调的是质量问题、时间不同步和格式不兼容。

</v-click>

---

## Question 5

**Which techniques are used for categorical data transformation? (Select all that apply)**

- a. Frequency encoding
- b. Binary encoding
- c. Integer encoding
- d. One-hot encoding

<v-click>

参考答案： `a, b, c, d`

解析：这 4 项都是常见的 categorical encoding / transformation 方法。

</v-click>

---

## Question 6

**What are the effects of high cardinality in categorical features on machine learning models? (Select all that apply)**

- a. Reduced predictive performance
- b. Slower computation times
- c. Increased model complexity
- d. Overfitting

<v-click>

参考答案： `a, b, c, d`

解析：高基数类别会让特征空间变大、计算更慢，也更容易学到噪声。

</v-click>

---

## Question 7

**In which data structures is the depth-first search (DFS) typically used?**

- a. Stack
- b. Tree
- c. Graph
- d. Array
- e. Queue

<v-click>

参考答案： `a, b, c`

解析：课程出题习惯里会把 `stack` 也算进去，因为 DFS 通常靠 stack 或 recursion 实现，而真正最典型的搜索对象是 tree 和 graph。

</v-click>

---

## Question 8

**Which issues are directly addressed by cleaning unstructured text data? (Select all that apply)**

- a. Semantic tagging
- b. Grammar improvements
- c. Spelling corrections
- d. Removal of stop words and stemming

<v-click>

参考答案： `c, d`

解析：text cleaning 更常处理 spelling、token normalization、stop words、stemming；semantic tagging 不属于典型 cleaning 动作。

</v-click>

---

## Question 9

**Which of the following data structures allow for efficient full-text search?**

- a. Suffix array
- b. Suffix tree
- c. Binary tree
- d. Trie
- e. Array

<v-click>

参考答案： `a, b, d`

解析：suffix array、suffix tree、trie 都是经典的 text indexing / retrieval 结构。

</v-click>

---

## Question 10

**Which of the following are common indicators of data quality issues? (Select all that apply)**

- a. Duplicate entries
- b. Irregular cardinality in categorical data
- c. High correlation between independent variables
- d. Evenly distributed data

<v-click>

参考答案： `a, b`

解析：duplicate 和异常类别分布都是直接的质量信号；`c` 更偏建模问题，`d` 本身不是质量异常。

</v-click>

---

## Question 11

**What transformations are applied to datasets to fulfill the linearity assumption for linear regression? (Select all that apply)**

- a. Interaction features
- b. Logarithmic transformation
- c. Inverse transformation
- d. Polynomial features

<v-click>

参考答案： `b, c, d`

解析：log、inverse、polynomial 都是常见的非线性关系线性化方法；interaction 更常用于建模交互，而不是直接处理线性化。

</v-click>

---

## Question 12

**Which of the following are valid reasons to apply data transformations? (Select all that apply)**

- a. To meet the assumptions of parametric tests
- b. To improve model interpretability
- c. To balance class distribution
- d. To simplify relationships between variables

<v-click>

参考答案： `a, b, d`

解析：transformation 常用来满足统计假设、改善变量关系与解释性；`c` 更接近 sampling / resampling 问题。

</v-click>

---

## Question 13

**In dealing with missing data, which approaches might be considered appropriate depending on the scenario? (Select all that apply)**

- a. Removal of incomplete records
- b. Use of algorithmic predictive models
- c. Multivariate imputation
- d. Replacement with mode/median/midpoint

<v-click>

参考答案： `a, b, c, d`

解析：缺失值处理没有单一标准答案，删除、简单插补、模型插补、多变量插补都可能在不同场景下合理。

</v-click>

---

## Question 14

**Which data cleaning tasks might typically be automated? (Select all that apply)**

- a. Correcting misspellings using algorithms
- b. Anomaly detection
- c. Manual data entry
- d. Removal of duplicate records

<v-click>

参考答案： `a, b, d`

解析：自动化最适合规则性强或可建模的问题；manual data entry 当然不属于自动 cleaning。

</v-click>

---

## Question 15

**Which of the following are best practices for data validation?**

- a. Documenting validation rules
- b. Validating data from multiple sources
- c. Ignoring minor errors
- d. Automating validation checks
- e. Performing validation early in the data pipeline

<v-click>

参考答案： `a, b, d, e`

解析：validation 的关键词是早做、自动做、可追踪地做；忽略小错误会导致问题累积。

</v-click>

---

## Question 16

**What actions are generally considered best practices in data cleaning for large datasets? (Select all that apply)**

- a. Segmenting data into manageable parts
- b. Utilizing distributed computing frameworks
- c. Applying transformations in memory
- d. Using cloud-based tools for scalability

<v-click>

参考答案： `a, b, d`

解析：这题我修正了原答案。对 large datasets 来说，分块、分布式和 cloud scalability 才是通用 best practice；把全部变换都放进内存里通常不具备可扩展性。

</v-click>

---

## Question 17

**Which of these data structures can be non-linear?**

- a. Linked list
- b. Array
- c. Hash table
- d. Tree
- e. Graph

<v-click>

参考答案： `c, d, e`

解析：array 和 linked list 是典型 linear structures；hash table、tree、graph 都不属于线性顺序结构。

</v-click>

---

## Question 18

**In which data structures is binary search applicable for searching?**

- a. Unsorted array
- b. Linked list
- c. Sorted array
- d. Heap
- e. Binary search tree

<v-click>

参考答案： `c, e`

解析：binary search 依赖有序结构，所以 sorted array 和 BST 可以；unsorted array、heap、普通 linked list 不行。

</v-click>

---

## Question 19

**Which transformations are typically used to prepare data for clustering algorithms? (Select all that apply)**

- a. Standardisation
- b. PCA for dimension reduction
- c. Normalisation
- d. Encoding categorical variables

<v-click>

参考答案： `a, b, c, d`

解析：clustering 前常做 scaling、dimensionality reduction 和必要的 encoding。

</v-click>

---

## Question 20

**What are typical use cases for data integration?**

- a. Regulatory compliance
- b. Single view of customer
- c. Business intelligence
- d. Data backup
- e. Performance monitoring

<v-click>

参考答案： `a, b, c`

解析：课程里最典型的是 compliance、customer 360 和 BI；`d` 是 storage/backup 任务，`e` 虽可能受益于 integration，但不是这题最核心的 textbook use case。

</v-click>

---

## Question 21

**Which types of data inconsistencies must be addressed in data integration?**

- a. Language discrepancies
- b. Spatial variations
- c. Format inconsistencies
- d. Temporal misalignments
- e. Encoding differences

<v-click>

参考答案： `c, d, e`

解析：按课程主线，integration 最常被直接点名的是 format、time synchronization 和 encoding / representation differences；`a`、`b` 更像 taxonomy 或 abstraction 层面的延伸情形。

</v-click>

---

## Question 22

**A trie is used to store a dictionary of the words ["read", "reader", "red", "render"]. After all words are inserted, how many children does the node representing re have?**

- a. 1
- b. 4
- c. 3
- d. 2

<v-click>

参考答案： `c`

解析：前缀 `re` 后面分别走向 `a`、`d`、`n`，所以有 3 个 children。

</v-click>

---

## Question 23

**If a doubly linked list contains nodes with values [5, 9, 2, 6], and the head points to 5, what node will be accessed by moving next from the head and then prev?**

- a. 2
- b. 9
- c. 5
- d. 6

<v-click>

参考答案： `c`

解析：从 5 走 `next` 到 9，再走 `prev` 回到 5。

</v-click>

---

## Question 24

**Given an array arr = [3, 1, 4, 1, 5], which operation would sort the array in ascending order?**

- a. Insertion to a hash table and retrieval by keys
- b. Pushing elements onto a stack and then popping them
- c. Enqueuing and dequeuing in a priority queue
- d. Insertion to a binary tree followed by in-order traversal

<v-click>

参考答案： `d`

解析：按课程常见出题口径，`d` 是最标准答案，因为 BST 的 inorder traversal 会输出有序结果。严格说 `c` 在最小优先队列设定下也能得到升序输出，所以这题本身有一点歧义。

</v-click>

---

## Question 25

**If a hash table uses chaining to resolve collisions and the keys 12, 22, 32 are inserted into a hash table with 10 buckets, which bucket will have the most keys?**

- a. 1
- b. 3
- c. 2
- d. None, all will have the same number of keys

<v-click>

参考答案： `c`

解析：若 bucket index 用 `key mod 10`，则 `12, 22, 32` 都落在 bucket `2`。

</v-click>

---

## Question 26

**A trie is used to store the words ["cat", "can", "cap"]. What will be the content of the node representing the prefix ca?**

- a. Complete words only
- b. The entire alphabet
- c. A null pointer
- d. Pointers to 't', 'n', 'p'

<v-click>

参考答案： `d`

解析：前缀 `ca` 的下一层分支就是 `t`、`n`、`p`。

</v-click>

---

## Question 27

**What is the primary purpose of data structuring?**

- a. To reduce data storage costs
- b. To simplify data deletion processes
- c. To organize data in a logical and efficient manner
- d. To increase data processing times

<v-click>

参考答案： `c`

解析：week6 的中心思想就是让数据组织方式支持 efficient access、update 和 processing。

</v-click>

---

## Question 28

**Which of the following scenarios illustrates the use of data enrichment in healthcare?**

- a. Reducing the number of health records
- b. Storing patient data in a centralized database
- c. Encrypting patient communications
- d. Adding patient socioeconomic data to clinical data

<v-click>

参考答案： `d`

解析：enrichment 的关键词是给已有记录追加外部上下文。

</v-click>

---

## Question 29

**Which data structure is optimal for implementing a priority queue?**

- a. Linked list
- b. Hash table
- c. Array
- d. Binary heap

<v-click>

参考答案： `d`

解析：priority queue 最经典的底层结构就是 binary heap。

</v-click>

---

## Question 30

**In the context of data enrichment, what does the term 'data fusion' refer to?**

- a. Converting analog data to digital format
- b. Removing duplicate data from a dataset
- c. Combining data from multiple sources to create a more comprehensive dataset
- d. Encrypting data for security purposes

<v-click>

参考答案： `c`

解析：data fusion 的本质是多源信息融合，让记录更完整。

</v-click>

---

## Question 31

**Which data cleansing operation involves correcting data that does not conform to specified rules?**

- a. Data auditing
- b. Data integration
- c. Data formatting
- d. Validating and correcting errors

<v-click>

参考答案： `d`

解析：不符合规则的数据需要通过 validation + correction 来处理，而不是只审计或只整合。

</v-click>

---

## Question 32

**Why is it important to validate data types in a dataset?**

- a. To ensure correct data processing
- b. To reduce data size
- c. To enhance visualization
- d. To simplify data structure

<v-click>

参考答案： `a`

解析：类型错了，后续计算、比较、聚合都可能出错。

</v-click>

---

## Question 33

**If you apply the exponential transformation ​ f(x)=ex to the dataset[0, 1, 2], what results do you get? (Assumee≈2.718)**

- a. [1, 1.718, 2.718]
- b. [1, 2.718, 7.389]
- c. [0, 1, 2]
- d. [1, e, e2]

<v-click>

参考答案： `b`

解析：数值结果是 `[e^0, e^1, e^2] = [1, 2.718, 7.389]`。如果把 `d` 读成 `[1, e, e^2]`，它是符号形式上的等价写法；但按当前 PDF 选项展示，`b` 是最清楚的标准答案。

</v-click>

---

## Question 34

**Geospatial enrichment of data might include the addition of which of the following?**

- a. Postal codes
- b. Email addresses
- c. Usernames
- d. Phone numbers

<v-click>

参考答案： `a`

解析：postal codes 属于典型的 geographic / location context。

</v-click>

---

## Question 35

**Calculate the results of applying the inverse transformation f(x)=1/x​to the dataset[1, 2, 4].**

- a. [1, 0.5, 0.25]
- b. [0, 0.5, 0.25]
- c. [1, -0.5, -0.25]
- d. [1, 2, 4]

<v-click>

参考答案： `a`

解析：逐个求倒数即可：`1/1=1`，`1/2=0.5`，`1/4=0.25`。

</v-click>

---

## Question 36

**What is the result of effective data validation?**

- a. Improved data quality and integrity
- b. Increased data redundancy
- c. Reduced data size
- d. More complex data structure

<v-click>

参考答案： `a`

解析：validation 的直接价值就是提高数据的正确性、完整性和可用性。

</v-click>

---

## Question 37

**Stochastic regression imputation differs from simple regression imputation by adding:**

- a. A constant to all scores
- b. A fixed percentage to the missing values
- c. Predicted scores to the existing values
- d. Random residuals to the predicted values

<v-click>

参考答案： `d`

解析：week8 明确强调 stochastic regression 会加入 residual noise 来恢复一部分波动性。

</v-click>

---

## Question 38

**Data enrichment's impact on customer relationship management (CRM) systems is primarily seen in:**

- a. Increased system maintenance
- b. Decreased data storage needs
- c. Enhanced customer segmentation
- d. Reduced data accessibility

<v-click>

参考答案： `c`

解析：更多上下文通常最直接带来更好的 segmentation 和 personalization。

</v-click>

---

## Question 39

**Data enrichment can be critical for which type of analysis?**

- a. Diagnostic analysis
- b. Predictive analysis
- c. Descriptive analysis
- d. All of the above

<v-click>

参考答案： `d`

解析：enrichment 可以改善描述、解释和预测，不局限于一种分析类型。

</v-click>

---

## Question 40

**Which method is typically used to ensure data consistency?**

- a. Data hashing
- b. Consistency checks
- c. Data serialization
- d. Data mirroring

<v-click>

参考答案： `b`

解析：consistency 要靠 explicit checks / rules，而不是靠 hashing 或 mirroring。

</v-click>

---

## Question 41

**Data enrichment in financial services often involves adding which type of external data?**

- a. In-house transaction records
- b. Historical stock prices
- c. Consumer behaviour logs
- d. Employee performance metrics

<v-click>

参考答案： `b`

解析：题目强调的是外部市场背景信息，historical stock prices 最贴切。

</v-click>

---

## Question 42

**Which is not a method used for outlier detection?**

- a. 3σ edit rule
- b. Hampel identifier
- c. Cross-validation
- d. Median absolute deviation

<v-click>

参考答案： `c`

解析：cross-validation 是 model evaluation 技术，不是 outlier detection rule。

</v-click>

---

## Question 43

**What does the term "schema validation" refer to in data validation?**

- a. Ensuring data is consistent across multiple sources
- b. Ensuring data is within a specific range
- c. Ensuring data conforms to a specific structure or schema
- d. Ensuring data is free of duplicates

<v-click>

参考答案： `c`

解析：schema validation 看的就是 structure、types、required fields 这类约束。

</v-click>

---

## Question 44

**In data enrichment, what is the primary purpose of adding socio-demographic data to consumer profiles?**

- a. To comply with international data laws
- b. To increase data volume
- c. To improve targeting and personalization in marketing
- d. To simplify data architecture

<v-click>

参考答案： `c`

解析：socio-demographic variables 最常见的业务价值就是 segmentation、targeting 和 personalization。

</v-click>

---

## Question 45

**Outliers in a dataset are important because:**

- a. They simplify data analyses
- b. They may provide insights into abnormal conditions
- c. They are errors in the data
- d. They are always removed before analysis

<v-click>

参考答案： `b`

解析：这题我修正了原答案。week8 明确强调 outliers 不一定是错误，也不一定要删；它们往往能揭示异常行为、测量问题或特殊业务机制。

</v-click>

---

## Question 46

**Which is not a direct objective of a data audit?**

- a. Increase the quantity of data
- b. Assess data completeness
- c. Identify data quality issues
- d. Evaluate data consistency

<v-click>

参考答案： `a`

解析：data audit 的目的在于诊断数据健康状况，而不是增加数据量。

</v-click>

---

## Question 47

**What type of validation rule would you apply to ensure a date falls within a certain period?**

- a. Format check
- b. Range check
- c. Uniqueness check
- d. Null check

<v-click>

参考答案： `b`

解析：先后范围、上下界、允许区间都属于 range check。

</v-click>

---

## Question 48

**Which of the following checks ensures that data falls within a specified range?**

- a. Uniqueness check
- b. Consistency check
- c. Format check
- d. Range check

<v-click>

参考答案： `d`

解析：这题和上一题本质同一个知识点：range condition 对应 range check。

</v-click>

---

## Question 49

**Which of the following is an example of data enrichment in e-commerce?**

- a. Tracking number of items sold
- b. Adding user-generated content to product descriptions
- c. Listing available products
- d. Calculating total sales

<v-click>

参考答案： `b`

解析：user-generated content 是附加到已有产品记录上的新信息，符合 enrichment 的定义。

</v-click>

---

## Question 50

**Which process is essential before performing data enrichment to ensure compatibility of data sources?**

- a. Data indexing
- b. Data streaming
- c. Data normalization
- d. Data encryption

<v-click>

参考答案： `c`

解析：enrichment 前先把表示方式和字段语义尽量对齐，normalization / standardization 才能保证数据能接得上。

</v-click>

---
layout: section
---

# Set 2

Quiz 2 corrected walkthrough


---
layout: default
---

# Set 2 讲解重点

- 这一套保持原卷顺序，方便你按真实做题节奏复盘
- 重点关注我修正或特别说明的题：`Q6、Q8、Q9、Q27`
- 遇到多选题时，先判断题目在考定义、场景还是方法边界


## Question 1

**Which approach is commonly used to ensure the consistency of enriched data?**

- a. Data purging
- b. Data isolation
- c. Data masking
- d. Data validation

<v-click>

参考答案： `d`

解析：enrichment 之后最关键的是验证新增信息是否和原数据一致，`data validation` 最直接。

</v-click>

---

## Question 2

**In which scenarios is range checking particularly useful?**

- a. Validating age data in a demographic survey
- b. Ensuring numerical values are non-negative
- c. Ensuring email addresses are properly formatted
- d. Confirming that dates fall within a specific period
- e. Checking for duplicates in a dataset

<v-click>

参考答案： `a, b, d`

解析：range check 关注上下界和允许区间，不负责 email format 或 duplicate detection。

</v-click>

---

## Question 3

**Identify the preprocessing steps necessary for integrating multiple data sources: (Select all that apply)**

- a. Schema alignment
- b. Outlier removal
- c. Normalisation
- d. Record linkage

<v-click>

参考答案： `a, c, d`

解析：多源 integration 的核心准备工作是 schema 对齐、表示统一和 record/entity matching。

</v-click>

---

## Question 4

**Which of these are valid reasons to perform data cleaning? (Select all that apply)**

- a. To comply with data privacy standards
- b. To improve model accuracy
- c. To reduce computational costs
- d. To enhance data visualization

<v-click>

参考答案： `a, b, c, d`

解析：cleaner data 不只服务建模，也会提升治理、效率和可视化结果。

</v-click>

---

## Question 5

**Which techniques are used for identifying and correcting inconsistencies in data collected from multiple sources? (Select all that apply)**

- a. Rule-based cleaning
- b. Using checksums for data integrity
- c. Automatic data merging tools
- d. Manual inspection

<v-click>

参考答案： `a, b, c, d`

解析：多源不一致通常需要规则、工具和人工复核配合处理。

</v-click>

---

## Question 6

**Which of the following are reasons to document data validation processes?**

- a. To facilitate debugging
- b. To ensure repeatability
- c. To improve team collaboration
- d. To enhance data visualization
- e. For audit purposes

<v-click>

参考答案： `a, b, c, e`

解析：这题我修正了原答案。documentation 的核心价值是追踪、复现、协作和审计，`data visualization` 不是主要理由。

</v-click>

---

## Question 7

**Which of the following data structures allow for efficient full-text search?**

- a. Array
- b. Suffix tree
- c. Trie
- d. Binary tree
- e. Suffix array

<v-click>

参考答案： `b, c, e`

解析：suffix tree、trie、suffix array 都是经典的 text indexing 结构。

</v-click>

---

## Question 8

**Which statements are true regarding the use of PCA for data cleaning? (Select all that apply)**

- a. PCA can identify and remove outliers
- b. PCA automatically handles missing values
- c. PCA simplifies data by transforming it to new coordinate systems
- d. PCA can reduce the dimensionality of the data

<v-click>

参考答案： `c, d`

解析：这题我修正了原答案。PCA 不会自动处理 missing values，也不直接“remove outliers”；它主要是换坐标系和做降维。

</v-click>

---

## Question 9

**What are the signs that a dataset has been well-cleaned? (Select all that apply)**

- a. No missing values
- b. Data types are appropriate for each column
- c. Descriptive statistics before and after cleaning are similar
- d. Values fall within expected ranges

<v-click>

参考答案： `a, b, d`

解析：这题我修正了原答案。`c` 不是可靠标准，因为 cleaning 本来就可能显著改变统计摘要。

</v-click>

---

## Question 10

**Which types of data inconsistencies must be addressed in data integration?**

- a. Temporal misalignments
- b. Format inconsistencies
- c. Encoding differences
- d. Spatial variations
- e. Language discrepancies

<v-click>

参考答案： `a, b, c`

解析：课程最直接强调的是 time、format、encoding 这三类 integration inconsistency。

</v-click>

---

## Question 11

**Select the data transformation techniques that are suitable for handling outliers in data. (Select all that apply)**

- a. Trimming
- b. Winsorizing
- c. Log transformation
- d. Binning

<v-click>

参考答案： `a, b, c, d`

解析：这几种都可以降低异常值影响，只是适用目的和副作用不同。

</v-click>

---

## Question 12

**Which of the following data validation techniques can be used to handle missing values?**

- a. Imputation
- b. Leaving them as is
- c. Deletion of incomplete records
- d. Interpolation
- e. Flagging for review

<v-click>

参考答案： `a, c, d, e`

解析：处理 missing values 的常见做法包括补、删、插值和标记；“原样不动”不算处理技术。

</v-click>

---

## Question 13

**What practices are recommended when transforming data for use in logistic regression? (Select all that apply)**

- a. Encoding of categorical variables
- b. Scaling to unit variance
- c. Normalisation of continuous variables
- d. Logarithmic transformation of skewed features

<v-click>

参考答案： `a, b, d`

解析：logistic regression 前常做 encoding、scaling，以及对严重 skew 的变量做变换；`normalisation` 不是这里最核心的必选项。

</v-click>

---

## Question 14

**In dealing with missing data, which approaches might be considered appropriate depending on the scenario? (Select all that apply)**

- a. Use of algorithmic predictive models
- b. Replacement with mode/median/midpoint
- c. Removal of incomplete records
- d. Multivariate imputation

<v-click>

参考答案： `a, b, c, d`

解析：删除、简单插补、模型插补、多变量插补都可能合理，取决于 missingness 机制和分析目标。

</v-click>

---

## Question 15

**Which of the following are examples of consistency checks in data validation?**

- a. Cross-referencing customer IDs in different tables
- b. Verifying that all records have a unique identifier
- c. Checking for missing values
- d. Ensuring date formats are uniform
- e. Ensuring all prices are positive numbers

<v-click>

参考答案： `a, d, e`

解析：这题按课程的宽口径理解，`a` 是跨表一致性，`d` 和 `e` 是确保表示和数值规则一致；`b` 更像 uniqueness，`c` 更像 completeness。

</v-click>

---

## Question 16

**How can data validation contribute to data cleaning?**

- a. By ensuring data conforms to expected formats
- b. By removing duplicate records
- c. By identifying and correcting errors
- d. By normalizing data values
- e. By reducing the size of the dataset

<v-click>

参考答案： `a, b, c, d`

解析：validation 能帮助识别格式问题、重复和错误，并推动必要的 standardization / normalization。

</v-click>

---

## Question 17

**Identify effective methods to handle time-series data specific issues during data cleaning. (Select all that apply)**

- a. Decomposition of seasonal components
- b. Handling of time zone differences
- c. Smoothing noisy data
- d. Time alignment across different sources

<v-click>

参考答案： `a, b, c, d`

解析：time series 的清洗常常就落在 seasonality、noise、timezone 和 time alignment 上。

</v-click>

---

## Question 18

**Which techniques are used for categorical data transformation? (Select all that apply)**

- a. One-hot encoding
- b. Frequency encoding
- c. Binary encoding
- d. Integer encoding

<v-click>

参考答案： `a, b, c, d`

解析：这 4 项都是标准 categorical transformation 方法。

</v-click>

---

## Question 19

**Which of the following can be validated using format checks?**

- a. Order time
- b. Last name
- c. First name
- d. Email addresses
- e. Date formats

<v-click>

参考答案： `d, e`

解析：format check 典型对象就是 email、date、postcode 这类有明确结构模式的字段。

</v-click>

---

## Question 20

**What benefits do cloud-based data integration services offer?**

- a. High customizability
- b. Lower initial costs
- c. On-premises control
- d. Scalability
- e. Rapid deployment

<v-click>

参考答案： `b, d, e`

解析：cloud integration 的典型优势是低前期成本、弹性扩展和快速上线。

</v-click>

---

## Question 21

**Which tools or languages are commonly used for data validation in data science?**

- a. Python
- b. SQL
- c. R
- d. SPSS
- e. SAS

<v-click>

参考答案： `a, b, c, d, e`

解析：这些都可以承担 validation 工作，只是使用场景和流行度不同。

</v-click>

---

## Question 22

**Consider a linked list implemented with the following node values: ["node1", "node2", "node3", "node4"]. If node2 is deleted, what is the new value of node1.next?**

- a. "node4"
- b. "node3"
- c. "node1"
- d. "node2"

<v-click>

参考答案： `b`

解析：删掉 `node2` 后，`node1.next` 会直接跳到 `node3`。

</v-click>

---

## Question 23

**For a binary search tree containing the values [10, 5, 15, 3, 7], what is the result of a pre-order traversal?**

- a. [3, 5, 7, 10, 15]
- b. [15, 10, 7, 5, 3]
- c. [3, 5, 10, 15, 7]
- d. [10, 5, 3, 7, 15]

<v-click>

参考答案： `d`

解析：pre-order 是 root, left, right，所以顺序是 `10, 5, 3, 7, 15`。

</v-click>

---

## Question 24

**If a graph is represented using an adjacency matrix and contains 3 vertices with connections between 1-2 and 2-3, which cell in the matrix represents a connection between vertex 1 and vertex 2?**

- a. (3,1)
- b. (2,2)
- c. (1,3)
- d. (1,2)

<v-click>

参考答案： `d`

解析：邻接矩阵里顶点 1 到顶点 2 的连接就记录在 `(1,2)`。

</v-click>

---

## Question 25

**If 12, 22, 32 are inserted into a hash table with 10 buckets, which bucket will have the most keys?**

- a. None, all will have the same number of keys
- b. 1
- c. 3
- d. 2

<v-click>

参考答案： `d`

解析：若按 `key mod 10`，三者都落到 bucket `2`。

</v-click>

---

## Question 26

**Which data structure would you choose to efficiently find and adjust the median of a dataset as new data are continually added?**

- a. Heap
- b. Hash table
- c. Array
- d. Binary search tree

<v-click>

参考答案： `a`

解析：动态维护 median 的经典做法就是 two-heaps。

</v-click>

---

## Question 27

**Outliers in a dataset are important because:**

- a. They may provide insights into abnormal conditions
- b. They simplify data analyses
- c. They are always removed before analysis
- d. They are errors in the data

<v-click>

参考答案： `a`

解析：这题我修正了原答案。week8 明确强调 outliers 不一定是错误，也不一定必须删除，它们可能揭示异常机制。

</v-click>

---

## Question 28

**In a directed graph, what does an 'edge' represent?**

- a. A data value
- b. The maximum distance between two nodes
- c. A cycle in the graph
- d. A connection between two vertices

<v-click>

参考答案： `d`

解析：edge 表示两个 vertices 之间的连接关系。

</v-click>

---

## Question 29

**Pairwise deletion differs from list-wise deletion because it:**

- a. Cannot handle MCAR data
- b. Uses available cases for each analysis separately
- c. Is less commonly used in practice
- d. Handles outliers instead of missing data

<v-click>

参考答案： `b`

解析：pairwise deletion 会针对不同统计量使用不同的可用样本子集。

</v-click>

---

## Question 30

**What type of validation ensures that an integer field contains no null values?**

- a. Format check
- b. Null check
- c. Uniqueness check
- d. Range check

<v-click>

参考答案： `b`

解析：没有 null 值，对应的就是 null check。

</v-click>

---

## Question 31

**What is the definition of "Missing at Random (MAR)"?**

- a. Missing data is unrelated to the dataset
- b. The probability of missing data is predictable
- c. Missing data is a random subset of the dataset
- d. The probability of missing data is related to other measured variables but not to the values of the variable itself

<v-click>

参考答案： `d`

解析：MAR 的核心就是 missingness 依赖已观测变量，但不直接依赖该变量真实缺失值本身。

</v-click>

---

## Question 32

**Which is not a method used for outlier detection?**

- a. Hampel identifier
- b. 3σ edit rule
- c. Median absolute deviation
- d. Cross-validation

<v-click>

参考答案： `d`

解析：cross-validation 是模型评估方法，不是异常值检测方法。

</v-click>

---

## Question 33

**What does the term "schema validation" refer to in data validation?**

- a. Ensuring data is within a specific range
- b. Ensuring data is consistent across multiple sources
- c. Ensuring data is free of duplicates
- d. Ensuring data conforms to a specific structure or schema

<v-click>

参考答案： `d`

解析：schema validation 看的是结构、字段类型、required fields 等是否符合定义。

</v-click>

---

## Question 34

**For the dataset [9, 16, 25], apply a square root transformation. What are the results?**

- a. [81, 256, 625]
- b. [3, 4, 5]
- c. [9, 16, 25]
- d. [81, 64, 25]

<v-click>

参考答案： `b`

解析：逐个开方即可，得到 `[3, 4, 5]`。

</v-click>

---

## Question 35

**Which of the following is an example of a format check?**

- a. Ensuring no duplicate records exist
- b. Ensuring values are within a specified range
- c. Ensuring no values are null
- d. Ensuring all dates are in the format YYYY-MM-DD

<v-click>

参考答案： `d`

解析：format check 就是在验证数据是否符合规定表示格式。

</v-click>

---

## Question 36

**How does 'link prediction' benefit from data enrichment in social network analysis?**

- a. By simplifying the network structure
- b. By enhancing the visual appeal of the network graph
- c. By identifying potential new connections
- d. By reducing the number of connections

<v-click>

参考答案： `c`

解析：更多上下文特征能帮助模型发现潜在连接关系。

</v-click>

---

## Question 37

**What mechanism describes data missing at random?**

- a. Missingness of data depends on the observed data only
- b. Missingness is completely unpredictable
- c. Data is missing based on the observer’s decision
- d. Data is missing according to a preset pattern

<v-click>

参考答案： `a`

解析：这道题是 MAR 的另一种表述：missingness 依赖 observed data。

</v-click>

---

## Question 38

**What type of validation rule would you apply to ensure a date falls within a certain period?**

- a. Format check
- b. Range check
- c. Null check
- d. Uniqueness check

<v-click>

参考答案： `b`

解析：日期是否落在合法区间，本质上是 range check。

</v-click>

---

## Question 39

**Which data structure is primarily used for implementing undo functionality in software applications?**

- a. Tree
- b. Queue
- c. Graph
- d. Stack

<v-click>

参考答案： `d`

解析：undo 是典型的 LIFO 行为，所以用 stack。

</v-click>

---

## Question 40

**Which transformation technique is best for handling positive skewness in a dataset?**

- a. Square transformation
- b. Logarithmic transformation
- c. Inverse transformation
- d. Cube tail transformation

<v-click>

参考答案： `b`

解析：对正偏分布，log transform 是最经典、最常见的处理方式。

</v-click>

---

## Question 41

**List-wise deletion is a method used to handle:**

- a. Outliers
- b. Duplicate data
- c. Inconsistent data
- d. Missing data

<v-click>

参考答案： `d`

解析：listwise deletion 是缺失值处理方法，不是 outlier 或 duplicate 处理方法。

</v-click>

---

## Question 42

**In a heap data structure, the highest (or lowest) priority element is always found at the:**

- a. Middle
- b. End
- c. Leaf
- d. Root

<v-click>

参考答案： `d`

解析：heap 的 priority element 总在 root。

</v-click>

---

## Question 43

**What is the main challenge associated with data enrichment from multiple external sources?**

- a. Decreasing the data's lifespan
- b. Maintaining data accuracy and consistency
- c. Reducing the cost of data storage
- d. Increasing the speed of data processing

<v-click>

参考答案： `b`

解析：多源 enrichment 的真正难点是让新增信息仍然准确、一致且可信。

</v-click>

---

## Question 44

**What type of data structure would be most appropriate for a router's routing table?**

- a. Stack
- b. Queue
- c. Trie
- d. Vector

<v-click>

参考答案： `c`

解析：routing / prefix lookup 的典型结构就是 trie。

</v-click>

---

## Question 45

**What is a key benefit of data enrichment in predictive analytics?**

- a. Increased data redundancy
- b. Enhanced accuracy of predictions
- c. Simplified data queries
- d. Reduced data storage needs

<v-click>

参考答案： `b`

解析：额外上下文最直接的价值就是提升预测质量。

</v-click>

---

## Question 46

**What is the purpose of a consistency check in data validation?**

- a. To identify duplicate records
- b. To ensure data is within a specified range
- c. To verify that data entries are logically consistent with each other
- d. To ensure data conforms to a specific format

<v-click>

参考答案： `c`

解析：consistency check 的目标是看字段与字段、记录与记录之间是否逻辑协调。

</v-click>

---

## Question 47

**Which process is essential before performing data enrichment to ensure compatibility of data sources?**

- a. Data encryption
- b. Data streaming
- c. Data normalization
- d. Data indexing

<v-click>

参考答案： `c`

解析：做 enrichment 前先统一表示方式和结构，normalization / standardization 很关键。

</v-click>

---

## Question 48

**What is the main reason for performing a data backup before cleansing?**

- a. To comply with legal requirements
- b. To provide a safety net against data loss or corruption
- c. To speed up the cleansing process
- d. To increase data volume

<v-click>

参考答案： `b`

解析：backup 的目的就是保底，防止 cleansing 过程造成不可逆损失。

</v-click>

---

## Question 49

**What is the Big-O notation used to describe in the context of data structures?**

- a. Processing power required
- b. Duration of algorithm execution
- c. Complexity of operations
- d. Memory usage

<v-click>

参考答案： `c`

解析：Big-O 说的是 operation complexity 的增长级别，不只是“运行时间字面值”。

</v-click>

---

## Question 50

**Which technique is NOT commonly used in data enrichment?**

- a. Data minimisation
- b. Data fusion
- c. Data augmentation
- d. Data scrubbing

<v-click>

参考答案： `a`

解析：minimisation 的方向是减少数据，不属于 enrichment。

</v-click>

---
layout: section
---

# Set 3

Quiz 2 corrected walkthrough


---
layout: default
---

# Set 3 讲解重点

- 这一套保持原卷顺序，方便你按真实做题节奏复盘
- 重点关注我修正或特别说明的题：`Q8、Q13、Q49`
- 遇到多选题时，先判断题目在考定义、场景还是方法边界


## Question 1

**Which is a benefit of using software tools for data auditing?**

- a. Increased need for manual review
- b. Reduction in data transparency
- c. Increase in data redundancy
- d. Automatic scanning for common issues

<v-click>

参考答案： `d`

解析：software tools 的优势就是自动扫描和快速定位常见问题。

</v-click>

---

## Question 2

**Which data structures can be used to efficiently implement associative arrays (or maps)?**

- a. Array
- b. Trie
- c. Tree
- d. Linked list
- e. Hash table

<v-click>

参考答案： `b, c, e`

解析：tree 和 hash table 是最典型的 map 结构，trie 也可作为字符串键的映射结构。

</v-click>

---

## Question 3

**Select the correct data quality dimensions that data cleaning aims to improve: (Select all that apply)**

- a. Timeliness
- b. Accuracy
- c. Completeness
- d. Relevance
- e. Consistency

<v-click>

参考答案： `b, c, e`

解析：这题最标准的核心维度是 accuracy、completeness 和 consistency。

</v-click>

---

## Question 4

**Which techniques are used for categorical data transformation? (Select all that apply)**

- a. Integer encoding
- b. Binary encoding
- c. One-hot encoding
- d. Frequency encoding

<v-click>

参考答案： `a, b, c, d`

解析：这 4 种都属于 categorical transformation / encoding。

</v-click>

---

## Question 5

**How can data validation contribute to data cleaning?**

- a. By reducing the size of the dataset
- b. By removing duplicate records
- c. By ensuring data conforms to expected formats
- d. By normalizing data values
- e. By identifying and correcting errors

<v-click>

参考答案： `b, c, d, e`

解析：validation 最直接帮助 cleaning 的地方是格式检查、错误识别、重复发现，以及推动必要的标准化。

</v-click>

---

## Question 6

**Which factors determine the technique used for missing data imputation? (Select all that apply)**

- a. Urgency of the analysis
- b. Amount of missing data
- c. Pattern of missingness
- d. Data type (categorical or continuous)

<v-click>

参考答案： `b, c, d`

解析：缺失值处理方法最依赖 missingness pattern、缺失比例和变量类型。

</v-click>

---

## Question 7

**Which validation methods are used to ensure data integrity in relational databases?**

- a. Unique constraints
- b. Foreign key constraints
- c. Indexing
- d. Primary key constraints
- e. Check constraints

<v-click>

参考答案： `a, b, d, e`

解析：integrity 依靠各种约束；indexing 提升性能，但不是 integrity rule。

</v-click>

---

## Question 8

**What are the primary benefits of data normalisation? (Select all that apply)**

- a. To mitigate the influence of outliers
- b. To prevent data leakage
- c. To allow fair comparison between features
- d. To improve the convergence of machine learning algorithms

<v-click>

参考答案： `c, d`

解析：这题我修正了原答案。normalisation / scaling 的主价值是让不同尺度特征可比较，并帮助优化过程；它并不专门处理 outliers，也不负责防止 leakage。

</v-click>

---

## Question 9

**Which data structures support dynamic resizing?**

- a. Circular buffer
- b. Static array
- c. Hash table
- d. Linked list
- e. Dynamic array

<v-click>

参考答案： `c, d, e`

解析：static array 不能动态扩容，而 hash table、linked list 和 dynamic array 都可以在实现层面扩展。

</v-click>

---

## Question 10

**Which of the following can be considered as data validation techniques for time series data?**

- a. Validating time intervals
- b. Checking for missing timestamps
- c. Checking for duplicate timestamps
- d. Normalizing data values
- e. Ensuring chronological order

<v-click>

参考答案： `a, b, c, e`

解析：time series validation 重点看时间间隔、缺失、重复和顺序是否正确。

</v-click>

---

## Question 11

**Which of the following can be validated using format checks?**

- a. Order time
- b. Last name
- c. Date formats
- d. Email addresses
- e. First name

<v-click>

参考答案： `c, d`

解析：format check 最典型的对象就是日期、邮箱、邮编等有固定模式的字段。

</v-click>

---

## Question 12

**Which data structures are suitable for implementing a LIFO system?**

- a. Linked list
- b. Priority queue
- c. Queue
- d. Deque
- e. Stack

<v-click>

参考答案： `a, d, e`

解析：stack 最直接，deque 也可实现 LIFO，linked list 也常用作 stack 底层。

</v-click>

---

## Question 13

**Which types of data inconsistencies must be addressed in data integration?**

- a. Spatial variations
- b. Encoding differences
- c. Language discrepancies
- d. Temporal misalignments
- e. Format inconsistencies

<v-click>

参考答案： `b, d, e`

解析：这题我修正了原答案。课程最明确强调的是 encoding、time synchronization 和 format inconsistency。

</v-click>

---

## Question 14

**What are the suitable data structures for real-time data processing?**

- a. Stream
- b. Stack
- c. Priority queue
- d. Circular buffer
- e. Queue

<v-click>

参考答案： `a, c, d, e`

解析：real-time processing 常用 stream、queue、buffer，也可能用 priority queue 做调度。

</v-click>

---

## Question 15

**Which technologies facilitate real-time data integration?**

- a. Message brokers
- b. Stream processing frameworks
- c. Batch processing systems
- d. FTP servers
- e. Webhooks

<v-click>

参考答案： `a, b, e`

解析：message brokers、stream frameworks 和 webhooks 都是 real-time integration 的典型技术。

</v-click>

---

## Question 16

**Which methods are typically used to handle outliers in dataset? (Select all that apply)**

- a. Trimming data at specified percentiles
- b. Clustering to identify anomalies
- c. Applying robust scaling techniques
- d. Logarithmic transformation

<v-click>

参考答案： `a, b, c, d`

解析：这些都可以用于发现或减弱 outlier 的影响。

</v-click>

---

## Question 17

**What are typical use cases for data integration?**

- a. Business intelligence
- b. Regulatory compliance
- c. Data backup
- d. Performance monitoring
- e. Single view of customer

<v-click>

参考答案： `a, b, d, e`

解析：integration 的高频 use case 包括 BI、compliance、monitoring 和 customer 360；backup 不属于核心 use case。

</v-click>

---

## Question 18

**In which scenarios is range checking particularly useful?**

- a. Confirming that dates fall within a specific period
- b. Ensuring email addresses are properly formatted
- c. Validating age data in a demographic survey
- d. Checking for duplicates in a dataset
- e. Ensuring numerical values are non-negative

<v-click>

参考答案： `a, c, e`

解析：range check 看的是数值或时间是否落在允许区间，不管格式和重复。

</v-click>

---

## Question 19

**Which of the following data structures allow for efficient full-text search?**

- a. Suffix array
- b. Trie
- c. Binary tree
- d. Suffix tree
- e. Array

<v-click>

参考答案： `a, b, d`

解析：suffix array、trie、suffix tree 都适合 text retrieval。

</v-click>

---

## Question 20

**Which transformations are typically used to prepare data for clustering algorithms? (Select all that apply)**

- a. Encoding categorical variables
- b. PCA for dimension reduction
- c. Standardisation
- d. Normalisation

<v-click>

参考答案： `a, b, c, d`

解析：clustering 前通常要统一尺度、处理类别变量，并可能做降维。

</v-click>

---

## Question 21

**In dealing with missing data, which approaches might be considered appropriate depending on the scenario? (Select all that apply)**

- a. Multivariate imputation
- b. Removal of incomplete records
- c. Replacement with mode/median/midpoint
- d. Use of algorithmic predictive models

<v-click>

参考答案： `a, b, c, d`

解析：这些都属于常见 missing-data handling 方法。

</v-click>

---

## Question 22

**For a binary search tree containing the values [10, 5, 15, 3, 7], what is the result of a pre-order traversal?**

- a. [10, 5, 3, 7, 15]
- b. [3, 5, 10, 15, 7]
- c. [15, 10, 7, 5, 3]
- d. [3, 5, 7, 10, 15]

<v-click>

参考答案： `a`

解析：pre-order 是 root-left-right，所以结果是 `10, 5, 3, 7, 15`。

</v-click>

---

## Question 23

**A trie is used to store a dictionary of the words ["read", "reader", "red", "render"]. After all words are inserted, how many children does the node representing re have?**

- a. 1
- b. 3
- c. 4
- d. 2

<v-click>

参考答案： `b`

解析：前缀 `re` 后面走向 `a`、`d`、`n`，所以有 3 个 children。

</v-click>

---

## Question 24

**Given a stack, if you push the following sequence of elements: [5, 8, 2, 9], then pop two elements, what element is at the top of the stack?**

- a. 9
- b. 2
- c. 5
- d. 8

<v-click>

参考答案： `d`

解析：push 后顶端是 9；pop 两次去掉 9 和 2，新的 top 是 8。

</v-click>

---

## Question 25

**In a binary search tree, if you insert the elements in the order [30, 20, 40, 10, 25], which element will be the left child of the root after all insertions?**

- a. 25
- b. 20
- c. 10
- d. 40

<v-click>

参考答案： `b`

解析：root 是 30，它的 left child 必然是 20。

</v-click>

---

## Question 26

**Consider a priority queue where elements are integers with priorities corresponding to their values. If the elements 20, 15, 10, 5 are inserted, in what order will they be dequeued?**

- a. 10, 15, 5, 20
- b. 20, 15, 10, 5
- c. 15, 10, 20, 5
- d. 5, 10, 15, 20

<v-click>

参考答案： `b`

解析：如果数值越大优先级越高，就按 `20, 15, 10, 5` 出队。

</v-click>

---

## Question 27

**What is the primary purpose of data cleansing in data wrangling?**

- a. To duplicate data records for redundancy
- b. To create backup copies of data
- c. To enhance the aesthetic appeal of data
- d. To correct or remove corrupt or inaccurate records from a dataset

<v-click>

参考答案： `d`

解析：data cleansing 的核心目的就是修正或清除错误、不准确、无效的数据。

</v-click>

---

## Question 28

**What does data enrichment primarily involve?**

- a. Removing all data from a dataset
- b. Adding metadata to existing data
- c. Simplifying complex data structures
- d. Enhancing existing data with additional sources

<v-click>

参考答案： `d`

解析：enrichment 的关键词是为现有记录追加外部信息。

</v-click>

---

## Question 29

**Which of the following best describes 'feature engineering' in the context of data enrichment for machine learning?**

- a. Removing irrelevant features
- b. Encoding labels for classification
- c. Transforming raw data into useful features
- d. Selecting the best machine learning model

<v-click>

参考答案： `c`

解析：feature engineering 是从原始数据构造更有用的特征表示。

</v-click>

---

## Question 30

**Temporal data enrichment involves:**

- a. Adding timestamps to datasets
- b. Predicting future data points
- c. Removing outdated records
- d. Analyzing historical trends only

<v-click>

参考答案： `a`

解析：temporal enrichment 是给数据增加时间上下文。

</v-click>

---

## Question 31

**What is a common approach to handling outliers in data validation?**

- a. Transforming them
- b. Always removing them
- c. Always keeping them
- d. Ignoring them

<v-click>

参考答案： `a`

解析：相较于机械删除，transforming 或进一步 investigate 是更常见的合理做法。

</v-click>

---

## Question 32

**What is encapsulation in the context of a data structure?**

- a. Storing data within a set of functions
- b. Dividing data into modules
- c. Organizing data in a hierarchical manner
- d. Wrapping data and methods into a single unit

<v-click>

参考答案： `d`

解析：encapsulation 就是把数据和操作方法打包成一个整体。

</v-click>

---

## Question 33

**What is an outlier?**

- a. A duplicate data point
- b. A data point that fits well within the data set
- c. A missing data point
- d. A data point that deviates significantly from other observations

<v-click>

参考答案： `d`

解析：outlier 的定义就是明显偏离整体模式的观测值。

</v-click>

---

## Question 34

**In a binary search tree (BST), each node has how many children?**

- a. Up to three
- b. Up to two
- c. Zero or one
- d. Exactly one

<v-click>

参考答案： `b`

解析：BST 是 binary tree，所以每个节点最多两个 children。

</v-click>

---

## Question 35

**Why is it important to validate data types in a dataset?**

- a. To ensure correct data processing
- b. To enhance visualization
- c. To reduce data size
- d. To simplify data structure

<v-click>

参考答案： `a`

解析：类型不对会直接影响比较、聚合、建模和计算结果。

</v-click>

---

## Question 36

**What type of transformation would be best to normalise data with outliers?**

- a. Robust Scaler
- b. Min-Max scaler
- c. Min-Max scaling
- d. Decimal scaling

<v-click>

参考答案： `a`

解析：有明显 outliers 时，应优先考虑使用 median 和 IQR 的 robust scaling。

</v-click>

---

## Question 37

**If you apply the exponential transformation f(x)=e^x to the dataset [0, 1, 2], what results do you get? (Assume e≈2.718)**

- a. [1, 2.718, 7.389]
- b. [1, e, e2]
- c. [0, 1, 2]
- d. [1, 1.718, 2.718]

<v-click>

参考答案： `a`

解析：数值结果展开后就是 `[e^0, e^1, e^2] = [1, 2.718, 7.389]`。

</v-click>

---

## Question 38

**In a heap data structure, the highest (or lowest) priority element is always found at the:**

- a. End
- b. Root
- c. Middle
- d. Leaf

<v-click>

参考答案： `b`

解析：heap 的优先级元素总在 root。

</v-click>

---

## Question 39

**What is a key benefit of data enrichment in predictive analytics?**

- a. Reduced data storage needs
- b. Simplified data queries
- c. Increased data redundancy
- d. Enhanced accuracy of predictions

<v-click>

参考答案： `d`

解析：enrichment 最核心的 predictive benefit 就是更好的 predictive signal。

</v-click>

---

## Question 40

**In the context of data enrichment, what does the term 'data fusion' refer to?**

- a. Combining data from multiple sources to create a more comprehensive dataset
- b. Encrypting data for security purposes
- c. Removing duplicate data from a dataset
- d. Converting analog data to digital format

<v-click>

参考答案： `a`

解析：data fusion 就是多源融合，形成更完整的数据表示。

</v-click>

---

## Question 41

**What type of validation ensures that an integer field contains no null values?**

- a. Null check
- b. Range check
- c. Format check
- d. Uniqueness check

<v-click>

参考答案： `a`

解析：该字段是否为空，看的是 null check。

</v-click>

---

## Question 42

**Which of the following is true about doubly linked lists compared to singly linked lists?**

- a. They allow traversal only in one direction
- b. They can be traversed in both directions
- c. They use less memory
- d. They do not allow insertion of new nodes

<v-click>

参考答案： `b`

解析：doubly linked list 的核心区别就是同时有 `next` 和 `prev`。

</v-click>

---

## Question 43

**Which of the following is an example of data enrichment in e-commerce?**

- a. Listing available products
- b. Calculating total sales
- c. Tracking number of items sold
- d. Adding user-generated content to product descriptions

<v-click>

参考答案： `d`

解析：把用户生成内容追加到产品记录，是典型 enrichment。

</v-click>

---

## Question 44

**What is a 'hash function' used for in a hash table?**

- a. Sorting the elements
- b. Connecting nodes
- c. Encrypting data
- d. Distributing keys uniformly across the buckets

<v-click>

参考答案： `d`

解析：hash function 的目标是把键映射到 buckets，并尽量均匀分布。

</v-click>

---

## Question 45

**Which of these is not a standard step in the data cleansing process?**

- a. Data duplication
- b. Data validation
- c. Data verification
- d. Data transformation

<v-click>

参考答案： `a`

解析：duplication 不是 cleansing step，反而常常是要解决的问题。

</v-click>

---

## Question 46

**What is a data audit primarily used for in the context of data cleansing?**

- a. To prepare data for deletion
- b. To impress stakeholders
- c. To fulfill legal compliance
- d. To ensure accuracy, completeness, consistency, and reliability of data

<v-click>

参考答案： `d`

解析：data audit 的目的就是系统性评估数据健康状况。

</v-click>

---

## Question 47

**What is the primary purpose of data structuring?**

- a. To organize data in a logical and efficient manner
- b. To simplify data deletion processes
- c. To increase data processing times
- d. To reduce data storage costs

<v-click>

参考答案： `a`

解析：data structuring 的中心目标是支持高效组织、检索和处理。

</v-click>

---

## Question 48

**What is the result of effective data validation?**

- a. Improved data quality and integrity
- b. Reduced data size
- c. More complex data structure
- d. Increased data redundancy

<v-click>

参考答案： `a`

解析：validation 的直接收益就是更可靠、更可用的数据。

</v-click>

---

## Question 49

**What type of data transformation is typically used to correct constant variance issues in a dataset?**

- a. Log transformation
- b. Categorical encoding
- c. Box-Cox transformation
- d. Polynomial features

<v-click>

参考答案： `c`

解析：这题我补上并校正了缺失答案。variance stabilization 的标准教材答案更接近 Box-Cox；`log` 只是它的一个特例。

</v-click>

---

## Question 50

**List-wise deletion is a method used to handle:**

- a. Outliers
- b. Missing data
- c. Duplicate data
- d. Inconsistent data

<v-click>

参考答案： `b`

解析：listwise deletion 是删除带缺失值记录的 missing-data handling 方法。

</v-click>

---
layout: end
---

# End

Quiz 2 corrected master deck
