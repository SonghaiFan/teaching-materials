---
theme: apple-basic
title: FIT5196 - Data Wrangling
---


# FIT5196 Data Wrangling

Lincoin tutoring slides

---

# 设计原则

本模板设计目标：

- **简洁** - 减少视觉干扰，专注内容
- **灵活** - 易于调整和扩展
- **一致** - 保持整体风格统一

---
layout: default
---

# 布局选择指南

| 场景 | 推荐布局 | 用途 |
|------|----------|------|
| 开场/结束 | `cover`, `end` | 课程开始和结束 |
| 内容讲解 | `default` | 大多数教学页面 |
| 图文并排 | `two-cols` | 对比或图文混排 |
| 章节分隔 | `section` | 标记新阶段 |
| 强调要点 | `statement` | 单一重要信息 |
| 数据展示 | `default` + 表格 | 结构化数据 |

---
layout: two-cols
---

# 目录示例

::right::

<div class="card">
  <Toc maxDepth="1" />
</div>

---
layout: section
---

# 章节分隔页

使用 `section` 布局标记新的学习阶段

---
layout: default
---

# 标准内容页

默认布局适用于大多数教学场景。

- 解释概念
- 列出要点
- 总结关键信息

## 二级标题

使用 `##` 创建二级标题，自动使用克莱因蓝。

---
layout: two-cols
---

# 对比布局

左侧内容：
- 要点 A
- 要点 B
- 要点 C

::right::

右侧内容：
- 对比项 1
- 对比项 2
- 对比项 3

---
layout: default
---

# 表格示例

紧凑表格样式：

| 项目 | 说明 | 权重 |
|------|------|------|
| 任务一 | 基础练习 | 20% |
| 任务二 | 综合应用 | 30% |
| 任务三 | 项目作业 | 50% |

---
layout: default
---

# 代码示例

行内代码：`print("Hello")`

代码块：
```python
def hello(name):
    return f"Hello, {name}!"

hello("World")
```

---
layout: statement
---

这是一个 `statement` 布局页面

用于强调单一重要信息

---
layout: fact
---

# 60%

数据科学家 60% 的时间用于数据清洗和整理

---
layout: quote
---

"简洁是复杂的终极形式。"

—— 达芬奇

---
layout: default
---

# 实用技巧

**Markdown 基础：**

```markdown
# 一级标题
## 二级标题

- 无序列表
- 无序列表

1. 有序列表
2. 有序列表

[链接文字](https://example.com)
```

---
layout: two-cols
---

# 好的实践

- 使用内置布局
- 保持内容简洁
- 多用留白
- 统一风格

::right::

# 避免的做法

- 过度装饰
- 复杂自定义
- 密集排版
-  inconsistent 样式

---
layout: end
---

# 模板就绪

开始创建你的课件吧
