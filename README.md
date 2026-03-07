# Teaching Slides Repository

This repository contains teaching slide decks for both Monash University courses and external tutoring (Lincoin).

## Folder Structure

```
teaching/
├── courses/
│   ├── lincoin/          # External tutoring slides (课外辅导)
│   │   └── slides/
│   │       ├── fit5178/  # Example: FIT5178 - Software Design
│   │       ├── fit5196/  # Example: FIT5196 - Data Visualisation
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

### 1. Lincoin (External Tutoring)
- **Purpose**: Personal tutoring outside of Monash
- **Location**: `courses/lincoin/slides/<course-code>/`

### 2. Monash (Internal Tutor)
- **Purpose**: Official Monash University tutoring
- **Location**: `courses/monash/slides/<course-code>/`

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
   - `slides.md` - Update title and content (this is your slide template)
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

## Template Reference

Each course folder contains a `slides.md` file that serves as the template for that specific course. Refer to the `slides.md` in each folder to see the available layouts and styling options for that particular course.

## Common Commands

```bash
# Development
npm run dev          # Start dev server

# Export
npm run build        # Build for production
npm run export       # Export to PDF
npm run export-per   # Export per-slide PDFs
```

## Notes

- Each course folder is self-contained with its own `node_modules`
- The `slides.md` file in each course folder is the main template for that course
- Shared assets can be copied between projects as needed
