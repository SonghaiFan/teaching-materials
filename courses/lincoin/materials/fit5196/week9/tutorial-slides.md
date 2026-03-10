---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
color: #333
math: katex
header: "FIT5196 Data Wrangling - Week 9 Tutorial"
footer: "Data Transformation 数据转换"
---

# 📚 FIT5196 Week 9 Tutorial

## Data Transformation 数据转换

**补习班课程 - 重点知识梳理**

---

## 📋 今天的学习目标

1. 掌握数据缩放的各种方法
2. 理解数据标准化的原理和应用
3. 学会使用 Box-Cox 变换处理偏态数据
4. 掌握数据离散化和分箱技术
5. 了解特征工程的基本概念
6. 学会数据采样方法

---

## 🔄 数据预处理流程回顾

```
原始数据 → 数据发现 → 数据收集 → 数据存储
         ↓
数据清洗 → 数据验证 → 数据转换 → 数据增强
```

**上周**: Data Cleaning (缺失值、异常值处理)
**本周**: Data Transformation (数据转换)

---

# 📊 Part 1: 数据缩放 (Data Scaling)

## 为什么需要数据缩放？

- **问题**: 不同特征的量纲差异巨大
  - 年龄: 20-80
  - 收入: 30,000-200,000
- **后果**: 机器学习算法被大数值特征"主导"
- **解决**: 将所有特征缩放到相似范围

---

## 🔹 方法 1: Min-Max Scaling

**公式**:
$$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$

**特点**:

- ✅ 结果在 [0,1] 范围内
- ❌ 对异常值敏感
- 🎯 适用于: 数据分布均匀，无极端异常值

---

**Python 代码**:

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🔹 方法 2: MaxAbs Scaling

**公式**:
$$x' = \frac{x}{\max |x|}$$

**特点**:

- ✅ 保留正负号
- ✅ 结果在 [-1,1] 范围内
- 🎯 适用于: 稀疏数据，需要保持符号

---

## 🔹 方法 3: Robust Scaling

**公式**:
$$x' = \frac{x - \text{median}(x)}{\text{IQR}}$$

**特点**:

- ✅ 对异常值鲁棒
- ✅ 使用中位数和四分位距
- 🎯 适用于: 有异常值的数据

---

**Python 代码**:

```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🔹 方法 4: Log Scaling

**公式**:
$$x' = \log(x)$$

**特点**:

- ✅ 减少数据偏态
- ✅ 展开小数值，压缩大数值
- ❌ 要求 x > 0
- 🎯 适用于: 右偏分布数据

---

# 📊 Part 2: 数据标准化 (Standardisation)

## Z-score 标准化

**公式**:
$$z = \frac{x - \mu}{\sigma}$$

**特点**:

- ✅ 结果均值=0，标准差=1
- ✅ 假设数据服从正态分布
- 🎯 适用于: 大多数机器学习算法

---

**Python 代码**:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 💡 练习题：选择合适的缩放方法

**场景 1**: 房价数据，范围从 10 万到 1000 万，有少量豪宅
**答案**: Robust Scaling (对异常值鲁棒)

**场景 2**: 图像像素值，0-255 范围，分布均匀
**答案**: Min-Max Scaling (简单有效)

**场景 3**: 用户评分数据，1-5 星，服从正态分布
**答案**: Z-score Standardisation (适合正态分布)

---

# 📊 Part 3: Box-Cox 变换

## 为什么需要 Box-Cox？

**问题**: 数据分布偏态 (skewed)

- 右偏: 少数极大值
- 左偏: 少数极小值

**解决**: 找到合适的变换，使数据更接近正态分布

---

## Box-Cox 基本公式

$$
y = \begin{cases}
\frac{x^\lambda - 1}{\lambda}, & \lambda \neq 0 \\
\log(x), & \lambda = 0
\end{cases}
$$

**参数 λ 的作用**:

- λ = 1: 不变换
- λ = 0.5: 平方根变换
- λ = 0: 对数变换
- λ = -1: 倒数变换

---

## Box-Cox 处理负数

**问题**: 基本 Box-Cox 要求 x > 0

**解决**: 扩展公式

$$
y = \begin{cases}
\frac{(x+c)^\lambda - 1}{g\lambda}, & \lambda \neq 0 \\
\frac{\log(x+c)}{g}, & \lambda = 0
\end{cases}
$$

- **c**: 偏移量，使 x+c > 0
- **g**: 缩放因子，通常用几何均值

---

## 📝 Box-Cox 实战示例

```python
from scipy import stats
import numpy as np

# 生成右偏数据
data = np.random.exponential(2, 1000)

# Box-Cox变换
transformed_data, lambda_optimal = stats.boxcox(data)

print(f"最优 λ 值: {lambda_optimal:.3f}")
```

**效果对比**:

- 原始数据: 右偏分布
- 变换后: 接近正态分布

---

# 📊 Part 4: 数据离散化 (Discretisation)

## 什么是数据离散化？

**定义**: 将连续数值转换为离散类别

**例子**:

- 年龄 25 岁 → "青年"
- 收入 50000 → "中等收入"
- 温度 32°C → "热"

---

## 离散化的好处

1. **数据压缩**: 减少存储空间
2. **噪声减少**: 平滑数据波动
3. **算法兼容**: 某些算法只接受类别数据
4. **可解释性**: 更容易理解和解释

---

# 📊 Part 5: 分箱 (Binning)

## 🔹 等宽分箱 (Equal-Width Binning)

**方法**: 将数据范围等分为 n 个区间

**公式**:
$$w = \frac{x_{max} - x_{min}}{n}$$

**例子**:
数据: [10, 15, 25, 34, 44, 48, 55, 59, 64, 69, 88, 94]
4 个等宽箱: [10-31], [31-52], [52-73], [73-94]

---

## 🔹 等深分箱 (Equal-Depth Binning)

**方法**: 每个箱包含相同数量的数据点

**例子**:
数据: [10, 15, 25, 34, 44, 48, 55, 59, 64, 69, 88, 94]
4 个等深箱 (每箱 3 个数据):

- 箱 1: [10, 15, 25]
- 箱 2: [34, 44, 48]
- 箱 3: [55, 59, 64]
- 箱 4: [69, 88, 94]

---

## 分箱后的平滑方法

1. **箱均值**: 用箱内均值替代所有值
2. **箱中位数**: 用箱内中位数替代
3. **箱边界**: 用最近的边界值替代

**Python 实现**:

```python
import pandas as pd

# 等宽分箱
pd.cut(data, bins=4, labels=['低', '中低', '中高', '高'])

# 等深分箱
pd.qcut(data, q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
```

---

# 📊 Part 6: 特征工程 (Feature Engineering)

## 特征工程的两个分支

### 🔹 特征提取/生成 (Feature Extraction/Generation)

- **目标**: 从原始数据创造新特征
- **例子**:

  - 日期 → 年、月、周几
  - 文本 → 词频、TF-IDF
  - 图像 → 边缘、纹理特征

---

### 🔹 特征选择 (Feature Selection)

- **目标**: 从现有特征中选择最重要的
- **好处**: 减少复杂度，提高性能，增强可解释性

---

## 特征选择方法

### 1. 前向选择 (Forward Selection)

- 从空集开始，逐步添加最佳特征

### 2. 后向消除 (Backward Elimination)

- 从全集开始，逐步删除最差特征

### 3. 混合方法 (Hybrid)

- 结合前向选择和后向消除

### 4. 决策树方法

- 基于信息增益选择特征

---

# 📊 Part 7: 数据采样 (Data Sampling)

## 为什么需要采样？

1. **数据量太大**: 计算资源有限
2. **类别不平衡**: 某些类别样本过少
3. **创建数据集**: 训练集/验证集/测试集划分

---

## 采样方法

### 🔹 简单随机采样 (Simple Random Sampling)

**SRSWOR (不放回)**:

- 每个样本最多被选择一次
- 适用于大数据集

**SRSWR (有放回)**:

- 样本可能被重复选择
- 适用于小数据集

---

### 🔹 分层采样 (Stratified Sampling)

**原理**: 保持各类别的原始比例

**例子**:

- 原始数据: 70%男性, 30%女性
- 采样后: 仍然保持 70%男性, 30%女性

**Python 实现**:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

---

# 🎯 综合练习

## 场景：房价预测数据预处理

**原始数据特征**:

- 面积 (sqft): 500-5000
- 价格 (price): 100,000-2,000,000
- 建造年份 (year): 1950-2023
- 地段评分 (location_score): 1-10

**任务**: 设计完整的数据转换流程

---

## 解决方案

1. **特征工程**:

   ```python
   # 创建房龄特征
   df['age'] = 2023 - df['year']

   # 创建单价特征
   df['price_per_sqft'] = df['price'] / df['sqft']
   ```

---

2. **处理偏态分布**:

   ```python
   # 价格通常右偏，使用log变换
   df['log_price'] = np.log(df['price'])
   ```

---

3. **数据缩放**:
   ```python
   # 标准化数值特征
   scaler = StandardScaler()
   numerical_features = ['sqft', 'age', 'price_per_sqft']
   df[numerical_features] = scaler.fit_transform(df[numerical_features])
   ```

---

## 4. 数据离散化:

```python
# 地段评分分箱
df['location_level'] = pd.cut(df['location_score'],
                             bins=[0, 3, 6, 10],
                             labels=['差', '中', '好'])

# 房龄分箱
df['age_group'] = pd.cut(df['age'],
                        bins=[0, 10, 30, 100],
                        labels=['新房', '次新', '老房'])
```

## 5. 数据采样:

```python
# 分层采样创建训练/测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=df['location_level']
)
```

---

# 📝 课堂小测验

## 问题 1: 选择题

以下哪种缩放方法最适合处理有异常值的收入数据？
A. Min-Max Scaling  
B. Z-score Standardisation
C. Robust Scaling
D. Log Scaling

---

**答案**: C. Robust Scaling

---

## 问题 2: 计算题

使用 Min-Max 缩放将数据 [10, 20, 30, 40, 50] 转换到 [0,1] 范围。

---

**解答**:

- min = 10, max = 50
- 10 → (10-10)/(50-10) = 0
- 20 → (20-10)/(50-10) = 0.25
- 30 → (30-10)/(50-10) = 0.5
- 40 → (40-10)/(50-10) = 0.75
- 50 → (50-10)/(50-10) = 1

---

## 问题 3: 应用题

## 有一个右偏的销售额数据，你会选择哪种变换方法？为什么？

---

**答案**:

- Box-Cox 变换或 Log 变换
- **原因**: 右偏数据通过幂变换(λ<1)或对数变换可以减少偏态，使分布更接近正态

---

# 🔚 课程总结

## 关键知识点回顾

1. **数据缩放**: Min-Max, Robust, Z-score 等方法
2. **Box-Cox 变换**: 处理偏态分布的强大工具
3. **数据离散化**: 连续 → 离散，降噪平滑
4. **分箱技术**: 等宽 vs 等深分箱
5. **特征工程**: 特征生成与选择
6. **数据采样**: 随机采样 vs 分层采样

**Good luck with your studies!** 📈
