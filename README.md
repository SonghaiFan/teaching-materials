# Teaching Slides Repository

This repository contains teaching slide decks for both Monash University courses and external tutoring (Lincoin).

## Folder Structure

```
teaching/
├── courses/
│   ├── lincoin/          # External tutoring slides (课外辅导)
│   │   └── slides/
│   │       ├── fit5178/  # Example: FIT5178 - Software Design
│   │       ├── fit5196/  # Example: FIT5196 - Data Wrangling
│   │       └── ...       # Add new courses as needed
│   │
│   └── monash/           # Monash University internal tutor slides (校内tutor)
│       └── slides/
│           ├── fit2179/  # Example: FIT2179 - Data Visualisation
│           ├── fit5196/  # Example: FIT5196 - Data Visualisation
│           └── ...       # Add new courses as needed
│
└── README.md             # This file
```

## Two Different Contexts

### 1. Lincoin (External Tutoring / 课外辅导)
- **Purpose**: Personal tutoring outside of Monash
- **Language**: **中文 (Chinese)**
- **Location**: `courses/lincoin/slides/<course-code>/`
- **Style**: Custom Lincoin branding
- **Focus**: 补充课内未覆盖的内容，强化编程基础

### 2. Monash (Internal Tutor / 校内tutor)
- **Purpose**: Official Monash University tutoring
- **Language**: **English**
- **Location**: `courses/monash/slides/<course-code>/`
- **Style**: Monash University branding
- **Focus**: 跟随课程进度，解答课内问题

## Teaching Philosophy: 课内课外互补

### 核心原则
**课内课外是互补关系，不是重复。**

| 方面 | 课内 (Monash) | 课外 (Lincoin) |
|------|---------------|----------------|
| **内容** | 课程大纲内容、理论讲解 | 补充内容、编程强化 |
| **Python** | 默认学生已掌握，不教授 | **重点强化 Python 基础** |
| **语言** | English | 中文 |
| **节奏** | 跟随学校进度 | 根据学生需求调整 |
| **作业** | 解答课内作业问题 | 额外练习、代码实践 |

## Language Guidelines

| Context | Language | Rationale |
|---------|----------|-----------|
| **Lincoin** | 中文 | Students are Chinese-speaking; easier to explain complex concepts |
| **Monash** | English | Official university requirement; prepares students for assessments |

> ⚠️ **Important**: Always use the correct language for each context to maintain consistency and meet student expectations.

## How to Add a New Course

### For Monash Courses:

1. Create a new folder under `courses/monash/slides/`:
   ```bash
   mkdir courses/monash/slides/fitxxxx
   ```

2. Copy the template files from an existing Monash course (e.g., `fit2179` or `fit5196`):
   ```bash
   cp -r courses/monash/slides/fit2179/* courses/monash/slides/fitxxxx/
   ```

3. Update the following files:
   - `package.json` - Change name to `fitxxxx-slides`
   - `slides.md` - Update title and content **in English**
   - `slidev.config.ts` - Update base path to `/fitxxxx-slides/`
   - `README.md` - Update course-specific information

4. Install dependencies and start:
   ```bash
   cd courses/monash/slides/fitxxxx
   npm install
   npm run dev
   ```

### For Lincoin Courses:

1. Create a new folder under `courses/lincoin/slides/`:
   ```bash
   mkdir courses/lincoin/slides/fitxxxx
   ```

2. Copy the template files from an existing Lincoin course.

3. Update the following files:
   - `package.json` - Change name to `fitxxxx-slides`
   - `slides.md` - Update title and content **in Chinese (中文)**
   - `slidev.config.ts` - Update base path
   - `README.md` - Update course-specific information

4. **Design slides with complementary content in mind:**
   - 回顾课内核心概念（简要）
   - **重点补充编程基础**
   - 提供额外代码练习
   - 避免重复课内行政信息

## Template Reference

Each course folder contains a `slides.md` file that serves as the template for that specific course. Refer to the `slides.md` in each folder to see the available layouts and styling options for that particular course.

## Common Commands

```bash
# Development
npm run dev -- <path-to-file>    # Start dev server with specific file

# Export
npm run build -- <file>          # Build for production
npm run export -- <file>         # Export to PDF
npm run export-per -- <file>     # Export per-slide PDFs
```

## Notes

- Each course folder is self-contained with its own `node_modules`
- The `slides.md` file in each course folder is the main template for that course
- **Lincoin slides should be in Chinese (中文)**
- **Monash slides should be in English**
- **Lincoin focuses on programming fundamentals that Monash assumes students already know**
- Shared assets can be copied between projects as needed
