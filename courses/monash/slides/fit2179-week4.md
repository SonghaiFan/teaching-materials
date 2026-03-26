---
theme: default
title: FIT2179 Week 4 Studio
layout: cover
---

# FIT2179 Data Visualisation Week 4

Tableau with multiple data sources, dual-axis charts, and the first step into HTML + GitHub

Songhai Fan · Monash University

---
layout: default
---

# Today's agenda

| Time | Focus |
|---|---|
| 20 min | Forum Posting 3 discussion |
| 35 min | Tableau guided practice |
| 25 min | VS Code, HTML, and GitHub basics |
| Remaining | Practice, proposal approvals, questions |

> Keep your laptop open with Tableau, VS Code, and your browser ready.

---
layout: default
---

# Week 4 Studio Goals

1. Build a dual-axis chart in Tableau without misleading the reader.
2. Learn when to `join` data and when to `blend` data.
3. Create a basic `index.html`, upload it to GitHub, and publish it with GitHub Pages.

| Part | What we will do | What you should leave with |
|---|---|---|
| Part A  | Compare `average` and `maximum` pedestrian counts; combine multiple datasets safely | Build a dual-axis chart and synchronise axes; understand join types, multi-key joins, and blending |
| Part B | Start building for the web | Use VS Code, write HTML, upload to GitHub, and publish online |

---
layout: section
---

# Forum Posting 3

Use feedback to improve Assignment 1, not just to answer the weekly task.

---
layout: fact
---

# In studio today

The forum post has already been submitted.

Today, we will look at a few examples together and discuss:

- what is not working in the visualisation
- why the design may be misleading or ineffective
- how the chart could be improved

---
layout: default
---

# How to critique a post

When we look at a selected forum example, try to answer:

1. What is the chart trying to show?
2. What is making it hard to read or trust?
3. Is the problem chartjunk, poor data-ink ratio, lying design, or a mix of these?
4. What is one realistic improvement you would make first?

---
layout: default
---

# What to look for in poor visualisations

- truncated axes or distorted scales
- too many colours, shapes, or decorative effects
- labels or legends that are hard to follow
- chart types that do not fit the task
- clutter that adds ink but not insight

---
layout: fact
---

# Discussion prompts

As we review each post, be ready to explain:

1. whether the chart is actually lying, or just poorly designed
2. how to improve the data-ink ratio
3. what chartjunk could be removed
4. whether the chart type supports the intended story

---
layout: default
---

# How to suggest improvements

Try to make your feedback practical:

- simplify the encoding
- choose a better chart type
- fix the axis or scale
- remove unnecessary decoration
- label the important takeaway more clearly

---
layout: fact
---

# Goal of the discussion

The point is not to say "this chart is bad".

The point is to practise turning critique into redesign ideas that you can apply to your own `Data Visualisation 1`.

---
layout: section
---

# Tableau Part A

Dual axis, joining, and blending

---
layout: default
---

# Tableau Learning Goals

- Create a dual-axis chart from the pedestrian dataset
- Recognise when a dual axis becomes misleading
- Distinguish `join` vs `blend`
- Notice when a join key is incomplete and duplicates rows

---
layout: default
---

# Activity: Dual-Axis Chart

In this activity, you will:

1. Create a bar chart of `AVG(Hourly Counts)` by `Day`
2. Add `MAX(Hourly Counts)` as a second measure
3. Change the maximum series to a line
4. Convert the view to `Dual Axis`
5. Fix the chart by using `Synchronise Axis`

> The key lesson is not just how to make a composite chart, but how to make sure it is honest.

---
layout: two-cols
---

# Why dual axis is attractive

- Lets us compare two measures in one frame
- Reduces duplicated axes and repeated labels
- Can support the `least ink` principle when used carefully

## In this activity

- Bar: `AVG(Hourly Counts)`
- Line: `MAX(Hourly Counts)`

::right::

# Why dual axis is risky

- Different scales can distort the relationship
- Maximum may appear lower than average
- Readers may compare position before reading labels

## Rule

- If measures share the same unit, synchronise the axes

---
layout: default
---

# Second Tableau Exercise

Next, recreate the same idea by `Hour` instead of `Day`.

- Derive `Hour` from `Date Time`
- Compare `AVG` vs `MAX` hourly counts
- Replace extra colour with direct labels
- Prefer `line-end labels` over a heavy legend when possible

> This is a small but important design move: less ink, same information.

---
layout: section
---

# Tableau Part B

Multiple data sources

---
layout: default
---

# Joining vs Blending

Today we will use two different workflows:

| Technique | What Tableau does | Best for |
|---|---|---|
| `Join` | Combines tables into one data source | When rows should be matched before analysis |
| `Blend` | Links sources on the fly inside a sheet | When sources stay separate but related |

> The important question is not “can Tableau connect these files?” but “what relationship am I assuming between rows?”

---
layout: default
---

# Join Types Refresher

| Join type | Keeps which rows? | Risk to watch |
|---|---|---|
| Inner | Only matches in both tables | Missing unmatched records |
| Left | All rows from the left table | Nulls on the right |
| Right | All rows from the right table | Nulls on the left |
| Full Outer | All rows from both tables | Many blanks and harder interpretation |

---
layout: fact
---

# The Most Important Join Lesson

In the `camera_store_sales` example, joining only on `trans_id` created repeated rows and inflated totals.

Why?

- `STORE1` and `STORE2` can share the same transaction id
- A single key was not enough to identify the record correctly

**Fix:** join on both `trans_id` and `store`.

---
layout: default
---

# Blending Activity

Using the pedestrian datasets, you will:

1. Import `Pedestrian_volume__updated_monthly_.csv`
2. Add `Pedestrian_sensor_locations.csv` as a second data source
3. Choose the main source by placing its field in the view first
4. Activate the correct link, especially `Sensor ID`
5. Build a bar chart of pedestrian counts by `Year Installed`

> Tableau blends at the sheet level, so the first field you use matters.

---
layout: statement
---

If Tableau cannot figure out how two sources relate, check:

- which source is currently the `main` source
- which linking field is active
- whether the matching field names actually represent the same thing

---
layout: section
---

# Part B Lab

VS Code, HTML, and GitHub

---
layout: default
---

# Why this matters

This lab is the bridge into `Data Vis 2`.

- `VS Code` gives you a place to write and preview files
- `HTML` gives your page structure
- `Bootstrap` helps you create a responsive layout faster
- `GitHub` stores and publishes your work

By the end of this part, you should have a basic webpage online.

---
layout: default
---

# HTML Essentials

This is the minimum structure every page needs:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My first webpage</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>This is my first HTML page.</p>
  </body>
</html>
```

- `head` holds metadata and page title
- `body` holds visible content
- Save the file as `index.html`

---
layout: default
---

# Add Bootstrap CSS

To use Bootstrap, place this line inside the `head` of your page:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
```

- Bootstrap gives you ready-made layout classes
- It is useful for building a clean page structure quickly

---
layout: default
---

# Bootstrap Grid Basics

Bootstrap layout usually follows this pattern:

```html
<div class="container">
  <div class="row g-3">
    <div class="col-lg-8">Main content</div>
    <div class="col-lg-4">Sidebar</div>
  </div>
</div>
```

- `container` keeps the page aligned
- `row` creates a horizontal layout
- `col-*` controls how much width each section gets

---
layout: fact
---

# How to use the grid docs

Bootstrap grid reference:

`https://getbootstrap.com/docs/5.3/layout/grid/`

When you read the docs, focus on:

1. the 12-column system
2. breakpoint classes like `col-md-*` and `col-lg-*`
3. gutters using `g-*`
4. how content stacks on smaller screens

---
layout: default
---

# Core HTML elements introduced

| Element | Purpose |
|---|---|
| `h1` to `h6` | Headings and structure |
| `p` | Paragraph text |
| `table`, `tr`, `th`, `td` | Tables |
| `img` | Images with a `src` path |
| `a` | Hyperlinks using `href` |
| `div` and `section` | Grouping content into sections |
| `ul` and `li` | Bullet lists |

> HTML gives structure first. Styling and interactivity come later with CSS and JavaScript.

---
layout: two-cols
---

# Split your files

For this week, we will keep the project in separate files:

- `index.html` for structure
- `style.css` for styling
- `main.js` for page-level JavaScript
- `barchart.js` for the Vega-Lite chart

::right::

# Why split them?

- easier to read
- easier to debug
- easier to reuse code
- closer to how you will build your assignments

---
layout: default
---

# Minimum Vega-Lite project structure

```text
project-folder/
  index.html
  style.css
  main.js
  barchart.js
```

- `index.html` links the CSS and JS files
- `main.js` calls the chart function
- `barchart.js` stores the chart spec

---
layout: default
---

# What the demo page includes

Our simple Bootstrap demo page now shows:

1. text with headings and paragraphs
2. a `section` with a title
3. an `img` element
4. a `ul` list
5. a simple `table`
6. one Vega-Lite bar chart

---
layout: default
---

# VS Code setup

- Install Visual Studio Code
- Add `Live Server`
- Add `Vega Preview`
- Add `Vega Viewer`

## Why these tools?

- Faster edit-preview loop
- Better syntax highlighting
- Easier debugging for web work

::right::

# First workflow to remember

1. Create a project folder
2. Open the folder in VS Code
3. Create `index.html`
4. Add `style.css`, `main.js`, and `barchart.js`
5. Use `html:5` shortcut
6. Link Bootstrap CSS and your own `style.css`
7. Build the layout with `container`, `row`, and `col-*`
8. Add text, image, list, and table elements
9. Render the chart with JavaScript
10. Save often and preview with Live Server

---
layout: default
---

# Demo for today

We will open the Bootstrap example in:

`materials/fit2179/week4/Web layout for data visualisation (bootstrap)/index.html`

What to notice:

- how the grid separates summary cards, main content, and side content
- how HTML, CSS, and JS are split into separate files
- how the page stays simple for a first web visualisation
- how charts are added into a normal `div`

---
layout: default
---

# GitHub Workflow

1. Create a public repository
2. Upload your `index.html`
3. Write a meaningful commit message
4. Update the file either locally or directly on GitHub
5. Turn on `GitHub Pages`
6. Publish from the `main` branch

> If `index.html` is not at the base of the published path, the site may not display as expected.

---
layout: fact
---

# By the end of studio

By the end of studio, you should be able to say:

1. I know how to build and fix a dual-axis chart.
2. I know why a wrong join key can break an analysis.
3. I know the difference between joining and blending.
4. I can create and publish a simple HTML page with GitHub Pages.

---
layout: default
---

# Proposal Check and Practice Time

If you still need proposal approval today, please have these ready:

- topic and intended audience
- rough story or message
- likely data sources
- one sketch or example inspiration
- any question you want feedback on

---
layout: default
---

# Reminders

## This week

- Forum Posting 4
- We will review selected examples in class
- Due Sunday `11:55 PM`

## Studio focus

- Ask questions while building
- It is normal for Tableau joins and GitHub Pages to feel unfamiliar at first
