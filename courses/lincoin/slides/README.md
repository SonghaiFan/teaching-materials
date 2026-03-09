# Lincoin Slides

Lincoin slides follow the same pattern as other institutions in this repo: one Slidev project root per institution, and multiple course decks inside it.

## Directory Structure

```text
slides/
├── slides.md              # template / default entry
├── package.json
├── public/                # Lincoin shared static assets
├── styles/                # Lincoin shared styles
├── fit5196/               # course decks
│   ├── week1.md
│   ├── week2.md
│   └── images/
└── exports/
```

## Structure Rules

- `slides.md` is the institution template or default entry, not the main location for all course content.
- Real decks live in course folders such as `fit5196/week1.md`.
- Shared institution branding belongs in `public/` and `styles/`.
- Course-local figures should stay inside the course folder, for example `fit5196/images/`.

## Development

```bash
cd /Users/songhaifan/.openclaw/workspace/teaching/courses/lincoin/slides

# install once
npm install

# open the template / default entry
npm run dev

# open a specific course deck
npm run dev -- fit5196/week1.md
```

## Authoring Guidance

- Prefer built-in Slidev layouts first.
- Keep the institution style in shared files under `styles/`.
- Keep course-only screenshots and diagrams in the course directory.
- If multiple Lincoin courses reuse the same asset, then move it to `public/`.
