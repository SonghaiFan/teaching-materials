---
theme: apple-basic
title: FIT5196 Quiz 2 真题版 Set 1 校对与解析
layout: intro
---

# FIT5196 Quiz 2

真题版 Set 1 校对与解析

---
layout: default
---

# 说明

- 这份文件基于 [fit5196-quiz2-real.md](/Users/songhaifan/Documents/GitHub/teaching-materials/courses/lincoin/slides/fit5196-quiz2-real.md) 做答案校对
- 原始题干与选项来自 `2025_5196_S1_Quiz2 2.pdf` 的第一整套 `50` 题
- 这里的 `参考答案` 是按课程知识主线复核后的版本
- 我保留了少数有歧义题的说明，避免把模糊题硬写成唯一标准答案
- 明确修正的题包括：`Q16`、`Q45`

---

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
layout: end
---

# End

Verified real-question set 1
