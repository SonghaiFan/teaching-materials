---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
color: #333
style: |
  section {
    font-family: "Noto Sans CJK SC","Source Han Sans SC","PingFang SC","Microsoft YaHei",sans-serif;
  }
---

# Data Quality & Data Cleansing

## FIT5196 Data Wrangling

### Key Concepts

---

## What is Data Quality? 数据质量

**Data Quality**: The overall condition of data based on:

- **Accuracy** 准确性 - Data correctly represents reality
- **Completeness** 完整性 - All required data is present
- **Reliability** 可靠性 - Data is consistent and trustworthy
- **Relevance** 相关性 - Data is applicable to the context
- **Timeliness** 及时性 - Data is up-to-date

> **Why it matters**: Good decisions rely on good data
> 重要性：良好的决策依赖于良好的数据

---

## The Data Cleansing Workflow 数据清洗工作流程

```
Data Audit → Define Goals → Cleansing Plan → Backup Data
     ↑                                               ↓
Review ← Documentation ← Verification ← Cleansing Operations
```

1. **Data Audit** 数据审计
2. **Define Cleansing Goals** 定义清洗目标
3. **Data Cleansing Plan** 数据清洗计划
4. **Backup Data** 备份数据
5. **Data Cleansing Operations** 数据清洗操作
6. **Verification** 验证
7. **Documentation & Reporting** 文档记录与报告
8. **Review** 复审 (feedback loop)

## Missing Data: The Challenge 缺失数据挑战

---

**Missing Data**: Data points with no value for a variable
缺失数据：在某变量上没有值的数据点

### Missing Data Mechanisms 缺失数据机制

- **MCAR** (Missing Completely At Random) 完全随机缺失
- **MAR** (Missing At Random) 随机缺失
- **MNAR** (Missing Not At Random) 非随机缺失

> Understanding the mechanism determines the handling method
> 理解缺失机制决定了处理方法

---

| 机制     | 解释                                     | 举例                                                         | 处理方法                                                             |
| -------- | ---------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------- |
| **MCAR** | 缺失纯属意外，和任何变量都没关系         | 问卷有几页纸被风吹走丢了，缺失答案和人的情况无关             | 可以直接删除（listwise / pairwise），影响不大                        |
| **MAR**  | 缺失和**别的变量**有关，但和自己本身无关 | 年轻人更容易不填“收入”问题（和年龄相关，但不是因为收入多少） | 可以用插补（回归插补、均值插补），模型能利用其他变量预测             |
| **MNAR** | 缺失和**自己本身的值**有关               | 高收入的人更可能拒绝填写收入问题                             | 需要建模专门处理（如选择模型、模式混合模型），不能随便忽略或简单插补 |

---

⚡ 一句话记忆：

- **MCAR** = 数据意外掉了，最无害。
- **MAR** = 和别的变量有关系，能补救。
- **MNAR** = 和缺失值自己有关系，最麻烦。

---

## Handling Missing Data: Deletion Methods 删除方法

### Listwise Deletion (Complete Case) 逐案删除

- Remove any case with missing values
- **Pros**: Simple, unbiased if MCAR
- **Cons**: Reduces sample size, wastes data

### Pairwise Deletion (Available Case) 成对删除

- Use all available data for each analysis
- **Pros**: Preserves more data
- **Cons**: Can distort estimates if MCAR assumption fails

> **Key**: Both methods rely on MCAR assumption
> 关键：两种方法都依赖于 MCAR 假设

---

⚡ 一句话总结：

- **Listwise** = 缺一项就丢整行 → 简单但浪费。
- **Pairwise** = 用得上就用 → 数据利用率高，但容易出偏差。

---

## Missing Data Patterns 缺失数据模式

### Pattern Types 模式类型

**Univariate** 单变量

- Missing values in one variable only

**Monotone** 单调

- If variable X is missing, all subsequent variables are missing

**General** 一般

- Arbitrary missing data patterns
- Most complex to handle

---

⚡ 一句话总结：

- **Univariate** = 缺在一个变量上。
- **Monotone** = 越往后缺得越多，像逐步退出。
- **General** = 哪里都可能缺，没规律。

---

## Handling Missing Data: Imputation Methods 插补方法

### Mean Imputation 均值插补

- Replace missing values with variable mean
- **Issue**: Reduces variability

---

### Regression Imputation 回归插补

```
JPi = β₀ + β₁ × IQi
```

- Uses relationships between variables
- **Issue**: Can be biased if model is wrong

---

### Stochastic Regression 随机回归插补

```
Pi = β₀ + β₁ × IQi + zi
where zi ~ N(0, σ²)
```

- Adds random residuals to restore variability

---

### Evaluate a missing-data method

1. Minimise bias —— 尽量减少偏差
2. Maximise the use of available information —— 最大化利用已有数据
3. Yield good estimates of uncertainty —— 给出合理的不确定性估计

⚡ 一句话总结：  
一个好的缺失数据处理方法 = **偏差小 + 不浪费数据 + 不确定性估计准确**。

---

# 🚨 Outliers（异常值）

## **异常值的影响 (Impacts of Outliers)**

- **增加误差方差** → 让统计检验的 **显著性检验力下降**。
- **破坏正态性** → 如果异常值分布不随机，会让数据偏离正态分布假设。
- **偏倚估计** → 影响均值、回归系数等关键参数。
- **破坏模型假设** → 例如回归、ANOVA 等统计模型通常假设残差独立同分布，异常值会破坏这些前提。

---

## **异常值的类型 (Types of Outliers)**

- **单变量异常值 (Univariate outlier)**  
  只考虑一个变量的数据分布，偏离过大就是异常。
- **多变量异常值 (Multivariate outlier)**  
  在多维空间里，点和整体数据分布差异过大就是异常。

---

## **单变量异常值检测 (Univariate Outlier Detection)**

- **基准值 (x₀)**：均值 (mean) 或 中位数 (median)
- **波动尺度 (ζ)**：标准差 (σ)、MAD、IQR
- **阈值 (t)**：通常取 3
- **判定条件**： $|x_k - x_0| > t \times \zeta$

---

## 3σ Rule（三倍标准差规则, Extreme Studentized Deviation）

- **基本思想**：如果数据大致符合正态分布（均值 μ，标准差 σ），那么超过 3σ 的值出现概率只有 **0.3%**。
- **判定条件**：
  $$
    |x_k - \bar{x}| > 3\sigma
  $$
  就认为是异常值。
- **缺点**：如果数据里本身就有异常值，它们会拉高均值和标准差 → 导致检测不准确。

---

## Hampel Identifier（汉佩尔识别法）

- **基本思想**：用 **中位数 (Median)** 和 **中位数绝对偏差 (MAD)** 代替均值和标准差，更稳健。

  - 参考值 $x_0 = median(x)$
  - 变异尺度 $\zeta = 1.4826 \times median(|x_k - median(x)|)$

- **判定条件**：
  $$
  |x_k - x_0| > 3\zeta
  $$
- **优点**：对异常值不敏感，比 3σ 更稳健。
- **缺点**：如果超过 50% 的数据都相同，MAD = 0，方法失效。

---

## 四分位数法（Boxplot / IQR Rule）

- **原理**：基于箱线图的四分位数范围（IQR = Q3 - Q1）。
- **判定条件**：
  $$
  x_k < Q1 - 1.5 \times IQR \quad \text{或} \quad x_k > Q3 + 1.5 \times IQR
  $$
- **优点**：简单直观，适用于非正态分布数据。

---

## **单变量异常值检测 (Univariate Outlier Detection)**

- **基准值 (x₀)**：均值 (mean) 或 中位数 (median)
- **波动尺度 (ζ)**：标准差 (σ)、MAD、IQR
- **阈值 (t)**：通常取 3
- **判定条件**： $|x_k - x_0| > t \times \zeta$

---

### 组合规则

- **3σ 规则**： $x_0 = \bar{x}, \zeta = \sigma$
  判定条件： $|x_k - \bar{x}| > 3\zeta$
- **Hampel 方法**： $x_0 = x^\dagger, \zeta = 1.4826 \times MAD$
  判定条件： $|x_k - x^\dagger| > 3\zeta$
- **箱线图规则 (Boxplot Rule)**： $\quad x_0 \in \{Q1, Q3\}, \zeta = IQR$
  判定条件： $|x_k - x_0| > 1.5\zeta$

---

⚡ **一句话总结**：  
检测异常值就是：先选一个 **基准值**（均值 or 中位数），再选一个 **波动尺度**（标准差、MAD、IQR），设定一个阈值 $t$，超出范围的点就算异常。
