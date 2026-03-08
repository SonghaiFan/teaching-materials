---
theme: apple-basic
title: FIT5196 - Week 1-2 辅导
layout: intro
---

# FIT5196 Data Wrangling

## Week 1-2 补习班

<!--
这两周是整门课的起点。
今天的目标不是把所有细节一次讲完，而是先把课程结构、数据整理的主线流程、以及 applied session 里最容易考的基础操作打牢。
如果你们这两周能跟上，后面 regex、EDA、cleaning 那些内容会顺很多。
-->

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

<!--
先用这一页给大家建立全局地图。
Week 1 到 Week 2 主要是定义 data wrangling、理解流程、熟悉 notebook 和 pandas 的基本动作。
后面几周会把每个步骤拆开深入讲，所以现在先把“框架感”建立起来。
-->

---
layout: section
---

# 作业与时间

<!--
这一页我只做过渡，不展开太细。
重点是让大家知道，这门课不是只考概念，还会通过 quiz、assessment 和 applied session 把概念和操作一起考。
-->

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

<!--
这一页只抓三个重点。
第一，assessment 占比很高，所以不能等到 Week 6 再开始学。
第二，quiz 是个人、线下、短时间完成，不能靠临时抱佛脚。
第三，这门课真正拿分的能力，是把 notebook 里的过程、代码和解释连起来。
-->

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

<!--
Assessment 1 更偏 EDA 和前期处理，Assessment 2 更偏 parsing、cleaning、integrating。
所以大家会发现，Week 1 到 Week 2 学的是“总流程”和“基础操作”，后面慢慢会转向更硬核的清洗和整合。
如果现在连 notebook、pandas、流程步骤都不熟，后面写 report 会非常吃力。
-->


---
layout: two-cols
---

# 上课节奏

- seminar 讲概念、流程、判断题思路 （软）
- session 更偏 notebook / Python 操作 （硬）
- attendance 很重要，尤其 quiz 和 in-class participation 都跟线下节奏强相关

::right::

# 沟通方式

- 讨论优先走 `Ed Forum`
- 教学团队会定期看 forum
- 紧急情况才发邮件
- 涉及个人情况用 private post 更合适

<!--
这里我想传达的重点不是行政信息本身，而是课程运行方式。
Seminar 更像讲思路和判断题；applied session 更像让你亲手做 notebook。
很多同学 quiz 失分，不是不会背定义，而是平时没有在线下节奏里练到位。
-->

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

<!--
这一页建议你们特别记住 quiz 的几个边界条件。
它是 in-person、个人完成，而且时间短，所以题目通常不会让你慢慢推导，而是要求你快速识别概念。
今天后面的真题讲解，其实就是在训练这种快速识别能力。
-->

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

<!--
如果你问这门课一开始最需要补什么，我会说三件事。
第一是基础 Python，至少要能读懂 loop 和 function。
第二是 Jupyter Notebook，因为 assessment 要靠它展示过程。
第三是 pandas 的基本探索和清洗动作，这些会在 applied session 反复出现。
-->

---
layout: default
---

# 一句话定义

Data Wrangling 是把原始数据变成可分析数据的过程。

`Raw Data -> Clean / Tidy Data -> Actionable Insights`

| 不要误解成 | 原因 |
|-----------|------|
| 只是可视化 | 可视化只是后续分析的一部分 |
| 只是收集数据 | 收集只是流程中的一环 |
| 只是机器学习 | wrangling 是分析前准备工作 |

<!--
这一页是全课最核心的一句话定义。
很多同学会把 data wrangling 误解成某一个局部动作，比如收集数据、画图，或者直接做模型。
但课程定义很清楚，它是把原始数据一步步变成可分析数据的整个过程。
-->

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

<!--
这道题我会先让大家自己选一下。
[click]
答案是 c，因为它把 acquire、clean、structure、enrich 这些关键词都覆盖了。
这类题的关键不是记一个词，而是看哪个选项最接近课程定义的完整表述。
-->

---
layout: section
---

# Week 1

<!--
从这里开始正式进入 Week 1 的内容。
Week 1 的目标是先回答三个问题：为什么要做 wrangling，它的目标是什么，它会遇到什么挑战。
-->

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

<div class="callout text-sm">
常见反向陷阱：不是增加复杂度，不是忽略不一致，不是制造冗余。
</div>

<!--
这一页建议大家把目标和反向选项一起记。
考试很喜欢不直接问“什么是目标”，而是问“什么不是目标”。
所以 improving quality、easier access、support integration 这些正向词要熟，增加复杂度这种反项也要敏感。
-->

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

<!--
这道题是 goals 的标准考法。
先让大家自己排除明显反项，再点答案。
[click]
这里的思路很简单，只要看到 increase complexity、ignore inconsistencies，基本就可以直接划掉。
-->

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

<!--
这一页是回答“为什么 wrangling 不可省略”。
原始数据的问题往往不是很炫的高级问题，而是很朴素的缺失、重复、格式不统一。
但这些问题如果不处理，后面再高级的分析也会建立在不可靠的数据上。
-->

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

<!--
这一页不要把它理解成“背数据源清单”。
真正要记的是判断标准，也就是来源是不是 accessible、relevant、high quality，而且成本可接受。
数据来源可以很多，但不是越多越好，关键是适不适合你的问题。
-->

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

<!--
这一页要让大家意识到，wrangling 本身就是难点，不只是分析前的小准备。
量大、格式杂、标准不统一、还有隐私约束，这些都会让前处理阶段非常耗时。
所以现实里经常说，数据项目大部分时间不是花在模型上，而是花在整理数据上。
-->

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

<!--
这题的考点是 challenge 的识别。
先让大家自己做判断，再点答案。
[click]
small volumes 看起来像个选项，但它明显不是 challenge，所以这种题其实是在看你有没有抓到课程里的典型关键词。
-->

---
layout: two-cols
---

# Week 1 默认工具链

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

<!--
这一页不是要你们把所有库都马上会用，而是建立默认工具链意识。
Week 1 到 Week 2 最核心的是 Python、Jupyter、pandas。
其他库知道用途就够了，后面碰到对应任务再逐步展开。
-->

---
layout: section
---

# Week 1 Applied

<!--
从这里开始切到 applied session 的视角。
这部分和 seminar 最大的差别是：不是只会说概念，而是要能在 notebook 里把动作做出来。
-->

---
layout: default
---

# Week 1 Applied 概览

- Jupyter Notebook 的两种 cell
- markdown 写说明
- Python 变量、list、dict
- `for loop` 与 nested `for loop`
- `function`
- `transpose_matrix` 练习

<!--
这一页其实是在告诉大家 applied session 的最小技能包。
你不需要一开始就会写很复杂的程序，但至少要能切换 cell、写 markdown、读懂简单 loop 和 function。
后面的 transpose_matrix 就是把这些基础动作拼起来。
-->

---
layout: default
---

# Week 1 Applied 硬知识

## Jupyter Notebook 为什么是 FIT5196 标配

| 组件 | 你要会什么 |
|------|------------|
| Code cell | 写 Python、运行、看 output |
| Markdown cell | 写标题、解释、表格、过程说明 |
| Output area | 检查代码结果是否合理 |
| Kernel | 维护变量状态，重启后变量会丢失 |

<div class="callout mt-4 text-sm">
Assessment 里 notebook 不只是“放代码”，而是要同时展示 <code>过程</code>、<code>判断</code>、<code>结果</code>。
</div>

<!--
这一页一定要反复强调 notebook 在这门课里的角色。
它不是代码编辑器的替代品，而是你展示分析过程的载体。
老师看 report 的时候，不只是看你结果对不对，也看你中间怎么想、怎么解释。
-->

---
layout: default
---

# Week 1 Applied 硬知识

## Notebook 两种模式和常用快捷键

| 场景 | 关键点 |
|------|--------|
| Command mode | 对 cell 做操作，不是在编辑文本 |
| Edit mode | 正在编辑 cell 内容 |
| `M` | 把当前 cell 切成 markdown |
| `Y` | 把当前 cell 切回 code |
| `Shift + Enter` | 运行当前 cell 并跳到下一格 |

<!--
快捷键本身不是课程核心，但它直接影响你的操作流畅度。
尤其 applied session 时间有限，如果每个 cell 都靠鼠标点，会明显拖慢节奏。
所以至少把 M、Y、Shift Enter 这几个动作练熟。
-->

---
layout: default
---

# Week 1 Applied 练习任务

| 练习 | 要求 |
|------|------|
| Markdown 总结 | 写你过去处理过的数据、遇到的问题、怎么处理、学到了什么 |
| Matrix transpose | 写一个函数，把矩阵行列互换 |

<!--
这两个练习其实对应两种能力。
第一个练的是表达能力，也就是你能不能把数据问题说清楚。
第二个练的是基础编码能力，也就是你能不能把二维结构、loop 和 function 组合起来。
-->

---
layout: default
---

# Week 1 Applied 硬知识

## Markdown 最少要掌握哪些语法

| 功能 | 写法示例 |
|------|----------|
| Heading | `#` 到 `#####` |
| Bullet list | `- item` |
| Numbered list | `1. item` |
| Link | `[text](url)` |
| Image | `![alt](path)` |
| Table | `| col | col |` |

<div class="callout mt-4 text-sm">
Notebook 里的 markdown 不是装饰，是你报告表达和解释思路的主要载体。
</div>

<!--
很多同学会忽略 markdown，觉得只要代码能跑就行。
但在 FIT5196 里，markdown 直接决定你能不能把分析逻辑讲清楚。
所以 heading、list、link、table 这些语法至少要能熟练写出来。
-->

---
layout: default
---

# Week 1 Applied 参考代码

## `transpose_matrix` 参考写法

```python
def transpose_matrix(matrix):
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

<!--
这一页我会把它当参考答案，不会要求大家照抄。
重点是先看结构：先算行列数，再新建结果矩阵，再用双层循环去填。
如果你们能把这个思路讲出来，其实已经比只会背代码更重要。
-->

---
layout: two-cols
---

# Week 1 Applied 硬知识

## `for loop` / `function` / nested loop

| 概念 | 你要记住什么 |
|------|--------------|
| `for x in seq` | 逐个取元素 |
| nested loop | 外层控制行，内层控制列 |
| `def f(x):` | 用 `def` 定义函数 |
| parameter | 函数输入 |
| `return` | 函数输出 |

::right::

```python
def greet(name):
    print("Hello", name)

for item in [1, 2, 3]:
    print(item)
```

<div class="callout mt-4 text-sm">
Week 1 applied 的核心不是语法背诵，而是能看懂并写出最基础的控制流。
</div>

<!--
这里建议边讲边提醒大家，function 和 loop 不要分开学。
真实题目里通常不是单独考一个 for，也不是单独考一个 def，而是要求你把它们放进同一个小任务里。
transpose_matrix 就是这种组合题。
-->

---
layout: default
---

# Week 1 Applied 硬知识

## `transpose_matrix` 到底在考什么

1. matrix 本质上是 `list of lists`
2. `rows = len(matrix)`，`cols = len(matrix[0])`
3. 外层循环遍历 `col`
4. 内层循环遍历 `row`
5. 每次把 `matrix[row][col]` 放进新的 row
6. 最后返回新的 matrix

<div class="callout mt-4 text-sm">
这题不是考高级算法，而是考你能不能把二维索引、nested loops、function 组合起来。
</div>

<!--
这一页是对上一个参考代码做抽象总结。
如果学生说自己不会这题，我通常会让他先别看完整代码，而是先回答三件事：行数怎么算，列数怎么算，matrix[row][col] 取的是什么。
能回答这三件事，代码基本就能写出来。
-->

---
layout: default
---

# Week 1 Applied 硬知识

## Jupyter 里必须会的两种 Cell

| 类型 | 作用 |
|------|------|
| Code cell | 写并执行 Python |
| Markdown cell | 写标题、说明、列表、表格 |

<div class="muted mt-4 text-sm">
FIT5196 的 group assessment 很依赖 notebook 表达过程，所以“会写解释”跟“会写代码”同样重要。
</div>

<!--
这一页可以当作 Week 1 applied 的收束。
Code cell 和 markdown cell 不是二选一，而是要一起出现。
代码负责执行，markdown 负责解释，这两个结合起来才是这门课想看到的 notebook。
-->

---
layout: default
---

# 真题演练

**How do you make text italic in Markdown?**  
`Select all that apply`

| 选项 | 内容 |
|------|------|
| a | Surround the text with `**` |
| b | Surround the text with `~~` |
| c | Surround the text with `_` |
| d | Surround the text with `*` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>c, d</code><br>
<strong>讲解：</strong><code>*text*</code> 和 <code>_text_</code> 都是 italic；<code>**</code> 是 bold，<code>~~</code> 是 strikethrough。
</div>

<!--
这道题建议直接用来带大家熟悉 markdown 细节。
先让大家自己选，再点答案。
[click]
顺便提醒他们，quiz 很喜欢把 bold、italic、strikethrough 放在一起混。
-->

---
layout: default
---

# 真题讲解

**To create a bullet list in Markdown, which symbol can you use?**

| 选项 | 内容 |
|------|------|
| a | All of the above |
| b | `*` |
| c | `-` |
| d | `+` |

<div v-click class="callout mt-4 text-sm">
<strong>答案：</strong><code>a</code><br>
<strong>讲解：</strong>Markdown 的 unordered list 三种写法都能用，所以遇到这种题先看有没有 all of the above。
</div>

<!--
这道题的技巧是先看有没有 all of the above。
[click]
如果前面几个符号都确实成立，那这类题可以很快做完。
在限时 quiz 里，这种识别速度很重要。
-->

---
layout: default
---

# Week 1 结束前至少要会

1. 能打开并运行 notebook
2. 能切换 markdown / code cell
3. 能写基础 Python
4. 能自己定义简单函数
5. 能看懂 list of lists 和 nested loops
6. 能完成简单 notebook 报告表达

<!--
这一页是 Week 1 的最低达标线。
如果这几条里有一半还不稳，建议本周优先补 Python 和 notebook，而不是急着看后面更复杂的内容。
因为后面所有清洗和转换动作，都是建立在这些基础之上的。
-->

---
layout: section
---

# Week 2

<!--
Week 2 的重点是把“定义”推进到“流程”。
也就是不只知道 data wrangling 是什么，还要知道它通常按什么顺序展开。
-->

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

<!--
这张表建议大家按顺序背下来。
后面很多题不是问定义本身，而是问某个动作属于哪一步，或者哪一步在前、哪一步在后。
只要流程顺序不清，题目一变形就容易错。
-->

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

<!--
这题我会拿来提醒大家，课程用词要跟课程定义保持一致。
[click]
像 presentation 这种看起来也跟数据有关，但不是这里定义的 wrangling task。
所以做题时尽量回到课上那套八步流程去判断。
-->

---
layout: two-cols
---

# 1. Discovery

- 先确认要解决什么分析问题
- 找可能的数据来源，不是立刻下载
- 评估来源是否可访问、相关、可用
- 先看 suitability / availability / quality

::right::

# 医疗案例里会找什么

- EHR / 电子病历
- admission / discharge records
- insurance claims
- wearable device data
- patient histories / medications

<div class="muted mt-4 text-sm">
关键词：identify sources, accessibility, suitability, quality
</div>

<!--
Discovery 不是马上下载数据，而是先找可能的数据源并做判断。
很多学生会把 discovery 和 collection 混在一起，所以这里要反复强调：discovery 的关键词是 identify 和 assess。
先判断值不值得用，再进入真正收集。
-->

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

<!--
这道题本质上是在考流程顺序。
[click]
如果顺序已经背熟，这种题几乎不需要思考。
所以我一般会建议大家把八步流程写在纸上默写几次。
-->

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

<!--
Collection 阶段的重点是把收集这件事想清楚。
不是说“我知道一个数据源”就结束了，而是要想字段、格式、质量、隐私、成本这些条件能不能满足任务。
这一步考虑得越清楚，后面返工越少。
-->

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

<!--
这题最容易错在把 collecting 和 storing 混掉。
[click]
storage physical location 听起来也像工程问题，但它更靠近 storing，不是 collection 的核心判断点。
-->

---
layout: default
---

# 3. Pre-processing

| 常见动作 | 说明 |
|----------|------|
| Subsetting | 只保留相关行或列 |
| Sampling | 数据太大时抽代表性样本 |
| Date formatting | 统一日期格式 |
| Numeric formatting | 小数点、千位分隔符统一 |
| Categorical formatting | `Male/M`、`Female/F` 统一 |
| Unit / currency conversion | 公里英里、USD/AUD 等统一 |
| Encoding / timezone | UTF-8、时区对齐 |
| File conversion | XML 转 CSV，JSON 转结构化表 |

<div class="muted mt-4 text-sm">
关键词：subset、sample、format、unit、encoding、conversion
</div>

<!--
Pre-processing 的特点是“先整理到可处理的状态”，但还没真正进入修错。
像 subsetting、sampling、统一格式、统一单位，这些都属于预处理。
如果题目强调 conversion 或 formatting，优先想到 pre-processing。
-->

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

<!--
这题是 pre-processing 里 very common 的概念题。
[click]
只要看到 consistent format，就往 standardization 想；如果看到 mean 0、variance 1，那才是另一个层面的标准化。
-->

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

<!--
Cleaning 是八步流程里最容易被考的一步。
因为它的关键词很集中，像 missing values、duplicates、inconsistencies、outliers，几乎一出现就该往 cleaning 去联想。
-->

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

<!--
这题建议大家先看有没有明显反项。
[click]
introducing new errors 当然不可能是 cleaning 的目标，所以先排除它，再回头看剩下几个正项。
-->

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

<!--
Transformation 的核心是把数据变成更适合分析的表示。
这里学生最容易混的是 normalization、standardization、aggregation、discretization。
所以讲这一页时，重点不是把定义背出来，而是能区分它们的使用场景。
-->

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

<!--
这一页补的是 transformation 不只针对数值。
文本也会做 tokenization、lemmatization，图像也会做 resize、normalization。
所以 transformation 可以理解成“把原始表示改造成更适合后续分析的表示”。
-->

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

<!--
这是 transformation 里最典型的一道概念题。
[click]
只要题干写 small specified range，基本就该优先选 normalization。
考试会故意把 standardization 放进来混淆，但关键词不一样。
-->

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

<!--
Enrichment 最容易和 cleaning 混。
我一般会用一句话区分：cleaning 是修问题，enrichment 是补信息。
如果题目强调 adding context、adding attributes、integrating external info，多半就是 enrichment。
-->

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

<!--
这题的关键是看动作性质。
[click]
simplifying formats 更像格式整理，不像 enrichment。
enrichment 要抓的是 value、context、analysis capability 这些词。
-->

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

<!--
Validation 是 checking，不是 fixing。
这一点一定要和 cleaning 区分开。
如果 cleaning 是“修”，那 validation 更像“检查规则是否满足”。
-->

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

<!--
这题里最明显的反项是 promoted inconsistency。
[click]
validation 的方向永远是提高可靠性和可用性，不可能去鼓励不一致。
-->

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

<!--
Storing 常常被学生忽略，但它不是单纯“存起来”。
它还包括 schema、security、indexing、backup、metadata 这些可维护性问题。
所以 storing 更接近长期可复用和可治理的设计。
-->

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

<!--
这题容易把 governance 相关概念一起混进来。
[click]
但 cataloging 的核心还是 metadata、lineage、catalog creation 这些能帮助你“找到并理解数据”的东西。
-->

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

<!--
这一页是把前面的八步流程串成一个完整案例。
我建议讲的时候不要急着逐字念，而是让学生看到：同一个项目会从找数据源，一路走到清洗、转换、验证、存储。
这样他们对流程就不会停留在背单词，而是能形成完整画面。
-->

---
layout: default
---

# Week 2 Applied 常见 pandas 操作

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

<!--
这一页是过渡页，把 Week 2 的流程概念接到 applied session 的 pandas 操作。
重点是告诉学生，这些函数名字不需要一次全背完，但至少要知道它们各自负责什么。
后面的真题里会直接考这些 API 的识别。
-->

---
layout: section
---

# Week 2 Applied

<!--
从这里开始切到 Week 2 applied。
重点会从“概念属于哪一步”转成“具体用 pandas 怎么看、怎么选、怎么处理缺失值”。
-->

---
layout: default
---

# Week 2 Applied 硬知识

## `pandas` / `DataFrame` 基础认知

| 知识点 | 要点 |
|--------|------|
| 导入方式 | `import pandas as pd` |
| DataFrame | 二维表格数据结构 |
| case sensitive | `DataFrame` 不等于 `dataframe` |
| 创建方式 | list、dict、日期索引都可以建表 |
| 常见变量名 | 通常写成 `df` |

```python
import pandas as pd

df = pd.DataFrame([2, 4, 6, 8])
```

<!--
这里我会先把 pandas 和 DataFrame 的最低认知讲清楚。
DataFrame 就是二维表结构，很多后续操作都是围绕它展开。
另外 case sensitive 这种细节在初学阶段很常见，写错大小写就会直接报错。
-->

---
layout: default
---

# Week 2 Applied 硬知识

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

<!--
这是 Week 2 applied 最重要的习惯之一：先探索，再清洗。
不要一拿到表就开始改值或删行。
先用 info、describe、head、shape 把数据结构看清楚，后面的动作才有依据。
-->

---
layout: default
---

# Week 2 Applied 硬知识

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

<!--
loc 和 iloc 是 pandas 高频考点。
我建议课堂上直接反复说一句：loc 看标签，iloc 看位置。
只要这句话记住，后面很多题都会简单很多。
-->

---
layout: default
---

# Week 2 Applied 硬知识

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

<!--
这页是缺失值处理的最小工作流。
先看有没有缺失，再定位到哪些行，最后再决定是不是 drop。
很多同学一上来就 dropna，但如果不先看缺失分布，容易把重要数据直接删掉。
-->

---
layout: default
---

# Week 2 Applied 硬知识

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

<!--
这一页我建议你一定要慢一点讲。
因为很多同学肉眼看到空字符串，就以为 pandas 会自动把它当 missing。
但真正会被 isna 或 isnull 识别的，是 NaN、None、NaT 这些标准缺失值。
-->

---
layout: default
---

# Week 2 Applied 硬知识

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

<!--
这页的重点不是让你们背更多 API，而是理解一个工作习惯。
如果 pandas 已经提供了列操作、表操作，就尽量不要回到逐行写 loop。
因为真实数据表一大，逐行写法通常更慢，也更容易出错。
-->

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

<!--
这题就是 pandas API 识别题。
先让大家分清 info 和 describe 的功能，再点答案。
[click]
info 看结构和类型，describe 看统计摘要，这两个必须分开记。
-->

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
<strong>答案：</strong><code>a, b</code><br>
<strong>讲解：</strong><code>iloc</code> 是位置切片，起点 0-based 且右边不含；<code>loc</code> 是标签切片，通常两端都含。<code>locate</code> 根本不是 pandas API。
</div>

<!--
这题是 loc 和 iloc 的具体应用。
[click]
iloc 的关键是位置切片，0-based，而且右边界不含。
locate 这个选项是假的，考试很喜欢这样放一个长得像 API 的干扰项。
-->

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
<strong>讲解：</strong><code>isna()</code> 和 <code>isnull()</code> 在 pandas 里都能用。考试常用两个假 API 选项混进来。
</div>

<!--
这题主要考 API 真假辨别。
[click]
isna 和 isnull 都是对的，has_null 和 missing 都不是标准 pandas 方法。
这种题如果平时不亲手写，很容易被名字骗到。
-->

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

<!--
这题最关键的是看动词。
[click]
题干说的是 drop rows，那就直接往 dropna 想。
如果题干改成 fill missing values，那才会去想 fillna。
-->

---
layout: section
---

# Quiz 易错点

<!--
前面已经把概念、流程和 applied 基础都过了一遍。
最后这一段我会专门帮大家收拢成做题规则，方便考前快速回看。
-->

---
layout: default
---

# 最容易混的概念

| 概念组 | 区别 |
|--------|------|
| Discovery vs Collection | 找来源 vs 真正收集 |
| Subsetting vs Sampling | 取子集 vs 抽样本 |
| Cleaning vs Validation | 修问题 vs 检规则 |
| Enrichment vs Storing | 补信息 vs 保存管理 |
| Normalization vs Standardization | 缩放范围 vs 均值方差标准化 |
| Discretization vs Binning | 分类别区间 vs 分桶 |

<!--
这一页建议大家考前重点回看。
因为 quiz 最常见的错，不是完全不会，而是两个很像的概念分不清。
如果这些 pairs 能分清，正确率会明显提升。
-->

---
layout: default
---

# 看到题目先抓关键词

| 题目关键词 | 先想到什么 |
|------------|------------|
| identify sources | discovery |
| budget / privacy / objectives | collection |
| subset / sample / format / unit | pre-processing |
| duplicates / missing / outliers | cleaning |
| aggregate / normalize / discretize | transformation |
| external context / merge more info | enrichment |
| allowed values / ranges / uniqueness | validation |
| schema / backup / warehouse / indexing | storing |

<!--
这一页就是做题时的关键词匹配表。
我的建议是，看到题目先不要急着选答案，先抓关键词，再映射到流程步骤。
这样在限时环境下会稳很多。
-->

---
layout: section
---

# 学习建议

<!--
最后我不再加新知识点，而是把接下来怎么补课说清楚。
如果学生现在知道下一步该练什么，这份 slides 才真正有用。
-->

---
layout: default
---

# Week 1 必须完成

1. 能打开并运行 Jupyter Notebook 或 Google Colab
2. 能创建并运行 code cell
3. 能写 markdown cell
4. 会写变量、list、dict
5. 会写 for loop 和 nested loop
6. 会定义简单函数
7. 能手写 `transpose_matrix`
8. 知道 Quiz 1、Assessment 1、Assessment 2 的时间点

<!--
这一页可以当作本周行动清单。
如果这几条都能做到，说明 Week 1 到 Week 2 的基础已经过关。
如果还做不到，就优先回练 notebook、Python 基础和 pandas 的探索动作。
-->

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

<!--
这页主要帮助大家安排节奏。
不要等 quiz 前一周才开始准备，因为 quiz 考的是前几周逐步积累出来的识别能力。
最好的策略是每周把 seminar 概念和 applied 操作一起消化掉。
-->

---
layout: default
---

# Final Checklist

1. 能用自己的话定义 data wrangling
2. 能说出它的目标和主要挑战
3. 能按顺序写出 8 个步骤
4. 能给每一步举一个例子
5. 能分清 discovery / collection / pre-processing / cleaning / transformation / enrichment / validation / storing
6. 知道 subsetting、sampling、normalization、standardization、discretization、binning 的区别
7. 能在 Jupyter Notebook 里完成基础代码与 markdown 操作
8. 能用 pandas 读入 CSV 并查看数据结构
9. 会做基础缺失值处理

<!--
这一页就是整份 Week 1-2 slides 的最终检查表。
如果学生能把这几条都做到，后面的 Week 3 以后虽然会更难，但至少不会因为基础薄弱而直接掉队。
-->

---
layout: end
---

# 下阶段

Week 3 会开始更具体地碰到 regex / text handling；

<!--
最后告诉大家，Week 3 会开始进入更具体的字符串和文本处理。
所以 Week 1 到 Week 2 的基础如果还不稳，建议这周尽快补齐，不然后面会越积越多。
-->
