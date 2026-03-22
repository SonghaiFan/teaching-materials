---
theme: apple-basic
title: FIT5196 Quiz 1 全题真题解析
layout: intro
---

# FIT5196 Quiz 1

真题解析

---

### Week 1 (6 题)

- 范围：Jupyter Notebook、Markdown、Python basics

## Question 1


**How do you make text italic in Markdown?** (Select all that apply)

- a. Surround the text with `**`
- b. Surround the text with `~~`
- c. Surround the text with `_`
- d. Surround the text with `*`

<v-click>

参考答案： `c, d`

解析： 斜体在 Markdown 里通常写成 `*text*` 或 `_text_`，不是 `**`（粗体）也不是 `~~`（删除线）。

</v-click>

---

## Question 6



**To create a bullet list in Markdown, which symbol can you use?**

- a. All of the above
- b. `*`
- c. `-`
- d. `+`

<v-click>

参考答案： `a`

解析： 正确项是 `a`: All of the above。它最符合这道题在课程里的定义。

</v-click>

---

## Question 20



**To emphasise text with bold in Markdown, you can use:**

- a. Double tildes or double dollar signs
- b. Double asterisks or double underscores
- c. Single asterisks or single underscores
- d. Triple asterisks or triple underscores

<v-click>

参考答案： `b`

解析： Markdown 粗体用双星号或双下划线，即 `**text**` 或 `__text__`。

</v-click>
---

## Question 26



**For numbered lists in Markdown, what character follows the number? (Select all that apply)**

- a. `)`
- b. `*`
- c. `.`
- d. `-`

<v-click>

参考答案： `a, c`

解析： 常见的的 Markdown 有序列表写法是 `1.`，`1)` 其实也可以。

</v-click>

---

## Question 116



**To emphasise text with bold in Markdown, you can use:**

- a. Double asterisks or double underscores
- b. Triple asterisks or triple underscores
- c. Single asterisks or single underscores
- d. Double tildes or double dollar signs

<v-click>

参考答案： `a`

解析： 和 Q20 同义，粗体是双星号或双下划线。

</v-click>
---

## Question 155



**To emphasise text with bold in Markdown, you can use:**

- a. Single asterisks or single underscores
- b. Double tildes or double dollar signs
- c. Triple asterisks or triple underscores
- d. Double asterisks or double underscores

<v-click>

参考答案： `d`

解析： 和 Q20/Q116 同义，粗体仍是双星号或双下划线。

</v-click>
---

### Week 2 (48 题)

- 范围：Data Wrangling Process & Tasks + Week 2 pandas applied session

## Question 8



**How do you select rows 10 to 20 from a DataFrame df? (Select all that apply)**

- a. `df.iloc[9:20]`
- b. `df.loc[10:20]`
- c. `df.locate[9:20]`
- d. `df[9:20]`

<v-click>

参考答案： `a, d`

解析： `iloc[9:20]` 取的是第 10 到第 20 行（位置索引，右端不含）；`df[9:20]` 也会按切片取对应行。`loc[10:20]` 依赖标签索引，课内通常不作为标准答案。没有`locate`这样的语法。

</v-click>

---

## Question 9



**Which of the following are considered tasks in the Data Wrangling process? (Select all that apply)**

- a. Data Modification
- b. Data Storing
- c. Data Validation
- d. Data Presentation
- e. Data Cleaning

<v-click>

参考答案： `b, c, e`

解析： 正确项是 `b`: Data Storing, `c`: Data Validation, `e`: Data Cleaning。这些选项共同对应课程里的正确定义。

</v-click>

---

## Question 12



**Data simplification can involve: (Select all that apply)**

- a. Enhancing understandability of data
- b. Removing relevant information
- c. Filtering out irrelevant information
- d. Summarizing complex data

<v-click>

参考答案： `a, c, d`

解析： `b`是明显的错误答案。

</v-click>

---

## Question 14



**The goals of data enrichment include: (Select all that apply)**

- a. Adding value to the data
- b. Improving data quality
- c. Enhancing data analysis capabilities
- d. Simplifying data formats

<v-click>

参考答案： `a, b, c`

解析： data enrichment 的目标是加上下文、提升价值、改善可分析性；“simplifying data formats” 更像 pre-processing / transformation。

</v-click>
---

## Question 17



**Data cleaning may involve: (Select all that apply)**

- a. Introducing new errors
- b. Removing duplicates
- c. Handling missing values
- d. Correcting errors

<v-click>

参考答案： `b, c, d`

解析： `a`是明显的错误答案。

</v-click>

---

## Question 22



**How can you rename the column 'A' to 'B' in a DataFrame df?**

- a. `df.columns['A'] = 'B'`
- b. `df.columns.rename('A', 'B')`
- c. `df.rename('A', 'B')`
- d. `df.rename(columns={'A': 'B'})`

<v-click>

参考答案： `d`

解析： Pandas 改列名标准写法是 `df.rename(columns={"A": "B"})`。

</v-click>

---

## Question 33



**How do you check for missing values in a DataFrame df? (Select all that apply)**

- a. `df.isna()`
- b. `df.has_null()`
- c. `df.missing()`
- d. `df.isnull()`

<v-click>

参考答案： `a, d`

解析： Pandas 检查缺失值常用 `isna()` 和 `isnull()`。

</v-click>

---

## Question 34



**Scalability in data wrangling is essential for:**

- a. Handling increased data loads without performance loss
- b. Reducing data processing power
- c. Maintaining a constant volume of data
- d. Complicating data integration processes

<v-click>

参考答案： `a`

解析： scalability 指数据量上来后仍能处理，不是把数据量固定不变。

</v-click>
---

## Question 36



**Data standardization helps ensure data is:**

- a. In a consistent format
- b. Only available in one unit of measurement
- c. Inconsistent across datasets
- d. Difficult to analyze

<v-click>

参考答案： `a`

解析： 这里的 standardization 更偏“统一标准/格式”，目标是让数据表示保持一致。

</v-click>
---

## Question 39



**What process involves scaling data to a small, specified range?**

- a. Diversification
- b. Normalisation
- c. Aggregation
- d. Segmentation

<v-click>

参考答案： `b`

解析： 把数值缩到一个小范围（如 `[0,1]`）是 normalisation。

</v-click>
---

## Question 41



**In data quality management, what is crucial for maintaining high-quality data?**

- a. Aesthetic appeal
- b. Data volume
- c. Data Governance
- d. Data variety

<v-click>

参考答案： `c`

解析： 持续高质量数据离不开 data governance，因为要靠规则、责任和流程来维护。

</v-click>
---

## Question 43



**Data enrichment may involve:**

- a. Verifying data accuracy
- b. Adding time-related data
- c. Correcting data errors
- d. Converting data into a binary format

<v-click>

参考答案： `b`

解析： enrichment 常见做法是补充时间、地理、人口等额外上下文。

</v-click>
---

## Question 45



**Machine Learning enhances data quality management through:**

- a. Solely focusing on data visualization
- b. A combination of techniques including NLP and continuous monitoring
- c. Only data cleansing
- d. Only automated error detection

<v-click>

参考答案： `b`

解析： 机器学习在 data quality management 里常用于自动识别问题、持续监控和 NLP 等组合方法。

</v-click>
---

## Question 46



**Data Integration aims to:**

- a. Reduce the overall data quality
- b. Create inconsistent datasets
- c. Combine multiple data sources for a unified view
- d. Provide a disjointed view of information

<v-click>

参考答案： `c`

解析： data integration 的目标是把多个来源统一成一个一致视图。

</v-click>
---

## Question 47



**Which type of data anomalies refers to a single data point deviating significantly from the rest?**

- a. Complex Anomalies
- b. Contextual Anomalies
- c. Collective Anomalies
- d. Point Anomalies

<v-click>

参考答案： `d`

解析： 单个点明显偏离整体，就是 point anomaly。

</v-click>
---

## Question 48



**Which of the following is NOT a goal of data validation?**

- a. Verify data is in the expected format
- b. Validate range and constraints
- c. Ensure data accurately reflects real-world entities
- d. Enhance the speed of data retrieval

<v-click>

参考答案： `d`

解析： validation 是检查格式、范围、逻辑是否合理，不是提升读取速度。

</v-click>
---

## Question 52



**In data wrangling, data validation ensures: (Select all that apply)**

- a. Data inconsistency is promoted
- b. Data meets predefined standards
- c. Data is in a usable format for analysis
- d. Accuracy and reliability of data

<v-click>

参考答案： `b, c, d`

解析： validation 要保证数据符合预设标准、可靠且可用于后续分析。 `a`是明显的错误答案。

</v-click>

---

## Question 53



**How can you rename the column 'A' to 'B' in a DataFrame df?**

- a. `df.rename(columns={'A': 'B'})`
- b. `df.columns['A'] = 'B'`
- c. `df.rename('A', 'B')`
- d. `df.columns.rename('A', 'B')`

<v-click>

参考答案： `a`

解析： 这题和 Q22 同义，标准写法仍是 `df.rename(columns={"A": "B"})`。

</v-click>
---

## Question 59



**Which of the following are common goals of data wrangling? (Select all that apply)**

- a. Increasing data complexity
- b. Ignoring data inconsistencies
- c. Improving data quality
- d. Facilitating easier access to data

<v-click>

参考答案： `c, d`

解析： wrangling 的常见目标是提高质量、提升可访问性，不是增加复杂度。

</v-click>
---

## Question 67



**What role does machine learning play in data quality management?**

- a. Enhancing processes of identifying and correcting data quality issues
- b. Reducing the need for data governance
- c. Only for data visualization
- d. Only for database management

<v-click>

参考答案： `a`

解析： 机器学习的作用是帮助发现、识别并修正数据质量问题。

</v-click>
---

## Question 70



**Data cleaning may involve: (Select all that apply)**

- a. Correcting errors
- b. Removing duplicates
- c. Handling missing values
- d. Introducing new errors

<v-click>

参考答案： `a, b, c`

解析： cleaning 包括纠错、去重、处理缺失，不会“引入新错误”。

</v-click>
---

## Question 78



**Which method would you use to sort a DataFrame df by the column 'Name'?**

- a. `df.rank('Name')`
- b. `df.sort_values(by='Name')`
- c. `df.sort_by('Name')`
- d. `df.sort('Name')`

<v-click>

参考答案： `b`

解析： 按列排序标准写法是 `df.sort_values(by="Name")`。

</v-click>
---

## Question 79



**Which is NOT a feature of Big Data?**

- a. Manageable by traditional software
- b. Voluminous
- c. Includes various data structures
- d. Involves high velocity

<v-click>

参考答案： `a`

解析： Big Data 的典型特征是 volume、variety、velocity，通常不能被传统软件轻松处理。

</v-click>
---

## Question 80



**What does simplifying access to data aim to achieve?**

- a. Increase the complexity of data access
- b. Organise data in a user-friendly manner
- c. Make data accessible only to data scientists
- d. Restrict data access

<v-click>

参考答案： `b`

解析： simplifying access 的目标是让数据更容易找、更容易用。

</v-click>
---

## Question 82



**What is the primary purpose of Data Wrangling?**

- a. To analyze complex data types
- b. To ensure data privacy
- c. To acquire, clean, structure, and enrich raw data for analysis
- d. To visualize data trends

<v-click>

参考答案： `c`

解析： data wrangling 的核心就是把原始数据整理成可分析数据。

</v-click>
---

## Question 83



**What does data enrichment not involve?**

- a. Creating new variables
- b. Reducing data insights
- c. Adding external context
- d. Enhancing data with additional information

<v-click>

参考答案： `b`

解析： enrichment 是增加信息与洞察，不是减少 insights。

</v-click>
---

## Question 86



**The process of identifying and correcting inconsistencies in data is called:**

- a. Data collection
- b. Data integration
- c. Data cleaning
- d. Data enrichment

<v-click>

参考答案： `c`

解析： 识别并修正不一致，属于 data cleaning。

</v-click>
---

## Question 87



**Facilitating data integration helps with:**

- a. Ignoring data quality
- b. Keeping data in isolated systems
- c. Transforming disparate data into a common format
- d. Making it harder to combine data from different sources

<v-click>

参考答案： `c`

解析： integration 的一个关键作用就是把异构数据转成共同格式。

</v-click>
---

## Question 92



**Which of the following is NOT a goal of data validation?**

- a. Validate range and constraints
- b. Ensure data accurately reflects real-world entities
- c. Enhance the speed of data retrieval
- d. Verify data is in the expected format

<v-click>

参考答案： `c`

解析： 和 Q48 同理，validation 不以提升检索速度为目标。

</v-click>
---

## Question 93



**A major challenge in data wrangling is:**

- a. Avoiding data standardization
- b. Maintaining low data quality
- c. Data privacy and security
- d. Handling small volumes of data

<v-click>

参考答案： `c`

解析： data privacy and security 是 data wrangling 的典型难点之一。

</v-click>
---

## Question 94



**Machine Learning enhances data quality management through:**

- a. Solely focusing on data visualization
- b. A combination of techniques including NLP and continuous monitoring
- c. Only data cleansing
- d. Only automated error detection

<v-click>

参考答案： `b`

解析： 这题和 Q45 同义，关键是 ML 能结合多种自动化方法提升质量管理。

</v-click>
---

## Question 101



**Data Integration and Consolidation require: (Select all that apply)**

- a. Combining data sources
- b. Harmonise data formats
- c. Data anonymisation
- d. Data cleaning
- e. Ensuring consistency

<v-click>

参考答案： `a, b, d, e`

解析： integration / consolidation 要合并来源、统一格式、清洗并保证一致性。

</v-click>

---

## Question 103



**How do you select a single column named 'Age' from a DataFrame df? (Select al that apply)**

- a. `df['Age']`
- b. `df.select('Age')`
- c. `df.index('Age')`
- d. `df.Age`

<v-click>

参考答案： `a, d`

解析： 单列可用 `df["Age"]` 或属性访问 `df.Age`。

</v-click>
---

## Question 104



**Which of the following are common goals of data wrangling? (Select all that apply)**

- a. Increasing data complexity
- b. Ignoring data inconsistencies
- c. Facilitating easier access to data
- d. Improving data quality

<v-click>

参考答案： `c, d`

解析： 和 Q59 同义，目标仍是提升质量与可访问性。

</v-click>
---

## Question 108



**In data wrangling, data validation ensures: (Select all that apply)**

- a. Data meets predefined standards
- b. Accuracy and reliability of data
- c. Data inconsistency is promoted
- d. Data is in a usable format for analysis

<v-click>

参考答案： `a, b, d`

解析： 和 Q52 同义，validation 关注标准、可靠性和可用性。

</v-click>
---

## Question 109



**To drop rows with any missing values in the data frame `df`, you use:**

- a. `df.fillna()`
- b. `df.dropna()`
- c. `df.remove_na()`
- d. `df.delete_missing()`

<v-click>

参考答案： `b`

解析： 删除含缺失值的行用 `df.dropna()`。

</v-click>
---

## Question 114



**Data cleaning may involve: (Select all that apply)**

- a. Removing duplicates
- b. Correcting errors
- c. Handling missing values
- d. Introducing new errors

<v-click>

参考答案： `a, b, c`

解析： 和 Q17/Q70 同义，cleaning 还是去重、纠错、处理缺失。

</v-click>
---

## Question 118



**Which function is used to concatenate two DataFrames vertically?**

- a. `pd.concat()`
- b. `pd.join()`
- c. `pd.merge()`
- d. `pd.append()`

<v-click>

参考答案： `a`

解析： 纵向拼接两个 DataFrame 通常用 `pd.concat()`。

</v-click>
---

## Question 119



**Effective data validation checks are: (Select all that apply)**

- a. Completeness checking
- b. Range checking
- c. Encryption methods
- d. Consistency checking

<v-click>

参考答案： `a, b, d`

解析： 有效 validation check 常见有 completeness、range、consistency；encryption 不是 validation check。

</v-click>
---

## Question 121



**Data integration challenges include:**

- a. Combining data of varying formats and quality
- b. Maintaining data in disparate formats
- c. Simplifying the combination of similar data
- d. Ignoring data from different sources

<v-click>

参考答案： `a`

解析： integration 真正难在格式和质量不一致，不是“忽略不同来源”。

</v-click>
---

## Question 125



**Which type of data anomalies refers to a single data point deviating significantly from the rest?**

- a. Collective Anomalies
- b. Point Anomalies
- c. Complex Anomalies
- d. Contextual Anomalies

<v-click>

参考答案： `b`

解析： 和 Q47 同义，这里 point anomaly 的选项顺序变了。

</v-click>
---

## Question 126



**Data duplication is an example of:**

- a. Regular expression pattern
- b. Data quality issue
- c. Data wrangling task
- d. Data anomaly

<v-click>

参考答案： `b`

解析： 重复数据首先是 data quality issue；虽然也常被看作 anomaly，但复习时先按课程答案记。

</v-click>
---

## Question 129



**Which is NOT a challenge in data wrangling?**

- a. Handling large volumes of data
- b. Ensuring data privacy and security
- c. Maintaining outdated data formats
- d. Decreasing analytical efficiency

<v-click>

参考答案： `d`

解析： 前三项都是挑战；“decreasing analytical efficiency” 不是挑战表述，而是负面结果说法。

</v-click>

---

## Question 130



**Which is NOT a challenge in maintaining data quality?**

- a. Complexity of data integration
- b. Volume and variety of data
- c. Data silos
- d. High-quality data tools

<v-click>

参考答案： `d`

解析： 真正的挑战是集成复杂、量大、数据孤岛；高质量工具本身不是挑战。

</v-click>
---

## Question 138



**The purpose of data aggregation is to:**

- a. Increase data detail
- b. Disperse data across sources
- c. Summarise data for analysis
- d. Complicate data analysis

<v-click>

参考答案： `c`

解析： aggregation 的目的就是把明细汇总成更适合分析的结果。

</v-click>
---

## Question 143



**What is a 'Point Anomaly'?**

- a. A data point that adheres perfectly to the data set pattern
- b. A data point that significantly deviates from the rest of the data set
- c. A standard deviation in statistical analysis
- d. A group of data points that are not unusual

<v-click>

参考答案： `b`

解析： point anomaly 就是单个点显著偏离整体。

</v-click>
---

## Question 152



**Which method would you use to sort a DataFrame df by the column 'Name'?**

- a. `df.sort_values(by='Name')`
- b. `df.sort('Name')`
- c. `df.rank('Name')`
- d. `df.sort_by('Name')`

<v-click>

参考答案： `a`

解析： 和 Q78 同义，只是正确项顺序换成了 `a`。

</v-click>
---

## Question 160



**What process involves scaling data to a small, specified range?**

- a. Diversification
- b. Aggregation
- c. Normalisation
- d. Segmentation

<v-click>

参考答案： `c`

解析： 和 Q39 同义，缩放到小范围依然是 normalisation。

</v-click>
---

### Week 3 (39 题)

- 范围：Regular Expressions

## Question 3



**For matching IPv4 addresses, which regex is accurate and avoids matching numbers beyond the valid range of 0-255?**

- a. `\b(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\b`
- b. `[0-9]{1,3}\.([0-9]{1,3}){3}`
- c. `\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b`
- d. `\b(\d{1,3}\.){3}\d{1,3}\b`

<v-click>

参考答案： `(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`

解析： 
`\b` = word boundary（单词边界），放在每个分支前，目的是避免匹配到数字中间，例如：1234 里不会误匹配 234
选项只有 `c` 勉强成立，把每一段都限制在 `0-255` 范围内； `25[0-5]` → 250–255，`2[0-4][0-9]` → 200–249，`[01]?[0-9][0-9]?` → 0–199。 `b` 和 `d` 只限制位数，不限制数值大小。

</v-click>
---

## Question 7



**What does a regular expression describe?**

- a. Text pattern
- b. Image pattern
- c. Numeric calculation
- d. Audio frequency

<v-click>

参考答案： `a`

解析： 正确项是 `a`: Text pattern。它最符合这道题在课程里的定义。

</v-click>
---

## Question 11



**In the regex `(?:foo)(foo)`, what is the difference between `(?:foo)` and `(foo)`?**

- a. `(?:foo)` matches and captures "foo"; (foo) only matches "foo"
- b. Neither captures "foo"; they only match
- c. `(?:foo)` only matches "foo"; `(foo)` matches and captures "foo"
- d. Both capture "foo" for future use

<v-click>

参考答案： `c`

解析： `(?:foo)` 是非捕获组，只分组不保存；`(foo)` 是捕获组，会把匹配结果保存下来供后续引用。

</v-click>
---

## Question 13



**What does the regex `(?<=\b20)\d{2}\b` match in "Class of 2024"?**

- a. 2024
- b. Class of
- c. 24
- d. 20

<v-click>

参考答案： `c`

解析： lookbehind `(?<=\b20)` 要求前面紧跟 `20`，因此真正被匹配的是后面的两位数字 `24`。

</v-click>
---

## Question 15



**Which of the following is NOT a character set used in regular expressions?**

- a. `[a-zA-Z]`
- b. `\d`
- c. `[0-9]`
- d. `(a-z)`

<v-click>

参考答案： `d`

解析： 正确项是 `d`: `(a-z)`。

</v-click>
---

## Question 18



**How would you match "http" at the beginning of a string?**

- a. `\bhttp`
- b. `http$`
- c. `http\b`
- d. `^http`

<v-click>

参考答案： `d`

解析： `^` 匹配字符串开头，所以要写 `^http`。

</v-click>
---

## Question 19



**What will the regex `(?<=\b20)[0-9]{2}\b` match in "Graduating in 2025"?**

- a. 2025
- b. 25
- c. 20
- d. No match

<v-click>

参考答案： `b`

解析： 和 Q13 同理，`(?<=\b20)` 只把 `20` 后面的两位数取出来，所以是 `25`。

</v-click>
---

## Question 21



**Which character escapes special characters in regular expressions?**

- a. `^`
- b. `$`
- c. `|`
- d. `\`

<v-click>

参考答案： `d`

解析： 正确项是 `d`: \。它最符合这道题在课程里的定义。

</v-click>
---

## Question 29



**Which of the following is a valid way to match either 'color' or 'colour'?**

- a. `colo(u|r)`
- b. `colou|r`
- c. `colou?r`
- d. `(color|colour)`

<v-click>

参考答案： `c，d`

解析： `colou?r` 中 `u?` 表示 `u` 可有可无，因此能同时匹配 `color` 和 `colour`。`(color|colour)` 也能匹配，但比较笨。

</v-click>

---

## Question 30



**Given the string 'hello123', what does the regex `(?<=\D)(?=\d)` locate?**

- a. The position between 'o' and '1'
- b. The sequence "123"
- c. The digit "1"
- d. The letter 'o'

<v-click>

参考答案： `a`

解析： 这个零宽断言定位的是“非数字后面紧跟数字”的那个位置，也就是 `o` 和 `1` 中间。
```
h e l l o | 1 2 3
          ↑
        匹配点（但没有宽度）
```
</v-click>

---

## Question 54



**Which regex finds all instances of "not" that are not immediately followed by "good"?**

- a. `not(?! good)`
- b. `not(?= good)`
- c. `not(?=good)`
- d. `not(?!good)`

<v-click>

参考答案： `d`

解析： 负向前瞻 `(?!good)` 表示后面不能立刻跟 `good`，所以选 `not(?!good)`。

</v-click>

---

## Question 56



**What does the regex `^[\w.+-]+@([\w-]+\.)+[a-zA-Z]{2,7}$` not allow in the email username part?**

- a. Spaces
- b. Underscore
- c. Plus signs
- d. Digits

<v-click>

参考答案： `a`

解析： 用户名部分的字符类里不包含空格，所以空格不允许。

</v-click>
---

## Question 58



**What does the regex `(?<=\b20)\d{2}\b` match in "Class of 2024"?**

- a. 20
- b. 24
- c. 2024
- d. Class of

<v-click>

参考答案： `b`

解析： 和 Q13/Q19 同理，真正被匹配到的是 `20` 后面的两位，即 `24`。

</v-click>
---

## Question 61



**Which metacharacter matches the beginning of a line?**

- a. ^
- b. |
- c. \b
- d. $

<v-click>

参考答案： `a`

解析： 行首锚点是 `^`。

</v-click>
---

## Question 62



**How would you match "cat" or "bat"?**

- a. [cb]at
- b. cat||bat
- c. (cb)at
- d. [c&b]at

<v-click>

参考答案： `a`

解析： `[cb]at` 表示首字母可以是 `c` 或 `b`。

</v-click>
---

## Question 64



**In regex, what does (?:abc) represent?**

- a. An optional character sequence
- b. A non-capturing group
- c. A capturing group
- d. A repeated sequence

<v-click>

参考答案： `b`

解析： `(?:abc)` 是 non-capturing group。

</v-click>
---

## Question 69



**What does the `+` quantifier do?**

- a. Matches exactly one occurrence
- b. Matches zero or more occurrences
- c. Matches zero or one occurrence
- d. Matches one or more occurrences

<v-click>

参考答案： `d`

解析： `+` 表示前一项出现 1 次或多次。

</v-click>

---

## Question 73



**What does the {3,6} quantifier mean?**

- a. Matches at least 3 occurrences of the preceding element
- b. Matches up to 6 occurrences of the preceding element
- c. Matches between 3 and 6 occurrences of the preceding element
- d. Matches exactly 3 or exactly 6 occurrences of the preceding element

<v-click>

参考答案： `c`

解析： `{3,6}` 就是前一项出现 3 到 6 次。

</v-click>
---

## Question 74



**In regular expressions, what does \A match?**

- a. The beginning of a string
- b. A word boundary
- c. The end of a string
- d. A non-word boundary

<v-click>

参考答案： `a`

解析： `\A` 匹配整个字符串开头。

</v-click>
---

## Question 76



**What does the regex `^(?!.*\bfoo\b).*$` ensure about the matched strings?**

- a. They must not contain "foo"
- b. They must contain "foo"
- c. They start with "foo"
- d. They end with "foo"

<v-click>

参考答案： `a`

解析： 整条表达式用负向前瞻排除了包含独立单词 `foo` 的字符串。

</v-click>
---

## Question 95



**Which regex matches a string if it starts with "http://" and does not have "www" immediately after?**

- a. `^http(?!://www\.)`
- b. `^http:\/\/(?!www\.)`
- c. `^http:\/\/(?!www).*`
- d. `^https?(?!://www\.)`

<v-click>

参考答案： `c`

解析： `^http://(?!www).*` 的思路最直接：以 `http://` 开头，且后面不是 `www`。`b` 只匹配开头部分，不是完整字符串匹配。

</v-click>

---

## Question 97



**What does the regex `\A(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\z` match?**

- a. An IPv6 address
- b. A MAC address
- c. An IPv4 address
- d. An email address

<v-click>

参考答案： `b`

解析： 六组两位十六进制加冒号分隔，是典型 MAC address。

</v-click>

---

## Question 99



**What does the regex `\d{2,}(?=\D*$)` match in "Item 23 is 42 years old"?**

- a. 2342
- b. 23
- c. No match
- d. 42

<v-click>

参考答案： `d`

解析： 正则要找的是“最后一个连续数字片段”，所以会匹配到句尾前的 `42`。

</v-click>

---

## Question 100



**What is a regular expression?**

- a. A way to calculate expressions in math
- b. A method for searching text in a document
- c. A sequence of characters that define a search pattern
- d. A programming language

<v-click>

参考答案： `c`

解析： regular expression 本质上就是定义搜索模式的一串字符。

</v-click>
---

## Question 102



**What does the regex `\b\d{1,3}(,\d{3})*\b` match?**

- a. A number formatted with commas (e.g., "1,000")
- b. A comma-separated list of numbers
- c. An IP address
- d. Any digit sequence without commas

<v-click>

参考答案： `a`

解析： 这个模式匹配像 `1,000`、`12,345,678` 这样的千分位数字格式。

</v-click>

---

## Question 106



**Given the string "hello123", what does the regex `(?<=\D)(?=\d)` locate?**

- a. The digit "1"
- b. The letter "o"
- c. The position between "o" and "1"
- d. The sequence "123"

<v-click>

参考答案： `c`

解析： 和 Q30 同义，定位的是 `o` 与 `1` 之间的位置。

</v-click>

---

## Question 112



**What does the regex `(?<!cat)dog` ensure?**

- a. "dog" is preceded by "cat"
- b. "dog" is not preceded by "cat"
- c. "dog" follows "cat"
- d. Both "cat" and "dog" are present

<v-click>

参考答案： `b`

解析： 负向后顾 `(?<!cat)` 要求 `dog` 前面不能是 `cat`。

</v-click>

---

## Question 113



**What would the regex `^(\w+)(\s+\1)+$` match?**

- a. A word repeated at least once, separated by whitespace
- b. Any number of repeated words without spaces
- c. A single word with trailing whitespace
- d. A line containing only whitespace

<v-click>

参考答案： `a`

解析： 这个表达式通过反向引用 `\1` 匹配“同一个词重复出现”。
```
hello hello
hello hello hello
test   test
abc abc abc abc
```
</v-click>

---

## Question 115



**Which character escapes special characters in regular expressions?**

- a. `^`
- b. `|`
- c. `\`
- d. `$`

<v-click>

参考答案： `c`

解析： 和 Q21 同义，转义特殊字符靠反斜杠。

</v-click>

---

## Question 117



**What is the function of the `?` quantifier?**

- a. Matches one or more occurrences
- b. Matches zero or more occurrences
- c. Matches zero or one occurrence
- d. Matches exactly one occurrence

<v-click>

参考答案： `c`

解析： `?` 表示前一项出现 0 次或 1 次。

</v-click>

---

## Question 141



**What does the `*` quantifier do in regular expressions?**

- a. Matches exactly one character
- b. Matches zero or more occurrences of the preceding element
- c. Matches one or more occurrences of the preceding element
- d. Matches zero or one occurrence of the preceding element

<v-click>

参考答案： `b`

解析： `*` 表示前一项出现 0 次或多次。

</v-click>

---

## Question 142



**What does `(?<=>)\d+(?=<\/?)` match in a string like `"<div>123</div>"`?**

- a. The entire string including the tags
- b. Any digits followed by "</"
- c. Any digits preceded by ">"
- d. 123, if it appears inside HTML tags

<v-click>

参考答案： `d`

解析： 这个模式会把 HTML 标签之间的数字内容 `123` 抠出来。
兼容（不使用 lookbehind）的等价重写`>(\d+)(?=<\/?)`
</v-click>

---

## Question 144



**Which regex captures text between double quotes, including escaped quotes within the text?**

- a. `"[^"]+"`
- b. `\\\"[\w\s]*\\\"`
- c. `"(.*?)"`
- d. `".*"`

<v-click>

参考答案： `d`

解析： 在给出的选项里，`"(.*?)"` 最接近“抓取双引号之间内容”的写法；但这题选项本身不够严谨。

</v-click>

---

## Question 146



**What would the regex `\b(?!\d+\b)\w+\b` exclude in its matches?**

- a. Words ending with a digit
- b. Words starting with a digit
- c. Words containing any digits
- d. Words entirely composed of digits

<v-click>

参考答案： `d`

解析： 负向前瞻 `(?!\d+\b)` 排除了“整个词就是纯数字”的情况。

</v-click>
---

## Question 147



**Which regex finds all instances of "not" that are not immediately followed by "good"?**

- a. `not(?!good)`
- b. `not(?=good)`
- c. `not(?! good)`
- d. `not(?= good)`

<v-click>

参考答案： `a`

解析： 和 Q54 同义，这里标准答案写成了带反引号的 `not(?!good)`。

</v-click>
---

## Question 148



**Which of the following is NOT a character set used in regular expressions?**

- a. \d
- b. [a-zA-Z]
- c. [0-9]
- d. {a-z}

<v-click>

参考答案： `d`

解析： `{a-z}` 不是字符集写法；字符集要用方括号。

</v-click>
---

## Question 150



**Which quantifier would match exactly 3 occurrences of the letter 'a'?**

- a. a3
- b. a{3}
- c. a[3]
- d. a(3)

<v-click>

参考答案： `b`

解析： 恰好 3 次要用 `{3}`，所以是 `a{3}`。

</v-click>
---

## Question 156



**How would you match any line that does not contain the exact phrase "regex"?**

- a. `^(?=.*\bregex\b).*$`
- b. `^(?!.*\bregex\b).*`
- c. `.*\bregex\- b.*`
- d. `^.*(regex).*`

<v-click>

参考答案： `b`

解析： 负向前瞻 `^(?!.*\bregex\b).*` 用来排除包含 `regex` 的整行。

</v-click>

---

## Question 157



**What will `(\b[a-zA-Z]{3}\b)\s+\1` match?**

- a. Any word repeated exactly once after one or more spaces
- b. A three-letter word followed by another three-letter word
- c. Any three-letter word repeated with one or more spaces in between
- d. A sequence of six letters with a space in the middle

<v-click>

参考答案： `c`

解析： 这里要求“三个字母的单词重复出现”，且中间有空格。

</v-click>

---

### Week 4 (41 题)

- 范围：EDA & Pre-processing + Week 4 parsing + mock quiz text pre-processing block

## Question 2



**What challenges are presented by textual content in EDA for character and text data? (Select all that apply)**

- a. Variability in text formats
- b. Data sparsity
- c. Ambiguity in language
- d. High dimensionality
e. High computational costs

<v-click>

参考答案： `a, b, c, d, e`

解析： 正确项是 `a`: Variability in text formats, `b`: Data sparsity, `c`: Ambiguity in language, `d`: High dimensionality, `e`: High computational costs。这些选项共同对应课程里的正确定义。

</v-click>
---

## Question 4



**What factors influence the choice of data pre-processing techniques? (Select all that apply)**

- a. Algorithm requirements
- b. Data quantity
- c. Data integrity
- d. Visualisation needs
e. Data type

<v-click>

参考答案： `a, b, c, d, e`

解析： 正确项是 `a`: Algorithm requirements, `b`: Data quantity, `c`: Data integrity, `d`: Visualisation needs, `e`: Data type。这些选项共同对应课程里的正确定义。

</v-click>
---

## Question 5



**What measures of central tendency are commonly used in EDA for numerical data? (Select all that apply)**

- a. Median
- b. Variance
- c. Mode
- d. Standard Deviation
e. Mean

<v-click>

参考答案： `a, c, e`

解析： 中心趋势看的是数据“中心”在哪里，常见是 mean / median / mode；variance 和 standard deviation 属于离散程度。

</v-click>
---

## Question 16



**Which method is used to get a summary of a DataFrame's structure and column types?**

- a. `df.info()`
- b. `df.describe()`
- c. `df.overview()`
- d. `df.summary()`

<v-click>

参考答案： `a`

解析： `df.info()` 会给出列名、非空数、dtype 等结构信息；`describe()` 更偏统计摘要。

</v-click>

---

## Question 23



**For what reasons might case normalisation not always be needed in text data pre-processing? (Select all that apply)**

- a. To maintain the original meaning of words
- b. In information retrieval tasks
- c. For graphical data representation
- d. When performing named entity recognition
e. In audio data processing

<v-click>

参考答案： `a, b, d`

解析： case normalisation 并不总是必须；像 named entity recognition 或需要保留原大小写信息时，大小写本身就有语义。

</v-click>
---

## Question 24



**For what reasons might case normalisation not always be needed in text data pre-processing? (Select all that apply)**

- a. To maintain the original meaning of words
- b. In information retrieval tasks
- c. For graphical data representation
- d. When performing named entity recognition
e. In audio data processing

<v-click>

参考答案： `a, b, d`

解析： 这题和 Q23 同义，核心也是“某些任务里大小写信息本身有用，所以不一定统一转小写”。

</v-click>
---

## Question 25



**The process that simplifies text by converting it to its base form is called:**

- a. Case normalization
- b. One-hot encoding
- c. Tokenisation
- d. Lemmatisation

<v-click>

参考答案： `d`

解析： 把词还原成词典中的基本形式是 lemmatisation。

</v-click>
---

## Question 27



**Why is understanding the structure of language (syntax) important in EDA for character and text data? (Select all that apply)**

- a. It is crucial for visual data representation
- b. It supports the understanding of grammar rules
- c. It assists in analysing sentence structure
- d. It aids in constructing well-formed sentences and paragraphs
e. It helps in hardware optimisation

<v-click>

参考答案： `b, c, d`

解析： syntax 关注语言结构与语法规则，有助于分析句子结构并生成/识别 well-formed text。

</v-click>
---

## Question 28



**Which Pandas function is used to read a CSV file?**

- a. `pd.read_csv()`
- b. `pd.to_csv()`
- c. `pd.read_excel()`
- d. `pd.load_csv()`

<v-click>

参考答案： `a`

解析： 读取 CSV 用 `pd.read_csv()`。

</v-click>

---

## Question 32



**Which parameter in `pd.read_csv()` specifies the delimiter?**

- a. `delim`
- b. `split`
- c. `delimiter`
- d. `sep`

<v-click>

参考答案： `d`

解析： `pd.read_csv()` 指定分隔符最常用的是 `sep`。

</v-click>
---

## Question 35



**What does 'Character Data' consist of?**

- a. Sequences of characters
- b. Single alphabetic letters, symbols, or numerals
- c. Quantifiable information
- d. Binary data

<v-click>

参考答案： `b`

解析： character data 指单个字符层面的数据，如字母、数字、符号。

</v-click>
---

## Question 37



**Which technique is used to handle categorical data by creating a binary column for each category?**

- a. One-hot Encoding
- b. Label Encoding
- c. Normalisation
- d. Vectorisation

<v-click>

参考答案： `a`

解析： 为每个类别开一列 0/1 特征，就是 one-hot encoding。

</v-click>
---

## Question 40



**In the context of text data pre-processing, what is the purpose of case normalisation?**

- a. To differentiate between common nouns and proper nouns
- b. To convert all the words into either uppercase or lowercase
- c. To increase the complexity of the text
- d. To identify and correct grammatical errors

<v-click>

参考答案： `b`

解析： case normalisation 就是把文本统一成大写或小写，减少同词不同写法带来的碎片化。

</v-click>
---

## Question 42



**Exploratory Data Analysis (EDA) is used for:**

- a. Finalizing data collection methods
- b. Reducing the volume of data
- c. Uncovering patterns, trends, and anomalies
- d. Reducing the volume of data

<v-click>

参考答案： `c`

解析： EDA 的目标是发现模式、趋势和异常，不是定稿数据采集方案。

</v-click>
---

## Question 55



**Why is it important to remove stop words in text data pre-processing? (Select all that apply)**

- a. To highlight more meaningful words in text analysis
- b. To prevent skew in analysis results
- c. To add more complexity to the model
- d. To increase data set size
e. To reduce computational load

<v-click>

参考答案： `a, b, e`

解析： 去停用词是为了突出更有信息量的词、减少噪声并降低计算负担。

</v-click>
---

## Question 57



**To read an Excel file into a DataFrame, which function is used?**

- a. `pd.load_excel()`
- b. `pd.read_excel()`
- c. `pd.read_csv()`
- d. `pd.import_excel()`

<v-click>

参考答案： `b`

解析： 读取 Excel 文件用 `pd.read_excel()`。

</v-click>
---

## Question 63



**How do you set a DataFrame's column 'ID' as its index?**

- a. `df.index = 'ID'`
- b. `df.set_index('ID')`
- c. `df.set('ID')`
- d. `df.index_col('ID')`

<v-click>

参考答案： `b`

解析： 把某列设成索引常用 `df.set_index("ID")`。

</v-click>
---

## Question 66



**What does the pd.read_json() function do?**

- a. Converts a DataFrame to a JSON object
- b. Writes data to a JSON file
- c. Reads data from a JSON file into a DataFrame
- d. Parses JSON data into a list

<v-click>

参考答案： `c`

解析： `pd.read_json()` 会把 JSON 读进 DataFrame。

</v-click>
---

## Question 71



**Which techniques are essential for handling numerical data in EDA? (Select all that apply)**

- a. Descriptive statistics
- b. Encoding
- c. Tokenisation
- d. Vectorisation
e. Normalisation

<v-click>

参考答案： `a, e`

解析： 数值型 EDA 常用 descriptive statistics，也可能做 normalisation；encoding / tokenisation / vectorisation 不是数值数据核心方法。

</v-click>
---

## Question 75



**Which parameter in read_csv() is used to specify which rows should be used as header?**

- a. `top_row`
- b. `head_row`
- c. `header`
- d. `usecols`

<v-click>

参考答案： `c`

解析： `header` 参数决定哪一行当列名。

</v-click>

---

## Question 77



**What does the `skiprows=3` parameter in `pd.read_csv()` do?**
**For example, `df = pd.read_csv('dat- a.csv', skiprow = 3)`**

- a. Skips any three rows randomly
- b. Skips first three columns from the left of the file
- c. Skips last three rows at the end of the file
- d. Skips first three rows from the beginning of the file

<v-click>

参考答案： `d`

解析： `skiprows=3` 表示从文件开头跳过前三行。

</v-click>
---

## Question 81



**What is the middle value after all values are ordered in a data set called?**

- a. Mean
- b. Mode
- c. Variance
- d. Median

<v-click>

参考答案： `d`

解析： 有序数据中间那个值叫 median。

</v-click>
---

## Question 88



**Which of the following is crucial for preparing text for NLP tasks?**

- a. Variance Calculation
- b. Tokenization
- c. Normalization
- d. Image Encoding

<v-click>

参考答案： `b`

解析： NLP 的第一步通常是 tokenization。

</v-click>
---

## Question 90



**Which measure of central tendency is the arithmetic average of a set of values?**

- a. Median
- b. Mode
- c. Mean
- d. Range

<v-click>

参考答案： `c`

解析： 算术平均数就是 mean。

</v-click>
---

## Question 96



**For what reasons might case normalisation not always be needed in text data pre-processing? (Select all that apply)**

- a. In information retrieval tasks
- b. In audio data processing
- c. For graphical data representation
- d. When performing named entity recognition
e. To maintain the original meaning of words

<v-click>

参考答案： `a, d, e`

解析： 和 Q23/Q24 同理，IR、NER、保留原义等场景不一定要统一大小写。

</v-click>
---

## Question 105



**Which technique is used to handle categorical data by creating a binary column for each category?**

- a. Label Encoding
- b. Vectorisation
- c. One-hot Encoding
- d. Normalisation

<v-click>

参考答案： `c`

解析： 和 Q37 同义，这里正确项是顺序不同后的 one-hot encoding。

</v-click>
---

## Question 110



**Which data types are primarily analysed during EDA? (Select all that apply)**

- a. Audio Data
- b. Categorical Data
- c. Numerical Data
- d. Text Data
e. Image Data

<v-click>

参考答案： `b, c, d`

解析： 课程中的 EDA 主要看 categorical、numerical、text 三类。

</v-click>
---

## Question 111



**Which steps are involved in Lemmatisation for text data pre-processing? (Select all that apply)**

- a. Reduction of words to their stems
- b. Application of morphological analysis
- c. Conversion of words to their base or dictionary form
- d. Use of part-of-speech tags
e. Use of context surrounding the words

<v-click>

参考答案： `b, c, d, e`

解析： lemmatisation 依赖词形分析、词性和上下文，把词还原成 dictionary form；“stem” 不是它的核心定义。

</v-click>
---

## Question 120



**Which method is used to get a summary of a DataFrame's structure and column types?**

- a. `df.overview()`
- b. `df.summary()`
- c. `df.describe()`
- d. `df.info()`

<v-click>

参考答案： `d`

解析： 和 Q16 同义，结构摘要用 `df.info()`。

</v-click>

---

## Question 122



**Which parameter in pd.read_csv() specifies the delimiter?**

- a. `sep`
- b. `delim`
- c. `delimiter`
- d. `split`

<v-click>

参考答案： `a`

解析： 和 Q32 同义，这里正确项换成了 `sep`。

</v-click>

---

## Question 123



**What is the aim of using Descriptive Statistics in EDA for Numerical Data?**

- a. To manipulate the dataset
- b. To encode textual information into numerical values
- c. To provide insights into the central tendency, dispersion, and distribution shape
- d. To visualize data in 3D

<v-click>

参考答案： `c`

解析： descriptive statistics 的目标是概括中心位置、离散程度和分布形态。

</v-click>
---

## Question 124



**What does continuous data represent?**

- a. Visual information encoded digitally
- b. Quantifiable information that can be divided infinitely
- c. Single alphabetic letters or symbols
- d. Countable values or categories

<v-click>

参考答案： `b`

解析： continuous data 是可以无限细分的可量化数值。

</v-click>
---

## Question 131



**Exploratory Data Analysis (EDA) is used for:**

- a. Reducing the volume of data
- b. Uncovering patterns, trends, and anomalies
- c. Reducing the volume of data
- d. Finalizing data collection methods

<v-click>

参考答案： `b`

解析： 和 Q42 同义，EDA 用来发现 patterns / trends / anomalies。

</v-click>
---

## Question 135



**Which data visualisation method is primarily used for numerical data to understand its spread and central tendency?**

- a. Pie Charts
- b. Histograms
- c. Mind Maps
- d. Flowcharts

<v-click>

参考答案： `b`

解析： 看数值分布与中心位置最常用 histogram。

</v-click>
---

## Question 145



**Which of the following are benefits of correctly identifying data types during EDA? (Select that all apply)**

- a. Guides data cleaning and preprocessing
- b. Enables effective visualisation
- c. Determines the color scheme of visualisations
- d. Assists in feature engineering
e. Allows for appropriate analysis

<v-click>

参考答案： `a, b, d, e`

解析： 正确识别数据类型能指导清洗、可视化、特征工程和后续分析。

</v-click>
---

## Question 149



**What challenges are presented by textual content in EDA for character and text data? (Select all that apply)**

- a. Variability in text formats
- b. Data sparsity
- c. Ambiguity in language
- d. High dimensionality
e. High computational costs

<v-click>

参考答案： `a, b, c, d, e`

解析： 和 Q2 同义，文本常见难点包括格式多变、稀疏、高维、歧义和计算成本。

</v-click>
---

## Question 151



**What are the steps involved in Count Vectorisation? (Select all that apply)**

- a. Vocabulary Building
- b. Normalisation
- c. Count Calculation
- d. Encoding
e. Tokenisation

<v-click>

参考答案： `a, c, e`

解析： count vectorisation 通常先 tokenise、建立词表，再统计每个词出现次数。

</v-click>
---

## Question 153



**Which of the following are goals of Exploratory Data Analysis (EDA)? (Select all that apply)**

- a. To understand the patterns, anomalies, and relationships in the data
- b. To explore and summarise the main characteristics of the data visually
- c. To use statistical graphics, plots, and information tables
- d. To perform complex predictive modeling
e. To manipulate the data set

<v-click>

参考答案： `a, b, c`

解析： EDA 目标是理解数据并做可视化总结，不是直接做复杂预测建模。

</v-click>
---

## Question 158



**For what reasons might case normalisation not always be needed in text data pre-processing? (Select all that apply)**

- a. In information retrieval tasks
- b. When performing named entity recognition
- c. For graphical data representation
- d. In audio data processing
e. To maintain the original meaning of words

<v-click>

参考答案： `a, b, e`

解析： 和 Q23/Q24/Q96 同理，IR、NER、保留原始含义时不一定要大小写归一化。

</v-click>
---

## Question 163



**What is the aim of using Descriptive Statistics in EDA for Numerical Data?**

- a. To provide insights into the central tendency, dispersion, and distribution shape
- b. To visualize data in 3D
- c. To encode textual information into numerical values
- d. To manipulate the dataset

<v-click>

参考答案： `a`

解析： 和 Q123 同义，这里正确项换成了 `a`。

</v-click>
---

## Question 164



**What is the significance of identifying data types during EDA?**

- a. It changes the textual content into images
- b. It influences how data will be processed and analyzed
- c. It is only important for numerical data
- d. It determines the type of cake to bake

<v-click>

参考答案： `b`

解析： 识别数据类型会直接影响后续怎么处理和分析数据。

</v-click>
---

### Week 5 (25 题)

- 范围：Data Discovery & Collection

## Question 10



**What aspects does Data Cataloging and Metadata Management cover? (Select all that apply)**

- a. Usage metadata
- b. Data anonymisation
- c. Metadata collection
- d. Data lineage documentation
e. Catalog creation

<v-click>

参考答案： `a, c, d, e`

解析： cataloging / metadata management 关注 metadata collection、lineage、catalog 本身，也会包含 usage metadata；anonymisation 属于隐私保护，不是 cataloging 核心内容。

</v-click>
---

## Question 31



**Qualitative Data is:**

- a. Exclusively about quantities
- b. Only numerical
- c. Descriptive and conceptual
- d. Limited to structured research instruments

<v-click>

参考答案： `c`

解析： qualitative data 强调描述性、概念性，不是纯数量。

</v-click>
---

## Question 44



**Data Cataloging aids in:**

- a. Making it harder to find and understand data
- b. Ignoring data lineage
- c. Decreasing data accessibility
- d. Creating a searchable catalog of data assets

<v-click>

参考答案： `d`

解析： data catalog 的作用是让数据资产可搜索、可理解、可发现。

</v-click>
---

## Question 49



**Which is NOT a method of collecting structured data?**

- a. Relational databases
- b. Online forms
- c. Surveys and questionnaires
- d. Text mining and NLP

<v-click>

参考答案： `d`

解析： text mining / NLP 主要处理非结构化文本，不属于 structured data collection 方法。

</v-click>
---

## Question 50



**Which of the following is NOT a part of the Data Discovery Process?**

- a. Data Cataloging and Metadata Management
- b. Data Exploration and Visualization
- c. Data Encryption
- d. Data Integration and Consolidation

<v-click>

参考答案： `c`

解析： data encryption 属于安全控制，不是 data discovery 流程本身。

</v-click>
---

## Question 68



**Factors to consider during the data collection phase include: (Select all that apply)**

- a. Collection method efficiency
- b. Source reliability
- c. Data format
- d. Cost of data storage physical locations

<v-click>

参考答案： `a, b, c`

解析： collection 阶段常看方法效率、来源可靠性、数据格式；“physical locations” 不是这里的核心。

</v-click>
---

## Question 72



**Which are considered primary sources of data? (Select all that apply)**

- a. Observations
- b. Experiments
- c. Industry reports
- d. Surveys
e. Government publications

<v-click>

参考答案： `a, b, d`

解析： primary source 是直接采集的数据，如 observations、experiments、surveys；industry reports / government publications 更像二手资料。

</v-click>
---

## Question 84



**Which is NOT a method of collecting structured data?**

- a. Surveys and questionnaires
- b. Online forms
- c. Relational databases
- d. Text mining and NLP

<v-click>

参考答案： `d`

解析： 和 Q49 同理，text mining / NLP 不是 structured collection method。

</v-click>
---

## Question 85



**Which phase comes immediately after data discovery?**

- a. Data storage
- b. Data collection
- c. Data cleaning
- d. Data analysis

<v-click>

参考答案： `b`

解析： discovery 后面紧接着就是 collection。

</v-click>
---

## Question 89



**Data Security measures are essential for:**

- a. Ensuring data is openly accessible
- b. Secure storage and transmission of data
- c. Reducing data quality
- d. Encouraging unauthorized data access

<v-click>

参考答案： `b`

解析： data security 关注安全存储与传输，不是开放访问。

</v-click>
---

## Question 91



**Data Cataloging aids in:**

- a. Creating a searchable catalog of data assets
- b. Ignoring data lineage
- c. Making it harder to find and understand data
- d. Decreasing data accessibility

<v-click>

参考答案： `a`

解析： 这题和 Q44 同义，catalog 的目的就是形成可搜索的数据资产目录。

</v-click>
---

## Question 98



**What roles does data play in decision-making? (Select all that apply)**

- a. Crisis prediction and response
- b. Compliance monitoring
- c. Understanding customer behaviour
- d. Enhancing product quality
e. Operational efficiency

<v-click>

参考答案： `a, b, c, d, e`

解析： 数据在决策里能支持风险、合规、客户洞察、产品和运营优化，所以五项都对。

</v-click>
---

## Question 107



**Ethical considerations in Data Collection include: (Select all that apply)**

- a. Privacy and anonymity
- b. Informed consent
- c. Data retention and disposal
- d. Data beautification
e. Compliance with laws and regulations

<v-click>

参考答案： `a, b, c, e`

解析： 伦理采集通常包括隐私、知情同意、保留/销毁规范和法律合规。

</v-click>
---

## Question 127



**Qualitative Data is:**

- a. Descriptive and conceptual
- b. Only numerical
- c. Limited to structured research instruments
- d. Exclusively about quantities

<v-click>

参考答案： `a`

解析： 和 Q31 同义，qualitative data 是描述性/概念性数据。

</v-click>
---

## Question 128



**The main advantage of using existing data is:**

- a. Always perfectly matching specific needs
- b. Time efficiency and cost reduction
- c. Increased costs
- d. Reduced access to diverse data

<v-click>

参考答案： `b`

解析： existing data 的主要优势通常是省时省钱。

</v-click>
---

## Question 132



**Metadata in Data Cataloging includes:**

- a. Only structural metadata
- b. Descriptive, Structural, and Technical Metadata
- c. Only usage metadata
- d. Only descriptive metadata

<v-click>

参考答案： `b`

解析： metadata 不只是一种类型，常见有 descriptive、structural、technical 等。

</v-click>
---

## Question 133



**What role does data play in modern business decision-making?**

- a. It is not significant in decision-making
- b. It is exclusively used for financial analysis
- c. It is only used for data storage
- d. It aids in understanding customer behavior and evidence-based strategic planning

<v-click>

参考答案： `d`

解析： 现代业务决策里，数据能支持客户理解和基于证据的规划。

</v-click>
---

## Question 134



**Metadata Collection is critical for understanding:**

- a. Only the data's numerical value
- b. Restricting data access
- c. How to delete the data
- d. The data's origin, format, and characteristics

<v-click>

参考答案： `d`

解析： metadata collection 帮助理解数据从哪来、什么格式、有哪些特征。

</v-click>
---

## Question 136



**Ensuring data privacy and security is crucial due to:**

- a. Regulations
- b. Lack of regulations
- c. Unimportance of data sensitivity
- d. The ease of data handling

<v-click>

参考答案： `a`

解析： 隐私和安全之所以重要，一个直接原因就是法规要求。

</v-click>
---

## Question 137



**Which of the following is NOT a part of the Data Discovery Process?**

- a. Data Cataloging and Metadata Management
- b. Data Encryption
- c. Data Exploration and Visualization
- d. Data Integration and Consolidation

<v-click>

参考答案： `b`

解析： 这题和 Q50 同义，只是正确项换成了 `b`。

</v-click>
---

## Question 139



**Text Mining and Natural Language Processing (NLP) are methods for collecting:**

- a. Structured data
- b. Numerical data only
- c. Semi-structured data
- d. Unstructured data

<v-click>

参考答案： `d`

解析： text mining / NLP 处理的是 unstructured text。

</v-click>
---

## Question 154



**What are the roles of Data in modern business decision-making? (Select all that apply)**

- a. Risk Management
- b. Enhancing product quality
- c. Compliance monitoring
- d. Understanding customer behaviour
e. Performance Optimisation

<v-click>

参考答案： `a, b, c, d, e`

解析： 这题列出的 risk、quality、compliance、customer、performance 都是数据支撑决策的典型作用。

</v-click>
---

## Question 159



**Data Security measures are essential for:**

- a. Encouraging unauthorized data access
- b. Reducing data quality
- c. Ensuring data is openly accessible
- d. Secure storage and transmission of data

<v-click>

参考答案： `d`

解析： 和 Q89 同义，正确项换成了 `d`。

</v-click>
---

## Question 161



**Data Privacy measures are intended to:**

- a. Expose sensitive information
- b. Increase data accessibility to the public
- c. Limit the use of data for analysis
- d. Protect sensitive information in compliance with regulations

<v-click>

参考答案： `d`

解析： privacy measures 的目标是依法保护敏感信息，而不是公开它。

</v-click>
---

## Question 162



**Metadata Collection is critical for understanding:**

- a. Only the data's numerical value
- b. How to delete the data
- c. Restricting data access
- d. The data's origin, format, and characteristics

<v-click>

参考答案： `d`

解析： 和 Q134 同义，metadata 帮你理解 origin / format / characteristics。


</v-click>
---

### Week 6 (5 题)

- 范围：Data Structuring

## Question 38



**Graph data models are ideal for:**

- a. Representing relationships between entities
- b. Ignoring entity relationships
- c. Simple numerical analysis
- d. Storing textual data only

<v-click>

参考答案： `a`

解析： graph data model 最适合表达实体之间的关系。

</v-click>
---

## Question 51



**What does Structured Data refer to?**

- a. Data that is organized and easily understandable by machine language
- b. Multimedia data
- c. Social media content
- d. Data that is disorganized and random

<v-click>

参考答案： `a`

解析： structured data 是机器容易理解、字段组织清晰的数据。

</v-click>
---

## Question 60



**Data Profiling and Assessment involve understanding which types of data structure? (Select all that apply)**

- a. Big data
- b. Time-series data
- c. Structured data
- d. Unstructured data
e. Graph data

<v-click>

参考答案： `b, c, d, e`

解析： profiling / assessment 需要先看数据是什么结构，因此 time-series、structured、unstructured、graph 都要识别。

</v-click>
---

## Question 65



**Which data structures are essential for Data Discovery and Collection? (Select all that apply)**

- a. Relational databases
- b. Multimedia data
- c. Graph data models
- d. Time-series data
e. Data warehouses

<v-click>

参考答案： `a, b, c, d, e`

解析： 这题把“数据结构”和“数据来源/类型”混在一起了；按课程复习时先把这几类都记住。

</v-click>
---

## Question 140



**Time-series data is indexed in:**

- a. Time order
- b. Random order
- c. Hierarchical order
- d. Alphabetical order

<v-click>

参考答案： `a`

解析： time-series 数据按时间顺序索引。
</v-click>
---
