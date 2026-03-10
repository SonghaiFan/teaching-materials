# FIT5196 Week 1-2 补习班课程总结

本总结根据以下材料整理：

- `week1/intro_slides 2.pdf`
- `week1/week_1_applied_session_material.ipynb`
- `week1/mock-quiz.md`
- `week2/intro_slides.md`
- `week2/case_study_slides.md`
- `week2/week_2_applied_session.ipynb`

目标：帮助补习班同学快速回顾 Week 1 和 Week 2 的核心概念、课堂实操、quiz 易错点和复习重点。

## 1. 这两周到底在学什么

FIT5196 前两周的重点不是直接做复杂建模，而是先建立对 `Data Wrangling` 的整体理解：

- 知道什么是 data wrangling
- 知道为什么数据分析前必须先做 wrangling
- 能说清楚 wrangling 的八个步骤
- 能区分每一步分别在解决什么问题
- 能在 Jupyter Notebook 里完成最基本的 Python 与 pandas 操作

一句话概括：

> Data Wrangling 是把原始数据变成可分析数据的过程。

它通常包括：

- acquiring / discovery
- collection
- pre-processing
- cleaning
- transformation
- enrichment
- validation
- storing

## 2. Week 1 核心内容总结

### 2.1 什么是 Data Wrangling

Data Wrangling 是将原始数据转换为可以直接分析的数据。

可以把它理解为：

`Raw Data -> Clean / Tidy Data -> Actionable Insights`

Week 1 最重要的是先记住这个定义，不要把它误解成：

- 只是数据可视化
- 只是收集数据
- 只是机器学习建模

### 2.2 Data Wrangling 的主要目标

根据 slides，data wrangling 的目标包括：

- 提高数据质量
- 简化数据访问
- 促进数据整合
- 降低数据复杂度
- 提高分析效率
- 支持决策制定

常见反向陷阱：

- 不是增加数据复杂度
- 不是忽略不一致问题
- 不是制造冗余

### 2.3 为什么必须做 Data Wrangling

如果不先做 wrangling，分析结果可能错误、偏差很大，甚至无法分析。

原始数据常见问题有：

- 缺失值
- 错误值
- 重复记录
- 格式不一致
- 结构复杂

典型数据来源也很多样：

- CSV / Excel
- JSON / XML / HTML
- social media data
- Wikipedia structured data
- 医疗影像和报告

所以 Week 1 的重点是建立一个正确认识：

> 现实世界的数据默认不是干净整齐的。

### 2.4 Data Wrangling 的主要挑战

Slides 里把挑战归纳为几类：

- `Volume and scalability`
  - 数据量大，传统工具难以处理
- `Data quality`
  - 缺失、错误、异常、重复
- `Diverse sources`
  - CSV、XML、JSON、图片、数据库等来源很多
- `Lack of standardization`
  - 日期、货币、地址、命名规则不统一
- `Time-consuming`
  - 数据科学工作里很大比例时间花在清洗整理
- `Skills and tools`
  - 需要 Python、统计、数据库、NLP 等能力
- `Privacy and security`
  - 敏感数据必须考虑合规和隐私

### 2.5 Week 1 工具与环境

Week 1 还强调了这门课默认工具链：

- Python 3
- Jupyter Notebook
- Google Colab
- Anaconda
- VS Code / PyCharm

常见 Python 库：

- `pandas`
- `numpy`
- `scipy`
- `scikit-learn`
- `BeautifulSoup`
- `NLTK`

## 3. Week 1 Applied Session 重点

Week 1 的 applied session 更偏基础工具入门，重点不是复杂数据处理，而是让你能开始写 notebook。

### 3.1 Jupyter Notebook 必须会什么

你需要理解：

- notebook 由 `cell` 组成
- `code cell` 用来运行 Python 代码
- `markdown cell` 用来写解释、标题、列表和报告文字
- notebook 是代码、文字说明、输出结果放在一起的工作方式

这门课后续 group assessment 需要用 notebook 展示解决过程，所以不是只会写代码就够了，还要会把过程写清楚。

### 3.2 Week 1 Python 基础

Week 1 applied session 重点练了：

- 变量
- list
- dict
- `for loop`
- nested `for loop`
- function

课程还安排了一个很典型的练习：

- 写 `transpose_matrix(matrix)` 函数

这个练习的目的不是考复杂算法，而是确保你能：

- 理解 list of lists
- 使用 nested loops
- 自己定义函数
- 正确返回结果

### 3.3 Week 1 结束前你至少要达到

- 能打开并运行 notebook
- 能切换 markdown / code cell
- 能运行基础 Python 代码
- 能写简单函数
- 能看懂并手写简单循环逻辑

如果这部分不熟，后面 pandas 和 wrangling 流程会跟得很痛苦。

## 4. Week 2 核心内容总结

Week 2 重点是把 Week 1 的总体认识，展开成完整流程和具体任务。

## 5. Data Wrangling 八大任务流程

### 5.1 Data Discovery

目标：找出可用数据源。

评估维度：

- Accessibility
- Relevance
- Quality
- Cost

典型例子：

- 找 hospital EHR 数据
- 找医保理赔数据
- 找 wearable device data
- 找健康史和药物记录

记忆点：

> Discovery 是 “找什么数据可以用”，不是开始清洗。

### 5.2 Data Collection

目标：真正去收集数据，并决定如何收集。

要考虑：

- Objectives
- Format
- Volume
- Privacy
- Budget
- Timeline

在 case study 里，这一步尤其强调：

- 是否合法合规
- 是否包含关键字段
- 字段命名是否统一

记忆点：

> Discovery 是找来源，Collection 是真正收集并规划收集过程。

### 5.3 Data Pre-processing

这一步是让数据先变得更适合后续分析。

常见任务：

- subsetting
- sampling
- formatting
- unit conversion
- text normalization

最容易混淆的是：

- `Subsetting`
  - 只选一部分相关数据
- `Sampling`
  - 从大数据中抽一部分样本

例如：

- 只保留 2000-2010 年记录是 `subsetting`
- 从 billions of rows 里抽部分样本是 `sampling`

### 5.4 Data Cleaning

这是 Week 2 quiz 最常考的步骤之一。

主要任务：

- 处理 missing values
- 识别 outliers
- 去重
- 修正格式不一致
- 纠正错误值

case study 和 applied session 都反复出现这一类操作，例如：

- 删除重复记录
- 统一 `YES` 和 `yes`
- 处理空值
- 检查类别标签不一致

记忆点：

> remove duplicates / handle missing values / correct inconsistencies 基本都属于 cleaning。

### 5.5 Data Transformation

Transformation 是把数据变成另一种更适合分析的形式。

数值转换常见类型：

- normalization
- standardization
- aggregation
- discretization
- binning

文本转换常见类型：

- tokenization
- stemming
- vectorization

图像转换常见类型：

- resizing
- color space conversion
- rotation / flipping

常见区分：

- `Aggregation`
  - 汇总，例如总月消费
- `Discretization`
  - 连续变量转区间类别
- `Binning`
  - 把数值分桶
- `Standardization`
  - 均值 0、标准差 1
- `Normalization`
  - 缩放到统一范围

### 5.6 Data Enrichment

Enrichment 是让数据更完整、更有上下文。

常见方法：

- 合并多个数据集
- 增加衍生特征
- 补充时间维度
- 补充语义或外部知识

case study 里的例子包括：

- 药品名称补充药物分类信息
- postcode 补充 suburb / region / income / population density
- patient data 补 wearable sensor readings

记忆点：

> enrichment 的方向是增加信息，不是减少 insights。

### 5.7 Data Validation

Validation 是在清洗和转换后检查数据是否仍然正确、合理、可用。

常见检查：

- accuracy
- consistency
- logical completeness
- range constraints
- format standards
- uniqueness checks

case study 里的典型验证：

- `Age` 是否在合理范围
- `patient_id` 是否唯一
- 关键字段是否缺失
- `Discharge_Date` 是否早于 `Readmit_Date`

记忆点：

> validation 的核心是 “检查规则是否满足”，不是做新转换。

### 5.8 Data Storing

最后一步是把数据保存到合适系统中。

重点考虑：

- schema design
- security
- indexing
- backup
- lifecycle management

这一部分常考的判断包括：

- 设计 schema 属于 storing
- backups / recovery planning 属于 storing
- warehouse / database selection 属于 storing
- relational database 减少冗余通常对应 normalization

## 6. Week 2 Case Study 总结

Week 2 的案例研究以医疗数据为背景，目标是预测病人出院后 30 天内是否再入院。

这个案例的价值在于它把八个步骤从抽象概念变成了真实场景。

### 6.1 从案例中学到的核心方法

- Discovery 阶段要先枚举可用数据源
- Collection 阶段要看关键字段、隐私和一致性
- Pre-processing 阶段先统一日期格式、标签格式、编码方式
- Cleaning 阶段处理重复、异常、缺失、不一致
- Transformation 阶段把原始特征转成模型友好的形式
- Enrichment 阶段引入外部知识或补充信息
- Validation 阶段检查范围、逻辑顺序和唯一性
- Storing 阶段考虑如何让后续查询和分析稳定进行

### 6.2 这个案例最值得学生学会的不是答案，而是判断方式

看到一个操作时，先问：

1. 这是在找数据源吗？
2. 这是在真正收集数据吗？
3. 这是在预处理格式吗？
4. 这是在清洗问题吗？
5. 这是在转换数据结构吗？
6. 这是在补信息吗？
7. 这是在做规则检查吗？
8. 这是在为保存和后续使用设计吗？

如果能这么判断，Week 2 quiz 就会容易很多。

## 7. Week 2 Applied Session 重点

Week 2 applied session 从概念过渡到 pandas 实操。

### 7.1 pandas 基础

最基本操作包括：

- `import pandas as pd`
- `pd.DataFrame()`
- 创建 DataFrame 并赋值给变量
- 查看 index、columns、values

还强调了 Python / pandas 的基本习惯：

- 大小写敏感
- index 从 0 开始
- 需要把结果存到变量里，后面才能复用

### 7.2 探索 DataFrame

Week 2 实操中重点练了这些命令：

- `df.shape`
- `df.columns`
- `df.dtypes`
- `df.values`
- `df.describe()`
- `df.head()`
- `df.tail()`
- `df.info()`

这些命令的核心作用是：

- 先理解数据长什么样
- 再决定后面怎么清洗和处理

### 7.3 读取数据

Week 2 实操还涉及到常见读取方式，例如：

- `pd.read_csv(...)`
- 带 `skiprows` 读取数据

例如 `xmart.csv` 的练习：

- 看多少条记录
- 看多少个属性
- 看每个属性的数据类型
- 在没有说明文档时，尝试用 `info()` 和 `columns` 自己总结数据内容

这实际上就是一个小型的 profiling / assessment 训练。

### 7.4 编辑和清洗 DataFrame

Week 2 实操中非常重要的一部分是对缺失值和列进行处理，例如：

- `isna()`
- `isna().sum()`
- `dropna()`
- `fillna(...)`
- `copy()`
- 新建列
- 合并列内容

重要理解：

- 不是所有缺失值都适合直接删掉
- 填充值也要看字段语义，不能机械填 0
- 处理前最好先复制数据，保留原始版本

这部分和 quiz 高度相关，因为 quiz 常常就是考你能否判断：

- 什么属于 cleaning
- 什么属于 transformation
- 什么属于 validation

## 8. Week 1-2 常见 quiz 易错点

### 8.1 这些概念最容易混

- `Data Discovery` vs `Data Collection`
- `Subsetting` vs `Sampling`
- `Cleaning` vs `Transformation`
- `Cleaning` vs `Validation`
- `Enrichment` vs `Storing`
- `Normalization` vs `Standardization`
- `Discretization` vs `Binning`
- `Formatting` vs `Encoding`

### 8.2 记忆规则

- 发现来源：`Discovery`
- 真正获取和规划：`Collection`
- 先整理格式和范围：`Pre-processing`
- 修复脏数据：`Cleaning`
- 改成新形式：`Transformation`
- 补充外部信息：`Enrichment`
- 检查规则与合理性：`Validation`
- 保存与后续管理：`Storing`

### 8.3 题目里看到这些词时的快速判断

- `identify sources` -> discovery
- `budget / privacy / timeline / objectives` -> collection
- `subset / sample / format / unit conversion` -> pre-processing
- `duplicates / missing / outliers / inconsistencies` -> cleaning
- `normalize / standardize / aggregate / discretize` -> transformation
- `merge external data / add context` -> enrichment
- `range / uniqueness / logical rules / allowed values` -> validation
- `schema / backups / indexing / warehouse` -> storing

## 9. 补习班建议怎么复习

### 第一轮：先背流程

把八步按顺序写出来：

1. discovery
2. collection
3. pre-processing
4. cleaning
5. transformation
6. enrichment
7. validation
8. storing

### 第二轮：每一步配一个例子

例如：

- discovery -> 找医院 EHR 数据
- collection -> 确认字段和隐私要求
- pre-processing -> 统一日期格式
- cleaning -> 删除重复、处理缺失
- transformation -> 年龄标准化
- enrichment -> 加 postcode 对应区域信息
- validation -> 检查年龄范围和 ID 唯一性
- storing -> 设计 schema 和备份

### 第三轮：补命令

至少要熟悉这些 pandas / notebook 基础：

- `import pandas as pd`
- `pd.read_csv()`
- `df.shape`
- `df.columns`
- `df.dtypes`
- `df.info()`
- `df.head()`
- `df.describe()`
- `df.isna()`
- `df.dropna()`
- `df.fillna()`

### 第四轮：练判断题

不要只背定义，要训练看到一句话就能判断属于哪个步骤。

例如：

- “只选择 2000-2010 的记录” -> subsetting
- “把 XML 转成 CSV” -> transformation
- “检查 gender 只能是 M/F” -> validation
- “删除重复记录” -> cleaning
- “加入 wearable device data” -> enrichment

## 10. 一页最终复习清单

考前至少确认自己能做到：

- 能用自己的话解释什么是 data wrangling
- 能说出 data wrangling 的目标
- 能说出主要挑战
- 能按顺序写出八大任务
- 能区分 discovery / collection / pre-processing / cleaning / transformation / enrichment / validation / storing
- 能解释 subsetting、sampling、normalization、standardization、discretization、binning
- 能理解 cleaning、validation、enrichment 的区别
- 能在 Jupyter Notebook 里完成基本代码与 markdown 操作
- 能用 pandas 读取 CSV 并查看数据结构
- 能处理最基本的缺失值问题

## 11. 最后一句话

Week 1 和 Week 2 的核心不是记很多零散术语，而是建立一个稳定的分析框架：

> 看到任何数据处理任务时，先判断它处在 wrangling pipeline 的哪一步，再决定该用什么方法和工具。

只要这套框架建立起来，后面 regex、EDA、data quality、integration、validation 等内容都会更容易接上。
