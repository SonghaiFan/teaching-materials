---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
color: #333
header: "FIT5196 Data Wrangling - Week 9 Tutorial"
footer: "Data Transformation 数据转换"
style: |
  section {
    font-family: "Noto Sans CJK SC","Source Han Sans SC","PingFang SC","Microsoft YaHei",sans-serif;
  }
---

# 📚 FIT5196 Week 9 Tutorial

## Data Transformation 数据转换

**补习班课程 - 重点知识梳理**

---

#### 回顾：Data Wrangling Tasks

- **数据预处理阶段 (Data Pre-processing)**：对原始数据进行准备，使其更适合后续分析。
- **上周内容**：Data Cleaning → 处理缺失值、异常值。
- **整体流程**：数据发现 → 数据收集 → 数据存储 → 数据清洗 → 数据验证 → 数据转换 → 数据增强。

---

#### Data Transformation 概述

- **定义**：清理并转换原始数据，使其更适合分析。
- **目标**：确保数据处于可用、有效率的格式，让分析更简单、更可靠。

---

**涵盖内容**：

- Data Normalisation（数据标准化）
- Data Discretisation（数据离散化）
- Data Construction（数据构造）
  - Feature Engineering（特征工程）
  - Data Sampling（数据采样）

---

# Scaling 缩放

---

### Min-Max Scaling

- Formula:

  $$
  x' = \frac{x - x_{min}}{x_{max} - x_{min}}
  $$

- ⚡ Maps to [0,1], sensitive to outliers.

- ⚡ 映射到 [0,1]，对异常值敏感。

---

### MaxAbs Scaling

- Formula:

  $$
  x' = \frac{x}{\max (|x|) }
  $$

- ⚡ Keeps sign, scales to [-1,1].

- ⚡ 保留符号，缩放到 [-1,1]。

---

### Decimal Scaling

- Move decimal point by factor 10^j until max(|x|)<1.
- ⚡ Simple rescaling via decimal shift.
- ⚡ 通过小数点移动缩放。

---

### Robust Scaling

- Formula:

  $$
  x' = \frac{x - \text{median}(x)}{\text{IQR}}
  $$

- ⚡ Resistant to outliers.

- ⚡ 对异常值鲁棒。

---

### Log Scaling

- Formula:

  $$
  x' = \log(x)
  $$

- ⚡ Reduces skew, spreads small values.

- ⚡ 减少偏态，展开小数值。

---

# 2. Standardisation 标准化

### Z-score Normalisation

- Formula:

  $$
  z = \frac{x - \mu}{\sigma}
  $$

- ⚡ Mean=0, Std=1, assumes Gaussian.

- ⚡ 均值=0，标准差=1，适合正态分布算法。

---

# 3. Transformation 变换

### Linear Transformation

- Add constant (shift) or multiply constant (scale).
- ⚡ Simple shift/scale of data.
- ⚡ 简单平移/缩放数据。

---

### Power Transformation (Box-Cox)

- Formula:

  $$
  y =
  \begin{cases}
  \frac{x^\lambda - 1}{\lambda}, & \lambda \neq 0 \\
  \log(x), & \lambda = 0
  \end{cases}
  $$

- ⚡ Makes data closer to normal distribution.

- ⚡ 使数据更接近正态分布。

- **要求**：输入 $x > 0$，因为对数和幂函数在负数上不定义。

- **作用**：找到合适的 $\lambda$，把数据分布拉近正态分布。

- **特点**：只能处理严格正的连续变量（比如价格、年龄、收入）。

---

## 解决办法：取极限

当 $\lambda \to 0$ 时，可以用 **洛必达法则** 来算极限：

$$
\lim_{\lambda \to 0} \frac{x^\lambda - 1}{\lambda} = \log(x)
$$

所以当 $\lambda = 0$ 时，Box-Cox 变换就自然退化成了 **对数变换**。

---

- **连续性**：  
  这样定义后，Box-Cox 变换在不同 $\lambda$ 值下是 **连续平滑的**，不会在 $\lambda=0$ 出现“断点”。
- **灵活性**：
  - 当 $\lambda = 1$：就是线性变换（不变）。
  - 当 $\lambda = 0$：就是对数变换。
  - 当 $\lambda = 0.5$：是平方根变换。
  - 当 $\lambda = -1$：是倒数变换。
- **统一框架**：  
  Box-Cox 可以看作一个“超集”，不同 $\lambda$ 对应不同常见变换（log、sqrt、reciprocal 等），不需要单独写多个公式。

---

⚡ **一句话总结**：  
Box-Cox 用两种情况（$\lambda \neq 0$ 和 $\lambda = 0$）是为了避免除零，同时保证变换在 $\lambda = 0$ 处连续，把 **对数变换**纳入同一个统一框架里。

---

### Box-Cox with Negatives

- Formula with offset c and scale g.
- ⚡ Shift negatives (c), scale (g), optimise λ.
- ⚡ 通过 c 平移负值，g 缩放，λ 搜索最佳正态化。

$$
y =
\begin{cases}
\frac{(x+c)^\lambda - 1}{g \lambda}, & \lambda \neq 0 \\
\frac{\log(x+c)}{g}, & \lambda = 0
\end{cases}
$$

- **新增参数**：
  - $c$：把负数/零整体平移为正（offset）。
  - $g$：缩放因子，常取几何均值（geometric mean），避免数值过大或过小。
- **作用**：可以在原始数据包含 **负值** 或 **0** 的情况下仍能使用 Box-Cox。
- **好处**：更灵活，不会因为数据里有负数就没法用。

---

| Box-Cox 版本       | 输入要求    | 新增参数           | 适用场景                     |
| ------------------ | ----------- | ------------------ | ---------------------------- |
| 基础版             | $x > 0$     | 无                 | 适合自然正数（价格、销量等） |
| 扩展版（带 $c,g$） | $x + c > 0$ | 偏移 $c$、缩放 $g$ | 可处理负数、0、不同量纲数据  |

---

⚡ **一句话总结**：

- **基础版 Box-Cox** 只能处理正数变量；
- **扩展版 Box-Cox** 通过平移 $c$ 和缩放 $g$ 扩展到负数场景，更通用。
