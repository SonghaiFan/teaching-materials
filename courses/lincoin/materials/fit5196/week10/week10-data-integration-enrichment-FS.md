---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
color: #333
math: katex
header: "FIT5196 Data Wrangling - Week 10 Tutorial"
footer: "Data Integration & Enrichment 数据集成与增强"
style: |
  section {
    font-family: "Noto Sans CJK SC","Source Han Sans SC","PingFang SC","Microsoft YaHei",sans-serif;
  }
---

# 📚 FIT5196 Week 10 Tutorial

## Data Integration & Enrichment

## 数据集成与增强

**补习班课程 - 重点知识梳理**

---

## 本节大纲 Outline

1. **回顾** - Data Transformation 要点
2. **数据增强** - Data Enrichment 概念与步骤
3. **数据集成** - Data Integration 核心理论
4. **模式集成** - Schema Integration 挑战与解决方案
5. **数据层面集成** - Data-level Integration 实用方法
6. **考试要点** - 重点总结

---

## 1. 回顾：Data Transformation 数据转换

### 上周重点回顾

- **数据标准化** (Data Normalisation)：Min-Max, Z-score, Robust Scaling
- **数据离散化** (Data Discretisation)：连续变量转分类
- **数据构造** (Data Construction)：特征工程与采样

⚡ **连接本周**: 数据转换是单数据源的预处理，本周学习多数据源的集成与增强

---

## 2. Data Enrichment 数据增强

### 定义与目标

**Data Enrichment** 数据增强：通过添加来自外部数据源的附加上下文或信息来增强现有数据的过程。

#### 核心目标

- **上下文增加** (Contextual Addition)：添加人口统计、地理、行业指标等
- **质量改善** (Quality Improvement)：提高数据的粒度和准确性
- **价值提升** (Value Enhancement)：提升数据的分析和决策价值

---

### Data Enrichment vs Data Integration

| 方面 | Data Enrichment 数据增强 | Data Integration 数据集成 |
|------|------------------------|------------------------|
| **目的** | 通过添加详细信息增强数据价值 | 组合数据创建统一数据库 |
| **输出** | 带有额外信息层的增强数据集 | 来自多个源的整合数据集 |
| **过程** | 向现有记录追加相关数据 | 合并和协调各种源的数据 |

⚡ **记忆要点**: Enrichment = 增强价值，Integration = 统一整合

---

### Data Enrichment 步骤流程

```text
定义目标 → 选择数据源 → 集成数据 → 确保质量 → 持续更新
    ↓           ↓           ↓         ↓         ↓
确定缺失信息   选择可靠源   ETL处理   质量验证   保持时效性
```

#### 具体操作

1. **Define Objectives** 定义目标：确定需要增强的具体信息
2. **Select Data Sources** 选择数据源：基于可靠性、准确性、相关性
3. **Integrate Data** 集成数据：复杂的ETL过程
4. **Ensure Data Quality** 质量保证：准确性、完整性、及时性验证
5. **Continuous Updating** 持续更新：维护数据的相关性

---

### 应用案例 Applications

#### 成功案例

- **Google Knowledge Graph** 知识图谱：搜索结果增强
- **HousingMaps** 房产地图：房价与地图结合
- **TrendMaps** 趋势地图：Twitter趋势地理化

💡 **实践技巧**: 选择数据源时优先考虑权威性、更新频率、数据质量

---

## 3. Data Integration 数据集成

### 定义与重要性

**Data Integration** 数据集成：将来自不同源的数据组合以创建统一视图的过程。

#### 关键特征

- **源多样性** (Source Diversity)：多个数据库、电子表格、外部API
- **模式合并** (Schema Merging)：统一各种数据模式
- **实体解析** (Entity Resolution)：识别和整合同一实体的记录
- **集中化** (Centralization)：便于访问和分析的统一存储库

---

### Data Integration 面临的挑战

#### 主要挑战 🚨

1. **异构数据** (Heterogeneous Data)
   - 不同源独立开发，模式和目标不同

2. **格式多样** (Various Formats)
   - 文本、网络日志、社交网络、传感器数据等

3. **分类不兼容** (Incompatible Taxonomies)
   - 对象身份不同，模式分离

4. **时间同步** (Time Synchronisation)
   - 不同时间窗口的数据同步

---

### 更多挑战

1. **遗留数据** (Legacy Data)
   - 历史数据与现代数据的结合

2. **抽象层次** (Abstraction Levels)
   - 不同抽象级别：郊区级别 vs 州级别

3. **数据质量** (Data Quality)
   - 错误数据会加剧集成后的质量问题

4. **数据源数量** (Number of Sources)
   - 网络规模的集成挑战

⚡ **考试重点**: 理解每种挑战的含义和解决思路

---

## 4. Schema Integration 模式集成

### Schema 定义

#### 不同环境下的Schema

- **关系数据库**: 表的集合，每个表包含属性及其数据类型
- **XML/JSON**: 标签、类和属性的集合
- **数据科学**: 数据安排、关系和内容的表示

#### 为什么需要Schema Integration？

不同数据源有不同的结构和表示方法，需要统一的中介模式 (Mediated Schema)

---

### Schema Mapping 模式映射

**Semantic Mapping** 语义映射：指定源属性如何对应中介模式属性

#### 映射类型

- **一对一映射** (One-to-One)
  - Movies.title ≈ Items.name
  - Movies.year ≈ Items.year

- **一对多映射** (One-to-Many)
  - Items.price ≈ Products.basePrice × (1 + Locations.taxRate)

---

### Schema Integration 问题

#### 1. 结构冲突 (Structure Conflicts)

- 数据结构不一致
- 不同数据源格式：XML, HTML, JSON, 半结构化, 非结构化

#### 2. 命名冲突 (Naming Conflicts)

| 冲突类型 | 定义 | 示例 |
|----------|------|------|
| **同形异义** (Homonyms) | 同名不同义 | ID可指客户ID、产品ID、店铺ID |
| **同义异形** (Synonyms) | 异名同义 | Customer ID 和 Client ID |

---

### Schema Integration 问题 (续)

#### 3. 实体解析冲突 (Entity Resolution Conflicts)

**单位不同**

- 温度单位：摄氏度 vs 华氏度
- 货币单位：USD vs EUR vs RMB

**数据类型异构**

- 电话号码在一个数据库中存储为字符串，另一个存储为整数

**值异构**

- 缩写使用：Professor vs Prof, Street vs St, Road vs Rd

**抽象层次不同**

- 地址可拆分为：街道号码、街道名称、郊区、城市、邮编等

---

### Schema Matching 模式匹配

#### Name-Based Matching 基于名称的匹配

**处理步骤**:

1. **分割名称**: ClientName ⇒ Client Name
2. **扩展缩写**: loc ⇒ location, cust ⇒ customer
3. **同义词扩展**: Location ⇒ Address, Cost ⇒ Price
4. **上位词扩展**: product ⇒ book, DVD, etc.
5. **移除冗余词**: 排除 "in", "at" 等

✅ **优点**: 成本低，不需要训练
❌ **缺点**: 无法有效利用数据实例

---

### Instance-based Matching 基于实例的匹配

#### Rule-based Method 基于规则的方法

- 利用模式信息：元素名称、数据类型、结构、完整性约束
- 示例：DVD评级 (G, PG, PG-13, R) 的识别

#### Learning-based Method 基于学习的方法

- 利用模式和数据信息的学习技术
- 分类方法，需要训练数据

⚡ **选择建议**: 规则方法适用于明确规则场景，学习方法适用于复杂模式识别

---

## 5. Data-level Integration 数据层面集成

### 两大类别

#### Attribute-level Integration 属性级别集成

- **冗余** (Redundancy)：属性可从其他属性计算得出
- **相关性** (Correlation)：不同值表示相同属性但单位不同

#### Tuple-level Integration 元组级别集成

- **重复** (Duplication)：多行指向同一对象
- **不一致性** (Inconsistency)：重复记录未同时更新

---

### Attribute-level Integration 技术

#### 分类变量：Chi-square Test 卡方检验

**目的**: 检验两个分类变量是否独立

**检验统计量**:

$$\chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i}$$

**期望频数**:

$$E = \frac{\text{行总计} \times \text{列总计}}{\text{样本总数}}$$

⚡ **判断标准**: $\chi^2 >$ 临界值 → 拒绝零假设 → 变量相关

---

### Chi-square Test 实例

#### 示例：性别与教育水平是否独立？

- **零假设**: 性别与教育水平独立
- **备择假设**: 性别与教育水平相关
- **计算结果**: $\chi^2 = 8.006$
- **自由度**: $(r-1)(c-1) = 3$
- **临界值** (α=0.05): 7.815

**结论**: 8.006 > 7.815，拒绝零假设，性别与教育水平在5%显著性水平下相关

---

### 数值变量：Correlation Coefficient 相关系数

#### Pearson 相关系数

$$r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

**取值范围**: $-1 \leq r \leq +1$

- **正相关**: $r$ 接近 +1
- **负相关**: $r$ 接近 -1  
- **无相关**: $r$ 接近 0

#### 决定系数 $R^2$

$$R^2 = 1 - \frac{RSS}{TSS}$$

表示一个变量方差中可由另一个变量预测的比例

---

### Tuple-level Integration 方法

#### String Matching 字符串匹配

**相似性度量分类**

1. **序列基础** (Sequence-based)
   - Edit Distance 编辑距离
   - Needleman-Wunch 测度

2. **集合基础** (Set-based)  
   - Overlap 重叠测度
   - TF/IDF 测度

3. **混合方法** (Hybrid)
   - 结合序列和集合方法

4. **语音相似性** (Phonetic)
   - 基于发音的匹配

---

### Edit Distance 编辑距离

**定义**: 将一个字符串转换为另一个字符串所需的最少编辑操作数

#### 编辑操作

- **插入** (Insertion)
- **删除** (Deletion)  
- **替换** (Substitution)

#### 动态规划求解

通过构建矩阵，逐步计算最小编辑距离

💡 **应用场景**: 姓名匹配、地址标准化、重复记录识别

---

### Data Matching 数据匹配

#### 挑战

- 格式约定差异
- 缩写和简化使用
- 不同命名约定
- 遗漏和错误

#### 方法分类

**Rule-based Method 基于规则**

$$sim(x,y) = \sum_{i=1}^n \alpha_i \cdot sim_i(x,y)$$

**Learning-based Method 基于学习**

- **监督学习**: 需要训练数据
- **聚类方法**: 同一簇内的元组匹配
- **概率方法**: 基于概率模型

---

### 监督学习数据匹配

#### 训练数据格式

$$T = \{(x_1, y_1, l_1), (x_2, y_2, l_2), \ldots, (x_n, y_n, l_n)\}$$

其中 $(x_i, y_i)$ 表示元组对，$l_i$ 表示布尔标签

#### 处理步骤

1. **定义特征** $f_1, f_2, \ldots, f_m$
2. **特征向量转换** 
3. **应用监督学习算法**

⚡ **优势**: 能学习复杂模式，准确性高
❌ **劣势**: 需要大量标注数据

---

## 6. 考试要点总结

### 必考概念 ⭐⭐⭐

#### 定义对比

- **Data Enrichment vs Data Integration** 的区别和联系
- **Schema Integration vs Data-level Integration** 的层次差异

#### 核心技术

- **Chi-square Test** 卡方检验：公式、应用、解释
- **Correlation Coefficient** 相关系数：计算、判断标准
- **Edit Distance** 编辑距离：算法思想、动态规划

---

### 常考题型 ⭐⭐

#### 计算题

- 给定contingency table计算卡方统计量
- 计算两变量的Pearson相关系数
- 手工计算编辑距离

#### 分析题  

- 识别Schema Integration中的冲突类型
- 选择合适的相似性度量方法
- 设计数据匹配规则

#### 应用题

- 描述Data Enrichment的步骤
- 分析实际案例中的集成挑战

---

### 易错点提醒 🚨

#### 概念混淆

- **同形异义 vs 同义异形**: 记住定义和举例
- **监督学习 vs 无监督学习** 在数据匹配中的区别

#### 计算错误

- 卡方检验中期望频数的计算公式
- 相关系数公式中各项的含义
- 编辑距离的边界条件处理

#### 应用判断

- 什么时候用基于规则 vs 基于学习的方法
- 如何选择合适的相似性度量

---

## 实践建议 💡

### 掌握核心流程

#### Data Enrichment 流程

```text
业务需求分析 → 外部数据源评估 → ETL设计实现 → 质量验证 → 持续监控
```

#### Schema Integration 流程  

```text
模式分析 → 冲突识别 → 映射设计 → 一致性检查 → 集成验证
```

#### Data Matching 流程

```text
特征工程 → 相似性计算 → 阈值设定 → 匹配验证 → 结果优化
```

---

## 下周预告 📋

### Week 11: Data Validation 数据验证

#### 主要内容

- **数据质量评估** - 准确性、完整性、一致性度量
- **约束检查** - 完整性约束、业务规则验证
- **异常检测** - 统计方法、机器学习方法
- **质量报告** - 数据质量仪表板、KPI设计

📚 **准备建议**: 

- 复习统计基础知识
- 了解常见的数据质量问题
- 准备Assignment 2的数据验证部分

---

## 总结 Summary

### 本节重点 Key Points

1. **理解** Data Enrichment 和 Data Integration 的区别和应用
2. **掌握** Schema Integration 中各种冲突类型的识别和解决
3. **熟练** 卡方检验和相关系数的计算和解释
4. **应用** 各种字符串匹配和数据匹配方法

### 实践要求

- 能够设计数据集成方案
- 会计算统计检验指标
- 理解机器学习在数据匹配中的应用

⚡ **一句话总结**: 数据集成是多源数据统一的艺术，需要在技术方法和业务理解间找到平衡

---

## Thank you! 感谢聆听！

### Q&A 问答环节

**有问题随时提问** 🙋‍♂️🙋‍♀️

#### 常见问题预判

- Chi-square检验的自由度如何计算？
- 什么情况下选择Edit Distance vs TF/IDF？
- 如何处理多对多的Schema映射？

**联系方式**: 课后答疑时间或通过Moodle留言