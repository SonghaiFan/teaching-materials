---
theme: default
title: FIT2179 Studio Week 3
info: |
  ## FIT2179 Data Visualisation
  Week 3 - Tableau Introduction
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

<!-- 
Slidev 官方最佳实践：
1. 使用 frontmatter 配置全局属性
2. 使用 ::right:: 语法实现双栏布局
3. 使用 v-click 实现动画
4. 使用 HTML 注释添加演讲者备注
-->

---
layout: monash-cover
subtitle: Data Visualisation Fundamentals and Tableau Introduction
date: 09/08/2023
presenter: Songhai (Frank) Fan
---

# FIT2179 Studio Week 3

<!-- 
演讲者备注：
- 欢迎学生，介绍本周主题
- 提醒学生打开 Tableau Public
- 确认大家都已完成课前准备
-->

---
layout: monash-title-content-side
eyebrow: Speaker introduction
image: /images/pptx/image2.jpg
imageAlt: Songhai (Frank) Fan
imageFit: contain
---

# Introduction

My name is **Songhai (Frank) Fan**.

I'm a PhD candidate in the Monash Embodied Visualisation Lab, where we primarily focus on VR and AR data visualisation.

However, I'm especially interested in **text visualisation for narratives** among news media leveraging LLM.

<!-- 
演讲者备注：
- 简要介绍自己的研究背景
- 提到 EMVIS 实验室
- 说明与数据可视化的关联
-->

---
layout: monash-title-content
eyebrow: Workshop roadmap
---

# Today's Agenda

<v-clicks>

1. **Tableau Basics** - getting started with the interface
2. **Data Connection** - importing and preparing datasets
3. **Visual Encoding** - marks and channels
4. **Hands-on Exercise** - build your first worksheet

</v-clicks>

<!-- 
演讲者备注：
- 强调今天的实践导向
- 提醒带上笔记本电脑
- 说明每个环节的时间分配
-->

---
layout: monash-title-content
eyebrow: Key concept
---

# What Is Tableau?

Tableau is a powerful data visualisation tool that allows you to:

<v-clicks>

- **Connect** to various data sources
- **Explore** data through interactive visualisations
- **Create** dashboards and stories
- **Share** insights with others

</v-clicks>

<v-click>

<div class="monash-callout">
<strong>No coding required</strong> for basic visualisations, which makes it a strong first tool for studio exercises.
</div>

</v-click>

<!-- 
演讲者备注：
- 强调 Tableau 的易用性
- 对比 Excel 和编程工具
- 提到 Tableau Public 是免费的
-->

---
layout: monash-title-content
eyebrow: Data types
---

# Key Concepts

### Dimensions vs Measures

| Dimensions | Measures |
|-----------|----------|
| Categorical | Numerical |
| Discrete | Continuous |
| e.g., Country, Date | e.g., Sales, Temperature |

<!-- 
演讲者备注：
- 这是 Tableau 的核心概念
- 用实际例子说明区别
- 强调拖拽时的颜色区分（蓝 vs 绿）
-->

---
layout: monash-title-content
eyebrow: Visual grammar
---

# Visual Encoding

## Marks and Channels

<div class="grid grid-cols-2 gap-4">

<div>

### Marks
The visual elements:
- Points
- Bars  
- Lines
- Areas

</div>

<div>

### Channels
How data maps to visuals:
- Position
- Color
- Size
- Shape

</div>

</div>

<!-- 
演讲者备注：
- 参考 Cleveland & McGill 的研究
- 解释为什么位置编码最有效
- 展示不同编码的示例
-->

---
layout: monash-title-content
eyebrow: Best practices
---

# Design Principles

<v-clicks>

1. **Start with questions** - What do you want to know?
2. **Choose appropriate charts** - Match data to visualisation type
3. **Simplify** - Remove unnecessary elements (chart junk)
4. **Highlight insights** - Use color strategically

</v-clicks>

<v-click>

> "Above all else, show the data." - Edward Tufte

</v-click>

<!-- 
演讲者备注：
- 引用 Tufte 的设计原则
- 展示好 vs 坏的图表对比
- 强调数据墨水比 (data-ink ratio)
-->

---
layout: monash-title-content
eyebrow: Hands-on
---

# Exercise: Create Your First Visualization

## Dataset: Sample Superstore

<v-clicks>

**Goals:**
1. Connect to the data source
2. Create a bar chart of sales by category
3. Add a filter for region
4. Format and publish to Tableau Public

</v-clicks>

<v-click>

<div class="monash-tip">
💡 Tip: Drag 'Category' to Columns, 'Sales' to Rows
</div>

</v-click>

<!-- 
演讲者备注：
- 给学生 15-20 分钟完成
- 巡视提供帮助
- 鼓励互相讨论
-->

---
layout: monash-title-content
eyebrow: Resources
---

# Learn More

## Official Resources

- **Tableau Public**: https://public.tableau.com
- **Documentation**: https://help.tableau.com
- **Community**: https://community.tableau.com

## Recommended Reading

- *The Visual Display of Quantitative Information* - Edward Tufte
- *Storytelling with Data* - Cole Nussbaumer Knaflic

<!-- 
演讲者备注：
- 推荐学生注册 Tableau Public 账号
- 建议关注 Tableau 社区的优秀作品
- 提醒下周的预习内容
-->

---
layout: monash-end
speaker: Songhai (Frank) Fan
contact: songhai.fan@monash.edu
---

# Questions?

<!-- 
演讲者备注：
- 开放提问时间
- 收集学生的困惑点
- 预告下周内容：Advanced Visual Encoding
-->
