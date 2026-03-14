---
theme: apple-basic
title: FIT5196 Quiz 1 真题解析
layout: intro
transition: slide-left
mdc: true
---

# FIT5196 Quiz 1

## Week 1-6 真题解析

---
layout: default
---

# 使用方式

- 先只看题目和选项，自己判断。
- 按一次空格，看思路提示。
- 再按一次空格，看参考答案。
- 最后看解析，确认自己错在概念、关键词还是干扰项。

<div class="mt-6 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
这份 deck 选的是高频和高价值真题，不是把 164 题全部铺进 slides。
</div>

---
layout: default
---

# 这份 deck 讲什么

| Week | 主题 | 重点 |
|------|------|------|
| 1 | Notebook / Markdown | 基础格式题 |
| 2 | Data Wrangling Process & Tasks | 目标、流程、validation、integration |
| 3 | Regular Expressions | anchors、groups、lookarounds |
| 4 | EDA & Pre-processing | numerical / text / parsing |
| 5 | Data Discovery & Collection | sources、ethics、metadata |
| 6 | Data Structuring | structured / graph / time-series |

---
layout: section
---

# Week 1

Notebook / Markdown 基础

---
layout: default
---

# Q1 Markdown Italic

**How do you make text italic in Markdown?**  
`Select all that apply`

- a. Surround the text with `**`
- b. Surround the text with `~~`
- c. Surround the text with `_`
- d. Surround the text with `*`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：先排除粗体和删除线，再保留斜体的两种常见写法。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c, d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：Markdown 斜体常见写法是 <code>*text*</code> 或 <code>_text_</code>。<code>**</code> 是粗体，<code>~~</code> 是删除线。
</div>

---
layout: default
---

# Q20 Markdown Bold

**To emphasise text with bold in Markdown, you can use:**

- a. Double tildes or double dollar signs
- b. Double asterisks or double underscores
- c. Single asterisks or single underscores
- d. Triple asterisks or triple underscores

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：单星号是斜体，双星号/双下划线才是粗体。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`b`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：粗体的标准写法是 <code>**text**</code> 或 <code>__text__</code>。
</div>

---
layout: section
---

# Week 2

Data Wrangling Process & Tasks

---
layout: default
---

# Q82 Primary Purpose

**What is the primary purpose of Data Wrangling?**

- a. To analyze complex data types
- b. To ensure data privacy
- c. To acquire, clean, structure, and enrich raw data for analysis
- d. To visualize data trends

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：题干问的是 <code>primary purpose</code>，要选最完整、最定义式的表达。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：privacy、visualization、complex data analysis 都可能相关，但不是 data wrangling 的完整定义。课上最核心的定义就是把 raw data 整理成可分析数据。
</div>

---
layout: default
---

# Q59 Common Goals

**Which of the following are common goals of data wrangling?**  
`Select all that apply`

- a. Increasing data complexity
- b. Ignoring data inconsistencies
- c. Improving data quality
- d. Facilitating easier access to data

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：看到 <code>goals</code>，先排除反向干扰项。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c, d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：data wrangling 的目标包括提高质量、简化访问、促进整合、降低复杂度。a 和 b 都是在故意反着说。
</div>

---
layout: default
---

# Q48 Validation Goal

**Which of the following is NOT a goal of data validation?**

- a. Verify data is in the expected format
- b. Validate range and constraints
- c. Ensure data accurately reflects real-world entities
- d. Enhance the speed of data retrieval

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：validation 看的是格式、范围、逻辑、一致性，不是性能优化。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：retrieval speed 属于系统/存储性能问题，不是 validation 的核心目标。
</div>

---
layout: default
---

# Q103 Select Column

**How do you select a single column named 'Age' from a DataFrame df?**  
`Select all that apply`

- a. `df['Age']`
- b. `df.select('Age')`
- c. `df.index('Age')`
- d. `df.Age`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：Pandas 选单列最常见有方括号和属性访问两种。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a, d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：<code>df['Age']</code> 是最稳妥的标准写法；<code>df.Age</code> 在列名合法时也能用。b 和 c 不是这里的 Pandas API。
</div>

---
layout: default
---

# Q118 Vertical Concatenation

**Which function is used to concatenate two DataFrames vertically?**

- a. `pd.concat()`
- b. `pd.join()`
- c. `pd.merge()`
- d. `pd.append()`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：vertical stack 看的是 concat，不是 join / merge。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：<code>pd.concat()</code> 用来按行或按列拼接；题目问 vertically，就是按行堆叠。
</div>

---
layout: section
---

# Week 3

Regular Expressions

---
layout: default
---

# Q3 IPv4 Regex

**For matching IPv4 addresses, which regex is accurate and avoids matching numbers beyond 0-255?**

- a. `\b(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\.(0-255){1,3}\b`
- b. `[0-9]{1,3}\.([0-9]{1,3}){3}`
- c. `\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b`
- d. `\b(\d{1,3}\.){3}\d{1,3}\b`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：只限制“1 到 3 位数字”不够，还要限制每段数值范围。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：只有 c 对每个 octet 都做了 0-255 的精确约束；b 和 d 会错误接受像 999 这样的值。
</div>

---
layout: default
---

# Q54 Negative Lookahead

**Which regex finds all instances of "not" that are not immediately followed by "good"?**

- a. `not(?! good)`
- b. `not(?= good)`
- c. `not(?=good)`
- d. `not(?!good)`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：关键词是 <code>not immediately followed by</code>，所以要用 negative lookahead。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：<code>(?!good)</code> 表示后面不能立刻出现 <code>good</code>。如果带空格，就不是“immediately”了。
</div>

---
layout: default
---

# Q95 Start with http:// but no www

**Which regex matches a string if it starts with "http://" and does not have "www" immediately after?**

- a. `^http(?!://www\.)`
- b. `^http:\/\/(?!www\.)`
- c. `^http:\/\/(?!www).*`
- d. `^https?(?!://www\.)`

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：最直观的结构应该是 <code>^http://</code> 开头，然后立刻检查后面不是 <code>www</code>。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：c 的结构最完整，既固定前缀，又排除了紧随其后的 <code>www</code>。b 也常被看作可接受写法，这题本身有一点出题歧义。
</div>

---
layout: default
---

# Q113 Backreference

**What would the regex `^(\w+)(\s+\1)+$` match?**

- a. A word repeated at least once, separated by whitespace
- b. Any number of repeated words without spaces
- c. A single word with trailing whitespace
- d. A line containing only whitespace

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：看见 <code>\1</code> 就要想到 backreference，表示“和前面捕获的一样”。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：这个模式先捕获一个单词，再要求后面出现“空白 + 同一个单词”的重复结构。
</div>

---
layout: section
---

# Week 4

EDA & Pre-processing

---
layout: default
---

# Q42 EDA Purpose

**Exploratory Data Analysis (EDA) is used for:**

- a. Finalizing data collection methods
- b. Reducing the volume of data
- c. Uncovering patterns, trends, and anomalies
- d. Reducing the volume of data

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：EDA 的关键词是 explore / understand / uncover，不是 finalize 或 reduce。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：EDA 用来发现数据中的模式、趋势、异常和关系，为后续分析做准备。
</div>

---
layout: default
---

# Q71 Numerical EDA Techniques

**Which techniques are essential for handling numerical data in EDA?**  
`Select all that apply`

- a. Descriptive statistics
- b. Encoding
- c. Tokenisation
- d. Vectorisation
- e. Normalisation

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：区分 numerical data 和 text data 的常用方法。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a, e`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：descriptive statistics 用来概括数值分布；normalisation 是常见数值预处理。tokenisation / vectorisation 更偏文本。
</div>

---
layout: default
---

# Q111 Lemmatisation

**Which steps are involved in Lemmatisation for text data pre-processing?**  
`Select all that apply`

- a. Reduction of words to their stems
- b. Application of morphological analysis
- c. Conversion of words to their base or dictionary form
- d. Use of part-of-speech tags
- e. Use of context surrounding the words

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：lemmatisation 比 stemming 更“懂语义”，会借助词性和上下文。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`b, c, d, e`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：a 更接近 stemming。lemmatisation 强调把词还原成 dictionary form，并利用 morphology、POS 和 context。
</div>

---
layout: default
---

# Q151 Count Vectorisation

**What are the steps involved in Count Vectorisation?**  
`Select all that apply`

- a. Vocabulary Building
- b. Normalisation
- c. Count Calculation
- d. Encoding
- e. Tokenisation

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：count vectorisation 先切词，再建词表，再统计每个词出现次数。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a, c, e`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：tokenisation 是输入切分，vocabulary building 是确定特征空间，count calculation 是生成向量。normalisation 不是 count vectorisation 的必经步骤。
</div>

---
layout: section
---

# Week 5

Data Discovery & Collection

---
layout: default
---

# Q50 Discovery Process

**Which of the following is NOT a part of the Data Discovery Process?**

- a. Data Cataloging and Metadata Management
- b. Data Exploration and Visualization
- c. Data Encryption
- d. Data Integration and Consolidation

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：discovery 看的是“找到并理解数据”，不是安全防护动作。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`c`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：encryption 属于安全与隐私保护，不属于 discovery process 本身。
</div>

---
layout: default
---

# Q72 Primary Sources

**Which are considered primary sources of data?**  
`Select all that apply`

- a. Observations
- b. Experiments
- c. Industry reports
- d. Surveys
- e. Government publications

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：primary = 你直接采来的；secondary = 别人已经整理好的。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a, b, d`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：observations、experiments、surveys 都是直接采集。industry reports 和 government publications 通常作为二手数据使用。
</div>

---
layout: default
---

# Q107 Ethics in Collection

**Ethical considerations in Data Collection include:**  
`Select all that apply`

- a. Privacy and anonymity
- b. Informed consent
- c. Data retention and disposal
- d. Data beautification
- e. Compliance with laws and regulations

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：伦理题通常围绕 privacy、consent、compliance，不会围绕“美化数据”。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a, b, c, e`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：d 是明显干扰项。真实的数据伦理问题是你能不能合法、透明、负责任地采、存、用和删数据。
</div>

---
layout: default
---

# Q132 Metadata Types

**Metadata in Data Cataloging includes:**

- a. Only structural metadata
- b. Descriptive, Structural, and Technical Metadata
- c. Only usage metadata
- d. Only descriptive metadata

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：cataloging 不会只看单一一种 metadata。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`b`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：课程里 metadata 至少要能帮助我们理解数据的意义、结构和技术属性，所以不会只有一种类型。
</div>

---
layout: section
---

# Week 6

Data Structuring

---
layout: default
---

# Q51 Structured Data

**What does Structured Data refer to?**

- a. Data that is organized and easily understandable by machine language
- b. Multimedia data
- c. Social media content
- d. Data that is disorganized and random

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：structured 的关键词是 schema 清晰、字段明确、机器易处理。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：structured data 的重点是组织良好、格式明确，比如关系型表结构。
</div>

---
layout: default
---

# Q38 Graph Data Models

**Graph data models are ideal for:**

- a. Representing relationships between entities
- b. Ignoring entity relationships
- c. Simple numerical analysis
- d. Storing textual data only

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：graph 的核心不是“值”，而是“连接关系”。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：graph 特别适合描述 people-network、route、knowledge graph 这种实体之间的联系。
</div>

---
layout: default
---

# Q140 Time-series

**Time-series data is indexed in:**

- a. Time order
- b. Random order
- c. Hierarchical order
- d. Alphabetical order

<div v-click class="mt-5 rounded-xl border border-main/20 bg-main/5 px-4 py-3 text-sm">
思路：time-series 的本质就是“按时间排列的观测值”。
</div>

<div v-click class="mt-4 rounded-xl border border-green-500/30 bg-green-500/10 px-4 py-3">
答案：`a`
</div>

<div v-click class="mt-4 text-sm leading-6">
解析：没有时间顺序，就谈不上 time-series 的趋势、季节性和时序依赖。
</div>

---
layout: default
---

# 最后怎么复习更高效

<v-clicks>

- 先背 Week 2：定义、目标、流程、validation / integration 这些最容易反复出现。
- 再刷 Week 3：regex 是高密度考点，尤其是 anchor、quantifier、lookaround。
- Week 4 抓“方法和数据类型”的对应关系。
- Week 5 抓 discovery / collection / metadata / ethics 的边界。
- Week 6 重点记 structured / graph / time-series 的定义和场景。

</v-clicks>

---
layout: end
---

# Deck Ready

`slides/fit5196-quiz1-real-quiz.md`

按空格即可渐进式披露答案和解析
