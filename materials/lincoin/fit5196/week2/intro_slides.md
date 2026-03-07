---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
marp: true
---

# **Data Wrangling 数据规整**

## 知识点总结

FIT5196 - Data Wrangling
Week 1 & 2 Core Concepts

---

## 📋 目录

1. 什么是 Data Wrangling？
2. 为什么要做 Data Wrangling？
3. 数据规整的挑战
4. Data Wrangling 八大任务流程
5. 编程环境 & 工具

---

# 📌 一、什么是 Data Wrangling？

> 数据规整是将原始数据转换为可供分析使用的过程

---

## ✅ 定义

- **包括**：获取、清洗、结构化、丰富数据，使其适合分析
- **本质**：数据分析前的关键准备步骤
- **转换过程**：Raw Data → Clean Data → Actionable Insights

---

## ✅ 目的

- 🎯 **提高数据质量**
- 🔍 **简化访问**
- 🔗 **促进整合**
- ⚡ **降低复杂度**
- 📈 **提升分析效率**
- 💡 **支持决策制定**

---

# 📌 二、为什么要做 Data Wrangling？

> 不经过数据规整，分析可能得出错误或无法执行的结论

---

## ✅ 示例数据源

- **UCI 数据集**：census income、credit approval
- **社交媒体**：Twitter、Facebook 数据
- **百科全书**：Wikipedia 结构化数据
- **医疗影像**：CT 报告等原始数据

**问题**：格式不一、缺失严重、结构复杂

---

## ✅ 数据转换流程

```
Raw Data → Tidy Data → Actionable Insights
原始数据 → 整洁数据 → 可行动的洞察
```

**目标**：从混乱的原始数据中提取有价值的知识产品

---

<!-- _class: lead -->

# 📌 三、数据规整的挑战

---

## 🌊 数据体量挑战

- **大数据时代**：每天产生 2.5 quintillion 字节的数据
- **处理难度**：传统工具无法有效处理大规模数据
- **存储与计算**：需要分布式系统和云计算支持

---

## 🎯 质量问题

- **缺失值**：数据不完整
- **错误值**：输入错误、系统故障
- **重复数据**：同一记录多次出现
- **格式不一致**：日期、货币、地址格式混乱

---

## 🔄 多源数据整合

- **格式多样**：JSON、XML、CSV、Excel、图片等
- **结构差异**：结构化 vs 半结构化 vs 非结构化
- **标准不一**：缺少统一的数据交换标准

---

## ⏰ 时间与技能挑战

- **耗时严重**：数据科学家 60% 的时间用于清洗和组织数据
- **技能要求高**：需掌握 Python、统计、NLP、数据库等
- **隐私与安全**：特别是医疗等敏感领域的合规要求

---

<!-- _class: lead -->

# 📌 四、Data Wrangling 八大任务流程

---

## 🔄 完整流程图

```
Data Discovery → Data Collection → Data Pre-processing
     ↓
Data Cleaning → Data Transformation → Data Enrichment
     ↓
Data Validation → Data Storing
```

---

## 1. 🔍 Data Discovery

- **目标**：找出可用的数据源
- **评估维度**：
  - 可访问性 (Accessibility)
  - 适用性 (Relevance)
  - 质量 (Quality)
  - 成本 (Cost)

---

## 2. 📥 Data Collection

**考虑因素**：

- 🎯 目标 (Objectives)
- 📊 格式 (Format)
- 📈 体量 (Volume)
- 🔒 隐私 (Privacy)
- 💰 预算 (Budget)
- ⏰ 时间 (Timeline)

---

## 3. ⚙️ Data Pre-processing

- **子集选择**：筛选相关数据
- **抽样**：处理大数据集
- **格式转换**：统一数据格式
- **单位转换**：标准化度量单位
- **文本标准化**：处理编码、大小写等

---

## 4. 🧹 Data Cleaning

**主要任务**：

- 处理缺失值 (Missing Values)
- 识别异常值 (Outliers)
- 去除重复 (Duplicates)
- 修正格式不一致 (Format Inconsistencies)

---

<!-- _class: lead -->

# 5. 🔄 Data Transformation

---

### 📊 数值数据转换

- **归一化** (Normalization)
- **标准化** (Standardization)
- **聚合** (Aggregation)
- **离散化** (Discretization)
- **分箱** (Binning)

---

### 📝 文本数据转换

- **分词** (Tokenization)
- **词干化** (Stemming)
- **向量化** (Vectorization)
- **情感分析** (Sentiment Analysis)

---

### 🖼️ 图像数据转换

- **尺寸调整** (Resizing)
- **颜色空间转换** (Color Space Conversion)
- **旋转与翻转** (Rotation & Flipping)
- **加噪与增强** (Noise & Augmentation)

---

## 6. 🔧 Data Enrichment

- **整合数据源**：合并多个数据集
- **增加属性**：计算新的特征
- **时间维度**：添加时间序列信息
- **语义信息**：增强数据表达力

---

## 7. ✅ Data Validation

**检查项目**：

- 📏 准确性 (Accuracy)
- 🔄 一致性 (Consistency)
- 🧩 逻辑完整性 (Logical Completeness)
- 📊 范围限制 (Range Constraints)
- 📝 格式规范 (Format Standards)

---

## 8. 💾 Data Storing

**存储考虑**：

- 🏗️ 结构设计 (Schema Design)
- 🔒 安全性 (Security)
- 📇 索引优化 (Indexing)
- 💾 备份策略 (Backup)
- 🔄 生命周期管理 (Lifecycle Management)

---

<!-- _class: lead -->

# 📌 五、编程环境 & 工具

---

## 🐍 编程语言：Python 3.12

**核心优势**：

- 语法简洁易学
- 丰富的数据处理库
- 强大的社区支持
- 跨平台兼容性

---

## 📚 常用 Python 库

- **`pandas`**：数据结构和处理
- **`NLTK`**：自然语言处理
- **`BeautifulSoup`**：HTML/XML 解析
- **`scikit-learn`**：数据挖掘与分析
- **`scipy`**：科学计算
- **`numpy`**：数值计算基础

---

## 🛠️ 推荐开发环境

### 主要选择：

- **Jupyter Notebook** - 交互式开发
- **Anaconda** - 完整的数据科学平台
- **Google Colab** - 云端免费 GPU 支持

### 其他工具：

- **VS Code** - 专业代码编辑器
- **PyCharm** - Python 集成开发环境

---

# 🎯 总结

Data Wrangling 是数据科学的基础，掌握其核心概念和流程对于：

- 🎯 **提升数据质量**
- ⚡ **加速分析过程**
- 💡 **支持决策制定**
- 🚀 **推动业务价值创造**

至关重要！

---

# Thank You!

## 谢谢

**Questions & Discussion**

FIT5196 - Data Wrangling
