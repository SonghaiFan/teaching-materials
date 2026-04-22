---
theme: default
title: Data Visualisation Studio 7
layout: cover
info: |
  ## FIT2179 Week 7
  Data Visualisation 2 introduction, topic approval, sketching, and Vega-Lite start
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT2179 Data Visualisation Week 7

Data Visualisation 2, topic discussion, sketching, and a light Vega-Lite start

Songhai Fan · Monash University

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Session plan</p>

# Today's agenda

| Time | Focus |
|---|---|
| 10 to 15 min | Introduce `Data Visualisation 2` |
| 10 to 15 min | Light `Vega-Lite` and HTML embedding intro |
| Majority of studio | Topic discussion, approval guidance, and sketching |

> This studio is project-driven. Use the time to make real progress on `DV2`.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Studio focus</p>

# Week 7 goals

1. Understand what `DV2` requires.
2. Confirm a viable topic direction with your tutor.
3. Start sketching your visualisation in studio.
4. Leave with a clear next step for data, design, and implementation.

---
layout: section
---

# Data Visualisation 2

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Assignment overview</p>

# What changes in DV2?

- you will build the project as a public web page on `GitHub`
- you must use `Vega-Lite` for maps and diagrams
- you must include at least `one geographic map`
- the domain must be clearly different from `DV1`

<div class="mt-5 border border-slate-300 bg-white/60 p-4 text-sm">
DV2 is similar in spirit to DV1, but the technical expectations are higher.
</div>

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Higher expectations</p>

# Because AI lowers the baseline

- more visualisations
- more complexity
- more interactivity
- stronger layout and storytelling

::right::

# What that means

- do not stop at a few standard charts
- combine idioms thoughtfully
- use interactivity where it helps
- aim for a polished, coherent web page

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Non-negotiables</p>

# Minimum requirements to remember

- due `Friday, 29 May 2026, 11:55 PM`
- at least `10` charts
- at least `one` map
- data from `two different sources`
- public GitHub page and readable Vega-Lite JSON files
- topic must be different from your `DV1` domain

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Design brief</p>

# DV2 is still presentation first

- tell a story, not just show charts
- design for an average Australian or Malaysian audience
- use layout, typography, colour, and annotations deliberately
- avoid building an expert exploration dashboard

---
layout: section
---

# Topic Discussion

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Tutor discussion</p>

# What happens in topic approval

During studio, talk to your tutor about:

- whether the topic is appropriate
- whether the data direction is realistic
- whether the scope is manageable
- whether you can proceed

> This is guidance, not a formal recorded approval step.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Topic check</p>

# A good DV2 topic should be

- clearly different from your `DV1` domain
- relevant to Australia or Malaysia unless approved otherwise
- personally meaningful to you
- understandable to a general audience
- feasible with public data and `Vega-Lite`

---
layout: fact
---

# If you do more now, you do less later

Use studio time for:

- topic refinement
- sketching
- early design thinking
- identifying data needs early

---
layout: section
---

# Sketching

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Start now</p>

# Begin sketching in studio

- use paper, not digital tools
- sketch sections, charts, map ideas, annotations, and layout
- start rough, then improve it with tutor feedback

<div class="mt-5 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
The sketch is not graded today, but it will be submitted later for `DV2`.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">What to sketch</p>

# Your sketch should show

1. the overall story structure
2. where the map will appear
3. the main charts or sections
4. notes about interaction or annotations
5. rough text or headings

---
layout: section
---

# Vega-Lite Start

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Teaching strategy</p>

# Light-touch technical intro

- we will not over-teach technical content today
- the goal is to get you moving on the project
- `Vega-Lite` matters more than a long JavaScript introduction
- if you already know JavaScript, move ahead faster

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Mental model</p>

# The basic Vega-Lite idea

- `data` = where the values come from
- `mark` = the basic visual form, such as `bar`, `line`, or `point`
- `encoding` = how fields map to channels like `x`, `y`, `color`, or `size`
- `transform` = how values are changed, grouped, or aggregated

<div class="mt-5 border border-slate-300 bg-white/60 p-4 text-sm">
Most of your early work is choosing the right mark and the right encodings.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Official workflow</p>

# A simple learning path

1. start with `data`
2. choose a `mark`
3. add `encoding`
4. apply aggregation or other transforms if needed
5. customise labels or titles
6. embed the chart in HTML

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Minimum setup</p>

# Basic Vega-Lite embedding

```html
<div id="vis"></div>

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
<script type="module" src="main.js"></script>
```

> Your first goal is simple: make one Vega-Lite chart appear on a web page.

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">The data</p>

# Inline data as `values`

```js
const data = [
  { a: "C", b: 2 },
  { a: "C", b: 7 },
  { a: "C", b: 4 },
  { a: "D", b: 1 },
  { a: "D", b: 2 },
  { a: "D", b: 6 },
  { a: "E", b: 8 },
  { a: "E", b: 4 },
  { a: "E", b: 7 }
]
```
::right::

```js
const vlSpec = {
  data: {
    values: data
  },
}
```

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Marks and encodings</p>

# Start with raw points

```js
const vlSpec = {
  data: { values: data },
  mark: "point",
  encoding: {
    x: { field: "a", type: "nominal" },
    y: { field: "b", type: "quantitative" }
  }
}
```

- `a` is categorical, so use `nominal`
- `b` is numeric, so use `quantitative`
- Vega-Lite will add axes automatically

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Aggregation</p>

# Then aggregate if needed

```js
const vlSpec = {
  data: { values: data },
  mark: "bar",
  encoding: {
    y: { field: "a", type: "nominal" },
    x: {
      aggregate: "average",
      field: "b",
      type: "quantitative",
      title: "Mean of b"
    }
  }
}
```

This is a useful pattern:

- start with raw data
- then decide whether you need an aggregate such as `average`
- then choose a mark that fits the task

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Embed step</p>

# Render it in the page

```js
vegaEmbed("#vis", vlSpec)
```

- build the first simple chart
- then replace inline data with your real dataset
- then add layout, annotations, interaction, and a map

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Good next step</p>

# Start simple, then grow

1. make one chart render
2. load real data
3. refine the idiom and encoding
4. add more charts and one map
5. build the full story page

---
layout: default
zoom: 0.82
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Live demo</p>

# Edit The Spec, See The Chart

<VegaLitePlayground
  title="Starter Vega-Lite demo"
  :height="300"
  :initial-spec="{
    $schema: 'https://vega.github.io/schema/vega-lite/v6.json',
    data: {
      values: [
        { a: 'C', b: 2 },
        { a: 'C', b: 7 },
        { a: 'C', b: 4 },
        { a: 'D', b: 1 },
        { a: 'D', b: 2 },
        { a: 'D', b: 6 },
        { a: 'E', b: 8 },
        { a: 'E', b: 4 },
        { a: 'E', b: 7 },
      ],
    },
    mark: 'bar',
    encoding: {
      y: { field: 'a', type: 'nominal' },
      x: {
        aggregate: 'average',
        field: 'b',
        type: 'quantitative',
        title: 'Mean of b',
      },
    },
  }"
/>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Timeline</p>

# What happens after today

- `Week 7`: topic discussion and sketching
- by end of `Week 8`: find relevant public data
- `Weeks 9 to 11`: build the web page, maps, charts, layout, and interaction
- due `29 May 2026`: submit URLs and short written description

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Before you leave</p>

# By the end of this studio

- have a topic direction
- start a paper sketch
- know what data you need next
- understand that `DV2` must include `maps` and `Vega-Lite`
- use tutor feedback to reduce rework later
