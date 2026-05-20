---
theme: apple-basic
title: FIT5196 Quiz 2 真题版 Set 3 校对与解析
layout: intro
---

# FIT5196 Quiz 2

真题版 Set 3 校对与解析

---
layout: default
---

# 说明

- 原始题干与选项来自 `2025_5196_S1_Quiz2 2.pdf` 的第三套题
- 这一版按课程内容复核了参考答案，并补上简洁解析
- 我重点修正了较可疑的题目，尤其是 `Q8`、`Q13`、`Q49`

---

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

Verified real-question set 3
