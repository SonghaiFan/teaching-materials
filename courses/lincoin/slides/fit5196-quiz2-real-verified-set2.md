---
theme: apple-basic
title: FIT5196 Quiz 2 真题版 Set 2 校对与解析
layout: intro
---

# FIT5196 Quiz 2

真题版 Set 2 校对与解析

---
layout: default
---

# 说明

- 原始题干与选项来自 `2025_5196_S1_Quiz2 2.pdf` 的第二套题
- 这一版按课程内容复核了参考答案，并补上简洁解析
- 我修正了几道明显不合理的原始答案，尤其是 `Q6`、`Q8`、`Q9`、`Q27`

---

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
layout: end
---

# End

Verified real-question set 2
