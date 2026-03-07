# Lincoin Slides

Lincoin tutoring slides using Slidev.

## Structure

```
slides/
├── fit5196/              # FIT5196 Data Visualisation
│   ├── week1.md          # Week 1: Introduction
│   ├── week2.md          # Week 2: Data Types and Encodings
│   └── ...               # Add more weeks as needed
├── fit5178/              # Other courses
│   └── week1.md
└── ...
```

## How to View Slides

Each `.md` file is a complete slide deck. To view:

```bash
# Navigate to slides folder
cd /Users/songhaifan/.openclaw/workspace/teaching/courses/lincoin/slides

# Install dependencies (first time only)
npm install

# Start dev server with specific file
npm run dev -- week1.md

# Or for a specific course week
npm run dev -- fit5196/week1.md
```

## Creating New Weeks

1. Create a new `.md` file in the course folder
2. Copy the frontmatter from an existing week
3. Write your slides using Slidev syntax
4. Run `npm run dev -- <path-to-file>`

## Slidev Commands

```bash
npm run dev -- <file>      # Start dev server
npm run build -- <file>    # Build for production
npm run export -- <file>   # Export to PDF
```
