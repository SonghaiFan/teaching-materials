---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
color: #333
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

## Core Data Processes 核心数据处理

### Data Cleansing (Data Cleaning) 数据清洗

- Detecting and correcting corrupt or inaccurate records
- 检测并纠正损坏或不准确的记录

### Data Audit 数据审计

- Systematic review to identify quality issues
- 系统性审查以识别质量问题

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

---

## Missing Data: The Challenge 缺失数据挑战

**Missing Data**: Data points with no value for a variable
缺失数据：在某变量上没有值的数据点

### Missing Data Mechanisms 缺失数据机制

- **MCAR** (Missing Completely At Random) 完全随机缺失
- **MAR** (Missing At Random) 随机缺失
- **MNAR** (Missing Not At Random) 非随机缺失

> Understanding the mechanism determines the handling method
> 理解缺失机制决定了处理方法

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

### Stochastic Regression 随机回归插补

```
Pi = β₀ + β₁ × IQi + zi
where zi ~ N(0, σ²)
```

- Adds random residuals to restore variability

---

## Advanced Missing Data Methods 高级缺失数据方法

### Model-Based Methods 基于模型的方法

**Maximum Likelihood**

- Models the data to address missingness
- Less biased under MAR/MNAR assumptions

**Multiple Imputation**

- Creates multiple complete datasets
- Combines results to account for uncertainty
- Generally provides more robust estimates

> These methods minimize bias and use all available information
> 这些方法最小化偏差并利用所有可用信息

---

## Outliers: Special Cases 异常值处理

**Outliers**: Observations markedly different from others
异常值：明显不同于其他观测值的样本

### Impact 影响

- May distort analyses
- Require special handling
- Could indicate data errors or genuine extreme cases

### Handling Approaches 处理方法

- Investigation and validation
- Transformation or removal
- Robust statistical methods

---

## Data Cleansing Operations Checklist 数据清理操作检查表

### Core Operations 核心操作

✅ **Removing duplicates** 删除重复项
✅ **Validating and correcting errors** 验证并纠正错误
✅ **Consistency checks** 一致性检查
✅ **Filling missing values** 填充缺失值
✅ **Handling outliers** 处理异常值

### Tools 工具

- Excel, Talend, IBM InfoSphere
- OpenRefine, Python/R libraries
- Mix of automated tools + human judgment

---

## Data Audit Outputs 数据审计输出

### Quality Metrics 质量指标

- **Accuracy** measures 准确性度量
- **Completeness** assessment 完整性评估
- **Consistency** checks 一致性检查
- **Reliability** evaluation 可靠性评估

### Additional Outputs 其他输出

- Data mapping across organization
- Sampling strategies for analysis
- Software tools + manual review processes

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

## Verification & Documentation 验证与文档记录

### Verification Ensures 验证确保

- Final data meet quality criteria
- Data ready for analysis
- Accuracy, consistency, completeness

---

### Documentation Captures 文档记录捕捉

- What was done (reproducibility)
- Methods used
- Decisions made
- Results achieved

> Essential for transparency and future reference
> 对透明度和未来参考至关重要

---

## Key Takeaways for Success 成功要点

### Process Understanding 流程理解

- Data cleansing is **iterative** and **documented**
- Start with audit → define goals → plan → execute → verify

### Method Selection 方法选择

- **MCAR vs MAR vs MNAR** determines approach
- **Deletion methods**: Simple but can waste data
- **Imputation methods**: Preserve data but have trade-offs
- **Model-based methods**: Most robust under MAR/MNAR

---

### Practical Skills 实践技能

- Identify and handle duplicates
- Write queries to find/resolve data issues
- Balance automation with human judgment

---

## Why Clean Data Matters 为什么干净数据很重要

### Impact Areas 影响领域

**Machine Learning** 机器学习

- Better model performance
- Reduced bias in predictions

**Statistics** 统计学

- Valid inference and conclusions
- Accurate parameter estimates

**Business Intelligence** 商业智能

- Reliable reporting and dashboards
- Trustworthy decision support

> **Bottom Line**: Clean data underpins trustworthy analyses
> 底线：干净的数据是可信分析的基础

---

## Summary: The Data Quality Journey

```
Poor Data Quality → Data Audit → Cleansing Plan
        ↓                ↓              ↓
   Biased Results ← Clean Data ← Proper Methods
        ↓                ↓              ↓
  Wrong Decisions → Good Analysis → Right Decisions
```

### Remember 记住

- **Quality first**: Invest time in understanding your data
- **Document everything**: Make your process reproducible
- **Choose wisely**: Match methods to missing data mechanisms
- **Verify thoroughly**: Ensure results meet quality standards

---

# Questions?

### Thank you for your attention!
