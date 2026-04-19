---
theme: apple-basic
title: FIT5196 Week 7 - Data Quality and Anomalies
layout: intro
mdc: true
---

<style>
.compact-table table {
	width: 100%;
	table-layout: fixed;
	font-size: 0.78em;
	line-height: 1.25;
}

.compact-table th,
.compact-table td {
	white-space: normal;
	overflow-wrap: anywhere;
	word-break: break-word;
	padding: 0.3rem 0.4rem;
}

.table-scroll {
	max-width: 100%;
	overflow-x: auto;
}

.table-scroll table {
	min-width: 980px;
}

.anomaly-hit {
	color: #b91c1c;
	font-weight: 700;
	background: rgba(220, 38, 38, 0.14);
	padding: 0 0.22rem;
	border-radius: 0.2rem;
}
</style>

# FIT5196 Data Wrangling

## Week 7: Data Quality and Anomalies

---
layout: default
---

# 本周目标

| Learning Outcome | 你要会什么 |
|------|------|
| Explain data quality | 能清楚解释数据质量定义和价值 |
| Diagnose poor quality impact | 能说明坏数据会造成什么业务后果 |
| Distinguish dimensions vs measures | 能区分维度和度量 |
| Identify anomalies | 能区分 point/contextual/collective anomalies |
| Audit quality issues | 能按 syntactical/semantic/coverage 分类问题 |
| Propose management framework | 能讲出可执行的数据质量治理框架 |

---
layout: section
---

# Part 1

# Data Quality 基础

---
layout: statement
---

## Data quality 决定了分析结果是否可信。

Raw data 不等于 usable data。  
高质量数据是可解释、可复现、可决策的前提。

---
layout: default
---

# Data Quality 定义

Data quality 指数据在以下方面的状态：

- Accuracy
- Completeness
- Reliability
- Relevance
- Timeliness

<div class="callout mt-4 text-sm">
如果数据不准确、不完整，即使模型很复杂，输出也可能毫无价值。
</div>

---
layout: two-cols
---

# 为什么重要

- 决策更可靠
- 合规风险更可控
- 运营效率更高
- 客户体验更好
- 成本更低、收益更稳

::right::

# 坏数据的代价

- 错误决策
- 重工和时间浪费
- KPI 被误导
- 品牌信誉受损
- 法律与审计风险上升

---
layout: default
---

# 真题演练

**Which of the following are impacts of poor data quality?**  
Select all that apply

| 选项 | 内容 |
|------|------|
| a | Inaccurate decision-making |
| b | Improved regulatory compliance |
| c | Customer dissatisfaction |
| d | Analytical and forecasting errors |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, c, d</code><br>
<strong>讲解：</strong>b 是反向干扰项。poor data quality 通常会增加而不是降低合规风险。
</div>

---
layout: default
---

# Data Quality Dimensions vs Measures

| 概念 | 含义 | 例子 |
|------|------|------|
| Dimensions | 质量评估视角 | accuracy, completeness, timeliness |
| Measures | 可量化指标 | error rate, duplicate rate, fill rate, latency |

<div class="muted mt-4 text-sm">
口诀：dimension 是“看什么”，measure 是“怎么算”。
</div>

---
layout: section
---

# Part 2

# Challenges 与 Anomalies

---
layout: default
---

# Data Quality Challenges

| 挑战 | 具体表现 |
|------|------|
| Volume and variety | 数据体量大、类型杂、来源多 |
| Data silos | 系统孤岛导致重复和不一致 |
| Evolving data | 业务变化快，规则跟不上 |
| Human error | 录入、映射、解释都可能出错 |
| Weak governance | 缺标准、缺责任人、缺流程 |
| Tooling/resource limits | 工具能力和人力预算不足 |

---
layout: default
---

# 真题演练

**A common challenge in data quality management is:**

| 选项 | 内容 |
|------|------|
| a | Data silos |
| b | Perfect standardization |
| c | Zero governance overhead |
| d | Fully consistent multi-source schemas |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a</code><br>
<strong>讲解：</strong>b/c/d 都是假设理想状态，真实场景里正好相反。
</div>

---
layout: default
---

# Data Anomalies: 三种核心类型

| 类型 | 定义 | 例子 |
|------|------|------|
| Point anomaly | 单条记录显著偏离 | 某员工工时 500 |
| Contextual anomaly | 在特定上下文下异常 | 夜间能耗突增 |
| Collective anomaly | 作为整体模式异常 | 一串可疑交易组合 |

---
layout: two-cols
---

# Point Anomaly 示例

<div class="compact-table">

| Staff_ID | Name | Work_Hour |
|------|------|------|
| S009 | James | 10 |
| S010 | Anddy | <span class="anomaly-hit">500</span> |
| S011 | Jane | 8 |

</div>

::right::

# 解读

- 500 与其余样本差异极大
- 可能是录入错误，也可能是真实异常事件
- 不能直接删除，先做 root-cause 分析

---
layout: default
---

# Contextual Anomaly：具体数据表

**场景：家庭/物业每小时能耗（kWh）**

<div class="table-scroll compact-table">

| Property | 00:00 | 01:00 | 02:00 | 03:00 | 04:00 | 05:00 | 06:00 | 07:00 | 08:00 | 09:00 | 10:00 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| P0001 | 24 | 13 | 7 | 4 | 2 | 6 | 25 | 37 | 47 | 58 | 36 |
| P0002 | 12 | 21 | 11 | 4 | 5 | 3 | 16 | 24 | 35 | 63 | 66 |
| P0003 | 34 | 22 | 9 | 3 | 3 | 1 | 11 | 21 | 33 | 21 | 37 |
| P0004 | <span class="anomaly-hit">56</span> | <span class="anomaly-hit">43</span> | <span class="anomaly-hit">21</span> | <span class="anomaly-hit">35</span> | <span class="anomaly-hit">37</span> | <span class="anomaly-hit">32</span> | 43 | 26 | 11 | 21 | 35 |

</div>

<div class="callout mt-4 text-sm">
讲解：P0004 在凌晨时段（00:00-05:00）持续高于其他住户，属于“在特定时间上下文下异常”。
</div>

---
layout: default
---

# Collective Anomaly：具体数据表

**场景：信用卡连续交易记录**

<div class="compact-table">

| Date | Merchant | Amount |
|------|------|------|
| 3/2/2022 | Tasty Burger | $16.99 |
| 3/2/2022 | Tasty Burger | $16.99 |
| 4/2/2022 | Tasty Burger | $24.99 |
| 4/2/2022 | Tasty Burger | $16.99 |
| 4/2/2022 | KFC | $18.98 |
| 5/2/2022 | Tasty Burger | $16.99 |
| <span class="anomaly-hit">6/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$2.50</span> |
| <span class="anomaly-hit">6/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$16.99</span> |
| <span class="anomaly-hit">6/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$21.99</span> |
| <span class="anomaly-hit">6/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$47.98</span> |
| <span class="anomaly-hit">7/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$16.99</span> |
| <span class="anomaly-hit">7/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$21.98</span> |
| <span class="anomaly-hit">7/2/2022</span> | <span class="anomaly-hit">Tasty Burger</span> | <span class="anomaly-hit">$16.99</span> |

</div>

<div class="callout mt-4 text-sm">
讲解：单笔金额不一定异常，但“短期内同商户高频重复交易”构成 collective anomaly。
</div>

---
layout: default
---

# Contextual / Collective 小结

- Contextual：同一值在不同上下文下，异常结论可能不同
- Collective：单点正常不代表整体正常，需看序列/组合模式

<div class="callout mt-4 text-sm">
异常不一定等于错误。  
异常也可能是风险信号或业务机会。
</div>

---
layout: section
---

# Part 3

# Data Quality Issues 审计框架

---
layout: default
---

# 按问题类型分类

| 类别 | 关注点 | 常见问题 |
|------|------|------|
| Syntactical | 格式和值表示 | 拼写错误、单位不一致、格式不统一 |
| Semantic | 含义和逻辑关系 | 约束冲突、矛盾记录、重复实体 |
| Coverage | 缺失性 | 缺失值、缺失记录 |

---
layout: default
---

# Source-Based 分类也要会

| Source View | 你要识别什么 |
|------|------|
| Single-source problems | 单一数据源内部的问题：非法值、依赖冲突、重复、参照完整性 |
| Multi-source problems | 跨来源合并问题：命名差异、格式差异、实体对齐冲突 |

<div class="muted mt-4 text-sm">
课堂文献来源：Data Cleaning: Problems and Current Approaches (Rahm and Do)
</div>

---
layout: two-cols
---

# Single-source 例子

- Illegal values: `bdate=30.13.70`
- Dependency conflict: `age=22, bdate=12.02.70`
- Uniqueness violation: 相同 SSN 对应不同人
- Referential integrity violation: `deptno` 指向不存在部门

::right::

# Multi-source 例子

- Kristen/Christian/Christoph 可能是同实体家族
- `Hurley St` vs `Hurley Place`
- `S Fork MN` vs `South Fork, MN 48503`
- 多表合并后需做实体对齐与冲突消解

---
layout: default
---

# Type-Based 细分要点

| 类型 | 核心关键词 | 典型例子 |
|------|------|------|
| Syntactical | format/value representation | typo、单位不一致、格式不统一 |
| Semantic | logic/non-redundancy | 约束冲突、重复实体、无效观测 |
| Coverage | missingness | 缺失值、缺失记录 |

---
layout: default
---

# Dirty Data 三层细化

| 层级 | 常见情形 |
|------|------|
| Missing data | 该空却没空/不该空却空 |
| Not missing but wrong | 类型越界、重复键、参照完整性错误 |
| Not missing and not wrong but unusable | 缩写歧义、编码差异、单位混用、特殊字符混乱 |

<div class="callout mt-4 text-sm">
考试会混淆 “wrong” 和 “unusable”。  
记忆：wrong 是“错值”，unusable 是“值本身不一定错，但无法直接用”。
</div>

---
layout: default
---

# Dirty Data 的三种形态

1. Missing data
2. Not missing but wrong data
3. Not missing and not wrong but unusable data

| 形态 | 例子 |
|------|------|
| Missing | 关键字段为空 |
| Wrong | 日期越界、主键重复、参照完整性错误 |
| Unusable | 缩写歧义、编码混乱、单位混用 |

---
layout: default
---

# 真题演练

**Which issue belongs to semantic anomalies?**

| 选项 | 内容 |
|------|------|
| a | Spelling typo in city name |
| b | Duplicate observations of the same entity |
| c | Missing values in optional field |
| d | Different currency symbols in one column |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>a/d 更偏 syntactical，c 更偏 coverage。
</div>

---
layout: section
---

# Part 4

# Framework 与实践落地

---
layout: default
---

# Data Quality Management Framework

| 模块 | 关键动作 |
|------|------|
| Governance | 角色、责任、流程、规则 |
| Standards | 字段规范、质量阈值、命名规则 |
| Assessment | 维度评估 + 指标量化 |
| Monitoring | 持续监控与告警 |
| Improvement | 闭环修复与复盘 |
| Compliance | 审计可追溯与合规管理 |
| Tools & Tech | 自动化检测、质量规则执行 |
| Training & Awareness | 数据质量文化与团队能力建设 |

---
layout: two-cols
---

# ML 在 Data Quality 的作用

- Automated error detection
- Record matching and deduplication
- Predictive quality scoring
- NLP-based standardization
- Continuous monitoring

::right::

# 注意点

- ML 不是替代治理
- 先定义规则和标签再上模型
- 关注可解释性与偏差风险

---
layout: default
---

# Week 7 Checklist

1. 能定义 data quality 和 business value
2. 能区分 dimensions 与 measures
3. 能识别三类 anomalies
4. 能按 syntactical/semantic/coverage 分类问题
5. 能说清 dirty data 三种形态
6. 能描述一个可执行的质量管理框架

---
layout: default
---

# Summary & To-do

- 回顾 Week 7 概念图：quality -> issues -> anomalies -> framework
- 复盘一组单源/多源脏数据例子，做分类与修复建议
- 重点准备下周 Data Cleansing 实操：
	- missing value strategy
	- duplicate handling
	- standardization + validation rules

---
layout: end
---

# Next Week

Week 8: Missing value
