---
theme: apple-basic
title: FIT5196 - 软知识与硬知识辅导
layout: intro
---

# FIT5196 Data Wrangling

## 软知识 + 硬知识辅导


---
layout: default
---

# 课程安排

| Week | 主题 |
|------|------|
| 1 | Introduction to Data Wrangling |
| 2 | Data Wrangling Process & Tasks |
| 3 | Regular Expression |
| 4-5 | EDA / Data Discovery / Collection |
| 6 | Data Structuring |
| 7-11 | Quality, Cleaning, Transformation, Enrichment, Validation |
| 12 | Advanced Data Wrangling |


---
layout: section
---

# 作业与时间


---
layout: default
---

# Assessment 总表

| 项目 | 权重 | 内容 | 截止时间 | 形式 |
|------|------|------|----------|------|
| Quiz 1 | 10% | Applied session MCQ | Week 6 | 个人、线下 |
| Quiz 2 | 10% | Applied session MCQ | Week 12 | 个人、线下 |
| Assessment 1 | 35% | Coding + Report + Demo Video | Week 7 周四 23:55 | 小组 |
| Assessment 2 | 40% | Coding + Report | Week 12 周四 23:55 | 小组 |
| Presentation | 未单独列权重 | 课堂展示 | Week 15 周一 / 周二 | 小组 |
| In-class Participation | 5% | 课堂活动 | 若干周 seminar | 个人 |


---
layout: two-cols
---

# Assessment 1

### - EDA

- 读取和提取数据
- 做基础预处理
- 做 exploratory data analysis
- 使用合适的可视化
- 总结 raw / processed data 的发现

::right::

# Assessment 2
### - Parsing, Cleansing, Integrating

- 检查并审计 parsed data
- 识别 lexical errors / irregularities
- 处理 duplication / inconsistency
- 修复并整合多源数据


---
layout: default
---

# Quiz 和 Group Assessment 规则

- `Quiz 1` 覆盖 Week 1-6，`Quiz 2` 覆盖 Week 7-12
- 每次 quiz `30 minutes`
- 必须 `in-person` 完成 applied session quiz
- quiz 是个人作业，不允许 collaboration，不应使用 AI
- quiz 会使用 `Safe Exam Browser`
- in-class participation 也是跟 seminar 时段绑定的
- `Assessment 1/2` 是 group work，通常没有 2-day short extension
- presentation 在 `Week 15`，而且有 hurdle 要求


---
layout: default
---

# 你需要尽早掌握什么

- `Python` 基础：变量、list、dict、for loop、function  
- `Jupyter Notebook`：写代码、写 markdown、记录分析过程  
- `pandas` 基础操作：读取、查看和简单处理数据  
- 数据清洗思路：缺失值、异常值、重复、不一致  
- 基础数据可视化  
- 读懂常见数据格式：`CSV`、`JSON`、`HTML/XML`


---
layout: section
---

# 软知识：定义、目标与挑战



---
layout: statement
---

## Data Wrangling 是把原始数据变成可分析数据的过程。

`Raw Data -> Clean / Tidy Data -> Actionable Insights`

| 不要误解成 | 原因 |
|-----------|------|
| 只是可视化 | 可视化只是后续分析的一部分 |
| 只是数据清洗 | 清洗只是流程中的一环 |
| 只是机器学习 | wrangling 是分析前准备工作 |


---
layout: default
---

# 真题讲解

**What is the primary purpose of Data Wrangling?**

| 选项 | 内容 |
|------|------|
| a | To analyze complex data types |
| b | To ensure data privacy |
| c | To acquire, clean, structure, and enrich raw data for analysis |
| d | To visualize data trends |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>题干问的是 primary purpose，所以选最完整定义。privacy、visualization 都相关，但不是核心定义。
</div>


---
layout: default
---

# Data Wrangling 的主要目标

| 目标 | 含义 |
|------|------|
| Improve quality | 提高数据质量 |
| Simplify access | 让数据更容易获取和使用 |
| Support integration | 让多源数据更容易整合 |
| Reduce complexity | 降低处理难度 |
| Improve efficiency | 提高分析效率 |
| Support decisions | 支持后续决策 |


---
layout: default
---

# 真题演练

**Which of the following are common goals of data wrangling?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Increasing data complexity |
| b | Ignoring data inconsistencies |
| c | Improving data quality |
| d | Facilitating easier access to data |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c, d</code><br>
<strong>讲解：</strong>看到 goals 先排除反项。increase complexity、ignore inconsistencies 都是典型干扰项。
</div>


---
layout: default
---

# 为什么一定要做 Wrangling

| 原始数据问题 | 会导致什么 |
|--------------|------------|
| Missing values | 结果不稳定、信息不完整 |
| Wrong values | 结论错误 |
| Duplicate records | 统计被放大 |
| Inconsistent formats | 难以合并和比较 |
| Complex structures | 无法直接分析 |


---
layout: default
---

# 现实中的数据来源

- 表格：CSV、Excel、数据库导出
- 半结构化：JSON、XML、HTML
- 文本：日志、评论、报告
- 图像与传感器：医疗影像、wearable devices
- 开放与平台数据：UCI、Wikipedia、social media

<div class="muted mt-4 text-sm">
重点不是来源越多越好，而是 accessibility、relevance、quality、cost 是否合适。
</div>


---
layout: default
---

# Wrangling的挑战

| 挑战 | 具体表现 |
|------|----------|
| Volume and scalability | 数据量大，传统工具顶不住 |
| Data quality | 缺失、错误、异常、重复 |
| Diverse sources | 来源多、结构杂 |
| Lack of standardization | 日期、货币、命名规则不统一 |
| Time-consuming | 大量时间花在清洗和整理 |
| Skills and tools | 要会 Python、统计、数据库、NLP |
| Privacy and security | 敏感数据要合规处理 |


---
layout: default
---

# 真题演练

**A major challenge in data wrangling is:**

| 选项 | 内容 |
|------|------|
| a | Avoiding data standardization |
| b | Maintaining low data quality |
| c | Data privacy and security |
| d | Handling small volumes of data |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c</code><br>
<strong>讲解：</strong>Week 1 的 challenge 重点是 volume、quality、diversity、standardization、privacy/security。small volumes 不是挑战。
</div>


---
layout: two-cols
---

# 工具链

| 工具 | 用途 |
|------|------|
| Python 3 | 主语言 |
| Jupyter Notebook | 代码、文字、输出放一起 |
| Google Colab | 免安装练习环境 |
| Anaconda | 本地数据科学环境 |
| VS Code / PyCharm | 后续脚本开发 |

::right::

| 常见库 | 用途 |
|--------|------|
| `pandas` | 表格数据处理 |
| `numpy` | 数值计算 |
| `scipy` | 科学计算 |
| `scikit-learn` | 数据分析与建模工具 |
| `BeautifulSoup` | HTML/XML 解析 |
| `NLTK` | 文本处理 |


---
layout: section
---

# 软知识：流程与判断


---
layout: default
---

# Data Wrangling 的八大步骤

| 步骤 | 含义 |
|------|------|
| Discovery | 发现数据 |
| Collection | 收集数据 |
| Pre-processing | 预处理 |
| Cleaning | 数据清洗 |
| Transformation | 数据转换 |
| Enrichment | 数据增强 / 补充信息 |
| Validation | 数据验证 |
| Storing | 数据存储 |


---
layout: default
---

# 真题演练

**Which of the following are considered tasks in the Data Wrangling process?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Data Modification |
| b | Data Storing |
| c | Data Validation |
| d | Data Presentation |
| e | Data Cleaning |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b, c, e</code><br>
<strong>讲解：</strong>看到 pipeline 里的标准任务就选；presentation 不是本课程定义的 wrangling task，modification 过于模糊，不是课上标准标签。
</div>


---
layout: two-cols
---

# 1. Discovery

- 先确认要解决什么分析问题
- 找可能的数据来源，不是立刻下载
- 评估来源是否可访问、相关、可用
- 先看 suitability / availability / quality

::right::

# 医疗案例:

- EHR / 电子病历
- admission / discharge records
- insurance claims
- wearable device data
- patient histories / medications

<div class="muted mt-4 text-sm">
关键词：identify sources, accessibility, suitability, quality
</div>


---
layout: default
---

# 真题讲解

**Which phase comes immediately after data discovery?**

| 选项 | 内容 |
|------|------|
| a | Data storage |
| b | Data collection |
| c | Data cleaning |
| d | Data analysis |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>Week 2 八步流程必须背顺序。最常见考法就是问前后相邻步骤。
</div>


---
layout: default
---

# 2. Collection

| 收集前要想清楚 | 为什么 |
|----------------|--------|
| objective | 你到底要回答什么问题 |
| data requirements | 需要哪些字段和粒度 |
| source / format | 从哪里拿、是什么格式 |
| quality / volume | 数据够不够、质量稳不稳 |
| ethics / privacy | 合规、授权、敏感信息处理 |
| methods / tools | API、database、spreadsheet 还是 web |
| timeframe / budget | 时间和资源能不能支撑 |
| documentation | 后面要复现和解释过程 |


---
layout: default
---

# 真题演练

**Factors to consider during the data collection phase include:**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Collection method efficiency |
| b | Source reliability |
| c | Data format |
| d | Cost of data storage physical locations |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, b, c</code><br>
<strong>讲解：</strong>collection 阶段关注怎么收、来源靠不靠谱、格式能不能用。storage physical locations 更偏 storing，不是这里的重点。
</div>


---
layout: default
---

# 3. Pre-processing

| 常见动作 | 说明 |
|----------|------|
| Subsetting | 只保留相关行或列 |
| Sampling | 数据太大时抽代表性样本 |
| Date / Numeric / Categorical formatting | 统一日期格式; 小数点、千位分隔符统一; `Male/M` 统一 |
| Unit / currency conversion | 公里英里、USD/AUD 等统一 |
| Encoding / timezone | UTF-8、时区对齐 |
| File conversion | XML 转 CSV，JSON 转结构化表 |

<div class="muted mt-4 text-sm">
关键词：subset、sample、format、unit、encoding、conversion
</div>


---
layout: default
---

# 真题演练

**Data standardization helps ensure data is:**

| 选项 | 内容 |
|------|------|
| a | In a consistent format |
| b | Only available in one unit of measurement |
| c | Inconsistent across datasets |
| d | Difficult to analyze |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a</code><br>
<strong>讲解：</strong>standardization 的关键词是 consistent format。题里如果出现 inconsistent、difficult 这类反向措辞，通常直接排除。
</div>


---
layout: default
---

# 4. Cleaning

- 找并修复 `missing values`
- 检查 `outliers`
- 删除或合并 `duplicate records`
- 修正 `consistency issues`
- 识别 data anomalies
- 注意 anomaly 不一定只是错误，也可能是新模式或重要信号

<div class="callout text-sm">
考试里看到 correcting inaccuracies / inconsistencies / duplicates，优先想到 cleaning。
</div>


---
layout: default
---

# 真题演练

**Data cleaning may involve:**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Correcting errors |
| b | Removing duplicates |
| c | Handling missing values |
| d | Introducing new errors |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, b, c</code><br>
<strong>讲解：</strong>cleaning 的典型关键词就是 correcting errors、duplicates、missing values。题里常故意放一个明显错误项来扰乱节奏。
</div>


---
layout: two-cols
---

# 5. Transformation

- 把数据变成更适合分析的结构或表示
- 常见于 numeric / text / image 三类数据
- 目标是让后续分析、建模、比较更稳定

::right::

| Numeric 常见操作 | 作用 |
|------------------|------|
| Normalization | 缩放到固定范围 |
| Standardization | 调到均值 0、方差 1 |
| Aggregation | 求和、均值、分组统计 |
| Discretization | 连续值切成区间 |
| Binning / Bucketing | 分桶后变成类别 |


---
layout: default
---

# 5. Transformation 还包括什么

| 数据类型 | 常见操作 |
|----------|----------|
| Text | tokenization, stemming / lemmatization, vectorization |
| Image | resize, crop, normalization, colour conversion |
| Image augmentation | rotation, flipping, translation, noise / brightness / contrast adjustment |

<div class="muted mt-4 text-sm">
易混点：normalization 和 standardization 不一样；discretization 和 binning 也不要混。
</div>


---
layout: default
---

# 真题讲解

**What process involves scaling data to a small, specified range?**

| 选项 | 内容 |
|------|------|
| a | Diversification |
| b | Normalisation |
| c | Aggregation |
| d | Segmentation |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong>如果题干强调 fixed range，例如 `0-1`，优先想到 normalization；如果强调 mean 0 / variance 1，才是 standardization。
</div>


---
layout: default
---

# 6. Enrichment

| 方式 | 含义 |
|------|------|
| Data integration | 合并不同来源数据 |
| Data augmentation | 给现有记录补更多信息 |
| Attribute enrichment | 新增特征或属性 |
| Temporal enrichment | 补充时间维度 |
| Semantic enrichment | 加 metadata / tag / meaning |

一句话：不是修错，而是让数据“更完整、更有上下文”。


---
layout: default
---

# 真题演练

**The goals of data enrichment include:**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Adding value to the data |
| b | Improving data quality |
| c | Enhancing data analysis capabilities |
| d | Simplifying data formats |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, b, c</code><br>
<strong>讲解：</strong>enrichment 是补上下文、补特征、补时间维度。simplifying formats 更像 pre-processing / transformation，不是 enrichment 核心。
</div>


---
layout: default
---

# 7. Validation

| 检查项 | 典型问题 |
|--------|----------|
| Accuracy | 值是否反映真实世界 |
| Consistency | 同一字段规则是否统一 |
| Completeness | 关键值是否缺失 |
| Logical integrity | 年龄、日期、关系是否讲得通 |
| Range / constraints | 值域是否超界 |
| Format validation | 格式是否符合预期 |
| Uniqueness | 本应唯一的键是否重复 |
| Cross-validation | 能否用别的数据源交叉验证 |


---
layout: default
---

# 真题演练

**In data wrangling, data validation ensures:**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Data meets predefined standards |
| b | Accuracy and reliability of data |
| c | Data inconsistency is promoted |
| d | Data is in a usable format for analysis |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, b, d</code><br>
<strong>讲解：</strong>validation 是 checking，不是 fixing。它检查 standards、accuracy、usability；promoted inconsistency 显然是反项。
</div>


---
layout: default
---

# 8. Storing

| 存储阶段要考虑 | 重点 |
|----------------|------|
| Storage solution | database / warehouse / cloud |
| Schema design | 查询和维护是否方便 |
| Normalization / denormalization | 完整性 vs 读取效率 |
| Format / encoding | 存储格式要一致 |
| Security | 权限、隐私、合规 |
| Indexing / optimization | 检索速度 |
| Backup / recovery | 可恢复性 |
| Metadata / monitoring | 后续治理与维护 |


---
layout: default
---

# 真题演练

**What aspects does Data Cataloging and Metadata Management cover?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Usage metadata |
| b | Data anonymisation |
| c | Metadata collection |
| d | Data lineage documentation |
| e | Catalog creation |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, c, d, e</code><br>
<strong>讲解：</strong>关键词是 metadata、lineage、catalog。anonymisation 更偏 privacy / governance，不是 cataloging 的直接定义。
</div>


---
layout: default
---

# 用一个例子串起来

1. `Discovery`：找医院再入院预测相关数据源
2. `Collection`：确认权限、字段、格式、预算、时间
3. `Pre-processing`：筛时间范围、抽样、统一日期和单位
4. `Cleaning`：处理缺失、重复、异常和不一致
5. `Transformation`：聚合、标准化、把文本转成可分析形式
6. `Enrichment`：补保险、地理、行为或时间信息
7. `Validation`：检查范围、唯一性、逻辑约束
8. `Storing`：把结果存进可复用的数据表或仓库



---
layout: section
---

# 硬知识


---
layout: default
---

# 硬知识概览

- Notebook 只是载体，不是重点
- Python 基础只保留最低门槛
- 主体放在 `pandas for data wrangling`
- 重点练 DataFrame 的查看、筛选、清洗、转换
- 重点练 `loc / iloc / isna / dropna / rename / sort_values`

<div class="callout mt-4 text-sm">
这一部分只高度概括 Python / Markdown，课堂主轴是 <code>pandas</code> 如何服务 data wrangling。
</div>


---
layout: default
---

# 硬知识

## Python / Markdown 只保留最低要求

| 模块 | 最少会什么 |
|------|------------|
| Jupyter Notebook | 分清 code cell 和 markdown cell，能运行 cell |
| Markdown | 会标题、列表、表格，能写过程说明 |
| Python | 会变量、list、dict，能读懂 `for loop` 和 `function` |
| 练习题 | `transpose_matrix` 只当基础控制流组合题 |

```python
for item in [1, 2, 3]:
    print(item)
```

<div class="muted mt-4 text-sm">
要求不是把 Python 单独讲深，而是够用就好，后面立刻进入 pandas。
</div>


---
layout: default
---

# 硬知识：常见 pandas 操作

| 任务 | 常见写法 |
|------|----------|
| 读 CSV | `pd.read_csv(...)` |
| 读 Excel | `pd.read_excel(...)` |
| 读 JSON | `pd.read_json(...)` |
| 改列名 | `df.rename(columns={'A': 'B'})` |
| 设 index | `df.set_index('ID')` |
| 排序 | `df.sort_values(by='Name')` |
| 指定 header | `header=` |
| 跳过前几行 | `skiprows=3` |


---
layout: default
---

# 硬知识练习顺序

| 顺序 | 对应练习 |
|------|----------|
| 1 | Creating DataFrames |
| 2 | Inspecting a DataFrame |
| 3 | Subset Observations (Rows) |
| 4 | Subset Variables (Columns) |
| 5 | Sort, Rename, Drop, Index |
| 6 | Reshaping Data |
| 7 | Summarize Data |

---
layout: default
---

# 硬知识练习顺序

| 顺序 | 对应练习 |
|------|----------|
| 8 | Handling Missing Data |
| 9 | Make New Columns |
| 10 | Group Data |
| 11 | Combine Data Sets |
| 12 | Windows |
| 13 | Plotting |
| 14 | Method Chaining |

---
layout: default
---

# 硬知识

## `pandas` / `DataFrame` 基础认知

| 知识点 | 要点 |
|--------|------|
| 导入方式 | `import pandas as pd` |
| DataFrame | 二维表格数据结构 |
| case sensitive | `DataFrame` 不等于 `dataframe` |
| 创建方式 | list、dict、日期索引都可以建表 |

```python
df = pd.DataFrame(
    {
        'product': ['pen', 'notebook', 'eraser'],
        'price': [2.5, 5.0, 1.2],
        'stock': [100, 50, 200],
    }
)
```

---
layout: default
---

# 硬知识

## 先探索，再清洗

| 函数 | 用来干什么 |
|------|------------|
| `df.info()` | 看列名、非空数、dtype |
| `df.describe()` | 看数值统计摘要 |
| `df.head()` | 看前 5 行 |
| `df.tail()` | 看后 5 行 |
| `df.shape` | 看行列数 |
| `df.columns.tolist()` | 看字段列表 |

<div class="callout mt-4 text-sm">
真实 wrangling 流程里，不是拿到数据就改；先知道结构、字段、缺失情况，再动手。
</div>


---
layout: default
---

# 硬知识

## `loc` 和 `iloc` 的本质区别

| 方法 | 按什么选 |
|------|----------|
| `loc` | label / 列名 / index 名称 |
| `iloc` | integer position / 数字位置 |

```python
ufo.loc[:, 'City':'State'].head()
ufo.iloc[1:6, 2:6]
```

<div class="callout mt-4 text-sm">
考试和 applied session 都很喜欢考这个区别。一个按标签，一个按位置，不要混。
</div>


---
layout: default
---

# 硬知识

## 缺失值检查的最短工作流

```python
ufo.isna().sum()
ufo[ufo.isna().any(axis=1)]
ufo1 = ufo.dropna()
```

| 步骤 | 作用 |
|------|------|
| `isna()` / `isnull()` | 判断缺失 |
| `.sum()` | 统计每列缺失数 |
| `.any(axis=1)` | 找含缺失值的行 |
| `dropna()` | 直接删掉缺失行 |


---
layout: default
---

# 硬知识

## 一个高频坑：空字符串不等于缺失值

`pandas` 里的 `isnull()` / `isna()` 默认只把这些视为缺失：

- `NaN`
- `None`
- `NaT`

下面这种不会自动算缺失：

```python
df = pd.DataFrame({"A": ["", None, "text"]})
```

<div class="callout mt-4 text-sm">
所以 data 看起来“空着”，不代表 pandas 会把它当 missing value。这个坑在 cleaning 题里很常见。
</div>


---
layout: default
---

# 硬知识

## Basic editing 不只是改值

| 操作 | 例子 |
|------|------|
| 新增列 | `df['place'] = ''` |
| 复制 DataFrame | `df2 = df.copy()` |
| 删除列 | `df.drop(columns=['State'])` |
| 合并文本列 | 把 `City` 和 `State` 拼成 `place` |

<div class="callout mt-4 text-sm">
Applied session 还专门比较了 loop 写法和 pandas 写法的效率，隐含结论是：能用表格操作时，尽量别回到逐行手写循环。
</div>


---
layout: default
---

# 真题演练

**Which method is used to get a summary of a DataFrame's structure and column types?**

| 选项 | 内容 |
|------|------|
| a | `df.info()` |
| b | `df.describe()` |
| c | `df.overview()` |
| d | `df.summary()` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a</code><br>
<strong>讲解：</strong><code>df.info()</code> 看结构和 dtype；<code>df.describe()</code> 看数值统计摘要。exam 很喜欢拿这两个放一起混淆。
</div>


---
layout: default
---

# 真题讲解

**How do you select rows 10 to 20 from a DataFrame `df`?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | `df.iloc[9:20]` |
| b | `df.loc[10:20]` |
| c | `df.locate[9:20]` |
| d | `df[9:20]` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, d</code><br>
<strong>讲解：</strong><code>iloc</code> 是位置切片，起点 0-based 且右边不含；<code>loc</code> 是标签切片，通常两端都含。<code>locate</code> 根本不是 pandas API。
</div>


---
layout: default
---

# 真题讲解

**How do you check for missing values in a DataFrame `df`?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | `df.isna()` |
| b | `df.has_null()` |
| c | `df.missing()` |
| d | `df.isnull()` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a, d</code><br>
<strong>讲解：</strong><code>isna()</code> 和 <code>isnull()</code> 在 pandas 里都能用。考试常用假 API 选项混进来。
</div>


---
layout: default
---

# 真题讲解

**To drop rows with any missing values in the data frame `df`, you use:**

| 选项 | 内容 |
|------|------|
| a | `df.fillna()` |
| b | `df.dropna()` |
| c | `df.remove_na()` |
| d | `df.delete_missing()` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>b</code><br>
<strong>讲解：</strong><code>fillna()</code> 是填补，不是删除；只要题干出现 drop rows with missing values，优先锁定 <code>dropna()</code>。
</div>



---
layout: section
---

# 学习建议



---
layout: default
---

# 总 Checklist

1. 能用自己的话定义 data wrangling
2. 能说出它的目标和主要挑战
3. 能按顺序写出 8 个步骤
4. 能给每一步举一个例子
5. 能分清 discovery / collection / pre-processing / cleaning / transformation / enrichment / validation / storing
6. 知道 subsetting、sampling、normalization、standardization、discretization、binning 的区别
7. 能在 Jupyter Notebook 里完成基础代码与 markdown 操作
8. 能用 pandas 读入 CSV 并查看数据结构
9. 会做基础缺失值处理



---
layout: default
---

# 接下来怎么学

| 时间 | 建议 |
|------|------|
| 本周 | 把 Python / Jupyter 基础补齐 |
| Week 2-4 | 跟上 wrangling 流程、regex、EDA |
| Week 5-6 | 开始为 Quiz 1 和 A1 做准备 |
| Week 7 后 | 重点转向 parsing / cleansing / integrating |




---
layout: end
---

# 下阶段

Week 3 会开始更具体地碰到 regex / text handling；
