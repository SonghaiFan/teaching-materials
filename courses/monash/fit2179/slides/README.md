# FIT2179 - Data Visualisation

## Slidev 课件项目

### 项目结构

```
slides/
├── slides.md              # 主入口文件（导入所有周）
├── package.json           # Slidev 依赖
├── components/            # 可复用组件
│   ├── CodeBlock.vue
│   ├── DataVizExample.vue
│   └── WeekHeader.vue
├── layouts/               # 自定义布局
│   ├── week-intro.vue
│   └── exercise.vue
├── public/                # 静态资源
│   ├── images/
│   ├── datasets/
│   └── icons/
├── styles/                # 自定义样式
│   └── custom.css
├── weeks/                 # 每周课件
│   ├── week01-intro.md
│   ├── week02-data-types.md
│   ├── week03-tableau-basics.md
│   ├── week04-visual-encoding.md
│   ├── week05-interaction.md
│   ├── week06-color-design.md
│   ├── week07-narrative.md
│   ├── week08-evaluation.md
│   ├── week09-advanced-tableau.md
│   ├── week10-d3-intro.md
│   ├── week11-d3-advanced.md
│   └── week12-wrapup.md
└── exports/               # 导出 PDF（不提交 Git）
```

### 开发命令

```bash
# 进入项目目录
cd slides

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 导出 PDF
npm run export

# 构建静态站点
npm run build
```

### Monash Slidev 模版

当前项目已经补了一组可复用的 Monash 风格 layout，放在 [layouts](./layouts)：

- `monash-cover`：黑底封面，右侧 Monash 风格装饰栏
- `monash-section`：章节切换页
- `monash-default`：标准内容页
- `monash-split`：左文右图或左图右文
- `monash-end`：收尾 / Q&A 页面
- `monash-bottom-graphic`：带底部图形条的内容页
- `monash-vertical`：右侧竖排标题页

为了和 `week3_pptx` 的 PowerPoint 母版对齐，也补了更贴近原始母版名的 Slidev layout 别名：

- `title-slide-6` -> `Title Slide 6`
- `title-content-side-pic` -> `Title and Content Side pic`
- `title-content` -> `Title and Content`
- `title-content-bottom-graphic` -> `Title and Content bottom graphic`
- `vertical-title-text` -> `Vertical Title and Text`
- `section-header` -> `Section Header`
- `thank-you` -> `Thank You`

样式入口在 `styles/index.css`，主题定义在 `styles/monash-theme.css`，示例文件在 `week03-pptx-style.md`。

示例：

```md
---
layout: title-slide-6
subtitle: Data Visualisation Fundamentals and Tableau Introduction
date: 09/08/2023
presenter: Songhai (Frank) Fan
---

# FIT2179 Studio Week 3

---
layout: title-content-side-pic
eyebrow: Speaker introduction
image: /images/pptx/image2.jpg
imageAlt: Songhai (Frank) Fan
---

# Introduction

Your content here.
```

### 每周课件规范

- 文件名：`week{NN}-{topic}.md`
- 每节课 8-15 张 slides
- 包含：学习目标、核心内容、实践练习、总结

### 当前状态

| 周次 | 主题 | 文件 | 状态 |
|-----|------|------|------|
| 1 | Introduction to Data Visualisation | week01-intro.md | ✅ 已创建 |
| 2 | Data Types & Structures | week02-data-types.md | 📝 待创建 |
| 3 | Tableau Basics | week03-tableau-basics.md | ✅ 已有 |
| 4-12 | ... | ... | 📝 待创建 |

---

## Git 忽略规则

以下内容不提交 Git：
- `node_modules/` - 依赖（通过 npm install 恢复）
- `exports/` - 导出的 PDF（按需生成）
- `.slidev/` - 缓存
- `dist/` - 构建输出

---

## 快速开始

1. 安装依赖：`npm install`
2. 启动开发：`npm run dev`
3. 编辑 `weeks/weekXX-xxx.md` 文件
4. 导出 PDF：`npm run export`
