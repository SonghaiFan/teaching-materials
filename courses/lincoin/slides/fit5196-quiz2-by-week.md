---
theme: apple-basic
title: FIT5196 Quiz 2 by Week
info: |
  Week 6-11 real-question review deck, regrouped by topic and taught with recap slides.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# FIT5196 Quiz 2
## Week 6-11 真题整理版

按知识周次重组，方便课堂讲解、复习和串联核心概念。

---

## 使用说明

- 本套题来自 Quiz 2 真题，但这里按 `week6-11` 的教学顺序重排。
- 我去掉了明显有问题、歧义太大或重复价值不高的题。
- 每周开头先用一页 recap 对齐对应 lecture slide 的核心知识点。
- 点击后会展开 `参考答案` 和更详细的 `解析`。

---

---
layout: section
---

# Week 6: Data Structures

---

---
layout: two-cols-header
---

## Week 6: Data Structures Recap

::left::

### 这周要会

- Data structuring 的目标：让数据更易于存储、查找、更新和处理。
- Linear vs non-linear：array、linked list 是线性的；tree、graph、hash table 不是。
- 典型结构用途：BST 管有序查找，heap 管优先级，hash table 管快速精确查找，graph 管关系建模。

::right::

### 做题时先想

- 题目是在问“按什么规则组织数据”，还是在问“哪种操作最快”？
- 看到 sorted search、ordered insertion、traversal，优先想 BST。
- 看到 priority queue、top-k、scheduler，优先想 heap；看到 DFS / recursion，联想到 stack。

---

## Week 6 Quiz 1

**In which data structures is the depth-first search (DFS) typically used?**

- a. Stack
- b. Tree
- c. Graph
- d. Array
- e. Queue

<v-click>

参考答案： `a, b, c`

解析：这题不要只盯住“DFS 是一种算法”，还要想到它依赖的结构。DFS 最典型地运行在 tree 和 graph 上，而实现层面经常使用 stack 或 recursion，所以课程题里会把 stack 也算进来。array 和 queue 本身都不是 DFS 的典型承载对象，因此不选。

</v-click>

---

## Week 6 Quiz 2

**In which data structures is binary search applicable for searching?**

- a. Unsorted array
- b. Linked list
- c. Sorted array
- d. Heap
- e. Binary search tree

<v-click>

参考答案： `c, e`

解析：binary search 的关键前提是数据必须有序，或者结构本身能利用有序性质缩小搜索范围。sorted array 显然满足这一点；BST 也依靠左小右大的规则逐步缩小搜索空间。unsorted array、linked list 和 heap 都不具备这种标准 binary search 条件，所以不选。

</v-click>

---

## Week 6 Quiz 3

**Which of these data structures can be non-linear?**

- a. Linked list
- b. Array
- c. Hash table
- d. Tree
- e. Graph

<v-click>

参考答案： `c, d, e`

解析：non-linear structure 的关键是元素之间不是单一路径顺序排开的。array 和 linked list 都沿着一条线访问；hash table、tree 和 graph 则允许分支、映射或多连接关系，所以属于 non-linear。

</v-click>

---

## Week 6 Quiz 4

**In a heap data structure, the highest (or lowest) priority element is always found at the:**

- a. Middle
- b. End
- c. Leaf
- d. Root

<v-click>

参考答案： `d`

解析：heap 的核心不是左右大小顺序，而是父节点和子节点之间满足 priority rule，所以最高优先级或最低优先级元素一定放在 root。中间、末尾和叶子节点都不保证保存全局最优先级元素。做 heap 题时，先抓住一句话：`heap is for getting the top priority at the root`。

</v-click>

---

## Week 6 Quiz 5

**If a hash table uses chaining to resolve collisions and the keys 12, 22, 32 are inserted into a hash table with 10 buckets, which bucket will have the most keys?**

- a. 1
- b. 3
- c. 2
- d. None, all will have the same number of keys

<v-click>

参考答案： `c`

解析：只要 hashing 规则是 `key mod 10`，`12`、`22`、`32` 的余数都等于 `2`，所以会被 chaining 到同一个 bucket。题目真正想考的是 collision resolution 和 hash bucket 的定位，而不是链表本身。

</v-click>

---

## Week 6 Quiz 6

**What is the primary purpose of data structuring?**

- a. To reduce data storage costs
- b. To simplify data deletion processes
- c. To organize data in a logical and efficient manner
- d. To increase data processing times

<v-click>

参考答案： `c`

解析：week6 的主线不是“省空间”，而是“把数据组织得更好用”。data structuring 的核心价值在于 logical and efficient organisation，这样后续 search、update、processing 才能更高效。其他选项要么太窄，要么和课程主旨相反。

</v-click>

---

## Week 6 Quiz 7

**Which data structure is optimal for implementing a priority queue?**

- a. Linked list
- b. Hash table
- c. Array
- d. Binary heap

<v-click>

参考答案： `d`

解析：priority queue 的关键词是“每次都要高效拿到最高或最低优先级元素”。binary heap 正好支持高效插入和取顶，所以是标准答案。linked list 和 array 可以做，但性能通常不如 heap；hash table 又不维护优先级顺序。

</v-click>

---

## Week 6 Quiz 8

**For a binary search tree containing the values [10, 5, 15, 3, 7], what is the result of a pre-order traversal?**

- a. [3, 5, 7, 10, 15]
- b. [15, 10, 7, 5, 3]
- c. [3, 5, 10, 15, 7]
- d. [10, 5, 3, 7, 15]

<v-click>

参考答案： `d`

解析：pre-order traversal 的顺序固定是 root -> left -> right。以 `10` 为根，左子树是 `5, 3, 7`，右子树是 `15`，所以结果是 `[10, 5, 3, 7, 15]`。这类题不要背结果，要现场按 traversal rule 走一遍。

</v-click>

---

## Week 6 Quiz 9

**Which data structure is primarily used for implementing undo functionality in software applications?**

- a. Tree
- b. Queue
- c. Graph
- d. Stack

<v-click>

参考答案： `d`

解析：undo 功能体现的是 “最后一个操作先被撤销”，也就是典型的 LIFO。LIFO 对应 stack，所以答案是 `d`。如果题目变成 task scheduling 或 waiting line，才更可能联想到 queue。

</v-click>

---

## Week 6 Quiz 10

**What is a 'hash function' used for in a hash table?**

- a. Sorting the elements
- b. Connecting nodes
- c. Encrypting data
- d. Distributing keys uniformly across the buckets

<v-click>

参考答案： `d`

解析：hash function 不是为了排序，也不是为了加密。它的任务是把 key 映射到 buckets，并尽量分布均匀，从而减少 collision、提升查找效率。做题时看到 hash table，先想“映射”和“分布”，不要想“顺序”。

</v-click>

---

---
layout: section
---

# Week 7: Data Quality Foundations

---

---
layout: two-cols-header
---

## Week 7: Data Quality Foundations Recap

::left::

### 这周要会

- Data quality 关心数据是否准确、完整、一致、可靠。
- 常见异常与坏数据信号：duplicate、异常 cardinality、缺失、冲突记录。
- Data audit 的作用是先诊断问题，再决定后续 cleaning / management 动作。

::right::

### 做题时先想

- 先分清题目问的是 quality issue、anomaly，还是 management / audit 目标。
- 建模层面的统计现象，不一定等于 data quality problem。
- 凡是 audit 题，核心一般都围绕发现问题、评估完整性和一致性。

---

## Week 7 Quiz 1

**Which of the following are common indicators of data quality issues? (Select all that apply)**

- a. Duplicate entries
- b. Irregular cardinality in categorical data
- c. High correlation between independent variables
- d. Evenly distributed data

<v-click>

参考答案： `a, b`

解析：duplicate entries 和 irregular cardinality 都是很直接的数据质量警报，因为它们说明记录可能重复、类别可能被错误编码或清洗不一致。高 correlation 更像建模阶段的 multicollinearity 问题；evenly distributed data 本身并不代表质量差。

</v-click>

---

## Week 7 Quiz 2

**Which data cleaning tasks might typically be automated? (Select all that apply)**

- a. Correcting misspellings using algorithms
- b. Anomaly detection
- c. Manual data entry
- d. Removal of duplicate records

<v-click>

参考答案： `a, b, d`

解析：自动化最适合规则明确、可以算法化的 cleaning task，所以 misspelling correction、anomaly detection、duplicate removal 都常见于工具链里。manual data entry 不是 cleaning，而是数据录入过程。做题时先分“清洗动作”与“数据产生动作”。

</v-click>

---

## Week 7 Quiz 3

**Which is not a direct objective of a data audit?**

- a. Increase the quantity of data
- b. Assess data completeness
- c. Identify data quality issues
- d. Evaluate data consistency

<v-click>

参考答案： `a`

解析：data audit 的目标是检查完整性、一致性、质量问题，而不是让数据量变多。题目中的 `increase the quantity of data` 明显脱离 audit 的定义，所以是反向选项。

</v-click>

---

## Week 7 Quiz 4

**Which of these are valid reasons to perform data cleaning? (Select all that apply)**

- a. To comply with data privacy standards
- b. To improve model accuracy
- c. To reduce computational costs
- d. To enhance data visualization

<v-click>

参考答案： `a, b, c, d`

解析：cleaner data 几乎会同时提升多个方面：更容易合规、更能提高模型效果、更能减少无效计算，也会让图表更可信。这个题型常考“data cleaning 不只是为了建模”，所以四项都能成立。

</v-click>

---

## Week 7 Quiz 5

**Which is a benefit of using software tools for data auditing?**

- a. Increased need for manual review
- b. Reduction in data transparency
- c. Increase in data redundancy
- d. Automatic scanning for common issues

<v-click>

参考答案： `d`

解析：software tools 的优势在于自动扫描、批量检查、快速定位常见问题。它们通常减少手工排查负担，而不是增加 manual review、redundancy 或降低 transparency。做 audit 题时，看到 tool 的价值，通常联想到 automation。

</v-click>

---

## Week 7 Quiz 6

**Select the correct data quality dimensions that data cleaning aims to improve: (Select all that apply)**

- a. Timeliness
- b. Accuracy
- c. Completeness
- d. Relevance
- e. Consistency

<v-click>

参考答案： `b, c, e`

解析：这题按这门课的讲法，最核心的 quality dimensions 是 accuracy、completeness、consistency。timeliness 和 relevance 虽然在 broader data quality 框架里也常出现，但这套题的知识主轴更集中在前面三项。

</v-click>

---

## Week 7 Quiz 7

**Which of these is not a standard step in the data cleansing process?**

- a. Data duplication
- b. Data validation
- c. Data verification
- d. Data transformation

<v-click>

参考答案： `a`

解析：standard cleansing process 里会出现 validation、verification、transformation，但不会把 “data duplication” 当成一个步骤，因为 duplication 本身往往是问题。也就是说，题目考的是“问题”与“处理步骤”的区分。

</v-click>

---

## Week 7 Quiz 8

**What is a data audit primarily used for in the context of data cleansing?**

- a. To prepare data for deletion
- b. To impress stakeholders
- c. To fulfill legal compliance
- d. To ensure accuracy, completeness, consistency, and reliability of data

<v-click>

参考答案： `d`

解析：在 cleansing 语境下，data audit 的核心是系统性检查数据是否准确、完整、一致、可靠。它不是为了 impress stakeholder，也不是单纯为了删数据或只满足合规。做 audit 题时，优先抓“诊断数据健康度”。

</v-click>

---

---
layout: section
---

# Week 8: Data Cleansing

---

---
layout: two-cols-header
---

## Week 8: Data Cleansing Recap

::left::

### 这周要会

- Cleansing workflow：audit -> goals -> plan -> backup -> operations -> verification。
- Missing data 机制：MCAR、MAR、MNAR；处理方法包括 deletion、imputation、model-based methods。
- Outlier detection 常见规则：3σ、Hampel、IQR；异常值不等于一定删除。

::right::

### 做题时先想

- missing value 题先判断它在问机制、方法，还是方法的副作用。
- 看到 pairwise / listwise，先抓“样本是否对每个分析都一样”。
- 看到 outlier 题，先判断题目是在问 detection rule、handling technique，还是 outlier 的业务意义。

---

## Week 8 Quiz 1

**In dealing with missing data, which approaches might be considered appropriate depending on the scenario? (Select all that apply)**

- a. Removal of incomplete records
- b. Use of algorithmic predictive models
- c. Multivariate imputation
- d. Replacement with mode/median/midpoint

<v-click>

参考答案： `a, b, c, d`

解析：missing data 处理没有唯一正确方法，要根据 missingness、样本量、业务风险和分析目标来选。删除记录、简单插补、模型预测、多变量插补都可能合理，所以四项都选。题目真正考的是“方法库”而不是单一最佳答案。

</v-click>

---

## Week 8 Quiz 2

**Stochastic regression imputation differs from simple regression imputation by adding:**

- a. A constant to all scores
- b. A fixed percentage to the missing values
- c. Predicted scores to the existing values
- d. Random residuals to the predicted values

<v-click>

参考答案： `d`

解析：simple regression imputation 只给出一个预测值，会让数据显得过于平滑；stochastic regression imputation 会再加上随机 residual，让补出来的值保留一定波动性。课程里特别强调这一点，因为它更接近真实分布。

</v-click>

---

## Week 8 Quiz 3

**Which is not a method used for outlier detection?**

- a. 3σ edit rule
- b. Hampel identifier
- c. Cross-validation
- d. Median absolute deviation

<v-click>

参考答案： `c`

解析：3σ edit rule、Hampel identifier、MAD 都属于 outlier detection 家族。cross-validation 则是模型评估方法，用来估计泛化性能，不是拿来找异常值的。做题时先判断题目问的是 “数据规则” 还是 “建模流程”。

</v-click>

---

## Week 8 Quiz 4

**Outliers in a dataset are important because:**

- a. They simplify data analyses
- b. They may provide insights into abnormal conditions
- c. They are errors in the data
- d. They are always removed before analysis

<v-click>

参考答案： `b`

解析：outlier 不等于错误。week8 很重要的一点就是：异常值有时揭示的是异常业务状态、罕见事件、设备故障或新模式，因此它们可能非常有信息量。所以最稳的答案是 `they may provide insights into abnormal conditions`。

</v-click>

---

## Week 8 Quiz 5

**Select the data transformation techniques that are suitable for handling outliers in data. (Select all that apply)**

- a. Trimming
- b. Winsorizing
- c. Log transformation
- d. Binning

<v-click>

参考答案： `a, b, c, d`

解析：trimming、winsorizing、log transformation、binning 都可能用来减轻 outlier 对分析的影响，只是作用方式不同。trimming 是删，winsorizing 是截尾，log 是压缩尺度，binning 是降低精度与敏感度，所以四项都可以成立。

</v-click>

---

## Week 8 Quiz 6

**Which of the following data validation techniques can be used to handle missing values?**

- a. Imputation
- b. Leaving them as is
- c. Deletion of incomplete records
- d. Interpolation
- e. Flagging for review

<v-click>

参考答案： `a, c, d, e`

解析：处理 missing values 的手段包括 imputation、deletion、interpolation 和 flagging for review。`leaving them as is` 不算真正的处理方案，因为它只是把问题原样留在数据里。做 missing value 题时，看到“处理 technique”就优先排除被动不作为。

</v-click>

---

## Week 8 Quiz 7

**Pairwise deletion differs from list-wise deletion because it:**

- a. Cannot handle MCAR data
- b. Uses available cases for each analysis separately
- c. Is less commonly used in practice
- d. Handles outliers instead of missing data

<v-click>

参考答案： `b`

解析：pairwise deletion 和 listwise deletion 的差别在于样本使用方式。pairwise 会为每个统计分析单独使用当前可用的样本，因此不同统计量可能基于不同 sample base；listwise 则是一刀切地删掉任何有缺失的记录。

</v-click>

---

## Week 8 Quiz 8

**What is the definition of "Missing at Random (MAR)"?**

- a. Missing data is unrelated to the dataset
- b. The probability of missing data is predictable
- c. Missing data is a random subset of the dataset
- d. The probability of missing data is related to other measured variables but not to the values of the variable itself

<v-click>

参考答案： `d`

解析：MAR 的标准定义是：缺失概率和其他已观测变量有关，但不直接依赖该变量本身未观测的真实值。很多题会把 “random subset” 写得像对，但那更接近不严谨的口语说法，不是课程里的正式定义。

</v-click>

---

## Week 8 Quiz 9

**List-wise deletion is a method used to handle:**

- a. Outliers
- b. Duplicate data
- c. Inconsistent data
- d. Missing data

<v-click>

参考答案： `d`

解析：list-wise deletion 是专门处理 missing data 的方法，不是处理 outlier、duplicate 或 inconsistency 的方法。看到 listwise / pairwise，基本就已经锁定在 missing-value chapter 里了。

</v-click>

---

## Week 8 Quiz 10

**What is the main reason for performing a data backup before cleansing?**

- a. To comply with legal requirements
- b. To provide a safety net against data loss or corruption
- c. To speed up the cleansing process
- d. To increase data volume

<v-click>

参考答案： `b`

解析：backup 的真正意义不是加快清洗，也不是增加数据量，而是提供回滚和恢复能力。因为 cleansing 常涉及删除、替换、标准化，一旦操作失误，没有 backup 就可能造成不可逆损失。

</v-click>

---

---
layout: section
---

# Week 9: Data Transformation

---

---
layout: two-cols-header
---

## Week 9: Data Transformation Recap

::left::

### 这周要会

- Transformation 的目标是让数据更适合分析、建模与解释。
- Scaling / standardisation 处理尺度问题；power transformation 处理 skewness、linearity、variance。
- 还要会 discretisation、feature construction、sampling 的用途与区别。

::right::

### 做题时先想

- 先分清题目问的是 numerical scaling、categorical encoding，还是 feature construction。
- 看到 positive skewness，优先联想到 log；看到 clustering，优先联想到 scaling。
- 看到“满足模型假设”或“关系更线性”，优先考虑 transformation，而不是 cleaning。

---

## Week 9 Quiz 1

**You are applying a log transformation with base 10 to the data set[10, 100, 1000]**

- a. [2, 3, 4]
- b. [0, 1, 2]
- c. [1, 2, 3]
- d. [10, 100, 1000]

<v-click>

参考答案： `c`

解析：base 10 log transformation 只需要逐项取 `log10`。`10, 100, 1000` 分别变成 `1, 2, 3`，所以答案是 `c`。这类题先别被 transformation 这个词吓到，本质上就是基础函数计算。

</v-click>

---

## Week 9 Quiz 2

**Which techniques are used for categorical data transformation? (Select all that apply)**

- a. Frequency encoding
- b. Binary encoding
- c. Integer encoding
- d. One-hot encoding

<v-click>

参考答案： `a, b, c, d`

解析：frequency encoding、binary encoding、integer encoding、one-hot encoding 都是 categorical data transformation 的常见做法。题目考的是你是否知道 week9 不只处理 numerical scaling，也处理类别变量的表示转换。

</v-click>

---

## Week 9 Quiz 3

**What are the effects of high cardinality in categorical features on machine learning models? (Select all that apply)**

- a. Reduced predictive performance
- b. Slower computation times
- c. Increased model complexity
- d. Overfitting

<v-click>

参考答案： `a, b, c, d`

解析：high cardinality 会把类别空间拉得很大，结果通常是模型更复杂、计算更慢、更容易过拟合，甚至影响预测表现。所以四项都可能发生。做这类题时，记住核心逻辑：类别太多 -> 特征表示更稀疏、更复杂。

</v-click>

---

## Week 9 Quiz 4

**What transformations are applied to datasets to fulfill the linearity assumption for linear regression? (Select all that apply)**

- a. Interaction features
- b. Logarithmic transformation
- c. Inverse transformation
- d. Polynomial features

<v-click>

参考答案： `b, c, d`

解析：为了更接近 linear regression 的线性假设，常见手段包括 log、inverse 和 polynomial transformation。interaction features 当然也会改变模型形式，但它不是这题最核心的“把关系变得更线性”的标准答案。

</v-click>

---

## Week 9 Quiz 5

**Which of the following are valid reasons to apply data transformations? (Select all that apply)**

- a. To meet the assumptions of parametric tests
- b. To improve model interpretability
- c. To balance class distribution
- d. To simplify relationships between variables

<v-click>

参考答案： `a, b, d`

解析：data transformation 常用于满足 parametric assumptions、让变量关系更简单、也可能提升解释性。`balance class distribution` 则更像 resampling / class imbalance 处理，不是 transformation 的核心目的。

</v-click>

---

## Week 9 Quiz 6

**Which transformations are typically used to prepare data for clustering algorithms? (Select all that apply)**

- a. Standardisation
- b. PCA for dimension reduction
- c. Normalisation
- d. Encoding categorical variables

<v-click>

参考答案： `a, b, c, d`

解析：clustering 前通常要做 scaling，让距离计算更公平；若维度太高，还会做 PCA；若有类别变量，也需要先编码。所以这题四项都合理，考的是 clustering 前的常见准备动作。

</v-click>

---

## Week 9 Quiz 7

**Calculate the results of applying the inverse transformation f(x)=1/x​to the dataset[1, 2, 4].**

- a. [1, 0.5, 0.25]
- b. [0, 0.5, 0.25]
- c. [1, -0.5, -0.25]
- d. [1, 2, 4]

<v-click>

参考答案： `a`

解析：inverse transformation `f(x)=1/x` 逐项计算就行，所以 `[1, 2, 4]` 会变成 `[1, 0.5, 0.25]`。这题很基础，但它也提醒你：看到 transformation 题时，先确认是“概念判断”还是“直接算值”。

</v-click>

---

## Week 9 Quiz 8

**What practices are recommended when transforming data for use in logistic regression? (Select all that apply)**

- a. Encoding of categorical variables
- b. Scaling to unit variance
- c. Normalisation of continuous variables
- d. Logarithmic transformation of skewed features

<v-click>

参考答案： `a, b, d`

解析：logistic regression 常见的准备包括 categorical encoding、适当 scaling，以及对严重 skew 的特征做 log transform。题目里 `normalisation of continuous variables` 不一定错到完全不能做，但不是这门课在 logistic regression 语境下最核心、最稳的推荐项。

</v-click>

---

## Week 9 Quiz 9

**For the dataset [9, 16, 25], apply a square root transformation. What are the results?**

- a. [81, 256, 625]
- b. [3, 4, 5]
- c. [9, 16, 25]
- d. [81, 64, 25]

<v-click>

参考答案： `b`

解析：square root transformation 就是逐项开方，所以 `9, 16, 25` 分别得到 `3, 4, 5`。和 log / inverse 题一样，这类题先算，不需要过度解读。

</v-click>

---

## Week 9 Quiz 10

**Which transformation technique is best for handling positive skewness in a dataset?**

- a. Square transformation
- b. Logarithmic transformation
- c. Inverse transformation
- d. Cube tail transformation

<v-click>

参考答案： `b`

解析：positive skewness 最常见的处理方式是 logarithmic transformation，因为它会压缩右尾、拉近大值之间的距离。square 或 cube 反而可能把右尾拉得更长，不是首选。

</v-click>

---

---
layout: section
---

# Week 10: Data Integration & Enrichment

---

---
layout: two-cols-header
---

## Week 10: Data Integration & Enrichment Recap

::left::

### 这周要会

- Enrichment 是给已有记录加上下文；integration 是把多个来源整成一个统一视图。
- Schema-level 要处理 naming、format、encoding、time 等冲突。
- Data-level 要会 schema alignment、record linkage、matching、data fusion。

::right::

### 做题时先想

- 先判断题目在问“加信息”还是“拼来源”。
- 问 preprocessing / compatibility 时，常见答案是 schema alignment、normalisation、matching。
- integration 难点通常不是“有没有数据”，而是“数据能不能对齐并保持一致”。

---

## Week 10 Quiz 1

**What are the key benefits of data integration?**

- a. Enhanced decision-making
- b. Better data accessibility
- c. Increased data storage
- d. Improved data consistency
- e. Reduced IT costs

<v-click>

参考答案： `a, b, d, e`

解析：integration 的价值在于把分散数据变成统一可用的信息资产，因此更好的 accessibility、consistency 和 decision-making 都是自然收益。`increased data storage` 不是 benefit，本身甚至可能是成本；`reduced IT costs` 在课程语境里可以视作减少重复系统和维护代价带来的好处。

</v-click>

---

## Week 10 Quiz 2

**What are typical use cases for data integration?**

- a. Regulatory compliance
- b. Single view of customer
- c. Business intelligence
- d. Data backup
- e. Performance monitoring

<v-click>

参考答案： `a, b, c`

解析：regulatory compliance、single customer view、business intelligence 都是 textbook 级别的 data integration use cases。data backup 更偏基础设施任务；performance monitoring 虽可能借助 integration，但不是这题最核心的标准用例。

</v-click>

---

## Week 10 Quiz 3

**Which types of data inconsistencies must be addressed in data integration?**

- a. Language discrepancies
- b. Spatial variations
- c. Format inconsistencies
- d. Temporal misalignments
- e. Encoding differences

<v-click>

参考答案： `c, d, e`

解析：integration 真正常见的 inconsistency 包括 format inconsistency、temporal misalignment、encoding differences，因为这些都会直接妨碍数据拼接和统一解释。language discrepancy 或 spatial variation 有时也会出现，但不是这道题聚焦的主轴。

</v-click>

---

## Week 10 Quiz 4

**Which of the following scenarios illustrates the use of data enrichment in healthcare?**

- a. Reducing the number of health records
- b. Storing patient data in a centralized database
- c. Encrypting patient communications
- d. Adding patient socioeconomic data to clinical data

<v-click>

参考答案： `d`

解析：data enrichment 的定义是“给已有记录追加更多上下文”。在 healthcare 里，把 socioeconomic data 加到 clinical data 上正好符合这个定义；存储、加密、减少记录数量都不属于 enrichment。

</v-click>

---

## Week 10 Quiz 5

**In the context of data enrichment, what does the term 'data fusion' refer to?**

- a. Converting analog data to digital format
- b. Removing duplicate data from a dataset
- c. Combining data from multiple sources to create a more comprehensive dataset
- d. Encrypting data for security purposes

<v-click>

参考答案： `c`

解析：data fusion 就是把多个来源的信息融合成更完整的数据表示。它不是 digitisation、deduplication 或 encryption。看到 fusion 题时，优先联想到 multi-source combination。

</v-click>

---

## Week 10 Quiz 6

**In data enrichment, what is the primary purpose of adding socio-demographic data to consumer profiles?**

- a. To comply with international data laws
- b. To increase data volume
- c. To improve targeting and personalization in marketing
- d. To simplify data architecture

<v-click>

参考答案： `c`

解析：socio-demographic data 加到 consumer profile 中，最直接的业务价值就是 segmentation、targeting 和 personalization。它不是为了单纯增加 volume，也不是为了简化架构。

</v-click>

---

## Week 10 Quiz 7

**Which of the following is an example of data enrichment in e-commerce?**

- a. Tracking number of items sold
- b. Adding user-generated content to product descriptions
- c. Listing available products
- d. Calculating total sales

<v-click>

参考答案： `b`

解析：adding user-generated content to product descriptions 属于典型 enrichment，因为它是在原有产品记录上追加新信息。tracking items sold 或 calculating total sales 更像原始业务指标，不一定体现“补充外部或附加上下文”。

</v-click>

---

## Week 10 Quiz 8

**Which process is essential before performing data enrichment to ensure compatibility of data sources?**

- a. Data indexing
- b. Data streaming
- c. Data normalization
- d. Data encryption

<v-click>

参考答案： `c`

解析：在做 enrichment 之前，如果不同来源格式不统一、字段表示不一致，后面就很难可靠合并，所以 normalisation 是关键前置步骤。streaming、indexing、encryption 都不是这题要考的 compatibility 核心。

</v-click>

---

## Week 10 Quiz 9

**Identify the preprocessing steps necessary for integrating multiple data sources: (Select all that apply)**

- a. Schema alignment
- b. Outlier removal
- c. Normalisation
- d. Record linkage

<v-click>

参考答案： `a, c, d`

解析：多源 integration 的前处理常见于 schema alignment、normalisation 和 record linkage，因为你要先让字段能对齐、表示能兼容、实体能匹配。outlier removal 当然有时也会做，但它不是 integration-specific preprocessing 的核心项。

</v-click>

---

## Week 10 Quiz 10

**What is the main challenge associated with data enrichment from multiple external sources?**

- a. Decreasing the data's lifespan
- b. Maintaining data accuracy and consistency
- c. Reducing the cost of data storage
- d. Increasing the speed of data processing

<v-click>

参考答案： `b`

解析：从多个外部源 enrichment 时，最大难点通常不是数量，而是 accuracy 和 consistency。来源越多，冲突、噪声和语义不一致就越多，所以维护可信度才是重点。

</v-click>

---

---
layout: section
---

# Week 11: Data Validation

---

---
layout: two-cols-header
---

## Week 11: Data Validation Recap

::left::

### 这周要会

- Validation 常见检查：schema、type、null、format、range、consistency、uniqueness。
- 关系型场景还要会 primary key、foreign key、check constraints 等 integrity rules。
- Validation 要尽量早做、自动做、文档化，避免错误一路流进后续流程。

::right::

### 做题时先想

- 先识别题目是在问哪一类检查：null、range、format 还是 consistency。
- 如果是“字段之间是否逻辑协调”，通常是 consistency；如果是“结构是否符合定义”，通常是 schema。
- time series validation 常关注时间间隔、顺序、缺失时间戳和重复时间戳。

---

## Week 11 Quiz 1

**Which of the following are best practices for data validation?**

- a. Documenting validation rules
- b. Validating data from multiple sources
- c. Ignoring minor errors
- d. Automating validation checks
- e. Performing validation early in the data pipeline

<v-click>

参考答案： `a, b, d, e`

解析：这题把 validation best practice 几乎都列出来了：规则要文档化、检查要自动化、最好在 pipeline 早期进行，还要覆盖多来源数据。`ignoring minor errors` 明显违背 validation 的精神，因为小错误会在后面放大。

</v-click>

---

## Week 11 Quiz 2

**Which data cleansing operation involves correcting data that does not conform to specified rules?**

- a. Data auditing
- b. Data integration
- c. Data formatting
- d. Validating and correcting errors

<v-click>

参考答案： `d`

解析：题眼是 “does not conform to specified rules”。这类问题对应的是 validating and correcting errors，而不是只做 audit、integration 或 formatting。validation 在 week11 里是“检查并纠正”的动作。

</v-click>

---

## Week 11 Quiz 3

**Why is it important to validate data types in a dataset?**

- a. To ensure correct data processing
- b. To reduce data size
- c. To enhance visualization
- d. To simplify data structure

<v-click>

参考答案： `a`

解析：数据类型决定了一个字段能否被正确比较、聚合、计算或转换，所以 type validation 是最基础也最重要的验证之一。它不是为了减小数据量，也不是为了美化可视化。

</v-click>

---

## Week 11 Quiz 4

**What does the term "schema validation" refer to in data validation?**

- a. Ensuring data is consistent across multiple sources
- b. Ensuring data is within a specific range
- c. Ensuring data conforms to a specific structure or schema
- d. Ensuring data is free of duplicates

<v-click>

参考答案： `c`

解析：schema validation 检查的是数据是否符合预定义结构，比如 required fields、field types、nested shape 等。它和 range、duplicate、cross-source consistency 是不同层面的检查。

</v-click>

---

## Week 11 Quiz 5

**What type of validation rule would you apply to ensure a date falls within a certain period?**

- a. Format check
- b. Range check
- c. Uniqueness check
- d. Null check

<v-click>

参考答案： `b`

解析：如果要确保日期落在某个允许时间段内，本质上是在检查上下界，因此是 range check。format check 只会检查日期长得像不像日期，不会判断它是不是落在允许期间。

</v-click>

---

## Week 11 Quiz 6

**Which of the following can be validated using format checks?**

- a. Order time
- b. Last name
- c. First name
- d. Email addresses
- e. Date formats

<v-click>

参考答案： `d, e`

解析：format check 适合那些存在明确模式或语法的字段，例如 email address、date format、postcode。名字或普通文本字段通常没有这么严格的结构模板，所以不适合作为 format check 的典型例子。

</v-click>

---

## Week 11 Quiz 7

**What type of validation ensures that an integer field contains no null values?**

- a. Format check
- b. Null check
- c. Uniqueness check
- d. Range check

<v-click>

参考答案： `b`

解析：题目问的是 “contains no null values”，所以最直接的检查就是 null check。range、format、uniqueness 都是别的维度，不能直接回答“有没有空值”。

</v-click>

---

## Week 11 Quiz 8

**What is the purpose of a consistency check in data validation?**

- a. To identify duplicate records
- b. To ensure data is within a specified range
- c. To verify that data entries are logically consistent with each other
- d. To ensure data conforms to a specific format

<v-click>

参考答案： `c`

解析：consistency check 的重点不是单字段格式，而是多个字段、多个记录之间是否逻辑一致。比如 start date 不应晚于 end date、customer ID 在两张表中应能对应上，这类都属于 consistency thinking。

</v-click>

---

## Week 11 Quiz 9

**Which validation methods are used to ensure data integrity in relational databases?**

- a. Unique constraints
- b. Foreign key constraints
- c. Indexing
- d. Primary key constraints
- e. Check constraints

<v-click>

参考答案： `a, b, d, e`

解析：在 relational database 里，data integrity 主要靠 constraints 保证，例如 primary key、foreign key、unique 和 check。indexing 主要是性能工具，不直接承担 integrity rule 的职责。

</v-click>

---

## Week 11 Quiz 10

**Which of the following can be considered as data validation techniques for time series data?**

- a. Validating time intervals
- b. Checking for missing timestamps
- c. Checking for duplicate timestamps
- d. Normalizing data values
- e. Ensuring chronological order

<v-click>

参考答案： `a, b, c, e`

解析：time series validation 会特别关注时间间隔是否合理、timestamp 是否缺失或重复、记录是否保持时间顺序。normalizing values 可能是 transformation，但不属于 time-series-specific validation technique。

</v-click>

---
