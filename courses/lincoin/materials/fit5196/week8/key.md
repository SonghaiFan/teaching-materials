### Key Terms 关键词

- [Essential] Data quality: The overall condition of data based on accuracy, completeness, reliability, relevance, and timeliness. Why it matters: good decisions rely on good data.
  【必要】数据质量：基于准确性、完整性、可靠性、相关性和及时性对数据整体状况的评估。重要性：良好的决策依赖于良好的数据。
- [Essential] Data cleansing (data cleaning): Detecting and correcting or removing corrupt or inaccurate records to improve data quality. Why it matters: clean data underpins trustworthy analyses and models.
  【必要】数据清洗（data cleaning）：检测并纠正或删除损坏或不准确的记录，以提高数据质量。重要性：干净的数据是可信分析和模型的基础。
- [Essential] Data wrangling: End-to-end process of discovering, cleaning, transforming, and enriching data to make it usable for analysis.
  【必要】数据整理：发现、清洗、转换和丰富数据的端到端流程，以使其可用于分析。
- [Essential] Data audit: A systematic review of data to identify quality issues, determine health, and set the stage for cleansing.
  【必要】数据审计：对数据进行系统性审查，以识别质量问题、评估健康状况并为清洗工作奠定基础。
- [Essential] Data cleansing plan: A structured plan detailing goals, strategies, tools, timeline, and governance for cleansing data.
  [重要] 数据清洗计划：一份结构化的计划，详细说明清洗数据的目标、策略、工具、时间表和治理。
- [Essential] Missing data: Data points that have no value for a variable; can bias results if not handled properly.
  [重要] 缺失数据：在某变量上没有值的数据点；如果不妥善处理，可能会导致结果偏差。
- [Advanced] Missing data mechanisms: The reasons data are missing; MCAR (missing completely at random), MAR (missing at random), MNAR (not at random). These determine how to handle missingness.
  [高级] 缺失数据机制：数据缺失的原因；MCAR（完全随机缺失）、MAR（随机缺失）、MNAR（非随机缺失）。这些机制决定了如何处理缺失情况。
- [Advanced] Imputation: Methods to fill in missing values (e.g., mean, regression, stochastic regression) to create a complete dataset for analysis.
  [高级] 插补：用于填补缺失值的方法（例如均值、回归、随机回归），以创建用于分析的完整数据集。
- [Essential] Deletion methods: Techniques to handle missing data by removing cases (listwise/complete case, pairwise/available-case).
  【关键】删除方法：通过删除样本来处理缺失数据的技术（逐案删除/完全案例、成对删除/可用案例）。
- [Advanced] Pairwise deletion: Uses all available data for each analysis, can distort estimates if MCAR assumption and correlations are problematic.
  [高级] 成对删除：在每次分析中使用所有可用数据，如果不满足完全随机缺失（MCAR）假设且存在相关性，可能会扭曲估计值。
- [Advanced] Model-based methods: Approaches like maximum likelihood or multiple imputation that model the data to address missingness.
  [高级] 基于模型的方法：像最大似然或多重插补等通过对数据建模来处理缺失值的方法。
- [Essential] Outliers: Observations that are markedly different from others; may distort analyses and require special handling.
  [重要] 异常值：明显不同于其他观测值的样本；可能会扭曲分析结果，需要特殊处理。

### Main Ideas 主要观点

- Big idea: Data cleansing is a crucial, multi-step workflow that begins with a data audit, defines cleansing goals, plans the cleansing, backups, and then executes cleansing, verification, and documentation. Clean data leads to better analytics and reliable decisions.
  核心观点：数据清洗是一个关键的多步骤工作流，始于数据审计，明确清洗目标，制定清洗计划、备份数据，然后执行清洗、验证和文档记录。干净的数据带来更好的分析和可靠的决策。
- The cleansing workflow connects: Data Audit -> Define Cleansing Goals -> Data Cleansing Plan -> Backup Data -> Data Cleansing Operations -> Verification -> Documentation & Reporting -> Review (with feedback looping to Data Audit).
  清洗工作流程的连接顺序为：数据审计 -> 定义清洗目标 -> 数据清洗计划 -> 备份数据 -> 数据清洗操作 -> 验证 -> 文档记录与报告 -> 复审（并将反馈循环回数据审计）。
- Missing data are common and can bias analyses; understanding why data are missing (MAR, MCAR, MNAR) guides the choice of handling method.
  缺失数据很常见且可能导致分析偏差；理解数据缺失的原因（MAR、MCAR、MNAR）有助于选择处理方法。
- Imputation methods (mean, regression, stochastic regression) are designed to preserve relationships and variability; single imputation tends to bias estimates and underestimate uncertainty.
  插补方法（均值插补、回归插补、随机回归插补）旨在保留变量之间的关系和变异性；单次插补往往会使估计产生偏差并低估不确定性。
- Deletion methods are simple but can waste data or distort results unless MCAR holds; paired with understanding of data structure, they may be acceptable in some contexts.
  删除方法简单但可能浪费数据或扭曲结果，除非满足完全随机缺失（MCAR）；在理解数据结构的基础上，在某些情境下可能可以接受。
- Data cleansing uses a mix of automated tools and human judgment; tools range from Excel to Talend, IBM Infosphere, OpenRefine, etc.
  数据清洗结合了自动化工具和人工判断；工具包括从 Excel 到 Talend、IBM Infosphere、OpenRefine 等。
- Verification ensures the final data meet quality criteria and are ready for analysis, and documentation captures what was done for reproducibility.
  核验确保最终数据符合质量标准并可用于分析，文档记录则捕捉了所做的工作以便可复现。

### Important Data 重要数据

- Data cleanup steps (from the Data Cleansing Operations checklist):
  数据清理步骤（来自“数据清理操作”检查表）：
  - Removing duplicates 删除重复项
  - Validating and correcting errors
    验证并纠正错误
  - Consistency checks 一致性检查
  - Filling missing values 填充缺失值
  - Handling outliers 处理异常值
- Data audit outputs: metrics for accuracy, completeness, consistency, reliability; data mapping across the organization; sampling for analysis; use of software tools plus manual review.
  数据审计输出：准确性、完整性、一致性、可靠性的度量；组织内的数据映射；用于分析的抽样；软件工具与人工审查并用。
- Key formulas and concepts:
  关键公式和概念：
  - Covariance-based measures in pairwise deletion contexts (illustrated in the notes with formulas for means, variances, and covariance using available data).
    成对删除情境中的协方差度量（注释中用可用数据的均值、方差和协方差公式进行了说明）。
  - Imputation formula examples:
    插补公式示例：
    - Regression imputation: JPi = β0 + β1 × IQi
      回归插补：JPi = β0 + β1 × IQi
    - Stochastic regression: Pi = β0 + β1 × IQi + zi, where zi ~ N(0, σ^2JP|IQ)
      随机回归：Pi = β0 + β1 × IQi + zi，其中 zi ~ N(0, σ^2JP|IQ)
- Example snippets: 示例片段：
  - Deletion: List-wise deletion discards any case with missing values.
    删除法：逐案删除会丢弃任何存在缺失值的样本。
  - Multiple imputation and model-based approaches aim to minimize bias and use all available information.
    多重插补和基于模型的方法旨在最小化偏差并利用所有可用信息。
  - Missing data patterns: Univariate, Monotone, General patterns.
    缺失数据模式：单变量、单调、一般模式。
- Illustrative queries (from the material):
  说明性查询（来自材料）：
  - Simple regression-based imputation setup: JPi = β0 + β1(IQ i)
    基于简单回归的插补设置：JPi = β0 + β1(IQ i)
  - Stochastic residual addition: Pi = β0 + β1(IQ i) + zi
    随机残差添加：Pi = β0 + β1(IQ i) + zi
- Typical visualization notes:
  典型可视化说明：
  - Scatter plots showing relationship between IQ and Job Performance to illustrate how imputation might preserve relationships.
    散点图显示智商与工作表现之间的关系，以说明插补如何可能保留这种关系。

### Key Takeaways for Your Exam 考试要点

- The data cleansing process is iterative and documented: start with a data audit, define goals, plan, back up, cleanse, verify, and report.
  数据清洗过程是迭代且需记录的：从数据审计开始，明确目标，制定计划，备份，清洗，验证，并报告。
- Understand when to use which missing-data method:
  了解何时使用哪种缺失数据方法：
  - Deletion methods (listwise/pairwise) rely on MCAR and can reduce sample size or bias results if MCAR fails.
    删除法（逐列表/逐对）依赖于完全随机缺失（MCAR），如果不满足 MCAR 可能会减少样本量或导致结果偏差。
  - Imputation methods (mean, regression, stochastic) fill in values but have trade-offs: mean imputation reduces variability; regression uses relationships but can be biased if model is wrong; stochastic regression adds residuals to restore variability.
    插补法（均值、回归、随机）用于填补缺失值，但各有取舍：均值插补会降低变异性；回归插补利用变量间关系但若模型错误可能产生偏差；随机回归通过加入残差以恢复变异性。
  - Model-based methods (maximum likelihood, multiple imputation) generally provide less biased, more robust estimates under MAR/MNAR assumptions.
    基于模型的方法（极大似然、多重插补）在 MAR/MNAR 假设下通常能提供偏差更小、稳健性更强的估计。
- MAR vs MCAR vs MNAR matters: MAR uses observed data to model missingness; MCAR ignores data values; MNAR depends on unobserved data. Choose methods accordingly.
  MAR 与 MCAR 与 MNAR 的区别很重要：MAR 使用观测到的数据来建模缺失机制；MCAR 忽略数据值；MNAR 则依赖于未观测到的数据。应据此选择方法。
- Verification and uncertainty: After cleansing, you should verify accuracy, consistency, and completeness, and you should have good estimates of uncertainty (standard errors, confidence intervals).
  验证与不确定性：清洗后，应验证准确性、一致性和完整性，并对不确定性（标准误、置信区间）有良好的估计。
- Practical skill: be able to identify duplicates, understand when to remove or keep them, and be able to write simple SQL-like queries to find and resolve duplicates.
  实践技能：能够识别重复数据，理解何时删除或保留它们，并能编写类似 SQL 的简单查询来查找并解决重复问题。
- Know the pros/cons of listwise vs pairwise deletion, and the general idea behind imputations (mean, regression, stochastic), including their impact on bias and variance.
  了解逐案删除与成对删除的优缺点，以及插补（均值、回归、随机插补）的一般思想，包括它们对偏差和方差的影响。
- For exams, be ready to explain why clean data matters for machine learning, statistics, and BI tools, and describe a high-level cleansing workflow with a sample plan and audit steps.
  备考时，准备好解释为何干净的数据对机器学习、统计学和商业智能工具重要，并描述一个高层次的清洗工作流程，附带示例计划和审计步骤。
