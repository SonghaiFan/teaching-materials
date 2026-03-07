---
theme: default
title: FIT5196 - Data Wrangling
layout: cover
info: |
  ## FIT5196 Slide Template
  Lincoin tutoring style - clean and rounded
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

<style>
@import './styles/lincoin-theme.css';
</style>

# FIT5196 Data Wrangling

Lincoin tutoring slides

---

# 设计原则

本模板设计目标是：

- **简洁通用** - 覆盖大多数教学场景
- **灵活可扩展** - 易于针对特定页面调整
- **视觉一致** - 保持整体风格统一

<div class="mt-6 card">
    <p>规则：如果某个视觉决定只适用于一个课件，请将其保留在 markdown 或本地 HTML 中，而不是推送到全局 CSS。</p>
</div>

---
layout: default
---

# 布局选择指南

| 场景 | 推荐布局 | 本地调整 |
|------|----------|----------|
| 开场或结束 | `cover`, `end` | 添加副标题间距 |
| 讲解内容 | `default`, `center` | 使用卡片包裹内容 |
| 图文并排 | `image-right`, `image-left` | 调整图片比例 |
| 对比展示 | `two-cols` | 调整列间距 |
| 章节分隔 | `section`, `statement` | 添加简短说明 |
| 引用强调 | `quote`, `fact` | 调整字体大小 |

---
layout: two-cols
---

# 目录示例

::right::

<div class="card text-sm">
  <Toc maxDepth="1" listClass="text-sm leading-snug" />
</div>

---
layout: section
---

# 章节分隔页

使用 section 布局标记新的学习阶段

---
layout: default
---

# 标准内容页

这是大多数教学幻灯片的默认模式。

- 解释一个概念
- 列出要点
- 添加关键总结

## 为什么有效

页面简洁、易读，易于使用 HTML 块或工具类扩展。

<div class="mt-6 card">
    <p>使用一个强标题、一个二级标题，然后少量要点或短段落。</p>
</div>

---
layout: two-cols
---

# 对比布局示例

当页面真正需要对比两个概念时，使用 `two-cols` 布局。

- 左侧：概念 A
- 右侧：概念 B
- 简单的插槽语法
- 无需自定义布局文件

::right::

<div class="card text-sm">
  <p class="tag mb-2">对比块</p>
  <p>此幻灯片仅使用内置布局加本地类进行紧凑间距调整。</p>
</div>

---
layout: default
---

# 表格示例

内置 `default` 布局适用于表格，只需本地调整紧凑样式。

| 项目 | 用途 | 权重 |
|------|------|------|
| 论坛发帖 | 批判练习 | 2% |
| 课堂任务 | 实践应用 | 3% |
| 项目作业 | 深度综合 | 25% |

## 实际应用场景

- 评估 breakdown
- 任务清单

---
layout: default
---

# 交互组件

<div class="grid grid-cols-2 gap-6 items-start">

<div>

  <VClicks>

  - 逐步揭示内容
  - 控制课堂节奏
n  - 减少密集幻灯片的杂乱

  </VClicks>

  <div class="mt-6 card text-sm">
    <VSwitch>
      <template #1>状态 1：引入概念</template>
      <template #2>状态 2：对比替代方案</template>
      <template #3>状态 3：得出结论</template>
    </VSwitch>
  </div>

</div>

<div class="card">
  <Transform :scale="0.82" origin="top left">
    <table>
      <thead>
        <tr>
          <th>组件</th>
          <th>用途</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>`Toc`</td>
          <td>议程和概览</td>
        </tr>
        <tr>
          <td>`VClicks`</td>
          <td>逐步揭示</td>
        </tr>
        <tr>
          <td>`VSwitch`</td>
          <td>展示状态</td>
        </tr>
        <tr>
          <td>`Transform`</td>
          <td>缩放内容</td>
        </tr>
      </tbody>
    </table>
  </Transform>
</div>

</div>

---
layout: statement
---

当内置布局已经是最快表达幻灯片的方式时，使用它们进行强调。

这是 `statement`：一个清晰的教学要点，最少的支持文本。

---
layout: fact
---

# 75%

教学课件中的布局问题大多是密度问题，而非样式问题。

---
layout: quote
---

"主题的重点是一致性，而非装饰。"

使用 `quote` 展示引用语、反思提示或你想让学生暂停思考的一句话。

---
layout: default
---

# 推荐的内置布局

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

## 推荐布局

- `default`
- `center`
- `two-cols`
- `statement`, `quote`, `fact`
- `image-left`, `image-right`

</div>

<div>

## 谨慎使用

- `iframe` 相关
- `Youtube`
- `Tweet`
- `SlidevVideo`

</div>

</div>

<div class="mt-6 card text-sm">
模板不会尝试重新样式化每个内置布局，只保持视觉基线足够简洁，使内置布局保持可用。
</div>

---
layout: two-cols
---

# AI 提示建议

在 markdown 中直接放入艺术指导。

好的指示：

- 避免大圆角
- 偏好细边框和平面块
- 保持配色克制
- 使用不对称和留白
- 让图表和截图功能化，而非装饰性
- 偏爱编辑式排版而非仪表板杂乱

::right::

不好的指示：

- 为每个页面发明新的全局辅助类
- 为每个变体添加新布局文件
- 将单个课程的风格选择编码到主题中

---
layout: end
---

# 模板就绪

内置布局优先，本地样式其次，新布局最后。
