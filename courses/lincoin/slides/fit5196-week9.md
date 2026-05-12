---
theme: apple-basic
title: FIT5196 Week 9 - Data Transformation
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

.two-cols-header {
  column-gap: 2.2rem;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 0.92fr);
}

.two-cols-header .col-left {
  padding-right: 0.2rem;
}

.two-cols-header .col-right {
  padding-left: 0.2rem;
}

</style>

# FIT5196 Data Wrangling

## Week 9: Data Transformation

---
layout: default
---

# 本周目标

| Learning Outcome | 你要会什么 |
|------|------|
| Explain data transformation | 能解释 transformation 在 data wrangling 中的作用 |
| Distinguish scaling vs standardisation | 能区分缩放与标准化 |
| Compare normalisation methods | 能比较 Min-Max / MaxAbs / Decimal / Robust / Log |
| Explain linear and power transformation | 能讲出 linear / Box-Cox 的用途与限制 |
| Understand discretisation | 能解释 binning 及 equal-width / equal-depth |
| Describe construction and sampling | 能说明 feature engineering、feature selection、sampling |

---
layout: statement
---

## Data transformation 的重点是把数据变成更适合分析、建模和解释的形状。

同样的数据，不同表示方式，会直接影响模型假设是否成立、特征是否可比较，以及结果是否容易解释。

---
layout: default
---

# Week 9 放在课程哪里

Data wrangling 常见链路：

- Discovery
- Collection
- Pre-processing
- Cleaning
- Validation
- **Transformation**
- Enrichment

<div class="muted mt-4 text-sm">
Week 8 解决“数据有问题”，Week 9 更关注“数据怎么变得更可用”。
</div>

---
layout: section
---

# Part 1

# Data Transformation Basics

---
layout: default
---

# Data Transformation 是什么

这一部分最核心的定义有两点：

- cleaning and converting raw data into a more suitable format
- making analysis straightforward and reliable

常见原因：

- Fix skewness in data
- Enhance data visualisation
- Better interpretability
- Improve compatibility with model assumptions

---
layout: default
---

# Week 9 内容地图

本周 transformation 主要包括：

- Data normalisation
- Linear transformation
- Power transformation
- Data discretisation
- Data construction
- Data reduction / sampling

---
layout: default
---

# 真题演练

**Why do we often transform data before modelling?**

| 选项 | 内容 |
|------|------|
| a | To make every dataset larger |
| b | To improve compatibility with model assumptions |
| c | To remove all uncertainty |
| d | To guarantee causal inference |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>这题考的是 transformation 的本质目标：让数据更适配分析、可视化和模型假设，而不是单纯“改数据样子”。
</div>

---
layout: section
---

# Part 2

# Data Normalisation

---
layout: default
---

# 什么是 Data Normalisation

这里要抓住的是：

- 把 numeric columns 调整到 common scale
- 不扭曲原有差异
- 不无端丢失信息

特别重要的场景：

- 特征单位不同：dollars / kilometres / hours
- 特征量纲差异很大
- 距离型或梯度型算法对尺度敏感

---
layout: two-cols
---

# 两种大类

- **Scaling**
  - 改变数值范围
- **Standardisation**
  - 调整均值与标准差

::right::

# 一个常见误区

- “normalisation” 不总是只指 Min-Max
- 课程里它是更广义的数据尺度调整

<div class="callout mt-4 text-sm">
所以回答题目时，先区分课程语境：normalisation 在这里包含 scaling 和 standardisation。
</div>

---
layout: default
---

# Scaling 方法总览

| 方法 | 核心思路 | 典型特点 |
|------|------|------|
| Min-Max | 映射到固定区间 | 简单，但怕异常值 |
| MaxAbs | 除以最大绝对值 | 保留符号与稀疏性 |
| Decimal | 挪动小数点 | 很直观，但标准化能力有限 |
| Robust | 用 median 和 IQR | 对 outliers 更稳健 |
| Log | 压缩偏态分布 | 适合正值、指数增长数据 |

---
layout: two-cols-header
---

# Min-Max Scaling

::left::

<div class="formula-box">

$$
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

推广到区间 $[n, m]$：

$$
x' = \frac{x - x_{min}}{x_{max} - x_{min}} (m-n) + n
$$

</div>

<div class="small-note mt-3">
最常见用途：把不同量纲的特征压到统一范围。
</div>

::right::

## 优点

- Easy to implement
- 保留原始分布形状

## 局限

- 对异常值敏感
- outlier 会把其他样本挤进很窄区间

---
layout: two-cols-header
---

# MaxAbs Scaling

::left::

<div class="formula-box">

$$
x' = \frac{x}{\max(|x|)}
$$

</div>

适合：

- 数据有正有负
- 想保留 0 的位置
- 稀疏矩阵不希望被居中破坏

::right::

## 优点

- 不 shift / centre 数据
- 简单快速

## 局限

- 同样对 outliers 敏感

---
layout: two-cols-header
---

# Decimal Scaling

::left::

<div class="formula-box">

$$
x' = \frac{x}{10^c}
$$

其中 $c$ 是最小整数，使得 $\max(|x'|) < 1$

</div>

理解方式：

- 本质上是移动小数点
- 更像简单重缩放，而不是深度分布调整

::right::

## 优点

- Simple and intuitive
- 保留相对关系

## 局限

- 对异常值敏感
- 标准化效果有限

---
layout: two-cols-header
---

# Robust Scaling

::left::

<div class="formula-box">

$$
x' = \frac{x - x_{median}}{IQR(x)}
$$

$$
IQR(x) = Q3(x) - Q1(x)
$$

</div>

<div class="small-note mt-3">
如果数据里有明显极端值，这通常比 Min-Max 更稳妥。
</div>

::right::

## 优点

- 对异常值更稳健
- 中位数和分位数更不容易被极端值拉偏

## 局限

- quartile 计算成本略高

---
layout: two-cols-header
---

# Log Scaling

::left::

<div class="formula-box">

$$
x' = \log(x)
$$

</div>

什么时候特别有用：

- exponential growth
- right-skewed data
- variance 随量级变大

::right::

## 优点

- 减少偏态
- 稳定方差

## 局限

- 只适合正值
- 可能掩盖小差异

---
layout: default
---

# Scaling 该怎么选

| 场景 | 更常见选择 |
|------|------|
| 范围需要统一到固定区间 | Min-Max |
| 稀疏数据，不想中心化 | MaxAbs |
| 极端值较多 | Robust |
| 明显右偏、指数型增长 | Log |
| 只想简单缩小数值量级 | Decimal |

---
layout: default
---

# 一句话记忆：Scaling

- `Min-Max`：想统一范围时最直观，但怕 outlier
- `MaxAbs`：想保留正负号和稀疏性时优先想它
- `Decimal`：只是简单缩量级，不擅长处理分布
- `Robust`：数据脏、极端值多时更稳
- `Log`：右偏明显、量级跨得大时很常见

<div class="callout mt-4 text-sm">
做题时先不要背方法名，先判断你要解决的是 <code>范围</code>、<code>异常值</code>、<code>偏态</code> 还是 <code>稀疏结构</code>。
</div>

---
layout: default
---

# 真题演练

**If a feature contains many extreme values, which scaling method is usually the safest first choice?**

| 选项 | 内容 |
|------|------|
| a | Min-Max scaling |
| b | Decimal scaling |
| c | Robust scaling |
| d | MaxAbs scaling |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>核心考点不是“记名字”，而是知道 robust scaling 用 median 和 IQR，因此比依赖 min/max 的方法更抗异常值。
</div>

---
layout: two-cols-header
---

# Standardisation

::left::

<div class="formula-box">

核心定义：

- mean = 0
- standard deviation = 1

$$
z = \frac{x-\mu}{\sigma}
$$

它不是把数据压到固定上下界，而是把数据放到“离均值几个标准差”的尺度上。
</div>

::right::

## 优点

- 比 Min-Max 更能承受一些 outliers
- 适合很多默认正态假设的算法

## 局限

- 结果不在固定区间
- 仍然会受极端值影响

<div class="callout mt-4 text-sm">
如果题目问 “same scale”，Min-Max 和 z-score 都能改善可比性，但方式不同：一个改区间，一个改分布尺度。
</div>

---
layout: section
---

# Part 3

# Linear and Power Transformation

---
layout: two-cols-header
---

# Linear Transformation

::left::

<div class="formula-box">

这里要抓住的是：

- preserves linear relationship
- aggregates information from multiple features

$$
x_{linear} = w_0 + \sum_{i=1}^{m} w_i x_i
$$

常见例子：

- Celsius -> Fahrenheit
- Miles -> Kilometres
- Inches -> Centimetres
</div>

::right::

## 优点

- Simple and clear
- Enhances comparability

## 局限

- 对 outliers 敏感
- 不能解决非线性或严重偏态问题

---
layout: default
---

# Power Transformation

这部分的核心目标是：

- 让分布更接近正态
- 改善线性关系
- 稳定方差

可以把它理解成两步：

- 先判断数据关系或分布“往哪个方向变换更合理”
- 再选一个具体变换方法去执行

`Tukey and Mosteller’s bulging rule` 提供的是前一步的直觉框架：

- 它帮助我们判断应该对变量做什么类型的幂变换
- 目标是把关系拉直、把分布变得更适合分析

在这周内容里，更需要真正掌握的是后一步，也就是最常用的 `Box-Cox transformation`。

---
layout: two-cols
---

# 怎么读这张 Ladder 图

- `X^(1)` 是不变换
- 往上走：`X^(2), X^(3), ...`
- 往下走：`X^(1/2), X^(0)=log(X), X^(-1)=1/X ...`

可以把它理解成一把“变换强度梯子”：

- 越往上，幂越大
- 越往下，压缩越强

这张图真正想表达的是：

- 它不是让你背每一级
- 而是告诉你：**幂变换是一整族方法**
- 不同的指数，会把数据压成不同形状


::right::

<div class="h-full flex items-center justify-center">
  <img
    src="/images/Tukey and Mosteller’s bulging rule.png"
    alt="Tukey and Mosteller’s bulging rule"
    style="object-fit: contain;"
  />
</div>

---
layout: default
---

# Tukey and Mosteller’s Bulging Rule 在帮你判断什么

这条 rule 的核心不是“机械套公式”，而是判断：

- 现在的数据关系是不是弯的
- 如果是弯的，应该往哪个方向拉直
- 需要强一点还是弱一点的变换

一个直观理解是：

- **down-the-ladder**：
  - 常用于压缩大值
  - 适合右偏、尾部很长、增长太快的数据
- **up-the-ladder**：
  - 常用于把被压扁的变化重新拉开
  - 适合某些需要增强大值差异的场景

<div class="callout mt-4 text-sm">
在本周课程里，真正最常用、最值得掌握的是 <code>down-the-ladder</code> 这一侧，因为它和 <code>log / sqrt / Box-Cox</code> 的联系最紧。
</div>

---
layout: default
---

# 怎么把这条 Rule 和 Box-Cox 联系起来

可以把 Box-Cox 看成是把整条“ladder”统一起来的一种写法：

- 当 $\lambda = 1$：接近不变换
- 当 $\lambda = 0.5$：接近平方根
- 当 $\lambda = 0$：就是对数
- 当 $\lambda < 0$：会更接近倒数类变换

所以：

- `bulging rule` 更像“选方向的直觉地图”
- `Box-Cox` 更像“把很多幂变换写进一个公式的工具”

---
layout: default
---

# Box-Cox Transformation

<div class="formula-box">

$$
y =
\begin{cases}
\frac{x^\lambda - 1}{\lambda}, & \lambda \neq 0 \\
\log(x), & \lambda = 0
\end{cases}
$$

</div>

核心作用：

- 把连续变量拉得更接近 normal distribution
- 把多种常见变换放进一个统一框架
- 通过寻找合适的 $\lambda$ 来调整分布形状

这一页还要顺手记住三点：

- 要求输入 $x > 0$
- 典型对象是连续变量
- 它本质上是在“选一个更合适的变换曲线”

---
layout: two-cols
---

# 为什么 $\lambda = 0$ 要写成 log

为了让 Box-Cox 在 $\lambda = 0$ 处保持连续。

如果直接把 $\lambda = 0$ 代进

$$
\frac{x^\lambda - 1}{\lambda}
$$

会出现除以 0 的问题。

::right::

解决思路是取极限：

$$
\lim_{\lambda \to 0} \frac{x^\lambda - 1}{\lambda} = \log(x)
$$

常见理解：

- $\lambda = 1$：近似原始线性尺度
- $\lambda = 0$：log transform
- $\lambda = 0.5$：sqrt transform
- $\lambda = -1$：reciprocal style transform

---
layout: default
---

# Box-Cox 的限制

标准 Box-Cox 只能用于：

- strictly positive
- continuous variables

适合的例子：

- price
- age
- income
- sales

不适合的情况：

- 有负数
- 有 0
- 离散类别变量

---
layout: default
---

# 真题演练

**Which statement about the standard Box-Cox transformation is correct?**

| 选项 | 内容 |
|------|------|
| a | It can be directly applied to any negative-valued feature |
| b | It only works on strictly positive continuous variables |
| c | It always maps data into the range [0,1] |
| d | It is mainly used to create train/test splits |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>这题考的是边界条件。Box-Cox 的核心用途是改善分布，不是缩放到固定区间；标准版也不能直接处理负数或 0。
</div>

---
layout: default
---

# Box-Cox with Negatives

如果数据里有负值，可以用扩展形式处理：

<div class="formula-box">

$$
y =
\begin{cases}
\frac{(x+c)^\lambda - 1}{g\lambda}, & \lambda \neq 0 \\
\frac{\log(x+c)}{g}, & \lambda = 0
\end{cases}
$$

</div>

其中：

- $c$：offset negative values
- $g$：scale the resulting values
- $\lambda$：搜索最合适的 normalising power

作用上可以这样理解：

- $c$ 先把负数或 0 平移到合法区域
- $g$ 控制缩放，避免结果量级过大或过小
- 整个扩展版的目标仍然是让分布更适合分析

---
layout: default
---

# 基础版 vs 扩展版

| 版本 | 输入要求 | 额外参数 | 更适合什么情况 |
|------|------|------|------|
| 标准 Box-Cox | $x > 0$ | 无 | 自然正数的连续变量 |
| 扩展 Box-Cox | $x + c > 0$ | $c, g$ | 含 0、负值或量级不方便直接处理的数据 |

---
layout: default
---

# 这一页怎么记更稳妥

不需要死记每个公式细节，但至少要抓住四件事：

- 标准 Box-Cox 要求正数输入
- 有负值时要先做平移
- $\lambda = 0$ 对应 `log`
- power transformation 的目的仍然是让数据更接近建模友好的分布

---
layout: default
---

# 一句话记忆：Box-Cox

- 目标：把分布拉得更接近 normal
- 标准版：只适用于正的连续变量
- $\lambda = 0$：自然退化成 `log`
- 有负值：先平移，再考虑扩展形式
- 它的价值在于把 `log / sqrt / reciprocal` 放进统一框架里

<div class="callout mt-4 text-sm">
如果题目在考 Box-Cox，通常不是让你手算，而是在考：<code>它解决什么问题</code>、<code>何时不能直接用</code>、<code>为什么会出现 λ=0 的特殊情况</code>。
</div>

---
layout: section
---

# Part 4

# Data Discretisation

---
layout: default
---

# 什么是 Data Discretisation

把 continuous variables 转换成 discretised / nominal variables。

离散化最值得记住的作用：

- Find concise category representation
- Retain as much information as possible
- Smooth data
- Reduce noise
- Reduce data size
- Enable methods that need nominal data

---
layout: default
---

# Binning

binning 是一种 unsupervised discretisation 方法：

- 先把数据排序
- 再分成若干 bins
- 不直接看 dependent variable

两种核心方式：

- Equal-width binning
- Equal-depth binning

---
layout: default
---

# Equal-Width vs Equal-Depth


| 方法 | 思路 | 优点 | 局限 |
|------|------|------|------|
| Equal-width | 每个 bin 宽度差不多一样 | 简单直观 | 对 outliers 和 skewed data 敏感 |
| Equal-depth | 每个 bin 样本数差不多一样 | 更能保留分布平衡 | bin 边界不均匀 |


Equal-width 的经典宽度公式：

$$
w = \frac{x_{max} - x_{min}}{n}
$$

---
layout: default
---

# Binning 后可以怎么代表一个 bin

分箱后最常见的三种代表方式：

- Mean value
- Median value
- Bin boundaries

理解：

- mean / median 更像 smoothing
- boundaries 更像把值拉回区间边缘

---
layout: default
---

# 一句话记忆：Discretisation

- `Equal-width`：按区间宽度切，简单但怕 outlier
- `Equal-depth`：按样本数量切，更能保住分布平衡
- `Mean / median / boundary`：是在 bin 内做不同程度的 smoothing

<div class="callout mt-4 text-sm">
这部分最容易考“哪种方法更受异常值影响”以及“离散化为什么能降噪、降复杂度”。
</div>

---
layout: default
---

# 真题演练

**Which discretisation approach is usually more sensitive to outliers?**

| 选项 | 内容 |
|------|------|
| a | Equal-depth binning |
| b | Equal-width binning |
| c | Stratified sampling |
| d | Feature selection |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>这题抓的是 discretisation 的核心差异。equal-width 直接依赖整体取值范围，因此最容易被 outlier 拉大 bin width。
</div>

---
layout: section
---

# Part 5

# Data Construction

---
layout: default
---

# Feature Engineering

这里可以分成两支来看：

- **Feature extraction / generation**
  - 从 raw data 或已有特征生成新特征
- **Feature selection**
  - 从已有特征中选一个更有用的子集

---
layout: two-cols
---

# Feature Generation 的目标

- 产生更 meaningful 的特征
- 产生更 descriptive 的特征
- 产生更 discriminant 的特征

::right::

# Feature Selection 的目标

- Remove irrelevant data
- Increase predictive accuracy
- Improve learning efficiency
- Reduce complexity
- Increase interpretability

---
layout: default
---

# Feature Subset Selection

这一部分的重点是：

- 去掉 irrelevant 或 redundant features
- 用更小特征集尽量保留原始类别分布信息

常见方法：

- Stepwise forward selection
- Stepwise backward elimination
- Forward + backward combination
- Decision tree induction

---
layout: default
---

# 一句话记忆：Construction

- `Feature generation`：造出新特征
- `Feature selection`：删掉没用或重复的特征
- 目标不是“特征越多越好”，而是“信息够用、模型更稳、解释更清楚”

<div class="callout mt-4 text-sm">
做题时看到 “subset / remove redundant / improve efficiency” 往往是在指 feature selection；看到 “combine / derive / create new variable” 更像 feature generation。
</div>

---
layout: default
---

# 真题演练

**Which option best describes feature selection rather than feature generation?**

| 选项 | 内容 |
|------|------|
| a | Creating `price_per_sqft` from `price` and `area` |
| b | Combining several variables into a new linear score |
| c | Removing redundant attributes while keeping predictive power |
| d | Applying Box-Cox to reduce skewness |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>feature selection 的关键词是 “subset” 和 “remove irrelevant/redundant features”；a、b 更接近 feature generation，d 属于 transformation。
</div>

---
layout: section
---

# Part 6

# Data Sampling

---
layout: default
---

# 为什么要 Sampling

采样不只是“少拿一点数据”，它常用于：

- Reduce data volume
- Fix imbalanced distribution
- Create training / validation / testing sets

---
layout: default
---

# Simple Random Sampling

这里要清楚区分两种：

- **SRSWOR**
  - Simple random sample without replacement
- **SRSWR**
  - Simple random sample with replacement

关键区别：

- without replacement：抽过的不再放回
- with replacement：抽过后放回，可能重复抽到

---
layout: default
---

# Stratified Sampling

如果数据能分成 mutually disjoint strata：

- 先按 strata 分层
- 再在每一层内做 SRS

适合：

- 类别不平衡
- 希望每类都被代表
- 总体内部异质性较强

---
layout: default
---

# Sampling 方法怎么比较

| 方法 | 核心特点 | 常见用途 |
|------|------|------|
| SRSWOR | 不放回抽样 | 纯随机代表性抽样 |
| SRSWR | 放回抽样 | bootstrap 风格思路、重复可出现 |
| Stratified | 分层后再抽 | 处理类别失衡、确保各组覆盖 |

---
layout: default
---

# 一句话记忆：Sampling

- `SRSWOR`：最普通的随机抽样，不放回
- `SRSWR`：放回抽样，允许重复抽到
- `Stratified`：想保住各类比例、处理不平衡时最关键

<div class="callout mt-4 text-sm">
一看到题目里有 <code>imbalanced</code>、<code>representation</code>、<code>group proportion</code> 这类词，就优先联想到 stratified sampling。
</div>

---
layout: default
---

# 真题演练

**If a dataset is highly imbalanced and you want each class to be represented in the sample, which method is usually most appropriate?**

| 选项 | 内容 |
|------|------|
| a | SRSWOR |
| b | SRSWR |
| c | Stratified sampling |
| d | Min-Max scaling |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>这题考的是“方法和目标匹配”。当题目出现 class imbalance、group proportion、representation 这类词，优先想到 stratified sampling。
</div>

---
layout: default
---

# Exam / Assignment 视角怎么答

- 先说明为什么原始数据不适合直接分析
- 再指出要解决的是尺度、分布、表示还是样本结构问题
- 然后选择对应 transformation 方法
- 最后说明代价与限制

<div class="callout mt-4 text-sm">
高分答案通常会把 <code>problem -> transformation -> expected effect -> limitation</code> 讲完整。
</div>

---
layout: default
---

# Week 9 Takeaways

- transformation 是让数据更适配分析目标的过程
- scaling 和 standardisation 解决的是不同层面的“可比性”
- Box-Cox 是本周最重要的 power transformation
- discretisation 会牺牲一部分连续信息，换取更简洁表示
- feature engineering 与 feature selection 都属于 construction
- sampling 既能降规模，也能改善数据代表性

---
layout: end
---

# Next Step

- Review Week 9 content
- Connect these ideas with the applied session
- Prepare for later transformation-heavy assignment work
