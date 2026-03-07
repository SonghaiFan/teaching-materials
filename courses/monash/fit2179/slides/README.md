# FIT2179 - Data Visualisation

## Slidev 课件项目

### 项目结构

```
slides/
├── slides.md              # 主入口文件（当前作为 AI-friendly template）
├── package.json           # Slidev 依赖
├── public/                # 静态资源
│   ├── images/
│   ├── datasets/
│   └── icons/
├── styles/                # 当前启用的全局样式
│   ├── index.css
│   └── monash-theme.css
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

当前模板推荐 **built-in layouts first**：

- 优先使用 Slidev 内建 layout，例如 `cover`、`default`、`two-cols`、`image-right`、`section`、`statement`、`end`、`none`
- 页面层面的微调优先放在 markdown 里，用 `class:`、局部 `<style>`、HTML 和 utility classes 完成
- 只有当一个页面壳会在很多 deck 里重复出现时，才考虑新增自定义 layout

样式入口在 `styles/index.css`，主题定义在 `styles/monash-theme.css`。

当前主题已经收敛为 **AI-friendly** 的薄样式层：

- 全局只定义字体、logo、cover image、背景和基础排版
- AI 可以在具体 slide 中自由使用 Markdown、HTML 和 Tailwind/UnoCSS utility classes
- 具体美术风格尽量写在 markdown 文档里，用局部 HTML 和 utility classes 完成
- 除非一个视觉模式会在多个 deck 重复出现，否则不要继续往全局样式里加 helper class

示例：

```md
---
layout: default
class: compact-slide
---

# FIT2179 Studio Week 3

<div class="max-w-[85%]">
  Your content here.
</div>

<style>
.compact-slide table {
  font-size: 0.92rem;
}
</style>

---
layout: image-right
image: /images/pptx/image2.jpg
---

# Introduction

Use a built-in image layout, then style locally.
```

### 模板使用建议

- 默认先选 built-in layout，不要先写新的 `.vue` layout
- 默认内容页优先用 Markdown + HTML + utility classes 自由排版
- 用 `class:` 和局部 `<style>` 做单页微调，例如表格密度、两栏间距、局部字号
- 全局样式负责品牌一致性，不负责替代具体页面设计
- 美术风格建议直接写在 deck 文档里，例如避免圆角、限制颜色、鼓励扁平化版式等

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
3. 从 `slides.md` 复制或扩展新 deck
4. 导出 PDF：`npm run export`
