---
theme: apple-basic
title: FIT5196 Week 8 - Data Cleansing
layout: intro
mdc: true
---

<style>
.compact-table table {
  width: 100%;
  table-layout: fixed;
  font-size: 0.82em;
  line-height: 1.25;
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

.risk {
  color: #b91c1c;
  font-weight: 700;
}
</style>

# FIT5196 Data Wrangling

## Week 8: Data Cleansing

---
layout: default
---

# 本周目标

| Learning Outcome | 你要会什么 |
|------|------|
| Explain data cleansing | 能解释 data cleansing 的定义、目标和位置 |
| Describe workflow | 能讲出 audit -> plan -> cleanse -> verify 的流程 |
| Distinguish missingness mechanisms | 能区分 MCAR / MAR / MNAR |
| Compare handling methods | 能比较 deletion / imputation / model-based methods |
| Diagnose outliers | 能解释异常值影响与常见检测规则 |
| Choose practical actions | 能按场景判断何时删、补、保留、复核 |

---
layout: statement
---

## Data cleansing 的目标，不是把数据“修漂亮”，而是让数据“可分析、可信、可复现”。

脏数据如果直接进入统计分析、BI 报表或机器学习模型，错误会被放大，而不是自动消失。

---
layout: default
---

# Week 8 放在课程哪里

Data wrangling 常见链路：

- Discovery
- Collection
- Pre-processing
- Structuring
- Quality audit
- **Cleansing**
- Transformation
- Enrichment
- Validation

<div class="muted mt-4 text-sm">
Week 7 讲“发现质量问题”，Week 8 更进一步，讲“如何处理这些问题”。
</div>

---
layout: section
---

# Part 1

# Data Cleansing Workflow

---
layout: default
---

# 什么是 Data Cleansing

Data cleansing / data cleaning 指：

- 识别错误、损坏、不一致或不完整的数据
- 纠正、删除或替换问题记录
- 提高数据质量，降低下游分析风险

它通常依赖：

- 自动化规则
- 统计方法
- 领域知识
- 人工复核

---
layout: two-cols
---

# Workflow 主线

1. Data Audit
2. Define Cleansing Goals
3. Cleansing Plan
4. Backup Data
5. Cleansing Operations
6. Verification
7. Documentation & Reporting
8. Review

::right::

# 每一步在回答什么

- 数据哪里有问题？
- 什么算修好？
- 怎么修、谁来修、何时修？
- 出错能不能回滚？
- 修完后是否真的变好？
- 后续能不能复现？

---
layout: default
---

# 真题演练

**Which step should usually happen before large-scale cleansing operations?**

| 选项 | 内容 |
|------|------|
| a | Backup the data |
| b | Randomly delete suspicious rows |
| c | Publish the final report |
| d | Train the predictive model first |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a</code><br>
<strong>讲解：</strong>backup 是高风险清洗操作前的基本保护措施。
</div>

---
layout: default
---

# Data Audit 会产出什么

- Accuracy / completeness / consistency 指标
- 重复、缺失、异常、格式问题的分布情况
- 数据流向与字段映射关系
- 清洗优先级
- 后续规则设计依据

<div class="callout mt-4 text-sm">
Audit 不是可选前戏，而是 cleansing plan 的输入。
</div>

---
layout: default
---

# Data Audit 具体看什么

<div class="compact-table">

| 官方强调的目标 | 要检查的内容 |
|------|------|
| Identify data quality issues | inaccuracies / inconsistencies / duplicates / missing values / anomalies |
| Assess data completeness | 关键字段是否缺失或不完整 |
| Evaluate data consistency | 跨系统、跨来源是否一致 |
| Understand data usage | 数据是否满足真实使用需求 |
| Compliance check | 是否符合隐私、治理、合规要求 |

</div>

---
layout: default
---

# Data Audit 常见方法

- 建立 accuracy / completeness / consistency / reliability 指标
- 绘制数据在组织中的位置与流转地图
- 与 stakeholder 沟通真实数据需求
- 抽取代表性样本做详细分析
- 用软件自动扫描常见问题
- 对复杂或高风险部分做人工复核

---
layout: default
---

# Defining Cleansing Goals

官方课件把这一步单独展开，重点包括：

- Understanding business requirements
- Identifying data quality dimensions
- Setting specific, measurable goals
- Prioritizing goals
- Creating a roadmap
- Continuous improvement
- Communication and documentation

<div class="muted mt-4 text-sm">
不是“发现问题就开始修”，而是先定义修到什么标准才算完成。
</div>

---
layout: default
---

# Data Cleansing Plan 要写什么

<div class="compact-table">

| 模块 | 作用 |
|------|------|
| Assess data quality | 确认问题规模与优先级 |
| Define cleansing objective | 明确清洗目标 |
| Develop cleansing strategies | 选择删、补、改、标准化等策略 |
| Select tools & resources | 确认工具、人力、时间 |
| Create implementation timeline | 排期与执行顺序 |
| Establish monitoring procedures | 运行中持续监测 |
| Documentation & training | 确保可交接、可复现 |

</div>

---
layout: default
---

# Verification 不只是“看起来变干净了”

官方课件强调 verification 至少包括：

- Accuracy check：修改是否正确落地
- Consistency validation：数据集内外是否一致
- Completeness verification：有没有误删必要信息
- Quality assurance：是否达到预定质量标准

<div class="callout mt-4 text-sm">
如果没有 verification，cleaning 可能只是“改了很多东西”，但不一定“改对了”。
</div>

---
layout: section
---

# Part 2

# Missing Data

---
layout: default
---

# Missing Data 是什么

Missing data 指某个变量在某些样本上没有值。

常见风险：

- 样本量下降
- 参数估计偏差
- 标准误不可靠
- 模型性能不稳定
- 结论不可泛化

---
layout: default
---

# Missing values 为什么会出现

官方给出的典型原因包括：

- Equipment errors
- Absence of survey participants
- GPS signal unavailable
- Change of circumstances: death / graduation / dropout
- Filter questions in surveys

<div class="muted mt-4 text-sm">
这一步很重要，因为缺失原因往往决定它更像 MCAR、MAR 还是 MNAR。
</div>

---
layout: default
---

# 为什么 missing data 是分析问题

- 很多标准统计方法默认所有变量信息完整
- 忽略缺失值会导致 biased estimation
- 可能高估或低估均值与方差
- 最终会产生错误推断：garbage in, garbage out

---
layout: default
---

# Missingness Mechanisms

<div class="compact-table">

| 机制 | 含义 | 典型例子 | 处理提示 |
|------|------|------|------|
| MCAR | 缺失与任何变量都无关 | 问卷页面意外丢失 | 删除法影响相对较小 |
| MAR | 缺失与其他已观测变量有关 | 年轻人更少填收入 | 可借助其他变量建模 |
| MNAR | 缺失与自身真实值有关 | 高收入者拒填收入 | 不能随便忽略，风险最高 |

</div>

---
layout: default
---

# 一句话记忆

- **MCAR**：像数据“意外掉了”
- **MAR**：和别的变量有关，仍可补救
- **MNAR**：和它自己有关，最难处理

<div class="callout mt-4 text-sm">
核心原则：先判断缺失机制，再讨论处理方法。方法选错，比不处理更危险。
</div>

---
layout: two-cols
---

# 删除法

## Listwise deletion

- 只要某行有缺失，就删整行
- 简单直接
- 但会明显损失样本量

## Pairwise deletion

- 每次分析尽量使用可用数据
- 数据利用率更高
- 但不同统计量可能基于不同样本集合

::right::

# 什么时候更合理

- 更依赖 **MCAR** 假设
- 小比例缺失时更常见
- 样本足够大时更容易接受

<div class="callout mt-4 text-sm">
如果缺失不是 MCAR，删除法可能系统性扭曲结果。
</div>

---
layout: default
---

# Missing Data Patterns

| Pattern | 含义 | 理解方式 |
|------|------|------|
| Univariate | 只在一个变量上缺 | 单点问题 |
| Monotone | 后面的变量越往后越缺 | 像逐步退出 |
| General | 到处都可能缺 | 最复杂、最常见 |

---
layout: default
---

# Pairwise deletion 的额外风险

官方课件特别提醒：

- 它依赖 MCAR 假设
- 会受变量间相关性影响
- 可能产生不合理的 covariance matrix
- 不同统计量可能基于不同样本基数
- 会给 standard error 和 covariance 计算带来麻烦

---
layout: default
---

# Imputation Methods

<div class="compact-table">

| 方法 | 思路 | 优点 | 局限 |
|------|------|------|------|
| Mean imputation | 用均值补缺失值 | 简单、快 | 降低方差，削弱分布真实性 |
| Regression imputation | 用其他变量预测缺失值 | 保留变量关系 | 模型错了会带偏 |
| Stochastic regression | 预测值再加随机残差 | 更能保留波动 | 实现更复杂 |
| Model-based methods | 直接对缺失机制建模 | 往往更稳健 | 需要更强统计假设 |

</div>

---
layout: default
---

# Single imputation 的共性问题

官方课件把 mean / regression / stochastic regression 放在 single imputation 下面讨论，并提醒：

- 它们都会生成完整数据集
- 但很多 single imputation 方法仍会带来 biased estimates
- 也常常低估 standard errors

<div class="callout mt-4 text-sm">
所以“数据补齐了”不代表“统计性质就恢复了”。
</div>

---
layout: default
---

# 两个常见公式

<div class="formula-box">

回归插补：

$$
JP_i = \beta_0 + \beta_1 \times IQ_i
$$

随机回归插补：

$$
P_i = \beta_0 + \beta_1 \times IQ_i + z_i
$$

其中 $z_i \sim N(0, \sigma^2)$，用来恢复一部分随机波动。

</div>

---
layout: default
---

# 关于 stochastic regression 的官方结论

课件里有一个很重要的判断：

- 在本章介绍的方法里
- stochastic regression imputation
- 是唯一一个在 **MAR** 机制下可给出无偏参数估计的方法

<div class="muted mt-4 text-sm">
这句话很像考试点，值得单独记住。
</div>

---
layout: default
---

# 如何评价一个缺失值处理方法

一个好的方法，至少应该尽量做到：

1. Minimise bias
2. Maximise available information
3. Yield good uncertainty estimates

<div class="muted mt-4 text-sm">
口诀：偏差小、浪费少、不确定性估计靠谱。
</div>

---
layout: default
---

# 真题演练

**Which statement about mean imputation is most accurate?**

| 选项 | 内容 |
|------|------|
| a | It preserves variability well |
| b | It is simple but can reduce variability |
| c | It only works for MNAR data |
| d | It always outperforms model-based methods |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>均值插补的最大问题之一，就是把数据分布“压扁”。
</div>

---
layout: section
---

# Part 3

# Outliers

---
layout: default
---

# Outliers 的价值不只是“脏”

官方课件强调：异常值常常包含关于系统异常行为的有用信息。

典型场景：

- intrusion detection
- credit-card fraud
- medical analysis
- law enforcement / insurance claims

<div class="callout mt-4 text-sm">
所以 outlier detection 经常不是为了“删掉异常”，而是为了“找出异常背后的机制”。
</div>

---
layout: default
---

# 为什么要重视 Outliers

异常值可能会：

- 增加误差方差
- 拉偏均值与回归系数
- 破坏正态性假设
- 影响显著性检验
- 误导业务判断

<div class="callout mt-4 text-sm">
异常值不等于脏数据。它可能是录入错误，也可能是真实但罕见的重要信号。
</div>

---
layout: default
---

# 异常值类型

| 类型 | 定义 | 例子 |
|------|------|------|
| Univariate outlier | 在单变量分布上偏离很大 | 某员工工时 500 小时 |
| Multivariate outlier | 单看每维正常，但组合异常 | 收入与消费组合极不合理 |

---
layout: default
---

# Univariate detection 的通用模板

给定参考值 $x_0$、波动尺度 $\zeta$ 和阈值 $t$，官方写法是：

$$
|x_k - x_0| > t\zeta
$$

真正的问题是三件事：

- $x_0$ 取 mean 还是 median
- $\zeta$ 取 $\sigma$、MAD 还是 IQR
- $t$ 取多少才合理

---
layout: default
---

# 检测规则其实是“组合选择”

<div class="compact-table">

| 规则 | 参考值 $x_0$ | 波动尺度 $\zeta$ |
|------|------|------|
| 3σ rule | mean | standard deviation |
| Hampel identifier | median | MAD |
| Boxplot rule | median | IQR |

</div>

<div class="muted mt-4 text-sm">
官方这一页的重点是：方法差异，本质上来自参考值和尺度估计方式的不同。
</div>

---
layout: default
---

# 3σ Rule

如果数据近似正态分布，可用：

$$
|x_k - \bar{x}| > 3\sigma
$$

则将该点视为异常值。

优点：

- 规则简单
- 容易解释

局限：

- 本身就受异常值影响
- 对偏态分布不稳健

---
layout: default
---

# Hampel Identifier

更稳健的替代思路：

$$
x_0 = median(x)
$$

$$
\zeta = 1.4826 \times median(|x_k - median(x)|)
$$

判定条件：

$$
|x_k - x_0| > 3\zeta
$$

---
layout: default
---

# IQR / Boxplot Rule

令：

$$
IQR = Q3 - Q1
$$

若

$$
x_k < Q1 - 1.5 \times IQR
$$

或

$$
x_k > Q3 + 1.5 \times IQR
$$

则可视为异常值。

<div class="muted mt-4 text-sm">
优点：对非正态分布通常更友好，也更常见于实际探索分析。
</div>

---
layout: two-cols
---

# 处理异常值时别急着删

- 先确认是不是录入错误
- 再判断是不是测量问题
- 再看是否具有业务意义
- 最后决定删、改、截尾或保留

::right::

# 一个稳妥顺序

1. Detect
2. Diagnose
3. Document
4. Decide
5. Re-check downstream impact

<div class="callout mt-4 text-sm">
删除异常值必须能解释“为什么删”，而不是只因为它不好看。
</div>

---
layout: default
---

# Multivariate Outlier Detection

官方课件后半段还补充了多变量检测思路：

- **Linear models**
  - 看点到拟合超平面的 residual
- **Proximity-based models**
  - 不在 dense region 的点更可疑
  - clustering methods
  - density-based methods

<div class="callout mt-4 text-sm">
有些点单看每个变量都正常，但组合起来非常异常，这就是为什么只看单变量规则不够。
</div>

---
layout: default
---

# Regression 视角下怎么理解 multivariate outliers

- 线性模型会给出预测值
- outlier 常表现为明显偏离预测值的 residual
- 目标是找到那些在某个低维子空间里行为明显不同的点

<div class="muted mt-4 text-sm">
这是官方最后几页的核心意思，不要求复杂推导，但要知道 residual 可以作为 outlier score。
</div>

---
layout: section
---

# Part 4

# Practical Cleansing Actions

---
layout: default
---

# 常见数据清洗操作

- Removing duplicates
- Validating and correcting errors
- Consistency checks
- Filling missing values
- Handling outliers
- Standardising formats
- Logging every change

---
layout: default
---

# Removing Duplicates: 官方列出的办法

- Manual review and removal
- Sorting and sequential check
- Deduplication software
- Database queries (SQL)
- Hashing techniques
- Pivot tables
- Scripting and programming
- Machine learning algorithms

---
layout: two-cols
---

# Duplicate handling 的典型步骤

1. Identifying duplicates
2. Reviewing duplicates
3. Deleting or merging duplicates

::right::

# 什么时候不能直接删

- 需要保留主记录与从记录
- 重复记录其实代表合法多次事件
- 不同源系统字段冲突，需要先决策合并规则

<div class="callout mt-4 text-sm">
duplicate handling 的关键不只是“找重复”，还包括“定义什么算重复”。
</div>

---
layout: default
---

# 工具与方法

| 类型 | 例子 | 适合做什么 |
|------|------|------|
| Spreadsheet | Excel | 小规模人工检查 |
| Data cleaning tools | OpenRefine | 批量标准化、聚类修正 |
| ETL / integration | Talend, IBM InfoSphere | 企业级流程化清洗 |
| Programming | Python / Pandas / SQL | 可复现、可扩展、可自动化 |

<div class="muted mt-4 text-sm">
真正有效的 cleansing 很少只靠一个工具，通常是规则、代码和人工判断一起完成。
</div>

---
layout: default
---

# Exam / Assignment 视角怎么答

- 先定义问题是什么
- 再说明为什么它会影响分析
- 然后给出可执行处理方案
- 最后补上验证与文档记录

<div class="callout mt-4 text-sm">
高分答案通常不是“背概念”，而是能把 <code>问题 -> 风险 -> 方法 -> 代价 -> 验证</code> 串起来。
</div>

---
layout: default
---

# 真题演练

**Which of the following best describes a good data cleansing process?**

| 选项 | 内容 |
|------|------|
| a | Delete anything unusual immediately |
| b | Fix values without backup or documentation |
| c | Audit, clean systematically, verify, and document |
| d | Only focus on missing values |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>cleansing 是系统工程，不是单点修补。
</div>

---
layout: end
---

# Week 8 Takeaways

- Data cleansing 是数据可信度的保障
- Missingness mechanism 决定方法选择
- Deletion 简单，但风险不一定小
- Imputation 要考虑偏差、方差和假设
- Outliers 要先解释，再决定处理
- Verification + documentation 是闭环的一部分
