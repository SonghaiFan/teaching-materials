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
