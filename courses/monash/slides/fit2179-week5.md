---
theme: default
title: Data Visualisation Studio 5
layout: cover
info: |
  ## FIT2179 Week 5
  Test 1 logistics, critique preparation, and introduction to CSS
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT2179 Data Visualisation Week 5

Test 1, critique preparation, and introduction to CSS

Songhai Fan · Monash University

---
layout: default
---

# Today's agenda

| Time | Focus |
|---|---|
| 15 min | Test 1 |
| 5 to 10 min | Data Visualisation 1 critique briefing |
| 40 min | Introduction to CSS |
| Remaining | Practice, peer help, consultation, and questions |

> Please have your laptop ready for the studio activities, but note that `Test 1` is pen and paper only.

---
layout: default
---

# Week 5 Studio Goals

1. Understand the `Test 1` format and logistics clearly.
2. Understand exactly how the `Data Visualisation 1 Critique` works in Week 6.
3. Learn the role of `CSS` in turning a plain HTML page into a designed visualisation page.
4. Leave with a clear plan for `Test 1`, critique preparation, and next steps on `Vis 1`.

---
layout: section
---

# Test 1

Week 5 studio includes the first in-class test.

---
layout: two-cols
---

# Test 1 logistics

- conducted during the `Week 5` workshop session
- `pen and paper` only
- `no laptops` allowed
- students complete the test in batches
- time allowed: `15 minutes`

::right::

<div class="border border-slate-300 bg-white/60 p-4 text-sm">
  <p><strong>Preparation</strong></p>
  <ul class="mt-3">
    <li>listen carefully for your batch instructions</li>
    <li>bring only what is permitted</li>
    <li>manage time tightly during the test</li>
  </ul>
</div>

<div class="mt-5 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
The test is short by design, so accuracy and clarity matter more than writing a lot.
</div>

---
layout: default
---

# Test 1 sample

The sample test asks you to inspect a visualisation and answer short analysis questions such as:

1. identify the `idiom`
2. note the major issue or issues, if any
3. explain how to fix the issue or issues
4. identify attributes, attribute types, marks, and channels used

> Revise the What-Why-How framework, common chart problems, and marks/channels from Weeks `1` to `4`.

---
layout: section
---

# Data Visualisation 1 Critique

Next week, you will give and receive structured feedback in studio.

---
layout: default
---

# Why this critique matters

The purpose of this assessment is:

- to receive feedback from both peers and tutor
- to practise giving constructive, design-focused feedback
- to improve your `Data Visualisation 1` before final submission

This task is worth `3%` of the overall mark and must be completed during studio hours because it depends on paired critique, tutor feedback, and discussion.

---
layout: statement
---

To participate, you must have a draft of `Data Visualisation 1` publicly available on `Tableau Public`.

- the draft must show multiple charts and real design decisions
- peers need enough content to critique layout, typography, colour, and chart design
- if the draft only contains a few simple charts, a penalty of up to `2%` may apply

---
layout: default
---

# Critique procedure

1. Publish your draft on `Tableau Public`.
2. Post the public URL on the group forum on Moodle.
3. In studio, work in pairs and exchange visualisations.
4. Prepare your critique in `10 minutes` using the assignment rubric.
5. Reply to your partner with at least `four` bullet points, ranked from most important to least important.
6. Present a `two-minute` critique to the studio group.
7. Take part in `three minutes` of discussion with tutor and peers.

---
layout: two-cols
---

# What to focus on in your critique

- chart idioms and whether they fit the task
- choice of data and whether comparisons are meaningful
- colour, typography, spacing, and layout
- clarity of the message and visual hierarchy
- any misleading or weak design decisions

::right::

# What not to do

- do not list tiny cosmetic issues first
- do not spend all four points on the same problem
- do not give vague comments like "make it nicer"
- do not ignore major design flaws

---
layout: default
---

# Marking rubric

| Component | Weight | What it requires |
|---|---|---|
| Presentation | `1%` | Well-structured, clear, and on time. Exceeding time receives `0%` for this part. |
| Critique and Suggestions | `2%` | At least four valid, substantial suggestions for improvement, prioritised by importance. |

## Important marking logic

- each substantial suggestion is worth `0.5%`
- a penalty of `0.5%` applies for each major issue not mentioned
- major missed issues include misleading encodings or unsuitable use of data

---
layout: fact
---

# A simple recipe for strong critique

For each bullet point:

1. identify the problem
2. explain why it matters
3. suggest a practical improvement

> Think like a designer helping a teammate, not like a grader hunting for faults.


---
layout: section
---

# Introduction to CSS

Last week we built structure with HTML. This week we first recap what `CSS` is, then move to `CSS frameworks` such as `Bootstrap`.

---
layout: two-cols
---

# What CSS does

- controls colour, spacing, borders, and fonts
- helps create hierarchy and emphasis
- separates visual styling from HTML structure
- makes the page feel designed rather than raw

::right::

# A simple mental model

- `HTML` = structure and content
- `CSS` = appearance and layout
- `JavaScript` = behaviour and interactivity

---
layout: default
---

# First: CSS itself

Before talking about frameworks, remember:

- `CSS` is the language used to style web pages
- it controls how HTML elements look and are arranged
- you can write your own rules in files like `style.css`
- even when you use a framework, you are still relying on CSS

---
layout: two-cols
---

# Then: what is a CSS framework?

- a ready-made library of CSS rules
- gives you reusable classes for layout and styling
- helps you build pages faster
- keeps common patterns consistent

::right::

# In our class

- we use `Bootstrap`
- it provides classes like `container`, `row`, and `col-lg-6`
- it also styles elements like tables and spacing utilities such as `py-4` and `mb-0`

---
layout: default
---

# Learn from the Bootstrap example

We will continue from the example in last week.

That example already shows the workflow we want:

1. `Bootstrap` handles much of the layout
2. `style.css` adds your own visual decisions
3. `main.js` and `barchart.js` keep chart logic separate

---
layout: default
---

# Bootstrap first, custom CSS second

From the example page:

```html
<div class="container py-4">
  <div class="row">
    <div class="col-lg-8">
      <section class="box">...</section>
    </div>
    <div class="col-lg-4">
      <section class="box">...</section>
    </div>
  </div>
</div>
```

- `container`, `row`, and `col-lg-*` come from `Bootstrap`
- `.box` is your own class from `style.css`
- good pages usually combine framework classes with a small amount of custom CSS

---
layout: two-cols
---

# What Bootstrap is doing

- centering the page with `container`
- creating columns with `row` and `col-lg-*`
- adding spacing with classes like `py-4` and `mb-0`
- styling the table with `table table-bordered`

::right::

# What your CSS is doing

- setting the page background
- creating the white content boxes
- adding border and padding
- making the image scale neatly

---
layout: default
---

# The custom CSS in the example

```css
body {
  background-color: #f8f9fa;
}

.box {
  background-color: white;
  border: 1px solid #dee2e6;
  padding: 1rem;
  margin-bottom: 1rem;
}
```

This is a good first pattern:

- let the framework solve common layout problems
- use your own CSS for identity, emphasis, and small refinements

---
layout: default
---

# Basic CSS syntax

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f8fafc;
  color: #1f2937;
}

h1 {
  color: #006dae;
}
```

- the selector chooses what to style
- each rule uses `property: value;`
- declarations sit inside `{ }`

---
layout: default
---

# Linking Bootstrap and your own stylesheet

Add these inside the `head` of `index.html`:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="style.css">
```

Why both?

- `Bootstrap` gives you a fast starting point
- `style.css` lets you make the page your own
- together they are easier to manage than putting styles everywhere in HTML

---
layout: two-cols
---

# CSS selectors you will use first

- `body`
- `h1`, `h2`, `p`
- `.card`
- `.chart-container`
- `#main-vis`

::right::

```css
p {
  line-height: 1.6;
}

.card {
  padding: 1rem;
  background: white;
}

#main-vis {
  margin-top: 2rem;
}
```

---
layout: default
---

# First styling priorities for your vis page

Start simple:

1. improve spacing
2. choose readable font sizes
3. create clear section hierarchy
4. use colour sparingly and consistently
5. give charts enough room to breathe

> Good CSS is not decoration first. It is clarity first.

---
layout: default
---

# CSS framework practice ideas for today

- use `Bootstrap` grid classes to improve page layout
- add or adjust spacing with utility classes
- style the page background and text colours in `style.css`
- wrap text or charts in simple panels such as `.box`
- make the page feel more intentional without adding clutter

---
layout: fact
---

# Reminders

- prepare your `Tableau Public` draft before the Week 6 critique
- post your visualisation URL on the forum
- use consultation hours if you are stuck
- revise for `Test 1`
- keep improving `Vis 1`, not just the technical setup
