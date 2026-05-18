---
theme: apple-basic
title: FIT5196 Week 10 - Data Integration and Enrichment
layout: intro
mdc: true
---

<style>
.compact-table table {
  width: 100%;
  table-layout: fixed;
  font-size: 0.8em;
  line-height: 1.22;
}

.compact-table th,
.compact-table td {
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: break-word;
  padding: 0.3rem 0.4rem;
}

.formula-box {
  background: rgba(15, 23, 42, 0.04);
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 0.75rem;
  padding: 0.9rem 1rem;
}

.small-note {
  font-size: 0.88em;
  color: #475569;
}
</style>

# FIT5196 Data Wrangling

## Week 10: Data Integration & Enrichment

---
layout: default
---

# 本周目标

| Learning Outcome | 你要会什么 |
|------|------|
| Explain enrichment vs integration | 能区分 enrichment 和 integration 的目标与输出 |
| Describe enrichment workflow | 能讲出 enrichment 的基本步骤 |
| Identify integration challenges | 能说明多源数据集成为什么难 |
| Understand schema integration | 能解释 schema、mapping、matching 和冲突类型 |
| Distinguish data-level integration methods | 能区分 attribute-level 与 tuple-level integration |
| Interpret core techniques | 能解释 chi-square、correlation、edit distance、rule-based / learning-based matching |

---
layout: statement
---

## Week 9 解决“单数据源怎么变得更可用”，Week 10 解决“多数据源怎么拼得起来、拼得对、拼得有价值”。

真正难的地方不是把数据放在一起，而是让它们在语义、结构和内容上都能协调工作。

---
layout: default
---

# 和上周怎么接上

上周重点：

- Data normalisation
- Data discretisation
- Data construction
- Data sampling

这周往前走一步：

- Data enrichment：给已有数据加上下文
- Data integration：把多个来源的数据整合成统一视图

<div class="small-note mt-3">
一句话：Week 9 更偏单表/单源整理，Week 10 更偏多源协同。
</div>

---
layout: section
---

# Part 1

# Enrichment & Integration

---
layout: default
---

# 什么是 Data Enrichment

Data enrichment 指：

- 向现有数据追加外部上下文或附加信息
- 提高数据的深度、质量和价值
- 让分析和决策更细、更准

常见增强内容：

- demographic information
- geographic details
- industry-specific metrics

---
layout: default
---

# Enrichment 在增强什么

| 维度 | 具体意思 |
|------|------|
| Contextual addition | 给原数据增加更有解释力的背景信息 |
| Quality improvement | 提升准确性、粒度、时效性 |
| Value enhancement | 让数据更适合分析和业务决策 |

---
layout: two-cols
---

# Data Enrichment

- 往已有记录上追加信息
- 目标是提升价值和上下文
- 结果是“更丰富的数据”

::right::

# Data Integration

- 合并多个来源的数据
- 目标是统一视图和一致性
- 结果是“整合后的数据集”

<div class="callout mt-4 text-sm">
记忆：`enrichment = 增加信息层`，`integration = 统一多个来源`。
</div>

---
layout: default
---

# Data Enrichment 步骤

```text
Define objectives -> Select data sources -> Integrate data
-> Ensure data quality -> Continuous updating
```

做法上通常对应：

1. 明确还缺什么信息
2. 选择可靠且相关的外部源
3. 通过 ETL 合并
4. 验证准确性、完整性、时效性
5. 持续更新，保持数据不过时

---
layout: default
---

# 真题演练

**A company adds postcode-level demographics to its customer table to improve targeting. This is primarily:**

| 选项 | 内容 |
|------|------|
| a | Data discretisation |
| b | Data enrichment |
| c | Tuple-level integration |
| d | Correlation analysis |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>这里的关键动作是“给现有记录追加外部上下文”，所以是 enrichment，不是单纯的 schema 或 row matching。
</div>

---
layout: default
---

# 什么是 Data Integration

Data integration 指：

- 组合不同来源的数据
- 创建统一视图
- 便于后续分析和决策

几个高频关键词：

- Source diversity
- Schema merging
- Entity resolution
- Centralization

---
layout: default
---

# 为什么 Data Integration 难

第一组挑战：

- Heterogeneous data：不同源独立开发，目标不同
- Various formats：text / logs / social / sensors / records
- Incompatible taxonomies：同一对象定义不一致
- Time synchronisation：不同时间窗口难对齐

---
layout: default
---

# 更多挑战

- Legacy data：历史格式和现代系统混在一起
- Abstraction levels：suburb vs state，annual vs weekly
- Data quality：坏数据会被“集成放大”
- Number of sources：来源越多，复杂度越高

<div class="callout mt-4 text-sm">
多源集成的难点，往往不是“有没有数据”，而是“这些数据讲的是不是同一件事”。
</div>

---
layout: default
---

# 一句话记忆：Enrichment vs Integration

- `Enrichment`：让已有数据更有信息量
- `Integration`：让多个来源的数据能统一工作
- enrichment 更像“加料”
- integration 更像“对齐、整合、消冲突”

---
layout: section
---

# Part 2

# Schema Integration

---
layout: default
---

# 什么是 Schema

Schema 在不同环境里可以长得不一样：

- Relational databases：表、属性、数据类型
- XML / JSON：tags、classes、properties
- Data science：数据安排、关系和内容的表示

<div class="small-note mt-3">
所以 schema 不只是“数据库建表语句”，而是“数据是怎么组织和表达的”。
</div>

---
layout: default
---

# 为什么需要 Schema Integration

因为不同数据源：

- 结构不同
- 字段命名不同
- 抽象层次不同
- 对同一实体的表达方式不同

我们需要一个 mediated schema，来把多源表示统一起来。

---
layout: two-cols-header
---

# Schema Mapping

::left::

Schema mapping 关心的是：

- source attribute 对应 mediated schema 的哪个属性
- source 中不同字段组合怎样被解释
- 冲突怎么被消解

::right::

常见类型：

- One-to-one
  - `Movies.title ≈ Items.name`
- One-to-many
  - `Items.price ≈ Products.basePrice × (1 + taxRate)`

---
layout: default
---

# Schema Integration 的三类典型问题

| 类型 | 典型问题 | 例子 |
|------|------|------|
| Structure conflicts | 结构表达不同 | XML vs JSON vs relational |
| Naming conflicts | 名字和语义不一致 | ID / Client ID / Customer ID |
| Entity resolution conflicts | 单位、类型、值、抽象层次不同 | Celsius vs Fahrenheit, Prof vs Professor |

---
layout: two-cols
---

# Naming Conflicts

- Homonyms：同名不同义
- Synonyms：异名同义

例子：

- `ID` 可能是 customer ID、product ID、store ID
- `Customer ID` 和 `Client ID` 可能其实是同一概念

::right::

# 做题最容易混

- `homonym`
  - one name -> many meanings
- `synonym`
  - many names -> one meaning

<div class="callout mt-4 text-sm">
背法：`homo = same form`，`syn = same meaning`。
</div>

---
layout: default
---

# Entity Resolution / Conflict Resolution

除了命名，还会碰到这些问题：

- Different units：Celsius vs Fahrenheit，USD vs EUR
- Data type heterogeneity：phone number 可能是 string 或 integer
- Value heterogeneity：Prof vs Professor，St vs Street
- Level of abstraction：地址可能被拆成多个字段
- Generalisation / Specialisation：`phone` vs `home/work/cell phone`
- Different points of time：fortnight vs monthly payment

---
layout: default
---

# 真题演练

**“Customer ID” and “Client ID” refer to the same real-world concept. This is an example of:**

| 选项 | 内容 |
|------|------|
| a | Homonym conflict |
| b | Synonym conflict |
| c | Time synchronisation issue |
| d | Equal-depth binning |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>名字不同，但指向同一个对象，所以是 synonym，不是 homonym。
</div>

---
layout: default
---

# Schema Matching

Schema matching 的目标是：

- 把 schema S 里的元素
- 和 schema T 里的元素
- 按语义关系对应起来

高频形式：

- One-to-one matching
- One-to-many matching

---
layout: two-cols
---

# Name-Based Matching

常见步骤：

- split names
- expand abbreviations / acronyms
- expand synonyms
- expand hypernyms
- remove articles / prepositions / conjunctions

::right::

# 它的特点

- 成本低
- 不需要训练
- 但很依赖名字本身是否携带语义

<div class="small-note mt-3">
例如：`ClientName -> Client Name`, `DOB -> Date of Birth`, `loc -> location`
</div>

---
layout: two-cols
---

# Instance-based Matching

- Rule-based matching
  - 利用名称、类型、结构、完整性约束
- Learning-based matching
  - 同时利用 schema 和 data instances

::right::

# 怎么选

- 规则明确、成本敏感：rule-based
- 模式复杂、想吃更多数据特征：learning-based

<div class="callout mt-4 text-sm">
一句话：name-based 看“字段名像不像”，instance-based 看“数据值像不像”。
</div>

---
layout: section
---

# Part 3

# Data-Level Integration

---
layout: default
---

# Data-Level Integration 是什么

它关注的是：

- integrated contents / values
- 不是 schema 本身

也就是：结构先对上之后，数据内容怎么进一步整合。

---
layout: default
---

# 两大类别

| 类别 | 关注点 | 典型问题 |
|------|------|------|
| Attribute-level | columns 之间的关系 | redundancy / correlation |
| Tuple-level | rows 之间是否指向同一对象 | duplication / inconsistency |

---
layout: default
---

# Attribute-level Integration

典型问题：

- 一个属性可以由其他属性推出来
  - annual salary vs fortnight payment
- 不同属性其实表达同一东西
  - kg vs lb

常见技术：

- Chi-square test：categorical variables
- Correlation coefficient：numerical attributes

---
layout: default
---

# Chi-square Test

用于：

- 检验两个 categorical variables 是否独立

假设：

- Null hypothesis：两个变量独立
- Alternative hypothesis：两个变量相关

<div class="formula-box">

$$
\chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i}
$$

$$
E = \frac{\text{Row Total} \times \text{Column Total}}{\text{Sample Size}}
$$

</div>

---
layout: default
---

# Chi-square 怎么判断

判断逻辑：

1. 计算 $\chi^2$
2. 算自由度 $(r-1)(c-1)$
3. 查临界值
4. 若统计量 > 临界值，则拒绝零假设

例子里：

- $\chi^2 = 8.006$
- df = 3
- critical value at 5% = 7.815

因此：`8.006 > 7.815`，说明变量不独立。

---
layout: default
---

# Correlation Coefficient

Pearson correlation coefficient：

<div class="formula-box">

$$
r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}
$$

</div>

解释：

- $r \approx +1$：强正相关
- $r \approx -1$：强负相关
- $r \approx 0$：弱线性相关或无线性相关

---
layout: default
---

# Coefficient of Determination

`R^2` 关心的是：

- 一个变量的方差中
- 有多少可以由另一个变量解释

<div class="formula-box">

$$
R^2 = 1 - \frac{RSS}{TSS}
$$

</div>

直观理解：

- 越接近 1，说明回归线解释力越强
- 越接近 0，说明解释力越弱

---
layout: default
---

# 真题演练

**In a chi-square test of independence, if the test statistic is greater than the critical value, we should:**

| 选项 | 内容 |
|------|------|
| a | accept that the variables are independent |
| b | reject the null hypothesis of independence |
| c | conclude the sample size is too small |
| d | switch to Min-Max scaling |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>这题考的是最核心的 decision rule：统计量超过临界值，就说明“独立”这个零假设站不住。
</div>

---
layout: default
---

# Tuple-level Integration

典型问题：

- Duplicates：多行指向同一对象
- Inconsistent update：重复记录没有同步更新

高频困难：

- formatting conventions
- naming conventions
- abbreviations
- omissions
- errors

---
layout: default
---

# String Matching 方法家族

| 类别 | 核心思路 | 例子 |
|------|------|------|
| Sequence-based | 把字符串看成字符序列 | Edit distance, Needleman-Wunsch |
| Set-based | 把字符串看成 token 集合 | Overlap, TF/IDF |
| Hybrid | 结合 sequence 和 set | Generalised Jaccard, Soft TF/IDF |
| Phonetic | 按发音相似 | sound-based matching |

---
layout: default
---

# Edit Distance

定义：

- 把一个字符串变成另一个字符串
- 所需最少编辑操作数

操作包括：

- insertion
- deletion
- substitution

应用场景：

- 姓名匹配
- 地址标准化
- 重复记录识别

---
layout: default
---

# Data Matching

Data matching 的难点常见在：

- formatting differences
- abbreviations / shortening
- different naming conventions
- omissions
- errors

方法上通常分成：

- Rule-based
- Learning-based

---
layout: two-cols-header
---

# Rule-based vs Learning-based Matching

::left::

Rule-based matching：

<div class="formula-box">

$$
sim(x,y) = \sum_{i=1}^{n} \alpha_i \cdot sim_i(x,y)
$$

</div>

- 通过加权组合多个相似度
- 规则可解释性强
- 成本相对低

::right::

Learning-based matching：

- supervised learning
- clustering
- probabilistic approaches

特点：

- 能学习复杂模式
- 但通常需要训练数据或更高实现成本

---
layout: default
---

# 监督学习匹配怎么做

训练数据形式：

$$
T = \{(x_1,y_1,l_1), (x_2,y_2,l_2), \ldots, (x_n,y_n,l_n)\}
$$

流程：

1. 定义特征 $f_1, f_2, ..., f_m$
2. 把 tuple pair 转成 feature vector
3. 训练 supervised learning model

---
layout: default
---

# 一句话记忆：Matching

- `name-based`：看字段名像不像
- `instance-based`：看数据值像不像
- `string matching`：多用于 tuple-level 的文本相似性
- `rule-based`：便宜、直接、可解释
- `learning-based`：更强，但更贵

---
layout: default
---

# 真题演练

**Which method typically requires labelled training data?**

| 选项 | 内容 |
|------|------|
| a | Name-based matching |
| b | Learning-based matching with supervised learning |
| c | Homonym detection by definition |
| d | Equal-width binning |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>监督学习型 matching 需要 labelled tuple pairs；这也是它和 rule-based 方法的关键区别之一。
</div>

---
layout: section
---

# Part 4

# Exam & Review

---
layout: default
---

# 一句话记忆：Week 10

- `Enrichment`：加上下文，提升价值
- `Integration`：统一多个来源，解决冲突
- `Schema integration`：先解决结构和语义对齐
- `Data-level integration`：再解决 columns / rows 的内容整合
- `Matching`：核心在于“怎么判断两个东西是不是同一个”

---
layout: default
---

# 考试最该抓的点

| 主题 | 最可能考什么 |
|------|------|
| Enrichment vs Integration | 定义、目的、输出区别 |
| Schema conflicts | homonyms / synonyms / units / abstraction |
| Chi-square | 公式、假设、判断逻辑 |
| Correlation / $R^2$ | 含义与解释 |
| Edit distance | 操作类型与使用场景 |
| Rule vs Learning matching | 何时用、是否需要训练数据 |

---
layout: default
---

# 做题框架

- 如果题目在问“加信息”还是“做整合”：
  - 先分 enrichment vs integration
- 如果题目在问“字段怎么对齐”：
  - 先想 schema integration
- 如果题目在问“值和记录怎么合并”：
  - 先想 data-level integration
- 如果题目在问“两个文本/记录是不是同一个”：
  - 先想 matching family

<div class="callout mt-4 text-sm">
高分答案通常不是只写名词，而是能把 <code>problem -> conflict type -> method -> why</code> 串起来。
</div>

---
layout: end
---

# Week 10 Takeaways

- 多源数据工作的重点是“语义对齐 + 内容整合”
- enrichment 和 integration 服务的是不同目标
- schema integration 关注结构、命名、实体和语义冲突
- data-level integration 关注属性关系和记录匹配
- matching 方法选择，取决于你手里有名字、值、规则还是训练数据

