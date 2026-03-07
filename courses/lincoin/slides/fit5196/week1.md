---
theme: default
title: FIT5196 - Week 1 辅导
layout: cover
info: |
  ## FIT5196 Week 1 课外辅导
  数据规整核心概念 + Python 基础强化
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

<style>
@import '../styles/lincoin-theme.css';
</style>

# FIT5196 数据规整

## Week 1 课外辅导

<div class="mt-8 text-sm" style="color: var(--lincoin-text-soft);">
上半场：核心概念回顾 (50分钟)<br>
下半场：Python 基础强化 (50分钟)
</div>

---

# 今日安排

## 上半场：核心概念回顾
1. 什么是数据规整 (Data Wrangling) ?
2. 为什么要做数据规整 ?
3. 数据规整的挑战
4. 六大任务流程

## 下半场：Python 基础强化
1. Jupyter Notebook 快速上手
2. Python 核心语法回顾
3. 代码实践练习

<div class="mt-4" style="border-left: 3px solid var(--lincoin-primary); padding-left: 1rem; font-size: 0.875rem; color: var(--lincoin-text-soft);">
提示：课内详细内容请参考学校课件，有问题积极在 Ed Forum 向老师提问
</div>

---
layout: section
---

# 第一部分：核心概念回顾

---

# 什么是数据规整 ?

> "数据规整是将原始数据转换为可供分析使用的过程"

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
定义包括：获取、清洗、结构化、丰富数据，使其适合分析
</div>

---

# 数据规整的本质

<div class="grid grid-cols-3 gap-4 text-center">

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold text-lg">Raw Data</h3>
  <p class="text-sm mt-2 text-slate-500">原始数据</p>
  <ul class="text-xs mt-2 text-left">
    <li>格式混乱</li>
    <li>质量参差</li>
    <li>结构复杂</li>
  </ul>
</div>

<div class="border border-slate-300 bg-sky-100 p-4">
  <h3 class="font-bold text-lg text-sky-700">Wrangling</h3>
  <p class="text-sm mt-2 text-sky-600">数据规整</p>
  <ul class="text-xs mt-2 text-left">
    <li>清洗</li>
    <li>转换</li>
    <li>结构化</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold text-lg">Clean Data</h3>
  <p class="text-sm mt-2 text-slate-500">整洁数据</p>
  <ul class="text-xs mt-2 text-left">
    <li>格式统一</li>
    <li>质量可靠</li>
    <li>结构清晰</li>
  </ul>
</div>

</div>

---

# 数据规整的目的

| 目的 | 说明 |
|------|------|
| **提高数据质量** | 修复错误、填补缺失、去除噪声 |
| **简化访问** | 统一格式，便于查询和使用 |
| **促进整合** | 合并多源数据，形成完整视图 |
| **降低复杂度** | 简化数据结构，易于分析 |
| **提升分析效率** | 减少后续处理时间 |
| **支持决策制定** | 提供可靠的数据基础 |

---

# 为什么要做数据规整 ?

> "不经过数据规整，分析可能得出错误或无法执行的结论"

---

# 常见数据源与问题

**示例数据源：**
- UCI 数据集：census income、credit approval
- 社交媒体：Twitter、Facebook
- 数据百科全书：Wikipedia
- 医疗影像：CT 报告等

**原始数据常见问题：**
- 格式不一
- 缺失严重
- 结构复杂

---

# 数据转换流程

```
Raw Data        ->    Tidy Data        ->    Actionable Insights
原始数据              整洁数据                可行动的洞察
   |                      |                        |
格式混乱              格式统一                  有价值
质量参差              质量可靠                  可分析
结构复杂              结构清晰                  可决策
```

**目标：** 从混乱的原始数据中提取有价值的知识产品

---
layout: section
---

# 数据规整的挑战

---

# 挑战一：数据体量

**大数据时代：**
- 每天产生 2.5 quintillion 字节的数据
- 传统工具无法有效处理大规模数据
- 需要分布式系统和云计算支持

<div class="mt-4 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
应对：学习使用 Pandas、Dask、Spark 等工具
</div>

---

# 挑战二：质量问题

| 问题类型 | 具体表现 | 处理方法 |
|----------|----------|----------|
| **缺失值** | 数据不完整 | 填补、删除、标记 |
| **错误值** | 输入错误、系统故障 | 识别、修正、删除 |
| **重复数据** | 同一记录多次出现 | 去重、合并 |
| **格式不一致** | 日期、货币、地址格式混乱 | 标准化 |

---

# 挑战三：多源数据整合

**格式多样：**
- JSON、XML、CSV、Excel
- 图片、音频、视频

**结构差异：**
- 结构化 vs 半结构化 vs 非结构化

**标准不一：**
- 缺少统一的数据交换标准

---

# 挑战四：时间与技能

**时间挑战：**
- 数据科学家 60% 的时间用于清洗和组织数据
- 数据规整是最耗时的环节

**技能要求：**
- Python 编程
- 统计学基础
- 自然语言处理 (NLP)
- 数据库知识

**隐私与安全：**
- 特别是医疗等敏感领域的合规要求

---
layout: section
---

# 六大任务流程

---

# 完整流程图

```
Data Discovery          ->      Data Collection
数据发现                         数据收集
        |                              |
        v                              v
Data Pre-processing     ->      Data Cleaning
数据预处理                       数据清洗
        |                              |
        v                              v
Data Transformation     ->      Data Enrichment
数据转换                         数据丰富
        |                              |
        v                              v
Data Validation         ->      Data Storing
数据验证                         数据存储
```

---

# 1. Data Discovery (数据发现)

**目标：** 找出可用的数据源

**评估维度：**
- **可访问性 (Accessibility)** - 能否获取到数据
- **适用性 (Relevance)** - 数据是否适合解决问题
- **质量 (Quality)** - 数据的准确性和完整性
- **成本 (Cost)** - 获取和处理数据的成本

---

# 2. Data Collection (数据收集)

**考虑因素：**

| 因素 | 说明 |
|------|------|
| **目标 (Objectives)** | 收集数据的目的 |
| **格式 (Format)** | 数据的存储格式 |
| **体量 (Volume)** | 数据的大小和规模 |
| **隐私 (Privacy)** | 数据隐私和合规要求 |
| **预算 (Budget)** | 收集数据的成本预算 |
| **时间 (Timeline)** | 收集数据的时间限制 |

---

# 3. Data Pre-processing (数据预处理)

| 任务 | 说明 |
|------|------|
| **子集选择** | 筛选相关数据 |
| **抽样** | 处理大数据集 |
| **格式转换** | 统一数据格式 |
| **单位转换** | 标准化度量单位 |
| **文本标准化** | 处理编码、大小写等 |

---

# 4. Data Cleaning (数据清洗)

**主要任务：**

- **处理缺失值 (Missing Values)**
  - 删除、填补、插值

- **识别异常值 (Outliers)**
  - 统计方法、可视化检测

- **去除重复 (Duplicates)**
  - 识别并合并重复记录

- **修正格式不一致 (Format Inconsistencies)**
  - 标准化日期、货币等格式

---

# 5. Data Transformation (数据转换)

**常见转换操作：**

- **规范化 (Normalization)** - 将数据缩放到特定范围
- **标准化 (Standardization)** - 均值为0，标准差为1
- **离散化 (Discretization)** - 连续值转为离散类别
- **特征工程 (Feature Engineering)** - 创建新特征
- **数据聚合 (Aggregation)** - 汇总和统计

---

# 6. Data Enrichment & Validation

**Data Enrichment (数据丰富)**
- 合并外部数据源
- 添加元数据
- 补充上下文信息

**Data Validation (数据验证)**
- 检查数据完整性
- 验证数据准确性
- 确保符合业务规则

---
layout: section
---

# 第二部分：Python 基础强化

---

# Jupyter Notebook 简介

**Jupyter Notebook** = 交互式编程环境

**主要优势：**
- 代码 + 文档一体
- 即时查看结果
- 易于分享和展示

**两种单元格：**
- **代码单元格**：运行 Python 代码
- **Markdown 单元格**：编写文档说明

---

# Markdown 快速参考

**标题：**
```markdown
# 一级标题
## 二级标题
### 三级标题
```

**列表：**
```markdown
- 项目符号
- 项目符号

1. 编号列表
2. 编号列表
```

**链接和代码：**
```markdown
[链接文字](https://example.com)
`行内代码`
```

---

# Python 基础回顾

### 变量与数据类型
```python
# 数字
x = 10
y = 3.14

# 字符串
name = "Alice"

# 列表
fruits = ["apple", "banana"]

# 字典
person = {"name": "Bob", "age": 25}
```

---

# For 循环详解

### 基本形式
```python
# 遍历列表
for item in ["a", "b", "c"]:
    print(item)

# 遍历范围
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# 遍历字符串
for char in "hello":
    print(char)
```

### 带索引的遍历
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

---

# 嵌套循环

### 二维数据处理
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 遍历每个元素
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

### 常见应用：乘法表
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ")
    print()
```

---

# 函数定义

### 基本结构
```python
def 函数名(参数):
    """文档字符串（说明函数作用）"""
    # 函数体
    return 返回值
```

### 示例
```python
def greet(name):
    """向指定名字打招呼"""
    return f"Hello, {name}!"

# 调用
message = greet("Alice")
print(message)  # Hello, Alice!
```

---

# 实践练习

### 练习 1：计算矩阵所有元素之和
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 你的代码
```

### 练习 2：矩阵转置
```python
def transpose(matrix):
    """实现矩阵转置"""
    # 你的代码
    pass

# 测试
result = transpose([[1, 2], [3, 4], [5, 6]])
# 期望输出: [[1, 3, 5], [2, 4, 6]]
```

---
layout: two-cols
---

# 参考答案

### 练习 1
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

total = 0
for row in matrix:
    for element in row:
        total += element

print(total)  # 45
```
::right::

### 练习 2
```python
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        result.append(new_row)
    
    return result
```

---

# Jupyter 快捷键速查

| 快捷键 | 功能 |
|--------|------|
| `Shift + Enter` | 运行当前单元格 |
| `Esc` | 进入命令模式（蓝框） |
| `Enter` | 进入编辑模式（绿框） |
| `B` | 下方插入单元格 |
| `A` | 上方插入单元格 |
| `M` | 转为 Markdown 单元格 |
| `Y` | 转为代码单元格 |
| `H` | 查看所有快捷键 |

---
layout: statement
---

课上有不懂的，记得多用 Ed Forum 向老师提问！

---
layout: end
---

# 下周预告

## Week 2：数据规整流程详解 + 正则表达式入门

- 六大任务流程深入讲解
- 正则表达式基础语法
- 文本处理实践

<div class="mt-8 text-sm">
课后多练习，有问题随时交流！
</div>
