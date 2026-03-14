---
theme: apple-basic
title: FIT5196 Quiz 1 全题真题解析
layout: intro
transition: slide-left
mdc: true
---

# FIT5196 Quiz 1

## 全题真题解析 Deck

补习班课堂版

按 Mock Quiz 的 Week 1-6 范围重组。

---
layout: default
---

# 这份 deck 怎么用

- 每题先自己做判断，不要急着按答案。
- 第一次点击：看参考答案。
- 第二次点击：看解析。
- 同题重复版本已经合并，页眉会保留原题号来源。

---
layout: default
---

# Deck 结构

| Week | 题量 | 范围 |
|------|------|------|
| Week 1 | 4 | Jupyter Notebook、Markdown、Python basics |
| Week 2 | 37 | Data Wrangling Process & Tasks + Week 2 pandas applied session |
| Week 3 | 34 | Regular Expressions |
| Week 4 | 32 | EDA & Pre-processing + Week 4 parsing + text pre-processing |
| Week 5 | 18 | Data Discovery & Collection |
| Week 6 | 5 | Data Structuring |

---
layout: section
---

# Week 1

Jupyter Notebook、Markdown、Python basics

---
layout: statement
---

Markdown 格式题不难，但很容易因为粗体 / 斜体 / 列表符号混淆而丢分。

---
layout: default
---

# Q1

How do you make text italic in Markdown? (Select all that apply)

- a. Surround the text with **
- b. Surround the text with ~~
- c. Surround the text with _
- d. Surround the text with *
<v-click>

**参考答案**

`c, d`

</v-click>

<v-click>

**解析**

斜体在 Markdown 里通常写成 `*text*` 或 `_text_`，不是 `**`（粗体）也不是 `~~`（删除线）。

</v-click>

---
layout: default
---

# Q6

To create a bullet list in Markdown, which symbol can you use?

- a. All of the above
- b. *
- c. -
- d. +
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

正确项是 `a`: All of the above。它最符合这道题在课程里的定义。

</v-click>

---
layout: default
---

# Q20 / Q116 / Q155

To emphasise text with bold in Markdown, you can use:

- a. Double tildes or double dollar signs
- b. Double asterisks or double underscores
- c. Single asterisks or single underscores
- d. Triple asterisks or triple underscores
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

Markdown 粗体用双星号或双下划线，即 `**text**` 或 `__text__`。

</v-click>
---
layout: default
---

# Q26

For numbered lists in Markdown, what character follows the number? (Select all that apply)

- a. )
- b. *
- c. .
- d. -
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

课程默认的 Markdown 有序列表写法是 `1.`，所以答案按 `.` 记。

</v-click>

---
layout: section
---

# Week 2

Data Wrangling Process & Tasks + Week 2 pandas applied session

---
layout: statement
---

Week 2 是 Quiz 1 的骨架，很多题其实都在反复考定义、目标、流程边界和基础 pandas 操作。

---
layout: default
---

# Q8

How do you select rows 10 to 20 from a DataFrame df? (Select all that apply)

- a. `df.iloc[9:20]`
- b. `df.loc[10:20]`
- c. `df.locate[9:20]`
- d. `df[9:20]`
<v-click>

**参考答案**

`a, d`

</v-click>

<v-click>

**解析**

`iloc[9:20]` 取的是第 10 到第 20 行（位置索引，右端不含）；`df[9:20]` 也会按切片取对应行。`loc[10:20]` 依赖标签索引，课内通常不作为标准答案。

</v-click>

---
layout: default
---

# Q9

Which of the following are considered tasks in the Data Wrangling process? (Select all that apply)

- a. Data Modification
- b. Data Storing
- c. Data Validation
- d. Data Presentation
- e. Data Cleaning
<v-click>

**参考答案**

`b, c, e`

</v-click>

<v-click>

**解析**

正确项是 `b`: Data Storing, `c`: Data Validation, `e`: Data Cleaning。这些选项共同对应课程里的正确定义。

</v-click>

---
layout: default
---

# Q12

Data simplification can involve: (Select all that apply)

- a. Enhancing understandability of data
- b. Removing relevant information
- c. Filtering out irrelevant information
- d. Summarizing complex data
<v-click>

**参考答案**

`a, c, d`

</v-click>

<v-click>

**解析**

正确项是 `a`: Enhancing understandability of data, `c`: Filtering out irrelevant information, `d`: Summarizing complex data。这些选项共同对应课程里的正确定义。

</v-click>

---
layout: default
---

# Q14

The goals of data enrichment include: (Select all that apply)

- a. Adding value to the data
- b. Improving data quality
- c. Enhancing data analysis capabilities
- d. Simplifying data formats
<v-click>

**参考答案**

`a, b, c`

</v-click>

<v-click>

**解析**

data enrichment 的目标是加上下文、提升价值、改善可分析性；“simplifying data formats” 更像 pre-processing / transformation。

</v-click>

---
layout: default
---

# Q17 / Q70 / Q114

Data cleaning may involve: (Select all that apply)

- a. Introducing new errors
- b. Removing duplicates
- c. Handling missing values
- d. Correcting errors
<v-click>

**参考答案**

`b, c, d`

</v-click>

<v-click>

**解析**

正确项是 `b`: Removing duplicates, `c`: Handling missing values, `d`: Correcting errors。这些选项共同对应课程里的正确定义。

</v-click>

---
layout: default
---

# Q22 / Q53

How can you rename the column 'A' to 'B' in a DataFrame df?

- a. df.columns['A'] = 'B'
- b. df.columns.rename('A', 'B')
- c. df.rename('A', 'B')
- d. df.rename(columns={'A': 'B'})
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

Pandas 改列名标准写法是 `df.rename(columns={"A": "B"})`。

</v-click>

---
layout: default
---

# Q33

How do you check for missing values in a DataFrame df? (Select all that apply)

- a. `df.isna()`
- b. `df.has_null()`
- c. `df.missing()`
- d. `df.isnull()`
<v-click>

**参考答案**

`a, d`

</v-click>

<v-click>

**解析**

Pandas 检查缺失值常用 `isna()` 和 `isnull()`。

</v-click>

---
layout: default
---

# Q34

Scalability in data wrangling is essential for:

- a. Handling increased data loads without performance loss
- b. Reducing data processing power
- c. Maintaining a constant volume of data
- d. Complicating data integration processes
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

scalability 指数据量上来后仍能处理，不是把数据量固定不变。

</v-click>

---
layout: default
---

# Q36

Data standardization helps ensure data is:

- a. In a consistent format
- b. Only available in one unit of measurement
- c. Inconsistent across datasets
- d. Difficult to analyze
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

这里的 standardization 更偏“统一标准/格式”，目标是让数据表示保持一致。

</v-click>

---
layout: default
---

# Q39 / Q160

What process involves scaling data to a small, specified range?

- a. Diversification
- b. Normalisation
- c. Aggregation
- d. Segmentation
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

把数值缩到一个小范围（如 `[0,1]`）是 normalisation。

</v-click>
---
layout: default
---

# Q41

In data quality management, what is crucial for maintaining high-quality data?

- a. Aesthetic appeal
- b. Data volume
- c. Data Governance
- d. Data variety
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

持续高质量数据离不开 data governance，因为要靠规则、责任和流程来维护。

</v-click>

---
layout: default
---

# Q43

Data enrichment may involve:

- a. Verifying data accuracy
- b. Adding time-related data
- c. Correcting data errors
- d. Converting data into a binary format
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

enrichment 常见做法是补充时间、地理、人口等额外上下文。

</v-click>

---
layout: default
---

# Q45 / Q94

Machine Learning enhances data quality management through:

- a. Solely focusing on data visualization
- b. A combination of techniques including NLP and continuous monitoring
- c. Only data cleansing
- d. Only automated error detection
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

机器学习在 data quality management 里常用于自动识别问题、持续监控和 NLP 等组合方法。

</v-click>
---
layout: default
---

# Q46

Data Integration aims to:

- a. Reduce the overall data quality
- b. Create inconsistent datasets
- c. Combine multiple data sources for a unified view
- d. Provide a disjointed view of information
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

data integration 的目标是把多个来源统一成一个一致视图。

</v-click>

---
layout: default
---

# Q47 / Q125 / Q143

Which type of data anomalies refers to a single data point deviating significantly from the rest?

- a. Complex Anomalies
- b. Contextual Anomalies
- c. Collective Anomalies
- d. Point Anomalies
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

单个点明显偏离整体，就是 point anomaly。

</v-click>
---
layout: default
---

# Q48 / Q92

Which of the following is NOT a goal of data validation?

- a. Verify data is in the expected format
- b. Validate range and constraints
- c. Ensure data accurately reflects real-world entities
- d. Enhance the speed of data retrieval
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

validation 是检查格式、范围、逻辑是否合理，不是提升读取速度。

</v-click>
---
layout: default
---

# Q52 / Q108

In data wrangling, data validation ensures: (Select all that apply)

- a. Data inconsistency is promoted
- b. Data meets predefined standards
- c. Data is in a usable format for analysis
- d. Accuracy and reliability of data
<v-click>

**参考答案**

`b, c, d`

</v-click>

<v-click>

**解析**

validation 要保证数据符合预设标准、可靠且可用于后续分析。

</v-click>
---
layout: default
---

# Q59 / Q104

Which of the following are common goals of data wrangling? (Select all that apply)

- a. Increasing data complexity
- b. Ignoring data inconsistencies
- c. Improving data quality
- d. Facilitating easier access to data
<v-click>

**参考答案**

`c, d`

</v-click>

<v-click>

**解析**

wrangling 的常见目标是提高质量、提升可访问性，不是增加复杂度。

</v-click>
---
layout: default
---

# Q67

What role does machine learning play in data quality management?

- a. Enhancing processes of identifying and correcting data quality issues
- b. Reducing the need for data governance
- c. Only for data visualization
- d. Only for database management
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

机器学习的作用是帮助发现、识别并修正数据质量问题。

</v-click>

---
layout: default
---

# Q78 / Q152

Which method would you use to sort a DataFrame df by the column 'Name'?

- a. `df.rank('Name')`
- b. `df.sort_values(by='Name')`
- c. `df.sort_by('Name')`
- d. `df.sort('Name')`
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

按列排序标准写法是 `df.sort_values(by="Name")`。

</v-click>
---
layout: default
---

# Q79

Which is NOT a feature of Big Data?

- a. Manageable by traditional software
- b. Voluminous
- c. Includes various data structures
- d. Involves high velocity
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

Big Data 的典型特征是 volume、variety、velocity，通常不能被传统软件轻松处理。

</v-click>

---
layout: default
---

# Q80

What does simplifying access to data aim to achieve?

- a. Increase the complexity of data access
- b. Organise data in a user-friendly manner
- c. Make data accessible only to data scientists
- d. Restrict data access
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

simplifying access 的目标是让数据更容易找、更容易用。

</v-click>

---
layout: default
---

# Q82

What is the primary purpose of Data Wrangling?

- a. To analyze complex data types
- b. To ensure data privacy
- c. To acquire, clean, structure, and enrich raw data for analysis
- d. To visualize data trends
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

data wrangling 的核心就是把原始数据整理成可分析数据。

</v-click>

---
layout: default
---

# Q83

What does data enrichment not involve?

- a. Creating new variables
- b. Reducing data insights
- c. Adding external context
- d. Enhancing data with additional information
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

enrichment 是增加信息与洞察，不是减少 insights。

</v-click>

---
layout: default
---

# Q86

The process of identifying and correcting inconsistencies in data is called:

- a. Data collection
- b. Data integration
- c. Data cleaning
- d. Data enrichment
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

识别并修正不一致，属于 data cleaning。

</v-click>

---
layout: default
---

# Q87

Facilitating data integration helps with:

- a. Ignoring data quality
- b. Keeping data in isolated systems
- c. Transforming disparate data into a common format
- d. Making it harder to combine data from different sources
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

integration 的一个关键作用就是把异构数据转成共同格式。

</v-click>

---
layout: default
---

# Q93

A major challenge in data wrangling is:

- a. Avoiding data standardization
- b. Maintaining low data quality
- c. Data privacy and security
- d. Handling small volumes of data
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

data privacy and security 是 data wrangling 的典型难点之一。

</v-click>

---
layout: default
---

# Q101

Data Integration and Consolidation require: (Select all that apply)

- a. Combining data sources
- b. Harmonise data formats
- c. Data anonymisation
- d. Data cleaning
- e. Ensuring consistency
<v-click>

**参考答案**

`a, b, d, e`

</v-click>

<v-click>

**解析**

integration / consolidation 要合并来源、统一格式、清洗并保证一致性。

</v-click>

---
layout: default
---

# Q103

How do you select a single column named 'Age' from a DataFrame df? (Select al that apply)

- a. `df['Age']`
- b. `df.select('Age')`
- c. `df.index('Age')`
- d. `df.Age`
<v-click>

**参考答案**

`a, d`

</v-click>

<v-click>

**解析**

单列可用 `df["Age"]` 或属性访问 `df.Age`。

</v-click>

---
layout: default
---

# Q109

To drop rows with any missing values in the data frame `df`, you use:

- a. `df.fillna()`
- b. `df.dropna()`
- c. `df.remove_na()`
- d. `df.delete_missing()`
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

删除含缺失值的行用 `df.dropna()`。

</v-click>

---
layout: default
---

# Q118

Which function is used to concatenate two DataFrames vertically?

- a. `pd.concat()`
- b. `pd.join()`
- c. `pd.merge()`
- d. `pd.append()`
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

纵向拼接两个 DataFrame 通常用 `pd.concat()`。

</v-click>

---
layout: default
---

# Q119

Effective data validation checks are: (Select all that apply)

- a. Completeness checking
- b. Range checking
- c. Encryption methods
- d. Consistency checking
<v-click>

**参考答案**

`a, b, d`

</v-click>

<v-click>

**解析**

有效 validation check 常见有 completeness、range、consistency；encryption 不是 validation check。

</v-click>

---
layout: default
---

# Q121

Data integration challenges include:

- a. Combining data of varying formats and quality
- b. Maintaining data in disparate formats
- c. Simplifying the combination of similar data
- d. Ignoring data from different sources
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

integration 真正难在格式和质量不一致，不是“忽略不同来源”。

</v-click>

---
layout: default
---

# Q126

Data duplication is an example of:

- a. Regular expression pattern
- b. Data quality issue
- c. Data wrangling task
- d. Data anomaly
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

重复数据首先是 data quality issue；虽然也常被看作 anomaly，但复习时先按课程答案记。

</v-click>

---
layout: default
---

# Q129

Which is not a challenge in data wrangling?

- a. Handling large volumes of data
- b. Ensuring data privacy and security
- c. Maintaining outdated data formats
- d. Decreasing analytical efficiency
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

前三项都是挑战；“decreasing analytical efficiency” 不是挑战表述，而是负面结果说法。

</v-click>

---
layout: default
---

# Q130

Which is NOT a challenge in maintaining data quality?

- a. Complexity of data integration
- b. Volume and variety of data
- c. Data silos
- d. High-quality data tools
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

真正的挑战是集成复杂、量大、数据孤岛；高质量工具本身不是挑战。

</v-click>

---
layout: default
---

# Q138

The purpose of data aggregation is to:

- a. Increase data detail
- b. Disperse data across sources
- c. Summarise data for analysis
- d. Complicate data analysis
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

aggregation 的目的就是把明细汇总成更适合分析的结果。

</v-click>

---
layout: section
---

# Week 3

Regular Expressions

---
layout: statement
---

正则题最稳的做法不是猜，而是逐段拆：锚点、字符类、量词、前后顾。

---
layout: default
---

# Q3

For matching IPv4 addresses, which regex is accurate and avoids matching numbers beyond the valid range of 0-255?

- a. \b(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\b
- b. [0-9]{1,3}\.([0-9]{1,3}){3}
- c. \b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b
- d. \b(\d{1,3}\.){3}\d{1,3}\b
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

只有 `c` 把每一段都限制在 `0-255` 范围内；`b` 和 `d` 只限制位数，不限制数值大小。

</v-click>

---
layout: default
---

# Q7

What does a regular expression describe?

- a. Text pattern
- b. Image pattern
- c. Numeric calculation
- d. Audio frequency
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

正确项是 `a`: Text pattern。它最符合这道题在课程里的定义。

</v-click>

---
layout: default
---

# Q11

In the regex (?:foo)(foo), what is the difference between (?:foo) and (foo)?

- a. (?:foo) matches and captures "foo"; (foo) only matches "foo"
- b. Neither captures "foo"; they only match
- c. (?:foo) only matches "foo"; (foo) matches and captures "foo"
- d. Both capture "foo" for future use
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`(?:foo)` 是非捕获组，只分组不保存；`(foo)` 是捕获组，会把匹配结果保存下来供后续引用。

</v-click>

---
layout: default
---

# Q13 / Q58

What does the regex `(?&lt;=\b20)\d{2}\b` match in "Class of 2024"?

- a. 2024
- b. Class of
- c. 24
- d. 20
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

lookbehind `(?&lt;=\b20)` 要求前面紧跟 `20`，因此真正被匹配的是后面的两位数字 `24`。

</v-click>
---
layout: default
---

# Q15 / Q148

Which of the following is NOT a character set used in regular expressions?

- a. [a-zA-Z]
- b. \d
- c. [0-9]
- d. (a-z)
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

正确项是 `d`: (a-z)。它最符合这道题在课程里的定义。

</v-click>
---
layout: default
---

# Q18

How would you match "http" at the beginning of a string?

- a. \bhttp
- b. http$
- c. http\b
- d. ^http
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

`^` 匹配字符串开头，所以要写 `^http`。

</v-click>

---
layout: default
---

# Q19

What will the regex (?&lt;=\b20)[0-9]{2}\b match in "Graduating in 2025"?

- a. 2025
- b. 25
- c. 20
- d. No match
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

和 Q13 同理，`(?&lt;=\b20)` 只把 `20` 后面的两位数取出来，所以是 `25`。

</v-click>

---
layout: default
---

# Q21 / Q115

Which character escapes special characters in regular expressions?

- a. ^
- b. $
- c. |
- d. \
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

正确项是 `d`: \。它最符合这道题在课程里的定义。

</v-click>
---
layout: default
---

# Q29

Which of the following is a valid way to match either 'color' or 'colour'?

- a. colo(u|r)
- b. colou|r
- c. colou?r
- d. (color|colour)
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`colou?r` 中 `u?` 表示 `u` 可有可无，因此能同时匹配 `color` 和 `colour`。`(color|colour)` 也能匹配，但课里通常把 `c` 当标准答案。

</v-click>

---
layout: default
---

# Q30 / Q106

Given the string 'hello123', what does the regex (?&lt;=\D)(?=\d) locate?

- a. The position between 'o' and '1'
- b. The sequence "123"
- c. The digit "1"
- d. The letter 'o'
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

这个零宽断言定位的是“非数字后面紧跟数字”的那个位置，也就是 `o` 和 `1` 中间。

</v-click>
---
layout: default
---

# Q54 / Q147

Which regex finds all instances of "not" that are not immediately followed by "good"?

- a. not(?! good)
- b. not(?= good)
- c. not(?=good)
- d. not(?!good)
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

负向前瞻 `(?!good)` 表示后面不能立刻跟 `good`，所以选 `not(?!good)`。

</v-click>
---
layout: default
---

# Q56

What does the regex `^[\w.+-]+@([\w-]+\.)+[a-zA-Z]{2,7}$` not allow in the email username part?

- a. Spaces
- b. Underscore
- c. Plus signs
- d. Digits
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

用户名部分的字符类里不包含空格，所以空格不允许。

</v-click>

---
layout: default
---

# Q61

Which metacharacter matches the beginning of a line?

- a. ^
- b. |
- c. \b
- d. $
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

行首锚点是 `^`。

</v-click>

---
layout: default
---

# Q62

How would you match "cat" or "bat"?

- a. [cb]at
- b. cat||bat
- c. (cb)at
- d. [c&amp;b]at
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

`[cb]at` 表示首字母可以是 `c` 或 `b`。

</v-click>

---
layout: default
---

# Q64

In regex, what does (?:abc) represent?

- a. An optional character sequence
- b. A non-capturing group
- c. A capturing group
- d. A repeated sequence
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

`(?:abc)` 是 non-capturing group。

</v-click>

---
layout: default
---

# Q69

What does the + quantifier do?

- a. Matches exactly one occurrence
- b. Matches zero or more occurrences
- c. Matches zero or one occurrence
- d. Matches one or more occurrences
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

`+` 表示前一项出现 1 次或多次。

</v-click>

---
layout: default
---

# Q73

What does the {3,6} quantifier mean?

- a. Matches at least 3 occurrences of the preceding element
- b. Matches up to 6 occurrences of the preceding element
- c. Matches between 3 and 6 occurrences of the preceding element
- d. Matches exactly 3 or exactly 6 occurrences of the preceding element
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`{3,6}` 就是前一项出现 3 到 6 次。

</v-click>

---
layout: default
---

# Q74

In regular expressions, what does \A match?

- a. The beginning of a string
- b. A word boundary
- c. The end of a string
- d. A non-word boundary
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

`\A` 匹配整个字符串开头。

</v-click>

---
layout: default
---

# Q76

What does the regex `^(?!.*\bfoo\b).*$` ensure about the matched strings?

- a. They must not contain "foo"
- b. They must contain "foo"
- c. They start with "foo"
- d. They end with "foo"
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

整条表达式用负向前瞻排除了包含独立单词 `foo` 的字符串。

</v-click>

---
layout: default
---

# Q95

Which regex matches a string if it starts with "http://" and does not have "www" immediately after?

- a. ^http(?!://www\.)
- b. ^http:\/\/(?!www\.)
- c. ^http:\/\/(?!www).*
- d. ^https?(?!://www\.)
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`^http://(?!www).*` 的思路最直接：以 `http://` 开头，且后面不是 `www`。`b` 也能匹配，但这里先按 `c` 记。

</v-click>

---
layout: default
---

# Q97

What does the regex \A(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\z match?

- a. An IPv6 address
- b. A MAC address
- c. An IPv4 address
- d. An email address
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

六组两位十六进制加冒号分隔，是典型 MAC address。

</v-click>

---
layout: default
---

# Q99

What does the regex \d{2,}(?=\D*$) match in "Item 23 is 42 years old"?

- a. 2342
- b. 23
- c. No match
- d. 42
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

正则要找的是“最后一个连续数字片段”，所以会匹配到句尾前的 `42`。

</v-click>

---
layout: default
---

# Q100

What is a regular expression?

- a. A way to calculate expressions in math
- b. A method for searching text in a document
- c. A sequence of characters that define a search pattern
- d. A programming language
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

regular expression 本质上就是定义搜索模式的一串字符。

</v-click>

---
layout: default
---

# Q102

What does the regex \b\d{1,3}(,\d{3})*\b match?

- a. A number formatted with commas (e.g., "1,000")
- b. A comma-separated list of numbers
- c. An IP address
- d. Any digit sequence without commas
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

这个模式匹配像 `1,000`、`12,345,678` 这样的千分位数字格式。

</v-click>

---
layout: default
---

# Q112

What does the regex (?&lt;!cat)dog ensure?

- a. "dog" is preceded by "cat"
- b. "dog" is not preceded by "cat"
- c. "dog" follows "cat"
- d. Both "cat" and "dog" are present
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

负向后顾 `(?&lt;!cat)` 要求 `dog` 前面不能是 `cat`。

</v-click>

---
layout: default
---

# Q113

What would the regex ^(\w+)(\s+\1)+$ match?

- a. A word repeated at least once, separated by whitespace
- b. Any number of repeated words without spaces
- c. A single word with trailing whitespace
- d. A line containing only whitespace
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

这个表达式通过反向引用 `\1` 匹配“同一个词重复出现”。

</v-click>

---
layout: default
---

# Q117

What is the function of the ? quantifier?

- a. Matches one or more occurrences
- b. Matches zero or more occurrences
- c. Matches zero or one occurrence
- d. Matches exactly one occurrence
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`?` 表示前一项出现 0 次或 1 次。

</v-click>

---
layout: default
---

# Q141

What does the * quantifier do in regular expressions?

- a. Matches exactly one character
- b. Matches zero or more occurrences of the preceding element
- c. Matches one or more occurrences of the preceding element
- d. Matches zero or one occurrence of the preceding element
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

`*` 表示前一项出现 0 次或多次。

</v-click>

---
layout: default
---

# Q142

What does (?&lt;=&gt;)\d+(?=&lt;\/?) match in a string like "&lt;div&gt;123&lt;/div&gt;"?

- a. The entire string including the tags
- b. Any digits followed by "&lt;/"
- c. Any digits preceded by "&gt;"
- d. 123, if it appears inside HTML tags
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

这个模式会把 HTML 标签之间的数字内容 `123` 抠出来。

</v-click>

---
layout: default
---

# Q144

Which regex captures text between double quotes, including escaped quotes within the text?

- a. `"[^"]+"`
- b. `\\\"[\w\s]*\\\"`
- c. `"(.*?)"`
- d. `".*"`
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

在给出的选项里，`"(.*?)"` 最接近“抓取双引号之间内容”的写法；但这题选项本身不够严谨。

</v-click>

---
layout: default
---

# Q146

What would the regex `\b(?!\d+\b)\w+\b` exclude in its matches?

- a. Words ending with a digit
- b. Words starting with a digit
- c. Words containing any digits
- d. Words entirely composed of digits
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

负向前瞻 `(?!\d+\b)` 排除了“整个词就是纯数字”的情况。

</v-click>

---
layout: default
---

# Q150

Which quantifier would match exactly 3 occurrences of the letter 'a'?

- a. a3
- b. a{3}
- c. a[3]
- d. a(3)
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

恰好 3 次要用 `{3}`，所以是 `a{3}`。

</v-click>

---
layout: default
---

# Q156

How would you match any line that does not contain the exact phrase "regex"?

- a. ^(?=.*\bregex\b).*$
- b. ^(?!.*\bregex\b).*
- c. .*\bregex\b.*
- d. ^.*(regex).*
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

负向前瞻 `^(?!.*\bregex\b).*` 用来排除包含 `regex` 的整行。

</v-click>

---
layout: default
---

# Q157

What will (\b[a-zA-Z]{3}\b)\s+\1 match?

- a. Any word repeated exactly once after one or more spaces
- b. A three-letter word followed by another three-letter word
- c. Any three-letter word repeated with one or more spaces in between
- d. A sequence of six letters with a space in the middle
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

这里要求“三个字母的单词重复出现”，且中间有空格。

</v-click>

---
layout: section
---

# Week 4

EDA & Pre-processing + Week 4 parsing + text pre-processing

---
layout: statement
---

Week 4 最容易把 numerical EDA、text pre-processing、文件读取混成一团，复习时要按“数据类型 -> 方法”去记。

---
layout: default
---

# Q2 / Q149

What challenges are presented by textual content in EDA for character and text data? (Select all that apply)

- a. Variability in text formats
- b. Data sparsity
- c. Ambiguity in language
- d. High dimensionality
- e. High computational costs
<v-click>

**参考答案**

`a, b, c, d, e`

</v-click>

<v-click>

**解析**

正确项是 `a`: Variability in text formats, `b`: Data sparsity, `c`: Ambiguity in language, `d`: High dimensionality, `e`: High computational costs。这些选项共同对应课程里的正确定义。

</v-click>
---
layout: default
---

# Q4

What factors influence the choice of data pre-processing techniques? (Select all that apply)

- a. Algorithm requirements
- b. Data quantity
- c. Data integrity
- d. Visualisation needs
- e. Data type
<v-click>

**参考答案**

`a, b, c, d, e`

</v-click>

<v-click>

**解析**

正确项是 `a`: Algorithm requirements, `b`: Data quantity, `c`: Data integrity, `d`: Visualisation needs, `e`: Data type。这些选项共同对应课程里的正确定义。

</v-click>

---
layout: default
---

# Q5

What measures of central tendency are commonly used in EDA for numerical data? (Select all that apply)

- a. Median
- b. Variance
- c. Mode
- d. Standard Deviation
- e. Mean
<v-click>

**参考答案**

`a, c, e`

</v-click>

<v-click>

**解析**

中心趋势看的是数据“中心”在哪里，常见是 mean / median / mode；variance 和 standard deviation 属于离散程度。

</v-click>

---
layout: default
---

# Q16 / Q120

Which method is used to get a summary of a DataFrame's structure and column types?

- a. df.info()
- b. df.describe()
- c. df.overview()
- d. df.summary()
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

`df.info()`` 会给出列名、非空数、dtype 等结构信息；`describe()` 更偏统计摘要。

</v-click>
---
layout: default
---

# Q23 / Q24 / Q96 / Q158

For what reasons might case normalisation not always be needed in text data pre-processing? (Select all that apply)

- a. To maintain the original meaning of words
- b. In information retrieval tasks
- c. For graphical data representation
- d. When performing named entity recognition
- e. In audio data processing
<v-click>

**参考答案**

`a, b, d`

</v-click>

<v-click>

**解析**

case normalisation 并不总是必须；像 named entity recognition 或需要保留原大小写信息时，大小写本身就有语义。

</v-click>
---
layout: default
---

# Q25

The process that simplifies text by converting it to its base form is called:

- a. Case normalization
- b. One-hot encoding
- c. Tokenisation
- d. Lemmatisation
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

把词还原成词典中的基本形式是 lemmatisation。

</v-click>

---
layout: default
---

# Q27

Why is understanding the structure of language (syntax) important in EDA for character and text data? (Select all that apply)

- a. It is crucial for visual data representation
- b. It supports the understanding of grammar rules
- c. It assists in analysing sentence structure
- d. It aids in constructing well-formed sentences and paragraphs
- e. It helps in hardware optimisation
<v-click>

**参考答案**

`b, c, d`

</v-click>

<v-click>

**解析**

syntax 关注语言结构与语法规则，有助于分析句子结构并生成/识别 well-formed text。

</v-click>

---
layout: default
---

# Q28

Which Pandas function is used to read a CSV file?

- a. pd.read_csv()
- b. pd.to_csv()
- c. pd.read_excel()
- d. pd.load_csv()
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

读取 CSV 用 `pd.read_csv()`。

</v-click>

---
layout: default
---

# Q32 / Q122

Which parameter in `pd.read_csv()` specifies the delimiter?

- a. `delim`
- b. `split`
- c. `delimiter`
- d. `sep`
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

`pd.read_csv()` 指定分隔符最常用的是 `sep`。

</v-click>
---
layout: default
---

# Q35

What does 'Character Data' consist of?

- a. Sequences of characters
- b. Single alphabetic letters, symbols, or numerals
- c. Quantifiable information
- d. Binary data
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

character data 指单个字符层面的数据，如字母、数字、符号。

</v-click>

---
layout: default
---

# Q37 / Q105

Which technique is used to handle categorical data by creating a binary column for each category?

- a. One-hot Encoding
- b. Label Encoding
- c. Normalisation
- d. Vectorisation
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

为每个类别开一列 0/1 特征，就是 one-hot encoding。

</v-click>
---
layout: default
---

# Q40

In the context of text data pre-processing, what is the purpose of case normalisation?

- a. To differentiate between common nouns and proper nouns
- b. To convert all the words into either uppercase or lowercase
- c. To increase the complexity of the text
- d. To identify and correct grammatical errors
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

case normalisation 就是把文本统一成大写或小写，减少同词不同写法带来的碎片化。

</v-click>

---
layout: default
---

# Q42 / Q131

Exploratory Data Analysis (EDA) is used for:

- a. Finalizing data collection methods
- b. Reducing the volume of data
- c. Uncovering patterns, trends, and anomalies
- d. Reducing the volume of data
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

EDA 的目标是发现模式、趋势和异常，不是定稿数据采集方案。

</v-click>
---
layout: default
---

# Q55

Why is it important to remove stop words in text data pre-processing? (Select all that apply)

- a. To highlight more meaningful words in text analysis
- b. To prevent skew in analysis results
- c. To add more complexity to the model
- d. To increase data set size
- e. To reduce computational load
<v-click>

**参考答案**

`a, b, e`

</v-click>

<v-click>

**解析**

去停用词是为了突出更有信息量的词、减少噪声并降低计算负担。

</v-click>

---
layout: default
---

# Q57

To read an Excel file into a DataFrame, which function is used?

- a. `pd.load_excel()`
- b. `pd.read_excel()`
- c. `pd.read_csv()`
- d. `pd.import_excel()`
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

读取 Excel 文件用 `pd.read_excel()`。

</v-click>

---
layout: default
---

# Q63

How do you set a DataFrame's column 'ID' as its index?

- a. `df.index = 'ID'`
- b. `df.set_index('ID')`
- c. `df.set('ID')`
- d. `df.index_col('ID')`
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

把某列设成索引常用 `df.set_index("ID")`。

</v-click>

---
layout: default
---

# Q66

What does the pd.read_json() function do?

- a. Converts a DataFrame to a JSON object
- b. Writes data to a JSON file
- c. Reads data from a JSON file into a DataFrame
- d. Parses JSON data into a list
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`pd.read_json()` 会把 JSON 读进 DataFrame。

</v-click>

---
layout: default
---

# Q71

Which techniques are essential for handling numerical data in EDA? (Select all that apply)

- a. Descriptive statistics
- b. Encoding
- c. Tokenisation
- d. Vectorisation
- e. Normalisation
<v-click>

**参考答案**

`a, e`

</v-click>

<v-click>

**解析**

数值型 EDA 常用 descriptive statistics，也可能做 normalisation；encoding / tokenisation / vectorisation 不是数值数据核心方法。

</v-click>

---
layout: default
---

# Q75

Which parameter in read_csv() is used to specify which rows should be used as header?

- a. top_row
- b. head_row
- c. header
- d. usecols
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

`header` 参数决定哪一行当列名。

</v-click>

---
layout: default
---

# Q77

What does the `skiprows=3` parameter in `pd.read_csv()` do?

- a. Skips any three rows randomly
- b. Skips first three columns from the left of the file
- c. Skips last three rows at the end of the file
- d. Skips first three rows from the beginning of the file
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

`skiprows=3` 表示从文件开头跳过前三行。

</v-click>

---
layout: default
---

# Q81

What is the middle value after all values are ordered in a data set called?

- a. Mean
- b. Mode
- c. Variance
- d. Median
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

有序数据中间那个值叫 median。

</v-click>

---
layout: default
---

# Q88

Which of the following is crucial for preparing text for NLP tasks?

- a. Variance Calculation
- b. Tokenization
- c. Normalization
- d. Image Encoding
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

NLP 的第一步通常是 tokenization。

</v-click>

---
layout: default
---

# Q90

Which measure of central tendency is the arithmetic average of a set of values?

- a. Median
- b. Mode
- c. Mean
- d. Range
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

算术平均数就是 mean。

</v-click>

---
layout: default
---

# Q110

Which data types are primarily analysed during EDA? (Select all that apply)

- a. Audio Data
- b. Categorical Data
- c. Numerical Data
- d. Text Data
- e. Image Data
<v-click>

**参考答案**

`b, c, d`

</v-click>

<v-click>

**解析**

课程中的 EDA 主要看 categorical、numerical、text 三类。

</v-click>

---
layout: default
---

# Q111

Which steps are involved in Lemmatisation for text data pre-processing? (Select all that apply)

- a. Reduction of words to their stems
- b. Application of morphological analysis
- c. Conversion of words to their base or dictionary form
- d. Use of part-of-speech tags
- e. Use of context surrounding the words
<v-click>

**参考答案**

`b, c, d, e`

</v-click>

<v-click>

**解析**

lemmatisation 依赖词形分析、词性和上下文，把词还原成 dictionary form；“stem” 不是它的核心定义。

</v-click>

---
layout: default
---

# Q123 / Q163

What is the aim of using Descriptive Statistics in EDA for Numerical Data?

- a. To manipulate the dataset
- b. To encode textual information into numerical values
- c. To provide insights into the central tendency, dispersion, and distribution shape
- d. To visualize data in 3D
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

descriptive statistics 的目标是概括中心位置、离散程度和分布形态。

</v-click>
---
layout: default
---

# Q124

What does continuous data represent?

- a. Visual information encoded digitally
- b. Quantifiable information that can be divided infinitely
- c. Single alphabetic letters or symbols
- d. Countable values or categories
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

continuous data 是可以无限细分的可量化数值。

</v-click>

---
layout: default
---

# Q135

Which data visualisation method is primarily used for numerical data to understand its spread and central tendency?

- a. Pie Charts
- b. Histograms
- c. Mind Maps
- d. Flowcharts
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

看数值分布与中心位置最常用 histogram。

</v-click>

---
layout: default
---

# Q145

Which of the following are benefits of correctly identifying data types during EDA? (Select that all apply)

- a. Guides data cleaning and preprocessing
- b. Enables effective visualisation
- c. Determines the color scheme of visualisations
- d. Assists in feature engineering
- e. Allows for appropriate analysis
<v-click>

**参考答案**

`a, b, d, e`

</v-click>

<v-click>

**解析**

正确识别数据类型能指导清洗、可视化、特征工程和后续分析。

</v-click>

---
layout: default
---

# Q151

What are the steps involved in Count Vectorisation? (Select all that apply)

- a. Vocabulary Building
- b. Normalisation
- c. Count Calculation
- d. Encoding
- e. Tokenisation
<v-click>

**参考答案**

`a, c, e`

</v-click>

<v-click>

**解析**

count vectorisation 通常先 tokenise、建立词表，再统计每个词出现次数。

</v-click>

---
layout: default
---

# Q153

Which of the following are goals of Exploratory Data Analysis (EDA)? (Select all that apply)

- a. To understand the patterns, anomalies, and relationships in the data
- b. To explore and summarise the main characteristics of the data visually
- c. To use statistical graphics, plots, and information tables
- d. To perform complex predictive modeling
- e. To manipulate the data set
<v-click>

**参考答案**

`a, b, c`

</v-click>

<v-click>

**解析**

EDA 目标是理解数据并做可视化总结，不是直接做复杂预测建模。

</v-click>

---
layout: default
---

# Q164

What is the significance of identifying data types during EDA?

- a. It changes the textual content into images
- b. It influences how data will be processed and analyzed
- c. It is only important for numerical data
- d. It determines the type of cake to bake
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

识别数据类型会直接影响后续怎么处理和分析数据。

</v-click>

---
layout: section
---

# Week 5

Data Discovery & Collection

---
layout: statement
---

Week 5 的关键词是 metadata、catalog、profiling、provenance，考试很爱考概念边界。

---
layout: default
---

# Q10

What aspects does Data Cataloging and Metadata Management cover? (Select all that apply)

- a. Usage metadata
- b. Data anonymisation
- c. Metadata collection
- d. Data lineage documentation
- e. Catalog creation
<v-click>

**参考答案**

`a, c, d, e`

</v-click>

<v-click>

**解析**

cataloging / metadata management 关注 metadata collection、lineage、catalog 本身，也会包含 usage metadata；anonymisation 属于隐私保护，不是 cataloging 核心内容。

</v-click>

---
layout: default
---

# Q31 / Q127

Qualitative Data is:

- a. Exclusively about quantities
- b. Only numerical
- c. Descriptive and conceptual
- d. Limited to structured research instruments
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

qualitative data 强调描述性、概念性，不是纯数量。

</v-click>
---
layout: default
---

# Q44 / Q91

Data Cataloging aids in:

- a. Making it harder to find and understand data
- b. Ignoring data lineage
- c. Decreasing data accessibility
- d. Creating a searchable catalog of data assets
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

data catalog 的作用是让数据资产可搜索、可理解、可发现。

</v-click>
---
layout: default
---

# Q49 / Q84

Which is NOT a method of collecting structured data?

- a. Relational databases
- b. Online forms
- c. Surveys and questionnaires
- d. Text mining and NLP
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

text mining / NLP 主要处理非结构化文本，不属于 structured data collection 方法。

</v-click>
---
layout: default
---

# Q50 / Q137

Which of the following is NOT a part of the Data Discovery Process?

- a. Data Cataloging and Metadata Management
- b. Data Exploration and Visualization
- c. Data Encryption
- d. Data Integration and Consolidation
<v-click>

**参考答案**

`c`

</v-click>

<v-click>

**解析**

data encryption 属于安全控制，不是 data discovery 流程本身。

</v-click>
---
layout: default
---

# Q68

Factors to consider during the data collection phase include: (Select all that apply)

- a. Collection method efficiency
- b. Source reliability
- c. Data format
- d. Cost of data storage physical locations
<v-click>

**参考答案**

`a, b, c`

</v-click>

<v-click>

**解析**

collection 阶段常看方法效率、来源可靠性、数据格式；“physical locations” 不是这里的核心。

</v-click>

---
layout: default
---

# Q72

Which are considered primary sources of data? (Select all that apply)

- a. Observations
- b. Experiments
- c. Industry reports
- d. Surveys
- e. Government publications
<v-click>

**参考答案**

`a, b, d`

</v-click>

<v-click>

**解析**

primary source 是直接采集的数据，如 observations、experiments、surveys；industry reports / government publications 更像二手资料。

</v-click>

---
layout: default
---

# Q85

Which phase comes immediately after data discovery?

- a. Data storage
- b. Data collection
- c. Data cleaning
- d. Data analysis
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

discovery 后面紧接着就是 collection。

</v-click>

---
layout: default
---

# Q89 / Q159

Data Security measures are essential for:

- a. Ensuring data is openly accessible
- b. Secure storage and transmission of data
- c. Reducing data quality
- d. Encouraging unauthorized data access
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

data security 关注安全存储与传输，不是开放访问。

</v-click>
---
layout: default
---

# Q98 / Q154

What roles does data play in decision-making? (Select all that apply)

- a. Crisis prediction and response
- b. Compliance monitoring
- c. Understanding customer behaviour
- d. Enhancing product quality
- e. Operational efficiency
<v-click>

**参考答案**

`a, b, c, d, e`

</v-click>

<v-click>

**解析**

数据在决策里能支持风险、合规、客户洞察、产品和运营优化，所以五项都对。

</v-click>
---
layout: default
---

# Q107

Ethical considerations in Data Collection include: (Select all that apply)

- a. Privacy and anonymity
- b. Informed consent
- c. Data retention and disposal
- d. Data beautification
- e. Compliance with laws and regulations
<v-click>

**参考答案**

`a, b, c, e`

</v-click>

<v-click>

**解析**

伦理采集通常包括隐私、知情同意、保留/销毁规范和法律合规。

</v-click>

---
layout: default
---

# Q128

The main advantage of using existing data is:

- a. Always perfectly matching specific needs
- b. Time efficiency and cost reduction
- c. Increased costs
- d. Reduced access to diverse data
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

existing data 的主要优势通常是省时省钱。

</v-click>

---
layout: default
---

# Q132

Metadata in Data Cataloging includes:

- a. Only structural metadata
- b. Descriptive, Structural, and Technical Metadata
- c. Only usage metadata
- d. Only descriptive metadata
<v-click>

**参考答案**

`b`

</v-click>

<v-click>

**解析**

metadata 不只是一种类型，常见有 descriptive、structural、technical 等。

</v-click>

---
layout: default
---

# Q133

What role does data play in modern business decision-making?

- a. It is not significant in decision-making
- b. It is exclusively used for financial analysis
- c. It is only used for data storage
- d. It aids in understanding customer behavior and evidence-based strategic planning
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

现代业务决策里，数据能支持客户理解和基于证据的规划。

</v-click>

---
layout: default
---

# Q134 / Q162

Metadata Collection is critical for understanding:

- a. Only the data's numerical value
- b. Restricting data access
- c. How to delete the data
- d. The data's origin, format, and characteristics
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

metadata collection 帮助理解数据从哪来、什么格式、有哪些特征。

</v-click>
---
layout: default
---

# Q136

Ensuring data privacy and security is crucial due to:

- a. Regulations
- b. Lack of regulations
- c. Unimportance of data sensitivity
- d. The ease of data handling
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

隐私和安全之所以重要，一个直接原因就是法规要求。

</v-click>

---
layout: default
---

# Q139

Text Mining and Natural Language Processing (NLP) are methods for collecting:

- a. Structured data
- b. Numerical data only
- c. Semi-structured data
- d. Unstructured data
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

text mining / NLP 处理的是 unstructured text。

</v-click>

---
layout: default
---

# Q161

Data Privacy measures are intended to:

- a. Expose sensitive information
- b. Increase data accessibility to the public
- c. Limit the use of data for analysis
- d. Protect sensitive information in compliance with regulations
<v-click>

**参考答案**

`d`

</v-click>

<v-click>

**解析**

privacy measures 的目标是依法保护敏感信息，而不是公开它。

</v-click>

---
layout: section
---

# Week 6

Data Structuring

---
layout: statement
---

Data structuring 题量不大，但经常和 collection、integration 混淆，要特别区分目标。

---
layout: default
---

# Q38

Graph data models are ideal for:

- a. Representing relationships between entities
- b. Ignoring entity relationships
- c. Simple numerical analysis
- d. Storing textual data only
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

graph data model 最适合表达实体之间的关系。

</v-click>

---
layout: default
---

# Q51

What does Structured Data refer to?

- a. Data that is organized and easily understandable by machine language
- b. Multimedia data
- c. Social media content
- d. Data that is disorganized and random
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

structured data 是机器容易理解、字段组织清晰的数据。

</v-click>

---
layout: default
---

# Q60

Data Profiling and Assessment involve understanding which types of data structure? (Select all that apply)

- a. Big data
- b. Time-series data
- c. Structured data
- d. Unstructured data
- e. Graph data
<v-click>

**参考答案**

`b, c, d, e`

</v-click>

<v-click>

**解析**

profiling / assessment 需要先看数据是什么结构，因此 time-series、structured、unstructured、graph 都要识别。

</v-click>

---
layout: default
---

# Q65

Which data structures are essential for Data Discovery and Collection? (Select all that apply)

- a. Relational databases
- b. Multimedia data
- c. Graph data models
- d. Time-series data
- e. Data warehouses
<v-click>

**参考答案**

`a, b, c, d, e`

</v-click>

<v-click>

**解析**

这题把“数据结构”和“数据来源/类型”混在一起了；按课程复习时先把这几类都记住。

</v-click>

---
layout: default
---

# Q140

Time-series data is indexed in:

- a. Time order
- b. Random order
- c. Hierarchical order
- d. Alphabetical order
<v-click>

**参考答案**

`a`

</v-click>

<v-click>

**解析**

time-series 数据按时间顺序索引。

</v-click>

---
layout: end
---

# End

这份全题版 deck 可直接用于补习班逐题讲解。
