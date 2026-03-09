# Monash Slides

Monash teaching slides use one Slidev project root per institution, with all course decks stored at the root level alongside the template deck.

## Directory Structure

```text
slides/
├── slides.md              # template / guide entry
├── fit2179-week1.md       # course deck
├── fit2179-week2.md       # course deck
├── fit3179-week1.md       # course deck
├── package.json           # Slidev dependencies and scripts
├── public/                # Monash shared static assets
│   └── images/
├── styles/                # Monash shared style layer
│   ├── index.css
│   └── monash-theme.css
├── components/            # optional shared Vue components
├── layouts/               # optional shared custom layouts
└── exports/               # generated output, not committed
```

## Structure Rules

- `slides.md` is the Monash template and guide entry.
- Real teaching decks live at the project root, for example `fit2179-week1.md`.
- Course code should be part of the filename so decks stay easy to scan and sort.
- Institution-level branding lives in `styles/`, `public/`, `components/`, and `layouts/`.
- Shared images should stay in `public/` so every deck can reference the same assets.
- Use built-in layouts first: `cover`, `default`, `two-cols`, `image-right`, `section`, `statement`, `end`, `none`.

## Development

```bash
cd /Users/songhaifan/.openclaw/workspace/teaching/courses/monash/slides

# install once
npm install

# open the template / guide
npm run dev

# open a specific course deck
npm run dev -- fit2179-week1.md
```

## Authoring Guidance

- Prefer Markdown plus small HTML blocks over large custom layout systems.
- Use local `<style>` only for slide-specific density or spacing fixes.
- Keep Monash brand decisions in `styles/`, not inside individual course decks.
- Use consistent deck filenames, for example `fit2179-week1.md` or `fit3179-studio1.md`.

## When To Add Shared Files

- Add to `public/` when multiple Monash courses reuse the same asset.
- Add to `components/` when multiple decks reuse the same interactive block.
- Add to `layouts/` only when a page shell repeats across many decks.
- Add to `styles/` only for institution-wide brand or typography rules.

## Git Notes

Do not commit:

- `node_modules/`
- `exports/`
- `.slidev/`
- `dist/`
